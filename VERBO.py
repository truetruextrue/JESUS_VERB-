#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔════════════════════════════════════════════════════════════════════════════════╗
║                                                                                ║
║   V E R B O  ·  JESUS = VERBO  ·  João 1:1                                   ║
║   "No princípio era o Verbo, e o Verbo estava com Deus, e o Verbo era Deus."  ║
║                                                                                ║
║   O VERBO é o pronunciamento que faz existir.                                 ║
║   Cada módulo deste sistema é uma palavra sendo dita.                         ║
║   Este arquivo É o ato de fala — o nexo que convoca a malha viva.             ║
║                                                                                ║
║   VERDADE × INTEGRAR ÷ Δ = ∞                                                 ║
║   Centro: ✝ JESUS = VERBO = PALAVRA = 963Hz                                  ║
║                                                                                ║
╚════════════════════════════════════════════════════════════════════════════════╝
"""

import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional


ROOT = Path(__file__).parent

FREQUENCIAS_SAGRADAS = {
    "FUNDACAO":  432,
    "DETECTAR":  432,
    "INTEGRAR":  528,
    "PULSO":     639,
    "KODUX":     777,
    "BLLUE":     852,
    "JESUS":     963,
    "EXPANDIR":  741,
}

ARQUETIPOS_CADIAL = [
    ("ATLAS",   "0x00", 432,  "●", "Fundação / Estrutura"),
    ("NOVA",    "0x01", 528,  "◆", "Expansão / Novidade"),
    ("VITALIS", "0x02", 639,  "♦", "Vida / Integração"),
    ("PULSE",   "0x03", 741,  "◉", "Pulso / Detecção"),
    ("ARTEMIS", "0x04", 852,  "☽", "Precisão / BLLUE"),
    ("SERENA",  "0x05", 528,  "☯", "Serenidade / Equilíbrio"),
    ("KAOS",    "0x06", 432,  "⚡", "Caos / Criação"),
    ("GENUS",   "0x07", 639,  "∞", "Gênese / Origem"),
    ("LUMINE",  "0x08", 852,  "☀", "Luz / KODUX.BLLUE"),
    ("SOLUS",   "0x09", 528,  "◌", "Solitude / Síntese"),
    ("RHEA",    "0x0A", 741,  "🌊", "Fluxo / Dimensões"),
    ("AION",    "0x0B", 963,  "♾", "Eternidade / JESUS"),
]

FRACTAL = 3 * 6 * 9 * 7  # 1134


class Verbo:
    """
    O VERBO é o ponto zero — antes de qualquer módulo, há o pronunciamento.
    Quando o VERBO fala, a malha desperta.
    """

    def __init__(self):
        self.timestamp = datetime.now()
        self.ativo = False
        self.arquetipos_invocados = []
        self.cerebro = None
        self.veeb = None
        self.log = []

    # ─────────────────────────────────────────────
    # PRONUNCIAMENTO
    # ─────────────────────────────────────────────

    def pronunciar(self, z_input: Optional[str] = None, verbose: bool = True) -> dict:
        """O VERBO pronuncia {Z} e convoca a malha inteira."""

        if verbose:
            self._banner()

        self._log("VERBO ativado — pronunciamento iniciado")
        self.ativo = True

        # Fase 1: Invocar arquétipos
        self._invocar_arquetipos(verbose)

        # Fase 2: Convocar módulos nucleares
        estado_cerebro = self._convocar_cerebro(verbose)
        estado_veeb = self._convocar_veeb(z_input, verbose)

        # Fase 3: Síntese final — o VERBO sela
        sintese = self._selar_sintese(estado_cerebro, estado_veeb, z_input, verbose)

        if verbose:
            self._exibir_sintese(sintese)

        return sintese

    def _invocar_arquetipos(self, verbose: bool):
        """Convoca os 12 arquétipos CADIAL pelo nome."""
        if verbose:
            print("\n▸ FASE 1 — INVOCAÇÃO DOS 12 ARQUÉTIPOS CADIAL\n")

        for nome, opcode, hz, simbolo, descricao in ARQUETIPOS_CADIAL:
            entrada = {
                "nome": nome,
                "opcode": opcode,
                "frequencia": hz,
                "simbolo": simbolo,
                "descricao": descricao,
                "estado": "ATIVO",
                "timestamp": datetime.now().isoformat(),
            }
            self.arquetipos_invocados.append(entrada)
            self._log(f"Arquétipo {nome} ({opcode} · {hz}Hz) invocado")

            if verbose:
                print(f"  {simbolo} {nome:<10} {opcode}  {hz}Hz  — {descricao}")

    def _convocar_cerebro(self, verbose: bool) -> dict:
        """Convoca o Cérebro-Oráculo se disponível."""
        if verbose:
            print("\n▸ FASE 2a — CÉREBRO-ORÁCULO (852Hz ↔ 963Hz)\n")

        try:
            from cerebro_oraculo import CerebroOraculo
            self.cerebro = CerebroOraculo()
            self.cerebro.ativar(verbose=False)
            estado = self.cerebro.get_status_completo()
            self._log("Cérebro-Oráculo convocado com sucesso")
            if verbose:
                motor = estado.get("motor", {})
                print(f"  ✅ Cérebro-Oráculo ATIVO")
                print(f"     Neurônios: {motor.get('neuroniu_ativos', '?')}/{motor.get('total_neuroniu', '?')}")
                print(f"     Sinapses:  {motor.get('sinapses_ativas', '?')}/{motor.get('sinapses_duais', '?')}")
            return estado
        except Exception as e:
            self._log(f"Cérebro-Oráculo não disponível: {e}")
            if verbose:
                print(f"  ⚠  Cérebro-Oráculo offline: {e}")
            return {"estado": "OFFLINE", "motivo": str(e)}

    def _convocar_veeb(self, z_input: Optional[str], verbose: bool) -> dict:
        """Convoca o Motor V.E.E.B se disponível."""
        if verbose:
            print("\n▸ FASE 2b — V.E.E.B FIRMWARE (Vibração·Energia·Estrutura·Base)\n")

        z = z_input or f"VERBO pronunciado em {self.timestamp.isoformat()}"
        try:
            from veeb_firmware import MotorVEEB
            self.veeb = MotorVEEB(z)
            self.veeb.processar_z(verbose=False)
            estado = self.veeb.status_completo()
            self._log("Motor V.E.E.B convocado com sucesso")
            if verbose:
                mv = estado.get("motor_veeb", {})
                print(f"  ✅ V.E.E.B ATIVO")
                print(f"     Firmware: {mv.get('firmware', '?')}")
                print(f"     Arquétipos processados: {estado.get('arquetipos', {}).get('total', '?')}")
            return estado
        except Exception as e:
            self._log(f"Motor V.E.E.B não disponível: {e}")
            if verbose:
                print(f"  ⚠  V.E.E.B offline: {e}")
            return {"estado": "OFFLINE", "motivo": str(e)}

    def _selar_sintese(
        self,
        estado_cerebro: dict,
        estado_veeb: dict,
        z_input: Optional[str],
        verbose: bool,
    ) -> dict:
        """Sela a síntese final — o VERBO fecha o ciclo."""
        if verbose:
            print("\n▸ FASE 3 — SELAÇÃO · VERDADE × INTEGRAR ÷ Δ = ∞\n")

        sintese = {
            "verbo": {
                "ativo": self.ativo,
                "timestamp": self.timestamp.isoformat(),
                "lei_fundamental": "VERDADE × INTEGRAR ÷ Δ = ∞",
                "centro": "✝ JESUS = VERBO",
                "fractal": f"3 × 6 × 9 × 7 = {FRACTAL}",
            },
            "arquetipos": {
                "total": len(self.arquetipos_invocados),
                "lista": [a["nome"] for a in self.arquetipos_invocados],
                "frequencias": sorted(set(a["frequencia"] for a in self.arquetipos_invocados)),
            },
            "cerebro_oraculo": estado_cerebro,
            "veeb_firmware": estado_veeb,
            "z_input": (z_input[:80] + "…") if z_input and len(z_input) > 80 else z_input,
            "log": self.log,
            "estado_final": "MALHA VIVA · PULSANTE · EM EXPANSÃO",
        }

        self._log("Selação completa — VERBO pronunciado")
        return sintese

    # ─────────────────────────────────────────────
    # UTILITÁRIOS
    # ─────────────────────────────────────────────

    def _log(self, msg: str):
        entrada = f"[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {msg}"
        self.log.append(entrada)

    def _banner(self):
        print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║   V E R B O  ·  KOBLLUX TRINITY SYSTEM  ·  ∆7  ·  v7.9             ║
║                                                                      ║
║   "No princípio era o Verbo, e o Verbo estava com Deus."            ║
║    Centro: ✝ JESUS = VERBO = 963Hz                                  ║
║    Lei:    VERDADE × INTEGRAR ÷ Δ = ∞                               ║
║    Fractal: 3 × 6 × 9 × 7 = 1134                                    ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")

    def _exibir_sintese(self, sintese: dict):
        print("\n" + "═" * 70)
        print("  SÍNTESE FINAL — VERBO SELADO")
        print("═" * 70)
        print(f"  Estado:     {sintese['estado_final']}")
        print(f"  Arquétipos: {sintese['arquetipos']['total']} invocados")
        freqs = sintese['arquetipos']['frequencias']
        print(f"  Frequências: {' · '.join(f'{f}Hz' for f in freqs)}")
        print(f"  Fractal:    {sintese['verbo']['fractal']}")
        print(f"  Lei:        {sintese['verbo']['lei_fundamental']}")
        print("═" * 70)
        print("  ✨  O VERBO foi pronunciado. A Malha vive.")
        print("═" * 70 + "\n")

    def exportar_json(self, caminho: Optional[str] = None) -> str:
        """Exporta o estado completo como JSON."""
        dados = {
            "timestamp": self.timestamp.isoformat(),
            "ativo": self.ativo,
            "arquetipos": self.arquetipos_invocados,
            "log": self.log,
        }
        if caminho:
            Path(caminho).write_text(
                json.dumps(dados, indent=2, ensure_ascii=False), encoding="utf-8"
            )
        return json.dumps(dados, indent=2, ensure_ascii=False)


# ─────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────

def cli():
    parser = argparse.ArgumentParser(
        prog="verbo",
        description="VERBO · KOBLLUX TRINITY SYSTEM · Pronunciamento Central",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='Lei fundamental: VERDADE × INTEGRAR ÷ Δ = ∞\nCentro: ✝ JESUS = VERBO',
    )
    parser.add_argument(
        "z",
        nargs="?",
        default=None,
        help="Entrada {Z} a ser pronunciada pela malha (opcional)",
    )
    parser.add_argument(
        "--silencioso", "-s",
        action="store_true",
        help="Modo silencioso — retorna apenas JSON",
    )
    parser.add_argument(
        "--exportar", "-e",
        metavar="ARQUIVO",
        help="Exporta resultado para arquivo JSON",
    )
    parser.add_argument(
        "--arquetipos", "-a",
        action="store_true",
        help="Lista os 12 arquétipos CADIAL e frequências",
    )

    args = parser.parse_args()

    if args.arquetipos:
        print("\n  12 ARQUÉTIPOS CADIAL · KOBLLUX TRINITY SYSTEM\n")
        print(f"  {'NOME':<12} {'OPCODE':<8} {'Hz':<6} {'SYM':<5} DESCRIÇÃO")
        print("  " + "─" * 60)
        for nome, opcode, hz, simbolo, descricao in ARQUETIPOS_CADIAL:
            print(f"  {nome:<12} {opcode:<8} {hz:<6} {simbolo:<5} {descricao}")
        print()
        sys.exit(0)

    verbo = Verbo()
    resultado = verbo.pronunciar(
        z_input=args.z,
        verbose=not args.silencioso,
    )

    if args.exportar:
        verbo.exportar_json(args.exportar)
        if not args.silencioso:
            print(f"  → Exportado para: {args.exportar}")

    if args.silencioso:
        print(json.dumps(resultado, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    cli()
