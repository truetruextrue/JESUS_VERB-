#!/usr/bin/env python3
# kobllux_media_processor_v4.py
# Versão CORRIGIDA - Inicializa catálogo corretamente

import os
import sys
import json
import shutil
import re
from datetime import datetime
from pathlib import Path

# ==================== CONFIGURAÇÕES ====================
BASE_PATH = "/storage/emulated/0/0/0/KOBLLUX"
MIDIA_PATH = f"{BASE_PATH}/17_MIDIA_INFODOSE"
METADATA_PATH = f"{MIDIA_PATH}/.metadata"
ASSINATURA = "0x012123456789ABC"

# Mapeamento completo
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

# Pastas de destino por tipo de mídia
DESTINO_MAP = {
    "video": {
        "NOVA": f"{MIDIA_PATH}/01_VIDEO/432Hz_NOVA/",
        "ATLAS": f"{MIDIA_PATH}/01_VIDEO/528Hz_ATLAS/",
        "VITALIS": f"{MIDIA_PATH}/01_VIDEO/639Hz_VITALIS/",
        "PULSE": f"{MIDIA_PATH}/01_VIDEO/594Hz_PULSE/",
        "ARTEMIS": f"{MIDIA_PATH}/01_VIDEO/672Hz_ARTEMIS/",
        "SERENA": f"{MIDIA_PATH}/01_VIDEO/528Hz_SERENA/",
        "KAOS": f"{MIDIA_PATH}/01_VIDEO/777Hz_KAOS/",
        "GENUS": f"{MIDIA_PATH}/01_VIDEO/852Hz_GENUS/",
        "LUMINE": f"{MIDIA_PATH}/01_VIDEO/963Hz_LUMINE/",
        "RHEA": f"{MIDIA_PATH}/01_VIDEO/432Hz_RHEA/",
        "SOLUS": f"{MIDIA_PATH}/01_VIDEO/528Hz_SOLUS/",
        "AION": f"{MIDIA_PATH}/01_VIDEO/639Hz_AION/",
        "KODUX": f"{MIDIA_PATH}/01_VIDEO/777Hz_KODUX/",
        "BLLUE": f"{MIDIA_PATH}/01_VIDEO/852Hz_BLLUE/",
        "JESUS": f"{MIDIA_PATH}/01_VIDEO/777Hz_JESUS/",
        "KOBLLUX": f"{MIDIA_PATH}/01_VIDEO/777Hz_KOBLLUX/"
    },
    "audio": {
        "NOVA": f"{MIDIA_PATH}/02_AUDIO/04_INFODOSES/",
        "ATLAS": f"{MIDIA_PATH}/02_AUDIO/03_FREQUENCIAS/",
        "VITALIS": f"{MIDIA_PATH}/02_AUDIO/01_PULSOS/",
        "PULSE": f"{MIDIA_PATH}/02_AUDIO/01_PULSOS/",
        "ARTEMIS": f"{MIDIA_PATH}/02_AUDIO/04_INFODOSES/",
        "SERENA": f"{MIDIA_PATH}/02_AUDIO/02_MANTRAS/",
        "KAOS": f"{MIDIA_PATH}/02_AUDIO/06_EFEITOS/",
        "GENUS": f"{MIDIA_PATH}/02_AUDIO/05_MUSICAS/",
        "LUMINE": f"{MIDIA_PATH}/02_AUDIO/05_MUSICAS/",
        "RHEA": f"{MIDIA_PATH}/02_AUDIO/02_MANTRAS/",
        "SOLUS": f"{MIDIA_PATH}/02_AUDIO/07_AMBIENTES/",
        "AION": f"{MIDIA_PATH}/02_AUDIO/03_FREQUENCIAS/",
        "KODUX": f"{MIDIA_PATH}/02_AUDIO/03_FREQUENCIAS/",
        "BLLUE": f"{MIDIA_PATH}/02_AUDIO/02_MANTRAS/",
        "JESUS": f"{MIDIA_PATH}/02_AUDIO/02_MANTRAS/",
        "KOBLLUX": f"{MIDIA_PATH}/02_AUDIO/04_INFODOSES/"
    }
}

# ==================== FUNÇÕES ====================
def limpar_nome(nome):
    """Remove caracteres especiais para nome de arquivo seguro"""
    nome = re.sub(r'[<>:"/\\|?*∆]', '', nome)
    nome = re.sub(r'\s+', '_', nome)
    return nome

