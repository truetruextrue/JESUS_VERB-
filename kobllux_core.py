#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
kobllux_core.py - Arquivo kobllux_core.py do sistema
"""

import sys

class KoblluxCore:
    def __init__(self):
        self.nome = "kobllux_core"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = KoblluxCore()
    print(obj.ativar())
