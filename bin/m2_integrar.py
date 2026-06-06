#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX • M2 (0x06 INTEGRAR): Linguagem · Contexto · Correlação

Recebe os dados brutos do M1 e correlaciona com linguagem,
stopwords e diacríticos para produzir um relatório de contexto.
Depende obrigatoriamente do M1.
"""

import os, re, json, argparse
from datetime import datetime

# stopwords mínimas PT + EN para heurística de idioma
_STOP_PT = {"o", "a", "os", "as", "e", "de", "da", "do", "em", "um", "uma",
             "que", "se", "com", "por", "para", "não", "mas", "ou", "ao", "na", "no"}
_STOP_EN = {"the", "a", "an", "and", "or", "in", "of", "to", "is", "was",
             "for", "on", "with", "at", "by", "as", "be", "it", "not", "from"}

_DIAC_PT = re.compile(r"[áéíóúâêîôûãõàèìòùçÁÉÍÓÚÂÊÎÔÛÃÕÀÇ]")
_DIAC_EN = re.compile(r"[a-zA-Z]")


def read(path):
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""


def detect_language(txt):
    tokens = set(re.findall(r"\b\w+\b", txt.lower(), flags=re.UNICODE))
    pt = len(tokens & _STOP_PT)
    en = len(tokens & _STOP_EN)
    diac = len(_DIAC_PT.findall(txt))

    if diac > 3 or pt > en:
        lang, conf = "pt-BR", round(pt / max(pt + en, 1), 3)
    elif en > pt:
        lang, conf = "en-US", round(en / max(pt + en, 1), 3)
    else:
        lang, conf = "und", 0.5

    return {"lang": lang, "confidence": conf, "pt_hits": pt, "en_hits": en, "diacritics": diac}


def tokenize(txt):
    tokens = re.findall(r"\b\w+\b", txt, flags=re.UNICODE)
    unique = list(dict.fromkeys(tokens))
    return {"total": len(tokens), "unique": len(unique), "sample": unique[:20]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", required=True)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--m1",     default="")
    args = ap.parse_args()

    src_d = read(args.direct)
    src_m = read(args.mirror)

    m1_data = {}
    if args.m1:
        try:
            m1_data = json.loads(read(args.m1))
        except Exception:
            pass

    report = {
        "timestamp":  datetime.now().isoformat(),
        "language":   {"direct": detect_language(src_d), "mirror": detect_language(src_m)},
        "tokens":     {"direct": tokenize(src_d), "mirror": tokenize(src_m)},
        "m1_ref":     args.m1,
        "m1_direct":  m1_data.get("direct", {}),
        "seal":       "∆7_INTEGRAR",
    }

    os.makedirs(os.path.join(args.root, "state"), exist_ok=True)
    out = os.path.join(args.root, "state", "m2_lang_report.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"[KOBLLUX] 0x06 INTEGRAR (M2) OK → {out}")


if __name__ == "__main__":
    main()
