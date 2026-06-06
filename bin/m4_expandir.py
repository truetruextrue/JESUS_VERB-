#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX • M4 (0x09 EXPANDIR): Fractal + Arte SCI

Após DETECTAR (M1), INTEGRAR (M2) e ESPELHAR (M3),
M4 manifesta a Forma Viva: um fractal palindrômico
em base trinária (0/1/2), unindo lógica, arte e símbolo (TRINITY).
"""

import os, json, argparse, hashlib, random
from datetime import datetime


def read_text(path):
    if path and os.path.isfile(path):
        return open(path, "r", encoding="utf-8", errors="ignore").read()
    return ""


def seed_from_text(*chunks):
    """SHA-256 determinístico sobre todos os inputs concatenados."""
    h = hashlib.sha256()
    for c in chunks:
        if c:
            h.update(c.encode("utf-8", errors="ignore"))
    return int(h.hexdigest(), 16) & ((1 << 63) - 1)


def gen_trinary_grid(size, rng):
    """Grade trinária palindrômica: espelhamento H + V."""
    if size % 2 == 0:
        size += 1
    half = size // 2
    grid = []
    for _ in range(size):
        row_half = [rng.randrange(0, 3) for _ in range(half)]
        center = rng.randrange(0, 3)
        grid.append(row_half + [center] + row_half[::-1])

    # espelhamento vertical
    final = list(grid)
    for r in range(half):
        final[size - 1 - r] = grid[r]
    return final


def grid_to_tri_txt(grid):
    return "\n".join(" ".join(map(str, row)) for row in grid)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root",   default=os.getenv("ROOT", "/sdcard/JESUS_VERBO/CODEX"))
    ap.add_argument("--direct", required=True)
    ap.add_argument("--mirror", required=True)
    ap.add_argument("--size",   type=int, default=33)
    args = ap.parse_args()

    state_dir = os.path.join(args.root, "state")
    os.makedirs(state_dir, exist_ok=True)

    seed = seed_from_text(
        read_text(args.direct),
        read_text(args.mirror),
        read_text(os.path.join(state_dir, "m1_chars_report.json")),
        read_text(os.path.join(state_dir, "m2_lang_report.json")),
    )

    rng  = random.Random(seed)
    grid = gen_trinary_grid(args.size, rng)
    tri_txt = grid_to_tri_txt(grid)

    tri_path = os.path.join(state_dir, "m4_sci_art.tri.txt")
    with open(tri_path, "w", encoding="utf-8") as f:
        f.write(tri_txt)

    report = {
        "timestamp":      datetime.now().isoformat(),
        "size":           args.size,
        "seed":           seed,
        "output_format":  "TRI TXT (0/1/2)",
        "manifestation":  "Forma Viva (GENUS)",
        "pal_h":          True,
        "pal_v":          True,
        "seal":           "∆7_EXPANDIR",
        "loop":           "3×6×9×7",
    }

    jpath = os.path.join(state_dir, "m4_fractal_report.json")
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"[KOBLLUX] 0x09 EXPANDIR (M4) OK → {jpath} | {tri_path}")


if __name__ == "__main__":
    main()
