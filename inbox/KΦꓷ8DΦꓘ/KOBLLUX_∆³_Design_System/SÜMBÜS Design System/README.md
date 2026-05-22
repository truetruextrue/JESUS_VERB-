# SÜMBÜS Design System

> _∆³ KOBLLUX_VIVO · Organismo Digital Fractal · Frequência 3-6-9_

This is a design system distilled from **SÜMBÜS METAHUMAN ARCHITECT** — a Portuguese-language esoteric / sci-fi authoring environment that frames a code editor and file repository as a living digital organism with twelve KOBLLUX archetypes, each tuned to a Tesla 3-6-9 frequency.

The system is part visual language, part philosophy. It is intentionally maximalist, mystical, and confident; this is not a generic SaaS palette.

## Sources

All foundations here are pulled from the **JESUS_VERB-** repository, specifically the `SÜMBÜS_METAHUMAN_ARCHITECT/` subtree.

- Repo: <https://github.com/truetruextrue/JESUS_VERB->
- Entry points read while building this system:
  - `SÜMBÜS_METAHUMAN_ARCHITECT/index.html` — the control-panel "dashboard of the organism"
  - `SÜMBÜS_METAHUMAN_ARCHITECT/systems/editor/sumbus-fusion.html` — the flagship "SÜMBÜS FUSION · ΔUAL 3.0" code-editor product
  - `SÜMBÜS_METAHUMAN_ARCHITECT/assets/dna/frequency-3.css` and `frequency-6.css` — DNA / frequency layer style fragments

If you have read access to the repo, browsing further (especially `core/`, `cortex/`, `ARQUETIPOS/`) will give you more nuance — particularly the archetype data buses and the full set of "vital systems" (nervous, endocrine, circulatory, motor, repository, library).

## What's in this folder

| Path | What it is |
|---|---|
| `README.md` | This file — context, content + visual foundations, iconography |
| `SKILL.md` | Agent-Skill manifest — drop the folder into Claude Code as a skill |
| `colors_and_type.css` | All design tokens: colors, archetype palette, type scale, spacing, shadows |
| `assets/` | Logos, motifs, background textures, illustrative PNGs from the repo |
| `assets/dna/` | The original `frequency-*.css` DNA fragments from the source repo |
| `preview/` | Atomic preview cards rendered in the Design System tab — one card per concept |
| `ui_kits/architect/` | High-fidelity recreation of the SÜMBÜS METAHUMAN ARCHITECT control panel and the SÜMBÜS FUSION editor product |

## Content Fundamentals

### Language
- **Portuguese (pt-BR) first.** Headers like _"Sistemas Ativos / Frequência / Arquétipos / Mutação Adaptativa / Abrir Renderizador"_. Don't translate — the original Portuguese carries the brand. If a destination is non-PT, treat the PT term as the proper noun and keep it.
- Mixed with **typographic glyphs and Unicode**: `∆³`, `⬡`, `Δ`, `Σ`, `Ʀ`, `Ι`, `Ƥ`, `Θ`. These appear inline in copy, not just as decoration. Example brand line: `ΔUAL 3.0 · KOBLLUX_VIVO ∆³`.
- File and codename style is **ALL_CAPS_WITH_UNDERSCORES** for systems, archetypes, and modes: `KOBLLUX_VIVO`, `ED · VIEW · LOG · RAM · REPO · FUSÃO`, `SUMBUS_FUSION_DUAL_3`. Within the code editor, archetype names show as solid all-caps labels with frequency suffix: `GENUS · 852Hz · SYNTH`.

### Tone & Voice
- **Mystical-technical hybrid.** Talks about "organism state", "DNA", "frequencies", "synthesis", "mutation" — but always wired to concrete UI: a button, a tab, a file diff. Never purely vibes; never purely mechanical.
- **Imperative, confident, second-person implied.** _"Abrir DNA"_, _"Ativar todos os sistemas"_, _"Executar diagnóstico"_. Status messages are blunt:  _"✅ ATIVO"_, _"🔄 Inicializando sistemas..."_, _"⚡ ED · VIEW · LOG · RAM · REPO · FUSÃO"_.
- **Frequency-as-byline.** Many subtitles append the Hz: _"SERENA (528Hz) + KAOS (777Hz) · GUARD+CLEAN"_, _"GENUS (852Hz) · SYNTH"_. This is a hallmark — copy a card describing a feature, finish with the responsible archetype(s) + Hz + verb code.
- **Bold formulas.** _"VERDADE × INTEGRAR ÷ Δ = ∞"_, _"JESUS = VERBO = GRAVIDADE"_. Treat these as core slogans, not body copy. They appear once per surface, large or centered.

