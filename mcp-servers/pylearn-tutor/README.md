# PyLearn Tutor - AI MCP Server

A Model Context Protocol (MCP) server providing intelligent Python tutoring capabilities for the PyLearn learning platform.

## Features

- **Lesson Design** (`design_lesson`) - Decompose any Python topic into 3-6 progressive knowledge points
- **Interactive Pages** (`generate_page`) - Auto-generate self-contained HTML learning pages with code examples, quizzes, and interactive elements
- **Socratic Tutoring** (`tutor_chat`) - Context-aware tutoring chat that guides students through discovery
- **Smart Hints** (`get_exercise_hint`) - Progressive hints that help without revealing answers

## Architecture

Built on:
- **FastMCP 2.14.6** - Fast, protocol-compliant MCP server
- **Ollama** - Local LLM inference (default: llama3.2:3b)
- **httpx** - Async HTTP client for Ollama API calls
- **Python 3.11+** - Modern async/await patterns

## Installation

```bash
pip install -e .
```

## Configuration

Environment variables (defaults shown):

```bash
OLLAMA_URL=http://localhost:11434          # Ollama server endpoint
OLLAMA_MODEL=llama3.2:3b                   # LLM model to use
PYLEARN_EXERCISES_PATH=../../../docs/exercises.json  # Path to exercises JSON
```

## Starting the Server

```bash
python server.py
```

The server starts on stdio and is ready to accept MCP requests.

## Tools Reference

### 1. `design_lesson(topic: str) -> str`

Decomposes a Python topic into structured knowledge points.

**Example:**
```
topic: "Python list comprehensions"
```

**Output:** JSON with knowledge_points array:
```json
{
  "knowledge_points": [
    {
      "title": "Basic Comprehension Syntax",
      "summary": "Learn the foundational syntax of list comprehensions",
      "difficulty": "beginner",
      "key_concepts": ["syntax", "basic iteration", "list creation"],
      "exercises": ["list_10", "list_11"]
    }
  ]
}
```

### 2. `generate_page(title: str, summary: str, difficulty: str) -> str`

Generates a complete, standalone HTML learning page.

**Example:**
```
title: "Variables and Data Types"
summary: "Understanding Python's fundamental data types and variable assignment"
difficulty: "beginner"
```

**Output:** Complete HTML5 document with:
- Modern, responsive design
- Python code examples
- Interactive quiz
- Collapsible sections
- No external dependencies

### 3. `tutor_chat(question: str, context: str = "", history: str = "") -> str`

Socratic tutoring through conversation.

**Example:**
```
question: "How do I loop through a list?"
context: "We're learning about for loops"
history: '[{"role": "user", "content": "What is a list?"}, {"role": "assistant", "content": "..."}]'
```

**Output:** Guiding response that helps students discover answers:
```
Great question! Before I give you the answer, can you think about what a list contains? What do you think 'looping' means - repeating something multiple times?
```

### 4. `get_exercise_hint(exercise_id: str, attempt: str = "") -> str`

Progressive hints for specific exercises.

**Example:**
```
exercise_id: "var_01"
attempt: "name = Alice"  # Student's incorrect attempt
```

**Output:** Targeted hint:
```
Good start! You have the right idea about assignment. But string values in Python need to be enclosed in quotes - single or double. Can you add quotes around Alice?
```

## System Prompts

Prompts are loaded from `prompts/` directory at startup:

- `design_lesson.txt` - Instructs LLM to output valid JSON with knowledge point structure
- `generate_page.txt` - Ensures complete, valid HTML5 with no external resources
- `tutor_chat.txt` - Enforces Socratic method and student-centered guidance
- `exercise_hint.txt` - Progressive hint generation without spoiling answers

Each prompt is cached after its first read, so restart the server after editing one.

## Exercises Database

The server loads 450 exercises from PyLearn's `docs/exercises.json`:

- 9 topics: variables, data_types, conditionals, loops, functions, lists_sets, dictionaries, fastapi_ex, api_calling
- 50 exercises per topic
- Each exercise includes: id, title, difficulty (1-5), description, hints, solution, starter_code, test_code, concepts

The exercise database is:
- Pre-loaded at startup for fast searching
- Cached in memory to avoid repeated file I/O
- Searched by keyword matching when relevant exercises are needed for tutoring

## HTTP Bridge (used by the Pytor site)

`api_bridge.py` is a second entry point and does not use FastMCP. It is a stdlib-only HTTP
server that the Pytor site and the PyQuest app talk to. It calls Groq first when
`GROQ_API_KEY` is set and falls back to Ollama.

```bash
python3 api_bridge.py      # listens on localhost:8100
```

Routes: `GET /health`, `POST /chat`, `POST /hint`, `POST /design-lesson`,
`POST /generate-page`. `/chat` takes a `mode` of `chat` (the default, Socratic), `study`
(explains and quizzes, never writes code) or `quest` (the expert persona PyQuest uses).
The two extra prompts, `tutor_study.txt` and `tutor_quest.txt`, live in `prompts/` next to
the four above.

Environment variables (defaults are set in `api_bridge.py`):

- `GROQ_API_KEY`, `GROQ_MODEL`: the primary backend.
- `OLLAMA_URL`, `OLLAMA_MODEL`: the fallback. Unlike the MCP server, `OLLAMA_URL` here is
  the full `/v1/chat/completions` endpoint, not the base URL.
- `TUTOR_HOST`, `TUTOR_PORT`: bind address and port, `localhost` and `8100` by default.
- `PROMPTS_DIR`, `PYLEARN_EXERCISES_PATH`: where prompts and `exercises.json` are read from.
- `TUTOR_DAILY_CAP`: global ceiling on LLM calls per UTC day (1500 by default, in memory,
  reset by a restart).
- `TUTOR_MAX_BODY_BYTES`: request body limit (65536 by default).
- `QUEST_LOG_PATH`: JSONL log of quest-mode exchanges (question, context, answer, backend,
  timing, no IPs). Defaults to `quest_chat.jsonl` next to the script; an empty string
  turns it off.

Per-IP limits are 10 requests a minute on `/chat` and `/hint` and 5 on `/design-lesson`
and `/generate-page`; localhost is exempt. Over a limit, or once the daily cap is spent,
the bridge answers HTTP 429.

## Development

Tests can be run with pytest:

```bash
pytest tests/
```

## Performance

- **Ollama calls**: ~2-5s per request (depends on model and hardware)
- **Exercise search**: O(n) simple keyword matching (negligible for 450 exercises)
- **Concurrent requests**: Handled by FastMCP + httpx async patterns

## Error Handling

- **Missing exercises**: Returns user-friendly error message
- **Ollama unavailable**: Logs error and returns error string
- **Invalid JSON from LLM** (`design_lesson`): Valid JSON without `knowledge_points` gets one retry with explicit instructions; unparseable output returns an error JSON holding the first 500 characters of the raw response
- **Malformed HTML**: Uses fallback template with core features

## Logging

Logs to stderr (standard for MCP servers):

```
2025-04-08 10:32:15,123 - pylearn-tutor - INFO - Loaded 450 exercises
2025-04-08 10:32:16,456 - pylearn-tutor - INFO - Designing lesson for topic: functions
```

## Future Enhancements

- [ ] Caching of generated pages to reduce LLM calls
- [ ] Exercise difficulty prediction based on student performance
- [ ] Integration with student progress tracking
- [ ] Multi-language support
- [ ] Voice-to-text tutoring input
