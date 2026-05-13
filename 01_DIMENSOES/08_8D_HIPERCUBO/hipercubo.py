#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
hipercubo.py - Transição entre camadas
"""

import sys

class Hipercubo:
    def __init__(self):
        self.nome = "hipercubo"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Hipercubo()
    print(obj.ativar())
