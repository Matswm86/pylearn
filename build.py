#!/usr/bin/env python3
"""Build script: converts Python exercise modules into web-ready JS data file."""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from pylearn.exercises import (
    variables, data_types, conditionals, functions,
    lists_sets, dictionaries, fastapi_ex, api_calling,
)
from pylearn.exercises.base import Exercise


def generate_test_code(ex: Exercise) -> str:
    """Generate Python assertion strings for web grading."""
    lines: list[str] = []

    # Mode 1: function_name + test_cases
    if ex.function_name and ex.test_cases:
        lines.append(f"assert '{ex.function_name}' in dir(), \"Function '{ex.function_name}' not defined. Did you write: def {ex.function_name}(...)?\"")
        for i, tc in enumerate(ex.test_cases):
            args_parts = []
            for a in tc.input_args:
                args_parts.append(repr(a))
            for k, v in tc.input_kwargs.items():
                args_parts.append(f"{k}={v!r}")
            args_str = ", ".join(args_parts)
            call = f"{ex.function_name}({args_str})"

            if callable(tc.expected):
                lines.append(f"_r{i} = {call}")
                lines.append(f"assert _r{i} is not None, 'Test {i+1}: {ex.function_name} returned None'")
            else:
                lines.append(f"_r{i} = {call}")
                lines.append(f"assert _r{i} == {tc.expected!r}, f'Test {i+1}: {call} returned {{_r{i}!r}}, expected {tc.expected!r}'")
        return "\n".join(lines)

    # Mode 2: expected_output
    if ex.expected_output is not None:
        return f"# Output check handled by runner\n__expected_output__ = {ex.expected_output!r}"

    # Mode 3: check-based — run solution to get expected namespace values
    if ex.check is not None and ex.solution:
        return _generate_from_solution(ex)

    # Fallback: if there's a solution, verify it runs
    if ex.solution:
        return _generate_from_solution(ex)

    return "pass  # No automated test"


def _value_required_by_description(var_name: str, value: object, description: str) -> bool:
    """Check if the exercise description explicitly requires a specific value.

    Returns True if the description makes it clear that a SPECIFIC value is required.
    Returns False if the exercise is about a CONCEPT (e.g., "your name",
    "create a list", "sample data") where any valid answer should be accepted.

    Key insight: Some exercises ask for ANY example (RELAXED),
    while others specify exact values or deterministic results (STRICT).
    """
    desc_lower = description.lower()

    # CONCEPT: Exercises where ANY valid answer is acceptable.
    # Look for patterns like "your X", "any X", "sample X", "create a [type]"
    # WITHOUT a specific value constraint.
    if "your name" in desc_lower or "your age" in desc_lower:
        return False
    if "your favorite" in desc_lower or "your " in desc_lower:
        return False
    if "sample" in desc_lower or "example " in desc_lower:
        return False
    if "any " in desc_lower or "any," in desc_lower:
        return False

    # For strings: Check if it's explicitly required
    if isinstance(value, str):
        # If the exact string appears quoted in the description, it's required
        if f"'{value}'" in description or f'"{value}"' in description:
            return True
        # Phrases that imply a specific string value is needed
        if any(phrase in desc_lower for phrase in [
            "set it to", "assign it the value", "should be", "must equal",
            "with the value", "containing the text", "with the string",
            "store the string", "equals",
        ]):
            if value.lower() in desc_lower:
                return True
        return False

    if isinstance(value, bool):
        # For booleans, only required if explicitly stated
        if str(value).lower() in desc_lower:
            return True
        return False

    if isinstance(value, (int, float)):
        # For numbers: required if:
        # 1. The number appears explicitly in the description (e.g., "the value 25", "10, 20, 30")
        # 2. The exercise is about a calculation or deterministic result (swap, sum, etc.)

        # Check if description explicitly mentions the number
        if str(value) in description:
            return True

        # Check for calculation/deterministic phrases (calculation results must be exact)
        if any(phrase in desc_lower for phrase in [
            "swap", "calculate", "compute", "result", "total", "sum",
            "add", "multiply", "divide", "tax", "discount", "price"
        ]):
            return True

        return False

    return False


