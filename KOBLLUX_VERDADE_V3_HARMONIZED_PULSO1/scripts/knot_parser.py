#!/usr/bin/env python3
# coding: utf-8
"""
KOBLLUX · scripts/knot_parser.py
Knot Rules Parser — roteador semântico de seções Markdown
Lei: VERDADE × INTEGRAR ÷ Δ = ∞ · Ritmo: 3-6-9-7

Lê um arquivo Markdown (ex: quicknote.md), divide por seções ##,
aplica regras Knot (match → kind + archetypes + lang),
e gera eventos para o LOG.jsonl.
"""
import re, json, argparse, pathlib, time, hashlib
from datetime import datetime, timezone

# ─── REGRAS KNOT CANÔNICAS ───────────────────────────────────────────────────
KNOT_RULES_DEFAULT = [
    {"match": r"^##\s*Hist(ó|o)ria",      "kind": "story",    "archetypes": ["NOVA","LUMINE"]},
    {"match": r"^##\s*(Manual|Guia|Passo)","kind": "tutorial", "archetypes": ["RHEA","SERENA"]},
    {"match": r"^##\s*Código.*JSON",       "kind": "text",     "archetypes": ["ATLAS","RHEA"],  "lang": "json"},
    {"match": r"^##\s*Código.*HTML",       "kind": "text",     "archetypes": ["ATLAS","RHEA"],  "lang": "html"},
    {"match": r"^##\s*Código.*Python",     "kind": "text",     "archetypes": ["RHEA","GENUS"],  "lang": "python"},
    {"match": r"^##\s*Código.*React",      "kind": "text",     "archetypes": ["BLLUE","GENUS"], "lang": "jsx"},
    {"match": r"^##\s*Código.*Bash",       "kind": "text",     "archetypes": ["KAOS","ATLAS"],  "lang": "bash"},
    {"match": r"^##\s*(Análise|Resumo)",   "kind": "text",     "archetypes": ["ATLAS","SOLUS"]},
    {"match": r"^##\s*(Fusão|Correlação)", "kind": "text",     "archetypes": ["KOBLLUX","AION"]},
    {"match": r"^##\s*(Voz|Som|TTS)",      "kind": "text",     "archetypes": ["PULSE","SERENA"]},
    {"match": r"^##\s*(Tempo|Ciclo|Loop)", "kind": "text",     "archetypes": ["AION","VITALIS"]},
    {"match": r"^##\s*(Memória|Memory)",   "kind": "text",     "archetypes": ["AION","RHEA"]},
]

# ─── HEURÍSTICA DE ARQUÉTIPOS por palavra-chave ──────────────────────────────
KEYWORD_MAP = {
    "estrutura": "ATLAS",  "planejamento": "ATLAS",
    "inspira":   "NOVA",   "criação": "NOVA",
    "energia":   "VITALIS","vida": "VITALIS",
    "ritmo":     "PULSE",  "emoção": "PULSE",
    "precisão":  "ARTEMIS","mapa": "ARTEMIS",
    "cuidado":   "SERENA", "nutri": "SERENA",
    "kaos":      "KAOS",   "ruptura": "KAOS",
    "fabrica":   "GENUS",  "moldar": "GENUS",
    "luz":       "LUMINE", "alegria": "LUMINE",
    "silêncio":  "SOLUS",  "sabedoria": "SOLUS",
    "vínculo":   "RHEA",   "rede": "RHEA",
    "tempo":     "AION",   "ciclo": "AION",
}

def match_knot_rule(titulo: str, regras: list) -> dict | None:
    for r in regras:
        if re.search(r["match"], titulo, re.IGNORECASE):
            return r
    return None

def heuristica_arquetipos(texto: str) -> list[str]:
    texto_lower = texto.lower()
    encontrados = []
    for kw, arq in KEYWORD_MAP.items():
        if kw in texto_lower and arq not in encontrados:
            encontrados.append(arq)
    return encontrados[:3] or ["ATLAS"]

def dividir_secoes(md: str) -> list[dict]:
    secoes = []
    partes = re.split(r'(?m)^(##\s+.+)$', md)
    atual_titulo = "(preamble)"
    atual_corpo  = []
    for parte in partes:
        if re.match(r'^##\s+', parte):
            if atual_corpo:
                secoes.append({"titulo": atual_titulo, "corpo": "\n".join(atual_corpo).strip()})
            atual_titulo = parte.strip()
            atual_corpo  = []
        else:
            atual_corpo.append(parte)
    if atual_corpo:
        secoes.append({"titulo": atual_titulo, "corpo": "\n".join(atual_corpo).strip()})
    return secoes

def sha7(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:7]

def parse_md(caminho: str, regras: list, log_path: str, output_dir: str):
    texto = pathlib.Path(caminho).read_text(encoding="utf-8")
    secoes = dividir_secoes(texto)
    eventos = []
    ts_base = datetime.now(timezone.utc)

    for i, sec in enumerate(secoes):
        regra = match_knot_rule(sec["titulo"], regras)
        if regra:
            kind       = regra["kind"]
            arquetipos = regra["archetypes"]
            lang       = regra.get("lang")
        else:
            kind       = "text"
            arquetipos = heuristica_arquetipos(sec["corpo"])
            lang       = None

        ts = ts_base.replace(second=(ts_base.second + i) % 60).isoformat()
        evento = {
            "ts":        ts,
            "actor":     "KODUX",
            "state":     arquetipos[0] if arquetipos else "ATLAS",
            "action":    kind,
            "note":      "UNO" if kind in ("story",) else ("DUO" if kind == "tutorial" else "TRINITY"),
            "secao":     sec["titulo"],
            "arquetipos":arquetipos,
            "lang":      lang,
            "sha7":      sha7(sec["corpo"]),
        }
        eventos.append(evento)

    # append ao LOG.jsonl
    log = pathlib.Path(log_path)
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a", encoding="utf-8") as f:
        for ev in eventos:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")

    # relatório
    out = pathlib.Path(output_dir) / "knot_report.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({
        "fonte": caminho,
        "secoes": len(secoes),
        "eventos": len(eventos),
        "ts": ts_base.isoformat(),
        "lei": "VERDADE × INTEGRAR ÷ Δ = ∞",
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[knot_parser] ✓ {len(eventos)} eventos gerados → {log_path}")
    print(f"[knot_parser] ✓ relatório → {out}")
    return eventos

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="KOBLLUX · Knot Rules Parser")
    ap.add_argument("--input",      required=True,  help="Markdown de entrada (ex: quicknote.md)")
    ap.add_argument("--output-dir", default="LOGS", help="Diretório de saída")
    ap.add_argument("--log",        default=None,   help="Caminho do LOG.jsonl")
    ap.add_argument("--rules",      default=None,   help="JSON com regras Knot adicionais")
    args = ap.parse_args()

    regras = KNOT_RULES_DEFAULT[:]
    if args.rules:
        extras = json.loads(pathlib.Path(args.rules).read_text(encoding="utf-8"))
        regras = extras + regras

    log_path = args.log or str(pathlib.Path(args.output_dir) / "LOG.jsonl")
    parse_md(args.input, regras, log_path, args.output_dir)
