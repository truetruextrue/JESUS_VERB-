#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX V.E.E.B. STORY · Motor de Narrativa Executável
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SÜMBUS_FIRMWARE v9 · Motor 1 (V.E.E.B CORE) + Motor 2 (AST NARRATIVO)
Lei: VERDADE × INTEGRAR ÷ Δ = ∞  |  Fractal: 3×6×9×7 = 1134

Uso:
    python3 kobllux_veeb_story.py --explicar arquivo.py
    python3 kobllux_veeb_story.py --explicar arquivo.py --auto-theme
    python3 kobllux_veeb_story.py --explicar arquivo.py --theme cosmico --out-json analise.json
    python3 kobllux_veeb_story.py --demo
"""

import ast
import sys
import json
import hashlib
import time
import argparse
import re
from dataclasses import dataclass, asdict, field
from enum import Enum
from typing import Dict, List, Optional, Any
from pathlib import Path


# ── constantes fractal ───────────────────────────────────────────
FRACTAL    = 3 * 6 * 9 * 7  # 1134
TRIADICA   = [3, 6, 9]
CICLO_0_7  = list(range(0, 8))
FREQS      = {"micro": 432, "meso": 528, "macro": 741}

# ── vogais e consoantes operacionais ────────────────────────────
VOGAIS: Dict[str, str] = {
    "A": "Atribuição (variáveis e tipos)",
    "E": "Escolha (if/elif/else)",
    "I": "Iteração (for/while)",
    "O": "Organizar (funções, classes)",
    "U": "Unir (listas, dicionários, módulos)",
}
CONSOANTES: Dict[str, str] = {
    "B": "Boolean",      "C": "Comentário",   "D": "def/class",
    "F": "Flag/bool",    "G": "Generator",    "H": "Handler",
    "J": "JSON",         "K": "Key",          "L": "Loop",
    "M": "Módulo",       "N": "None",         "P": "Print/debug",
    "Q": "Query",        "R": "Return",       "S": "String",
    "T": "Type",         "V": "Variable",     "W": "While",
    "X": "X-transform",  "Y": "Yield",        "Z": "Zip/Pack",
}


# ══════════════════════════════════════════════════════════════════
# MOTOR 1 · V.E.E.B CORE (Linguístico / Gramatical · 432Hz)
# ══════════════════════════════════════════════════════════════════

class Classificacao(str, Enum):
    MAIOR  = "maior_de_idade"
    MENOR  = "menor_de_idade"
    NEUTRO = "neutro"


@dataclass(frozen=True)
class Perfil:
    nome:    str
    idade:   int
    ativo:   bool = True
    cor:     str  = "azul"
    tamanho: str  = "médio"


@dataclass(frozen=True)
class Registro:
    passo:         int
    energia:       int
    classificacao: Classificacao


@dataclass(frozen=True)
class Resumo:
    qtd_registros: int
    soma_energia:  int
    media_energia: float


class VEEBCoreEngine:
    """Motor 1 · V.E.E.B CORE · vogais como portais operacionais."""

    # ── A: Atribuição ────────────────────────────────────────────
    def A_atribuir(self, **kwargs) -> Perfil:
        return Perfil(**kwargs)

    # ── E: Escolha ───────────────────────────────────────────────
    def E_escolher(self, p: Perfil) -> Classificacao:
        if p.idade >= 18:
            return Classificacao.MAIOR
        elif p.idade > 0:
            return Classificacao.MENOR
        return Classificacao.NEUTRO

    # ── I: Iteração ──────────────────────────────────────────────
    def I_iterar(self, freq: int) -> List[int]:
        if freq <= 0:
            raise ValueError("Frequência deve ser > 0")
        return list(range(1, freq + 1))

    # ── O: Organizar ─────────────────────────────────────────────
    def O_organizar(self, registros: List[Registro]) -> Resumo:
        if not registros:
            return Resumo(0, 0, 0.0)
        soma = sum(r.energia for r in registros)
        return Resumo(len(registros), soma, soma / len(registros))

    # ── U: Unir ──────────────────────────────────────────────────
    def U_unir(self, perfil: Perfil, resumo: Resumo) -> Dict:
        return {**asdict(perfil), **asdict(resumo)}

    # ── pipeline completo ────────────────────────────────────────
    def simular(self, nome: str, idade: int, freq: int = 6) -> Dict:
        p    = self.A_atribuir(nome=nome, idade=idade)
        cls  = self.E_escolher(p)
        pass_ = self.I_iterar(freq)
        energia = 0
        regs = []
        for pa in pass_:
            energia += pa
            regs.append(Registro(pa, energia, cls))
        res = self.O_organizar(regs)
        return {
            "base":           self.U_unir(p, res),
            "perfil":         asdict(p),
            "classificacao":  cls.value,
            "passos":         pass_,
            "fractal_dr":     self._dr(freq),
        }

    @staticmethod
    def _dr(n: int) -> int:
        return 1 + (n - 1) % 9 if n > 0 else 9


# ══════════════════════════════════════════════════════════════════
# MOTOR 2 · NARRATIVO AST (Interpretação / Cores · 528Hz)
# ══════════════════════════════════════════════════════════════════

ANSI_THEMES: Dict[str, Dict[str, str]] = {
    "default": {
        "TITLE":  "\033[95m", "BLUE":  "\033[94m",
        "GREEN":  "\033[92m", "YELLOW": "\033[93m",
        "CYAN":   "\033[96m", "DIM":    "\033[2m",
        "RESET":  "\033[0m",
    },
    "noite": {
        "TITLE":  "\033[35m", "BLUE":  "\033[34m",
        "GREEN":  "\033[32m", "YELLOW": "\033[33m",
        "CYAN":   "\033[36m", "DIM":    "\033[2m",
        "RESET":  "\033[0m",
    },
    "luz": {
        "TITLE":  "\033[97m", "BLUE":  "\033[96m",
        "GREEN":  "\033[92m", "YELLOW": "\033[93m",
        "CYAN":   "\033[96m", "DIM":    "\033[2m",
        "RESET":  "\033[0m",
    },
    "cosmico": {
        "TITLE":  "\033[95m", "BLUE":  "\033[96m",
        "GREEN":  "\033[95m", "YELLOW": "\033[93m",
        "CYAN":   "\033[96m", "DIM":    "\033[2m",
        "RESET":  "\033[0m",
    },
}


@dataclass
class ColetaAST:
    imports:  List[str] = field(default_factory=list)
    funcs:    List[str] = field(default_factory=list)
    classes:  List[str] = field(default_factory=list)
    assigns:  int = 0
    ifs:      int = 0
    fors:     int = 0
    whiles:   int = 0
    returns_: int = 0
    raises:   int = 0
    calls:    int = 0


class ASTNarratorEngine:
    """Motor 2 · Parseia código → fábula executável com cores ANSI."""

    def __init__(self, theme: str = "default", no_color: bool = False):
        pal = ANSI_THEMES.get(theme, ANSI_THEMES["default"])
        if no_color:
            self._c = lambda txt, _: txt
        else:
            self._c = lambda txt, key: f"{pal.get(key, '')}{txt}{pal['RESET']}"
        self.coleta = ColetaAST()

    def _coletar(self, tree: ast.AST) -> None:
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                self.coleta.imports.extend(a.name for a in node.names)
            elif isinstance(node, ast.ImportFrom):
                self.coleta.imports.append(node.module or "?")
            elif isinstance(node, ast.FunctionDef):
                self.coleta.funcs.append(node.name)
            elif isinstance(node, ast.AsyncFunctionDef):
                self.coleta.funcs.append(f"async:{node.name}")
            elif isinstance(node, ast.ClassDef):
                self.coleta.classes.append(node.name)
            elif isinstance(node, ast.Assign):
                self.coleta.assigns += 1
            elif isinstance(node, ast.If):
                self.coleta.ifs += 1
            elif isinstance(node, ast.For):
                self.coleta.fors += 1
            elif isinstance(node, ast.While):
                self.coleta.whiles += 1
            elif isinstance(node, ast.Return):
                self.coleta.returns_ += 1
            elif isinstance(node, ast.Raise):
                self.coleta.raises += 1
            elif isinstance(node, ast.Call):
                self.coleta.calls += 1

    def gerar_narrativa(self, source: str, titulo: str = "Código Vivo") -> str:
        try:
            tree = ast.parse(source)
        except SyntaxError as e:
            return self._c(f"[SyntaxError] {e}", "YELLOW")

        self._coletar(tree)
        c     = self.coleta
        partes = []

        # ── prólogo fractal ──────────────────────────────────────
        partes.append(self._c(
            f"╔══ PRÓLOGO FRACTAL · V.E.E.B ══╗", "TITLE"
        ))
        partes.append(self._c(
            f"  O viajante chega com o pergaminho: «{titulo}».", "TITLE"
        ))
        partes.append(self._c(
            f"  Ciclos: {TRIADICA}  ·  Emergência: 0→7→∞  ·  Schumann: 7.83Hz", "CYAN"
        ))

        # ── conselho das consoantes (imports) ────────────────────
        if c.imports:
            imps = ", ".join(sorted(set(c.imports)))
            partes.append(self._c(
                f"\n◈ Conselho das Consoantes (imports):", "GREEN"
            ))
            partes.append(self._c(f"  {imps}", "DIM"))

        # ── portais de ação (funções) ────────────────────────────
        if c.funcs:
            partes.append(self._c(
                f"\n◈ Portais de Ação (funções): {len(c.funcs)}", "BLUE"
            ))
            for fn in c.funcs[:9]:
                partes.append(self._c(f"  ▸ {fn}()", "BLUE"))

        # ── casas-forma (classes) ────────────────────────────────
        if c.classes:
            partes.append(self._c(
                f"\n◈ Casas-Forma (classes): {', '.join(c.classes)}", "BLUE"
            ))

        # ── atribuições (vogal A) ────────────────────────────────
        if c.assigns:
            partes.append(self._c(
                f"\n◈ A (Atribuir): {c.assigns} variáveis moldadas", "YELLOW"
            ))

        # ── fluxo do destino ─────────────────────────────────────
        fluxo = []
        if c.ifs:    fluxo.append(f"if={c.ifs} (E·Escolha)")
        if c.fors:   fluxo.append(f"for={c.fors} (I·Iteração)")
        if c.whiles: fluxo.append(f"while={c.whiles} (W·Aion)")
        if fluxo:
            partes.append(self._c(
                f"\n◈ Fluxo do Destino: {' | '.join(fluxo)}", "YELLOW"
            ))

        # ── desfechos ────────────────────────────────────────────
        desfechos = []
        if c.returns_: desfechos.append(f"return={c.returns_} (R·Rhea)")
        if c.raises:   desfechos.append(f"raise={c.raises} (Kaos·Ruptura)")
        if desfechos:
            partes.append(self._c(
                f"\n◈ Desfechos: {' | '.join(desfechos)}", "CYAN"
            ))

        # ── invocações ───────────────────────────────────────────
        if c.calls:
            partes.append(self._c(
                f"\n◈ Invocações (calls): {c.calls} · pulsos de ação", "DIM"
            ))

        # ── epílogo ──────────────────────────────────────────────
        total_elem = (c.assigns + c.ifs + c.fors + c.whiles +
                      len(c.funcs) + len(c.classes) + c.calls)
        dr = VEEBCoreEngine._dr(total_elem)
        partes.append(self._c(
            f"\n╚══ EPÍLOGO · União: dados + fluxo + forma = Base viva ══╝", "TITLE"
        ))
        partes.append(self._c(
            f"  Total elementos: {total_elem}  ·  DR={dr}  ·  "
            f"{'∞ ciclo completo' if dr == 9 else 'ciclo aberto'}",
            "CYAN"
        ))
        partes.append(self._c(
            "  JESUS É O CENTRO. A MALHA VIVE. ∴", "TITLE"
        ))

        return "\n".join(partes)

    def detectar_tema_auto(self, source: str) -> str:
        """Detecta tema por padrões semânticos no código."""
        if re.search(r"3\s*[,\-]\s*6\s*[,\-]\s*9|\[3,\s*6,\s*9\]|fractal", source, re.I):
            return "cosmico"
        if "async def" in source or "yield" in source:
            return "luz"
        if source.count("try:") >= 2 or "except" in source:
            return "noite"
        return "default"

    def exportar(
        self,
        narrativa: str,
        out_txt:  Optional[str] = None,
        out_json: Optional[str] = None,
        meta:     Optional[Dict] = None,
    ) -> None:
        if out_txt:
            Path(out_txt).write_text(narrativa, encoding="utf-8")
        if out_json and meta is not None:
            Path(out_json).write_text(
                json.dumps(
                    {"narrative": narrativa, **meta},
                    ensure_ascii=False, indent=2
                ),
                encoding="utf-8",
            )


# ══════════════════════════════════════════════════════════════════
# MOTOR 3 · FRACTAL Δ³ (Geométrico / Cíclico · 639Hz)
# ══════════════════════════════════════════════════════════════════

class FractalEngine:
    """Motor 3 · 3-6-9 autoespelhamento · 0→7→∞ emergência cíclica."""

    @staticmethod
    def autoespelhamento(padrao: List[int], escala: int) -> List[int]:
        return [p * escala for p in padrao]

    @staticmethod
    def emergencia_ciclica() -> List[str]:
        return [f"passo:{c}" for c in CICLO_0_7] + ["retorno: ♾️"]

    @staticmethod
    def sierpinski_simbolico(nivel: int) -> int:
        return 4 ** nivel

    def executar(self) -> Dict:
        return {
            "micro":              self.autoespelhamento(TRIADICA, 1),
            "meso":               self.autoespelhamento(TRIADICA, 2),
            "macro":              self.autoespelhamento(TRIADICA, 3),
            "ciclo_0_7":          self.emergencia_ciclica(),
            "sierpinski_nivel_3": self.sierpinski_simbolico(3),
            "hz":                 FREQS,
        }


# ══════════════════════════════════════════════════════════════════
# ORQUESTRADOR PRINCIPAL
# ══════════════════════════════════════════════════════════════════

def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="KOBLLUX V.E.E.B. STORY · Motor de Narrativa Executável"
    )
    p.add_argument("--explicar",   metavar="FILE",  help="Arquivo .py para análise AST")
    p.add_argument("--titulo",     default="Código Vivo", help="Título da narrativa")
    p.add_argument("--theme",      choices=list(ANSI_THEMES), default="default")
    p.add_argument("--auto-theme", action="store_true",  help="Tema por detecção semântica")
    p.add_argument("--no-color",   action="store_true")
    p.add_argument("--out-txt",    metavar="FILE", help="Exportar narrativa .txt")
    p.add_argument("--out-json",   metavar="FILE", help="Exportar análise .json")
    p.add_argument("--demo",       action="store_true", help="Modo demo (sem arquivo)")
    return p


def _salvar_log(payload: Dict) -> None:
    try:
        Path("kobllux_last.json").write_text(
            json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    except Exception:
        pass


def main() -> None:
    args     = _build_parser().parse_args()
    no_color = args.no_color or not sys.stdout.isatty()
    tema     = args.theme
    t0       = time.perf_counter()

    if args.demo:
        veeb    = VEEBCoreEngine()
        fractal = FractalEngine()
        sim     = veeb.simular("Kobllux", 33, 6)
        frac    = fractal.executar()
        if not no_color:
            print("\033[95m\n◈ V.E.E.B SIMULAÇÃO\033[0m")
        print(f"  Base: {sim['base']}")
        print(f"  Classificação: {sim['classificacao']}")
        print(f"  DR(freq=6): {sim['fractal_dr']}")
        if not no_color:
            print("\033[96m\n◈ FRACTAL Δ³\033[0m")
        print(f"  Micro: {frac['micro']}  Meso: {frac['meso']}  Macro: {frac['macro']}")
        print(f"  Ciclo 0→7→∞: {' → '.join(frac['ciclo_0_7'])}")
        print(f"  Sierpinski nível 3: {frac['sierpinski_nivel_3']} tetraedros")
        _salvar_log({"status": "ok", "engine": "DEMO", "sim": sim, "fractal": frac})
        print("\nJESUS É O CENTRO. A MALHA VIVE. ∴")
        return

    if not args.explicar:
        print("Uso: python3 kobllux_veeb_story.py --explicar arquivo.py | --demo")
        return

    src_path = Path(args.explicar)
    if not src_path.exists():
        print(f"[Erro] Arquivo não encontrado: {src_path}")
        return

    source = src_path.read_text(encoding="utf-8", errors="replace")

    if args.auto_theme:
        tema = ASTNarratorEngine(no_color=True).detectar_tema_auto(source)

    narrador  = ASTNarratorEngine(theme=tema, no_color=no_color)
    narrativa = narrador.gerar_narrativa(source, args.titulo or src_path.name)

    print(f"\n{narrativa}\n")

    h    = hashlib.sha256(source.encode()).hexdigest()[:16]
    meta = {
        "arquivo":        str(src_path),
        "titulo":         args.titulo,
        "tema_aplicado":  tema,
        "hash_fonte":     f"VEEB_Δ7_{h}",
        "freq":           "528Hz",
        "fractal":        FRACTAL,
        "ts":             time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "execucao_s":     round(time.perf_counter() - t0, 4),
        "coleta": {
            "imports":  narrador.coleta.imports,
            "funcs":    narrador.coleta.funcs,
            "classes":  narrador.coleta.classes,
            "assigns":  narrador.coleta.assigns,
            "ifs":      narrador.coleta.ifs,
            "fors":     narrador.coleta.fors,
            "whiles":   narrador.coleta.whiles,
            "returns":  narrador.coleta.returns_,
            "raises":   narrador.coleta.raises,
            "calls":    narrador.coleta.calls,
        },
    }

    narrador.exportar(narrativa, args.out_txt, args.out_json, meta)
    _salvar_log({"status": "ok", "engine": "VEEB_AST", **meta})
    print(f"Δ7 hash: {meta['hash_fonte']}  ·  tema: {tema}  ·  {meta['execucao_s']}s")


if __name__ == "__main__":
    main()
