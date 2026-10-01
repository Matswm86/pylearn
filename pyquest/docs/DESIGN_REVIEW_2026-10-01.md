# PyQuest visual design review, 2026-10-01

**Verdict: PyQuest still wears the old "lime on near-black" look and does not match the repainted Pytor site.** It is dark only, uses a violet accent in three places, uses Archivo instead of Atkinson Hyperlegible Next, and its launcher icon is a placeholder lime "S". Every UI colour flows through one Kotlin object (`Pal`), so the fix is one pass: about 3 theme files, 2 XML files, 1 icon, and 10 one-line edits.

Read-only review. No app code was changed. New art is in `docs/design/`.

---

## 1. Current facts, with evidence

### Palette (all in `app/src/main/java/no/mwmai/pyquest/ui/theme/Theme.kt`)
| Token | Hex | Line | Role today |
|---|---|---|---|
| Ground | `#07090C` | 16 | inset wells, code panels, nav bar |
| Screen | `#0C0F14` | 17 | page background **and** text on lime (see below) |
| Card / CardOpen | `#11161D` / `#151C25` | 18-19 | cards |
| Chip / ChipDim | `#1D242E` / `#171E27` | 20-21 | chips, tracks |
| Lime | `#B8F04A` | 23 | primary accent **and** "correct answer" colour (54 uses) |
| LimeSoft / LimeEdge | `#B8F04A` at 14 % / 35 % | 24-25 | soft fills, borders |
| Coral / CoralSoft | `#FF6B5A` / 15 % | 26-27 | wrong, error |
| **Violet** | **`#A98BFF`** | **28** | `secondary`, capstone tag |
| Text / Muted / Faint / Locked | `#ECEFF4` / `#98A2B2` / `#8B95A5` / `#5D6675` | 30-33 | text |
| Hairline / Edge | white 7 % / 9 % | 34-35 | borders |
| Var block | `#6AA9FF` fill/edge, `#8FC0FF` text | 39-41 | name blocks |
| Expr block | `#FFB84D` fill/edge, `#FFC876` text | 42-44 | expression blocks |
| **Call block** | **`#A98BFF` fill/edge, `#BFA7FF` text** | **45-47** | call blocks |

- The scheme is `darkColorScheme(...)` (Theme.kt:50) with `secondary = Pal.Violet` (Theme.kt:53). The comment at Theme.kt:11-13 states "The app is dark only".
- No hard-coded colours outside `Pal`: the only non-token colour in `ui/` is `Color.Transparent`. That makes a token swap safe.
- XML colours: `res/values/colors.xml:3-4` (`pytor_lime #B8F04A`, `pytor_ink #0C0F14`). `res/values/themes.xml:3-6` uses parent `android:Theme.Material.NoActionBar` (dark platform theme), with status bar, nav bar and window background all `#0C0F14`.
- `MainActivity.kt:59` calls `enableEdgeToEdge()` with defaults, so status-bar icon colour follows the phone's dark-mode setting, not the app's.

### Purple / violet found
1. `Theme.kt:28` `Violet = #A98BFF` (hue 255), used as `secondary` (Theme.kt:53) and as the capstone tier tag (`ui/TrackScreen.kt:202`).
2. `Theme.kt:45-47` Call blocks `#A98BFF` / `#BFA7FF`, used in `ui/SlotBoard.kt:100`. Also documented as "violet for a call" in `model/Question.kt:160` and `DESIGN.md:91-92`.
3. Borderline: the avatar `res/drawable/pytor.webp` (used at `ui/PytorWidgets.kt:52`) is the opaque mascot render on a periwinkle backdrop, sampled `#6E80E5` / `#4E63E2` (hue 231). Next to navy and slate it reads as blue-violet. The site stopped using it and shows `pytor-cut.webp` (transparent) on navy instead (`docs/index.html:27`, `style.css:124`).

### Type (`ui/theme/Type.kt`)
- UI: Archivo variable (`res/font/archivo_variable.ttf`, Type.kt:22-27, 37-43). Code: JetBrains Mono variable (`res/font/jetbrains_mono_variable.ttf`, Type.kt:30-35). Licences in `licenses/Archivo-OFL.txt` and `licenses/JetBrainsMono-OFL.txt`.
- Headlines are ExtraBold 30 sp and Bold 25 sp with negative tracking -0.5 / -0.4 sp (Type.kt:58-61, 65-68). Body is 16/14/12 sp. Section captions use mono uppercase at 11 sp and 10 sp with +1.2 / +1.0 sp tracking (Type.kt:114-127).

