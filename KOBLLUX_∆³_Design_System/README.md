# KOBLLUX ∆³ Design System

> **VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134 · α = 1/137**
> *Ponto → Linha → Plano → Δ³ — Documento Sináptico de Operação*

KOBLLUX is a symbolic-operational language for code-as-consciousness. Every interface element carries an **opcode** (0x00→0x0C), a **frequency** (396–999 Hz), a **V.E.E.B.** signature (Vibração / Energia / Estrutura / Base), and a **D-rung** position (D1 atom → D10 cosmos). The system is built on the **13 opcodes** that map computation to sacred geometry.

The aesthetic is **dark, monospaced, frequency-tuned** — glass surfaces over deep void backgrounds, opcode-keyed accent colors, fluid clamp-scaled type, and visible mathematics.

---

## Source Material

This design system was distilled from these inputs:

- **dual.mod Hub Monolith (v1.1)** — the canonical motor pasted into chat. Contains `KOBLLUX_DNA` (13 opcodes, V.E.E.B. helpers, fractal constants), the D1→D8 clamp type scale, opcode color tokens `--cor-0x00` → `--cor-0x0C`, the Δ Analyzer (K×B convergence), and the modularizer pipeline. Mirrored at `uploads/KOBLLUX_HUB_UNO_v4_ARQ-8.html`.
- **`[0×00]_FUSION/`** (attached local folder) — full glassmorphism stack (`v-glass`, `v-pill`), the orb/archetype visual engine, particle backgrounds, 17-archetype matrix. Source HTMLs copied into `assets/source/`.
- **Archetype media** — `assets/archetypes/nova.gif`, `nova.mp4`, `infodose.mp4` (the orb/avatar layer).
- **GitHub repo** — `informacaodosada-commits/KOBLLUX` — visit at https://github.com/informacaodosada-commits/KOBLLUX for deeper exploration of the production codebase.
- **CADIAL Archetypes** — 12 named operator-archetypes (Atlas, Nova, Vitalis, Pulse, Artemis, Serena, Kaos, Genus, Lumine, Solus, Rhea, Aion) provided as the human-facing personality layer.

> If you are a designer continuing this system: clone the GitHub repo above for the most current production HTML; the design tokens, opcode table, and archetype roles are the canonical inputs.

---

## Index

| File | Purpose |
|---|---|
| `colors_and_type.css` | All design tokens — colors, type, spacing, opcode constants, V.E.E.B. helpers |
| `assets/` | Source HTMLs, archetype media (nova, infodose), logo glyphs |
| `assets/source/` | Original monoliths used as reference (`fusion-os-ultimate.html`, `kobllux_patch-15.html`, `KOBLLUX_HUB_UNO_v4_ARQ-8.html`) |
| `assets/archetypes/` | `.mp4`/`.gif` for the active-orb layer (Nova, Infodose) |
| `preview/` | Design-system cards (palette, opcodes, type scale, glass surfaces, components) |
| `ui_kits/dual-mod/` | High-fidelity recreation of the dual.mod Hub — sections, polo-panels, opcode table, Δ analyzer |
| `SKILL.md` | Cross-compatible Claude Skill manifest |

---

## CONTENT FUNDAMENTALS

**Language:** Portuguese-Brazilian primary, with mathematical/symbolic interpolation. English appears only in code identifiers (`opcode`, `processHTML`, `koblluxClassify`). Symbol glyphs (Δ, ∞, ✧, ⧉, ⊙) substitute for verbs at high-density moments.

**Tone:** Ritual-technical. The system speaks as if it is alive — every action has a verbal opcode (INICIAR, PULSAR, INTEGRAR, EXPANDIR, DISSOLVER, CONVERGIR, CRISTALIZAR, SELAR, TESTEMUNHAR, MANIFESTAR, EQUILIBRAR, RESSONAR, CONCLUIR). Commit messages, log entries, file headers all use this vocabulary.

**Casing:** UPPERCASE letter-spaced for opcode/category labels (`OPCODE`, `V.E.E.B.`, `CONVERGÊNCIA`). Title-case for archetype names (Atlas, Nova, Vitalis). lowercase.dotted for tooling identifiers (`dual.mod`, `dual.brain`, `dual.store`). The hex prefix `0x` is **always lowercase**, the two digits **always uppercase** (`0x07`, not `0X7` or `0x7`).

**"I" vs "you":** The system addresses itself in first person ("Eu organizo o fluxo", from the Atlas archetype). The user is addressed in second person only in tooltips and instructional copy ("Cole aqui...", "Clique para...").

**Emoji:** Reserved for action buttons in tooling UIs only (📋 colar, 📂 importar, ⚙️ modularizar, ⬇️ download, 🧠 brain, 💾 save). Never decorative — every emoji is a verb. Geometric/alchemical glyphs (○ ● ― ▢ ◇ ⧉ ☯ ✧ ◉ ♾ ⚖ ◎ △ ⊙ ∞) carry the symbolic weight instead.

