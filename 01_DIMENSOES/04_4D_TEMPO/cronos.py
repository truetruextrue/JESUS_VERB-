#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
cronos.py - Fluxo da evolução
"""

import sys

class Cronos:
    def __init__(self):
        self.nome = "cronos"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Cronos()
    print(obj.ativar())
