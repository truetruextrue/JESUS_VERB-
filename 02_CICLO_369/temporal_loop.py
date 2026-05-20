#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
temporal_loop.py · FASE 03 · CICLO 3-6-9 · aion · 0x3 · ∆7
3=Mente 6=Corpo 9=Alma

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class TemporalLoop(KoblluxPhaseBase):
    """FASE 03 · CICLO 3-6-9 — 3=Mente 6=Corpo 9=Alma."""
    FASE   = 3
    OPCODE = 0x3
    NOME   = "CICLO 3-6-9"
    ARCH   = "aion"
    DESC   = "3=Mente 6=Corpo 9=Alma"


if __name__ == "__main__":
    obj = TemporalLoop()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
