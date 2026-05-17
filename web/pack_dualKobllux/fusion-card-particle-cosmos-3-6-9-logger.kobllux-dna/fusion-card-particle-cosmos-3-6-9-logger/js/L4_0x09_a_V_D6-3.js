/* ═══════════════════════════════════════════════════════════
   0x09 · MANIFESTAR · V · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-particle-cosmos-3-6-9-logger/js/L4_0x09_a_V_D6-3.js
   Opcode    : 0x09 · MANIFESTAR · ♾ · 963Hz
   V.E.E.B.  : Vibração
   Degrau    : D6 (section)
   Fórmula   : Vibração · f₉=963Hz · campo→forma visual · S² χ=2
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=963)
     χ = 1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function syncParticlesToArchetype() {
    if (!window.pJSDom || !window.pJSDom.length) return;
    try {
      const a  = STATE.archetype;
      const op = KOBLLUX_OPCODES[a.opcode];
      const ps = window.pJSDom[0].pJS;
      ps.particles.color.value = [a.primary, op.cor, '#ffffff'];
      ps.particles.line_linked.color = a.primary;
      // re-render cores em tempo real
      ps.particles.array.forEach(p => {
        const pool = [a.primary, op.cor, '#ffffff'];
        const hex  = pool[Math.floor(Math.random() * pool.length)];
        const h = hex.replace('#','');
        p.color.rgb = {
          r: parseInt(h.substring(0,2),16),
          g: parseInt(h.substring(2,4),16),
          b: parseInt(h.substring(4,6),16)
        };
      });
      ps.fn.particlesRefresh();
    } catch(e) { /* silent */ }
  }
  // hook: aplicar arch também ressoa partículas