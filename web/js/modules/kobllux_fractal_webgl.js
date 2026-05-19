/**
 * kobllux_fractal_webgl.js · VITALIS · 0×08 · PULSAR · 639Hz
 * "A energia pulsante que mantém a vida em fluxo."
 *
 * CORRELAÇÃO DETECTADA:
 *   fractal Mandelbrot/Julia híbrido  ←→  UNO oscilando entre KODUX↔BLLUE
 *   EMA 3-6-9 (mood detector)        ←→  ciclo fractal 3·6·9·7 do KOBLLUX
 *   Schumann 7.83Hz (tags)            ←→  Hz frequencies (432/528/639/777)
 *   logMistico()                      ←→  kobllux_auto_session --capture
 *   DualStore.get()                   ←→  KBLX_LS localStorage map
 *   IndexedDB 'giro_logs'             ←→  _index/memory.jsonl (APPEND ONLY)
 *   FRAQ-HUD buttons                  ←→  #kblx-quick contextual panel
 *   collect_logs.sh                   ←→  kobllux_auto_session.py --from-memory
 *   u_rot / u_zoom state              ←→  kobllux_vocabulario parse_intent()
 *   tema bem/triste/equilíbrio        ←→  arquétipos PULSE/SOLUS/SERENA
 *
 * CAMADAS Z-INDEX (respeita o sistema existente):
 *   z-index: 2  → fractal-bg (este módulo)
 *   z-index: 3  → #particles-js
 *   z-index: 4  → #frame / conteúdo principal
 *
 * USO:
 *   <script src="./kobllux_fractal_webgl.js"></script>
 *   // ou com opções:
 *   window.addEventListener('load', () => {
 *     const fx = KoblluxFractal.mount({ logTarget: '#pulsos', theme: 'dark' });
 *     fx.toggle();  // liga/desliga
 *   });
 *
 * VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7
 */
