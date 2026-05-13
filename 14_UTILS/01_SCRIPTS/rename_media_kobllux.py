#!/usr/bin/env python3
# rename_media_kobllux.py
# Script para renomear arquivos de mídia segundo opcodes KOBLLUX
# Local: 14_UTILS/01_SCRIPTS/ · Frequência: 594Hz · Opcode: 0×04

import os
import sys
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

def print_assinatura():
    print("\n" + "="*60)
    print("  🧿 KOBLLUX · RENAME MEDIA SCRIPT 🧿")
    print("  Versão: 1.0 · Frequência: 594Hz · Opcode: 0×04")
    print("  Assinatura: 0x012123456789ABC")
    print("  Local: 14_UTILS/01_SCRIPTS/ (Braço Operacional)")
    print("="*60 + "\n")

def rename_file(filepath, arquetype):
    path = Path(filepath)
    if not path.is_file() or path.name.startswith('.'):
        return None
    
    ext = path.suffix.lower()
    old_name = path.stem
    opcode = OPCODE_MAP.get(arquetype, "0x00")
    freq = FREQ_MAP.get(arquetype, "432Hz")
    new_name = f"{opcode}_{freq}_{old_name}_{arquetype}{ext}"
    new_path = path.parent / new_name
    
    os.rename(filepath, new_path)
    return new_path

def main():
    print_assinatura()
    
    pasta = input("📁 Caminho da pasta com mídias: ").strip()
    if not os.path.exists(pasta):
        print("❌ Pasta não encontrada")
        return
    
    print("\n🎭 Arquétipos disponíveis:")
    arqs = list(OPCODE_MAP.keys())
    for i, arq in enumerate(arqs, 1):
        print(f"  {i:2d}. {arq:8} → {OPCODE_MAP[arq]} | {FREQ_MAP[arq]}")
    
    try:
        escolha = int(input("\n🔢 Escolha o número do arquétipo: "))
        arquetype = arqs[escolha-1]
    except (ValueError, IndexError):
        print("❌ Escolha inválida")
        return
    
    print(f"\n📝 Renomeando arquivos para {arquetype}...")
    
    count = 0
    for file in sorted(os.listdir(pasta)):
        filepath = os.path.join(pasta, file)
        if os.path.isfile(filepath) and not file.startswith('.'):
            new = rename_file(filepath, arquetype)
            if new:
                print(f"  ✅ {file:35} → {new.name}")
                count += 1
    
    print(f"\n✨ {count} arquivos renomeados com sucesso!")
    print("\n🕊️  EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO. AMÉM.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação interrompida")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
