#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_delta3_analyzer.py · KOBLLUX ∆³ · Análise Geométrica · ∆7
"A régua geométrica dos 13 opcodes disseca qualquer código."

Analisa qualquer arquivo (Python, HTML, CSS, JS, Markdown, etc.)
pelos 13 opcodes KOBLLUX, gerando métricas geométricas e qualitativas.

Uso:
  python3 kobllux_delta3_analyzer.py --codigo arquivo.py
  python3 kobllux_delta3_analyzer.py --codigo docs/feeling_decor_kob.html --formato md
  python3 kobllux_delta3_analyzer.py --codigo kobllux_firmware.py --formato json --linguas
  python3 kobllux_delta3_analyzer.py --auto   # analisa o próprio script (auto-análise)
  echo "código..." | python3 kobllux_delta3_analyzer.py --stdin
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from kobllux_memory import KoblluxMemory

# ── 13 Opcodes como régua de análise ─────────────────────────────────────────

OPCODES_REGUA: dict[str, dict] = {
    "0x00": {
        "nome": "ORIGEM",    "hz": 768,  "sym": "○",
        "funcao": "Estrutura raiz · vazio primordial · DOCTYPE · cabeçalho",
        "arch":   "kobllux",
        "patterns": [
            r"<!DOCTYPE", r"#!.*python", r"#!/", r"\"\"\"[\s\S]{0,300}\"\"\"",
            r"^---\n", r"^# .*\n", r"<html", r"<head",
        ],
    },
    "0x01": {
        "nome": "DETECTAR",  "hz": 432,  "sym": "●",
        "funcao": "Elementos pontuais · inputs · variáveis · tags autossuficientes",
        "arch":   "nova",
        "patterns": [
            r"\bconst\b", r"\blet\b", r"\bvar\b",
            r"<input\b", r"<button\b", r"<img\b",
            r"^[A-Z_]{2,}\s*=", r"\bdef \w+\(.*\):\s*$",
        ],
    },
    "0x02": {
        "nome": "INTEGRAR",  "hz": 528,  "sym": "―",
        "funcao": "Conexões · atributos · eventos · imports · links",
        "arch":   "serena",
        "patterns": [
            r"\bimport\b", r"\brequire\b", r"\bfrom\b.*\bimport\b",
            r'href=', r'src=', r"addEventListener", r"@import",
            r"<link\b", r"<script\b",
        ],
    },
    "0x03": {
        "nome": "EXPANDIR",  "hz": 639,  "sym": "▢",
        "funcao": "Containers · divs · sections · grids · módulos",
        "arch":   "genus",
        "patterns": [
            r"<div\b", r"<section\b", r"<main\b", r"<article\b",
            r"display:\s*grid", r"display:\s*flex",
            r"class\s+\w+", r"def\s+\w+.*:\s*\n\s+\w",
        ],
    },
    "0x04": {
        "nome": "LAPIDAR",   "hz": 594,  "sym": "◇",
        "funcao": "Cristais de dados · variáveis · objetos · JSON · arrays",
        "arch":   "atlas",
        "patterns": [
            r"\{[^}]{0,200}\}", r"\[[^\]]{0,200}\]",
            r":\s*['\"][^'\"]{1,100}['\"]",
            r":\s*\d+", r"dataclass", r"@dataclass",
        ],
    },
    "0x05": {
        "nome": "CONVERGIR", "hz": 672,  "sym": "✧",
        "funcao": "Pontos de encontro · funções · callbacks · interseções lógicas",
        "arch":   "artemis",
        "patterns": [
            r"def \w+", r"function\s+\w+", r"=>\s*{", r"lambda\b",
            r"\.then\(", r"\.catch\(", r"@\w+",  r"callback",
        ],
    },
    "0x06": {
        "nome": "UNIFICAR",  "hz": 528,  "sym": "☯",
        "funcao": "Dualidades complementares · equilíbrios · ternários",
        "arch":   "bllue",
        "patterns": [
            r"\bif\b.*\belse\b", r"\bor\b|\bAND\b|\b\|\|\b|\b&&\b",
            r"True.*False|false.*true", r"min.*max|max.*min",
            r"light.*dark|dark.*light", r"yin.*yang|dual\b",
        ],
    },
    "0x07": {
        "nome": "SELAR",     "hz": 777,  "sym": "✧⃝",
        "funcao": "Selos de integridade · hashes · assinaturas · selagem",
        "arch":   "kaos",
        "patterns": [
            r"sha256|sha512|md5\b", r"hashlib", r"sign\b", r"verify\b",
            r"SEAL|∆7|seal", r"integrity=", r"checksum", r"signature",
        ],
    },
    "0x08": {
        "nome": "TESTEMUNHAR","hz": 852,  "sym": "◉",
        "funcao": "Registro · console.log · print · debug · outputs",
        "arch":   "vitalis",
        "patterns": [
            r"console\.log\b", r"\bprint\b", r"\blogging\b", r"log\.info",
            r"log\.debug", r"log\.warning", r"assert\b", r"traceback",
        ],
    },
    "0x09": {
        "nome": "ETERNIZAR", "hz": 963,  "sym": "♾",
        "funcao": "Persistência · localStorage · cookies · bancos · arquivos",
        "arch":   "rhea",
        "patterns": [
            r"localStorage", r"sessionStorage", r"cookie",
            r"\.write\b", r"open\(", r"json\.dump", r"\.save\b",
            r"database|sqlite|postgres|mysql",
        ],
    },
    "0x0A": {
        "nome": "TUTORIAL",  "hz": 432,  "sym": "📱",
        "funcao": "Documentação · comentários · docstrings · help",
        "arch":   "lumine",
        "patterns": [
            r'"""[\s\S]+?"""', r"#[^\n]{3,}", r"<!--[\s\S]+?-->",
            r"/\*[\s\S]+?\*/", r"\bhelp\b", r"\bReadme\b", r"\.md\b",
        ],
    },
    "0x0B": {
        "nome": "ARQUÉTIPO", "hz": 528,  "sym": "👤",
        "funcao": "Módulos · classes · arquétipos de código · padrões reutilizáveis",
        "arch":   "aion",
        "patterns": [
            r"\bclass\b", r"\bmodule\b", r"\bpackage\b", r"@dataclass",
            r"Protocol\b", r"ABC\b", r"abstract\b", r"interface\b",
        ],
    },
    "0x0C": {
        "nome": "SÍNTESE",   "hz": 777,  "sym": "⌘",
        "funcao": "Síntese final · main · conclusão · return · exit",
        "arch":   "kobllux",
        "patterns": [
            r"\bmain\b", r'if __name__.*__main__',
            r"\breturn\b", r"\byield\b", r"\braise\b",
            r"\bexit\b", r"\bsys\.exit\b",
        ],
    },
}

