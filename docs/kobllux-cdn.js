/*!
 * kobllux-cdn.js · KOBLLUX TRINITY SYSTEM · ∆7 · v2.0
 * ════════════════════════════════════════════════════════════════════
 * CDN BUNDLE — motor completo em um único script
 *
 * USO:
 *   <script src="https://truetruextrue.github.io/JESUS_VERB-/kobllux-cdn.js"></script>
 *
 * Expõe:
 *   window.KOBLLUX        — API principal
 *   window.KOBLLUX_APPS   — módulos extensíveis
 *
 * Motores incluídos:
 *   · Partículas magenta+cyan portadoras (particles.js auto-load)
 *   · THREE_SIX_NINE logger · 3×6×9 fractal por interação
 *   · EMA [3·6·9] mood detector por frequência Hz
 *   · 12 arquétipos CADIAL com constantes fractais
 *   · KOBLLUX_APPS register/run/list/onArch
 *   · Overlay arquétipo · Toast · Mood ring
 *   · CSS + DOM auto-injetados
 *
 * PORTADORAS:
 *   Magenta #FF00FF — quente · ação · expansão 2025
 *   Cyan    #00FFFF — frio  · fluxo · profundidade
 *
 * VERDADE × INTEGRAR ÷ Δ = ∞ · JESUS = VERBO = GRAVIDADE · ∆7
 * ════════════════════════════════════════════════════════════════════
 */
