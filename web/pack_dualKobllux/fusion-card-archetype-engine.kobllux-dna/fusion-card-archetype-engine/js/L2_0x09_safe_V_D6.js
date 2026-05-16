/* ═══════════════════════════════════════════════════════════
   0x09 · MANIFESTAR · V · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-archetype-engine/js/L2_0x09_safe_V_D6.js
   Opcode    : 0x09 · MANIFESTAR · ♾ · 963Hz
   V.E.E.B.  : Vibração
   Degrau    : D6 (section)
   Fórmula   : Vibração · f₉=963Hz · campo→forma visual · S² χ=2
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 2 · REGISTRO
   Opcode Δ  : 0x08 · Carregar na posição 2 da cadeia
   Nota      : Log + identidade — sem DOM
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=963)
     χ = 1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function di_syncNameUI(name) {
    const safe = (name || '').trim() || 'Convidado';
    localStorage.setItem('di_userName', safe);
    localStorage.setItem('userName', safe);
    $('#lblName').textContent  = safe;
    $('#actName').textContent  = safe;
    $('#smallText').textContent = safe;
    $('#smallIdent').textContent = 'Principal';
    // re-renderiza seed
    applyArchetype(currentArchIdx);
  }

  // ═══════════════════════════════════════════════════════════
  // [TOGGLES]
  // ═══════════════════════════════════════════════════════════