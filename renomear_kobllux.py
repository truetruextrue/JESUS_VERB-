#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX · RENOMEAÇÃO COM TEMPLATE FRACTAL
Uso: python renomear_kobllux.py [--prefixo PREFIXO] [--nome NOME] [--veeb VEEB]
                                 [--drung DRUNG] [--inicio INICIO] [--ext EXT]
Exemplo: python renomear_kobllux.py --prefixo apoone --nome nome --veeb V.E.EB --drung D.rung --inicio 210 --ext png
"""

import os
import argparse
import glob

def renomear_arquivos(diretorio=".", prefixo="apoone", nome="neme", veeb="V.E.EB",
                      drung="D.rung", inicio=210, extensao="png", simulacao=False):
    """
    Renomeia arquivos para o padrão:
    {prefixo}_{nome}_{veeb}_{drung}_{numero:03d}.{extensao}
    """
    # Busca arquivos com a extensão (case-insensitive)
    padrao = os.path.join(diretorio, f"*.{extensao}")
    arquivos = glob.glob(padrao) + glob.glob(padrao.upper()) + glob.glob(padrao.lower())
    arquivos = sorted(list(set(arquivos)))  # Remove duplicatas e ordena

    if not arquivos:
        print(f"❌ Nenhum arquivo .{extensao} encontrado em {diretorio}")
        return

    print(f"📂 Encontrados {len(arquivos)} arquivo(s).")
    if simulacao:
        print("🔍 MODO SIMULAÇÃO — Nenhum arquivo será modificado.\n")

    contador = inicio
    for caminho_antigo in arquivos:
        _, ext = os.path.splitext(caminho_antigo)
        novo_nome = f"{prefixo}_{nome}_{veeb}_{drung}_{contador:03d}{ext}"
        caminho_novo = os.path.join(diretorio, novo_nome)

        if os.path.exists(caminho_novo) and not simulacao:
            print(f"⚠️  {caminho_novo} já existe. Pulando {os.path.basename(caminho_antigo)}")
            continue

        print(f"🔄 {os.path.basename(caminho_antigo)} → {novo_nome}")
        if not simulacao:
            os.rename(caminho_antigo, caminho_novo)
        contador += 1

    print(f"\n✅ Processo concluído. {contador - inicio} arquivo(s) {'simulados' if simulacao else 'renomeados'}.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Renomeia arquivos usando um template KOBLLUX.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="""
Exemplos:
  python renomear_kobllux.py --prefixo apoone --nome nome --veeb V.E.EB --drung D.rung --inicio 210 --ext png
  python renomear_kobllux.py --simulacao  # apenas para ver o que será feito
        """
    )
    parser.add_argument("--prefixo", default="apoone", help="Primeira parte do nome (padrão: apoone)")
    parser.add_argument("--nome", default="neme", help="Segunda parte do nome (padrão: neme)")
    parser.add_argument("--veeb", default="V.E.EB", help="Terceira parte do nome (padrão: V.E.EB)")
    parser.add_argument("--drung", default="D.rung", help="Quarta parte do nome (padrão: D.rung)")
    parser.add_argument("--inicio", type=int, default=210, help="Número inicial do contador (padrão: 210)")
    parser.add_argument("--ext", default="png", help="Extensão dos arquivos (padrão: png)")
    parser.add_argument("--simulacao", action="store_true", help="Apenas simula, sem renomear")
    args = parser.parse_args()

    renomear_arquivos(
        prefixo=args.prefixo,
        nome=args.nome,
        veeb=args.veeb,
        drung=args.drung,
        inicio=args.inicio,
        extensao=args.ext,
        simulacao=args.simulacao
    )