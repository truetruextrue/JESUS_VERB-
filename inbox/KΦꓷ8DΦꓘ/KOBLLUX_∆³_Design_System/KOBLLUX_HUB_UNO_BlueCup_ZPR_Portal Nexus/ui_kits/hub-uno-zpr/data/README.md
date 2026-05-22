# ui_kits/hub-uno-zpr/data

Payloads extraídos de blocos `<script type="application/json">` do monolito.

| Arquivo | Origem | Consumidores |
|---|---|---|
| `apps.json` | HUB UNO v12 #8 `<script id="APPS_JSON">` | `09-apps-store.js`, renderer de `v-apps` |

No `index.html` o conteúdo é reembutido inline dentro de `<script id="APPS_JSON" type="application/json">…</script>` para que `JSON.parse(document.getElementById('APPS_JSON').textContent)` funcione sem `fetch`.
