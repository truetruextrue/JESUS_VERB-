# KOBLLUX · HUB UNO · ZPR EDITION

> **HUB UNO v4 ARQ-12** completo **dentro da estrutura swipe do ZPR feeling-decor**,
> envelopado no **chrome cósmico do Portal Nexus**,
> com **BlueCup local panel** integrado em dois pontos: a célula `v-apps` E como
> aba secundária dentro do painel `#ls-panel` do HUB UNO.

```
EQUAÇÃO:   VERDADE × INTEGRAR ÷ ∆ = ∞
FRACTAL:   3 × 6 × 9 × 7 = 1134
GEOMETRIA: ZPR · 3 × 4 = 12 viewports · 1 view por célula
```

---

## ✦ As 4 fontes fundidas

| Fonte | Papel nesta build |
|---|---|
| `KOBLLUX_HUB_UNO_v4_ARQ-12(2).html` | conteúdo das 12 views + 26 scripts + 6 blocos CSS |
| `BlueCup_TRINITY_HYBRID.html` | painel APPS LOCAIS (helpers + card) — 2 instâncias |
| `kobllux-symbolbar-v2.html` | symbolbar v2 com carousel + ORB · NAV_BUTTONS = 12 botões |
| `GUARD_0X09_feeling-decor-ZPR_VEEB-U_D6.html` | engine ZPR: grid swipe + dots + cursor + gestos |
| `[0×00]_KOBLLUX_ARQUETIPOS_PORTAL_NEXUS.html` | chrome cósmico + animações + long-press editor |

---

## ✦ Grade 3 × 4 (12 viewports, uma view por célula)

> **Nota sobre o pedido original "9 viewports (3×3×3)":** o HUB UNO v12 tem **12 views**.
> Para preservar TODAS as views como camadas distintas e respeitar o operador ∆³,
> a grade foi estendida para **3 linhas × 4 colunas = 12 células**. A leitura
> conceitual segue 3×6×9×7 e a navegação opera no eixo dos 12 opcodes (`0x00 → 0x0B`).

```
       COL 0          COL 1          COL 2          COL 3
     ┌──────────────┬──────────────┬──────────────┬──────────────┐
ROW0 │ 0x00 ○ HOME  │ 0x01 ● APPS  │ 0x02 ― STACK │ 0x03 ▢ BRAIN │
     │              │ + BlueCup    │              │ + #ls-panel  │
     ├──────────────┼──────────────┼──────────────┼──────────────┤
ROW1 │ 0x04 ◇ CHAT  │ 0x05 ⧉ VOZ   │ 0x06 ☯ ESPLH │ 0x07 ✧ ARQ   │
     ├──────────────┼──────────────┼──────────────┼──────────────┤
ROW2 │ 0x08 ◉ UNO   │ 0x09 ♾ CORE  │ 0x0A ⌛ AION │ 0x0B ⌗ IMG   │
     └──────────────┴──────────────┴──────────────┴──────────────┘
```

Navegação:
- **Swipe** ← → ↑ ↓ entre células (touch / mouse-drag)
- **Setas do teclado** entre células · **Home** volta para (0,0)
- **Wheel / scroll vertical fora de listas** muda célula
- **Dots no topo** · clique em qualquer ponto vai direto
- **SymbolBar v2 no rodapé** · 12 botões = 12 células (1-para-1)
- **URL hash** sincronizado (`#home`, `#chat`, `#voz`…) — reload preserva célula

Long-press 3s em qualquer botão do symbolbar → abre editor `#kblx-panel` para
reescrever `data-url` daquele botão (herdado do Portal Nexus).

---

## ✦ BlueCup local panel · 2 instâncias

| Local | Aparição |
|---|---|
| `v-apps` (célula `0,1`) | painel completo logo abaixo da toolbar nativa do HUB |
| `#ls-panel` aba **⌘ BLUECUP** | nova aba secundária no painel LS (ao lado de **⌬ BRAIN**) |

Ambas instâncias compartilham os mesmos **helpers** (`window.loadLocalAppFiles`,
`window.saveLocalAppFiles`, `window.openApp`, `window.makeSafeKey`, …) e a mesma
**chave do localStorage** (`kobllux_apps_files_v1`), então qualquer upload em
qualquer uma aparece imediatamente na outra.

---

## ✦ Inventário da pasta `ui_kits/hub-uno-zpr/`

