"""Exercise definition and test infrastructure."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Callable


class Difficulty(Enum):
    BEGINNER = 1
    EASY = 2
    MEDIUM = 3
    HARD = 4
    CHALLENGE = 5

    def __str__(self) -> str:
        return self.name.capitalize()

    @property
    def stars(self) -> str:
        return "\u2b50" * self.value


@dataclass
class TestCase:
    """A single test case for an exercise."""

    input_args: tuple = ()
    input_kwargs: dict = field(default_factory=dict)
    expected: Any = None
    description: str = ""


@dataclass
class Exercise:
    """A single auto-graded exercise."""

    id: str
    title: str
    topic: str
    difficulty: Difficulty
    description: str
    hints: list[str] = field(default_factory=list)
    solution: str = ""
    starter_code: str = ""
    # For function-based exercises
    test_cases: list[TestCase] = field(default_factory=list)
    function_name: str = ""
    # For expression/variable-based exercises
    check: Callable[[dict], tuple[bool, str]] | None = None
    # For code-output exercises
    expected_output: str | None = None
    # Concepts taught
    concepts: list[str] = field(default_factory=list)


def make_exercise(
    id: str,
    title: str,
    topic: str,
    difficulty: int,
    description: str,
    *,
    hints: list[str] | None = None,
    solution: str = "",
    starter_code: str = "",
    test_cases: list[tuple | dict] | None = None,
    function_name: str = "",
    check: Callable[[dict], tuple[bool, str]] | None = None,
    expected_output: str | None = None,
    concepts: list[str] | None = None,
) -> Exercise:
    """Convenience factory for creating exercises with less boilerplate."""
    cases = []
    if test_cases:
        for tc in test_cases:
            if isinstance(tc, dict):
                cases.append(TestCase(**tc))
            elif isinstance(tc, tuple) and len(tc) == 2:
                cases.append(TestCase(input_args=(tc[0],) if not isinstance(tc[0], tuple) else tc[0], expected=tc[1]))
            elif isinstance(tc, tuple) and len(tc) == 3:
                args = tc[0] if isinstance(tc[0], tuple) else (tc[0],)
                cases.append(TestCase(input_args=args, expected=tc[1], description=tc[2]))

    return Exercise(
        id=id,
        title=title,
        topic=topic,
        difficulty=Difficulty(difficulty),
        description=description,
        hints=hints or [],
        solution=solution,
        starter_code=starter_code,
        test_cases=cases,
        function_name=function_name,
        check=check,
        expected_output=expected_output,
        concepts=concepts or [],
    )
