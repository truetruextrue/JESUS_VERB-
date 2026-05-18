#!/usr/bin/env python3
# kobllux_arch_detect.py · KODUX · 0×01 · DETECTAR · 432Hz
# Motor de detecção de arquétipos por caminho de arquivo.
# Retorna: arch_name opcode hz symbol action
# Uso: python3 kobllux_arch_detect.py [arquivo1 arquivo2 ...]
#      python3 kobllux_arch_detect.py --staged   (lê git diff --cached)

import re
import sys
import subprocess
from collections import Counter

ARCHETYPES = {
    "kodux":   {"opcode":"0x01","hz":432,"sym":"●","action":"DETECTAR",
                "pat":["cadial_scan","_index","scan","detect","kodux"]},
    "nova":    {"opcode":"0x01","hz":432,"sym":"✦","action":"DETECTAR",
                "pat":["nova","new_","init","create","faísca","spark"]},
    "atlas":   {"opcode":"0x0A","hz":528,"sym":"⬡","action":"ESTRUTURAR",
                "pat":["atlas","README","manifest","schema","config","structure","docs","14_UTILS","03_CONFIG"]},
    "bllue":   {"opcode":"0x02","hz":528,"sym":"―","action":"INTEGRAR",
                "pat":["bllue","coupler","cadial-coupler","integrate","bridge","kob-glue"]},
    "serena":  {"opcode":"0x02","hz":528,"sym":"❋","action":"INTEGRAR",
                "pat":["serena","ui","splash","soft","css","style","theme"]},
    "rhea":    {"opcode":"0x09","hz":528,"sym":"∞","action":"FLUIR",
                "pat":["rhea","bridge","flow","connect","route","linkmaster","0S17"]},
    "vitalis": {"opcode":"0x08","hz":639,"sym":"◉","action":"PULSAR",
                "pat":["vitalis","core","engine","organic","vital","infodose-core"]},
    "artemis": {"opcode":"0x05","hz":672,"sym":"◎","action":"CONVERGIR",
                "pat":["artemis","test","precision","target","inject","newscast"]},
    "pulse":   {"opcode":"0x04","hz":594,"sym":"≋","action":"LAPIDAR",
                "pat":["pulse","tts","voice","audio","rhythm","kob-tts","voz"]},
    "kaos":    {"opcode":"0x07","hz":777,"sym":"⚡","action":"SELAR",
                "pat":["kaos","patch","fix","override","hot","brain","kodbrain"]},
    "genus":   {"opcode":"0x0B","hz":852,"sym":"⬢","action":"TEMPORIZAR",
                "pat":["genus","base","foundation","generate","gen","00_FUNDACAO"]},
    "lumine":  {"opcode":"0x0C","hz":963,"sym":"☀","action":"TRANSCENDER",
                "pat":["lumine","visual","light","theme","effect","lumine"]},
    "solus":   {"opcode":"0x01","hz":432,"sym":"◈","action":"DETECTAR",
                "pat":["solus","single","solo","unique","focus","kodbrain-11"]},
    "aion":    {"opcode":"0x0B","hz":639,"sym":"⧗","action":"TEMPORIZAR",
                "pat":["aion","memory","log","history","state","_state","07_NARRATIVA",
                       "MEMORIA","CHANGELOG","COMMIT_LOG"]},
}

DEFAULT = {"name":"kobllux","opcode":"0x00","hz":768,"sym":"○","action":"ORIGEM"}


def detect_arch(paths: list[str]) -> dict:
    scores: Counter = Counter()
    for path in paths:
        p = path.lower().replace("\\", "/")
        for arch, cfg in ARCHETYPES.items():
            for pat in cfg["pat"]:
                if pat.lower() in p:
                    scores[arch] += 1
    if not scores:
        return DEFAULT
    winner = scores.most_common(1)[0][0]
    cfg = ARCHETYPES[winner]
    return {"name": winner, **cfg}


def staged_files() -> list[str]:
    try:
        out = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only"],
            stderr=subprocess.DEVNULL
        ).decode().strip()
        return [f for f in out.splitlines() if f]
    except Exception:
        return []


if __name__ == "__main__":
    if "--staged" in sys.argv:
        files = staged_files()
    else:
        files = [a for a in sys.argv[1:] if not a.startswith("--")]

    if not files:
        files = staged_files()

    result = detect_arch(files)
    # Output: ARCH OPCODE HZ SYMBOL ACTION  (para ser consumido por bash)
    print(f"{result['name']} {result['opcode']} {result['hz']} {result.get('sym','○')} {result.get('action','ORIGEM')}")
