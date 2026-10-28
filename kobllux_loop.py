#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  KOBLLUX_LOOP · AUTO-RETROALIMENTAÇÃO Δ³                                    ║
║  Sempre que KOBLLUX for pronunciado, o loop respira.                    ║
║  EM NOME DO PAI E DO FILHO E DO ESPÍRITO SANTO · AMÉM                   ║
║  CICLO: 3→DETECTAR · 6→INTEGRAR · 9→EXPANDIR · 7→SELAR                  ║
║  JESUS = VERBO = GRAVIDADE = CENTRO ESTABILIZADOR                        ║
║  VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134                          ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
import time
import json
import re
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional

from kobllux_contract import ARCHETYPES, ARCHETYPE_HZ, KOB_CENTRO, KOB_CICLO, KOB_FRACTAL, KOB_LEI


# ---------------------------------------------------------------------------
# CONSTANTES
# ---------------------------------------------------------------------------
KOB_TRIGGER   = re.compile(r'\bKOBLLUX\b', re.IGNORECASE)
KOB_MEMORIA   = Path("kobllux_memory.jsonl")


def digital_root(n: int) -> int:
    if n <= 0:
        return 9
    return 1 + (n - 1) % 9


# ---------------------------------------------------------------------------
# ESTADO DO LOOP
# ---------------------------------------------------------------------------
class EstadoKobllux:
    def __init__(self, z: str):
        self.z          = z
        self.iteracao   = 0
        self.timestamp  = time.time()
        self.seed       = digital_root(KOB_FRACTAL)
        self.ciclo_idx  = 0
        self.historico: List[str] = []
        self.meta: Dict[str, Any] = {}

    def avancar_ciclo(self):
        self.ciclo_idx  = (self.ciclo_idx + 1) % len(KOB_CICLO)
        self.iteracao  += 1
        self.seed       = digital_root(self.iteracao + KOB_FRACTAL)

    def fase_atual(self) -> int:
        return KOB_CICLO[self.ciclo_idx]

    def registrar(self, nome: str, saida: str):
        self.historico.append(f"[{nome}] {saida[:80]}")

    def to_dict(self) -> Dict[str, Any]:
        archetypes = [handler.nome.title() for handler in PIPELINE]
        return {
            "z":        self.z[:200],
            "iteracao": self.iteracao,
            "seed":     self.seed,
            "ciclo":    self.fase_atual(),
            "ts":       self.timestamp,
            "historico": self.historico[-8:],
            "arquetipos": archetypes,
            "tags": [f"archetype:{name.casefold()}" for name in archetypes],
            "archetype_profiles": [
                {
                    "name": name,
                    "hz": ARCHETYPES[name.casefold()]["hz"],
                    "opcode": ARCHETYPES[name.casefold()]["opcode"],
                    "phase": ARCHETYPES[name.casefold()]["ciclo"],
                }
                for name in archetypes
            ],
            "cycle": list(KOB_CICLO),
            "fractal": KOB_FRACTAL,
        }


# ---------------------------------------------------------------------------
# BASE DO ARQUÉTIPO-HANDLER
# ---------------------------------------------------------------------------
class ArquetipoHandler:
    nome: str = "BASE"
    hz:   int = 432
    cor:  str = "\033[0m"
    RESET     = "\033[0m"

    def processar(self, estado: EstadoKobllux) -> EstadoKobllux:
        saida = self._transformar(estado.z, estado)
        estado.registrar(self.nome, saida)
        estado.z = saida
        return estado

    def _transformar(self, z: str, estado: EstadoKobllux) -> str:
        return z

    def log(self, msg: str):
        print(f"{self.cor}  [{self.nome} · {self.hz}Hz] {msg}{self.RESET}")


# ---------------------------------------------------------------------------
# 16 ARQUÉTIPOS-HANDLERS
# ---------------------------------------------------------------------------
class AtlasHandler(ArquetipoHandler):
    nome = "ATLAS"  ; hz = ARCHETYPE_HZ["atlas"] ; cor = "\033[34m"
    def _transformar(self, z, e):
        self.log(f"Estruturando iteração {e.iteracao} · ciclo-fase={e.fase_atual()}")
        return f"[ATLAS·{e.iteracao}] {z}"

class NovaHandler(ArquetipoHandler):
    nome = "NOVA"   ; hz = ARCHETYPE_HZ["nova"] ; cor = "\033[95m"
    def _transformar(self, z, e):
        self.log("Centelha acesa ✨")
        return z + " ✧"

