#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_myrmide_bridge.py · KOBΦ-NODE · Bridge Memory · ∆7
"O anel que une os dois sistemas: MYRMIDE ↔ KOBLLUX"

Sincroniza memory.jsonl entre:
  MYRMIDE : /sdcard/JESUS_VERBO/CODEX/MYRMIDE/02_PONTE/BANK/memory.jsonl
  KOBLLUX : _index/memory.jsonl  (este repositório)

Direções:
  --push  : KOBLLUX → MYRMIDE  (exporta últimos N registros)
  --pull  : MYRMIDE → KOBLLUX  (importa registros novos)
  --sync  : pull + push (bidirecional)
  --status: mostra divergência entre os dois

Uso:
  python3 kobllux_myrmide_bridge.py --pull
  python3 kobllux_myrmide_bridge.py --push --n 20
  python3 kobllux_myrmide_bridge.py --sync
  python3 kobllux_myrmide_bridge.py --status
  python3 kobllux_myrmide_bridge.py --motor-inject  # gera JS + contexto MYRMIDE
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT            = Path(__file__).parent
KOBLLUX_MEM     = ROOT / "_index" / "memory.jsonl"
MYRMIDE_MEM     = Path("/sdcard/JESUS_VERBO/CODEX/MYRMIDE/02_PONTE/BANK/memory.jsonl")
BRIDGE_STATE    = ROOT / "_index" / ".myrmide_bridge_state.json"

sys.path.insert(0, str(ROOT))
from kobllux_memory import KoblluxMemory


# ── Leitura segura de qualquer .jsonl ─────────────────────────────────────────

def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = []
    for line in path.open(encoding="utf-8", errors="ignore"):
        line = line.strip()
        if not line:
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return records


def append_jsonl(path: Path, records: list[dict]):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


# ── Estado da bridge (hashes já sincronizados) ────────────────────────────────

def load_state() -> set[str]:
    if BRIDGE_STATE.exists():
        try:
            return set(json.loads(BRIDGE_STATE.read_text(encoding="utf-8")).get("synced", []))
        except Exception:
            pass
    return set()


