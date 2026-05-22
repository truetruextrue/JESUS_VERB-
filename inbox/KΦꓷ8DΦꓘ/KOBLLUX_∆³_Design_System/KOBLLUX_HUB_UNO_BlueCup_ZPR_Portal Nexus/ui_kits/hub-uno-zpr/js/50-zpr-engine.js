/* ╔══════════════════════════════════════════════════════════╗
   ║  ZPR ENGINE · 3×4 grid + swipe + dots + cursor          ║
   ║  Adaptado de GUARD_0X09_feeling-decor-ZPR_VEEB-U_D6     ║
   ║  Expõe: window.navigateToCell(row,col),                 ║
   ║          window.navigateToView(viewId|navName)          ║
   ╚══════════════════════════════════════════════════════════╝ */
(function(){
  'use strict';

  const ROWS = 3, COLS = 4;
  const grid = document.getElementById('universe-grid');
  if (!grid) { console.warn('[ZPR] #universe-grid não encontrado'); return; }

  // Cell map (row,col) → view id (matches data-nav of symbolbar buttons)
  const CELL_MAP = [
    // Row 0
    [{view:'v-home',   nav:'home',    opcode:'0x00', glyph:'○'},
     {view:'v-apps',   nav:'apps',    opcode:'0x01', glyph:'●'},
     {view:'v-stack',  nav:'stack',   opcode:'0x02', glyph:'―'},
     {view:'v-brain',  nav:'brain',   opcode:'0x03', glyph:'▢'}],
    // Row 1
    [{view:'v-chat',   nav:'chat',    opcode:'0x04', glyph:'◇'},
     {view:'v-voz',    nav:'voz',     opcode:'0x05', glyph:'⧉'},
     {view:'v-espelho',nav:'espelho', opcode:'0x06', glyph:'☯'},
     {view:'v-arq',    nav:'arq',     opcode:'0x07', glyph:'✧'}],
    // Row 2
    [{view:'v-uno',    nav:'uno',     opcode:'0x08', glyph:'◉'},
     {view:'v-core',   nav:'core',    opcode:'0x09', glyph:'♾'},
     {view:'v-aion',   nav:'aion',    opcode:'0x0A', glyph:'⌛'},
     {view:'v-img',    nav:'img',     opcode:'0x0B', glyph:'⌗'}]
  ];

  // Build dots
  const navMatrix = document.getElementById('navMatrix');
  if (navMatrix) {
    navMatrix.innerHTML = '';
    navMatrix.style.setProperty('--zpr-cols', COLS);
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        const cell = CELL_MAP[r][c];
        const dot = document.createElement('div');
        dot.className = 'matrix-dot';
        dot.dataset.row = r;
        dot.dataset.col = c;
        dot.dataset.opcode = cell.opcode;
        dot.dataset.view = cell.view;
        dot.title = cell.opcode + ' · ' + cell.nav + ' · ' + cell.glyph;
        dot.addEventListener('click', () => navigateToCell(r, c));
        navMatrix.appendChild(dot);
      }
    }
  }

  // State
  let currentRow = 0, currentCol = 0;
  let isAnimating = false;

  // Update transform + dots
  function updateView() {
    const tx = -currentCol * (100 / COLS);
    const ty = -currentRow * (100 / ROWS);
    grid.style.transform = 'translate(' + tx + '%, ' + ty + '%)';

    document.querySelectorAll('.matrix-dot').forEach(d => {
      d.classList.toggle('active',
        +d.dataset.row === currentRow && +d.dataset.col === currentCol);
    });
    document.querySelectorAll('#universe-grid .screen').forEach(s => {
      s.classList.toggle('is-active',
        +s.dataset.row === currentRow && +s.dataset.col === currentCol);
    });
    document.querySelectorAll('#symbolBar .symbol-button[data-nav]').forEach(btn => {
      const v = btn.getAttribute('data-nav');
      const active = (CELL_MAP[currentRow]?.[currentCol]?.nav === v);
      btn.classList.toggle('is-active', active);
    });

    // Update HUD label
    const hud = document.getElementById('hudStatus');
    if (hud) {
      const c = CELL_MAP[currentRow][currentCol];
      hud.textContent = c.opcode + ' · ' + c.nav.toUpperCase();
    }

    // Update browser URL hash (so reload restores cell)
    try { history.replaceState(null, '', '#' + CELL_MAP[currentRow][currentCol].nav); } catch(e){}
  }

  function navigateToCell(row, col) {
    if (row < 0 || row >= ROWS || col < 0 || col >= COLS) return;
    if (row === currentRow && col === currentCol) return;
    if (isAnimating) return;
    isAnimating = true;
    currentRow = row; currentCol = col;
    updateView();
    setTimeout(() => { isAnimating = false; }, 560);
  }
  function navigateToView(idOrNav) {
    for (let r = 0; r < ROWS; r++) {
      for (let c = 0; c < COLS; c++) {
        const cell = CELL_MAP[r][c];
        if (cell.view === idOrNav || cell.nav === idOrNav) {
          return navigateToCell(r, c);
        }
      }
    }
  }

  window.navigateToCell = navigateToCell;
  window.navigateToView = navigateToView;
  window.go = navigateToView;  // bridge: replace HUB UNO router's window.go

  // ── GESTOS ─────────────────────────────────────────────
  const SWIPE_DIST = 50, SWIPE_TIME = 420;
  let drag = { x: 0, y: 0, t: 0, active: false };

  function shouldIgnoreTarget(t) {
    if (!t) return false;
    return !!t.closest('input, textarea, select, .ls-tab, #ls-panel, #kblx-back, #symbolBar, .scroller, #chatFeed, #iaFeed, #logs');
  }

  document.addEventListener('touchstart', e => {
    if (shouldIgnoreTarget(e.target)) return;
    drag.x = e.touches[0].clientX;
    drag.y = e.touches[0].clientY;
    drag.t = Date.now(); drag.active = true;
  }, { passive: true });

  document.addEventListener('touchend', e => {
    if (!drag.active) return;
    drag.active = false;
    if (Date.now() - drag.t > SWIPE_TIME) return;
    const dx = e.changedTouches[0].clientX - drag.x;
    const dy = e.changedTouches[0].clientY - drag.y;
    handleSwipe(dx, dy);
  }, { passive: true });

  // Mouse drag (desktop)
  document.addEventListener('mousedown', e => {
    if (shouldIgnoreTarget(e.target)) return;
    drag.x = e.clientX; drag.y = e.clientY;
    drag.t = Date.now(); drag.active = true;
  });
  document.addEventListener('mouseup', e => {
    if (!drag.active) return;
    drag.active = false;
    const dx = e.clientX - drag.x;
    const dy = e.clientY - drag.y;
    const dt = Date.now() - drag.t;
    if (dt > SWIPE_TIME) return;
    if (Math.abs(dx) < SWIPE_DIST && Math.abs(dy) < SWIPE_DIST) return;
    handleSwipe(dx, dy);
  });

  function handleSwipe(dx, dy) {
    const ax = Math.abs(dx), ay = Math.abs(dy);
    if (ax > ay && ax > SWIPE_DIST) {
      dx < 0 ? navigateToCell(currentRow, currentCol + 1)
             : navigateToCell(currentRow, currentCol - 1);
    } else if (ay > ax && ay > SWIPE_DIST) {
      dy < 0 ? navigateToCell(currentRow + 1, currentCol)
             : navigateToCell(currentRow - 1, currentCol);
    }
  }

  // Keyboard
  document.addEventListener('keydown', e => {
    if (e.target.matches('input,textarea,select')) return;
    switch(e.key) {
      case 'ArrowRight': navigateToCell(currentRow, currentCol+1); e.preventDefault(); break;
      case 'ArrowLeft':  navigateToCell(currentRow, currentCol-1); e.preventDefault(); break;
      case 'ArrowDown':  navigateToCell(currentRow+1, currentCol); e.preventDefault(); break;
      case 'ArrowUp':    navigateToCell(currentRow-1, currentCol); e.preventDefault(); break;
      case 'Home':       navigateToCell(0, 0); e.preventDefault(); break;
    }
  });

  // Wheel (debounced)
  let wheelCooldown = false;
  document.addEventListener('wheel', e => {
    if (shouldIgnoreTarget(e.target)) return;
    if (wheelCooldown) return;
    wheelCooldown = true;
    setTimeout(() => { wheelCooldown = false; }, 750);
    if (Math.abs(e.deltaY) > Math.abs(e.deltaX)) {
      e.deltaY > 0 ? navigateToCell(currentRow+1, currentCol)
                   : navigateToCell(currentRow-1, currentCol);
    } else {
      e.deltaX > 0 ? navigateToCell(currentRow, currentCol+1)
                   : navigateToCell(currentRow, currentCol-1);
    }
  }, { passive: true });

  // Custom cursor (desktop only)
  const cur  = document.getElementById('custom-cursor');
  const ring = document.getElementById('cursor-ring');
  let cx = 0, cy = 0, rx = 0, ry = 0;
  if (cur && ring && window.matchMedia('(pointer: fine)').matches) {
    document.addEventListener('mousemove', e => {
      cx = e.clientX; cy = e.clientY;
      cur.style.left = cx + 'px'; cur.style.top = cy + 'px';
    });
    (function anim() {
      rx += (cx - rx) * 0.12; ry += (cy - ry) * 0.12;
      ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
      requestAnimationFrame(anim);
    })();
  }

  // Initial: read URL hash or default to home (0,0)
  function init() {
    const hash = (location.hash || '').replace(/^#/, '');
    if (hash) {
      for (let r = 0; r < ROWS; r++) for (let c = 0; c < COLS; c++) {
        if (CELL_MAP[r][c].nav === hash) {
          currentRow = r; currentCol = c;
          break;
        }
      }
    }
    updateView();
  }
  init();

  console.log('%c ZPR · 3×4 · 12 VIEWS · KOBLLUX HUB UNO ',
    'background:#c9a84c;color:#000;font-weight:bold;padding:4px 8px;');
})();
