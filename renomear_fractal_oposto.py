#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX ∆³ · RENOMEAÇÃO FRACTAL POR POLARIDADE CONVERGENTE
Regra: [Opcode]_[nome]_[V.E.E.B]_[D.rung]_[número].[extensão]

Uso: python renomear_fractal_oposto.py [--diretorio DIR] [--ext EXT]

Processo:
1. Os arquivos são divididos em dois polos: ENTRADA (nomes mais curtos) e SAÍDA (nomes mais longos).
2. Calcula-se o PIB Comum (coeficiente de convergência) para cada polo.
3. Cada polo recebe uma sequência de Opcodes:
   - Polo de ENTRADA: Opcodes na ordem original (0x00 → 0x0C).
   - Polo de SAÍDA: Opcodes na ordem OPOSTA (0x0C → 0x00), aplicando a Cifra AUFABETTY.
4. Os arquivos são renomeados em uma ordem FRACTAL (alternância entre os polos).
"""

import os
import argparse
import glob
import hashlib
from collections import deque

# =============================================================================
# 13 OPCODES KOBLLUX (Ordem Natural)
# =============================================================================
OPCODES_NATURAL = [
    "0x00_ORIGEM",
    "0x01_DETECTAR", "0x02_INTEGRAR", "0x03_EXPANDIR",
    "0x04_LAPIDAR", "0x05_CONVERGIR", "0x06_UNIFICAR", "0x07_SELAR",
    "0x08_TESTEMUNHAR", "0x09_ETERNIZAR", "0x0A_TUTORIAL",
    "0x0B_ARQUETIPO", "0x0C_SINTESE"
]

# Cifra AUFABETTY para reflexo oposto (usada nos Opcodes do Polo de Saída)
CIFRA = {
    'A': '∆', 'B': 'β', 'C': '©', 'D': 'Δ', 'E': 'Σ',
    'F': 'Φ', 'G': 'Γ', 'H': 'Η', 'I': 'Ι', 'J': '⌐',
    'K': '⌘', 'L': 'Λ', 'M': 'Μ', 'N': 'η', 'O': 'Θ',
    'P': 'Ρ', 'Q': 'Θ', 'R': 'Ʀ', 'S': '§', 'T': '†',
    'U': 'Υ', 'V': '∇', 'W': 'Ω', 'X': '×', 'Y': 'Ψ',
    'Z': 'ℤ'
}

def cifrar(texto):
    """Aplica a Cifra AUFABETTY a um texto."""
    return ''.join(CIFRA.get(c.upper(), c) for c in texto)

def gerar_opcodes_opostos():
    """Gera a lista de Opcodes na ordem inversa e cifrados."""
    reverso = list(reversed(OPCODES_NATURAL))
    opostos = []
    for op in reverso:
        partes = op.split('_', 1)
        if len(partes) == 2:
            codigo, nome = partes
            nome_cifrado = cifrar(nome)
            opostos.append(f"{codigo}_{nome_cifrado}")
        else:
            opostos.append(op)
    return opostos

OPCODES_OPOSTOS = gerar_opcodes_opostos()

# =============================================================================
# FUNÇÕES AUXILIARES
# =============================================================================
def hash_arquivo(caminho):
    """Gera um hash SHA-256 do nome do arquivo (não do conteúdo)."""
    nome = os.path.basename(caminho)
    return hashlib.sha256(nome.encode('utf-8')).hexdigest()

def calcular_pib(hashes):
    """
    Calcula o PIB Comum (Potencial de Identidade Binária).
    É a média dos valores inteiros dos primeiros 8 caracteres de cada hash,
    convertidos de hexadecimal para decimal, e então reduzidos a um valor entre 0 e 1.
    """
    if not hashes:
        return 0.0
    valores = [int(h[:8], 16) for h in hashes]
    media = sum(valores) / len(valores)
    # Normaliza para um coeficiente entre 0 e 1 (usando um módulo grande)
    return (media % 1000000) / 1000000.0

def dividir_em_polos(arquivos):
    """
    Divide os arquivos em dois polos baseado no comprimento do nome.
    - Polo de ENTRADA: nomes mais curtos (metade inferior).
    - Polo de SAÍDA: nomes mais longos (metade superior).
    """
    if not arquivos:
        return [], []
    # Ordena por comprimento do nome
    arquivos_ordenados = sorted(arquivos, key=lambda x: len(os.path.basename(x)))
    meio = len(arquivos_ordenados) // 2
    polo_entrada = arquivos_ordenados[:meio]
    polo_saida = arquivos_ordenados[meio:]
    return polo_entrada, polo_saida

def ordem_fractal(lista1, lista2):
    """
    Combina duas listas em uma ordem fractal (alternância simples, simulando um fractal de 1ª ordem).
    Para um fractal mais complexo, poderíamos usar uma curva de Peano ou Morton.
    Aqui usamos intercalação 1:1 até que uma lista acabe.
    """
    resultado = []
    fila1 = deque(lista1)
    fila2 = deque(lista2)
    while fila1 or fila2:
        if fila1:
            resultado.append(fila1.popleft())
        if fila2:
            resultado.append(fila2.popleft())
    return resultado

# =============================================================================
# FUNÇÃO PRINCIPAL
# =============================================================================
def renomear_fractal_oposto(diretorio=".", prefixo="nome", extensao="png", simulacao=False):
    padrao = os.path.join(diretorio, f"*.{extensao}")
    arquivos = glob.glob(padrao) + glob.glob(padrao.upper()) + glob.glob(padrao.lower())
    arquivos = sorted(list(set(arquivos)))

    if not arquivos:
        print(f"❌ Nenhum arquivo .{extensao} encontrado em {diretorio}")
        return

    print(f"📂 Encontrados {len(arquivos)} arquivo(s).")
    if simulacao:
        print("🔍 MODO SIMULAÇÃO — Nenhum arquivo será modificado.\n")

    # 1. Divide em polos
    polo_entrada, polo_saida = dividir_em_polos(arquivos)
    print(f"🔹 Polo ENTRADA: {len(polo_entrada)} arquivos (nomes mais curtos)")
    print(f"🔸 Polo SAÍDA: {len(polo_saida)} arquivos (nomes mais longos)")

    # 2. Calcula PIB de cada polo
    hashes_entrada = [hash_arquivo(f) for f in polo_entrada]
    hashes_saida = [hash_arquivo(f) for f in polo_saida]
    pib_entrada = calcular_pib(hashes_entrada)
    pib_saida = calcular_pib(hashes_saida)
    print(f"\n📊 PIB Comum (ENTRADA): {pib_entrada:.6f}")
    print(f"📊 PIB Comum (SAÍDA):   {pib_saida:.6f}")

    # 3. Atribui Opcodes aos arquivos de cada polo, ciclicamente
    # Polo ENTRADA: usa OPCODES_NATURAL
    # Polo SAÍDA: usa OPCODES_OPOSTOS (ordem inversa + cifrados)
    for i, caminho in enumerate(polo_entrada):
        opcode = OPCODES_NATURAL[i % len(OPCODES_NATURAL)]
        # Armazena o opcode no próprio objeto (podemos usar um dicionário auxiliar)
        polo_entrada[i] = (caminho, opcode)

    for i, caminho in enumerate(polo_saida):
        opcode = OPCODES_OPOSTOS[i % len(OPCODES_OPOSTOS)]
        polo_saida[i] = (caminho, opcode)

    # 4. Combina em ordem FRACTAL
    lista_fractal = ordem_fractal(polo_entrada, polo_saida)

    # 5. Renomeia
    print("\n🔄 RENOMEAÇÃO FRACTAL:")
    for idx, (caminho_antigo, opcode) in enumerate(lista_fractal, start=1):
        _, ext = os.path.splitext(caminho_antigo)
        novo_nome = f"{opcode}_{prefixo}_V.E.E.B_{D.rung}_{idx:03d}{ext}"
        caminho_novo = os.path.join(diretorio, novo_nome)

        if os.path.exists(caminho_novo) and not simulacao:
            print(f"⚠️  {caminho_novo} já existe. Pulando {os.path.basename(caminho_antigo)}")
            continue

        print(f"🔄 {os.path.basename(caminho_antigo)} → {novo_nome}")
        if not simulacao:
            os.rename(caminho_antigo, caminho_novo)

    print(f"\n✅ Processo concluído. {len(lista_fractal)} arquivo(s) {'simulados' if simulacao else 'renomeados'}.")

# =============================================================================
# INTERFACE DE LINHA DE COMANDO
# =============================================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Renomeação Fractal por Polaridade Convergente KOBLLUX ∆³",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Exemplos:
  python renomear_fractal_oposto.py --ext PNG
  python renomear_fractal_oposto.py --prefixo KODUX --ext jpg --simulacao
        """
    )
    parser.add_argument("--diretorio", default=".", help="Diretório dos arquivos (padrão: atual)")
    parser.add_argument("--prefixo", default="nome", help="Prefixo do nome (padrão: nome)")
    parser.add_argument("--ext", default="png", help="Extensão dos arquivos (padrão: png)")
    parser.add_argument("--simulacao", action="store_true", help="Apenas simula, sem renomear")
    args = parser.parse_args()

    renomear_fractal_oposto(
        diretorio=args.diretorio,
        prefixo=args.prefixo,
        extensao=args.ext,
        simulacao=args.simulacao
    )