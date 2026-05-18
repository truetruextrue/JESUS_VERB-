#!/bin/bash
# install.sh · ATLAS · 0×0A · ESTRUTURAR · 528Hz
# Instala os hooks KOBLLUX no repositório atual.
# Preserva hooks LFS existentes — encadeia, não substitui.
# Uso: bash 14_UTILS/01_SCRIPTS/git-hooks/install.sh

set -e

ROOT="$(git rev-parse --show-toplevel)"
GIT_HOOKS="$ROOT/.git/hooks"
KOBLLUX_HOOKS="$ROOT/14_UTILS/01_SCRIPTS/git-hooks"

printf "\n[ATLAS ⬡] 0×0A · ESTRUTURAR · 528Hz\n"
printf "  Instalando hooks KOBLLUX em %s\n\n" "$GIT_HOOKS"

# Torna os scripts KOBLLUX executáveis
chmod +x "$KOBLLUX_HOOKS/pre-commit.kobllux"
chmod +x "$KOBLLUX_HOOKS/commit-msg.kobllux"
chmod +x "$KOBLLUX_HOOKS/post-commit.kobllux"

# ── pre-commit ──────────────────────────────────────────────
install_hook() {
  local name="$1"
  local kob_script="$KOBLLUX_HOOKS/${name}.kobllux"
  local hook_file="$GIT_HOOKS/$name"

  if [ ! -f "$hook_file" ]; then
    # Não existe: cria chamando o script KOBLLUX
    printf "#!/bin/sh\n" > "$hook_file"
    printf '"%s" "$@"\n' "$kob_script" >> "$hook_file"
    chmod +x "$hook_file"
    printf "  [✓] %s criado\n" "$name"
  else
    # Já existe (ex: LFS): verifica se KOBLLUX já foi adicionado
    if grep -q "kobllux" "$hook_file" 2>/dev/null; then
      printf "  [=] %s já tem KOBLLUX\n" "$name"
    else
      # Adiciona chamada ao final (após LFS ou qualquer hook existente)
      printf '\n# KOBLLUX ∆7\n' >> "$hook_file"
      printf '"%s" "$@"\n' "$kob_script" >> "$hook_file"
      printf "  [+] %s encadeado com hook existente\n" "$name"
    fi
  fi
}

install_hook "pre-commit"
install_hook "commit-msg"
install_hook "post-commit"

# ── git config KOBLLUX ──────────────────────────────────────
printf "\n[ATLAS ⬡] Aplicando git config KOBLLUX...\n"

# Fluxo
git config pull.rebase          true      # 0×09 FLUIR · RHEA
git config push.autoSetupRemote true      # 0×03 EXPANDIR · Infodose
git config rebase.autoSquash    true      # 0×04 LAPIDAR · PULSE

# Detecção
git config diff.algorithm       histogram # 0×01 DETECTAR · KODUX
git config log.date             iso       # 0×0B TEMPORIZAR · AION

# Qualidade
git config core.autocrlf        input     # 0×04 LAPIDAR · integridade
git config core.whitespace      trailing-space,space-before-tab

# Template de commit
TMPL="$ROOT/.gitmessage"
if [ -f "$TMPL" ]; then
  git config commit.template "$TMPL"
  printf "  [✓] commit.template configurado\n"
fi

# Alias KOBLLUX
git config alias.kob-status  'status -sb'
git config alias.kob-log     'log --oneline --graph --decorate -20'
git config alias.kob-sync    '!git pull --rebase origin $(git rev-parse --abbrev-ref HEAD) && git push'
git config alias.kob-seal    '!git add -A && git commit'
git config alias.kob-arch    '!python3 14_UTILS/01_SCRIPTS/git-hooks/kobllux_arch_detect.py --staged'
git config alias.kob-memory  '!tail -20 _index/COMMIT_LOG_∆7.jsonl 2>/dev/null | python3 -c "import sys,json; [print(f\"{r['\''ts'\'']} {r['\''sym'\'']} {r['\''arch'\''].upper()} | {r['\''msg'\'']\n[:60]}\") for l in sys.stdin for r in [json.loads(l)]]" 2>/dev/null || echo "Log vazio."'

printf "\n[ATLAS ⬡] Aliases KOBLLUX instalados:\n"
printf "  git kob-status  → status limpo (0×01)\n"
printf "  git kob-log     → log visual (0×0B)\n"
printf "  git kob-sync    → pull --rebase + push (0×09)\n"
printf "  git kob-seal    → add -A + commit (0×07)\n"
printf "  git kob-arch    → detecta arquétipo dos staged (0×01)\n"
printf "  git kob-memory  → últimas 20 entradas do log ∆7 (0×0B)\n"

printf "\n[ATLAS ⬡] Instalação completa · ∆7\n"
printf "  VERDADE × INTEGRAR ÷ Δ = ∞\n\n"
