#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX • M3 (ESPELHO): Símbolo · Padrões · Reflexo

Primeiro ponto onde o ESPELHO vira critério de verdade.
Compara direto × espelho, detecta padrões A/B/C/D e
classes de símbolos. Gera cartão simbólico (M3_SYMBOL_CARD.md).
"""

import os, re, json, argparse
from datetime import datetime


def read(path):
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""


def classify_symbols(txt):
    return {
        "letras":      len(re.findall(r"[a-zA-ZÀ-ſ]", txt)),
        "digitos":     len(re.findall(r"\d", txt)),
        "pontuacao":   len(re.findall(r"[.,;:!?]", txt)),
        "especiais":   len(re.findall(r"[^a-zA-ZÀ-ſ\d\s.,;:!?]", txt)),
        "espacos":     len(re.findall(r"\s", txt)),
    }


def detect_patterns(txt):
    found = {
        "A": bool(re.search(r"\b111+\b|\b222+\b|\b333+\b", txt)),
        "B": bool(re.search(r"888\s*=\s*\d+\s*\+\s*9\s*×\s*89", txt)
                  or "…888" in txt or "...888" in txt),
        "C": bool(re.search(r"\b12321\b|\b1234321\b|\b123454321\b", txt)),
        "D": bool(re.search(r"999+\s*×\s*999+|\b10+0+\s*8+9+\b", txt)),
    }
    found["active"] = [k for k, v in found.items() if v and k != "active"]
    return found


def mirror_line(s):
    return s[::-1]


def compare_mirror(direct, mirror_txt):
    d_lines = direct.splitlines()
    m_lines = [mirror_line(l) for l in direct.splitlines()]
    m_src   = mirror_txt.splitlines()

    match_count = sum(1 for a, b in zip(m_lines, m_src) if a == b)
    total = max(len(d_lines), 1)
    return {
        "lines_direct": len(d_lines),
        "lines_mirror_generated": len(m_lines),
        "lines_mirror_provided":  len(m_src),
        "match_ratio": round(match_count / total, 4),
        "invariant": match_count == total,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", required=True)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--m1",     default="")
    ap.add_argument("--m2",     default="")
    args = ap.parse_args()

    src_d = read(args.direct)
    src_m = read(args.mirror)

    symbols_d = classify_symbols(src_d)
    symbols_m = classify_symbols(src_m)
    patterns_d = detect_patterns(src_d)
    patterns_m = detect_patterns(src_m)
    comparison = compare_mirror(src_d, src_m)

    report = {
        "timestamp":  datetime.now().isoformat(),
        "symbols":    {"direct": symbols_d, "mirror": symbols_m},
        "patterns":   {"direct": patterns_d, "mirror": patterns_m},
        "comparison": comparison,
        "m1_ref":     args.m1,
        "m2_ref":     args.m2,
        "seal":       "∆7_ESPELHO",
    }

    state_dir = os.path.join(args.root, "state")
    cards_dir = os.path.join(args.root, "cards")
    os.makedirs(state_dir, exist_ok=True)
    os.makedirs(cards_dir, exist_ok=True)

    jpath = os.path.join(state_dir, "m3_symbol_report.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    card_path = os.path.join(cards_dir, "M3_SYMBOL_CARD.md")
    with open(card_path, "w", encoding="utf-8") as f:
        f.write("# KOBLLUX — M3 SYMBOL CARD\n\n")
        f.write("**O que é verdadeiro sobrevive ao espelho.** — M3\n\n")
        f.write(f"## Padrões Ativos\n")
        active = patterns_d.get("active", [])
        f.write(f"- Direto: {active if active else 'nenhum'}\n")
        active_m = patterns_m.get("active", [])
        f.write(f"- Espelho: {active_m if active_m else 'nenhum'}\n\n")
        f.write(f"## Comparação Direto × Espelho\n")
        f.write(f"- Match ratio: {comparison['match_ratio']}\n")
        f.write(f"- Invariante: {comparison['invariant']}\n\n")
        f.write(f"> Selo: ∆⁷ · Ciclo: 9 (ESPELHAR)\n")

    print(f"[KOBLLUX] M3 ESPELHO OK → {jpath} | {card_path}")


if __name__ == "__main__":
    main()
