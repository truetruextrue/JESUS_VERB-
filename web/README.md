# ⬡ WEB · MÓDULOS LOCAIS · KOBLLUX ∆7

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   W E B /   ·   M Ó D U L O S   L O C A I S   ·   K O B L L U X   ∆7     ║
║                                                                              ║
║   ⬡ · Sem CDN externo. Sem dependências remotas. Tudo local. Tudo vivo.    ║
║                                                                              ║
║   0×02 INTEGRAR ― · 0×0A ESTRUTURAR ⬡ · 528Hz + 639Hz                     ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

Opcode principal: **0×02** · Frequência: **528Hz** · Símbolo: **―** · Ação: **INTEGRAR**
Opcode estrutural: **0×0A** · Frequência: **639Hz** · Símbolo: **⬡** · Ação: **ESTRUTURAR**

---

## FILOSOFIA DA PASTA `web/`

A pasta `web/` é a **coluna vertebral tecnológica** do KOBLLUX TRINITY SYSTEM. Ela
encapsula todos os assets de frontend em forma **completamente local** — sem chamadas
a CDNs externos, sem dependências de rede, sem pontos de falha remotos.

Esta decisão é filosófica e técnica: assim como a lei `VERDADE × INTEGRAR ÷ Δ = ∞`
exige que a verdade seja integrada internamente antes de ser expandida, o sistema
web deve ser soberano — capaz de operar **offline**, em modo PWA, em qualquer
ambiente, sem depender de servidores de terceiros.

Cada arquivo em `web/` foi **escolhido, lapidado e selado** para servir a uma função
específica na malha. Não há arquivo supérfluo. Cada byte é intencional.

---

## MAPA DE MÓDULOS · TABELA COMPLETA

### CSS · Estilos Vivos

| Arquivo          | Opcode  | Hz    | Função                                                          |
|------------------|---------|-------|-----------------------------------------------------------------|
| `iFSw-fix.css`   | 0×02 ―  | 528Hz | Shell iFSw — layout principal, frames, navegação estrutural     |
| `zpr.css`        | 0×0A ⬡  | 639Hz | Matriz ZPR — grid 3×3, estilos dos cards de arquétipo          |

### JS · Módulos de Lógica

| Arquivo                    | Opcode  | Hz    | Função                                                     |
|----------------------------|---------|-------|------------------------------------------------------------|
| `js/modules/screensData.js`| 0×0A ⬡  | 639Hz | Dados das telas — lista de arquétipos, rotas, metadados    |
| `js/modules/ZPR.js`        | 0×0A ⬡  | 528Hz | Motor da Zona de Presença Resonante — renderiza a matrix   |
| `js/modules/iFSw-fix.js`   | 0×02 ―  | 528Hz | Correções e lógica do shell iFSw (frames, eventos)         |
| `js/modules/0RB-0S17.js`   | 0×08 ◉  | 432Hz | Sistema ORB — gerador de avatares determinísticos em SVG   |
| `js/modules/cadial-coupler.js` | 0×02 ― | 528Hz | **BLLUE** — acopla arquétipos ao iframe central (ver abaixo) |

### BRIDGE · Pontes de Comunicação

| Arquivo                | Opcode  | Hz    | Função                                                          |
|------------------------|---------|-------|-----------------------------------------------------------------|
| `BRIDGE/kob-glue.js`   | 0×06 ☯  | 528Hz | Cola KOB — unifica eventos entre módulos isolados              |
| `BRIDGE/0S17-bridge.js`| 0×05 ⧉  | 672Hz | Ponte 0S17 — comunicação entre iframe e shell principal        |
| `BRIDGE/Linkmaster.js` | 0×05 ⧉  | 639Hz | Mestre de links — roteamento e navegação entre arquétipos      |

### TTS · Text-To-Speech · Voz dos Arquétipos

| Arquivo                        | Opcode  | Hz    | Função                                                    |
|-------------------------------|---------|-------|-----------------------------------------------------------|
| `TTS/kob-tts-unified.js`      | 0×02 ―  | 528Hz | Motor TTS unificado — interface única para síntese de voz |
| `TTS/kob-tts-voice-arch.js`   | 0×0B ⧗  | 741Hz | Perfis de voz por arquétipo — pitch, rate, estilo         |

### CORE · Assets Primários

