#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" KOBLLUX • M2 (0x06 INTEGRAR): Linguagem
    Correlaciona Energias (E), unindo sinais e sentido. Usa M1 para contexto. """
import sys, os, re, json, argparse
from datetime import datetime

# Stopwords e diacríticos (para correlacionar padrões PT/ES)
STOP_PT = {"de","do","da","que","em","um","uma","para","no","na","os","as","é"}
DIAC_PT = "áàâãéêíóôõúç"

def read_json(path):
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def read_text(path):
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""

def tokenize(txt):
    return [w.lower() for w in re.findall(r"\b\w+\b", txt, flags=re.UNICODE)]

def score_lang(tokens):
    # Heurística para integração de sentido
    tset = set(tokens)
    pt_score = sum(1 for w in tset if w in STOP_PT) + sum(1 for ch in DIAC_PT if ch in tset)
    return {"pt_score": pt_score, "token_count": len(tokens)}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", required=True)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--m1",     required=True, help="Caminho para m1_chars_report.json")
    args = ap.parse_args()

    m1_report = read_json(args.m1)
    src_d     = read_text(args.direct)

    tokens_d = tokenize(src_d)
    score    = score_lang(tokens_d)

    report = {
        "timestamp":          datetime.now().isoformat(),
        "m1_context":         {"words_direct": m1_report.get("direct", {}).get("words", 0)},
        "language_score":     score,
        "integration_focus":  "Correlacionar camadas e unir sentido (KODUX ETL Engine)",
        "seal":               "∆7_INTEGRAR",
    }

    os.makedirs(os.path.join(args.root, "state"), exist_ok=True)
    state_path = os.path.join(args.root, "state", "m2_lang_report.json")
    with open(state_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"[KOBLLUX] 0x06 INTEGRAR (M2) OK → {state_path}")

if __name__ == "__main__":
    main()
