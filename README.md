# Pytor and PyQuest

Two ways to learn Python and AI engineering, sharing one tutor and one repo.

| | What it is | Where |
|---|---|---|
| **Pytor** | The **site**. Real Python typed in a browser, run in the browser, graded instantly. | [pytor.mwmai.no](https://pytor.mwmai.no/) |
| **PyQuest** | The **app**. An Android game you tap through on a phone, no typing. | [pyquest/](pyquest/) · [latest APK](https://github.com/Matswm86/pylearn/releases) |

Pytor is also the name of the snake who tutors you in both. On the site he is a
beginner's guide; in the app he is an expert. Same character, different register.

<p align="center">
  <img src="docs/pytor.webp" alt="Pytor, the Python snake tutor" width="180">
</p>

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
| `#/exam` | A 50-question AI-901 drill in real exam format |
| `#/questions` | 30 questions on embeddings and retrieval, the part of AI engineering that is hardest to learn from a tutorial |
| `/blocks/` | Python Block Bench: 44 drag-and-drop syntax puzzles, no keyboard needed |

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
small stdlib-only Python bridge at `pytor.mwmai.no/api/tutor`. The model names live in
environment variables, not in the code, because hosted model catalogues change. The
frontend is vanilla JS and degrades to a no-op if the bridge is unreachable, so the
exercises never depend on the tutor being up.

---

## PyQuest, the app

An Android game that walks from `print("hello")` to scoping and pricing an AI-engineering
consultancy job: **231 questions across 8 tiers**, multiple-choice cards and Scratch-style
drag blocks, Leitner spaced repetition, weak-tag tracking, XP and streaks. Pytor rides
along as an expert, with a 95-entry offline reference and an online chat mode.

It has no Python interpreter on purpose. Typing Python on a phone keyboard is miserable,
and the site already does that properly. Full detail in [pyquest/README.md](pyquest/README.md).

---

## Repo layout

```
docs/                Pytor, the site (served by GitHub Pages and by pytor.mwmai.no)
  index.html         shell and SPA router
  app.js             routing, Pyodide integration, exercise flow
  lessons.js         lesson content for all nine topics
  exercises.json     450 exercises, generated from the Python source
  path.js  checklist.js  exam.js  questions.js  playground.js  tutor.js
  blocks/            Python Block Bench
pylearn/             Python source of truth for the exercises, with auto-grading
build.py             regenerates docs/exercises.json from pylearn/
mcp-servers/         the Pytor tutor bridge (Groq primary, Ollama fallback)
solutions/  tests/
pyquest/             PyQuest, the Android app (Kotlin + Compose)
.github/workflows/   the Android build, which only fires on changes under pyquest/
```

## Working on it

```bash
# the site
cd docs && python -m http.server 8000     # then open http://localhost:8000

# regenerate exercise data after editing pylearn/exercises/*.py
python build.py

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

MIT.
