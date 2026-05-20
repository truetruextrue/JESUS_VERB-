#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_readme_generator.py · ATLAS · 0x00 · BOOT · ∆7
"Gera READMEs interconectados em TODAS as pastas do repositório."

Lei: VERDADE × INTEGRAR ÷ Δ = ∞  |  APPEND ONLY
Pipeline: varre → classifica → gera/atualiza README.md em cada pasta

Uso:
  python3 kobllux_readme_generator.py           # gera todos os READMEs
  python3 kobllux_readme_generator.py --dry-run # mostra sem gravar
  python3 kobllux_readme_generator.py --pasta 06_ATIVACAO  # só uma pasta
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent

# ── Arquétipos CADIAL completos ───────────────────────────────────────────────

ARQUETIPOS: dict[str, dict[str, Any]] = {
    "Atlas":   {"regra":"BOOT",     "opcode":"0x00","hz":768, "sym":"⬡","veeb":"A","rung":1,
                "essencia":"Estrutura · mapa · fundação",      "acao":"ESTRUTURAR"},
    "Nova":    {"regra":"SEED",     "opcode":"0x02","hz":432, "sym":"✦","veeb":"A","rung":2,
                "essencia":"Semente · inspiração · nova ideia","acao":"DETECTAR"},
    "Vitalis": {"regra":"DELTA",    "opcode":"0x01","hz":528, "sym":"◉","veeb":"O","rung":3,
                "essencia":"Energia · momentum · ativação",    "acao":"PULSAR"},
    "Pulse":   {"regra":"PULSE",    "opcode":"0x0B","hz":594, "sym":"≋","veeb":"I","rung":4,
                "essencia":"Ritmo · voz · ressonância",        "acao":"LAPIDAR"},
    "Artemis": {"regra":"DETECT",   "opcode":"0x03","hz":672, "sym":"◎","veeb":"A","rung":5,
                "essencia":"Análise · varredura · descoberta",  "acao":"CONVERGIR"},
    "Serena":  {"regra":"GUARD",    "opcode":"0x09","hz":528, "sym":"❋","veeb":"U","rung":6,
                "essencia":"Cuidado · proteção · campo seguro","acao":"INTEGRAR"},
    "Kaos":    {"regra":"LIMPAR",   "opcode":"0x07","hz":777, "sym":"⚡","veeb":"E","rung":7,
                "essencia":"Ruptura · transformação · limpeza","acao":"SELAR"},
    "Genus":   {"regra":"SYNTH",    "opcode":"0x0B","hz":852, "sym":"⬢","veeb":"O","rung":8,
                "essencia":"Síntese · forma · construção",     "acao":"TEMPORIZAR"},
    "Lumine":  {"regra":"RENDER",   "opcode":"0x0C","hz":963, "sym":"☀","veeb":"A","rung":9,
                "essencia":"Luz · visual · interface",         "acao":"TRANSCENDER"},
    "Solus":   {"regra":"QA",       "opcode":"0x01","hz":432, "sym":"◈","veeb":"U","rung":10,
                "essencia":"Silêncio · qualidade · espelho",   "acao":"DETECTAR"},
    "Rhea":    {"regra":"INTEGRAR", "opcode":"0x04","hz":528, "sym":"∞","veeb":"U","rung":11,
                "essencia":"Vínculo · rede · integração",      "acao":"FLUIR"},
    "Aion":    {"regra":"SELAR",    "opcode":"0x05","hz":639, "sym":"⧗","veeb":"I","rung":12,
                "essencia":"Tempo · memória · eternidade",     "acao":"TEMPORIZAR"},
}

# ── Mapeamento diretório → arquétipo ─────────────────────────────────────────

