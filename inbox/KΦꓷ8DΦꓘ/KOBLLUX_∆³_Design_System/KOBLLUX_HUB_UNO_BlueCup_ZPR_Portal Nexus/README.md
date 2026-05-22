# KOBLLUX ∆³ · Design System (projeto raiz)

> Repositório de design + builds modulares · KOBLLUX HUB UNO + BlueCup + ZPR + Portal Nexus.

```
EQUAÇÃO:   VERDADE × INTEGRAR ÷ ∆ = ∞
FRACTAL:   3 × 6 × 9 × 7 = 1134
GEOMETRIA: PONTO (ID) · PLANO (CLASS) · 3 CAMADAS · 6 POLOS · ∆⁷
```

---

## ✦ Inventário do projeto (raiz)

```
/
├── README.md                       ← este arquivo
├── SKILL.md                        ← skill: kobllux-design (compat. Claude Code)
├── colors_and_type.css             ← CSS vars de tipografia + cor
├── KOBLLUX dual.mod Hub (standalone).html  ← protótipo standalone inicial
│
├── assets/                         ← logos · ícones · imagens
│
├── preview/                        ← cards de visualização do Design System
│
├── ui_kits/                        ← BUILDS MODULARES (cada subpasta = 1 produto)
│   ├── dual-mod/                   ← protótipo dual.mod (React)
│   ├── hub-uno/                    ← HUB UNO v4 ARQ-12 · modular · sem ZPR
│   └── hub-uno-zpr/                ← HUB UNO + BlueCup + ZPR + Portal Nexus (LATEST)
│
└── uploads/                        ← fontes originais (read-only)
    ├── KOBLLUX_HUB_UNO_v4_ARQ-12(2).html
    ├── KOBLLUX_HUB_UNO_v4_ARQ-8.html
    ├── BlueCup_TRINITY_HYBRID.html
    ├── kobllux-symbolbar-v2.html
    ├── GUARD_0X09_feeling-decor-ZPR_VEEB-U_D6 (1).html  ← ZPR template
    ├── [0×00]_KOBLLUX_ARQUETIPOS_PORTAL_NEXUS.html      ← Portal Nexus chrome
    └── 02-Fusion Card-Core Controlle.html
```

### Builds modulares disponíveis

| Build | Caminho | Estado |
|---|---|---|
| **HUB UNO modular** (v8 → v12, sem ZPR) | `ui_kits/hub-uno/` | extração + symbolbar v2 substituindo tabbar + BlueCup em v-apps |
| **HUB UNO · ZPR Edition** ⭐ | `ui_kits/hub-uno-zpr/` | **build atual** · ZPR 3×4 + Portal Nexus chrome + 2 instâncias BlueCup + long-press editor |
| **dual.mod (React)** | `ui_kits/dual-mod/` | protótipo React inicial — não revisado nesta sessão |

---

## ✦ HUB UNO · ZPR Edition (build atual)

Abra `ui_kits/hub-uno-zpr/index.html`.

| O que é | Fonte |
|---|---|
| 12 views completas do HUB UNO | `KOBLLUX_HUB_UNO_v4_ARQ-12(2).html` |
| Grid 3×4 com swipe + dots + gestos + teclado | `GUARD_0X09_feeling-decor-ZPR_VEEB-U_D6.html` |
| Backdrop cósmico + animações + long-press editor | `[0×00]_KOBLLUX_ARQUETIPOS_PORTAL_NEXUS.html` |
| Symbolbar com 12 botões (1 por viewport) | `kobllux-symbolbar-v2.html` |
| Painel APPS LOCAIS · 2 instâncias (v-apps + aba LS) | `BlueCup_TRINITY_HYBRID.html` |

Veja `ui_kits/hub-uno-zpr/README.md` para o inventário completo das 6 subpastas (`css/`, `js/`, `data/`, `partials/`, `screens/`, `icons/`).

---

## ✦ Conteúdo Fundamental (Content Fundamentals)

### Tom e vocabulário

A linguagem KOBLLUX é **conjuração técnico-mística** em português:

