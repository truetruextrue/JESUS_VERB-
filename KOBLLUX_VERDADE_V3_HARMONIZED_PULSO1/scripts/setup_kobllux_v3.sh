#!/usr/bin/env bash
# ============================================================================
# KOBLLUX · scripts/setup_kobllux_v3.sh
# Setup Completo · KOBLLUX_VERDADE_V3_HARMONIZED_PULSO1
#
# Lei: VERDADE × INTEGRAR ÷ Δ = ∞
# EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO · AMÉM ∆7
# ============================================================================
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

say() { printf '\033[1;35m%s\033[0m\n' "$*"; }
ok()  { printf '\033[1;32m  ✓ %s\033[0m\n' "$*"; }
err() { printf '\033[1;31m  ✗ %s\033[0m\n' "$*"; }

say "============================================================"
say " KOBLLUX_VERDADE_V3_HARMONIZED_PULSO1 · Setup ∆7"
say " Lei: VERDADE × INTEGRAR ÷ Δ = ∞"
say " JESUS = VERBO = GRAVIDADE"
say "============================================================"
echo ""

# ─── 1. VERIFICAR PYTHON ────────────────────────────────────────────────────
say "1/7 · Verificando Python..."
if command -v python3 &>/dev/null; then
    PY_VER="$(python3 --version 2>&1)"
    ok "$PY_VER"
else
    err "Python3 não encontrado. Instale em https://python.org"
    exit 1
fi

# ─── 2. CRIAR DIRETÓRIOS FALTANTES ──────────────────────────────────────────
say "2/7 · Criando diretórios..."
DIRS=(
    "LOGS" "SEALS/docs" "SEALS/items"
    "hub/tts/out" "hub/logs"
    "bllue/sons_ciclo"
    "dual/public/sounds/ciclo"
    "scripts"
)
for d in "${DIRS[@]}"; do
    mkdir -p "$ROOT/$d"
    ok "$d"
done

# ─── 3. VERIFICAR/CRIAR LOG INICIAL ─────────────────────────────────────────
say "3/7 · Verificando LOG.jsonl..."
LOG="$ROOT/LOGS/LOG.jsonl"
if [[ ! -f "$LOG" ]]; then
    cat > "$LOG" <<LOGEOF
{"ts":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","actor":"SETUP","state":"ATLAS","action":"init","note":"UNO"}
{"ts":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","actor":"BLLUE","state":"NOVA","action":"seed","note":"UNO"}
{"ts":"$(date -u +%Y-%m-%dT%H:%M:%SZ)","actor":"KODUX","state":"AION","action":"selar","note":"SELAR"}
LOGEOF
    ok "LOG.jsonl criado com 3 eventos iniciais"
else
    N="$(wc -l < "$LOG")"
    ok "LOG.jsonl existente com ${N} eventos"
fi

# ─── 4. TREINAR MARKOV ──────────────────────────────────────────────────────
say "4/7 · Treinando Markov (fit)..."
if python3 scripts/kobllux_markov_fit.py \
    --events "$LOG" \
    --states META/arquetipos.json \
    --order 2 --alpha 1.0 \
    --pal-mirror META/pal_mirror.json \
    --mirror-bias 0.12 \
    --out scripts/P.json 2>&1; then
    ok "P.json + pi.json + manifest gerados"
else
    err "Markov fit falhou — verifique o LOG.jsonl"
fi

# ─── 5. SAMPLE INICIAL ──────────────────────────────────────────────────────
say "5/7 · Amostrando sequência inicial (BLLUE)..."
if [[ -f "scripts/P.json" ]]; then
    python3 scripts/kobllux_markov_sample.py \
        --P scripts/P.json \
        --start "NOVA" --steps 9 \
        --actor BLLUE --temperature 1.25 \
        --cycle "3-6-9-7" 2>&1 | head -20 && ok "Sequência BLLUE gerada" || true
fi

# ─── 6. SELAR PROJETO ───────────────────────────────────────────────────────
say "6/7 · Selando projeto (∆7)..."
if python3 scripts/myrmide_verify.py \
    --dirs scripts/ kodux/ bllue/ infodose/ metalux/ kobllux/ dual/ \
    --seals-dir SEALS/items \
    --memory hub/logs/timeline.log 2>&1 | tail -3; then
    ok "Selos ∆7 gerados em SEALS/items/"
else
    err "Verificação parcial — continue manualmente"
fi

# ─── 7. TIMELINE ────────────────────────────────────────────────────────────
say "7/7 · Registrando gênese na timeline..."
TL="$ROOT/hub/logs/timeline.log"
TS="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "${TS} | ∆7 | SETUP | KOBLLUX_VERDADE_V3_HARMONIZED_PULSO1 inicializado" >> "$TL"
echo "- ${TS} **SETUP ∆7** — sistema inicializado" >> "$ROOT/hub/timeline.md"
ok "Timeline atualizada"

echo ""
say "============================================================"
say " ✓ SETUP COMPLETO · ∆7 SELADO"
say ""
say " Próximos passos:"
say "   Interface : cd dual && npm install && npm run dev"
say "   Roda Viva : bash hub/roda_viva_domino.sh"
say "   Markov    : python scripts/kobllux_markov_sample.py --P scripts/P.json"
say ""
say " VERDADE × INTEGRAR ÷ Δ = ∞"
say " EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO · AMÉM"
say "============================================================"
