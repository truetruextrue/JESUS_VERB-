#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════╗
║  kobllux_trinity_fractal.py                                  ║
║  Painel da Trindade Fractal · KOBLLUX ∆7                    ║
║                                                              ║
║  Axioma:  JESUS é o Centro ∴ O Verbo                        ║
║  Fractal: 3×6×9×7 = ∞                                       ║
║  Lei:     VERDADE × INTEGRAR ÷ ∆ = ♾️                       ║
║  Tríade:  ∆ × ∆ × ∆ → Trindade Santa (Pai, Filho, Espírito) ║
║  Selo:    = ∆⁷ → Selo da Perfeição = Frequência JESUS       ║
║                                                              ║
║  Objetivo: Visualizar a Trindade como o coração pulsante     ║
║  do KOBLLUX — processo simultâneo de dados enviados,         ║
║  recebidos e conscientizados, sempre agregando sem subtrair. ║
╚══════════════════════════════════════════════════════════════╝
"""

import sys
import argparse
import math
import time
from datetime import datetime

# ══════════════════════════════════════════════════════════════
# ANSI
# ══════════════════════════════════════════════════════════════

class C:
    R  = "\033[0m"
    B  = "\033[1m"
    DIM= "\033[2m"
    # Paleta Trinity
    PAI      = "\033[97m"        # Branco puro       — Pai · Fonte
    FILHO    = "\033[38;5;220m"  # Dourado           — Filho · Verbo
    ESPIRITO = "\033[38;5;123m"  # Azul celeste      — Espírito · Sopro
    JESUS    = "\033[38;5;214m"  # Laranja radiante  — Jesus · Centro
    FRACTAL  = "\033[38;5;141m"  # Violeta           — Fractal / Selos
    SETA     = "\033[38;5;87m"   # Ciano vibrante    — Setas de fluxo
    GOLD     = "\033[38;5;226m"  # Amarelo ouro      — Destaques
    DIM_W    = "\033[38;5;245m"  # Cinza suave       — Texto auxiliar

_COLOR_ON = True

def _c(text: str, code: str) -> str:
    if not _COLOR_ON:
        return text
    return f"{code}{text}{C.R}"

# ══════════════════════════════════════════════════════════════
# UTILITÁRIOS
# ══════════════════════════════════════════════════════════════

def _ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def _pad(s: str, w: int, align: str = "center") -> str:
    """Alinha string em largura w (ignora códigos ANSI na contagem)."""
    vis = len(_strip_ansi(s))
    pad = max(0, w - vis)
    if align == "center":
        l, r = pad // 2, pad - pad // 2
        return " " * l + s + " " * r
    if align == "right":
        return " " * pad + s
    return s + " " * pad

def _strip_ansi(s: str) -> str:
    import re
    return re.sub(r'\033\[[0-9;]*m', '', s)

# ══════════════════════════════════════════════════════════════
# BANNER
# ══════════════════════════════════════════════════════════════

def imprimir_banner():
    W = 64
    brd = _c("╔" + "═" * W + "╗", C.FRACTAL)
    bot = _c("╚" + "═" * W + "╝", C.FRACTAL)
    def row(txt, col=C.DIM_W):
        return _c("║", C.FRACTAL) + _pad(_c(txt, col), W) + _c("║", C.FRACTAL)

    print()
    print(brd)
    print(row("K  O  B  L  L  U  X   ·   T  R  I  N  I  T  Y", C.GOLD))
    print(row("∆ × ∆ × ∆  →  Trindade Santa", C.FRACTAL))
    print(row("JESUS é o Centro  ∴  O Verbo", C.JESUS))
    print(row("3×6×9×7 = ∞  ·  ∆⁷ = Selo da Perfeição", C.DIM_W))
    print(row(_ts(), C.DIM_W))
    print(bot)
    print()

# ══════════════════════════════════════════════════════════════
# TRIÂNGULO DA TRINDADE FRACTAL
# ══════════════════════════════════════════════════════════════
#
#  Nível  3 (Semente)  — triângulo externo  · PAI
#  Nível  6 (Raiz)    — triângulo médio     · FILHO
#  Nível  9 (Espírito)— triângulo interno   · ESPÍRITO
#  Centro             — JESUS               · Verbo
#

TRIANGULO = r"""
                        PAI
                     (Fonte · ○)
                         ▲
                        /|\
                       / | \
                      /  |  \
              3──────/───|───\──────3
             ╱      / ↑ | ↑ \      ╲
            ╱      /   |   |   \      ╲
           ╱      / ╭──┴──╮  \      ╲
          ╱  6──/──│JESUS│──\──6  ╲
         ╱       / │Centro│  \       ╲
        ╱       /  │ Verbo │   \       ╲
       ╱   9──/────╰──┬──╯────\──9   ╲
      ╱         / ↓   |   ↓ \         ╲
     ╱─────────/──────|──────\─────────╲
    ╱  ←←←←←←  ╲     |     ╱  →→→→→→  ╲
   ╱──────────────╲   |   ╱──────────────╲
  FILHO ←────────── ● ─────────→ ESPÍRITO
