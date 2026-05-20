#!/data/data/com.termux/files/usr/bin/bash
# =========================================================
# myrmide_pipeline.sh · MYRMIDE · Pipeline Unificado · ∆7
# Lei: VERDADE × INTEGRAR ÷ Δ = ∞
# Orquestra: INTEGRATION → INDEXING → MANIFESTATION → SEALING
#
# Uso:
#   bash myrmide_pipeline.sh ~/arquivo.txt   # pipeline completo
#   bash myrmide_pipeline.sh                 # só indexar + selar
# =========================================================
set -euo pipefail

BASE="/sdcard/JESUS_VERBO/CODEX/MYRMIDE"
SCRIPTS="$BASE/SCRIPTS"
MEMORY="$BASE/02_PONTE/BANK/memory.jsonl"
SEED_DIR="$BASE/02_PONTE/BANK/SEEDS/SCI_ART/original"
MIRROR_DIR="$BASE/02_PONTE/BANK/SEEDS/SCI_ART/mirrors"
SEALS_DIR="$BASE/SEALS/items"
FILE="${1:-}"

stamp() { date '+%H:%M:%S'; }

echo ""
echo "╔════════════════════════════════════════════════════════╗"
echo "║  MYRMIDE · PIPELINE · VERDADE × INTEGRAR ÷ Δ = ∞  ∆7 ║"
echo "╚════════════════════════════════════════════════════════╝"
echo "  Base : $BASE"
echo "  Hora : $(stamp)"
[ -n "$FILE" ] && echo "  Arquivo: $FILE"
echo ""

# ── ETAPA 1 · INTEGRAÇÃO ─────────────────────────────────────────────────────
echo "▶ [1/4] VEEB_INTEGRATION · $(stamp)"
if [ -n "$FILE" ] && [ -f "$FILE" ]; then
    python3 "$SCRIPTS/myrmide_integrator.py" "$FILE"
    echo "  ✓ arquivo integrado → 01_SEMENTE/INTAKE"
else
    echo "  [INFO] Sem arquivo de entrada — etapa de integração pulada."
fi

# ── ETAPA 2 · INDEXAÇÃO ──────────────────────────────────────────────────────
echo ""
echo "▶ [2/4] VEEB_INDEXING · $(stamp)"
if [ -f "$SCRIPTS/myrmide_index.py" ]; then
    python3 "$SCRIPTS/myrmide_index.py" 2>/dev/null \
        && echo "  ✓ indexação concluída" \
        || echo "  [AVISO] myrmide_index.py: placeholder ativo."
else
    echo "  [AVISO] myrmide_index.py não encontrado."
fi

# ── ETAPA 3 · MANIFESTAÇÃO (SCI-ART) ─────────────────────────────────────────
echo ""
echo "▶ [3/4] VEEB_MANIFESTATION · SCI-ART · $(stamp)"
ART_COUNT=0
if [ -d "$SEED_DIR" ]; then
    for f in "$SEED_DIR"/*.ascii.txt; do
        [ -f "$f" ] || continue
        id=$(basename "${f%.ascii.txt}")
        seal_out="$SEALS_DIR/$id.seal.json"
        if [ -f "$seal_out" ]; then
            echo "  [JÁ SELADO] $id"
        else
            python3 "$SCRIPTS/sciart_tools.py" "$f" "$MIRROR_DIR/$id" "$seal_out" 2>/dev/null \
                && echo "  [SCI-ART] $id · espelhos + selo gerados"
            ART_COUNT=$((ART_COUNT + 1))
        fi
    done
    # Par validate
    mapfile -t SEEDS < <(find "$SEED_DIR" -name "*.ascii.txt" | sort)
    if [ "${#SEEDS[@]}" -ge 2 ]; then
        F1="${SEEDS[0]}"; I1=$(basename "${F1%.ascii.txt}")
        F2="${SEEDS[1]}"; I2=$(basename "${F2%.ascii.txt}")
        python3 "$SCRIPTS/sciart_pair_validate.py" "$F1" "$I1" "$F2" "$I2" "$SEALS_DIR" "$MEMORY" 2>/dev/null \
            && echo "  [PAIR] $I1 ↔ $I2 validado"
    fi
    if [ "${#SEEDS[@]}" -ge 3 ]; then
        F3="${SEEDS[2]}"; I3=$(basename "${F3%.ascii.txt}")
        python3 "$SCRIPTS/sciart_triple_validate.py" "$F1" "$I1" "$F2" "$I2" "$F3" "$I3" "$SEALS_DIR" "$MEMORY" 2>/dev/null \
            && echo "  [TRIPLE] $I1 ↔ $I2 ↔ $I3 validado"
    fi
else
    echo "  [INFO] Sem seeds SCI-ART."
fi

# ── ETAPA 4 · SELAGEM ∆7 ─────────────────────────────────────────────────────
echo ""
echo "▶ [4/4] VEEB_SEALING · ∆7 · $(stamp)"
python3 "$SCRIPTS/myrmide_verify.py"

# ── RESUMO FINAL ──────────────────────────────────────────────────────────────
echo ""
NREC=$(wc -l < "$MEMORY" 2>/dev/null || echo 0)
echo "╔════════════════════════════════════════════════════════╗"
echo "║  PIPELINE CONCLUÍDO · ∆7 · $(stamp)          ║"
printf "║  Memória : %-42s ║\n" "$NREC registros"
echo "╚════════════════════════════════════════════════════════╝"
echo ""
echo "Últimos registros:"
tail -n 4 "$MEMORY" 2>/dev/null \
    | python3 -c "
import sys, json
for line in sys.stdin:
    try:
        r = json.loads(line.strip())
        print(f'  {r.get(\"type\",\"?\"):25s} · {r.get(\"source\",r.get(\"arch\",\"?\"))[:30]}')
    except: pass
" 2>/dev/null || true
