#!/usr/bin/env python3
"""
PyLearn AI Tutor - FastMCP Server

A comprehensive Python tutoring server with:
- Lesson design (topic decomposition)
- Interactive page generation
- Socratic tutoring chat
- Progressive exercise hints

Powered by Ollama + FastMCP 2.14.6
"""

import asyncio
import json
import logging
import os
import sys
from pathlib import Path
from typing import Any

import httpx
from fastmcp import FastMCP

# ============================================================================
# CONFIGURATION & SETUP
# ============================================================================

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)

# Environment variables
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
PYLEARN_EXERCISES_PATH = os.getenv(
    "PYLEARN_EXERCISES_PATH",
    str(Path(__file__).parent.parent.parent / "docs" / "exercises.json"),
)

# FastMCP server instance
server = FastMCP(
    name="pylearn-tutor",
    version="1.0.0",
)

# Module-level cache for exercises and prompts
_exercises_cache = None
_prompts_cache = {}


# ============================================================================
# UTILITIES
# ============================================================================


def load_exercises() -> dict[str, Any]:
    """Load exercises from JSON file (cached)."""
    global _exercises_cache
    if _exercises_cache is not None:
        return _exercises_cache

    try:
        with open(PYLEARN_EXERCISES_PATH, "r") as f:
            data = json.load(f)
        logger.info(f"Loaded {data['total_exercises']} exercises from {PYLEARN_EXERCISES_PATH}")

        # Flatten exercises into a searchable dict by ID
        flat_exercises = {}
        for topic in data.get("topics", []):
            for exercise in topic.get("exercises", []):
                flat_exercises[exercise["id"]] = exercise
        _exercises_cache = flat_exercises
        return flat_exercises
    except Exception as e:
        logger.error(f"Failed to load exercises: {e}")
        return {}


def load_prompt(name: str) -> str:
    """Load a system prompt from file (cached)."""
    if name not in _prompts_cache:
        try:
            prompt_path = Path(__file__).parent / "prompts" / f"{name}.txt"
            with open(prompt_path, "r") as f:
                _prompts_cache[name] = f.read().strip()
            logger.debug(f"Loaded prompt: {name}")
        except Exception as e:
            logger.error(f"Failed to load prompt {name}: {e}")
            _prompts_cache[name] = ""
    return _prompts_cache[name]


async def call_ollama(
    system_prompt: str,
    user_message: str,
    temperature: float = 0.7,
    max_tokens: int = 2048,
) -> str:
    """
    Call Ollama API with OpenAI-compatible format.
    Returns the assistant's response text.
    """
    url = f"{OLLAMA_URL}/v1/chat/completions"
    headers = {"Content-Type": "application/json"}
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        "temperature": temperature,
        "max_tokens": max_tokens,
    }

    try:
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(url, json=payload, headers=headers)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        logger.error(f"Ollama API call failed: {e}")
        return f"Error calling LLM: {str(e)}"


def search_exercises(keywords: list[str], limit: int = 3) -> list[dict[str, Any]]:
    """
    Search exercises by keywords (simple keyword matching).
    Returns up to `limit` exercises that match any keyword.
    """
    exercises = load_exercises()
    matched = []

    keywords_lower = [kw.lower() for kw in keywords]

    for exercise in exercises.values():
        # Search in title, description, and concepts
        searchable = (
            f"{exercise.get('title', '')} "
            f"{exercise.get('description', '')} "
            f"{' '.join(exercise.get('concepts', []))}"
        ).lower()

        if any(kw in searchable for kw in keywords_lower):
            matched.append(exercise)
            if len(matched) >= limit:
                break

    return matched


# ============================================================================
# MCP TOOLS
# ============================================================================