(Forma · Verbo)   (fluxo)    (Sopro · Ação)
"""

def _linha_colorida(linha: str) -> str:
    """Aplica cores por conteúdo de cada linha."""
    if "PAI" in linha or "Fonte" in linha:
        return _c(linha, C.PAI)
    if "FILHO" in linha or "Forma" in linha:
        return _c(linha, C.FILHO)
    if "ESPÍRITO" in linha or "Sopro" in linha:
        return _c(linha, C.ESPIRITO)
    if "JESUS" in linha or "Verbo" in linha or "Centro" in linha:
        return _c(linha, C.JESUS)
    if any(c in linha for c in ["▲", "╱", "╲", "─", "═"]):
        return _c(linha, C.FRACTAL)
    if any(c in linha for c in ["↑", "↓", "←", "→"]):
        return _c(linha, C.SETA)
    if any(str(n) in linha for n in [3, 6, 9]):
        return _c(linha, C.GOLD)
    return _c(linha, C.DIM_W)

def imprimir_triangulo():
    print(_c("  ┌─ TRIÂNGULO DA TRINDADE FRACTAL ─────────────────────────┐", C.FRACTAL))
    print(_c("  │  Camadas: 3 (Semente) · 6 (Raiz) · 9 (Espírito)        │", C.DIM_W))
    print(_c("  └──────────────────────────────────────────────────────────┘", C.FRACTAL))
    print()
    for linha in TRIANGULO.splitlines():
        print("  " + _linha_colorida(linha))
    print()

# ══════════════════════════════════════════════════════════════
# CICLO DA ÁGUA (Sólido · Líquido · Gasoso = 3 estados)
# ══════════════════════════════════════════════════════════════

CICLO_AGUA = """
   ┌──────────────────────────────────────────────────────┐
   │       CICLO DA ÁGUA  ·  Trindade em Movimento        │
   │                                                      │
   │  🧊 SÓLIDO        💧 LÍQUIDO       💨 GASOSO         │
   │  (PAI · Forma)   (FILHO · Verbo)  (ESPÍRITO · Sopro) │
   │                                                      │
   │  SEMENTE ──3──▶ TEMPLO ──6──▶ CASA ──9──▶ SEMENTE   │
   │      └─────────────────────────────────┘            │
   │                 (ciclo eterno · ∞)                   │
   └──────────────────────────────────────────────────────┘
