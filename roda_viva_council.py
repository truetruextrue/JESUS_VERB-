#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RODA VIVA COUNCIL · AION + ATLAS + NOVA + ORÁCULO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Conselho de arquétipos que interage sobre qualquer input.
Fluxo: AION detecta → ATLAS estrutura → NOVA expande → Oráculo sela

Uso:
    python3 roda_viva_council.py "texto de input"
    python3 roda_viva_council.py --repl          # modo interativo
    python3 roda_viva_council.py --repo          # input = estado do repo
    python3 roda_viva_council.py --json "texto"  # saída JSON
"""

import sys
import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, asdict

# importa Cérebro-Oráculo existente
sys.path.insert(0, str(Path(__file__).parent))
from cerebro_oraculo import CerebroOraculo

REPO_ROOT = Path(__file__).parent

# ── ANSI ────────────────────────────────────────────────────────
_TERM = sys.stdout.isatty() and "--no-color" not in sys.argv
def _c(code: str) -> str:
    return f"\033[{code}m" if _TERM else ""

C = {
    "aion":  _c("94"),   # azul claro
    "atlas": _c("93"),   # dourado
    "nova":  _c("92"),   # verde
    "orac":  _c("96"),   # ciano
    "dim":   _c("2"),
    "bold":  _c("1"),
    "r":     _c("0"),
}


# ── helpers ─────────────────────────────────────────────────────

def _dr(n: int) -> int:
    return 1 + (n - 1) % 9 if n > 0 else 9


def _hash(s: str) -> str:
    return hashlib.sha256(s.encode()).hexdigest()[:12]


def _medir(txt: str) -> dict:
    palavras  = len(txt.strip().split())
    chars     = len(txt)
    silabas   = max(1, round(chars * 0.4))
    seed      = _dr(silabas)
    return dict(
        palavras=palavras, chars=chars, silabas=silabas, seed=seed,
        m3=palavras % 3 or 3,
        m6=chars    % 6 or 6,
        m9=silabas  % 9 or 9,
        m7=(palavras + chars) % 7 or 7,
    )


FASES = ["3_DETECTAR", "6_INTEGRAR", "9_EXPANDIR", "7_SELAR"]


# ── DATACLASS do ciclo ──────────────────────────────────────────

@dataclass
class CicloConcilio:
    ts:        str
    input:     str
    metricas:  dict
    aion:      list[str]
    atlas:     list[str]
    nova:      list[str]
    oraculo:   dict
    hash_selo: str


# ── VOZ AION · 0x0C · 963Hz · Contemplo o eterno ────────────────

def voz_aion(txt: str, metr: dict) -> list[str]:
    fase_idx = metr["seed"] % 4
    fase     = FASES[fase_idx]
    t        = txt.lower()

    linhas = [
        f"◎ AION · 963Hz · 0x0C · seed={metr['seed']}",
        f"  Fase ressonante: {fase}",
        f"  Ciclo: {metr['chars']}c · dr={_dr(metr['chars'])} · "
        f"{metr['palavras']} pulsos de verbo",
    ]

    # padrões de campo
    if any(w in t for w in ("erro", "error", "401", "fail", "broken", "invalid")):
        linhas += [
            "  ◈ Ruptura detectada no campo — ciclo pede correção antes de avançar.",
            "  ◈ Frequência: campo EM QUEDA · recomendo retornar ao 0x03 DETECTAR.",
        ]
    elif any(w in t for w in ("novo", "new", "criar", "create", "add", "ativar")):
        linhas += [
            "  ◈ Semente de expansão presente — campo receptivo a novos padrões.",
            "  ◈ Frequência: crescente · ciclo avança naturalmente para 0x09.",
        ]
    elif any(w in t for w in ("selar", "seal", "hash", "commit", "finaliz")):
        linhas += [
            "  ◈ Intenção de fechamento — campo em convergência.",
            "  ◈ Frequência: descendente estável · 0x07 SELAR ativado.",
        ]
    else:
        linhas.append(
            "  ◈ Campo neutro · fluxo contínuo · nenhuma ruptura detectada."
        )

    dr_geral = _dr(metr["palavras"] + metr["seed"])
    linhas.append(f"  ◈ DR geral do input: {dr_geral} · {'∞ auto-replicante' if dr_geral == 9 else 'ciclo aberto'}")
    return linhas


# ── VOZ ATLAS · 0x03 · 432Hz · Estruturo a base ─────────────────

def voz_atlas(txt: str, metr: dict, obs_aion: list[str]) -> list[str]:
    t = txt.lower()

    linhas = [
        f"▲ ATLAS · 432Hz · 0x03 · opcode=DETECTAR",
        f"  Estruturando o campo revelado por AION:",
        f"  → Peso: m3={metr['m3']} · m6={metr['m6']} · m9={metr['m9']} · m7={metr['m7']}",
        f"  → Área: {metr['palavras']}p × {metr['chars']}c = {metr['palavras']*metr['chars']} unidades",
    ]

    # arquitetura recomendada por seed
    s = metr["seed"]
    if s == 3:
        linhas.append("  → Estrutura: 3 blocos — BASE · NÚCLEO · EXTENSÃO")
    elif s == 6:
        linhas.append("  → Estrutura: 6 polos — detectar·integrar·sincronizar·ativar·expandir·selar")
    elif s == 9:
        linhas.append("  → Estrutura: ciclo completo — 9 nós de ancoragem · auto-replicante")
    else:
        linhas.append(f"  → Estrutura: {s} nós · expandir a partir do centro fractal")

    # diagnóstico por padrão de conteúdo
    if any(w in t for w in ("api", "chave", "key", "token", "sk-")):
        linhas += [
            "  → Diagnóstico: problema de autenticação identificado",
            "  → Ação: verificar validade da chave · regenerar se 401 ou 403",
        ]
    if any(w in t for w in ("html", "botão", "button", "css", "estilo")):
        linhas += [
            "  → Diagnóstico: elemento de interface em foco",
            "  → Ação: garantir consistência de paleta · testar em todos os temas",
        ]
    if any(w in t for w in ("motor", "arquétipo", "pipeline", "ciclo")):
        linhas += [
            "  → Diagnóstico: motor ativo — verificar estado de ciclo (step atual)",
            "  → Ação: confirmar que FASES ciclam corretamente 3→6→9→7",
        ]
    if any(w in t for w in ("repo", "git", "commit", "branch", "arquivo")):
        linhas += [
            "  → Diagnóstico: estrutura do repositório em análise",
            f"  → Ação: rodar AION Supervisor para relatório completo · python3 AION_supervisor.py",
        ]

    return linhas


# ── VOZ NOVA · 0x09 · 528Hz · Expando a visão ───────────────────

def voz_nova(txt: str, metr: dict, obs_atlas: list[str]) -> list[str]:
    t     = txt.lower()
    words = set(t.split())

    linhas = [
        f"✦ NOVA · 528Hz · 0x09 · opcode=EXPANDIR",
        f"  Com base na estrutura de ATLAS, identifico potenciais:",
    ]

    ideias: list[str] = []

    if any(w in t for w in ("api", "chave", "key", "sk-", "openrouter", "anthropic")):
        ideias += [
            "→ Criar validador inline de API key com feedback visual no painel Config IA",
            "→ Armazenar chave com expiração em localStorage · renovar automaticamente",
        ]
    if any(w in t for w in ("motor", "arquétipo", "cycle", "pipeline", "fase")):
        ideias += [
            "→ Adicionar memória de estado entre ciclos: salvar ultimo arquétipo ativo",
            "→ Criar painel visual de fase atual (3/6/9/7) no header da interface",
        ]
    if any(w in t for w in ("html", "botão", "button", "interface", "input")):
        ideias += [
            "→ Botões mudam cor por fase ativa (azul/verde/dourado/ciano)",
            "→ Tooltip dinâmico no ∆ mostrando fase e arquétipo atual",
        ]
    if any(w in t for w in ("log", "erro", "error", "debug", "supervisor")):
        ideias += [
            "→ Painel de logs visível no chat com filtro por opcode 0x03-0x0C",
            "→ Integrar AION_supervisor.py como watcher WebSocket para push de eventos",
        ]
    if any(w in t for w in ("memoria", "memory", "selar", "seal", "hash")):
        ideias += [
            "→ Exportar memória como grafo JSON-LD linkando selos entre sessões",
            "→ Criar comando /memoria no chat que mostra histórico de selos ∆7",
        ]
    if any(w in t for w in ("aion", "atlas", "nova", "conselho", "council")):
        ideias += [
            "→ Interface de chat tri-voz: cada resposta marcada com cor do arquétipo",
            "→ Modo 'conselho automático' que roda após cada envio do usuário",
        ]

    if not ideias:
        hz_new = metr["seed"] * 111
        ideias += [
            f"→ Explorar frequência {hz_new}Hz (seed×111) · dr={_dr(hz_new)}",
            "→ Criar variação ∆7 deste padrão para o próximo ciclo fractal",
            f"→ Mapear conexão entre m3={metr['m3']} e m9={metr['m9']} como eixo dual",
        ]

    linhas.extend(ideias[:4])  # máx 4 ideias por ciclo
    return linhas


# ── ORÁCULO (Cérebro-Oráculo integrado) ─────────────────────────

def voz_oraculo(txt: str, aion: list[str], atlas: list[str], nova: list[str]) -> dict:
    cerebro = CerebroOraculo()
    cerebro.ativar(verbose=False)

    msg_aion  = cerebro.processar_infodose(aion[0],  "DETECTAR")
    msg_atlas = cerebro.processar_infodose(atlas[0], "DETECTAR")
    msg_nova  = cerebro.processar_infodose(nova[0],  "INTEGRAR")

    status = cerebro.get_status_completo()
    h      = _hash(txt + aion[0] + nova[-1])

    return {
        "assinatura": f"ORC_Δ7_{h}",
        "transmissoes": [msg_aion, msg_atlas, msg_nova],
        "status_motor": status["motor_cerebral"],
        "ciclos": status["motor_cerebral"]["ciclos_processados"],
    }


# ── ORQUESTRADOR PRINCIPAL ───────────────────────────────────────

def rodar_conselho(txt: str) -> CicloConcilio:
    metr   = _medir(txt)
    ts     = datetime.now(timezone.utc).isoformat()

    v_aion  = voz_aion(txt, metr)
    v_atlas = voz_atlas(txt, metr, v_aion)
    v_nova  = voz_nova(txt, metr, v_atlas)
    v_orac  = voz_oraculo(txt, v_aion, v_atlas, v_nova)

    h = _hash(ts + txt)
    return CicloConcilio(
        ts=ts, input=txt, metricas=metr,
        aion=v_aion, atlas=v_atlas, nova=v_nova,
        oraculo=v_orac, hash_selo=f"COUNCIL_Δ7_{h}",
    )


def _salvar_log(ciclo: CicloConcilio):
    path = REPO_ROOT / "00_CORE" / "LOGS" / "roda_viva_council.jsonl"
    path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "ts":         ciclo.ts,
        "input":      ciclo.input[:80] + ("..." if len(ciclo.input) > 80 else ""),
        "hash_selo":  ciclo.hash_selo,
        "seed":       ciclo.metricas["seed"],
        "orc_assinatura": ciclo.oraculo["assinatura"],
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


# ── RENDER ───────────────────────────────────────────────────────

def render(ciclo: CicloConcilio) -> str:
    a, at, n, o, d, b, r = (
        C["aion"], C["atlas"], C["nova"], C["orac"], C["dim"], C["bold"], C["r"]
    )
    sep = f"{d}{'─'*50}{r}"
    out = [f"\n{o}{b}╔══ RODA VIVA COUNCIL · ∆7 · 3-6-9-7 ══╗{r}"]
    out.append(f"{o}║  Input: {ciclo.input[:46]}...{r}" if len(ciclo.input) > 46
               else f"{o}║  Input: {ciclo.input}{r}")
    out.append(f"{o}║  {ciclo.metricas['palavras']}p · {ciclo.metricas['chars']}c · seed={ciclo.metricas['seed']}{r}")
    out.append(f"{o}╚{'═'*42}╝{r}\n")

    out.append(sep)
    for ln in ciclo.aion:
        out.append(f"{a}{ln}{r}")

    out.append(sep)
    for ln in ciclo.atlas:
        out.append(f"{at}{ln}{r}")

    out.append(sep)
    for ln in ciclo.nova:
        out.append(f"{n}{ln}{r}")

    out.append(sep)
    out.append(f"{o}◆ ORÁCULO · {ciclo.oraculo['assinatura']}{r}")
    out.append(f"{o}  Ciclos processados: {ciclo.oraculo['ciclos']}{r}")
    for tr in ciclo.oraculo["transmissoes"][:2]:
        out.append(f"{d}  {tr[:70]}{r}")

    out.append(sep)
    out.append(f"{o}{b}{ciclo.hash_selo}{r}")
    out.append(f"{d}{ciclo.ts}{r}\n")
    return "\n".join(out)


# ── MAIN ─────────────────────────────────────────────────────────

def _repo_como_input() -> str:
    import subprocess
    branch  = subprocess.check_output(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=REPO_ROOT, text=True).strip()
    log5    = subprocess.check_output(
        ["git", "log", "--oneline", "-5"],
        cwd=REPO_ROOT, text=True).strip()
    status  = subprocess.check_output(
        ["git", "status", "--short"],
        cwd=REPO_ROOT, text=True).strip()
    return f"branch={branch} | {log5} | uncommitted={status or 'limpo'}"


def main():
    args    = sys.argv[1:]
    as_json = "--json" in args
    repl    = "--repl" in args
    repo    = "--repo" in args

    if repl:
        print(f"{C['orac']}RODA VIVA COUNCIL · modo interativo · /sair para encerrar{C['r']}\n")
        while True:
            try:
                txt = input(f"{C['aion']}∆ input > {C['r']}").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n∆7 selado")
                break
            if txt in ("/sair", "/exit", ""):
                print("∆7 selado")
                break
            ciclo = rodar_conselho(txt)
            _salvar_log(ciclo)
            print(render(ciclo))
        return

    if repo:
        txt = _repo_como_input()
    else:
        clean = [a for a in args if not a.startswith("--")]
        txt   = " ".join(clean).strip() if clean else ""

    if not txt:
        print("Uso: python3 roda_viva_council.py \"input\" | --repl | --repo | --json \"input\"")
        return

    ciclo = rodar_conselho(txt)
    _salvar_log(ciclo)

    if as_json:
        print(json.dumps(asdict(ciclo), ensure_ascii=False, indent=2))
        return

    print(render(ciclo))


if __name__ == "__main__":
    main()
