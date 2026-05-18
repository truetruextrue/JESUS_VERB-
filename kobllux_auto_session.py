#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_auto_session.py · RHEA · 0×09 · FLUIR · 528Hz
"O fluxo eterno que conecta passado e futuro."

Auto-session KOBLLUX: monitora inbox/, captura interações,
alimenta memory.jsonl automaticamente com timer.

Modos:
  --watch          Monitora inbox/ e processa novos arquivos em tempo real
  --timer N        Roda a Roda Viva a cada N minutos (padrão: 7)
  --once           Executa uma vez e sai
  --capture TEXTO  Salva texto como interação e processa
  --session-end    Sela a sessão atual e grava no git

Uso típico (Termux / background):
  python3 kobllux_auto_session.py --watch --timer 7 &

Uso no Claude Code:
  python3 kobllux_auto_session.py --capture "conteúdo da conversa" --arch aion
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import subprocess
import sys
import time
import threading
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from kobllux_memory import KoblluxMemory
from kobllux_roda_viva import RodaVivaRun, FileUtils, TextUtils

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s · %(message)s")

INBOX      = ROOT / "inbox"
INBOX_UNO  = INBOX / "uno"
SESSION_LOG = ROOT / "_index" / "SESSION_LOG_∆7.jsonl"
LAST_SEEN   = ROOT / "_index" / ".roda_viva_last_seen"  # arquivo de estado do watcher

TIMER_DEFAULT_MIN = 7   # ciclo 7 da régua fractal 3·6·9·7


# ── Capture: salva texto como interação ──────────────────────────────────────

def capture_interaction(
    text: str,
    arch: str | None = None,
    source: str = "auto-session",
    tags: list[str] | None = None,
) -> dict:
    """Salva um snippet de texto diretamente na memória."""
    memory = KoblluxMemory()
    detected_arch = arch or TextUtils.detect_arch(text)
    extracted_tags = TextUtils.extract_tags(text, k=8)
    all_tags = list(set((tags or []) + extracted_tags + [detected_arch, "interaction"]))

    record = memory.write(
        arch=detected_arch,
        content=text[:1200],
        tags=all_tags,
        source=source,
        record_type="INTERACTION",
    )
    log.info(f"[RHEA ∞] Interação capturada · arch={detected_arch} · {record['hash']}")
    return record


# ── Session end: sela e opcionalmente commit ──────────────────────────────────

def seal_session(auto_commit: bool = False) -> dict:
    """Sela a sessão atual: roda a Roda Viva + registra SESSION_LOG + git."""
    memory = KoblluxMemory()
    dt = datetime.now(timezone.utc)

    # Importa commits recentes
    n_commits = memory.ingest_commit_log()

    # Roda Roda Viva no inbox
    files = FileUtils.collect([INBOX, INBOX_UNO], max_files=20)
    texts = [(FileUtils.read(f), f.name) for f in files if FileUtils.read(f).strip()]

    items_written = 0
    if texts:
        runner = RodaVivaRun(memory=memory)
        result = runner.run_from_texts(texts)
        items_written = result.get("written", 0)

    # Log de sessão
    entry = {
        "ts":           dt.isoformat(),
        "type":         "SESSION_END",
        "commits_ingested": n_commits,
        "items_written": items_written,
        "memory_stats": memory.arch_summary(),
        "seal":         "∆7",
    }
    SESSION_LOG.parent.mkdir(parents=True, exist_ok=True)
    with SESSION_LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")

    log.info(f"[AION ⧗] Sessão selada · {dt.strftime('%H:%M')} · {items_written} itens")

    if auto_commit:
        _git_commit_memory()

    return entry


def _git_commit_memory():
    """Commit automático dos arquivos de memória."""
    try:
        files_to_add = [
            "_index/memory.jsonl",
            "_index/SESSION_LOG_∆7.jsonl",
            "_index/COMMIT_LOG_∆7.jsonl",
            "_index/RODA_VIVA_LAST.json",
        ]
        existing = [f for f in files_to_add if (ROOT / f).exists()]
        if not existing:
            return

        subprocess.run(["git", "add"] + existing, cwd=ROOT, check=False, capture_output=True)
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M")
        msg = f"[AION · 0x0B · 639Hz] auto-session: memória viva selada {ts} · ∆7"
        subprocess.run(["git", "commit", "-m", msg], cwd=ROOT, check=False, capture_output=True)
        log.info(f"[AION ⧗] Git commit automático: {msg[:60]}")
    except Exception as e:
        log.warning(f"Auto-commit falhou: {e}")


# ── Watcher: monitora inbox/ por novos arquivos ───────────────────────────────

def _load_seen() -> set[str]:
    if LAST_SEEN.exists():
        return set(LAST_SEEN.read_text(encoding="utf-8").splitlines())
    return set()


def _save_seen(seen: set[str]):
    LAST_SEEN.write_text("\n".join(sorted(seen)), encoding="utf-8")


