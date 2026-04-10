#!/usr/bin/env python3
"""PyLearn AI Tutor — Groq-primary, Ollama-fallback HTTP bridge.

Stdlib-only HTTP server. Deployed under `/opt/tutor/` (or equivalent
per-host path) and fronted by Caddy as
`https://pytor.mwmai.no/api/tutor/*` (Caddy uses `handle_path` to strip
the `/api/tutor` prefix, so this backend only sees the short routes
`/health`, `/chat`, `/hint`, `/design-lesson`, `/generate-page`).

Backend selection mirrors the oso-sync responder:
  - Groq (llama-3.3-70b-versatile) — primary, ~1s per request on free tier
  - Ollama (llama3.1:8b on 127.0.0.1:11434) — fallback for rate-limit / outage

CLOUDFLARE UA TRAP: api.groq.com is fronted by Cloudflare, which returns
HTTP 403 error:1010 for the default `Python-urllib/3.x` User-Agent. We
set an explicit UA to avoid it — copy/do NOT drop. See
memory/feedback/feedback_groq_cloudflare_ua.md.
"""
from __future__ import annotations

import json
import logging
import os
import socketserver
import sys
import threading
import time
from collections import deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

HOST = os.environ.get("TUTOR_HOST", "127.0.0.1")
PORT = int(os.environ.get("TUTOR_PORT", "8100"))

SCRIPT_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = Path(os.environ.get("PROMPTS_DIR", str(SCRIPT_DIR / "prompts")))
EXERCISES_PATH = Path(
    os.environ.get(
        "PYLEARN_EXERCISES_PATH",
        str(SCRIPT_DIR.parent.parent / "docs" / "exercises.json"),
    )
)

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434/v1/chat/completions")
OLLAMA_MODEL = os.environ.get("OLLAMA_MODEL", "llama3.1:8b")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = os.environ.get("GROQ_MODEL", "llama-3.3-70b-versatile")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "").strip()

GROQ_TIMEOUT = 30
OLLAMA_TIMEOUT = 120

# CORS: same-origin requests from pytor.mwmai.no need no CORS header, but
# the GitHub Pages mirror (matswm86.github.io/pylearn) needs explicit allow.
CORS_ALLOWED_ORIGINS = {
    "https://pytor.mwmai.no",
    "https://matswm86.github.io",
    "http://localhost:3000",
    "http://localhost:5500",
    "http://localhost:8080",
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8080",
}

logging.basicConfig(
    level=os.environ.get("LOG_LEVEL", "INFO"),
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    stream=sys.stderr,
)
log = logging.getLogger("pytor-tutor")

# ---------------------------------------------------------------------------
# Caches
# ---------------------------------------------------------------------------

_prompts_cache: dict[str, str] = {}
_exercises_cache: dict[str, dict] | None = None
_cache_lock = threading.Lock()

# ---------------------------------------------------------------------------
# Rate limiting (sliding window, per-IP, per-route)
# ---------------------------------------------------------------------------
# Stops a bad actor from burning Groq credits by spamming /chat. Routes not
# listed are unlimited. Localhost bypasses the limit so internal health
# checks are not throttled.

RATE_LIMITS: dict[str, tuple[int, float]] = {
    "/chat": (10, 60.0),
    "/hint": (10, 60.0),
    "/design-lesson": (5, 60.0),
    "/generate-page": (5, 60.0),
    "/health": (60, 60.0),
}

_rate_buckets: dict[tuple[str, str], deque] = {}
_rate_lock = threading.Lock()


def rate_limit_check(client_ip: str, path: str) -> tuple[bool, int]:
    """Return (allowed, retry_after_seconds). retry_after is 0 when allowed."""
    if client_ip in ("127.0.0.1", "::1", ""):
        return True, 0
    limit_cfg = RATE_LIMITS.get(path)
    if limit_cfg is None:
        return True, 0
    max_requests, window = limit_cfg
    now = time.monotonic()
    cutoff = now - window
    key = (client_ip, path)
    with _rate_lock:
        bucket = _rate_buckets.get(key)
        if bucket is None:
            bucket = deque()
            _rate_buckets[key] = bucket
        while bucket and bucket[0] < cutoff:
            bucket.popleft()
        if len(bucket) >= max_requests:
            retry_after = max(1, int(bucket[0] + window - now) + 1)
            return False, retry_after
        bucket.append(now)
        return True, 0


def load_prompt(name: str) -> str:
    with _cache_lock:
        if name in _prompts_cache:
            return _prompts_cache[name]
        try:
            text = (PROMPTS_DIR / f"{name}.txt").read_text(encoding="utf-8").strip()
        except OSError as exc:
            log.error(f"prompt {name} load failed: {exc}")
            text = ""
        _prompts_cache[name] = text
        return text


