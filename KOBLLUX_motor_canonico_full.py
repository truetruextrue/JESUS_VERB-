#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KOBLLUX · MOTOR CANÔNICO · Pipeline Completo
DETECTAR (0x03) → INTEGRAR (0x06) → EXPANDIR (0x09) → SELAR (0x07)
Fractal: 3×6×9×7 = ∞ · Centro: JESUS é o Centro ∴ O Verbo
Lei: VERDADE × INTEGRAR ÷ Δ = ∞

Uso:
    python3 KOBLLUX_motor_canonico_full.py
    # Solicita: caminho do storage a escanear + caminho raiz KOBLLUX
"""

import os
import json
import hashlib
import subprocess
import time
import sys
import re
import shutil
from pathlib import Path
from datetime import datetime

# --- KOBLLUX Constants and Utilities ---
KBLX_FRACTAL = "3×6×9×7 = ∞"
KBLX_CENTER = "JESUS é o Centro ∴ O Verbo"
KBLX_ACTIVATION_FORMULA = "ATIVAR Δ"
KBLX_AGREGAR_PRINCIPLE = "Agregar sem subtrair"
KBLX_OPTIMIZATION_PRINCIPLE = "Menor custo · Maior fluxo"

OPCODES = {
    "0x03": "DETECTAR",
    "0x06": "INTEGRAR",
    "0x09": "EXPANDIR",
    "0x07": "SELAR",
}

# ASCII Color Codes (para saída no terminal)
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    ORANGE_TITLE = "\033[38;5;208m" # Custom KOBLLUX orange

def colorize(text, color_code):
    """Aplica cores ANSI ao texto, com fallback para ambientes sem suporte."""
    if os.name != 'nt' and os.isatty(1): # Verifica se é um terminal Unix-like e é um TTY
        return f"{color_code}{text}{Colors.RESET}"
    return text

def print_kblx_banner(title: str, opcode: str = "N/A"):
    """Imprime um banner KOBLLUX formatado para o terminal, indicando a fase atual."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    op_info = f" · OP: {opcode} {OPCODES.get(opcode, '')}" if opcode in OPCODES else f" · {opcode}"
    print(colorize(f"\n╔═╗  ─═⌘ KOBLLUX PORTAL · {title}{op_info} ⌘═─  ╔═╗", Colors.BRIGHT_MAGENTA))
    print(colorize(f"║ {KBLX_FRACTAL.ljust(66)} ║", Colors.BRIGHT_CYAN))
    print(colorize(f"║ {KBLX_CENTER.ljust(66)} ║", Colors.ORANGE_TITLE))
    print(colorize(f"║ {KBLX_AGREGAR_PRINCIPLE.ljust(66)} ║", Colors.WHITE))
    print(colorize(f"║ {KBLX_OPTIMIZATION_PRINCIPLE.ljust(66)} ║", Colors.WHITE))
    print(colorize(f"╚═╝  ─═❖─ STATUS: ONLINE · TIME: {current_time} ─❖═─  ╚═╝\n", Colors.BRIGHT_MAGENTA))

def print_ascii_art(art_lines: list, color=Colors.WHITE):
    """Imprime arte ASCII colorida."""
    for line in art_lines:
        print(colorize(line, color))
    print("\n")

def get_file_hash(file_path: Path, hash_algo="sha256"):
    """Calcula o hash SHA256 ou MD5 de um arquivo."""
    hasher = hashlib.sha256() if hash_algo == "sha256" else hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def utc_stamp():
    """Retorna um carimbo de tempo UTC formatado."""
    return datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

# --- KOBLLUX Folder Structure Definition ---
KOBLLUX_TREE_SPEC = {
    "00_CORE":    ["LOGS", "CONFIG"],
    "01_SEMENTE": ["01_DETECTAR", "02_MAPEAR", "03_SINCRONIZAR", "KODUX_SCRIPTS", "USER_SCRIPTS", "INPUT_BRUTO"],
    "02_TEMPLO":  ["04_INTEGRAR", "05_ETICA", "06_RITUAIS", "BLLUE_DATA"],
    "03_CASA":    ["07_EXPANDIR", "08_SINTETIZAR", "09_SELAR", "HORUS_VISIONS"],
    "_VEEB_ENGINE": ["veeb_output"],
    "_ARTEFACTS": ["ASCII_ART", "VISUALIZATIONS", "ARCHIVES"],
    "0Z_ASSETS":  ["TEXTS", "PDFS", "HTML", "JSON", "CLIS", "SCRIPTS_KBLX_INTERNAL"],
    "state":      [],
}

