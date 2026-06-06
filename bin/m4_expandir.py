#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""" KOBLLUX • M4 (0x09 EXPANDIR): Fractal + Arte SCI
    Gera padrões palindrômicos e arte SCI, manifestando a Plenitude (TRINITY). """
import os, sys, json, argparse, hashlib, random
from datetime import datetime

def read_text(path):
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""

def seed_from_text(*chunks):
    # Semente determinística para garantir que o pulso se mantém o mesmo
    h = hashlib.sha256()
    for c in chunks:
        if c: h.update(c.encode("utf-8", errors="ignore"))
    return int(h.hexdigest(), 16) & ((1 << 63) - 1)

def gen_trinary_grid(size, rng):
    # Simula a geração da Forma Viva (Fractal) palindrômica
    if size % 2 == 0:
        size += 1
    half = size // 2
    grid = [None] * size          # FIX: era [*size …] — TypeError no original
    for r in range(size):
        row_half = [rng.randrange(0, 3) for _ in range(half)]
        center   = rng.randrange(0, 3)
        # Espelha horizontalmente (Palíndromo H)
        row      = row_half + [center] + row_half[::-1]
        grid[r]  = row

    # Simetria vertical (Palíndromo V)
    final_grid = [None] * size    # FIX: era [*size …]
    v_half = size // 2
    for r in range(v_half + 1):
        # Linhas de cima copiam para baixo (espelho vertical)
        final_grid[r] = grid[r]
        if r < v_half:
            final_grid[size - 1 - r] = grid[r]

    return final_grid

def grid_to_tri_txt(grid):
    # Formato de leitura trinária (0/1/2)
    return "\n".join(" ".join(map(str, row)) for row in grid)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", required=True)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--size",   type=int, default=33)   # Tamanho ímpar
    ap.add_argument("--m3",     default="")              # M3 state (opcional, entra na seed)
    ap.add_argument("--base",   type=int, default=3)     # Base trinária (reservado)
    args = ap.parse_args()

    state_dir = os.path.join(args.root, "state")
    os.makedirs(state_dir, exist_ok=True)

    # Integra inputs M1/M2/M3 para semente determinística
    seed = seed_from_text(
        read_text(args.direct),
        read_text(args.mirror),
        read_text(os.path.join(state_dir, "m1_chars_report.json")),
        read_text(os.path.join(state_dir, "m2_lang_report.json")),
        read_text(args.m3) if args.m3 else "",
    )
    rng  = random.Random(seed)

    grid    = gen_trinary_grid(args.size, rng)
    tri_txt = grid_to_tri_txt(grid)

    tri_path = os.path.join(state_dir, "m4_sci_art.tri.txt")
    with open(tri_path, "w", encoding="utf-8") as f:
        f.write(tri_txt)

    report = {
        "timestamp":     datetime.now().isoformat(),
        "size":          args.size,
        "seed":          seed,
        "output_format": "TRI TXT (0/1/2)",
        "manifestation": "Forma Viva (GENUS)",
        "pal_h":         True,
        "pal_v":         True,
        "seal":          "∆7_EXPANDIR",
        "loop":          "3×6×9×7",
    }

    jpath = os.path.join(state_dir, "m4_fractal_report.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"[KOBLLUX] 0x09 EXPANDIR (M4) OK → {jpath} | {tri_path}")

if __name__ == "__main__":
    main()
