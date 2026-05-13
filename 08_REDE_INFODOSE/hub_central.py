#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
hub_central.py - O Sistema de Transmissão
"""

import sys

class HubCentral:
    def __init__(self):
        self.nome = "hub_central"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = HubCentral()
    print(obj.ativar())