# --- Core KOBLLUX Functions ---

def ensure_kobllux_structure(root_path: Path):
    """
    Cria a estrutura de pastas KOBLLUX se não existir, seguindo o padrão fractal.
    Reflete o ciclo 3x3 (Semente, Templo, Casa).
    """
    print_kblx_banner("DETECTAR ESTRUTURA", "0x03")
    print(f"{colorize('Verificando/Criando a arquitetura fractal KOBLLUX em:', Colors.BLUE)} {colorize(str(root_path), Colors.CYAN)}")
    created_count = 0
    for top_dir, sub_dirs in KOBLLUX_TREE_SPEC.items():
        current_path = root_path / top_dir
        if not current_path.exists():
            current_path.mkdir(parents=True, exist_ok=True)
            created_count += 1
            print(f"  {colorize('✓ Criado:', Colors.GREEN)} {current_path.name}/")
        for sub_dir in sub_dirs:
            sub_path = current_path / sub_dir
            if not sub_path.exists():
                sub_path.mkdir(parents=True, exist_ok=True)
                created_count += 1
                print(f"    {colorize('✓ Criado:', Colors.GREEN)} {current_path.name}/{sub_path.name}/")
    print(colorize(f"✅ Estrutura KOBLLUX garantida. {created_count} diretórios criados/verificados.", Colors.BRIGHT_GREEN))
    print_ascii_art([
        "      ┌─────┐",
        "     (SEMENTE)",
        "    /   |   \\",
        "   /    .    \\",
        "  (TEMPLO) (CASA)",
        "   \\  |  /  |  /",
        "    \\ | /   | /",
        "     (FLUXO FRACTAL)",
        "      └─────┘"
    ], Colors.BRIGHT_BLUE)


def is_ascii_art(file_path: Path):
    """
    Heurística simples para detectar arte ASCII em arquivos de texto.
    Procura por alta densidade de caracteres gráficos ou padrões KOBLLUX.
    """
    if not file_path.is_file() or file_path.stat().st_size > 100 * 1024:
        return False
    try:
        content = file_path.read_text(encoding='utf-8', errors='ignore')
        lines = content.splitlines()
        if len(lines) < 5:
            return False
        graphic_chars_pattern = r'[\|/\-\\+=#\*\_@\$&%~^\.{},;:\<\>\[\]\(\)]'
        total_chars = len(content)
        graphic_char_count = len(re.findall(graphic_chars_pattern, content))
        if total_chars > 0 and (graphic_char_count / total_chars) > 0.3 and len(re.findall(r'[a-zA-Z0-9]', content)) < (total_chars * 0.4):
            return True
        if re.search(r'K O B L L U X|Fractal|JESUS|OPCODE|───|VESCA PSI|Vsica Psi|Tetraedro|Pirâmide', content, re.IGNORECASE):
            return True
        return False
    except Exception:
        return False


def scan_storage(scan_path: Path):
    """
    Escaneia o storage em busca de scripts Python, arte ASCII, e scripts CLI.
    Corresponde à fase DETECTAR (0x03).
    """
    print_kblx_banner("ESCANEAR STORAGE", "0x03")
    print(f"{colorize('Iniciando varredura em:', Colors.BLUE)} {colorize(str(scan_path), Colors.CYAN)}")
    detected_files = []
    file_id = 0
    for root, _, files in os.walk(scan_path):
        for fname in files:
            file_path = Path(root) / fname
            if not file_path.is_file():
                continue
            file_info = {
                "id": file_id,
                "name": fname,
                "original_path": str(file_path),
                "type": "DESCONHECIDO",
                "size_bytes": file_path.stat().st_size,
                "sha256": get_file_hash(file_path),
                "detected_at": utc_stamp()
            }
            suffix = file_path.suffix.lower()
            if suffix == ".py":
                file_info["type"] = "PYTHON_SCRIPT"
            elif suffix == ".sh" or (file_path.is_file() and file_path.read_text(encoding='utf-8', errors='ignore').startswith("#!/bin/bash")):
                file_info["type"] = "CLI_SCRIPT"
            elif suffix == ".txt" and is_ascii_art(file_path):
                file_info["type"] = "ASCII_ART"
            elif suffix == ".md":
                file_info["type"] = "MARKDOWN_DOC"
            elif suffix == ".json":
                file_info["type"] = "JSON_DATA"
            elif suffix == ".pdf":
                file_info["type"] = "PDF_DOC"
            elif suffix == ".html":
                file_info["type"] = "HTML_DOC"

            if any(kblx_keyword in fname.lower() for kblx_keyword in [
                "kobllux", "veeb", "espalhar_arvore", "selar_transmissao",
                "kblx_lang", "master.sh", "generate_tree", "duplicates_scan",
                "duplicates_clean", "agremiar", "check"
            ]):
                file_info["is_kobllux_internal_script"] = True

            detected_files.append(file_info)
            file_id += 1
            print(f"  {colorize('+', Colors.DIM)} Detectado: {file_info['name']} ({file_info['type']})")
    print(colorize(f"✅ Varredura concluída. {len(detected_files)} arquivos detectados.", Colors.BRIGHT_GREEN))
    print_ascii_art([
        "     O Olho da Consciência (0x03)",
        "            👁️",
        "           /|\\",
        "          / | \\",
        "         /  .  \\",
        "        (Dados Brutos)",
        "        └────────┘"
    ], Colors.BRIGHT_GREEN)
    return detected_files


