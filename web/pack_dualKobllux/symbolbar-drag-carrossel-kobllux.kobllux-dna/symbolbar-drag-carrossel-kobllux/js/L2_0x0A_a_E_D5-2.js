/* ═══════════════════════════════════════════════════════════
   0x0A · EQUILIBRAR · E · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : symbolbar-drag-carrossel-kobllux/js/L2_0x0A_a_E_D5-2.js
   Opcode    : 0x0A · EQUILIBRAR · ⚖ · 528Hz
   V.E.E.B.  : Energia
   Degrau    : D5 (block)
   Fórmula   : Energia · f_A=528Hz · teorema do virial · SO(2) simetria
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 2 · REGISTRO
   Opcode Δ  : 0x08 · Carregar na posição 2 da cadeia
   Nota      : Log + identidade — sem DOM
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=528)
     χ = 1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function applyArchetype(idx) {
    currentArchIdx = (idx + ARCHETYPES_DB.length) % ARCHETYPES_DB.length;
    const a  = ARCHETYPES_DB[currentArchIdx];
    const op = KOBLLUX_OPCODES[a.opcode];
    document.documentElement.style.setProperty('--arch-primary', a.primary);
    document.documentElement.style.setProperty('--arch-secondary', op.cor);
    $('#archLabel').textContent = `${a.name} · ${a.opcode} ${op.nome}`;
    $('#archTag').textContent   = a.opcode;
    $('#hudStatus').textContent = `KOBLLUX · ${a.name}`;
    localStorage.setItem('di_activeArchetype', a.id);
  }