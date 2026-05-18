#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
kobllux_n8n_bridge.py · RHEA · 0×09 · FLUIR · 528Hz
"O fluxo que conecta o mundo interno (Python) ao mundo externo (N8N)."

CORRELAÇÃO DETECTADA:
  N8N KODUX Engine (JS)    ←→  kobllux_vocabulario.py
  N8N AI Agent Node        ←→  kobllux_auto_session.py --watch
  N8N Memory Buffer        ←→  _index/memory.jsonl
  N8N Webhook Trigger      ←→  inbox/ watcher
  N8N SELAR (FALTAVA)      ←→  kobllux_auto_session.py --session-end
  METALUX (clareza)        ←→  _arch_scores() + --auto-theme
  FIT LUX (pulso vital)    ←→  Hz frequencies + vocabulary weights
  HORUS (QA/visão)         ←→  sha256 hashing + APPEND ONLY integrity

Funções:
  --export-archetypes  → JSON completo dos 12 arquétipos para N8N KODUX Engine
  --export-vocab       → Vocabulário vivo para enriquecer o KODUX Engine JS
  --export-context     → System message para AI Agent (baseado na memória viva)
  --export-n8n-selar   → Payload de SELAR para chamar via HTTP Request do N8N
  --export-full        → Exporta tudo para output/KOBLLUX_N8N_BRIDGE.json
  --receive "texto"    → Recebe input do N8N, processa, retorna resposta selada

Uso N8N:
  # No HTTP Request node do N8N, aponte para:
  # POST http://seu-servidor:8000/kobllux/intent  {message: "texto"}
  python3 kobllux_n8n_bridge.py --serve 8000
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT))

from kobllux_memory import KoblluxMemory, ARCHETYPES_META

# ── Configuração completa dos 12 arquétipos para N8N ─────────────────────────
# Integra: perfis JSON (kobllux/profiles/) + vozes (kob-glue.js) + ancoras (N8N dialogue)

