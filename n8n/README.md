# KOBLLUX shared-memory integration

This integration has three real components:

1. `kobllux_memory_proxy.py` is an authenticated relay. It binds to loopback by
   default, enforces an origin allowlist and payload limits, and keeps n8n's
   credential on the server side.
2. `workflows/KOBLLUX_MEMORY_INGEST.json` validates events and inserts them
   idempotently into PostgreSQL.
3. `migrations/001_kobllux_interactions.sql` creates the shared event table and
   indexes.

The proxy and n8n/PostgreSQL are not deployed by importing these source files.
Do not expose the proxy directly to the internet: put it behind an HTTPS
reverse proxy with rate limiting, and set an exact `KOBLLUX_ALLOWED_ORIGINS`
origin. Generate independent random proxy and n8n credentials outside the
repository.

## n8n setup

1. Apply `migrations/001_kobllux_interactions.sql` to the intended PostgreSQL
   database.
2. Import `workflows/KOBLLUX_MEMORY_INGEST.json`.
3. Attach an n8n **Basic Auth** credential to `Authenticated Memory Webhook`.
   Set the same username/password in the proxy environment.
4. Attach the intended PostgreSQL credential to `Persist Idempotently in
   PostgreSQL`.
5. Test the imported workflow, then activate it. Its production path is
   `/webhook/kobllux-memory`.

The workflow is inactive on import and has no embedded credentials.

## Proxy configuration

Configure these values in the proxy's secret/environment manager, not in Git:

- `KOBLLUX_PROXY_TOKEN`: at least 32 random characters; browser/GitHub clients
  use this bearer token.
- `KOBLLUX_N8N_WEBHOOK_URL`: the n8n production webhook URL, HTTPS outside
  localhost.
- `KOBLLUX_N8N_WEBHOOK_USER` and `KOBLLUX_N8N_WEBHOOK_PASSWORD`: n8n webhook
  Basic Auth credential.
- `KOBLLUX_ALLOWED_ORIGINS`: comma-separated exact browser origins, for example
  `https://truetruextrue.github.io`.
- Optional `KOBLLUX_PROXY_HOST` and `KOBLLUX_PROXY_PORT` (defaults:
  `127.0.0.1:3698`).

Run `python3 kobllux_memory_proxy.py` under a process manager. The HTTP listener
binds to loopback by default; terminate TLS and enforce rate limits at the
reverse proxy. Never use wildcard CORS for this endpoint.

## GitHub Actions

Set repository Actions secrets `KOBLLUX_MEMORY_PROXY_URL` (the proxy's
`/events` URL) and `KOBLLUX_PROXY_TOKEN`. Once set, the Malha Viva workflow
forwards the Rhea event to PostgreSQL in addition to its append-only JSONL
record. The proxy must be reachable by GitHub-hosted runners through its
HTTPS reverse proxy; a private loopback-only service cannot receive workflow
traffic. A missing secret prevents the optional forward step from running;
the local repository memory remains intact. Push events include up to 20
changed paths per added/modified/removed category; file contents are not
forwarded, and canonical archetypes are detected from paths and event text.

## SÜMBÜS Fusion

In Hypervision, enable local memory only after its consent prompt. Shared
sync is a separate opt-in: enter the proxy `/events` URL and bearer token in
the memory settings. The URL is stored in this browser; the bearer token is
kept in `sessionStorage` for the current browser tab. Each explicitly sent
chat exchange is stored locally (up to 50 records) and, when shared sync is
enabled, posted to the proxy. The editor code injected into a prompt is not
stored as a separate field. Export and erase controls remain available.

Other browser origins, VS Code/Copilot conversations, WhatsApp, and unrelated
localStorage databases are not read automatically. Each requires its own
explicit connector and consent. File Library uploads are covered as GitHub
push events; browsing, previewing, and downloads are not sent as separate
events.