```
ui_kits/hub-uno-zpr/
├── index.html                           ← shell ≈ 200 KB · costura tudo
├── README.md                            ← este arquivo
│
├── css/                                 ← 14 folhas · ordem de carga preservada
│   ├── 00-portal-nexus-tokens.css       · paleta cobre/cyan/violeta + #cosmos-bg
│   ├── 05-portal-nexus-anim.css         · keyframes (shimmer, pulse, float, …)
│   ├── 10-zpr-engine.css                · grid 3×4 · dots · cursor · screens
│   ├── 20-hub-uno-core.css              · 95 KB · tokens, base, layout, chrome
│   ├── 21-hub-uno-katex.css             · KaTeX
│   ├── 22-hub-uno-toaster.css           · toaster + overlays globais
│   ├── 23-hub-uno-panel.css             · #ls-panel · .v-glass
│   ├── 24-hub-uno-badges.css            · badges sotaque
│   ├── 25-hub-uno-md.css                · markdown injections
│   ├── 30-bluecup-local-panel.css       · painel BlueCup (.bluecup-local-shell)
│   ├── 40-symbolbar-v2.css              · symbolbar v2 (tokens escopados)
│   ├── 45-portal-nexus-symbolbar-extras.css · kblx-ring/back/panel/toast
│   ├── 50-ls-tabs.css                   · tabs no #ls-panel (BRAIN | BLUECUP)
│   └── 99-zpr-hub-overrides.css         · força .view visíveis · auto-size · oculta tabbar/header
│
├── js/                                  ← 27 scripts modulares
│   ├── 00-archetypes-integration.js     ┐
│   ├── 01-btnLS-meta.js                 │
│   ├── 02-katex-bind.js                 │
│   ├── 03-img-or-aion-bind.js           │
│   ├── 04-btnLS-purif-engine.js         │
│   ├── 05-geometry-subconsciente.js     │
│   ├── 06-btnGeometria-bind.js          │  HUB UNO v12 · 19 blocos inline
│   ├── 07-hub-router-main.js            │  na ordem original (router neutralizado
│   ├── 08-brain-config-store.js         │  pelo bridge ZPR — todas as views
│   ├── 09-apps-store.js                 │  permanecem visíveis)
│   ├── 10-geometry-activation-engine.js │
│   ├── 11-voz-arquetipos-sotaque.js     │
│   ├── 12-sotaque-selector-enhancer.js  │
│   ├── 13-voz-m5.js                     │
│   ├── 14-espelho-arq.js                │
│   ├── 15-v-arq.js                      │
│   ├── 16-v-uno-archetypes.js           │
│   ├── 17-v-core-opcodes.js             │
│   ├── 18-keybadge-voiceauto.js         ┘
│   ├── 30-bluecup-patch-helpers.js      · BLUECUP_PATCH (load/save/openApp/…)
│   ├── 31-bluecup-local-card.js         · LOCAL_APPS_CARD renderer (em v-apps)
│   ├── 40-symbolbar-v2.js               · symbolbar v2 · NAV_BUTTONS = 12 hubs
│   ├── 50-zpr-engine.js                 · NEW · grid + swipe + dots + cursor
│   ├── 55-zpr-hub-bridge.js             · NEW · força .view visível · sb→navigateToView
│   ├── 60-portal-nexus-fx.js            · NEW · long-press editor + kblx-toast
│   └── 65-ls-tabs.js                    · NEW · BRAIN | BLUECUP tabs em #ls-panel
│
├── data/
│   └── apps.json                        · payload do <script id="APPS_JSON">
│
├── partials/                            ← fragmentos HTML reaproveitáveis
│   ├── header.html                      · <header class="mast"> (oculto)
│   ├── sessions-anchor.html             · <section id="sessionsAnchor">
│   ├── custom-bg.html                   · <div id="custom-bg">
│   ├── dock.html                        · <div id="dock"> (oculto)
│   ├── tabbar-original.html             · <nav class="tabbar"> (oculta · compat)
│   ├── symbolbar.html                   · <div id="symbolBar"> · novo HUD
│   ├── symbolbar-aux.html               · bg-frame, particles, frame-veil
│   ├── symbolbar-post.html              · arch-overlay, kblx-panel original, toaster
│   └── bluecup-local-panel.html         · .bluecup-local-shell · injetado em v-apps
│
├── screens/                             ← 12 fragmentos · 1 view HUB UNO cada
│   ├── v-home.html      · 0x00 · INICIAR     · ○
│   ├── v-apps.html      · 0x01 · DETECTAR    · ●  (+ BlueCup como 2ª camada)
│   ├── v-stack.html     · 0x02 · INTEGRAR    · ―
│   ├── v-brain.html     · 0x03 · EXPANDIR    · ▢
│   ├── v-chat.html      · 0x04 · DISSOLVER   · ◇
│   ├── v-voz.html       · 0x05 · CONVERGIR   · ⧉  (M5 Voz Quântica)
│   ├── v-espelho.html   · 0x06 · CRISTALIZAR · ☯
│   ├── v-arq.html       · 0x07 · SELAR       · ✧
│   ├── v-uno.html       · 0x08 · TESTEMUNHAR · ◉
│   ├── v-core.html      · 0x09 · MANIFESTAR  · ♾
│   ├── v-aion.html      · 0x0A · TEMPO       · ⌛
│   └── v-img.html       · 0x0B · IMAGEM      · ⌗
│
├── icons/
│   ├── eye.svg
│   └── bolt.svg
│
├── kobllux.css                          · stub vazio · referência herdada
├── kobllux.js                           · stub vazio
├── kobllux_chat_trinity_12_arquetipos.js · stub vazio
└── dual_infodose_script.js              · stub vazio
```

