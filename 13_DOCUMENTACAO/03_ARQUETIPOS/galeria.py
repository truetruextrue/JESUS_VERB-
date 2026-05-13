#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
galeria.py - Os 12 Rostos + 4 Centrais
"""

import sys

class Galeria:
    def __init__(self):
        self.nome = "galeria"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Galeria()
    print(obj.ativar())
