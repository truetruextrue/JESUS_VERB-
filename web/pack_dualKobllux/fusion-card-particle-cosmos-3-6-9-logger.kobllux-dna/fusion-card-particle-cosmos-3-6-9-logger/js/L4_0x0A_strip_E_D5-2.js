/* ═══════════════════════════════════════════════════════════
   0x0A · EQUILIBRAR · E · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-particle-cosmos-3-6-9-logger/js/L4_0x0A_strip_E_D5-2.js
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
     χ = -1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function buildStrip() {
    const strip = $('#archStrip');
    strip.innerHTML = '';
    ARCHETYPES_DB.forEach((a, i) => {
      const chip = document.createElement('div');
      chip.className = 'arch-chip';
      chip.style.background = `radial-gradient(circle at 35% 35%, ${a.primary}, ${KOBLLUX_OPCODES[a.opcode].cor})`;
      chip.style.color = a.primary;
      chip.title = `${a.name} · ${a.opcode} ${KOBLLUX_OPCODES[a.opcode].nome}`;
      chip.addEventListener('click', () => applyArchetype(i));
      strip.appendChild(chip);
    });
  }

  // ═══════════════════════════════════════════════════════════
  // [NAME SYNC] · di_syncNameUI
  // ═══════════════════════════════════════════════════════════