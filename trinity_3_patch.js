/**
 * TRINITY 3.0 PATCH · Acoplamento Quântico
 * ─────────────────────────────────────────
 * Regra de Ouro: NÃO reescrever — apenas inserir, conectar, ressoar.
 * Carrega via: <script src="./trinity_3_patch.js" defer></script>
 * (última linha antes de </body>, depois de todos os scripts existentes)
 *
 * Fornece:
 *  - Portal Trinity iframe injetado sem alterar HTML existente
 *  - Intercepta CallAI() se existir, adiciona camada simbólica
 *  - postMessage bidirecional (app ↔ trinityFrame)
 *  - TRINITY_MEM: memória persistente via localStorage
 *  - TRINITY_THEME: troca de tema ao vivo sem reload
 */

(function () {
  'use strict';

  /* ── 1. CONSTANTES ──────────────────────────────────── */
  const TRINITY_KEY   = 'trinity_3_mem';
  const TRINITY_PHASE = ['3_DETECTAR', '6_INTEGRAR', '9_EXPANDIR', '7_SELAR'];
  const ARCHS         = ['atlas', 'bllue', 'nova', 'serena', 'aion', 'solus'];
  let   _phaseIdx     = 0;
  let   _archIdx      = 0;

  /* ── 2. MEMÓRIA PERSISTENTE ─────────────────────────── */
  const TRINITY_MEM = {
    _load() {
      try { return JSON.parse(localStorage.getItem(TRINITY_KEY) || '[]'); }
      catch (_) { return []; }
    },
    selar(entrada, saida, fase, arquetipo) {
      const mem  = this._load();
      const h    = [...(entrada + saida)].reduce((a, c) => (a * 31 + c.charCodeAt(0)) >>> 0, 7)
                    .toString(16).slice(0, 8);
      const selo = {
        ts:        new Date().toISOString(),
        entrada:   entrada.slice(0, 120),
        saida:     saida.slice(0, 120),
        fase,
        arquetipo,
        hash:      'Δ7_' + h,
      };
      mem.push(selo);
      try { localStorage.setItem(TRINITY_KEY, JSON.stringify(mem)); } catch (_) {}
      window.dispatchEvent(new CustomEvent('trinity:selado', { detail: selo }));
      return selo;
    },
    exportar() {
      const blob = new Blob(
        [JSON.stringify(this._load(), null, 2)],
        { type: 'application/json' }
      );
      const a = Object.assign(document.createElement('a'), {
        href:     URL.createObjectURL(blob),
        download: 'trinity_mem_' + Date.now() + '.json',
      });
      a.click();
    },
    limpar() { localStorage.removeItem(TRINITY_KEY); },
  };

  window.TRINITY_MEM = TRINITY_MEM;

  /* ── 3. TEMAS AO VIVO ───────────────────────────────── */
  const TRINITY_THEME = {
    _temas: {
      dark_fractal: { '--bg': '#050811', '--fg': '#e0e0e0', '--acc': '#00d4ff' },
      gold_seal:    { '--bg': '#0a0800', '--fg': '#ffd700', '--acc': '#ff9900' },
      vibe:         { '--bg': '#0d0020', '--fg': '#e0b4ff', '--acc': '#b388ff' },
      luz:          { '--bg': '#f5f5f5', '--fg': '#111',    '--acc': '#1565c0' },
    },
    aplicar(nome) {
      const tema = this._temas[nome] || this._temas['dark_fractal'];
      const root = document.documentElement;
      Object.entries(tema).forEach(([k, v]) => root.style.setProperty(k, v));
      localStorage.setItem('trinity_tema', nome);
      window.dispatchEvent(new CustomEvent('trinity:tema', { detail: { nome } }));
    },
    restaurar() {
      const salvo = localStorage.getItem('trinity_tema') || 'dark_fractal';
      this.aplicar(salvo);
    },
  };

  window.TRINITY_THEME = TRINITY_THEME;
  TRINITY_THEME.restaurar();

  /* ── 4. PORTAL IFRAME (injetado sem alterar HTML) ────── */
  function injetarPortal() {
    if (document.getElementById('trinityContainer')) return; // já existe

    const css = `
      #trinityContainer {
        position: fixed; bottom: 16px; right: 16px;
        width: 340px; height: 480px; z-index: 9990;
        border: 1px solid rgba(0,212,255,.25);
        border-radius: 12px; overflow: hidden;
        box-shadow: 0 4px 32px rgba(0,0,0,.6);
        transition: opacity .3s;
      }
      #trinityContainer.trinity-hide { opacity: 0; pointer-events: none; }
      #trinityToggleBtn {
        position: fixed; bottom: 16px; right: 16px; z-index: 9991;
        width: 44px; height: 44px; border-radius: 50%;
        background: #0a0f1a; border: 1px solid #00d4ff55;
        color: #00d4ff; font-size: 20px; cursor: pointer;
        display: flex; align-items: center; justify-content: center;
      }
    `;

    const style = document.createElement('style');
    style.textContent = css;
    document.head.appendChild(style);

    const container = document.createElement('div');
    container.id        = 'trinityContainer';
    container.className = 'trinity-hide';

    const iframe = document.createElement('iframe');
    iframe.id    = 'trinityFrame';
    iframe.name  = 'trinityFrame';
    iframe.src   = './trinity.html'; // arquivo externo — crie conforme necessário
    iframe.style.cssText = 'width:100%;height:100%;border:none;';
    container.appendChild(iframe);

    const btn = document.createElement('button');
    btn.id          = 'trinityToggleBtn';
    btn.textContent = '∆';
    btn.title       = 'Trinity 3.0';
    btn.addEventListener('click', () => {
      container.classList.toggle('trinity-hide');
    });

    document.body.appendChild(container);
    document.body.appendChild(btn);
  }

  /* ── 5. postMessage BIDIRECIONAL ─────────────────────── */
  window.addEventListener('message', function (ev) {
    const m = ev.data;
    if (!m || typeof m !== 'object') return;

    switch (m.type) {
      case 'trinity:tema':
        TRINITY_THEME.aplicar(m.tema);
        break;
      case 'trinity:comando':
        // comandos simbólicos: { type, comando, valor }
        window.dispatchEvent(new CustomEvent('trinity:exec', { detail: m }));
        break;
      case 'trinity:ping':
        ev.source && ev.source.postMessage(
          { type: 'trinity:pong', fase: TRINITY_PHASE[_phaseIdx % 4] },
          '*'
        );
        break;
    }
  });

  function enviarParaIframe(msg) {
    const frame = document.getElementById('trinityFrame');
    if (frame && frame.contentWindow) {
      frame.contentWindow.postMessage(msg, '*');
    }
  }

  window.TRINITY_SEND = enviarParaIframe;

  /* ── 6. INTERCEPTAR CallAI() ─────────────────────────── */
  function interceptarCallAI() {
    if (typeof window.CallAI !== 'function') return;

    const _original = window.CallAI;

    window.CallAI = function (entrada, ...rest) {
      const fase      = TRINITY_PHASE[_phaseIdx % 4];
      const arquetipo = ARCHS[_archIdx % ARCHS.length];
      _phaseIdx++;
      _archIdx++;

      // chama a função original e captura a Promise/resultado
      const resultado = _original.call(this, entrada, ...rest);

      if (resultado && typeof resultado.then === 'function') {
        resultado.then(saida => {
          const saidaStr = typeof saida === 'string' ? saida : JSON.stringify(saida);
          TRINITY_MEM.selar(entrada || '', saidaStr, fase, arquetipo);
          enviarParaIframe({
            type:      'trinity:ia_resp',
            fase,
            arquetipo,
            entrada:   (entrada || '').slice(0, 120),
            saida:     saidaStr.slice(0, 120),
          });
        });
      }

      return resultado;
    };
  }

  /* ── 7. BOOT ─────────────────────────────────────────── */
  function boot() {
    injetarPortal();
    interceptarCallAI(); // opera apenas se CallAI existir

    // expõe API pública
    window.TRINITY = {
      mem:       TRINITY_MEM,
      tema:      TRINITY_THEME,
      send:      enviarParaIframe,
      fase:      () => TRINITY_PHASE[_phaseIdx % 4],
      arquetipo: () => ARCHS[_archIdx % ARCHS.length],
    };

    console.log('[TRINITY 3.0] ∆7 ativo · fase:', window.TRINITY.fase());
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }

})();
