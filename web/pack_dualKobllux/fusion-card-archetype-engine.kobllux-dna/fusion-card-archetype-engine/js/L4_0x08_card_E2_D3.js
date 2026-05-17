/* ═══════════════════════════════════════════════════════════
   0x08 · TESTEMUNHAR · E2 · D3
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-archetype-engine/js/L4_0x08_card_E2_D3.js
   Opcode    : 0x08 · TESTEMUNHAR · ◉ · 852Hz
   V.E.E.B.  : Estrutura
   Degrau    : D3 (word)
   Fórmula   : Estrutura · f₈=852Hz · observação sem colapso · ◉
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=852)
     χ = 0  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function setMode(mode) {
    $$('.mode-btn').forEach(b => b.classList.remove('active-mode'));
    $('#btnMode' + mode.charAt(0).toUpperCase() + mode.slice(1))?.classList.add('active-mode');

    const card = $('#mainCard');
    if (mode === 'orb') {
      card.classList.add('closed');
    } else {
      card.classList.remove('closed');
    }
    console.log('[KOBLLUX] Modo: ' + mode);
  }