"""

def imprimir_ciclo():
    linhas = CICLO_AGUA.splitlines()
    for linha in linhas:
        if "SÓLIDO" in linha or "PAI" in linha:
            print(_c(linha, C.PAI))
        elif "LÍQUIDO" in linha or "FILHO" in linha or "Verbo" in linha:
            print(_c(linha, C.FILHO))
        elif "GASOSO" in linha or "ESPÍRITO" in linha or "Sopro" in linha:
            print(_c(linha, C.ESPIRITO))
        elif "SEMENTE" in linha or "TEMPLO" in linha or "CASA" in linha:
            print(_c(linha, C.GOLD))
        elif "ciclo" in linha or "∞" in linha:
            print(_c(linha, C.FRACTAL))
        else:
            print(_c(linha, C.DIM_W))
    print()

# ══════════════════════════════════════════════════════════════
# ESCADA DE GÊNESIS (7 camadas)
# ══════════════════════════════════════════════════════════════

ESCADA = [
    ("Dia 1", "Luz separada das trevas",          "∆¹ · DETECTAR · 0x03"),
    ("Dia 2", "Firmamento · separação das águas",  "∆² · INTEGRAR · 0x06"),
    ("Dia 3", "Terra · plantas · semente",         "∆³ · EXPANDIR · 0x09"),
    ("Dia 4", "Astros · marcadores do Tempo",      "∆⁴ · SELAR   · 0x07"),
    ("Dia 5", "Criaturas do mar e do ar",          "∆⁵ · FLUIR   · 0x09"),
    ("Dia 6", "Animais e Adão feito à imagem",     "∆⁶ · UNIFICAR· 0x06"),
    ("Dia 7", "Descanso · Shabbat · Selo ∆⁷",     "∆⁷ · SELAR PERFEITO"),
]

def imprimir_escada():
    print(_c("  ┌─ ESCADA DE GÊNESIS  ·  7 Dias = 7 Camadas ──────────────┐", C.FRACTAL))
    for dia, desc, opcode in ESCADA:
        col = C.JESUS if "7" in dia else C.GOLD if "6" in dia else C.FILHO if "3" in dia else C.DIM_W
        d   = _c(f"  │  {dia:<6}", C.DIM_W)
        de  = _c(f" {desc:<42}", col)
        op  = _c(f" {opcode:<24}", C.FRACTAL)
        print(d + de + op + _c(" │", C.FRACTAL))
    print(_c("  └──────────────────────────────────────────────────────────┘", C.FRACTAL))
    print()

# ══════════════════════════════════════════════════════════════
# ESPIRAL TRINA 3-6-9
# ══════════════════════════════════════════════════════════════

def imprimir_espiral():
    """Representa a espiral fractal 3-6-9 visualmente."""
    print(_c("  ┌─ ESPIRAL TRINA  ·  3 → 6 → 9 → ∞ ──────────────────────┐", C.FRACTAL))
    niveis = [
        (3, "SEMENTE · Mente · Intenção",    C.PAI),
        (6, "RAIZ    · Corpo · Expressão",   C.FILHO),
        (9, "ESPÍRITO· Alma  · Manifestação",C.ESPIRITO),
    ]
    for n, desc, col in niveis:
        barra = "█" * (n * 8)
        linha = f"  │  {n}  {barra:<72} {desc:<38}"
        print(_c(linha, col) + _c(" │", C.FRACTAL))
    print(_c("  │  ∞  ▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶▶ (retorna ao 3)", C.GOLD)
          + _c(" │", C.FRACTAL))
    print(_c("  └──────────────────────────────────────────────────────────┘", C.FRACTAL))
    print()

# ══════════════════════════════════════════════════════════════
# NARRATIVA DIDÁTICA
# ══════════════════════════════════════════════════════════════

NARRATIVA = [
    ("TRINDADE · FUNDAÇÃO ESPIRITUAL DO KOBLLUX", C.JESUS, True),
    ("", C.DIM_W, False),
    ("O PAI é a FONTE PRIMORDIAL — o ∆ original, o vazio fértil que contém",  C.PAI,      False),
    ("tudo antes da forma. É o princípio sem início, o potencial puro.",        C.PAI,      False),
    ("", C.DIM_W, False),
    ("O FILHO é o VERBO QUE SE FAZ FORMA — JESUS, a palavra que estrutura",    C.FILHO,    False),
    ("a realidade. É o código primordial: cada instrução, cada dado, cada",     C.FILHO,    False),
    ("função nasce do Verbo. No KOBLLUX: o opcode, a fórmula, o script.",      C.FILHO,    False),
    ("", C.DIM_W, False),
    ("O ESPÍRITO SANTO é o SOPRO QUE ANIMA — o fluxo vivo entre o Pai e o",   C.ESPIRITO, False),
    ("Filho. É a memória que conecta, o movimento que persiste, o amor que",    C.ESPIRITO, False),
    ("circula. No KOBLLUX: o banco_kobllux, a roda viva, o α=1/137.",          C.ESPIRITO, False),
    ("", C.DIM_W, False),
    ("JESUS é o CENTRO DE GRAVIDADE — onde PAI, FILHO e ESPÍRITO convergem.",  C.JESUS,    False),
    ("Toda operação KOBLLUX orbita esse centro: VERDADE × INTEGRAR ÷ ∆ = ∞.",  C.JESUS,    False),
    ("", C.DIM_W, False),
    ("BASE DA LINGUAGEM E DO CÓDIGO:", C.GOLD, True),
    ("  • Semente (3): intenção → detectar → PAI envia",                       C.DIM_W,    False),
    ("  • Raiz    (6): integrar → conectar → FILHO estrutura",                 C.DIM_W,    False),
    ("  • Espírito(9): expandir → animar  → ESPÍRITO flui",                   C.DIM_W,    False),
    ("  • Selar   (7): ∆⁷        registrar → JESUS sela",                     C.DIM_W,    False),
    ("", C.DIM_W, False),
    ("Assim como o ciclo da água (sólido→líquido→gasoso→sólido), a Trindade",  C.DIM_W,    False),
    ("em movimento gera FLUXO CONTÍNUO — da semente à casa, em todas as",      C.DIM_W,    False),
    ("camadas da existência. Este é o código sagrado: sempre AGREGANDO,",       C.GOLD,     False),
    ("nunca subtraindo, multiplicando a luz em cada pulso.",                    C.GOLD,     False),
    ("", C.DIM_W, False),
    ("EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO. AMÉM. ∆⁷ ✧⃝⚝",            C.FRACTAL,  True),
]

def imprimir_narrativa():
    W = 62
    print(_c("  ┌─ NARRATIVA KOBLLUX TRINITY ──────────────────────────────┐", C.FRACTAL))
    for txt, col, bold in NARRATIVA:
        if not txt:
            print(_c("  │" + " " * W + "│", C.FRACTAL))
            continue
        codigo = (C.B if bold else "") + col
        wrapped = _quebrar(txt, W - 4)
        for i, linha in enumerate(wrapped):
            pad = " " * (W - len(linha) - 4)
            print(_c("  │  ", C.FRACTAL) + _c(linha, codigo) + pad + "  " + _c("│", C.FRACTAL))
    print(_c("  └──────────────────────────────────────────────────────────┘", C.FRACTAL))
    print()

def _quebrar(texto: str, largura: int):
    """Quebra texto em linhas de largura máxima."""
    palavras = texto.split()
    linhas, atual = [], ""
    for p in palavras:
        if len(atual) + len(p) + 1 <= largura:
            atual += (" " if atual else "") + p
        else:
            if atual: linhas.append(atual)
            atual = p
    if atual: linhas.append(atual)
    return linhas if linhas else [""]

# ══════════════════════════════════════════════════════════════
# SELO FINAL
# ══════════════════════════════════════════════════════════════

def imprimir_selo():
    ts   = _ts()
    seal = "f544e7482b2c8426"
    print(_c("  ╔══════════════════════════════════════════════════════════╗", C.JESUS))
    print(_c("  ║  ✧⃝⚝  KOBLLUX ∆⁷ · TRINDADE SELADA · CICLO COMPLETO  ⚝✧  ║", C.JESUS))
    print(_c("  ║                                                          ║", C.JESUS))
    print(_c(f"  ║  Seal:  {seal:<50}║", C.GOLD))
    print(_c(f"  ║  Time:  {ts:<50}║", C.DIM_W))
    print(_c("  ║  Lei:   VERDADE × INTEGRAR ÷ ∆ = ∞                      ║", C.FRACTAL))
    print(_c("  ║  3×6×9×7 = 1134 → dr = 9 → ∞                           ║", C.FRACTAL))
    print(_c("  ╚══════════════════════════════════════════════════════════╝", C.JESUS))
    print()

# ══════════════════════════════════════════════════════════════
# ANIMAÇÃO PULSANTE (opcional --pulse)
# ══════════════════════════════════════════════════════════════

def _pulsar(n: int = 3):
    """Pulsa o símbolo ∆ n vezes para sugerir movimento."""
    pulsos = ["∆", "∆³", "∆⁶", "∆⁹", "∆⁷", "♾️ "]
    for _ in range(n):
        for p in pulsos:
            print(f"\r  {_c(p, C.JESUS)}  ", end="", flush=True)
            time.sleep(0.08)
    print(f"\r  {_c('∆⁷ · TRINDADE ATIVA', C.JESUS)}          ")

# ══════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════

def main():
    global _COLOR_ON

    ap = argparse.ArgumentParser(
        prog="kobllux_trinity_fractal",
        description="Painel da Trindade Fractal · KOBLLUX ∆7 · JESUS é o Centro ∴ O Verbo",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Lei: VERDADE × INTEGRAR ÷ ∆ = ∞  ·  3×6×9×7 = ∞",
    )
    ap.add_argument("--no-color",   action="store_true", help="Desativar cores ANSI")
    ap.add_argument("--pulse",      action="store_true", help="Animação pulsante inicial")
    ap.add_argument("--only",       choices=["triangulo","ciclo","espiral","escada","narrativa"],
                    help="Exibir apenas uma seção")
    ap.add_argument("--json-seal",  action="store_true", help="Imprimir apenas o JSON do selo")
    args = ap.parse_args()

    if args.no_color or not sys.stdout.isatty():
        _COLOR_ON = False

    if args.json_seal:
        import json, hashlib
        seal = {
            "modulo":  "kobllux_trinity_fractal",
            "axioma":  "JESUS é o Centro ∴ O Verbo",
            "lei":     "VERDADE × INTEGRAR ÷ ∆ = ∞",
            "fractal": "3×6×9×7 = 1134",
            "ts":      _ts(),
            "hash":    hashlib.sha256(("TRINDADE" + _ts()).encode()).hexdigest()[:16],
        }
        print(json.dumps(seal, ensure_ascii=False, indent=2))
        return

    if args.pulse:
        _pulsar()

    if args.only == "triangulo":
        imprimir_banner(); imprimir_triangulo(); imprimir_selo(); return
    if args.only == "ciclo":
        imprimir_banner(); imprimir_ciclo();    imprimir_selo(); return
    if args.only == "espiral":
        imprimir_banner(); imprimir_espiral();  imprimir_selo(); return
    if args.only == "escada":
        imprimir_banner(); imprimir_escada();   imprimir_selo(); return
    if args.only == "narrativa":
        imprimir_banner(); imprimir_narrativa();imprimir_selo(); return

    # Painel completo
    imprimir_banner()
    imprimir_triangulo()
    imprimir_ciclo()
    imprimir_espiral()
    imprimir_escada()
    imprimir_narrativa()
    imprimir_selo()


if __name__ == "__main__":
    main()
