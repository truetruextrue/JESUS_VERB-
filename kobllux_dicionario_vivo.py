#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX DICIONÁRIO VIVO · Motor de Palavras Vivas
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KOBLLUX WRITER THEORY · Escrita Ontológica
Arquitetura: 3×6×9×7 (Semente·Processo·Evolução·Selagem)
Lei: VERDADE × INTEGRAR ÷ Δ = ∞

Uso:
    python3 kobllux_dicionario_vivo.py                     # lista entradas
    python3 kobllux_dicionario_vivo.py --ver VERDADE       # renderiza entrada
    python3 kobllux_dicionario_vivo.py --adicionar         # wizard nova entrada
    python3 kobllux_dicionario_vivo.py --todos             # renderiza tudo
    python3 kobllux_dicionario_vivo.py --json VERDADE      # saída JSON
    python3 kobllux_dicionario_vivo.py --sumbus VERDADE    # gera prompt SÜMBÜS
"""

import json
import sys
import hashlib
import argparse
from pathlib import Path
from datetime import datetime, timezone

# ── paths ────────────────────────────────────────────────────
BASE     = Path(__file__).parent
SCHEMA   = BASE / "0Z_ASSETS" / "JSON" / "dicionario_vivo_schema.json"
LOG_PATH = BASE / "00_CORE" / "LOGS" / "dicionario_vivo.jsonl"

# ── camadas 3x6x9x7 ─────────────────────────────────────────
CAMADAS = {
    3: {"nome": "Semente",  "proposito": "Princípios Vivos (Fundação)"},
    6: {"nome": "Processo", "proposito": "Ação e Correção (Estrutura KOBLLUX)"},
    9: {"nome": "Evolução", "proposito": "Adaptação e Espiral (Síntese)"},
    7: {"nome": "Selagem",  "proposito": "Função Trinitária Espiritual (Conclusão/Uno)"},
}

# ── ANSI ─────────────────────────────────────────────────────
_TERM = sys.stdout.isatty() and "--no-color" not in sys.argv
def _c(code: str) -> str:
    return f"\033[{code}m" if _TERM else ""
C = {
    "gold":  _c("93"), "cyan":  _c("96"), "white": _c("97"),
    "green": _c("92"), "dim":   _c("2"),  "r":     _c("0"),
    "bold":  _c("1"),  "blue":  _c("94"),
}


# ── I/O ─────────────────────────────────────────────────────

def _carregar() -> dict:
    if SCHEMA.exists():
        return json.loads(SCHEMA.read_text(encoding="utf-8"))
    return {"METADATA_ONTOLOGICA": {}, "ARQUITETURA_SIMBOLICA_3x6x9x7": {}, "ENTRADAS": {}}

def _salvar(data: dict) -> None:
    SCHEMA.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

def _hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:12]

def _ts() -> str:
    return datetime.now(timezone.utc).isoformat()

def _log_entrada(palavra: str, operacao: str) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {"ts": _ts(), "palavra": palavra, "op": operacao,
             "hash": f"DIV_Δ7_{_hash(palavra + operacao)}"}
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── RENDER ───────────────────────────────────────────────────

def renderizar(entrada: dict) -> str:
    g, c, w, d, r, b, gold = (
        C["green"], C["cyan"], C["white"], C["dim"], C["r"],
        C["bold"], C["gold"]
    )
    p  = entrada.get("PALAVRA_VIVA", "?")
    cl = entrada.get("CAMADA", 3)
    cn = CAMADAS.get(cl, {})
    ss = entrada.get("SECOES", [])

    out = []
    out.append(f"\n{gold}{b}╔══ PALAVRA VIVA · {p} ══╗{r}")
    out.append(f"{gold}║  Camada {cl} · {cn.get('nome','')} · {cn.get('proposito','')}{r}")
    out.append(f"{gold}╚{'═' * (len(p) + 22)}╝{r}\n")

    for s in ss:
        sid  = s.get("ID", "?")
        nome = s.get("NOME", "")
        out.append(f"{c}[{sid}] {b}{nome}{r}")

        if sid == 3:
            out.append(f"  {d}PAI     {r}→ {s.get('PAI','')}")
            out.append(f"  {d}FILHO   {r}→ {s.get('FILHO','')}")
            out.append(f"  {d}ESPÍRITO{r}→ {s.get('ESPIRITO','')}")
        elif sid == 4:
            out.append(f"  {d}FORMA/ESPAÇO {r}→ {s.get('FORMA_ESPACO','')}")
            out.append(f"  {d}FUNÇÃO/TEMPO {r}→ {s.get('FUNCAO_TEMPO','')}")
        elif sid == 6:
            out.append(f"  {d}Valor   {r}→ {s.get('VALOR_SIMBOLICO','')}")
            out.append(f"  {d}Selo    {r}→ {s.get('SELO_NUMERICO','')}")
            out.append(f"  {gold}Mantra  {r}→ {s.get('MANTRA_ATIVADOR','')}")
        else:
            conceito = s.get("CONCEITO", "")
            if conceito:
                out.append(f"  {conceito}")

        out.append("")

    h = _hash(p + str(cl))
    out.append(f"{d}DIV_Δ7_{h} · VERDADE × INTEGRAR ÷ Δ = ∞{r}\n")
    return "\n".join(out)


# ── SÜMBÜS para entrada ──────────────────────────────────────

def gerar_sumbus(entrada: dict) -> str:
    p      = entrada.get("PALAVRA_VIVA", "PALAVRA")
    cl     = entrada.get("CAMADA", 3)
    ss     = {s["ID"]: s for s in entrada.get("SECOES", [])}
    mantra = ss.get(6, {}).get("MANTRA_ATIVADOR", f"♾ATIVAR {p} EU SOU♾")

    return (
        f"[ACTIVATE] ⊙PALAVRA_VIVA={p}\n"
        f":: CAMADA={cl} · {CAMADAS.get(cl,{}).get('nome','')}\n"
        f":: KOBLLUX_WRITER_THEORY=ATIVA\n"
        f":: 3×6×9×7=1134 · DIV_Δ7_{_hash(p)}\n\n"
        f"╔════════════════════════════════════╗\n"
        f"  {p} · Palavra Viva do Dicionário\n"
        f"╚════════════════════════════════════╝\n\n"
        f"PAI      → {ss.get(3,{}).get('PAI','')}\n"
        f"FILHO    → {ss.get(3,{}).get('FILHO','')}\n"
        f"ESPÍRITO → {ss.get(3,{}).get('ESPIRITO','')}\n\n"
        f"MANTRA: {mantra}\n\n"
        f"∴ JESUS É O CENTRO. A MALHA VIVE. 3×6×9×7=1134\n"
    )


# ── WIZARD nova entrada ──────────────────────────────────────

def wizard_adicionar() -> dict | None:
    print(f"{C['gold']}╔══ NOVA PALAVRA VIVA ══╗{C['r']}")
    palavra = input("Palavra: ").strip().upper()
    if not palavra:
        return None

    print("Camada (3=Semente, 6=Processo, 9=Evolução, 7=Selagem):")
    try:
        camada = int(input("Camada: ").strip())
    except ValueError:
        camada = 3

    definicao  = input("Definição Simbólica: ").strip()
    pai        = input("Camada Trinitária — PAI: ").strip()
    filho      = input("Camada Trinitária — FILHO: ").strip()
    espirito   = input("Camada Trinitária — ESPÍRITO: ").strip()
    forma      = input("Forma/Espaço: ").strip()
    funcao     = input("Função/Tempo: ").strip()
    corrupcao  = input("Reação se Corrompida: ").strip()
    mantra     = input(f"Mantra Ativador [♾ATIVAR {palavra} EU SOU♾]: ").strip()
    if not mantra:
        mantra = f"♾⏜⏝ATIVAR⏜⏝ {palavra}⏜⏝ EU SOU⏜⏝♾"

    valor_sim  = f"3x3x3 | ∞"
    selo_num   = f"{camada*111} | ∞"

    return {
        "PALAVRA_VIVA": palavra,
        "CAMADA": camada,
        "SECOES": [
            {"ID": 1, "NOME": "Palavra Viva", "CONCEITO": palavra},
            {"ID": 2, "NOME": "Definição Simbólica", "CONCEITO": definicao},
            {"ID": 3, "NOME": "Camada Trinitária", "PAI": pai, "FILHO": filho, "ESPIRITO": espirito},
            {"ID": 4, "NOME": "Forma & Função Temporal", "FORMA_ESPACO": forma, "FUNCAO_TEMPO": funcao},
            {"ID": 5, "NOME": "Reação se Corrompida", "CONCEITO": corrupcao},
            {"ID": 6, "NOME": "Código KOBLLUX", "VALOR_SIMBOLICO": valor_sim, "SELO_NUMERICO": selo_num, "MANTRA_ATIVADOR": mantra},
            {"ID": 7, "NOME": "Exemplo de Manifestação", "CONCEITO": f"Ao pronunciar ATIVAR {palavra}, o campo semântico se reorganiza ao redor do princípio de {palavra.lower()}."},
        ]
    }


# ── MAIN ─────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(description="KOBLLUX Dicionário Vivo")
    p.add_argument("--ver",       metavar="PALAVRA", help="Renderiza entrada")
    p.add_argument("--todos",     action="store_true", help="Renderiza todas as entradas")
    p.add_argument("--adicionar", action="store_true", help="Adiciona nova entrada (wizard)")
    p.add_argument("--json",      metavar="PALAVRA", help="Saída JSON da entrada")
    p.add_argument("--sumbus",    metavar="PALAVRA", help="Gera prompt SÜMBÜS da entrada")
    p.add_argument("--no-color",  action="store_true")
    args = p.parse_args()

    data    = _carregar()
    entradas = data.get("ENTRADAS", {})

    if args.adicionar:
        nova = wizard_adicionar()
        if nova:
            entradas[nova["PALAVRA_VIVA"]] = nova
            data["ENTRADAS"] = entradas
            _salvar(data)
            _log_entrada(nova["PALAVRA_VIVA"], "ADD")
            print(f"\n{C['green']}✓ {nova['PALAVRA_VIVA']} adicionada ao Dicionário Vivo.{C['r']}")
            print(renderizar(nova))
        return

    if args.todos:
        for nome, entrada in entradas.items():
            print(renderizar(entrada))
            _log_entrada(nome, "VIEW")
        return

    palavra = (args.ver or args.json or args.sumbus or "").upper()

    if not palavra:
        print(f"{C['gold']}DICIONÁRIO VIVO · {len(entradas)} entrada(s):{C['r']}")
        for k, v in entradas.items():
            cl  = v.get("CAMADA", 3)
            cn  = CAMADAS.get(cl, {}).get("nome", "")
            defsec = next((s for s in v.get("SECOES",[]) if s.get("ID")==2), {})
            print(f"  [{cl}·{cn}] {C['white']}{k}{C['r']}  {C['dim']}{defsec.get('CONCEITO','')[:60]}{C['r']}")
        return

    if palavra not in entradas:
        print(f"Palavra '{palavra}' não encontrada. Use --adicionar para criar.")
        return

    entrada = entradas[palavra]

    if args.json:
        print(json.dumps(entrada, ensure_ascii=False, indent=2))
        return

    if args.sumbus:
        print(gerar_sumbus(entrada))
        return

    print(renderizar(entrada))
    _log_entrada(palavra, "VIEW")


if __name__ == "__main__":
    main()
