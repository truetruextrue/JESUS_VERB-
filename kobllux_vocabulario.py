#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_vocabulario.py · AION · 0×0B · TEMPORIZAR · 741Hz
"A Pirâmide que se Lembra de Si."

Vocabulário vivo KOBLLUX — APPEND ONLY.
Cada conversa, cada commit, cada análise AST alimenta este dicionário.
O sistema aprende o vocabulário natural do usuário e mapeia para arquétipos.
Com o tempo, não é necessário digitar comandos de máquina — o vocabulário
reconhece a intenção e sugere o comando automaticamente.

APPEND ONLY: nunca remove ou modifica entradas — apenas acrescenta.

Uso:
  python3 kobllux_vocabulario.py --parse "texto da conversa"
  python3 kobllux_vocabulario.py --learn "quero selar a memória" --arch aion
  python3 kobllux_vocabulario.py --comando "texto"     # sugere auto-comando
  python3 kobllux_vocabulario.py --summary             # top vocabulário
  python3 kobllux_vocabulario.py --from-memory         # constrói vocab da memória
  python3 kobllux_vocabulario.py --from-ast arquivo.py # constrói vocab via AST
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

VOCAB_FILE    = ROOT / "_index" / "vocabulario_vivo.jsonl"
MEMORY_FILE   = ROOT / "_index" / "memory.jsonl"
COMMIT_LOG    = ROOT / "_index" / "COMMIT_LOG_∆7.jsonl"

# ── Vocabulário semântico de cada arquétipo ───────────────────────────────────

ARCH_SEEDS: Dict[str, List[str]] = {
    "kodux":   ["detectar","escanear","varrer","índice","scan","buscar","encontrar",
                "rastrear","mapear","observar","ver","olho","arquivo","listar","cadial"],
    "nova":    ["criar","iniciar","novo","começar","gerar","spark","faísca","nasce",
                "surge","origem","inventar","inspirar","ideia","semente"],
    "atlas":   ["estruturar","organizar","planejar","grade","mapa","ordem","config",
                "schema","hierarquia","pasta","sistema","arquitetura","base","README"],
    "vitalis": ["pulsar","energia","ciclo","iterar","loop","respirar","vivo","orgânico",
                "movimento","ritmo","contínuo","seiva","motor","pipeline"],
    "pulse":   ["ritmo","batida","voz","tts","audio","som","falar","narrar","emoção",
                "sentir","ressoar","frequência","melodia","sincronizar"],
    "artemis": ["precisão","alvo","focar","convergir","injetar","target","analisar",
                "depurar","investigar","raio","flecha","estratégia","objetivo"],
    "serena":  ["integrar","acolher","cuidar","suave","conectar","unir","harmonizar",
                "bridge","UI","interface","suporte","silêncio","calma","curar"],
    "kaos":    ["selar","patch","fix","consertar","ruptura","romper","liberar","override",
                "transformar","quebrar","reconstruir","entropy","caos","patch"],
    "genus":   ["gerar","base","fundação","construir","estrutura","criar","arquétipo",
                "semente","origem","definir","classe","função","módulo"],
    "lumine":  ["iluminar","luz","visual","tema","efeito","clareza","transcender","ver",
                "revelar","brilhar","cor","estética","CSS","UI","design"],
    "solus":   ["foco","singular","único","silêncio","profundo","só","isolar","concentrar",
                "meditar","central","essência","puro","diamante"],
    "rhea":    ["fluir","conectar","ponte","bridge","rota","navegar","corrente","link",
                "integrar","sinapse","fluxo","passagem","caminho","rede"],
    "aion":    ["tempo","memória","guardar","registrar","histórico","ciclo","temporal",
                "passado","futuro","selagem","log","salvar","permanente","eternidade"],
    "bllue":   ["espelhar","integrar","refletir","coupler","canal","dual","interface",
                "sincronizar","pontes","eco","espelho","vivo"],
}

