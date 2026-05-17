/* ═══════════════════════════════════════════════════════════
   0x03 · EXPANDIR · V · D7
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L4_0x03_u_V_D7.js
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
     χ = 0  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function onBlockClick(block, para) {
    STATE.autoAdvance = false;
    block.classList.add('clicked');
    setTimeout(() => block.classList.remove('clicked'), 800);
    if (block.dataset.spoken) {
      block.classList.toggle('expanded');
    } else {
      block.dataset.spoken = '1';
    }
    try {
      speechSynthesis.cancel();
      const u = new SpeechSynthesisUtterance(para);
      u.lang = 'pt-BR'; u.rate = 1.1;
      speechSynthesis.speak(u);
    } catch(e) {}
    KOBLLUX_LOG.emit('CHAT·BLOCK', { detail: para.slice(0, 60) + (para.length > 60 ? '…' : '') });
  }