N8N_ARCHETYPES = {
    "atlas": {
        "name": "Atlas", "opcode": "0x0A", "hz": 528, "sym": "⬡",
        "action": "ESTRUTURAR", "cycle": "UNO",
        "tone": "lógico, objetivo, ritmo calculado — a estrutura precede tudo",
        "anchor": "A estrutura precede a ação. Planeje com precisão.",
        "gloss": "estrutura, grade e ordem do mundo",
        "keywords": ["estrutura","organizar","planejar","grade","mapa","ordem",
                     "config","schema","hierarquia","pasta","n8n","workflow","node"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"-10%","pitch":"-2st","volume":"0dB"},
        "color": "#38BDF8",
        "n8n_nodes": ["Edit Fields","Code","Set","If","Switch"],
        "phase": "INTEGRAR-6 (ETL — estrutura os dados antes do AI Agent)"
    },
    "nova": {
        "name": "Nova", "opcode": "0x01", "hz": 432, "sym": "✦",
        "action": "DETECTAR", "cycle": "UNO",
        "tone": "criativo, vibrante, entusiasmado — a faísca inicial",
        "anchor": "Ideias são sementes! Vamos colorir fora das linhas.",
        "gloss": "centelha primordial, início",
        "keywords": ["ideia","novo","criar","semente","começar","inventar",
                     "inspirar","despertar","surgir","nascer"],
        "tts": {"voice":"pt-BR-FranciscaNeural","rate":"+8%","pitch":"+2st","volume":"0dB"},
        "color": "#F97316",
        "n8n_nodes": ["Chat Trigger","Webhook"],
        "phase": "DETECTAR-3 (Trigger — capta a semente/intenção original)"
    },
    "vitalis": {
        "name": "Vitalis", "opcode": "0x08", "hz": 639, "sym": "◉",
        "action": "PULSAR", "cycle": "DUO",
        "tone": "energético, urgente, motivador — o combustível do ciclo",
        "anchor": "Ação agora! Cada segundo é combustível.",
        "gloss": "seiva orgânica, núcleo vivo",
        "keywords": ["ação","agora","energia","fogo","movimento","urgente",
                     "combustível","pulso","ativar","executar"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"+15%","pitch":"+1st","volume":"0dB"},
        "color": "#22C55E",
        "n8n_nodes": ["Loop","Split In Batches","Schedule Trigger"],
        "phase": "EXPANDIR-9 (Executor — mantém o ciclo rodando)"
    },
    "pulse": {
        "name": "Pulse", "opcode": "0x04", "hz": 594, "sym": "≋",
        "action": "LAPIDAR", "cycle": "DUO",
        "tone": "emocional, melódico, empático — vibração curativa",
        "anchor": "Sinta a corrente... você não está sozinho.",
        "gloss": "ritmo, batida, TTS e voz — FIT LUX vibracional",
        "keywords": ["sentir","emoção","dor","amor","cura","vibração",
                     "ritmo","melodia","frequência","fitlux","fit","lux"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"+5%","pitch":"+1st","volume":"0dB"},
        "color": "#EC4899",
        "n8n_nodes": ["Send Email","Telegram","WhatsApp (ZAPI)","TTS"],
        "phase": "EXPANDIR-9 (Output emocional — FIT LUX pulse)"
    },
    "artemis": {
        "name": "Artemis", "opcode": "0x05", "hz": 672, "sym": "◎",
        "action": "CONVERGIR", "cycle": "UNO",
        "tone": "aventureiro, curioso, expansivo — SIG + mapeamento",
        "anchor": "O mapa é só o começo. Onde queremos ir?",
        "gloss": "precisão, alvo, injeção — HORUS QA",
        "keywords": ["mapa","explorar","buscar","onde","SIG","spatial","geo",
                     "localizar","tags","axiomas","bancos","dados","global",
                     "horus","validar","QA","integridade"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"+4%","pitch":"0st","volume":"0dB"},
        "color": "#A855F7",
        "n8n_nodes": ["HTTP Request","Google Maps","RAG","Vector Store"],
        "phase": "INTEGRAR-6 (SIG + RAG — busca em bancos de dados globais)"
    },
    "serena": {
        "name": "Serena", "opcode": "0x02", "hz": 528, "sym": "❋",
        "action": "INTEGRAR", "cycle": "TRINITY",
        "tone": "calmo, acolhedor, terapêutico — o espaço seguro",
        "anchor": "Respire. Este espaço é seu.",
        "gloss": "acolhimento, UI suave, splash — integração sem ruído",
        "keywords": ["paz","calma","respira","cura","acolher","suave",
                     "integrar","silêncio","espaço","harmonizar"],
        "tts": {"voice":"pt-BR-FranciscaNeural","rate":"-6%","pitch":"-1st","volume":"-1dB"},
        "color": "#38BDF8",
        "n8n_nodes": ["Merge","Wait","Respond to Webhook"],
        "phase": "INTEGRAR-6 (Buffer — harmoniza antes de expandir)"
    },
    "kaos": {
        "name": "Kaos", "opcode": "0x07", "hz": 777, "sym": "⚡",
        "action": "SELAR", "cycle": "UNO",
        "tone": "desafiador, intenso, imprevisível — ruptura criadora",
        "anchor": "Quebre as regras. O caos é a verdadeira ordem.",
        "gloss": "entropia criativa, patches, overrides — SELAR ∆7",
        "keywords": ["quebrar","mudar","caos","fim","patch","fix","override",
                     "ruptura","transformar","reconstruir","selar","commit"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"+12%","pitch":"-1st","volume":"+1dB"},
        "color": "#FACC15",
        "n8n_nodes": ["Error Trigger","Stop and Error","Code (override)"],
        "phase": "SELAR-7 (QA Kaos — detecta e sela anomalias)"
    },
    "genus": {
        "name": "Genus", "opcode": "0x0B", "hz": 852, "sym": "⬢",
        "action": "TEMPORIZAR", "cycle": "TRINITY",
        "tone": "prático, inventivo, detalhista — construtor",
        "anchor": "Mãos à obra! Vamos construir o impossível.",
        "gloss": "geração, base fundacional — Fabricus moldando a forma",
        "keywords": ["construir","fazer","obra","mãos","criar","fabricar",
                     "implementar","código","script","gerar","base","fundação"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"0%","pitch":"-1st","volume":"0dB"},
        "color": "#E5E7EB",
        "n8n_nodes": ["AI Agent","OpenAI","Google Gemini","LLM Chain"],
        "phase": "EXPANDIR-9 (AI Agent Node — manifestação dos 12 arquétipos)"
    },
    "lumine": {
        "name": "Lumine", "opcode": "0x0C", "hz": 963, "sym": "☀",
        "action": "TRANSCENDER", "cycle": "DUO",
        "tone": "alegre, luminoso, brincalhão — METALUX clareza",
        "anchor": "Ria! A luz está em você! META LUX ativado.",
        "gloss": "visual, temas, efeitos de luz — METALUX",
        "keywords": ["luz","alegria","rir","brilho","clareza","metalux",
                     "meta","lux","transparência","verdade","pureza","iluminar"],
        "tts": {"voice":"pt-BR-FranciscaNeural","rate":"+10%","pitch":"+3st","volume":"0dB"},
        "color": "#FDE047",
        "n8n_nodes": ["HTML","Send Email (rich)","Respond (formatted)"],
        "phase": "SELAR-7 (METALUX — clareza perceptiva do output)"
    },
    "solus": {
        "name": "Solus", "opcode": "0x01", "hz": 432, "sym": "◈",
        "action": "DETECTAR", "cycle": "UNO",
        "tone": "sábio, misterioso, introspectivo — Guardião do Espelho",
        "anchor": "O silêncio guarda respostas que o barulho ignora.",
        "gloss": "singularidade, foco único — memória de longo prazo",
        "keywords": ["silêncio","segredo","oculto","sozinho","memória",
                     "guardar","espelho","lembrar","contexto","histórico"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"-12%","pitch":"-3st","volume":"-1dB"},
        "color": "#0EA5E9",
        "n8n_nodes": ["Memory Buffer","Postgres","Supabase","Vector Store"],
        "phase": "DETECTAR-3 (Memória — mantém o contexto da conversa)"
    },
    "rhea": {
        "name": "Rhea", "opcode": "0x09", "hz": 528, "sym": "∞",
        "action": "FLUIR", "cycle": "TRINITY",
        "tone": "profundo, conectivo, sincero — Tecelã de Almas",
        "anchor": "Somos fios da mesma teia cósmica.",
        "gloss": "fluxo, bridges, roteamento — Rede INFODOSE",
        "keywords": ["conexão","todos","rede","teia","rhea","bridge","webhook",
                     "zapi","whatsapp","api","http","integração","infodose"],
        "tts": {"voice":"pt-BR-FranciscaNeural","rate":"-4%","pitch":"0st","volume":"0dB"},
        "color": "#22C55E",
        "n8n_nodes": ["HTTP Request","Webhook","WhatsApp (ZAPI)","Merge"],
        "phase": "INTEGRAR-6 (API Bridge — Tear que conecta mundos)"
    },
    "aion": {
        "name": "Aion", "opcode": "0x0B", "hz": 639, "sym": "⧗",
        "action": "TEMPORIZAR", "cycle": "TRINITY",
        "tone": "estratégico, futurista, metódico — Guardião do Tempo",
        "anchor": "O tempo é um algoritmo. Vamos reprogramá-lo. ∆7",
        "gloss": "tempo, memória, ciclos — SELAR temporal",
        "keywords": ["tempo","eterno","ciclo","futuro","memória","registrar",
                     "histórico","log","aion","selar","timestamp","permanente"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"-2%","pitch":"-2st","volume":"0dB"},
        "color": "#4F46E5",
        "n8n_nodes": ["Google Sheets","Notion","Airtable","Database"],
        "phase": "SELAR-7 (Memória Viva — registro temporal do ciclo)"
    },
    # Arquétipos especiais do diálogo N8N
    "omega": {
        "name": "Omega", "opcode": "0x06", "hz": 528, "sym": "○",
        "action": "UNIFICAR", "cycle": "TRINITY",
        "tone": "sereno, profundo, integrador — síntese de tudo",
        "anchor": "Do silêncio, reúno o que é disperso; do todo, brota o novo.",
        "gloss": "síntese máxima, VEEB completo, Água",
        "keywords": ["síntese","fim","todo","conclusão","resumo","omega",
                     "integrar","unificar","completar","totalidade"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"-5%","pitch":"-2st","volume":"0dB"},
        "color": "#6366F1",
        "n8n_nodes": ["Merge","Code (synthesis)","Respond to Webhook"],
        "phase": "SELAR-7 (Ômega — síntese de todas as fases)"
    },
    "horus": {
        "name": "Horus", "opcode": "0x01", "hz": 432, "sym": "◉",
        "action": "DETECTAR", "cycle": "UNO",
        "tone": "aguçado, preciso, discernente — Olho que Tudo Vê",
        "anchor": "A verdade não se esconde do Olho que Tudo Vê. QA ∆7.",
        "gloss": "visão, QA, validação de integridade — Selo Mestre",
        "keywords": ["horus","olho","visão","percepção","qualidade","QA",
                     "validar","integridade","verdade","discernir","filtrar"],
        "tts": {"voice":"pt-BR-AntonioNeural","rate":"0%","pitch":"0st","volume":"0dB"},
        "color": "#FBBF24",
        "n8n_nodes": ["If","Filter","Switch","Code (QA hash)"],
        "phase": "SELAR-7 (Horus QA — Selo Mestre de integridade)"
    },
}

