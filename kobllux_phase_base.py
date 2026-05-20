#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_phase_base.py · Atlas · 0x00 · BOOT · ∆7
Classe base para todos os módulos de fase KOBLLUX.

Qualquer fase herda de KoblluxPhaseBase e ganha:
  - ativar(opcode)     → dispara opcode via SumbusFirmware + grava memory
  - status()           → estado atual
  - context()          → contexto para 78K-motor
"""
from __future__ import annotations
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from kobllux_firmware import SumbusFirmware, OPCODES
from kobllux_memory   import KoblluxMemory


class KoblluxPhaseBase:
    """
    Base comum a todas as 13 fases do sistema KOBLLUX.
    Conecta automaticamente ao SumbusFirmware e à KoblluxMemory.
    """

    FASE:    int  = 0
    OPCODE:  int  = 0x00
    NOME:    str  = "KOBLLUX"
    ARCH:    str  = "kobllux"
    DESC:    str  = "fase base"

    def __init__(self):
        self._fw     = SumbusFirmware()
        self._mem    = KoblluxMemory(ROOT / "_index" / "memory.jsonl")
        self.ativo   = False
        self._source = f"FASE{self.FASE:02d}/{self.__class__.__name__.lower()}.py"

    def ativar(self, extra: dict[str, Any] | None = None) -> dict:
        """Ativa a fase: dispara opcode → grava memory → retorna resultado."""
        op = self.OPCODE
        if op not in OPCODES:
            op = 0x00
        result = self._fw.ativar_opcode(op)
        self.ativo = True
        self._mem.write(
            arch=self.ARCH,
            content=f"FASE {self.FASE:02d} {self.NOME} ativada · {self.DESC}",
            tags=[f"fase{self.FASE:02d}", self.NOME.lower(), "∆7"],
            source=self._source,
            record_type=f"FASE_{self.FASE:02d}",
            extra=extra or {},
        )
        print(f"✓ FASE {self.FASE:02d} · {self.NOME} · {result['nome']} · {result['hz']}Hz · ∆7")
        return result

    def status(self) -> dict:
        op_info = OPCODES.get(self.OPCODE, {})
        return {
            "fase":   self.FASE,
            "nome":   self.NOME,
            "opcode": hex(self.OPCODE),
            "hz":     op_info.get("hz", 0),
            "arch":   self.ARCH,
            "ativo":  self.ativo,
            "lei":    "VERDADE × INTEGRAR ÷ Δ = ∞",
        }

    def context(self) -> str:
        return self._fw.context_for_motor()

    def __repr__(self):
        return f"<{self.__class__.__name__} FASE={self.FASE} ativo={self.ativo}>"


# ── Mapa canônico fase → opcode ───────────────────────────────────────────────
FASE_OPCODE: dict[int, int] = {
    1:  0x00,  # FUNDAÇÃO       · FIT LUX
    2:  0x02,  # DIMENSÕES      · OLHO DE HÓRUS
    3:  0x03,  # CICLO 3-6-9    · VSICA PSI
    4:  0x04,  # FLUXO ENERG.   · (bridge)
    5:  0x05,  # APRENDIZADO    · BLLUE
    6:  0x06,  # PENSAMENTO     · INFODOSE
    7:  0x07,  # ATIVAÇÃO       · DUAL APP
    8:  0x08,  # NARRATIVA      · NEPHESH ELYON
    9:  0x09,  # REDE INFODOSE  · KAEL DOMINUS
    10: 0x0A,  # LINHA PULSO    · 3×6×9
    11: 0x0B,  # ÁRVORE FRACTAL · VERDADE×INTEGRAR÷Δ
    12: 0x0B,  # CIÊNCIAS       · VERDADE×INTEGRAR÷Δ
    13: 0x0C,  # V.E.E.B.       · JESUS VERBO
}

FASE_ARCH: dict[int, str] = {
    1:"nova", 2:"atlas", 3:"aion", 4:"vitalis", 5:"nova",
    6:"atlas", 7:"vitalis", 8:"aion", 9:"rhea", 10:"pulse",
    11:"genus", 12:"artemis", 13:"kobllux",
}
