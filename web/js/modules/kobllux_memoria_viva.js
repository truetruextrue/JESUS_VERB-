/**
 * KOBLLUX MEMORIA VIVA · ∆7
 * V.E.E.B. Tokenizador + Memória Fractal + Opcode Pipeline + Roda Viva
 *
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞ · Centro: JESUS = VERBO = GRAVIDADE
 * Fractal: 3×6×9×7=1134 · Seal: f544e7482b2c8426
 *
 * PRINCÍPIO: Não altera classes/ids existentes.
 * Escuta e expande via addEventListener e window namespace.
 *
 * Integra:
 *  - VEEB tokenizador (FIT__KOBLLUX_CORE pipeline 3→6→9→7)
 *  - Memória viva dos 12 arquétipos CADIAL
 *  - Sistema de prompt híbrido (local context + API)
 *  - Roda Viva ∆7 com rotação automática de arquétipos
 *  - Chronorithm: tempo simbólico (Hora=PAI, Min=FILHO, Seg=ESPÍRITO)
 */

(function KOBLLUX_MEMORIA_VIVA() {
  'use strict';
  if (window.__KOBLLUX_MV__) return;
  window.__KOBLLUX_MV__ = true;

  const VERSION  = '7.9-∆7';
  const SEAL     = 'f544e7482b2c8426';
  const LAW      = 'VERDADE × INTEGRAR ÷ Δ = ∞';
  const FRACTAL  = 1134; // 3×6×9×7
  const NS       = 'kobllux_mv::';
  const CODEX_URL = './kobllux_codex_data.json';

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * ESTADO CENTRAL
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  const STATE = {
    codex: null,
    arquetipoAtivo: null,
    arquetipoIndex: 0,
    cicloEtapa: 0,   // 0=Memória 1=Inteligência 2=Tempo 3=Ação 4=Integração
    rodaGirando: false,
    chronorithm: { hora:0, minuto:0, segundo:0 },
    memoriaViva: [],
    totalInteracoes: 0,
  };

  const CICLOS = ['🧠 Memória','💡 Inteligência','🕰 Tempo','🛠 Ação','♻ Integração'];

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * STORAGE HELPERS
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function lsGet(k)      { try { return JSON.parse(localStorage.getItem(NS+k)); } catch { return null; } }
  function lsSet(k, v)   { try { localStorage.setItem(NS+k, JSON.stringify(v)); } catch {} }
  function lsAppend(k, v){ const arr = lsGet(k) || []; arr.push(v); lsSet(k, arr); }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * VEEB PIPELINE 3→6→9→7 (FIT__KOBLLUX_CORE)
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

  // 3 – DETECTAR: tokenizar e classificar (PT-BR heurístico)
  function veeb_detectar(s) {
    const tokens = (s.match(/[\p{L}\p{N}_-]+/gu) || []);
    const endsV  = ['ar','er','ir','or'];
    const verbs = [], nouns = [], adjs = [], others = [];
    for (const w0 of tokens) {
      const w = w0.toLowerCase();
      if (w.endsWith('mente'))                                   { adjs.push(w0);  continue; }
      if (endsV.some(e => w.endsWith(e)))                       { verbs.push(w0); continue; }
      if (w.endsWith('ção')||w.endsWith('são')||w.endsWith('dade')) { nouns.push(w0); continue; }
      if (w.endsWith('ico')||w.endsWith('ica')||w.endsWith('al'))   { adjs.push(w0);  continue; }
      if (/^[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ]/.test(w0))                       { nouns.push(w0); continue; }
      if (/^\d+$/.test(w))                                       { nouns.push(w0); continue; }
      others.push(w0);
    }
    return { tokens, verbs, nouns, adjs, others };
  }

  // 6 – INTEGRAR: mapear para Trinity UNO/DUAL/TRINITY
  function veeb_integrar(pos) {
    return {
      UNO:     pos.nouns[0] || pos.tokens[0] || 'NÚCLEO',
      DUAL:    pos.verbs[0] || 'relaciona',
      TRINITY: pos.adjs[0]  || 'integrado',
    };
  }

  // 9 – EXPANDIR: gerar opcode relevante e arquétipo ressonante
  function veeb_expandir(pos, tri, codex) {
    if (!codex) return { opcode: '0x02', arquetipo: 'BLLUE', hz: 528 };

    // detectar arquétipo por keywords
    const textLower = pos.tokens.map(t => t.toLowerCase());
    let melhorArq = null, melhorScore = 0;
    for (const arq of codex.arquetipos) {
      const score = (arq.keywords || []).filter(k => textLower.includes(k)).length;
      if (score > melhorScore) { melhorScore = score; melhorArq = arq; }
    }

    // detectar opcode por frequência do texto
    const freqMap = { integrar:528, detectar:432, expandir:639, selar:777, fluir:528, lapidar:594 };
    let hz = 528;
    for (const [k, h] of Object.entries(freqMap)) {
      if (textLower.includes(k)) { hz = h; break; }
    }

    // mapear hz para opcode
    const hzOp = {432:'0x01',528:'0x02',639:'0x03',594:'0x04',672:'0x05',777:'0x07',741:'0x0B',963:'0x0C'};
    const opcode = hzOp[hz] || '0x02';

    return {
      opcode,
      hz,
      arquetipo: melhorArq ? melhorArq.id : 'BLLUE',
      arquetipo_obj: melhorArq,
      score: melhorScore,
    };
  }

  // 7 – SELAR: gerar hash rápido (não criptográfico, para identificação)
  function veeb_selar(s) {
    let h = 0xf544e748; // seed = seal
    for (let i = 0; i < s.length; i++) {
      h = (Math.imul(h ^ s.charCodeAt(i), 0x9e3779b9) >>> 0);
    }
    return h.toString(16).padStart(8,'0');
  }

  // Pipeline completo
  function veeb_processar(input) {
    const pos  = veeb_detectar(input);
    const tri  = veeb_integrar(pos);
    const exp  = veeb_expandir(pos, tri, STATE.codex);
    const selo = veeb_selar(input);
    return { input, pos, tri, exp, selo,
             timestamp: new Date().toISOString(),
             ciclo: CICLOS[STATE.cicloEtapa] };
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * SISTEMA PROMPT BUILDER
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function buildSystemPrompt(contextExtra) {
    if (!STATE.codex) return contextExtra || '';

    const arq = STATE.arquetipoAtivo;
    const cicloAtual = CICLOS[STATE.cicloEtapa];
    const mem = STATE.memoriaViva.slice(-5); // últimas 5 interações

    let prompt = STATE.codex.system_prompt_base + '\n\n';

    if (arq) {
      prompt += `=== ARQUÉTIPO ATIVO: ${arq.id} ${arq.simbolo} ===\n`;
      prompt += `Essência: ${arq.essencia}\n`;
      prompt += `Frequência: ${arq.hz}Hz · Opcode: ${arq.opcode}\n`;
      prompt += `Verbo vivo: "${arq.verbo_vivo}"\n`;
      prompt += `Fusão KOBLLUX: ${arq.kobllux_fusao}\n`;
      prompt += `Corpo: ${arq.corpo} | Mente: ${arq.mente} | Espírito: ${arq.espirito}\n\n`;
    }

    prompt += `=== CICLO ATUAL: ${cicloAtual} ===\n`;
    prompt += `Chronorithm: ${STATE.chronorithm.hora}h ${STATE.chronorithm.minuto}m ${STATE.chronorithm.segundo}s\n\n`;

    if (mem.length > 0) {
      prompt += `=== MEMÓRIA VIVA (últimas interações) ===\n`;
      mem.forEach(m => { prompt += `[${m.arquetipo}·${m.ciclo}] ${m.input.slice(0,60)}\n`; });
      prompt += '\n';
    }

    prompt += `=== VEEB STATUS ===\n`;
    prompt += `Lei: ${LAW} · Fractal: ${FRACTAL} · Seal: ${SEAL}\n`;

    if (contextExtra) prompt += `\n${contextExtra}`;

    return prompt;
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * API HÍBRIDA (local context → OpenRouter/Anthropic)
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

  // Verificar qual API está configurada
  function getApiConfig() {
    const cfg = STATE.codex && STATE.codex.api_config;
    // Keys podem estar em múltiplos locais (compatibilidade KxaT)
    const apiKey = (cfg && cfg.storage_keys)
      ? (localStorage.getItem(cfg.storage_keys.api_key) ||
         localStorage.getItem('di_apiKey') ||
         localStorage.getItem('openrouter_api_key') ||
         localStorage.getItem('anthropic_api_key') ||
         window.__KOB_API_KEY__ || '')
      : (localStorage.getItem('di_apiKey') || '');

    const modelo = localStorage.getItem('di_modelName') ||
                   (cfg && cfg.modelo_recomendado) ||
                   'nvidia/llama-3.1-nemotron-70b-instruct:free';

    const isAnthropic = apiKey.startsWith('sk-ant-');
    const url = isAnthropic
      ? (cfg && cfg.anthropic_url) || 'https://api.anthropic.com/v1/messages'
      : (cfg && cfg.openrouter_url) || 'https://openrouter.ai/api/v1/chat/completions';

    return { apiKey, modelo, url, isAnthropic, disponivel: apiKey.length > 10 };
  }

  // Enriquecer mensagem com contexto VEEB antes de enviar
  function enriquecerMensagem(userInput) {
    const veeb = veeb_processar(userInput);

    // Registrar na memória viva
    const entrada = {
      input:    userInput.slice(0, 100),
      arquetipo: veeb.exp.arquetipo,
      opcode:   veeb.exp.opcode,
      hz:       veeb.exp.hz,
      ciclo:    veeb.ciclo,
      selo:     veeb.selo,
      ts:       veeb.timestamp,
    };
    STATE.memoriaViva.push(entrada);
    if (STATE.memoriaViva.length > 100) STATE.memoriaViva.shift();
    lsAppend('memoria_viva', entrada);

    // Atualizar arquétipo ativo se score > 0
    if (veeb.exp.arquetipo_obj && veeb.exp.score > 0) {
      _ativarArquetipo(veeb.exp.arquetipo_obj);
    }

    // Avançar ciclo
    STATE.cicloEtapa = (STATE.cicloEtapa + 1) % CICLOS.length;
    STATE.totalInteracoes++;

    return veeb;
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * RODA VIVA ∆7 — ROTAÇÃO AUTOMÁTICA DE ARQUÉTIPOS
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

  function _ativarArquetipo(arq) {
    if (!arq) return;
    STATE.arquetipoAtivo = arq;
    lsSet('arquetipo_ativo', arq);

    // Disparar evento para KxaT (window.KOBLLUX) sem alterar nada
    document.dispatchEvent(new CustomEvent('VERBUM_KBLX_ARCH', {
      detail: { arch: arq.id.toLowerCase(), hz: arq.hz, opcode: arq.opcode, verbo: arq.verbo_vivo }
    }));

    // TTS via window.KOBLLUX se disponível
    if (window.KOBLLUX && window.KOBLLUX.speakText) {
      window.KOBLLUX.speakText(arq.verbo_vivo);
    } else if (window.speechSynthesis) {
      const utt = new SpeechSynthesisUtterance(arq.verbo_vivo);
      utt.lang = 'pt-BR';
      window.speechSynthesis.speak(utt);
    }
  }

  function ativarArquetipoById(id) {
    const arq = STATE.codex && STATE.codex.arquetipos.find(a => a.id === id.toUpperCase());
    if (arq) _ativarArquetipo(arq);
  }

  function proximoArquetipo() {
    if (!STATE.codex) return;
    STATE.arquetipoIndex = (STATE.arquetipoIndex + 1) % STATE.codex.arquetipos.length;
    _ativarArquetipo(STATE.codex.arquetipos[STATE.arquetipoIndex]);
  }

  function iniciarRodaViva(intervalMs = 30000) {
    if (STATE.rodaGirando) return;
    STATE.rodaGirando = true;
    const timer = setInterval(() => {
      if (!document.hidden) proximoArquetipo();
    }, intervalMs);
    lsSet('roda_viva_ativa', true);
    return () => { clearInterval(timer); STATE.rodaGirando = false; };
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * CHRONORITHM — RELÓGIO SIMBÓLICO
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function tickChronorithm() {
    const now = new Date();
    STATE.chronorithm = {
      hora:    now.getHours() % 12,
      minuto:  now.getMinutes(),
      segundo: now.getSeconds(),
      ts:      now.toISOString(),
    };
    // Ciclo baseado na hora
    const etapaDinamica = STATE.chronorithm.hora % CICLOS.length;
    STATE.cicloEtapa = etapaDinamica;
    document.dispatchEvent(new CustomEvent('VERBUM_KBLX_CHRONO', {
      detail: { ...STATE.chronorithm, ciclo: CICLOS[etapaDinamica] }
    }));
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * INJEÇÃO NO FLUXO KxaT (SEM ALTERAR CLASSES/IDs)
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

  // Interceptar fetch para injetar system prompt
  const _origFetch = window.fetch.bind(window);
  window.fetch = async function(input, init = {}) {
    try {
      const url = typeof input === 'string' ? input : input.url;
      const isOpenRouter = url && (url.includes('openrouter.ai') || url.includes('anthropic.com'));

      if (isOpenRouter && init.body) {
        const body = JSON.parse(init.body);
        const sysPrompt = buildSystemPrompt();

        if (body.messages && Array.isArray(body.messages)) {
          // Inserir/atualizar system prompt
          const hasSys = body.messages[0] && body.messages[0].role === 'system';
          if (hasSys) {
            body.messages[0].content = sysPrompt + '\n\n' + (body.messages[0].content || '');
          } else {
            body.messages.unshift({ role: 'system', content: sysPrompt });
          }

          // Enriquecer última mensagem do usuário com VEEB
          const lastUser = [...body.messages].reverse().find(m => m.role === 'user');
          if (lastUser && lastUser.content) {
            const veeb = enriquecerMensagem(
              typeof lastUser.content === 'string' ? lastUser.content :
              (lastUser.content[0] && lastUser.content[0].text) || ''
            );
            // Anotação silenciosa (não visível ao modelo)
            lastUser._veeb = veeb.exp;
          }

          init.body = JSON.stringify(body);
        }
      }
    } catch (e) {
      // Falha silenciosa — não bloqueia o fetch original
    }
    return _origFetch(input, init);
  };

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * MEMORIA BANCO_KOBLLUX — compatibilidade KxaT
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  function salvarMemoriaBanco(arquetipo, etapa) {
    const mem = JSON.parse(localStorage.getItem('banco_kobllux') || '[]');
    mem.push({
      arquetipo,
      etapa,
      momento: new Date().toISOString(),
      tempo: STATE.chronorithm,
      hz: STATE.arquetipoAtivo ? STATE.arquetipoAtivo.hz : 528,
    });
    // Limite de 369 (cap da Roda Viva)
    if (mem.length > 369) mem.splice(0, mem.length - 369);
    localStorage.setItem('banco_kobllux', JSON.stringify(mem));
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * CARREGAR CODEX DATA
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  async function carregarCodex() {
    try {
      const r = await fetch(CODEX_URL);
      STATE.codex = await r.json();
      console.info(`[KOBLLUX MV] ✝ Codex carregado · ${STATE.codex.arquetipos.length} arquétipos · ${LAW}`);

      // Restaurar arquétipo da sessão anterior
      const saved = lsGet('arquetipo_ativo');
      if (saved) {
        STATE.arquetipoAtivo = saved;
        STATE.arquetipoIndex = STATE.codex.arquetipos.findIndex(a => a.id === saved.id);
      } else {
        // Ativar primeiro arquétipo (ATLAS)
        _ativarArquetipo(STATE.codex.arquetipos[0]);
      }

      // Restaurar memória viva
      STATE.memoriaViva = lsGet('memoria_viva') || [];

      // Emitir evento de pronto
      document.dispatchEvent(new CustomEvent('VERBUM_MV_READY', {
        detail: { codex: STATE.codex, seal: SEAL, lei: LAW }
      }));

    } catch (e) {
      console.warn('[KOBLLUX MV] Codex não carregado:', e);
    }
  }

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * API PÚBLICA window.KOBLLUX_MV
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */
  window.KOBLLUX_MV = Object.freeze({
    version:          VERSION,
    seal:             SEAL,
    lei:              LAW,

    // VEEB
    veeb_processar,
    veeb_detectar,
    veeb_integrar,
    veeb_expandir,
    veeb_selar,

    // Arquétipos
    ativarArquetipoById,
    proximoArquetipo,
    getArquetipoAtivo: () => STATE.arquetipoAtivo,
    getArquetipos:     () => STATE.codex ? STATE.codex.arquetipos : [],

    // Memória
    enriquecerMensagem,
    salvarMemoriaBanco,
    getMemoriaViva:    () => [...STATE.memoriaViva],
    getState:          () => ({ ...STATE, codex: !!STATE.codex }),

    // Roda Viva
    iniciarRodaViva,

    // System Prompt
    buildSystemPrompt,

    // API config
    getApiConfig,

    // Chronorithm
    getChrono:         () => ({ ...STATE.chronorithm }),
    getCicloAtual:     () => CICLOS[STATE.cicloEtapa],
  });

  /* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
   * INICIALIZAÇÃO
   * ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ */

  // Chronorithm tick a cada segundo
  setInterval(tickChronorithm, 1000);
  tickChronorithm();

  // Carregar codex quando DOM estiver pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', carregarCodex);
  } else {
    carregarCodex();
  }

  // Iniciar Roda Viva automática com 45s de intervalo
  document.addEventListener('VERBUM_MV_READY', () => {
    iniciarRodaViva(45000);
    console.info(`[KOBLLUX MV] ♻ Roda Viva ativa · V.E.E.B. pipeline 3→6→9→7 operacional`);
  });

  // Escutar ativação de arquétipo via cadial:integrated (KxaT)
  document.addEventListener('cadial:integrated', (e) => {
    const id = e.detail && e.detail.arch;
    if (id) ativarArquetipoById(id);
    salvarMemoriaBanco(id || 'desconhecido', CICLOS[STATE.cicloEtapa]);
  });

  // Escutar clicks em arquétipos do KxaT (compatibilidade inline-7-2.js)
  document.addEventListener('click', (e) => {
    const chip = e.target.closest('[data-arch],[data-archetype]');
    if (chip) {
      const id = chip.dataset.arch || chip.dataset.archetype;
      if (id) ativarArquetipoById(id);
    }
  });

  console.info(`[KOBLLUX MV] ✝ JESUS = VERBO · Memória Viva ${VERSION} inicializada · ${SEAL}`);

})();