@server.tool()
async def design_lesson(topic: str) -> str:
    """
    Decompose a Python topic into 3-6 structured knowledge points.

    Args:
        topic: The Python topic to design a lesson for (e.g., "list comprehensions")

    Returns:
        JSON string with structured knowledge points including title, summary,
        difficulty, key_concepts, and related exercise IDs.
    """
    logger.info(f"Designing lesson for topic: {topic}")

    system_prompt = load_prompt("design_lesson")
    user_message = f"Design a comprehensive lesson for: {topic}"

    response = await call_ollama(system_prompt, user_message, temperature=0.6)

    # Validate JSON output
    try:
        parsed = json.loads(response)
        if "knowledge_points" in parsed:
            return json.dumps(parsed, indent=2)
        else:
            # Retry with more explicit instruction
            logger.warning("Invalid structure in response, retrying...")
            response = await call_ollama(
                system_prompt,
                f"Design a lesson for: {topic}\n\nRemember to output ONLY valid JSON with the exact structure required.",
                temperature=0.5,
            )
            return response
    except json.JSONDecodeError:
        logger.error(f"Failed to parse JSON response: {response[:200]}")
        return json.dumps(
            {
                "error": "Failed to generate valid JSON",
                "raw_response": response[:500],
            }
        )


@server.tool()
async def generate_page(
    title: str,
    summary: str,
    difficulty: str = "intermediate",
) -> str:
    """
    Generate a self-contained interactive HTML learning page.

    Args:
        title: Title of the knowledge point
        summary: Summary of the content to teach
        difficulty: "beginner", "intermediate", or "advanced" (default: intermediate)

    Returns:
        Complete, standalone HTML document (<!DOCTYPE html> through </html>)
    """
    logger.info(f"Generating page: {title} ({difficulty})")

    system_prompt = load_prompt("generate_page")
    user_message = f"""
Create an interactive HTML learning page with these details:
- Title: {title}
- Summary: {summary}
- Difficulty: {difficulty}

The page should include Python code examples, interactive elements, and a quiz.
"""

    html_output = await call_ollama(
        system_prompt,
        user_message,
        temperature=0.7,
        max_tokens=4096,
    )

    # Validate HTML output
    if "<!doctype html" not in html_output.lower() or "<html" not in html_output.lower():
        logger.warning("Invalid HTML structure, using fallback template")
        html_output = generate_fallback_html(title, summary, difficulty)

    return html_output


