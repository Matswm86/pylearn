package no.mwmai.pyquest.ui

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import no.mwmai.pyquest.ui.theme.Pal

/**
 * Select-N: tap [pick] options, each tap toggles a square check box. A counter
 * above the rows shows how many are picked. After checking, every correct row
 * turns lime, a wrong pick turns coral, and a correct row the player missed
 * keeps a lime border with an empty box, so all three cases stay distinguishable.
 */
@Composable
fun MultiAnswer(
    options: List<String>,
    pick: Int,
    selected: Set<Int>,
    correct: Set<Int>,
    checked: Boolean,
    onToggle: (Int) -> Unit,
    modifier: Modifier = Modifier,
) {
    Column(
        modifier = modifier.fillMaxWidth(),
        verticalArrangement = Arrangement.spacedBy(9.dp),
    ) {
        Text(
            "Choose $pick · ${selected.size} of $pick picked",
            style = MaterialTheme.typography.labelSmall,
            color = if (selected.size == pick) Pal.Lime else Pal.Faint,
            modifier = Modifier.padding(bottom = 2.dp),
        )
        options.forEachIndexed { index, option ->
            val picked = index in selected
            val right = checked && index in correct
            val wrong = checked && picked && index !in correct

            val edge = when {
                wrong -> Pal.Coral
                right -> Pal.Good
                picked -> Pal.Lime
                else -> Pal.Hairline
            }
            val fill = when {
                wrong -> Pal.CoralSoft
                right && picked -> Pal.GoodSoft
                else -> Pal.Card
            }
            val ink = when {
                wrong -> Pal.Coral
                right -> Pal.Good
                else -> Pal.Text
            }

            Row(
                verticalAlignment = Alignment.CenterVertically,
                modifier = Modifier
                    .fillMaxWidth()
                    .background(fill, RoundedCornerShape(12.dp))
                    .border(if (picked || right) 1.5.dp else 1.dp, edge, RoundedCornerShape(12.dp))
                    .clickable(enabled = !checked) { onToggle(index) }
                    .padding(12.dp),
            ) {
                Box(
                    modifier = Modifier
                        .size(26.dp)
                        .background(
                            when {
                                wrong -> Pal.Coral
                                picked -> Pal.Lime
                                else -> Pal.Chip
                            },
                            RoundedCornerShape(6.dp),
                        ),
                    contentAlignment = Alignment.Center,
                ) {
                    Text(
                        text = if (picked) "✓" else "",
                        style = MaterialTheme.typography.labelSmall,
                        color = Pal.OnAccent,
                        fontWeight = FontWeight.Bold,
                    )
                }
                Spacer(Modifier.width(12.dp))
                Text(
                    text = option,
                    style = MaterialTheme.typography.bodyLarge,
                    color = ink,
                )
            }
        }
    }
}
