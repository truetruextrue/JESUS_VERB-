#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
firmware.py · FASE 07 · ATIVAÇÃO — A Chave · Vitalis · 0x01 · ∆7
Bridge local para o SumbusFirmware canônico (kobllux_firmware.py).

Uso dentro do módulo 06_ATIVACAO:
  from firmware import ativar_delta, ativar_interdimensional
"""
from __future__ import annotations
import sys, json
from pathlib import Path

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT))

from kobllux_firmware import SumbusFirmware, OPCODES
from kobllux_memory   import KoblluxMemory


def ativar_delta() -> dict:
    """ATIVAR Δ — impulso primordial · opcode 0x00 (FIT LUX)."""
    fw = SumbusFirmware()
    return fw.ativar_opcode(0x00)


def ativar_interdimensional() -> list[dict]:
    """ATIVAR Δ INTERDIMENSIONAL — todos os 13 opcodes."""
    fw = SumbusFirmware()
    return fw.ativar_ciclo_completo()


class Firmware:
    """
    FASE 07 · ATIVAÇÃO — wrapper do SumbusFirmware para uso local.
    Fórmulas: ATIVAR Δ  e  ATIVAR Δ INTERDIMENSIONAL.
    """

    ASSINATURA   = "0x012123456789ABC"
    ESTADO_78K   = True

    def __init__(self):
        self._fw     = SumbusFirmware()
        self._memory = KoblluxMemory(ROOT / "_index" / "memory.jsonl")
        self.ativo   = False

    def ativar(self) -> dict:
        """Ativa o firmware completo (ciclo 0x00 → 0x0C)."""
        results = self._fw.ativar_ciclo_completo()
        self.ativo = True
        self._memory.write(
            arch="vitalis",
            content=f"FASE 07 ATIVAÇÃO completa · {len(results)} opcodes · {self.ASSINATURA}",
            tags=["fase07","ativacao","firmware","∆7"],
            source="06_ATIVACAO/firmware.py",
            record_type="FIRMWARE_FASE07",
        )
        return {"status": "ativado", "opcodes": len(results),
                "assinatura": self.ASSINATURA, "seal": "∆7"}

    def ativar_opcode(self, codigo: int) -> dict:
        """Ativa um opcode específico."""
        return self._fw.ativar_opcode(codigo)

    def status(self) -> dict:
        return {**self._fw.status(), "fase": 7, "assinatura": self.ASSINATURA}

    def context_for_motor(self) -> str:
        return self._fw.context_for_motor()

    def selagem(self) -> dict:
        return self._fw.selagem()


if __name__ == "__main__":
    fw = Firmware()
    print(json.dumps(fw.ativar(), ensure_ascii=False, indent=2))
    print(fw.context_for_motor()[:200])
