#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
transmissores.py - O Sistema de Transmissão
"""

import sys

class Transmissores:
    def __init__(self):
        self.nome = "transmissores"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Transmissores()
    print(obj.ativar())