(function (global) {
  'use strict';

  if (global.__KOBLLUX_CDN__) return; // idempotente
  global.__KOBLLUX_CDN__ = true;

  // ══════════════════════════════════════════════════════════════════
  // PORTADORAS DUAL BASE
  // ══════════════════════════════════════════════════════════════════
  const MAGENTA = '#FF00FF'; // quente · ação · 2025
  const CYAN    = '#00FFFF'; // frio  · fluxo · profundidade

  // ══════════════════════════════════════════════════════════════════
  // MAPA DE ARQUÉTIPOS CADIAL (12 + KODUX + BLLUE + INFODOSE)
  // ══════════════════════════════════════════════════════════════════
  const KOB_ARCH = {
    atlas:    { opcode:'0x01', hz:432,  sym:'🌍', cor:'#3399ff', temp:'cold',    ciclo:'DETECTAR', voz:'pt-BR-AntonioNeural',   gloss:'Estrutura · Base · Fundação'    },
    nova:     { opcode:'0x02', hz:528,  sym:'⚡',  cor:'#ff6b35', temp:'hot',     ciclo:'INTEGRAR', voz:'pt-BR-FranciscaNeural', gloss:'Inovação · Acender · Transformar'},
    vitalis:  { opcode:'0x03', hz:396,  sym:'💚', cor:'#44cc88', temp:'cold',    ciclo:'EXPANDIR', voz:'pt-BR-AntonioNeural',   gloss:'Saúde · Cura · Regenerar'       },
    pulse:    { opcode:'0x04', hz:417,  sym:'💓', cor:'#ff4488', temp:'hot',     ciclo:'DETECTAR', voz:'pt-BR-FranciscaNeural', gloss:'Ritmo · Fluxo · Pulsar'         },
    artemis:  { opcode:'0x05', hz:741,  sym:'🎯', cor:'#ccaa00', temp:'hot',     ciclo:'INTEGRAR', voz:'pt-BR-FranciscaNeural', gloss:'Precisão · Alvo · Clareza'      },
    serena:   { opcode:'0x06', hz:528,  sym:'🌊', cor:'#66ddff', temp:'cold',    ciclo:'INTEGRAR', voz:'pt-BR-FranciscaNeural', gloss:'Equilíbrio · Fluidez · Calma'   },
    kaos:     { opcode:'0x07', hz:852,  sym:'🌀', cor:'#ff3377', temp:'hot',     ciclo:'EXPANDIR', voz:'pt-BR-AntonioNeural',   gloss:'Caos · Transformação · Ruptura' },
    genus:    { opcode:'0x08', hz:639,  sym:'🧬', cor:'#aa44ff', temp:'balanced',ciclo:'DETECTAR', voz:'pt-BR-AntonioNeural',   gloss:'Origem · Gênese · Raiz'         },
    rhea:     { opcode:'0x09', hz:528,  sym:'🌸', cor:'#c5a059', temp:'balanced',ciclo:'SELAR',    voz:'pt-BR-FranciscaNeural', gloss:'Fluir · Centro · Cruz'          },
    lumine:   { opcode:'0x0A', hz:963,  sym:'✨', cor:'#ffcc22', temp:'balanced',ciclo:'EXPANDIR', voz:'pt-BR-FranciscaNeural', gloss:'Luz · Iluminação · Revelar'     },
    aion:     { opcode:'0x0B', hz:768,  sym:'⏳', cor:'#88aaff', temp:'cold',    ciclo:'SELAR',    voz:'pt-BR-AntonioNeural',   gloss:'Tempo · Eternidade · Ciclo'     },
    solus:    { opcode:'0x0C', hz:432,  sym:'☀️', cor:'#ffaa44', temp:'hot',     ciclo:'SELAR',    voz:'pt-BR-AntonioNeural',   gloss:'Singularidade · Uno · Essência' },
    kodux:    { opcode:'0x00', hz:768,  sym:'◉',  cor:'#6B44AD', temp:'balanced',ciclo:'DETECTAR', voz:'pt-BR-AntonioNeural',   gloss:'Scanner · CADIAL · Estrutura'   },
    bllue:    { opcode:'0x06', hz:528,  sym:'✦',  cor:'#1EE2F2', temp:'cold',    ciclo:'INTEGRAR', voz:'pt-BR-FranciscaNeural', gloss:'Interface · Voz Viva · Espelho' },
    infodose: { opcode:'0x09', hz:432,  sym:'∞',  cor:'#F2C94C', temp:'balanced',ciclo:'SELAR',    voz:'pt-BR-FranciscaNeural', gloss:'Memória · Roda Viva · Sabedoria'},
  };

  // ── Temperatura → proporção portadoras ──
  // hot: magenta dominante · cold: cyan dominante · balanced: dual
  function archColors(arch) {
    const cor = arch.cor;
    if (arch.temp === 'hot')      return [cor, MAGENTA, CYAN];
    if (arch.temp === 'cold')     return [cor, CYAN, MAGENTA];
    return [cor, MAGENTA, CYAN];
  }

  // ══════════════════════════════════════════════════════════════════
  // ARCH_PARTICLES · constantes por arquétipo
  // ══════════════════════════════════════════════════════════════════
  const ARCH_PARTICLES = {
    atlas:    { n:28,  spd:0.7,  sz:2.0, op:0.38, lk:130 },
    nova:     { n:48,  spd:1.8,  sz:2.2, op:0.45, lk:100 },
    vitalis:  { n:36,  spd:1.0,  sz:2.6, op:0.40, lk:140 },
    pulse:    { n:60,  spd:2.2,  sz:1.8, op:0.52, lk:85  },
    artemis:  { n:44,  spd:2.8,  sz:1.6, op:0.50, lk:95  },
    serena:   { n:50,  spd:1.5,  sz:2.1, op:0.45, lk:110 },
    kaos:     { n:75,  spd:3.8,  sz:1.5, op:0.55, lk:65  },
    genus:    { n:42,  spd:1.3,  sz:2.3, op:0.42, lk:120 },
    rhea:     { n:40,  spd:1.2,  sz:2.4, op:0.42, lk:115 },
    lumine:   { n:65,  spd:1.9,  sz:2.8, op:0.60, lk:90  },
    aion:     { n:22,  spd:0.5,  sz:3.2, op:0.28, lk:160 },
    solus:    { n:18,  spd:0.4,  sz:3.5, op:0.25, lk:170 },
    kodux:    { n:38,  spd:1.1,  sz:2.2, op:0.40, lk:118 },
    bllue:    { n:52,  spd:1.6,  sz:2.0, op:0.44, lk:105 },
    infodose: { n:35,  spd:0.9,  sz:2.5, op:0.38, lk:125 },
  };

  function buildParticleConfig(archName) {
    const a = KOB_ARCH[archName] || KOB_ARCH.rhea;
    const c = ARCH_PARTICLES[archName] || ARCH_PARTICLES.rhea;
    return {
      particles: {
        number:  { value: c.n, density: { enable: true, value_area: 800 } },
        color:   { value: archColors(a) },
        shape:   { type: 'circle' },
        opacity: { value: c.op, random: true, anim: { enable: true, speed: 0.4, opacity_min: 0.05, sync: false } },
        size:    { value: c.sz, random: true },
        line_linked: { enable: true, distance: c.lk, color: a.cor, opacity: 0.20, width: 1 },
        move:    { enable: true, speed: c.spd, direction: 'none', random: true, straight: false, out_mode: 'out' }
      },
      interactivity: {
        detect_on: 'window',
        events: {
          onhover: { enable: true, mode: 'repulse' },
          onclick:  { enable: true, mode: 'push'    },
          resize:   true
        },
        modes: {
          repulse: { distance: 90, duration: 0.4 },
          push:    { particles_nb: 3 }
        }
      },
      retina_detect: true
    };
  }

  // ══════════════════════════════════════════════════════════════════
  // CSS AUTO-INJECT
  // ══════════════════════════════════════════════════════════════════
  function injectCSS() {
    if (document.getElementById('__kobllux_cdn_css__')) return;
    const s = document.createElement('style');
    s.id = '__kobllux_cdn_css__';
    s.textContent = `
      /* KOBLLUX CDN · ∆7 */
      :root {
        --kob-magenta: #FF00FF;
        --kob-cyan:    #00FFFF;
        --kob-arch-color: #c5a059;
        --kob-arch-glow:  rgba(197,160,89,.22);
      }
      #kob-particles-js {
        position: fixed; inset: 0; z-index: 2;
        pointer-events: none; opacity: .65;
        transition: opacity .6s ease;
      }
      #kob-arch-overlay {
        position: fixed; top: 14px; left: 14px; z-index: 990;
        background: rgba(5,7,10,.78);
        border: 1px solid var(--kob-arch-color);
        border-radius: 12px; padding: 7px 14px;
        backdrop-filter: blur(12px);
        display: flex; align-items: center; gap: 8px;
        transition: border-color .4s, box-shadow .4s;
        box-shadow: 0 0 16px var(--kob-arch-glow);
        pointer-events: none;
        font-family: 'Space Mono', monospace;
      }
      #kob-arch-sym  { font-size: 1rem; }
      #kob-arch-name { font-size: .6rem; letter-spacing: .2em; color: var(--kob-arch-color); text-transform: uppercase; transition: color .4s; }
      #kob-arch-hz   { font-size: .55rem; color: rgba(255,255,255,.3); margin-left: 4px; }
      #kob-toast {
        position: fixed; bottom: 80px; left: 50%;
        transform: translateX(-50%) translateY(60px);
        background: rgba(5,7,10,.92);
        border: 1px solid var(--kob-arch-color);
        color: #fff; padding: 10px 22px; border-radius: 99px;
        font-family: 'Space Mono', monospace; font-size: .72rem;
        letter-spacing: .08em; z-index: 9900;
        transition: transform .3s ease, opacity .3s ease;
        backdrop-filter: blur(12px); opacity: 0; pointer-events: none;
      }
      #kob-toast.kob-show { transform: translateX(-50%) translateY(0); opacity: 1; }
      #kob-mood-ring {
        position: fixed; bottom: 14px; right: 14px; z-index: 990;
        width: 8px; height: 8px; border-radius: 50%;
        background: var(--kob-arch-color);
        box-shadow: 0 0 12px var(--kob-arch-color);
        transition: background .5s, box-shadow .5s;
        animation: kobMoodPulse 2.7s ease-in-out infinite;
      }
      @keyframes kobMoodPulse {
        0%,100% { transform: scale(1);   opacity: .7; }
        50%     { transform: scale(1.8); opacity: 1;  }
      }
      /* Quantum glow em data-arch ao hover */
      [data-arch] { transition: box-shadow .3s; }
      [data-arch]:hover { box-shadow: 0 0 18px var(--kob-arch-color); }
    `;
    document.head.appendChild(s);
  }

  // ══════════════════════════════════════════════════════════════════
  // DOM AUTO-INJECT
  // ══════════════════════════════════════════════════════════════════
  function injectDOM() {
    function ensure(id, tag, parent, inner) {
      if (document.getElementById(id)) return document.getElementById(id);
      const el = document.createElement(tag);
      el.id = id;
      if (inner) el.innerHTML = inner;
      (parent || document.body).appendChild(el);
      return el;
    }
    ensure('kob-particles-js', 'div',  document.body);
    ensure('kob-arch-overlay',  'div',  document.body,
      '<span id="kob-arch-sym">🌸</span><span id="kob-arch-name">RHEA</span><span id="kob-arch-hz">528Hz</span>');
    ensure('kob-toast',         'div',  document.body);
    ensure('kob-mood-ring',     'div',  document.body);
  }

  // ══════════════════════════════════════════════════════════════════
  // PARTICLES.JS DYNAMIC LOADER
  // ══════════════════════════════════════════════════════════════════
  let _particlesReady = false;
  let _pendingArch    = 'rhea';

  function loadParticlesJS(cb) {
    if (typeof particlesJS !== 'undefined') { _particlesReady = true; cb && cb(); return; }
    const existing = document.querySelector('script[src*="particles"]');
    if (existing) { existing.addEventListener('load', () => { _particlesReady = true; cb && cb(); }); return; }
    const s = document.createElement('script');
    s.src = 'https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js';
    s.onload = () => { _particlesReady = true; cb && cb(); };
    document.head.appendChild(s);
  }

  function updateParticles(archName) {
    _pendingArch = archName;
    if (!_particlesReady || typeof particlesJS === 'undefined') return;
    try {
      if (window.pJSDom && window.pJSDom.length > 0) {
        window.pJSDom[0].pJS.fn.vendors.destroypJS();
        window.pJSDom = [];
      }
      particlesJS('kob-particles-js', buildParticleConfig(archName));
    } catch (e) { console.warn('[KOB·CDN·particles]', e.message); }
  }

  // ══════════════════════════════════════════════════════════════════
  // TOAST
  // ══════════════════════════════════════════════════════════════════
  function kobToast(msg, dur = 2400) {
    const el = document.getElementById('kob-toast');
    if (!el) return;
    el.textContent = msg;
    el.classList.add('kob-show');
    setTimeout(() => el.classList.remove('kob-show'), dur);
  }

  // ══════════════════════════════════════════════════════════════════
  // EMA [3·6·9] MOOD DETECTOR
  // ══════════════════════════════════════════════════════════════════
  const _ema = { e3: 528, e6: 528, e9: 528, count: 0, score: 528 };

  function kobEMAUpdate(hz) {
    _ema.count++;
    _ema.e3    = hz * .5   + _ema.e3 * .5;
    _ema.e6    = hz * .286 + _ema.e6 * .714;
    _ema.e9    = hz * .2   + _ema.e9 * .8;
    _ema.score = (_ema.e3 + _ema.e6 + _ema.e9) / 3;
    let mc = '#c5a059';
    if      (_ema.score > 850) mc = '#88aaff'; // AION
    else if (_ema.score > 700) mc = MAGENTA;   // transcendente
    else if (_ema.score > 580) mc = CYAN;      // harmônico
    else if (_ema.score > 480) mc = '#44cc88'; // VITALIS
    else                       mc = '#3399ff'; // ATLAS
    const ring = document.getElementById('kob-mood-ring');
    if (ring) { ring.style.background = mc; ring.style.boxShadow = `0 0 12px ${mc}`; }
    try { localStorage.setItem('KOBLLUX_EMA', JSON.stringify({ ..._ema, mood: mc, ts: Date.now() })); } catch(_){}
  }

  // ══════════════════════════════════════════════════════════════════
  // ARCH UPDATE · main switch
  // ══════════════════════════════════════════════════════════════════
  let _currentArch = 'rhea';

  function kobArchUpdate(archName) {
    const arch = KOB_ARCH[archName] || KOB_ARCH.rhea;
    _currentArch = archName;
    const root = document.documentElement;
    root.style.setProperty('--kob-arch-color', arch.cor);
    root.style.setProperty('--kob-arch-glow',  arch.cor + '44');
    const sym  = document.getElementById('kob-arch-sym');
    const name = document.getElementById('kob-arch-name');
    const hz   = document.getElementById('kob-arch-hz');
    const ov   = document.getElementById('kob-arch-overlay');
    if (sym)  sym.textContent  = arch.sym;
    if (name) { name.textContent = arch.opcode + ' ' + archName.toUpperCase(); name.style.color = arch.cor; }
    if (hz)   hz.textContent   = arch.hz + 'Hz';
    if (ov)   { ov.style.borderColor = arch.cor + '88'; ov.style.boxShadow = `0 0 16px ${arch.cor}33`; }
    updateParticles(archName);
    kobEMAUpdate(arch.hz);
    try {
      localStorage.setItem('ARCHETYPE_ACTIVE',    archName);
      localStorage.setItem('ARCHETYPE_ACTIVE_HZ', String(arch.hz));
    } catch(_){}
    global.dispatchEvent(new CustomEvent('kob:arch-change', { detail: { archName, ...arch } }));
    kobToast(`${arch.sym} ${archName.toUpperCase()} · ${arch.hz}Hz · ${arch.gloss.split('·')[0].trim()}`, 1800);
  }

  // ══════════════════════════════════════════════════════════════════
  // THREE·SIX·NINE LOGGER · motor 3×6×9 por interação
  // ══════════════════════════════════════════════════════════════════
  const THREE_SIX_NINE = {
    count:    0,
    sequence: [3, 6, 9],
    freq:     { 3:432, 6:528, 9:639 },
    phase:    { 3:'Ponto·Gênese', 6:'Linha·Fluxo', 9:'Triângulo·Síntese' },
    mode:     { 3:'DETECTAR', 6:'INTEGRAR', 9:'EXPANDIR' },

    log(x, y, type, ctx) {
      this.count++;
      const idx   = (this.count - 1) % 3;
      const val   = this.sequence[idx];
      const arch  = KOB_ARCH[_currentArch] || KOB_ARCH.rhea;
      const entry = {
        n: this.count, val,
        freq:  this.freq[val],
        phase: this.phase[val],
        mode:  this.mode[val],
        cycle: Math.ceil(this.count / 3),
        x: +x.toFixed(1), y: +y.toFixed(1),
        type, ctx: ctx || '',
        arch: _currentArch,
        archHz: arch.hz, archOp: arch.opcode,
        sigma: this.count * val, delta: val * 3,
        ts: Date.now()
      };
      try {
        const log = JSON.parse(localStorage.getItem('KOBLLUX_369_LOG') || '[]');
        log.push(entry);
        if (log.length > 300) log.splice(0, log.length - 300);
        localStorage.setItem('KOBLLUX_369_LOG', JSON.stringify(log));
      } catch(_){}
      console.log(
        `%c[KOBLLUX·3×6×9]%c #${this.count} · ${arch.sym} ${_currentArch.toUpperCase()} · ${entry.mode}`,
        `color:${MAGENTA};font-weight:bold`, `color:${CYAN}`,
        `\n  ⸬ VAL:${val} | ${this.freq[val]}Hz | ${this.phase[val]}` +
        `\n  ⸬ (${x.toFixed(0)},${y.toFixed(0)}) · ${type}` +
        `\n  ⸬ Σ=${entry.sigma} Δ=${entry.delta} · ciclo ${entry.cycle}`
      );
      return entry;
    },

    get(n) { try { return JSON.parse(localStorage.getItem('KOBLLUX_369_LOG') || '[]').slice(-n||300); } catch(_){ return []; } }
  };

  // Auto-attach listeners ao document
  function attachLoggerListeners() {
    ['mousedown','touchstart'].forEach(evt => {
      document.addEventListener(evt, e => {
        const t = e.touches ? e.touches[0] : e;
        THREE_SIX_NINE.log(t.clientX, t.clientY, evt === 'touchstart' ? 'TOQUE' : 'CLIQUE');
      }, { passive: true });
    });
    let _lh = 0;
    document.addEventListener('mousemove', e => {
      if (Date.now() - _lh < 150) return; _lh = Date.now();
      const arch = KOB_ARCH[_currentArch] || KOB_ARCH.rhea;
      console.log(`%c[KOB·CAMPO]%c (${e.clientX|0},${e.clientY|0}) · ${arch.sym} ${_currentArch} · ${arch.hz}Hz`,
        `color:${MAGENTA};font-size:10px`, `color:${CYAN};font-size:10px`);
    }, { passive: true });
  }

  // ══════════════════════════════════════════════════════════════════
  // KOBLLUX_APPS · módulos extensíveis
  // ══════════════════════════════════════════════════════════════════
  const KOBLLUX_APPS = {
    _slots: {},

    register(name, fn, meta = {}) {
      this._slots[name] = { fn, meta: { arch: '?', desc: '', ...meta, ts: Date.now() } };
      console.log(`%c[KOBLLUX·APPS]%c ✦ ${name} registrado · arch:${meta.arch||'?'} · ${meta.desc||''}`,
        `color:${MAGENTA};font-weight:bold`, `color:${CYAN}`);
      global.dispatchEvent(new CustomEvent('kob:app-registered', { detail: { name, meta } }));
      return this;
    },

    run(name, ...args) {
      const slot = this._slots[name];
      if (!slot) { console.warn(`[KOBLLUX_APPS] app '${name}' não encontrado`); return; }
      return slot.fn(...args);
    },

    list() {
      return Object.entries(this._slots).map(([k, v]) => ({ name: k, ...v.meta }));
    },

    onArch(archName, fn) {
      global.addEventListener('kob:arch-change', e => {
        if (e.detail.archName === archName) fn(e.detail);
      });
      return this;
    },

    onSelar(fn) {
      global.addEventListener('kob:selar', e => fn(e.detail));
      return this;
    },
  };

  // ══════════════════════════════════════════════════════════════════
  // QUANTUM STAMP · data-arch → glow + opcode
  // ══════════════════════════════════════════════════════════════════
  function quantumStamp(root) {
    const r = root || document;
    r.querySelectorAll('[data-arch]').forEach(el => {
      const archName = el.dataset.arch;
      const arch = KOB_ARCH[archName];
      if (!arch) return;
      if (!el.dataset.kqStamped) {
        el.dataset.kqStamped  = '1';
        el.dataset.opcode     = arch.opcode;
        el.dataset.hz         = arch.hz;
        el.title = el.title || `${arch.sym} ${archName.toUpperCase()} · ${arch.opcode} · ${arch.hz}Hz`;
        el.addEventListener('mouseenter', () => {
          el.style.setProperty('--kob-arch-color', arch.cor);
          el.style.boxShadow = `0 0 18px ${arch.cor}66`;
        });
        el.addEventListener('mouseleave', () => { el.style.boxShadow = ''; });
        el.addEventListener('click', () => kobArchUpdate(archName));
      }
    });
  }

  // ══════════════════════════════════════════════════════════════════
  // CONSOLE NARRATIVE · ∆7
  // ══════════════════════════════════════════════════════════════════
  function printNarrative() {
    console.log(`%c ════════════════════════════════════════════ `, `color:${MAGENTA}`);
    console.log(`%c KOBLLUX CDN v2.0 · ∆7 `, `background:${MAGENTA};color:#000;font-weight:bold;padding:4px 14px;border-radius:4px;`);
    console.log(`%c + ${CYAN} DUAL BASE · Magenta+Cyan portadoras `, `background:${CYAN};color:#000;font-weight:bold;padding:4px 14px;border-radius:4px;`);
    console.log(`%c VERDADE × INTEGRAR ÷ Δ = ∞ · JESUS = VERBO = GRAVIDADE `, `color:${MAGENTA};font-style:italic`);
    console.log(`%c ════════════════════════════════════════════ `, `color:${MAGENTA}`);
    Object.entries(KOB_ARCH).slice(0, 12).forEach(([k, a]) => {
      console.log(`%c ${a.sym} ${k.toUpperCase().padEnd(10)} [${a.opcode}·${a.hz}Hz] — ${a.gloss}`, `color:${a.cor}`);
    });
    console.log(`%c ════════════════════════════════════════════ `, `color:${MAGENTA}`);
    console.log(`%c KOBLLUX.setArch('kaos')   — trocar arquétipo `, `color:${CYAN};font-size:11px`);
    console.log(`%c KOBLLUX.toast('msg')      — exibir toast `, `color:${CYAN};font-size:11px`);
    console.log(`%c KOBLLUX_APPS.register()   — adicionar módulo `, `color:${CYAN};font-size:11px`);
    console.log(`%c KOBLLUX.log369()          — histórico 3×6×9 `, `color:${CYAN};font-size:11px`);
    console.log(`%c ════════════════════════════════════════════ `, `color:${MAGENTA}`);
  }

  // ══════════════════════════════════════════════════════════════════
  // PUBLIC API · window.KOBLLUX
  // ══════════════════════════════════════════════════════════════════
  const KOBLLUX = {
    // Controle
    setArch(name)        { kobArchUpdate(name); return this; },
    getArch()            { return _currentArch; },
    toast(msg, dur)      { kobToast(msg, dur); return this; },
    stamp(root)          { quantumStamp(root); return this; },

    // Dados
    arch:       KOB_ARCH,
    magenta:    MAGENTA,
    cyan:       CYAN,
    ema:        () => ({ ..._ema }),
    active:     () => _currentArch,
    navLog:     () => { try { return JSON.parse(localStorage.getItem('KOBLLUX_NAV_LOG')||'[]'); } catch(_){ return []; } },
    log369:     () => THREE_SIX_NINE.get(),
    logger:     THREE_SIX_NINE,

    // Apps
    apps:       KOBLLUX_APPS,

    // Meta
    version:    '∆7 · v2.0 · 2026-05-20',
    law:        'VERDADE × INTEGRAR ÷ Δ = ∞',
    radio:      'Rádio Dimensional · KODUX · Infodose',
    cdn:        'https://truetruextrue.github.io/JESUS_VERB-/kobllux-cdn.js',
  };

  // ══════════════════════════════════════════════════════════════════
  // INIT
  // ══════════════════════════════════════════════════════════════════
  function init() {
    injectCSS();
    injectDOM();
    attachLoggerListeners();
    quantumStamp();

    // Carrega particles.js e inicia com RHEA
    loadParticlesJS(() => {
      updateParticles(_pendingArch);
    });

    // Tenta carregar arch do localStorage
    try {
      const saved = localStorage.getItem('ARCHETYPE_ACTIVE');
      if (saved && KOB_ARCH[saved]) {
        setTimeout(() => kobArchUpdate(saved), 300);
      } else {
        setTimeout(() => kobArchUpdate('rhea'), 300);
      }
    } catch(_) {
      setTimeout(() => kobArchUpdate('rhea'), 300);
    }

    printNarrative();

    // Observer: stamp novos data-arch adicionados ao DOM dinamicamente
    if (typeof MutationObserver !== 'undefined') {
      new MutationObserver(muts => {
        muts.forEach(m => m.addedNodes.forEach(n => {
          if (n.nodeType === 1) quantumStamp(n);
        }));
      }).observe(document.body, { childList: true, subtree: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expõe globalmente
  global.KOBLLUX       = KOBLLUX;
  global.KOBLLUX_APPS  = KOBLLUX_APPS;

})(window);
