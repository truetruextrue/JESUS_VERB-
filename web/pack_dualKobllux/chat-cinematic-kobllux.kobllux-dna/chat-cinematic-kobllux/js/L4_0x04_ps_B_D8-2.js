/* ═══════════════════════════════════════════════════════════
   0x04 · DISSOLVER · B · D8
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L4_0x04_ps_B_D8-2.js
   Opcode    : 0x04 · DISSOLVER · ◇ · 594Hz
   V.E.E.B.  : Base
   Degrau    : D8 (system)
   Fórmula   : Base · f₄=594Hz · transição de fase · forma em dissolução
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=594)
     χ = 0  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function splitText(t) {
    let ps = t.split(/\n\s*\n/).filter(p => p.trim());
    if (ps.length < 2) ps = (t.match(/[^\.!\?]+[\.!\?]+/g) || []).map(s => s.trim());
    return ps;
  }