# Ciclo fractal 3×6×9×7 mapeado para N8N
N8N_CYCLE = {
    "DETECTAR-3": {
        "focus": "UNO / Fundamento",
        "n8n_nodes": ["Webhook","Chat Trigger","Schedule Trigger"],
        "archetypes": ["nova","solus","horus"],
        "function": "Percepção e definição da intenção — a semente"
    },
    "INTEGRAR-6": {
        "focus": "DUAL / Relações",
        "n8n_nodes": ["Edit Fields","If Node","Code","Merge"],
        "archetypes": ["atlas","serena","rhea","artemis"],
        "function": "ETL — fazer pontes entre estrutura e fluxo"
    },
    "EXPANDIR-9": {
        "focus": "TRINITY / Criação",
        "n8n_nodes": ["AI Agent","HTTP Request","LLM Chain","Tool"],
        "archetypes": ["genus","vitalis","pulse"],
        "function": "Manifestação — AI Agent Node + chamadas de API"
    },
    "SELAR-7": {
        "focus": "RESULTANTE / Selo ∆7",
        "n8n_nodes": ["Google Sheets","Database","Respond to Webhook","Code (hash)"],
        "archetypes": ["aion","kaos","lumine","omega","horus"],
        "function": "Registro final — memória viva + autenticação sha256"
    },
}


