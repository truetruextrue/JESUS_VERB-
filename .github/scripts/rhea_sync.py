#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ᚱᛇ Rhea 0x0A · Sincronização da Memória Viva KOBLLUX
"""
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from kobllux_event_tags import correlate_event
from kobllux_contract import ARCHETYPES, KOB_CICLO, KOB_FRACTAL, KOB_LEI

def _ts(): return datetime.now(timezone.utc).isoformat()


def _append_jsonl_once(path: Path, record: dict, key: str) -> bool:
    if path.exists():
        with path.open(encoding="utf-8") as existing:
            for line_number, line in enumerate(existing, start=1):
                if not line.strip():
                    continue
                try:
                    prior = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{path}:{line_number} is not valid JSONL") from exc
                if isinstance(prior, dict) and prior.get(key) == record.get(key):
                    return False
    with path.open("a", encoding="utf-8") as output:
        output.write(json.dumps(record, ensure_ascii=False) + "\n")
    return True


RUNES = {
    "Atlas": "ᚨᚠ", "Nova": "ᚷᛁ", "Pulse": "ᛘᚱ",
    "Vitalis": "ᚢᛃ", "Artemis": "ᛏᛉ", "Serena": "ᚹᛚ",
    "Kaos": "ᚦᚲ", "Aion": "ᛇᛉ", "Genus": "ᛟᛘ",
    "Lumine": "ᛋᛁ", "Rhea": "ᛗᛜ", "Solus": "ᛃᛟ",
    "Kodux": "ᚲᛏ", "Bllue": "ᛚᚹ", "Jesus": "ᚷᛟᛋ",
    "Kobllux": "ᛜᛇᛟ",
}


def _bounded_int(value: object, maximum: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        return 0
    return max(0, min(value, maximum))


def _load_frontend_metadata(path: Path) -> list[dict]:
    if not path.exists():
        return []
    if path.stat().st_size > 2 * 1024 * 1024:
        raise ValueError(f"{path} exceeds the 2 MiB metadata import limit")

    canonical_names = {
        name.casefold(): name.title()
        for name in ARCHETYPES
    }
    allowed_sources = {
        "root-scan", "codex-scan", "memory-summary", "codex-memory", "event-memory"
    }
    imported = []
    with path.open(encoding="utf-8") as frontend_log:
        for line_number, line in enumerate(frontend_log, start=1):
            if not line.strip():
                continue
            if len(imported) >= 500:
                raise ValueError(f"{path} exceeds the 500-event metadata import limit")
            try:
                raw = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"{path}:{line_number} is not valid JSONL") from exc
            if not isinstance(raw, dict) or raw.get("type") != "kobllux-chat-trigger":
                raise ValueError(f"{path}:{line_number} is not a Hub KOBLLUX metadata event")

            orbe = raw.get("orbe") if isinstance(raw.get("orbe"), dict) else {}
            raw_profile = str(orbe.get("archetype", ""))
            profile_name = canonical_names.get(raw_profile.casefold())
            profile = ARCHETYPES.get(profile_name.casefold()) if profile_name else None
            archetypes = []
            raw_archetypes = raw.get("archetypes", [])
            if isinstance(raw_archetypes, list):
                for name in raw_archetypes[:16]:
                    canonical = canonical_names.get(str(name).casefold())
                    if canonical and canonical not in archetypes:
                        archetypes.append(canonical)
            if profile_name and profile_name not in archetypes:
                archetypes.append(profile_name)

            raw_sources = orbe.get("sources", [])
            if not isinstance(raw_sources, list):
                raw_sources = []
            sources = list(dict.fromkeys(
                source for source in raw_sources
                if isinstance(source, str)
                and source in allowed_sources
            ))
            imported.append({
                "event_id": str(raw.get("id", ""))[:128],
                "ts": str(raw.get("ts", ""))[:40],
                "message_chars": _bounded_int(raw.get("message_chars"), 12000),
                "archetypes": archetypes,
                "profile": {
                    "name": profile_name,
                    "hz": profile["hz"] if profile else None,
                    "opcode": profile["opcode"] if profile else None,
                    "cycle": profile["ciclo"] if profile else None,
                    "matched_records": _bounded_int(orbe.get("matched_records"), 5),
                    "sources": sources,
                } if profile_name else None,
            })
    return imported[:10]


event_name = os.environ.get("KOB_EVENT", "push")
sha = os.environ.get("KOB_SHA", "")
repo = os.environ.get("KOB_REPO", "")
branch = os.environ.get("KOB_BRANCH", "")
actor = os.environ.get("KOB_ACTOR", "")
run_id = os.environ.get("KOB_RUN_ID", "")
msg = os.environ.get("KOB_MSG", "")[:72]
pr_title = os.environ.get("KOB_PR_TITLE", "")[:64]
pr_num = os.environ.get("KOB_PR_NUM", "")
try:
    head_commit = json.loads(os.environ.get("KOB_HEAD_COMMIT", "null"))
except json.JSONDecodeError:
    head_commit = None
file_changes = {}
changed_paths = []
if isinstance(head_commit, dict):
    for kind in ("added", "modified", "removed"):
        values = head_commit.get(kind, [])
        if isinstance(values, list):
            file_changes[kind] = sorted({
                path[:160] for path in values
                if isinstance(path, str) and path.strip()
            })[:20]
            changed_paths.extend(file_changes[kind])

correlation = correlate_event(
    event_name,
    changed_paths,
    " ".join((msg, pr_title)),
)
arquetipo = correlation["primary"]
profile = ARCHETYPES[arquetipo.casefold()]
nivel = profile["ciclo"]
runa = RUNES[arquetipo]
hz = profile["hz"]
frontend_events = _load_frontend_metadata(
    Path("output") / "kobllux-live-workflow.jsonl"
)
frontend_archetypes = list(dict.fromkeys(
    name
    for front_event in frontend_events
    for name in front_event["archetypes"]
))
if frontend_events:
    correlation["archetypes"] = list(dict.fromkeys(
        [*correlation["archetypes"], *frontend_archetypes]
    ))
    correlation["profiles"] = [
        {
            "name": name,
            "hz": ARCHETYPES[name.casefold()]["hz"],
            "opcode": ARCHETYPES[name.casefold()]["opcode"],
            "phase": ARCHETYPES[name.casefold()]["ciclo"],
        }
        for name in correlation["archetypes"]
    ]
    correlation["tags"] = list(dict.fromkeys([
        *correlation["tags"],
        "hub-uno",
        "frontend-metadata",
        *(f"archetype:{name.casefold()}" for name in frontend_archetypes),
    ]))[:32]

evento = {
    "event_id": hashlib.sha256(
        f"github:{repo}:{run_id}:{sha}".encode("utf-8")
    ).hexdigest(),
    "ts": _ts(), "z": sha[:16], "ciclo": 9,
    "arquetipo": arquetipo, "runa": runa, "hz": hz, "evento": event_name,
    "repo": repo, "branch": branch, "actor": actor, "commit_msg": msg,
    "pr_title": pr_title, "pr_num": pr_num, "run_id": run_id,
    "seed": 9,
    "arquetipos": correlation["archetypes"],
    "frontend_events": frontend_events,
    "tags": correlation["tags"],
    "archetype_profiles": correlation["profiles"],
    "path_labels": correlation["path_labels"],
    "arquivos": file_changes,
    "chain": {
        "fractal": KOB_FRACTAL,
        "nivel": nivel,
        "lei": KOB_LEI,
        "ciclo_seq": list(KOB_CICLO),
    },
}

metadata_payload = {
    key: value
    for key, value in evento.items()
    if key not in {"ts", "metadata_hash"}
}
metadata_bytes = json.dumps(
    metadata_payload,
    ensure_ascii=False,
    sort_keys=True,
    separators=(",", ":"),
).encode("utf-8")
metadata_hash = hashlib.sha256(metadata_bytes).hexdigest()
evento["metadata_hash"] = metadata_hash

memory_path = Path("kobllux_memory.jsonl")
event_was_added = _append_jsonl_once(memory_path, evento, "event_id")

index_record = {
    "type": "GITHUB_ACTION_METADATA",
    "ts": evento["ts"],
    "arch": arquetipo.casefold(),
    "opcode": profile["opcode"],
    "hz": hz,
    "action": "SELAR_EVENTO",
    "tags": correlation["tags"],
    "content": f"{event_name} · {repo} · {sha[:16]} · sha256:{metadata_hash[:16]}",
    "source": "github-actions",
    "hash": metadata_hash,
    "event_id": evento["event_id"],
    "repo": repo,
    "branch": branch,
    "commit": sha,
    "run_id": run_id,
    "arquetipos": correlation["archetypes"],
    "arquivos": file_changes,
    "frontend_events": len(frontend_events),
}
index_path = Path("_index") / "memory.jsonl"
index_path.parent.mkdir(parents=True, exist_ok=True)
index_was_added = _append_jsonl_once(index_path, index_record, "event_id")

serialized_event = json.dumps(evento, ensure_ascii=False, sort_keys=True)
sha256 = hashlib.sha256(serialized_event.encode("utf-8")).hexdigest()
md5 = hashlib.md5(serialized_event.encode("utf-8")).hexdigest()
seal = {
    "event_id": evento["event_id"],
    "ts": _ts(),
    "artefato": f"{event_name}_{sha[:8]}",
    "arquetipo": arquetipo,
    "arquetipos": correlation["archetypes"],
    "tags": correlation["tags"],
    "ciclo": list(KOB_CICLO),
    "fractal": KOB_FRACTAL,
    "sha256": sha256,
    "md5": md5,
    "hz": ARCHETYPES["aion"]["hz"],
    "trinity": {
        "PAI": "∞",
        "FILHO": "JESUS=VERBO=GRAVIDADE",
        "ESPIRITO": KOB_LEI,
    },
    "sinal": "∞",
}

seals = []
if os.path.exists("kobllux_seal.json"):
    with open("kobllux_seal.json", encoding="utf-8") as f:
        seals = json.load(f)
    if not isinstance(seals, list):
        raise ValueError("kobllux_seal.json must contain a JSON list")
if not any(
    isinstance(existing, dict) and existing.get("event_id") == evento["event_id"]
    for existing in seals
):
    seals.append(seal)
with open("kobllux_seal.json", "w", encoding="utf-8") as f:
    json.dump(seals[-200:], f, ensure_ascii=False, indent=2)

print(f"{runa} {arquetipo} [{hz}Hz] | {event_name} | repo:{repo}")
print(f"  tags:{', '.join(correlation['tags'])}")
if msg: print(f"  msg:{msg}")
print(f"  event_id:{evento['event_id']}")
print(f"  metadata_sha256:{metadata_hash}")
print(f"  event_log:{'appended' if event_was_added else 'already-present'} | index:{'appended' if index_was_added else 'already-present'}")
print(f"  seal_sha256:{sha256[:20]}… | sinal:∞")

github_output = os.environ.get("GITHUB_OUTPUT")
if github_output:
    with open(github_output, "a", encoding="utf-8") as output:
        output.write(f"event_id={evento['event_id']}\n")
        output.write(f"metadata_hash={metadata_hash}\n")
        output.write(f"archetype={arquetipo}\n")