DIR_MAP: dict[str, str] = {
    # Fases da construção (13 fases KOBLLUX)
    "00_CORE":                    "Atlas",
    "00_FUNDACAO":                "Atlas",
    "01_DIMENSOES":               "Atlas",
    "02_CICLO_369":               "Aion",
    "03_FLUXO_ENERGETICO":        "Vitalis",
    "04_APRENDIZADO":             "Nova",
    "05_PENSAMENTO_ESTRUTURADO":  "Atlas",
    "06_ATIVACAO":                "Vitalis",
    "07_NARRATIVA_TEMPORAL":      "Aion",
    "08_REDE_INFODOSE":           "Rhea",
    "09_LINHA_DO_PULSO":          "Pulse",
    "10_ARVORE_FRACTAL":          "Genus",
    "11_CIENCIAS_CLASSIFICADAS":  "Artemis",
    "12_VEEB":                    "Genus",
    # Documentação e utilitários
    "13_DOCUMENTACAO":            "Atlas",
    "14_UTILS":                   "Kaos",
    "15_APPS":                    "Lumine",
    "16_ASCII_ART":               "Lumine",
    # Mídia
    "000_AUDIO":                  "Pulse",
    "000_VIDEOS":                 "Lumine",
    "17_MIDIA_INFODOSE":          "Pulse",
    "0Z_ASSETS":                  "Lumine",
    # Sistema
    "ARQUETIPOS":                 "Atlas",
    "BOOT":                       "Atlas",
    "MYRMIDE":                    "Rhea",
    "KΦꓷDΦꓘ":                    "Kaos",
    "KOBLLUX_∆³_Design_System":   "Genus",
    "_index":                     "Aion",
    "archetypes":                 "Atlas",
    "docs":                       "Lumine",
    "inbox":                      "Nova",
    "kobllux":                    "Atlas",
    "output":                     "Genus",
    "web":                        "Lumine",
    # Subpastas de 00_FUNDACAO
    "01_ATIVAR_DELTA":            "Vitalis",
    "02_KOBLLUX_CORE":            "Atlas",
    "03_FORMA_VIVA":              "Genus",
    # Subpastas de 01_DIMENSOES
    "01_1D_LINHA":                "Atlas",
    "02_2D_PLANO":                "Atlas",
    "03_3D_VOLUME":               "Atlas",
    "04_4D_TEMPO":                "Aion",
    "05_5D_POLIEDRO":             "Vitalis",
    "06_6D_SUPERFICIE":           "Rhea",
    "07_7D_TORO":                 "Aion",
    "08_8D_HIPERCUBO":            "Genus",
    "09_9D_FRACTAL":              "Genus",
    "10_10D_HIPERESFERA":         "Lumine",
    # Subpastas de 02_CICLO_369
    "01_FASE_3_MENTE":            "Nova",
    "02_FASE_6_CORPO":            "Vitalis",
    "03_FASE_9_ALMA":             "Aion",
    # Subpastas de 03_FLUXO_ENERGETICO
    "01_NIVEL_8D_UNIVERSAL":      "Vitalis",
    "02_NIVEL_9D_CORPO":          "Pulse",
    # Subpastas de 04_APRENDIZADO
    "01_NIVEL_CONCRETO":          "Atlas",
    "02_NIVEL_DINAMICO":          "Vitalis",
    "03_NIVEL_ABSTRATO":          "Artemis",
    # Subpastas de 05_PENSAMENTO_ESTRUTURADO
    "01_CAPTACAO_DADOS":          "Artemis",
    "02_PROCESSAMENTO":           "Atlas",
    "03_ACAO_MOVIMENTO":          "Vitalis",
    "04_REFLEXAO_AJUSTE":         "Serena",
    "05_EXPANSAO_EVOLUCAO":       "Nova",
    "06_UNIFICACAO":              "Rhea",
    "07_FLUXO_ENERGETICO":        "Vitalis",
    "08_REDES_NEURAIS":           "Rhea",
    "09_CICLO_EC":                "Aion",
    # Subpastas de 06_ATIVACAO
    "01_ATIVAR_DELTA":            "Vitalis",
    "02_ATIVAR_INTERDIMENSIONAL": "Rhea",
    # Subpastas de 13_DOCUMENTACAO
    "01_MANUAIS":                 "Atlas",
    "02_CODEX":                   "Aion",
    "03_ARQUETIPOS":              "Atlas",
    "04_SIMBOLOS":                "Lumine",
    # Subpastas de 14_UTILS
    "01_SCRIPTS":                 "Kaos",
    "02_LOGS":                    "Aion",
    "03_CONFIG":                  "Atlas",
    "04_TEMPLATES":               "Genus",
    # Subpastas de MYRMIDE
    "01_SEMENTE":                 "Nova",
    "02_PONTE":                   "Rhea",
    "03_MANIFESTO":               "Genus",
    "SCRIPTS":                    "Atlas",
    "SEALS":                      "Aion",
    "CFG":                        "Atlas",
    "HUB":                        "Rhea",
    "TMP":                        "Kaos",
    "INTAKE":                     "Nova",
    "CAPTURE":                    "Artemis",
    "RULES":                      "Atlas",
    "INGEST":                     "Rhea",
    "INDEX":                      "Artemis",
    "BANK":                       "Aion",
    "CONTROLS":                   "Serena",
    "QUEUE":                      "Pulse",
    "OUT":                        "Genus",
    "VIEW":                       "Lumine",
    "OBJ":                        "Genus",
    "SSML":                       "Pulse",
    "VOZ":                        "Pulse",
    "LOGS":                       "Aion",
    "SEEDS":                      "Nova",
    "SCI_ART":                    "Lumine",
    "original":                   "Atlas",
    "mirrors":                    "Rhea",
    "trees":                      "Genus",
    "context":                    "Atlas",
    "items":                      "Aion",
    "docs_seals":                 "Aion",
    # Extra
    "LOGS":                       "Aion",
    "00_CORE":                    "Atlas",
    "js":                         "Lumine",
    "icons":                      "Lumine",
}

