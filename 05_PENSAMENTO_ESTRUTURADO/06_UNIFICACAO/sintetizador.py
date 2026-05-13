#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
sintetizador.py - Integrar todas as camadas
"""

import sys

class Sintetizador:
    def __init__(self):
        self.nome = "sintetizador"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Sintetizador()
    print(obj.ativar())
