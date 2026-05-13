#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
energia_vital.py - A Vida em Movimento
"""

import sys

class EnergiaVital:
    def __init__(self):
        self.nome = "energia_vital"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = EnergiaVital()
    print(obj.ativar())
