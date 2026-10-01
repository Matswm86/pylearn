package no.mwmai.pyquest.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.onGloballyPositioned
import androidx.compose.ui.layout.positionInWindow
import androidx.compose.ui.unit.dp
import no.mwmai.pyquest.model.Block
import no.mwmai.pyquest.model.BlockKind
import no.mwmai.pyquest.model.Question
import no.mwmai.pyquest.ui.theme.CodeStyle
import no.mwmai.pyquest.ui.theme.Pal

/**
 * Match every row to one option: the exam's drag-into-box item.
 *
 * Each row has one box. Tapping an option fills the selected box, or the first
 * empty one when none is selected; long-pressing an option drags it onto any
 * box. Options are never used up, because one answer can fit several rows.
 * Tapping a filled box empties it.
 */
@OptIn(ExperimentalLayoutApi::class)
@Composable
fun MatchAnswer(
    question: Question,
    placed: List<String?>,
    onPlacedChange: (List<String?>) -> Unit,
    enabled: Boolean,
    checked: Boolean,
    modifier: Modifier = Modifier,
) {
    val state = rememberSlotDragState()
    val slotCount = question.slotCount
    val pool = question.options.map { Block(id = it, code = it, kind = BlockKind.VAR) }
    var active by remember(question.id) { mutableStateOf<Int?>(null) }

    fun place(slot: Int, option: String) {
        onPlacedChange(placed.toMutableList().also { it[slot] = option })
        active = placed.indices.firstOrNull { it != slot && placed[it] == null }
    }

    fun clear(slot: Int) {
        onPlacedChange(placed.toMutableList().also { it[slot] = null })
        active = slot
    }

    Box(modifier = modifier.onGloballyPositioned { state.parentOrigin = it.positionInWindow() }) {
        Column(modifier = Modifier.fillMaxWidth()) {
            question.rows.forEachIndexed { index, row ->
                val filled = placed.getOrNull(index)
                val verdict = when {
                    !checked -> SlotVerdict.NONE
                    filled == question.answer.getOrNull(index) -> SlotVerdict.RIGHT
                    else -> SlotVerdict.WRONG
                }
                Column(
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(bottom = 10.dp)
                        .background(Pal.Ground, RoundedCornerShape(14.dp))
                        .border(
                            1.5.dp,
                            if (active == index && enabled) Pal.Lime else Pal.Edge,
                            RoundedCornerShape(14.dp),
                        )
                        .clickable(enabled = enabled) { active = index }
                        .padding(12.dp),
                    verticalArrangement = Arrangement.spacedBy(8.dp),
                ) {
                    Text(
                        text = row,
                        style = if (question.mono) CodeStyle else MaterialTheme.typography.bodyMedium,
                        color = Pal.Text,
                    )
                    DropSlot(
                        index = index,
                        state = state,
                        filled = filled?.let { Block(id = it, code = it, kind = BlockKind.VAR) },
                        plainLabels = false,
                        enabled = enabled,
                        hint = "drop answer here",
                        onClear = { clear(index) },
                        verdict = verdict,
                    )
                    if (verdict == SlotVerdict.WRONG) {
                        Text(
                            text = "Answer: ${question.answer.getOrNull(index).orEmpty()}",
                            style = MaterialTheme.typography.bodySmall,
                            color = Pal.Good,
                        )
                    }
                }
            }

            Spacer(Modifier.height(8.dp))
            Row(
                verticalAlignment = Alignment.CenterVertically,
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                Text("ANSWERS", style = MaterialTheme.typography.labelMedium, color = Pal.Faint)
                Text(
                    "tap a box, then an answer; each answer can be used more than once",
                    style = MaterialTheme.typography.bodySmall,
                    color = Pal.Locked,
                )
            }
            Spacer(Modifier.height(10.dp))

            FlowRow(
                horizontalArrangement = Arrangement.spacedBy(8.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp),
                modifier = Modifier.fillMaxWidth(),
            ) {
                pool.forEach { block ->
                    TrayBlock(
                        block = block,
                        plainLabels = false,
                        enabled = enabled,
                        state = state,
                        slotCount = slotCount,
                        onTap = {
                            val slot = active?.takeIf { it < slotCount }
                                ?: placed.indexOfFirst { it == null }.takeIf { it >= 0 }
                            if (slot != null) place(slot, block.id)
                        },
                        onDroppedOn = { slot -> place(slot, block.id) },
                    )
                }
            }
        }

        DragOverlay(
            state = state,
            block = state.draggingId?.let { id -> pool.firstOrNull { it.id == id } },
            plainLabels = false,
        )
    }
}
