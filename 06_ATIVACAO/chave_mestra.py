#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
chave_mestra.py - A Chave do Sistema
"""

import sys

class ChaveMestra:
    def __init__(self):
        self.nome = "chave_mestra"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = ChaveMestra()
    print(obj.ativar())