def load_exercises() -> dict[str, dict]:
    global _exercises_cache
    with _cache_lock:
        if _exercises_cache is not None:
            return _exercises_cache
        flat: dict[str, dict] = {}
        try:
            data = json.loads(EXERCISES_PATH.read_text(encoding="utf-8"))
            for topic in data.get("topics", []):
                for ex in topic.get("exercises", []):
                    flat[ex["id"]] = ex
            log.info(f"loaded {len(flat)} exercises from {EXERCISES_PATH}")
        except (OSError, json.JSONDecodeError, KeyError) as exc:
            log.error(f"exercises load failed: {exc}")
        _exercises_cache = flat
        return flat


def search_exercises(keywords: list[str], limit: int = 3) -> list[dict]:
    exercises = load_exercises()
    keywords_lower = [kw.lower() for kw in keywords if kw]
    matched: list[dict] = []
    for ex in exercises.values():
        searchable = (
            f"{ex.get('title', '')} "
            f"{ex.get('description', '')} "
            f"{' '.join(ex.get('concepts', []))}"
        ).lower()
        if any(kw in searchable for kw in keywords_lower):
            matched.append(ex)
            if len(matched) >= limit:
                break
    return matched


# ---------------------------------------------------------------------------
# LLM calls
# ---------------------------------------------------------------------------