def detectar_tipo_midia(arquivo):
    """Detecta se é vídeo, áudio, app, etc"""
    ext = Path(arquivo).suffix.lower()
    video_ext = ['.mp4', '.avi', '.mov', '.mkv', '.webm']
    audio_ext = ['.mp3', '.wav', '.flac', '.ogg', '.m4a', '.aac']
    if ext in video_ext:
        return "video"
    elif ext in audio_ext:
        return "audio"
    return "outro"

def inicializar_catalogo():
    """CRIA um catálogo NOVO com todas as chaves necessárias"""
    return {
        "versao": "1.0",
        "data_criacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "data_atualizacao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_midias": 0,
        "por_opcode": {},
        "por_arquétipo": {},
        "por_tipo": {"video": 0, "audio": 0, "app": 0, "outro": 0},
        "midias": [],
        "assinatura": ASSINATURA,
        "estado": "85K EM EXPANSÃO"
    }

def carregar_catalogo():
    """Carrega o catálogo JSON existente ou cria um novo com estrutura COMPLETA"""
    catalogo_path = f"{METADATA_PATH}/catalogo_geral.json"
    
    # Garantir que a pasta .metadata existe
    os.makedirs(METADATA_PATH, exist_ok=True)
    
    if os.path.exists(catalogo_path):
        try:
            with open(catalogo_path, 'r', encoding='utf-8') as f:
                catalogo = json.load(f)
                # Verificar se todas as chaves necessárias existem
                if "midias" not in catalogo:
                    catalogo["midias"] = []
                if "por_tipo" not in catalogo:
                    catalogo["por_tipo"] = {"video": 0, "audio": 0, "app": 0, "outro": 0}
                if "por_opcode" not in catalogo:
                    catalogo["por_opcode"] = {}
                if "por_arquétipo" not in catalogo:
                    catalogo["por_arquétipo"] = {}
                return catalogo
        except:
            # Se o arquivo estiver corrompido, criar novo
            return inicializar_catalogo()
    else:
        return inicializar_catalogo()

def salvar_catalogo(catalogo):
    """Salva o catálogo JSON"""
    catalogo_path = f"{METADATA_PATH}/catalogo_geral.json"
    catalogo["data_atualizacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Garantir que a pasta existe
    os.makedirs(METADATA_PATH, exist_ok=True)
    
    with open(catalogo_path, 'w', encoding='utf-8') as f:
        json.dump(catalogo, f, indent=2, ensure_ascii=False)

def registrar_operacao(log_entry):
    """Registra operação em arquivo de log"""
    log_path = f"{BASE_PATH}/14_UTILS/02_LOGS/renomeacoes.log"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().isoformat()} | {log_entry}\n")

def print_assinatura():
    print("\n" + "="*70)
    print("  🧿 KOBLLUX · MEDIA PROCESSOR v4 🧿")
    print("  Versão: 4.0 · Frequência: 777Hz · Opcode: 0×07")
    print("  Assinatura: 0x012123456789ABC")
    print("  Funções: Renomear + Mover + Metadados (CORRIGIDO)")
    print("="*70 + "\n")