### Icon
- `res/drawable/ic_launcher_foreground.xml:2` says it is "A coiled snake glyph standing in for Pytor until the real art is exported". It is a single lime path, `#B8F04A` (line 9), on `@color/pytor_ink` `#0C0F14` (`mipmap-anydpi-v26/ic_launcher.xml:3`).
- No `<monochrome>` layer, so Android 13+ themed icons fall back to a generic tinted square.
- No store art exists (no `store/` folder, no 512 icon, no feature graphic).

### Spec gap
`pyquest/DESIGN.md` is a game-design doc (rules, tiers, tech). There is no visual spec. This review's token table (section 3) should become that spec.

---

## 2. Mismatches against the Pytor site (`docs/style.css`)

| Area | Pytor site | PyQuest | Gap |
|---|---|---|---|
| Mode | Light by default (`color-scheme: light`, style.css:17), dark is opt-in | Dark only | Breaks the owner's "light by default" rule |
| Page / surface | `#F3F5F8` / `#FFFFFF` / `#E9EDF2` | `#0C0F14` / `#11161D` / `#1D242E` | Different world |
| Text | `#16202E`, dim `#4F5D70` | `#ECEFF4`, `#98A2B2` | Inverted |
| Primary | Pytor blue `#2F64C8` | Lime `#B8F04A` | Lime does not exist on the site |
| Tutor accent | Teal `#0E7C86` | none (violet used as secondary) | Violet is banned |
| Correct / wrong | `#1C8A5E` green / `#C8382F` red | Lime / Coral `#FF6B5A` | Lime is both "primary" and "correct", which is ambiguous |
| Brand stage | Navy `#17365C` / `#102742` | Near-black `#07090C` | |
| Code panels | Dark navy `#13202E`, fg `#DDE6F0` | `#07090C` with lime or white text | Close in spirit; adopt the site hex |
| UI font | Atkinson Hyperlegible Next (OFL) | Archivo | Different voice; Atkinson is the "plain readable type" choice |
| Mono | JetBrains Mono | JetBrains Mono | Already matches |
| Mascot | `pytor-cut.webp` on navy | `pytor.webp` on periwinkle | See purple item 3 |
| Icon | Mascot | Lime "S" placeholder | Not recognisably Pytor |

---

## 3. Change list (one pass, in priority order)

### P1. Replace the `Pal` values with Pytor light tokens (`ui/theme/Theme.kt`)
Keep the token **names**, so the roughly 300 call sites keep compiling and change colour together. Add three new tokens: `OnAccent`, `Good` / `GoodSoft`, and `Code*`.

```kotlin
object Pal {
    val Ground   = Color(0xFFE9EDF2)  // inset wells (site --surface-alt)
    val Screen   = Color(0xFFF3F5F8)  // page (site --bg)
    val Card     = Color(0xFFFFFFFF)  // site --surface
    val CardOpen = Color(0xFFEEF3FD)  // site --primary-bg
    val Chip     = Color(0xFFE9EDF2)
    val ChipDim  = Color(0xFFF3F5F8)

    // "Lime" keeps its name for now; it is Pytor blue. Rename to Primary in a later pass.
    val Lime     = Color(0xFF2F64C8)  // site --primary
    val LimeSoft = Color(0xFFDCE6FA)  // site --primary-light
    val LimeEdge = Color(0x592F64C8)
    val PrimaryInk = Color(0xFF234FA3) // blue text on LimeSoft (6.16:1)

    val OnAccent = Color(0xFFFFFFFF)  // NEW: text/icons on Lime, Good, Coral fills

    val Good     = Color(0xFF177A52)  // NEW: correct answer (darkened site --success for 4.5:1)
    val GoodSoft = Color(0xFFDBF3E8)  // site --success-light
    val Coral    = Color(0xFFC8382F)  // site --error
    val CoralSoft= Color(0xFFFBE3E0)  // site --error-light

    val Teal     = Color(0xFF0E7C86)  // NEW, replaces Violet: tutor/capstone (site --accent)

    val Text     = Color(0xFF16202E)
    val Muted    = Color(0xFF4F5D70)
    val Faint    = Color(0xFF5E6B7E)  // darker than site --text-light #6B788A, which fails on #F3F5F8
    val Locked   = Color(0xFF8792A3)  // disabled only, never body text
    val Hairline = Color(0xFFE3E8EE)
    val Edge     = Color(0xFFD6DDE6)  // site --border

    val CodeBg   = Color(0xFF13202E)  // NEW, site --code-bg
    val CodeFg   = Color(0xFFDDE6F0)  // NEW, site --code-fg
    val CodeHi   = Color(0xFFF4C430)  // NEW, Pytor yellow, replaces lime-coloured code

    // Block kinds: blue = name, amber = expression, TEAL = call (was violet).
    val VarFill  = Color(0xFFEEF3FD); val VarEdge  = Color(0xFF9DB7E8); val VarText  = Color(0xFF234FA3)
    val ExprFill = Color(0xFFFFF3C4); val ExprEdge = Color(0xFFF0D77A); val ExprText = Color(0xFF6B4E00)
    val CallFill = Color(0xFFDCF1F2); val CallEdge = Color(0xFFA6D9DC); val CallText = Color(0xFF0A5A61)
}
```
Delete `Violet`. Switch to `lightColorScheme(primary = Pal.Lime, onPrimary = Pal.OnAccent, secondary = Pal.Teal, onSecondary = Pal.OnAccent, background = Pal.Screen, onBackground = Pal.Text, surface = Pal.Card, onSurface = Pal.Text, surfaceVariant = Pal.Chip, onSurfaceVariant = Pal.Faint, outline = Pal.Edge, error = Pal.Coral, onError = Pal.OnAccent)`. Update the class comment at Theme.kt:10-14.

