# dual.mod · KOBLLUX ∆³ Hub — UI Kit

High-fidelity recreation of the **dual.mod Hub Monolith (v1.1)** distilled into reusable, well-factored React components. This is the canonical KOBLLUX surface: dark void background, opcode-keyed accents, V.E.E.B. metrics, the Δ Analyzer (K↔B convergence), and the modularizer pipeline.

## Files

| File | Component |
|---|---|
| `index.html` | Live interactive recreation — drives all components |
| `HubShell.jsx` | Header + main scroll layout + section wrapper |
| `EquationBar.jsx` | The Δ equation strip (K · Δ · B · 12_K×B_12) |
| `PoloPanel.jsx` | K/B input panel pair for the Δ Analyzer |
| `OpcodeChip.jsx` | Camada toggle + opcode identity badge |
| `DeltaButton.jsx` | The gold "CONVERGIR · CALCULAR Δ" CTA with pulse animation |
| `MetricCells.jsx` | The 6-cell coefficient grid (Coef. K / B / Δ / α×β / 12_K×B_12 / Estado) |
| `VeebRow.jsx` | V.E.E.B. layer cards (V / E / E / B) |
| `OpcodeTable.jsx` | The 13-opcode DNA table |
| `FileCard.jsx` | A generated-file row with opcode left-border, badge, and ⊙ Copiar |
| `ArchetypeOrb.jsx` | Circular media slot for Nova/Infodose etc. |

## What it demonstrates

- The **D1→D8 clamp type scale** in real layout
- **Glass surfaces** vs **panel sections** side-by-side
- The two **brand-vocabulary buttons** — the bordered gold CTA (Δ button) and the rounded blue solid (default)
- Opcode-keyed left-border-3px for any file/module identity
- Real Δ-result coefficients computed live from the K and B textarea content (length-based heuristic — the live API call is not wired)
- Archetype orbs using the local `assets/archetypes/*.mp4|gif` media

## What is intentionally not wired

- The actual API call (`CFG.call`) — the textarea-driven Δ analysis is a local heuristic only.
- Git commit shell — visual surface only.
- The full modularizer pipeline (file generation) — shown as preview file cards using fixture data.

The goal of this kit is **pixel-fidelity of the KOBLLUX surface**, not production replication of the engine.