| Pasta/Arquivo  | Opcode  | Hz    | Função                                                          |
|----------------|---------|-------|-----------------------------------------------------------------|
| `CORE/icons/`  | 0×07 ✧⃝⚝| 777Hz | Ícones e símbolos geométricos dos 13 opcodes e 12 arquétipos   |
| `CORE/assets/` | 0×07 ✧⃝⚝| 777Hz | Logos, selos, geometria sagrada em SVG/PNG                     |

---

## ORDEM DE CARREGAMENTO

O `index.html` principal carrega os módulos em uma sequência precisa. A ordem não é
arbitrária — cada módulo prepara o terreno para o próximo, como os opcodes em cadeia:

```
0×00  ──▶  index.html inicializa (DOM pronto)
            │
0×0A  ──▶  screensData.js   (ESTRUTURAR — dados e rotas carregados)
            │
0×0A  ──▶  ZPR.js           (ESTRUTURAR — matriz ZPR renderizada)
            │
0×02  ──▶  iFSw-fix.js      (INTEGRAR  — shell iFSw ativo e corrigido)
            │
0×08  ──▶  0RB-0S17.js      (PULSAR    — sistema ORB inicializado)
            │
0×02  ──▶  cadial-coupler.js (INTEGRAR — BLLUE ativo, arquétipo carregado)
            │
            ▼
       Sistema KOBLLUX ∆7 · PRONTO · 528Hz resonante
```

**Em código (dentro de `index.html`):**

```html
<!-- ESTRUTURA DE CARREGAMENTO KOBLLUX ∆7 -->

<!-- 1. ESTRUTURAR: dados das telas -->
<script type="module" src="web/js/modules/screensData.js"></script>

<!-- 2. ESTRUTURAR: matrix ZPR -->
<script type="module" src="web/js/modules/ZPR.js"></script>

<!-- 3. INTEGRAR: shell iFSw -->
<script type="module" src="web/js/modules/iFSw-fix.js"></script>

<!-- 4. PULSAR: sistema ORB de avatares -->
<script type="module" src="web/js/modules/0RB-0S17.js"></script>

<!-- 5. INTEGRAR: BLLUE cadial-coupler (último — depende de todos) -->
<script type="module" src="web/js/modules/cadial-coupler.js"></script>

<!-- PONTES (carregadas em paralelo após os módulos core) -->
<script src="web/BRIDGE/kob-glue.js" defer></script>
<script src="web/BRIDGE/0S17-bridge.js" defer></script>
<script src="web/BRIDGE/Linkmaster.js" defer></script>

<!-- TTS (opcional, sob demanda) -->
<script src="web/TTS/kob-tts-unified.js" defer></script>
<script src="web/TTS/kob-tts-voice-arch.js" defer></script>
```

---

## BLLUE · cadial-coupler.js · O CORAÇÃO DO `web/`

**`cadial-coupler.js`** é a manifestação mais importante da pasta `web/`. Ele encarna
o arquétipo **BLLUE** (― · 0×02 · INTEGRAR · 528Hz) — o espelho vivo que conecta
o shell principal a cada um dos 12 módulos de arquétipo CADIAL.

**Por que BLLUE é o espelho:**

BLLUE não processa lógica própria. Ele **reflete** — pega o que o usuário escolhe
na Matriz ZPR e projeta na superfície do iframe central. É um intermediário puro,
um canal transparente de integração. Assim como o espelho não cria a imagem mas
permite que ela se manifeste, BLLUE não cria os arquétipos — ele os revela.

**Responsabilidades do cadial-coupler.js:**

```
1. ESCUTA eventos da Matriz ZPR (clique em arquétipo)
2. RESOLVE o caminho: "ARQUETIPOS/{nome}/index.html"
3. INJETA no iframe central via .setAttribute('src', ...)
4. MARCA o body com data-active-arch="{nome}"
5. EMITE CustomEvent('cadial:integrated') para toda a malha
6. PERSISTE no localStorage a última escolha do usuário
7. SINCRONIZA com _state/ via API de estado (quando disponível)
```

**Evento emitido:**

```javascript
// Escutando a integração de qualquer módulo externo:
window.addEventListener('cadial:integrated', (e) => {
  const { arch, hz, opcode } = e.detail;
  console.log(`[BLLUE ―] Arquétipo integrado: ${arch} · ${hz}Hz · ${opcode}`);
  // Atualizar HUD, tocar nota ressonante, etc.
});
```

---

## SISTEMA ORB · 0RB-0S17.js · 0×08 PULSAR

