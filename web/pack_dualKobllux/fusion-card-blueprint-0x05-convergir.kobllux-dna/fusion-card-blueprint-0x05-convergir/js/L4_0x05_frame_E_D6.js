/* ═══════════════════════════════════════════════════════════
   0x05 · CONVERGIR · E · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-blueprint-0x05-convergir/js/L4_0x05_frame_E_D6.js
   Opcode    : 0x05 · CONVERGIR · ⧉ · 672Hz
   V.E.E.B.  : Energia
   Degrau    : D6 (section)
   Fórmula   : Energia · f₅=672Hz · fluxo convergente · L₁∩L₂=P*
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=672)
     χ = 2  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function bpCall(action) {
      const frame = document.querySelector('.bp-iframe');
      const w = frame?.contentWindow;
      if (!w || !w.KOBLLUX_CARD) return;
      const api = w.KOBLLUX_CARD;
      switch (action) {
        case 'toggleCard': api.toggleCard(); break;
        case 'openKeys':   api.openModal('#keysModal'); break;
      }
    }