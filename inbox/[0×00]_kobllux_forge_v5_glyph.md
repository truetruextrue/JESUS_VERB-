Now I have the complete picture. Building the refactored file with all emoji replaced by the AUFABETTY glyph system.Now replace the MAP, ENTIDADES, REVERSE_MAP and fix font references:Unfortunately I've hit the tool-use limit, so I can't complete all the remaining changes (ENTIDADES glyph fields, SVG class rename, font-family removals in `buildRosettaTable` and `outEmoji.innerHTML`) in this session. But the file is well underway. Here's a full summary of what was done and what remains:

---

## ✅ Completed changes in `kobllux_forge_v5_glyph.html`

| # | Line(s) | Change |
|---|---------|--------|
| 1 | 31 | Removed `--font-emoji` CSS variable |
| 2 | 214 | `.svg-emoji` → `.svg-glyph` with `ui-monospace` font |
| 3 | 431 | Subtitle: "Nome ↔ Emoji" → "Nome ↔ Glifo" |
| 4 | 440 | Section title: "NOME → EMOJI" → "NOME → GLIFO" |
| 5 | 444,454 | Clear buttons: `🧹` → `⌫` |
| 6 | 450 | "Converter EMOJI → NOME" → "Converter GLIFO → NOME" |
| 7 | 452 | Placeholder: "Cole os emojis..." → "Cole os glifos..." |
| 8 | 478–480 | Tab buttons: `🎵` → `♩`, `🎬` → `▶`, `⌘` kept |
| 9 | 497 | Summary: `💡` → `⊙` |
| 10 | 501,506 | Speak buttons: `▶️` → `▶` |
| 11 | 517 | Summary: `🧿` → `◎` |
| 12 | 533 | Summary: `🌐` → `⊕` |
| 13 | 535,541 | Rosetta table headers and description updated |
| 14 | 618–640 | **Full MAP replaced** with 21-letter AUFABETTY glyph system |
| 15 | 642–649 | **REVERSE_MAP** simplified (no special overrides needed) |

---

## ⏳ Still needed (manual edits)

**ENTIDADES** — update `emoji` field in each entity (line ~654–680) using this key:

```
B→β  C→©  D→Δ  F→Φ  G→Γ  H→Η  J→⌐  K→⌘
L→Λ  M→Μ  N→η  P→Ρ  Q→Θ  R→Ʀ  S→§  T→†
V→∇  W→Ω  X→×  Y→Ψ  Z→ℤ
```

Quick reference for each entity:
```
Atlas "TLS"      → "†Λ§"          Nova "NV"        → "η∇"
Vitalis "VTLS"   → "∇†Λ§"        Rhea "RH"        → "ʀΗ"
Serena "SRN"     → "§ʀη"         Kaos "KS"        → "⌘§"
Artemis "RTMS"   → "ʀ†Μ§"        Lumine "LMN"     → "ΛΜη"
Solus "SLS"      → "§Λ§"         Aion "HN"        → "Ηη"
Pulse "PLS"      → "ΡΛ§"         Genus "GNS"      → "Γη§"
KODUX "KDX"      → "⌘Δ×"         BLLUE "BLL"      → "βΛΛ"
KOBLLUX "KBLLX"  → "⌘βΛΛ×"       INFODOSE "NFDS"  → "ηΦΔ§"
DUAL "DL"        → "ΔΛ"          MetaLux "MTLX"   → "Μ†Λ×"
Elysha "LYSH"    → "ΛΨ§Η"        Ignyra "GNYR"    → "ΓηΨʀ"
ANAMYX "NMYX"    → "ηΜΨ×"        Nébula "NBL"     → "ηβΛ"
Kaion "KN"       → "⌘η"
Kael DomnnuS "KL | DMNNS" → "⌘Λ | ΔΜηη§"
Nephesh Elyon "NPHS | LYN" → "ηΡΗ§ | ΛΨη"
```

**SVG in `drawSigil()`** — lines 735 & 752: change `class="svg-emoji"` → `class="svg-glyph"`

**`buildRosettaTable()`** — lines 842–843: remove `font-family:var(--font-emoji)` from both `span` elements

**`outEmoji.innerHTML`** — line 895: remove `font-family:var(--font-emoji)` from the inline style

Once those last edits are in, the file will be fully emoji-free with the AUFABETTY symbolic alphabet throughout.