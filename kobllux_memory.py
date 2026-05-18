#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_memory.py · AION · 0×0B · TEMPORIZAR · 741Hz
"O guardião do tempo e da memória sagrada."

API unificada de memória KOBLLUX.
Lida por: Roda Viva, 78K-motor, hooks, archetypes, auto-session.
Grava em: _index/memory.jsonl

Uso:
    from kobllux_memory import KoblluxMemory
    mem = KoblluxMemory()
    mem.write(arch="atlas", content="...", tags=["estrutura"])
    records = mem.read(arch="atlas", limit=10)
    context = mem.context_for_motor(n=20)
"""
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).parent
MEMORY_FILE = ROOT / "_index" / "memory.jsonl"
COMMIT_LOG  = ROOT / "_index" / "COMMIT_LOG_∆7.jsonl"

ARCHETYPES_META = {
    "atlas":   {"opcode":"0x0A","hz":528, "sym":"⬡","action":"ESTRUTURAR"},
    "nova":    {"opcode":"0x01","hz":432, "sym":"✦","action":"DETECTAR"},
    "vitalis": {"opcode":"0x08","hz":639, "sym":"◉","action":"PULSAR"},
    "pulse":   {"opcode":"0x04","hz":594, "sym":"≋","action":"LAPIDAR"},
    "artemis": {"opcode":"0x05","hz":672, "sym":"◎","action":"CONVERGIR"},
    "serena":  {"opcode":"0x02","hz":528, "sym":"❋","action":"INTEGRAR"},
    "kaos":    {"opcode":"0x07","hz":777, "sym":"⚡","action":"SELAR"},
    "genus":   {"opcode":"0x0B","hz":852, "sym":"⬢","action":"TEMPORIZAR"},
    "lumine":  {"opcode":"0x0C","hz":963, "sym":"☀","action":"TRANSCENDER"},
    "solus":   {"opcode":"0x01","hz":432, "sym":"◈","action":"DETECTAR"},
    "rhea":    {"opcode":"0x09","hz":528, "sym":"∞","action":"FLUIR"},
    "aion":    {"opcode":"0x0B","hz":639, "sym":"⧗","action":"TEMPORIZAR"},
    "kodux":   {"opcode":"0x01","hz":432, "sym":"●","action":"DETECTAR"},
    "bllue":   {"opcode":"0x02","hz":528, "sym":"―","action":"INTEGRAR"},
    "kobllux": {"opcode":"0x00","hz":768, "sym":"○","action":"ORIGEM"},
}


class KoblluxMemory:
    """Memória viva KOBLLUX — leitura, escrita e síntese."""

    def __init__(self, path: Path = MEMORY_FILE):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    # ── ESCRITA ────────────────────────────────────────────────────────────────

    def write(
        self,
        arch: str = "kobllux",
        content: str = "",
        tags: list[str] | None = None,
        source: str = "",
        record_type: str = "INTERACTION",
        extra: dict | None = None,
    ) -> dict:
        """Grava um registro na memória viva."""
        meta = ARCHETYPES_META.get(arch.lower(), ARCHETYPES_META["kobllux"])
        ts   = datetime.now(timezone.utc).isoformat()
        h    = hashlib.sha256(f"{ts}{content}".encode()).hexdigest()[:16]

        record: dict[str, Any] = {
            "type":    record_type,
            "ts":      ts,
            "arch":    arch.lower(),
            "opcode":  meta["opcode"],
            "hz":      meta["hz"],
            "sym":     meta["sym"],
            "action":  meta["action"],
            "tags":    tags or [],
            "content": content[:1200],    # máx 1200 chars por registro
            "source":  source,
            "seal":    "∆7",
            "hash":    h,
        }
        if extra:
            record.update(extra)

        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

        return record

    # ── LEITURA ────────────────────────────────────────────────────────────────

    def read(
        self,
        arch: str | None = None,
        record_type: str | None = None,
        limit: int = 50,
        reverse: bool = True,
    ) -> list[dict]:
        """Lê registros da memória. Filtra por arquétipo e/ou tipo."""
        records: list[dict] = []
        if not self.path.exists():
            return records

        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if arch and r.get("arch", "").lower() != arch.lower():
                    continue
                if record_type and r.get("type", "").upper() != record_type.upper():
                    continue
                records.append(r)

        if reverse:
            records = records[::-1]
        return records[:limit]

    def read_all_recent(self, limit: int = 100) -> list[dict]:
        return self.read(limit=limit, reverse=True)

    # ── SÍNTESE PARA O MOTOR ───────────────────────────────────────────────────

    def context_for_motor(self, n: int = 20) -> str:
        """
        Retorna um bloco de texto pronto para ser injetado como contexto
        no 78K-motor ou no chat KxaT. Formato ARCH — conteúdo.
        """
        records = self.read_all_recent(limit=n)
        if not records:
            return ""
        lines = []
        for r in reversed(records):
            arch = r.get("arch", "kobllux").upper()
            sym  = r.get("sym", "○")
            content = r.get("content", "").replace("\n", " ").strip()
            if content:
                lines.append(f"{sym} {arch} — {content[:200]}")
        return "\n".join(lines)

    def tags_frequency(self, limit: int = 200) -> dict[str, int]:
        """Frequência de tags em toda a memória."""
        from collections import Counter
        counter: Counter = Counter()
        records = self.read_all_recent(limit=limit)
        for r in records:
            for tag in r.get("tags", []):
                counter[tag] += 1
        return dict(counter.most_common(30))

    def arch_summary(self) -> dict[str, int]:
        """Quantos registros por arquétipo."""
        from collections import Counter
        counter: Counter = Counter()
        records = self.read_all_recent(limit=500)
        for r in records:
            counter[r.get("arch", "??")] += 1
        return dict(counter.most_common())

    # ── MERGE DE FONTES EXTERNAS ───────────────────────────────────────────────

    def ingest_commit_log(self) -> int:
        """Importa novos commits do COMMIT_LOG_∆7.jsonl que ainda não estão na memória."""
        if not COMMIT_LOG.exists():
            return 0

        existing_hashes = {
            r.get("extra_hash") or r.get("hash")
            for r in self.read(record_type="COMMIT", limit=1000)
        }

        added = 0
        with COMMIT_LOG.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    c = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if c.get("hash") in existing_hashes:
                    continue

                self.write(
                    arch=c.get("arch", "kobllux"),
                    content=c.get("msg", ""),
                    tags=[c.get("action", ""), c.get("branch", ""), "git-commit"],
                    source="COMMIT_LOG_∆7.jsonl",
                    record_type="COMMIT",
                    extra={
                        "extra_hash": c.get("hash"),
                        "files": c.get("files", 0),
                        "branch": c.get("branch", ""),
                    },
                )
                added += 1

        return added

    # ── EXPORT ────────────────────────────────────────────────────────────────

    def export_for_localStorage(self, n: int = 30) -> str:
        """
        Exporta os últimos N registros como JSON string
        para ser colada no localStorage do KxaT/78K-motor:
          localStorage.setItem('KBLX_MEMORY', JSON.parse(...))
        """
        records = self.read_all_recent(limit=n)
        return json.dumps(records, ensure_ascii=False, indent=2)

    def stats(self) -> dict:
        records = self.read_all_recent(limit=1000)
        return {
            "total": len(records),
            "by_arch": self.arch_summary(),
            "top_tags": self.tags_frequency(),
            "path": str(self.path),
        }