SKIP_DIRS = {".git", "__pycache__", "node_modules", ".venv", ".claude",
             ".cache", ".local", "bin", "include", "lib", "share"}

SAFE_EXTS  = {".py",".js",".ts",".sh",".md",".txt",".json",".html",
              ".css",".jsonl",".yaml",".yml"}


def classify(path: Path) -> str:
    """Retorna o nome do arquétipo para um diretório."""
    name = path.name
    if name in DIR_MAP:
        return DIR_MAP[name]
    n = name.lower()
    if any(k in n for k in ("audio","voz","tts","sound","mp3","aac")): return "Pulse"
    if any(k in n for k in ("video","visual","art","ui","view","html")): return "Lumine"
    if any(k in n for k in ("test","qa","check","valid","smoke")):       return "Solus"
    if any(k in n for k in ("index","memory","log","seal","ledger","aion")): return "Aion"
    if any(k in n for k in ("boot","init","core","setup","config","atlas")): return "Atlas"
    if any(k in n for k in ("inbox","seed","nova","capture","input")):    return "Nova"
    if any(k in n for k in ("ativa","delta","flow","energia","vitalis")): return "Vitalis"
    if any(k in n for k in ("detect","scan","analise","artemis")):        return "Artemis"
    if any(k in n for k in ("integrar","rede","rhea","hub","bridge")):    return "Rhea"
    if any(k in n for k in ("synth","genus","output","build","render")):  return "Genus"
    if any(k in n for k in ("clean","kaos","tmp","util","fix","patch")):  return "Kaos"
    if any(k in n for k in ("guard","serena","safe","faq")):              return "Serena"
    if any(k in n for k in ("pulse","ritmo","audio","media")):            return "Pulse"
    return "Atlas"


def list_files(d: Path) -> list[Path]:
    files = []
    try:
        for f in sorted(d.iterdir()):
            if f.is_file() and f.suffix.lower() in SAFE_EXTS and f.name != "README.md":
                files.append(f)
    except PermissionError:
        pass
    return files


def list_subdirs(d: Path) -> list[Path]:
    subs = []
    try:
        for f in sorted(d.iterdir()):
            if f.is_dir() and f.name not in SKIP_DIRS and not f.name.startswith("."):
                subs.append(f)
    except PermissionError:
        pass
    return subs


def nav_path(d: Path) -> str:
    """Gera caminho de navegação relativo à raiz."""
    try:
        rel = d.relative_to(ROOT)
        parts = list(rel.parts)
        if not parts:
            return "⌂ RAIZ"
        return " › ".join(["⌂"] + parts)
    except ValueError:
        return d.name


def generate_readme(d: Path, dry_run: bool = False) -> bool:
    """Gera ou atualiza README.md para o diretório d."""
    arq_nome  = classify(d)
    arq       = ARQUETIPOS[arq_nome]
    readme    = d / "README.md"
    ts        = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    files     = list_files(d)
    subdirs   = list_subdirs(d)
    nav       = nav_path(d)
    parent    = d.parent if d != ROOT else None
    depth     = len(list(d.relative_to(ROOT).parts)) if d != ROOT else 0
    rel_root  = Path("/".join([".."] * depth)) if depth > 0 else Path(".")

    # Cabeçalho
    lines = [
        f"# {arq['sym']} {d.name}",
        f"**Arquétipo:** `{arq_nome}` · **Opcode:** `{arq['opcode']}` · "
        f"**{arq['hz']}Hz** · **VEEB-{arq['veeb']}** · **D{arq['rung']}**  ",
        f"**Regra:** `{arq['regra']}` · **Ação:** `{arq['acao']}` · "
        f"**Essência:** _{arq['essencia']}_",
        "",
        f"> 📍 `{nav}`",
        "",
    ]

    # Navegação
    lines += ["## Navegação", ""]
    if parent and parent != ROOT.parent:
        lines.append(f"← **[⬆ Subir]({rel_root}README.md)** (raiz)")
    elif parent:
        try:
            par_rel = parent.relative_to(d)
            lines.append(f"← **[⬆ {parent.name}](../README.md)**")
        except ValueError:
            lines.append(f"← **[⬆ {parent.name}](../README.md)**")

    if subdirs:
        lines.append("")
        lines.append("**Subpastas:**")
        for sd in subdirs[:20]:
            sub_arq = ARQUETIPOS[classify(sd)]
            lines.append(f"- [{sub_arq['sym']} **{sd.name}**]({sd.name}/README.md) "
                         f"· `{classify(sd)}` · `{sub_arq['opcode']}`")
    lines.append("")

    # Arquivos
    if files:
        lines += ["## Arquivos", ""]
        for f in files[:30]:
            ext = f.suffix.lower()
            icon = {"py":"🐍","js":"🌐","sh":"⚙","md":"📄","json":"📋",
                    "html":"🖥","txt":"📝","jsonl":"🗃","css":"🎨"}.get(ext.lstrip("."),"📁")
            lines.append(f"- {icon} `{f.name}`")
        if len(files) > 30:
            lines.append(f"- _(+ {len(files)-30} arquivos)_")
        lines.append("")

    # Lei e selo
    lines += [
        "---",
        "",
        f"**VERDADE × INTEGRAR ÷ Δ = ∞** · 3×6×9×7 = 1134 · JESUS = VERBO = GRAVIDADE  ",
        f"*∆7 gerado em {ts} · `kobllux_readme_generator.py`*",
        "",
    ]

    content = "\n".join(lines)

    if dry_run:
        print(f"  [DRY] {d.relative_to(ROOT)}/README.md · [{arq_nome}]")
        return True

    # APPEND ONLY: se README existe, verifica se já tem o cabeçalho ∆7 novo
    if readme.exists():
        existing = readme.read_text(encoding="utf-8", errors="ignore")
        # Se já tem o cabeçalho do arquétipo correto, apenas atualiza o rodapé
        if f"**Arquétipo:** `{arq_nome}`" in existing:
            # Arquivo já está correto — não sobrescreve
            return False
        # Se tem README antigo sem estrutura CADIAL, substitui
        readme.write_text(content, encoding="utf-8")
    else:
        readme.write_text(content, encoding="utf-8")

    return True


