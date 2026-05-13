#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
2024_encontro.py - Fase de Encontro
"""

import sys

class 2024Encontro:
    def __init__(self):
        self.nome = "2024_encontro"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = 2024Encontro()
    print(obj.ativar())
