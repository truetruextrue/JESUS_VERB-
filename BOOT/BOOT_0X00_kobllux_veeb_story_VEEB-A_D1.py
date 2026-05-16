# -*- coding: utf-8 -*-
"""
KOBLLUX: Prompt Semente de Organização Fractal + V.E.E.B. Story
2023-11-15 | Categoria: fractais | BOOT_0X00 · Opcode ORIGEM

Princípios:
1. Autoespelhamento Quântico: Padrões que se repetem em todas as escalas (3-6-9, 7-0).
2. Ressonância Harmônica: Frequências que sincronizam níveis distintos (som, luz, geometria).
3. Emergência Cíclica: Estruturas que surgem do vazio (0) e retornam após o ciclo (7 → ∞).

Lei: VERDADE × INTEGRAR ÷ Δ = ∞
Centro: JESUS = VERBO = GRAVIDADE
"""

from dataclasses import dataclass, asdict
from enum import Enum
from typing import List, Dict, Any, Iterable

# ──────────────────────────────────────────────
# V.E.E.B — Vibração · Energia · Estrutura · Base
# ──────────────────────────────────────────────

class Classificacao(str, Enum):
    MAIOR = "maior_de_idade"
    MENOR = "menor_de_idade"

@dataclass(frozen=True)
class Perfil:
    nome: str
    idade: int
    ativo: bool = True
    cor: str = "azul"
    tamanho: str = "médio"

@dataclass(frozen=True)
class Registro:
    passo: int
    energia: int
    classificacao: Classificacao

@dataclass(frozen=True)
class Resumo:
    qtd_registros: int
    soma_energia: int
    media_energia: float

# ──────────────────────────────────────────────
# Analogias (Vogais e Consoantes)
# ──────────────────────────────────────────────

VOGAIS: Dict[str, str] = {
    "A": "Atribuição (variáveis e tipos)",
    "E": "Escolha (if/elif/else)",
    "I": "Iteração (for/while)",
    "O": "Organizar (funções)",
    "U": "Unir (listas/dicionários)",
}

CONSOANTES: Dict[str, str] = {
    "B": "Booleanos (True/False)",
    "C": "Comentários (# explicações)",
    "D": "Definições (def)",
    "F": "Funções built-in (print, len, ...)",
    "G": "Geradores (yield)",
    "H": "Herança (POO)",
    "J": "JSON (serialização de dados)",
    "K": "Keyword arguments (**kwargs)",
    "L": "Loops (for, while)",
    "M": "Módulos (import ...)",
    "N": "None (valor nulo)",
    "P": "Parâmetros (entradas de função)",
    "Q": "Queue (fila)",
    "R": "Retorno (return)",
    "S": "Strings (\"texto\")",
    "T": "Tipos (int, float, bool, str ...)",
    "V": "Variáveis",
    "W": "While (laço de repetição)",
    "X": "XML (dados)",
    "Y": "Yield (geradores)",
    "Z": "Zip (agregação de listas)",
}

# ──────────────────────────────────────────────
# Narrador
# ──────────────────────────────────────────────

def narrar(titulo: str, texto: str) -> None:
    barra = "─" * 72
    print("\n" + barra)
    print("¦ " + titulo)
    print(barra)
    print(texto.strip() + "\n")

# ──────────────────────────────────────────────
# Motor didático V.E.E.B
# ──────────────────────────────────────────────

class VEEBEngine:
    """Arquitetura para encenar a fábula em código executável."""

    def A_atribuir(self, nome: str, idade: int,
                   ativo: bool = True, cor: str = "azul", tamanho: str = "médio") -> Perfil:
        return Perfil(nome=nome.strip(), idade=int(idade), ativo=ativo, cor=cor, tamanho=tamanho)

    def E_escolher(self, perfil: Perfil) -> Classificacao:
        return Classificacao.MAIOR if perfil.idade >= 18 else Classificacao.MENOR

    def I_iterar(self, freq: int) -> List[int]:
        if freq <= 0:
            raise ValueError("freq deve ser positiva")
        return list(range(1, freq + 1))

    def O_organizar(self, registros: List[Registro]) -> Resumo:
        if not registros:
            return Resumo(0, 0, 0.0)
        soma = sum(r.energia for r in registros)
        return Resumo(len(registros), soma, soma / len(registros))

    def U_unir(self, perfil: Perfil, resumo: Resumo) -> Dict[str, Any]:
        return {**asdict(perfil), **asdict(resumo)}

    def simular(self, nome: str, idade: int, vibracao_freq: int = 4) -> Dict[str, Any]:
        perfil        = self.A_atribuir(nome, idade)
        classificacao = self.E_escolher(perfil)
        passos        = self.I_iterar(vibracao_freq)
        energia = 0
        registros: List[Registro] = []
        for passo in passos:
            energia += passo
            registros.append(Registro(passo=passo, energia=energia, classificacao=classificacao))
        resumo = self.O_organizar(registros)
        base   = self.U_unir(perfil, resumo)
        return {"perfil": perfil, "classificacao": classificacao,
                "passos": passos, "registros": registros, "resumo": resumo, "base": base}