def _generate_from_solution(ex: Exercise) -> str:
    """Execute solution and generate assertions from the resulting namespace.

    For each variable, decide whether to check:
    1. Exact value (if the description requires it)
    2. Type only (if it's a concept exercise)
    """
    ns: dict = {}
    try:
        exec(ex.solution, ns)
    except Exception:
        return "pass  # Solution requires external modules"

    lines: list[str] = []
    skip = {'__builtins__', '__name__', '__doc__', '__loader__', '__spec__', '__package__'}

    for name, value in ns.items():
        if name in skip or name.startswith('_'):
            continue

        # Skip modules, classes, functions — only assert on simple values
        if callable(value) and not isinstance(value, (list, dict, set, tuple)):
            # For functions, just check they exist
            lines.append(f"assert '{name}' in dir(), \"'{name}' is not defined\"")
            lines.append(f"assert callable({name}), \"'{name}' should be a function\"")
            continue

        if isinstance(value, type):
            lines.append(f"assert '{name}' in dir(), \"Class '{name}' not defined\"")
            continue

        is_exact_required = _value_required_by_description(name, value, ex.description)

        if isinstance(value, str):
            # For strings: only check exact value if the description requires it
            if is_exact_required:
                lines.append(f"assert {name} == {value!r}, f\"{name} should be {value!r}, got {{{name}!r}}\"")
            else:
                # Just check it's a string and non-empty
                lines.append(f"assert isinstance({name}, str), f\"{name} should be a string (text), got {{type({name}).__name__}}\"")
                lines.append(f"assert len({name}) > 0, \"{name} should not be empty\"")
        elif isinstance(value, bool):
            # For booleans: check exact value only if explicitly required
            if is_exact_required:
                lines.append(f"assert {name} == {value!r}, f\"{name} should be {value!r}, got {{{name}!r}}\"")
            else:
                lines.append(f"assert isinstance({name}, bool), f\"{name} should be a boolean (True/False), got {{type({name}).__name__}}\"")
        elif isinstance(value, (int, float)):
            # For numbers: check exact value only if explicitly required
            if is_exact_required:
                lines.append(f"assert {name} == {value!r}, f\"{name} should be {value!r}, got {{{name}!r}}\"")
            else:
                lines.append(f"assert isinstance({name}, ({int.__name__}, {float.__name__})), f\"{name} should be a number, got {{type({name}).__name__}}\"")
        elif isinstance(value, list):
            # For lists: check type and non-empty if concept exercise, exact if specified
            if is_exact_required:
                lines.append(f"assert {name} == {value!r}, f\"{name} has wrong value\"")
            else:
                lines.append(f"assert isinstance({name}, list), f\"{name} should be a list, got {{type({name}).__name__}}\"")
                if len(value) > 0:
                    lines.append(f"assert len({name}) > 0, \"{name} should not be empty\"")
        elif isinstance(value, dict):
            # For dicts: check type and non-empty if concept exercise, exact if specified
            if is_exact_required:
                lines.append(f"assert {name} == {value!r}, f\"{name} has wrong value\"")
            else:
                lines.append(f"assert isinstance({name}, dict), f\"{name} should be a dictionary, got {{type({name}).__name__}}\"")
                if len(value) > 0:
                    lines.append(f"assert len({name}) > 0, \"{name} should not be empty\"")
        elif isinstance(value, (tuple, set)):
            # For tuples and sets: similar approach
            if is_exact_required:
                lines.append(f"assert {name} == {value!r}, f\"{name} has wrong value\"")
            else:
                type_name = "tuple" if isinstance(value, tuple) else "set"
                lines.append(f"assert isinstance({name}, {type(value).__name__}), f\"{name} should be a {type_name}, got {{type({name}).__name__}}\"")
                if len(value) > 0:
                    lines.append(f"assert len({name}) > 0, \"{name} should not be empty\"")

    if not lines:
        lines.append("pass  # Verify your code runs without errors")

    return "\n".join(lines)


def exercise_to_dict(ex: Exercise) -> dict:
    """Convert an Exercise dataclass to a web-friendly dict."""
    return {
        "id": ex.id,
        "title": ex.title,
        "difficulty": ex.difficulty.value,
        "description": ex.description,
        "hints": ex.hints,
        "solution": ex.solution,
        "starter_code": ex.starter_code or "",
        "test_code": generate_test_code(ex),
        "concepts": ex.concepts,
    }


TOPIC_ORDER = [
    ("variables", "Variables", variables.exercises),
    ("data_types", "Data Types", data_types.exercises),
    ("conditionals", "Conditionals", conditionals.exercises),
    ("functions", "Functions", functions.exercises),
    ("lists_sets", "Lists & Sets", lists_sets.exercises),
    ("dictionaries", "Dictionaries", dictionaries.exercises),
    ("fastapi_ex", "FastAPI", fastapi_ex.exercises),
    ("api_calling", "API Calling", api_calling.exercises),
]


def build() -> None:
    topics = []
    total = 0

    for topic_id, topic_title, exs in TOPIC_ORDER:
        exercises_data = [exercise_to_dict(ex) for ex in exs]
        topics.append({
            "id": topic_id,
            "title": topic_title,
            "exercise_count": len(exercises_data),
            "exercises": exercises_data,
        })
        total += len(exercises_data)
        print(f"  {topic_title}: {len(exercises_data)} exercises")

    output = {
        "version": "1.0.0",
        "total_exercises": total,
        "topics": topics,
    }

    out_path = Path(__file__).parent / "docs" / "exercises.json"
    out_path.parent.mkdir(exist_ok=True)
    out_path.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"\nWrote {total} exercises to {out_path}")


if __name__ == "__main__":
    build()
