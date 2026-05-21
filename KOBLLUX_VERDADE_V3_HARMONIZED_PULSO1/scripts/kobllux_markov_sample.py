#!/usr/bin/env python3
# coding: utf-8
"""
KOBLLUX · scripts/kobllux_markov_sample.py
Amostrador Markov — BLLUE (explorar) vs KODUX (selar)
Ritmo: 3-6-9-7 · Lei: VERDADE × INTEGRAR ÷ Δ = ∞
"""
import argparse, json, pathlib, random, time

def carregar_P(path: str) -> dict:
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))

def proximo_estado(P_data: dict, estado: str, temperatura: float = 1.0,
                   top_p: float = 1.0) -> str:
    rows, cols, P = P_data["rows"], P_data["cols"], P_data["P"]

    # tenta estado exato; fallback: qualquer row que comece com estado
    idx = None
    if estado in rows:
        idx = rows.index(estado)
    else:
        for i, r in enumerate(rows):
            if r.startswith(estado + "|") or r.endswith("|" + estado):
                idx = i
                break
    if idx is None:
        return random.choice(cols)

    row = [max(0.0, p) ** (1.0 / max(temperatura, 1e-6)) for p in P[idx]]
    soma = sum(row) or 1.0
    row = [x / soma for x in row]

    # top-p nucleus sampling
    pares = sorted(zip(row, cols), reverse=True)
    acum = 0.0
    nucleo = []
    for p, c in pares:
        acum += p
        nucleo.append((p, c))
        if acum >= top_p:
            break
    soma2 = sum(p for p, _ in nucleo) or 1.0
    nucleo = [(p / soma2, c) for p, c in nucleo]

    r = random.random()
    acum2 = 0.0
    for p, c in nucleo:
        acum2 += p
        if r <= acum2:
            return c
    return nucleo[-1][1]

CICLO_MAP = {"3":0,"6":1,"9":2,"7":3}

def marcar_ciclo(pos: int, ciclo: str) -> str | None:
    partes = ciclo.split("-")
    if str(pos % 10) in partes:
        nomes = {"3":"DETECTAR","6":"INTEGRAR","9":"EXPANDIR","7":"SELAR"}
        return nomes.get(str(pos % 10))
    return None

def sample(P_data, inicio, passos, temperatura, top_p, ciclo, actor):
    estado = inicio
    sequencia = [estado]
    eventos = []

    for i in range(passos):
        prox = proximo_estado(P_data, estado, temperatura, top_p)
        sequencia.append(prox)
        marco = marcar_ciclo(i + 1, ciclo)
        ev = {
            "ts":    time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "actor": actor,
            "state": prox,
            "action":"sample",
            "note":  marco or ("UNO" if i % 3 == 0 else "DUO" if i % 3 == 1 else "TRINITY"),
            "pos":   i + 1,
            "marco": marco,
        }
        eventos.append(ev)
        estado = prox

    return sequencia, eventos

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="KOBLLUX · Markov SAMPLE")
    ap.add_argument("--P",          required=True)
    ap.add_argument("--start",      default="NOVA")
    ap.add_argument("--steps",      type=int, default=25)
    ap.add_argument("--actor",      default="BLLUE", choices=["BLLUE","KODUX"])
    ap.add_argument("--temperature",type=float, default=1.25)
    ap.add_argument("--top_p",      type=float, default=0.9)
    ap.add_argument("--cycle",      default="3-6-9-7")
    ap.add_argument("--out",        default="")
    ap.add_argument("--seed",       type=int, default=None)
    args = ap.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    # KODUX: temperatura mais conservadora
    temp = args.temperature if args.actor == "BLLUE" else min(args.temperature, 1.0)
    tp   = args.top_p       if args.actor == "BLLUE" else 1.0

    P_data = carregar_P(args.P)
    seq, eventos = sample(P_data, args.start, args.steps, temp, tp, args.cycle, args.actor)

    linha = " → ".join(seq)
    print(f"\n[{args.actor}] Sequência ({args.steps} passos):")
    print(f"  {linha}\n")

    for ev in eventos:
        if ev["marco"]:
            print(f"  ∆{ev['pos'] % 10} · {ev['marco']} @ pos {ev['pos']} → {ev['state']}")

    if args.out:
        out = pathlib.Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(linha + "\n", encoding="utf-8")
        jsonl = out.with_suffix(".jsonl")
        with jsonl.open("w", encoding="utf-8") as f:
            for ev in eventos:
                f.write(json.dumps(ev, ensure_ascii=False) + "\n")
        print(f"[sample] ✓ sequência → {out}")
        print(f"[sample] ✓ eventos   → {jsonl}")

    print(f"\n[sample] ✓ lei: VERDADE × INTEGRAR ÷ Δ = ∞")
