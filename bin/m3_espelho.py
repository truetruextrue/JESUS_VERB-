#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX • M3 (ESPELHO): símbolo
- Lê M1 e M2 para contexto
- Conta classes de símbolos e valida vestígios A/B/C/D
Saídas:
  state/m3_symbol_report.json
  cards/M3_SYMBOL_CARD.md
"""
import sys, os, re, json, argparse
from datetime import datetime
from collections import Counter

SYM_MATH   = set(list("+-=×÷*/^()[]{}∆∞♾∴∵<>≥≤±%"))
SYM_ARROWS = set(list("→←↔↕⇄⇆⇒⇐⇔↑↓"))
SYM_BOX    = set(list("╔═╗║╚╝╩╦╠╣╬█▀▄▌▐"))
SYM_STARS  = set(list("★☆✦✧✪✫✬✭✮✯⼺"))
SYM_SEAL   = set(list("∆⁷♾"))

def read(path):
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""

def count_symbols(txt):
    c = Counter()
    for ch in txt:
        if ch in SYM_MATH:   c["math"]   += 1
        if ch in SYM_ARROWS: c["arrows"] += 1
        if ch in SYM_BOX:    c["box"]    += 1
        if ch in SYM_STARS:  c["stars"]  += 1
        if ch in SYM_SEAL:   c["seal"]   += 1
    return c

def detect_patterns(txt):
    found = {"A": False, "B": False, "C": False, "D": False}
    # A: repunits / somas com 9 → ...111 etc.
    if re.search(r"\b1{2,}\b", txt) and re.search(r"\b9\s*×\s*[\d\s]+", txt):
        found["A"] = True
    # B: ...888 = k + 9 × ...89
    if re.search(r"8{3,}\s*=\s*.*\+\s*9\s*×\s*.*89", txt):
        found["B"] = True
    # C: palíndromos-escada 12321, 1234321, 123454321
    if re.search(r"\b12321\b|\b1234321\b|\b123454321\b", txt):
        found["C"] = True
    # D: 9…9² → 10…008…99 (vestígios de 999 × 999 etc.)
    if re.search(r"9{2,}\s*×\s*9{2,}", txt) or re.search(r"10+0+\s*8+9+", txt):
        found["D"] = True
    return found

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", default="")
    ap.add_argument("--mirror", default="")
    ap.add_argument("--m1",     default="")
    ap.add_argument("--m2",     default="")
    args = ap.parse_args()

    root  = args.root
    state = os.path.join(root, "state")
    cards = os.path.join(root, "cards")
    os.makedirs(state, exist_ok=True)
    os.makedirs(cards, exist_ok=True)

    src_d  = read(args.direct)
    src_m  = read(args.mirror)
    sym_d  = count_symbols(src_d)
    sym_m  = count_symbols(src_m)
    pat_d  = detect_patterns(src_d)
    pat_m  = detect_patterns(src_m)

    # Integra M1/M2 se existirem
    m1 = json.load(open(args.m1, encoding="utf-8")) if os.path.isfile(args.m1) else None
    m2 = json.load(open(args.m2, encoding="utf-8")) if os.path.isfile(args.m2) else None

    rep = {
        "timestamp": datetime.now().isoformat(),
        "root":      root,
        "m1_report": args.m1 if m1 else None,
        "m2_report": args.m2 if m2 else None,
        "symbols":   {"direct": dict(sym_d), "mirror": dict(sym_m)},
        "patterns":  {"direct": pat_d, "mirror": pat_m},
        "seal":      "∆7",
        "synthesis": {
            "law":             "VERDADE × INTEGRAR ÷ Δ = ♾️",
            "interdependence": ["M1→M2→M3 selam ∆⁷"],
        },
    }

    jpath = os.path.join(state, "m3_symbol_report.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(rep, f, ensure_ascii=False, indent=2)

    mpath = os.path.join(cards, "M3_SYMBOL_CARD.md")
    with open(mpath, "w", encoding="utf-8") as f:
        f.write("# KOBLLUX — M3 • Símbolo (ESPELHO)\n\n")
        f.write(f"**Símbolos (direto):** {dict(sym_d)}\n\n")
        f.write(f"**Símbolos (espelho):** {dict(sym_m)}\n\n")
        f.write(f"**Padrões A/B/C/D (direto):** {pat_d}\n")
        f.write(f"**Padrões A/B/C/D (espelho):** {pat_m}\n\n")
        f.write("> Selo: ∆⁷\n")

    print(f"[KOBLLUX] M3 OK → {jpath} | {mpath}")

if __name__ == "__main__":
    main()
