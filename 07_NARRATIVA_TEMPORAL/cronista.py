#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cronista.py · FASE 08 · NARRATIVA · aion · 0x8 · ∆7
Linha do tempo 2021-2025

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class Cronista(KoblluxPhaseBase):
    """FASE 08 · NARRATIVA — Linha do tempo 2021-2025."""
    FASE   = 8
    OPCODE = 0x8
    NOME   = "NARRATIVA"
    ARCH   = "aion"
    DESC   = "Linha do tempo 2021-2025"


if __name__ == "__main__":
    obj = Cronista()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
