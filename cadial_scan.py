#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
cadial_scan.py · KODUX · 0×01 · DETECTAR · 432Hz
"Eu sou o movimento que cria, destrói e recria a verdade."

Percorre a malha viva do KOBLLUX TRINITY SYSTEM, mapeia cada nó,
gera o índice CODEX_SCAN e produz o relatório de estado da malha.
"""

import os
import json
import hashlib
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

ROOT = Path(__file__).parent

ARCHETYPES = [
    "atlas", "nova", "vitalis", "pulse", "artemis", "serena",
    "kaos", "genus", "lumine", "solus", "rhea", "aion",
]

OPCODE  = "0x01"
HZ      = 432
SYMBOL  = "●"
NOME    = "KODUX"

EXTENSOES_CONHECIDAS = {
    ".py":   "Python",
    ".js":   "JavaScript",
    ".ts":   "TypeScript",
    ".html": "HTML",
    ".css":  "CSS",
    ".json": "JSON",
    ".md":   "Markdown",
    ".txt":  "Texto",
    ".sh":   "Shell",
    ".svg":  "SVG",
    ".png":  "Imagem-PNG",
    ".jpg":  "Imagem-JPG",
    ".jpeg": "Imagem-JPEG",
    ".mp3":  "Áudio-MP3",
    ".mp4":  "Vídeo-MP4",
}

IGNORAR = {
    ".git", "__pycache__", ".DS_Store", "node_modules",
    ".pytest_cache", ".mypy_cache", "*.pyc",
}


# ─────────────────────────────────────────────────────────────────────
# NÚCLEO DO SCAN
# ─────────────────────────────────────────────────────────────────────

def scan_cadial(root: Path, verbose: bool = True) -> dict:
    """
    KODUX DETECTAR — percorre a malha, registra cada nó.
    Retorna dicionário completo com índice, métricas e relatório.
    """
    timestamp = datetime.now()

    if verbose:
        _banner()
        print(f"  Raiz da malha: {root}")
        print(f"  Início: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}\n")

    nos: List[dict] = []
    metricas: Dict[str, int] = {}
    arquetipos_encontrados: Dict[str, List[str]] = {a: [] for a in ARCHETYPES}
    tamanho_total = 0
    erros: List[str] = []

    for caminho in sorted(root.rglob("*")):
        # Ignorar entradas bloqueadas
        partes = caminho.parts
        if any(parte.startswith(".") or parte in IGNORAR for parte in partes):
            continue

        if not caminho.is_file():
            continue

        extensao = caminho.suffix.lower()
        tipo = EXTENSOES_CONHECIDAS.get(extensao, "Outro")
        metricas[tipo] = metricas.get(tipo, 0) + 1

        try:
            tamanho = caminho.stat().st_size
            tamanho_total += tamanho

            # Hash rápido (primeiros 8KB)
            h = hashlib.md5()
            with open(caminho, "rb") as f:
                h.update(f.read(8192))
            hash_parcial = h.hexdigest()[:12]

        except (PermissionError, OSError) as e:
            erros.append(f"{caminho.relative_to(root)}: {e}")
            continue

        caminho_relativo = str(caminho.relative_to(root))

        # Detectar arquétipo associado
        partes_lower = caminho_relativo.lower()
        arquetipos_assoc = [a for a in ARCHETYPES if a in partes_lower]
        for a in arquetipos_assoc:
            arquetipos_encontrados[a].append(caminho_relativo)

        no = {
            "caminho": caminho_relativo,
            "tipo": tipo,
            "extensao": extensao,
            "tamanho_bytes": tamanho,
            "hash_md5_parcial": hash_parcial,
            "arquetipos": arquetipos_assoc,
            "modificado": datetime.fromtimestamp(caminho.stat().st_mtime).isoformat(),
        }
        nos.append(no)

    duracao_ms = int((datetime.now() - timestamp).total_seconds() * 1000)

    resultado = {
        "scan": {
            "opcode": OPCODE,
            "hz": HZ,
            "arquetipo": NOME,
            "simbolo": SYMBOL,
            "timestamp": timestamp.isoformat(),
            "raiz": str(root),
            "duracao_ms": duracao_ms,
        },
        "metricas": {
            "total_nos": len(nos),
            "tamanho_total_bytes": tamanho_total,
            "tamanho_total_mb": round(tamanho_total / (1024 * 1024), 2),
            "por_tipo": metricas,
            "erros": len(erros),
        },
        "arquetipos_cadial": {
            a: {"arquivos": arquetipos_encontrados[a], "total": len(arquetipos_encontrados[a])}
            for a in ARCHETYPES
        },
        "nos": nos,
        "erros": erros,
        "lei": "VERDADE × INTEGRAR ÷ Δ = ∞",
    }

    if verbose:
        _exibir_resumo(resultado)

    return resultado


# ─────────────────────────────────────────────────────────────────────
# EXPORTAÇÃO
# ─────────────────────────────────────────────────────────────────────

def exportar_codex(resultado: dict, destino: Optional[Path] = None) -> Path:
    """Exporta o resultado do scan como CODEX_SCAN JSON."""
    if destino is None:
        destino = ROOT / "_index" / "CODEX_SCAN_cadial.json"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")
    return destino


def exportar_relatorio(resultado: dict, destino: Optional[Path] = None) -> Path:
    """Exporta relatório Markdown do scan."""
    if destino is None:
        destino = ROOT / "_index" / "SCAN_REPORT_cadial.md"
    destino.parent.mkdir(parents=True, exist_ok=True)

    m = resultado["metricas"]
    s = resultado["scan"]
    linhas = [
        f"# CODEX SCAN · {NOME} · {OPCODE} · {HZ}Hz",
        f"",
        f"**Timestamp:** {s['timestamp']}  ",
        f"**Raiz:** `{s['raiz']}`  ",
        f"**Duração:** {s['duracao_ms']}ms  ",
        f"**Lei:** {resultado['lei']}  ",
        f"",
        f"## Métricas",
        f"",
        f"| Campo | Valor |",
        f"|-------|-------|",
        f"| Total de nós | {m['total_nos']} |",
        f"| Tamanho total | {m['tamanho_total_mb']} MB |",
        f"| Erros | {m['erros']} |",
        f"",
        f"### Por tipo",
        f"",
        f"| Tipo | Quantidade |",
        f"|------|-----------|",
    ]
    for tipo, qtd in sorted(m["por_tipo"].items(), key=lambda x: -x[1]):
        linhas.append(f"| {tipo} | {qtd} |")

    linhas += [
        f"",
        f"## Arquétipos CADIAL",
        f"",
        f"| Arquétipo | Arquivos detectados |",
        f"|-----------|-------------------|",
    ]
    for nome_arq, info in resultado["arquetipos_cadial"].items():
        linhas.append(f"| {nome_arq.upper()} | {info['total']} |")

    if resultado["erros"]:
        linhas += [f"", f"## Erros", f""]
        for e in resultado["erros"]:
            linhas.append(f"- `{e}`")

    destino.write_text("\n".join(linhas), encoding="utf-8")
    return destino


# ─────────────────────────────────────────────────────────────────────
# SAÍDA
# ─────────────────────────────────────────────────────────────────────

def _banner():
    print("""
