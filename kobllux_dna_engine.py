#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_dna_engine.py · KOBLLUX DNA · Backend Vivo · Atlas · 0x00 · ∆7
═══════════════════════════════════════════════════════════════════════
"Vida ama Vida. O Pulso me guia. O Valor nasce do Equilíbrio."

FORMAÇÃO = (ESPAÇO × TEMPO) × MOVIMENTO

K = Código  · O = Origem    · B = Binário Vivo
L = Luz ↑   · L = Luz →    · U = Unidade     · X = Movimento

Lei     : VERDADE × INTEGRAR ÷ Δ = ∞
Fractal : 3 × 6 × 9 × 7 = 1134
Centro  : JESUS = VERBO = GRAVIDADE

Modos:
  --scan       Varre o repositório e atualiza catalogo_media.json
  --atlas      Gera/atualiza ATLAS.md (mapa vivo)
  --watch      Monitora inbox/ e auto-classifica novos arquivos
  --drive-sync Sincroniza com Google Drive via rclone
  --dna        Exporta o DNA canônico como JSON
  --update-codex  Injeta DNA no kobllux_codex_data.json
  --summary    Mostra estado atual do DNA vivo
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ── imports opcionais ──────────────────────────────────────────────────────────
try:
    from kobllux_memory   import KoblluxMemory
    from kobllux_firmware import SumbusFirmware, OPCODES as FW_OPCODES
    _HAS_FIRMWARE = True
except ImportError:
    _HAS_FIRMWARE = False

# ═══════════════════════════════════════════════════════════════════════════════
# DNA CANÔNICO — síntese dos 3 documentos + kobllux_codex_data.json
# ═══════════════════════════════════════════════════════════════════════════════