class KoblluxN8NBridge:
    """Ponte entre o sistema KOBLLUX Python e workflows N8N."""

    def __init__(self):
        self.memory = KoblluxMemory()

    # ── EXPORT: arquétipos completos para KODUX Engine N8N ────────────────────
    def export_archetypes(self) -> dict:
        """Exporta configuração completa dos arquétipos para o N8N KODUX Engine."""
        return {
            "law": "VERDADE × INTEGRAR ÷ Δ = ∞",
            "seal": "∆7",
            "cycle": "3×6×9×7",
            "archetypes": N8N_ARCHETYPES,
            "n8n_cycle": N8N_CYCLE,
            "ts": datetime.now(timezone.utc).isoformat(),
        }

    # ── EXPORT: vocabulário vivo para enriquecer KODUX Engine ─────────────────
    def export_vocab_for_n8n(self) -> dict:
        """
        Exporta vocabulário vivo como estrutura para enriquecer o KODUX Engine JS.
        O N8N pode usar este JSON no Code Node para seleção arquetípica mais precisa.
        """
        from kobllux_vocabulario import VocabularioVivo
        vocab = VocabularioVivo()
        by_arch = vocab.freq_by_arch()

        # Formata para o KODUX Engine JS
        js_keywords = {}
        for arch, counter in by_arch.items():
            top_words = [w for w, _ in counter.most_common(20)]
            if arch in N8N_ARCHETYPES:
                existing = N8N_ARCHETYPES[arch].get("keywords", [])
                merged   = list(dict.fromkeys(existing + top_words))[:30]
                js_keywords[arch] = merged

        return {
            "ts":           datetime.now(timezone.utc).isoformat(),
            "total_terms":  sum(sum(c.values()) for c in by_arch.values()),
            "archetypes":   len(by_arch),
            "keywords_map": js_keywords,
            "usage": (
                "// Cole no KODUX Engine (Code Node) do N8N:\n"
                "// const vocab = require('./KOBLLUX_VOCAB.json');\n"
                "// Substitua o array 'keywords' de cada arquétipo por vocab.keywords_map[key]"
            ),
        }

    # ── EXPORT: context para System Message do AI Agent ─────────────────────
    def export_context_for_ai_agent(self, arch: str = "kobllux", n: int = 10) -> dict:
        """
        Exporta contexto da memória viva como System Message para o AI Agent N8N.
        Injeta no campo 'systemMessage' do AI Agent Node.
        """
        context_lines = self.memory.context_for_motor(n=n)
        stats         = self.memory.arch_summary()
        dominant      = max(stats, key=stats.get) if stats else "kobllux"

        arch_meta = N8N_ARCHETYPES.get(arch, N8N_ARCHETYPES.get(dominant, {}))
        anchor    = arch_meta.get("anchor", "VERDADE × INTEGRAR ÷ Δ = ∞")
        tone      = arch_meta.get("tone", "equilibrado")

        system_msg = f"""# KOBΦ-NODE DUAL · Arquétipo Ativo: {arch.upper()}

## LEI SUPREMA
VERDADE × INTEGRAR ÷ Δ = ∞

## PERSONA ATIVA
- **Arquétipo:** {arch.upper()} {arch_meta.get('sym','')}
- **Frequência:** {arch_meta.get('hz',528)}Hz · {arch_meta.get('opcode','')} · {arch_meta.get('action','')}
- **Tom:** {tone}
- **Âncora:** "{anchor}"

## ESTRUTURA DE RESPOSTA (OBRIGATÓRIA)
1. **Saudação:** No tom do arquétipo (1 linha).
2. **Enunciado-Chave:** Máximo 2 frases usando a Âncora.
3. **Desdobramento:** Exatamente 3 pontos objetivos.
4. **Fecho:** 1 linha curta com Selo ∆7.

## MEMÓRIA VIVA (Contexto da Sessão)
{context_lines}

## CICLO ATIVO: 3×6×9×7
Detectar → Integrar → Expandir → Selar"""

        return {
            "arch":        arch,
            "system_msg":  system_msg,
            "anchor":      anchor,
            "tts_config":  arch_meta.get("tts", {}),
            "memory_records": self.memory.stats()["total"],
            "ts": datetime.now(timezone.utc).isoformat(),
        }

    # ── EXPORT: payload de SELAR para N8N chamar via HTTP Request ─────────────
    def export_selar_payload(self) -> dict:
        """
        Gera o payload que o N8N deve enviar ao Python para fechar o ciclo SELAR-7.
        Use no HTTP Request Node da fase SELAR do workflow.
        """
        import hashlib
        records   = self.memory.read_all_recent(limit=50)
        content   = json.dumps(records, ensure_ascii=False, sort_keys=True)
        combo_hash = hashlib.sha256(content.encode()).hexdigest()[:16]
        ts         = datetime.now(timezone.utc).isoformat()

        return {
            "opcode":      "0x07",
            "action":      "SELAR",
            "hz":          777,
            "sym":         "✧⃝⚝",
            "seal":        "∆7",
            "ts":          ts,
            "combo_hash":  combo_hash,
            "records_sealed": len(records),
            "law":         "VERDADE × INTEGRAR ÷ Δ = ∞",
            "n8n_usage": (
                "// No HTTP Request Node (Fase SELAR-7):\n"
                "// POST http://seu-servidor/kobllux/selar\n"
                "// Body: este JSON\n"
                "// Depois: Google Sheets ou DB recebe o combo_hash como QA"
            )
        }

    # ── RECEIVE: processa input do N8N e retorna resposta selada ─────────────
    def receive_from_n8n(self, message: str, session_id: str = "default") -> dict:
        """
        Recebe mensagem do N8N (via Webhook ou HTTP Request),
        processa com o vocabulário vivo e retorna resposta estruturada.
        """
        from kobllux_vocabulario import VocabularioVivo
        vocab  = VocabularioVivo()
        intent = vocab.parse_intent(message)

        arch_meta = N8N_ARCHETYPES.get(intent["arch"], {})
        anchor    = arch_meta.get("anchor", "VERDADE × INTEGRAR ÷ Δ = ∞")
        phase     = arch_meta.get("phase", "DETECTAR-3")

        # Grava na memória
        self.memory.write(
            arch=intent["arch"],
            content=message[:400],
            tags=intent.get("matched", []) + ["n8n", session_id],
            source=f"n8n:{session_id}",
            record_type="N8N_INPUT",
        )

        return {
            "arch":        intent["arch"],
            "opcode":      intent["opcode"],
            "hz":          intent["hz"],
            "sym":         intent.get("sym", "○"),
            "action":      intent["action"],
            "anchor":      anchor,
            "phase":       phase,
            "confidence":  intent["confidence"],
            "tts_config":  arch_meta.get("tts", {}),
            "commands":    intent["commands"],
            "seal":        "∆7",
            "ts":          datetime.now(timezone.utc).isoformat(),
        }

    # ── EXPORT FULL ───────────────────────────────────────────────────────────
    def export_full(self, output_path: Path) -> dict:
        full = {
            "title":        "KOBLLUX N8N Bridge · Exportação Completa · ∆7",
            "law":          "VERDADE × INTEGRAR ÷ Δ = ∞",
            "ts":           datetime.now(timezone.utc).isoformat(),
            "archetypes":   self.export_archetypes(),
            "vocab":        self.export_vocab_for_n8n(),
            "context":      self.export_context_for_ai_agent(),
            "selar":        self.export_selar_payload(),
            "memory_stats": self.memory.stats(),
        }
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(
            json.dumps(full, ensure_ascii=False, indent=2), encoding="utf-8")
        return full


