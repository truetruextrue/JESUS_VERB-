#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_status.py · MYRMIDE · Web Panel Status Generator · ∆7
Gera status.json para o painel_myrmide.html validar o ecossistema.

Uso:
  python3 build_status.py           # gera status.json
  python3 build_status.py --quiet   # sem saída verbose
  python3 build_status.py --watch   # monitora em loop
"""
from __future__ import annotations

import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/sdcard/JESUS_VERBO/CODEX/MYRMIDE")
OUT  = BASE / "03_MANIFESTO" / "VIEW" / "painel"

CHECKS = [
    ("memory.jsonl",    BASE / "02_PONTE" / "BANK" / "memory.jsonl"),
    ("01_SEMENTE",      BASE / "01_SEMENTE"),
    ("02_PONTE",        BASE / "02_PONTE"),
    ("03_MANIFESTO",    BASE / "03_MANIFESTO"),
    ("SEALS/items",     BASE / "SEALS" / "items"),
    ("SCI-ART seeds",   BASE / "02_PONTE" / "BANK" / "SEEDS" / "SCI_ART" / "original"),
    ("voices.json",     BASE / "CFG" / "voices.json"),
    ("archetypes.json", BASE / "CFG" / "archetypes.json"),
    ("integrator",      BASE / "SCRIPTS" / "myrmide_integrator.py"),
    ("verify",          BASE / "SCRIPTS" / "myrmide_verify.py"),
    ("pipeline",        BASE / "SCRIPTS" / "myrmide_pipeline.sh"),
    ("sciart_tools",    BASE / "SCRIPTS" / "sciart_tools.py"),
]


def build() -> dict:
    ts      = datetime.now(timezone.utc).isoformat()
    items   = []
    all_ok  = True

    for label, path in CHECKS:
        exists = path.exists()
        detail = ""
        if exists:
            if path.is_file() and path.suffix == ".jsonl":
                try:
                    lines = sum(1 for _ in path.open(encoding="utf-8", errors="ignore"))
                    detail = f"{lines} registros"
                except Exception:
                    detail = "erro leitura"
            elif path.is_dir():
                count = sum(1 for _ in path.rglob("*") if _.is_file())
                detail = f"{count} arquivo(s)"
            elif path.is_file():
                detail = f"{path.stat().st_size} bytes"
        else:
            all_ok = False

        items.append({
            "label":  label,
            "ok":     exists,
            "status": "VALIDADO" if exists else "PENDENTE",
            "detail": detail,
            "path":   str(path),
        })

    # SCI-ART pair/triple seals
    seals_dir = BASE / "SEALS" / "items"
    pair_seals   = list(seals_dir.glob("*.pair.json"))   if seals_dir.exists() else []
    triple_seals = list(seals_dir.glob("*.triple.json")) if seals_dir.exists() else []

    # memory stats
    mem_path = BASE / "02_PONTE" / "BANK" / "memory.jsonl"
    mem_stats: dict = {}
    if mem_path.exists():
        from collections import Counter
        types: Counter = Counter()
        for line in mem_path.open(encoding="utf-8", errors="ignore"):
            try:
                r = json.loads(line)
                types[r.get("type", "?")] += 1
            except Exception:
                pass
        mem_stats = dict(types.most_common())

    status = {
        "ts":           ts,
        "all_ok":       all_ok,
        "checks":       items,
        "pair_seals":   len(pair_seals),
        "triple_seals": len(triple_seals),
        "memory_stats": mem_stats,
        "seal":         "∆7",
        "law":          "VERDADE × INTEGRAR ÷ Δ = ∞",
    }

    OUT.mkdir(parents=True, exist_ok=True)
    out_path = OUT / "status.json"
    out_path.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")
    return status


def main():
    p = argparse.ArgumentParser(description="MYRMIDE build_status · ∆7")
    p.add_argument("--quiet", action="store_true")
    p.add_argument("--watch", action="store_true", help="Monitora e regenera a cada 30s")
    args = p.parse_args()

    def run_once():
        s = build()
        if not args.quiet:
            ok_count = sum(1 for c in s["checks"] if c["ok"])
            total    = len(s["checks"])
            flag     = "✓" if s["all_ok"] else "⚠"
            print(f"[BUILD_STATUS] {flag} {ok_count}/{total} checks OK · {s['ts'][:19]}")
            for c in s["checks"]:
                sym = "✓" if c["ok"] else "✗"
                detail = f"  ({c['detail']})" if c["detail"] else ""
                print(f"  {sym} {c['label']:20s} {c['status']}{detail}")
            if s["pair_seals"]:
                print(f"  ✓ SCI-ART pair seals: {s['pair_seals']}")
            if s["triple_seals"]:
                print(f"  ✓ SCI-ART triple seals: {s['triple_seals']}")
            if s["memory_stats"]:
                print(f"  Memória: {s['memory_stats']}")

    if args.watch:
        print("[WATCH] Monitorando — Ctrl+C para parar")
        while True:
            run_once()
            time.sleep(30)
    else:
        run_once()


if __name__ == "__main__":
    main()
