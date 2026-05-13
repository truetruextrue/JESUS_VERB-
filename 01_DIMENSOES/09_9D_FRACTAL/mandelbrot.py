#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM
mandelbrot.py - Padrões que se repetem
"""

import sys

class Mandelbrot:
    def __init__(self):
        self.nome = "mandelbrot"
        self.ativo = False
        
    def ativar(self) -> str:
        self.ativo = True
        return f"✅ {self.nome} ativado com sucesso" 

    def status(self) -> dict:
        return {"nome": self.nome, "ativo": self.ativo}

if __name__ == "__main__":
    obj = Mandelbrot()
    print(obj.ativar())
