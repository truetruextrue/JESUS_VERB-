#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_roda_viva.py · INFODOSE · 0×03 · EXPANDIR · 639Hz
"O alquimista que transforma dado em memória viva."

Adaptação de INFODOSE_DUAL HORUS v2.1 para o ecossistema KOBLLUX.
Pipeline: DETECTAR → INTEGRAR → EXPANDIR → SELAR (3-6-9-7)

Fontes suportadas:
  - inbox/uno/        → notas rápidas (quicknote)
  - inbox/            → qualquer .md/.txt/.py/.json/.html
  - _index/           → logs e memórias existentes
  - stdin             → pipe de qualquer texto

Saídas:
  - _index/memory.jsonl         → memória viva unificada
  - _index/RODA_VIVA_LAST.json  → estado da última execução
  - output/RODA_VIVA_*.md       → relatório legível

Uso:
  python3 kobllux_roda_viva.py                  # processa inbox/
  python3 kobllux_roda_viva.py --source texto   # processa texto direto
  python3 kobllux_roda_viva.py --arch atlas     # força arquétipo
  python3 kobllux_roda_viva.py --dry-run        # não grava
  python3 kobllux_roda_viva.py --summary        # lê memória existente
  python3 kobllux_roda_viva.py --export-js      # exporta para localStorage
  echo "texto" | python3 kobllux_roda_viva.py --stdin
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

# ── Importa a API de memória ────────────────────────────────────────────────
ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))
from kobllux_memory import KoblluxMemory, ARCHETYPES_META

# ── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(level=logging.INFO, format="%(levelname)s · %(message)s")
log = logging.getLogger(__name__)

# ── Constantes ───────────────────────────────────────────────────────────────
LAW = "VERDADE×INTEGRAR÷Δ=∞"
SEAL = "∆7"
SAFE_EXTS = (".txt", ".md", ".py", ".json", ".html", ".js", ".css")

STOPWORDS_PT = {
    "a","o","as","os","um","uma","de","do","da","dos","das","no","na",
    "nos","nas","que","com","para","por","em","e","ou","mais","menos",
    "voce","isso","esta","estao","como","ja","tambem","sobre","entre",
    "foi","ser","sao","se","ao","aos","nao","ter","ele","ela","sua","seu",
    "esse","essa","este","aqui","ali","quando","cada","todo","toda",
}

KOBLLUX_HINTS = [
    "kobllux","verbo","fractal","infodose","termux","python","rede","tts",
    "delta","kodux","bllue","atlas","nova","vitalis","pulse","artemis",
    "serena","kaos","genus","lumine","solus","rhea","aion","opcode",
    "cadial","roda","viva","memoria","seal","∆7","trinity","uno","dual",
]

# Padrões de detecção de arquétipo por conteúdo
ARCH_CONTENT_PATTERNS = {
    "atlas":   r"estrutur|grid|manifest|config|README|schema|grade|organiz",
    "nova":    r"início|começ|faísca|criar|gerar|novo|spark|nova\b",
    "vitalis": r"vita|energia|orgânico|núcleo|core|vivo|pulsant",
    "pulse":   r"ritmo|batida|tts|voz|audio|emoção|pulse\b",
    "artemis": r"precisão|alvo|target|injetar|convergir|foco|artemis",
    "serena":  r"acolh|cuidado|suave|integrar|ui|serena\b|calma",
    "kaos":    r"ruptura|patch|fix|override|entropia|bug|kaos\b",
    "genus":   r"base|fundação|gerar|genus\b|geração|fundament",
    "lumine":  r"luz|visual|tema|efeito|clareza|lumine\b|iluminação",
    "solus":   r"singular|foco único|silêncio|só\b|isolamento|solus",
    "rhea":    r"fluxo|bridge|conectar|rota|rhea\b|ligação|fluir",
    "aion":    r"tempo|memória|log|história|estado|aion\b|ciclo|temporal",
    "kodux":   r"scan|detectar|varrer|índice|kodux\b|arquivo|rastrear",
    "bllue":   r"integrar|espelho|bllue\b|coupler|cadial|reflexo",
}


# ── Utilitários de texto ─────────────────────────────────────────────────────

