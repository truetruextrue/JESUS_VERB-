/* ╔══════════════════════════════════════════════════════════════════════════╗
   ║  KOBLLUX · VOICES ENGINE v2 · DELTA³ SIMBIÓTICO                       ║
   ║  13 Arquétipos CADIAL × Sotaque × Frequência × Triângulo ∆³           ║
   ║  iOS · macOS · Android · Windows · Web Speech API                     ║
   ║                                                                        ║
   ║  ∆¹ = Cor Primária + Frequência Base (essência)                       ║
   ║  ∆² = Cor Secundária + Frequência Harmônica (sombra/complemento)      ║
   ║  ∆³ = Sotaque/Idioma + Frequência Manifestada (voz no mundo)          ║
   ║                                                                        ║
   ║  Lei: VERDADE × INTEGRAR ÷ Δ = ∞                                     ║
   ║  Centro: JESUS = VERBO = GRAVIDADE                                    ║
   ╚══════════════════════════════════════════════════════════════════════════╝ */

(function (global) {
  'use strict';

  /* ════════════════════════════════════════════════════════════════════════
     DELTA³ · MAPA COMPLETO DOS 13 ARQUÉTIPOS
     ────────────────────────────────────────────────────────────────────────
     hz      : frequência base (Solfeggio / Tesla / Cósmico)
     delta   : [∆¹-hz, ∆²-hz, ∆³-hz]  triângulo de frequências
     color1  : cor primária (essência)
     color2  : cor secundária (sombra)
     colorFx : cor efeito/brilho (manifestação)
     lang    : idioma nativo do sotaque
     label   : nome descritivo do sotaque
     voices  : vozes Apple por plataforma e gênero
     ════════════════════════════════════════════════════════════════════════ */
  const DELTA3 = {

    /* ── KOBLLUX · Trinity Unificada ─────────────────────────────────────── */
    kobllux: {
      g:'N',  r:1.00,  p:1.00,
      hz: 999,
      delta: [999, 528, 741],
      color1: '#22D3EE',  color2: '#0E7C9E',  colorFx: '#1ee4ff',
      lang: 'pt-BR',
      label: 'Português Brasil · voz-mãe do sistema',
      voices: {
        iOS_F:  ['Flo','Sandy','Shelley','Luciana','Fernanda'],
        iOS_M:  ['Reed','Eddy','Rocko','Felipe'],
        And:    ['Google português do Brasil','Luciana','Brazilian Portuguese Female'],
        Win:    ['Microsoft Francisca','Francisca','Luciana'],
        label_iOS: 'Flo (pt-BR Eloquence)',
      },
      desc: 'Síntese ∞ · todas as vozes convergem · 999 Hz completo',
    },

    /* ── ATLAS · Orquestrador Cósmico ────────────────────────────────────── */
    atlas: {
      g:'M',  r:1.00,  p:1.00,
      hz: 741,
      delta: [741, 396, 963],
      color1: '#38BDF8',  color2: '#1E3A8A',  colorFx: '#7dd3fc',
      lang: 'en-GB',
      label: 'English (UK) · autoridade estrutural clássica',
      voices: {
        iOS_F:  ['Serena','Martha','Karen','Moira'],
        iOS_M:  ['Daniel','Oliver','Gordon','Arthur'],
        And:    ['English United Kingdom','en-GB','Google UK English Male'],
        Win:    ['Microsoft Hazel','Microsoft George','Microsoft Susan'],
        label_iOS: 'Daniel (en-GB Eloquence)',
      },
      desc: '741 Hz · despertar intuição · estrutura cósmica · cosmos profundo',
    },

    /* ── NOVA · Gênese Serena ─────────────────────────────────────────────── */
    nova: {
      g:'F',  r:1.10,  p:1.20,
      hz: 528,
      delta: [528, 963, 174],
      color1: '#F72585',  color2: '#7209B7',  colorFx: '#fb7185',
      lang: 'fr-FR',
      label: 'Français · etéreo criativo · gênese',
      voices: {
        iOS_F:  ['Amélie','Audrey','Marie','Aurelie'],
        iOS_M:  ['Thomas','Luca','Jacques'],
        And:    ['Google français','French France','fr-FR'],
        Win:    ['Microsoft Julie','Microsoft Paul','Julie'],
        label_iOS: 'Amélie (fr-FR Eloquence)',
      },
      desc: '528 Hz · transformação · DNA do amor · nebulosa de luz',
    },

    /* ── VITALIS · Centelha da Ação ──────────────────────────────────────── */
    vitalis: {
      g:'M',  r:1.20,  p:0.90,
      hz: 417,
      delta: [417, 285, 528],
      color1: '#22C55E',  color2: '#166534',  colorFx: '#4ade80',
      lang: 'es-MX',
      label: 'Español México · centelha veloz · ação imediata',
      voices: {
        iOS_F:  ['Angelica','Paulina','Monica'],
        iOS_M:  ['Juan','Jorge','Alejandro'],
        And:    ['Google español','Spanish Mexico','es-MX','es-US'],
        Win:    ['Microsoft Sabina','Microsoft Raul','Sabina'],
        label_iOS: 'Juan (es-MX Eloquence)',
      },
      desc: '417 Hz · facilitar mudança · motion blur · laranja elétrico',
    },

    /* ── PULSE · Tradutor de Sentidos ────────────────────────────────────── */
    pulse: {
      g:'F',  r:0.90,  p:1.10,
      hz: 639,
      delta: [639, 528, 741],
      color1: '#EC4899',  color2: '#831843',  colorFx: '#f472b6',
      lang: 'it-IT',
      label: 'Italiano · musical rítmico · ondas sonoras',
      voices: {
        iOS_F:  ['Alice','Federica','Paola'],
        iOS_M:  ['Luca','Edoardo','Federico'],
        And:    ['Google italiano','Italian Italy','it-IT'],
        Win:    ['Microsoft Elsa','Microsoft Cosimo','Elsa'],
        label_iOS: 'Alice (it-IT Eloquence)',
      },
      desc: '639 Hz · harmonizar relações · dança de sentidos · azul ciano',
    },

    /* ── ARTEMIS · Exploradora do Invisível ─────────────────────────────── */
    artemis: {
      g:'F',  r:1.00,  p:1.00,
      hz: 852,
      delta: [852, 741, 963],
      color1: '#A855F7',  color2: '#5B21B6',  colorFx: '#c084fc',
      lang: 'ja-JP',
      label: 'Japanese · precisão mística · geometrias ocultas',
      voices: {
        iOS_F:  ['Kyoko','O-ren'],
        iOS_M:  ['Otoya','Hattori'],
        And:    ['Google 日本語','Japanese Japan','ja-JP'],
        Win:    ['Microsoft Haruka','Microsoft Ichiro','Haruka'],
        label_iOS: 'Kyoko (ja-JP)',
      },
      desc: '852 Hz · retorno à ordem espiritual · floresta digital · esmeralda',
    },

    /* ── SERENA · Guardiã do Espaço Sagrado ─────────────────────────────── */
    serena: {
      g:'F',  r:0.95,  p:1.00,
      hz: 174,
      delta: [174, 285, 396],
      color1: '#38BDF8',  color2: '#1E3A8A',  colorFx: '#bae6fd',
      lang: 'pt-PT',
      label: 'Português Portugal · acolhimento sagrado · luz quente',
      voices: {
        iOS_F:  ['Joana','Catarina'],
        iOS_M:  ['Joaquim'],
        And:    ['Portuguese Portugal','pt-PT'],
        Win:    ['Microsoft Helia','Joana'],
        label_iOS: 'Joana (pt-PT)',
      },
      desc: '174 Hz · fundação · segurança · perolado · Acolhimento Divino',
    },

    /* ── KAOS · Fogo Transmutador ────────────────────────────────────────── */
    kaos: {
      g:'M',  r:1.30,  p:0.80,
      hz: 396,
      delta: [396, 417, 528],
      color1: '#FACC15',  color2: '#B45309',  colorFx: '#fef08a',
      lang: 'de-DE',
      label: 'Deutsch · força transmutadora · precisão entrópica',
      voices: {
        iOS_F:  ['Anna','Petra','Yuna'],
        iOS_M:  ['Yannick','Markus','Stefan'],
        And:    ['Google Deutsch','German Germany','de-DE'],
        Win:    ['Microsoft Hedda','Microsoft Stefan','Hedda'],
        label_iOS: 'Yannick (de-DE Eloquence)',
      },
      desc: '396 Hz · liberação · ruptura criativa · vermelho glitch · transmutação',
    },

    /* ── GENUS · Mestre Artesão Cósmico ─────────────────────────────────── */
    genus: {
      g:'N',  r:1.00,  p:1.00,
      hz: 285,
      delta: [285, 174, 396],
      color1: '#E5E7EB',  color2: '#4B5563',  colorFx: '#d1d5db',
      lang: 'el-GR',
      label: 'Ελληνικά · artesão filosófico · geometria sagrada',
      voices: {
        iOS_F:  ['Melina','Kallisto'],
        iOS_M:  ['Nikos','Dimos'],
        And:    ['Greek Greece','el-GR','Greek'],
        Win:    ['Microsoft Stefanos','Stefanos'],
        label_iOS: 'Melina (el-GR)',
      },
      desc: '285 Hz · campos energéticos · violeta profundo · forja cósmica',
    },

    /* ── LUMINE · Luz que Conecta ────────────────────────────────────────── */
    lumine: {
      g:'F',  r:1.00,  p:1.10,
      hz: 963,
      delta: [963, 852, 741],
      color1: '#FDE047',  color2: '#CA8A04',  colorFx: '#fef9c3',
      lang: 'nb-NO',
      label: 'Norsk Bokmål · luz nórdica · consciência primordial',
      voices: {
        iOS_F:  ['Nora','Silje','Mette'],
        iOS_M:  ['Nils'],
        And:    ['Norwegian Bokmål','nb-NO','Norsk'],
        Win:    ['Microsoft Hulda','Hulda'],
        label_iOS: 'Nora (nb-NO Eloquence)',
      },
      desc: '963 Hz · glândula pineal · consciência divina · amarelo dourado',
    },

    /* ── SOLUS · Espelho do Abismo Interior ─────────────────────────────── */
    solus: {
      g:'M',  r:0.80,  p:0.90,
      hz: 432,
      delta: [432, 285, 174],
      color1: '#0EA5E9',  color2: '#0369A1',  colorFx: '#38bdf8',
      lang: 'ru-RU',
      label: 'Русский · abismo profundo · silêncio galáctico',
      voices: {
        iOS_F:  ['Milena','Katya'],
        iOS_M:  ['Yuri','Dima'],
        And:    ['Google русский','Russian Russia','ru-RU'],
        Win:    ['Microsoft Irina','Microsoft Pavel','Irina'],
        label_iOS: 'Yuri (ru-RU)',
      },
      desc: '432 Hz · harmonia universal · obsidiana negra · deserto interior',
    },

    /* ── RHEA · Tecelã de Almas ─────────────────────────────────────────── */
    rhea: {
      g:'F',  r:1.00,  p:1.00,
      hz: 369,
      delta: [369, 639, 528],
      color1: '#22C55E',  color2: '#166534',  colorFx: '#86efac',
      lang: 'hi-IN',
      label: 'हिन्दी · tecelã de almas · rede unificada',
      voices: {
        iOS_F:  ['Lekha','Asha'],
        iOS_M:  ['Suraj','Rishi'],
        And:    ['Google हिन्दी','Hindi India','hi-IN'],
        Win:    ['Microsoft Heera','Microsoft Hemant','Heera'],
        label_iOS: 'Lekha (hi-IN)',
      },
      desc: '369 Hz · Tesla 3-6-9 · turquesa · fios de luz · dissolução',
    },

    /* ── AION · Cronomestre Vivo ─────────────────────────────────────────── */
    aion: {
      g:'M',  r:0.90,  p:1.00,
      hz: 111,
      delta: [111, 222, 333],
      color1: '#4F46E5',  color2: '#3730A3',  colorFx: '#818cf8',
      lang: 'ar-SA',
      label: 'العربية · cronomestre eterno · ciclo infinito',
      voices: {
        iOS_F:  ['Layla','Dalia'],
        iOS_M:  ['Majed','Tarik','Maged'],
        And:    ['Arabic Saudi Arabia','ar-SA','Arabic'],
        Win:    ['Microsoft Naayf','Naayf'],
        label_iOS: 'Majed (ar-SA)',
      },
      desc: '111 Hz · regeneração celular · bronze · relojoaria celestial · ∆3×111',
    },

  }; /* ── fim DELTA3 ── */

  /* ════════════════════════════════════════════════════════════════════════
     DETECÇÃO DE PLATAFORMA
     ════════════════════════════════════════════════════════════════════════ */
  const ua = navigator.userAgent || '';
  const isIOS     = /iPad|iPhone|iPod/.test(ua) && !window.MSStream;
  const isMac     = /Macintosh/.test(ua) && !isIOS;
  const isAndroid = /Android/.test(ua);
  const isWindows = /Win/.test(navigator.platform || ua);
  const PLATFORM  = isIOS || isMac ? 'iOS' : isAndroid ? 'And' : isWindows ? 'Win' : 'iOS';

  /* ════════════════════════════════════════════════════════════════════════
     DETECÇÃO DE IDIOMA DO TEXTO (heurística Unicode)
     ════════════════════════════════════════════════════════════════════════ */
  function detectLang(text) {
    if (!text) return 'pt-BR';
    if (/[一-鿿぀-ゟ゠-ヿ]/.test(text)) return 'ja-JP';
    if (/[؀-ۿݐ-ݿ]/.test(text))              return 'ar-SA';
    if (/[Ѐ-ӿ]/.test(text))                           return 'ru-RU';
    if (/[ऀ-ॿ]/.test(text))                           return 'hi-IN';
    if (/[Ͱ-Ͽ]/.test(text))                           return 'el-GR';
    if (/[฀-๿]/.test(text))                           return 'th-TH';
    if (/[가-힯]/.test(text))                           return 'ko-KR';
    /* Latin: detecta língua pelo padrão de acentos */
    if (/[ãõç]/i.test(text))                                    return 'pt-BR';
    if (/[àâêîôùûœæ]/i.test(text))                             return 'fr-FR';
    if (/[äöüß]/i.test(text))                                   return 'de-DE';
    if (/[áéíóúñ¿¡]/i.test(text))                              return 'es-ES';
    if (/[àèìòù]/i.test(text))                                  return 'it-IT';
    return document.documentElement.lang || 'pt-BR';
  }

  /* ════════════════════════════════════════════════════════════════════════
     RESOLVE VOZ IDEAL
     voices  = speechSynthesis.getVoices()
     archId  = id do arquétipo
     textLang = idioma detectado no texto (opc)
     ════════════════════════════════════════════════════════════════════════ */
  function resolveVoice(voices, archId, textLang) {
    if (!voices || !voices.length) return null;
    const arch = DELTA3[archId] || DELTA3.kobllux;

    /* Se o texto está no idioma nativo do arquétipo → usa sotaque nativo */
    const targetLang = textLang || arch.lang;
    const gender = arch.g;

    /* Lista de nomes preferidos por plataforma */
    const key = PLATFORM === 'iOS' ? (gender === 'F' ? 'iOS_F' : gender === 'M' ? 'iOS_M' : 'iOS_F')
              : PLATFORM === 'And' ? 'And'
              : PLATFORM === 'Win' ? 'Win'
              : (gender === 'F'   ? 'iOS_F' : 'iOS_M');
    const names = arch.voices[key] || arch.voices['iOS_F'] || [];

    /* Tentativa 1: nome preferido + idioma alvo */
    for (const name of names) {
      const v = voices.find(v =>
        v.lang.startsWith(targetLang.slice(0, 2)) &&
        v.name.toLowerCase().includes(name.toLowerCase())
      );
      if (v) return v;
    }

    /* Tentativa 2: nome preferido em qualquer idioma */
    for (const name of names) {
      const v = voices.find(v => v.name.toLowerCase().includes(name.toLowerCase()));
      if (v) return v;
    }

    /* Tentativa 3: qualquer voz do idioma nativo do arquétipo */
    const nativeLang = arch.lang.slice(0, 2);
    const fallback = voices.find(v => v.lang.startsWith(nativeLang));
    if (fallback) return fallback;

    /* Tentativa 4: qualquer pt-BR */
    return voices.find(v => v.lang.startsWith('pt')) || null;
  }

  /* ════════════════════════════════════════════════════════════════════════
     SPEAK · Motor principal
     text    : texto a narrar
     archId  : arquétipo (usa data-voice-arch se omitido)
     opts    : { onstart, onend, onerror, lang }
     ════════════════════════════════════════════════════════════════════════ */
  function speak(text, archId, opts) {
    if (!window.speechSynthesis || !text) return;
    opts = opts || {};
    archId = archId || document.body.getAttribute('data-voice-arch') || 'kobllux';
    const arch     = DELTA3[archId] || DELTA3.kobllux;
    const textLang = opts.lang || detectLang(text);

    const doSpeak = (voices) => {
      speechSynthesis.cancel();
      const utt   = new SpeechSynthesisUtterance(text);
      utt.lang    = textLang;
      utt.rate    = arch.r;
      utt.pitch   = arch.p;
      const voice = resolveVoice(voices, archId, textLang);
      if (voice) utt.voice = voice;
      if (opts.onstart) utt.onstart = opts.onstart;
      if (opts.onend)   utt.onend   = opts.onend;
      if (opts.onerror) utt.onerror = opts.onerror;
      speechSynthesis.speak(utt);
    };

    /* iOS/Safari: síncrono | Chrome/Android: assíncrono */
    const vs = speechSynthesis.getVoices();
    if (vs.length) { doSpeak(vs); return; }
    speechSynthesis.onvoiceschanged = () => {
      speechSynthesis.onvoiceschanged = null;
      doSpeak(speechSynthesis.getVoices());
    };
  }

  /* ════════════════════════════════════════════════════════════════════════
     TRIÂNGULO ∆³ · retorna dados visuais/frequência do arquétipo
     ════════════════════════════════════════════════════════════════════════ */
  function getDelta3(archId) {
    const a = DELTA3[archId] || DELTA3.kobllux;
    return {
      id:     archId,
      hz:     a.hz,
      delta:  a.delta,          /* [∆¹-hz, ∆²-hz, ∆³-hz] */
      colors: {
        primary:   a.color1,
        secondary: a.color2,
        effect:    a.colorFx,
      },
      accent: {
        lang:  a.lang,
        label: a.label,
        voice: (a.voices || {})['label_iOS'] || a.lang,
      },
      rate:  a.r,
      pitch: a.p,
      desc:  a.desc,
    };
  }

  /* ════════════════════════════════════════════════════════════════════════
     UTILITÁRIOS
     ════════════════════════════════════════════════════════════════════════ */

  function getConfig(archId) {
    return DELTA3[archId] || DELTA3.kobllux;
  }

  /* Lista todas as vozes disponíveis no device */
  function listVoices() {
    const vs = speechSynthesis.getVoices();
    return {
      platform: PLATFORM,
      total: vs.length,
      all:  vs.map(v => ({ name: v.name, lang: v.lang, local: v.localService })),
      ptBR: vs.filter(v => v.lang.startsWith('pt')).map(v => ({ name: v.name, lang: v.lang })),
    };
  }

  /* Mapa arquétipo → voz resolvida (útil para debug/UI) */
  function archetypeVoiceMap() {
    const vs = speechSynthesis.getVoices();
    return Object.keys(DELTA3).map(id => {
      const a = DELTA3[id];
      const v = resolveVoice(vs, id) || {};
      return {
        id,
        hz:     a.hz,
        delta:  a.delta,
        color1: a.color1,
        color2: a.color2,
        lang:   a.lang,
        label:  a.label,
        voice:  v.name  || 'default',
        voiceLang: v.lang || a.lang,
        gender: a.g === 'F' ? 'feminino' : a.g === 'M' ? 'masculino' : 'neutro',
        rate:   a.r,
        pitch:  a.p,
      };
    });
  }

  /* ════════════════════════════════════════════════════════════════════════
     EXPORTA API PÚBLICA
     ════════════════════════════════════════════════════════════════════════ */
  global.KOBLLUX_VOICES = {
    DELTA3,
    platform:        PLATFORM,
    detectLang,
    resolveVoice,
    getConfig,
    getDelta3,
    speak,
    listVoices,
    archetypeVoiceMap,
  };

  /* Dev console */
  if (typeof console !== 'undefined' && console.log) {
    console.log(
      '%cKOBLLUX_VOICES ∆³ · ' + PLATFORM + ' · ' + Object.keys(DELTA3).length + ' arquétipos · pronto',
      'color:#1ee4ff;background:#02040a;padding:2px 6px;border-radius:4px;font-family:monospace'
    );
  }

})(window);