# Mapeamento opcode → comandos sugeridos
OPCODE_COMMANDS: Dict[str, List[str]] = {
    "DETECTAR":    ["git kob-arch","python3 cadial_scan.py","git kob-status"],
    "INTEGRAR":    ["git add -A","python3 kobllux_roda_viva.py","python3 kobllux_auto_session.py --once"],
    "EXPANDIR":    ["git push origin HEAD","python3 kobllux_roda_viva.py --inbox inbox"],
    "SELAR":       ["git kob-seal","python3 kobllux_auto_session.py --session-end"],
    "ESTRUTURAR":  ["git kob-log","python3 14_UTILS/01_SCRIPTS/monolith_consolidator.py --all"],
    "FLUIR":       ["git kob-sync","python3 kobllux_auto_session.py --once"],
    "TEMPORIZAR":  ["python3 kobllux_auto_session.py --summary","git kob-memory"],
    "TRANSCENDER": ["python3 kobllux_veeb_story.py","python3 VERBO.py"],
    "PULSAR":      ["python3 kobllux_auto_session.py --watch --timer 7"],
    "LAPIDAR":     ["git pull --rebase","python3 14_UTILS/01_SCRIPTS/monolith_consolidator.py"],
    "CONVERGIR":   ["python3 kobllux_roda_viva.py --summary"],
    "UNIFICAR":    ["python3 kobllux_auto_session.py --session-end --auto-commit"],
}

from kobllux_memory import ARCHETYPES_META


# ── API de Vocabulário ────────────────────────────────────────────────────────

