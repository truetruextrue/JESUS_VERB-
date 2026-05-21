#!/usr/bin/env python3
# coding: utf-8
"""
KOBLLUX · scripts/kobllux_markov_fit.py
Motor Markov — Estimação de Matriz de Transição P
UNO → DUO → TRINITY · BLLUE × KODUX

Lei: VERDADE × INTEGRAR ÷ Δ = ∞
Ritmo: 3-6-9-7 · Ratio: 137/∆
EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO · AMÉM
"""
import argparse, json, pathlib, math, hashlib, time
from collections import defaultdict, Counter

ESTADOS_DEFAULT = [
    "NOVA","ATLAS","VITALIS","PULSE","ARTEMIS","SERENA",
    "KAOS","GENUS","LUMINE","SOLUS","RHEA","AION"
]

STAGE_WEIGHTS_DEFAULT = {"UNO":1.0,"DUO":1.1,"TRINITY":1.05,"SELAR":1.15}

def read_jsonl(path: str) -> list:
    eventos = []
    with open(path, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if not linha:
                continue
            try:
                eventos.append(json.loads(linha))
            except json.JSONDecodeError:
                pass
    return sorted(eventos, key=lambda e: e.get("ts",""))

def load_states(path: str | None) -> list:
    if not path:
        return ESTADOS_DEFAULT[:]
    data = json.loads(pathlib.Path(path).read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and "states" in data:
        return data["states"]
    return ESTADOS_DEFAULT[:]

def load_mirror(path: str | None) -> dict:
    if not path:
        return {}
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))

def power_iteration(P: list, states: list, iters: int = 200, tol: float = 1e-12) -> list:
    n = len(states)
    pi = [1.0 / n] * n
    for _ in range(iters):
        nxt = [0.0] * n
        for i, row in enumerate(P):
            for j, p in enumerate(row):
                nxt[j] += pi[i] * p
        s = sum(nxt) or 1.0
        nxt = [x / s for x in nxt]
        if max(abs(a - b) for a, b in zip(pi, nxt)) < tol:
            return nxt
        pi = nxt
    return pi