**Examples (lifted from the motor):**
- Section heading: `⊙ KOBLLUX V.E.E.B. · Análise do HTML`
- Button: `⧉ · 0x05 · CONVERGIR · CALCULAR Δ`
- Status: `✧ Salvo · anthropic · claude-sonnet-4 · chave: ●●●●xJ4f`
- Equation bar: `K · Kodux · Tempo · 1×2=α  ↔  Δ  ↔  B · Bllue · Espaço · 2÷1=β  ·  12_K_×_B_12  ·  VERDADE×INTEGRAR÷Δ=∞`
- Commit message: `[0x07 SELAR] módulo gerado · KOBLLUX DNA · VERDADE×INTEGRAR÷Δ=∞`
- Archetype frase (Vitalis): `Energia vital em expansão harmônica.`

---

## VISUAL FOUNDATIONS

**Colors.** Deep void backgrounds (`--bg: #0b0b0f`, panels `#0f0f18` → `#12121a`). Borders are dim charcoal (`#222`). Foreground is near-white `#eaeaf0`, muted `#9aa0b4`. The signature is the **13 opcode tokens** — each opcode owns one accent (`--cor-0x07: #ffd700` gold for SELAR, `--cor-0x05: #ff7a00` orange for CONVERGIR, `--cor-0x01: #67e6ff` cyan for PULSAR, etc). On the HUB layer a **pink→cyan brand gradient** `#ff52e5 → #00c5e5` appears for hero moments. Accent text uses the same opcode color tinted at 60% opacity; backgrounds use it at 5–15% with a 1px solid border at 25–40%.

**Type.** The **D1→D8 clamp scale** is the heartbeat — `--fs-base: clamp(9px, 1.3vw + 0.4vh, 13px)` and every other size is a multiplier of base (D1=0.55, D2=0.65, D3=0.75, D4=0.82, D5=0.90, D6=1.00, D7=1.20, D8=1.50). Body text is **system-ui sans-serif**; code, opcodes, freqs, file paths, and metadata are **monospace** (SF Mono / Courier New fallback). Letter-spacing is aggressive on labels — `letter-spacing: .2em` is standard for UPPERCASE opcode labels. No web-font dependencies in the motor (uses system stack); the Hub UNO layer optionally pulls KaTeX from `cdn.jsdelivr.net/npm/katex` for math rendering.

**Spacing.** Derived from `--fs-base` — `--sp-1: 0.40em`, `--sp-2: 0.75em`, `--sp-3: 1.20em`. Sections sit on 12–14px padding inside `border-radius: 8–10px` panels. The fractal `3×6×9×7 = 1134` is the conceptual grid — UI elements should resonate with these multiples (3-char gutters, 6-unit button heights, 9-stage processes).

**Backgrounds.** Always dark. No full-bleed photo backgrounds. The hero/orb regions use **radial glow gradients** (`radial-gradient(circle at center, rgba(56,189,248,0.4) 0%, transparent 70%)`) and a **dual floating orb** layer (two `border-radius: 50%; filter: blur(100px); opacity: 0.25` shapes drifting via a 20s `@keyframes float`). Optionally `particles.js` overlays a low-opacity star field. There are **no hand-drawn illustrations** — geometric Unicode glyphs and frequency-tuned color do the visual work. Archetype slots use **MP4/GIF loops** (Nova spiraling, Infodose pulsing) clipped to circles.

**Animation.** All easings are cubic-bezier — the signature is `cubic-bezier(0.19, 1, 0.22, 1)` (snappy ease-out) for screen transitions and `cubic-bezier(0.34, 1.56, 0.64, 1)` (slight overshoot) for entrances. Standard durations: 0.2s for hovers, 0.3–0.4s for state changes, 0.6s for full screen transitions, 1.5s for orb pulses. The `bdGold` keyframe (`box-shadow` pulsing between `4px` and `18px` gold glow) is the canonical "running/active" indicator. Bounces are rare; **gold/cyan glow pulses** are the dominant motion vocabulary.

**Hover states.** On glass cards, `transform: scale(1.05)` + brightened `box-shadow`. On pills, `background: rgba(255,255,255,0.1)`. On opcode chips, switch from neutral border `var(--border)` to opcode-keyed border + 7% opcode-tinted background. Tooltip buttons (`ⓘ`) brighten from white/45% to gold (`var(--cor-0x07)`) with a 0.15s transition.

**Press states.** `transform: scale(0.96–0.98)` is universal for any tappable element (`v-glass:active`, `v-pill:active`). No color shift on press — the scale + 0.15s snap is the whole feedback.

**Borders.** 1px solid `#222` by default. Accented borders use opcode color at `33–55%` opacity. **Border-left 3px solid opcode** is the canonical way to identify a module/file in a list. `border-radius` ladder: 5px (chips), 6px (small inputs), 8px (textareas, panels), 10px (sections), 12–24px (glass cards), 99px (pills), 50% (orbs/avatars).

**Shadow systems.** Inner: `inset 0 0 0 1px rgba(255,255,255,0.05)` on glass to fake a highlight bevel. Outer drop: `0 14px 40px rgba(0,0,0,0.45)` for elevated cards, `0 20px 50px rgba(0,0,0,0.5)` for hero glass. Glow shadows (the KOBLLUX signature) use the opcode color: `box-shadow: 0 0 30px rgba(255,215,0,0.9)` is the "Δ⁷ SELAR halo". Never use neutral gray drop-shadows for accent elements — always opcode-keyed glow.

