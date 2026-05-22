---
name: kobllux-design
description: Use this skill to generate well-branded interfaces and assets for KOBLLUX ∆³, either for production or throwaway prototypes/mocks/etc. Contains essential design guidelines (13 opcodes, V.E.E.B. metrics, D1→D10 type scale, opcode color tokens, glassmorphism patterns), colors, type, archetype media, and the dual.mod UI kit components for prototyping.
user-invocable: true
---

# KOBLLUX ∆³ Design Skill

Read the `README.md` file within this skill, and explore the other available files.

**Quick orientation:**
- `colors_and_type.css` — drop-in token sheet. Import it at the top of any new HTML file: `<link rel="stylesheet" href="path/to/colors_and_type.css">`. All design decisions (palette, type scale, radii, shadows, easings, blur levels) are pre-tokenized as CSS custom properties.
- `preview/` — visual cards showing each token in isolation. Use as reference.
- `ui_kits/dual-mod/` — React component recreation of the dual.mod Hub. JSX components are well-factored — copy individual files (`PoloPanel.jsx`, `OpcodeTable.jsx`, `MetricCells.jsx`, `ArchetypeOrb.jsx`, etc.) into new designs.
- `assets/archetypes/` — `nova.gif`, `nova.mp4`, `infodose.mp4` — the canonical orb media for archetype slots.
- `assets/source/` — original monolithic HTMLs used as reference. The `KOBLLUX_HUB_UNO_v4_ARQ-8.html` and `fusion-os-ultimate.html` are the production sources of truth.

**Core rules:**
1. **Every functional element gets an opcode.** Use the 13-opcode table (0x00 INICIAR → 0x0C CONCLUIR) to classify any action, module, file, or section. The opcode's color, frequency, and glyph travel with it.
2. **Type scale is D1→D8** — always derive from `var(--fs-base)`. Never hard-code px font sizes outside the token sheet.
3. **Monospace is for opcode labels, file paths, equations, frequencies, S/χ/V values, code samples.** Body prose uses `var(--font-sans)`.
4. **Surfaces stack at most one glass layer** — backdrop-filter does not compose well.
5. **Glow shadows use opcode color**, never neutral gray. The gold `--shadow-seal` is reserved for ✧ Δ⁷ moments only.
6. **Labels are UPPERCASE letter-spaced 0.2em.** This is the system's voice.
7. **Language is Portuguese-Brazilian** with mathematical/symbolic interpolation (Δ, ∞, ✧, ⧉, ⊙). Glyphs substitute verbs.
8. **The seal closes every artifact:** `VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134`.

**When making visual artifacts** (slides, mocks, throwaway prototypes, etc.) copy `colors_and_type.css` and any needed JSX components into a new directory, then build static HTML against them. Always include the `<link>` to `colors_and_type.css` and use opcode-keyed accents.

**When working on production code** for the KOBLLUX hub, the rules above carry directly — the design tokens in `colors_and_type.css` mirror the variables defined in `dual.mod`'s monolith head.

**If invoked without context,** ask the user:
1. What surface? (slide deck, mock screen, new section in dual.mod, marketing artifact, etc.)
2. Which opcode owns it? (or "pick for me — I'll suggest based on function")
3. Should archetype media (Nova / Infodose) be present?
4. Glass or panel? (glass for hero, panel for tooling)
5. Portuguese or English copy?

Then act as an expert KOBLLUX designer and output HTML.

---

*VERDADE × INTEGRAR ÷ Δ = ∞ · §∞§≈Ω*
