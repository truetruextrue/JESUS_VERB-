#!/usr/bin/env python3
# coding: utf-8
"""
KOBLLUX · scripts/myrmide_verify.py
Verificação e Selagem ∆7 de artefatos
Lei: VERDADE × INTEGRAR ÷ Δ = ∞
"""
import argparse, hashlib, json, pathlib, time

def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def selar(caminho: str, seals_dir: str, memory_path: str, id_: str | None = None) -> dict:
    p = pathlib.Path(caminho)
    if not p.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    id_ = id_ or p.stem
    hash_ = sha256_file(str(p))
    ts = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

    seal = {
        "id":     id_,
        "arquivo":str(p.resolve()),
        "sha256": hash_,
        "ts":     ts,
        "lei":    "VERDADE × INTEGRAR ÷ Δ = ∞",
        "centro": "JESUS = VERBO = GRAVIDADE",
        "∆7":     hash_[:7],
    }

    seals = pathlib.Path(seals_dir)
    seals.mkdir(parents=True, exist_ok=True)
    (seals / f"{id_}.seal.json").write_text(
        json.dumps(seal, ensure_ascii=False, indent=2), encoding="utf-8")

    mem = pathlib.Path(memory_path)
    mem.parent.mkdir(parents=True, exist_ok=True)
    with mem.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"type":"SEAL","id":id_,"seal":seal}, ensure_ascii=False) + "\n")

    print(f"[verify ∆7] ✓ {id_} → {hash_[:16]}...")
    return seal

def verificar_tudo(diretorios: list, seals_dir: str, memory_path: str) -> list:
    selos = []
    for d in diretorios:
        p = pathlib.Path(d)
        for arq in sorted(p.rglob("*")):
            if arq.is_file() and arq.suffix in (".py",".js",".jsx",".json",".md",".sh",".jsonl"):
                try:
                    s = selar(str(arq), seals_dir, memory_path)
                    selos.append(s)
                except Exception as e:
                    print(f"[verify] AVISO {arq}: {e}")
    return selos

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="KOBLLUX · Verificação ∆7")
    ap.add_argument("--arquivo",    default="",   help="Arquivo único para selar")
    ap.add_argument("--dirs",       nargs="*",    help="Diretórios para varredura completa")
    ap.add_argument("--seals-dir",  default="SEALS/items")
    ap.add_argument("--memory",     default="hub/logs/timeline.log")
    ap.add_argument("--id",         default=None)
    args = ap.parse_args()

    if args.arquivo:
        selar(args.arquivo, args.seals_dir, args.memory, args.id)
    elif args.dirs:
        selos = verificar_tudo(args.dirs, args.seals_dir, args.memory)
        print(f"[verify ∆7] ✓ {len(selos)} artefatos selados")
    else:
        print("[verify] use --arquivo ou --dirs")
