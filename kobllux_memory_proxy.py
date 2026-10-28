#!/usr/bin/env python3
"""Authenticated local relay from KOBLLUX clients to an n8n memory webhook."""

from __future__ import annotations

import argparse
import base64
import hmac
import json
import os
from datetime import datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import re
import sys
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import HTTPRedirectHandler, Request, build_opener
import uuid

from kobllux_event_tags import correlate_event


ROOT = Path(__file__).resolve().parent
ARCHETYPES = {
    "ATLAS", "NOVA", "PULSE", "VITALIS", "ARTEMIS", "SERENA", "KAOS", "AION",
    "GENUS", "LUMINE", "RHEA", "SOLUS", "KODUX", "BLLUE", "JESUS", "KOBLLUX",
}
MAX_BODY_BYTES = 64 * 1024
MAX_TAGS = 32
MAX_TEXT_CHARS = 12_000
UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$",
    re.IGNORECASE,
)


def _required_env(name: str, minimum: int = 1) -> str:
    value = os.environ.get(name, "").strip()
    if len(value) < minimum:
        raise ValueError(f"{name} must be configured (minimum {minimum} characters)")
    return value


def _webhook_url() -> str:
    url = _required_env("KOBLLUX_N8N_WEBHOOK_URL")
    parsed = urlparse(url)
    if parsed.scheme != "https" and parsed.hostname not in {"localhost", "127.0.0.1"}:
        raise ValueError("KOBLLUX_N8N_WEBHOOK_URL must use HTTPS")
    if not parsed.hostname:
        raise ValueError("KOBLLUX_N8N_WEBHOOK_URL must include a host")
    return url


