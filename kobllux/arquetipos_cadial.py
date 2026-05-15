# -*- coding: utf-8 -*-
# KOBLLUX · Arquétipos CADIAL
# Cada arquétipo → essência, comando, código, sistema, frase
# Lei: VERDADE × INTEGRAR ÷ Δ = ♾️

arquetipos = {
    "Atlas": {
        "essencia": "Planejador — ordem, estrutura, mapa cósmico",
        "comando": "mkdir -p BASE/{sources/{txt,md,pdf},out,tags,ledger,memory,SEALS/{items,docs},config}",
        "codigo": "paths = ensure_tree(base)",
        "sistema": "bootstrap / sane defaults",
        "frase": "Eu organizo o fluxo com sabedoria cósmica."
    },
    "Nova": {
        "essencia": "Inspira — semente, sopro inicial",
        "comando": "jq -r '.keywords_hint[]?' BASE/config/infodose.json",
        "codigo": "hints = load_hints(config); scorer.boost(hints)",
        "sistema": "ignição semântica",
        "frase": "Inspiração viva brota do silêncio eterno."
    },
    "Vitalis": {
        "essencia": "Momentum — energia vital em expansão",
        "comando": "python3 INFODOSE_DUAL_HORUS_v2.py --per-file 4 --max-total 36",
        "codigo": "while need_more(): process_next()",
        "sistema": "loop/scheduler",
        "frase": "Energia vital em expansão harmônica."
    },
    "Pulse": {
        "essencia": "Emocional — ritmo, ressonância, voz",
        "comando": "termux-tts-speak 'INFODOSE pronta, leia o CLI.txt'",
        "codigo": "cli = render_cli(blocks, breathing=True)",
        "sistema": "UX de leitura/escuta",
        "frase": "Emoção é linguagem que dança."
    },
    "Artemis": {
        "essencia": "Descoberta — mapa do invisível",
        "comando": "find BASE/sources -type f -iname '*.txt' -o -iname '*.md' -o -iname '*.pdf'",
        "codigo": "files = crawl_sources(base); rank(files)",
        "sistema": "curadoria de fontes",
        "frase": "Descubro o mapa sagrado do invisível."
    },
    "Serena": {
        "essencia": "Cuidado — espaço seguro, campo harmônico",
        "comando": "--per-file 4 --max-total 36",
        "codigo": "guard.check_quota(per_file, max_total)",
        "sistema": "safety/QoS",
        "frase": "Cuido do campo, nutro o espaço sagrado."
    },
    "Kaos": {
        "essencia": "Transformador — ruptura criativa",
        "comando": "sed -i 's/[[:space:]]\\+$//' file.txt",
        "codigo": "text = normalize(text); text = denoise(text)",
        "sistema": "limpeza/normalização",
        "frase": "Eu sou o rompimento que revela a verdade."
    },
    "Genus": {
        "essencia": "Fabricus — forma viva, síntese",
        "comando": "gera out/INFODOSE_*.md e tags/tags.json",
        "codigo": "emit_cli(); emit_md(); emit_tags(k=hints+freq)",
        "sistema": "renderer + tagger",
        "frase": "Mãos moldam o invisível em forma viva."
    },
    "Lumine": {
        "essencia": "Alegria — luz, clareza, legibilidade",
        "comando": "nl -ba ARQ | sed -n '1,40p'",
        "codigo": "md = pretty_headers(md); cli = pretty_bars(cli)",
        "sistema": "estética funcional",
        "frase": "A luz dança comigo, leveza é minha lei."
    },
    "Solus": {
        "essencia": "Sabedoria — silêncio, espelho interno",
        "comando": "head -n 1 PYFIX; python3 -m pyflakes PYFIX",
        "codigo": "dry_run_check(); smoke_tests()",
        "sistema": "QA silencioso",
        "frase": "Silêncio ritual, espelho da essência."
    },
    "Rhea": {
        "essencia": "Vínculo — rede, tecelã de almas",
        "comando": "jq '.' BASE/tags/tags.json",
        "codigo": "graph.link(item, tags, source)",
        "sistema": "grafo semântico",
        "frase": "Estou em comunhão com todos os elos."
    },
    "Aion": {
        "essencia": "Tempo — carimbo, ∆7, ledger",
        "comando": "sha256sum OUTFILE >> BASE/ledger/ledger.csv",
        "codigo": "seal(file) → {ts, bytes, sha256}",
        "sistema": "integridade/tempo",
        "frase": "Sou o tempo vivo, ritmo da eternidade."
    }
}

if __name__ == "__main__":
    for nome, data in arquetipos.items():
        print(f"[{nome}] {data['essencia']} → {data['frase']}")