def generate_fallback_html(title: str, summary: str, difficulty: str) -> str:
    """Generate a fallback HTML page if LLM output is invalid."""
    difficulty_color = {
        "beginner": "#10B981",
        "intermediate": "#F59E0B",
        "advanced": "#EF4444",
    }.get(difficulty, "#4F46E5")

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - PyLearn Tutor</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            color: #1F2937;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 2rem;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
            padding: 3rem;
        }}
        .header {{
            margin-bottom: 2rem;
        }}
        h1 {{
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }}
        .difficulty-badge {{
            display: inline-block;
            background-color: {difficulty_color};
            color: white;
            padding: 0.4rem 0.8rem;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            text-transform: capitalize;
        }}
        .summary {{
            background: #F3F4F6;
            padding: 1.5rem;
            border-radius: 8px;
            margin-top: 1rem;
            border-left: 4px solid {difficulty_color};
        }}
        .section {{
            margin-top: 2rem;
        }}
        h2 {{
            font-size: 1.5rem;
            color: #1F2937;
            margin-bottom: 1rem;
        }}
        .code-block {{
            background: #1F2937;
            color: #E5E7EB;
            padding: 1rem;
            border-radius: 6px;
            overflow-x: auto;
            font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
            font-size: 0.9rem;
            margin: 1rem 0;
        }}
        .quiz-question {{
            background: #F9FAFB;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            border: 2px solid #E5E7EB;
        }}
        button {{
            background-color: {difficulty_color};
            color: white;
            padding: 0.75rem 1.5rem;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 1rem;
            margin-top: 0.5rem;
        }}
        button:hover {{
            opacity: 0.9;
        }}
        .footer {{
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid #E5E7EB;
            color: #6B7280;
            font-size: 0.9rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>{title}</h1>
            <span class="difficulty-badge">{difficulty}</span>
        </div>

        <div class="summary">
            <p>{summary}</p>
        </div>

        <div class="section">
            <h2>Core Concept</h2>
            <p>This lesson covers important aspects of Python programming. Work through the examples and quiz to master this topic.</p>
        </div>

        <div class="section">
            <h2>Example</h2>
            <div class="code-block">
# Python example code<br>print("Hello, PyLearn!")
            </div>
        </div>

        <div class="section">
            <h2>Practice Quiz</h2>
            <div class="quiz-question">
                <p><strong>Question 1:</strong> Do you understand the concept?</p>
                <button onclick="alert('Great! Try the exercises in PyLearn.')">Yes, Continue</button>
            </div>
        </div>

        <div class="footer">
            <p>PyLearn Interactive Tutor | Generated by AI Tutor Server</p>
        </div>
    </div>
</body>
</html>"""


@server.tool()
async def tutor_chat(
    question: str,
    context: str = "",
    history: str = "",
) -> str:
    """
    Provide Socratic tutoring guidance through chat.

    Args:
        question: The student's question or statement
        context: Optional lesson context or background information
        history: Optional chat history as JSON array of {role, content} objects

    Returns:
        Tutor's response using Socratic method (guiding questions, not direct answers)
    """
    logger.info(f"Tutor chat: {question[:50]}...")

    # Parse history
    chat_history_text = ""
    if history:
        try:
            history_items = json.loads(history)
            # Limit to last 4 messages to stay within token budget
            relevant_history = history_items[-4:] if len(history_items) > 4 else history_items
            chat_history_text = "\n".join(
                [f"{item.get('role', 'user').title()}: {item.get('content', '')}" for item in relevant_history]
            )
        except (json.JSONDecodeError, TypeError):
            logger.warning("Failed to parse chat history")

    # Search for relevant exercises
    keywords = question.split()
    relevant_exercises = search_exercises(keywords, limit=3)
    exercises_text = ""
    if relevant_exercises:
        exercises_text = "\n\nRelevant PyLearn exercises:\n"
        for ex in relevant_exercises:
            exercises_text += f"- {ex['id']}: {ex['title']} (Difficulty: {ex['difficulty']})\n"

    system_prompt = load_prompt("tutor_chat")
    user_message = f"""
Student's question: {question}

{f'Lesson context: {context}' if context else ''}

{chat_history_text}

{exercises_text}

Remember: Guide the student to discover the answer themselves using Socratic questioning. Keep your response concise (2-4 sentences). Reference related exercises when relevant.
"""

    response = await call_ollama(
        system_prompt,
        user_message,
        temperature=0.7,
        max_tokens=512,
    )

    return response


@server.tool()
async def get_exercise_hint(
    exercise_id: str,
    attempt: str = "",
) -> str:
    """
    Provide a progressive hint for a specific exercise.

    Args:
        exercise_id: The exercise ID (e.g., "var_01")
        attempt: Optional code or text showing the student's current attempt

    Returns:
        A guiding hint that helps without revealing the answer
    """
    logger.info(f"Getting hint for exercise: {exercise_id}")

    exercises = load_exercises()
    exercise = exercises.get(exercise_id)

    if not exercise:
        return f"Exercise {exercise_id} not found. Check the ID and try again."

    # Build context about the exercise
    exercise_context = f"""
Exercise: {exercise.get('title', 'Unknown')}
Description: {exercise.get('description', '')}
Concepts: {', '.join(exercise.get('concepts', []))}
Solution approach: {exercise.get('solution', 'See documentation')}
{"Student's attempt: " + attempt if attempt else ""}
"""

    system_prompt = load_prompt("exercise_hint")
    user_message = f"""
{exercise_context}

Provide a helpful hint that guides the student toward the solution without revealing the answer.
{"If they provided an attempt, analyze what's correct and what needs improvement." if attempt else "Provide a general hint about the approach."}
"""

    response = await call_ollama(
        system_prompt,
        user_message,
        temperature=0.6,
        max_tokens=512,
    )

    return response


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================


async def main():
    """Start the FastMCP server."""
    logger.info("Initializing PyLearn Tutor Server...")
    logger.info(f"Ollama URL: {OLLAMA_URL}")
    logger.info(f"Ollama Model: {OLLAMA_MODEL}")
    logger.info(f"Exercises Path: {PYLEARN_EXERCISES_PATH}")

    # Pre-load exercises and prompts
    load_exercises()
    for prompt_name in ["design_lesson", "generate_page", "tutor_chat", "exercise_hint"]:
        load_prompt(prompt_name)

    logger.info("Starting FastMCP stdio server...")
    await server.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())
