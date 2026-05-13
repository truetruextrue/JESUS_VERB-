#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
codex_azure.py - Fruto/Livro Digital
"""

import sys

class CodexAzure:
    def __init__(self):
        self.nome = "codex_azure"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = CodexAzure()
    print(obj.ativar())
