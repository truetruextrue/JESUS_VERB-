#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
metodo_atlas.py - O Método do Sistema
"""

import sys

class MetodoAtlas:
    def __init__(self):
        self.nome = "metodo_atlas"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = MetodoAtlas()
    print(obj.ativar())