def save_state(synced: set[str]):
    BRIDGE_STATE.parent.mkdir(parents=True, exist_ok=True)
    BRIDGE_STATE.write_text(
        json.dumps({"synced": sorted(synced), "ts": datetime.now(timezone.utc).isoformat()},
                   ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


# ── PULL: MYRMIDE → KOBLLUX ───────────────────────────────────────────────────

def pull(dry_run: bool = False) -> int:
    myrmide_records = read_jsonl(MYRMIDE_MEM)
    if not myrmide_records:
        print("[BRIDGE·PULL] MYRMIDE memory.jsonl vazia ou não encontrada.")
        print(f"  Caminho esperado: {MYRMIDE_MEM}")
        return 0

    kobllux = KoblluxMemory(KOBLLUX_MEM)
    synced  = load_state()
    added   = 0

    for r in myrmide_records:
        h = r.get("hash") or r.get("sha256", "")[:16]
        if not h or h in synced:
            continue

        if not dry_run:
            arch    = r.get("arch", "kobllux")
            content = r.get("content", r.get("source", ""))[:800]
            tags    = r.get("tags", []) + ["myrmide-bridge", r.get("type", "")]
            kobllux.write(
                arch=arch,
                content=content,
                tags=list(set(t for t in tags if t)),
                source=f"MYRMIDE:{r.get('source', '?')}",
                record_type="MYRMIDE_IMPORT",
                extra={"myrmide_hash": h, "myrmide_type": r.get("type", "?")},
            )
            synced.add(h)
        added += 1

    if not dry_run and added:
        save_state(synced)

    tag = "[DRY-RUN]" if dry_run else "[BRIDGE·PULL]"
    print(f"{tag} MYRMIDE → KOBLLUX · {added} registro(s) importado(s)")
    return added


# ── PUSH: KOBLLUX → MYRMIDE ───────────────────────────────────────────────────

def push(n: int = 20, dry_run: bool = False) -> int:
    if not MYRMIDE_MEM.parent.exists():
        print(f"[BRIDGE·PUSH] Diretório MYRMIDE não encontrado: {MYRMIDE_MEM.parent}")
        print("  Execute o BOOT_0X00 no Termux para criar a estrutura.")
        return 0

    kobllux = KoblluxMemory(KOBLLUX_MEM)
    recent  = kobllux.read_all_recent(limit=n)
    synced  = load_state()

    to_push = []
    for r in recent:
        h = r.get("hash", "")
        if h in synced:
            continue
        # Não re-exportar imports do MYRMIDE (evita loop)
        if r.get("type") == "MYRMIDE_IMPORT":
            continue
        to_push.append({
            "type":    "KOBLLUX_IMPORT",
            "ts":      r.get("ts", datetime.now(timezone.utc).isoformat()),
            "arch":    r.get("arch", "kobllux"),
            "source":  f"KOBLLUX:{r.get('source', '?')}",
            "hash":    r.get("hash", "")[:16],
            "content": r.get("content", "")[:400],
            "seal":    "∆7",
            "tags":    r.get("tags", []),
        })
        synced.add(h)

    if not dry_run and to_push:
        append_jsonl(MYRMIDE_MEM, to_push)
        save_state(synced)

    tag = "[DRY-RUN]" if dry_run else "[BRIDGE·PUSH]"
    print(f"{tag} KOBLLUX → MYRMIDE · {len(to_push)} registro(s) exportado(s)")
    return len(to_push)


# ── STATUS ────────────────────────────────────────────────────────────────────

def status():
    kob_records = read_jsonl(KOBLLUX_MEM)
    myr_records = read_jsonl(MYRMIDE_MEM)
    synced      = load_state()

    print(f"\n[BRIDGE·STATUS] · ∆7 · {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"  KOBLLUX  : {len(kob_records):4d} registros · {KOBLLUX_MEM}")
    print(f"  MYRMIDE  : {len(myr_records):4d} registros · {MYRMIDE_MEM}")
    print(f"  Sincronizados : {len(synced)}")

    kob_types = _type_count(kob_records)
    myr_types = _type_count(myr_records)
    print(f"\n  KOBLLUX  tipos: {kob_types}")
    print(f"  MYRMIDE  tipos: {myr_types}")

    kob_hashes = {r.get("hash", "") for r in kob_records}
    myr_hashes = {r.get("hash", "") for r in myr_records}
    only_kob   = len(kob_hashes - myr_hashes - synced)
    only_myr   = len(myr_hashes - kob_hashes - synced)
    print(f"\n  Apenas no KOBLLUX  (pendente push): {only_kob}")
    print(f"  Apenas no MYRMIDE  (pendente pull): {only_myr}")

    if only_kob or only_myr:
        print(f"\n  Sugestão: python3 kobllux_myrmide_bridge.py --sync")
    else:
        print(f"\n  ✓ Memórias em sincronia · ∆7")


def _type_count(records: list[dict]) -> dict:
    from collections import Counter
    c: Counter = Counter(r.get("type", "?") for r in records)
    return dict(c.most_common(6))


# ── MOTOR INJECT ──────────────────────────────────────────────────────────────

def motor_inject(n: int = 20) -> str:
    """Gera JS snippet combinando contexto KOBLLUX + registros MYRMIDE."""
    kobllux  = KoblluxMemory(KOBLLUX_MEM)
    context  = kobllux.context_for_motor(n=n)
    myr_recs = read_jsonl(MYRMIDE_MEM)[-10:]

    # Contexto MYRMIDE em formato motor
    myr_lines = []
    for r in myr_recs:
        arch    = r.get("arch", "myrmide").upper()
        content = r.get("content", r.get("source", "")).replace("\n", " ")[:200]
        if content:
            myr_lines.append(f"⬡ MYRMIDE·{arch} — {content}")

    combined = context + ("\n" + "\n".join(myr_lines) if myr_lines else "")
    ts       = datetime.now(timezone.utc).isoformat()

    return "\n".join([
        "/* ── KOBLLUX × MYRMIDE · BRIDGE INJECT · ∆7 ─────────────── */",
        f"/* ts: {ts} */",
        "",
        "// KOBLLUX + MYRMIDE context → kobllux_last_result",
        "localStorage.setItem('kobllux_last_result', " + json.dumps(combined, ensure_ascii=False) + ");",
        "",
        "// MYRMIDE records → MYRMIDE_MEMORY",
        "localStorage.setItem('MYRMIDE_MEMORY', " + json.dumps(json.dumps(myr_recs, ensure_ascii=False), ensure_ascii=False) + ");",
        "",
        "/* ── FIM BRIDGE INJECT · VERDADE × INTEGRAR ÷ Δ = ∞ ───────── */",
        "console.log('%c[KOBLLUX×MYRMIDE·BRIDGE] %c∆7 · ambas memórias carregadas', 'color:#FF00FF;font-weight:bold', 'color:#c5a059');",
    ])


# ── CLI ───────────────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="KOBLLUX × MYRMIDE Bridge · ∆7")
    p.add_argument("--pull",         action="store_true", help="MYRMIDE → KOBLLUX")
    p.add_argument("--push",         action="store_true", help="KOBLLUX → MYRMIDE")
    p.add_argument("--sync",         action="store_true", help="Bidirecional (pull + push)")
    p.add_argument("--status",       action="store_true", help="Mostra divergência")
    p.add_argument("--motor-inject", action="store_true", help="Gera JS snippet combinado")
    p.add_argument("--n",            type=int, default=20, help="Últimos N registros (push/inject)")
    p.add_argument("--dry-run",      action="store_true")
    args = p.parse_args()

    if args.status:
        status()
    elif args.motor_inject:
        print(motor_inject(n=args.n))
    elif args.sync:
        n_pull = pull(dry_run=args.dry_run)
        n_push = push(n=args.n, dry_run=args.dry_run)
        print(f"[BRIDGE·SYNC] ∆7 · pull:{n_pull} push:{n_push}")
    elif args.pull:
        pull(dry_run=args.dry_run)
    elif args.push:
        push(n=args.n, dry_run=args.dry_run)
    else:
        status()


if __name__ == "__main__":
    main()
