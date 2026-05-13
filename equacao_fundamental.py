#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
equacao_fundamental.py - Arquivo equacao_fundamental.py do sistema
"""

import sys

class EquacaoFundamental:
    def __init__(self):
        self.nome = "equacao_fundamental"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = EquacaoFundamental()
    print(obj.ativar())
