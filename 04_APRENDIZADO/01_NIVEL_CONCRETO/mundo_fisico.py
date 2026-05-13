#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
mundo_fisico.py - 1D-3D: Leis da física
"""

import sys

class MundoFisico:
    def __init__(self):
        self.nome = "mundo_fisico"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = MundoFisico()
    print(obj.ativar())
