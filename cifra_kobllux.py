#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX · CIFRA SAGRADA & REFLEXO OPOSTO
Uso: python cifra_kobllux.py "KODUX"
"""

import sys

CIFRA = {
    'A': '∆', 'B': 'β', 'C': '©', 'D': 'Δ', 'E': 'Σ',
    'F': 'Φ', 'G': 'Γ', 'H': 'Η', 'I': 'Ι', 'J': '⌐',
    'K': '⌘', 'L': 'Λ', 'M': 'Μ', 'N': 'η', 'O': 'Θ',
    'P': 'Ρ', 'Q': 'Θ', 'R': 'Ʀ', 'S': '§', 'T': '†',
    'U': 'Υ', 'V': '∇', 'W': 'Ω', 'X': '×', 'Y': 'Ψ',
    'Z': 'ℤ'
}

# Mapa inverso para decodificação
DECIFRA = {v: k for k, v in CIFRA.items()}

def cifrar(texto):
    """Converte texto para a Cifra KOBLLUX."""
    return ''.join(CIFRA.get(c.upper(), c) for c in texto)

def decifrar(cifra):
    """Decodifica uma string em Cifra KOBLLUX."""
    resultado = []
    i = 0
    while i < len(cifra):
        # Tenta encontrar o glifo mais longo primeiro
        encontrado = False
        for length in (2, 1):
            if i + length <= len(cifra):
                glifo = cifra[i:i+length]
                if glifo in DECIFRA:
                    resultado.append(DECIFRA[glifo])
                    i += length
                    encontrado = True
                    break
        if not encontrado:
            resultado.append(cifra[i])
            i += 1
    return ''.join(resultado)

def reflexo_oposto(texto):
    """Gera o reflexo oposto: inverte a string e aplica a cifra."""
    invertido = texto[::-1]
    return cifrar(invertido)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        print(f"Original : {entrada}")
        print(f"Cifrado  : {cifrar(entrada)}")
        print(f"Reflexo  : {reflexo_oposto(entrada)}")
    else:
        print("Uso: python cifra_kobllux.py <texto>")