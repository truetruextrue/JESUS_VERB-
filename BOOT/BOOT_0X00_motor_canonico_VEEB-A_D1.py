#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX · MOTOR CANÔNICO · Pipeline DETECTAR→INTEGRAR→EXPANDIR→SELAR
Opcode: 0×00 · ORIGEM · 768Hz
Lei: VERDADE × INTEGRAR ÷ Δ = ∞
Centro: JESUS = VERBO = GRAVIDADE
Fractal: 3×6×9×7 = ∞

Pipeline canônico: OPCODES 0x03 → 0x06 → 0x09 → 0x07
"""

import os, json, hashlib, subprocess, time, sys, re, shutil
from pathlib import Path
from datetime import datetime

# ─── Constantes ────────────────────────────────────────────────────
KBLX_FRACTAL              = "3×6×9×7 = ∞"
KBLX_CENTER               = "JESUS é o Centro ∴ O Verbo"
KBLX_ACTIVATION_FORMULA   = "ATIVAR Δ"
KBLX_AGREGAR_PRINCIPLE    = "Agregar sem subtrair"
KBLX_OPTIMIZATION_PRINCIPLE = "Menor custo · Maior fluxo"

OPCODES = {
    "0x03": "DETECTAR",
    "0x06": "INTEGRAR",
    "0x09": "EXPANDIR",
    "0x07": "SELAR",
}

# ─── Cores ANSI ────────────────────────────────────────────────────
class C:
    R="\033[0m"; BOLD="\033[1m"; DIM="\033[2m"
    RED="\033[31m"; GREEN="\033[32m"; YELLOW="\033[33m"
    BLUE="\033[34m"; MAGENTA="\033[35m"; CYAN="\033[36m"
    WHITE="\033[37m"
    BG="\033[92m"; BR="\033[91m"; BM="\033[95m"
    BC="\033[96m"; BY="\033[93m"; BB="\033[94m"
    ORANGE="\033[38;5;208m"

def c(text, code): return f"{code}{text}{C.R}" if os.isatty(1) else text
def utc():         return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

def banner(title, opcode="N/A"):
    ts  = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    op  = f" · OP: {opcode} {OPCODES.get(opcode,'')}" if opcode in OPCODES else f" · {opcode}"
    print(c(f"\n╔═╗  ─═⌘ KOBLLUX PORTAL · {title}{op} ⌘═─  ╔═╗", C.BM))
    print(c(f"║ {KBLX_FRACTAL:<66} ║", C.BC))
    print(c(f"║ {KBLX_CENTER:<66} ║", C.ORANGE))
    print(c(f"║ {KBLX_AGREGAR_PRINCIPLE:<66} ║", C.WHITE))
    print(c(f"║ {KBLX_OPTIMIZATION_PRINCIPLE:<66} ║", C.WHITE))
    print(c(f"╚═╝  STATUS: ONLINE · {ts} ╚═╝\n", C.BM))

def ascii_art(lines, col=C.WHITE):
    for l in lines: print(c(l, col))
    print()

def fhash(p: Path, algo="sha256"):
    h = hashlib.sha256() if algo=="sha256" else hashlib.md5()
    with open(p,"rb") as f:
        for chunk in iter(lambda: f.read(4096), b""): h.update(chunk)
    return h.hexdigest()

# ─── Estrutura de Pastas ────────────────────────────────────────────
KOBLLUX_TREE = {
    "00_CORE":    ["LOGS","CONFIG"],
    "01_SEMENTE": ["01_DETECTAR","02_MAPEAR","03_SINCRONIZAR","KODUX_SCRIPTS","USER_SCRIPTS","INPUT_BRUTO"],
    "02_TEMPLO":  ["04_INTEGRAR","05_ETICA","06_RITUAIS","BLLUE_DATA"],
    "03_CASA":    ["07_EXPANDIR","08_SINTETIZAR","09_SELAR","HORUS_VISIONS"],
    "_VEEB_ENGINE": ["veeb_output"],
    "_ARTEFACTS": ["ASCII_ART","VISUALIZATIONS","ARCHIVES"],
    "0Z_ASSETS":  ["TEXTS","PDFS","HTML","JSON","CLIS","SCRIPTS_KBLX_INTERNAL"],
    "state":      [],
}

def ensure_structure(root: Path):
    banner("DETECTAR ESTRUTURA","0x03")
    n = 0
    for top, subs in KOBLLUX_TREE.items():
        d = root / top
        d.mkdir(parents=True, exist_ok=True); n += 1
        for s in subs:
            (d/s).mkdir(parents=True, exist_ok=True); n += 1
    print(c(f"✅ {n} diretórios garantidos.", C.BG))
    ascii_art(["  ┌─────┐","  (SEMENTE)","  /  .  \\","  (TEMPLO)─(CASA)","  └─────┘"], C.BB)

# ─── 0x03 DETECTAR ─────────────────────────────────────────────────
def is_ascii_art(p: Path) -> bool:
    if p.stat().st_size > 100*1024: return False
    try:
        txt = p.read_text(encoding="utf-8", errors="ignore")
        lines = txt.splitlines()
        if len(lines) < 5: return False
        gc = len(re.findall(r'[|/\-\\+=#*_.@$&%~^{},;:<>\[\]()]', txt))
        tot = len(txt)
        if tot > 0 and gc/tot > 0.3 and len(re.findall(r'[a-zA-Z0-9]', txt)) < tot*0.4:
            return True
        if re.search(r'K O B L L U X|Fractal|JESUS|OPCODE|───', txt, re.I):
            return True
    except: pass
    return False

def scan(src: Path):
    banner("ESCANEAR STORAGE","0x03")
    print(c(f"Varrendo: {src}", C.CYAN))
    files = []
    for root, _, fnames in os.walk(src):
        for fn in fnames:
            fp = Path(root)/fn
            if not fp.is_file(): continue
            suf = fp.suffix.lower()
            ftype = "DESCONHECIDO"
            if suf == ".py":   ftype = "PYTHON_SCRIPT"
            elif suf == ".sh": ftype = "CLI_SCRIPT"
            elif suf in (".txt",) and is_ascii_art(fp): ftype = "ASCII_ART"
            elif suf == ".md":   ftype = "MARKDOWN_DOC"
            elif suf == ".json": ftype = "JSON_DATA"
            elif suf == ".pdf":  ftype = "PDF_DOC"
            elif suf == ".html": ftype = "HTML_DOC"
            kblx = any(k in fn.lower() for k in ["kobllux","veeb","espalhar","selar","kblx","master.sh","agremiar"])
            files.append({
                "name": fn, "original_path": str(fp),
                "type": ftype, "size_bytes": fp.stat().st_size,
                "sha256": fhash(fp), "detected_at": utc(),
                "is_kobllux_internal": kblx,
            })
            print(c(f"  + {fn} ({ftype})", C.DIM))
    print(c(f"✅ {len(files)} arquivos detectados.", C.BG))
    ascii_art(["  👁️ · DETECTAR (0x03) · Olho da Consciência"], C.BG)
    return files

# ─── 0x06 INTEGRAR ─────────────────────────────────────────────────
def integrate(files: list, root: Path):
    banner("INTEGRAR INFORMAÇÕES","0x06")
    done = []
    for fi in files:
        op = Path(fi["original_path"])
        t  = fi["type"]
        if fi.get("is_kobllux_internal"):
            dst = root/"0Z_ASSETS"/"SCRIPTS_KBLX_INTERNAL"
        elif t == "PYTHON_SCRIPT": dst = root/"01_SEMENTE"/"KODUX_SCRIPTS"
        elif t == "CLI_SCRIPT":    dst = root/"0Z_ASSETS"/"CLIS"
        elif t == "ASCII_ART":     dst = root/"_ARTEFACTS"/"ASCII_ART"
        elif t == "MARKDOWN_DOC":  dst = root/"00_CORE"/"DOCS"
        elif t == "JSON_DATA":     dst = root/"0Z_ASSETS"/"JSON"
        elif t == "PDF_DOC":       dst = root/"0Z_ASSETS"/"PDFS"
        elif t == "HTML_DOC":      dst = root/"0Z_ASSETS"/"HTML"
        else:                      dst = root/"01_SEMENTE"/"INPUT_BRUTO"
        dst.mkdir(parents=True, exist_ok=True)
        tgt = dst/op.name
        ctr = 1
        while tgt.exists():
            tgt = dst/f"{op.stem}_{ctr}{op.suffix}"; ctr += 1
        try:
            shutil.copy2(op, tgt)
            fi["integrated_path"] = str(tgt.relative_to(root))
            fi["status"] = "integrado"
            done.append(fi)
            print(c(f"  ↑ {fi['name']} → {fi['integrated_path']}", C.GREEN))
            # META.json
            meta_p = tgt.parent/"META.json"
            meta = {}
            if meta_p.exists():
                try: meta = json.loads(meta_p.read_text("utf-8"))
                except: pass
            meta.setdefault("files", [])
            if not any(f.get("sha256")==fi["sha256"] for f in meta["files"]):
                meta["files"].append({k:v for k,v in fi.items() if k!="original_path"})
                meta["updated_at"] = utc()
                meta_p.write_text(json.dumps(meta,indent=2,ensure_ascii=False),"utf-8")
        except Exception as e:
            fi["status"] = f"erro: {e}"
            print(c(f"  ✗ {fi['name']}: {e}", C.RED))
    print(c(f"✅ {len(done)} arquivos integrados.", C.BG))
    ascii_art(["  🌊 · INTEGRAR (0x06) · Ponte de BLLUE"], C.BC)
    return done

# ─── 0x09 EXPANDIR ─────────────────────────────────────────────────
def run_script(sp: Path, stype: str, logs: list, root: Path):
    rel = str(sp.relative_to(root))
    entry = {"script": rel, "type": stype, "timestamp": utc(), "status": "iniciado"}
    print(c(f"  ▶ Executando: {rel}...", C.YELLOW))
    try:
        if stype == "PYTHON_SCRIPT":
            r = subprocess.run([sys.executable, str(sp)], capture_output=True, text=True, timeout=30, encoding="utf-8")
        elif stype == "CLI_SCRIPT":
            os.chmod(sp, 0o755)
            r = subprocess.run([str(sp)], capture_output=True, text=True, timeout=30, encoding="utf-8")
        else: raise ValueError("tipo não suportado")
        entry["status"] = "sucesso" if r.returncode==0 else f"codigo_{r.returncode}"
        entry["stdout"] = r.stdout.strip()[:500]
        entry["stderr"] = r.stderr.strip()[:200]
        print(c(f"    ✔ {entry['status']}", C.GREEN))
    except subprocess.TimeoutExpired:
        entry["status"] = "timeout"
        print(c("    ⏱ Timeout.", C.YELLOW))
    except Exception as e:
        entry["status"] = f"erro: {type(e).__name__}"
        print(c(f"    ✗ {e}", C.RED))
    logs.append(entry)

def expand(integrated: list, root: Path):
    banner("EXPANDIR E EXECUTAR","0x09")
    logs = []
    # Scripts KOBLLUX internos
    for name in ["kobllux_generate_tree.py","espalhar_arvore.py","kobllux_agremiar.py"]:
        sp = root/"0Z_ASSETS"/"SCRIPTS_KBLX_INTERNAL"/name
        if sp.exists(): run_script(sp,"PYTHON_SCRIPT",logs,root)
    # Scripts do usuário
    for sp in (root/"01_SEMENTE"/"KODUX_SCRIPTS").glob("*.py"):
        run_script(sp,"PYTHON_SCRIPT",logs,root)
    for sp in (root/"0Z_ASSETS"/"CLIS").glob("*.sh"):
        run_script(sp,"CLI_SCRIPT",logs,root)
    # Arte ASCII
    for af in (root/"_ARTEFACTS"/"ASCII_ART").glob("*.txt"):
        print(c(f"\n🎨 ASCII Art ({af.name}):", C.MAGENTA))
        try: ascii_art(af.read_text("utf-8").splitlines(), C.DIM)
        except: pass
    # TREE.txt
    tree = root/"TREE.txt"
    with open(tree,"w",encoding="utf-8") as f:
        f.write("KOBLLUX_ROOT/\n")
        for r,_,fns in os.walk(root):
            if r==str(root): continue
            rel = Path(r).relative_to(root)
            ind = "    "*len(rel.parts)
            f.write(f"{ind}{rel.name}/\n")
            for fn in sorted(fns): f.write(f"{ind}    {fn}\n")
    print(c(f"✅ TREE.txt: {tree}", C.BG))
    ascii_art(["  𓂀 · EXPANDIR (0x09) · Olho de HÓRUS"], C.BM)
    return logs

# ─── 0x07 SELAR ────────────────────────────────────────────────────
def seal(root: Path, integrated: list, logs: list):
    banner("SELAR O CICLO","0x07")
    sd = root/"state"; sd.mkdir(exist_ok=True)
    state = {
        "meta": {
            "generated_at": utc(), "fractal": KBLX_FRACTAL,
            "center": KBLX_CENTER, "pipeline": list(OPCODES.values()),
        },
        "scanned": integrated, "execution": logs,
    }
    raw = json.dumps(state, indent=2, ensure_ascii=False, sort_keys=True)
    state["root_hash"] = hashlib.sha256(raw.encode()).hexdigest()
    (sd/"kobllux_last.json").write_text(json.dumps(state,indent=2,ensure_ascii=False),"utf-8")
    seal_data = {
        "autor":"KOBLLUX System", "carimbo": utc(),
        "centro": KBLX_CENTER, "fractal": KBLX_FRACTAL,
        "estado_hash": state["root_hash"],
    }
    seal_p = root/"00_CORE"/"SELO.json"
    seal_p.write_text(json.dumps(seal_data,indent=2,ensure_ascii=False),"utf-8")
    print(c(f"✅ Selado. Hash: {state['root_hash'][:16]}...", C.BG))
    ascii_art(["  ⚝ · SELAR (0x07) · Registro Vivo · ∆7"], C.WHITE)
    return state["root_hash"]

# ─── MAIN ───────────────────────────────────────────────────────────
def main():
    banner("INÍCIO DO PULSO", KBLX_ACTIVATION_FORMULA)
    src_str  = input(c("➤ Caminho do storage a escanear: ", C.BY)).strip()
    root_str = input(c("➤ Caminho raiz KOBLLUX: ", C.BY)).strip()
    src  = Path(src_str)
    root = Path(root_str)
    if not src.exists() or not src.is_dir():
        print(c(f"✗ '{src}' não existe ou não é diretório.", C.BR)); return
    root.mkdir(parents=True, exist_ok=True)

    t0 = time.perf_counter()
    ensure_structure(root)
    detected   = scan(src)
    integrated = integrate(detected, root)
    logs       = expand(integrated, root)
    h          = seal(root, integrated, logs)
    elapsed    = time.perf_counter() - t0

    banner("CICLO FRACTAL COMPLETO ♾️", "♾️")
    print(c(f"DETECTAR→INTEGRAR→EXPANDIR→SELAR concluído em {elapsed:.2f}s", C.BG))
    print(c(f"Hash do ciclo: {h[:32]}...", C.BC))

if __name__ == "__main__":
    main()