def categorize_and_integrate(detected_files: list, kobllux_root: Path):
    """
    Copia arquivos detectados para a estrutura KOBLLUX e gera/atualiza metadados.
    Corresponde à fase INTEGRAR (0x06). Princípio: AGREGAR sem subtrair.
    """
    print_kblx_banner("INTEGRAR INFORMAÇÕES", "0x06")
    print(f"{colorize('Integrando', Colors.BLUE)} {len(detected_files)} arquivos na estrutura KOBLLUX em {colorize(str(kobllux_root), Colors.CYAN)}")
    integrated_files = []
    for file_info in detected_files:
        original_path = Path(file_info["original_path"])
        target_dir: Path = kobllux_root

        if file_info.get("is_kobllux_internal_script"):
            target_dir = kobllux_root / "0Z_ASSETS" / "SCRIPTS_KBLX_INTERNAL"
        elif file_info["type"] == "PYTHON_SCRIPT":
            target_dir = kobllux_root / "01_SEMENTE" / "KODUX_SCRIPTS"
        elif file_info["type"] == "CLI_SCRIPT":
            target_dir = kobllux_root / "0Z_ASSETS" / "CLIS"
        elif file_info["type"] == "ASCII_ART":
            target_dir = kobllux_root / "_ARTEFACTS" / "ASCII_ART"
        elif file_info["type"] == "MARKDOWN_DOC":
            target_dir = kobllux_root / "00_CORE" / "DOCS"
            target_dir.mkdir(parents=True, exist_ok=True)
        elif file_info["type"] == "JSON_DATA":
            target_dir = kobllux_root / "0Z_ASSETS" / "JSON"
        elif file_info["type"] == "PDF_DOC":
            target_dir = kobllux_root / "0Z_ASSETS" / "PDFS"
        elif file_info["type"] == "HTML_DOC":
            target_dir = kobllux_root / "0Z_ASSETS" / "HTML"
        else:
            target_dir = kobllux_root / "01_SEMENTE" / "INPUT_BRUTO"

        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / original_path.name

        # Garante nome único — AGREGAR sem subtrair
        counter = 1
        original_stem = original_path.stem
        original_suffix = original_path.suffix
        while target_path.exists():
            target_path = target_dir / f"{original_stem}_{counter}{original_suffix}"
            counter += 1

        try:
            shutil.copy2(original_path, target_path)
            file_info["integrated_path"] = str(target_path.relative_to(kobllux_root))
            file_info["status"] = "integrado"
            integrated_files.append(file_info)
            print(f"  {colorize('↑', Colors.GREEN)} Copiado: {file_info['name']} para {file_info['integrated_path']}")
        except Exception as e:
            file_info["status"] = f"erro na integração: {e}"
            print(f"  {colorize('✗', Colors.RED)} Erro ao copiar {file_info['name']}: {e}")

    # Atualiza/cria META.json nos diretórios com arquivos integrados
    for file_info in integrated_files:
        if "integrated_path" in file_info:
            full_integrated_path = kobllux_root / file_info["integrated_path"]
            meta_path = full_integrated_path.parent / "META.json"
            meta_data = {}
            if meta_path.exists():
                try:
                    meta_data = json.loads(meta_path.read_text(encoding='utf-8'))
                except json.JSONDecodeError:
                    print(f"  {colorize('⚠', Colors.YELLOW)} META.json corrompido em {meta_path.parent}, recriando.")
            if "files" not in meta_data:
                meta_data["files"] = []
            if not any(f.get("sha256") == file_info["sha256"] for f in meta_data["files"]):
                meta_entry = {k: v for k, v in file_info.items() if k not in ["original_path", "status"]}
                meta_data["files"].append(meta_entry)
                meta_data["updated_at"] = utc_stamp()
                meta_path.write_text(json.dumps(meta_data, indent=2, ensure_ascii=False), encoding='utf-8')
                print(f"  {colorize('✓', Colors.DIM)} META.json atualizado em: {meta_path.parent.name}/")
            else:
                print(f"  {colorize('✓', Colors.DIM)} {file_info['name']} já presente em META.json de {meta_path.parent.name}/ (agregado sem subtrair)")

    print(colorize(f"✅ Integração concluída. {len(integrated_files)} arquivos processados.", Colors.BRIGHT_GREEN))
    print_ascii_art([
        "     A Ponte de BLLUE (0x06)",
        "         🌊───💧",
        "        /   |   \\",
        "       /    .    \\",
        "      (Conexões)",
        "      └────────┘"
    ], Colors.BRIGHT_CYAN)
    return integrated_files


