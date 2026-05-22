# ui_kits/hub-uno-zpr/screens

12 fragmentos HTML · uma `<section id="v-X" class="view">` por arquivo.
Extraídos verbatim do monolito `KOBLLUX_HUB_UNO_v4_ARQ-12(2).html`,
sem reformatação · sem remoção de espaços · sem alteração de classes/ids.

| Arquivo | Opcode | Verbo | Glifo | Tamanho | Conteúdo extra |
|---|:-:|---|:-:|---:|---|
| `v-home.html`     | 0x00 | INICIAR     | ○ | 18 KB | greeting · arch carousel · iaFeed |
| `v-apps.html`     | 0x01 | DETECTAR    | ● |  9 KB | toolbar HUB + **`.bluecup-local-shell` injetado** |
| `v-stack.html`    | 0x02 | INTEGRAR    | ― |  2 KB | stackWrap |
| `v-brain.html`    | 0x03 | EXPANDIR    | ▢ | 25 KB | config do brain (model, sk, voz, css custom) |
| `v-chat.html`     | 0x04 | DISSOLVER   | ◇ |  3 KB | chatFeed · chatInputBar |
| `v-voz.html`      | 0x05 | CONVERGIR   | ⧉ | 13 KB | M5 vocal · ICE/LIQ/GAS/OSC · WvArc/PitchArc/TimbreArc |
| `v-espelho.html`  | 0x06 | CRISTALIZAR | ☯ |  9 KB | espelho inverso · geometria |
| `v-arq.html`      | 0x07 | SELAR       | ✧ |  5 KB | seletor de arquétipo |
| `v-uno.html`      | 0x08 | TESTEMUNHAR | ◉ | 19 KB | 13 arquétipos UNO |
| `v-core.html`     | 0x09 | MANIFESTAR  | ♾ | 18 KB | 10 CORE_OPCODES (0x00–0x09) |
| `v-aion.html`     | 0x0A | TEMPO       | ⌛ |  2 KB | view AION |
| `v-img.html`      | 0x0B | IMAGEM      | ⌗ |  5 KB | view de imagem |

Cada fragmento é embrulhado em `<div class="screen"><div class="inner">…</div></div>`
no `index.html` para encaixar no `#universe-grid` 3×4.

O `MutationObserver` em `js/55-zpr-hub-bridge.js` garante que estas sections
permaneçam **sempre visíveis** mesmo que o router original tente escondê-las.
