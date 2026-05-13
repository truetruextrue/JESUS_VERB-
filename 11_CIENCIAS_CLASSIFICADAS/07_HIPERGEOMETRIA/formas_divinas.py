#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
formas_divinas.py - Forma da forma
"""

import sys

class FormasDivinas:
    def __init__(self):
        self.nome = "formas_divinas"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = FormasDivinas()
    print(obj.ativar())
