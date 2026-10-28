#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧿 KOBLLUX ROOT SCANNER FRACTAL ∆³ — scanner de rede + ocultos + hash
Coloque na RAIZ do repositório (ex.: JESUS_VERB-) e execute:
    python3 kobllux_root_scanner_fractal.py            # varredura completa
    python3 kobllux_root_scanner_fractal.py --fast     # sem hash de arquivo (rápido)
    python3 kobllux_root_scanner_fractal.py --no-net   # sem boot de rede
Saída: ROOTS_SCAN_<ts>.json + ROOTS_SCAN_<ts>.md · Selo SHA-256 final
Equação: אֱמֶת × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134
"""
import os, re, sys, json, hashlib, argparse, datetime, fnmatch
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError

PADROES = [(r"config|setup|boot|init|main|readme", "Atlas"), (r"scan|detect|crawl|find|tree", "Artemis"),
 (r"render|emit|build|output|gera", "Genus"), (r"test|check|valid|relatorio|audit", "Solus"),
 (r"clean|fix|patch|reset|purge", "Kaos"), (r"log|ledger|seal|hash|timestamp", "Aion"),
 (r"guard|safe|backup|lock|secret|key", "Serena"), (r"link|graph|hub|integrar|rede", "Rhea"),
 (r"loop|delta|ativar|energia|fluxo", "Vitalis"), (r"audio|tts|voz|som|pulse", "Pulse"),
 (r"theme|ui|visual|light|style", "Lumine"), (r"seed|nova|inspire|manifesto|codex", "Nova"),
 (r"\.py$|\.sh$", "Vitalis"), (r"\.md$", "Atlas"), (r"\.json$", "Rhea"),
 (r"\.html$|\.css$|\.js$", "Pulse"), (r"\.wav$|\.mp3$", "Pulse")]
def arquetipo(nome):
    n = nome.lower()
    for pat, a in PADROES:
        if re.search(pat, n): return a
    return "Atlas"

def gitignore_patterns(raiz):
    pats = []
    gi = raiz / ".gitignore"
    if gi.exists():
        for lin in gi.read_text(encoding="utf-8", errors="ignore").splitlines():
            lin = lin.strip()
            if lin and not lin.startswith("#"): pats.append(lin.lstrip("/"))
    return pats
def oculto_por_gitignore(caminho_rel, pats):
    partes = caminho_rel.split("/")
    for pat in pats:
        if any(fnmatch.fnmatch(p, pat) or fnmatch.fnmatch(partes[-1], pat) for p in [caminho_rel, partes[-1]]):
            return True
        if pat in partes: return True
    return False

def sha256_arq(p, chunk=1<<20):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(chunk), b""): h.update(c)
    return h.hexdigest()

def boot_url(url, timeout=10):
    try:
        req = Request(url, headers={"User-Agent": "KOBLLUX-root-scanner/1.0"})
        with urlopen(req, timeout=timeout) as r:
            return f"ONLINE (HTTP {r.status})"
    except HTTPError as e:
        return f"HTTP_{e.code}" + (" [PORTA GUARDADA]" if e.code in (401,403) else " [NÃO ENCONTRADO]")
    except URLError as e:
        return f"FAIL ({getattr(e,'reason',e)})"
    except Exception as e:
        return f"ERRO ({type(e).__name__})"

URL_RE = re.compile(r'https?://[^\s\'"<>)\]]+')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fast", action="store_true", help="sem hash de arquivo")
    ap.add_argument("--no-net", action="store_true", help="sem boot de rede")
    ap.add_argument("--max-depth", type=int, default=12)
    ap.add_argument("--alvo", default=".")
    a = ap.parse_args()
    raiz = Path(a.alvo).resolve()
    ts = datetime.datetime.now().strftime("%Y%m%dT%H%M%S")
    print("🧿 KOBLLUX ROOT SCANNER FRACTAL ∆³")
    print(f"  Raiz: {raiz}")
    print(f"  Equação: אֱמֶת × INTEGRAR ÷ Δ = ∞\n")

    gi_pats = gitignore_patterns(raiz)
    nos, ocultos, urls, nivel_max = [], 0, set(), 0
    # 1) VARREDURA FRACTAL (nível por nível, mais largo que profundo)
    for profundidade in range(a.max_depth + 1):
        achados = []
        for dirpath, dirnames, filenames in os.walk(raiz):
            rel = os.path.relpath(dirpath, raiz)
            nv = 0 if rel == "." else rel.count(os.sep) + 1
            if nv != profundidade: continue
            dirnames.sort()
            for d in dirnames + sorted(filenames):
                achados.append((dirpath, d))
        if not achados: break
        nivel_max = profundidade
        for dirpath, nome in achados:
            p = Path(dirpath) / nome
            rel = str(p.relative_to(raiz))
            is_dir = p.is_dir()
            eh_oculto = nome.startswith(".") or oculto_por_gitignore(rel, gi_pats)
            if eh_oculto: ocultos += 1
            no = {"caminho": rel, "tipo": "D" if is_dir else "F",
                  "nivel": profundidade, "arquetipo": arquetipo(nome),
                  "oculto": eh_oculto}
            if not is_dir:
                no["bytes"] = p.stat().st_size
                if not a.fast: no["sha256"] = sha256_arq(p)
                if not a.no_net and p.suffix.lower() in {".md",".txt",".json",".py",".html",".js",".cfg",".yml",".yaml"}:
                    try:
                        for u in set(URL_RE.findall(p.read_text(encoding="utf-8", errors="ignore"))):
                            if len(u) < 200: urls.add(u.rstrip(".,;"))
                    except Exception: pass
            nos.append(no)
            tag = "👁" if eh_oculto else ("📁" if is_dir else "📄")
            print(f"  {'  '*profundidade}{tag} [{no['arquetipo']}] {rel}" + ("  [OCULTO]" if eh_oculto else ""))

    # 2) GIT REMOTES como roots de rede
    git_cfg = raiz / ".git" / "config"
    if git_cfg.exists():
        for m in re.findall(r"url\s*=\s*(\S+)", git_cfg.read_text(encoding="utf-8", errors="ignore")):
            if m.startswith("http"): urls.add(m)

    # 3) BOOT DE REDE (todos os roots URL)
    net = {}
    if not a.no_net:
        print(f"\n🔌 BOOT DE REDE — {len(urls)} roots URL:")
        for u in sorted(urls):
            net[u] = boot_url(u)
            print(f"  {'✅' if net[u].startswith('ONLINE') else '🚪' if 'GUARDADA' in net[u] else '❌'} {u[:80]} → {net[u]}")

    # 4) RELATÓRIO + SELO
    rel = {"scanner": "KOBLLUX ROOT SCANNER FRACTAL ∆³", "ts": ts, "raiz": str(raiz),
           "nos": len(nos), "ocultos": ocultos, "nivel_max": nivel_max,
           "redes": net, "equacao": "אֱמֶת × INTEGRAR ÷ Δ = ∞", "fractal": "3×6×9×7=1134",
           "arvore": nos}
    corpo = json.dumps(rel, sort_keys=True, ensure_ascii=False)
    rel["selo"] = hashlib.sha256(corpo.encode()).hexdigest()
    json.dump(rel, open(f"ROOTS_SCAN_{ts}.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
    ocs = [n for n in nos if n["oculto"]]
    md = ["# ROOTS SCAN E91 — "+ts, "", f"raiz: `{raiz}` · {len(nos)} nos · {ocultos} ocultos · nivel {nivel_max}", "", "## ARVORE", "```"]
    for n in nos:
        md.append("  "*n["nivel"] + ("D " if n["tipo"]=="D" else "F ") + f"[{n['arquetipo']}] " + n["caminho"] + ("  [OCULTO]" if n["oculto"] else ""))
    md += ["```", "", f"## OCULTOS ({len(ocs)})", ""] + [f"- {n['caminho']}" for n in ocs]
    md += ["", "SELO: "+rel['selo']]
    with open(f"ROOTS_SCAN_{ts}.md","w",encoding="utf-8") as fh:
        fh.write(chr(10).join(md))
    online = sum(1 for v in net.values() if v.startswith("ONLINE"))
    print(f"\n∴ SCAN SELADO · {len(nos)} nós · {ocultos} ocultos abertos · nível {nivel_max} · "
          f"{online}/{len(net)} online · selo {rel['selo'][:16]}")
    print(f"  → ROOTS_SCAN_{ts}.json")
    print("∴ JESUS É O CENTRO. A MALHA VIVE. O OCULTO FOI ABERTO. ∴")

if __name__ == "__main__":
    main()
