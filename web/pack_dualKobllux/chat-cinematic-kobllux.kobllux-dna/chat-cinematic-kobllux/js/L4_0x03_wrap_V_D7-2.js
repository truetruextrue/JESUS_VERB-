/* ═══════════════════════════════════════════════════════════
   0x03 · EXPANDIR · V · D7
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L4_0x03_wrap_V_D7-2.js
   Opcode    : 0x03 · EXPANDIR · ▢ · 639Hz
   V.E.E.B.  : Vibração
   Degrau    : D7 (module)
   Fórmula   : Vibração · f₃=639Hz · crescimento fractal · V=(4/3)πr³
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=639)
     χ = 0  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function showLoading(msg) {
    const wrap = $('.pages-wrapper');
    wrap.innerHTML = '';
    const p = document.createElement('div'); p.className = 'page active initial';
    const f = document.createElement('p'); f.className = 'footer-text loading';
    msg.split('').forEach((ch, i) => {
      const s = document.createElement('span'); s.textContent = ch;
      s.style.animationDelay = (i * .02) + 's';
      f.appendChild(s);
    });
    p.appendChild(f); wrap.appendChild(p);
    $('#pageIndicator').textContent = '1 / 1';
  }

  // ═══════════════════════════════════════════════════════════
  // [BOOT TEXT TYPEWRITER]
  // ═══════════════════════════════════════════════════════════