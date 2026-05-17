/* ═══════════════════════════════════════════════════════════
   0x0A · EQUILIBRAR · E · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-core-isolado/js/L3_0x0A_safe_E_D5.js
   Opcode    : 0x0A · EQUILIBRAR · ⚖ · 528Hz
   V.E.E.B.  : Energia
   Degrau    : D5 (block)
   Fórmula   : Energia · f_A=528Hz · teorema do virial · SO(2) simetria
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 3 · STORAGE_DOM
   Opcode Δ  : 0x06 · Carregar na posição 3 da cadeia
   Nota      : Storage + DOM — só após HTML parseado
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=528)
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

      $('#avatarTarget').innerHTML    = makeOrbAvatar(safe, 64);
      $('#smallMiniAvatar').innerHTML = makeOrbAvatar(safe, 24);
      $('#actMiniAvatar').innerHTML   = makeOrbAvatar(safe, 36);

      const activeKey = { name: 'Principal' };
      $('#smallIdent').textContent = activeKey ? activeKey.name : '--';
      $('#actBadge').textContent   = activeKey ? `key:${activeKey.name}` : 'v:--';
    }

    // ═══════════════════════════════════════════════════════════
    // [JS::TOGGLE-SECTION]  abre/fecha activation-cards (accordion)
    // ═══════════════════════════════════════════════════════════