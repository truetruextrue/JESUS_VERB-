/* ═══════════════════════════════════════════════════════════
   0x09 · MANIFESTAR · V · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L4_0x09_wrap_V_D6-2.js
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
function renderResponse(txt) {
    const wrap = $('.pages-wrapper');
    wrap.innerHTML = '';
    STATE.pages = []; STATE.currentPage = 0; STATE.autoAdvance = true;

    txt = txt
      .replace(/`([^`]+)`/g,    '<code>$1</code>')
      .replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.+?)\*/g,     '<em>$1</em>');

    const paras = splitText(txt);
    const total = paras.length;
    if (total === 0) return;

    const maxPerPage = 3;
    const numPages = Math.ceil(total / maxPerPage);
    const baseSize = Math.floor(total / numPages);
    const extra = total % numPages;

    let cursor = 0;
    for (let i = 0; i < numPages; i++) {
      const thisSize = baseSize + (i < extra ? 1 : 0);
      const pg = document.createElement('div');
      pg.className = 'page' + (i === 0 ? ' active' : '');
      for (let j = 0; j < thisSize; j++) {
        const para = paras[cursor++].trim();
        const posClass = j === 0 ? 'intro' : (j === thisSize - 1 ? 'ending' : 'middle');
        const block = document.createElement('div');
        block.className = `response-block ${posClass}`;
        block.innerHTML = `<p>${para}</p>`;
        block.addEventListener('click', () => onBlockClick(block, para));
        pg.appendChild(block);
      }
      wrap.appendChild(pg);
      STATE.pages.push(pg);
    }
    $('#pageIndicator').textContent = `1 / ${STATE.pages.length}`;
    KOBLLUX_LOG.emit('CHAT·RENDER', { detail: `${total} parágrafos · ${numPages} páginas` });
  }