class VocabularioVivo:
    """
    Vocabulário vivo KOBLLUX — APPEND ONLY.
    Aprende com conversas, commits e análises AST.
    Mapeia texto natural → arquétipo → comando sugerido.
    """

    def __init__(self, path: Path = VOCAB_FILE):
        self.path = Path(path)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self._cache: Optional[Counter] = None

    # ── ESCRITA (APPEND ONLY) ─────────────────────────────────────────────────

    def learn(self, text: str, arch: str, source: str = "manual", weight: int = 1) -> list[dict]:
        """
        Registra termos do texto como vocabulário do arquétipo.
        APPEND ONLY — cada chamada só adiciona, nunca remove.
        """
        words = self._tokenize(text)
        if not words:
            return []

        ts = datetime.now(timezone.utc).isoformat()
        entries = []
        with self.path.open("a", encoding="utf-8") as f:
            for word in words:
                entry = {
                    "ts":     ts,
                    "arch":   arch.lower(),
                    "word":   word,
                    "source": source,
                    "weight": weight,
                    "seal":   "∆7",
                }
                f.write(json.dumps(entry, ensure_ascii=False) + "\n")
                entries.append(entry)

        self._cache = None  # invalida cache
        return entries

    def learn_from_seeds(self) -> int:
        """Registra as palavras-semente de cada arquétipo na primeira execução."""
        existing = self._load_words_set()
        added = 0
        for arch, words in ARCH_SEEDS.items():
            for w in words:
                if f"{arch}:{w}" not in existing:
                    self.learn(w, arch, source="seed", weight=2)
                    added += 1
        return added

    # ── LEITURA ───────────────────────────────────────────────────────────────

    def _load(self) -> list[dict]:
        if not self.path.exists():
            return []
        records = []
        with self.path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    records.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
        return records

    def _load_words_set(self) -> set[str]:
        return {f"{r['arch']}:{r['word']}" for r in self._load()}

    def freq_by_arch(self) -> Dict[str, Counter]:
        """Frequência de palavras por arquétipo."""
        by_arch: Dict[str, Counter] = {}
        for r in self._load():
            arch = r.get("arch", "kobllux")
            if arch not in by_arch:
                by_arch[arch] = Counter()
            w = r.get("word", "")
            by_arch[arch][w] += r.get("weight", 1)
        return by_arch

    # ── PARSE / DETECÇÃO ──────────────────────────────────────────────────────

    def parse_intent(self, text: str) -> dict:
        """
        Analisa texto e retorna arquétipo dominante + confiança + palavras-chave encontradas.
        A pirâmide lembra: quanto mais vocabulário acumulado, mais precisa a detecção.
        """
        words = set(self._tokenize(text))
        by_arch = self.freq_by_arch()

        # Score: palavras encontradas × seu peso acumulado
        scores: Counter = Counter()
        matched_words: Dict[str, list] = {}

        for arch, vocab in by_arch.items():
            for word in words:
                if word in vocab:
                    scores[arch] += vocab[word]
                    matched_words.setdefault(arch, []).append(word)

        # Fallback: seeds estáticos
        if not scores:
            for arch, seeds in ARCH_SEEDS.items():
                for s in seeds:
                    if s in words:
                        scores[arch] += 1
                        matched_words.setdefault(arch, []).append(s)

        if not scores:
            return {
                "arch":     "kobllux",
                "opcode":   "0x00",
                "action":   "ORIGEM",
                "hz":       768,
                "score":    0,
                "confidence": 0.0,
                "matched":  [],
                "commands": OPCODE_COMMANDS.get("ORIGEM", []),
            }

        total = sum(scores.values())
        dominant = scores.most_common(1)[0][0]
        meta = ARCHETYPES_META.get(dominant, ARCHETYPES_META["kobllux"])

        return {
            "arch":       dominant,
            "opcode":     meta["opcode"],
            "action":     meta["action"],
            "hz":         meta["hz"],
            "sym":        meta["sym"],
            "score":      scores[dominant],
            "confidence": round(scores[dominant] / total, 3),
            "matched":    matched_words.get(dominant, []),
            "all_scores": dict(scores.most_common(5)),
            "commands":   OPCODE_COMMANDS.get(meta["action"], []),
        }

    def suggest_command(self, text: str, auto_run: bool = False) -> str:
        """
        Analisa o texto e sugere o comando KOBLLUX correspondente.
        Se auto_run=True, executa o primeiro comando sugerido.
        """
        intent = self.parse_intent(text)
        arch   = intent["arch"].upper()
        action = intent["action"]
        sym    = intent.get("sym", "○")
        cmds   = intent["commands"]

        output = [
            f"\n[{sym} {arch} · {intent['opcode']} · {intent['hz']}Hz · {action}]",
            f"  Confiança  : {int(intent['confidence']*100)}%",
            f"  Palavras   : {', '.join(intent['matched'][:6])}",
        ]
        if cmds:
            output.append("  Comandos sugeridos:")
            for i, cmd in enumerate(cmds[:3], 1):
                output.append(f"    {i}. {cmd}")
        else:
            output.append("  [sem comando específico — ORIGEM]")

        result = "\n".join(output)
        print(result)

        if auto_run and cmds:
            print(f"\n  → Executando: {cmds[0]}")
            subprocess.run(cmds[0], shell=True, cwd=ROOT)

        return result

    # ── ALIMENTAÇÃO AUTOMÁTICA ────────────────────────────────────────────────

    def from_memory(self) -> int:
        """Constrói vocabulário a partir de memory.jsonl (APPEND ONLY)."""
        if not MEMORY_FILE.exists():
            return 0
        existing = self._load_words_set()
        added = 0
        with MEMORY_FILE.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue
                arch    = r.get("arch", "kobllux")
                content = r.get("content", "") + " " + " ".join(r.get("tags", []))
                words = self._tokenize(content)
                for w in words:
                    if f"{arch}:{w}" not in existing:
                        self.learn(w, arch, source="memory.jsonl", weight=1)
                        existing.add(f"{arch}:{w}")
                        added += 1
        return added

    def from_commit_log(self) -> int:
        """Constrói vocabulário a partir de COMMIT_LOG_∆7.jsonl."""
        if not COMMIT_LOG.exists():
            return 0
        existing = self._load_words_set()
        added = 0
        with COMMIT_LOG.open("r", encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line.strip())
                except json.JSONDecodeError:
                    continue
                arch = r.get("arch", "kobllux")
                msg  = r.get("msg", "")
                for w in self._tokenize(msg):
                    if f"{arch}:{w}" not in existing:
                        self.learn(w, arch, source="commit-log", weight=2)
                        existing.add(f"{arch}:{w}")
                        added += 1
        return added

    def from_ast(self, filepath: str) -> int:
        """Analisa arquivo Python via AST e aprende vocabulário dos nomes."""
        import ast as _ast
        try:
            source = Path(filepath).read_text(encoding="utf-8", errors="replace")
            tree   = _ast.parse(source)
        except Exception as e:
            print(f"[erro] {e}"); return 0

        from kobllux_veeb_story import ColetorAST, _arch_scores
        col = ColetorAST(); col.visit(tree)
        arch_sc = _arch_scores(col)
        dominant = next(iter(arch_sc), "kodux")

        tokens: List[str] = []
        tokens += [f["name"] for f in col.funcs]
        tokens += [c["name"] for c in col.classes]
        tokens += col.assigns
        tokens += col.imports

        existing = self._load_words_set()
        added = 0
        for t in tokens:
            for w in self._tokenize(t):
                if f"{dominant}:{w}" not in existing:
                    self.learn(w, dominant, source=f"ast:{Path(filepath).name}", weight=2)
                    existing.add(f"{dominant}:{w}")
                    added += 1
        return added

    def summary(self, top_n: int = 10) -> dict:
        """Resumo do vocabulário acumulado."""
        by_arch = self.freq_by_arch()
        return {
            "total_entries": sum(sum(v.values()) for v in by_arch.values()),
            "archetypes":    len(by_arch),
            "vocab_path":    str(self.path),
            "top_by_arch":   {
                arch: dict(counter.most_common(top_n))
                for arch, counter in by_arch.items()
            },
        }

    # ── Utils ─────────────────────────────────────────────────────────────────

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Tokeniza texto em palavras únicas ≥3 chars, lowercase, sem stopwords."""
        STOP = {
            "que","de","do","da","os","as","um","uma","com","para","por","no","na",
            "nos","nas","e","ou","se","ao","ao","já","mais","não","é","são","foi",
            "ser","ter","em","com","sua","seu","esse","essa","this","the","and","or",
            "for","def","import","from","return","class","if","else","elif","while",
            "true","false","none","self","args","kwargs",
        }
        words = re.findall(r"[a-záàâãéêíóôõúüçA-Z_][a-záàâãéêíóôõúüçA-Z0-9_]{2,}", text)
        return list({
            w.lower() for w in words
            if w.lower() not in STOP and not w.isdigit() and len(w) >= 3
        })


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="KOBLLUX Vocabulário Vivo · A Pirâmide que se Lembra")
    p.add_argument("--parse",   metavar="TEXTO",  help="Detecta arquétipo no texto")
    p.add_argument("--learn",   metavar="TEXTO",  help="Aprende vocabulário do texto")
    p.add_argument("--arch",    default="kobllux",help="Arquétipo para --learn")
    p.add_argument("--source",  default="cli",    help="Fonte do aprendizado")
    p.add_argument("--comando", metavar="TEXTO",  help="Sugere e executa comando")
    p.add_argument("--auto-run",action="store_true",help="Executa o comando sugerido")
    p.add_argument("--summary", action="store_true",help="Resumo do vocabulário")
    p.add_argument("--from-memory",     action="store_true",help="Aprende da memory.jsonl")
    p.add_argument("--from-commits",    action="store_true",help="Aprende do commit log")
    p.add_argument("--from-ast", metavar="ARQUIVO",help="Aprende via AST de arquivo .py")
    p.add_argument("--init-seeds",action="store_true",help="Carrega vocabulário inicial")
    p.add_argument("--json",    action="store_true",help="Saída em JSON")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    vocab = VocabularioVivo()

    if args.init_seeds:
        n = vocab.learn_from_seeds()
        print(f"[AION ⧗] {n} seeds registradas no vocabulário vivo")
        return

    if args.from_memory:
        n = vocab.from_memory()
        print(f"[AION ⧗] {n} termos aprendidos da memória viva")

    if args.from_commits:
        n = vocab.from_commit_log()
        print(f"[AION ⧗] {n} termos aprendidos dos commits")

    if args.from_ast:
        n = vocab.from_ast(args.from_ast)
        print(f"[AION ⧗] {n} termos aprendidos do AST: {args.from_ast}")

    if args.learn:
        entries = vocab.learn(args.learn, args.arch, source=args.source)
        print(f"[RHEA ∞] {len(entries)} termos aprendidos → arch={args.arch}")
        if args.json: print(json.dumps(entries[:5], ensure_ascii=False))

    if args.parse:
        intent = vocab.parse_intent(args.parse)
        if args.json:
            print(json.dumps(intent, ensure_ascii=False, indent=2))
        else:
            print(f"\n[{intent.get('sym','○')} {intent['arch'].upper()} · {intent['action']}]")
            print(f"  Hz={intent['hz']} · score={intent['score']} · conf={int(intent['confidence']*100)}%")
            print(f"  Palavras: {', '.join(intent['matched'])}")
            print(f"  Scores: {intent.get('all_scores',{})}")
            if intent["commands"]:
                print(f"  Comandos: {' | '.join(intent['commands'][:2])}")

    if args.comando:
        vocab.suggest_command(args.comando, auto_run=args.auto_run)

    if args.summary:
        s = vocab.summary()
        if args.json:
            print(json.dumps(s, ensure_ascii=False, indent=2))
        else:
            print(f"\n[VOCABULÁRIO VIVO · {s['total_entries']} entradas · {s['archetypes']} arquétipos]")
            for arch, words in s["top_by_arch"].items():
                top = list(words.items())[:5]
                print(f"  {arch.upper()}: {' · '.join(f'{w}({n})' for w,n in top)}")


if __name__ == "__main__":
    main()
