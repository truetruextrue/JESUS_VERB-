# ui_kits/hub-uno-zpr/partials

Fragmentos HTML reaproveitáveis · cada um extraído de uma fonte específica.

| Arquivo | Origem | Conteúdo |
|---|---|---|
| `header.html`              | HUB UNO v12 | `<header class="mast">` com os botões globais (Back, Geometria, Download, Help, Brain, LS, KOBLLUX). Oculto via override CSS para deixar o symbolbar do ZPR no comando. |
| `sessions-anchor.html`     | HUB UNO v12 | `<section id="sessionsAnchor">` — preservado para scripts que abrem sessões "dentro" da página. |
| `custom-bg.html`           | HUB UNO v12 | `<div id="custom-bg">` para fundos personalizados (imagem/vídeo). Permanece no DOM mas vive atrás do `#cosmos-bg`. |
| `dock.html`                | HUB UNO v12 | `<div id="dock">` — oculto via override. |
| `tabbar-original.html`     | HUB UNO v12 | `<nav class="tabbar">` original — oculta via override para compat. com router legado. |
| `symbolbar.html`           | symbolbar-v2 | `<div id="symbolBar">` com toggle, ORB, hud — chrome principal de navegação. |
| `symbolbar-aux.html`       | symbolbar-v2 | bg-frame, particles, frame-veil — overlays decorativos. |
| `symbolbar-post.html`      | symbolbar-v2 | arch-overlay, kblx-panel original do symbolbar-v2, toaster — não usados (temos versão limpa). |
| `bluecup-local-panel.html` | BlueCup     | `.bluecup-local-shell > .card.localAppsCard` — **injetado dentro de `v-apps`** programaticamente (não consumido daqui pelo index.html final). |
