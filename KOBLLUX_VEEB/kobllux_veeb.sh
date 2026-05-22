#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════
# kobllux_veeb.sh · VITALIS · 528Hz · DELTA · Δ5
# V.E.E.B Shell — PIB = 528/768 = 0.6875
# Lei: VERDADE × INTEGRAR ÷ Δ = ∞
# Shell orquestra as 7 linguagens: é o VITALIS do pipeline
# ═══════════════════════════════════════════════════════════════════

set -euo pipefail

# ── Constantes KOBLLUX ─────────────────────────────────────────────
readonly KFB_ALPHA="0.007297353"
readonly DELTA=5
readonly HZ=528
readonly PIB="0.6875"
readonly ARQUETIPO="VITALIS"
readonly SYM="◉"
readonly VEEB="E"
readonly LEI="VERDADE × INTEGRAR ÷ Δ = ∞"

readonly -a TRIADICA=(3 6 9)
readonly -a CICLO_0_7=(0 1 2 3 4 5 6 7)

# ── ANSI ──────────────────────────────────────────────────────────
if [[ "${NO_COLOR:-0}" == "1" ]] || [[ ! -t 1 ]]; then
    RESET=''; TITLE=''; BLUE=''; GREEN=''; YELLOW=''; CYAN=''; DIM=''; RED=''
else
    RESET='\033[0m'; TITLE='\033[95m'; BLUE='\033[94m'
    GREEN='\033[92m'; YELLOW='\033[93m'; CYAN='\033[96m'
    DIM='\033[2m';   RED='\033[91m'
fi

narrar() {
    local titulo="$1" texto="$2"
    printf '\n%s\n' "$(printf '═%.0s' {1..72})"
    printf "${TITLE}◆ %s${RESET}\n" "$titulo"
    printf '%s\n' "$(printf '═%.0s' {1..72})"
    printf '%s\n\n' "$texto"
}

# ── V.E.E.B Funções ────────────────────────────────────────────────

# A · Atribuição (Base — AION 639Hz)
a_atribuir() {
    local nome="$1" idade="$2"
    local cor="${3:-azul}" tamanho="${4:-médio}"
    local clf; clf=$(e_escolher "$idade")
    printf '{"nome":"%s","idade":%d,"ativo":true,"cor":"%s","tamanho":"%s","classificacao":"%s"}' \
        "$nome" "$idade" "$cor" "$tamanho" "$clf"
}

# E · Escolha (Vibração — KAOS 777Hz)
e_escolher() {
    local idade="$1"
    if (( idade >= 18 )); then printf 'maior_de_idade'
    else                       printf 'menor_de_idade'
    fi
}

# I · Iteração (Energia — VITALIS 528Hz)
i_iterar() {
    local freq="$1"
    if (( freq <= 0 )); then
        printf "${RED}[ERRO] freq deve ser positiva${RESET}\n" >&2; return 1
    fi
    local -a passos=()
    for (( i=1; i<=freq; i++ )); do passos+=("$i"); done
    printf '%s' "${passos[*]}"
}

