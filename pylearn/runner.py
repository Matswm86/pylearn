"""Exercise runner with auto-grading."""

from __future__ import annotations

import io
import sys
import traceback
from contextlib import redirect_stdout
from pathlib import Path
from typing import Any

from .exercises.base import Exercise


class ExerciseResult:
    """Result of running an exercise."""

    def __init__(self, exercise: Exercise):
        self.exercise = exercise
        self.passed = False
        self.total_tests = 0
        self.passed_tests = 0
        self.errors: list[str] = []
        self.output: str = ""

    @property
    def score_pct(self) -> int:
        if self.total_tests == 0:
            return 100 if self.passed else 0
        return int(self.passed_tests / self.total_tests * 100)


def run_code(code: str) -> tuple[dict[str, Any], str, str | None]:
    """Execute user code and return namespace, stdout, and error (if any)."""
    namespace: dict[str, Any] = {}
    stdout_capture = io.StringIO()
    error = None

    try:
        with redirect_stdout(stdout_capture):
            exec(code, namespace)
    except Exception:
        error = traceback.format_exc()

    return namespace, stdout_capture.getvalue(), error


def grade_exercise(exercise: Exercise, user_code: str) -> ExerciseResult:
    """Grade user code against exercise requirements."""
    result = ExerciseResult(exercise)

    # Run user code
    namespace, output, error = run_code(user_code)
    result.output = output

    if error:
        result.errors.append(f"Code error:\n{error}")
        return result

    # Check-based exercises (variable/expression checks)
    if exercise.check is not None:
        result.total_tests = 1
        try:
            passed, msg = exercise.check(namespace)
            result.passed = passed
            result.passed_tests = 1 if passed else 0
            if not passed:
                result.errors.append(msg)
        except Exception as e:
            result.errors.append(f"Check failed: {e}")
        return result

    # Output-based exercises
    if exercise.expected_output is not None:
        result.total_tests = 1
        actual = output.strip()
        expected = exercise.expected_output.strip()
        if actual == expected:
            result.passed = True
            result.passed_tests = 1
        else:
            result.errors.append(f"Expected output:\n  {expected}\nGot:\n  {actual}")
        return result

    # Function-based exercises with test cases
    if exercise.function_name and exercise.test_cases:
        func = namespace.get(exercise.function_name)
        if func is None:
            result.errors.append(
                f"Function '{exercise.function_name}' not found. "
                f"Make sure you defined: def {exercise.function_name}(...)"
            )
            result.total_tests = len(exercise.test_cases)
            return result

        result.total_tests = len(exercise.test_cases)
        for i, tc in enumerate(exercise.test_cases):
            try:
                actual = func(*tc.input_args, **tc.input_kwargs)
                # Support both direct equality and callable checkers
                if callable(tc.expected):
                    passed = tc.expected(actual)
                else:
                    passed = actual == tc.expected

                if passed:
                    result.passed_tests += 1
                else:
                    desc = tc.description or f"Test {i + 1}"
                    result.errors.append(
                        f"{desc}: {exercise.function_name}{tc.input_args} "
                        f"returned {actual!r}, expected {tc.expected!r}"
                    )
            except Exception as e:
                desc = tc.description or f"Test {i + 1}"
                result.errors.append(f"{desc}: raised {type(e).__name__}: {e}")

        result.passed = result.passed_tests == result.total_tests
        return result

    # If no test mechanism defined, just check it ran without errors
    result.passed = True
    result.total_tests = 1
    result.passed_tests = 1
    return result


def load_user_solution(exercise_id: str, workspace: Path | None = None) -> str | None:
    """Load user's solution file for an exercise."""
    ws = workspace or Path.cwd() / "solutions"
    solution_file = ws / f"{exercise_id}.py"
    if solution_file.exists():
        return solution_file.read_text()
    return None


def save_starter_code(exercise: Exercise, workspace: Path | None = None) -> Path:
    """Save exercise starter code to workspace."""
    ws = workspace or Path.cwd() / "solutions"
    ws.mkdir(parents=True, exist_ok=True)
    solution_file = ws / f"{exercise.id}.py"
    if not solution_file.exists():
        content = f'# {exercise.title}\n# {exercise.description}\n\n'
        if exercise.starter_code:
            content += exercise.starter_code
        else:
            content += "# Write your solution below:\n"
        solution_file.write_text(content)
    return solution_file
