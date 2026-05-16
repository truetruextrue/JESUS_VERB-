/* ═══════════════════════════════════════════════════════════
   0x01 · PULSAR · V · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L4_0x01_el_V_D5-3.js
   Opcode    : 0x01 · PULSAR · ● · 432Hz
   V.E.E.B.  : Vibração
   Degrau    : D5 (block)
   Fórmula   : Vibração · f₁=432Hz · P(t)=A·sin(2π·432·t) · impulso sonoro
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=432)
     χ = 1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function bootTypewriter() {
    const el = $('#bootText');
    const txt = el?.dataset?.text || '';
    if (!el) return;
    el.textContent = '';
    let i = 0;
    const tick = () => {
      if (i < txt.length) {
        el.textContent += txt.charAt(i++);
        setTimeout(tick, 38);
      } else {
        el.classList.add('pulse');
      }
    };
    tick();
  }

  // ═══════════════════════════════════════════════════════════
  // [INPUT HANDLER · mapeamento simbólico local]
  // ═══════════════════════════════════════════════════════════