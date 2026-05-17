/* ═══════════════════════════════════════════════════════════
   0x01 · PULSAR · V · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : symbolbar-drag-carrossel-kobllux/js/L7_0x01_savedarch_V_D5-3.js
   Opcode    : 0x01 · PULSAR · ● · 432Hz
   V.E.E.B.  : Vibração
   Degrau    : D5 (block)
   Fórmula   : Vibração · f₁=432Hz · P(t)=A·sin(2π·432·t) · impulso sonoro
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 7 · ORQUESTRADOR
   Opcode Δ  : 0x0C · Carregar na posição 7 da cadeia
   Nota      : Init — espera DOM + todos os scripts
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 62  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=432)
     χ = -13  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
    const savedArch = localStorage.getItem('di_activeArchetype');
    const idx = ARCHETYPES_DB.findIndex(a => a.id === savedArch);
    applyArchetype(idx >= 0 ? idx : 0);

    BAR.init();
    bindCarouselSwipe();

    // botões
    $('#toggleBtn').addEventListener('click', () => {
      KOBLLUX_LOG.emit('BAR·TOGGLE');
      // toggle manual shrunk
      const wasShrunk = BAR.el.classList.contains('shrunk');
      BAR.el.classList.toggle('shrunk');
      if (!wasShrunk) { BAR.carouselIdx = 0; BAR.updateCarousel(); }
      else            { BAR.track.style.transform = ''; }
    });

    bindLongPress(
      $('#btn-arch'),
      () => {
        const log = KOBLLUX_LOG.emit('ORB·RESSONA');
        BAR.el.classList.add('speaking');
        setTimeout(() => BAR.el.classList.remove('speaking'), 900);
        if (log.val === 9) nextArchetype();
      },
      () => nextArchetype()
    );

    $('#btn-prev').addEventListener('click', () => { KOBLLUX_LOG.emit('PLAY·PREV'); prevArchetype(); });
    $('#btn-play').addEventListener('click', (e) => {
      const btn = e.currentTarget;
      const playing = btn.dataset.playing === '1';
      btn.dataset.playing = playing ? '0' : '1';
      btn.textContent = playing ? '▶' : '∥∥';
      KOBLLUX_LOG.emit('PLAY·TOGGLE', { detail: playing ? 'PAUSE' : 'PLAY' });
    });
    $('#btn-next').addEventListener('click', () => { KOBLLUX_LOG.emit('PLAY·NEXT'); nextArchetype(); });

    $$('.symbol-button[data-id]').forEach(b => {
      b.addEventListener('click', () => {
        KOBLLUX_LOG.emit('NAV·' + b.dataset.id.toUpperCase(), { detail: b.dataset.url });
      });
    });

    ['pointerdown','pointermove','touchstart','mousemove','keydown','scroll']
      .forEach(ev => document.addEventListener(ev, resetIdle, { passive: true }));
    resetIdle();

    document.addEventListener('keydown', (e) => {
      if (e.target.matches('input, textarea, select')) return;
      if (e.key === 'ArrowRight') {
        if (BAR.el.classList.contains('shrunk')) BAR.cycleCarousel(1);
        else nextArchetype();
        e.preventDefault();
      }
      if (e.key === 'ArrowLeft')  {
        if (BAR.el.classList.contains('shrunk')) BAR.cycleCarousel(-1);
        else prevArchetype();
        e.preventDefault();
      }
    });

    setTimeout(() => KOBLLUX_LOG.emit('BAR·BOOT', { detail: 'drag livre · shrink em bordas · carrossel' }), 80);
  });

  // expor API
  window.KOBLLUX_BAR = {
    applyArchetype, nextArchetype, prevArchetype,
    ARCHETYPES_DB, KOBLLUX_OPCODES,
    BAR
  };