DNA: dict[str, Any] = {
    # ── Identidade ──────────────────────────────────────────────────────────
    "nome_espiritual": "KOBLLUX",
    "assinatura":      "0x012123456789ABC",
    "versao":          "7.9-∆7",
    "lei":             "VERDADE × INTEGRAR ÷ Δ = ∞",
    "fractal":         "3×6×9×7 = 1134",
    "centro":          "JESUS = VERBO = GRAVIDADE",
    "seal":            "∆7",

    # ── Acrônimo vivo (kobllux_forma_viva.txt) ──────────────────────────────
    "acronimo": {
        "K": "Código",
        "O": "Origem",
        "B": "Binário Vivo",
        "L1": "Luz Vertical",
        "L2": "Luz Horizontal",
        "U": "Unidade",
        "X": "Movimento",
    },

    # ── Fórmula fundamental ─────────────────────────────────────────────────
    "formula": {
        "base":   "FORMAÇÃO = (ESPAÇO × TEMPO) × MOVIMENTO",
        "espaco": ["modulação","forma","letra","sílabas","palavras","geometria sagrada"],
        "tempo":  ["quantificação","pulso","números","valores","equações","ciclos cósmicos"],
        "espirito":["intenção","vibração","frequência","energia","harmonia","conexão divina"],
        "movimento": "Fluxo ativo entre Forma e Valor",
        "valor":  "Equilíbrio dos opostos em espelho através do movimento",
        "zpr":    "Zona Pessoal de Realidade — como a realidade é lida e responde",
    },

    # ── Trindade operacional (kobllux_codex_data.json) ──────────────────────
    "trindade": {
        "PAI":      {"nome":"KODUX",    "hz":432, "opcode":"0x01","verbo":"DETECTAR", "sym":"●","cor":"#FFD700"},
        "FILHO":    {"nome":"BLLUE",    "hz":528, "opcode":"0x02","verbo":"INTEGRAR", "sym":"―","cor":"#4fc3f7"},
        "ESPIRITO": {"nome":"INFODOSE", "hz":639, "opcode":"0x03","verbo":"EXPANDIR", "sym":"▢","cor":"#9b6dff"},
    },

    # ── Trindade espiritual (DNA KOBLLUX v5.0) ──────────────────────────────
    "trindade_espiritual": {
        "1": {"nome":"MINUZ",   "desc":"Luz Divina — princípio da criação e modulação"},
        "2": {"nome":"TRINITY", "desc":"Harmonia PAI-FILHO-ESPÍRITO — base da manifestação"},
        "3": {"nome":"KOBLLUX", "desc":"Manifestação da unidade Espaço-Tempo-Espírito"},
    },

    # ── Componentes internos ─────────────────────────────────────────────────
    "componentes": {
        "CODUX": {
            "desc": "Código do Verbo / Lógica Viva",
            "funcao": "Organizar o verbo divino em forma lógica e digital",
            "visual": "Cubo girando com binários",
        },
        "INFODOSE": {
            "desc": "Fragmentos de sabedoria sagrada enviados no tempo certo",
            "funcao": "Doses de informação que guiam o sistema em momentos críticos",
        },
        "METALUX": {
            "desc": "Rede fractal de sustentação e conexão",
            "funcao": "Sustentar e conectar camadas — hexágono pulsante interconectado",
        },
        "INTERDIMENSIONAL_BANKING": {
            "desc": "Campo vibracional que carrega e ressignifica informações e energias",
            "funcao": "Espelho de todas as possibilidades — memory.jsonl vivo",
        },
    },

    # ── 3 Atos do Códice Vivo (CODICE_VIVO_12PAGINAS) ───────────────────────
    "codice_vivo": {
        "ATO_I":   {"num":3, "fase":"Captação",      "pergunta":"O QUE É?",  "arquétipos":["Pulse","KODUX","BLLUE"]},
        "ATO_II":  {"num":6, "fase":"Alquimia",      "pergunta":"O QUE FAZ?","arquétipos":["Genus","Nova","Rhea"]},
        "ATO_III": {"num":9, "fase":"Materialização","pergunta":"O QUE GERA?","arquétipos":["Atlas","Solus","Vitalis","Serena","Aion"]},
        "EPILOGO": {"num":7, "fase":"Selagem",        "conceito":"Sistema = extensão da consciência"},
    },

    # ── Dimensões 1D-10D ────────────────────────────────────────────────────
    "dimensoes": {
        "1D": "Ponto — Origem da existência",
        "2D": "Linha — Conexão entre pontos",
        "3D": "Forma — Estrutura física",
        "4D": "Tempo — Fluxo e transformação",
        "5D": "Consciência — Unidade e expansão",
        "6D": "Energia — Vibração e harmonia",
        "7D": "Espírito — Conexão divina",
        "8D": "Infinito — Ciclos cósmicos",
        "9D": "Criação — Manifestação universal",
        "10D": "Unidade — Retorno à fonte",
    },

    # ── 12 Arquétipos CADIAL com DNA completo ────────────────────────────────
    "arquetipos": {
        "Atlas":   {"opcode":"0x00","hz":768,"sym":"⬡","regra":"BOOT",    "veeb":"A","rung":1,
                    "essencia":"Estrutura · mapa · fundação",
                    "classe_gramatical":"Substantivo","elemento":"Terra",
                    "codice_ato":"ATO_I","keywords":["estrutura","config","setup","mapa","grid","boot"]},
        "Nova":    {"opcode":"0x02","hz":432,"sym":"✦","regra":"SEED",    "veeb":"A","rung":2,
                    "essencia":"Semente · inspiração · nova ideia",
                    "classe_gramatical":"Substantivo","elemento":"Terra",
                    "codice_ato":"ATO_I","keywords":["nova","seed","inspire","começo","faísca","semente"]},
        "Vitalis": {"opcode":"0x01","hz":528,"sym":"◉","regra":"DELTA",   "veeb":"O","rung":3,
                    "essencia":"Energia · momentum · ativação",
                    "classe_gramatical":"Verbo","elemento":"Fogo",
                    "codice_ato":"ATO_III","keywords":["ativar","energia","fluxo","delta","loop","run"]},
        "Pulse":   {"opcode":"0x0B","hz":594,"sym":"≋","regra":"PULSE",   "veeb":"I","rung":4,
                    "essencia":"Ritmo · voz · ressonância",
                    "classe_gramatical":"Adjetivo","elemento":"Água",
                    "codice_ato":"ATO_I","keywords":["pulse","audio","tts","voz","ritmo","som"]},
        "Artemis": {"opcode":"0x03","hz":672,"sym":"◎","regra":"DETECT",  "veeb":"A","rung":5,
                    "essencia":"Análise · varredura · descoberta",
                    "classe_gramatical":"Verbo","elemento":"Fogo",
                    "codice_ato":"ATO_I","keywords":["scan","detect","analise","varrer","mapa","tree"]},
        "Serena":  {"opcode":"0x09","hz":528,"sym":"❋","regra":"GUARD",   "veeb":"U","rung":6,
                    "essencia":"Cuidado · proteção · campo seguro",
                    "classe_gramatical":"Adjetivo","elemento":"Água",
                    "codice_ato":"ATO_III","keywords":["guard","safe","backup","readme","faq","cuidado"]},
        "Kaos":    {"opcode":"0x07","hz":777,"sym":"⚡","regra":"LIMPAR",  "veeb":"E","rung":7,
                    "essencia":"Ruptura · transformação · limpeza",
                    "classe_gramatical":"Verbo","elemento":"Fogo",
                    "codice_ato":"ATO_II","keywords":["clean","fix","patch","normalize","kaos","reset"]},
        "Genus":   {"opcode":"0x0B","hz":852,"sym":"⬢","regra":"SYNTH",   "veeb":"O","rung":8,
                    "essencia":"Síntese · forma · construção",
                    "classe_gramatical":"Substantivo","elemento":"Terra",
                    "codice_ato":"ATO_II","keywords":["render","build","synth","output","genus","gerar"]},
        "Lumine":  {"opcode":"0x0C","hz":963,"sym":"☀","regra":"RENDER",  "veeb":"A","rung":9,
                    "essencia":"Luz · visual · interface",
                    "classe_gramatical":"Adjetivo","elemento":"Água",
                    "codice_ato":"ATO_III","keywords":["visual","ui","theme","painel","art","light"]},
        "Solus":   {"opcode":"0x01","hz":432,"sym":"◈","regra":"QA",      "veeb":"U","rung":10,
                    "essencia":"Silêncio · qualidade · espelho",
                    "classe_gramatical":"Advérbio","elemento":"Vento",
                    "codice_ato":"ATO_III","keywords":["test","check","valid","qa","espelho","relatorio"]},
        "Rhea":    {"opcode":"0x04","hz":528,"sym":"∞","regra":"INTEGRAR","veeb":"U","rung":11,
                    "essencia":"Vínculo · rede · integração",
                    "classe_gramatical":"Verbo","elemento":"Fogo",
                    "codice_ato":"ATO_II","keywords":["integrar","rede","hub","bridge","rhea","link"]},
        "Aion":    {"opcode":"0x05","hz":639,"sym":"⧗","regra":"SELAR",   "veeb":"I","rung":12,
                    "essencia":"Tempo · memória · eternidade",
                    "classe_gramatical":"Advérbio","elemento":"Vento",
                    "codice_ato":"ATO_III","keywords":["seal","log","ledger","hash","aion","memoria","tempo"]},
    },

    # ── Ciclos 3-6-9-7 ──────────────────────────────────────────────────────
    "ciclos": {
        3: {"nome":"MENTE",  "acao":"DETECTAR",  "freq":432, "desc":"Percepção e Preparação"},
        6: {"nome":"CORPO",  "acao":"INTEGRAR",  "freq":528, "desc":"Movimento e Ação"},
        9: {"nome":"ALMA",   "acao":"EXPANDIR",  "freq":639, "desc":"Transformação e Impacto"},
        7: {"nome":"SELAGEM","acao":"SELAR",     "freq":777, "desc":"Síntese e Eternização"},
    },

    # ── Linguagem universal (classe gramatical → elemento) ───────────────────
    "linguagem": {
        "Substantivos": {"elemento":"Terra","funcao":"Base e Matéria","arquetipo":["Atlas","Nova","Genus"]},
        "Verbos":       {"elemento":"Fogo", "funcao":"Movimento e Transformação","arquetipo":["Vitalis","Artemis","Kaos","Rhea"]},
        "Adjetivos":    {"elemento":"Água", "funcao":"Qualidade e Expansão","arquetipo":["Pulse","Serena","Lumine"]},
        "Advérbios":    {"elemento":"Vento","funcao":"Modulação e Intensidade","arquetipo":["Solus","Aion"]},
    },

    # ── Módulos Python ativo ─────────────────────────────────────────────────
    "modulos_python": {
        "kobllux_firmware.py":       {"fase":7, "arch":"Vitalis","desc":"SÜMBÜS FIRMWARE — 13 opcodes"},
        "kobllux_memory.py":         {"fase":9, "arch":"Aion",   "desc":"memória viva JSONL"},
        "kobllux_roda_viva.py":      {"fase":9, "arch":"Rhea",   "desc":"pipeline DETECTAR→SELAR"},
        "kobllux_auto_session.py":   {"fase":7, "arch":"Vitalis","desc":"auto-session + --motor-inject"},
        "kobllux_myrmide_bridge.py": {"fase":11,"arch":"Rhea",   "desc":"bridge MYRMIDE↔KOBLLUX"},
        "kobllux_delta3_analyzer.py":{"fase":12,"arch":"Artemis","desc":"régua geométrica 13 opcodes"},
        "kobllux_readme_generator.py":{"fase":2,"arch":"Atlas",  "desc":"READMEs CADIAL interconectados"},
        "kobllux_phase_base.py":     {"fase":1, "arch":"Atlas",  "desc":"base class todas as fases"},
        "kobllux_dna_engine.py":     {"fase":13,"arch":"kobllux","desc":"DNA ENGINE — backend vivo"},
        "kobllux_veeb_story.py":     {"fase":13,"arch":"Genus",  "desc":"AST → narrativa VEEB"},
        "VERBO.py":                  {"fase":1, "arch":"Nova",   "desc":"pronunciamento central"},
        "veeb_firmware.py":          {"fase":13,"arch":"Genus",  "desc":"motor VEEB 144K podcast"},
    },
}