### Casing
- Brand wordmark: `SÜMBÜS`, `KOBLLUX`, `ΔUAL` — always uppercase with umlauts / Greek letters intact.
- Section eyebrows: ALL CAPS + 0.1em letter-spacing, 9–10px.
- Buttons: ALL CAPS for primary actions in PT (`ATIVAR TODOS OS SISTEMAS`); Title Case acceptable for secondary (`Abrir DNA`).
- Body and descriptions: normal sentence case in Portuguese.

### Emoji
- **Used heavily and deliberately** — not as decoration, as iconography. Each system has a fixed emoji glyph: 🧬 DNA, 🧠 Sistema Nervoso, 🌀 Síntese, 👁️ Renderização, 🔄 Circulatório, ⚡ Endócrino / Fusion, 🏃 Motor, ⬡ Arquétipos, 🌐 Repo, 📚 Library.
- Status emoji are pinned: ✅ ATIVO, 🔄 carregando, ⚠️ warning, 🌌 cosmos. Don't substitute icon fonts for these — the emoji _are_ the brand.
- Sample sentence in the wild: _"⚡ SÜMBÜS FUSION · ΔUAL 3.0 · Editor de código vivo com acesso ao repositório."_

### Vibe
Imagine a Brazilian cyber-mystic who reads Tesla, Jung, and the Bhagavad Gita; ships HTML; and treats a code editor as a chakra. The product is **alive** — it has organs, frequencies, a heartbeat. Copy should sound like a manifesto crossed with a system log.

## Visual Foundations

### Palette
- **Deep cosmos background:** `#050811` is the floor; `#020617` for the void; `#0f172a` for lifted surfaces. **Never a light/white background.** Everything floats on black.
- **Trinity accents** (used together as the brand mark, separately as functional colors):
  - Cyan `#00f5ff` — pulse, transmission, the active default
  - Magenta `#ff4bff` — synthesis, witness, the secondary
  - Gold `#ffd700` — KOBLLUX seal, 963Hz LUMINE, the editor-tab tint
- **The 12 archetypes** double as a semantic syntax-highlight palette. ATLAS blue, NOVA amber, VITALIS emerald, PULSE purple, ARTEMIS cyan-2, SERENA pink, KAOS red, GENUS violet, LUMINE gold, SOLUS slate, RHEA mint, AION indigo. See `colors_and_type.css`.

