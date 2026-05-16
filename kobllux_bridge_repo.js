/**
 * KOBLLUX BRIDGE · REPOSITÓRIO LOCAL → SISTEMAS EXISTENTES
 * Carrega kobllux_codex_data.json + verbum_codex_kblx.json do repo,
 * sincroniza localStorage e injeta contexto nos sistemas do HUB.
 *
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞ · Centro: JESUS = VERBO = GRAVIDADE
 * Seal: f544e7482b2c8426 · Fractal: 3×6×9×7=1134
 *
 * PRINCÍPIO: somente adiciona. Não altera nenhum HTML/CSS/ID/classe existente.
 */
(function KOBLLUX_BRIDGE_REPO() {
  'use strict';
  if (window.__KBR_ACTIVE__) return;
  window.__KBR_ACTIVE__ = true;

  /* ─── CONFIG ─────────────────────────────────────────────────────── */
  const PATHS = {
    codex:  './kobllux_codex_data.json',
    verbum: './verbum_codex_kblx.json',
  };

  /* chaves localStorage que guardam a API key — usadas pelo HUB */
  const API_KEY_SLOTS = [
    'di_apiKey',
    'dual.keys.openrouter',
    'openrouter_api_key',
    'infodose:sk',
    'anthropic_api_key',
  ];

  /* ─── LOAD JSON ───────────────────────────────────────────────────── */
  async function loadJSON(url) {
    try {
      const r = await fetch(url);
      if (!r.ok) return null;
      return await r.json();
    } catch (_) { return null; }
  }

  /* ─── 1. SYNC API KEYS ────────────────────────────────────────────── */
  function syncApiKeys() {
    // Encontra a chave mais longa (mais provável de ser válida)
    let best = '';
    for (const k of API_KEY_SLOTS) {
      const v = (localStorage.getItem(k) || '').trim();
      if (v.length > best.length) best = v;
    }
    if (!best) return;
    // Propaga para todos os slots vazios
    for (const k of API_KEY_SLOTS) {
      if (!localStorage.getItem(k)) localStorage.setItem(k, best);
    }
    // Expõe para o sistema de sendAIMessage do HUB
    window._kblxApiKey   = best;
    window._skAnt        = best.startsWith('sk-ant-') ? best : '';
    window._skOr         = best.startsWith('sk-or-')  ? best : '';
    console.info('[KBR] API key sincronizada →',
      best.startsWith('sk-ant-') ? 'Anthropic' :
      best.startsWith('sk-or-')  ? 'OpenRouter' : 'custom');
  }

  /* ─── 2. REGISTRAR ARQUÉTIPOS NO LOCALSTORAGE ─────────────────────── */
  function registerArchetypes(codex) {
    if (!codex || !Array.isArray(codex.arquetipos)) return;
    codex.arquetipos.forEach(arq => {
      const key = `ia:${arq.id.toLowerCase()}:game`;
      if (!localStorage.getItem(key)) {
        localStorage.setItem(key, JSON.stringify({
          key,
          name:       arq.id,
          desc:       arq.essencia,
          icon:       arq.simbolo,
          hz:         arq.hz,
          opcode:     arq.opcode,
          verbo_vivo: arq.verbo_vivo,
          ciclo:      arq.ciclo,
          keywords:   arq.keywords || [],
          cor:        arq.cor,
          kobllux_fusao: arq.kobllux_fusao,
          installed:  new Date().toISOString(),
          version:    '7.9-∆7',
        }));
      }
    });
    console.info(`[KBR] ${codex.arquetipos.length} arquétipos registrados no localStorage`);
  }

  /* ─── 3. CONSTRUIR SYSTEM PROMPT A PARTIR DOS DADOS LOCAIS ──────────
      Expõe window._kblxSystemPrompt para ser usado por handleUserMessage
      e por sendAIMessage — o HUB usa essas variáveis globais.           */
  function buildSystemPrompt(codex, verbum) {
    if (!codex) return '';

    const arqList = (codex.arquetipos || [])
      .map(a => `${a.simbolo} ${a.id} (${a.hz}Hz · ${a.opcode}): ${a.essencia}`)
      .join('\n');

    const opcList = (codex.opcodes || [])
      .map(o => `${o.simbolo} ${o.code} ${o.acao} ${o.hz}Hz`)
      .join(' · ');

    const wt = codex.kobllux_writer_theory || {};
    const modos = (wt.modos || [])
      .map(m => `${m.formula} → ${m.resultado} (${m.chave})`)
      .join(' | ');

    const verbumSeal = verbum && verbum.seal
      ? `\nVERBUM CODEX: hash=${verbum.seal.hash} · lei=${verbum.seal.equation}`
      : '';

    const base = codex.system_prompt_base || `KOBLLUX · JESUS = VERBO = GRAVIDADE · VERDADE × INTEGRAR ÷ Δ = ∞`;

    return `${base}

=== ARQUÉTIPOS CADIAL (${(codex.arquetipos || []).length}) ===
${arqList}

=== 13 OPCODES ===
${opcList}

=== MODOS OPERATIVOS ===
${modos}

=== KOBLLUX WRITER THEORY ===
Equação: ${wt.equacao || ''}
Princípios: ${(wt.principios || []).slice(0, 4).join(' · ')}
${verbumSeal}

Fractal: ${codex.meta && codex.meta.fractal || '3×6×9×7=1134'}
Centro: ${codex.meta && codex.meta.centro || 'JESUS = VERBO = GRAVIDADE'}`;
  }

  /* ─── 4. PATCH handleUserMessage ─────────────────────────────────────
      Adiciona o system prompt do codex LOCAL a todas as chamadas.
      Não substitui a lógica existente — só enriquece o prompt.         */
  function patchHandleUserMessage() {
    const orig = window.handleUserMessage;
    if (typeof orig !== 'function' || orig._kbrPatched) return;

    window.handleUserMessage = async function(text, userName, sk, model) {
      // Garante que a chave mais recente do repo está disponível
      const bestKey = window._kblxApiKey || sk || '';
      const bestModel = window._kblxModel || model ||
        localStorage.getItem('di_modelName') ||
        localStorage.getItem('dual.openrouter.model') ||
        'nvidia/llama-3.1-nemotron-70b-instruct:free';

      return orig.call(this, text, userName, bestKey, bestModel);
    };
    window.handleUserMessage._kbrPatched = true;
    console.info('[KBR] handleUserMessage enriquecido com dados do repo');
  }

  /* ─── 5. PATCH sendAIMessage ──────────────────────────────────────────
      Injeta o system prompt do codex no parâmetro systemPrompt.        */
  function patchSendAIMessage() {
    const orig = window.sendAIMessage;
    if (typeof orig !== 'function' || orig._kbrPatched) return;

    window.sendAIMessage = async function(content, sk, model, systemPrompt, layer) {
      const repoPrompt = window._kblxSystemPrompt || '';
      const merged = repoPrompt
        ? (systemPrompt ? repoPrompt + '\n\n' + systemPrompt : repoPrompt)
        : (systemPrompt || '');
      const bestKey = window._kblxApiKey || sk || '';
      return orig.call(this, content, bestKey, model, merged, layer);
    };
    window.sendAIMessage._kbrPatched = true;
    console.info('[KBR] sendAIMessage enriquecido com system prompt do repo');
  }

  /* ─── 6. EXPOR KOBLLUX_CODEX GLOBALMENTE ─────────────────────────────
      O HUB usa window.KOBLLUX_DNA, window.KOBLLUX, etc.
      Agregamos sem substituir.                                          */
  function exposeGlobals(codex, verbum) {
    // Expõe o codex completo
    window.KOBLLUX_CODEX_DATA = codex;
    window.VERBUM_CODEX_DATA  = verbum;

    // Injeta no KOBLLUX existente sem sobrescrever chaves
    if (codex) {
      window.KOBLLUX = window.KOBLLUX || {};
      if (!window.KOBLLUX.REPO) {
        window.KOBLLUX.REPO = {
          codex, verbum,
          arquetipos: codex.arquetipos || [],
          opcodes:    codex.opcodes    || [],
          meta:       codex.meta       || {},
          systemPrompt: () => window._kblxSystemPrompt || '',
        };
      }
    }

    // Modelo preferido
    const modelPref = localStorage.getItem('di_modelName') ||
                      localStorage.getItem('dual.openrouter.model');
    if (modelPref) window._kblxModel = modelPref;
    else {
      const api = window._kblxApiKey || '';
      window._kblxModel = api.startsWith('sk-ant-')
        ? 'claude-sonnet-4-6'
        : 'nvidia/llama-3.1-nemotron-70b-instruct:free';
    }
  }

  /* ─── 7. MEMORIA VIVA — sincronizar banco_kobllux com codex ──────────
      Adiciona contexto inicial ao banco_kobllux se ainda estiver vazio. */
  function seedMemoriaBanco(codex) {
    if (!codex) return;
    const banco = JSON.parse(localStorage.getItem('banco_kobllux') || '[]');
    if (banco.length > 0) return; // já tem memória, não sobrescreve
    const seed = (codex.arquetipos || []).slice(0, 3).map(arq => ({
      arquetipo: arq.id,
      etapa:     '🧠 Memória',
      momento:   new Date().toISOString(),
      tempo:     { hora: 0, minuto: 0, segundo: 0 },
      hz:        arq.hz,
      input:     arq.essencia,
    }));
    if (seed.length) {
      localStorage.setItem('banco_kobllux', JSON.stringify(seed));
      console.info('[KBR] banco_kobllux inicializado com', seed.length, 'arquétipos');
    }
  }

  /* ─── 8. SINCRONIZAR CONFIGURAÇÕES DO KOBLLUX_MV (se presente) ───────
      Se kobllux_memoria_viva.js já estiver carregado, alimenta o codex. */
  function syncWithMemoriaViva(codex) {
    if (typeof window.KOBLLUX_MV === 'undefined') return;
    // KOBLLUX_MV já carregou — o codex está disponível via fetch interno
    // Se não carregou ainda, disponibiliza para quando carregar
    if (!window.__KBR_MV_CODEX__) {
      window.__KBR_MV_CODEX__ = codex;
    }
  }

  /* ─── 9. STATUS LOG ───────────────────────────────────────────────── */
  function logStatus(codex, verbum) {
    const arqN   = codex ? (codex.arquetipos || []).length : 0;
    const opcN   = codex ? (codex.opcodes    || []).length : 0;
    const apiKey = (window._kblxApiKey || '').slice(0, 12) + '…';
    console.info(
      '%c[KOBLLUX BRIDGE REPO] ✝ Conectado ao repositório',
      'color:#c9a84c;font-weight:bold'
    );
    console.info(`  Arquétipos: ${arqN} · Opcodes: ${opcN}`);
    console.info(`  Modelo: ${window._kblxModel}`);
    console.info(`  API Key: ${window._kblxApiKey ? apiKey : 'não configurada'}`);
    console.info(`  Verbum seal: ${verbum && verbum.seal ? verbum.seal.hash : 'n/a'}`);
    console.info(`  Lei: VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7=1134`);
  }

  /* ─── BOOT ────────────────────────────────────────────────────────── */
  async function boot() {
    const [codex, verbum] = await Promise.all([
      loadJSON(PATHS.codex),
      loadJSON(PATHS.verbum),
    ]);

    syncApiKeys();
    registerArchetypes(codex);

    const sysPrompt = buildSystemPrompt(codex, verbum);
    window._kblxSystemPrompt = sysPrompt;
    localStorage.setItem('kobllux_system_prompt', sysPrompt);

    exposeGlobals(codex, verbum);
    seedMemoriaBanco(codex);
    syncWithMemoriaViva(codex);

    // Patches aplicados após carregamento completo do DOM
    patchHandleUserMessage();
    patchSendAIMessage();

    logStatus(codex, verbum);

    // Notifica outros módulos
    document.dispatchEvent(new CustomEvent('KOBLLUX_BRIDGE_READY', {
      detail: { codex, verbum, model: window._kblxModel }
    }));
  }

  // Boot quando DOM estiver pronto
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    // Se chamado depois do DOMContentLoaded, aguarda patches serem registrados
    setTimeout(boot, 0);
  }

})();