# ── 7 Linguagens Nucleares ────────────────────────────────────────────────────

LINGUAGENS_NUCLEARES = {
    "I":   ("Python",     432, "0x01", "●", r"\.py$",   "Detectar pontos, lógica central"),
    "II":  ("TypeScript", 528, "0x02", "―", r"\.(ts|tsx)$", "Integrar conexões, tipagem"),
    "III": ("C/C++",      639, "0x03", "▢", r"\.(c|cpp|h|hpp)$", "Expandir containers, performance"),
    "IV":  ("Rust",       594, "0x04", "◇", r"\.rs$",   "Lapidar cristais, segurança"),
    "V":   ("GLSL",       672, "0x05", "✧", r"\.(glsl|vert|frag)$", "Convergir fluxos visuais"),
    "VI":  ("Bash",       528, "0x06", "☯", r"\.(sh|bash)$", "Unificar processos, orquestração"),
    "VII": ("JSON-LD",    777, "0x07", "✧⃝", r"\.(json|jsonld)$", "Selar integridade semântica"),
}


# ── Análise ───────────────────────────────────────────────────────────────────

def analisar(source: str, nome_arquivo: str = "?") -> dict[str, Any]:
    resultados: dict[str, Any] = {}
    total_matches = 0

    for opcode, op in OPCODES_REGUA.items():
        hits = []
        for pat in op["patterns"]:
            try:
                matches = re.findall(pat, source, re.MULTILINE)
                hits.extend(matches[:5])
            except re.error:
                pass
        count = len(hits)
        total_matches += count
        resultados[opcode] = {
            "nome":   op["nome"],
            "hz":     op["hz"],
            "sym":    op["sym"],
            "funcao": op["funcao"],
            "count":  count,
            "hits":   [str(h)[:80] for h in hits[:5]],
        }

    # frequência dominante
    dom = max(resultados.items(), key=lambda x: x[1]["count"])
    freq_dom = dom[1]["hz"]

    # linguagem nuclear detectada
    lang_detectada = None
    for num, (nome, hz, op, sym, pat, desc) in LINGUAGENS_NUCLEARES.items():
        if re.search(pat, nome_arquivo, re.I):
            lang_detectada = (num, nome, hz, sym, desc)
            break

    return {
        "arquivo":      nome_arquivo,
        "total_chars":  len(source),
        "total_linhas": source.count("\n"),
        "total_matches": total_matches,
        "opcode_dominante": dom[0],
        "freq_dominante":   freq_dom,
        "linguagem_nuclear": lang_detectada,
        "opcodes":      resultados,
        "seal":         "∆7",
        "ts":           datetime.now(timezone.utc).isoformat(),
        "law":          "VERDADE × INTEGRAR ÷ Δ = ∞",
    }