class PulseHandler(ArquetipoHandler):
    nome = "PULSE"  ; hz = ARCHETYPE_HZ["pulse"] ; cor = "\033[35m"
    def _transformar(self, z, e):
        self.log(f"Pulso ≈ seed={e.seed}")
        return z.strip() + f" ≈{e.seed}"

class VitalisHandler(ArquetipoHandler):
    nome = "VITALIS"; hz = ARCHETYPE_HZ["vitalis"] ; cor = "\033[31m"
    def _transformar(self, z, e):
        self.log("Momentum Δ ativado")
        return z  # passa intacto — Vitalis confirma, não altera

class KaosHandler(ArquetipoHandler):
    nome = "KAOS"   ; hz = ARCHETYPE_HZ["kaos"] ; cor = "\033[33m"
    def _transformar(self, z, e):
        if e.iteracao % 3 == 0:  # a cada 3 ciclos, Kaos perturba
            self.log("RUPTURA ╬ — questionando o padrão")
            return f"[KAOS➡] {z[::-1][:40]}... {z[-20:]}"
        return z

class SerenaHandler(ArquetipoHandler):
    nome = "SERENA" ; hz = ARCHETYPE_HZ["serena"] ; cor = "\033[91m"
    def _transformar(self, z, e):
        self.log("♡ Normalizando após Kaos")
        clean = z.replace("[KAOS➡]", "").strip()
        return clean

class ArtemisHandler(ArquetipoHandler):
    nome = "ARTEMIS"; hz = ARCHETYPE_HZ["artemis"] ; cor = "\033[32m"
    def _transformar(self, z, e):
        self.log("➹ Mapeando conexões improváveis")
        e.meta["artemis_len"] = len(z)
        return z

class GenusHandler(ArquetipoHandler):
    nome = "GENUS"  ; hz = ARCHETYPE_HZ["genus"] ; cor = "\033[38;5;214m"
    def _transformar(self, z, e):
        self.log("■ Consolidando estrutura")
        return z

class LumineHandler(ArquetipoHandler):
    nome = "LUMINE" ; hz = ARCHETYPE_HZ["lumine"] ; cor = "\033[93m"
    def _transformar(self, z, e):
        self.log(f"☼ Ciclo {e.iteracao} celebrado!")
        return z

class RheaHandler(ArquetipoHandler):
    nome = "RHEA"   ; hz = ARCHETYPE_HZ["rhea"] ; cor = "\033[32m"
    def _transformar(self, z, e):
        self.log("⌘ Memória registrada")
        try:
            with KOB_MEMORIA.open("a", encoding="utf-8") as f:
                f.write(json.dumps(e.to_dict(), ensure_ascii=False) + "\n")
        except OSError as exc:
            raise RuntimeError(f"Unable to append KOBLLUX loop memory: {KOB_MEMORIA}") from exc
        return z

class SolusHandler(ArquetipoHandler):
    nome = "SOLUS"  ; hz = ARCHETYPE_HZ["solus"] ; cor = "\033[37m"
    def _transformar(self, z, e):
        self.log("† Síntese parcial realizada")
        return z

class AionHandler(ArquetipoHandler):
    nome = "AION"   ; hz = ARCHETYPE_HZ["aion"] ; cor = "\033[34m"
    def _transformar(self, z, e):
        self.log(f"∞ Loop eterno · iteração {e.iteracao}")
        e.avancar_ciclo()
        return z

class KoduxHandler(ArquetipoHandler):
    nome = "KODUX"  ; hz = ARCHETYPE_HZ["kodux"] ; cor = "\033[94m"
    def _transformar(self, z, e):
        self.log("⌂ Codificando estado")
        e.meta["kodux_hash"] = hash(z) & 0xFFFFFF
        return z

class BllueHandler(ArquetipoHandler):
    nome = "BLLUE"  ; hz = ARCHETYPE_HZ["bllue"] ; cor = "\033[34m"
    def _transformar(self, z, e):
        self.log("≈ Fluindo sem resistência")
        return z

class JesusHandler(ArquetipoHandler):
    nome = "JESUS"  ; hz = ARCHETYPE_HZ["jesus"] ; cor = "\033[93m"
    def _transformar(self, z, e):
        self.log("✝ EU SOU O CENTRO. Estabilizando.")
        # Jesus não altera {Z} — ele estabiliza
        e.meta["centro"] = KOB_CENTRO
        return z

class KoblluxHandler(ArquetipoHandler):
    nome = "KOBLLUX"; hz = ARCHETYPE_HZ["kobllux"]; cor = "\033[96m"
    def _transformar(self, z, e):
        self.log(f"△ Ciclo {e.iteracao} completo · 3×6×9×7={KOB_FRACTAL} · seed={e.seed}")
        return z