# ──────────────────────────────────────────────
# Sistema fractal KOBLLUX (3-6-9 · Schumann)
# ──────────────────────────────────────────────

TRIADICA   = [3, 6, 9]
CICLO_0_7  = list(range(0, 8))
FREQS      = {"micro": 432, "meso": 528, "macro": 741}

@dataclass
class Camada:
    nome: str
    escala: int
    frequencia: int

def autoespelhamento(padrao: Iterable[int], escalar: int) -> List[int]:
    return [p * escalar for p in padrao]

def ressonancia(camada: Camada) -> str:
    return f"[{camada.nome}] f≈{camada.frequencia}Hz → ressoa com {TRIADICA}"

def emergencia_ciclica(ciclo: Iterable[int]) -> List[str]:
    trilha = [f"passo:{c}" for c in ciclo]
    trilha.append("retorno: ∞")
    return trilha

def encenar_fractal() -> Dict[str, Any]:
    micro = Camada("micro", 1, FREQS["micro"])
    meso  = Camada("meso",  2, FREQS["meso"])
    macro = Camada("macro", 3, FREQS["macro"])
    return {
        "espelhos": {
            "micro": autoespelhamento(TRIADICA, micro.escala),
            "meso":  autoespelhamento(TRIADICA, meso.escala),
            "macro": autoespelhamento(TRIADICA, macro.escala),
        },
        "ressonancia": [ressonancia(micro), ressonancia(meso), ressonancia(macro)],
        "emergencia":  emergencia_ciclica(CICLO_0_7),
    }

# ──────────────────────────────────────────────
# História + Demo
# ──────────────────────────────────────────────

def contar_historia() -> None:
    narrar("Prólogo — A Aldeia Python",
    "Havia uma aldeia chamada Python, onde as VOGAIS eram portais do caminho:\n"
    "A (Atribuir), E (Escolher), I (Iterar), O (Organizar), U (Unir).\n"
    "As CONSOANTES eram artesãs, cada qual com sua ferramenta e ofício.\n"
    "No centro da aldeia, o arquiteto VEEB guiava pela Jornada de Cinco Passos.")

    narrar("A Jornada de Cinco Passos (V.E.E.B)",
    "1) Atribuir — o viajante recebe nome, idade e manto azul (atributos).\n"
    "2) Escolher  — o Portal decide seu selo: maior ou menor de idade.\n"
    "3) Iterar    — a Estrada dos Passos acumula energia a cada etapa.\n"
    "4) Organizar — a Biblioteca conta e resume a epopeia do caminho.\n"
    "5) Unir      — a Base registra tudo: identidade + resumo = memória viva.")

    narrar("KOBLLUX — Organização Fractal Viva",
    "Em todo lugar, o Mesmo Movimento: padrões que se repetem (3-6-9),\n"
    "ciclos que emergem do zero e retornam ao infinito (0→7→∞),\n"
    "e frequências que alinham micro, meso e macro (432/528/741).\n"
    "O sistema canta em ressonância e espelha-se a si mesmo.")

def demonstrar_codigo() -> None:
    engine  = VEEBEngine()
    sim     = engine.simular(nome="Bllue", idade=22, vibracao_freq=6)
    narrar("Demonstração V.E.E.B — Resultado",
           f"Perfil: {asdict(sim['perfil'])}\n"
           f"Classificação: {sim['classificacao'].value}\n"
           f"Passos: {sim['passos']}\n"
           f"Resumo: {asdict(sim['resumo'])}\n"
           f"Base:   {sim['base']}")

    fractal = encenar_fractal()
    narrar("Autoespelhamento — 3 · 6 · 9",
           f"micro: {fractal['espelhos']['micro']}\n"
           f"meso:  {fractal['espelhos']['meso']}\n"
           f"macro: {fractal['espelhos']['macro']}")
    narrar("Ressonância Harmônica — 432 · 528 · 741",
           "\n".join(fractal["ressonancia"]))
    narrar("Emergência Cíclica — 0 → 7 → ∞",
           f"trilha: {fractal['emergencia']}")

def mostrar_alfabeto() -> None:
    narrar("Alfabeto do Código — Vogais & Consoantes",
           f"VOGAIS: {VOGAIS}\nCONSOANTES: (21 ferramentas mapeadas)")

if __name__ == "__main__":
    contar_historia()
    demonstrar_codigo()
    mostrar_alfabeto()
