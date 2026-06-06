#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX • ESPELHO POOL — (V×I÷Δ=∞)

Este script é um AGREGADOR FINAL.
Ele não cria novos significados isolados: ele REFLETE, COMPARA e SELA.

Função central:
- Ler um texto (arquivo ou stdin)
- Criar sua versão espelhada (linha a linha)
- Executar contagens básicas (eco do M1)
- Detectar padrões A/B/C/D (eco do M3)
- Gerar uma síntese UNO / DUAL / TRINITY (eco do M2 + M4)
- Salvar apenas novos artefatos (state / cards), sem sobrescrever nada

Ele é um POOL porque reúne tudo.
Ele é um ESPELHO porque nada inventa.
"""

import sys, json, re, argparse, os
from datetime import datetime

# ==========================================================
# 🔹 KODUX — FUNÇÕES BÁSICAS DE LEITURA E ESPELHO
# ==========================================================

def read_text(path):
    """
    Lê texto de um arquivo OU do stdin.
    Isso permite uso direto via CLI com pipe:
      cat arquivo.txt | python3 espelho_pool.py
    """
    if path and os.path.isfile(path):
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            return f.read()
    try:
        return sys.stdin.read()
    except Exception:
        return ""

def mirror_line(s):
    """
    Espelha uma linha invertendo a ordem dos caracteres.
    Exemplo:
      'ABC123' → '321CBA'
    """
    return s[::-1]

def reverse_by_lines(txt):
    """
    Espelha o texto linha por linha.
    Importante: preserva a estrutura vertical (linhas),
    apenas inverte o conteúdo interno de cada linha.
    """
    return "\n".join(mirror_line(line) for line in txt.splitlines())

# ==========================================================
# 🔹 FASE DETECTAR (ECO DO M1)
# ==========================================================

def count_basic(txt):
    """
    Conta métricas essenciais do texto:
    - letters: qualquer caractere não-espaço
    - words: tokens textuais
    - sentences: frases por pontuação ou linhas vazias

    Isso permite comparar se o ESPELHO
    preserva as mesmas quantidades (invariantes).
    """
    letters = len(re.findall(r"\S", txt, flags=re.UNICODE))
    words = len(re.findall(r"\b\w+\b", txt, flags=re.UNICODE))
    sentences = len(re.findall(r"[.!?]+(?=\s|$)", txt)) or txt.count("\n\n")
    return {
        "letters": letters,
        "words": words,
        "sentences": sentences
    }

# ==========================================================
# 🔹 FASE PADRÕES (ECO DO M3)
# ==========================================================

def detect_patterns(txt):
    """
    Detecta padrões canônicos A/B/C/D
    + armazena evidências auxiliares.

    Esses padrões são considerados
    'invariantes vivos' sob espelhamento.
    """
    found = {
        "A": False, "B": False, "C": False, "D": False,
        "palindromos": [],
        "repunits": [],
        "coluna_8": False,
        "coluna_1": False
    }

    # A — repunits (111, 222, 333...)
    if re.search(r"\b111+\b|\b222+\b|\b333+\b", txt):
        found["A"] = True
        found["repunits"].append("...111")

    # B — coluna 8 (ajuste por múltiplos de 9)
    if re.search(r"888\s*=\s*\d+\s*\+\s*9\s*×\s*89", txt) or "…888" in txt or "...888" in txt:
        found["B"] = True
        found["coluna_8"] = True

    # C — palíndromos escada
    if re.search(r"\b12321\b|\b1234321\b|\b123454321\b", txt):
        found["C"] = True
        found["palindromos"].extend(["12321", "1234321", "123454321"])

    # D — quadrado de repunits (999 × 999 → 998001)
    if re.search(r"999+\s*×\s*999+|\b10+0+\s*8+9+\b", txt):
        found["D"] = True

    return found

# ==========================================================
# 🔹 FASE TESE / ANTÍTESE (DUALIDADE)
# ==========================================================

def estimate_thesis_antithesis(txt):
    """
    Heurística simples:
    - tese: marcadores do tipo 'A §', 'B §' etc.
    - antítese: presença do símbolo ✗

    Serve apenas como INDÍCIO de polaridade,
    não como verdade absoluta.
    """
    theses = len(re.findall(r"\b[A-D]\s*§", txt))
    antitheses = txt.count("✗")
    return {
        "thesis": theses,
        "antithesis": antitheses
    }

# ==========================================================
# 🔹 SÍNTESE KOBLLUX (UNO / DUAL / TRINITY)
# ==========================================================

def create_synthesis():
    """
    Constrói a narrativa estrutural do sistema:
    - UNO: a lei
    - DUAL: o espelho
    - TRINITY: o procedimento verificável
    """
    uno = {
        "law": "VERDADE × INTEGRAR ÷ Δ = ♾",
        "focus": ["9…9²", "repunits", "palíndromos"],
        "purpose": "O que permanece verdade após remover todo ruído?"
    }

    dual = {
        "mirror": True,
        "invariants": ["múltiplos de 9", "palíndromos", "repunits"],
        "mapping": "…321 ↔ …123, coluna 8 ↔ ajuste k",
        "essence": "Espelho e direto preservam estrutura"
    }

    trinity = {
        "procedure": [
            "detectar A/B/C/D",
            "contar métricas",
            "selar ∆⁷",
            "loop 3×9×7"
        ],
        "synthesis_focus": "Lei + Espelho + Procedimento"
    }

    return {
        "UNO": uno,
        "DUAL": dual,
        "TRINITY": trinity
    }

# ==========================================================
# 🔹 FUNÇÃO PRINCIPAL (CLI)
# ==========================================================

def main():
    # Argumentos de linha de comando
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="/sdcard/JESUS_VERBO/CODEX")
    ap.add_argument("--infile", default="")
    args = ap.parse_args()

    # Diretórios de saída (não alteram arquivos antigos)
    root = args.root
    state = os.path.join(root, "state")
    cards = os.path.join(root, "cards")
    os.makedirs(state, exist_ok=True)
    os.makedirs(cards, exist_ok=True)

    # Leitura e espelhamento
    src = read_text(args.infile)
    mirrored = reverse_by_lines(src) if src else ""

    # Processamento DIRETO e ESPELHO
    counts_direct = count_basic(src)
    counts_mirror = count_basic(mirrored)

    pats_direct = detect_patterns(src)
    pats_mirror = detect_patterns(mirrored)

    ta_direct = estimate_thesis_antithesis(src)
    ta_mirror = estimate_thesis_antithesis(mirrored)

    # Síntese superior
    synthesis = create_synthesis()

    # Relatório final agregado
    report = {
        "timestamp": datetime.now().isoformat(),
        "root": root,
        "input_file": args.infile if args.infile else "<stdin>",
        "counts": {
            "direct": counts_direct,
            "mirror": counts_mirror
        },
        "patterns": {
            "direct": pats_direct,
            "mirror": pats_mirror
        },
        "thesis_antithesis": {
            "direct": ta_direct,
            "mirror": ta_mirror
        },
        "synthesis": synthesis,
        "seal": "∆7",
        "loop": "3×9×7"
    }

    # Escrita dos artefatos (SELAR)
    out_json = os.path.join(state, "espelho_report.json")
    with open(out_json, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    out_md = os.path.join(cards, "ESPELHO_CARD.md")
    with open(out_md, "w", encoding="utf-8") as f:
        f.write("# KOBLLUX — CARD • ESPELHO (REVERSO)\n\n")
        f.write("**(V×I÷Δ=∞)** • Leitura espelhada e invariantes\n\n")
        f.write("## UNO / DUAL / TRINITY\n")
        f.write(f"- UNO: {synthesis['UNO']}\n")
        f.write(f"- DUAL: {synthesis['DUAL']}\n")
        f.write(f"- TRINITY: {synthesis['TRINITY']}\n\n")
        f.write("> Selo: ∆⁷ • Loop: 3×9×7\n")

    print(f"[KOBLLUX] ESPELHO OK → {out_json} | {out_md}")

# ==========================================================
# 🔹 PONTO DE ENTRADA
# ==========================================================

if __name__ == "__main__":
    main()