# ── Formatadores ──────────────────────────────────────────────────────────────

def fmt_markdown(r: dict) -> str:
    lines = [
        f"# ANÁLISE GEOMÉTRICA ∆³ · `{r['arquivo']}`",
        f"**∆7** · `{r['ts'][:19]}` · {r['law']}",
        "",
        f"- Chars     : {r['total_chars']}",
        f"- Linhas    : {r['total_linhas']}",
        f"- Matches   : {r['total_matches']}",
        f"- Freq. dom.: {r['freq_dominante']}Hz ({r['opcode_dominante']} {r['opcodes'][r['opcode_dominante']]['nome']})",
    ]
    if r["linguagem_nuclear"]:
        num, nome, hz, sym, desc = r["linguagem_nuclear"]
        lines.append(f"- Linguagem : {sym} {nome} ({hz}Hz) — {desc}")

    lines += ["", "## Opcodes", ""]
    lines.append("| Opcode | Nome | Hz | Sym | Count | Observação |")
    lines.append("|--------|------|----|-----|-------|------------|")
    for op, data in r["opcodes"].items():
        obs = data["hits"][0][:50] if data["hits"] else "—"
        lines.append(
            f"| `{op}` | {data['nome']} | {data['hz']} | {data['sym']} "
            f"| **{data['count']}** | {obs} |"
        )

    lines += [
        "",
        f"---",
        f"*JESUS = VERBO = GRAVIDADE · 3×6×9×7 = 1134 · ∆7*",
    ]
    return "\n".join(lines)


