#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
evolucao.py - A Evolução do Sistema
"""

import sys

class Evolucao:
    def __init__(self):
        self.nome = "evolucao"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Evolucao()
    print(obj.ativar())
