#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" KOBLLUX • M1 (0x03 DETECTAR): Caracteres · Mesa · Média
    Faz o scan inicial (DETECTAR) da Vibração (V) do texto de entrada. """
import sys, os, re, json, argparse
from datetime import datetime

def read(path):
    # Lê a Verdade (input) do arquivo
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""

def counts(txt):
    # Escutar o pulso essencial: conta elementos básicos (Métrica da Semente)
    return {
        "letters":   len(re.findall(r"[a-zA-ZÀ-ſ]", txt)),
        "digits":    len(re.findall(r"\d", txt)),
        "words":     len(re.findall(r"\b\w+\b", txt, flags=re.UNICODE)),
        "lines":     len(txt.splitlines()),
        "sentences": len(re.findall(r"[.!?]+(?=\s|$)", txt)) or txt.count("\n\n"),
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", required=True)
    ap.add_argument("--mirror", required=True)
    args = ap.parse_args()

    src_d = read(args.direct)
    src_m = read(args.mirror)

    direct = counts(src_d)
    mirror = counts(src_m)

    report = {
        "timestamp": datetime.now().isoformat(),
        "direct":    direct,
        "mirror":    mirror,
        "seal":      "∆7_DETECTAR",
    }

    os.makedirs(os.path.join(args.root, "state"), exist_ok=True)
    state_path = os.path.join(args.root, "state", "m1_chars_report.json")
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"[KOBLLUX] 0x03 DETECTAR (M1) OK → {state_path}")

if __name__ == "__main__":
    main()