class TextUtils:
    _SENT = re.compile(r"(?<=[.!?\n])\s+")
    _PUNCT = re.compile(r"[,;:\-–—]\s?")
    _HIT = re.compile(
        r"\b(kobllux|verbo|codex|fractal|tts|termux|python|infodose|roda|viva|opcode|seal|∆7)\b",
        re.I,
    )

    @staticmethod
    def sha256(text: str) -> str:
        return hashlib.sha256(text.encode()).hexdigest()[:16]

    @staticmethod
    def sentences(text: str) -> list[str]:
        raw = [s.strip() for s in TextUtils._SENT.split(text.strip()) if s.strip()]
        return list(dict.fromkeys(raw))

    @staticmethod
    def score(sentence: str, hints: list[str]) -> int:
        s = len(sentence)
        if TextUtils._PUNCT.search(sentence): s += 15
        if TextUtils._HIT.search(sentence):   s += 50
        sl = sentence.lower()
        for h in hints:
            try:
                if re.search(r"\b" + re.escape(h.lower()) + r"\b", sl):
                    s += 30
            except re.error:
                pass
        return s

    @staticmethod
    def top_sentences(text: str, n: int = 3) -> list[str]:
        sents = TextUtils.sentences(text)
        return sorted(sents, key=lambda s: TextUtils.score(s, KOBLLUX_HINTS), reverse=True)[:n]

    @staticmethod
    def extract_tags(text: str, k: int = 12) -> list[str]:
        words = re.findall(r"[A-Za-zÀ-ÿ0-9_∆]{3,}", text.lower())
        freq = Counter(w for w in words if w not in STOPWORDS_PT and not w.isdigit())
        top = [w for w, _ in freq.most_common(k + 10)]
        hinted = [h.lower() for h in KOBLLUX_HINTS if h.lower() in text.lower()]
        merged = list(dict.fromkeys(hinted + top))
        return merged[:k]

    @staticmethod
    def detect_arch(text: str) -> str:
        """Detecta arquétipo dominante pelo conteúdo do texto."""
        scores: Counter = Counter()
        tl = text.lower()
        for arch, pat in ARCH_CONTENT_PATTERNS.items():
            matches = len(re.findall(pat, tl, re.I))
            if matches:
                scores[arch] += matches
        if not scores:
            return "kobllux"
        return scores.most_common(1)[0][0]


# ── Leitura de arquivos ───────────────────────────────────────────────────────

class FileUtils:
    @staticmethod
    def read(path: Path) -> str:
        ext = path.suffix.lower()
        if ext not in SAFE_EXTS:
            return ""
        try:
            return path.read_text(encoding="utf-8", errors="ignore")
        except IOError as e:
            log.warning(f"Não pôde ler {path}: {e}")
            return ""

    @staticmethod
    def collect(directories: list[Path], max_files: int = 50) -> list[Path]:
        found: list[Path] = []
        for d in directories:
            if not d.is_dir():
                continue
            for f in sorted(d.rglob("*")):
                if f.is_file() and f.suffix.lower() in SAFE_EXTS:
                    found.append(f)
                    if len(found) >= max_files:
                        break
        return found


# ── Motor da Roda Viva ────────────────────────────────────────────────────────

