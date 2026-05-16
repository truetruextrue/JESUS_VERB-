#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
reindex_vault.py · KODUX · 0×01 · DETECTAR · 432Hz
Fecha o GAP de 18.337 arquivos não indexados no vault CODEX.

Estado atual (2026-05-13):
  Indexados: 1.687  (index_codex.json · 2025-09-25)
  Vault:    20.024 arquivos
  GAP:      18.337 não indexados

Uso:
    python3 reindex_vault.py --status
    python3 reindex_vault.py --gap
    python3 reindex_vault.py --full
    python3 reindex_vault.py --buckets
"""

import os
import sys
import json
import hashlib
import argparse
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional

# ─────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO
# ─────────────────────────────────────────────────────────────────────

VAULT_PATHS = [
    Path("/storage/emulated/0/KOBΦ-NODE/JESUS_VERBO/JESUS_VERBO/CODEX"),
    Path("/sdcard/JESUS_VERBO/CODEX"),
    Path("/sdcard/KOBΦ-NODE/JESUS_VERBO/JESUS_VERBO/CODEX"),
    Path.home() / "CODEX",
]

INDEX_PATHS = [
    Path("/storage/emulated/0/KOBΦ-NODE/JESUS_VERBO/JESUS_VERBO/CODEX/_index"),
    Path("/sdcard/JESUS_VERBO/CODEX/_index"),
    Path.home() / "KOB--NODE" / "CODEX" / "_index",
]

ARQUETIPOS = [
    "ATLAS", "NOVA", "VITALIS", "PULSE", "ARTEMIS", "SERENA",
    "KAOS", "GENUS", "LUMINE", "SOLUS", "RHEA", "AION",
]

IGNORAR = {".git", "__pycache__", ".DS_Store", "node_modules",
           ".obsidian", "graphify-out"}

EXTENSOES_CONTENTES = {
    ".md", ".txt", ".py", ".js", ".ts", ".json", ".sh",
    ".html", ".css", ".yaml", ".yml", ".toml",
}


# ─────────────────────────────────────────────────────────────────────
# LOCALIZAÇÃO DO VAULT
# ─────────────────────────────────────────────────────────────────────

def encontrar_vault() -> Optional[Path]:
    for p in VAULT_PATHS:
        if p.exists():
            return p
    return None


def encontrar_index() -> Optional[Path]:
    for p in INDEX_PATHS:
        if p.exists():
            return p
    return None


# ─────────────────────────────────────────────────────────────────────
# STATUS DO VAULT
# ─────────────────────────────────────────────────────────────────────

def status_vault(vault: Path, index: Path) -> Dict:
    """Calcula o estado atual do vault e GAP de indexação."""

    # Contar arquivos no vault
    total = 0
    por_tipo: Dict[str, int] = {}
    for f in vault.rglob("*"):
        if f.is_file():
            parte = f.parts
            if any(p in IGNORAR for p in parte):
                continue
            total += 1
            ext = f.suffix.lower()
            por_tipo[ext] = por_tipo.get(ext, 0) + 1

    # Ler index existente
    index_json = index / "index_codex.json"
    indexados = 0
    index_data = {}
    if index_json.exists():
        try:
            index_data = json.loads(index_json.read_text(encoding="utf-8"))
            indexados = index_data.get("count", len(index_data.get("items", [])))
        except Exception:
            pass

    # Memória
    mem_summary = index / "memory_summary.json"
    mem_data = {}
    if mem_summary.exists():
        try:
            mem_data = json.loads(mem_summary.read_text(encoding="utf-8"))
        except Exception:
            pass

    gap = max(0, total - indexados)

    return {
        "vault": str(vault),
        "index": str(index),
        "total_arquivos": total,
        "indexados": indexados,
        "gap": gap,
        "por_tipo": dict(sorted(por_tipo.items(), key=lambda x: -x[1])[:15]),
        "memory_scanned": mem_data.get("scanned", 0),
        "memory_extracted": mem_data.get("extracted", 0),
        "buckets_ativos": [k for k, v in mem_data.get("by_bucket", {}).items() if v.get("count", 0) > 0],
        "buckets_pendentes": [k for k, v in mem_data.get("by_bucket", {}).items() if v.get("count", 0) == 0],
        "timestamp": datetime.now().isoformat(),
    }


# ─────────────────────────────────────────────────────────────────────
# GERAÇÃO DO ÍNDICE
# ─────────────────────────────────────────────────────────────────────

def hash_arquivo(path: Path, bytes_max: int = 8192) -> str:
    h = hashlib.md5()
    try:
        with open(path, "rb") as f:
            h.update(f.read(bytes_max))
    except Exception:
        pass
    return h.hexdigest()[:16]


def detectar_arquetipos(caminho_rel: str) -> List[str]:
    lower = caminho_rel.lower()
    return [a for a in ARQUETIPOS if a.lower() in lower]


def gerar_index(vault: Path, index_out: Path,
                apenas_gap: bool = False,
                index_existente: Optional[Path] = None,
                verbose: bool = True) -> Dict:
    """
    Percorre o vault e gera/atualiza index_codex.json.
    Se apenas_gap=True, só processa arquivos sem entrada no índice existente.
    """
    existentes: Dict[str, Dict] = {}
    if apenas_gap and index_existente and index_existente.exists():
        try:
            data = json.loads(index_existente.read_text(encoding="utf-8"))
            items = data.get("items", data if isinstance(data, list) else [])
            for item in items:
                p = item.get("path") or item.get("rel") or item.get("name", "")
                if p:
                    existentes[p] = item
            if verbose:
                print(f"  Índice existente: {len(existentes)} entradas carregadas")
        except Exception as e:
            if verbose:
                print(f"  ⚠  Erro ao ler índice existente: {e}")

    nos: List[Dict] = list(existentes.values()) if apenas_gap else []
    novos = 0
    erros = 0

    for f in sorted(vault.rglob("*")):
        if not f.is_file():
            continue
        partes = f.parts
        if any(p in IGNORAR for p in partes):
            continue

        rel = str(f.relative_to(vault))

        if apenas_gap and rel in existentes:
            continue

        try:
            stat = f.stat()
            no: Dict = {
                "path": rel,
                "ext": f.suffix.lower(),
                "size": stat.st_size,
                "mtime": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "hash": hash_arquivo(f),
                "arquetipos": detectar_arquetipos(rel),
            }
            if f.suffix.lower() in EXTENSOES_CONTENTES:
                try:
                    trecho = f.read_text(encoding="utf-8", errors="ignore")[:200]
                    no["trecho"] = trecho.strip()
                except Exception:
                    pass

            nos.append(no)
            novos += 1

            if verbose and novos % 1000 == 0:
                print(f"  → {novos} novos arquivos processados...")

        except Exception:
            erros += 1

    resultado = {
        "gerado_em": datetime.now().isoformat(),
        "vault": str(vault),
        "count": len(nos),
        "novos": novos,
        "erros": erros,
        "lei": "VERDADE × INTEGRAR ÷ Δ = ∞",
        "items": nos,
    }

    index_out.parent.mkdir(parents=True, exist_ok=True)
    saida = index_out / "index_codex_novo.json"
    saida.write_text(json.dumps(resultado, indent=2, ensure_ascii=False), encoding="utf-8")

    if verbose:
        print(f"  ✅ Índice gerado: {saida}")
        print(f"     Total: {len(nos)} | Novos: {novos} | Erros: {erros}")

    return resultado


# ─────────────────────────────────────────────────────────────────────
# REINDEX POR BUCKETS
# ─────────────────────────────────────────────────────────────────────

def reindex_buckets(vault: Path, index: Path, verbose: bool = True) -> Dict:
    """
    Percorre o vault e distribui arquivos nos 12 buckets CADIAL.
    Gera memory_summary_novo.json com distribuição atualizada.
    """
    buckets: Dict[str, Dict] = {a: {"count": 0, "arquivos": [], "keywords": set()}
                                  for a in ARQUETIPOS}
    sem_bucket = []

    for f in sorted(vault.rglob("*")):
        if not f.is_file():
            continue
        partes = f.parts
        if any(p in IGNORAR for p in partes):
            continue

        rel = str(f.relative_to(vault))
        arqs = detectar_arquetipos(rel)

        if arqs:
            for a in arqs:
                buckets[a]["count"] += 1
                buckets[a]["arquivos"].append(rel)
        else:
            sem_bucket.append(rel)

    # Resumo
    resumo: Dict = {
        "gerado_em": datetime.now().isoformat(),
        "vault": str(vault),
        "sem_bucket": len(sem_bucket),
        "by_bucket": {},
    }

    for nome, dados in buckets.items():
        resumo["by_bucket"][nome] = {
            "count": dados["count"],
            "status": "ATIVO" if dados["count"] > 0 else "VAZIO",
            "sample": dados["arquivos"][:5],
        }
        if verbose and dados["count"] > 0:
            print(f"  {nome:<10} → {dados['count']} arquivos")

    saida = index / "memory_summary_novo.json"
    index.mkdir(parents=True, exist_ok=True)
    saida.write_text(json.dumps(resumo, indent=2, ensure_ascii=False), encoding="utf-8")

    if verbose:
        print(f"\n  ✅ Buckets reindexados: {saida}")
        ativos = sum(1 for v in resumo["by_bucket"].values() if v["status"] == "ATIVO")
        print(f"     Buckets ativos: {ativos}/12 | Sem bucket: {len(sem_bucket)}")

    return resumo


# ─────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────

def cli():
    parser = argparse.ArgumentParser(
        prog="reindex_vault",
        description="KODUX · 0×01 · 432Hz — Reindexador do Vault CODEX",
        epilog="Lei: VERDADE × INTEGRAR ÷ Δ = ∞",
    )
    parser.add_argument("--vault", help="Caminho do vault (autodetectado se omitido)")
    parser.add_argument("--index", help="Caminho do _index (autodetectado se omitido)")
    parser.add_argument("--status", action="store_true",
                        help="Mostrar estado atual (GAP, indexados, buckets)")
    parser.add_argument("--gap", action="store_true",
                        help="Indexar apenas arquivos novos (fechar o GAP)")
    parser.add_argument("--full", action="store_true",
                        help="Reindexar vault completo do zero")
    parser.add_argument("--buckets", action="store_true",
                        help="Redistribuir arquivos nos 12 buckets CADIAL")
    parser.add_argument("--silencioso", "-s", action="store_true")

    args = parser.parse_args()
    verbose = not args.silencioso

    # Localizar vault
    vault = Path(args.vault) if args.vault else encontrar_vault()
    if not vault or not vault.exists():
        print("⚠  Vault CODEX não encontrado.")
        print("   Caminhos verificados:")
        for p in VAULT_PATHS:
            print(f"   · {p}")
        print("\n   Use --vault /caminho/para/CODEX")
        sys.exit(1)

    index = Path(args.index) if args.index else encontrar_index()
    if not index:
        index = vault / "_index"
        index.mkdir(parents=True, exist_ok=True)

    if verbose:
        print(f"\n  KOBΦ-NODE · REINDEX VAULT · KODUX 0×01 · 432Hz")
        print(f"  Vault: {vault}")
        print(f"  Index: {index}\n")

    if args.status or not any([args.gap, args.full, args.buckets]):
        s = status_vault(vault, index)
        if verbose:
            print(f"  Total arquivos:    {s['total_arquivos']:>8}")
            print(f"  Indexados:         {s['indexados']:>8}")
            print(f"  GAP (não indexado):{s['gap']:>8}  ← PRIORIDADE")
            print(f"  Memória scanned:   {s['memory_scanned']:>8}")
            print(f"  Memória extracted: {s['memory_extracted']:>8}")
            print(f"  Buckets ativos:  {s['buckets_ativos'] or 'nenhum'}")
            print(f"  Buckets pendentes: {len(s['buckets_pendentes'])}/12")
            if s["gap"] > 0:
                print(f"\n  → Execute: python3 reindex_vault.py --gap")
        else:
            print(json.dumps(s, indent=2, ensure_ascii=False))
        return

    if args.gap:
        if verbose:
            print("  Fechando GAP — indexando arquivos novos...\n")
        gerar_index(vault, index, apenas_gap=True,
                    index_existente=index / "index_codex.json", verbose=verbose)

    if args.full:
        if verbose:
            print("  Reindexação COMPLETA do vault...\n")
        gerar_index(vault, index, apenas_gap=False, verbose=verbose)

    if args.buckets:
        if verbose:
            print("  Redistribuindo 12 buckets CADIAL...\n")
        reindex_buckets(vault, index, verbose=verbose)


if __name__ == "__main__":
    cli()
