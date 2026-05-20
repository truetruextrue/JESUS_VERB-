#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sintese_final.py · FASE 13 · V.E.E.B. SÍNTESE · kobllux · 0xc · ∆7
Vibração·Energia·Estrutura·Base

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class SinteseFinal(KoblluxPhaseBase):
    """FASE 13 · V.E.E.B. SÍNTESE — Vibração·Energia·Estrutura·Base."""
    FASE   = 13
    OPCODE = 0xc
    NOME   = "V.E.E.B. SÍNTESE"
    ARCH   = "kobllux"
    DESC   = "Vibração·Energia·Estrutura·Base"


if __name__ == "__main__":
    obj = SinteseFinal()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
