/* ═══════════════════════════════════════════════════════════
   0x03 · EXPANDIR · V · D7
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-particle-cosmos-3-6-9-logger/js/L4_0x03_card_V_D7.js
   Opcode    : 0x03 · EXPANDIR · ▢ · 639Hz
   V.E.E.B.  : Vibração
   Degrau    : D7 (module)
   Fórmula   : Vibração · f₃=639Hz · crescimento fractal · V=(4/3)πr³
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=639)
     χ = -2  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function toggleCard() {
    const card = $('#mainCard');
    const wasClosed = card.classList.contains('closed');
    card.classList.toggle('closed', !wasClosed);
    if (wasClosed) {
      // reabriu
      $$('.mode-btn').forEach(b => b.classList.remove('active-mode'));
      $('#btnModeCard').classList.add('active-mode');
      setTimeout(() => $('#inputUser')?.focus(), 300);
      window.KOBLLUX_LOG?.emit('CARD·OPEN', { detail: 'orb → expand' });
    } else {
      $$('.mode-btn').forEach(b => b.classList.remove('active-mode'));
      $('#btnModeOrb').classList.add('active-mode');
      window.KOBLLUX_LOG?.emit('CARD·CLOSE', { detail: 'expand → orb' });
    }
  }