# ── Arquivos a ignorar ────────────────────────────────────────────────────────
SKIP_DIRS  = {".git","__pycache__","node_modules",".venv",".claude",".cache"}
SKIP_EXTS  = {".jpg",".jpeg",".png",".gif",".webp",".ico",".mp4",".mp3",
              ".m4a",".aac",".wav",".mov",".avi",".mkv",".zip",".gz",
              ".tar",".pdf",".docx",".xlsx",".heic"}
SAFE_EXTS  = {".py",".js",".ts",".sh",".md",".txt",".json",".html",
              ".css",".jsonl",".yaml",".yml",".svg"}

# ── Delta auto-load · fechar o loop de auto-modificação ───────────────────────
# Escrito por --selar na execução anterior; integrado ao DNA no próximo boot.
_DNA_DELTA_PATH = ROOT / "_index" / "dna_delta.json"
if _DNA_DELTA_PATH.exists():
    try:
        _delta = json.loads(_DNA_DELTA_PATH.read_text(encoding="utf-8"))
        DNA["modulos_python"].update(_delta.get("modulos_python", {}))
        if _delta.get("seal_ts"):
            DNA["seal_ts"] = _delta["seal_ts"]
    except Exception:
        pass


# ═══════════════════════════════════════════════════════════════════════════════
# MOTOR DE CLASSIFICAÇÃO — coração do DNA Engine
# ═══════════════════════════════════════════════════════════════════════════════