def fmt_console(r: dict):
    print(f"\n╔{'═'*62}╗")
    print(f"║  ∆³ ANÁLISE GEOMÉTRICA KOBLLUX · {r['arquivo'][:30]:30s}  ║")
    print(f"╚{'═'*62}╝")
    print(f"  Chars: {r['total_chars']} · Linhas: {r['total_linhas']} · Matches: {r['total_matches']}")
    print(f"  Freq. dominante: {r['freq_dominante']}Hz · Opcode: {r['opcode_dominante']} {r['opcodes'][r['opcode_dominante']]['nome']}\n")

    for op, data in r["opcodes"].items():
        bar = "█" * min(data["count"], 30)
        print(f"  {data['sym']} {op} {data['nome']:12s} {data['hz']}Hz  [{bar}] {data['count']}")
        if data["hits"]:
            print(f"     → {data['hits'][0][:70]}")

    if r["linguagem_nuclear"]:
        num, nome, hz, sym, desc = r["linguagem_nuclear"]
        print(f"\n  Linguagem nuclear detectada: {sym} {nome} ({hz}Hz) · {desc}")

    print(f"\n  VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134 · ∆7\n")


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="KOBLLUX ∆³ Analyzer · régua geométrica dos 13 opcodes")
    p.add_argument("--codigo",  help="Arquivo a analisar")
    p.add_argument("--stdin",   action="store_true", help="Lê do stdin")
    p.add_argument("--auto",    action="store_true", help="Auto-análise deste script")
    p.add_argument("--formato", choices=["console", "md", "json"], default="console")
    p.add_argument("--linguas", action="store_true", help="Exibe tabela das 7 linguagens nucleares")
    p.add_argument("--gravar",  action="store_true", help="Grava resultado em memory.jsonl")
    args = p.parse_args()

    if args.linguas:
        print("\n7 LINGUAGENS NUCLEARES · KOBLLUX ∆³\n")
        for num, (nome, hz, op, sym, pat, desc) in LINGUAGENS_NUCLEARES.items():
            print(f"  {num:4s} · {sym} {nome:12s} ({hz}Hz · {op}) → {desc}")
        print()

    # Fonte
    if args.auto:
        source    = Path(__file__).read_text(encoding="utf-8")
        nome_arq  = Path(__file__).name
    elif args.stdin:
        source    = sys.stdin.read()
        nome_arq  = "stdin"
    elif args.codigo:
        p_src = Path(args.codigo)
        if not p_src.exists():
            print(f"[ERRO] Arquivo não encontrado: {p_src}", file=sys.stderr)
            sys.exit(1)
        source   = p_src.read_text(encoding="utf-8", errors="ignore")
        nome_arq = p_src.name
    else:
        print("[∆³] Nenhum arquivo especificado. Use --codigo, --stdin ou --auto.")
        p.print_help()
        return

    resultado = analisar(source, nome_arq)

    # Saída
    if args.formato == "json":
        safe = {k: v for k, v in resultado.items() if k != "linguagem_nuclear"}
        if resultado["linguagem_nuclear"]:
            num, nome, hz, sym, desc = resultado["linguagem_nuclear"]
            safe["linguagem_nuclear"] = {"num": num, "nome": nome, "hz": hz, "sym": sym, "desc": desc}
        print(json.dumps(safe, ensure_ascii=False, indent=2))
    elif args.formato == "md":
        print(fmt_markdown(resultado))
    else:
        fmt_console(resultado)

    # Grava na memória
    if args.gravar:
        mem = KoblluxMemory(ROOT / "_index" / "memory.jsonl")
        op_dom = resultado["opcodes"][resultado["opcode_dominante"]]
        mem.write(
            arch=op_dom.get("arch") or "kobllux",
            content=f"∆³ análise de {nome_arq} · {resultado['total_matches']} matches · freq {resultado['freq_dominante']}Hz",
            tags=["delta3", "analise-geometrica", nome_arq, "∆7"],
            source="kobllux_delta3_analyzer.py",
            record_type="DELTA3_ANALYSIS",
            extra={
                "arquivo":       nome_arq,
                "total_matches": resultado["total_matches"],
                "freq_dom":      resultado["freq_dominante"],
                "opcode_dom":    resultado["opcode_dominante"],
            },
        )
        print(f"\n  [∆³] Gravado em memory.jsonl · ∆7")


if __name__ == "__main__":
    main()