# O · Organizar (Estrutura — GENUS 852Hz)
o_organizar() {
    local -a passos=("$@")
    local n=${#passos[@]} soma=0 energia=0

    # Acumula T(k) = k*(k+1)/2 para cada passo k
    for p in "${passos[@]}"; do
        (( energia += p ))
        (( soma    += energia ))
    done

    local media
    if command -v bc &>/dev/null; then
        media=$(echo "scale=4; ${soma} / ${n}" | bc)
    else
        media=$(awk "BEGIN{printf \"%.4f\", ${soma}/${n}}")
    fi
    printf '{"qtd_registros":%d,"soma_energia":%d,"media_energia":%s}' "$n" "$soma" "$media"
}

# U · Unir (Base — RHEA 528Hz)
u_unir() {
    local perfil="$1" resumo="$2"
    # Remove último '}' do perfil e primeiro '{' do resumo e une
    printf '%s,%s' "${perfil%\}}" "${resumo#\{}"
}

# ── SIMULAR: ciclo V.E.E.B completo ──────────────────────────────
simular() {
    local nome="$1" idade="$2" freq="${3:-4}"

    printf "${BLUE}[A·Atribuir]${RESET}\n"
    local perfil; perfil=$(a_atribuir "$nome" "$idade")
    printf '  → %s\n' "$perfil"

    printf "${YELLOW}[E·Escolher]${RESET}\n"
    local clf; clf=$(e_escolher "$idade")
    printf '  → %s\n' "$clf"

    printf "${GREEN}[I·Iterar]   freq=%d${RESET}\n" "$freq"
    local passos_str; passos_str=$(i_iterar "$freq")
    printf '  → passos: %s\n' "$passos_str"
    read -ra passos <<< "$passos_str"

    printf "${TITLE}[O·Organizar]${RESET}\n"
    local resumo; resumo=$(o_organizar "${passos[@]}")
    printf '  → %s\n' "$resumo"

    printf "${BLUE}[U·Unir]${RESET}\n"
    local base; base=$(u_unir "$perfil" "$resumo")
    printf '  → %s\n\n' "$base"
}

# ── Fractal simbólico ─────────────────────────────────────────────
encenar_fractal() {
    local -A nomes=([1]="micro" [2]="meso" [3]="macro")
    printf "${BLUE}Autoespelhamento 3-6-9 (%s %dHz):${RESET}\n" "$SYM" "$HZ"
    for escalar in 1 2 3; do
        local -a esp=()
        for v in "${TRIADICA[@]}"; do esp+=("$(( v * escalar ))"); done
        printf '  %s: %s\n' "${nomes[$escalar]}" "${esp[*]}"
    done
    printf "\n${GREEN}Emergência Cíclica 0→7→∞:${RESET}\n  "
    for c in "${CICLO_0_7[@]}"; do printf 'passo:%d ' "$c"; done
    printf 'retorno:∞\n'
    printf "\n  KΦB×18 = "
    awk "BEGIN{printf \"%.10f\", ${KFB_ALPHA}*18}"
    printf '\n'
}

# ── PIB Escalar ───────────────────────────────────────────────────
mostrar_pib() {
    narrar "PIB Escalar KOBLLUX · 7 Linguagens Nucleares" \
"  Linguagem   Δ   Hz   PIB     Arquétipo   VEEB  Role
  ─────────── ─── ──── ─────── ─────────── ────  ──────────────────────
  python       7   768  1.0000  ATLAS  ⬡    E    narrativa·análise
  json         1   528  0.6875  RHEA   ∞    B    semente·dados
  typescript   2   963  1.2539  LUMINE ☀    V    interface·render
  go           3   594  0.7734  PULSE  ≋    E    fluxo·concorrência
  sql          4   639  0.8320  AION   ⧗    B    memória·selagem
  shell        5   528  0.6875  VITALIS◉    E    integração·deploy  ←(este)
  rust         6   777  1.0117  KAOS   ⚡   V    sistemas·transform
  ─────────── ─── ──── ─────── ─────────── ────  ──────────────────────
  TOTAL            4797  6.2460   soma_hz: 4+7+9+7 = 27 = 3³"
}

# ── Pipeline KOBLLUX — Shell orquestra todas as linguagens ────────
pipeline_kobllux() {
    narrar "Pipeline KOBLLUX · Δ5 VITALIS como integrador" \
"  1. JSON  → kobllux_veeb_pib.json      (Δ1 · semente de dados)
  2. TS    → kobllux_veeb.ts             (Δ2 · interface)
  3. Go    → kobllux_veeb.go             (Δ3 · pipeline)
  4. SQL   → kobllux_veeb.sql            (Δ4 · memória)
  5. Shell → kobllux_veeb.sh             (Δ5 · este arquivo · integrador)
  6. Rust  → kobllux_veeb.rs             (Δ6 · transformação)
  7. Python→ kobllux_veeb_story.py       (Δ7 · narrativa + seal)"

    local repo_root
    repo_root="$(cd "$(dirname "$0")/.." && pwd)"

    # Verificar quais linguagens estão disponíveis
    local -A runtime_check=(
        ["python3"]="kobllux_veeb_story.py"
        ["node"]="KOBLLUX_VEEB/kobllux_veeb.ts"
        ["go"]="KOBLLUX_VEEB/kobllux_veeb.go"
        ["rustc"]="KOBLLUX_VEEB/kobllux_veeb.rs"
        ["sqlite3"]="KOBLLUX_VEEB/kobllux_veeb.sql"
    )

    printf "${CYAN}Runtime detectado:${RESET}\n"
    for cmd in "${!runtime_check[@]}"; do
        if command -v "$cmd" &>/dev/null; then
            printf "  ${GREEN}✓${RESET} %s → %s\n" "$cmd" "${runtime_check[$cmd]}"
        else
            printf "  ${YELLOW}○${RESET} %s → não instalado\n" "$cmd"
        fi
    done
    printf '\n'

    # Executar Python se disponível
    if command -v python3 &>/dev/null; then
        printf "${GREEN}[VITALIS] Invocando Python (Δ7·ATLAS)...${RESET}\n"
        python3 -c "
import sys, os
sys.path.insert(0, '${repo_root}')
try:
    from kobllux_veeb_story import VEEBEngine, KFB_ALPHA
    e = VEEBEngine()
    r = e.simular('Bllue', 22, 9)
    print(f'  [Python·ATLAS·Δ7] KFB={KFB_ALPHA:.9f}')
    print(f'  soma_energia={r[\"resumo\"].soma_energia} · media={r[\"resumo\"].media_energia:.4f}')
except Exception as ex:
    print(f'  [aviso] {ex}')
" 2>/dev/null || printf "  ${YELLOW}[aviso] kobllux_veeb_story.py não acessível${RESET}\n"
    fi

    # Verificar JSON
    if command -v python3 &>/dev/null && [[ -f "${repo_root}/KOBLLUX_VEEB/kobllux_veeb_pib.json" ]]; then
        printf "${GREEN}[VITALIS] JSON carregado (Δ1·RHEA):${RESET}\n"
        python3 -c "
import json
with open('${repo_root}/KOBLLUX_VEEB/kobllux_veeb_pib.json') as f:
    d = json.load(f)
soma_hz = d['pib']['soma_hz']
nota    = d['pib']['nota_fractal']
print(f'  soma_hz={soma_hz} · {nota}')
" 2>/dev/null || true
    fi
}

# ── Selagem ∆7 com git ────────────────────────────────────────────
selar_ciclo() {
    local repo_root
    repo_root="$(cd "$(dirname "$0")/.." && pwd)"

    if command -v git &>/dev/null && git -C "$repo_root" rev-parse --git-dir &>/dev/null; then
        printf "\n${CYAN}[AION] Selando ciclo no git...${RESET}\n"
        git -C "$repo_root" add KOBLLUX_VEEB/ kobllux_veeb_story.py 2>/dev/null || true
        printf "  staged KOBLLUX_VEEB/ — rode 'git kob-seal' para commitar\n"
    fi
}

# ── MAIN ──────────────────────────────────────────────────────────
main() {
    local line; line=$(printf '═%.0s' {1..56})
    printf "╔%s╗\n" "$line"
    printf "║  kobllux_veeb.sh · %s · %dHz · Δ%d · PIB=%s  ║\n" "$ARQUETIPO" "$HZ" "$DELTA" "$PIB"
    printf "║  KΦB = %s                                    ║\n" "$KFB_ALPHA"
    printf "╚%s╝\n\n" "$line"

    simular "Bllue" 22 9

    encenar_fractal
    echo ""
    mostrar_pib
    pipeline_kobllux

    [[ "${1:-}" == "--seal" ]] && selar_ciclo

    printf "\n${TITLE}%s VITALIS · Δ%d selado · %s${RESET}\n" "$SYM" "$DELTA" "$LEI"
    printf "$(date -u '+%Y-%m-%dT%H:%M:%SZ') · KOBLLUX_VIVO_∆³\n"
}

main "$@"