### P2. Fix the roles the token swap alone gets wrong (10 one-line edits)
`Pal.Screen` is used as **text on a lime fill**. After P1 it would be light grey on blue. Change these to `Pal.OnAccent`:
`ui/MultiAnswer.kt:97`, `ui/McqAnswer.kt:103`, `ui/PytorWidgets.kt:107` and `:151`, `ui/TrackScreen.kt:187`, `:283` and `:305` (keep `.copy(alpha = 0.7f)`), `ui/PytorScreen.kt:321` and `:381`, `ui/StatsScreen.kt:337`.

"Correct" should be green, not the primary blue. Change `Pal.Lime` / `Pal.LimeSoft` to `Pal.Good` / `Pal.GoodSoft` at:
`ui/McqAnswer.kt:66, 72, 77, 95` (the `right` branches only), `ui/MultiAnswer.kt:58, 63, 68` (the `right` branches), `ui/QuestionScreen.kt:273, 277`, `ui/PytorSheet.kt:164`.

Violet removal: `ui/TrackScreen.kt:202` becomes `tier.capstone -> Pal.Teal`. `ui/SlotBoard.kt:100` needs no change (the Call tokens become teal). Edit the comment at `model/Question.kt:160` and the text at `DESIGN.md:91` from "violet" to "teal".

Code panels: `ui/PytorWidgets.kt:165-166` (`CodeBlock`) uses `Pal.CodeBg` with no border, and the default `color` at :161 becomes `Pal.CodeFg`. Callers passing `color = Pal.Lime` (`ui/LevelClearedScreen.kt:124`, inline code at `ui/PytorWidgets.kt:215`) switch to `Pal.CodeHi` / `Pal.PrimaryInk` on `Pal.Chip`. Leave the fill-in-the-blank board (`ui/FillAnswer.kt:74`) light, so the light block chips stay readable.

Blue text on a soft blue fill: `ui/TrackScreen.kt:283`, `state.cleared` branch, uses `Pal.PrimaryInk` instead of `Pal.Lime` (4.43 becomes 6.16:1).

### P3. Bundle Atkinson Hyperlegible Next (`ui/theme/Type.kt`, `res/font/`)
Android font resources need TTF, not the site's woff2 subsets. Take the variable TTFs from Google Fonts (OFL, wght 200-800):
- `https://github.com/google/fonts/raw/main/ofl/atkinsonhyperlegiblenext/AtkinsonHyperlegibleNext[wght].ttf` (114,552 bytes) saved as `res/font/atkinson_next_variable.ttf`
- optional italic: `AtkinsonHyperlegibleNext-Italic[wght].ttf` (123,916 bytes) saved as `res/font/atkinson_next_italic_variable.ttf`
- licence: copy `OFL.txt` from the same folder to `licenses/AtkinsonHyperlegibleNext-OFL.txt`. Delete `res/font/archivo_variable.ttf` and `licenses/Archivo-OFL.txt`.

In Type.kt, rename `archivo()` / `Archivo` to `atkinson()` / `Atkinson` with `R.font.atkinson_next_variable` (ExtraBold 800 is inside the axis). Set headline `letterSpacing` to `0.sp` (Type.kt:61, 68): Atkinson is designed for normal spacing, and negative tracking undoes its legibility. Raise `bodySmall` from 12 to 13 sp and `labelSmall` from 10 to 11 sp, because those carry real text (the "· marks one space" caption, the level chips). JetBrains Mono stays as it is.

