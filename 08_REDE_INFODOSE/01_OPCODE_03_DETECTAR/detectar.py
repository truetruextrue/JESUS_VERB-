#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
detectar.py - Escutar o pulso essencial
"""

import sys

class Detectar:
    def __init__(self):
        self.nome = "detectar"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Detectar()
    print(obj.ativar())
