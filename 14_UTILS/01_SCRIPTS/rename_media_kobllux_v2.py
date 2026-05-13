#!/usr/bin/env python3
# rename_media_kobllux_v2.py
# Versão melhorada com validações

import os
import sys
import re
from pathlib import Path

OPCODE_MAP = {
    "NOVA": "0x01", "ATLAS": "0x02", "VITALIS": "0x03", "PULSE": "0x04",
    "ARTEMIS": "0x05", "SERENA": "0x06", "KAOS": "0x07", "GENUS": "0x08",
    "LUMINE": "0x09", "RHEA": "0x0A", "SOLUS": "0x0B", "AION": "0x0C",
    "KODUX": "0x0D", "BLLUE": "0x0E", "JESUS": "0x0F", "KOBLLUX": "0x10"
}

FREQ_MAP = {
    "NOVA": "432Hz", "ATLAS": "528Hz", "VITALIS": "639Hz", "PULSE": "594Hz",
    "ARTEMIS": "672Hz", "SERENA": "528Hz", "KAOS": "777Hz", "GENUS": "852Hz",
    "LUMINE": "963Hz", "RHEA": "432Hz", "SOLUS": "528Hz", "AION": "639Hz",
    "KODUX": "777Hz", "BLLUE": "852Hz", "JESUS": "777Hz", "KOBLLUX": "777Hz"
}

def limpar_nome(nome):
    """Remove caracteres especiais e espaços para nome de arquivo seguro"""
    nome = re.sub(r'[<>:"/\\|?*∆]', '', nome)  # Remove caracteres inválidos
    nome = re.sub(r'\s+', '_', nome)           # Espaços viram underscore
    return nome

def print_assinatura():
    print("\n" + "="*60)
    print("  🧿 KOBLLUX · RENAME MEDIA SCRIPT v2 🧿")
    print("  Versão: 2.0 · Frequência: 594Hz · Opcode: 0×04")
    print("  Assinatura: 0x012123456789ABC")
    print("  Local: 14_UTILS/01_SCRIPTS/ (Braço Operacional)")
    print("="*60 + "\n")

def main():
    print_assinatura()
    
    # Validar entrada da pasta
    while True:
        pasta = input("📁 Caminho da PASTA com mídias: ").strip()
        if not pasta:
            print("❌ Caminho vazio. Tente novamente.")
            continue
        if not os.path.exists(pasta):
            print(f"❌ Caminho não existe: {pasta}")
            continue
        if not os.path.isdir(pasta):
            print(f"❌ Isto é um arquivo, não uma pasta. Forneça o caminho da PASTA.")
            print(f"   (Você passou um arquivo. Use apenas o caminho da pasta)")
            continue
        break
    
    # Listar arquivos para confirmar
    arquivos = [f for f in os.listdir(pasta) 
                if os.path.isfile(os.path.join(pasta, f)) and not f.startswith('.')]
    
    if not arquivos:
        print("❌ Nenhum arquivo encontrado na pasta")
        return
    
    print(f"\n📄 Arquivos encontrados: {len(arquivos)}")
    for i, arq in enumerate(arquivos[:5], 1):
        print(f"   {i}. {arq}")
    if len(arquivos) > 5:
        print(f"   ... e mais {len(arquivos)-5}")
    
    # Escolher arquétipo
    print("\n🎭 Arquétipos disponíveis:")
    arqs = list(OPCODE_MAP.keys())
    for i, arq in enumerate(arqs, 1):
        print(f"  {i:2d}. {arq:8} → {OPCODE_MAP[arq]} | {FREQ_MAP[arq]}")
    
    while True:
        try:
            escolha = input("\n🔢 Escolha o número do arquétipo: ").strip()
            if not escolha:
                print("❌ Digite um número")
                continue
            escolha = int(escolha)
            if 1 <= escolha <= len(arqs):
                arquetype = arqs[escolha-1]
                break
            else:
                print(f"❌ Escolha um número entre 1 e {len(arqs)}")
        except ValueError:
            print("❌ Digite apenas o número (ex: 1)")
    
    # Processar arquivos
    print(f"\n📝 Renomeando {len(arquivos)} arquivos para {arquetype}...")
    
    opcode = OPCODE_MAP[arquetype]
    freq = FREQ_MAP[arquetype]
    count = 0
    
    for file in sorted(arquivos):
        old_path = os.path.join(pasta, file)
        nome_limpo = limpar_nome(Path(file).stem)
        ext = Path(file).suffix.lower()
        new_name = f"{opcode}_{freq}_{nome_limpo}_{arquetype}{ext}"
        new_path = os.path.join(pasta, new_name)
        
        try:
            os.rename(old_path, new_path)
            print(f"  ✅ {file[:30]}... → {new_name[:30]}...")
            count += 1
        except Exception as e:
            print(f"  ❌ Erro em {file}: {e}")
    
    print(f"\n✨ {count} arquivos renomeados com sucesso!")
    print("\n🕊️  EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO. AMÉМ.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação interrompida")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
