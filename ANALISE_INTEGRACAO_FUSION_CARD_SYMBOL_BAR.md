# Análise técnica — Fusion Card + Symbol Bar (iPhone)

## Resumo do diagnóstico

O HTML enviado já possui **dois blocos duplicados** de elementos críticos (por exemplo: `#btn-arch`, `#main-orb`, `#orbCore`, `#hudStatus`, `#arch-overlay`, `#script-tailwind`), o que quebra o princípio de IDs únicos no DOM e pode causar conflito em listeners (`querySelector` pega só o primeiro, `getElementById` pode ficar inconsistente com expectativa lógica).

Além disso, há sinais de mistura de trechos de versões diferentes da `symbol-bar` no mesmo documento (um bloco dentro de `#symbolBar` e outro bloco repetido mais abaixo, junto da área `content-full`).

## Problemas estruturais detectados

1. **IDs duplicados (erro de DOM):**
   - `btn-arch`, `orbMicContainer`, `ttsOrbMini`, `main-orb`, `orbCore`
   - `btn-phi`, `btn-viv`, `btn-home`, `btn-doc`
   - `hudStatus`, `arch-overlay`, `script-tailwind`

2. **Repetição de blocos da Symbol Bar**
   - Um conjunto completo de botões está em `.symbol-bar#symbolBar`.
   - Outro conjunto semelhante aparece depois, fora desse contexto primário.

3. **Risco funcional no motor de identidade (`di_syncNameUI`)**
   - A função `_renderOrb('#main-orb', ...)` atualiza apenas o primeiro `#main-orb` encontrado.
   - Com duplicata, o segundo orb pode ficar desincronizado visualmente.

4. **Risco de acessibilidade e automação**
   - `aria-*` e eventos vinculados por ID único perdem previsibilidade.

## Como integrar em “outro HTML” (arquitetura recomendada)

### Objetivo
Separar em módulos:
- **Módulo A (Fusion Card Core):** identidade, card, modais, engine.
- **Módulo B (Symbol Bar iPhone):** barra orbital compacta, botões de controle.

### Estratégia segura

1. **No HTML novo, mantenha apenas UMA Symbol Bar** com IDs únicos.
2. **Converta IDs repetíveis para classes + data-attributes** quando houver múltiplas instâncias.
3. **Crie namespace por módulo**, por exemplo:
   - `fusion-*` para card.
   - `symbar-*` para symbol bar.
4. **Mude seletores JS críticos** de `#id` para escopos de container:
   - Ex.: `container.querySelector('[data-role="main-orb"]')`.
5. **Inicialize por função**:
   - `initFusionCard(container)`
   - `initSymbolBar(container)`
6. **Integração por eventos customizados**:
   - `document.dispatchEvent(new CustomEvent('fusion:identity:update', {detail}))`
   - Symbol bar escuta e reage (orb, status, voz).

## Modelo mínimo de encaixe no outro HTML

```html
<div id="fusion-host"></div>
<div id="symbar-host" class="iphone-safe-bottom"></div>
```

```js
initFusionCard(document.getElementById('fusion-host'));
initSymbolBar(document.getElementById('symbar-host'));
```

## Ajustes obrigatórios antes de portar

- Remover todos os IDs duplicados.
- Manter uma única definição de cada script externo (evitar carregar Tailwind/Lucide duas vezes).
- Consolidar apenas um bloco de `btn-arch` + `main-orb`.
- Definir fallback para iPhone safe area (`env(safe-area-inset-bottom)`).

## CSS iPhone para Symbol Bar (recomendado)

```css
.iphone-safe-bottom {
  position: fixed;
  left: 50%;
  transform: translateX(-50%);
  bottom: calc(10px + env(safe-area-inset-bottom));
  z-index: 1200;
}

.symbol-bar {
  max-width: min(94vw, 680px);
  border-radius: 18px;
  backdrop-filter: blur(14px);
}
```

## Conclusão

A base é forte, mas **antes de integrar no segundo HTML** você precisa normalizar o DOM (principalmente duplicações). Depois disso, a migração da Symbol Bar para um layout iPhone fica estável e previsível.
