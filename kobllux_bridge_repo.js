/**
 * KOBLLUX BRIDGE · REPOSITÓRIO LOCAL → HUB UNO
 * ═══════════════════════════════════════════════════════
 * Conecta kobllux_codex_data.json + verbum_codex_kblx.json
 * ao HUB UNO, ativa todos os 12 arquétipos CADIAL e
 * sincroniza API keys, system prompt e banco_kobllux.
 *
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 * Centro: JESUS = VERBO = GRAVIDADE
 * Seal: f544e7482b2c8426 · Fractal: 3×6×9×7=1134
 *
 * PRINCÍPIO: somente adiciona. Nunca altera HTML/CSS/IDs existentes.
 */
(function KOBLLUX_BRIDGE_REPO() {
  'use strict';
  if (window.__KBR_ACTIVE__) return;
  window.__KBR_ACTIVE__ = true;

  /* ─── SLOTS DE API KEY — todos usados pelo HUB ───────────────── */
  const API_KEY_SLOTS = [
    'di_apiKey', 'dual.keys.openrouter',
    'openrouter_api_key', 'infodose:sk', 'anthropic_api_key',
  ];

  /* ─── ARQUÉTIPOS CADIAL — mapa filename → key ─────────────────── */
  const CADIAL_FILES = [
    'atlas','nova','vitalis','pulse','artemis','serena',
    'kaos','genus','lumine','solus','rhea','aion'
  ];

  /* iframes de arquétipos rastreados {key → HTMLIFrameElement} */
  const _iframes = {};
  let _codex = null, _verbum = null;

  /* ─── 1. LOAD JSON DO REPO ────────────────────────────────────── */
  async function loadJSON(url) {
    try {
      const r = await fetch(url + '?_=' + Date.now());
      return r.ok ? await r.json() : null;
    } catch (_) { return null; }
  }

  /* ─── 2. SYNC API KEYS ────────────────────────────────────────── */
  function syncApiKeys() {
    let best = '';
    for (const k of API_KEY_SLOTS) {
      const v = (localStorage.getItem(k) || '').trim();
      if (v.length > best.length) best = v;
    }
    if (!best) return best;
    for (const k of API_KEY_SLOTS) {
      if (!localStorage.getItem(k)) localStorage.setItem(k, best);
    }
    window._kblxApiKey = best;
    window._skAnt  = best.startsWith('sk-ant-') ? best : '';
    window._skOr   = best.startsWith('sk-or-')  ? best : '';
    return best;
  }

  /* ─── 3. BUILD SYSTEM PROMPT ─────────────────────────────────── */
  function buildSystemPrompt(codex, verbum) {
    if (!codex) return '';
    const arqList = (codex.arquetipos || [])
      .map(a => `${a.simbolo} ${a.id} (${a.hz}Hz·${a.opcode}): ${a.essencia} — "${a.verbo_vivo}"`)
      .join('\n');
    const opcList = (codex.opcodes || [])
      .map(o => `${o.simbolo} ${o.code} ${o.acao} ${o.hz}Hz`)
      .join(' · ');
    const wt = codex.kobllux_writer_theory || {};
    const modos = (wt.modos || [])
      .map(m => `${m.formula}→${m.resultado}(${m.chave})`)
      .join(' | ');
    const vseal = verbum && verbum.seal
      ? `\nVERBUM: ${verbum.seal.equation} · hash=${verbum.seal.hash}` : '';
    const base = codex.system_prompt_base ||
      'KOBLLUX · JESUS=VERBO=GRAVIDADE · VERDADE×INTEGRAR÷Δ=∞';
    return `${base}\n\n=== 12 ARQUÉTIPOS CADIAL ===\n${arqList}\n\n=== 13 OPCODES ===\n${opcList}\n\n=== MODOS OPERATIVOS ===\n${modos}${vseal}\n\nFractal: ${codex.meta?.fractal||'3×6×9×7=1134'} · Centro: ${codex.meta?.centro||'JESUS=VERBO'}`;
  }

  /* ─── 4. REGISTRAR ARQUÉTIPOS NO LOCALSTORAGE ─────────────────── */
  function registerArchetypes(codex) {
    if (!codex?.arquetipos) return;
    const map = {};
    codex.arquetipos.forEach(arq => { map[arq.id.toLowerCase()] = arq; });

    /* também registra no formato di_activeArchetype (Chat Cinematic) */
    const archDB = codex.arquetipos.map(arq => ({
      id:   arq.id.toLowerCase(),
      name: arq.id,
      hz:   arq.hz,
      primary:   arq.cor  || '#4fc3f7',
      secondary: arq.cor_accent || arq.cor || '#9b6dff',
      essencia:  arq.essencia,
      verbo_vivo: arq.verbo_vivo,
      simbolo:   arq.simbolo,
      opcode:    arq.opcode,
      ciclo:     arq.ciclo,
      keywords:  arq.keywords || [],
    }));
    window._kblxArchDB = archDB;

    /* localStorage ia:<nome>:game — usado pelo HUB */
    codex.arquetipos.forEach(arq => {
      const key = `ia:${arq.id.toLowerCase()}:game`;
      if (!localStorage.getItem(key)) {
        localStorage.setItem(key, JSON.stringify({
          key, name: arq.id, desc: arq.essencia,
          icon: arq.simbolo, hz: arq.hz, opcode: arq.opcode,
          verbo_vivo: arq.verbo_vivo, ciclo: arq.ciclo,
          keywords: arq.keywords || [], cor: arq.cor,
          kobllux_fusao: arq.kobllux_fusao,
          installed: new Date().toISOString(), version: '7.9-∆7',
          url: `./archetypes/${arq.id.toLowerCase()}.html`,
        }));
      }
    });
    console.info(`[KBR] ${codex.arquetipos.length} arquétipos registrados`);
  }

  /* ─── 5. EXPANDIR arch-select COM TODOS OS CADIAL ─────────────── */
  function expandArchSelect(codex) {
    const sel = document.getElementById('arch-select');
    if (!sel || !codex?.arquetipos) return;

    /* Preserva opções existentes não-CADIAL (elysha, horus, etc.) */
    const existingNonCadial = Array.from(sel.options)
      .filter(o => {
        const k = o.value.replace(/\.html$/i, '').toLowerCase();
        return !CADIAL_FILES.includes(k);
      })
      .map(o => ({ value: o.value, text: o.textContent }));

    sel.innerHTML = '';

    /* Adiciona todos os 12 CADIAL com nomes ricos */
    codex.arquetipos.forEach(arq => {
      const key = arq.id.toLowerCase();
      const opt = document.createElement('option');
      opt.value = `${key}.html`;
      opt.textContent = `${arq.simbolo} ${arq.id} · ${arq.hz}Hz`;
      opt.dataset.hz    = arq.hz;
      opt.dataset.cor   = arq.cor;
      opt.dataset.ciclo = arq.ciclo;
      sel.appendChild(opt);
    });

    /* Re-adiciona os não-CADIAL */
    existingNonCadial.forEach(({ value, text }) => {
      if (!CADIAL_FILES.includes(value.replace(/\.html$/i, '').toLowerCase())) {
        const opt = document.createElement('option');
        opt.value = value; opt.textContent = text;
        sel.appendChild(opt);
      }
    });

    /* Restaura seleção salva */
    const saved = localStorage.getItem('di_activeArchetype');
    if (saved) {
      const match = Array.from(sel.options)
        .find(o => o.value.replace(/\.html$/i,'').toLowerCase() === saved.toLowerCase());
      if (match) sel.value = match.value;
    }

    console.info(`[KBR] arch-select expandido: ${sel.options.length} opções`);
  }

  /* ─── 6. INJETAR DADOS NO IFRAME DO ARQUÉTIPO ─────────────────── */
  function injectToArchFrame(frame, archKey) {
    if (!frame || !_codex) return;
    const sk    = window._kblxApiKey || '';
    const model = window._kblxModel  || 'nvidia/llama-3.1-nemotron-70b-instruct:free';
    const arq   = (_codex.arquetipos || [])
      .find(a => a.id.toLowerCase() === archKey.toLowerCase());

    const msg = {
      type:  'arch:init',
      arch:  archKey,
      sk,
      model,
      data:  arq ? {
        essencia:   arq.essencia,
        verbo_vivo: arq.verbo_vivo,
        hz:         arq.hz,
        opcode:     arq.opcode,
        simbolo:    arq.simbolo,
        ciclo:      arq.ciclo,
        cor:        arq.cor,
        cor_accent: arq.cor_accent,
        keywords:   arq.keywords || [],
        kobllux_fusao: arq.kobllux_fusao,
      } : null,
      systemPrompt: window._kblxSystemPrompt || '',
    };

    try { frame.contentWindow.postMessage(msg, '*'); } catch (_) {}
  }

  /* ─── 7. OBSERVAR CARREGAMENTO DO arch-frame ──────────────────── */
  function watchArchFrame() {
    const frame = document.getElementById('arch-frame');
    if (!frame) return;

    frame.addEventListener('load', () => {
      const sel = document.getElementById('arch-select');
      const key = sel ? sel.value.replace(/\.html$/i, '') : 'atlas';
      _iframes[key] = frame;
      setTimeout(() => injectToArchFrame(frame, key), 200);
    });

    /* Observa mudanças no src do frame */
    const obs = new MutationObserver(() => {
      const sel = document.getElementById('arch-select');
      const key = sel ? sel.value.replace(/\.html$/i, '') : 'atlas';
      _iframes[key] = frame;
    });
    obs.observe(frame, { attributes: true, attributeFilter: ['src'] });
  }

  /* ─── 8. ESCUTAR postMessage DOS ARQUÉTIPOS ───────────────────── */
  function listenArchMessages() {
    window.addEventListener('message', (ev) => {
      const m = ev.data;
      if (!m || typeof m !== 'object') return;

      switch (m.type) {
        case 'arch:ready': {
          /* Arquétipo carregou e está pronto — injetar dados */
          const key   = m.arch || '';
          const frame = document.getElementById('arch-frame');
          if (frame && key) {
            _iframes[key] = frame;
            injectToArchFrame(frame, key);
            /* Salvar arquétipo ativo */
            localStorage.setItem('di_activeArchetype', key);
            localStorage.setItem('kobllux_arch_active', key);
            /* Notificar Chat Cinematic se disponível */
            if (window.KOBLLUX_CHAT?.applyArchetype) {
              const archDB = window._kblxArchDB || [];
              const idx = archDB.findIndex(a => a.id === key);
              if (idx >= 0) window.KOBLLUX_CHAT.applyArchetype(idx);
            }
          }
          break;
        }

        case 'arch:played': {
          const key = m.arch || '';
          localStorage.setItem('di_activeArchetype', key);
          /* Salvar na memória viva */
          try {
            const banco = JSON.parse(localStorage.getItem('banco_kobllux') || '[]');
            banco.push({
              arquetipo: key.toUpperCase(),
              etapa:     'Voz · Arquétipo',
              momento:   new Date().toISOString(),
              input:     (m.text || '').slice(0, 80),
            });
            if (banco.length > 369) banco.splice(0, banco.length - 369);
            localStorage.setItem('banco_kobllux', JSON.stringify(banco));
          } catch (_) {}
          break;
        }

        case 'arch:consulta-resposta':
          /* Log da consulta no KOBLLUX_LOG se disponível */
          try {
            if (window.KOBLLUX_LOG?.emit)
              window.KOBLLUX_LOG.emit('ARCH·CONSULTA', {
                arch: m.arch, pergunta: m.pergunta,
                resp: (m.resposta || '').slice(0, 60),
              });
          } catch (_) {}
          break;
      }
    }, false);
  }

  /* ─── 9. ATUALIZAR AGENTS DA RODA VIVA ───────────────────────── */
  function activateRodaVivaAgents(codex) {
    if (!codex?.arquetipos) return;

    /* Expõe ARCHETYPES_DB para o Chat Cinematic */
    if (!window.ARCHETYPES_DB) {
      window.ARCHETYPES_DB = (window._kblxArchDB || codex.arquetipos.map(a => ({
        id: a.id.toLowerCase(), name: a.id,
        primary: a.cor || '#4fc3f7', secondary: a.cor_accent || '#9b6dff',
        hz: a.hz, essencia: a.essencia, verbo_vivo: a.verbo_vivo,
        simbolo: a.simbolo, opcode: a.opcode,
      })));
    }

    /* Expõe para KOBLLUX_ARCH_MANAGER */
    window.KOBLLUX_ARCH_MANAGER = {
      codex,
      archetypes: codex.arquetipos,
      getByKey: k => codex.arquetipos.find(a => a.id.toLowerCase() === k.toLowerCase()),
      getActive: () => {
        const key = localStorage.getItem('di_activeArchetype') || 'atlas';
        return codex.arquetipos.find(a => a.id.toLowerCase() === key.toLowerCase());
      },
      activate: (key) => {
        const frame = document.getElementById('arch-frame');
        const sel   = document.getElementById('arch-select');
        if (sel) {
          const opt = Array.from(sel.options)
            .find(o => o.value.replace(/\.html$/i,'').toLowerCase() === key.toLowerCase());
          if (opt) sel.value = opt.value;
        }
        if (frame) injectToArchFrame(frame, key);
        localStorage.setItem('di_activeArchetype', key);
      },
      speakAll: () => {
        const frame = document.getElementById('arch-frame');
        if (frame) {
          try {
            frame.contentWindow.postMessage({ type: 'arch:requestSpeak' }, '*');
          } catch (_) {}
        }
      },
      consultAll: (pergunta) => {
        const frame = document.getElementById('arch-frame');
        if (frame) {
          try {
            frame.contentWindow.postMessage({
              type: 'arch:consultar', arch: 'todos', pergunta
            }, '*');
          } catch (_) {}
        }
      },
    };

    console.info('[KBR] KOBLLUX_ARCH_MANAGER ativo · ' + codex.arquetipos.length + ' agentes');
  }

  /* ─── 10. SINCRONIZAR MODELO PREFERIDO ───────────────────────── */
  function syncModel() {
    const stored = localStorage.getItem('di_modelName') ||
                   localStorage.getItem('dual.openrouter.model');
    if (stored) { window._kblxModel = stored; return; }
    const apiKey = window._kblxApiKey || '';
    window._kblxModel = apiKey.startsWith('sk-ant-')
      ? 'claude-sonnet-4-6'
      : 'nvidia/llama-3.1-nemotron-70b-instruct:free';
  }

  /* ─── 11. PATCH handleUserMessage + sendAIMessage ────────────── */
  function patchAIHandlers() {
    const origHandle = window.handleUserMessage;
    if (typeof origHandle === 'function' && !origHandle._kbrPatched) {
      window.handleUserMessage = async function(text, userName, sk, model) {
        return origHandle.call(this, text, userName,
          window._kblxApiKey || sk || '',
          window._kblxModel  || model || '');
      };
      window.handleUserMessage._kbrPatched = true;
    }

    const origSend = window.sendAIMessage;
    if (typeof origSend === 'function' && !origSend._kbrPatched) {
      window.sendAIMessage = async function(content, sk, model, systemPrompt, layer) {
        const repoPrompt = window._kblxSystemPrompt || '';
        const merged = repoPrompt
          ? repoPrompt + '\n\n' + (systemPrompt || '')
          : (systemPrompt || '');
        return origSend.call(this, content,
          window._kblxApiKey || sk || '', model, merged, layer);
      };
      window.sendAIMessage._kbrPatched = true;
    }
  }

  /* ─── 12. SEED banco_kobllux ─────────────────────────────────── */
  function seedMemoriaBanco(codex) {
    if (!codex?.arquetipos) return;
    try {
      const banco = JSON.parse(localStorage.getItem('banco_kobllux') || '[]');
      if (banco.length > 0) return;
      const seed = codex.arquetipos.slice(0, 3).map(arq => ({
        arquetipo: arq.id, etapa: '🧠 Memória',
        momento: new Date().toISOString(),
        tempo: { hora: 0, minuto: 0, segundo: 0 },
        hz: arq.hz, input: arq.essencia,
      }));
      localStorage.setItem('banco_kobllux', JSON.stringify(seed));
    } catch (_) {}
  }

  /* ─── 13. EXPOR GLOBAIS ──────────────────────────────────────── */
  function exposeGlobals(codex, verbum) {
    window.KOBLLUX_CODEX_DATA = codex;
    window.VERBUM_CODEX_DATA  = verbum;
    window.KOBLLUX = window.KOBLLUX || {};
    if (!window.KOBLLUX.REPO) {
      window.KOBLLUX.REPO = {
        codex, verbum,
        arquetipos:   codex?.arquetipos || [],
        opcodes:      codex?.opcodes    || [],
        meta:         codex?.meta       || {},
        systemPrompt: () => window._kblxSystemPrompt || '',
        apiKey:       () => window._kblxApiKey || '',
        model:        () => window._kblxModel  || '',
      };
    }
  }

  /* ─── BOOT SEQUENCE ──────────────────────────────────────────── */
  async function boot() {
    /* 1. Carregar JSONs em paralelo */
    const [codex, verbum] = await Promise.all([
      loadJSON('./kobllux_codex_data.json'),
      loadJSON('./verbum_codex_kblx.json'),
    ]);
    _codex  = codex;
    _verbum = verbum;

    /* 2. Sincronizar API keys e modelo */
    syncApiKeys();
    syncModel();

    /* 3. System prompt */
    const sysPrompt = buildSystemPrompt(codex, verbum);
    window._kblxSystemPrompt = sysPrompt;
    localStorage.setItem('kobllux_system_prompt', sysPrompt);

    /* 4. Registrar arquétipos */
    registerArchetypes(codex);

    /* 5. Expor globais */
    exposeGlobals(codex, verbum);

    /* 6. Semear memória */
    seedMemoriaBanco(codex);

    /* 7. Expandir arch-select */
    expandArchSelect(codex);

    /* 8. Ativar agentes da Roda Viva */
    activateRodaVivaAgents(codex);

    /* 9. Observar arch-frame */
    watchArchFrame();

    /* 10. Escutar postMessage dos arquétipos */
    listenArchMessages();

    /* 11. Patch AI handlers */
    patchAIHandlers();

    /* 12. Injetar nos iframes já carregados */
    const frame = document.getElementById('arch-frame');
    if (frame) {
      const sel = document.getElementById('arch-select');
      const key = sel?.value?.replace(/\.html$/i, '') || 'atlas';
      setTimeout(() => injectToArchFrame(frame, key), 500);
    }

    /* 13. Log final */
    const n = codex?.arquetipos?.length || 0;
    console.info(
      '%c[KOBLLUX BRIDGE REPO] ✝ Ativo · ' + n + ' arquétipos · ' + (codex?.opcodes?.length || 0) + ' opcodes',
      'color:#c9a84c;font-weight:bold'
    );
    console.info('  API: ' + (window._kblxApiKey ? (window._kblxApiKey.startsWith('sk-ant-') ? 'Anthropic' : 'OpenRouter') : 'não configurada'));
    console.info('  Model: ' + window._kblxModel);
    console.info('  Lei: VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7=1134');

    /* 14. Disparar evento */
    document.dispatchEvent(new CustomEvent('KOBLLUX_BRIDGE_READY', {
      detail: { codex, verbum, n, model: window._kblxModel }
    }));
  }

  /* ─── REINJETAR QUANDO arch-select MUDA ─────────────────────── */
  document.addEventListener('change', (e) => {
    if (e.target?.id !== 'arch-select') return;
    const key   = e.target.value.replace(/\.html$/i, '');
    const frame = document.getElementById('arch-frame');
    if (frame) {
      _iframes[key] = frame;
      setTimeout(() => injectToArchFrame(frame, key), 300);
    }
    localStorage.setItem('di_activeArchetype', key);
  });

  /* ─── BOOT ───────────────────────────────────────────────────── */
  if (document.readyState === 'loading')
    document.addEventListener('DOMContentLoaded', boot);
  else
    setTimeout(boot, 0);

})();
