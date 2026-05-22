---
name: sumbus-design
description: Use this skill to generate well-branded interfaces and assets for SÜMBÜS METAHUMAN ARCHITECT — a Portuguese-language esoteric/sci-fi authoring environment that frames a code editor and file repository as a living digital organism with twelve KOBLLUX archetypes tuned to the Tesla 3-6-9 / 528 / 963 frequency family. Use this for production work or throwaway prototypes/mocks/decks that need to look and sound like the SÜMBÜS brand.
user-invocable: true
---

# SÜMBÜS Design Skill

Read the `README.md` file within this skill, and explore the other available files (`colors_and_type.css`, `preview/`, `assets/`, `ui_kits/architect/`). The README contains the canonical content fundamentals, visual foundations, and iconography rules — read it before producing anything.

## What to do when the user invokes this skill

If creating visual artifacts (slides, mocks, throwaway prototypes, marketing imagery, etc):
1. Copy `colors_and_type.css` and the relevant pieces of `assets/` (seals, logos, illustrations) into the destination project.
2. Build static HTML files for the user to view. Use the nebula background, the rainbow `::before` top accent on cards, the 3-6-9 trinity gradient on hero titles, and the Montserrat 900 / JetBrains Mono pairing.
3. Default to Portuguese (pt-BR) copy. Keep the eyebrow / frequency-byline / mystical-technical voice described in the README.

If working on production code:
- Treat `colors_and_type.css` as the token source of truth — its CSS variables (`--c-primary`, `--arch-*`, `--grad-369`, `--shadow-card`, etc.) cover every reusable foundation.
- Read `ui_kits/architect/components.jsx` and `ui_kits/architect/fusion.jsx` as reference implementations. They are not production-ready, but they show the canonical visual structure: the 520px mobile-first column, the 58px header + 68px dock pinned chrome, the glass card with rainbow top accent, the trinity nav segmented control, and the archetype-tinted syntax highlighting in the FUSION editor.

If the user invokes this skill without any other guidance, ask them:
1. **Output**: production code? slide deck? mock screen? marketing landing? a new "system" inside the Architect?
2. **Language**: pt-BR (default) or another?
3. **Surface**: the mobile-first 520-column app, a wider desktop page, a 16:9 slide, or print?
4. **Archetype**: which of the 12 KOBLLUX should this lean into? (this drives accent color, frequency byline, and verb code — see README → palette section)

Then act as an expert SÜMBÜS designer and output HTML artifacts or production code, depending on the need.

## File index

| Path | Purpose |
|---|---|
| `README.md` | Brand context, content & visual fundamentals, iconography rules |
| `colors_and_type.css` | All design tokens — colors, archetype palette, type scale, spacing, shadows, gradients, easings |
| `assets/dna/` | The original `frequency-*.css` fragments imported from the source repo |
| `assets/seals/` | Decorative V.E.E.B archetype seal PNGs (1024×1024 pastel swirls) |
| `preview/` | Atomic preview cards — one per concept. Useful as quick visual lookups |
| `ui_kits/architect/` | Reference HTML/JSX recreation of the Architect control panel + the FUSION editor |

## Hard rules

- **Never** invent new "archetypes", new frequencies, or new system names. The 12 KOBLLUX archetypes and their Hz values are fixed (see `colors_and_type.css`).
- **Never** swap the brand emoji set for an icon font (🧬 🧠 🌀 👁️ 🔄 ⚡ 🏃 ⬡ 🌐 📚) — they're load-bearing.
- **Never** put the brand on a light background. Cosmos black (`#050811` / `#020617`) is the floor.
- **Never** machine-translate Portuguese terms into English just because the destination is English-speaking — keep `Arquétipos`, `Sistema Nervoso`, `Roda Viva`, `ATIVAR TODOS OS SISTEMAS` as proper nouns.
- **Always** end a feature description with the archetype + Hz + verb code (`GENUS · 852Hz · SYNTH`). This is the brand's signature copy device.

## Source

This skill is distilled from <https://github.com/truetruextrue/JESUS_VERB-> — the `SÜMBÜS_METAHUMAN_ARCHITECT/` subtree. If you have access, browsing the repo further (especially `00_CORE/`, `12_VEEB/`, `ARQUETIPOS/`) will deepen the archetype-and-frequency mapping.
