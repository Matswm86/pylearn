# PyLearn Tutor - Quick Start Guide

## 60-Second Setup

### 1. Install (one-time)
```bash
cd <pylearn-tutor>
pip install -r requirements.txt
```

### 2. Start Ollama
```bash
ollama serve
# In another terminal: ollama pull llama3.2:3b
```

### 3. Start Server
```bash
cd <pylearn-tutor>
python3 server.py
```

Or use the helper script:
```bash
./start-server.sh
```

### 4. Integrate with Claude Code
Add this to `~/.mcp.json` or `<pylearn-repo>/.mcp.json`:

```json
{
  "mcpServers": {
    "pylearn-tutor": {
      "command": "python3",
      "args": ["<pylearn-tutor>/server.py"],
      "env": {
        "OLLAMA_URL": "http://localhost:11434",
        "OLLAMA_MODEL": "llama3.2:3b",
        "PYTHONUNBUFFERED": "1"
      }
    }
  }
}
```

---

## Using the 4 Tools

### Tool 1: design_lesson
Decompose any Python topic into a learning sequence.

```
Prompt: "Design a lesson for Python list comprehensions"

Response: JSON with 3-6 knowledge points, each with:
- Title
- Summary
- Difficulty (beginner/intermediate/advanced)
- Key concepts
- Related exercise IDs
```

### Tool 2: generate_page
Create an interactive HTML learning page.

```
Prompt: "Generate an interactive page about Python functions"

Response: Complete HTML5 with:
- Modern responsive design
- Code examples
- Interactive quiz
- No external dependencies
```

### Tool 3: tutor_chat
Socratic tutoring through conversation.

```
Prompt: "How do I loop through a dictionary in Python?"

Response: Guiding questions instead of direct answers:
"Great question! What do you think you need to do with
each key-value pair in the dictionary? Can you think of
a tool you've learned that repeats actions?"
```

### Tool 4: get_exercise_hint
Progressive hints for specific exercises.

```
Prompt: "Give me a hint for exercise var_01. 
My attempt is: name = Alice"

Response: Targeted hint:
"Good start! String values need to be in quotes.
Can you add quotes around Alice?"
```

---

## Example Workflows

### Workflow 1: Create a Complete Lesson
```
1. "Design a lesson for Python dictionaries" (design_lesson)
2. Read the knowledge points from the response
3. "Create a page for 'Dictionary Basics' at beginner level" (generate_page)
4. Save the HTML and use it in the PyLearn app
```

### Workflow 2: Tutor a Student
```
1. "The student is stuck on list operations. Guide them."
2. Student: "How do I get the first item from a list?"
3. "Provide tutoring guidance without direct answers" (tutor_chat)
4. Continue conversation, referencing relevant exercises
```

### Workflow 3: Help with Specific Exercise
```
1. "Student needs help with var_05. They wrote: x, y, z = 10, 20"
2. "Get a hint for exercise var_05 with their attempt" (get_exercise_hint)
3. Share the hint with the student
4. Student makes another attempt, ask for another hint if needed
```

---

## Common Prompts

### For Lesson Design
```
"Design a complete lesson for Python [topic]"
"Break down [concept] into 5 learning modules"
"Create a structured lesson plan for teaching [topic]"
```

### For Page Generation
```
"Generate an interactive learning page about [topic] at [difficulty] level"
"Create a self-contained HTML lesson for [knowledge point]"
"Make an engaging page that teaches [concept]"
```

### For Tutoring
```
"I don't understand [topic]. Help me learn it."
"How do I [question about code]?"
"My code isn't working. Can you guide me to the fix?"
```

### For Exercise Hints
```
"I'm stuck on exercise [id]. Help?"
"Exercise [id]: my attempt is [code]. What's wrong?"
"Give me a hint for [id]. I've been working on it: [attempt]"
```

---

## Environment Variables

Set these before starting the server:

```bash
# Ollama configuration
export OLLAMA_URL=http://localhost:11434        # Default
export OLLAMA_MODEL=llama3.2:3b                 # Default

# Path to exercises
export PYLEARN_EXERCISES_PATH=/path/to/exercises.json

# Debug logging
export DEBUG=1                                  # Optional
```

Or in `.env`:
```
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
PYTHONUNBUFFERED=1
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "Connection refused" | Start Ollama: `ollama serve` |
| "Model not found" | Pull the model: `ollama pull llama3.2:3b` |
| "exercises.json not found" | Set `PYLEARN_EXERCISES_PATH` environment variable |
| "Slow responses" | Use `llama3.2:3b` (fast) instead of larger models |
| "Poor quality output" | Try `mistral:latest` or `llama3.2:latest` |

---

## Performance

| Tool | Time | Output |
|------|------|--------|
| design_lesson | 3-5s | ~500 chars JSON |
| generate_page | 4-7s | 5-15 KB HTML |
| tutor_chat | 2-3s | 100-300 chars |
| get_exercise_hint | 2-3s | 100-200 chars |

All tools run async - no blocking.

---

## File Locations

```
<pylearn-tutor>/
├── server.py                    # Main server
├── README.md                    # Full documentation
├── INTEGRATION.md               # Integration guide
├── BUILD_SUMMARY.md             # Architecture details
├── QUICKSTART.md                # This file
├── requirements.txt             # pip install
├── prompts/                     # Editable system prompts
│   ├── design_lesson.txt
│   ├── generate_page.txt
│   ├── tutor_chat.txt
│   └── exercise_hint.txt
└── tests/test_server.py         # Test suite
```

---

## Editing System Prompts

To customize how the tools work, edit the prompt files in `prompts/`:

```bash
nano <pylearn-tutor>/prompts/tutor_chat.txt
```

Changes take effect on the next tool call (prompts are reloaded).

---

## Helpful Links

- **README.md** - Complete tool reference and features
- **INTEGRATION.md** - Step-by-step Claude Code integration
- **BUILD_SUMMARY.md** - Architecture and implementation details
- **tests/test_server.py** - Example usage and test patterns

---

## Key Features

- ✓ 400 exercises automatically available as context
- ✓ Progressive hint generation (doesn't reveal solutions)
- ✓ Socratic tutoring (guides discovery instead of giving answers)
- ✓ Auto-generated interactive learning pages
- ✓ Lesson decomposition for any Python topic
- ✓ Full Ollama integration (async, non-blocking)
- ✓ No external dependencies or resources

---

## Next Steps

1. ✓ Server installed and configured
2. ✓ Ollama running and ready
3. → Start using with Claude Code
4. → Try the example prompts above
5. → Customize prompts as needed

Happy tutoring!
