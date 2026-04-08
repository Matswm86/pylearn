# PyLearn - Learn Python Interactively

**400 hands-on exercises. Zero setup. Runs in your browser.**

[**Start Learning**](https://matswm86.github.io/pylearn/)

---

## What is this?

PyLearn is a free, interactive app that teaches Python programming from absolute zero. No installation, no accounts — open the link and start coding.

- Works on **phones, tablets, and desktops**
- Python runs **directly in your browser** (via [Pyodide](https://pyodide.org/))
- **Instant feedback** — write code, click Run, see if you got it right
- **Progress tracking** — streaks and completion stats saved locally

## Topics (400 exercises)

| # | Topic | Exercises | What you'll learn |
|---|-------|:---------:|-------------------|
| 1 | **Variables** | 50 | Storing data, naming, assignment, f-strings, scope |
| 2 | **Data Types** | 50 | int, float, str, bool, type conversion, string methods |
| 3 | **Conditionals** | 50 | if/elif/else, boolean logic, ternary, match/case |
| 4 | **Functions** | 50 | def, arguments, return, *args/**kwargs, closures, decorators |
| 5 | **Lists & Sets** | 50 | Indexing, slicing, comprehensions, sorting, set operations |
| 6 | **Dictionaries** | 50 | Key-value pairs, nesting, comprehensions, Counter, grouping |
| 7 | **FastAPI** | 50 | Pydantic models, validation, CRUD APIs, auth, middleware |
| 8 | **API Calling** | 50 | JSON, HTTP headers, auth, pagination, rate limiting, webhooks |

Each topic has a **lesson** with plain-English explanations, analogies, runnable examples, and common mistakes — plus **50 progressive exercises** from Beginner to Challenge.

## ELI5 Mode

The **Explain Like I'm 5** mode is on by default. It adds simplified explanations using everyday analogies:

- Variables = labeled jars
- Functions = recipes
- Lists = shopping lists
- Dictionaries = phone books
- APIs = restaurant waiters

Toggle it with the **ELI5** button in the top-right corner.

## How it works

1. **Pick a topic** — start with Variables if you're brand new
2. **Read the lesson** — concepts explained with analogies and live examples
3. **Do the exercises** — write Python in the built-in editor
4. **Click Run & Check** — your code runs in-browser and gets auto-graded
5. **Use hints** if stuck — each exercise has progressive hints
6. **Check the solution** — learn from the answer when needed

## For developers

### Project structure

```
pylearn/
├── docs/                # Static site (GitHub Pages)
│   ├── index.html       # Main page
│   ├── style.css        # Responsive styles
│   ├── app.js           # SPA logic + Pyodide integration
│   ├── lessons.js       # Lesson content for all 8 topics
│   └── exercises.json   # 400 exercises (generated)
├── pylearn/             # Python source
│   └── exercises/       # Exercise definitions with auto-grading
├── build.py             # Generates exercises.json from Python source
└── pyproject.toml
```

### Rebuilding exercise data

The Python source in `pylearn/exercises/` is the source of truth. Each exercise has test mechanisms (check lambdas, function test cases, or expected output). The build script converts these to web-compatible assertion strings:

```bash
python build.py    # Regenerates docs/exercises.json
```

### Running locally

```bash
cd docs && python -m http.server 8000
# Open http://localhost:8000
```

### Tech stack

- **[Pyodide](https://pyodide.org/)** — CPython compiled to WebAssembly, runs Python in the browser
- **[CodeMirror 5](https://codemirror.net/5/)** — Code editor with Python syntax highlighting
- **Vanilla JS** — No framework, hash-based SPA routing
- **LocalStorage** — Progress persistence, no backend needed

## Contributing

Exercise data lives in `pylearn/exercises/*.py`. Each exercise is a `make_exercise()` call with description, hints, solution, and test mechanism. PRs welcome for new exercises, better descriptions, or additional topics.

## License

MIT
