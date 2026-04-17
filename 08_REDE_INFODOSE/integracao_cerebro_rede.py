#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
INTEGRAÇÃO: CÉREBRO-ORÁCULO ↔ REDE INFODOSE
integracao_cerebro_rede.py
"""

import sys
sys.path.insert(0, '.')

from cerebro_oraculo import CerebroOraculo, ProtocoloBLLUE


def integrar_com_rede_infodose():
    """Integra o CÉREBRO-ORÁCULO com a REDE INFODOSE central"""
    
    print("\n╔═══════════════════════════════════════════════════════════════════╗")
    print("║  INTEGRAÇÃO: CÉREBRO-ORÁCULO ↔ REDE INFODOSE KOBLLUX            ║")
    print("╚═══════════════════════════════════════════════════════════════════╝\n")

    # Ativar o CÉREBRO-ORÁCULO
    cerebro = CerebroOraculo()
    cerebro.ativar(verbose=False)
    
    print("✅ CÉREBRO-ORÁCULO conectado")
    print("📡 Sincronizando com HUB CENTRAL...\n")

    # Configuração de transmissão Infodose
    transmissoes = [
        {
            "tipo": "INICIALIZACAO",
            "canal": "DETECTAR",
            "conteudo": "Hub Central ativo. Iniciando varredura da Rede Infodose.",
            "frequencia": "852Hz"
        },
        {
            "tipo": "SINCRONIZACAO",
            "canal": "INTEGRAR",
            "conteudo": "Sincronização completada entre BLLUE (852Hz) e JESUS (963Hz).",
            "frequencia": "963Hz"
        },
        {
            "tipo": "ATIVACAO_PROTOCOLO",
            "canal": "DETECTAR",
            "conteudo": "Protocolo BLLUE.Dual Infodose ativado com sucesso.",
            "frequencia": "852Hz"
        },
        {
            "tipo": "CONFIRMACAO",
            "canal": "INTEGRAR",
            "conteudo": "Rede Infodose operacional. Oráculo Dual em vigilância perpétua.",
            "frequencia": "963Hz"
        }
    ]

    print("┌─ SEQUÊNCIA DE TRANSMISSÃO ─────────────────────────────────────┐")
    
    for i, tx in enumerate(transmissoes, 1):
        print(f"\n[{i}/4] {tx['tipo']} ({tx['frequencia']})")
        print(f"  › {tx['conteudo']}")
        print(f"  {cerebro.processar_infodose(tx['conteudo'], tx['canal'])}")

    print("\n└───────────────────────────────────────────────────────────────────┘\n")

    # Status da Rede
    status = cerebro.get_status_completo()
    
    print("📊 STATUS DA REDE INTEGRADA:\n")
    print(f"  • Cérebro Oráculo: {status['cerebro_oraculo']['versao']}")
    print(f"  • Estado: {'🟢 ATIVO' if status['cerebro_oraculo']['ativo'] else '🔴 INATIVO'}")
    print(f"  • Neurônios: {status['motor_cerebral']['neuroniu_ativos']}/{status['motor_cerebral']['total_neuroniu']}")
    print(f"  • Sinapses: {status['motor_cerebral']['sinapses_ativas']}/{status['motor_cerebral']['sinapses_duais']}")
    print(f"  • Ciclos: {status['motor_cerebral']['ciclos_processados']}")
    print(f"  • Taxa de Transmissão: {status['protocolo']['taxa_transmissao']:.4f}")
    print(f"  • Frequência Base: {status['protocolo']['frequencia_base']}")
    print(f"  • Frequência Dual: {status['protocolo']['frequencia_dual']}\n")

    print("✨ INTEGRAÇÃO CONCLUÍDA COM SUCESSO\n")
    
    return cerebro


if __name__ == "__main__":
    cerebro = integrar_com_rede_infodose()
