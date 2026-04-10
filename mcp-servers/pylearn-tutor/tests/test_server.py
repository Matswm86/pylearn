"""
Tests for PyLearn Tutor MCP Server

Note: These tests require:
- Ollama running at http://localhost:11434
- exercises.json available at the configured path
"""

import asyncio
import json
import pytest

from server import (
    design_lesson,
    generate_page,
    tutor_chat,
    get_exercise_hint,
    load_exercises,
    search_exercises,
)


class TestExerciseLoading:
    """Test exercise loading and caching."""

    def test_load_exercises(self):
        """Exercises should load successfully."""
        exercises = load_exercises()
        assert len(exercises) > 0
        assert "var_01" in exercises  # Known exercise from variables topic

    def test_exercise_structure(self):
        """Exercises should have required fields."""
        exercises = load_exercises()
        exercise = exercises.get("var_01")
        assert exercise is not None
        assert "id" in exercise
        assert "title" in exercise
        assert "difficulty" in exercise
        assert "description" in exercise
        assert "solution" in exercise
        assert "test_code" in exercise
        assert "concepts" in exercise

    def test_exercise_caching(self):
        """Loading exercises twice should use cache."""
        ex1 = load_exercises()
        ex2 = load_exercises()
        assert ex1 is ex2  # Same object reference = cached


class TestSearchExercises:
    """Test exercise search functionality."""

    def test_search_by_keyword(self):
        """Should find exercises matching keywords."""
        results = search_exercises(["variable"], limit=5)
        assert len(results) > 0
        assert all("variable" in ex.get("title", "").lower() or
                   "variable" in ex.get("description", "").lower() or
                   "variable" in [c.lower() for c in ex.get("concepts", [])]
                   for ex in results)

    def test_search_limit(self):
        """Search should respect limit parameter."""
        results = search_exercises(["assignment"], limit=2)
        assert len(results) <= 2

    def test_search_empty_keywords(self):
        """Search with no matches should return empty list."""
        results = search_exercises(["xyznonexistent123"], limit=5)
        assert len(results) == 0


@pytest.mark.asyncio
class TestLessonDesign:
    """Test lesson design tool."""

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_design_lesson_basic(self):
        """Should design a lesson for a topic."""
        result = await design_lesson("Python variables")
        assert isinstance(result, str)

        # Should return valid JSON
        data = json.loads(result)
        assert "knowledge_points" in data
        assert len(data["knowledge_points"]) >= 3

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_design_lesson_knowledge_points_structure(self):
        """Knowledge points should have required fields."""
        result = await design_lesson("Python loops")
        data = json.loads(result)

        for kp in data["knowledge_points"]:
            assert "title" in kp
            assert "summary" in kp
            assert "difficulty" in kp
            assert "key_concepts" in kp
            assert isinstance(kp["key_concepts"], list)
            assert "exercises" in kp
            assert isinstance(kp["exercises"], list)


@pytest.mark.asyncio
class TestPageGeneration:
    """Test interactive page generation."""

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_generate_page_basic(self):
        """Should generate a valid HTML page."""
        result = await generate_page(
            title="Python Variables",
            summary="Learn about storing and using data in Python",
            difficulty="beginner"
        )
        assert isinstance(result, str)
        assert "<!doctype html" in result.lower() or "<html" in result.lower()

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_generate_page_html_structure(self):
        """Generated HTML should have required elements."""
        result = await generate_page(
            title="Data Types",
            summary="Understanding different data types",
            difficulty="intermediate"
        )

        result_lower = result.lower()
        assert "<html" in result_lower
        assert "<head" in result_lower
        assert "<body" in result_lower
        assert "</html>" in result_lower

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_generate_page_responsive(self):
        """Generated HTML should be responsive."""
        result = await generate_page(
            title="Functions",
            summary="Creating reusable code blocks",
            difficulty="intermediate"
        )

        result_lower = result.lower()
        # Should have viewport meta tag
        assert "viewport" in result_lower


@pytest.mark.asyncio
class TestTutorChat:
    """Test Socratic tutoring chat."""

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_tutor_chat_basic(self):
        """Should respond to student questions."""
        result = await tutor_chat(question="How do I create a variable in Python?")
        assert isinstance(result, str)
        assert len(result) > 0
        # Should not give direct answer, but guide student
        assert "?" in result or "think" in result.lower()

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_tutor_chat_with_context(self):
        """Should use provided context."""
        result = await tutor_chat(
            question="How do I use this?",
            context="We're learning about for loops"
        )
        assert isinstance(result, str)
        assert len(result) > 0

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_tutor_chat_with_history(self):
        """Should incorporate chat history."""
        history = json.dumps([
            {"role": "user", "content": "What is a loop?"},
            {"role": "assistant", "content": "A loop repeats code..."}
        ])
        result = await tutor_chat(
            question="Can I nest loops?",
            history=history
        )
        assert isinstance(result, str)
        assert len(result) > 0


@pytest.mark.asyncio
class TestExerciseHints:
    """Test exercise hint generation."""

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_get_hint_known_exercise(self):
        """Should provide hint for known exercise."""
        result = await get_exercise_hint(exercise_id="var_01")
        assert isinstance(result, str)
        assert len(result) > 0
        # Should not contain the solution directly
        assert "Alice" not in result  # Solution contains "Alice"

    @pytest.mark.skip(reason="Requires Ollama running")
    async def test_get_hint_with_attempt(self):
        """Should analyze student attempt and give targeted hint."""
        result = await get_exercise_hint(
            exercise_id="var_01",
            attempt="name = Alice"  # Missing quotes
        )
        assert isinstance(result, str)
        assert len(result) > 0

    def test_get_hint_unknown_exercise(self):
        """Should handle unknown exercise gracefully."""
        result = asyncio.run(get_exercise_hint(
            exercise_id="nonexistent_99"
        ))
        assert "not found" in result.lower() or "unknown" in result.lower()


class TestIntegration:
    """Integration tests for the full workflow."""

    def test_full_workflow_setup(self):
        """System should initialize properly."""
        exercises = load_exercises()
        assert len(exercises) > 200  # Should have substantial exercise set

        # Should be able to find exercises about different topics
        variables = search_exercises(["variable"], limit=10)
        functions = search_exercises(["function"], limit=10)

        assert len(variables) > 0
        assert len(functions) > 0


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
