#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_veeb_story.py · LUMINE · 0×0C · TRANSCENDER · 963Hz
V.E.E.B = Vibração · Energia · Estrutura · Base

A Pirâmide que se Lembra de Si.
APPEND ONLY — alimenta memory.jsonl automaticamente.

Uso:
  python3 kobllux_veeb_story.py                          # demo + história
  python3 kobllux_veeb_story.py --explicar arquivo.py    # AST → narrativa
  python3 kobllux_veeb_story.py --stdin                  # pipe
  python3 kobllux_veeb_story.py --theme cosmico          # tema ANSI
  python3 kobllux_veeb_story.py --auto-theme             # tema automático
  python3 kobllux_veeb_story.py --alimentar-memoria      # grava na memória
  python3 kobllux_veeb_story.py --out-json relatorio.json
"""
from __future__ import annotations
import argparse, ast, json, re, sys, textwrap
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

# ═══════════════════════════════════════════════════════════════════════
# CONSTANTE KΦB = 1/137   ·   FUNDAÇÃO KOBLLUX
# ═══════════════════════════════════════════════════════════════════════
# Análoga à constante de estrutura fina α = 1/137.035999...
# que governa o acoplamento luz↔matéria.
# KΦB governa o acoplamento KODUX↔BLLUE no sistema KOBLLUX.
# KODUX + BLLUE = KOBLLUX    (como K + B = KΦB)
# KOBLLUX + KOBΦ-NODE = ∞   (a mesma dança dual escalada)
KFB_ALPHA: float = 1 / 137.035999084   # CODATA 2018

# ── PIB Escalar · 7 Linguagens Nucleares ──────────────────────────────────────
# PIB_VALUE = hz_lingua / 768 (Python·ATLAS como referência base = 1.0000)
# soma_hz = 4797 → 4+7+9+7 = 27 = 3³ (autoespelhamento quântico Tesla)
PIB_KOBLLUX: List[Dict[str, Any]] = [
    {"linguagem":"python",     "delta":7,"hz":768,"pib":1.0000,"arquetipo":"ATLAS",  "sym":"⬡","veeb":"E","role":"narrativa · análise · engine"},
    {"linguagem":"json",       "delta":1,"hz":528,"pib":0.6875,"arquetipo":"RHEA",   "sym":"∞","veeb":"B","role":"semente · dados · troca"},
    {"linguagem":"typescript", "delta":2,"hz":963,"pib":1.2539,"arquetipo":"LUMINE", "sym":"☀","veeb":"V","role":"interface · render · expressão"},
    {"linguagem":"go",         "delta":3,"hz":594,"pib":0.7734,"arquetipo":"PULSE",  "sym":"≋","veeb":"E","role":"fluxo · concorrência · ritmo"},
    {"linguagem":"sql",        "delta":4,"hz":639,"pib":0.8320,"arquetipo":"AION",   "sym":"⧗","veeb":"B","role":"memória · selagem · query"},
    {"linguagem":"shell",      "delta":5,"hz":528,"pib":0.6875,"arquetipo":"VITALIS","sym":"◉","veeb":"E","role":"integração · deploy · pipeline"},
    {"linguagem":"rust",       "delta":6,"hz":777,"pib":1.0117,"arquetipo":"KAOS",   "sym":"⚡","veeb":"V","role":"sistemas · transformação · segurança"},
]
PIB_SOMA_HZ:  int   = sum(l["hz"]  for l in PIB_KOBLLUX)   # 4797 = 27/digits = 3³
PIB_SOMA_PIB: float = round(sum(l["pib"] for l in PIB_KOBLLUX), 4)  # 6.2460

# Frequências Schumann (Hz) → chave de cor semântica
SCHUMANN: Dict[float, str] = {
    7.83:  "GREEN",    # fundamental Gaia     — VITALIS / Base
    14.3:  "CYAN",     # 2ª harmônica         — ARTEMIS / Detecção
    20.8:  "YELLOW",   # 3ª harmônica         — KAOS / Vibração
    27.3:  "TITLE",    # 4ª harmônica         — GENUS / Síntese
    33.8:  "BLUE",     # 5ª harmônica         — ATLAS / Estrutura
}

# ── ANSI / Temas ──────────────────────────────────────────────────────────────
THEMES: Dict[str, Dict[str, str]] = {
    "default": {"RESET":"\033[0m","TITLE":"\033[95m","BLUE":"\033[94m",
                "GREEN":"\033[92m","YELLOW":"\033[93m","CYAN":"\033[96m",
                "BOLD":"\033[1m","DIM":"\033[2m","RED":"\033[91m"},
    "noite":   {"RESET":"\033[0m","TITLE":"\033[35m","BLUE":"\033[34m",
                "GREEN":"\033[32m","YELLOW":"\033[33m","CYAN":"\033[36m",
                "BOLD":"\033[1m","DIM":"\033[2m","RED":"\033[31m"},
    "luz":     {"RESET":"\033[0m","TITLE":"\033[97m","BLUE":"\033[94m",
                "GREEN":"\033[92m","YELLOW":"\033[93m","CYAN":"\033[96m",
                "BOLD":"\033[1m","DIM":"\033[2m","RED":"\033[91m"},
    "cosmico": {"RESET":"\033[0m","TITLE":"\033[95m","BLUE":"\033[96m",
                "GREEN":"\033[95m","YELLOW":"\033[93m","CYAN":"\033[96m",
                "BOLD":"\033[1m","DIM":"\033[2m","RED":"\033[91m"},
    # schumann — frequências da Terra (7.83→33.8 Hz) como guia de cor
    "schumann":{"RESET":"\033[0m","TITLE":"\033[95m","BLUE":"\033[94m",
                "GREEN":"\033[92m","YELLOW":"\033[93m","CYAN":"\033[96m",
                "BOLD":"\033[1m","DIM":"\033[2m","RED":"\033[91m"},
    # veeb — cores mapeadas diretamente a V·E·E·B
    "veeb":    {"RESET":"\033[0m","TITLE":"\033[1;95m","BLUE":"\033[94m",
                "GREEN":"\033[92m","YELLOW":"\033[93m","CYAN":"\033[96m",
                "BOLD":"\033[1m","DIM":"\033[2m","RED":"\033[91m"},
}
ANSI = dict(THEMES["default"])
NO_COLOR = False

def apply_theme(name: str) -> None:
    global ANSI; ANSI = dict(THEMES.get(name, THEMES["default"]))

def color(txt: str, key: str) -> str:
    if NO_COLOR: return txt
    return f"{ANSI.get(key,'')}{txt}{ANSI['RESET']}"

# ── V.E.E.B Tipos ─────────────────────────────────────────────────────────────
class Classificacao(str, Enum):
    MAIOR = "maior_de_idade"
    MENOR = "menor_de_idade"

@dataclass(frozen=True)
class Perfil:
    nome: str; idade: int; ativo: bool = True
    cor: str = "azul"; tamanho: str = "médio"

@dataclass(frozen=True)
class Registro:
    passo: int; energia: int; classificacao: Classificacao

@dataclass(frozen=True)
class Resumo:
    qtd_registros: int; soma_energia: int; media_energia: float

# ── Analogias ─────────────────────────────────────────────────────────────────
VOGAIS: Dict[str, str] = {
    "A": "Atribuição   — variáveis e tipos        [B·Base   · AION  639Hz]",
    "E": "Escolha      — if / elif / else          [V·Vibr.  · KAOS  777Hz]",
    "I": "Iteração     — for / while               [E·Energ. · VITALIS 528Hz]",
    "O": "Organizar    — funções reutilizáveis     [E·Estr.  · GENUS  852Hz]",
    "U": "Unir         — listas / dicts / sets     [B·Base   · RHEA   528Hz]",
}
CONSOANTES: Dict[str, str] = {
    "B": "Booleanos   — True/False                [B·SOLUS  432Hz]",
    "C": "Comentários — # inline / docstrings      [B·SOLUS  432Hz]",
    "D": "Definições  — def (portais de ação)      [E·ATLAS  768Hz]",
    "F": "Funções     — built-in: print,len,range  [E·ARTEMIS672Hz]",
    "G": "Geradores   — yield / gen-expression     [V·PULSE  594Hz]",
    "H": "Herança     — POO / class Base(Pai)      [E·GENUS  852Hz]",
    "J": "JSON        — serialização de dados      [B·RHEA   528Hz]",
    "K": "Kwargs      — **kwargs (keyword args)    [V·NOVA   432Hz]",
    "L": "Loops       — for / while acumulativo    [E·VITALIS528Hz]",
    "M": "Módulos     — import / from...import     [B·RHEA   528Hz]",
    "N": "None        — valor nulo / ausência      [B·SOLUS  432Hz]",
    "P": "Parâmetros  — entradas de função         [E·ARTEMIS672Hz]",
    "Q": "Queue       — filas (collections.deque)  [V·PULSE  594Hz]",
    "R": "Retorno     — return (desfecho)          [B·AION   639Hz]",
    "S": "Strings     — \"texto\" / f-strings       [B·SERENA 528Hz]",
    "T": "Tipos       — int,float,bool,str,list    [E·ATLAS  768Hz]",
    "V": "Variáveis   — nomes que guardam valores  [E·VITALIS528Hz]",
    "W": "While       — laço de condição contínua  [V·KAOS   777Hz]",
    "X": "XML/Ext.    — dados externos / parsing   [B·RHEA   528Hz]",
    "Y": "Yield       — geração lazy / coroutines  [V·NOVA   432Hz]",
    "Z": "Zip         — agregar listas em paralelo [B·RHEA   528Hz]",
}

# Mapeamento V.E.E.B → Arquétipos CADIAL (letra → {veeb, arquétipo, Hz})
CADIAL_VEEB: Dict[str, Dict[str, Any]] = {
    "ATLAS":   {"veeb":"E","sym":"⬡","hz":768, "role":"Estrutura-Mapa"},
    "NOVA":    {"veeb":"V","sym":"✦","hz":432, "role":"Semente-Vibração"},
    "VITALIS": {"veeb":"E","sym":"◉","hz":528, "role":"Energia-Fluxo"},
    "PULSE":   {"veeb":"V","sym":"≋","hz":594, "role":"Vibração-Ritmo"},
    "ARTEMIS": {"veeb":"E","sym":"◎","hz":672, "role":"Energia-Detecção"},
    "SERENA":  {"veeb":"B","sym":"❋","hz":528, "role":"Base-Cuidado"},
    "KAOS":    {"veeb":"V","sym":"⚡","hz":777, "role":"Vibração-Ruptura"},
    "GENUS":   {"veeb":"E","sym":"⬢","hz":852, "role":"Estrutura-Síntese"},
    "LUMINE":  {"veeb":"E","sym":"☀","hz":963, "role":"Energia-Render"},
    "SOLUS":   {"veeb":"B","sym":"◈","hz":432, "role":"Base-Silêncio"},
    "RHEA":    {"veeb":"B","sym":"∞","hz":528, "role":"Base-Integração"},
    "AION":    {"veeb":"B","sym":"⧗","hz":639, "role":"Base-Tempo"},
}
# Atalho letra → arquétipo (mantido para compatibilidade)
VEEB_ARCH: Dict[str, str] = {
    "A":"atlas",  "E":"artemis","I":"vitalis","O":"genus", "U":"rhea",
    "B":"solus",  "C":"nova",   "D":"genus",  "F":"artemis","G":"pulse",
    "H":"atlas",  "J":"aion",   "K":"artemis","L":"vitalis","M":"rhea",
    "N":"serena", "P":"pulse",  "Q":"rhea",   "R":"aion",  "S":"serena",
    "T":"atlas",  "V":"vitalis","W":"kaos",   "X":"rhea",  "Y":"nova",
    "Z":"rhea",
}

# ── Narrador ──────────────────────────────────────────────────────────────────
def narrar(titulo: str, texto: str, c: str = "TITLE") -> None:
    barra = "─" * 76
    print("\n" + barra)
    print(color("◆ " + titulo, c))
    print(barra)
    print(textwrap.dedent(texto).strip() + "\n")

def prologo_fractal() -> None:
    narrar("Prólogo Fractal · KΦB=1/137 | Schumann ~7.83Hz | 3-6-9 | 0→7→∞",
        f"""Esta jornada segue três princípios vivos e a constante KΦB:

  {color("1) Autoespelhamento Quântico (3-6-9)", "BLUE")}
     padrões repetem em todas as escalas:
     micro:[3,6,9] · meso:[6,12,18] · macro:[9,18,27]

  {color("2) Ressonância Harmônica (Schumann ~7.83Hz)", "GREEN")}
     5 frequências da Terra sincronizam camadas:
     7.83 · 14.3 · 20.8 · 27.3 · 33.8 Hz

  {color("3) Emergência Cíclica (0→7→∞)", "YELLOW")}
     estruturas surgem do zero e retornam ao infinito

  {color(f"KΦB = {round(KFB_ALPHA, 9)}", "CYAN")} (constante de acoplamento KODUX↔BLLUE)
  {color("KODUX + BLLUE = KOBLLUX", "TITLE")} · KOBLLUX + KOBΦ-NODE = ∞

  VEEB: {color("V","YELLOW")}ibração · {color("E","GREEN")}nergia · {color("E","BLUE")}strutura · {color("B","TITLE")}ase""")

# ── Motor V.E.E.B ─────────────────────────────────────────────────────────────
class VEEBEngine:
    def A_atribuir(self, nome: str, idade: int,
                   ativo: bool = True, cor: str = "azul", tamanho: str = "médio") -> Perfil:
        p = Perfil(nome=nome.strip(), idade=int(idade), ativo=ativo, cor=cor, tamanho=tamanho)
        print(color(f"[A] Atribuir → {asdict(p)}", "BLUE")); return p

    def E_escolher(self, perfil: Perfil) -> Classificacao:
        c = Classificacao.MAIOR if perfil.idade >= 18 else Classificacao.MENOR
        print(color(f"[E] Escolher → {c.value}", "YELLOW")); return c

    def I_iterar(self, freq: int) -> List[int]:
        if freq <= 0: raise ValueError("freq deve ser positiva")
        passos = list(range(1, freq + 1))
        print(color(f"[I] Iterar → {passos}", "GREEN")); return passos

    def O_organizar(self, registros: List[Registro]) -> Resumo:
        if not registros: r = Resumo(0, 0, 0.0)
        else:
            soma = sum(x.energia for x in registros)
            r = Resumo(len(registros), soma, soma / len(registros))
        print(color(f"[O] Organizar → {asdict(r)}", "TITLE")); return r

    def U_unir(self, perfil: Perfil, resumo: Resumo) -> Dict[str, Any]:
        base = {**asdict(perfil), **asdict(resumo)}
        print(color(f"[U] Unir → base selada", "BLUE")); return base

    def simular(self, nome: str, idade: int, freq: int = 4) -> Dict[str, Any]:
        p = self.A_atribuir(nome, idade)
        cl = self.E_escolher(p)
        passos = self.I_iterar(freq)
        energia, registros = 0, []
        for s in passos:
            energia += s
            registros.append(Registro(s, energia, cl))
            print(color(f"  · p={s}", "GREEN"), color(f"e={energia}", "BLUE"),
                  color(cl.value, "YELLOW"))
        resumo = self.O_organizar(registros)
        base = self.U_unir(p, resumo)
        return {"perfil":p,"classificacao":cl,"passos":passos,
                "registros":registros,"resumo":resumo,"base":base}

# ── Fractal simbólico ─────────────────────────────────────────────────────────
TRIADICA = [3, 6, 9]; CICLO_0_7 = list(range(0, 8))
FREQS = {"micro":432,"meso":528,"macro":741}

@dataclass
class Camada:
    nome: str; escala: int; frequencia: int

def autoespelhamento(padrao: Iterable[int], escalar: int) -> List[int]:
    return [p * escalar for p in padrao]

def ressonancia(camada: Camada) -> str:
    return f"[{camada.nome}] f≈{camada.frequencia}Hz → ressoa com {TRIADICA}"

def encenar_fractal() -> Dict[str, Any]:
    mi = Camada("micro",1,FREQS["micro"]); me = Camada("meso",2,FREQS["meso"])
    ma = Camada("macro",3,FREQS["macro"])
    trilha = [f"passo:{c}" for c in CICLO_0_7] + ["retorno: ∞"]
    return {"kfb_alpha":    KFB_ALPHA,
            "kfb_x_18":     round(KFB_ALPHA * 18, 10),  # KΦB × (3+6+9)
            "schumann_hz":  list(SCHUMANN.keys()),
            "espelhos":     {"micro":autoespelhamento(TRIADICA,mi.escala),
                             "meso": autoespelhamento(TRIADICA,me.escala),
                             "macro":autoespelhamento(TRIADICA,ma.escala)},
            "ressonancia":  [ressonancia(mi),ressonancia(me),ressonancia(ma)],
            "emergencia":   trilha}

# ── AST Coletor ───────────────────────────────────────────────────────────────
class ColetorAST(ast.NodeVisitor):
    def __init__(self):
        self.imports: List[str] = []; self.from_imports: List[str] = []
        self.funcs: List[Dict] = []; self.classes: List[Dict] = []
        self.assigns: List[str] = []
        self.ifs=self.whiles=self.fors=self.returns=self.trys=self.withs=0
        self.lambdas=self.yields=self.async_funcs=0
        self.comps: Dict[str,int] = {"list":0,"dict":0,"set":0,"gen":0}

    def visit_Import(self,n):
        for a in n.names: self.imports.append(a.name); self.generic_visit(n)
    def visit_ImportFrom(self,n):
        self.from_imports.append(f"{n.module or ''}: {', '.join(a.name for a in n.names)}")
        self.generic_visit(n)
    def visit_FunctionDef(self,n):
        args=[a.arg for a in n.args.args]
        if n.args.vararg: args.append("*"+n.args.vararg.arg)
        if n.args.kwarg:  args.append("**"+n.args.kwarg.arg)
        self.funcs.append({"name":n.name,"args":args,"deco":len(n.decorator_list)})
        self.generic_visit(n)
    def visit_AsyncFunctionDef(self,n): self.async_funcs+=1; self.visit_FunctionDef(n)
    def visit_ClassDef(self,n):
        methods=[x.name for x in n.body if isinstance(x,(ast.FunctionDef,ast.AsyncFunctionDef))]
        self.classes.append({"name":n.name,"methods":methods}); self.generic_visit(n)
    def visit_Assign(self,n):
        for t in n.targets:
            if isinstance(t,ast.Name): self.assigns.append(t.id)
        self.generic_visit(n)
    def visit_If(self,n):      self.ifs+=1;    self.generic_visit(n)
    def visit_For(self,n):     self.fors+=1;   self.generic_visit(n)
    def visit_While(self,n):   self.whiles+=1; self.generic_visit(n)
    def visit_Return(self,n):  self.returns+=1;self.generic_visit(n)
    def visit_Try(self,n):     self.trys+=1;   self.generic_visit(n)
    def visit_With(self,n):    self.withs+=1;  self.generic_visit(n)
    def visit_Lambda(self,n):  self.lambdas+=1;self.generic_visit(n)
    def visit_Yield(self,n):   self.yields+=1; self.generic_visit(n)
    def visit_ListComp(self,n):      self.comps["list"]+=1;self.generic_visit(n)
    def visit_DictComp(self,n):      self.comps["dict"]+=1;self.generic_visit(n)
    def visit_SetComp(self,n):       self.comps["set"]+=1; self.generic_visit(n)
    def visit_GeneratorExp(self,n):  self.comps["gen"]+=1; self.generic_visit(n)

def _arch_scores(col: ColetorAST) -> Dict[str,int]:
    s: Dict[str,int] = {}
    def add(a,v): s[a] = s.get(a,0)+v
    add("kodux",   len(col.imports)*3)
    add("atlas",   len(col.classes)*4)
    add("genus",   len(col.funcs)*2)
    add("vitalis", (col.fors+col.whiles)*3)
    add("artemis", col.ifs*2)
    add("kaos",    col.trys*5)
    add("rhea",    col.withs*3)
    add("lumine",  col.lambdas*4)
    add("serena",  len(col.assigns))
    add("aion",    col.returns*2)
    add("pulse",   col.async_funcs*5)
    add("solus",   col.yields*4)
    return {k:v for k,v in sorted(s.items(),key=lambda x:-x[1]) if v>0}

def _tema_auto(source: str) -> str:
    pat = re.compile(r"(3\s*[-,]\s*6\s*[-,]\s*9)|(\[\s*3\s*,\s*6\s*,\s*9\s*\])")
    try:
        col = ColetorAST(); col.visit(ast.parse(source))
    except SyntaxError: return "default"
    if pat.search(source) or col.yields or col.async_funcs: return "cosmico"
    if col.trys >= 2: return "noite"
    if (col.funcs and len(col.funcs)+len(col.classes)) >= 6 and col.imports: return "luz"
    return "default"

def explicar_codigo_fonte(source: str, titulo: Optional[str] = None):
    try: tree = ast.parse(source)
    except SyntaxError as e:
        return color(f"[Erro] {e}", "YELLOW"), {"error": str(e)}
    col = ColetorAST(); col.visit(tree)
    nome = titulo or "Código analisado"
    partes = [color(f"Prólogo — O viajante chega: «{nome}»", "TITLE")]
    if col.imports or col.from_imports:
        partes.append(color("Conselho das Consoantes (imports):", "GREEN"))
        if col.imports:
            partes.append(color("  · Módulos: ","GREEN")+", ".join(sorted(set(col.imports))[:8]))
        if col.from_imports:
            partes.append(color("  · De: ","GREEN")+" | ".join(col.from_imports[:5]))
    if col.classes:
        partes.append(color("Casas-Forma (classes): ","BLUE")+
                      ", ".join(c["name"] for c in col.classes))
    if col.funcs:
        partes.append(color("Portais de ação (funções):","BLUE"))
        for f in col.funcs[:12]:
            args=", ".join(f["args"]) or "sem parâmetros"
            partes.append("  · "+color(f["name"],"BLUE")+"("+color(args,"GREEN")+")")
    if col.assigns:
        partes.append(color("Objetos nomeados: ","BLUE")+
                      ", ".join(sorted(set(col.assigns))[:15]))
    fluxo=[]
    if col.ifs:    fluxo.append(color(f"if={col.ifs}","YELLOW"))
    if col.fors:   fluxo.append(color(f"for={col.fors}","YELLOW"))
    if col.whiles: fluxo.append(color(f"while={col.whiles}","YELLOW"))
    if col.trys:   fluxo.append(color(f"try={col.trys}","RED"))
    if fluxo: partes.append(color("Fluxo: ","YELLOW")+" · ".join(fluxo))
    extras=[]
    if col.lambdas:    extras.append(color(f"lambda={col.lambdas}","CYAN"))
    if col.yields:     extras.append(color(f"yield={col.yields}","GREEN"))
    if col.async_funcs:extras.append(color(f"async={col.async_funcs}","BLUE"))
    if any(col.comps.values()):
        extras.append(color(f"comps={sum(col.comps.values())}","CYAN"))
    if extras: partes.append("Especiais: "+" · ".join(extras))
    if col.returns: partes.append(color(f"Desfechos (return): {col.returns}","TITLE"))
    arch_sc = _arch_scores(col)
    dominant = next(iter(arch_sc),"kobllux")
    partes.append(color(f"Arquétipo dominante: {dominant.upper()} ({arch_sc})","GREEN"))
    partes.append(color("Epílogo — A Pirâmide Lembra: dados+fluxo+forma = Base viva. ∆7","TITLE"))
    meta = {"title":nome,"imports":col.imports,"from_imports":col.from_imports,
            "functions":col.funcs,"classes":col.classes,"assignments":col.assigns,
            "flow":{"ifs":col.ifs,"fors":col.fors,"whiles":col.whiles,"trys":col.trys},
            "special":{"lambdas":col.lambdas,"yields":col.yields,"async":col.async_funcs},
            "returns":col.returns,"veeb_arch":arch_sc,"dominant_arch":dominant}
    return "\n".join(partes), meta

def alimentar_memoria(meta: dict, source_name: str) -> bool:
    try:
        from kobllux_memory import KoblluxMemory
        mem = KoblluxMemory()
        arch = meta.get("dominant_arch","kobllux")
        tags = ([f["name"] for f in meta.get("functions",[])[:5]] +
                [c["name"] for c in meta.get("classes",[])[:3]] +
                meta.get("imports",[])[:4] + ["veeb","ast"])
        summary = (f"AST: {len(meta['functions'])} funções · "
                   f"{len(meta['classes'])} classes · "
                   f"imports: {', '.join(meta['imports'][:3])}")
        mem.write(arch=arch, content=summary, tags=list(set(tags)),
                  source=source_name, record_type="VEEB_AST",
                  extra={"veeb_arch_scores":meta.get("veeb_arch",{}),"title":meta.get("title","")})
        print(color(f"[∆7] Memória alimentada · arch={arch}", "GREEN"))
        return True
    except ImportError:
        print(color("[aviso] kobllux_memory não encontrado","YELLOW")); return False

# ── PIB Escalar ───────────────────────────────────────────────────────────────
def mostrar_pib_escalar() -> None:
    """Exibe a tabela PIB das 7 linguagens nucleares KOBLLUX."""
    linhas = [
        color(f"  Base: Python·ATLAS·768Hz·Δ7 = PIB 1.0000", "BLUE"),
        color(f"  KΦB = {KFB_ALPHA:.9f}  ·  ciclo Δ0→Δ7→∞", "CYAN"),
        "",
        color("  Ling.        Δ   Hz    PIB    Arq.       V  Role", "DIM"),
        color("  ─────────── ─── ────  ─────── ─────────  ─  ──────────────────────", "DIM"),
    ]
    for l in PIB_KOBLLUX:
        pib_str = f"{l['pib']:.4f}"
        arch_str = (l['sym'] + ' ' + l['arquetipo'][:8]).ljust(10)
        linhas.append(
            f"  {color(l['linguagem'][:11].ljust(11),'BOLD')} "
            f"{l['delta']}   "
            f"{color(str(l['hz']).ljust(4),'GREEN')}  "
            f"{color(pib_str,'YELLOW')}  "
            f"{color(arch_str,'CYAN')}  "
            f"{color(l['veeb'],'TITLE')}  "
            f"{color(l['role'][:22],'DIM')}"
        )
    digits = sum(int(d) for d in str(PIB_SOMA_HZ))
    linhas += [
        color("  ─────────── ─── ────  ─────── ─────────  ─  ──────────────────────", "DIM"),
        f"  {'TOTAL'.ljust(11)}     "
        f"{color(str(PIB_SOMA_HZ),'GREEN')}  "
        f"{color(str(PIB_SOMA_PIB),'YELLOW')}  "
        f"{color(f'{PIB_SOMA_HZ}→{digits}=3³ (Tesla)','BLUE')}",
    ]
    narrar("PIB Escalar · 7 Linguagens Nucleares · KOBLLUX_VIVO", "\n".join(linhas), "BLUE")


# ── Demo + histórias ──────────────────────────────────────────────────────────
def contar_historia():
    prologo_fractal()
    narrar("Aldeia Python — Vogais (portais) + Consoantes (artesãos)",
           "\n".join([
               color("VOGAIS:", "BLUE"),
               *[f"  {color(k,'BOLD')} → {v}" for k,v in VOGAIS.items()],
               "",
               color("CONSOANTES:", "GREEN"),
               *[f"  {color(k,'BOLD')} → {v}" for k,v in CONSOANTES.items()],
           ]))
    narrar("Arquétipos CADIAL × V.E.E.B",
           "\n".join(
               f"  {color(k,'BOLD')} {v['sym']} {v['hz']}Hz → "
               f"{color(v['veeb'],'YELLOW')} · {v['role']}"
               for k,v in CADIAL_VEEB.items()
           ))

def demonstrar_codigo(freq: int = 6):
    narrar("Demo V.E.E.B","Simulando Bllue, 22 anos...")
    sim = VEEBEngine().simular("Bllue", 22, freq)
    f = encenar_fractal()
    narrar("Autoespelhamento",
           f"micro:{f['espelhos']['micro']}\nmeso:{f['espelhos']['meso']}\nmacro:{f['espelhos']['macro']}")
    narrar("Ressonância","\n".join(f["ressonancia"]))
    narrar("Base V.E.E.B", json.dumps(sim["base"],ensure_ascii=False,indent=2))
    mostrar_pib_escalar()

# ── CLI ───────────────────────────────────────────────────────────────────────
def build_parser():
    p = argparse.ArgumentParser(description="KOBLLUX V.E.E.B · A Pirâmide que se Lembra")
    p.add_argument("--explicar",metavar="ARQUIVO.py")
    p.add_argument("--stdin",action="store_true")
    p.add_argument("--titulo")
    p.add_argument("--so-narrativa",action="store_true")
    p.add_argument("--out-txt"); p.add_argument("--out-json")
    p.add_argument("--no-color",action="store_true")
    p.add_argument("--theme",choices=list(THEMES.keys()),default="default",
                   help="Tema ANSI: default|noite|luz|cosmico|schumann|veeb")
    p.add_argument("--auto-theme",action="store_true")
    p.add_argument("--freq",type=int,default=6)
    p.add_argument("--alimentar-memoria",action="store_true")
    return p

def main(argv=None):
    global NO_COLOR
    args = build_parser().parse_args(argv)
    if args.no_color: NO_COLOR = True
    else: apply_theme(args.theme)
    if args.explicar or args.stdin:
        if args.explicar:
            try: source = Path(args.explicar).read_text(encoding="utf-8",errors="replace")
            except Exception as e:
                print(color(f"[Erro] {e}","YELLOW")); return 1
            titulo = args.titulo or args.explicar
        else:
            source = sys.stdin.read(); titulo = args.titulo or "stdin"
        if args.auto_theme and not NO_COLOR:
            t = _tema_auto(source); apply_theme(t)
            print(color(f"[auto-theme] {t}","GREEN"))
        narrativa, meta = explicar_codigo_fonte(source, titulo)
        narrar("Conversor Narrativo", narrativa)
        if args.out_txt:
            Path(args.out_txt).write_text(narrativa,encoding="utf-8")
            print(color(f"[OK] {args.out_txt}","GREEN"))
        if args.out_json:
            Path(args.out_json).write_text(
                json.dumps({"narrative":narrativa,**meta},ensure_ascii=False,indent=2),
                encoding="utf-8")
            print(color(f"[OK] {args.out_json}","GREEN"))
        if args.alimentar_memoria: alimentar_memoria(meta, titulo)
        if args.so_narrativa: return 0
    contar_historia(); demonstrar_codigo(args.freq); return 0

if __name__ == "__main__":
    raise SystemExit(main())