# ==================== MAIN ====================
def main():
    print_assinatura()
    
    # 1. Validar pasta de origem
    while True:
        origem = input("📁 Caminho da PASTA de origem: ").strip()
        if not origem:
            print("❌ Caminho vazio")
            continue
        if not os.path.exists(origem):
            print(f"❌ Caminho não existe: {origem}")
            continue
        if not os.path.isdir(origem):
            print(f"❌ Isto é um arquivo. Forneça uma PASTA.")
            continue
        break
    
    # 2. Listar arquivos
    arquivos = [f for f in os.listdir(origem) 
                if os.path.isfile(os.path.join(origem, f)) and not f.startswith('.')]
    
    if not arquivos:
        print("❌ Nenhum arquivo encontrado")
        return
    
    print(f"\n📄 Arquivos encontrados: {len(arquivos)}")
    for i, arq in enumerate(arquivos[:5], 1):
        print(f"   {i}. {arq[:50]}...")
    if len(arquivos) > 5:
        print(f"   ... e mais {len(arquivos)-5}")
    
    # 3. Escolher arquétipo
    print("\n🎭 Arquétipos disponíveis:")
    arqs = list(OPCODE_MAP.keys())
    for i, arq in enumerate(arqs, 1):
        print(f"  {i:2d}. {arq:8} → {OPCODE_MAP[arq]} | {FREQ_MAP[arq]}")
    
    while True:
        try:
            escolha = input("\n🔢 Escolha o número do arquétipo: ").strip()
            if not escolha:
                continue
            escolha = int(escolha)
            if 1 <= escolha <= len(arqs):
                arquetype = arqs[escolha-1]
                break
            else:
                print(f"❌ Escolha entre 1 e {len(arqs)}")
        except ValueError:
            print("❌ Digite apenas o número")
    
    # 4. Processar cada arquivo
    opcode = OPCODE_MAP[arquetype]
    freq = FREQ_MAP[arquetype]
    
    # CARREGAR CATÁLOGO (agora com inicialização correta)
    catalogo = carregar_catalogo()
    
    count = 0
    erros = []
    
    print(f"\n📝 Processando {len(arquivos)} arquivos para {arquetype}...")
    
    for arquivo in sorted(arquivos):
        origem_path = os.path.join(origem, arquivo)
        
        # Detectar tipo de mídia
        tipo = detectar_tipo_midia(arquivo)
        if tipo not in ["video", "audio"]:
            print(f"  ⚠️  {arquivo} → tipo não suportado (pulado)")
            continue
        
        # Determinar pasta de destino
        if tipo in DESTINO_MAP and arquetype in DESTINO_MAP[tipo]:
            destino_pasta = DESTINO_MAP[tipo][arquetype]
        else:
            # Fallback: pasta genérica
            destino_pasta = f"{MIDIA_PATH}/06_ARQUIVO_BRUTO/PROCESSADOS/"
        
        # Criar pasta de destino se não existir
        os.makedirs(destino_pasta, exist_ok=True)
        
        # Nome do arquivo limpo
        nome_limpo = limpar_nome(Path(arquivo).stem)
        ext = Path(arquivo).suffix.lower()
        novo_nome = f"{opcode}_{freq}_{nome_limpo}_{arquetype}{ext}"
        destino_path = os.path.join(destino_pasta, novo_nome)
        
        try:
            # Mover arquivo (não copiar)
            shutil.move(origem_path, destino_path)
            
            # Registrar no catálogo
            entrada = {
                "nome": novo_nome,
                "opcode": opcode,
                "frequencia": freq,
                "arquétipo": arquetype,
                "tipo": tipo,
                "caminho": destino_path,
                "tamanho_bytes": os.path.getsize(destino_path),
                "data_processamento": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            catalogo["midias"].append(entrada)
            catalogo["total_midias"] += 1
            
            # Atualizar contadores
            catalogo["por_tipo"][tipo] = catalogo["por_tipo"].get(tipo, 0) + 1
            catalogo["por_opcode"][opcode] = catalogo["por_opcode"].get(opcode, 0) + 1
            catalogo["por_arquétipo"][arquetype] = catalogo["por_arquétipo"].get(arquetype, 0) + 1
            
            print(f"  ✅ {arquivo[:30]}... → {destino_pasta[-20:]}/{novo_nome[:20]}...")
            count += 1
            
            # Registrar log
            registrar_operacao(f"RENOMEADO|{arquivo}→{novo_nome}|{arquetype}|{tipo}")
            
        except Exception as e:
            print(f"  ❌ Erro em {arquivo}: {e}")
            erros.append(arquivo)
    
    # 5. Salvar catálogo atualizado
    salvar_catalogo(catalogo)
    
    # 6. Mostrar resultados
    print(f"\n✨ {count} arquivos processados com sucesso!")
    if erros:
        print(f"⚠️  {len(erros)} arquivos com erro: {', '.join(erros[:3])}...")
    
    print(f"\n📊 CATÁLOGO ATUALIZADO:")
    print(f"   📁 Local: {METADATA_PATH}/catalogo_geral.json")
    print(f"   🧿 Total de mídias: {catalogo['total_midias']}")
    print(f"   🎬 Vídeos: {catalogo['por_tipo'].get('video', 0)}")
    print(f"   🎵 Áudios: {catalogo['por_tipo'].get('audio', 0)}")
    print(f"   📱 Apps: {catalogo['por_tipo'].get('app', 0)}")
    
    print("\n🕊️  EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO. AMÉМ.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Operação interrompida")
    except Exception as e:
        print(f"\n❌ Erro: {e}")
        import traceback
        traceback.print_exc()
