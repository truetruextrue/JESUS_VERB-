# Análise técnica — Fusion Card + Symbol Bar (iPhone)

## 1) Diagnóstico do código enviado

O HTML enviado está **funcionalmente rico**, mas possui riscos de integração quando você tenta mover a `symbol-bar` para outro HTML:

- **IDs duplicados** no documento (por exemplo `btn-arch`, `main-orb`, `orbCore`, `arch-overlay`, `script-tailwind` aparecem mais de uma vez), o que quebra seletores `getElementById/querySelector` em integrações parciais.
- **Dependência forte de scripts externos** (`kob-mestre`, `kobdh0-main`, módulos inline e CSS remotos). Se a Symbol Bar for extraída sem esses scripts, parte dos botões deixa de responder.
- **Dependência do Identity Engine** (`window.DI`, `window.KOBLLUX`, `window.makeOrbAvatar`, `di_syncNameUI`) para render do Orb e parâmetros de voz.
- **Dependências de DOM global**: vários handlers presumem elementos fora da barra (`#frame`, `#mainCard`, modais, player, playlist etc.).

---

## 2) O que precisa acompanhar a Symbol Bar no “segundo HTML”

Para a barra funcionar isolada (estilo iPhone floating/orbital), leve junto estes blocos mínimos:

1. **Markup base da barra**
   - `#symbolBar`
   - `#toggleBtn`, `#btn-prev`, `#btn-play`, `#btn-next`
   - `#btn-arch` com `#main-orb`
   - botões de navegação (`#btn-phi`, `#btn-viv`, `#btn-home`, `#btn-doc`)

2. **Style mínimo**
   - classes `.symbol-bar`, `.symbol-button`, `.hud-info`, `.orb`, `.orb-core`
   - animações do orb (`orbSpin`, `orbPulse`, `orbBreathe`)

3. **Engine de identidade (obrigatório para orb/voz)**
   - bloco `script-identity-engine` inteiro

4. **Controller da barra (eventos)**
   - clique play/pause, prev/next
   - navegação por `data-url`
   - long-press do `#btn-arch`

---

## 3) Arquitetura recomendada de integração

Use separação modular em vez de copiar o HTML completo:

- `symbolbar.html` → somente estrutura da barra
- `symbolbar.css` → estilos da barra/orb
- `symbolbar-controller.js` → eventos da barra
- `identity-engine.js` → `DI` + `KOBLLUX`

No segundo HTML:

```html
<link rel="stylesheet" href="./symbolbar.css">
<div id="symbolbar-mount"></div>
<script src="./identity-engine.js"></script>
<script type="module" src="./symbolbar-controller.js"></script>
```

E o controller injeta `symbolbar.html` em `#symbolbar-mount`.

---

## 4) Regras críticas para não quebrar no iPhone

- Evite IDs globais repetidos.
- Prefira `data-*` + `closest()` ao invés de IDs hardcoded em múltiplas instâncias.
- Use `viewport-fit=cover` + `env(safe-area-inset-bottom)` para posicionar barra flutuante acima da home indicator.
- Use listeners de `pointer*` (não só mouse/touch separados).
- Long-press de 700–900ms para abrir card sem conflito com drag.

---

## 5) Checklist de migração (prático)

1. Extrair **uma única** versão da Symbol Bar (sem duplicatas).
2. Renomear IDs críticos para namespace, ex.: `sb-btn-play`, `sb-main-orb`.
3. Copiar o Identity Engine para arquivo próprio.
4. Criar adapter para funções externas esperadas (`setMode`, `togglePlay`, `navigate`, etc.).
5. Testar no Safari iOS (PWA e browser normal).
6. Validar acessibilidade (`role=toolbar`, `aria-label`, `aria-pressed`).

---

## 6) Conclusão objetiva

Sim, dá para colocar a função do “card” dentro de outro HTML com Symbol Bar estilo iPhone — mas a chave é **modularizar** e remover dependência de IDs duplicados + scripts globais implícitos.

Se quiser, no próximo passo eu monto para você um **pacote pronto** (`symbolbar.html + css + js + adapter`) para encaixar direto no seu segundo HTML.