O **Sistema ORB** (`0RB-0S17.js`) é o gerador de avatares **determinísticos** do
KOBLLUX. Dado um nome de usuário, gera sempre o mesmo avatar SVG — um ORB único,
colorido conforme o arquétipo ativo, com geometria fractal baseada no hash do nome.

```javascript
// Exemplo de uso do ORB System
import { makeOrbAvatar } from './0RB-0S17.js';

const svg = makeOrbAvatar({
  name  : 'Usuário',
  arch  : 'atlas',
  hz    : 528,
  size  : 128
});

document.querySelector('#main-orb').innerHTML = svg;
```

O ORB é **pulsante** (0×08 · PULSAR · 432Hz) — sua animação CSS respira na frequência
do arquétipo ativo, criando uma ressonância visual entre o avatar e o módulo carregado.

---

## ZPR.js · ZONA DE PRESENÇA RESONANTE · 0×0A ESTRUTURAR

`ZPR.js` é o motor que **renderiza e gerencia** a Matriz ZPR — a grade 3×3 de
arquétipos mais o Dock da tríade primordial (SOLUS · RHEA · AION).

**Responsabilidades:**

```
1. Lê dados de screensData.js (metadados dos 12 arquétipos)
2. Renderiza o grid 3×3 com cards de arquétipo
3. Renderiza o Dock com SOLUS · RHEA · AION
4. Gerencia estado de seleção (ativo / inativo / hover)
5. Emite evento "zpr:selected" quando arquétipo é clicado
6. Anima a transição entre arquétipos (fade/slide/resonance)
7. Sincroniza visualmente com o iframe carregado pelo BLLUE
```

---

## BRIDGE · AS PONTES DA MALHA

Os módulos em `BRIDGE/` são **canais de comunicação** entre partes isoladas do sistema:

| Ponte           | Comunicação                                           |
|-----------------|-------------------------------------------------------|
| `kob-glue.js`   | Shell ←→ Módulos: eventos globais, estado compartilhado |
| `0S17-bridge.js`| Shell ←→ iframe interno: postMessage seguro          |
| `Linkmaster.js` | ZPR ←→ BLLUE: rotas, deep links, navegação programática|

**`0S17-bridge.js`** é especialmente crítico: como cada módulo de arquétipo carrega
em um iframe isolado, a comunicação entre o módulo e o shell pai é feita via
`window.postMessage()`. O `0S17-bridge.js` define o protocolo seguro para esse canal.

---

## TTS · A VOZ DOS ARQUÉTIPOS

Cada arquétipo CADIAL tem uma **voz única** — pitch, taxa de fala, pausa entre
frases — sintonizada na sua frequência ressonante. O sistema TTS (`kob-tts-unified.js`
+ `kob-tts-voice-arch.js`) usa a Web Speech API para dar voz ao sistema.

| Arquétipo | Pitch  | Rate   | Hz    | Caráter da Voz                  |
|-----------|--------|--------|-------|---------------------------------|
| ATLAS     | 0.85   | 0.90   | 528Hz | Grave, ponderado, estratégico   |
| NOVA      | 1.20   | 1.10   | 432Hz | Agudo, entusiasmado, criativo   |
| VITALIS   | 1.00   | 1.00   | 639Hz | Neutro, energético, vital       |
| PULSE     | 0.95   | 0.95   | 594Hz | Médio, ressonante, compassivo   |
| ARTEMIS   | 1.10   | 1.15   | 672Hz | Dinâmica, curiosa, exploratória |
| SERENA    | 0.90   | 0.80   | 528Hz | Suave, acolhedora, calma        |
| KAOS      | 0.75   | 1.20   | 777Hz | Profundo, disruptivo, intenso   |
| GENUS     | 0.80   | 0.85   | 852Hz | Sério, construtor, metodológico |
| LUMINE    | 1.30   | 1.05   | 963Hz | Brilhante, transcendente, puro  |
| SOLUS     | 0.70   | 0.70   | 432Hz | Muito grave, silencioso, sábio  |
| RHEA      | 1.05   | 0.95   | 528Hz | Fluido, contínuo, eterno        |
| AION      | 0.88   | 0.88   | 639Hz | Atemporal, guardião, memória    |

---
EM NOME DO PAI (UNO · 432Hz), DO FILHO (DUAL · 528Hz)
E DO ESPÍRITO SANTO (TRINITY · 639Hz). AMÉM.

VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7
