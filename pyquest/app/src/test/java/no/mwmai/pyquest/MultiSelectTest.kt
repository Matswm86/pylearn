package no.mwmai.pyquest

import kotlinx.serialization.json.Json
import no.mwmai.pyquest.model.Question
import no.mwmai.pyquest.model.QuestionType
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * Select-N grading: the picks are a set, so tap order must not matter, and a
 * partial or padded pick must never pass.
 */
class MultiSelectTest {

    private val question = Json { ignoreUnknownKeys = true }.decodeFromString(
        Question.serializer(),
        """
        {"id": "t9.l1.q99", "tier": 9, "level": 1, "type": "multi",
         "prompt": "Which two are Responsible AI principles?",
         "options": ["Fairness", "Speed", "Transparency", "Cost"],
         "answer": ["Fairness", "Transparency"],
         "explain": "Fairness and transparency are two of the six principles."}
        """.trimIndent(),
    )

    @Test
    fun `multi decodes from the curriculum type name`() {
        assertEquals(QuestionType.MULTI, question.type)
        assertEquals(question.options, question.choices)
    }

    @Test
    fun `tap order does not matter`() {
        assertTrue(question.isCorrect(listOf("Fairness", "Transparency")))
        assertTrue(question.isCorrect(listOf("Transparency", "Fairness")))
    }

    @Test
    fun `partial, wrong, and duplicated picks fail`() {
        assertFalse(question.isCorrect(listOf("Fairness")))
        assertFalse(question.isCorrect(listOf("Fairness", "Speed")))
        assertFalse(question.isCorrect(listOf("Fairness", "Transparency", "Cost")))
        assertFalse(question.isCorrect(listOf("Fairness", "Fairness")))
    }
}
