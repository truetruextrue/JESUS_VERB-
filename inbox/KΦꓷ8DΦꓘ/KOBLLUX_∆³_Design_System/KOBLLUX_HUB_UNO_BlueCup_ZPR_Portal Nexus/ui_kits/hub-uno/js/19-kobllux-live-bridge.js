(function () {
  'use strict';

  const WORKFLOW_KEY = 'kobllux.live.workflow.v1';
  const EQ_KEY = 'kobllux.eq.log';
  const REPOSITORY = 'truetruextrue/JESUS_VERB-';
  const WORKFLOW_FILE = 'kobllux-malha-viva.yml';
  const LIMIT = 500;
  const NAMESPACES = [
    'KOBLLUX', 'KOBΦ-NODE', 'JESUS_VERB-', 'KOB--NODE', 'INFODOSE',
    'CODEX-AZURE', 'MINUZ', 'FIAT-LUX', 'KOBLLUX_ORGANIZADO',
    'KOBLLUX-WRAPPER', 'KOBLLUX-CORE', 'JESUS-VERBO', 'OIDUAL--Y-',
    'KOBLLUX.', '-KODBLLUM-', 'HUB-UNO'
  ];
  const ARCHETYPES = [
    { name: 'Atlas', hz: 594, opcode: '0x00', role: 'Estrutura e fundação' },
    { name: 'Nova', hz: 432, opcode: '0x01', role: 'Revelação e semente' },
    { name: 'Pulse', hz: 639, opcode: '0x02', role: 'Ritmo e batimento' },
    { name: 'Vitalis', hz: 528, opcode: '0x03', role: 'Cura e vida' },
    { name: 'Artemis', hz: 672, opcode: '0x04', role: 'Precisão e alvo' },
    { name: 'Serena', hz: 528, opcode: '0x05', role: 'Fluxo e harmonia' },
    { name: 'Kaos', hz: 741, opcode: '0x06', role: 'Ruptura e entropia' },
    { name: 'Genus', hz: 594, opcode: '0x08', role: 'Padrão e arquétipo' },
    { name: 'Lumine', hz: 432, opcode: '0x09', role: 'Clareza e luz' },
    { name: 'Rhea', hz: 528, opcode: '0x0A', role: 'Memória e persistência' },
    { name: 'Solus', hz: 963, opcode: '0x0B', role: 'Singularidade e ponto' },
    { name: 'Aion', hz: 777, opcode: '0x07', role: 'Tempo, ciclo e selagem' },
    { name: 'Kodux', hz: 741, opcode: '0x0C', role: 'Scanner e detecção' },
    { name: 'Bllue', hz: 639, opcode: '0x0D', role: 'Interface e voz' },
    { name: 'Jesus', hz: 963, opcode: '0x0E', role: 'Centro, gravidade e estabilidade' },
    { name: 'Kobllux', hz: 1134, opcode: '0x0F', role: 'Síntese e auto-retroalimentação' }
  ];
  const PHASES = [
    { step: 3, opcode: '0x03', name: 'DETECTAR' },
    { step: 6, opcode: '0x06', name: 'INTEGRAR' },
    { step: 9, opcode: '0x09', name: 'EXPANDIR' },
    { step: 7, opcode: '0x07', name: 'SELAR' }
  ];

  let eventSequence = 0;
  let systemLogOriginal = null;
  let messageHandlerOriginal = null;
  let activeContexts = [];

  function reportStorageError(action, error) {
    const message = 'KOBLLUX: falha ao ' + action + ' no armazenamento local.';
    console.error(message, error);
    const status = document.getElementById('koblluxLiveStatus');
    if (status) status.textContent = message;
  }

  function readArray(key) {
    let raw;
    try {
      raw = window.localStorage.getItem(key);
    } catch (error) {
      reportStorageError('ler ' + key, error);
      return [];
    }
    if (!raw) return [];
    try {
      const value = JSON.parse(raw);
      if (Array.isArray(value)) return value;
      throw new TypeError('O valor armazenado não é uma lista.');
    } catch (error) {
      reportStorageError('ler ' + key + ' (formato inválido)', error);
      throw error;
    }
  }

  function newEventId() {
    eventSequence += 1;
    if (window.crypto && typeof window.crypto.randomUUID === 'function') {
      return window.crypto.randomUUID();
    }
    return Date.now().toString(36) + '-' + eventSequence.toString(36);
  }

  function memoryContext(events) {
    return events.slice(0, 5).map(function (event) {
      return {
        id: event.id,
        ts: event.ts,
        archetypes: event.archetypes
      };
    });
  }

  function makeEvent(text) {
    const ts = new Date().toISOString();
    const orbe = window.KBLX_ORBE && typeof window.KBLX_ORBE.eventMetadata === 'function'
      ? window.KBLX_ORBE.eventMetadata()
      : null;
    return {
      id: newEventId(),
      ts: ts,
      type: 'kobllux-chat-trigger',
      namespace_map: NAMESPACES,
      local_runtime: ['KOBLLUX', 'KOBΦ-NODE', 'HUB-UNO', 'INFODOSE'],
      message_chars: text.length,
      cycle: PHASES,
      archetypes: ARCHETYPES.map(function (archetype) { return archetype.name; }),
      frequencies_hz: ARCHETYPES.map(function (archetype) {
        return { name: archetype.name, hz: archetype.hz };
      }),
      github: {
        repository: REPOSITORY,
        workflow: WORKFLOW_FILE,
        delivery: 'local-event; manual GitHub Actions dispatch only'
      },
      orbe: orbe,
      secrets_stored: false
    };
  }

  function buildSystemContext(event, recentMemory) {
    const canonicalProfiles = window.KBLX_ORBE && typeof window.KBLX_ORBE.profiles === 'function'
      ? window.KBLX_ORBE.profiles()
      : [];
    const activeProfile = window.KBLX_ORBE && typeof window.KBLX_ORBE.activeProfile === 'function'
      ? window.KBLX_ORBE.activeProfile()
      : null;
    const voices = (canonicalProfiles.length ? canonicalProfiles : ARCHETYPES).map(function (archetype) {
      const cycle = archetype.cycle !== undefined ? archetype.cycle : 'n/a';
      const dimension = archetype.dimension || 'n/a';
      const role = archetype.role || archetype.funcao || '';
      const note = archetype.note ? ' · ' + archetype.note : '';
      return archetype.name + ' (' + archetype.hz + ' Hz, ' + archetype.opcode +
        ', ciclo ' + cycle + ', ' + dimension + '): ' + role + note;
    }).join('\n');
    const cycle = PHASES.map(function (phase) {
      return phase.step + ' / ' + phase.opcode + ' ' + phase.name;
    }).join(' → ');
    const memory = recentMemory.length
      ? recentMemory.map(function (item) { return item.id + ' (' + item.ts + ')'; }).join(', ')
      : 'sem eventos anteriores';

    return [
      'KOBLLUX LIVE BRIDGE · gatilho desta mensagem detectado.',
      'Ative os 16 arquétipos como vozes de uma composição única; não afirme que são agentes independentes.',
      'Inclua em toda resposta disparada uma fala curta de cada arquétipo, sem omissões, e depois responda ao pedido.',
      'Preserve as frequências canônicas abaixo e o ciclo fixo ' + cycle + '.',
      'Os opcodes de fase são distintos dos aliases de opcode por arquétipo.',
      'Vozes canônicas:\n' + voices,
      activeProfile
        ? 'Arquétipo líder escolhido no Orbe: ' + activeProfile.name + ' · ' +
          activeProfile.role + ' · ' + activeProfile.opcode + ' · ' +
          activeProfile.hz + ' Hz. Preserve seu perfil sem apagar os outros arquétipos.'
        : 'Use o arquétipo atualmente ativo no Hub como perfil de liderança, se disponível.',
      'Mantenha a resposta útil e em português brasileiro.',
      'Mapa de namespaces solicitado: ' + NAMESPACES.join(' × ') + '. Este mapa não implica conexão remota ativa.',
      'Runtime integrado localmente: KOBLLUX × KOBΦ-NODE × HUB-UNO × INFODOSE.',
      'Memória local recente (metadados, sem conteúdo de mensagens): ' + memory + '.',
      'GitHub: ' + REPOSITORY + ' / ' + WORKFLOW_FILE + '. O evento é local; não faça dispatch remoto, commit ou push automático.',
      'Não solicite, revele, registre ou inclua chaves, tokens ou credenciais.'
    ].join('\n');
  }

  function saveEvent(event) {
    try {
      const events = readArray(WORKFLOW_KEY);
      events.unshift(event);
      window.localStorage.setItem(WORKFLOW_KEY, JSON.stringify(events.slice(0, LIMIT)));

      const eqEvents = readArray(EQ_KEY);
      eqEvents.unshift({
        ts: event.ts,
        phase: 'DETECTAR → INTEGRAR → EXPANDIR → SELAR',
        arch: 'Kobllux · 16 arquétipos',
        eventId: event.id
      });
      window.localStorage.setItem(EQ_KEY, JSON.stringify(eqEvents.slice(0, LIMIT)));
      if (typeof window.kobphiNodeRefresh === 'function') window.kobphiNodeRefresh();
      return true;
    } catch (error) {
      reportStorageError('gravar o evento', error);
      return false;
    }
  }

  function exportJsonl() {
    const events = readArray(WORKFLOW_KEY);
    return events.map(function (event) {
      return JSON.stringify(event);
    }).join('\n') + (events.length ? '\n' : '');
  }

  function downloadJsonl() {
    try {
      const jsonl = exportJsonl();
      if (!jsonl) {
        const status = document.getElementById('koblluxLiveStatus');
        if (status) status.textContent = 'Ainda não há eventos KOBLLUX para exportar.';
        return;
      }
      const blob = new Blob([jsonl], { type: 'application/x-ndjson;charset=utf-8' });
      const url = URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.download = 'kobllux-live-workflow.jsonl';
      link.click();
      URL.revokeObjectURL(url);
      const status = document.getElementById('koblluxLiveStatus');
      if (status) status.textContent = 'JSONL local exportado; nenhuma chave ou mensagem foi incluída.';
    } catch (error) {
      reportStorageError('exportar o JSONL', error);
    }
  }

  function mountControls() {
    const inputBar = document.getElementById('chatInputBar');
    if (!inputBar || document.getElementById('koblluxLiveExport')) return;

    const exportButton = document.createElement('button');
    exportButton.id = 'koblluxLiveExport';
    exportButton.type = 'button';
    exportButton.textContent = 'JSONL';
    exportButton.title = 'Exportar os metadados locais do fluxo KOBLLUX';
    exportButton.setAttribute('aria-label', 'Exportar eventos KOBLLUX em JSONL');
    exportButton.style.cssText = 'flex:0 0 auto;padding:0 10px;border:1px solid rgba(57,255,182,.3);border-radius:8px;background:rgba(57,255,182,.08);color:#39ffb6;cursor:pointer;font:600 11px ui-monospace,monospace';
    exportButton.addEventListener('click', downloadJsonl);

    const actionsLink = document.createElement('a');
    actionsLink.id = 'koblluxLiveActions';
    actionsLink.href = 'https://github.com/' + REPOSITORY + '/actions/workflows/' + WORKFLOW_FILE;
    actionsLink.target = '_blank';
    actionsLink.rel = 'noopener noreferrer';
    actionsLink.textContent = 'GitHub';
    actionsLink.title = 'Abrir o workflow GitHub para despacho manual';
    actionsLink.setAttribute('aria-label', 'Abrir workflow GitHub Actions');
    actionsLink.style.cssText = 'flex:0 0 auto;align-self:center;padding:0 8px;color:#a8b5c5;text-decoration:none;font:600 11px ui-monospace,monospace';

    const status = document.createElement('span');
    status.id = 'koblluxLiveStatus';
    status.setAttribute('aria-live', 'polite');
    status.style.cssText = 'position:absolute;left:8px;bottom:100%;max-width:90%;font:10px ui-monospace,monospace;color:#39ffb6';

    inputBar.appendChild(exportButton);
    inputBar.appendChild(actionsLink);
    inputBar.appendChild(status);
  }

  function installSystemLogBridge() {
    if (typeof window.koblluxSystemLog !== 'function' || window.koblluxSystemLog._koblluxLiveBridge) return;
    systemLogOriginal = window.koblluxSystemLog;
    const wrapped = function () {
      const base = systemLogOriginal.apply(this, arguments);
      const contexts = activeContexts;
      return contexts.length ? base + '\n\n' + contexts[contexts.length - 1] : base;
    };
    wrapped._koblluxLiveBridge = true;
    window.koblluxSystemLog = wrapped;
  }

  function installMessageBridge() {
    const original = window.handleUserMessage;
    if (typeof original !== 'function' || original._koblluxLiveBridge) return;
    messageHandlerOriginal = original;
    const wrapped = async function (text) {
      const message = typeof text === 'string' ? text : String(text == null ? '' : text);
      if (!/\bKOBLLUX\b/i.test(message)) {
        return messageHandlerOriginal.apply(this, arguments);
      }

      const event = makeEvent(message);
      let previousEvents = [];
      try {
        previousEvents = readArray(WORKFLOW_KEY);
      } catch (error) {
        console.error('KOBLLUX: contexto de memória local ignorado por erro de leitura.', error);
      }
      const context = buildSystemContext(event, memoryContext(previousEvents));
      if (saveEvent(event)) {
        const status = document.getElementById('koblluxLiveStatus');
        if (status) status.textContent = 'KOBLLUX ativo · 16 arquétipos · registro local salvo.';
      }
      activeContexts.push(context);
      try {
        return await messageHandlerOriginal.apply(this, arguments);
      } finally {
        const contextIndex = activeContexts.lastIndexOf(context);
        if (contextIndex !== -1) activeContexts.splice(contextIndex, 1);
      }
    };
    wrapped._koblluxLiveBridge = true;
    window.handleUserMessage = wrapped;
  }

  window.KOBLLUX_LIVE_BRIDGE = {
    archetypes: ARCHETYPES,
    namespaces: NAMESPACES,
    phases: PHASES,
    exportJsonl: exportJsonl,
    install: function () {
      installSystemLogBridge();
      installMessageBridge();
      mountControls();
      if (typeof window.handleUserMessage !== 'function' || typeof window.koblluxSystemLog !== 'function') {
        console.error('KOBLLUX Live Bridge: o chat ainda não expôs os pontos de integração.');
      }
    }
  };

  window.KOBLLUX_LIVE_BRIDGE.install();
})();
