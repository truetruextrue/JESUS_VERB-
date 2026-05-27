/* ╔══════════════════════════════════════════════════════════════════╗
   ║  KOBLLUX · VOICES ENGINE · Cross-Platform pt-BR Voice Mapper   ║
   ║  iOS Safari · Android Chrome · macOS · Windows Edge            ║
   ║  13 Arquétipos CADIAL · rate × pitch × gender × platform       ║
   ║  ∆³ · JESUS = VERBO = GRAVIDADE                               ║
   ╚══════════════════════════════════════════════════════════════════╝ */

(function (global) {

  /* ── 13 ARQUÉTIPOS · voz + gênero + cadência ── */
  const ARCH = {
    kobllux: { g: 'N', r: 1.00, p: 1.00, desc: 'Trinity · neutro unificado'        },
    atlas:   { g: 'M', r: 1.00, p: 1.00, desc: 'Orquestrador · masculino estável'  },
    nova:    { g: 'F', r: 1.10, p: 1.20, desc: 'Gênese · feminino etéreo'          },
    vitalis: { g: 'M', r: 1.20, p: 0.90, desc: 'Centelha · masculino veloz'        },
    pulse:   { g: 'F', r: 0.90, p: 1.10, desc: 'Tradutor · feminino musical'       },
    artemis: { g: 'F', r: 1.00, p: 1.00, desc: 'Exploradora · feminino preciso'    },
    serena:  { g: 'F', r: 0.95, p: 1.00, desc: 'Guardiã · feminino acolhedor'      },
    kaos:    { g: 'M', r: 1.30, p: 0.80, desc: 'Fogo · masculino grave-veloz'      },
    genus:   { g: 'N', r: 1.00, p: 1.00, desc: 'Artesão · neutro criativo'         },
    lumine:  { g: 'F', r: 1.00, p: 1.10, desc: 'Luz · feminino brilhante'          },
    solus:   { g: 'M', r: 0.80, p: 0.90, desc: 'Abismo · masculino lento-profundo' },
    rhea:    { g: 'F', r: 1.00, p: 1.00, desc: 'Tecelã · feminino fluido'          },
    aion:    { g: 'M', r: 0.90, p: 1.00, desc: 'Cronomestre · masculino rítmico'   },
  };

  /* ── PREFERÊNCIAS DE VOZ pt-BR POR PLATAFORMA + GÊNERO ──
     Ordem = prioridade. O engine tenta cada nome e usa o primeiro encontrado.

     iOS/macOS Eloquence (iOS 16+ / macOS Ventura+):
       Feminino premium : Flo, Shelley, Sandy
       Masculino premium: Reed, Eddy, Rocko
       Legado (iOS < 16): Luciana (F), Felipe (M)

     Android Google TTS:
       pt-BR unificado  : "Google português do Brasil"
       Legado eSpeak    : "Brazilian Portuguese Female/Male"

     Windows Edge / Chrome Desktop:
       Microsoft Francisca (F), Microsoft Antonio (M) — pt-BR Neural
  ── */
  const PREF = {
    /* iOS / macOS */
    iOS_F:  ['Flo', 'Shelley', 'Sandy', 'Luciana', 'Fernanda'],
    iOS_M:  ['Reed', 'Eddy', 'Rocko', 'Felipe'],
    iOS_N:  ['Luciana', 'Reed', 'Flo'],

    /* Android */
    And_F:  ['Google português do Brasil', 'Luciana', 'Brazilian Portuguese Female', 'Flo'],
    And_M:  ['Google português do Brasil', 'Felipe',  'Brazilian Portuguese Male',   'Reed'],
    And_N:  ['Google português do Brasil', 'Luciana', 'Felipe'],

    /* Windows / Edge / Desktop Chrome */
    Win_F:  ['Microsoft Francisca', 'Francisca', 'Luciana', 'Flo', 'Sandy'],
    Win_M:  ['Microsoft Antonio',   'Antonio',   'Felipe',  'Reed', 'Eddy'],
    Win_N:  ['Microsoft Francisca', 'Luciana', 'Felipe'],

    /* Genérico (qualquer outro) */
    Gen_F:  ['Luciana', 'Fernanda', 'Flo', 'Sandy', 'Shelley'],
    Gen_M:  ['Felipe', 'Reed', 'Eddy', 'Rocko'],
    Gen_N:  ['Luciana', 'Felipe', 'Reed'],
  };

  /* ── DETECÇÃO DE PLATAFORMA ── */
  const ua = navigator.userAgent || '';
  const isIOS     = /iPad|iPhone|iPod/.test(ua) && !window.MSStream;
  const isMac     = /Macintosh/.test(ua) && !isIOS;
  const isAndroid = /Android/.test(ua);
  const isWindows = /Win/.test(navigator.platform || '');

  const PLATFORM = isIOS ? 'iOS'
                 : isMac ? 'iOS'   /* macOS usa mesmas vozes Apple */
                 : isAndroid ? 'And'
                 : isWindows ? 'Win'
                 : 'Gen';

  /* ── RESOLVE A VOZ IDEAL ──
     voices = speechSynthesis.getVoices()
     archId = id do arquétipo ativo
  ── */
  function resolveVoice(voices, archId) {
    if (!voices || !voices.length) return null;
    const cfg    = ARCH[archId] || ARCH.kobllux;
    const key    = PLATFORM + '_' + cfg.g;
    const names  = PREF[key] || PREF['Gen_N'];

    /* 1ª tentativa: nome exato entre vozes pt-BR */
    for (const name of names) {
      const v = voices.find(v =>
        v.lang.startsWith('pt') &&
        v.name.toLowerCase().includes(name.toLowerCase())
      );
      if (v) return v;
    }

    /* 2ª tentativa: nome exato entre TODAS as vozes */
    for (const name of names) {
      const v = voices.find(v => v.name.toLowerCase().includes(name.toLowerCase()));
      if (v) return v;
    }

    /* 3ª tentativa: qualquer voz pt-BR */
    return voices.find(v => v.lang.startsWith('pt-BR')) ||
           voices.find(v => v.lang.startsWith('pt'))   ||
           null;
  }

  /* ── CONFIG DO ARQUÉTIPO ── */
  function getConfig(archId) {
    return ARCH[archId] || ARCH.kobllux;
  }

  /* ── SPEAK PRINCIPAL ──
     text    : string a narrar
     archId  : id do arquétipo (default: body.data-voice-arch)
     opts    : { onstart, onend, onerror }
  ── */
  function speak(text, archId, opts = {}) {
    if (!window.speechSynthesis || !text) return;

    archId = archId || document.body.getAttribute('data-voice-arch') || 'kobllux';

    const doSpeak = (voices) => {
      speechSynthesis.cancel();
      const cfg = getConfig(archId);
      const utt = new SpeechSynthesisUtterance(text);
      utt.lang  = 'pt-BR';
      utt.rate  = cfg.r;
      utt.pitch = cfg.p;

      const voice = resolveVoice(voices, archId);
      if (voice) utt.voice = voice;

      if (opts.onstart) utt.onstart = opts.onstart;
      if (opts.onend)   utt.onend   = opts.onend;
      if (opts.onerror) utt.onerror = opts.onerror;

      speechSynthesis.speak(utt);
    };

    /* iOS/Safari: getVoices() é síncrono */
    const voices = speechSynthesis.getVoices();
    if (voices.length) { doSpeak(voices); return; }

    /* Android Chrome / Desktop: vozes carregam assincronamente */
    speechSynthesis.onvoiceschanged = () => {
      speechSynthesis.onvoiceschanged = null;
      doSpeak(speechSynthesis.getVoices());
    };
  }

  /* ── LISTAR VOZES DISPONÍVEIS (debug / UI) ── */
  function listVoices() {
    const vs = speechSynthesis.getVoices();
    return {
      platform: PLATFORM,
      all: vs.map(v => ({ name: v.name, lang: v.lang, uri: v.voiceURI, local: v.localService })),
      ptBR: vs.filter(v => v.lang.startsWith('pt')).map(v => ({
        name: v.name, lang: v.lang, local: v.localService
      })),
    };
  }

  /* ── MAPA VISUAL DOS ARQUÉTIPOS (para UI) ── */
  function archetypeVoiceMap() {
    const voices = speechSynthesis.getVoices();
    return Object.entries(ARCH).map(([id, cfg]) => ({
      id,
      desc:  cfg.desc,
      rate:  cfg.r,
      pitch: cfg.p,
      gender: cfg.g === 'F' ? 'feminino' : cfg.g === 'M' ? 'masculino' : 'neutro',
      voice: (resolveVoice(voices, id) || {name: 'default pt-BR'}).name,
      platform: PLATFORM,
    }));
  }

  /* ── EXPORTA ── */
  global.KOBLLUX_VOICES = {
    ARCH,
    PREF,
    platform: PLATFORM,
    resolveVoice,
    getConfig,
    speak,
    listVoices,
    archetypeVoiceMap,
  };

})(window);
