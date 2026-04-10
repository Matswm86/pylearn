# PyLearn Tutor MCP Server - Integration Guide

This guide shows how to integrate the PyLearn Tutor server with Claude Code or other MCP clients.

## Quick Start

### 1. Install Dependencies

```bash
cd <pylearn-tutor>
pip install -r requirements.txt
```

### 2. Start Ollama (if not already running)

```bash
# On macOS or Linux with Ollama installed:
ollama serve

# Or in another terminal:
ollama run llama3.2:3b
```

Verify Ollama is running:
```bash
curl http://localhost:11434/api/tags
```

### 3. Configure in .mcp.json

Add to your project's `.mcp.json`:

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

Or for just the PyLearn project's `.mcp.json`:

```bash
cat > <pylearn-repo>/.mcp.json << 'EOF'
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
EOF
```

### 4. Test Connection

```bash
# With Claude Code open in the pylearn directory:
# Use the "Tools" panel to test the connection
# You should see 4 tools: design_lesson, generate_page, tutor_chat, get_exercise_hint
```

## Usage Examples

### Example 1: Design a Lesson

Prompt to Claude:
> "Design a lesson for Python list comprehensions using the design_lesson tool"

Claude will:
1. Call `design_lesson("Python list comprehensions")`
2. Receive structured knowledge points
3. Display them formatted

### Example 2: Generate Interactive Learning Page

Prompt to Claude:
> "Create an interactive learning page for 'Understanding Python Functions' at intermediate difficulty"

Claude will:
1. Call `generate_page(title="Understanding Python Functions", summary="...", difficulty="intermediate")`
2. Receive complete HTML
3. Save to a file or display in preview

### Example 3: Student Tutoring Session

Prompt to Claude:
> "Help me understand how to loop through a dictionary in Python"

Claude will:
1. Call `tutor_chat(question="How to loop through a dictionary")`
2. Receive Socratic guidance
3. Continue conversation with follow-up questions

### Example 4: Exercise Hint Request

Prompt to Claude:
> "I'm stuck on exercise var_05. My attempt is 'x, y, z = 10, 20' but it's not working"

Claude will:
1. Call `get_exercise_hint(exercise_id="var_05", attempt="x, y, z = 10, 20")`
2. Analyze the attempt
3. Provide a hint: "You're on the right track with unpacking! But you need to assign all three values..."

## Advanced Configuration

### Use a Different Ollama Model

```bash
export OLLAMA_MODEL=mistral:latest
python server.py
```

Or in .mcp.json:
```json
"env": {
  "OLLAMA_MODEL": "mistral:latest"
}
```

Available models (install with `ollama pull`):
- `llama3.2:3b` - Fast, good quality (default)
- `llama3.2:latest` - Larger, better quality
- `mistral:latest` - Fast, strong reasoning
- `neural-chat:latest` - Optimized for chat

### Customize Prompts

Edit the prompt files in `prompts/` directory:

```bash
# Edit the Socratic method prompt
nano prompts/tutor_chat.txt

# Changes take effect on next tool call (prompts are reloaded)
```

### Enable Debug Logging

```bash
export DEBUG=1
python server.py
```

Logs will show:
- Exercise loading
- Ollama API calls
- Prompt loading
- Search results

## Troubleshooting

### "Connection refused" - Ollama not running

```bash
# Start Ollama
ollama serve

# In another terminal, ensure model is cached
ollama pull llama3.2:3b
```

### "exercises.json not found"

```bash
# Verify path exists
ls -la <pylearn-repo>/docs/exercises.json

# Or set explicit path
export PYLEARN_EXERCISES_PATH=<pylearn-repo>/docs/exercises.json
```

### "Invalid JSON response" from design_lesson

The LLM may not be following instructions perfectly. The server:
1. Attempts to parse the response
2. If invalid, retries with stricter instructions
3. Falls back to a safe error message

Try with a larger model:
```bash
OLLAMA_MODEL=llama3.2:latest python server.py
```

### Generated HTML looks plain

The fallback HTML is minimal. To get better output:
1. Ensure Ollama is running
2. Check Ollama logs for errors
3. Try with `mistral:latest` model (better at code generation)

## Performance Tips

1. **Pre-load model**: Run `ollama pull llama3.2:3b` to cache it
2. **Use smaller model for speed**: llama3.2:3b (default) is fast
3. **Cache generated pages**: Save HTML output for reuse
4. **Batch operations**: Design lesson first, then generate page from its output

## API Reference

### design_lesson(topic: str) -> str
- **Input**: Topic string (e.g., "Python loops")
- **Output**: JSON with knowledge_points array
- **Calls LLM**: Yes
- **Time**: ~3-5 seconds

### generate_page(title: str, summary: str, difficulty: str = "intermediate") -> str
- **Input**: Page title, summary, difficulty level
- **Output**: Complete HTML5 document
- **Calls LLM**: Yes
- **Time**: ~4-7 seconds
- **Size**: ~5-15 KB HTML

### tutor_chat(question: str, context: str = "", history: str = "") -> str
- **Input**: Student question, optional context, optional chat history (JSON array)
- **Output**: Tutoring response
- **Calls LLM**: Yes
- **Time**: ~2-3 seconds

### get_exercise_hint(exercise_id: str, attempt: str = "") -> str
- **Input**: Exercise ID (e.g., "var_01"), optional student attempt
- **Output**: Progressive hint
- **Calls LLM**: Yes
- **Time**: ~2-3 seconds

## Next Steps

1. **Integrate with PyLearn UI**: Call tools from the web frontend
2. **Build student dashboard**: Track progress using chat history
3. **Create content management**: Auto-generate lesson pages from exercises
4. **Add persistence**: Store generated pages and chats in database
5. **Enhance hints**: Use exercise test_code to analyze student attempts

## Contributing

To improve the server:

1. Edit system prompts in `prompts/` directory
2. Add new tools following the existing pattern
3. Run tests: `pytest tests/test_server.py`
4. Submit improvements

## License

MIT - See LICENSE file

## Support

For issues:
1. Check logs in stderr
2. Verify Ollama is running: `curl http://localhost:11434/api/tags`
3. Test prompts manually: `curl -X POST http://localhost:11434/api/chat -d '{...}'`
