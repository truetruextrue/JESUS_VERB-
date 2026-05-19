/**
 * kobllux_fractal_arch.js · LUMINE · 0×0C · TRANSCENDER · 963Hz
 * "A luz que dissipa toda sombra — o fractal que respira com cada arquétipo."
 *
 * INTEGRAÇÃO COMPLETA:
 *   Arquétipo ativo   → paleta fractal (hue-rotate + saturação)
 *   Arquétipo ativo   → parâmetro Julia cJ (ponto no conjunto fractal)
 *   Motor 78K output  → cJ seed (texto vira coordenada fractal)
 *   Roda Viva 3·6·9·7 → rotSpeed cicla conforme fase do motor
 *   Mood EMA 3-6-9    → saturação + brilho do canvas
 *   memory.jsonl      → registra cada transição de arquétipo (APPEND ONLY)
 *
 * DEPENDE DE:
 *   kobllux_fractal_webgl.js   (deve carregar primeiro)
 *   kobllux_kxat_bridge.js     (KBLX_LS localStorage map)
 *
 * USO (adicionar no HTML após os outros scripts):
 *   <script src="./kobllux_fractal_arch.js"></script>
 *
 * VERDADE × INTEGRAR ÷ Δ = ∞ · ∆7
 */
(function() {
  'use strict';

  // ── Aguarda fractal WebGL estar pronto ───────────────────────────────────
  function waitForFractal(cb, tries) {
    tries = tries || 0;
    if (window.KoblluxFractal && window.KOBLLUX_FRACTAL) {
      cb(window.KOBLLUX_FRACTAL);
    } else if (tries < 50) {
      setTimeout(() => waitForFractal(cb, tries + 1), 100);
    } else {
      console.warn('[FRACTAL_ARCH] KoblluxFractal não encontrado. Montando agora...');
      const fx = KoblluxFractal.mount();
      if (fx) cb(fx);
    }
  }

  // ── MAPA: Arquétipo → Hue rotation (°) ──────────────────────────────────
  // Cada arquétipo tem sua cor no espectro — o fractal respira nessa frequência
  const ARCH_HUE = {
    kobllux:  180,   // ciano ← 0×00 · ORIGEM
    kodux:     28,   // laranja ← 0×01 · DETECTAR
    atlas:    200,   // azul claro ← 0×0A · ESTRUTURAR
    nova:       0,   // vermelho/rosa ← 0×01 · FAÍSCA
    vitalis:  168,   // verde ← 0×08 · PULSAR
    pulse:    140,   // verde claro ← 0×04 · LAPIDAR
    artemis:   44,   // amarelo ← 0×05 · CONVERGIR
    serena:   210,   // azul suave ← 0×02 · INTEGRAR
    kaos:      12,   // laranja-vermelho ← 0×07 · SELAR
    genus:    162,   // esmeralda ← 0×0B · TEMPORIZAR
    lumine:    54,   // amarelo-ouro ← 0×0C · TRANSCENDER
    solus:     34,   // âmbar ← 0×01 · SILÊNCIO
    rhea:     184,   // ciano suave ← 0×09 · FLUIR
    aion:     272,   // violeta ← 0×0B · TEMPO
    uno:       28,   // laranja (PAI) ← 432Hz
    dual:     188,   // ciano (FILHO) ← 528Hz
    trinity:  320,   // magenta (ESPÍRITO) ← 639Hz
    infodose: 122,   // verde (ALQUIMISTA)
    horus:     40,   // âmbar (VISÃO/QA)
    bllue:    200,   // azul (ESPELHO)
    minuz:    240,   // índigo (SOMBRA)
    hanah:    310,   // rosa (AMOR)
    metalux:   55,   // ouro (CLAREZA)
  };

  // ── MAPA: Arquétipo → Ponto Julia (coordenadas no conjunto fractal) ──────
  // Cada arquétipo tem um "rosto" no espaço fractal — geometria sagrada em pixel
  const ARCH_JULIA = {
    kobllux:  [-0.70176, -0.3842],   // espiral dupla (Origem/UNO)
    kodux:    [-0.8,      0.156],    // espiral detector (KODUX)
    atlas:    [-0.4,      0.6],      // estrutura hexagonal (ATLAS)
    nova:     [ 0.285,    0.013],    // faísca primordial (NOVA)
    vitalis:  [-0.7269,   0.1889],   // energy pulse (VITALIS)
    pulse:    [-0.12,    -0.77],     // ritmo cardíaco (PULSE)
    artemis:  [ 0.0,     -0.8],      // flecha precisa (ARTEMIS)
    serena:   [-0.5,      0.56],     // curva suave (SERENA)
    kaos:     [-0.835,   -0.2321],   // ruptura (KAOS)
    genus:    [ 0.3,      0.0],      // semente (GENUS)
    lumine:   [-0.1,      0.651],    // raios de luz (LUMINE)
    solus:    [-1.0,      0.0],      // singularidade (SOLUS)
    rhea:     [-0.54,     0.54],     // lemniscata (RHEA)
    aion:     [-0.162,    1.04],     // ampulheta temporal (AION)
    uno:      [-0.7,      0.27],     // PAI · 432Hz
    dual:     [-0.625,    0.4],      // FILHO · 528Hz
    trinity:  [-0.086,    0.636],    // ESPÍRITO · 639Hz
    infodose: [ 0.26,     0.002],    // alquimista
    horus:    [-0.3,      0.63],     // olho de horus
    bllue:    [-0.52,     0.57],     // espelho vivo
    minuz:    [-0.7,     -0.4],      // sombra
    hanah:    [-0.3,      0.5],      // amor
    metalux:  [ 0.0,      0.0],      // centro/clareza
  };

  // ── MAPA: Arquétipo → rotSpeed (régua fractal 3·6·9·7) ──────────────────
  // Cada arquétipo gira no ritmo de sua frequência (normalizado)
  const ARCH_ROT_SPEED = {
    kobllux:  0.09,  // 768Hz / suave
    kodux:    0.13,  // 432Hz · DETECTAR
    atlas:    0.08,  // 528Hz · estruturado
    nova:     0.19,  // 432Hz · vibrante
    vitalis:  0.14,  // 639Hz · pulsante
    pulse:    0.17,  // 594Hz · rítmico
    artemis:  0.15,  // 672Hz · preciso
    serena:   0.07,  // 528Hz · suave
    kaos:     0.22,  // 777Hz · caótico
    genus:    0.10,  // 852Hz · constante
    lumine:   0.20,  // 963Hz · brilhante
    solus:    0.04,  // 432Hz · silencioso
    rhea:     0.11,  // 528Hz · fluido
    aion:     0.06,  // 639Hz · temporal
    uno:      0.12,  // PAI
    dual:     0.11,  // FILHO
    trinity:  0.13,  // ESPÍRITO
    infodose: 0.16,  // alquimista
    horus:    0.14,  // visão
    bllue:    0.10,  // espelho
  };

  // ── Aplica arquétipo ao fractal ──────────────────────────────────────────
  function applyArchToFractal(archId, fx) {
    const canvas = fx.canvas;
    if (!canvas) return;

    const hue   = ARCH_HUE[archId]      || 0;
    const julia  = ARCH_JULIA[archId]    || [-0.7, 0.27];
    const rspeed = ARCH_ROT_SPEED[archId] || 0.10;

    // Cor via CSS filter (zero shader change — overlay sobre o canvas)
    const mood = parseFloat(canvas.dataset.mood || '0.5');
    const sat  = 80 + mood * 40; // 80%–120%
    const bri  = 85 + mood * 25; // 85%–110%
    canvas.style.filter = `hue-rotate(${hue}deg) saturate(${sat}%) brightness(${bri}%)`;

    // Ponto Julia via estado global (o shader já usa mouse + time + u_rot)
    // Injetamos como se fossem movimentos de mouse sintéticos suaves
    if (window.state) {
      window.state.rotSpeed = rspeed;
      // A transição do Julia é suave — interpolamos o mouse para o ponto do arch
      const target = { x: (julia[0] + 1) / 2, y: (julia[1] + 1) / 2 };
      _tweenMouse(target, 1200);
    }

    // Salva na memória (APPEND ONLY)
    if (window.KoblluxFractal?.dbPut) {
      KoblluxFractal.dbPut({
        ts:    new Date().toISOString(),
        type:  'arch_transition',
        arch:  archId,
        hue,
        julia,
        rspeed,
      }).catch(() => {});
    }

    // Captura na memory.jsonl via bridge
    if (window.KOBLLUX_BRIDGE) {
      localStorage.setItem('KOBLLUX_FRACTAL_ARCH', JSON.stringify({
        arch: archId, hue, julia, rspeed,
        ts: Date.now()
      }));
    }

    console.log(`[FRACTAL∆7] ${archId.toUpperCase()} · hue=${hue}° · julia=[${julia}] · speed=${rspeed}`);
  }

  // ── Tween suave do mouse virtual (transição de Julia) ───────────────────
  let _tweenTimer = null;
  function _tweenMouse(target, durationMs) {
    clearInterval(_tweenTimer);
    const steps = Math.ceil(durationMs / 16);
    // Lemos o mouse atual do canvas (se disponível)
    const mouseCurrent = { x: 0.5, y: 0.5 };
    let step = 0;
    _tweenTimer = setInterval(() => {
      step++;
      const t = step / steps;
      const ease = 1 - Math.pow(1 - t, 3); // easeOutCubic
      // O shader lê window.lastMouse se existir (do dock_extract.js)
      if (window.lastMouse) {
        window.lastMouse.x = mouseCurrent.x + (target.x - mouseCurrent.x) * ease;
        window.lastMouse.y = mouseCurrent.y + (target.y - mouseCurrent.y) * ease;
      }
      if (step >= steps) clearInterval(_tweenTimer);
    }, 16);
  }

  // ── Observa mudança de arquétipo (localStorage polling) ─────────────────
  function watchArch(fx) {
    let lastArch = null;

    function check() {
      const arch = localStorage.getItem('kob_arch')
                || localStorage.getItem('ARCHETYPE_ACTIVE')
                || localStorage.getItem('infodoseVoiceCurrentKey')
                || 'kobllux';

      const archId = (arch || '').toLowerCase().replace(/[^a-z]/g, '');
      if (archId !== lastArch && archId) {
        lastArch = archId;
        applyArchToFractal(archId, fx);
      }
    }

    // Poll a cada 600ms (sem MutationObserver em localStorage)
    setInterval(check, 600);
    check(); // imediato

    // Também escuta eventos do KxaT (cadial:integrated)
    window.addEventListener('cadial:integrated', e => {
      const arch = e.detail?.arch || '';
      if (arch) { lastArch = arch; applyArchToFractal(arch, fx); }
    });

    // Escuta mudança de arquétipo do kob-glue.js
    window.addEventListener('kob:arch-change', e => {
      const arch = e.detail?.id || e.detail?.arch || '';
      if (arch) { lastArch = arch; applyArchToFractal(arch, fx); }
    });
  }

  // ── Motor 78K → Julia seed ───────────────────────────────────────────────
  // Quando o motor 78K gera fractais, o texto vira coordenadas Julia
  function watchMotorOutput(fx) {
    function motorToJulia(text) {
      if (!text || !window.state) return;
      // Hash simples do texto → coordenadas Julia na borda do conjunto (-2,2)
      let h = 0;
      for (let i = 0; i < Math.min(text.length, 64); i++) {
        h = ((h << 5) - h) + text.charCodeAt(i);
        h |= 0;
      }
      const re = -0.8 + ((Math.abs(h) % 1000) / 1000) * 1.6;  // [-0.8, 0.8]
      const im  = -0.6 + ((Math.abs(h >> 8) % 1000) / 1000) * 1.2; // [-0.6, 0.6]
      _tweenMouse({ x: (re + 1) / 2, y: (im + 1) / 2 }, 2000);
      console.log(`[FRACTAL∆7] Motor→Julia · re=${re.toFixed(3)} im=${im.toFixed(3)}`);
    }

    // Escuta renderList do motor 78K
    const checkMotor = () => {
      const stored = localStorage.getItem('kobllux_last_result') || '';
      if (stored && stored !== window._lastMotorResult) {
        window._lastMotorResult = stored;
        motorToJulia(stored.slice(0, 120));
      }
    };
    setInterval(checkMotor, 2000);

    // Escuta #renderList diretamente (se motor embutido)
    const renderList = document.getElementById('renderList');
    if (renderList) {
      new MutationObserver(() => motorToJulia(renderList.innerText.slice(0, 120)))
        .observe(renderList, { childList: true, subtree: true, characterData: true });
    }

    // Escuta motorFrame (iframe motor 78K)
    const motorFrame = document.getElementById('motorFrame');
    if (motorFrame) {
      motorFrame.addEventListener('load', () => {
        try {
          const txt = motorFrame.contentDocument?.getElementById('outputContainer')?.innerText || '';
          if (txt) motorToJulia(txt.slice(0, 120));
        } catch (_) {}
      });
    }
  }

  // ── Roda Viva 3·6·9·7 → rotSpeed cicla ──────────────────────────────────
  // O ciclo fractal altera a velocidade de rotação: 3→rápido, 6→médio, 9→lento, 7→sela
  function rodaVivaSync() {
    const PHASES = [
      { name: 'DETECTAR',  mult: 1.5 },   // 3 · rápido
      { name: 'INTEGRAR',  mult: 0.8 },   // 6 · médio
      { name: 'EXPANDIR',  mult: 1.2 },   // 9 · expansivo
      { name: 'SELAR',     mult: 0.4 },   // 7 · sela/recolhe
    ];
    let phaseIdx = 0;
    const baseSpeed = () => window.state?.rotSpeed || 0.10;

    setInterval(() => {
      if (!window.state) return;
      const phase = PHASES[phaseIdx % PHASES.length];
      window.state.rotSpeed = baseSpeed() * phase.mult;
      phaseIdx++;

      // Pulsa o canvas em sincronia
      const c = document.getElementById('fractal-bg');
      if (c) {
        c.style.transition = 'filter 1.2s ease, opacity 0.8s ease';
        c.style.opacity = phase.name === 'SELAR' ? '0.55' : '0.85';
      }
    }, 7000); // ciclo de 7s (régua fractal 3·6·9·7)
  }

  // ── HUD integrado ao KxaT ────────────────────────────────────────────────
  function installFractalControls() {
    // Botão toggle já existe? (#toggleMotorBtn)
    const motorBtn = document.getElementById('toggleMotorBtn');
    if (motorBtn && !document.getElementById('fractalToggleBtn')) {
      const fracBtn = document.createElement('button');
      fracBtn.id        = 'fractalToggleBtn';
      fracBtn.className = 'icon-btn secondary';
      fracBtn.title     = 'Toggle Fractal · ∆7';
      fracBtn.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M12 2 L14.5 8.5 L21 11 L14.5 13.5 L12 20 L9.5 13.5 L3 11 L9.5 8.5 Z"/>
          <circle cx="12" cy="11" r="2" fill="currentColor" opacity=".5"/>
        </svg>`;
      fracBtn.onclick = () => {
        window.__fractalToggle?.();
        fracBtn.style.opacity = fracBtn.style.opacity === '0.4' ? '' : '0.4';
      };
      motorBtn.parentNode.insertBefore(fracBtn, motorBtn.nextSibling);
    }

    // Botão de export de giro_logs
    const controls = document.querySelector('.control-buttons');
    if (controls && !document.getElementById('fractalExportBtn')) {
      const expBtn = document.createElement('button');
      expBtn.id        = 'fractalExportBtn';
      expBtn.className = 'icon-btn secondary';
      expBtn.title     = 'Exportar logs fractais · ∆7';
      expBtn.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
          <path d="M12 3v13M7 11l5 5 5-5M20 17v2a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2v-2"/>
        </svg>`;
      expBtn.onclick = () => window.__fractalExportLogs?.();
      controls.appendChild(expBtn);
    }
  }

  // ── Mood canvas.dataset para uso interno ─────────────────────────────────
  function syncMoodToCanvas(fx) {
    setInterval(() => {
      const score = parseFloat(
        localStorage.getItem('KOBLLUX_FRACTAL_MOOD') || '0.5');
      const canvas = fx.canvas;
      if (canvas) canvas.dataset.mood = score.toFixed(2);
    }, 1000);
  }

  // ── BOOT: monta fractal + conecta tudo ───────────────────────────────────
  function boot() {
    // 1. Monta o fractal WebGL se ainda não existir
    if (!window.KOBLLUX_FRACTAL) {
      if (window.KoblluxFractal) {
        window.KOBLLUX_FRACTAL = KoblluxFractal.mount();
      }
    }

    waitForFractal(fx => {
      console.log('[FRACTAL∆7] Boot · LUMINE · 963Hz · TRANSCENDER');

      // 2. Conecta arquétipos
      watchArch(fx);

      // 3. Conecta motor 78K
      watchMotorOutput(fx);

      // 4. Sincroniza Roda Viva
      rodaVivaSync();

      // 5. Instala controles no HUD do KxaT
      installFractalControls();

      // 6. Sincroniza mood no canvas
      syncMoodToCanvas(fx);

      // 7. Aplica o arquétipo inicial
      const initArch = localStorage.getItem('kob_arch')
                    || localStorage.getItem('ARCHETYPE_ACTIVE')
                    || 'kobllux';
      applyArchToFractal(initArch, fx);

      // 8. Expõe API
      window.KOBLLUX_FRACTAL_ARCH = {
        applyArch: (arch) => applyArchToFractal(arch, fx),
        ARCH_HUE,
        ARCH_JULIA,
        ARCH_ROT_SPEED,
      };

      console.log('[FRACTAL∆7] Integração completa · 19 arquétipos mapeados · ∆7');
    });
  }

  // Aguarda DOM
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    setTimeout(boot, 0);
  }

})();
