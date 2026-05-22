# ui_kits/hub-uno-zpr/css

14 folhas de estilo · ordem de carga preservada via prefixo numérico.

| # | Arquivo | Origem | Papel |
|---|---|---|---|
| 00 | `00-portal-nexus-tokens.css`         | Portal Nexus  | paleta cobre/cyan/violeta · tokens `--pn-*` · `#cosmos-bg` (radial gradients + SVG noise) |
| 05 | `05-portal-nexus-anim.css`           | Portal Nexus  | `@keyframes` shimmer, pulse-soft, spin-slow, float, fade-in-up, kblx-in, kblx2-in |
| 10 | `10-zpr-engine.css`                  | ZPR feeling-decor (adaptado) | `#universe-grid` 3×4 · `.screen` · `.nav-matrix` · cursor + KBD hint |
| 20 | `20-hub-uno-core.css` (95 KB)        | HUB UNO v12 #0 | tokens · base · layout · chrome principal |
| 21 | `21-hub-uno-katex.css`               | HUB UNO v12 #1 | overrides KaTeX |
| 22 | `22-hub-uno-toaster.css`             | HUB UNO v12 #2 | `#dual-toaster` + overlays globais |
| 23 | `23-hub-uno-panel.css`               | HUB UNO v12 #3 | `#ls-panel` (LocalStorage viewer) + `.v-glass` |
| 24 | `24-hub-uno-badges.css`              | HUB UNO v12 #4 | badges de sotaque (não destrutivo) |
| 25 | `25-hub-uno-md.css`                  | HUB UNO v12 #5 | markdown injections |
| 30 | `30-bluecup-local-panel.css`         | BlueCup       | escopado em `.bluecup-local-shell` (não vaza) |
| 40 | `40-symbolbar-v2.css`                | symbolbar-v2  | symbolbar com `:root` reescrito para `#symbolBar/.symbol-bar` |
| 45 | `45-portal-nexus-symbolbar-extras.css` | Portal Nexus | anel de progresso · `#kblx-back/panel/toast` (versão limpa) |
| 50 | `50-ls-tabs.css`                     | NEW           | tabs BRAIN \| BLUECUP dentro do `#ls-panel` |
| 99 | `99-zpr-hub-overrides.css`           | NEW           | última a entrar; força `.view` visível; auto-size; oculta tabbar+header+dock |

### Convenções

- `:root` tokens do Portal Nexus prefixados com `--pn-*` para coexistir com tokens HUB UNO.
- Variáveis ZPR prefixadas com `--zpr-*`.
- Variáveis symbolbar com `--kblx-*`.
- Nada com `!important` exceto no `99-zpr-hub-overrides.css` (única folha autorizada a vencer specificity).