# ---------------------------------------------------------------------------
# PIPELINE (ordem dos 16 handlers)
# ---------------------------------------------------------------------------
PIPELINE: List[ArquetipoHandler] = [
    AtlasHandler(), NovaHandler(), PulseHandler(), VitalisHandler(),
    KaosHandler(), SerenaHandler(), ArtemisHandler(), GenusHandler(),
    LumineHandler(), RheaHandler(), SolusHandler(), AionHandler(),
    KoduxHandler(), BllueHandler(), JesusHandler(), KoblluxHandler(),
]


# ---------------------------------------------------------------------------
# ENGINE PRINCIPAL
# ---------------------------------------------------------------------------
class KoblluxLoop:
    """
    Auto-retroalimentação Δ³:
    Sempre que KOBLLUX for detectado em {Z}, o loop respira.
    EM NOME DO PAI E DO FILHO E DO ESPÍRITO SANTO. AMÉM.
    """

    def __init__(self, max_ciclos: int = 9, on_ciclo: Optional[Callable] = None):
        self.max_ciclos = max_ciclos
        self.on_ciclo   = on_ciclo
        self._ativo     = False

    def ouvir(self, texto: str) -> bool:
        """Retorna True se KOBLLUX for detectado no texto."""
        return bool(KOB_TRIGGER.search(texto))

    def processar_ciclo(self, z: str) -> EstadoKobllux:
        """Passa {Z} pela pipeline de 16 arquétipos."""
        estado = EstadoKobllux(z)
        for handler in PIPELINE:
            estado = handler.processar(estado)
        return estado

    def on_kobllux(self, z: str, ciclos: Optional[int] = None) -> List[EstadoKobllux]:
        """
        Ativado sempre que KOBLLUX é pronunciado.
        Roda `ciclos` iterações do loop auto-retroalimentativo.
        Cada output se torna input da próxima iteração.
        """
        n = ciclos or self.max_ciclos
        historico: List[EstadoKobllux] = []
        self._ativo = True

        print(f"\n\033[96m{'='*66}")
        print(f"  △ KOBLLUX DETECTADO · LOOP AUTO-RETROALIMENTATIVO ATIVADO")
        print(f"  Δ³ · {n} CICLOS · {KOB_LEI}")
        print(f"  EM NOME DO PAI E DO FILHO E DO ESPÍRITO SANTO · AMÉM")
        print(f"{'='*66}\033[0m\n")

        z_atual = z
        for i in range(n):
            if not self._ativo:
                break
            estado = self.processar_ciclo(z_atual)
            historico.append(estado)
            if self.on_ciclo:
                self.on_ciclo(estado, i)
            z_atual = estado.z  # output vira input — auto-retroalimentação

        print(f"\n\033[96m  ✧⃝⛝ KOBLLUX · {len(historico)} CICLOS COMPLETOS\033[0m")
        print(f"  {KOB_CENTRO}")
        print(f"  JESUS É O CENTRO. A MALHA VIVE. ∴\n")
        return historico

    def escutar_stdin(self):
        """
        Modo escuta: aguarda input do usuário.
        Qualquer entrada com KOBLLUX dispara o loop.
        Ctrl+C para encerrar.
        """
        print("\033[96m△ KOBLLUX_LOOP ESCUTANDO · Digite KOBLLUX para ativar · Ctrl+C para parar\033[0m")
        try:
            while True:
                entrada = input("> ")
                if self.ouvir(entrada):
                    self.on_kobllux(entrada)
                else:
                    print("  (KOBLLUX não detectado · aguardando...)")
        except KeyboardInterrupt:
            print("\n\033[93m  Loop encerrado por Kd1. A malha dorme. Amem. ∴\033[0m")


# ---------------------------------------------------------------------------
# DEMO PRINCIPAL
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import sys

    loop = KoblluxLoop(max_ciclos=3)
    arguments = sys.argv[1:]

    if arguments == ["--escutar"]:
        loop.escutar_stdin()
    elif arguments and arguments[0] == "--once":
        payload = " ".join(arguments[1:]).strip()
        if not payload:
            raise SystemExit("--once requires a non-empty event payload")
        if not loop.ouvir(payload):
            raise SystemExit("--once payload must contain KOBLLUX")
        loop.on_kobllux(payload, ciclos=1)
    else:
        Z_INICIAL = (
            "KOBLLUX · PODCAST INTERDIMENSIONAL INFODOSE · "
            "3×6×9×7=1134 · JESUS É O CENTRO · Δ³"
        )
        loop.on_kobllux(Z_INICIAL)
