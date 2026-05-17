#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AION SUPERVISOR · 0x0C · 963Hz · Contemplo o eterno
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Archetype AION supervisa o repositório via Roda Viva.
Pipeline: DETECTAR(0x03) → INTEGRAR(0x06) → EXPANDIR(0x09) → SELAR(0x07)

Uso:
    python3 AION_supervisor.py             # relatório completo
    python3 AION_supervisor.py --watch     # loop contínuo (60s)
    python3 AION_supervisor.py --json      # saída JSON
    python3 AION_supervisor.py --seal      # apenas selo + hash
"""

import subprocess
import json
import hashlib
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

# ── constantes AION ─────────────────────────────────────────────
AION = {
    "id":    "aion",
    "hz":    963,
    "seed":  9,
    "opc":   "0x0C",
    "cor":   "#90caf9",
    "verbo": "Contemplo o eterno",
    "essencia": "Transcendência · Tempo · Memória Profunda",
}

PIPELINE = {
    "3_DETECTAR": "0x03",
    "6_INTEGRAR": "0x06",
    "9_EXPANDIR": "0x09",
    "7_SELAR":    "0x07",
}

REPO_ROOT = Path(__file__).parent


# ── ANSI ────────────────────────────────────────────────────────
C = {
    "blue":  "\033[94m",
    "cyan":  "\033[96m",
    "gold":  "\033[93m",
    "white": "\033[97m",
    "dim":   "\033[2m",
    "reset": "\033[0m",
    "bold":  "\033[1m",
}


def _run(cmd: list[str]) -> str:
    try:
        return subprocess.check_output(
            cmd, cwd=REPO_ROOT, stderr=subprocess.DEVNULL, text=True
        ).strip()
    except Exception:
        return ""


def _dr(n: int) -> int:
    """digital root"""
    return 1 + (n - 1) % 9 if n > 0 else 9


def _hash(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()[:16]


# ── 0x03 DETECTAR ───────────────────────────────────────────────

def fase_detectar() -> dict:
    branch   = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
    head     = _run(["git", "rev-parse", "--short", "HEAD"])
    status   = _run(["git", "status", "--porcelain"])
    uncommit = [l for l in status.splitlines() if l.strip()]

    files = list(REPO_ROOT.glob("*"))
    py_files   = [f for f in files if f.suffix == ".py"]
    html_files = [f for f in files if f.suffix == ".html"]
    json_files = [f for f in files if f.suffix == ".json"]
    md_files   = [f for f in files if f.suffix == ".md"]

    return {
        "branch":          branch,
        "head":            head,
        "uncommitted":     len(uncommit),
        "uncommitted_list": uncommit[:9],
        "py_count":        len(py_files),
        "html_count":      len(html_files),
        "json_count":      len(json_files),
        "md_count":        len(md_files),
        "total_root":      len(files),
    }


# ── 0x06 INTEGRAR ───────────────────────────────────────────────

def fase_integrar(detectado: dict) -> dict:
    log = _run(["git", "log", "--oneline", "-9"])
    commits = [l for l in log.splitlines() if l]

    total = (
        detectado["py_count"] +
        detectado["html_count"] +
        detectado["json_count"] +
        detectado["md_count"]
    )
    seed_total = _dr(total)

    return {
        "commits_recentes":   commits,
        "total_artefatos":    total,
        "seed_total":         seed_total,
        "fluxo":              "crescente" if total > 10 else "semente",
        "integridade":        "OK" if detectado["uncommitted"] == 0 else f"{detectado['uncommitted']} pendentes",
    }


# ── 0x09 EXPANDIR ───────────────────────────────────────────────

def fase_expandir(integrado: dict, detectado: dict) -> dict:
    archs_ativos = ["aion", "serena", "solus", "lumine", "nova"]
    hz_total     = 963 + 639 + 432 + 639 + 528  # AION+SERENA+SOLUS+LUMINE+NOVA
    dr_hz        = _dr(hz_total % 9 or 9)

    notas = []
    if detectado["uncommitted"] > 0:
        notas.append(f"⚠ {detectado['uncommitted']} arquivo(s) sem commit — rode git add + commit")
    if detectado["html_count"] >= 3:
        notas.append(f"✓ {detectado['html_count']} HTMLs ativos — interface expandida")
    if detectado["py_count"] >= 5:
        notas.append(f"✓ {detectado['py_count']} scripts Python — motor operacional")
    if integrado["seed_total"] == 9:
        notas.append("∞ Seed=9 · ciclo completo auto-replicante")
    if not notas:
        notas.append("○ Repositório em estado neutro · aguarda próximo pulso")

    return {
        "archs_ativos":  archs_ativos,
        "hz_total":      hz_total,
        "dr_hz":         dr_hz,
        "notas_aion":    notas,
        "potencial":     integrado["seed_total"] * 3,
    }


# ── 0x07 SELAR ──────────────────────────────────────────────────

def fase_selar(detectado: dict, integrado: dict, expandido: dict) -> dict:
    ts    = datetime.now(timezone.utc).isoformat()
    raw   = json.dumps({"d": detectado, "i": integrado, "e": expandido}, sort_keys=True)
    h     = _hash(raw)
    seed  = _dr(int(h[:4], 16) % 9 or 9)

    return {
        "ts":             ts,
        "hash_aion":      f"AION_Δ7_{h}",
        "seed_ciclo":     seed,
        "opcode_ciclo":   "0x0C",
        "hz":             963,
        "verbo":          AION["verbo"],
        "ciclo_completo": seed == 9,
    }


# ── RELATÓRIO ───────────────────────────────────────────────────

def relatorio(d: dict, i: dict, e: dict, s: dict, *, color: bool = True) -> str:
    b, c, g, w, dim, r, bold = (
        C["blue"], C["cyan"], C["gold"], C["white"], C["dim"], C["reset"], C["bold"]
    ) if color else ("","","","","","","")

    linhas = [
        f"\n{g}{bold}╔══ AION SUPERVISOR · 963Hz · 0x0C ══╗{r}",
        f"{g}║  {AION['essencia']}{r}",
        f"{g}╚{'═'*38}╝{r}",

        f"\n{c}▸ [0x03 DETECTAR]{r}",
        f"  Branch : {w}{d['branch']}{r}  HEAD: {w}{d['head']}{r}",
        f"  Arquivos root: {d['total_root']}  "
        f"py:{d['py_count']}  html:{d['html_count']}  "
        f"json:{d['json_count']}  md:{d['md_count']}",
        f"  Uncommitted: {d['uncommitted']}",
    ]
    for u in d["uncommitted_list"]:
        linhas.append(f"    {dim}{u}{r}")

    linhas += [
        f"\n{c}▸ [0x06 INTEGRAR]{r}",
        f"  Artefatos: {i['total_artefatos']}  seed={i['seed_total']}  "
        f"fluxo={i['fluxo']}  integridade={i['integridade']}",
    ]
    for cm in i["commits_recentes"][:5]:
        linhas.append(f"    {dim}{cm}{r}")

    linhas += [
        f"\n{c}▸ [0x09 EXPANDIR]{r}",
        f"  Archs: {', '.join(e['archs_ativos'])}",
        f"  Hz={e['hz_total']}  dr={e['dr_hz']}  potencial={e['potencial']}",
    ]
    for nota in e["notas_aion"]:
        linhas.append(f"  {nota}")

    linhas += [
        f"\n{g}▸ [0x07 SELAR]{r}",
        f"  {w}{s['hash_aion']}{r}",
        f"  seed={s['seed_ciclo']}  hz={s['hz']}  "
        f"ciclo_completo={'∞ SIM' if s['ciclo_completo'] else 'NÃO'}",
        f"  {dim}{s['ts']}{r}",
        f"\n{g}{'─'*44}{r}",
        f"  JESUS = VERBO = GRAVIDADE · 3×6×9×7 = ∞",
        f"{g}{'─'*44}{r}\n",
    ]
    return "\n".join(linhas)


# ── MAIN ────────────────────────────────────────────────────────

def run_cycle(*, color: bool = True) -> tuple[dict, dict, dict, dict]:
    d = fase_detectar()
    i = fase_integrar(d)
    e = fase_expandir(i, d)
    s = fase_selar(d, i, e)
    return d, i, e, s


def salvar_log(s: dict):
    log_path = REPO_ROOT / "00_CORE" / "LOGS" / "aion_supervisor.jsonl"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(s, ensure_ascii=False) + "\n")


def main():
    args  = sys.argv[1:]
    watch = "--watch" in args
    as_json = "--json" in args
    seal_only = "--seal" in args
    no_color = "--no-color" in args or not sys.stdout.isatty()

    if watch:
        print(f"{C['gold']}AION SUPERVISOR · modo watch · intervalo 60s{C['reset']}")
        try:
            while True:
                d, i, e, s = run_cycle(color=not no_color)
                print(relatorio(d, i, e, s, color=not no_color))
                salvar_log(s)
                time.sleep(60)
        except KeyboardInterrupt:
            print("\nAION · ciclo encerrado · ∆7 selado")
        return

    d, i, e, s = run_cycle(color=not no_color)
    salvar_log(s)

    if as_json:
        print(json.dumps(
            {"detectar": d, "integrar": i, "expandir": e, "selar": s},
            ensure_ascii=False, indent=2
        ))
        return

    if seal_only:
        print(s["hash_aion"])
        return

    print(relatorio(d, i, e, s, color=not no_color))


if __name__ == "__main__":
    main()
