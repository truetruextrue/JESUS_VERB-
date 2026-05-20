#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
arborista.py · FASE 11 · ÁRVORE FRACTAL · genus · 0xb · ∆7
Raiz·Galhos·Frutos · régua 3-6-9-7

Conectado ao SumbusFirmware via KoblluxPhaseBase.
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_phase_base import KoblluxPhaseBase, FASE_OPCODE


class Arborista(KoblluxPhaseBase):
    """FASE 11 · ÁRVORE FRACTAL — Raiz·Galhos·Frutos · régua 3-6-9-7."""
    FASE   = 11
    OPCODE = 0xb
    NOME   = "ÁRVORE FRACTAL"
    ARCH   = "genus"
    DESC   = "Raiz·Galhos·Frutos · régua 3-6-9-7"


if __name__ == "__main__":
    obj = Arborista()
    print(json.dumps(obj.ativar(), ensure_ascii=False, indent=2))
    print(json.dumps(obj.status(), ensure_ascii=False, indent=2))