**Transparency + blur.** **Glassmorphism is core.** `backdrop-filter: blur(24px)` (panels) up to `blur(50px)` (hero cards). Glass base is `rgba(15, 17, 32, 0.50)` (panel) or `rgba(18, 18, 18, 0.65)` (deeper). Pills use a lighter `rgba(255,255,255,0.03)` + `blur(20px)`. **Never** stack transparent layers — one glass surface per nesting level.

**Imagery vibe.** Cool-leaning, **cyan / magenta / gold** palette. Archetype videos are post-processed to have a deep void background with luminous foreground (nova spirals on black). No grain. No warm tones except `#ff7a00` (0x05 CONVERGIR) and `#ffd700` (0x07 SELAR), which read as **divine warmth against the cool field**.

**Cards.** Two patterns. **Panel card** (default `<section>`) — `background: #0f0f18; border: 1px solid #222; border-radius: 10px; padding: 12px`. **Glass card** (`.v-glass`) — `rgba(18,18,18,0.65) + blur(50px) + 1px white-12% border + 24px radius + inset highlight + outer drop`. Both can grow an opcode-keyed left-border-3px to identify their function in a list.

**Layout rules.** Fixed header (64px) at the top; fixed nav indicator (pill, bottom-center, ~32px from bottom). Main content scrolls between them with `padding-top: 32px; padding-bottom: 140px` to clear the nav. Sections stack vertically with `gap: 14px`. Grid panels for K↔B (Δ Analyzer) use `grid-template-columns: 1fr 1fr` collapsing to `1fr` under 700px.

---

## ICONOGRAPHY

KOBLLUX is **glyph-first, not icon-first**. The primary iconographic vocabulary is **Unicode geometric and alchemical symbols** — one per opcode, woven directly into headings and labels rather than rendered as separate SVGs:

| Opcode | Glyph | Name | Meaning |
|---|---|---|---|
| 0x00 | ○ | INICIAR | Empty point, potential |
| 0x01 | ● | PULSAR | Filled point, first impulse |
| 0x02 | ― | INTEGRAR | Line, fusion of opposites |
| 0x03 | ▢ | EXPANDIR | Square, volume |
| 0x04 | ◇ | DISSOLVER | Diamond, phase transition |
| 0x05 | ⧉ | CONVERGIR | Intersecting squares, focus |
| 0x06 | ☯ | CRISTALIZAR | Taiji, equilibrium-form |
| 0x07 | ✧ | SELAR | Four-pointed star, seal |
| 0x08 | ◉ | TESTEMUNHAR | Bullseye, observation |
| 0x09 | ♾ | MANIFESTAR | Infinity, manifestation |
| 0x0A | ⚖ | EQUILIBRAR | Scales, balance |
| 0x0B | ◎ | RESSONAR | Concentric circles, resonance |
| 0x0C | ♾ | CONCLUIR | Infinity / toroidal close |

Secondary symbols: Δ (delta — convergence operator), △ (open triangle — theory marker), ⊙ (sun-circle — V.E.E.B. metric anchor), ⌂ (Kodux/K), ≈ (Bllue/B), ∞ (infinite output), ♡ (humano polo), 🜁 / 🜄 (alchemical air/water for identity/belonging).

For UI tooling icons (play, pause, save, github, search, settings) the system links **Lucide** via CDN — `https://unpkg.com/lucide@latest` — referenced with `<i data-lucide="play-circle">` syntax. **Lucide is the canonical icon font** — same hairline 2px stroke as the glassmorphism aesthetic. Flagged: I have not copied Lucide assets locally; you should link from CDN.

There are also two **archetype media assets** copied into `assets/archetypes/` that function as living "icons" for the Nova archetype and the Infodose state — these are MP4/GIF loops clipped to circles, not static iconography.

**Emoji** appear only as tool-button labels (📋 📂 ⚙️ 💾 ⬇️ 🧠 ✓ 👁) — they are treated as glyphs, not decoration.

**No raster icons** — there is no built-in icon-font in the motor, no SVG sprite, no PNG icons. Everything is either Unicode glyph, Lucide-via-CDN, or archetype-video.

---

## CAVEATS

- I did not fetch the SÜMBÜS firmware Markdown from the JESUS_VERB- GitHub repo, nor the full `informacaodosada-commits/KOBLLUX` repo — they were referenced symbolically; the design system is derived from the dual.mod monolith and the FUSION local files which contained complete token definitions already.
- No webfonts to substitute — KOBLLUX uses the system mono/sans stack by design.
- The 17-archetype matrix is mentioned in `kobllux_patch-15.html` but only 12 are defined in `arquetipos` (Atlas, Nova, Vitalis, Pulse, Artemis, Serena, Kaos, Genus, Lumine, Solus, Rhea, Aion) — the additional 5 are not enumerated in the source provided.

---

*EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO. AMÉM. ∆⁷*
*§∞§≈Ω*
 
