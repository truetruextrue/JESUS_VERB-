/* ╔══════════════════════════════════════════════════════════╗
   ║  PORTAL NEXUS FX                                        ║
   ║  • Long-press 3s em botão do symbolbar → abre editor   ║
   ║    de data-url (#kblx-back / #kblx-panel)              ║
   ║  • Toast helper window.kblxToast(msg, ms)              ║
   ║  • Anel de progresso visual durante o long-press       ║
   ╚══════════════════════════════════════════════════════════╝ */
(function(){
  'use strict';
  const LONG_MS = 3000;
  const DASH = 119.38;

  let _activeBtn = null, _timer = null, _raf = null, _t0 = null;

  function ensureRing(btn) {
    if (btn.querySelector('.kblx-ring')) return;
    btn.style.position = 'relative';
    const d = document.createElement('div');
    d.className = 'kblx-ring';
    d.innerHTML = '<svg viewBox="0 0 44 44"><circle cx="22" cy="22" r="19"/></svg>';
    btn.appendChild(d);
  }
  function setRingPct(btn, pct) {
    const c = btn.querySelector('.kblx-ring circle');
    if (!c) return;
    c.style.transition = 'none';
    c.style.strokeDashoffset = DASH * (1 - Math.min(pct, 1));
  }
  function resetRing(btn) {
    if (!btn) return;
    const c = btn.querySelector('.kblx-ring circle');
    if (!c) return;
    c.style.transition = 'stroke-dashoffset .2s ease';
    c.style.strokeDashoffset = DASH;
  }

  function getPanelEls() {
    return {
      back:  document.getElementById('kblx-back'),
      panel: document.getElementById('kblx-panel'),
      ttl:   document.getElementById('kblx-ttl'),
      inp:   document.getElementById('kblx-inp')
    };
  }

  function openPanel(btn) {
    const { back, ttl, inp } = getPanelEls();
    if (!back || !ttl || !inp) return;
    _activeBtn = btn;
    const sym = (btn.textContent.trim().match(/\S/)||[''])[0] || btn.dataset.id || '?';
    ttl.textContent = 'Botão  ' + sym + '  [data-id="' + (btn.dataset.id || '') + '"]';
    inp.value = btn.dataset.url || '';
    back.classList.add('open');
    setTimeout(()=>inp.focus(), 80);
  }
  function closePanel() {
    const { back } = getPanelEls();
    if (back) back.classList.remove('open');
    _activeBtn = null;
  }
  function saveUrl() {
    if (!_activeBtn) return closePanel();
    const { inp } = getPanelEls();
    const v = (inp?.value || '').trim();
    if (v) {
      _activeBtn.dataset.url = v;
      window.kblxToast && window.kblxToast('✓ data-url atualizado');
    }
    closePanel();
  }

  function attachLongPress(btn) {
    ensureRing(btn);
    function onDown(){
      _t0 = Date.now();
      _timer = setTimeout(()=>{
        cancelAnimationFrame(_raf);
        resetRing(btn);
        _t0 = null;
        openPanel(btn);
      }, LONG_MS);
      (function tick(){
        if (_t0 === null) return;
        setRingPct(btn, (Date.now()-_t0)/LONG_MS);
        _raf = requestAnimationFrame(tick);
      })();
    }
    function onUp(){
      clearTimeout(_timer);
      cancelAnimationFrame(_raf);
      resetRing(btn);
      _t0 = null;
    }
    ['pointerdown'].forEach(e => btn.addEventListener(e, onDown, { passive:true }));
    ['pointerup','pointerleave','pointercancel'].forEach(e => btn.addEventListener(e, onUp, { passive:true }));
  }

  // Toast
  window.kblxToast = function(msg, ms){
    const el = document.getElementById('kblx-toast');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('show');
    clearTimeout(el._t);
    el._t = setTimeout(()=>el.classList.remove('show'), ms || 2200);
  };

  function init() {
    document.querySelectorAll('#symbolBar .symbol-button').forEach(attachLongPress);

    const saveBtn  = document.getElementById('kblx-btn-save');
    const closeBtn = document.getElementById('kblx-btn-close');
    const back     = document.getElementById('kblx-back');
    saveBtn  && saveBtn .addEventListener('click', saveUrl);
    closeBtn && closeBtn.addEventListener('click', closePanel);
    back     && back    .addEventListener('click', e => { if (e.target === back) closePanel(); });
    document.addEventListener('keydown', e => {
      if (!back || !back.classList.contains('open')) return;
      if (e.key === 'Escape') closePanel();
      if (e.key === 'Enter')  saveUrl();
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
