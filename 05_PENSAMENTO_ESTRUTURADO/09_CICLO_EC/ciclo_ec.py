#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
ciclo_ec.py - Expansão e Contração
"""

import sys

class CicloEc:
    def __init__(self):
        self.nome = "ciclo_ec"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = CicloEc()
    print(obj.ativar())
