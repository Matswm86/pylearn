package no.mwmai.pyquest.ui.theme

import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.graphics.Color

/**
 * Pytor light tokens, matching the Pytor site (docs/style.css). Light is the
 * default; a later opt-in dark mode should use the site's dark tokens, not an
 * inversion of these. Blue means "tap this", green means "you were right", and
 * there is no violet anywhere.
 */
object Pal {
    val Ground = Color(0xFFE9EDF2) // inset wells (site --surface-alt)
    val Screen = Color(0xFFF3F5F8) // page (site --bg)
    val Card = Color(0xFFFFFFFF) // site --surface
    val CardOpen = Color(0xFFEEF3FD) // site --primary-bg
    val Chip = Color(0xFFE9EDF2)
    val ChipDim = Color(0xFFF3F5F8)

    // "Lime" keeps its name for now; it is Pytor blue. Rename to Primary in a later pass.
    val Lime = Color(0xFF2F64C8) // site --primary
    val LimeSoft = Color(0xFFDCE6FA) // site --primary-light
    val LimeEdge = Color(0x592F64C8)
    val PrimaryInk = Color(0xFF234FA3) // blue text on LimeSoft (6.16:1)

    val OnAccent = Color(0xFFFFFFFF) // text and icons on Lime, Good, Coral fills

    val Good = Color(0xFF177A52) // correct answer (darkened site --success for 4.5:1)
    val GoodSoft = Color(0xFFDBF3E8) // site --success-light
    val Coral = Color(0xFFC8382F) // site --error
    val CoralSoft = Color(0xFFFBE3E0) // site --error-light

    val Teal = Color(0xFF0E7C86) // tutor and capstone accent (site --accent)

    val Text = Color(0xFF16202E)
    val Muted = Color(0xFF4F5D70)
    val Faint = Color(0xFF5E6B7E) // darker than site --text-light, which fails on Screen
    val Locked = Color(0xFF8792A3) // disabled only, never body text
    val Hairline = Color(0xFFE3E8EE)
    val Edge = Color(0xFFD6DDE6) // site --border

    val CodeBg = Color(0xFF13202E) // site --code-bg
    val CodeFg = Color(0xFFDDE6F0) // site --code-fg
    val CodeHi = Color(0xFFF4C430) // Pytor yellow, for highlighted code

    // Block kinds, so a player learns to read "this slot wants an expression"
    // from colour before they can read it from syntax: blue = name,
    // amber = expression, teal = call.
    val VarFill = Color(0xFFEEF3FD)
    val VarEdge = Color(0xFF9DB7E8)
    val VarText = Color(0xFF234FA3)
    val ExprFill = Color(0xFFFFF3C4)
    val ExprEdge = Color(0xFFF0D77A)
    val ExprText = Color(0xFF6B4E00)
    val CallFill = Color(0xFFDCF1F2)
    val CallEdge = Color(0xFFA6D9DC)
    val CallText = Color(0xFF0A5A61)
}

private val PyQuestColors = lightColorScheme(
    primary = Pal.Lime,
    onPrimary = Pal.OnAccent,
    secondary = Pal.Teal,
    onSecondary = Pal.OnAccent,
    background = Pal.Screen,
    onBackground = Pal.Text,
    surface = Pal.Card,
    onSurface = Pal.Text,
    surfaceVariant = Pal.Chip,
    onSurfaceVariant = Pal.Faint,
    outline = Pal.Edge,
    error = Pal.Coral,
    onError = Pal.OnAccent,
)

/** True while the player is answering, so shared widgets can dim themselves. */
val LocalAnswering = staticCompositionLocalOf { true }

@Composable
fun PyQuestTheme(content: @Composable () -> Unit) {
    CompositionLocalProvider(LocalAnswering provides true) {
        MaterialTheme(
            colorScheme = PyQuestColors,
            typography = PyQuestTypography,
            content = content,
        )
    }
}
