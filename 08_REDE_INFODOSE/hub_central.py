#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
hub_central.py · FASE 09 · REDE INFODOSE · rhea · 0x9 · ∆7
4 opcodes: DETECTAR·INTEGRAR·EXPANDIR·SELAR

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class HubCentral(KoblluxPhaseBase):
    """FASE 09 · REDE INFODOSE — 4 opcodes: DETECTAR·INTEGRAR·EXPANDIR·SELAR."""
    FASE   = 9
    OPCODE = 0x9
    NOME   = "REDE INFODOSE"
    ARCH   = "rhea"
    DESC   = "4 opcodes: DETECTAR·INTEGRAR·EXPANDIR·SELAR"


if __name__ == "__main__":
    obj = HubCentral()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