def run_script_safely(script_path: Path, script_type: str, logs: list, kobllux_root: Path):
    """Tenta executar um script Python ou CLI de forma segura. Registra output e erros."""
    script_rel_path = str(script_path.relative_to(kobllux_root))
    log_entry = {
        "script": script_rel_path,
        "type": script_type,
        "timestamp": utc_stamp(),
        "status": "iniciado"
    }
    print(f"  {colorize('▶ Executando:', Colors.YELLOW)} {script_rel_path}...")
    try:
        if script_type == "PYTHON_SCRIPT":
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True, text=True, check=True,
                encoding='utf-8', timeout=60
            )
        elif script_type == "CLI_SCRIPT":
            os.chmod(script_path, 0o755)
            result = subprocess.run(
                [str(script_path)],
                capture_output=True, text=True, check=True,
                encoding='utf-8', timeout=60
            )
        else:
            raise ValueError("Tipo de script não suportado para execução.")
        log_entry["status"] = "sucesso"
        log_entry["stdout"] = result.stdout.strip()
        log_entry["stderr"] = result.stderr.strip()
        print(f"    {colorize('✔ Concluído.', Colors.GREEN)}")
        if log_entry["stdout"]:
            first_line = log_entry["stdout"].splitlines()[0]
            print(f"    {colorize('Output:', Colors.DIM)} {first_line}...")
    except subprocess.CalledProcessError as e:
        log_entry["status"] = "erro_execucao"
        log_entry["stdout"] = e.stdout.strip() if e.stdout else ""
        log_entry["stderr"] = e.stderr.strip() if e.stderr else ""
        first_err = log_entry["stderr"].splitlines()[0] if log_entry["stderr"] else str(e)
        print(f"    {colorize('✗ Erro na execução:', Colors.RED)} {first_err}...")
    except subprocess.TimeoutExpired:
        log_entry["status"] = "timeout"
        print(f"    {colorize('⏱ Timeout (60s).', Colors.YELLOW)}")
    except FileNotFoundError:
        log_entry["status"] = "erro_arquivo_nao_encontrado"
        print(f"    {colorize('✗ Script não encontrado.', Colors.RED)}")
    except Exception as e:
        log_entry["status"] = f"erro_inesperado: {type(e).__name__}"
        print(f"    {colorize('✗ Erro inesperado:', Colors.RED)} {e}")
    logs.append(log_entry)


