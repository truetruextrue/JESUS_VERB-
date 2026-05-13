#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
forma_viva.py - Processo contínuo de transformação
"""

import sys

class FormaViva:
    def __init__(self):
        self.nome = "forma_viva"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = FormaViva()
    print(obj.ativar())