class RodaVivaRun:
    """
    Uma execução da Roda Viva KOBLLUX.
    Pipeline: DETECTAR → INTEGRAR → EXPANDIR → SELAR
    """

    def __init__(
        self,
        memory: KoblluxMemory,
        forced_arch: str | None = None,
        dry_run: bool = False,
        per_file: int = 3,
        max_total: int = 30,
        k_tags: int = 12,
    ):
        self.memory     = memory
        self.forced_arch = forced_arch
        self.dry_run    = dry_run
        self.per_file   = per_file
        self.max_total  = max_total
        self.k_tags     = k_tags
        self.dt         = datetime.now(timezone.utc)
        self.stamp      = self.dt.strftime("%Y%m%d_%H%M")
        self.head       = f"RODA VIVA · {self.dt.strftime('%Y-%m-%d %H:%M')} · {LAW}"

    def run_from_texts(self, texts: list[tuple[str, str]]) -> dict:
        """
        texts: lista de (conteúdo, nome_fonte)
        Retorna resumo da execução.
        """
        log.info(f"[KODUX ●] 0×01 · DETECTAR · {len(texts)} fonte(s)")

        # INTEGRAR
        items, all_text_parts = [], []
        for content, source in texts:
            if len(items) >= self.max_total:
                break
            if not content.strip():
                continue
            all_text_parts.append(content[:4000])

            arch = self.forced_arch or TextUtils.detect_arch(content)
            highlights = TextUtils.top_sentences(content, n=self.per_file)
            if not highlights:
                continue

            items.append({
                "arch":       arch,
                "source":     source,
                "highlights": highlights,
                "content":    content[:800],
            })

        log.info(f"[BLLUE ―] 0×02 · INTEGRAR · {len(items)} item(s) extraído(s)")

        all_text = "\n".join(all_text_parts)
        tags = TextUtils.extract_tags(all_text, k=self.k_tags)

        # EXPANDIR — grava na memória
        written = 0
        if not self.dry_run:
            for item in items:
                rec = self.memory.write(
                    arch=item["arch"],
                    content="\n".join(item["highlights"]),
                    tags=tags + [item["arch"]],
                    source=item["source"],
                    record_type="RODA_VIVA",
                    extra={"full_snippet": item["content"][:400]},
                )
                written += 1
            log.info(f"[INFODOSE ▢] 0×03 · EXPANDIR · {written} registro(s) na memória")

        # SELAR
        combo = TextUtils.sha256(all_text + self.stamp)
        result = {
            "head":       self.head,
            "stamp":      self.stamp,
            "sources":    len(texts),
            "items":      len(items),
            "tags":       tags,
            "written":    written,
            "arch_dist":  Counter(i["arch"] for i in items),
            "seal":       SEAL,
            "hash":       combo,
        }

        if not self.dry_run:
            # Salva estado da última execução
            last_path = ROOT / "_index" / "RODA_VIVA_LAST.json"
            last_path.write_text(
                json.dumps({**result, "arch_dist": dict(result["arch_dist"])},
                           ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            # Sela na memória com tipo SEAL
            self.memory.write(
                arch="aion",
                content=f"Roda Viva executada · {len(items)} itens · tags: {', '.join(tags[:6])}",
                tags=tags[:6] + ["roda-viva", "seal"],
                source="kobllux_roda_viva.py",
                record_type="SEAL",
                extra={"combo_hash": combo, "items_sealed": len(items)},
            )
            # Gera relatório .md
            self._write_report(items, tags, result)

        log.info(f"[AION ⧗] 0×0B · SELAR · {combo[:8]}... · {SEAL}")
        return result

    def _write_report(self, items: list[dict], tags: list[str], result: dict) -> None:
        out_dir = ROOT / "output"
        out_dir.mkdir(exist_ok=True)
        lines = [
            f"# {self.head}", "",
            f"**{SEAL}** · `{result['hash'][:16]}`", "",
            f"Fontes: {result['sources']} · Itens: {result['items']} · Arquétipos: {len(result['arch_dist'])}",
            "", "## Registros", "",
        ]
        for item in items:
            meta = ARCHETYPES_META.get(item["arch"], {})
            sym  = meta.get("sym", "○")
            lines.append(f"### {sym} {item['arch'].upper()} · {meta.get('opcode','')} · {meta.get('hz','')}Hz")
            lines.append(f"_Fonte: {item['source']}_")
            lines.append("")
            for h in item["highlights"]:
                lines.append(f"- {h}")
            lines.append("")
        if tags:
            lines += ["## Tags", "", f"`{'` · `'.join(tags)}`", ""]
        lines += ["---", f"*VERDADE × INTEGRAR ÷ Δ = ∞ · {SEAL}*"]

        rpt = out_dir / f"RODA_VIVA_{self.stamp}.md"
        rpt.write_text("\n".join(lines), encoding="utf-8")
        log.info(f"Relatório: {rpt}")


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="KOBLLUX Roda Viva · INFODOSE · ∆7")
    p.add_argument("--source",    help="Texto direto para processar")
    p.add_argument("--stdin",     action="store_true", help="Lê texto do stdin (pipe)")
    p.add_argument("--arch",      help="Força um arquétipo (ex: atlas, kaos)")
    p.add_argument("--inbox",     default=str(ROOT / "inbox"), help="Pasta inbox")
    p.add_argument("--per-file",  type=int, default=3)
    p.add_argument("--max-total", type=int, default=30)
    p.add_argument("--k-tags",    type=int, default=12)
    p.add_argument("--dry-run",   action="store_true")
    p.add_argument("--summary",   action="store_true", help="Mostra resumo da memória atual")
    p.add_argument("--export-js", action="store_true", help="Exporta JSON para localStorage")
    p.add_argument("--ingest-commits", action="store_true", help="Importa COMMIT_LOG para memória")
    p.add_argument("--verbose",   "-v", action="store_true")
    return p


def main():
    args = build_parser().parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    memory = KoblluxMemory()

    # ── Modos especiais ────────────────────────────────────────────────────
    if args.summary:
        stats = memory.stats()
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        return

    if args.export_js:
        print(memory.export_for_localStorage(n=30))
        return

    if args.ingest_commits:
        n = memory.ingest_commit_log()
        print(f"[AION ⧗] {n} commits importados para memory.jsonl")
        return

    # ── Coleta fontes ──────────────────────────────────────────────────────
    texts: list[tuple[str, str]] = []

    if args.stdin:
        raw = sys.stdin.read()
        if raw.strip():
            texts.append((raw, "stdin"))

    elif args.source:
        texts.append((args.source, "cli:--source"))

    else:
        inbox = Path(args.inbox)
        src_dirs = [inbox, inbox / "uno"]
        files = FileUtils.collect(src_dirs, max_files=50)
        if not files:
            log.warning(f"Nenhum arquivo encontrado em {inbox}")
            log.info("Use --source 'texto' ou --stdin para processar texto direto.")
            return
        for f in files:
            content = FileUtils.read(f)
            if content.strip():
                texts.append((content, f.name))

    if not texts:
        log.warning("Nenhuma fonte com conteúdo encontrada.")
        return

    # ── Executa Roda Viva ──────────────────────────────────────────────────
    runner = RodaVivaRun(
        memory=memory,
        forced_arch=args.arch,
        dry_run=args.dry_run,
        per_file=args.per_file,
        max_total=args.max_total,
        k_tags=args.k_tags,
    )
    result = runner.run_from_texts(texts)

    print(f"\n[RODA VIVA ∆7] {result['stamp']}")
    print(f"  Fontes   : {result['sources']}")
    print(f"  Itens    : {result['items']}")
    print(f"  Gravados : {result['written']}")
    print(f"  Tags     : {', '.join(result['tags'][:8])}")
    print(f"  Seal     : {result['hash'][:12]}... · ∆7")
    if result.get("arch_dist"):
        print("  Arquétipos:", dict(result["arch_dist"]))
    print()


if __name__ == "__main__":
    main()
