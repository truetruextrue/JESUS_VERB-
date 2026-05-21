#!/bin/bash
INDEX_FILE="index.html"

echo "🔄 Atualizando index.html..."

# Adicionar entrada do sistema endócrino no log
if grep -q "Sistema endócrino online" "$INDEX_FILE"; then
    echo "✅ Sistema endócrino já está no log"
else
    # Adicionar após "sistema circulatório online"
    sed -i '/Sistema circulatório online/a\            <div class="log-entry">[ENDOCRINE] Sistema endócrino online</div>' "$INDEX_FILE"
    echo "✅ Sistema endócrino adicionado ao log"
fi

# Atualizar contagem de sistemas
sed -i 's/SISTEMAS ATIVOS.*6\/8/SISTEMAS ATIVOS 7\/8/' "$INDEX_FILE" 2>/dev/null || true
sed -i 's/sistemas ativos: 6/&1/' "$INDEX_FILE" 2>/dev/null || true

# Adicionar link para o sistema endócrino
if ! grep -q "endocrine" "$INDEX_FILE"; then
    # Adicionar após o link do sistema circulatório
    sed -i '/Sistema Circulatório<\/a>/a\                <a href="systems/endocrine/status-indicator.html" class="system-link">\n                    <div class="system-icon">⚡</div>\n                    <div class="system-name">Sistema Endócrino</div>\n                    <div class="system-status endocrine">SINCRONIZANDO</div>\n                </a>' "$INDEX_FILE"
    echo "✅ Link do sistema endócrino adicionado"
fi

echo "🎯 Index atualizado com sucesso!"
