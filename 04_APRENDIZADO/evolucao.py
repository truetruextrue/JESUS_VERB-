#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
evolucao.py · FASE 05 · APRENDIZADO · nova · 0x5 · ∆7
Expansão · Contração · Evolução

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class Evolucao(KoblluxPhaseBase):
    """FASE 05 · APRENDIZADO — Expansão · Contração · Evolução."""
    FASE   = 5
    OPCODE = 0x5
    NOME   = "APRENDIZADO"
    ARCH   = "nova"
    DESC   = "Expansão · Contração · Evolução"


if __name__ == "__main__":
    obj = Evolucao()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