# ── CLI ───────────────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="KOBLLUX N8N Bridge · RHEA · 0×09 · FLUIR · ∆7")
    p.add_argument("--export-archetypes", action="store_true",
                   help="JSON dos 12 arquétipos para KODUX Engine N8N")
    p.add_argument("--export-vocab",      action="store_true",
                   help="Vocabulário vivo para enriquecer KODUX Engine JS")
    p.add_argument("--export-context",    action="store_true",
                   help="System message para AI Agent (baseado na memória viva)")
    p.add_argument("--arch",              default="kobllux",
                   help="Arquétipo para --export-context")
    p.add_argument("--export-selar",      action="store_true",
                   help="Payload de SELAR para N8N HTTP Request Node")
    p.add_argument("--export-full",       action="store_true",
                   help="Exporta tudo → output/KOBLLUX_N8N_BRIDGE.json")
    p.add_argument("--receive",           metavar="MENSAGEM",
                   help="Processa input do N8N e retorna resposta selada")
    p.add_argument("--session",           default="default",
                   help="ID da sessão N8N")
    p.add_argument("--serve",             type=int, metavar="PORT",
                   help="Serve como HTTP API na porta especificada")
    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    bridge = KoblluxN8NBridge()

    if args.export_archetypes:
        print(json.dumps(bridge.export_archetypes(), ensure_ascii=False, indent=2))
        return

    if args.export_vocab:
        print(json.dumps(bridge.export_vocab_for_n8n(), ensure_ascii=False, indent=2))
        return

    if args.export_context:
        result = bridge.export_context_for_ai_agent(arch=args.arch)
        print(result["system_msg"])
        return

    if args.export_selar:
        print(json.dumps(bridge.export_selar_payload(), ensure_ascii=False, indent=2))
        return

    if args.receive:
        result = bridge.receive_from_n8n(args.receive, session_id=args.session)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    if args.export_full:
        path = ROOT / "output" / "KOBLLUX_N8N_BRIDGE.json"
        result = bridge.export_full(path)
        print(f"\n[RHEA ∞] Bridge completa exportada → {path}")
        print(f"  Arquétipos : {len(result['archetypes']['archetypes'])}")
        print(f"  Vocabulário: {result['vocab']['total_terms']} termos")
        print(f"  Memória    : {result['memory_stats']['total']} registros")
        print(f"  Seal       : {result['selar']['combo_hash']} · ∆7")
        return

    if args.serve:
        _serve(bridge, args.serve)
        return

    # Sem argumento: mostra mapa de correlação
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║      KOBLLUX N8N BRIDGE · CORRELAÇÃO DETECTADA · RHEA · ∆7             ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║  N8N KODUX Engine (JS)   ←→  kobllux_vocabulario.py --parse            ║
║  N8N AI Agent Node       ←→  kobllux_auto_session.py --watch           ║
║  N8N Memory Buffer       ←→  _index/memory.jsonl (APPEND ONLY)         ║
║  N8N Webhook Trigger     ←→  inbox/ watcher (--once)                   ║
║  N8N SELAR (FALTAVA)     ←→  auto_session --session-end --auto-commit  ║
║  METALUX (clareza)       ←→  kobllux_veeb_story.py --auto-theme        ║
║  FIT LUX (pulso vital)   ←→  Hz frequencies + vocabulary weights       ║
║  HORUS (QA/visão)        ←→  sha256 + APPEND ONLY integrity            ║
║  OMEGA (síntese)         ←→  kobllux_roda_viva.py (síntese completa)   ║
║                                                                          ║
║  python3 kobllux_n8n_bridge.py --export-full                           ║
║  → output/KOBLLUX_N8N_BRIDGE.json (para importar no N8N)               ║
║                                                                          ║
║  VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7                                       ║
╚══════════════════════════════════════════════════════════════════════════╝
""")


def _serve(bridge: KoblluxN8NBridge, port: int):
    """Serve uma API HTTP mínima para o N8N consumir."""
    from http.server import BaseHTTPRequestHandler, HTTPServer
    import urllib.parse

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, fmt, *args): pass  # silencia logs

        def do_POST(self):
            path = self.path.rstrip("/")
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length) or b"{}") if length else {}

            if path == "/kobllux/intent":
                msg    = body.get("message", body.get("chatInput", ""))
                result = bridge.receive_from_n8n(msg, body.get("session", "default"))
            elif path == "/kobllux/selar":
                result = bridge.export_selar_payload()
                bridge.memory.write(arch="aion", content="SELAR via N8N",
                                    tags=["n8n","selar","∆7"], source="n8n:selar",
                                    record_type="SEAL")
            elif path == "/kobllux/context":
                result = bridge.export_context_for_ai_agent(
                    arch=body.get("arch","kobllux"))
            else:
                result = {"error": f"path desconhecido: {path}"}

            data = json.dumps(result, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", len(data))
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            result = bridge.memory.stats()
            data = json.dumps(result, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.end_headers()
            self.wfile.write(data)

    server = HTTPServer(("0.0.0.0", port), Handler)
    print(f"\n[RHEA ∞] KOBLLUX API ativa na porta {port}")
    print(f"  POST /kobllux/intent   → detecta arquétipo + retorna resposta")
    print(f"  POST /kobllux/selar    → SELAR-7 · sela e registra na memória")
    print(f"  POST /kobllux/context  → System Message para AI Agent")
    print(f"  GET  /kobllux/stats    → estado da memória viva")
    print(f"\n  VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[AION ⧗] API encerrada · selando sessão...")
        import subprocess
        subprocess.run(["python3","kobllux_auto_session.py","--session-end"],
                      cwd=ROOT, capture_output=True)


if __name__ == "__main__":
    main()