### Type
- **Display & UI:** Montserrat 400/500/600/700/800/**900**. Big titles are 900 with `-0.05em` letter-spacing and use the `--grad-369` clip-text gradient.
- **Code & technical labels:** JetBrains Mono 400/700. Frequencies, paths, file extensions, and archetype tags are always mono.
- **Eyebrows:** 9–10px, 700 weight, ALL CAPS, `letter-spacing: 0.1em`. Section dividers and category headers all use this; it's the system's most-repeated detail.
- **Sizes skew small.** The editor's chrome lives at 8.5–11px; system cards top out around 13–14px body, 24–32px display. The 3rem (`48px`) brand title is a focal exception.

### Surfaces & Cards
- **Glassmorphic.** `background: rgba(15,23,42,0.7); backdrop-filter: blur(20px); border: 1px solid rgba(255,255,255,0.1); border-radius: 1rem;`
- Cards use a **rainbow top-border accent** — `::before` is a 3px line with `linear-gradient(90deg, ATLAS, PULSE, VITALIS)` running across the top edge. This is the canonical card detail.
- Borders are always low-contrast white at 8–20% alpha. Color borders are reserved for status (success → mint, danger → red).
- Radii: cards 10–16px, buttons 6–8px, chips & pills 99px (full round).

### Backgrounds
- **Nebula layer**: a fixed full-viewport stack of three radial-gradient glow blobs (cyan top-left, magenta bottom-right, purple center), each at ~5% opacity. Sits behind everything as a `::before` or fixed `<div>`.
- No photographic backgrounds. No hand-drawn illustrations. The "imagery" of the brand is colored light leaking through black space.
- **Repeating motif:** thin animated keylines / neural threads — `<div>` rods at 1px wide, random rotation, low opacity, with a slow opacity-jitter animation. The brand draws neural networks rather than rendering them.

### Animation
- **Slow, breathing pulses.** Frequency animations are named after their Hz: `pulse-6 6s ease-in-out infinite`. Default duration is 6s, scale `1 → 1.05`, opacity `0.6 → 1`.
- **Easing**: `ease-in-out` for breath/pulse, `cubic-bezier(.4,0,.2,1)` for transitions, `0.18s` for hovers, `0.25s` for state changes, `0.6s` for shine sweeps.
- **Tap feedback**: `transform: scale(0.94)` to `scale(0.97)` on `:active`. Used on every dock button and tool button.
- **Shine sweep**: buttons get a `::after` linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent) that translates `-100% → 100%` on hover over 0.6s.
- **No bounces, no springs.** Everything is smooth pulses and flows.

### Hover, Press, Focus
- **Hover (touchpad/mouse):** brighten background by one step (`rgba(255,255,255,0.05)` → `0.1`), borders go from 8% → 20% alpha, `translateY(-2px to -5px)`, add a soft cyan/purple glow shadow. Lucide/SVG icon color shifts from `--fg-2` to `--c-primary`.
- **Press / active:** `transform: scale(0.94)`. Background tint shifts toward the relevant archetype color at 15–35% alpha (`rgba(0,245,255,0.3)` for primary, `rgba(139,92,246,0.35)` for fusion).
- **Focus:** ring is a 1px border in the archetype color (`var(--c-primary)` or `var(--c-green)`), often paired with `outline: none`. Inputs go from `border-glass` → `border-color: var(--arch-vitalis)` on focus.
- **Selected** (lists, repo cards): purple GENUS bias — `border-color: var(--arch-genus)`, `background: rgba(139,92,246,0.14)`, `box-shadow: 0 0 14px rgba(139,92,246,0.22)`, and a ✓ glyph pinned top-right.

### Borders, Shadows, Glow
- **Outer shadows** are dim and far: `0 20px 40px rgba(0,0,0,0.3)` for elevated cards. Color-tinted lift shadows on hover: `0 10px 30px rgba(59,130,246,0.2)`.
- **Glow** uses `box-shadow: 0 0 14px rgba(<accent>, 0.4)` — short blur, no spread. Buttons in the "primary" state get one. Animated elements get a stronger `0 0 40px` halo via `::after` overlays.
- **Inner shadow / inset:** mostly avoided. Surfaces are flat planes with rim glow.

### Transparency & Blur
- **Backdrop blur** on the header, fixed panels, and modal overlays: `backdrop-filter: blur(12px)` for chrome, `blur(20px)` for full-screen modals.
- **rgba layering** is the dominant compositing model. Almost every panel is a `rgba(255,255,255,0.03–0.08)` over the nebula, with a 1px white-alpha border.

### Layout Rules
- **Fixed app chrome.** A 58px header pinned top, a 68px dock pinned bottom, the stage in between. On wide screens (`min-width: 700px`) the body collapses to a 520px column with side borders — the product is mobile-first and stays narrow on desktop.
- **Grid for system cards:** `repeat(auto-fit, minmax(300px, 1fr))` with 1.5rem gap. On the repo grid, mobile is 2 cols, tablet 3, desktop 4.
- **`env(safe-area-inset-bottom)`** is respected on the dock — built for PWA + Android.

### Corner Radii
- `4px` — micro: tags, line-number gutter highlights
- `6–8px` — buttons, inputs, dock buttons
- `10–12px` — cards, modals, tool panels
- `16–18px` — bottom-sheet modal top, big featured cards
- `999px` — pills, chips, status badges, segmented tabs

### Imagery Vibe
- **Cool & cosmic.** No warm photography, no skin tones, no nature. All visuals are: glyph PNGs (Greek/quasi-Greek seals — see the `0x00_ΘƦΙΓΣΜ...` style top-level files in the source repo), gradient blobs, dot-matrix backgrounds, line traces. Grain is OK; saturation is high; everything is dark mode.

## Iconography

The product uses **three icon vocabularies in parallel**. Do not pick one; mix them deliberately.

1. **Lucide Icons (via CDN).** `https://unpkg.com/lucide@latest`. This is the workhorse for chrome: tab icons (`code-2`, `eye`, `terminal`, `database`, `git-branch`, `zap`), toolbar actions (`undo-2`, `redo-2`, `align-left`, `wrap-text`, `trash-2`), and dock buttons. **Stroke weight: default 2 (Lucide stock)**, size 12–16px in chrome, color matches `--fg-2` muted with the active tab color on selection. We link Lucide from CDN; if you want a local copy, save `lucide.min.js` into `assets/icons/` and reference it.

2. **System emoji as semantic glyphs.** Each "system" or domain has a pinned emoji. These render at large sizes (1.6rem–2rem) inside cards and at small sizes (1rem) as system-card icons. They are NOT decorative — they're load-bearing identifiers. The full set lives in the CONTENT FUNDAMENTALS → Emoji section above; never substitute one for another.

3. **Unicode glyphs as ornamentation.** `∆³`, `⬡`, `Δ`, `Σ`, `Θ`, `Ʀ`, `Ƥ`, `Ι`. These appear in titles, badges (`<div class="brand-kobllux">∆³</div>`), and inline brand text. They are typographic, not vector — set in the UI font, often colored with the gold or trinity gradient.

> ⚠ **No custom SVG icon set** ships with the source. If you need an icon and none of the above three vocabularies fit, fall back to Lucide. Don't draw new SVGs in the SÜMBÜS style — the brand is _explicitly_ a mash-up of off-the-shelf icon kits + emoji + glyphs.

PNG glyphs that look like archetype "seals" (`0x00_ΘƦΙΓΣΜ_nome_V.E.E.B_D.rung_026.PNG` etc.) exist in the source repo root. These are large (1–4 MB each) and decorative. We imported **two** to seed the brand asset folder — see `assets/seals/origem-veeb-026.png` and `assets/seals/tutorial-veeb-021.png`. They are soft pastel swirls (light backgrounds!) — use with a dark overlay or radial vignette so they read on the cosmos floor. Pull more on demand from the source repo if you need a unique hero centerpiece.

## Index of this folder

| Path | What |
|---|---|
| `README.md` | This file |
| `SKILL.md` | Agent-Skill manifest (drop the folder into Claude Code) |
| `colors_and_type.css` | All design tokens — colors, archetype palette, type scale, spacing, shadows, gradients, easings |
| `assets/dna/frequency-3.css`, `frequency-6.css` | Source-repo DNA layer fragments — frequency-tinted utility classes |
| `assets/seals/*.png` | Decorative V.E.E.B archetype seal imagery |
| `preview/_card.css` | Shared base styles for the atomic Design-System-tab cards |
| `preview/colors-*.html` | Color cards: trinity, archetypes, cosmos surfaces, semantic |
| `preview/type-*.html` | Type cards: brand display, scale, mono, eyebrows |
| `preview/spacing-*.html` | Spacing/elevation cards: 4pt scale, radii, shadows, glows |
| `preview/components-*.html` | Component cards: buttons, badges, tabs, inputs, progress, syntax, system card, repo card, dock, header, VEEB orb |
| `preview/brand-seals.html` | Brand card showing the imported seals |
| `SÜMBÜS_METAHUMAN_ARCHITECT/` | Original source files imported from the repo — index, FUSION editor, DNA css, tree.md |
| `ui_kits/architect/index.html` | Working recreation of the Control Panel + FUSION editor — open this to preview |
| `ui_kits/architect/{components,fusion,app}.jsx` | Reusable JSX components |
| `ui_kits/architect/styles.css` | Kit-specific styles layered on the root tokens |
| `ui_kits/architect/README.md` | Kit-specific notes |
