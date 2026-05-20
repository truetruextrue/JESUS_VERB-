#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
myrmide_integrator.py · MYRMIDE · VEEB_INTEGRATION · ∆7
"Processa um arquivo: move para INTAKE, registra na memória viva."

Pipeline: arquivo → 01_SEMENTE/INTAKE → memory.jsonl (VEEB_INTEGRATION)

Uso:
  python3 myrmide_integrator.py ~/nova_verdade.txt
  python3 myrmide_integrator.py ~/arquivo.txt --arch atlas
  python3 myrmide_integrator.py ~/arquivo.txt --dry-run
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

BASE = Path("/sdcard/JESUS_VERBO/CODEX/MYRMIDE")

ARCH_PATTERNS = {
    "atlas":   r"estrutur|config|readme|schema|grade|organiz|manifest",
    "nova":    r"início|começ|criar|gerar|novo|spark|faísca",
    "vitalis": r"energia|orgânico|núcleo|vivo|pulsant|vital",
    "pulse":   r"ritmo|batida|tts|voz|audio|emoção",
    "serena":  r"integrar|ui|suave|acolh|calma|serena",
    "kaos":    r"ruptura|patch|fix|override|bug|erro|falha",
    "lumine":  r"luz|visual|tema|efeito|clareza|iluminação",
    "aion":    r"tempo|memória|log|história|estado|ciclo",
    "atlas":   r"estrutur|base|fundação|index|mapa",
}


def detect_arch(text: str) -> str:
    from collections import Counter
    scores: Counter = Counter()
    tl = text.lower()
    for arch, pat in ARCH_PATTERNS.items():
        m = len(re.findall(pat, tl, re.I))
        if m:
            scores[arch] += m
    return scores.most_common(1)[0][0] if scores else "kobllux"


def integrar(src_path: Path, forced_arch: str | None, dry_run: bool) -> dict:
    content = src_path.read_text(encoding="utf-8", errors="ignore")
    arch    = forced_arch or detect_arch(content)
    h       = hashlib.sha256(content.encode()).hexdigest()[:16]
    ts      = datetime.now(timezone.utc).isoformat()

    intake  = BASE / "01_SEMENTE" / "INTAKE"
    dst     = intake / src_path.name

    record = {
        "type":    "VEEB_INTEGRATION",
        "ts":      ts,
        "arch":    arch,
        "source":  src_path.name,
        "hash":    h,
        "seal":    "∆7",
        "content": content[:400].replace("\n", " "),
        "size":    src_path.stat().st_size,
    }

    if not dry_run:
        intake.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dst)
        mem = BASE / "02_PONTE" / "BANK" / "memory.jsonl"
        mem.parent.mkdir(parents=True, exist_ok=True)
        with mem.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")

    tag = "[DRY-RUN]" if dry_run else "[INTEGRAÇÃO]"
    print(f"{tag} {src_path.name} → {arch.upper()} · {h}")
    print(f"  ▸ 01_SEMENTE/INTAKE/{src_path.name}")
    print(f"[REGISTRO] Evento selado na memória viva.")
    print(f"  ▸ memory.jsonl")
    return record


def main():
    p = argparse.ArgumentParser(description="MYRMIDE Integrator · VEEB_INTEGRATION · ∆7")
    p.add_argument("file",      help="Arquivo a integrar")
    p.add_argument("--arch",    help="Força arquétipo (atlas, kaos, aion…)")
    p.add_argument("--dry-run", action="store_true", help="Não grava nada")
    args = p.parse_args()

    src = Path(args.file)
    if not src.exists():
        print(f"[ERRO] Arquivo não encontrado: {src}", file=sys.stderr)
        sys.exit(1)

    integrar(src, args.arch, args.dry_run)


if __name__ == "__main__":
    main()
