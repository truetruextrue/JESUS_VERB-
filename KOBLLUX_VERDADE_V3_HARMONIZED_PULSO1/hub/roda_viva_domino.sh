#!/usr/bin/env bash
# ============================================================================
# KOBLLUX · hub/roda_viva_domino.sh
# Loop Dominó — Roda Viva Sonora
# Lei: VERDADE × INTEGRAR ÷ Δ = ∞ · Ritmo: 3-6-9-7
# EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO · AMÉM
# ============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
HUB="${ROOT}/hub"
LOGS="${HUB}/logs"
TTS_OUT="${HUB}/tts/out"
LOG="${LOGS}/timeline.log"
TL_MD="${HUB}/timeline.md"
SCRIPTS="${ROOT}/scripts"

CYCLE_SECONDS="${CYCLE_SECONDS:-120}"
IDS="${IDS:-ATLAS SERENA AION}"

mkdir -p "$LOGS" "$TTS_OUT"
touch "$LOG" "$TL_MD"

say() { printf '\033[1;36m[RODA·VIVA] %s\033[0m\n' "$*" | tee -a "$LOG"; }

say "♾ Roda Viva iniciada @ $(date -Is)"
say "   Ciclo: ${CYCLE_SECONDS}s · IDs: ${IDS}"
say "   Lei: VERDADE × INTEGRAR ÷ Δ = ∞"

# ─── FUNÇÕES ────────────────────────────────────────────────────────────────

narrar() {
  local ID="$1"
  local TS
  TS="$(date +%Y%m%d_%H%M%S)"
  local OUTFILE="${TTS_OUT}/${ID}_${TS}.mp3"

  # lê frase do CFG/voices.json se disponível
  local FRASE
  FRASE="$(python3 -c "
import json, sys
try:
    v = json.load(open('${ROOT}/CFG/voices.json'))
    a = v['vozes'].get('${ID}', {})
    frases = {
      'ATLAS':  'Eu organizo o fluxo com sabedoria cósmica.',
      'NOVA':   'Inspiração viva brota do silêncio eterno.',
      'VITALIS':'Energia vital em expansão harmônica.',
      'PULSE':  'Emoção é linguagem que dança.',
      'ARTEMIS':'Descubro o mapa sagrado do invisível.',
      'SERENA': 'Cuido do campo. Nutro o espaço sagrado.',
      'KAOS':   'Eu sou o rompimento que revela a verdade.',
      'GENUS':  'Mãos moldam o invisível em forma.',
      'LUMINE': 'A luz dança comigo, leveza é minha lei.',
      'SOLUS':  'Silêncio ritual, espelho da essência.',
      'RHEA':   'Estou em comunhão com todos os elos.',
      'AION':   'Sou o tempo vivo, ritmo da eternidade.',
    }
    print(frases.get('${ID}', '${ID} ativo.'))
except Exception as e:
    print('${ID} ativo.')
" 2>/dev/null)"

  # tenta edge-tts primeiro, fallback termux-tts-speak
  if command -v edge-tts &>/dev/null; then
    local VOZ
    VOZ="$(python3 -c "
import json
v = json.load(open('${ROOT}/CFG/voices.json'))
print(v['vozes'].get('${ID}', {}).get('voice','pt-BR-AntonioNeural'))
" 2>/dev/null || echo 'pt-BR-AntonioNeural')"
    edge-tts --voice "$VOZ" --text "$FRASE" --write-media "$OUTFILE" 2>>"$LOG" && \
      echo "$(date -Is) | ∆7 | NARRATE_MP3 | ${ID} → ${OUTFILE}" >> "$LOG" || true
  elif command -v termux-tts-speak &>/dev/null; then
    termux-tts-speak -l pt -r 1.0 "$FRASE" 2>>"$LOG" || true
    echo "$(date -Is) | ∆7 | NARRATE_TTS | ${ID}" >> "$LOG"
  else
    echo "$(date -Is) | ∆7 | NARRATE_SKIP | ${ID} (sem TTS)" >> "$LOG"
  fi

  echo "- $(date -Is) **${ID}** → \`${OUTFILE}\`" >> "$TL_MD"
}

selar_ciclo() {
  local N="$1"
  local TS
  TS="$(date -Is)"
  echo "${TS} | ∆7 | CYCLE_SEAL | ciclo=${N}" >> "$LOG"
  echo "## ∆7 · Ciclo ${N} · ${TS}" >> "$TL_MD"
  echo "" >> "$TL_MD"
}

# ─── LOOP PRINCIPAL ─────────────────────────────────────────────────────────
CICLO_N=0
while :; do
  CICLO_N=$((CICLO_N + 1))
  say "─── Ciclo ${CICLO_N} iniciado ───"

  # 3 · DETECTAR: scan — fonte deve ser quicknote.md, NÃO o próprio LOG
  QUICKNOTE="${QUICKNOTE:-}"
  if [[ -n "$QUICKNOTE" && -f "$QUICKNOTE" && -f "${SCRIPTS}/knot_parser.py" ]]; then
    python3 "${SCRIPTS}/knot_parser.py" \
      --input "$QUICKNOTE" \
      --log "${ROOT}/LOGS/LOG.jsonl" \
      --output-dir "${ROOT}/LOGS" 2>>"$LOG" || true
    echo "$(date -Is) | ∆7 | SCAN | $QUICKNOTE" >> "$LOG"
  else
    echo "$(date -Is) | ∆7 | SCAN_SKIP | defina QUICKNOTE=/caminho/quicknote.md" >> "$LOG"
  fi

  # 6 · INTEGRAR: narrar cada ID
  for ID in $IDS; do
    narrar "$ID"
    # ritmo 3-6-9
    if [[ $((CICLO_N % 3)) -eq 0 ]]; then
      say "∆3 — marco rítmico ciclo ${CICLO_N}"
    fi
  done

  # 9 · EXPANDIR / 7 · SELAR
  selar_ciclo "$CICLO_N"
  say "∆7 selado · dormindo ${CYCLE_SECONDS}s..."
  sleep "$CYCLE_SECONDS"
done