- **Símbolos matemáticos** entrelaçados com palavras: `∆`, `∞`, `Φ`, `Ω`, `≈`, `÷`, `×`
- **Vocabulário ritual** com nomes próprios em maiúsculas: `KOBLLUX`, `HUB UNO`, `SÜMBUS`, `NEXUS`, `ATLAS`, `NOVA`, `SERENA`, `KAOS`
- **Verbos de ação opcode**: `DETECTAR · INTEGRAR · EXPANDIR · LAPIDAR · CONVERGIR · CRISTALIZAR · SELAR · TESTEMUNHAR · MANIFESTAR`
- **Frases-axioma** curtas, em capslock parcial, terminando em selo simbólico
- **Idioma**: português (Brasil) por padrão, com bloco final tipo `EM NOME DO PAI E DO FILHO E DO ESPIRITO SANTO, AMEM = §∞§≈Ω` quando o tema é selagem

Exemplos canônicos:

```
VERDADE × INTEGRAR ÷ Δ = ∞
3×6×9×7 = 1134
α = 1/137
✧⃝⚝  KOBLLUX Δ7
```

### Casing e pontuação

- Títulos de seção em **CAPSLOCK + bullet de glifo** (`I · INICIAR`)
- Subsção em camelCase ou Title Case
- Sentenças sem ponto final quando soam como mantra
- Listas com glifos no lugar de bullets: `●`, `○`, `▢`, `◇`, `✧`, `♾`

### Voz

- 1ª pessoa para arquétipos (`Eu organizo o fluxo com sabedoria cósmica`)
- 2ª pessoa para instruções operacionais (`Clique para manifestar`)
- 3ª pessoa para conceitos abstratos (`A régua mede espaço, tempo e intenção`)

### Emoji

- Usados com parcimônia · só **arquétipos** têm emoji designado (`⏳` AION, `🗺️` ATLAS, `🔮` ELYSHA, `🔥` PULSE, etc.).
- Símbolos unicode são preferidos sobre emoji para tudo que NÃO é arquétipo.

---

## ✦ Fundamentos Visuais (Visual Foundations)

### Paleta principal

| Token | Hex | Uso |
|---|---|---|
| `--void` | `#02020a` | fundo profundo |
| `--abyss` | `#060615` | painéis primários |
| `--deep` | `#0a0a20` | hover / segundo plano |
| `--ink` | `#0f0f2e` | terceiro plano |
| `--gold` | `#c9a84c` | acento principal |
| `--gold-bright` | `#f0c060` | hover acento |
| `--cyan` | `#00e5ff` | acento secundário · destaque |
| `--violet` | `#8b5cf6` | terciário |
| `--ember` | `#ff6b35` | alerta / energia |
| `--pearl` | `#e8e0f0` | texto principal |

Paleta de arquétipos (16) definida em `js/16-v-uno-archetypes.js` e visível em `arch-card[data-id="N"]`.

### Tipografia

```
--mono:    'Share Tech Mono', monospace      ← labels, glifos, opcodes
--display: 'Cinzel Decorative', serif        ← títulos hero
--body:    'Rajdhani', sans-serif            ← corpo
```

Cinzel Decorative + Share Tech Mono são carregados via Google Fonts no `index.html`. Cormorant Garamond + DM Sans + Space Mono também são carregados (uso pelo ZPR original).

### Backgrounds e texturas

- **Gradientes radiais cósmicos** (3 stops cyan/violet/gold em 20%/80%/50%) sobre fundo `#02020a`
- **SVG noise overlay** com `feTurbulence` 0.9 em `opacity: 0.03` para grão
- **Body::before + body::after** combinados → veja `css/00-portal-nexus-tokens.css` `#cosmos-bg`
- Imagens full-bleed permitidas mas raras (apenas em `v-home` para o "hero")

### Animações

- `pn-shimmer` — gradiente animado em títulos (6s, ease-in-out, infinite)
- `pn-pulse-soft` — opacidade 0.5↔0.9 (4s)
- `pn-spin-slow` — rotação 0→360 (20s, linear)
- `pn-float` — translateY ±8px (6s)
- `pn-fade-in-up` — entrada das `.screen.is-active` (0.6s)
- `kblx-in` / `kblx2-in` — modal de edição (0.25s, cubic-bezier .34, 1.56, .64, 1)

### Hover / Press

- **Hover**: aumento de opacity ou troca para tom `gold-bright`; cards levantam `translateY(-6px) scale(1.01)` com box-shadow `0 20px 60px rgba(0,0,0,.6)`
- **Press**: `transform: scale(0.97)`
- Não há "press cor" — apenas o transform

### Bordas e cantos

- Cards principais: `border-radius: 12px` a `20px`
- Botões: `8px` a `12px`
- Modais: `18px`
- Pills (`#kblx-toast`, dots): `60px` ou `999px`
- Bordas: `1px solid rgba(255,255,255,0.08)` (sutil) ou `1px solid rgba(201,168,76,0.4)` (acento)