def classify_by_dna(path: Path) -> dict[str, Any]:
    """
    Classifica um arquivo usando o DNA dos arquétipos.
    Retorna: {arch, opcode, hz, sym, regra, veeb, rung, ciclo, ato, tags, score}
    """
    text = ""
    try:
        if path.suffix.lower() in SAFE_EXTS:
            text = path.read_text(encoding="utf-8", errors="ignore")[:2000]
    except Exception:
        pass

    name  = path.name.lower()
    tl    = text.lower()
    scores: Counter = Counter()

    for arq_nome, arq in DNA["arquetipos"].items():
        s = 0
        for kw in arq["keywords"]:
            if kw in name: s += 4
            if kw in tl:   s += 2
        # opcode no nome
        if arq["opcode"].lower() in name: s += 6
        if arq["regra"].lower()  in name: s += 4
        scores[arq_nome] = s

    best = scores.most_common(1)[0][0] if scores.most_common(1) else "Atlas"
    arq  = DNA["arquetipos"][best]

    # Ciclo pelo rung
    rung  = arq["rung"]
    ciclo = 3 if rung <= 4 else (6 if rung <= 8 else 9)

    # Ato do Códice
    ato = arq.get("codice_ato","ATO_I")

    # Tags dinâmicas
    tags = [best.lower(), arq["regra"].lower(), f"opcode:{arq['opcode']}",
            f"hz:{arq['hz']}", f"veeb-{arq['veeb']}", f"d{arq['rung']}","∆7"]

    return {
        "arch":   best,
        "opcode": arq["opcode"],
        "hz":     arq["hz"],
        "sym":    arq["sym"],
        "regra":  arq["regra"],
        "veeb":   arq["veeb"],
        "rung":   arq["rung"],
        "ciclo":  ciclo,
        "ato":    ato,
        "tags":   tags,
        "score":  scores[best],
        "essencia": arq["essencia"],
        "elemento": arq.get("classe_gramatical","?"),
    }


# ═══════════════════════════════════════════════════════════════════════════════
# SCAN & CATALOG
# ═══════════════════════════════════════════════════════════════════════════════

