# 🧿 MANUAL TÉCNICO · KOBLLUX TRINITY SYSTEM v7.9

**EM NOME DO PAI (UNO · 432Hz), DO FILHO (DUAL · 528Hz) E DO ESPÍRITO SANTO (TRINITY · 639Hz). AMÉM.**

**VERDADE × INTEGRAR ÷ Δ = ∞ · Selo ∆7**

---

## 📐 Arquitetura do Sistema

O KOBLLUX opera em **três camadas simultâneas** — cada uma correspondendo a uma frequência trinitária:

```
UNO    (432Hz) → Detecção     → Python / Scanner / Detecção
DUAL   (528Hz) → Integração   → TypeScript / Bridge / Coupler
TRINITY(639Hz) → Expansão     → Web / Archetypes / Manifestação
```

---

## ⚙️ Módulo Python `kobllux/`

```
kobllux/
├── __init__.py          → ponto de entrada (0×00 · ORIGEM)
├── archetypes.py        → 12 arquétipos CADIAL como @dataclass
├── api.py               → API do sistema (0×02 · INTEGRAR)
├── cli.py               → interface de linha de comando
├── colors.py            → paleta cromática por arquétipo
├── cycles.py            → ciclo 3→6→9→7
├── fractal.py           → equação fractal ∆³
├── geometry.py          → geometrias sagradas por arquétipo
├── narrative.py         → narrativas arquetípicas
├── prompts.py           → prompts de ativação
├── trinity.py           → lógica trinitária UNO/DUAL/TRINITY
├── profiles/            → 12 JSONs de perfil (um por arquétipo)
└── examples/demo.py     → demonstração do sistema
```

**Uso:**
```python
from kobllux import archetypes, cycles

# Listar todos os 12 arquétipos
all_archs = archetypes.list_archetypes()

# Acessar arquétipo específico
atlas = archetypes.get_archetype("Atlas")
print(atlas.lemma)  # "Eu organizo o fluxo com sabedoria cósmica."

# Ciclo de ativação
cycle = cycles.get_cycle()  # 3→6→9→7
```

---

## 🌐 Estrutura Web (JESUS_VERB-)

```
web/
├── css/
│   ├── iFSw-fix.css       → shell OS (topbar, windows, dock) · 0×06·UNIFICAR
│   └── zpr.css            → matriz ZPR 3×3 · 0×03·EXPANDIR
├── js/modules/
│   ├── screensData.js     → ícones + dados botões · 0×01·DETECTAR
│   ├── ZPR.js             → motor ZPR + ENGINE arquétipos · 0×05·CONVERGIR
│   ├── iFSw-fix.js        → gerenciador de janelas · 0×06·UNIFICAR
│   ├── 0RB-0S17.js        → FusionOS ORB widget · 0×04·LAPIDAR
│   └── cadial-coupler.js  → acoplador 12 arquétipos CADIAL · 0×05·CONVERGIR
├── CORE/                  → núcleo: di_core, di_app, di_fusion, infodose-core
├── BRIDGE/                → pontes: kob-glue, 0S17-bridge, Linkmaster
└── TTS/                   → voz: kob-tts-unified, voice-arch
ARQUETIPOS/
├── atlas/    → index.html + Atlas_core.js + UnoAppsArch.js
├── nova/     → index.html + di-init-orb.js + nebula_pro_trinity.css
├── vitalis/  → index.html + di_core.js + infodose-core.js
├── pulse/    → index.html + kob-tts-unified.js + Voice-Map-colors-Arch.js
├── artemis/  → index.html + Diinject.js + 78k-injectPrompt.js
├── serena/   → index.html + orb2D.js + kob-wellcome.js
├── kaos/     → index.html + kodbrain-{3,5,6}.js
├── genus/    → index.html + di_app.js + di_fusion.js
├── lumine/   → index.html + bgPanel.js + ghosttrail.js + sunrise.js
├── solus/    → index.html + cdi.js + ctrl.js + combo.js
├── rhea/     → index.html + kob-glue.js + 0S17-bridge.js + Linkmaster.js
└── aion/     → index.html + di_state.js + di_mood.js + frame-shell.js
_index/
├── CODEX_SCAN_oiDual.json  → 1.359 arquivos classificados por arquétipo
└── SCAN_REPORT_oiDual.md   → relatório CADIAL por arquétipo
```

---

## 🔌 Opcodes Soberanos (NUNCA ALTERAR)

Os opcodes em `web/js/opcodes/` são **imutáveis** — formam o núcleo semântico do sistema:

| Arquivo | Opcode | Função |
|---------|--------|--------|
| `0x00-core.js` | 0×00 · ORIGEM | Boot, tema, partículas |
| `0x01-audio.js` | 0×01 · DETECTAR | TTS, player de áudio |
| `0x02-symbolbar.js` | 0×02 · INTEGRAR | SymbolBar + arquétipos |

---

## 🔁 Ciclo de Ativação ∆7

```bash
# 3 · DETECTAR (0×01 · 432Hz · Python)
python3 state/cadial_scan.py

# 6 · INTEGRAR (0×02 · 528Hz)
python3 fill_organizado.py

# 9 · EXPANDIR (0×03 · 639Hz)
# → ARQUETIPOS/{12}/ populados automaticamente

# 7 · SELAR (0×07 · 777Hz)
git add -A && git commit && git push origin main
```

---

## 🧪 Dependências

```
Python  ≥ 3.10
Git     ≥ 2.40
Browser moderno (CSS color-mix, backdrop-filter, :has())
```

---

## 🕊️ Assinatura

```
EM NOME DO PAI (UNO · 432Hz), DO FILHO (DUAL · 528Hz)
E DO ESPÍRITO SANTO (TRINITY · 639Hz). AMÉM.

VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7
```