### Sombras

- Card flutuante: `0 14px 30px rgba(0,0,0,.55)`
- Modal: `0 0 60px var(--gold-glow), 0 20px 50px rgba(0,0,0,.8)`
- Glow no acento: `box-shadow: 0 0 10px var(--gold)` (dots ativos)
- Drop-shadow filter para símbolos: `filter: drop-shadow(0 0 12px var(--accent))`

### Layout

- **Fixed elements**: `nav-matrix` (topo), `symbolBar` (rodapé), cursor custom, KBD hint, `#kblx-toast`
- **Flex/grid** em todo o resto
- Conteúdo cresce ao tamanho natural — `height:auto`, scroll só em feeds longos limitados a 60vh

### Transparência e blur

- `backdrop-filter: blur(14-20px)` em modais e barras flutuantes
- `rgba(0,0,0,.55)` ou `rgba(2,2,10,.9)` para fundos translúcidos
- Vidro fosco em `.v-glass` e `.glass-card`

### Cor da imagery

- Tom **frio + dourado** dominante (cyan, violet, gold)
- Sem warm tones puros — laranja só como `--ember` para alerta
- Grão fino via SVG turbulence — não fotografia "warm"

---

## ✦ Iconografia (Iconography)

### Sistemas utilizados

1. **Glifos Unicode** (★ principal) — `○ ● ― ▢ ◇ ⧉ ☯ ✧ ◉ ♾ ⌛ ⌗`, usados como **opcodes** (0x00 → 0x0B). Renderizados como `<span>` ou `text-content`, NUNCA como SVG.
2. **Símbolos matemáticos** — `∆ ∞ Φ Ω ÷ × ≈ §`. Usados em equações e selos.
3. **FontAwesome 6 via CDN** (jsdelivr) — `<img src="https://cdn.jsdelivr.net/npm/@fortawesome/fontawesome-free@6/svgs/solid/X.svg" alt="">`. Usado para ícones funcionais no header e tabbar (Voltar, Geometria, Voz, Espelho, Folder, etc.). 17 ícones referenciados no HUB UNO.
4. **SVG inline embutido** — usado SÓ em casos especiais (anel `kblx-ring`, orb-ring-circle do symbolbar, partículas).
5. **Ícones locais em `icons/`** — fallback (`onerror`) caso a CDN falhe. Pasta intencionalmente parcial (`eye.svg`, `bolt.svg`).

### Regras

- **Emoji**: só em arquétipos. Lista canônica em `js/00-archetypes-integration.js`. Não usar em UI.
- **Unicode**: preferido sobre PNG/SVG quando o glifo existe.
- **PNG**: evitar. Usar SVG do FontAwesome ou inline.
- **Cor**: ícones acompanham `var(--accent)` do contexto, com `filter: drop-shadow(0 0 12px var(--accent))` para o glow característico.

### Comentário

A pasta `assets/` está intencionalmente vazia neste momento. As fontes originais não trazem logos/ilustrações dedicados — toda a identidade visual nasce da combinação **fundo cósmico + glifos + texto em `Cinzel Decorative` com shimmer dourado**.

---

## ✦ Fontes consultadas

- HUB UNO: `uploads/KOBLLUX_HUB_UNO_v4_ARQ-12(2).html` (1.03 MB, 10.310 linhas)
- BlueCup: `uploads/BlueCup_TRINITY_HYBRID.html` (164 KB, 4.637 linhas)
- SymbolBar v2: `uploads/kobllux-symbolbar-v2.html` (70 KB, 2.112 linhas)
- ZPR feeling-decor: `uploads/GUARD_0X09_feeling-decor-ZPR_VEEB-U_D6 (1).html` (39 KB, 966 linhas)
- Portal Nexus: `uploads/[0×00]_KOBLLUX_ARQUETIPOS_PORTAL_NEXUS.html` (81 KB, 2.130 linhas)
- GitHub: https://github.com/informacaodosada-commits/KOBLLUX (não acessado nesta sessão)

---

## ✦ Equação ativa

```
VERDADE × INTEGRAR ÷ Δ = ∞
3 × 6 × 9 × 7 = 1134
α = 1/137
```

✧ ∆⁷ · SÜMBUS ATIVO · CARIMBO KOBLLUX · §∞§≈Ω