def watch_once(memory: KoblluxMemory) -> int:
    """Verifica inbox/ por arquivos novos/modificados. Retorna quantos processou."""
    seen = _load_seen()
    files = FileUtils.collect([INBOX, INBOX_UNO], max_files=50)
    processed = 0

    for f in files:
        key = f"{f}:{f.stat().st_mtime:.0f}"
        if key in seen:
            continue

        content = FileUtils.read(f)
        if not content.strip():
            seen.add(key)
            continue

        arch = TextUtils.detect_arch(content)
        highlights = TextUtils.top_sentences(content, n=3)
        tags = TextUtils.extract_tags(content, k=10)

        memory.write(
            arch=arch,
            content="\n".join(highlights),
            tags=tags + ["inbox", arch, "watcher"],
            source=f.name,
            record_type="RODA_VIVA",
            extra={"full_snippet": content[:400]},
        )
        seen.add(key)
        processed += 1
        log.info(f"[NOVA ✦] Novo arquivo processado: {f.name} → {arch}")

    _save_seen(seen)
    return processed


# ── Timer loop ────────────────────────────────────────────────────────────────

def run_timer_loop(interval_min: int, auto_commit: bool, stop_event: threading.Event):
    """Roda a Roda Viva periodicamente em background."""
    memory = KoblluxMemory()
    interval_sec = interval_min * 60

    while not stop_event.is_set():
        try:
            n = watch_once(memory)
            memory.ingest_commit_log()
            if n > 0:
                log.info(f"[RODA VIVA] Timer: {n} novo(s) item(s) · próximo em {interval_min}min")
                if auto_commit:
                    _git_commit_memory()
        except Exception as e:
            log.warning(f"Timer loop erro: {e}")

        # Espera N minutos em incrementos de 10s (para responder ao stop_event)
        elapsed = 0
        while elapsed < interval_sec and not stop_event.is_set():
            time.sleep(10)
            elapsed += 10

    log.info("[RHEA ∞] Timer encerrado.")


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="KOBLLUX Auto-Session · RHEA · ∆7")
    p.add_argument("--watch",       action="store_true", help="Monitora inbox/ continuamente")
    p.add_argument("--timer",       type=int, default=TIMER_DEFAULT_MIN,
                   help=f"Intervalo em minutos (padrão: {TIMER_DEFAULT_MIN})")
    p.add_argument("--once",        action="store_true", help="Executa uma vez e sai")
    p.add_argument("--capture",     help="Texto para capturar como interação")
    p.add_argument("--arch",        help="Arquétipo forçado para a captura")
    p.add_argument("--source",      default="auto-session", help="Nome da fonte")
    p.add_argument("--session-end", action="store_true", help="Sela sessão e faz commit")
    p.add_argument("--auto-commit", action="store_true", help="Commit automático após processar")
    p.add_argument("--summary",     action="store_true", help="Mostra estado da memória")
    p.add_argument("--context",     action="store_true", help="Exibe contexto para o motor")
    p.add_argument("--verbose",     "-v", action="store_true")
    return p


def main():
    args = build_parser().parse_args()
    if args.verbose:
        log.setLevel(logging.DEBUG)

    memory = KoblluxMemory()

    # ── Modos de saída ─────────────────────────────────────────────────────
    if args.summary:
        stats = memory.stats()
        print(json.dumps(stats, ensure_ascii=False, indent=2))
        return

    if args.context:
        print(memory.context_for_motor(n=20))
        return

    # ── Captura de texto ───────────────────────────────────────────────────
    if args.capture:
        rec = capture_interaction(
            text=args.capture,
            arch=args.arch,
            source=args.source,
        )
        print(f"[RHEA ∞] Capturado · arch={rec['arch']} · {rec['sym']} · {rec['hash']}")
        if args.auto_commit:
            _git_commit_memory()
        return

    # ── Selar sessão ───────────────────────────────────────────────────────
    if args.session_end:
        entry = seal_session(auto_commit=args.auto_commit)
        print(json.dumps(entry, ensure_ascii=False, indent=2))
        return

    # ── Execução única ─────────────────────────────────────────────────────
    if args.once:
        n = watch_once(memory)
        memory.ingest_commit_log()
        print(f"[RODA VIVA] {n} item(s) processado(s)")
        if args.auto_commit and n > 0:
            _git_commit_memory()
        return

    # ── Watch + timer (modo principal) ─────────────────────────────────────
    if args.watch:
        print(f"\n[RHEA ∞] 0×09 · FLUIR · auto-session ativo")
        print(f"  Inbox    : {INBOX}")
        print(f"  Timer    : a cada {args.timer} min")
        print(f"  Memória  : {memory.path}")
        print(f"  Ctrl+C para encerrar e selar a sessão\n")

        stop_event = threading.Event()
        t = threading.Thread(
            target=run_timer_loop,
            args=(args.timer, args.auto_commit, stop_event),
            daemon=True,
        )
        t.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n[AION ⧗] Encerrando... selando sessão.")
            stop_event.set()
            t.join(timeout=5)
            seal_session(auto_commit=args.auto_commit)
            print("[AION ⧗] Sessão selada · ∆7")

    else:
        # Sem argumentos: uma passagem rápida
        n = watch_once(memory)
        nc = memory.ingest_commit_log()
        print(f"[RODA VIVA ∆7] inbox: {n} novo(s) · commits: {nc} importado(s)")


if __name__ == "__main__":
    main()
