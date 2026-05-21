#!/usr/bin/env python3
# coding: utf-8
"""
KOBLLUX · scripts/sciart_tools.py
SCI-ART: Espelhos + Selos + Validação Palindrômica
Lei: VERDADE × INTEGRAR ÷ Δ = ∞
"""
import sys, json, hashlib, time, pathlib, argparse

def read_ascii(path: str) -> list[list[str]]:
    txt = pathlib.Path(path).read_text(encoding="utf-8").strip("\n")
    linhas = [list(l) for l in txt.splitlines()]
    if not linhas:
        return []
    w = max(len(r) for r in linhas)
    return [r + [" "] * (w - len(r)) for r in linhas]

def to_txt(grid: list) -> str:
    return "\n".join("".join(r) for r in grid)

def mirror_h(grid: list) -> list:
    return [list(reversed(r)) for r in grid]

def mirror_v(grid: list) -> list:
    return list(reversed(grid))

def rot180(grid: list) -> list:
    return mirror_v(mirror_h(grid))

def pal_h_ok(grid: list) -> bool:
    return all(r == list(reversed(r)) for r in grid)

def pal_v_ok(grid: list) -> bool:
    return grid == list(reversed(grid))

def ratio_rot180(grid: list) -> float:
    a = "".join("".join(r) for r in grid)
    b = "".join("".join(r) for r in rot180(grid))
    if not a:
        return 1.0
    return sum(1 for x, y in zip(a, b) if x == y) / len(a)

def sha256_txt(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def processar(ascii_path: str, out_dir: str, seals_dir: str, memory_path: str, id_: str) -> dict:
    out = pathlib.Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    grid = read_ascii(ascii_path)
    h_grid = mirror_h(grid)
    v_grid = mirror_v(grid)
    r_grid = rot180(grid)

    (out / "mirror_h.txt").write_text(to_txt(h_grid), encoding="utf-8")
    (out / "mirror_v.txt").write_text(to_txt(v_grid), encoding="utf-8")
    (out / "rot180.txt").write_text(to_txt(r_grid),   encoding="utf-8")

    report = {
        "id":            id_,
        "ts":            time.strftime("%Y-%m-%dT%H:%M:%S%z"),
        "pal_h":         pal_h_ok(grid),
        "pal_v":         pal_v_ok(grid),
        "rot_180_ratio": round(ratio_rot180(grid), 6),
        "sha256":        sha256_txt(to_txt(grid)),
        "lei":           "VERDADE × INTEGRAR ÷ Δ = ∞",
    }

    seals = pathlib.Path(seals_dir)
    seals.mkdir(parents=True, exist_ok=True)
    (seals / f"{id_}.seal.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    mem = pathlib.Path(memory_path)
    mem.parent.mkdir(parents=True, exist_ok=True)
    with mem.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"type":"SCI-ART","id":id_,"report":report}, ensure_ascii=False) + "\n")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return report

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="KOBLLUX · SCI-ART Tools")
    ap.add_argument("ascii_path")
    ap.add_argument("out_dir")
    ap.add_argument("seals_dir")
    ap.add_argument("memory_path")
    ap.add_argument("id_")
    args = ap.parse_args()
    processar(args.ascii_path, args.out_dir, args.seals_dir, args.memory_path, args.id_)
