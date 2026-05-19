/**
 * kobllux_quantum.js · KOBLLUX · 0×00 → 0×0C · ORIGEM→TRANSCENDER
 * "Acoplamento quântico fractal — cada elemento é uma face do todo."
 *
 * ARQUITETURA:
 *   Cada ID/classe do HTML recebe data-opcode + data-arch (DNA fractal).
 *   Módulos se comunicam exclusivamente via bus de sinais (CustomEvents).
 *   CSS é gerado dinamicamente por opcode ativo.
 *   Scripts carregam lazy conforme módulo é ativado.
 *   Zero sobreposição — cada opcode governa seu território.
 *
 * CAMADAS NUCLEARES (linguagem fractal):
 *   Python  (0×01) → DETECTAR: leitura, scan, input
 *   TS/JS   (0×02) → INTEGRAR: pontes, coupler, bridge
 *   C/C++   (0×03) → EXPANDIR: frames, motor, estrutura
 *   Rust    (0×04) → LAPIDAR:  voz, TTS, integridade
 *   GLSL    (0×05) → CONVERGIR: fractal visual, WebGL
 *   Bash    (0×06) → UNIFICAR: temas, config, harmonia
 *   JSON-LD (0×07) → SELAR:    patch, kblx-panel, selagem
 *
 * VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7
 */
