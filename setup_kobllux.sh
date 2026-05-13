#!/usr/bin/env bash
set -euo pipefail

# =========================
# CONFIGURAÇÕES (já adaptadas)
# =========================
REPO_OWNER="truetruextrue"
REPO_NAME="KOBLLUX"  # Mantendo o nome original
REPO_DIR="/storage/emulated/0/0/0/KOBLLUX"  # SEU DIRETÓRIO EXATO

# FONTE: seu diretório já é a fonte! (não precisa copiar de outro lugar)
ANDROID_SRC=""  # Deixar vazio, pois você já está no local certo

# Escolha do método de push (use PAT)
GITHUB_PAT="${GITHUB_PAT:-}"

# =========================
log(){ printf "\n\033[1;36m[LOG]\033[0m %s\n" "$*"; }
die(){ printf "\n\033[1;31m[ERRO]\033[0m %s\n" "$*" ; exit 1; }

# 0) Verificar se já estamos no diretório correto
if [ "$PWD" != "$REPO_DIR" ]; then
    log "Entrando no diretório: $REPO_DIR"
    cd "$REPO_DIR" || die "Diretório não encontrado!"
else
    log "Já estamos no diretório correto"
fi

# 1) Garantir que é um repositório git
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    log "Inicializando repositório git..."
    git init
    git branch -M main
else
    log "Repositório git já existe"
fi

# 2) Configurar remote (se não existir)
if ! git remote get-url origin >/dev/null 2>&1; then
    log "Configurando remote origin..."
    git remote add origin "https://github.com/${REPO_OWNER}/${REPO_NAME}.git"
else
    log "Remote origin já configurado: $(git remote get-url origin)"
fi

# 3) Verificar arquivos (listar para conferência)
log "Arquivos no diretório:"
ls -la

# 4) Garantir .gitignore adequado
log "Verificando .gitignore..."
if [ ! -f ".gitignore" ]; then
    cat > .gitignore <<'EOF'
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/
.venv/
.env
.vscode/
.idea/
.DS_Store
*.pub
id_ed25519*
*key*
arquetipos.json
SISTEMA_INFO.json
EOF
    log ".gitignore criado"
else
    log ".gitignore já existe"
fi

# 5) Adicionar arquivos e commitar
log "Adicionando arquivos ao git..."
git add -A

log "Verificando status..."
git status

log "Criando commit (se houver mudanças)..."
if git diff --cached --quiet; then
    log "Nada novo para commitar"
else
    git commit -m "🚀 KOBLLUX TRINITY SYSTEM · Estrutura completa

🏗️ 13 FASES · 52 FACETAS · 13 OPCODES · 7 LINGUAGENS
📁 93 pastas · 📄 417 arquivos · ⚡ 78K ATIVADO
🧿 Assinatura: 0x012123456789ABC
📜 Equação: VERDADE × INTEGRAR ÷ ∆ = ∞

EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO. AMÉM."
fi

# 6) Push para o GitHub
log "Enviando para o GitHub..."

# Se tiver PAT configurado, usar URL com token
if [ -n "$GITHUB_PAT" ]; then
    log "Usando autenticação via PAT"
    git remote set-url origin "https://${REPO_OWNER}:${GITHUB_PAT}@github.com/${REPO_OWNER}/${REPO_NAME}.git"
fi

# Tentar push
if git push -u origin main 2>/dev/null; then
    log "✅ PUSH REALIZADO COM SUCESSO!"
    log "Repositório: https://github.com/${REPO_OWNER}/${REPO_NAME}.git"
else
    log "⚠️ Push falhou. Provavelmente precisa de autenticação."
    
    cat <<MSG

🔑 AUTENTICAÇÃO NECESSÁRIA:

1. Crie um token em: https://github.com/settings/tokens
   - Clique em "Generate new token (classic)"
   - Marque a opção "repo"
   - Copie o token gerado

2. Execute novamente com o token:
   export GITHUB_PAT="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"
   ./${0##*/}

   OU configure diretamente:
   git remote set-url origin "https://${REPO_OWNER}:SEU_TOKEN@github.com/${REPO_OWNER}/${REPO_NAME}.git"
   git push -u origin main

MSG
fi

log "Script concluído!"