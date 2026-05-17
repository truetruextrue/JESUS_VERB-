/* ═══════════════════════════════════════════════════════════
   0x08 · TESTEMUNHAR · E2 · D3
   ═══════════════════════════════════════════════════════════
   Arquivo   : symbolbar-drag-carrossel-kobllux/js/L4_0x08_track_E2_D3.js
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
     χ = 1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function bindCarouselSwipe() {
    const track = $('#barTrack');
    let sx = 0, sy = 0, swiping = false;
    track.addEventListener('pointerdown', (e) => {
      if (!BAR.el.classList.contains('shrunk')) return;
      if (e.target.closest('.symbol-button')) return; // botões priorizam click
      swiping = true;
      sx = e.clientX; sy = e.clientY;
    });
    track.addEventListener('pointerup', (e) => {
      if (!swiping) return;
      swiping = false;
      const dx = e.clientX - sx;
      const dy = e.clientY - sy;
      const horiz = BAR.el.classList.contains('is-horizontal');
      const delta = horiz ? dx : dy;
      if (Math.abs(delta) > 30) {
        BAR.cycleCarousel(delta < 0 ? 1 : -1);
      }
    });
    track.addEventListener('pointercancel', () => swiping = false);
  }

  // ═══════════════════════════════════════════════════════════
  // [LONG PRESS · orb central]
  // ═══════════════════════════════════════════════════════════