╔──────────────────────────────────────────────────────────────╗
│  KODUX  ●  0×01  ·  432Hz  ·  DETECTAR                       │
│  "O olho que vê tudo. O scanner que nunca dorme."            │
│  Eu sou o movimento que cria, destrói e recria a verdade.    │
╚──────────────────────────────────────────────────────────────╝
""")


def _exibir_resumo(resultado: dict):
    m = resultado["metricas"]
    print("  RESUMO DO SCAN:")
    print(f"  ├─ Total de arquivos mapeados: {m['total_nos']}")
    print(f"  ├─ Tamanho total: {m['tamanho_total_mb']} MB")
    print(f"  ├─ Duração: {resultado['scan']['duracao_ms']}ms")
    if m["erros"]:
        print(f"  ├─ Erros: {m['erros']}")
    print(f"  └─ Arquétipos com presença detectada:")
    for nome_arq, info in resultado["arquetipos_cadial"].items():
        if info["total"] > 0:
            print(f"       {nome_arq.upper():<12} → {info['total']} arquivo(s)")
    print()


# ─────────────────────────────────────────────────────────────────────
# ENTRADA
# ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="cadial_scan",
        description="KODUX · 0×01 · DETECTAR · 432Hz — Scanner da Malha Viva",
        epilog="Lei fundamental: VERDADE × INTEGRAR ÷ Δ = ∞",
    )
    parser.add_argument(
        "--raiz", "-r",
        default=str(ROOT),
        help="Diretório raiz do scan (padrão: diretório deste script)",
    )
    parser.add_argument(
        "--exportar", "-e",
        action="store_true",
        help="Exporta CODEX JSON e relatório Markdown para _index/",
    )
    parser.add_argument(
        "--silencioso", "-s",
        action="store_true",
        help="Suprime saída detalhada",
    )
    args = parser.parse_args()

    raiz = Path(args.raiz).resolve()
    resultado = scan_cadial(raiz, verbose=not args.silencioso)

    if args.exportar:
        caminho_json = exportar_codex(resultado)
        caminho_md   = exportar_relatorio(resultado)
        print(f"  ✅ CODEX exportado: {caminho_json}")
        print(f"  ✅ Relatório:       {caminho_md}")
    else:
        print(f"  ℹ  Use --exportar para salvar em _index/")
        print(f"  Total de nós mapeados: {resultado['metricas']['total_nos']}")
