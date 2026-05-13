#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
ativar_sistema.py - Arquivo ativar_sistema.py do sistema
"""

import sys

class AtivarSistema:
    def __init__(self):
        self.nome = "ativar_sistema"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = AtivarSistema()
    print(obj.ativar())