def _openai_chat(url: str, model: str, system: str, user: str,
                 max_tokens: int, temperature: float, timeout: int,
                 api_key: str | None) -> str | None:
    """Shared OpenAI-compatible chat call. Both Groq and Ollama speak this."""
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }
    headers = {
        "Content-Type": "application/json",
        # Cloudflare in front of api.groq.com bans Python-urllib/3.x UA
        # with HTTP 403 error:1010. Any non-default UA is accepted.
        "User-Agent": "pytor-tutor/1.0",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    req = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["choices"][0]["message"]["content"].strip() or None
    except HTTPError as exc:
        body = ""
        try:
            body = exc.read().decode("utf-8", errors="replace")[:300]
        except Exception:  # noqa: BLE001
            pass
        log.warning(f"{url} HTTP {exc.code}: {body}")
        return None
    except (URLError, TimeoutError, KeyError, IndexError,
            json.JSONDecodeError) as exc:
        log.warning(f"{url} failed: {type(exc).__name__}: {exc}")
        return None


def query_groq(system: str, user: str, *, max_tokens: int = 600,
               temperature: float = 0.7) -> str | None:
    if not GROQ_API_KEY:
        return None
    return _openai_chat(
        GROQ_URL, GROQ_MODEL, system, user,
        max_tokens=max_tokens, temperature=temperature,
        timeout=GROQ_TIMEOUT, api_key=GROQ_API_KEY,
    )


def query_ollama(system: str, user: str, *, max_tokens: int = 600,
                 temperature: float = 0.7) -> str | None:
    return _openai_chat(
        OLLAMA_URL, OLLAMA_MODEL, system, user,
        max_tokens=max_tokens, temperature=temperature,
        timeout=OLLAMA_TIMEOUT, api_key=None,
    )


def chat_llm(system: str, user: str, *, max_tokens: int = 600,
             temperature: float = 0.7) -> tuple[str | None, str]:
    """Returns (response, backend_name). Groq-primary, Ollama-fallback."""
    answer = query_groq(system, user, max_tokens=max_tokens, temperature=temperature)
    if answer is not None:
        return answer, "groq"
    if GROQ_API_KEY:
        log.info("groq failed, falling back to ollama")
    answer = query_ollama(system, user, max_tokens=max_tokens, temperature=temperature)
    return answer, "ollama" if answer else "none"


# ---------------------------------------------------------------------------
# Route handlers
# ---------------------------------------------------------------------------


def handle_health() -> tuple[int, dict]:
    exercises = load_exercises()
    groq_ok = bool(GROQ_API_KEY)
    ollama_ok = query_ollama(
        "You reply with a single word.",
        "Say 'ok'.",
        max_tokens=4,
        temperature=0.0,
    ) is not None if not groq_ok else None  # don't burn ollama if groq is primary
    return 200, {
        "status": "ok",
        "backend": "groq" if groq_ok else "ollama",
        "groq": groq_ok,
        "groq_model": GROQ_MODEL,
        "ollama_model": OLLAMA_MODEL,
        "ollama_reachable": ollama_ok,
        "exercises_loaded": len(exercises),
    }


def handle_chat(body: dict) -> tuple[int, dict]:
    question = (body.get("question") or "").strip()
    if not question:
        return 400, {"error": "missing question"}

    context = (body.get("context") or "").strip()
    history_raw = body.get("history") or ""

    chat_history_text = ""
    if history_raw:
        try:
            items = json.loads(history_raw) if isinstance(history_raw, str) else history_raw
            relevant = items[-4:] if len(items) > 4 else items
            chat_history_text = "\n".join(
                f"{(it.get('role') or 'user').title()}: {it.get('content', '')}"
                for it in relevant
            )
        except (json.JSONDecodeError, TypeError, AttributeError):
            pass

    relevant_exercises = search_exercises(question.split(), limit=3)
    exercises_text = ""
    if relevant_exercises:
        exercises_text = "\n\nRelevant PyLearn exercises:\n" + "\n".join(
            f"- {ex['id']}: {ex.get('title', '')} (Difficulty: {ex.get('difficulty', '?')})"
            for ex in relevant_exercises
        )

    system_prompt = load_prompt("tutor_chat")
    user_message = (
        f"Student's question: {question}\n\n"
        f"{f'Lesson context: {context}' if context else ''}\n\n"
        f"{chat_history_text}{exercises_text}\n\n"
        "Remember: You are Pytor the Python snake — warm, curious, slightly "
        "playful. Guide the student using Socratic questions. Keep response "
        "to 2-4 sentences. Reference PyLearn exercises when relevant."
    )

    answer, backend = chat_llm(system_prompt, user_message, max_tokens=512, temperature=0.7)
    if answer is None:
        return 502, {"response": None, "error": "both backends failed"}
    return 200, {"response": answer, "backend": backend}


def handle_hint(body: dict) -> tuple[int, dict]:
    exercise_id = (body.get("exercise_id") or "").strip()
    if not exercise_id:
        return 400, {"error": "missing exercise_id"}

    exercise = load_exercises().get(exercise_id)
    if not exercise:
        return 404, {"response": None, "error": f"exercise {exercise_id} not found"}

    attempt = (body.get("attempt") or "").strip()
    exercise_ctx = (
        f"Exercise: {exercise.get('title', 'Unknown')}\n"
        f"Description: {exercise.get('description', '')}\n"
        f"Concepts: {', '.join(exercise.get('concepts', []))}\n"
        f"Solution approach: {exercise.get('solution', 'See documentation')}\n"
    )
    if attempt:
        exercise_ctx += f"Student's attempt:\n{attempt}\n"

    system_prompt = load_prompt("exercise_hint")
    user_message = (
        f"{exercise_ctx}\n\n"
        "Provide a helpful hint that guides the student toward the solution "
        "without revealing the answer. "
        + (
            "Analyze what's correct in their attempt and what needs improvement."
            if attempt else
            "Give a general hint about the approach."
        )
    )

    answer, backend = chat_llm(system_prompt, user_message, max_tokens=512, temperature=0.6)
    if answer is None:
        return 502, {"response": None, "error": "both backends failed"}
    return 200, {"response": answer, "backend": backend}


def handle_design_lesson(body: dict) -> tuple[int, dict]:
    topic = (body.get("topic") or "").strip()
    if not topic:
        return 400, {"error": "missing topic"}

    system_prompt = load_prompt("design_lesson")
    user_message = f"Design a comprehensive lesson for: {topic}"

    answer, backend = chat_llm(system_prompt, user_message, max_tokens=1200, temperature=0.6)
    if answer is None:
        return 502, {"response": None, "error": "both backends failed"}

    # Try to parse as JSON; if it fails, return raw string so the frontend
    # can still render something.
    try:
        return 200, {"response": json.loads(answer), "backend": backend}
    except json.JSONDecodeError:
        return 200, {"response": answer, "backend": backend}


def handle_generate_page(body: dict) -> tuple[int, dict]:
    title = (body.get("title") or "").strip()
    summary = (body.get("summary") or "").strip()
    difficulty = (body.get("difficulty") or "intermediate").strip()
    if not title or not summary:
        return 400, {"error": "missing title or summary"}

    system_prompt = load_prompt("generate_page")
    user_message = (
        "Create an interactive HTML learning page with these details:\n"
        f"- Title: {title}\n"
        f"- Summary: {summary}\n"
        f"- Difficulty: {difficulty}\n\n"
        "The page should include Python code examples, interactive elements, and a quiz."
    )

    answer, backend = chat_llm(system_prompt, user_message, max_tokens=4096, temperature=0.7)
    if answer is None or "<!doctype html" not in answer.lower() or "<html" not in answer.lower():
        answer = _fallback_html(title, summary, difficulty)
        backend = f"{backend}+fallback"
    return 200, {"response": answer, "backend": backend}


def _fallback_html(title: str, summary: str, difficulty: str) -> str:
    color = {
        "beginner": "#10B981",
        "intermediate": "#F59E0B",
        "advanced": "#EF4444",
    }.get(difficulty, "#4F46E5")
    return (
        "<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>"
        f"<title>{title} — Pytor</title>"
        "<style>body{font-family:system-ui,sans-serif;max-width:720px;margin:2rem auto;"
        "padding:2rem;line-height:1.6;color:#1f2937}"
        f"h1{{color:{color}}} .badge{{display:inline-block;background:{color};color:#fff;"
        "padding:.25rem .6rem;border-radius:.4rem;font-size:.8rem;text-transform:capitalize}"
        "pre{background:#1f2937;color:#e5e7eb;padding:1rem;border-radius:.5rem;overflow-x:auto}"
        "</style></head><body>"
        f"<h1>{title}</h1><span class='badge'>{difficulty}</span>"
        f"<p style='margin-top:1rem'>{summary}</p>"
        "<h2>Example</h2><pre># Pytor says hi\nprint('Hello from PyLearn!')</pre>"
        "<p><em>Pytor fell back to a simple template — the LLM output didn't "
        "come back as valid HTML. Try a more specific topic.</em></p>"
        "</body></html>"
    )


ROUTES = {
    ("GET", "/health"): lambda _body: handle_health(),
    ("POST", "/chat"): handle_chat,
    ("POST", "/hint"): handle_hint,
    ("POST", "/design-lesson"): handle_design_lesson,
    ("POST", "/generate-page"): handle_generate_page,
}


# ---------------------------------------------------------------------------
# HTTP server
# ---------------------------------------------------------------------------


class TutorHandler(BaseHTTPRequestHandler):
    server_version = "pytor-tutor/1.0"

    def log_message(self, format: str, *args) -> None:  # noqa: A002
        log.info("%s - %s", self.address_string(), format % args)

    def _client_ip(self) -> str:
        # Behind Caddy reverse_proxy: the real origin is in X-Forwarded-For.
        # The first entry of XFF is the original client, the rest are proxy
        # hops. Fall back to client_address[0] when no XFF is set (direct
        # localhost testing).
        xff = self.headers.get("X-Forwarded-For", "")
        if xff:
            return xff.split(",", 1)[0].strip()
        return self.client_address[0]

    def _cors_headers(self) -> None:
        origin = self.headers.get("Origin", "")
        if origin in CORS_ALLOWED_ORIGINS:
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.send_header("Access-Control-Max-Age", "86400")

    def _write_json(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self._cors_headers()
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self) -> None:  # noqa: N802
        self.send_response(204)
        self._cors_headers()
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802
        self._dispatch("GET")

    def do_POST(self) -> None:  # noqa: N802
        self._dispatch("POST")

    def _dispatch(self, method: str) -> None:
        path = self.path.split("?", 1)[0].rstrip("/") or "/"
        handler = ROUTES.get((method, path))
        if handler is None:
            self._write_json(404, {"error": f"no route for {method} {path}"})
            return

        client_ip = self._client_ip()
        allowed, retry_after = rate_limit_check(client_ip, path)
        if not allowed:
            log.warning(f"rate-limited {client_ip} on {path} (retry {retry_after}s)")
            body = json.dumps({
                "error": "rate limit exceeded",
                "retry_after": retry_after,
            }).encode("utf-8")
            self.send_response(429)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Retry-After", str(retry_after))
            self._cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        body: dict = {}
        if method == "POST":
            try:
                length = int(self.headers.get("Content-Length", "0") or "0")
                raw = self.rfile.read(length) if length > 0 else b""
                body = json.loads(raw.decode("utf-8")) if raw else {}
            except (ValueError, json.JSONDecodeError):
                self._write_json(400, {"error": "invalid JSON body"})
                return

        try:
            status, payload = handler(body)
        except Exception as exc:  # noqa: BLE001
            log.exception(f"handler {method} {path} crashed")
            self._write_json(500, {"error": f"{type(exc).__name__}: {exc}"})
            return

        self._write_json(status, payload)


class ThreadedServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True


def main() -> None:
    log.info(f"pytor-tutor starting on {HOST}:{PORT}")
    log.info(f"groq primary: {'yes' if GROQ_API_KEY else 'no (ollama only)'}")
    log.info(f"ollama fallback: {OLLAMA_URL} ({OLLAMA_MODEL})")
    log.info(f"prompts dir: {PROMPTS_DIR}")
    log.info(f"exercises: {EXERCISES_PATH}")
    # Pre-warm caches
    load_exercises()
    for name in ("tutor_chat", "exercise_hint", "design_lesson", "generate_page"):
        load_prompt(name)
    with ThreadedServer((HOST, PORT), TutorHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            log.info("shutting down")


if __name__ == "__main__":
    main()
