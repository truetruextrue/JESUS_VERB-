#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
input_handler.py - Coletar informações do ambiente
"""

import sys

class InputHandler:
    def __init__(self):
        self.nome = "input_handler"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = InputHandler()
    print(obj.ativar())