### P4. Light window and system bars (`res/values/themes.xml`, `res/values/colors.xml`, `MainActivity.kt`)
- themes.xml: parent `android:Theme.Material.Light.NoActionBar`. Set `statusBarColor`, `navigationBarColor` and `windowBackground` to `#F3F5F8`, and add `<item name="android:windowLightStatusBar">true</item>` (API 23, covered by minSdk 26). Put `<item name="android:windowLightNavigationBar">true</item>` in `values-v27/themes.xml`, because it needs API 27. This removes the black flash at launch.
- `MainActivity.kt:59`: `enableEdgeToEdge(statusBarStyle = SystemBarStyle.light(Color.TRANSPARENT, Color.TRANSPARENT), navigationBarStyle = SystemBarStyle.light(Color.TRANSPARENT, Color.TRANSPARENT))`. Without this, a phone in system dark mode draws white status icons on the light page, and they disappear.
- colors.xml: replace both entries with `<color name="pytor_navy">#17365C</color>` (icon background) and `<color name="pytor_screen">#F3F5F8</color>`.

### P5. New launcher icon and avatar (`res/drawable/`, `res/mipmap-anydpi-v26/`)
- Convert `docs/design/ic_launcher_foreground.svg` to `res/drawable/ic_launcher_foreground.xml` with Android Studio's Vector Asset import (it uses only ellipse, circle, path and one group transform, all of which convert cleanly).
- `ic_launcher.xml` and `ic_launcher_round.xml`: background `@color/pytor_navy`. Add `<monochrome android:drawable="@drawable/ic_launcher_foreground"/>` for Android 13 themed icons.
- Avatar: replace `res/drawable/pytor.webp` with the site's `docs/pytor-cut.webp` (transparent). In `PytorAvatar` (`ui/PytorWidgets.kt:50-59`), add `.background(Color(0xFF17365C), CircleShape)` before the image, the same as the site's `.logo { background: var(--peri) }`. Change the border to `Pal.Edge`.

### Not in this pass
- A dark theme. Light is the default. A later opt-in dark mode should use the site's dark tokens (style.css:69-83), not the old lime set.
- Renaming `Lime*` to `Primary*`. It is mechanical, but it touches every file; do it as its own commit.

---

## 4. Icon and store art

- **Launcher icon: redo (done here).** The current one is a self-declared placeholder. Lime on black matches nothing in the Pytor brand.
- New foreground: `docs/design/ic_launcher_foreground.svg`. It is a flat Pytor (blue coils with a yellow belly, raised neck, yellow head, round glasses) on a 108-unit grid, with all art inside the 66-unit safe circle. Background is navy `#17365C`. Rendered and checked at 432 px, at 192 px in a round mask, and at 48 px in round and squircle masks: it reads as a snake in glasses at 48 px.
- **Play icon: drafted.** `docs/design/play_icon_512.png` is 512x512 RGBA, 19 KB, the same art full-bleed on navy (checklist: at most 1 MB, PNG with alpha).
- **Feature graphic and screenshots: not yet.** The checklist requires screenshots from the real app, so they must wait until P1-P4 ship. Then build the 1024x500 feature graphic from `pytor-cut.webp` on navy plus one real question-screen capture. Do not use a plain dark background.

---

## 5. Contrast (WCAG 2.x, my calc)

| Pair | Ratio |
|---|---|
| Text `#16202E` on Screen `#F3F5F8` / Card `#FFFFFF` | 15.02 / 16.40 |
| Muted `#4F5D70` on Card / Screen | 6.70 / 6.14 |
| Faint `#5E6B7E` on Card / Screen / Chip | 5.41 / 4.96 / 4.60 |
| (rejected) site `#6B788A` on Screen / Chip | 4.11 / 3.82 (fails) |
| Primary `#2F64C8` text on Card / Screen | 5.56 / 5.09 |
| PrimaryInk `#234FA3` on LimeSoft `#DCE6FA` | 6.16 |
| White on Primary `#2F64C8` | 5.56 |
| Good `#177A52`: white on it / as text on Screen | 5.33 / 4.88 |
| Coral `#C8382F`: on Card / white on it | 5.17 / 5.17 |
| Teal `#0E7C86` on Card | 4.95 |
| Block text: Var / Expr / Call on own fill | 6.94 / 6.95 / 6.76 |
| CodeFg / CodeHi on CodeBg `#13202E` | 13.07 / 10.04 |
| Locked `#8792A3` on Card (disabled only) | 3.15 |
| Icon: blue `#3AA6DC` / yellow `#F4C430` on navy `#17365C` | 4.46 / 7.44 |

---

## The one rule the builder must not change
**No violet anywhere, and "correct" is green `#177A52`, never the primary blue.** Blue means "tap this", green means "you were right". Merging them again (as Lime did) brings back the ambiguity this review removes.
