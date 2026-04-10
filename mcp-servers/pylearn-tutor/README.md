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

Prompts can be edited without restarting the server (on next tool call).

## Exercises Database

The server loads 400 exercises from PyLearn's `docs/exercises.json`:

- 8 topics: variables, data_types, conditionals, functions, lists_sets, dictionaries, fastapi_ex, api_calling
- 50 exercises per topic (on average)
- Each exercise includes: id, title, difficulty (1-5), description, hints, solution, starter_code, test_code, concepts

The exercise database is:
- Pre-loaded at startup for fast searching
- Cached in memory to avoid repeated file I/O
- Searched by keyword matching when relevant exercises are needed for tutoring

## Development

Tests can be run with pytest:

```bash
pytest tests/
```

## Performance

- **Ollama calls**: ~2-5s per request (depends on model and hardware)
- **Exercise search**: O(n) simple keyword matching (negligible for 400 exercises)
- **Concurrent requests**: Handled by FastMCP + httpx async patterns

## Error Handling

- **Missing exercises**: Returns user-friendly error message
- **Ollama unavailable**: Logs error and returns error string
- **Invalid JSON from LLM**: Retries with explicit instructions, falls back to safe defaults
- **Malformed HTML**: Uses fallback template with core features

## Logging

Logs to stderr (standard for MCP servers):

```
2025-04-08 10:32:15,123 - pylearn-tutor - INFO - Loaded 400 exercises
2025-04-08 10:32:16,456 - pylearn-tutor - INFO - Designing lesson for topic: functions
```

## Future Enhancements

- [ ] Caching of generated pages to reduce LLM calls
- [ ] Exercise difficulty prediction based on student performance
- [ ] Integration with student progress tracking
- [ ] Multi-language support
- [ ] Voice-to-text tutoring input
