#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pulse_monitor.py · FASE 10 · LINHA DO PULSO · pulse · 0xa · ∆7
Decoder de sinais · registro vivo

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class PulseMonitor(KoblluxPhaseBase):
    """FASE 10 · LINHA DO PULSO — Decoder de sinais · registro vivo."""
    FASE   = 10
    OPCODE = 0xa
    NOME   = "LINHA DO PULSO"
    ARCH   = "pulse"
    DESC   = "Decoder de sinais · registro vivo"


if __name__ == "__main__":
    obj = PulseMonitor()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
