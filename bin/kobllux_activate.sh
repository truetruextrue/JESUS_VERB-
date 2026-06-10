#!/usr/bin/env bash
# KOBLLUX • ESPELHO•MOTORES — ativação M1→M2→M3→M4
# Uso: KOBLLUX_ROOT=/path/to/CODEX bash kobllux_activate.sh
set -euo pipefail

ROOT="${KOBLLUX_ROOT:-/sdcard/JESUS_VERBO/CODEX}"
BIN="$ROOT/bin"
STATE="$ROOT/state"
CARDS="$ROOT/cards"
LOG="$ROOT/logs/kobllux_activation.log"
mkdir -p "$STATE" "$CARDS" "$(dirname "$LOG")"

now(){ date +"%Y-%m-%dT%H:%M:%S%z"; }

# Normaliza CRLF (seguro se sed -i indisponível)
norm(){ sed -i 's/\r$//' "$1" 2>/dev/null || true; }

echo "[$(now)] ESPELHO•MOTORES • start M1→M2→M3→M4" | tee -a "$LOG"

# Input: state/espelho_input.txt ou .md
IN="$STATE/espelho_input.txt"
[ -f "$IN" ] || IN="$STATE/espelho_input.md"

# Gera versão-espelho (reverso por linha) para os motores
MIR="$STATE/espelho_input.mirror.txt"
python3 - "$IN" "$MIR" <<'PY'
import sys
src = open(sys.argv[1], 'r', encoding='utf-8', errors='ignore').read() if len(sys.argv) > 1 else ""
rev = "\n".join(line[::-1] for line in src.splitlines())
open(sys.argv[2], 'w', encoding='utf-8').write(rev)
print("[KOBLLUX] mirror ok ->", sys.argv[2])
PY

# M1 — caracteres/mesa/média
norm "$BIN/m1_detect.py"
python3 "$BIN/m1_detect.py" --root "$ROOT" --direct "$IN" --mirror "$MIR"

# M2 — linguagem (usa saída do M1)
norm "$BIN/m2_integrar.py"
python3 "$BIN/m2_integrar.py" --root "$ROOT" --direct "$IN" --mirror "$MIR" \
  --m1 "$STATE/m1_chars_report.json"

# M3 — símbolo (usa M1 e M2)
norm "$BIN/m3_espelho.py"
python3 "$BIN/m3_espelho.py" --root "$ROOT" --direct "$IN" --mirror "$MIR" \
  --m1 "$STATE/m1_chars_report.json" --m2 "$STATE/m2_lang_report.json"

# M4 — fractal + arte SCI (usa M1/M2/M3)
norm "$BIN/m4_expandir.py"
python3 "$BIN/m4_expandir.py" --root "$ROOT" \
  --direct "$IN" --mirror "$MIR" \
  --m3 "$STATE/m3_symbol_report.json" \
  --size 33 --base 3

# M5 — espelho pool (agregador final)
norm "$BIN/espelho_pool.py"
python3 "$BIN/espelho_pool.py" --root "$ROOT" --infile "$IN"

echo "[$(now)] ESPELHO•MOTORES • SEALED (∆7) • reports em $STATE" | tee -a "$LOG"
echo "[KOBLLUX] OK → M1/M2/M3/M4/M5 selados"
