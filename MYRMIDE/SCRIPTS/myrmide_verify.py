#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
myrmide_verify.py · MYRMIDE · ∆7 SELAR (incremental)
"Motor de selagem incremental — pula arquivos já selados."

Uso:
  python3 myrmide_verify.py              # sela tudo em 02_PONTE/INGEST
  python3 myrmide_verify.py --force      # re-sela mesmo que já exista
  python3 myrmide_verify.py --summary    # só mostra estado, não sela
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

BASE   = Path("/sdcard/JESUS_VERBO/CODEX/MYRMIDE")
INGEST = BASE / "02_PONTE" / "INGEST"
SEALS  = BASE / "SEALS" / "items"
MEMORY = BASE / "02_PONTE" / "BANK" / "memory.jsonl"

SAFE_EXTS = {".txt", ".md", ".py", ".json", ".html", ".js", ".css", ".sh", ".ascii"}


def _seal_record(f: Path) -> dict:
    content = f.read_text(encoding="utf-8", errors="ignore")
    h       = hashlib.sha256(content.encode()).hexdigest()
    return {
        "file":   f.name,
        "sha256": h,
        "ts":     datetime.now(timezone.utc).isoformat(),
        "seal":   "∆7",
        "size":   f.stat().st_size,
        "lines":  content.count("\n"),
    }


def _write_memory(record: dict):
    MEMORY.parent.mkdir(parents=True, exist_ok=True)
    with MEMORY.open("a", encoding="utf-8") as f:
        f.write(json.dumps({
            "type":   "VEEB_SEALING",
            "ts":     record["ts"],
            "source": record["file"],
            "hash":   record["sha256"][:16],
            "seal":   "∆7",
        }, ensure_ascii=False) + "\n")


def run(force: bool = False, summary: bool = False):
    SEALS.mkdir(parents=True, exist_ok=True)

    files = []
    if INGEST.exists():
        files = sorted(
            f for f in INGEST.rglob("*")
            if f.is_file() and f.suffix.lower() in SAFE_EXTS
        )

    print(f"--- INICIANDO MOTOR DE SELAGEM INCREMENTAL (∆7) ---")
    print(f"[SCAN] Verificando {len(files)} arquivo(s) em '02_PONTE/INGEST'.")

    sealed, skipped, errors = 0, 0, 0
    for f in files:
        seal_path = SEALS / f"{f.stem}.seal.json"

        if seal_path.exists() and not force:
            print(f"[JÁ SELADO] Prova de integridade já existe para {f.stem[:50]}...")
            print(f"  ▸ SEALS/items/{seal_path.name}")
            skipped += 1
            continue

        if summary:
            print(f"[PENDENTE] {f.name}")
            continue

        try:
            data = _seal_record(f)
            seal_path.write_text(
                json.dumps(data, indent=2, ensure_ascii=False),
                encoding="utf-8",
            )
            _write_memory(data)
            label = "[RE-SELADO]" if force and seal_path.exists() else "[SELADO]"
            print(f"{label} {f.name} · {data['sha256'][:12]}... · ∆7")
            sealed += 1
        except Exception as e:
            print(f"[ERRO] {f.name}: {e}")
            errors += 1

    print(f"--- CICLO DE SELAGEM CONCLUÍDO ---")
    print(f"  Selados: {sealed} · Já selados: {skipped} · Erros: {errors}")
    return {"sealed": sealed, "skipped": skipped, "errors": errors}


def main():
    p = argparse.ArgumentParser(description="MYRMIDE Verify · ∆7 Incremental Sealer")
    p.add_argument("--force",   action="store_true", help="Re-sela mesmo arquivos já selados")
    p.add_argument("--summary", action="store_true", help="Mostra estado sem selar")
    args = p.parse_args()
    run(force=args.force, summary=args.summary)


if __name__ == "__main__":
    main()