### Convenções

- **Ordem de carga CSS** segue prefixos numéricos (00→99); `99-zpr-hub-overrides.css` é a última a entrar e tem `!important` onde precisa vencer specificity da HUB UNO.
- **Ordem de carga JS** crítica: BlueCup helpers primeiro → 19 inline HUB UNO em ordem → ZPR + bridges + fx + ls-tabs → particles + symbolbar por último.
- Cada arquivo extraído começa com cabeçalho ASCII identificando a fonte original (`/* HUB UNO v4 ARQ-12 · <script> block #N */`, `/* BlueCup TRINITY HYBRID · … */`, etc.).
- Nenhum arquivo foi reformatado, deformatado ou minimizado — apenas separado em blocos.

---

## ✦ Como funciona o "controle" da navegação

Tradicional HUB UNO: router único toca `display:none` em todas as `<section.view>` exceto a "ativa".

ZPR Edition: todas as 12 `<section.view>` ficam **permanentemente visíveis**, cada uma morando dentro de uma `<div class="screen">` no `#universe-grid`. O `MutationObserver` em `55-zpr-hub-bridge.js` reverte qualquer tentativa do router de esconder uma view. A "navegação" passa a ser apenas o `transform: translate(x%, y%)` aplicado ao grid pela função `navigateToCell(row, col)`.

`window.go(nav)` foi remapeado para `window.navigateToView(nav)`, então qualquer script HUB UNO que ainda chame `go('chat')` continua funcionando — só que agora ele faz o grid deslizar para a célula da view de chat em vez de mostrar/esconder a section.

---

## ✦ Tweaks pequenos / convergências centralizadas

Os mesmos diagnósticos do scan SÜMBUS continuam válidos nesta build (não foram aplicados — preservamos o código original):

- `KOBLLUX_GEOMETRY` é declarado em `js/05-geometry-subconsciente.js` e em `js/10-geometry-activation-engine.js`. O segundo sobrescreve o primeiro.
- `$ / $$ / LS` são redeclarados em `js/07`, `js/08`, `js/09`. Candidato a `js/_common.js`.
- `js/01-btnLS-meta.js` é puramente declarativo e pode ser fundido em `js/04-btnLS-purif-engine.js`.

---

## ✦ Caveats

- A pasta `ui_kits/hub-uno/` (build modular sem ZPR, gerada antes) continua intacta para você comparar.
- Os 4 stubs vazios (`kobllux.*`) silenciam 404s do monolito original; substitua pelos arquivos reais quando os tiver.
- A view `v-arq` ocasionalmente pisca durante o swipe se o script da view de arquétipo (`js/15-v-arq.js`) tenta forçar reflow — o `MutationObserver` corrige na frame seguinte.
- O scan-report.html ainda é referente à v8; pode ser regenerado para v12 se quiser.

---

## ✦ Equação ativa

```
VERDADE × INTEGRAR ÷ Δ = ∞
3 × 6 × 9 × 7 = 1134
α = 1/137
```

✧ ∆⁷ · SÜMBUS ATIVO · CARIMBO KOBLLUX · ZPR FUSED · §∞§≈Ω