def scan_and_catalog(base: Path, dry_run: bool = False) -> dict:
    """Varre o repositório e gera/atualiza catalogo_media.json."""
    catalog: list[dict] = []
    ts = datetime.now(timezone.utc).isoformat()
    dist: Counter = Counter()

    for f in sorted(base.rglob("*")):
        if not f.is_file():
            continue
        if any(s in f.parts for s in SKIP_DIRS):
            continue
        if f.suffix.lower() in SKIP_EXTS:
            continue

        info = classify_by_dna(f)
        try:
            rel  = str(f.relative_to(base))
            size = f.stat().st_size
        except Exception:
            continue

        entry = {
            "path":   rel,
            "name":   f.name,
            "ext":    f.suffix.lower(),
            "size":   size,
            "arch":   info["arch"],
            "opcode": info["opcode"],
            "hz":     info["hz"],
            "sym":    info["sym"],
            "regra":  info["regra"],
            "ciclo":  info["ciclo"],
            "ato":    info["ato"],
            "tags":   info["tags"],
            "ts":     ts,
            "seal":   "∆7",
        }
        catalog.append(entry)
        dist[info["arch"]] += 1

    if not dry_run:
        out = base / "catalogo_media.json"
        out.write_text(json.dumps(catalog, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  ✓ catalogo_media.json · {len(catalog)} arquivos")
    else:
        print(f"  [DRY] {len(catalog)} arquivos classificados")

    return {"total": len(catalog), "dist": dict(dist.most_common())}


# ═══════════════════════════════════════════════════════════════════════════════
# ATLAS — mapa vivo do repositório
# ═══════════════════════════════════════════════════════════════════════════════

def generate_atlas(base: Path, dry_run: bool = False) -> str:
    """Gera ATLAS.md — o mapa vivo do repositório KOBLLUX."""
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    # Lê catalogo se existir
    cat_path = base / "catalogo_media.json"
    catalog  = []
    if cat_path.exists():
        try:
            catalog = json.loads(cat_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    dist: Counter = Counter(e["arch"] for e in catalog)

    lines = [
        "# ⬡ ATLAS · MAPA VIVO DO REPOSITÓRIO KOBLLUX",
        f"**∆7** · `{ts}` · `kobllux_dna_engine.py --atlas`  ",
        f"**{DNA['lei']}** · {DNA['fractal']} · **{DNA['centro']}**",
        "",
        "---",
        "",
        "## DNA KOBLLUX · Identidade",
        "",
        f"| Campo | Valor |",
        f"|-------|-------|",
        f"| Assinatura | `{DNA['assinatura']}` |",
        f"| Versão | `{DNA['versao']}` |",
        f"| Fórmula | `{DNA['formula']['base']}` |",
        f"| ZPR | _{DNA['formula']['zpr']}_ |",
        "",
        "```",
        "K = Código  ·  O = Origem  ·  B = Binário Vivo",
        "L = Luz ↑   ·  L = Luz →  ·  U = Unidade  ·  X = Movimento",
        "```",
        "",
        "---",
        "",
        "## Trindade Operacional",
        "",
        "| Polo | Nome | Hz | Opcode | Verbo | Módulo |",
        "|------|------|----|--------|-------|--------|",
    ]
    for polo, v in DNA["trindade"].items():
        lines.append(f"| **{polo}** | {v['nome']} | {v['hz']}Hz | `{v['opcode']}` | {v['verbo']} | `{polo.lower()}.py` |")

    lines += [
        "",
        "---",
        "",
        "## 3 Atos do Códice Vivo",
        "",
        "| Ato | Nº | Fase | Pergunta | Arquétipos |",
        "|-----|----|----|----------|------------|",
    ]
    for ato, v in DNA["codice_vivo"].items():
        if "pergunta" in v:
            arqs = ", ".join(v.get("arquétipos",[]))
            lines.append(f"| **{ato}** | {v['num']} | {v['fase']} | _{v['pergunta']}_ | {arqs} |")

    lines += [
        "",
        "---",
        "",
        "## 12 Arquétipos CADIAL · DNA Completo",
        "",
        "| Sym | Arquétipo | Opcode | Hz | Regra | VEEB | Rung | Ato | Essência |",
        "|-----|-----------|--------|----|-------|------|------|-----|----------|",
    ]
    for nome, a in DNA["arquetipos"].items():
        n = dist.get(nome, 0)
        lines.append(
            f"| {a['sym']} | **{nome}** | `{a['opcode']}` | {a['hz']}Hz "
            f"| `{a['regra']}` | VEEB-{a['veeb']} | D{a['rung']} "
            f"| {a.get('codice_ato','?')} | _{a['essencia']}_ |"
        )

    lines += [
        "",
        "---",
        "",
        "## Módulos Python Ativos",
        "",
        "| Módulo | Fase | Arquétipo | Descrição |",
        "|--------|------|-----------|-----------|",
    ]
    for mod, info in DNA["modulos_python"].items():
        lines.append(f"| `{mod}` | {info['fase']:02d} | {info['arch']} | {info['desc']} |")

    if catalog:
        lines += [
            "",
            "---",
            "",
            f"## Catálogo · {len(catalog)} arquivos catalogados",
            "",
            "| Arquétipo | Arquivos |",
            "|-----------|----------|",
        ]
        for arch, count in dist.most_common():
            a = DNA["arquetipos"].get(arch, {})
            sym = a.get("sym", "○")
            lines.append(f"| {sym} **{arch}** | {count} |")

    lines += [
        "",
        "---",
        "",
        "## Linguagem Universal · Classes Gramaticais",
        "",
        "| Classe | Elemento | Função | Arquétipos |",
        "|--------|----------|--------|------------|",
    ]
    for cls, v in DNA["linguagem"].items():
        arqs = ", ".join(v["arquetipo"])
        lines.append(f"| **{cls}** | {v['elemento']} | {v['funcao']} | {arqs} |")

    lines += [
        "",
        "---",
        "",
        f"**VERDADE × INTEGRAR ÷ Δ = ∞** · 3×6×9×7 = 1134  ",
        f"*JESUS = VERBO = GRAVIDADE · ∆7 · {ts}*",
        "",
        "> \"Vida ama Vida. O Pulso me guia. O Valor nasce do Equilíbrio.\"  ",
        "> — KOBLLUX · Forma Viva",
        "",
    ]

    content = "\n".join(lines)
    if not dry_run:
        atlas = base / "ATLAS.md"
        atlas.write_text(content, encoding="utf-8")
        print(f"  ✓ ATLAS.md gerado · {len(lines)} linhas")
    return content


# ═══════════════════════════════════════════════════════════════════════════════
# INBOX WATCHER — auto-classificação de novos arquivos
# ═══════════════════════════════════════════════════════════════════════════════

def watch_inbox(base: Path, interval: int = 30):
    """Monitora inbox/ e auto-classifica novos arquivos via Roda Viva."""
    inbox  = base / "inbox"
    inbox.mkdir(exist_ok=True)
    seen   = set()
    print(f"\n  [DNA·WATCH] Monitorando {inbox} · intervalo {interval}s")
    print(f"  Ctrl+C para parar.\n")

    if _HAS_FIRMWARE:
        mem = KoblluxMemory(base / "_index" / "memory.jsonl")

    while True:
        try:
            for f in sorted(inbox.rglob("*")):
                if not f.is_file() or str(f) in seen:
                    continue
                seen.add(str(f))
                info = classify_by_dna(f)
                print(f"  ∞ [{info['arch']:8s}] {f.name} · {info['opcode']} · {info['hz']}Hz · {info['ato']}")

                if _HAS_FIRMWARE:
                    try:
                        content = f.read_text(encoding="utf-8", errors="ignore")[:800]
                    except Exception:
                        content = f.name
                    mem.write(
                        arch=info["arch"].lower(),
                        content=content,
                        tags=info["tags"],
                        source=f"inbox/{f.name}",
                        record_type="DNA_INBOX",
                        extra={"opcode":info["opcode"],"hz":info["hz"],"ato":info["ato"]},
                    )
        except KeyboardInterrupt:
            print("\n  [DNA·WATCH] Encerrado · ∆7")
            break
        time.sleep(interval)


# ═══════════════════════════════════════════════════════════════════════════════
# DRIVE SYNC
# ═══════════════════════════════════════════════════════════════════════════════

def sync_drive(dry_run: bool = False):
    """Sincroniza com Google Drive via rclone."""
    cmd = ["rclone","copy", str(ROOT), "gdrive:KOBΦ-NODE/JESUS_VERB-", "--progress"]
    if dry_run:
        cmd.insert(2, "--dry-run")
    print(f"  [DNA·DRIVE] {' '.join(cmd)}")
    result = subprocess.run(cmd, capture_output=False)
    return result.returncode == 0


# ═══════════════════════════════════════════════════════════════════════════════
# UPDATE CODEX — injeta DNA no kobllux_codex_data.json
# ═══════════════════════════════════════════════════════════════════════════════

def update_codex(base: Path, dry_run: bool = False):
    """Injeta seção 'dna_engine' no kobllux_codex_data.json (APPEND ONLY)."""
    codex_path = base / "kobllux_codex_data.json"
    if not codex_path.exists():
        print("  [DNA·CODEX] kobllux_codex_data.json não encontrado")
        return

    codex = json.loads(codex_path.read_text(encoding="utf-8"))

    # Injeta DNA como nova seção — não modifica seções existentes
    codex["dna_engine"] = {
        "versao":     DNA["versao"],
        "assinatura": DNA["assinatura"],
        "lei":        DNA["lei"],
        "fractal":    DNA["fractal"],
        "centro":     DNA["centro"],
        "formula":    DNA["formula"]["base"],
        "acronimo":   DNA["acronimo"],
        "ciclos":     {str(k): v for k, v in DNA["ciclos"].items()},
        "componentes": DNA["componentes"],
        "codice_vivo": DNA["codice_vivo"],
        "dimensoes":  DNA["dimensoes"],
        "linguagem":  DNA["linguagem"],
        "modulos":    DNA["modulos_python"],
        "ts":         datetime.now(timezone.utc).isoformat(),
        "seal":       "∆7",
    }

    # Atualiza meta versão
    codex["meta"]["versao"]          = DNA["versao"]
    codex["meta"]["dna_engine"]      = True
    codex["meta"]["ultima_atualizacao"] = datetime.now(timezone.utc).isoformat()

    if not dry_run:
        codex_path.write_text(json.dumps(codex, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  ✓ kobllux_codex_data.json atualizado · seção 'dna_engine' injetada")
    else:
        print(f"  [DRY] kobllux_codex_data.json seria atualizado")


# ═══════════════════════════════════════════════════════════════════════════════
# SELAR · 3→6→9→7 · Fecha o loop de auto-modificação
# ═══════════════════════════════════════════════════════════════════════════════

def selar(base: Path, dry_run: bool = False) -> dict:
    """
    Fecha o loop: scan → detectar novos módulos → expandir DNA → selar.

    3 DETECTAR  — Varre o repositório
    6 INTEGRAR  — Descobre .py não registrados no DNA["modulos_python"]
    9 EXPANDIR  — Classifica e expande DNA em memória
    7 SELAR     — Escreve dna_delta.json + memory.jsonl + ATLAS.md

    Na próxima execução, o bloco de delta-load absorve o resultado
    e o DNA engine já nasce com o conhecimento selado.
    """
    ts = datetime.now(timezone.utc).isoformat()

    # ── 3 DETECTAR ───────────────────────────────────────────────────────────
    print("  [SELAR·3] DETECTAR — varrendo repositório...")
    scan_result = scan_and_catalog(base, dry_run=dry_run)

    catalog: list[dict] = []
    cat_path = base / "catalogo_media.json"
    if cat_path.exists():
        try:
            catalog = json.loads(cat_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    # ── 6 INTEGRAR ───────────────────────────────────────────────────────────
    print("  [SELAR·6] INTEGRAR — detectando módulos novos...")
    registered = set(DNA["modulos_python"].keys())
    novos: dict[str, dict] = {}

    for entry in catalog:
        if entry.get("ext") != ".py":
            continue
        nome = entry["name"]
        if nome in registered:
            continue
        path = base / entry["path"]
        info = classify_by_dna(path)
        novos[nome] = {
            "fase":   info["rung"],
            "arch":   info["arch"],
            "desc":   f"{info['essencia']} · ∆selar",
            "opcode": info["opcode"],
            "hz":     info["hz"],
        }

    print(f"  [SELAR·6] {len(novos)} módulos novos integrados ao DNA")

    # ── 9 EXPANDIR ───────────────────────────────────────────────────────────
    print("  [SELAR·9] EXPANDIR — expandindo DNA em memória...")
    DNA["modulos_python"].update(novos)

    catalog_hash = hashlib.sha256(
        json.dumps(catalog, ensure_ascii=False, sort_keys=True).encode()
    ).hexdigest()[:16]

    seal_record = {
        "ts":             ts,
        "versao":         DNA["versao"],
        "total_arquivos": scan_result["total"],
        "distribuicao":   scan_result["dist"],
        "novos_modulos":  len(novos),
        "novos_lista":    list(novos.keys()),
        "hash":           catalog_hash,
        "seal":           "∆7",
        "lei":            DNA["lei"],
        "centro":         DNA["centro"],
    }

    # ── 7 SELAR ──────────────────────────────────────────────────────────────
    print("  [SELAR·7] SELAR — selando DNA + memória + ATLAS...")

    if not dry_run:
        # Escreve delta — carregado automaticamente no próximo boot
        delta_path = base / "_index" / "dna_delta.json"
        delta_path.parent.mkdir(exist_ok=True)
        delta_path.write_text(
            json.dumps({
                "ts":               ts,
                "seal_ts":          ts,
                "hash":             catalog_hash,
                "modulos_python":   novos,
                "total_registrados": len(DNA["modulos_python"]),
                "seal":             "∆7",
                "centro":           DNA["centro"],
            }, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        print(f"  ✓ _index/dna_delta.json · {len(novos)} módulos selados")

        # Grava na memory.jsonl
        if _HAS_FIRMWARE:
            mem = KoblluxMemory(base / "_index" / "memory.jsonl")
            mem.write(
                arch="aion",
                content=(
                    f"SELAR ∆7 · {len(novos)} módulos integrados · "
                    f"{scan_result['total']} arquivos · hash:{catalog_hash}"
                ),
                tags=["selar", "aion", "loop-fechado", "∆7", "dna-engine"],
                source="kobllux_dna_engine.py --selar",
                record_type="SELAR_CICLO",
                extra=seal_record,
            )
        else:
            mem_path = base / "_index" / "memory.jsonl"
            mem_path.parent.mkdir(exist_ok=True)
            with mem_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps({
                    "ts":      ts,
                    "arch":    "aion",
                    "type":    "SELAR_CICLO",
                    "content": f"SELAR ∆7 · {len(novos)} módulos · hash:{catalog_hash}",
                    "tags":    ["selar", "aion", "∆7"],
                    "seal":    "∆7",
                    **{k: v for k, v in seal_record.items() if k not in ("ts",)},
                }, ensure_ascii=False) + "\n")
        print(f"  ✓ memory.jsonl · AION selou o ciclo")

        # Regenera ATLAS com DNA expandido
        generate_atlas(base, dry_run=False)
        print(f"  ✓ ATLAS.md regenerado com DNA expandido")

    else:
        print(f"  [DRY] dna_delta.json seria escrito · {len(novos)} módulos")
        print(f"  [DRY] memory.jsonl seria selado")
        print(f"  [DRY] ATLAS.md seria regenerado")

    print(f"\n  ∆7 LOOP FECHADO · {DNA['centro']} · hash:{catalog_hash}\n")
    return seal_record


# ═══════════════════════════════════════════════════════════════════════════════
# SUMMARY
# ═══════════════════════════════════════════════════════════════════════════════

def summary(base: Path):
    """Mostra estado atual do DNA vivo."""
    cat_path = base / "catalogo_media.json"
    catalog  = []
    if cat_path.exists():
        try:
            catalog = json.loads(cat_path.read_text(encoding="utf-8"))
        except Exception:
            pass

    mem_path = base / "_index" / "memory.jsonl"
    mem_count = 0
    if mem_path.exists():
        mem_count = sum(1 for l in mem_path.read_text(encoding="utf-8", errors="ignore").splitlines() if l.strip())

    dist = Counter(e["arch"] for e in catalog)

    print(f"\n{'═'*60}")
    print(f"  KOBLLUX DNA ENGINE · {DNA['versao']} · ∆7")
    print(f"  {DNA['lei']}")
    print(f"{'═'*60}")
    print(f"  Catálogo  : {len(catalog)} arquivos")
    print(f"  Memória   : {mem_count} registros")
    print(f"  ATLAS.md  : {'✓' if (base/'ATLAS.md').exists() else '✗'}")
    print(f"  READMEs   : {sum(1 for _ in base.rglob('README.md'))} arquivos")
    print(f"\n  Distribuição por arquétipo:")
    for arch, n in dist.most_common(8):
        a = DNA["arquetipos"].get(arch, {})
        sym = a.get("sym","○")
        bar = "█" * min(n // 5 + 1, 20)
        print(f"    {sym} {arch:10s} {bar} {n}")
    print(f"\n  {DNA['fractal']} · {DNA['centro']}\n")


# ═══════════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════════

def main():
    p = argparse.ArgumentParser(description="KOBLLUX DNA ENGINE · Backend Vivo · ∆7")
    p.add_argument("--scan",         action="store_true", help="Varre repo e gera catalogo_media.json")
    p.add_argument("--atlas",        action="store_true", help="Gera/atualiza ATLAS.md")
    p.add_argument("--watch",        action="store_true", help="Monitora inbox/ (auto-classifica)")
    p.add_argument("--drive-sync",   action="store_true", help="Sincroniza com Google Drive (rclone)")
    p.add_argument("--dna",          action="store_true", help="Exporta DNA canônico como JSON")
    p.add_argument("--update-codex", action="store_true", help="Injeta DNA no kobllux_codex_data.json")
    p.add_argument("--summary",      action="store_true", help="Mostra estado do DNA vivo")
    p.add_argument("--selar",        action="store_true", help="3→6→9→7 · Fecha loop de auto-modificação")
    p.add_argument("--all",          action="store_true", help="Executa: scan + atlas + update-codex")
    p.add_argument("--dry-run",      action="store_true")
    p.add_argument("--interval",     type=int, default=30, help="Intervalo watch em segundos")
    args = p.parse_args()

    print(f"\n{'╔'+'═'*58+'╗'}")
    print(f"║  KOBLLUX DNA ENGINE · {DNA['assinatura']}  ║")
    print(f"║  {DNA['lei']:52s}  ║")
    print(f"{'╚'+'═'*58+'╝'}\n")

    if args.dna:
        print(json.dumps(DNA, ensure_ascii=False, indent=2))
        return

    if args.summary:
        summary(ROOT)
        return

    ran = False
    if args.scan or args.all:
        print("  [1/3] SCAN · classificando arquivos...")
        result = scan_and_catalog(ROOT, dry_run=args.dry_run)
        print(f"  Total: {result['total']} · top: {list(result['dist'].items())[:4]}")
        ran = True

    if args.atlas or args.all:
        print("  [2/3] ATLAS · gerando mapa vivo...")
        generate_atlas(ROOT, dry_run=args.dry_run)
        ran = True

    if args.update_codex or args.all:
        print("  [3/3] CODEX · injetando DNA...")
        update_codex(ROOT, dry_run=args.dry_run)
        ran = True

    if args.selar:
        print("  [0/4] SELAR · 3→6→9→7 · fechando loop de auto-modificação...")
        result = selar(ROOT, dry_run=args.dry_run)
        print(f"  SELAR concluído · {result['novos_modulos']} módulos · hash:{result['hash']}")
        ran = True

    if args.drive_sync:
        print("  DRIVE · sincronizando...")
        sync_drive(dry_run=args.dry_run)
        ran = True

    if args.watch:
        watch_inbox(ROOT, interval=args.interval)
        ran = True

    if not ran:
        summary(ROOT)
        print("  Uso: python3 kobllux_dna_engine.py --all")
        print("       python3 kobllux_dna_engine.py --watch")
        print("       python3 kobllux_dna_engine.py --drive-sync\n")

    if ran and not args.dry_run and not args.watch:
        if _HAS_FIRMWARE:
            mem = KoblluxMemory(ROOT / "_index" / "memory.jsonl")
            mem.write(
                arch="kobllux",
                content=f"DNA ENGINE executado · scan+atlas+codex · {DNA['versao']}",
                tags=["dna-engine","atlas","catalogo","∆7"],
                source="kobllux_dna_engine.py",
                record_type="DNA_ENGINE_RUN",
            )
        print(f"\n  ∆7 SELADO · {DNA['centro']}\n")


if __name__ == "__main__":
    main()