(function(G) {
  'use strict';

  // ══════════════════════════════════════════════════════════════════════
  // 0. MAPA QUÂNTICO: IDs + classes → opcode + arquétipo + linguagem
  // ══════════════════════════════════════════════════════════════════════
  const QM = {
    // ── 0×00 ORIGEM ○ 768Hz — nascimento / splash ──────────────────────
    '0x00': {
      arch: 'kobllux', hz: 768, sym: '○', lang: null, action: 'ORIGEM',
      ids:     ['kdx-splash'],
      classes: ['kdx-splash', 'kdx-splash-inner', 'kdx-splash-logo', 'kdx-splash-title'],
    },

    // ── 0×01 DETECTAR ● 432Hz — Python — input/scan ────────────────────
    '0x01': {
      arch: 'kodux', hz: 432, sym: '●', lang: 'Python', action: 'DETECTAR',
      ids:     ['userInput', 'sendBtn', 'bootBlock', 'bootText', 'particles-js'],
      classes: ['content'],          // #particles-js container
    },

    // ── 0×02 INTEGRAR ― 528Hz — TypeScript — bridge/response ───────────
    '0x02': {
      arch: 'bllue', hz: 528, sym: '―', lang: 'TypeScript', action: 'INTEGRAR',
      ids:     ['response', 'responseList', 'copyBtn', 'pasteBtn'],
      classes: ['response-container', 'pages-wrapper', 'response-block',
                'response-controls', 'control-buttons'],
    },

    // ── 0×03 EXPANDIR ▢ 639Hz — C/C++ — motor/frame ────────────────────
    '0x03': {
      arch: 'atlas', hz: 639, sym: '▢', lang: 'C/C++', action: 'EXPANDIR',
      ids:     ['motorDock', 'motorFrame', 'toggleMotorBtn', 'motorDockClose'],
      classes: ['motor-dock', 'motor-dock-head'],
    },

    // ── 0×04 LAPIDAR ◇ 594Hz — Rust — voz/TTS/integridade ─────────────
    '0x04': {
      arch: 'pulse', hz: 594, sym: '◇', lang: 'Rust', action: 'LAPIDAR',
      ids:     ['btn-arch', 'voiceBtn', 'voiceConfigBtn', 'voiceConfigFile',
                'main-orb', 'kdx-orb'],
      classes: ['orb', 'orb-core', 'symbol-button', 'kdx-orb', 'kdx-orb-icon',
                'kdx-hidden'],
    },

    // ── 0×05 CONVERGIR ⧉ 672Hz — GLSL — fractal/visual ─────────────────
    '0x05': {
      arch: 'vitalis', hz: 639, sym: '⧉', lang: 'GLSL', action: 'CONVERGIR',
      ids:     ['logoContainer', 'assistantName', 'themeToggle'],
      classes: ['svg-container', 'logo-overlay'],
    },

    // ── 0×06 UNIFICAR ☯ 528Hz — Bash — tema/config/harmonia ────────────
    '0x06': {
      arch: 'serena', hz: 528, sym: '☯', lang: 'Bash', action: 'UNIFICAR',
      ids:     ['iaConfigPanel', 'iaConfigHeader', 'themeSelect', 'modelSelect',
                'customModelInput', 'saveIaConfigBtn', 'clearIaConfigBtn', 'iaStatus'],
      classes: ['ia-config-body', 'ia-field', 'ia-actions', 'ia-status', 'pill-btn'],
    },

    // ── 0×07 SELAR ✧⃝⚝ 777Hz — JSON-LD — patch/kblx/seal ───────────────
    '0x07': {
      arch: 'kaos', hz: 777, sym: '✧', lang: 'JSON-LD', action: 'SELAR',
      ids:     ['kblx-back', 'kblx-panel', 'kblx-ttl', 'kblx-inp',
                'kblx-btn-save', 'kblx-btn-close', 'parserBtn', 'parserFile'],
      classes: ['kblx-row', 'kblx-btn', 'kblx-save', 'kblx-close',
                'p-chip', 'p-title', 'p-lbl'],
    },

    // ── 0×08 PULSAR ◉ 432Hz — login/identidade/acolhimento ─────────────
    '0x08': {
      arch: 'serena', hz: 528, sym: '◉', lang: null, action: 'PULSAR',
      ids:     ['loginBox', 'loginForm', 'userName', 'assistantInput',
                'assistantName'],
      classes: ['login-container'],
    },

    // ── 0×09 FLUIR ∞ 528Hz — footer/persistência ────────────────────────
    '0x09': {
      arch: 'rhea', hz: 528, sym: '∞', lang: null, action: 'FLUIR',
      ids:     ['kobFooter', 'footerHint'],
      classes: ['kob-footer', 'kob-footer-inner', 'footer-text', 'footer-dot'],
    },

    // ── 0×0A ESTRUTURAR ⬡ 639Hz — input/envio ───────────────────────────
    '0x0A': {
      arch: 'nova', hz: 432, sym: '⬡', lang: null, action: 'ESTRUTURAR',
      ids:     ['sendBtn', 'userInput'],
      classes: ['input-container', 'send-label'],
    },

    // ── 0×0B TEMPORIZAR ⧗ 741Hz — API config / memória ──────────────────
    '0x0B': {
      arch: 'aion', hz: 741, sym: '⧗', lang: null, action: 'TEMPORIZAR',
      ids:     ['apiKeyInput', 'toggleLoginBtn', 'toggleSettingsBtn'],
      classes: [],
    },

    // ── 0×0C TRANSCENDER 𓇽 963Hz — fractal WebGL ────────────────────────
    '0x0C': {
      arch: 'lumine', hz: 963, sym: '𓇽', lang: 'GLSL', action: 'TRANSCENDER',
      ids:     [],
      classes: [],   // fractal-bg injetado pelo kobllux_fractal_webgl.js
    },
  };

  // ══════════════════════════════════════════════════════════════════════
  // 1. STAMPING: aplica data-opcode e data-arch em cada elemento
  // ══════════════════════════════════════════════════════════════════════
  function stamp() {
    Object.entries(QM).forEach(([opcode, cfg]) => {
      // Por ID
      cfg.ids.forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        el.dataset.opcode = opcode;
        el.dataset.arch   = cfg.arch;
        el.dataset.hz     = cfg.hz;
        el.dataset.action = cfg.action;
        el.classList.add(`kob-${opcode.replace('0x', '')}`);
      });
      // Por classe
      cfg.classes.forEach(cls => {
        document.querySelectorAll(`.${cls}`).forEach(el => {
          if (!el.dataset.opcode) {
            el.dataset.opcode = opcode;
            el.dataset.arch   = cfg.arch;
          }
        });
      });
    });
    console.log('[KQ∆7] Stamping completo · ', Object.keys(QM).length, 'opcodes');
  }

  // ══════════════════════════════════════════════════════════════════════
  // 2. CSS QUÂNTICO: gera variáveis por opcode + classe dinâmica ativa
  // ══════════════════════════════════════════════════════════════════════
  const OPCODE_COLORS = {
    '0x00': { h: 180, l: 60 },  // ciano
    '0x01': { h:  28, l: 60 },  // laranja (KODUX)
    '0x02': { h: 200, l: 65 },  // azul (BLLUE)
    '0x03': { h: 200, l: 60 },  // azul-estrutura (ATLAS)
    '0x04': { h: 145, l: 70 },  // verde-pulse
    '0x05': { h: 168, l: 68 },  // esmeralda (VITALIS)
    '0x06': { h: 210, l: 72 },  // azul suave (SERENA)
    '0x07': { h:  12, l: 62 },  // laranja-vermelho (KAOS)
    '0x08': { h: 210, l: 70 },  // azul (SERENA login)
    '0x09': { h: 184, l: 68 },  // ciano suave (RHEA)
    '0x0A': { h:   0, l: 62 },  // vermelho (NOVA)
    '0x0B': { h: 272, l: 68 },  // violeta (AION)
    '0x0C': { h:  54, l: 72 },  // ouro (LUMINE)
  };

  function injectQuantumCSS() {
    const rules = [];

    // Variáveis por opcode
    Object.entries(OPCODE_COLORS).forEach(([op, { h, l }]) => {
      const key = op.replace('0x', '');
      rules.push(`
        [data-opcode="${op}"] {
          --kq-opcode-h: ${h};
          --kq-opcode-l: ${l}%;
          --kq-color:  hsl(${h}, 70%, ${l}%);
          --kq-glow:   0 0 12px hsl(${h}, 70%, ${l}%, .4);
          --kq-bg:     hsl(${h}, 20%, 8%);
          --kq-border: 1px solid hsl(${h}, 40%, 25%);
          transition: --kq-color .6s ease, box-shadow .4s ease;
        }
        [data-opcode="${op}"].kq-active {
          box-shadow: var(--kq-glow);
          outline: 1px solid hsl(${h}, 50%, 35%);
        }
        .kob-${key} { --kq-mark: "${op}"; }
      `);
    });

    // Transição de entrada por opcode (stagger fractal 3·6·9·7)
    rules.push(`
      [data-opcode] {
        transition:
          opacity .4s ease,
          transform .4s ease,
          box-shadow .3s ease,
          border-color .5s ease;
      }
      [data-opcode].kq-loading { opacity: .4; pointer-events: none; }
      [data-opcode].kq-ready   { opacity: 1; }
      [data-opcode].kq-signal  {
        animation: kqPulse .35s ease;
      }
      @keyframes kqPulse {
        0%   { box-shadow: 0 0 0 0 var(--kq-color, #0cf); }
        50%  { box-shadow: 0 0 0 8px transparent; }
        100% { box-shadow: 0 0 0 0 transparent; }
      }
    `);

    // Inject
    const style = document.createElement('style');
    style.id = 'kobllux-quantum-css';
    style.textContent = rules.join('\n');
    document.head.appendChild(style);
    console.log('[KQ∆7] CSS quântico injetado ·', Object.keys(OPCODE_COLORS).length, 'opcodes');
  }

  // ══════════════════════════════════════════════════════════════════════
  // 3. BUS DE SINAIS QUÂNTICOS — acoplamento sem conhecimento mútuo
  // ══════════════════════════════════════════════════════════════════════
  const KQ_BUS_EVENT = 'kobllux:quantum';

  const KQ = {
    _handlers: {},

    // Emite sinal de um arquétipo para outro
    emit(from, to, payload = {}) {
      const target = Object.values(QM).find(m => m.arch === to);
      const opcode = target?.opcode || '0x00';
      const hz     = target?.hz     || 768;

      // Pulsa visualmente o elemento alvo
      target?.ids?.forEach(id => {
        const el = document.getElementById(id);
        if (el) {
          el.classList.add('kq-signal');
          setTimeout(() => el.classList.remove('kq-signal'), 400);
        }
      });

      window.dispatchEvent(new CustomEvent(KQ_BUS_EVENT, {
        detail: { from, to, opcode, hz, payload, ts: Date.now() }
      }));

      // APPEND ONLY: registra na memória (throttle 5s)
      _qlog(from, to, opcode, payload);
    },

    // Escuta sinais direcionados a um arquétipo
    on(arch, handler) {
      if (!this._handlers[arch]) this._handlers[arch] = [];
      this._handlers[arch].push(handler);
      window.addEventListener(KQ_BUS_EVENT, e => {
        if (e.detail.to === arch) handler(e.detail);
      });
    },

    // Broadcast para todos
    broadcast(from, payload = {}) {
      window.dispatchEvent(new CustomEvent(KQ_BUS_EVENT, {
        detail: { from, to: '*', opcode: '0x06', hz: 528, payload, ts: Date.now() }
      }));
    },
  };

  // Throttled log para memory.jsonl (APPEND ONLY)
  let _qlogTimer = null;
  const _qlogBuffer = [];
  function _qlog(from, to, opcode, payload) {
    _qlogBuffer.push({ ts: new Date().toISOString(), from, to, opcode, payload });
    if (!_qlogTimer) {
      _qlogTimer = setTimeout(() => {
        if (window.KoblluxFractal?.dbPut) {
          _qlogBuffer.forEach(r => KoblluxFractal.dbPut({ ...r, type: 'kq_signal' }));
        }
        _qlogBuffer.length = 0;
        _qlogTimer = null;
      }, 3000);
    }
  }

  // ══════════════════════════════════════════════════════════════════════
  // 4. LAZY MODULE LOADER — menor custo, carrega sob demanda
  // ══════════════════════════════════════════════════════════════════════
  const LAZY = {
    // Cada opcode pode ter módulos extras que só carregam quando necessário
    '0x04': null,  // PULSE TTS — carregado quando #btn-arch é clicado
    '0x05': null,  // GLSL fractal — já carregado pelo kobllux_fractal_webgl.js
    '0x07': null,  // SELAR patch — já pelo kobllux_dock_extract.js
    _loaded: new Set(),
  };

  function lazyLoad(opcode, url) {
    if (LAZY._loaded.has(opcode) || !url) return Promise.resolve();
    LAZY._loaded.add(opcode);
    return new Promise((res, rej) => {
      const s = document.createElement('script');
      s.src = url;
      s.onload  = () => { KQ.emit('loader', QM[opcode]?.arch || 'kobllux', { opcode, loaded: url }); res(); };
      s.onerror = rej;
      document.body.appendChild(s);
    });
  }

  // ══════════════════════════════════════════════════════════════════════
  // 5. MÓDULOS ATÔMICOS — cada opcode define seu comportamento
  // ══════════════════════════════════════════════════════════════════════

  // ── 0×01 KODUX · DETECTAR ─────────────────────────────────────────────
  function module_0x01_kodux() {
    const input = document.getElementById('userInput');
    const send  = document.getElementById('sendBtn');

    input?.addEventListener('input', e => {
      // Detecta arquétipo pela intenção do texto
      if (G.KOBLLUX_BRIDGE?.sync || G.koblluxVocab) {
        // Vocabu detecta em background (debounce 800ms)
        clearTimeout(input._kqTimer);
        input._kqTimer = setTimeout(() => {
          const detected = G.KOBLLUX_FRACTAL_ARCH
            ? G.KOBLLUX_FRACTAL_ARCH.applyArch('nova')
            : null;
          if (detected) KQ.emit('kodux', 'nova', { input: e.target.value.slice(0, 60) });
        }, 800);
      }
    }, { passive: true });

    // Enter = sinal para BLLUE (integrar)
    input?.addEventListener('keydown', e => {
      if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
        KQ.emit('kodux', 'bllue', { action: 'generate_fractal' });
      }
    });

    send?.addEventListener('click', () => KQ.emit('kodux', 'bllue', { action: 'send' }));
  }

  // ── 0×02 BLLUE · INTEGRAR ─────────────────────────────────────────────
  function module_0x02_bllue() {
    // Quando recebe sinal de KODUX, processa a resposta
    KQ.on('bllue', ({ from, payload }) => {
      const list = document.getElementById('responseList');
      if (payload?.action === 'motor_output' && list) {
        KQ.emit('bllue', 'vitalis', { trigger: 'motor_output', text: payload.text });
      }
    });

    // Observa responseList para detectar novos blocos
    const list = document.getElementById('responseList');
    if (list) {
      new MutationObserver(() => {
        KQ.emit('bllue', 'lumine', { action: 'new_block', count: list.children.length });
      }).observe(list, { childList: true });
    }
  }

  // ── 0×03 ATLAS · EXPANDIR (Motor 78K) ────────────────────────────────
  function module_0x03_atlas() {
    const motorBtn  = document.getElementById('toggleMotorBtn');
    const motorDock = document.getElementById('motorDock');
    const motorClose= document.getElementById('motorDockClose');
    const motorFrame= document.getElementById('motorFrame');

    motorBtn?.addEventListener('click', () => {
      const hidden = motorDock?.hasAttribute('hidden');
      if (motorDock) {
        if (hidden) {
          motorDock.removeAttribute('hidden');
          document.body.classList.add('motor-mode');
          KQ.emit('atlas', 'vitalis', { action: 'motor_open' });
        } else {
          motorDock.setAttribute('hidden', '');
          document.body.classList.remove('motor-mode');
          KQ.emit('atlas', 'aion', { action: 'motor_close' });
        }
      }
    });

    motorClose?.addEventListener('click', () => {
      motorDock?.setAttribute('hidden', '');
      document.body.classList.remove('motor-mode');
      KQ.emit('atlas', 'aion', { action: 'motor_close' });
    });

    // Escuta output do motor via localStorage
    KQ.on('atlas', ({ payload }) => {
      if (payload?.action === 'motor_output') {
        const stored = localStorage.getItem('kobllux_last_result') || '';
        if (stored) KQ.emit('atlas', 'bllue', { action: 'motor_output', text: stored });
      }
    });
  }

  // ── 0×04 PULSE · LAPIDAR (Voz/TTS/ORB) ──────────────────────────────
  function module_0x04_pulse() {
    const btnArch = document.getElementById('btn-arch');
    // Long press → #kblx-quick (via kobllux_dock_extract)
    btnArch?.addEventListener('pointerdown', () => {
      const t = setTimeout(() => {
        window.kblxOpenPanel?.(btnArch);
        KQ.emit('pulse', 'kaos', { action: 'long_press', target: 'btn-arch' });
      }, 600);
      btnArch.addEventListener('pointerup',   () => clearTimeout(t), { once: true });
      btnArch.addEventListener('pointermove', () => clearTimeout(t), { once: true });
    }, { passive: true });

    // Escuta mudança de arquétipo e emite para VITALIS (fractal)
    KQ.on('pulse', ({ payload }) => {
      if (payload?.arch && G.KOBLLUX_FRACTAL_ARCH) {
        G.KOBLLUX_FRACTAL_ARCH.applyArch(payload.arch);
        KQ.emit('pulse', 'vitalis', { action: 'arch_change', arch: payload.arch });
      }
    });
  }

  // ── 0×05 VITALIS · CONVERGIR (Fractal WebGL) ─────────────────────────
  function module_0x05_vitalis() {
    // Recebe sinais e propaga ao fractal
    KQ.on('vitalis', ({ from, payload }) => {
      if (!G.KOBLLUX_FRACTAL) return;
      if (payload?.action === 'motor_output' && payload.text) {
        // Texto do motor → semente Julia
        let h = 0;
        for (let i = 0; i < Math.min(payload.text.length, 64); i++) {
          h = ((h << 5) - h) + payload.text.charCodeAt(i); h |= 0;
        }
        const x = (Math.abs(h) % 1000) / 1000;
        const y = (Math.abs(h >> 8) % 1000) / 1000;
        if (G.state) { G.state.rot += (x - 0.5) * 0.5; G.state.zoom = 0.8 + y * 0.8; }
      }
      if (payload?.action === 'arch_change') {
        G.KOBLLUX_FRACTAL_ARCH?.applyArch(payload.arch);
      }
    });
  }

  // ── 0×06 SERENA · UNIFICAR (Tema/Config) ─────────────────────────────
  function module_0x06_serena() {
    const themeSelect = document.getElementById('themeSelect');
    themeSelect?.addEventListener('change', e => {
      document.body.className = e.target.value;
      localStorage.setItem('infodoseTheme', e.target.value);
      KQ.broadcast('serena', { action: 'theme_change', theme: e.target.value });
    });

    // Restaura tema salvo
    const saved = localStorage.getItem('infodoseTheme');
    if (saved) {
      document.body.classList.add(saved);
      if (themeSelect) themeSelect.value = saved;
    }

    // Config IA
    const saveBtn  = document.getElementById('saveIaConfigBtn');
    const clearBtn = document.getElementById('clearIaConfigBtn');
    const keyInp   = document.getElementById('apiKeyInput');
    const modelSel = document.getElementById('modelSelect');
    const status   = document.getElementById('iaStatus');

    // Restaura config
    if (keyInp)   keyInp.value   = localStorage.getItem('openrouter_api_key') || '';
    if (modelSel) modelSel.value = localStorage.getItem('openrouter_model')   || '';
    if (status && keyInp?.value) status.textContent = '✓ Chave carregada';

    saveBtn?.addEventListener('click', () => {
      if (keyInp?.value)   localStorage.setItem('openrouter_api_key',  keyInp.value.trim());
      if (modelSel?.value) localStorage.setItem('openrouter_model',    modelSel.value);
      if (status) status.textContent = '✓ Salvo · ∆7';
      KQ.emit('serena', 'aion', { action: 'config_saved' });
    });

    clearBtn?.addEventListener('click', () => {
      localStorage.removeItem('openrouter_api_key');
      localStorage.removeItem('openrouter_model');
      if (keyInp)   keyInp.value   = '';
      if (modelSel) modelSel.value = '';
      if (status)   status.textContent = 'Limpo.';
    });

    const settingsBtn = document.getElementById('toggleSettingsBtn');
    const configPanel = document.getElementById('iaConfigPanel');
    settingsBtn?.addEventListener('click', () => {
      const vis = configPanel?.style.display === 'block';
      if (configPanel) configPanel.style.display = vis ? '' : 'block';
    });
  }

  // ── 0×07 KAOS · SELAR (kblx-panel / patch) ───────────────────────────
  function module_0x07_kaos() {
    const back  = document.getElementById('kblx-back');
    const save  = document.getElementById('kblx-btn-save');
    const close = document.getElementById('kblx-btn-close');
    const inp   = document.getElementById('kblx-inp');

    back?.addEventListener('click',  e => { if (e.target === back) back.classList.remove('is-open'); });
    close?.addEventListener('click', () => back?.classList.remove('is-open'));

    save?.addEventListener('click', () => {
      const btn = G._kblxState?.currentBtn;
      if (!btn || !inp?.value.trim()) { back?.classList.remove('is-open'); return; }
      btn.dataset.url = inp.value.trim();
      // Persiste sessão
      const id = btn.id || `kblx-${Date.now()}`;
      if (!btn.id) btn.id = id;
      const sess = JSON.parse(localStorage.getItem('KDX_SESSIONS') || '{}');
      sess[id] = { url: inp.value.trim(), title: btn.title || inp.value, type: 'edit', ts: Date.now() };
      localStorage.setItem('KDX_SESSIONS', JSON.stringify(sess));
      KQ.emit('kaos', 'aion', { action: 'session_saved', id, url: inp.value.trim() });
      back?.classList.remove('is-open');
    });
  }

  // ── 0×08 SERENA · LOGIN ───────────────────────────────────────────────
  function module_0x08_login() {
    const loginBox  = document.getElementById('loginBox');
    const loginForm = document.getElementById('loginForm');
    const loginBtn  = document.getElementById('toggleLoginBtn');

    // Restaura nomes
    const savedUser  = localStorage.getItem('infodoseUserName')   || '';
    const savedAsst  = localStorage.getItem('infodoseAssistantName') || '';
    if (savedUser) {
      loginBox?.setAttribute('hidden', '');
      const asst = document.getElementById('assistantName');
      if (asst && savedAsst) asst.textContent = savedAsst;
    }

    loginForm?.addEventListener('submit', e => {
      e.preventDefault();
      const user = document.getElementById('userName')?.value?.trim();
      const asst = document.getElementById('assistantInput')?.value?.trim();
      if (user) {
        localStorage.setItem('infodoseUserName', user);
        localStorage.setItem('di_userName', user);
      }
      if (asst) {
        localStorage.setItem('infodoseAssistantName', asst);
        const nameEl = document.getElementById('assistantName');
        if (nameEl) nameEl.textContent = asst;
      }
      loginBox?.setAttribute('hidden', '');
      KQ.emit('serena', 'nova', { action: 'login', user, asst });
    });

    loginBtn?.addEventListener('click', () => {
      const h = loginBox?.hasAttribute('hidden');
      if (h) loginBox.removeAttribute('hidden');
      else   loginBox?.setAttribute('hidden', '');
    });
  }

  // ── 0×09 RHEA · FLUIR (footer/splashout) ─────────────────────────────
  function module_0x09_rhea() {
    // Splash → remove após 2.4s
    const splash = document.getElementById('kdx-splash');
    if (splash) {
      setTimeout(() => {
        splash.style.transition = 'opacity .6s ease';
        splash.style.opacity = '0';
        setTimeout(() => splash.setAttribute('hidden', ''), 650);
      }, 2400);
    }

    // Footer hint rotaciona com arquétipo ativo
    const hint = document.getElementById('footerHint');
    KQ.on('rhea', ({ payload }) => {
      if (hint && payload?.arch) {
        const anchors = {
          kodux: 'Eu sou o movimento que cria, destrói e recria a verdade.',
          atlas: 'A estrutura precede a ação. Planeje com precisão.',
          nova:  'Ideias são sementes! Vamos colorir fora das linhas.',
          kaos:  'Quebre as regras. O caos é a verdadeira ordem.',
          aion:  'O tempo é um algoritmo. Vamos reprogramá-lo. ∆7',
          lumine:'Ria! A luz está em você! METALUX ativado.',
          rhea:  'Somos fios da mesma teia cósmica.',
          serena:'Respire. Este espaço é seu.',
        };
        const msg = anchors[payload.arch] || 'VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7';
        hint.querySelector('.footer-text').textContent = msg;
      }
    });
  }

  // ── 0×0B AION · TEMPORIZAR (memória/config parser) ────────────────────
  function module_0x0B_aion() {
    const parserBtn  = document.getElementById('parserBtn');
    const parserFile = document.getElementById('parserFile');
    const vcBtn      = document.getElementById('voiceConfigBtn');
    const vcFile     = document.getElementById('voiceConfigFile');

    parserBtn?.addEventListener('click', () => parserFile?.click());
    vcBtn?.addEventListener('click',     () => vcFile?.click());

    parserFile?.addEventListener('change', () => {
      KQ.emit('aion', 'bllue', { action: 'parser_upload', file: parserFile.files[0]?.name });
    });

    vcFile?.addEventListener('change', () => {
      KQ.emit('aion', 'pulse', { action: 'voice_config_upload', file: vcFile.files[0]?.name });
    });

    // Escuta eventos e registra
    KQ.on('aion', ({ from, payload }) => {
      const ts = new Date().toISOString();
      const entry = { ts, from, ...payload };
      const log = JSON.parse(localStorage.getItem('KDX_AION_LOG') || '[]');
      log.push(entry);
      if (log.length > 100) log.splice(0, log.length - 100); // circular
      localStorage.setItem('KDX_AION_LOG', JSON.stringify(log));
    });
  }

  // ══════════════════════════════════════════════════════════════════════
  // 6. ARCHETYPE WATCHER — observa localStorage e propaga via bus
  // ══════════════════════════════════════════════════════════════════════
  function watchArchetype() {
    let lastArch = null;
    setInterval(() => {
      const arch = (
        localStorage.getItem('kob_arch') ||
        localStorage.getItem('ARCHETYPE_ACTIVE') ||
        'kobllux'
      ).toLowerCase().replace(/[^a-z]/g, '');

      if (arch !== lastArch) {
        lastArch = arch;
        // Sinaliza para todos os módulos relevantes
        KQ.emit('watcher', 'pulse',   { arch });
        KQ.emit('watcher', 'vitalis', { arch });
        KQ.emit('watcher', 'rhea',    { arch });
        KQ.emit('watcher', 'lumine',  { arch });
        // Stamping visual: destaca elementos do arquétipo ativo
        document.querySelectorAll('[data-arch]').forEach(el => {
          el.classList.toggle('kq-active', el.dataset.arch === arch);
        });
      }
    }, 700);
  }

  // ══════════════════════════════════════════════════════════════════════
  // 7. BOOT SEQUENCE fractal 3·6·9·7
  // ══════════════════════════════════════════════════════════════════════
  function boot() {
    console.log('[KQ∆7] Boot · KOBLLUX Quantum · VERDADE×INTEGRAR÷Δ=∞');

    // 3 — DETECTAR: stampeia e injeta CSS
    stamp();
    injectQuantumCSS();

    // 6 — INTEGRAR: sobe módulos
    module_0x01_kodux();
    module_0x02_bllue();
    module_0x03_atlas();
    module_0x04_pulse();
    module_0x05_vitalis();
    module_0x06_serena();
    module_0x07_kaos();
    module_0x08_login();
    module_0x09_rhea();
    module_0x0B_aion();

    // 9 — EXPANDIR: watchers
    watchArchetype();

    // 7 — SELAR: marca elementos como prontos
    setTimeout(() => {
      document.querySelectorAll('[data-opcode]').forEach(el =>
        el.classList.replace('kq-loading', 'kq-ready') || el.classList.add('kq-ready')
      );
      KQ.broadcast('system', { action: 'ready', opcodes: Object.keys(QM).length });
      G.logMistico?.('[KQ∆7] Sistema quântico online · ' + Object.keys(QM).length + ' módulos');
    }, 800);

    // Expõe API global
    G.KOBLLUX_QUANTUM = { KQ, QM, stamp, lazyLoad };
    console.log('[KQ∆7] window.KOBLLUX_QUANTUM disponível');
  }

  // Executa quando DOM estiver pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    setTimeout(boot, 0);
  }

})(window);