(function(global) {
  'use strict';

  // ── SHADER: vertex mínimo ──────────────────────────────────────────────
  const VERT = `
    attribute vec2 a;
    void main(){ gl_Position = vec4(a, 0., 1.); }
  `;

  // ── SHADER: Mandelbrot/Julia híbrido + rotação + zoom + temas KOBLLUX ─
  const FRAG = `
    precision highp float;
    uniform vec2  u_res;
    uniform float u_time;
    uniform vec2  u_mouse;
    uniform int   u_theme;
    uniform float u_rot;    /* rotação (rad) */
    uniform float u_zoom;   /* zoom multiplicador */
    uniform int   u_wire;   /* wireframe/edge mode (Konami easter egg) */

    vec3 pal(float t, vec3 a, vec3 b, vec3 c, vec3 d){
      return a + b * cos(6.28318 * (c * t + d));
    }

    void main(){
      vec2 uv = (gl_FragCoord.xy - 0.5*u_res) / u_res.y;

      /* rotação 2D */
      float cs = cos(u_rot), sn = sin(u_rot);
      uv = mat2(cs,-sn, sn,cs) * uv;

      float t = u_time * 0.06;

      /* parâmetro Julia oscilante + mouse */
      vec2 cJ = vec2(
        mix(-0.8, 0.8, u_mouse.x) + 0.15*sin(t*0.7),
        mix(-0.8, 0.8, u_mouse.y) + 0.15*cos(t*0.9)
      );

      /* zoom fractal com multiplicador externo */
      float zoom = (1.4 + 0.25*sin(t*0.8) + 0.1*cos(t*1.3)) * u_zoom;
      vec2  z0   = uv / zoom + vec2(-0.45, 0.0);
      vec2  z    = z0;
      vec2  c    = mix(z0, cJ, 0.55 + 0.35*sin(t*0.5));

      float m2 = 0.0, i;
      const float ITERS = 220.0;
      for(i=0.0; i<ITERS; i++){
        z  = vec2(z.x*z.x - z.y*z.y, 2.0*z.x*z.y) + c;
        m2 = dot(z,z);
        if(m2>256.0) break;
      }

      float n;
      if(i < ITERS){
        m2 = max(m2, 1e-8);
        n  = (i - log2(log2(m2))*0.5 + 1.0) / ITERS;
      } else { n = 0.0; }

      vec3 col;
      /* temas KOBLLUX: 0=dark 1=light 2=medium 3=vibe */
      if(u_theme==1)
        col = pal(n, vec3(0.85), vec3(0.25), vec3(1.0,0.8,0.6), vec3(0.00,0.10,0.20));
      else if(u_theme==2)
        col = pal(n, vec3(0.10,0.13,0.15), vec3(0.35,0.30,0.25), vec3(1.0,0.8,0.5), vec3(0.0,0.15,0.20));
      else if(u_theme==3)
        col = pal(n, vec3(0.06,0.02,0.10), vec3(0.80,0.55,0.90), vec3(1.0,0.5,0.25), vec3(0.0,0.15,0.25));
      else
        col = pal(n, vec3(0.03,0.05,0.07), vec3(0.65,0.55,0.75), vec3(1.0,0.6,0.22), vec3(0.0,0.1,0.2));

      /* wireframe easter egg (Konami) */
      if(u_wire==1){
        float k = smoothstep(0.0, 0.08, n) * (1.0 - smoothstep(0.9, 1.0, n));
        col = mix(vec3(0.02), vec3(0.95), k);
      }

      float edge = clamp(pow(n, 8.0)*1.4, 0.0, 1.0);
      col += vec3(0.04,0.06,0.08)*edge;
      gl_FragColor = vec4(col, 1.0);
    }
  `;

  // ── EMA 3-6-9 (mood detector) ─────────────────────────────────────────
  // Espelha o ciclo fractal 3·6·9·7 do KOBLLUX como média móvel exponencial
  function makeFractalEMA(periods) {
    const st = periods.map(() => ({ v: 0, ok: false }));
    let lastT = 0;
    return function step(x, now) {
      if (!lastT) lastT = now;
      const dt = Math.max(1e-3, (now - lastT) / 1000);
      lastT = now;
      return periods.reduce((acc, p, i) => {
        const alpha = 2 / (p / dt + 1);
        st[i].v = st[i].ok ? alpha * x + (1 - alpha) * st[i].v : x;
        st[i].ok = true;
        return acc + st[i].v;
      }, 0) / periods.length;
    };
  }

  // ── IndexedDB (APPEND ONLY — espelha memory.jsonl) ────────────────────
  const DB_NAME = 'fraquitais-db', DB_STORE = 'giro_logs';
  let _db = null;
  const _dbReady = new Promise((res, rej) => {
    const r = indexedDB.open(DB_NAME, 2);
    r.onupgradeneeded = () => {
      const d = r.result;
      if (!d.objectStoreNames.contains(DB_STORE))
        d.createObjectStore(DB_STORE, { keyPath: 'id', autoIncrement: true });
    };
    r.onsuccess  = () => { _db = r.result; res(); };
    r.onerror    = () => rej(r.error);
  });

  function dbPut(rec) {
    return _dbReady.then(() => new Promise((res, rej) => {
      const tx = _db.transaction(DB_STORE, 'readwrite');
      tx.objectStore(DB_STORE).put(rec);
      tx.oncomplete = res;
      tx.onerror = () => rej(tx.error);
    }));
  }

  function dbAll() {
    return _dbReady.then(() => new Promise((res, rej) => {
      const tx = _db.transaction(DB_STORE, 'readonly');
      const rq = tx.objectStore(DB_STORE).getAll();
      rq.onsuccess = () => res(rq.result || []);
      rq.onerror   = () => rej(rq.error);
    }));
  }

  // ── logMistico bridge ─────────────────────────────────────────────────
  // Se window.logMistico existir, usa. Senão, usa kobllux_auto_session via API.
  function logEvent(msg) {
    if (window.logMistico) {
      window.logMistico(msg);
    } else {
      console.log('[KOBLLUX∆7]', msg);
    }
    // Também captura na memória KOBLLUX (auto-session)
    if (window.KOBLLUX_BRIDGE?.motorToChat) {
      // noop — o capture é feito via dbPut → collect_logs.sh → memory.jsonl
    }
  }

  // ── KoblluxFractal.mount() ───────────────────────────────────────────
  function mount(opts) {
    opts = opts || {};
    const logTarget = opts.logTarget || null;
    const DPR = Math.max(1, Math.min(2.0, window.devicePixelRatio || 1));

    // Evita canvas duplicado
    let canvas = document.getElementById('fractal-bg');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'fractal-bg';
      document.body.prepend(canvas);
    }

    // CSS inline (APPEND ONLY — não toca CSS existente)
    if (!document.getElementById('kblx-fractal-css')) {
      const s = document.createElement('style');
      s.id = 'kblx-fractal-css';
      s.textContent = `
canvas#fractal-bg {
  position: fixed; inset: 0;
  z-index: 2;                   /* abaixo particles(3) e frame(4) */
  pointer-events: none;
  filter: saturate(110%);
  transition: opacity .6s ease;
}
@media (prefers-reduced-motion: reduce) {
  canvas#fractal-bg { filter: saturate(100%); }
}
/* temas KOBLLUX mood (EMA 3-6-9) */
:root.theme-bem        { --fraq-accent: #57ffd0; }
:root.theme-equilibrio { --fraq-accent: #7db2ff; }
:root.theme-triste     { --fraq-accent: #ff6ea8; }
/* toast */
#kblx-fractal-toast {
  position:fixed; left:50%; bottom:90px;
  transform:translateX(-50%);
  padding:8px 14px; border-radius:10px;
  background:rgba(0,0,0,.6); color:#fff; font-size:13px;
  z-index:100000; opacity:0; pointer-events:none;
  transition:opacity .25s;
}
#kblx-fractal-toast.show { opacity:1; }`;
      document.head.appendChild(s);
    }

    // Toast
    let toastEl = document.getElementById('kblx-fractal-toast');
    if (!toastEl) {
      toastEl = document.createElement('div');
      toastEl.id = 'kblx-fractal-toast';
      document.body.appendChild(toastEl);
    }
    let toastTimer;
    function toast(msg) {
      toastEl.textContent = msg;
      toastEl.classList.add('show');
      clearTimeout(toastTimer);
      toastTimer = setTimeout(() => toastEl.classList.remove('show'), 1400);
    }

    // WebGL
    const gl = canvas.getContext('webgl', {
      antialias: false,
      preserveDrawingBuffer: false,
      powerPreference: 'high-performance',
    });
    if (!gl) { logEvent('⚠️ WebGL indisponível'); return null; }

    function resize() {
      const w = Math.floor(innerWidth * DPR), h = Math.floor(innerHeight * DPR);
      if (canvas.width !== w || canvas.height !== h) {
        canvas.width = w; canvas.height = h;
      }
      canvas.style.width = '100%'; canvas.style.height = '100%';
      gl.viewport(0, 0, gl.drawingBufferWidth, gl.drawingBufferHeight);
    }

    function compile(type, src) {
      const s = gl.createShader(type);
      gl.shaderSource(s, src); gl.compileShader(s);
      if (!gl.getShaderParameter(s, gl.COMPILE_STATUS))
        console.warn(gl.getShaderInfoLog(s));
      return s;
    }

    const prg = gl.createProgram();
    gl.attachShader(prg, compile(gl.VERTEX_SHADER, VERT));
    gl.attachShader(prg, compile(gl.FRAGMENT_SHADER, FRAG));
    gl.linkProgram(prg);
    if (!gl.getProgramParameter(prg, gl.LINK_STATUS))
      console.warn(gl.getProgramInfoLog(prg));
    gl.useProgram(prg);

    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER,
      new Float32Array([-1,-1, 3,-1, -1,3]), gl.STATIC_DRAW);
    const aLoc = gl.getAttribLocation(prg, 'a');
    gl.enableVertexAttribArray(aLoc);
    gl.vertexAttribPointer(aLoc, 2, gl.FLOAT, false, 0, 0);

    const uRes   = gl.getUniformLocation(prg, 'u_res');
    const uTime  = gl.getUniformLocation(prg, 'u_time');
    const uMouse = gl.getUniformLocation(prg, 'u_mouse');
    const uTheme = gl.getUniformLocation(prg, 'u_theme');
    const uRot   = gl.getUniformLocation(prg, 'u_rot');
    const uZoom  = gl.getUniformLocation(prg, 'u_zoom');
    const uWire  = gl.getUniformLocation(prg, 'u_wire');

    // Estado (exposto globalmente para telemetria)
    window.state = window.state || {};
    const state = window.state;
    state.rot      = state.rot      || 0;
    state.zoom     = state.zoom     || 1;
    state.rotSpeed = state.rotSpeed || 0.15;

    const mouse = { x: 0.5, y: 0.5 };
    function onPointer(e) {
      const t = ('touches' in e) ? e.touches[0] : e;
      mouse.x = (t.clientX || 0) / innerWidth;
      mouse.y = 1 - ((t.clientY || 0) / innerHeight);
    }
    addEventListener('mousemove', onPointer, { passive: true });
    addEventListener('touchmove', onPointer, { passive: true });

    function themeIndex() {
      const b = document.body;
      if (b.classList.contains('light'))  return 1;
      if (b.classList.contains('medium')) return 2;
      if (b.classList.contains('vibe'))   return 3;
      // detecta via DualStore (KOBLLUX)
      try {
        const ds = window.DualStore?.get?.()?.ui?.theme || '';
        if (ds === 'light')  return 1;
        if (ds === 'medium') return 2;
        if (ds === 'vibe')   return 3;
      } catch (_) {}
      return 0;
    }

    // Giro/zoom via giroscópio
    function attachGyro() {
      addEventListener('deviceorientation', e => {
        const g = (e.gamma || 0) * 0.01;
        const b = (e.beta  || 0) * 0.001;
        state.rot  += g * 0.02;
        state.zoom  = Math.max(0.6, Math.min(1.6, 1.0 + b));
      }, true);
    }
    if (window.DeviceOrientationEvent &&
        typeof DeviceOrientationEvent.requestPermission === 'function') {
      window.enableGyro = async () => {
        try {
          const r = await DeviceOrientationEvent.requestPermission();
          if (r === 'granted') attachGyro();
        } catch (_) {}
      };
    } else { attachGyro(); }

    // Pinça zoom
    let pinchBase = 0;
    addEventListener('touchmove', ev => {
      if (ev.touches && ev.touches.length === 2) {
        const dx = ev.touches[0].clientX - ev.touches[1].clientX;
        const dy = ev.touches[0].clientY - ev.touches[1].clientY;
        const d  = Math.hypot(dx, dy);
        if (!pinchBase) pinchBase = d;
        else state.zoom = Math.max(0.5, Math.min(2.0, d / pinchBase));
      }
    }, { passive: true });
    addEventListener('touchend', () => { pinchBase = 0; });

    // Teclado (A/D giram, W/S zoom)
    addEventListener('keydown', e => {
      if (e.key === 'a' || e.key === 'A') state.rot  -= 0.08;
      if (e.key === 'd' || e.key === 'D') state.rot  += 0.08;
      if (e.key === 'w' || e.key === 'W') state.zoom  = Math.min(2.0, state.zoom + 0.05);
      if (e.key === 's' || e.key === 'S') state.zoom  = Math.max(0.5, state.zoom - 0.05);
    });

    // Easter egg Konami → wireframe
    let wire = 0;
    const SEQ = ['ArrowUp','ArrowUp','ArrowDown','ArrowDown',
                 'ArrowLeft','ArrowRight','ArrowLeft','ArrowRight','b','a'];
    let kIdx  = 0;
    addEventListener('keydown', e => {
      kIdx = (e.key === SEQ[kIdx]) ? kIdx + 1 : 0;
      if (kIdx === SEQ.length) {
        wire = 1 - wire;
        gl.uniform1i(uWire, wire);
        toast(wire ? '⚡ Edge mode ON' : '⚡ Edge mode OFF');
        kIdx = 0;
      }
    });

    // ✝ overlay por triplo toque
    (() => {
      let taps = 0, tm;
      const cross = document.createElement('div');
      cross.style.cssText = 'position:fixed;inset:0;pointer-events:none;display:none;z-index:9;';
      cross.innerHTML = '<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font-size:48px;opacity:.25">✝</div>';
      document.body.appendChild(cross);
      addEventListener('touchend', () => {
        clearTimeout(tm); taps++;
        if (taps >= 3) {
          cross.style.display = cross.style.display === 'none' ? 'block' : 'none';
          taps = 0;
        }
        tm = setTimeout(() => taps = 0, 450);
      }, { passive: true });
    })();

    // ── EMA 3-6-9 mood detector ──────────────────────────────────────────
    const emaStep = makeFractalEMA([3, 6, 9]);

    function applyMoodTheme(score) {
      const r = document.documentElement;
      if (score > 0.66) {
        r.classList.add('theme-bem');
        r.classList.remove('theme-equilibrio', 'theme-triste');
      } else if (score < 0.33) {
        r.classList.add('theme-triste');
        r.classList.remove('theme-equilibrio', 'theme-bem');
      } else {
        r.classList.add('theme-equilibrio');
        r.classList.remove('theme-bem', 'theme-triste');
      }
    }

    // ── Loop principal ───────────────────────────────────────────────────
    let t0 = performance.now(), raf = 0, running = true;
    let lastLog = 0;

    function draw() {
      const now = performance.now();
      const t   = (now - t0) / 1000;

      // Giro contínuo
      state.rot += state.rotSpeed * 0.016;

      gl.uniform2f(uRes,   gl.drawingBufferWidth, gl.drawingBufferHeight);
      gl.uniform1f(uTime,  running ? t : 0.0);
      gl.uniform2f(uMouse, mouse.x, mouse.y);
      gl.uniform1i(uTheme, themeIndex());
      gl.uniform1f(uRot,   state.rot);
      gl.uniform1f(uZoom,  state.zoom);
      gl.uniform1i(uWire,  wire);
      gl.drawArrays(gl.TRIANGLES, 0, 3);

      // Mood EMA 3-6-9 (throttle ~1Hz)
      if (t - lastLog > 1) {
        const motion = Math.min(1, Math.abs(state.rotSpeed) * 2 + Math.abs(state.zoom - 1));
        const moodScore = emaStep(motion, now);
        applyMoodTheme(moodScore);

        // Log no IndexedDB (APPEND ONLY)
        dbPut({
          ts:    new Date().toISOString(),
          type:  'mood',
          score: +moodScore.toFixed(3),
          rot:   +state.rot.toFixed(3),
          zoom:  +state.zoom.toFixed(3),
          mouse: { x: +mouse.x.toFixed(2), y: +mouse.y.toFixed(2) },
          theme: themeIndex(),
        }).catch(() => {});

        // logMistico (throttle ~2s)
        if (t - lastLog > 2) {
          logEvent(`∴ fractal · t=${t.toFixed(1)} rot=${state.rot.toFixed(2)} mood=${moodScore.toFixed(2)}`);
        }
        lastLog = t;
      }

      raf = requestAnimationFrame(draw);
    }

    // Pausa quando fora de foco (poupa bateria)
    document.addEventListener('visibilitychange', () => {
      running = !document.hidden;
      logEvent(running ? '▶️ fractal resumed' : '⏸ fractal paused');
      if (running) t0 = performance.now();
    });

    addEventListener('resize', resize);
    resize();
    draw();

    // Log inicial
    try {
      const ds = window.DualStore?.get?.();
      logEvent(`∴ fractal mount · theme=${ds?.ui?.theme || 'dark'} · DPR=${DPR} · rot=ENA`);
    } catch (_) {}

    // Export JSON
    function exportLogs() {
      dbAll().then(rows => {
        const blob = new Blob(
          [JSON.stringify({ app: 'kobllux_fractal', version: '∆7', logs: rows }, null, 2)],
          { type: 'application/json' });
        const a = document.createElement('a');
        const stamp = new Date().toISOString().replace(/[:.]/g, '-');
        a.href = URL.createObjectURL(blob);
        a.download = `kobllux_fractal_giro_${stamp}.json`;
        a.click();
        URL.revokeObjectURL(a.href);
        toast('⇩ Logs exportados');
      });
    }

    // API pública
    const api = {
      canvas,
      state,
      toggle() {
        if (raf) {
          cancelAnimationFrame(raf); raf = 0;
          canvas.style.opacity = '0';
          setTimeout(() => canvas.style.display = 'none', 600);
          running = false;
          logEvent('⛔ fractal off');
        } else {
          canvas.style.display = 'block';
          canvas.style.opacity = '1';
          running = true; t0 = performance.now(); draw();
          logEvent('✅ fractal on');
        }
      },
      exportLogs,
      destroy() {
        cancelAnimationFrame(raf); raf = 0;
        canvas.remove();
        logEvent('🗑️ fractal destroyed');
      },
    };

    // Expõe globalmente
    window.__fractalToggle    = api.toggle;
    window.__fractalExportLogs = api.exportLogs;
    window.KOBLLUX_FRACTAL    = api;

    return api;
  }

  // Namespace global
  global.KoblluxFractal = { mount, dbPut, dbAll };

})(window);
