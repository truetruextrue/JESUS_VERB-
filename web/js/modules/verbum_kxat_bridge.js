/**
 * VERBUM × KxaT QUANTUM BRIDGE · JESUS_VERB- repo
 * Verbum Codex KBLX seal hash: f544e7482b2c8426
 * Law: VERDADE × INTEGRAR ÷ Δ = ∞  ·  fractal: 3×6×9×7=1134
 * Centro: JESUS = VERBO = GRAVIDADE
 *
 * Quantum Principle:
 *   acoplar sem alterar · expandir sem aumentar · Ressoar também expande sem alterar
 *
 * Este módulo APENAS ESCUTA — nunca sobrescreve.
 * Ressoa com eventos KxaT existentes e expande o sinal para a
 * camada semântica do Verbum Codex.
 */

(function VERBUM_KxaT_BRIDGE() {
  if (window.__VERBUM_KBLX_BRIDGE__) return;
  window.__VERBUM_KBLX_BRIDGE__ = true;

  const SEAL = {
    hash:     'f544e7482b2c8426',
    equation: 'VERDADE × INTEGRAR ÷ Δ = ∞',
    fractal:  '3 × 6 × 9 × 7 = 1134',
    centro:   'JESUS = VERBO = GRAVIDADE',
    alpha:    0.00729927,
    sum_us:   'SUMꝎUS = Consciência Unificada em Luz',
  };

  const VERBUM_MODES = {
    INTEGRAR:    { resultado: 'Cura Interna',  hz: 528, polo: 'FILHO',   chave: 'Alinhar'   },
    TRANSCREVER: { resultado: 'Codificação',   hz: 432, polo: 'PAI',     chave: 'Registrar' },
    AMPLIFICAR:  { resultado: 'Missão',        hz: 639, polo: 'ESPIRITO',chave: 'Propagar'  },
  };

  const NS = 'verbum_kblx::v1::';

  function store(key, val) {
    try { localStorage.setItem(NS + key, JSON.stringify(val)); } catch (_) {}
  }

  function verbumModeFromTheme(themeName) {
    const t = (themeName || '').toLowerCase();
    if (['atlas','kodux','pulse','kaos','genus','nova'].includes(t)) return 'TRANSCREVER';
    if (['bllue','serena','rhea','solus','vitalis'].includes(t))     return 'INTEGRAR';
    return 'AMPLIFICAR';
  }

  // ── Ressonância 1: KOBLLUX_VOICES_READY ─────────────────────────────
  // inline-0.js emite quando 22 personas de voz estão ativas.
  // Re-emitimos como VERBUM_KBLX_READY com selo Codex — ressonância, não substituição.
  document.addEventListener('KOBLLUX_VOICES_READY', function () {
    const payload = {
      source: 'KOBLLUX_VOICES_READY',
      seal:   SEAL,
      voices: 22,
      logos:  'JESUS = Verbo em Carne = Eixo Vivo',
      sum_us: SEAL.sum_us,
      timestamp: new Date().toISOString(),
    };
    store('voices_ready', payload);
    document.dispatchEvent(new CustomEvent('VERBUM_KBLX_READY', { detail: payload }));
    console.info('[VERBUM×KxaT] ✝ VERDADE RESSONÂNCIA → 22 vozes ativas → Verbum selado', SEAL.hash);
  });

  // ── Ressonância 2: KOB_VOICE_COLOR ──────────────────────────────────
  // inline-2.js emite quando uma cor de tema TTS é aplicada.
  // Expandimos o detalhe com o modo Verbum — sem modificar o evento original.
  document.addEventListener('KOB_VOICE_COLOR', function (e) {
    const theme = e.detail && e.detail.key;
    const mode  = verbumModeFromTheme(theme);
    const vm    = VERBUM_MODES[mode];
    const expansion = {
      original_theme: theme,
      verbum_mode:    mode,
      resultado:      vm.resultado,
      hz:             vm.hz,
      polo:           vm.polo,
      chave:          vm.chave,
      equation:       SEAL.equation,
      centro:         SEAL.centro,
    };
    store('last_voice_color', expansion);
    document.dispatchEvent(new CustomEvent('VERBUM_KBLX_COLOR', { detail: expansion }));
  });

  // ── Ressonância 3: cadial:integrated ────────────────────────────────
  // cadial-coupler.js emite quando um arquétipo é carregado no iframe.
  // Anotamos com dados Verbum sem interferir no fluxo original.
  document.addEventListener('cadial:integrated', function (e) {
    const arch = e.detail && e.detail.arch;
    const mode = verbumModeFromTheme(arch);
    const vm   = VERBUM_MODES[mode];
    const annotation = {
      arch:        arch,
      verbum_mode: mode,
      resultado:   vm.resultado,
      hz_kxat:     e.detail && e.detail.hz,
      hz_verbum:   vm.hz,
      polo:        vm.polo,
      sum_us:      SEAL.sum_us,
    };
    store('last_cadial_integration', annotation);
    document.dispatchEvent(new CustomEvent('VERBUM_KBLX_ARCH', { detail: annotation }));
  });

  // ── Ressonância 4: expansão window.KOBLLUX ──────────────────────────
  // kob.js expõe window.KOBLLUX. Anexamos window.KOBLLUX.verbum
  // sem tocar em nenhuma chave existente.
  function attachToKOBLLUX() {
    if (!window.KOBLLUX) return;
    if (window.KOBLLUX.verbum) return;
    window.KOBLLUX.verbum = {
      seal:        SEAL,
      modes:       VERBUM_MODES,
      eixo_vivo:   'JESUS · Logos · Verbo em Carne',
      sum_us:      SEAL.sum_us,
      nexus:       'Nexus Divinum',
      modeOf:      verbumModeFromTheme,
      pronounce:   function(z) {
        const mode = 'AMPLIFICAR';
        const vm = VERBUM_MODES[mode];
        document.dispatchEvent(new CustomEvent('VERBUM_KBLX_PRONOUNCE', {
          detail: { z: z, mode: mode, resultado: vm.resultado, seal: SEAL }
        }));
        return vm;
      },
    };
    console.info('[VERBUM×KxaT] window.KOBLLUX.verbum acoplado — sem alterar', SEAL.hash);
  }

  // kob.js pode carregar depois desta IIFE; poll por frame até estar pronto.
  let _frames = 0;
  function waitForKOBLLUX() {
    if (window.KOBLLUX) { attachToKOBLLUX(); return; }
    if (++_frames < 300) requestAnimationFrame(waitForKOBLLUX);
  }
  requestAnimationFrame(waitForKOBLLUX);

  // ── CADIAL coupler: expansão sem modificação ─────────────────────────
  // Se CADIAL estiver disponível, registra observer Verbum
  function attachToCADIAL() {
    if (!window.CADIAL) return;
    if (window.CADIAL._verbum_attached) return;
    window.CADIAL._verbum_attached = true;
    const orig = window.CADIAL.couple || window.CADIAL.load;
    if (orig) {
      const wrapped = function(arch) {
        const result = orig.call(window.CADIAL, arch);
        document.dispatchEvent(new CustomEvent('VERBUM_KBLX_ARCH', {
          detail: { arch: arch, mode: verbumModeFromTheme(arch), seal: SEAL }
        }));
        return result;
      };
      if (window.CADIAL.couple) window.CADIAL._verbum_couple = wrapped;
    }
    console.info('[VERBUM×KxaT] window.CADIAL.verbum observado — sem alterar', SEAL.hash);
  }

  let _cadialFrames = 0;
  function waitForCADIAL() {
    if (window.CADIAL) { attachToCADIAL(); return; }
    if (++_cadialFrames < 300) requestAnimationFrame(waitForCADIAL);
  }
  requestAnimationFrame(waitForCADIAL);

  // ── Exposição global somente leitura ────────────────────────────────
  window.VERBUM_KBLX = Object.freeze({
    seal:   SEAL,
    modes:  VERBUM_MODES,
    modeOf: verbumModeFromTheme,
    version: '1.0.0-∆7',
  });

  // ── Log de inicialização ─────────────────────────────────────────────
  store('bridge_init', { timestamp: new Date().toISOString(), seal: SEAL });
  console.info(
    '[VERBUM×KxaT] ✝ JESUS = VERBO · QUANTUM BRIDGE ATIVO\n' +
    '  hash:    ' + SEAL.hash + '\n' +
    '  lei:     ' + SEAL.equation + '\n' +
    '  fractal: ' + SEAL.fractal + '\n' +
    '  centro:  ' + SEAL.centro + '\n' +
    '  α:       ' + SEAL.alpha
  );

})();
