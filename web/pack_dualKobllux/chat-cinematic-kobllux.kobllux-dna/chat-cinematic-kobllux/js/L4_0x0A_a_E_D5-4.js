/* ═══════════════════════════════════════════════════════════
   0x0A · EQUILIBRAR · E · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L4_0x0A_a_E_D5-4.js
   Opcode    : 0x0A · EQUILIBRAR · ⚖ · 528Hz
   V.E.E.B.  : Energia
   Degrau    : D5 (block)
   Fórmula   : Energia · f_A=528Hz · teorema do virial · SO(2) simetria
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=528)
     χ = 2  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function initParticles() {
    if (typeof particlesJS === 'undefined') return;
    const a = STATE.archetype, op = KOBLLUX_OPCODES[a.opcode];
    particlesJS('particles-js', {
      particles: {
        number:  { value: 40 },
        color:   { value: [a.primary, op.cor] },
        shape:   { type: 'circle' },
        opacity: { value: 0.4 },
        size:    { value: 2.4 },
        line_linked: { enable: true, distance: 140, color: a.primary, opacity: 0.12, width: 1 },
        move:    { enable: true, speed: 1.5 }
      },
      retina_detect: true
    });
  }