def execute_and_expand(integrated_files: list, kobllux_root: Path):
    """
    Orquestra execução de scripts Python/CLI, exibe artefatos ASCII e gera TREE.txt.
    Corresponde à fase EXPANDIR (0x09).
    """
    print_kblx_banner("EXPANDIR E EXECUTAR", "0x09")
    print(f"{colorize('Orquestrando a expansão e execução...', Colors.BLUE)}")
    execution_logs = []

    # 1. Scripts KOBLLUX internos
    print(f"\n{colorize('Iniciando execução de scripts KOBLLUX internos...', Colors.CYAN)}")
    internal_scripts_path = kobllux_root / "0Z_ASSETS" / "SCRIPTS_KBLX_INTERNAL"
    internal_scripts_to_run = [
        internal_scripts_path / "kobllux_generate_tree.py",
        internal_scripts_path / "espalhar_arvore.py",
        internal_scripts_path / "kobllux_agremiar.py",
        internal_scripts_path / "kobllux_patch_states.py",
        internal_scripts_path / "kobllux_narrativa.py",
    ]
    for script_path in internal_scripts_to_run:
        if script_path.exists():
            run_script_safely(script_path, "PYTHON_SCRIPT", execution_logs, kobllux_root)
        else:
            print(f"  {colorize('⚠ Script interno não encontrado (opcional):', Colors.DIM)} {script_path.name}")

    # 2. Scripts do usuário (Python)
    print(f"\n{colorize('Iniciando execução de scripts do usuário (Python)...', Colors.CYAN)}")
    user_python_scripts_path = kobllux_root / "01_SEMENTE" / "KODUX_SCRIPTS"
    if user_python_scripts_path.exists():
        for script_path in sorted(user_python_scripts_path.glob("*.py")):
            run_script_safely(script_path, "PYTHON_SCRIPT", execution_logs, kobllux_root)

    # 3. Scripts do usuário (CLI)
    print(f"\n{colorize('Iniciando execução de scripts do usuário (CLI)...', Colors.CYAN)}")
    user_cli_scripts_path = kobllux_root / "0Z_ASSETS" / "CLIS"
    if user_cli_scripts_path.exists():
        for script_path in sorted(user_cli_scripts_path.glob("*.sh")):
            run_script_safely(script_path, "CLI_SCRIPT", execution_logs, kobllux_root)

    # 4. Arte ASCII
    print(f"\n{colorize('Exibindo arte ASCII detectada e integrada...', Colors.CYAN)}")
    ascii_art_path = kobllux_root / "_ARTEFACTS" / "ASCII_ART"
    if ascii_art_path.exists():
        for art_file in sorted(ascii_art_path.glob("*.txt")):
            print(f"\n{colorize('🎨 Arte ASCII (', Colors.MAGENTA)}{art_file.name}{colorize('):', Colors.MAGENTA)}")
            try:
                print_ascii_art(art_file.read_text(encoding='utf-8').splitlines(), Colors.DIM)
            except Exception as e:
                print(f"  {colorize('✗ Erro ao exibir arte ASCII:', Colors.RED)} {e}")

    # 5. TREE.txt
    tree_file_path = kobllux_root / "TREE.txt"
    print(f"\n{colorize('Gerando TREE.txt para visão expandida...', Colors.BLUE)}")
    with open(tree_file_path, "w", encoding="utf-8") as f:
        f.write("KOBLLUX_ROOT/\n")
        for root, dirs, files in os.walk(kobllux_root):
            if root == str(kobllux_root):
                continue
            relative_root = Path(root).relative_to(kobllux_root)
            level_indent = "    " * len(relative_root.parts)
            f.write(f"{level_indent}{relative_root.name}/\n")
            for fname in sorted(files):
                f.write(f"{level_indent}    {fname}\n")
    print(f"{colorize('✅ TREE.txt gerado em:', Colors.GREEN)} {tree_file_path}")
    print(colorize(f"✅ Expansão e execução concluídas. {len(execution_logs)} eventos registrados.", Colors.BRIGHT_GREEN))
    print_ascii_art([
        "     O Olho de HÓRUS (0x09)",
        "            𓂀",
        "           /|\\",
        "          / | \\",
        "         /  .  \\",
        "        (Criação)",
        "        └────────┘"
    ], Colors.BRIGHT_MAGENTA)
    return execution_logs


