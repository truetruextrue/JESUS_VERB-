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
RUNES = {
    "Atlas": "ᚨᚠ", "Nova": "ᚷᛁ", "Pulse": "ᛘᚱ",
    "Vitalis": "ᚢᛃ", "Artemis": "ᛏᛉ", "Serena": "ᚹᛚ",
    "Kaos": "ᚦᚲ", "Aion": "ᛇᛉ", "Genus": "ᛟᛘ",
    "Lumine": "ᛋᛁ", "Rhea": "ᛗᛜ", "Solus": "ᛃᛟ",
    "Kodux": "ᚲᛏ", "Bllue": "ᛚᚹ", "Jesus": "ᚷᛟᛋ",
    "Kobllux": "ᛜᛇᛟ",
}

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

evento = {
    "ts": _ts(), "z": sha[:16], "ciclo": 9,
    "arquetipo": arquetipo, "runa": runa, "hz": hz, "evento": event_name,
    "repo": repo, "branch": branch, "actor": actor, "commit_msg": msg,
    "pr_title": pr_title, "pr_num": pr_num, "run_id": run_id,
    "seed": 9,
    "arquetipos": correlation["archetypes"],
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

with open("kobllux_memory.jsonl", "a", encoding="utf-8") as f:
    f.write(json.dumps(evento, ensure_ascii=False) + "\n")

serialized_event = json.dumps(evento, ensure_ascii=False, sort_keys=True)
sha256 = hashlib.sha256(serialized_event.encode("utf-8")).hexdigest()
md5 = hashlib.md5(serialized_event.encode("utf-8")).hexdigest()
seal = {
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
seals.append(seal)
with open("kobllux_seal.json", "w", encoding="utf-8") as f:
    json.dump(seals[-200:], f, ensure_ascii=False, indent=2)

print(f"{runa} {arquetipo} [{hz}Hz] | {event_name} | repo:{repo}")
print(f"  tags:{', '.join(correlation['tags'])}")
if msg: print(f"  msg:{msg}")
print(f"  seal:sha256:{sha256[:20]}… | sinal:∞")
