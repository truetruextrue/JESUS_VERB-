#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
arte_generator.py - Painel ASCII
"""

import sys

class ArteGenerator:
    def __init__(self):
        self.nome = "arte_generator"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = ArteGenerator()
    print(obj.ativar())