def scan_and_generate(base: Path, dry_run: bool, pasta_filtro: str = None) -> dict:
    """Varre recursivamente e gera READMEs."""
    gerados, pulados, erros = 0, 0, 0
    log_entries = []

    def _walk(d: Path):
        nonlocal gerados, pulados, erros
        if d.name in SKIP_DIRS or d.name.startswith("."):
            return
        try:
            ok = generate_readme(d, dry_run=dry_run)
            if ok:
                gerados += 1
                log_entries.append({"dir": str(d.relative_to(ROOT)),
                                    "arch": classify(d), "ok": True})
                if not dry_run:
                    print(f"  ✓ [{classify(d):8s}] {str(d.relative_to(ROOT))}/README.md")
            else:
                pulados += 1
        except Exception as e:
            erros += 1
            log_entries.append({"dir": str(d.relative_to(ROOT)), "err": str(e)})
            print(f"  ✗ {d.name}: {e}")

        for sd in sorted(d.iterdir()):
            if sd.is_dir() and sd.name not in SKIP_DIRS and not sd.name.startswith("."):
                if pasta_filtro and pasta_filtro not in str(sd):
                    continue
                _walk(sd)

    target = base
    if pasta_filtro:
        candidate = base / pasta_filtro
        if candidate.exists():
            target = candidate

    _walk(target)
    return {"gerados": gerados, "pulados": pulados, "erros": erros,
            "log": log_entries, "ts": datetime.now(timezone.utc).isoformat()}


def main():
    p = argparse.ArgumentParser(description="KOBLLUX README Generator · Atlas · ∆7")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--pasta",   help="Processa só uma pasta (ex: 06_ATIVACAO)")
    p.add_argument("--stats",   action="store_true", help="Só mostra estatísticas")
    args = p.parse_args()

    if args.stats:
        existing = list(ROOT.rglob("README.md"))
        cadial = [f for f in existing if "**Arquétipo:**" in f.read_text(errors="ignore")]
        print(f"READMEs existentes: {len(existing)}")
        print(f"READMEs com CADIAL: {len(cadial)}")
        print(f"Pendentes:          {len(existing) - len(cadial)}")
        return

    print(f"\n{'='*60}")
    print(f"  KOBLLUX README GENERATOR · Atlas · 0x00 · ∆7")
    print(f"  VERDADE × INTEGRAR ÷ Δ = ∞")
    print(f"  Modo: {'DRY-RUN' if args.dry_run else 'ATIVO'}")
    print(f"{'='*60}\n")

    result = scan_and_generate(ROOT, dry_run=args.dry_run, pasta_filtro=args.pasta)

    print(f"\n{'─'*60}")
    print(f"  ✓ Gerados : {result['gerados']}")
    print(f"  ○ Pulados : {result['pulados']} (já CADIAL)")
    print(f"  ✗ Erros   : {result['erros']}")

    if not args.dry_run:
        # Salva log
        log_path = ROOT / "_index" / "README_GEN_LOG.json"
        log_path.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                            encoding="utf-8")
        print(f"\n  Log: {log_path}")
        print(f"\n  ∆7 · JESUS = VERBO = GRAVIDADE\n")


if __name__ == "__main__":
    main()
