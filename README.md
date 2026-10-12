# Pytor and PyQuest

Two ways to learn Python and AI engineering, sharing one tutor and one repo.

## 📱 Download PyQuest for Android

### **[⬇ Download the PyQuest APK](https://github.com/Matswm86/pylearn/releases/download/latest/pyquest-d26e0d5.apk)**

Open that link on your Android phone, then open the downloaded file and allow
installs from your browser when Android asks. Needs Android 8.0 or newer. The link
always points at the newest build. Older builds: [all releases](https://github.com/Matswm86/pylearn/releases).

No Android phone? Open in the browser: [pytor.mwmai.no](https://pytor.mwmai.no/).
No install, no account.

| | What it is | Where |
|---|---|---|
| **Pytor** | The **site**. Real Python typed in a browser, run in the browser, graded instantly. | [pytor.mwmai.no](https://pytor.mwmai.no/) |
| **PyQuest** | The **app**. An Android game you tap through on a phone, no typing. | [pyquest/](pyquest/) · [download APK](https://github.com/Matswm86/pylearn/releases/download/latest/pyquest-d26e0d5.apk) |

Pytor is also the name of the snake who tutors you in both. On the site he is a
beginner's guide; in the app he is an expert. Same character, different register.

<p align="center">
  <img src="docs/pytor.webp" alt="Pytor, the Python snake tutor" width="180">
</p>

---

## What it does

- Teaches Python from variables to FastAPI and API calling with 450 graded exercises
  that run in your browser, with nothing to install.
- Opens every topic with a plain-English lesson, with analogies and runnable examples.
- Gives you Pytor, a snake tutor you can ask for hints, answers and generated lessons.
- Lets you play 654 questions in 10 tiers on an Android phone, tapping instead of
  typing, from `print("hello")` to scoping an AI-engineering consultancy job.
- Drills for the AI-901 and AI-103 exams, on the site and in the app.

## How it works

The site is static HTML and vanilla JavaScript with hash routing. Python runs in your
browser through Pyodide (CPython on WebAssembly) with a CodeMirror editor, and progress
sits in LocalStorage, so no server does the work and no account is needed. The
exercises are written as Python in `pylearn/` and `build.py` turns them into the
browser-runnable `docs/exercises.json`. Pytor's chat goes through a small stdlib-only
Python bridge that asks a Groq-hosted model first and falls back to a local Ollama
model. PyQuest is a Kotlin and Jetpack Compose app driven by question data in JSON
files, with no Python interpreter inside; GitHub Actions builds its APK.

---

## Pytor, the site

**450 exercises. Zero setup. Runs in your browser.** No account, no install, no server
doing the work: Python itself is compiled to WebAssembly and executes on your machine.

### The nine topics

| # | Topic | Exercises | What you learn |
|---|---|:---:|---|
| 1 | Variables | 50 | Storing data, naming, assignment, f-strings, scope |
| 2 | Data Types | 50 | int, float, str, bool, conversion, string methods |
| 3 | Conditionals | 50 | if/elif/else, boolean logic, ternary, match/case |
| 4 | Loops | 50 | for, while, range, break/continue, nesting, enumerate |
| 5 | Functions | 50 | def, arguments, return, *args/**kwargs, closures, decorators |
| 6 | Lists & Sets | 50 | Indexing, slicing, comprehensions, sorting, set operations |
| 7 | Dictionaries | 50 | Key-value pairs, nesting, comprehensions, Counter, grouping |
| 8 | FastAPI | 50 | Pydantic models, validation, CRUD APIs, auth, middleware |
| 9 | API Calling | 50 | JSON, HTTP headers, auth, pagination, rate limiting, webhooks |

Each topic opens with a lesson in plain English, with analogies, runnable examples and
the mistakes people actually make, then 50 exercises that climb from Beginner to
Challenge.

### The rest of the site

| Route | What it is |
|---|---|
| `#/playground` | A full browser Python IDE. No exercise, no grading, just run code |
| `#/path` | The AI Engineer Path: a study route through the topics, each paired with a video worth watching, plus the AI-901 to AI-103 certification track |
| `#/checklist` | A 100-item AI engineering skills checklist you tick off as you go |
| `#/exam` | A 117-question AI-901 drill in real exam format |
| `#/exam/103` | A 222-question AI-103 drill for the Azure AI Apps and Agents Developer exam: Foundry deployments, agents, retrieval and AI Search, vision, speech, document extraction and content safety, with case studies and matching and ordering items |
| `#/questions` | 30 questions on embeddings and retrieval, the part of AI engineering that is hardest to learn from a tutorial |
| `/blocks/` | Python Block Bench: 84 drag-and-drop syntax puzzles, no keyboard needed, with a line-by-line step-through that shows every variable change |

### ELI5 mode

On by default. Variables are labelled jars, functions are recipes, lists are shopping
lists, dictionaries are phone books, APIs are restaurant waiters. Toggle it off in the
top-right when the analogies stop helping.

### Pytor, the tutor in the corner

Click the snake (or the **🐍 Pytor** button) to open a chat sidebar:

- **Ask anything** about Python. He answers Socratically, steering you to the answer
  rather than handing it over.
- **Get a hint** on the exercise you are stuck on. He reads the code you have actually
  written and points at the next thing to try.
- **Generate a lesson** on any topic. Type "decorators" or "asyncio" and he builds an
  interactive lesson on the spot.

Under the hood: a Groq-hosted model first, a local Ollama model as the fallback, behind a
small stdlib-only Python bridge at `pytor.mwmai.no/api/tutor`. The model names can be
overridden through environment variables (`GROQ_MODEL`, `OLLAMA_MODEL`) because hosted
model catalogues change. The frontend is vanilla JS and degrades to a no-op if the bridge
is unreachable, so the exercises never depend on the tutor being up.

---

## PyQuest, the app

An Android game that walks from `print("hello")` to scoping and pricing an AI-engineering
consultancy job, plus two tiers of exam prep, AI-901 and AI-103: **654 questions across
10 tiers**, multiple-choice cards and Scratch-style drag blocks, Leitner spaced repetition,
weak-tag tracking, XP and streaks. Pytor rides along as an expert, with a 105-entry offline
reference and an online chat mode.

It has no Python interpreter on purpose. Typing Python on a phone keyboard is miserable,
and the site already does that properly. Full detail in [pyquest/README.md](pyquest/README.md).

---

## Status

Pytor is live at [pytor.mwmai.no](https://pytor.mwmai.no/). PyQuest is at 0.3.0, a
debug-signed build you sideload from the download link above; it does not grade typed
Python, which stays on the site.

---

## Repo layout

```
docs/                Pytor, the site (served by GitHub Pages and by pytor.mwmai.no)
  index.html         shell and SPA router
  app.js             routing, Pyodide integration, exercise flow
  lessons.js         lesson content for all nine topics
  exercises.json     450 exercises, generated from the Python source
  path.js  checklist.js  exam.js  exam103.js  questions.js  playground.js  tutor.js
  blocks/            Python Block Bench
pylearn/             Python source of truth for the exercises, with auto-grading
build.py             regenerates docs/exercises.json from pylearn/
build_exam103.py     regenerates docs/exam103.js from PyQuest's tier_10.json
tests/               runs every Block Bench solution and its step-through
mcp-servers/         the Pytor tutor bridge (Groq primary, Ollama fallback)
pyquest/             PyQuest, the Android app (Kotlin + Compose)
.github/workflows/   the Android build, which only fires on changes under pyquest/
                     or to its own workflow file
```

## Working on it

```bash
# the site
cd docs && python -m http.server 8000     # then open http://localhost:8000

# regenerate exercise data after editing pylearn/exercises/*.py
python build.py

# regenerate the AI-103 drill after editing pyquest tier_10.json
python build_exam103.py

# the app
cd pyquest && ./gradlew testDebugUnitTest
```

Exercises are defined in `pylearn/exercises/*.py` as `make_exercise()` calls carrying a
description, hints, a solution and a test mechanism. `build.py` turns those into
web-runnable assertions. Never hand-edit `docs/exercises.json`.

APKs are never built on a workstation: Gradle needs more memory than the dev box has, so
GitHub Actions is the only place an APK is produced.

## Tech

[Pyodide](https://pyodide.org/) (CPython on WebAssembly), [CodeMirror 5](https://codemirror.net/5/),
vanilla JS with hash routing, LocalStorage for progress. Kotlin and Jetpack Compose on the
app side.

## Contributing

New exercises, clearer descriptions and extra topics are all welcome. Exercise data lives
in `pylearn/exercises/`; question data lives in `pyquest/app/src/main/assets/curriculum/`
and is validated by a gate that runs before CI will build anything.

## Licence

MIT, see [LICENSE](LICENSE). The fonts bundled with the site (Atkinson Hyperlegible Next and JetBrains Mono) and in PyQuest (Archivo and JetBrains Mono) are under the SIL Open Font License; their texts are in `docs/fonts/` and `pyquest/licenses/`.

The AI-103 drill (site), PyQuest tier 10 and ten of Pytor's Codex notes draw on two third-party sources: an MIT-licensed open-source practice exam, and study notes used with their author's permission, which is not an open-source licence. Credits, terms and the licence text are in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
