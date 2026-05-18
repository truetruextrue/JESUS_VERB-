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
from collections import Counter
from dataclasses import dataclass, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

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
    "A": "Atribuição (variáveis e tipos)", "E": "Escolha (if/elif/else)",
    "I": "Iteração (for/while)",           "O": "Organizar (funções)",
    "U": "Unir (listas/dicionários)",
}
CONSOANTES: Dict[str, str] = {
    "B":"Booleanos (True/False)",  "C":"Comentários (# explicações)",
    "D":"Definições (def)",        "F":"Funções built-in (print, len...)",
    "G":"Geradores (yield)",       "H":"Herança (POO)",
    "J":"JSON (serialização)",     "K":"Keyword arguments (**kwargs)",
    "L":"Loops (for, while)",      "M":"Módulos (import ...)",
    "N":"None (valor nulo)",       "P":"Parâmetros (entradas de função)",
    "Q":"Queue (fila)",            "R":"Retorno (return)",
    "S":"Strings (\"texto\")",     "T":"Tipos (int, float, bool, str...)",
    "V":"Variáveis",               "W":"While (laço de repetição)",
    "X":"XML (dados)",             "Y":"Yield (geradores)",
    "Z":"Zip (agregação de listas)",
}

# Mapeamento V.E.E.B → Arquétipos KOBLLUX
VEEB_ARCH: Dict[str, str] = {
    "A":"atlas",  "E":"artemis","I":"vitalis","O":"genus", "U":"rhea",
    "B":"solus",  "C":"nova",   "D":"genus",  "F":"bllue", "G":"pulse",
    "H":"atlas",  "J":"aion",   "K":"artemis","L":"vitalis","M":"kodux",
    "N":"serena", "P":"pulse",  "Q":"rhea",   "R":"kaos",  "S":"bllue",
    "T":"atlas",  "V":"nova",   "W":"vitalis","X":"lumine","Y":"solus",
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
    narrar("Prólogo Fractal · 3-6-9 | Schumann ~7.83Hz | 0→7→∞",
        f"""{color("1) Autoespelhamento Quântico (3-6-9)", "BLUE")} — padrões em todas as escalas.
{color("2) Ressonância Harmônica (~7.83Hz)", "GREEN")} — frequências sincronizam camadas.
{color("3) Emergência Cíclica (0→7→∞)", "YELLOW")} — surge do zero, retorna ao infinito.
Cores: {color("Azul=padrões","BLUE")} · {color("Verde=conexões","GREEN")} · {color("Amarelo=ciclos","YELLOW")}""")

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
    return {"espelhos":{"micro":autoespelhamento(TRIADICA,mi.escala),
                        "meso":autoespelhamento(TRIADICA,me.escala),
                        "macro":autoespelhamento(TRIADICA,ma.escala)},
            "ressonancia":[ressonancia(mi),ressonancia(me),ressonancia(ma)],
            "emergencia": trilha}

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

# ── Demo + histórias ──────────────────────────────────────────────────────────
def contar_historia():
    prologo_fractal()
    narrar("Aldeia Python — Portais e Artesãos",
           f"VOGAIS: {VOGAIS}\n\nCONSOANTES: {CONSOANTES}")
    narrar("Mapeamento V.E.E.B → Arquétipos",
           "\n".join(f"  {k} → {v.upper()}" for k,v in VEEB_ARCH.items()))

def demonstrar_codigo(freq: int = 6):
    narrar("Demo V.E.E.B","Simulando Bllue, 22 anos...")
    sim = VEEBEngine().simular("Bllue", 22, freq)
    f = encenar_fractal()
    narrar("Autoespelhamento",
           f"micro:{f['espelhos']['micro']}\nmeso:{f['espelhos']['meso']}\nmacro:{f['espelhos']['macro']}")
    narrar("Ressonância","\n".join(f["ressonancia"]))
    narrar("Base V.E.E.B", json.dumps(sim["base"],ensure_ascii=False,indent=2))

# ── CLI ───────────────────────────────────────────────────────────────────────
def build_parser():
    p = argparse.ArgumentParser(description="KOBLLUX V.E.E.B · A Pirâmide que se Lembra")
    p.add_argument("--explicar",metavar="ARQUIVO.py")
    p.add_argument("--stdin",action="store_true")
    p.add_argument("--titulo")
    p.add_argument("--so-narrativa",action="store_true")
    p.add_argument("--out-txt"); p.add_argument("--out-json")
    p.add_argument("--no-color",action="store_true")
    p.add_argument("--theme",choices=list(THEMES.keys()),default="default")
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