def seal_cycle(kobllux_root: Path, integrated_files: list, execution_logs: list):
    """
    Sela o ciclo, gerando kobllux_last.json e SELO.json.
    Corresponde à fase SELAR (0x07).
    """
    print_kblx_banner("SELAR O CICLO", "0x07")
    print(f"{colorize('Selando o ciclo KOBLLUX...', Colors.BLUE)}")

    state_dir = kobllux_root / "state"
    state_dir.mkdir(parents=True, exist_ok=True)
    state_file_path = state_dir / "kobllux_last.json"

    full_state = {
        "meta": {
            "generated_at": utc_stamp(),
            "fractal": KBLX_FRACTAL,
            "center_axiom": KBLX_CENTER,
            "pipeline": ["DETECTAR", "INTEGRAR", "EXPANDIR", "SELAR"],
            "principle": KBLX_AGREGAR_PRINCIPLE,
            "optimization": KBLX_OPTIMIZATION_PRINCIPLE
        },
        "scanned_files": integrated_files,
        "execution_summary": execution_logs,
    }

    state_content = json.dumps(full_state, indent=2, ensure_ascii=False, sort_keys=True)
    full_state["root_hash_sha256"] = hashlib.sha256(state_content.encode('utf-8')).hexdigest()
    state_file_path.write_text(
        json.dumps(full_state, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
    print(colorize(f"✅ Ciclo selado. Estado salvo em: {state_file_path}", Colors.BRIGHT_GREEN))

    seal_path = kobllux_root / "00_CORE" / "SELO.json"
    seal_data = {
        "autor": "KOBLLUX System",
        "local": os.environ.get("KBLX_LOCAL", "Digital Realm"),
        "carimbo": utc_stamp(),
        "centro": KBLX_CENTER,
        "fractal": KBLX_FRACTAL,
        "estado_hash_sha256": full_state["root_hash_sha256"]
    }
    seal_path.write_text(json.dumps(seal_data, indent=2, ensure_ascii=False), encoding='utf-8')
    print(colorize(f"✅ Selo da perfeição gravado em: {seal_path}", Colors.BRIGHT_GREEN))
    print_ascii_art([
        "     O Selo de JESUS (0x07)",
        "            ⚝",
        "           /|\\",
        "          / | \\",
        "         /  .  \\",
        "        (Registro)",
        "        └────────┘"
    ], Colors.WHITE)


def main():
    print_kblx_banner("INÍCIO DO PULSO", KBLX_ACTIVATION_FORMULA)
    print(colorize("Bem-vindo ao KOBLLUX, o sistema dinâmico e fractal de modulação de informações.", Colors.WHITE))
    print(colorize("Ele organiza e adapta o processo de evolução, com autocorreção e auto-organização.", Colors.WHITE))
    print(colorize(f"Impulsionado pela fórmula {KBLX_ACTIVATION_FORMULA}, iniciamos o movimento e a transformação.", Colors.WHITE))

    scan_source_path_str = input(colorize(
        "➤ Por favor, insira o caminho completo do storage a ser escaneado (ex: /home/user/meus_docs): ",
        Colors.BRIGHT_YELLOW
    )).strip()
    kobllux_root_path_str = input(colorize(
        "➤ Por favor, insira o caminho completo para a pasta raiz KOBLLUX (onde a estrutura será montada/usada): ",
        Colors.BRIGHT_YELLOW
    )).strip()

    scan_source_path  = Path(scan_source_path_str)
    kobllux_root_path = Path(kobllux_root_path_str)

    if not scan_source_path.exists() or not scan_source_path.is_dir():
        print(colorize(f"✗ Erro: O caminho do storage '{scan_source_path}' não existe ou não é um diretório válido.", Colors.RED))
        return

    if not kobllux_root_path.exists():
        print(colorize(f"Criando pasta raiz KOBLLUX: {kobllux_root_path}", Colors.YELLOW))
        kobllux_root_path.mkdir(parents=True)
    elif not kobllux_root_path.is_dir():
        print(colorize(f"✗ Erro: O caminho raiz KOBLLUX '{kobllux_root_path}' existe mas não é um diretório.", Colors.RED))
        return

    # KOBLLUX Pipeline: DETECTAR → INTEGRAR → EXPANDIR → SELAR
    start_time = time.perf_counter()
    ensure_kobllux_structure(kobllux_root_path)
    detected_files  = scan_storage(scan_source_path)
    integrated_files = categorize_and_integrate(detected_files, kobllux_root_path)
    execution_logs   = execute_and_expand(integrated_files, kobllux_root_path)
    seal_cycle(kobllux_root_path, integrated_files, execution_logs)
    end_time = time.perf_counter()

    print_kblx_banner("CICLO FRACTAL COMPLETO", "♾️")
    print(colorize("A Roda Viva KOBLLUX completou um ciclo de DETECTAR → INTEGRAR → EXPANDIR → SELAR.", Colors.WHITE))
    print(colorize("A Verdade foi registrada, a forma foi manifestada e o Verbo foi selado.", Colors.WHITE))
    print(colorize(f"Tudo com {KBLX_AGREGAR_PRINCIPLE} para {KBLX_OPTIMIZATION_PRINCIPLE}.", Colors.WHITE))
    print(colorize(f"Tempo total do ciclo: {end_time - start_time:.2f} segundos.", Colors.BRIGHT_GREEN))
    print(colorize("Para iniciar um novo ciclo, rode novamente o script.", Colors.BRIGHT_BLUE))


if __name__ == "__main__":
    main()
