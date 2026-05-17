/* ═══════════════════════════════════════════════════════════
   0x05 · CONVERGIR · E · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-core-isolado/js/L2_0x05_safe_E_D6.js
   Opcode    : 0x05 · CONVERGIR · ⧉ · 672Hz
   V.E.E.B.  : Energia
   Degrau    : D6 (section)
   Fórmula   : Energia · f₅=672Hz · fluxo convergente · L₁∩L₂=P*
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 2 · REGISTRO
   Opcode Δ  : 0x08 · Carregar na posição 2 da cadeia
   Nota      : Log + identidade — sem DOM
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=672)
     χ = 1  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function makeOrbAvatar(name, size = 36) {
      const safe = name || 'DUAL';
      const seed = safe.split('').reduce((a, c) => a + c.charCodeAt(0), 0);
      const h1 = seed % 360;
      const h2 = (seed * 37) % 360;
      const uid = Math.random().toString(36).slice(2, 6);
      const id = 'g' + seed.toString(36) + uid;
      return `
        <svg width="${size}" height="${size}" viewBox="0 0 32 32" xmlns="http://www.w3.org/2000/svg">
          <defs>
            <linearGradient id="${id}" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="hsl(${h1},100%,55%)"/>
              <stop offset="100%" stop-color="hsl(${h2},90%,45%)"/>
            </linearGradient>
          </defs>
          <rect width="32" height="32" rx="7" fill="#071018"/>
          <circle cx="16" cy="16" r="9"  fill="url(#${id})" opacity="0.25"/>
          <circle cx="16" cy="16" r="7"  fill="url(#${id})"/>
          <circle cx="16" cy="16" r="13" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="1"/>
        </svg>`;
    }
    window.makeOrbAvatar = makeOrbAvatar;

    // ═══════════════════════════════════════════════════════════
    // [JS::SYNC-NAME]  di_syncNameUI(name)
    //   propaga nome em todos os slots do card + persiste localStorage
    // ═══════════════════════════════════════════════════════════