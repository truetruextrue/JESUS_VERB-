# UI Kit · SÜMBÜS METAHUMAN ARCHITECT

A high-fidelity recreation of the **Architect Control Panel** and the **SÜMBÜS FUSION · ΔUAL 3.0** code-editor surface from the source repo `SÜMBÜS_METAHUMAN_ARCHITECT/`. Mobile-first, 520-col, dark cosmos.

## Files

| File | What |
|---|---|
| `index.html` | Entry — loads React + Babel + the three JSX modules |
| `styles.css` | All UI kit styles, layered on the project-root `colors_and_type.css` tokens |
| `components.jsx` | Reusable: `<AppHeader>`, `<OrgHero>`, `<SystemCard>`, `<SystemGrid>`, `<ActionGrid>`, `<StatusPanel>`, `<LogPanel>`, `<Veeb>`, `<Dock>` |
| `fusion.jsx` | The editor surface: `<FusionTabs>`, `<FusionToolbar>`, `<EditorPane>`, `<FusionStatusbar>`, `<FusionEditor>` |
| `app.jsx` | Wires the two screens together with shared state (tab, progress, log) |

## What's interactive

- **Trinity nav** (top right) and **Dock** (bottom) both switch between the **Painel** view and the **FUSÃO** editor view.
- **⚡ ATIVAR TODOS OS SISTEMAS** animates the progress bar from its current value to 100%, ticking log entries as it goes.
- **🔍 DIAGNÓSTICO** writes a warning to the log.
- The **SÜMBÜS FUSION** card opens the editor view directly.
- Inside FUSION, the three editor tabs (`.html` · `.css` · `.js`) switch between three different archetype-tinted syntax samples.

## What's faked

- The repo tree, GitHub API integration, real file diffs / merges, GSAP particles, and the full 11-system openSystem() router. The Architect's actual product has all of these live; this kit is a cosmetic recreation.
- Lucide icons. Source uses Lucide for chrome glyphs; here we use the brand emoji + unicode mix described in the root `README.md` → ICONOGRAPHY.

## Pulling components into a new design

```html
<link rel="stylesheet" href="../../colors_and_type.css">
<link rel="stylesheet" href="../../ui_kits/architect/styles.css">

<script src="…react…"></script>
<script src="…react-dom…"></script>
<script src="…babel…"></script>

<script type="text/babel" src="../../ui_kits/architect/components.jsx"></script>
<!-- now <AppHeader>, <SystemCard>, <Veeb>, etc are on window -->
```

Components stay simple and visual-first. They take props like `icon`, `name`, `body`, `hueClass`, `status`, `statusVariant` — no real data layer.
