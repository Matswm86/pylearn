#!/usr/bin/env python3
"""Generate docs/examaiefs.js, the Pytor site's AI Engineering drill, from the
MIT-licensed ai-engineering-from-scratch quiz banks (phases 11 and 14).

Source: https://github.com/rohitg00/ai-engineering-from-scratch (MIT).
The 71 downloaded quiz.json files live in ~/MWM/scratch/aiefs/quizzes/;
re-run that download before this script if the upstream repo changed.

Every option list is reshuffled with a per-question seed (no positional
tells), questions are regrouped by lesson, and each item keeps the source
explanation. Credit: hero, per-section note, and THIRD_PARTY_NOTICES.md.

Usage:
    python3 build_aiefs.py [--src ~/MWM/scratch/aiefs/quizzes] [--out docs/examaiefs.js]
"""

from __future__ import annotations

import argparse
import json
import random
import re
from pathlib import Path

BASE_URL = "https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/"


def lesson_title(rel: str) -> tuple[str, str]:
    """'11-llm-engineering/01-prompt-engineering' -> ('11 · Prompt engineering', url)."""
    m = re.match(r"phases/(\d+)-([^/]+)/([^/]+)/quiz", rel)
    if not m:
        return (rel, BASE_URL + rel)
    phase, phase_slug, lesson_slug = m.group(1), m.group(2), m.group(3)
    lesson = lesson_slug.split("-", 1)[-1].replace("-", " ").title()
    phase_name = phase_slug.replace("-", " ").title()
    return (f"{phase} · {lesson} ({phase_name})", BASE_URL + rel)


def load_quizzes(src: Path) -> tuple[list[dict], int]:
    items = []
    skipped_blank = 0
    for f in sorted(src.glob("*.json")):
        rel = f.name.replace("__", "/").removesuffix(".json")
        data = json.loads(f.read_text(encoding="utf-8"))
        qs = data["questions"] if isinstance(data, dict) else data
        for q in qs:
            if not all(k in q for k in ("question", "options", "correct", "explanation")):
                raise SystemExit(f"{f}: unexpected item shape {sorted(q)}")
            if not isinstance(q["correct"], int):
                raise SystemExit(f"{f}: non-single correct {q['correct']!r}")
            explain = str(q["explanation"]).strip()
            if not explain:
                skipped_blank += 1  # the explanation is the product; skip items shipped blank
                continue
            items.append(
                {
                    "rel": rel,
                    "stage": q.get("stage", "check"),
                    "question": q["question"].strip(),
                    "options": [str(o).strip() for o in q["options"]],
                    "correct": int(q["correct"]),
                    "explain": q["explanation"].strip(),
                }
            )
    return items, skipped_blank


def shuffle_options(item: dict, seed: int) -> None:
    rng = random.Random(seed)
    order = list(range(len(item["options"])))
    rng.shuffle(order)
    item["options"] = [item["options"][i] for i in order]
    item["correct"] = order.index(item["correct"])


def build(src: Path) -> tuple[str, int, int]:
    items, skipped_blank = load_quizzes(src)
    groups: dict[str, list[dict]] = {}
    for i, item in enumerate(items):
        title, _url = lesson_title(item["rel"])
        groups.setdefault(title, []).append(item)
        shuffle_options(item, seed=90210 + i)

    refs: list[list[str]] = []
    sections: list[dict] = []
    n = 0
    for title, its in groups.items():
        refs.append([title, lesson_title(its[0]["rel"])[1]])
        ref_id = len(refs)
        sections.append(
            {
                "id": f"ai{len(sections) + 1}",
                "title": title,
                "weight": f"{len(its)} questions",
                "note": "Adapted from the MIT-licensed ai-engineering-from-scratch repository.",
                "questions": [],
            }
        )
        for item in its:
            n += 1
            sections[-1]["questions"].append(
                {
                    "n": n,
                    "q": item["question"],
                    "explain": item["explain"],
                    "ref": ref_id,
                    "type": "single",
                    "options": item["options"],
                    "correct": item["correct"],
                }
            )

    hero = f"""function renderExamAieHero() {{
    return `
    <div class="path-hero">
      <h2>🎓 AI Engineering drill: {n} questions</h2>
      <p>Prompting, RAG, fine-tuning, tools, MCP and agent engineering — the practice quizzes
      from the open-source <a class="hero-link" href="https://github.com/rohitg00/ai-engineering-from-scratch" target="_blank" rel="noopener">AI Engineering from Scratch</a>
      course (MIT), regrouped by lesson. Pair it with the <a class="hero-link" href="#/path">AI Engineer Path</a>.</p>
      <p class="path-note">Credit: every question is adapted from the MIT-licensed
      ai-engineering-from-scratch repository. We reshuffled the answer options and
      regrouped the items by lesson; the license text is in
      <a class="hero-link" href="https://github.com/Matswm86/pylearn/blob/main/THIRD_PARTY_NOTICES.md" target="_blank" rel="noopener">THIRD_PARTY_NOTICES.md</a>.</p>
    </div>
  `;
}}"""

    body = (
        "/* ===== AI Engineering drill: "
        + str(n)
        + """ questions =====
 *
 * GENERATED by build_aiefs.py at the repository root from the MIT-licensed
 * ai-engineering-from-scratch quiz banks; edit upstream or the generator,
 * never this file. Answers live in localStorage under pylearn_exam_aie.
 */

const EXAMAIEFS_REFS = """
        + json.dumps(refs, ensure_ascii=False, indent=2)
        + """;

const EXAMAIEFS_SECTIONS = """
        + json.dumps(sections, ensure_ascii=False, indent=2)
        + """;

"""
        + hero
        + """

EXAM_BANKS["aie"] = {
  key: "pylearn_exam_aie", prefix: "a", sections: EXAMAIEFS_SECTIONS, refs: EXAMAIEFS_REFS,
  name: "AI Eng", hero: renderExamAieHero,
};
"""
    )
    return body, n, skipped_blank


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--src", default=str(Path.home() / "MWM/scratch/aiefs/quizzes"))
    ap.add_argument("--out", default="docs/examaiefs.js")
    args = ap.parse_args()
    body, n, skipped = build(Path(args.src))
    Path(args.out).write_text(body, encoding="utf-8")
    print(f"wrote {args.out}: {n} questions ({skipped} upstream items skipped: blank explanation)")


if __name__ == "__main__":
    main()