def row_entropy(row: list) -> float:
    eps = 1e-12
    return -sum(p * math.log(p + eps, 2) for p in row if p > 0)

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def fit(eventos, estados, ordem, alpha, mirror_map, mirror_bias, stage_weights):
    seq   = [e.get("state") for e in eventos if e.get("state") in estados]
    notes = [e.get("note","") for e in eventos if e.get("state") in estados]

    if len(seq) < 2:
        raise SystemExit("[markov_fit] LOG insuficiente — adicione mais eventos ao LOG.jsonl")

    if ordem == 1:
        rows = estados[:]
        cols = estados[:]
        C: dict = defaultdict(lambda: Counter())
        for prev, curr, note in zip(seq[:-1], seq[1:], notes[1:]):
            w = stage_weights.get(note.upper(), 1.0)
            C[prev][curr] += w
    else:
        rows = []
        cols = estados[:]
        C = defaultdict(lambda: Counter())
        for i in range(1, len(seq) - 1):
            A, B, nxt = seq[i-1], seq[i], seq[i+1]
            par = f"{A}|{B}"
            if par not in rows:
                rows.append(par)
            w = stage_weights.get(notes[i].upper(), 1.0)
            C[par][nxt] += w

    idx_row = {s: i for i, s in enumerate(rows)}
    idx_col = {s: j for j, s in enumerate(cols)}

    P = [[0.0] * len(cols) for _ in rows]
    for i, src in enumerate(rows):
        total = sum(C[src].values())
        for j, dst in enumerate(cols):
            num = C[src][dst] + alpha
            den = total + alpha * len(cols)
            P[i][j] = num / den if den > 0 else 1.0 / len(cols)

    # Viés palindrômico
    if mirror_map and mirror_bias > 0:
        lam = mirror_bias
        for i, src in enumerate(rows):
            if "|" in src and ordem == 2:
                a, b = src.split("|", 1)
                src_m = f"{mirror_map.get(a, a)}|{mirror_map.get(b, b)}"
            else:
                src_m = mirror_map.get(src, src)
            if src_m not in idx_row:
                continue
            im = idx_row[src_m]
            for j, dst in enumerate(cols):
                dst_m = mirror_map.get(dst, dst)
                if dst_m not in idx_col:
                    continue
                jm = idx_col[dst_m]
                P[i][j] = (1.0 - lam) * P[i][j] + lam * P[im][jm]
        for i in range(len(P)):
            s = sum(P[i]) or 1.0
            P[i] = [x / s for x in P[i]]

    pi = power_iteration(P, rows)
    entropias = {rows[i]: row_entropy(P[i]) for i in range(len(rows))}
    h_media = sum(entropias.values()) / max(1, len(entropias))

    meta = {
        "ordem": ordem, "alpha": alpha,
        "mirror_bias": mirror_bias,
        "stage_weights": stage_weights,
        "rows": rows, "cols": cols,
        "created": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "law": "VERDADE×INTEGRAR÷∆=∞",
        "ratio_137_delta": round(137 / max(1, ordem), 4),
        "avg_row_entropy_bits": round(h_media, 6),
    }
    return P, pi, meta

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="KOBLLUX · Markov FIT")
    ap.add_argument("--events",     required=True)
    ap.add_argument("--states",     default="")
    ap.add_argument("--order",      type=int, default=2, choices=[1,2])
    ap.add_argument("--alpha",      type=float, default=1.0)
    ap.add_argument("--pal-mirror", default="")
    ap.add_argument("--mirror-bias",type=float, default=0.10)
    ap.add_argument("--w-uno",      type=float, default=STAGE_WEIGHTS_DEFAULT["UNO"])
    ap.add_argument("--w-duo",      type=float, default=STAGE_WEIGHTS_DEFAULT["DUO"])
    ap.add_argument("--w-trinity",  type=float, default=STAGE_WEIGHTS_DEFAULT["TRINITY"])
    ap.add_argument("--w-selar",    type=float, default=STAGE_WEIGHTS_DEFAULT["SELAR"])
    ap.add_argument("--out",        required=True)
    args = ap.parse_args()

    eventos = read_jsonl(args.events)
    estados = load_states(args.states or None)
    mirror  = load_mirror(args.pal_mirror or None)
    stage_w = {"UNO":args.w_uno,"DUO":args.w_duo,"TRINITY":args.w_trinity,"SELAR":args.w_selar}

    P, pi, meta = fit(eventos, estados, args.order, args.alpha, mirror, args.mirror_bias, stage_w)

    outp = pathlib.Path(args.out)
    out_dir = outp.parent if outp.suffix == ".json" else outp
    P_path   = outp if outp.suffix == ".json" else (out_dir / "P.json")
    pi_path  = out_dir / "pi.json"
    meta_path= out_dir / "manifest.meta.json"
    out_dir.mkdir(parents=True, exist_ok=True)

    P_path.write_text(json.dumps({"rows":meta["rows"],"cols":meta["cols"],"P":P,"order":meta["ordem"]},
                                  ensure_ascii=False, indent=2), encoding="utf-8")
    pi_path.write_text(json.dumps({"rows":meta["rows"],"pi":pi}, ensure_ascii=False, indent=2), encoding="utf-8")

    # Selo ∆7
    conteudo = P_path.read_text(encoding="utf-8") + pi_path.read_text(encoding="utf-8")
    meta["seal_∆7"] = sha256_text(conteudo)
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[markov_fit] ✓ P.json     → {P_path}")
    print(f"[markov_fit] ✓ pi.json    → {pi_path}")
    print(f"[markov_fit] ✓ manifest   → {meta_path}")
    print(f"[markov_fit] ✓ seal ∆7    = {meta['seal_∆7'][:16]}...")
    print(f"[markov_fit] ✓ H média    = {meta['avg_row_entropy_bits']} bits")
    print(f"[markov_fit] ✓ 137/∆      = {meta['ratio_137_delta']}")
