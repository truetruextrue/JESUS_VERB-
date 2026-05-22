# ui_kits/hub-uno-zpr/js

27 scripts modulares · ordem de carga **crítica** definida no `index.html`.

## Ordem de carga (todos com `defer`)

```
1. KaTeX (CDN)
2. BlueCup helpers (30, 31)              ← antes do router HUB UNO
3. HUB UNO v12 inline blocks (00 → 18)   ← ordem original do monolito
4. marked + stubs externos
5. ZPR engine + bridges (50, 55, 60, 65) ← depois do hub para sobrepor router
6. particles.js (CDN) + SymbolBar v2 (40) ← por último
```

## Inventário

| # | Arquivo | Origem | Bytes | Papel |
|---|---|---|---:|---|
| 00 | `00-archetypes-integration.js`      | HUB UNO v12 #2  | 12.9 KB | tabela completa dos arquétipos |
| 01 | `01-btnLS-meta.js`                  | HUB UNO v12 #3  |   253 B | anota meta no `#btnLS` |
| 02 | `02-katex-bind.js`                  | HUB UNO v12 #4  |  3.5 KB | bind do KaTeX |
| 03 | `03-img-or-aion-bind.js`            | HUB UNO v12 #5  |  4.9 KB | botões `#btnImg`/`#btnAion` |
| 04 | `04-btnLS-purif-engine.js`          | HUB UNO v12 #6  | 18.5 KB | engine de purificação LS |
| 05 | `05-geometry-subconsciente.js`      | HUB UNO v12 #7  | 35.3 KB | `KOBLLUX_GEOMETRY` v1 (subconsciente) |
| 06 | `06-btnGeometria-bind.js`           | HUB UNO v12 #9  |  1.1 KB | bind do `#btnGeometria` |
| 07 | `07-hub-router-main.js`             | HUB UNO v12 #10 |  379 KB | **motor central** (router · `$`,`$$`,`LS`) — router neutralizado pelo bridge |
| 08 | `08-brain-config-store.js`          | HUB UNO v12 #11 | 16.8 KB | store de config do v-brain |
| 09 | `09-apps-store.js`                  | HUB UNO v12 #12 | 13.4 KB | store de apps (catálogo) |
| 10 | `10-geometry-activation-engine.js`  | HUB UNO v12 #17 | 67.4 KB | `KOBLLUX_GEOMETRY` v2 (activation) — sobrescreve v1 |
| 11 | `11-voz-arquetipos-sotaque.js`      | HUB UNO v12 #18 | 42.0 KB | `KOBLLUX_VOZ_ARQUETIPOS_SOTAQUE` |
| 12 | `12-sotaque-selector-enhancer.js`   | HUB UNO v12 #19 |  6.1 KB | enhancer do seletor de sotaque |
| 13 | `13-voz-m5.js`                      | HUB UNO v12 #20 | 32.8 KB | M5 Voz Quântica |
| 14 | `14-espelho-arq.js`                 | HUB UNO v12 #21 | 26.7 KB | espelho + arquétipo |
| 15 | `15-v-arq.js`                       | HUB UNO v12 #22 |  8.8 KB | renderer do v-arq |
| 16 | `16-v-uno-archetypes.js`            | HUB UNO v12 #23 | 12.1 KB | renderer do v-uno |
| 17 | `17-v-core-opcodes.js`              | HUB UNO v12 #24 | 12.6 KB | renderer do v-core (10 opcodes) |
| 18 | `18-keybadge-voiceauto.js`          | HUB UNO v12 #25 |  7.1 KB | key badge + voice auto-activate |
| 30 | `30-bluecup-patch-helpers.js`       | BlueCup CAP2/3/4 | 21.3 KB | `loadLocalAppFiles`, `saveLocalAppFiles`, `openApp`, `makeSafeKey`, … |
| 31 | `31-bluecup-local-card.js`          | BlueCup LOCAL_APPS_CARD | 7.6 KB | render do card em `v-apps` |
| 40 | `40-symbolbar-v2.js`                | symbolbar-v2 (patched) | 33.8 KB | NAV_BUTTONS substituído pelos 12 botões `data-nav` do HUB |
| 50 | `50-zpr-engine.js`                  | NEW (baseado em ZPR) | ~6 KB | grid 3×4 · swipe · dots · cursor · `navigateToCell` · `navigateToView` |
| 55 | `55-zpr-hub-bridge.js`              | NEW             |  ~1 KB | força `.view` visíveis · bridge symbolbar→`navigateToView` (capture-phase) |
| 60 | `60-portal-nexus-fx.js`             | NEW (limpo)     |  ~3 KB | long-press 3s → editor `#kblx-panel` · `window.kblxToast` |
| 65 | `65-ls-tabs.js`                     | NEW             |  ~6 KB | tabs BRAIN \| BLUECUP em `#ls-panel` |

### APIs públicas (window.*)

| Função | Origem | O que faz |
|---|---|---|
| `window.navigateToCell(row, col)` | ZPR engine | mover grid para célula (row,col) |
| `window.navigateToView(idOrNav)`  | ZPR engine | navegar por id de view (`'v-chat'`) ou nome (`'chat'`) |
| `window.go(nav)`                  | ZPR (override) | alias de `navigateToView` — preserva chamadas legadas do HUB |
| `window.loadLocalAppFiles()`      | BlueCup    | retorna `{key: {title,desc,icon,html}}` do localStorage |
| `window.saveLocalAppFiles(obj)`   | BlueCup    | persiste o objeto inteiro |
| `window.openApp(app)`             | BlueCup    | abre app local em iframe / nova aba |
| `window.makeSafeKey(title)`       | BlueCup    | slug seguro para chave |
| `window.kblxToast(msg, ms)`       | Portal FX  | toast dourado · 2.2s default |
