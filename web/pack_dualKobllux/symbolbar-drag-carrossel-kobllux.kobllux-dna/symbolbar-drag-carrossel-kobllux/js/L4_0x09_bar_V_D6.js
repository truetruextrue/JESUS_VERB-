/* ═══════════════════════════════════════════════════════════
   0x09 · MANIFESTAR · V · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : symbolbar-drag-carrossel-kobllux/js/L4_0x09_bar_V_D6.js
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
     S = 139  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=963)
     χ = 2  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
const BAR = {
    el: null,
    track: null,
    isDragging: false,
    moved: false,
    startX: 0, startY: 0,
    offsetX: 0, offsetY: 0,
    EDGE_THRESHOLD: 110,    // px da borda para shrink
    carouselIdx: 0,
    carouselPages: 0,
    SHRUNK_SLOTS: 3,
    totalSlots: 0,

    init() {
      this.el    = $('#symbolBar');
      this.track = $('#barTrack');
      this.totalSlots = $$('#barTrack .symbol-wrap').length;
      this.carouselPages = Math.max(1, Math.ceil(this.totalSlots / this.SHRUNK_SLOTS));
      this.buildDots();

      // arrasta na barra mas NÃO nos botões
      this.el.addEventListener('pointerdown', this.onPointerDown.bind(this));
      window.addEventListener('pointermove', this.onPointerMove.bind(this));
      window.addEventListener('pointerup',   this.onPointerUp.bind(this));
      window.addEventListener('pointercancel', this.onPointerUp.bind(this));
      window.addEventListener('resize', () => this.applyDock());

      // posição inicial logo após boot
      this.placeAt(window.innerWidth * 0.06, window.innerHeight * 0.5);
      this.applyDock();
    },

    buildDots() {
      const dots = $('#carouselDots');
      dots.innerHTML = '';
      for (let i = 0; i < this.carouselPages; i++) {
        const d = document.createElement('span');
        d.className = 'dot' + (i === 0 ? ' active' : '');
        dots.appendChild(d);
      }
    },

    onPointerDown(e) {
      // ignora clique dentro de botão (só drag no chrome)
      if (e.target.closest('.symbol-button')) return;
      this.isDragging = true;
      this.moved = false;
      this.startX = e.clientX;
      this.startY = e.clientY;
      const rect = this.el.getBoundingClientRect();
      this.offsetX = e.clientX - rect.left;
      this.offsetY = e.clientY - rect.top;
      this.el.classList.add('dragging');
      this.el.setPointerCapture?.(e.pointerId);
      e.preventDefault();
    },

    onPointerMove(e) {
      if (!this.isDragging) return;
      const dx = e.clientX - this.startX;
      const dy = e.clientY - this.startY;
      if (Math.abs(dx) > 4 || Math.abs(dy) > 4) this.moved = true;

      const x = e.clientX - this.offsetX;
      const y = e.clientY - this.offsetY;
      // posiciona sem transform (drag livre)
      this.el.style.left = x + 'px';
      this.el.style.top  = y + 'px';
      this.el.style.right = 'auto';
      this.el.style.bottom = 'auto';
      this.el.style.transform = 'none';

      // pré-visualiza orientação durante drag
      this.previewOrientation(x, y);
    },

    onPointerUp(e) {
      if (!this.isDragging) return;
      this.isDragging = false;
      this.el.classList.remove('dragging');
      this.el.releasePointerCapture?.(e.pointerId);

      if (this.moved) {
        this.applyDock();
        KOBLLUX_LOG.emit('BAR·DRAG', {
          x: e.clientX, y: e.clientY,
          detail: this.el.classList.contains('shrunk') ? 'shrunk' : 'full'
        });
      }
    },

    previewOrientation(x, y) {
      // se está próximo do topo ou rodapé → horizontal
      const w = window.innerWidth;
      const h = window.innerHeight;
      const rect = this.el.getBoundingClientRect();
      const nearTop    = y < this.EDGE_THRESHOLD;
      const nearBottom = (y + rect.height) > (h - this.EDGE_THRESHOLD);
      const horizontal = nearTop || nearBottom;
      this.el.classList.toggle('is-horizontal', horizontal);
      this.el.classList.toggle('shrunk', nearTop || nearBottom);
    },

    applyDock() {
      const rect = this.el.getBoundingClientRect();
      const w = window.innerWidth;
      const h = window.innerHeight;

      const nearTop    = rect.top < this.EDGE_THRESHOLD;
      const nearBottom = rect.bottom > (h - this.EDGE_THRESHOLD);
      const horizontal = nearTop || nearBottom;
      const shrunk     = nearTop || nearBottom;

      this.el.classList.toggle('is-horizontal', horizontal);
      this.el.classList.toggle('shrunk', shrunk);

      // se shrunk, ajusta para offset 0 do carrossel
      if (shrunk) {
        this.carouselIdx = 0;
        this.updateCarousel();
      } else {
        // restaura translate dos slots
        this.track.style.transform = '';
      }

      // clamp à viewport
      const clampedLeft = Math.max(8, Math.min(w - rect.width  - 8, rect.left));
      const clampedTop  = Math.max(8, Math.min(h - rect.height - 8, rect.top));
      this.el.style.left = clampedLeft + 'px';
      this.el.style.top  = clampedTop  + 'px';
      this.el.style.transform = 'none';
    },

    // ── Carrossel no modo shrunk ──
    updateCarousel() {
      const offset = this.carouselIdx * this.SHRUNK_SLOTS;
      const slotPx = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--slot-h')) || 54;
      const gap    = 12;
      const step   = (slotPx + gap) * this.SHRUNK_SLOTS;
      if (this.el.classList.contains('is-horizontal')) {
        this.track.style.transform = `translateX(-${offset * (slotPx + gap)}px)`;
      } else {
        this.track.style.transform = `translateY(-${offset * (slotPx + gap)}px)`;
      }
      // atualiza dots
      $$('#carouselDots .dot').forEach((d, i) => d.classList.toggle('active', i === this.carouselIdx));
      KOBLLUX_LOG.emit('BAR·CAROUSEL', { detail: `page ${this.carouselIdx + 1}/${this.carouselPages}` });
    },

    cycleCarousel(dir) {
      if (!this.el.classList.contains('shrunk')) return;
      this.carouselIdx = (this.carouselIdx + dir + this.carouselPages) % this.carouselPages;
      this.updateCarousel();
    },

    placeAt(x, y) {
      this.el.style.left = x + 'px';
      this.el.style.top  = y + 'px';
      this.el.style.right = 'auto';
      this.el.style.bottom = 'auto';
      this.el.style.transform = 'none';
    }
  };

  // ═══════════════════════════════════════════════════════════
  // [SWIPE no track quando shrunk → carrossel]
  // ═══════════════════════════════════════════════════════════