def validate_event(event: object) -> dict:
    if not isinstance(event, dict):
        raise ValueError("event must be a JSON object")
    event_id = str(event.get("event_id", ""))
    if not UUID_RE.fullmatch(event_id):
        raise ValueError("event_id must be a UUID")
    source = event.get("source")
    if source not in {"sumbus-fusion/hypervision", "github-actions"}:
        raise ValueError("source is not allowed")
    ts = event.get("ts")
    if not isinstance(ts, str) or len(ts) > 40:
        raise ValueError("ts must be an ISO timestamp")
    try:
        parsed_ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("ts must be an ISO timestamp") from exc
    if parsed_ts.tzinfo is None:
        raise ValueError("ts must include a timezone")
    archetypes = event.get("archetypes")
    if not isinstance(archetypes, list) or not archetypes or len(archetypes) > len(ARCHETYPES):
        raise ValueError("archetypes must contain one or more canonical names")
    normalized_arches = list(dict.fromkeys(str(name).upper() for name in archetypes))
    if any(name not in ARCHETYPES for name in normalized_arches):
        raise ValueError("archetypes contains a non-canonical name")
    tags = event.get("tags", [])
    if not isinstance(tags, list) or len(tags) > MAX_TAGS:
        raise ValueError("tags must be a list of at most 32 entries")
    normalized_tags = []
    for tag in tags:
        if not isinstance(tag, str) or not tag.strip() or len(tag) > 80:
            raise ValueError("each tag must be a non-empty string of at most 80 characters")
        normalized_tags.append(tag.strip()[:80])
    payload = event.get("payload")
    if not isinstance(payload, dict):
        raise ValueError("payload must be a JSON object")
    encoded_payload = json.dumps(payload, ensure_ascii=False)
    if len(encoded_payload) > MAX_TEXT_CHARS:
        raise ValueError("payload exceeds 12,000 characters")
    return {
        "event_id": event_id.lower(),
        "ts": ts,
        "source": source,
        "archetypes": normalized_arches,
        "tags": list(dict.fromkeys(normalized_tags)),
        "payload": payload,
    }


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def forward_to_n8n(event: dict) -> tuple[int, bytes]:
    url = _webhook_url()
    username = _required_env("KOBLLUX_N8N_WEBHOOK_USER")
    password = _required_env("KOBLLUX_N8N_WEBHOOK_PASSWORD", 16)
    credentials = base64.b64encode(f"{username}:{password}".encode()).decode("ascii")
    body = json.dumps(event, ensure_ascii=False).encode("utf-8")
    request = Request(
        url,
        data=body,
        headers={
            "Authorization": f"Basic {credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    opener = build_opener(NoRedirect)
    try:
        with opener.open(request, timeout=10) as response:
            return response.status, response.read(8 * 1024)
    except HTTPError as exc:
        return exc.code, exc.read(8 * 1024)
    except URLError as exc:
        raise RuntimeError(f"n8n webhook request failed: {exc.reason}") from exc


def build_handler(allowed_origins: set[str], proxy_token: str):
    class Handler(BaseHTTPRequestHandler):
        server_version = "KoblluxMemoryProxy/1"

        def log_message(self, fmt, *args):
            return

        def _send_json(self, status: int, payload: dict, origin: str | None = None):
            body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            if origin and origin in allowed_origins:
                self.send_header("Access-Control-Allow-Origin", origin)
                self.send_header("Vary", "Origin")
            self.end_headers()
            self.wfile.write(body)

        def do_OPTIONS(self):
            origin = self.headers.get("Origin")
            if not origin or origin not in allowed_origins:
                self._send_json(403, {"error": "origin is not allowed"})
                return
            self.send_response(204)
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
            self.send_header("Access-Control-Max-Age", "600")
            self.send_header("Content-Length", "0")
            self.end_headers()

        def do_POST(self):
            origin = self.headers.get("Origin")
            if origin and origin not in allowed_origins:
                self._send_json(403, {"error": "origin is not allowed"})
                return
            if self.path != "/events":
                self._send_json(404, {"error": "not found"}, origin)
                return
            supplied = self.headers.get("Authorization", "")
            expected = f"Bearer {proxy_token}"
            if not hmac.compare_digest(supplied, expected):
                self._send_json(401, {"error": "unauthorized"}, origin)
                return
            try:
                length = int(self.headers.get("Content-Length", "0"))
            except ValueError:
                self._send_json(400, {"error": "invalid content length"}, origin)
                return
            if length < 1 or length > MAX_BODY_BYTES:
                self._send_json(413, {"error": "request body size is invalid"}, origin)
                return
            try:
                event = validate_event(json.loads(self.rfile.read(length)))
                status, response_body = forward_to_n8n(event)
            except (UnicodeDecodeError, json.JSONDecodeError, ValueError) as exc:
                self._send_json(400, {"error": str(exc)}, origin)
                return
            except RuntimeError as exc:
                self._send_json(502, {"error": str(exc)}, origin)
                return
            if 200 <= status < 300:
                self._send_json(status, {"accepted": True, "event_id": event["event_id"]}, origin)
            else:
                self._send_json(502, {
                    "error": "n8n rejected the memory event",
                    "upstream_status": status,
                    "upstream_response": response_body.decode("utf-8", errors="replace")[:500],
                }, origin)

    return Handler


def forward_latest_github_event() -> None:
    token = _required_env("KOBLLUX_PROXY_TOKEN", 32)
    proxy_url = _required_env("KOBLLUX_MEMORY_PROXY_URL")
    parsed = urlparse(proxy_url)
    if parsed.scheme != "https" and parsed.hostname not in {"localhost", "127.0.0.1"}:
        raise ValueError("KOBLLUX_MEMORY_PROXY_URL must use HTTPS")
    if not parsed.path.rstrip("/").endswith("/events"):
        raise ValueError("KOBLLUX_MEMORY_PROXY_URL must end in /events")
    memory_path = ROOT / "kobllux_memory.jsonl"
    if not memory_path.is_file():
        raise FileNotFoundError(f"memory log not found: {memory_path}")
    event_line = next(
        (line for line in reversed(memory_path.read_text(encoding="utf-8").splitlines()) if line.strip()),
        None,
    )
    if not event_line:
        raise ValueError("memory log has no events to forward")
    source = json.loads(event_line)
    sha = str(source.get("z", ""))
    run_id = str(source.get("run_id", ""))
    event_id = str(uuid.uuid5(uuid.NAMESPACE_URL, f"github:{run_id}:{sha}"))
    file_changes = source.get("arquivos", {})
    file_paths = [
        path
        for kind in ("added", "modified", "removed")
        for path in file_changes.get(kind, [])
        if isinstance(path, str)
    ] if isinstance(file_changes, dict) else []
    text = " ".join(
        [*(str(source.get(key, "")) for key in ("commit_msg", "pr_title", "evento")), *file_paths]
    )
    correlation = correlate_event(
        str(source.get("evento", "event")),
        file_paths,
        text,
    )
    primary = str(source.get("arquetipo", "RHEA")).upper()
    if primary not in ARCHETYPES:
        primary = "RHEA"
    supplied_archetypes = source.get("arquetipos", [])
    if not isinstance(supplied_archetypes, list):
        supplied_archetypes = []
    archetypes = list(dict.fromkeys(
        [primary]
        + [str(name).upper() for name in supplied_archetypes if str(name).upper() in ARCHETYPES]
        + [name.upper() for name in correlation["archetypes"]]
    ))[:len(ARCHETYPES)]
    source_tags = source.get("tags", [])
    if not isinstance(source_tags, list):
        source_tags = []
    tags = list(dict.fromkeys([
        *(tag for tag in source_tags if isinstance(tag, str)),
        *correlation["tags"],
    ]))[:MAX_TAGS]
    event = validate_event({
        "event_id": event_id,
        "ts": source.get("ts"),
        "source": "github-actions",
        "archetypes": archetypes,
        "tags": tags,
        "payload": {
            "event": source.get("evento"),
            "repository": source.get("repo"),
            "branch": source.get("branch"),
            "actor": source.get("actor"),
            "commit": sha,
            "commit_message": source.get("commit_msg"),
            "pull_request_title": source.get("pr_title"),
            "pull_request_number": source.get("pr_num"),
            "run_id": run_id,
            "metadata_hash": source.get("metadata_hash"),
            "changed_files": file_changes,
            "seal": source.get("chain"),
            "archetype_profiles": source.get(
                "archetype_profiles",
                correlation["profiles"],
            ),
            "path_labels": source.get("path_labels", correlation["path_labels"]),
            "frontend_events": source.get("frontend_events", []),
            "cycle": correlation["cycle"],
            "fractal": correlation["fractal"],
        },
    })
    body = json.dumps(event, ensure_ascii=False).encode("utf-8")
    request = Request(
        proxy_url,
        data=body,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    with build_opener(NoRedirect).open(request, timeout=15) as response:
        result = json.loads(response.read(8 * 1024).decode("utf-8"))
    if not result.get("accepted") or result.get("event_id") != event_id:
        raise RuntimeError("proxy did not confirm the GitHub event")
    print(f"Memory event forwarded: {event_id} · {', '.join(archetypes)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default=os.environ.get("KOBLLUX_PROXY_HOST", "127.0.0.1"))
    parser.add_argument("--port", type=int, default=int(os.environ.get("KOBLLUX_PROXY_PORT", "3698")))
    parser.add_argument("--forward-latest-github", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.forward_latest_github:
            forward_latest_github_event()
            return 0
        token = _required_env("KOBLLUX_PROXY_TOKEN", 32)
        webhook = _webhook_url()
        _required_env("KOBLLUX_N8N_WEBHOOK_USER")
        _required_env("KOBLLUX_N8N_WEBHOOK_PASSWORD", 16)
        allowed_origins = {
            origin.strip().rstrip("/")
            for origin in os.environ.get("KOBLLUX_ALLOWED_ORIGINS", "").split(",")
            if origin.strip()
        }
        server = ThreadingHTTPServer(
            (args.host, args.port),
            build_handler(allowed_origins, token),
        )
        print(
            f"KOBLLUX memory proxy listening on {args.host}:{args.port}; "
            f"n8n target {urlparse(webhook).netloc}",
            flush=True,
        )
        server.serve_forever()
    except (OSError, ValueError, RuntimeError, HTTPError, URLError, json.JSONDecodeError) as exc:
        print(f"memory proxy error: {exc}", file=sys.stderr, flush=True)
        return 1
    except KeyboardInterrupt:
        print("\nMemory proxy stopped.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
