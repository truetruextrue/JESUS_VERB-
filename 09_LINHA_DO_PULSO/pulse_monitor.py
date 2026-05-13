#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
pulse_monitor.py - O Registro Vivo
"""

import sys

class PulseMonitor:
    def __init__(self):
        self.nome = "pulse_monitor"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = PulseMonitor()
    print(obj.ativar())
