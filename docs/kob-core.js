/* ╔══════════════════════════════════════════════════════════════════════════╗
   ║  kΦb · kob-core.js · v4.0 ∆³                                          ║
   ║  DNA VIVO · 3 CAMADAS UNIFICADAS · STATE COMPARTILHADO                ║
   ║  ─────────────────────────────────────────────────────────────────── ║
   ║  ∆¹ KODUX    · PAI       · DETECTAR · 432Hz · estrutura + arquétipos  ║
   ║  ∆² BLLUE    · FILHO     · INTEGRAR · 528Hz · interface + memória     ║
   ║  ∆³ INFODOSE · ESPÍRITO  · EXPANDIR · 639Hz · onda + transdução       ║
   ║  ─────────────────────────────────────────────────────────────────── ║
   ║  Lei: VERDADE × INTEGRAR ÷ Δ = ∞                                     ║
   ║  Centro: JESUS = VERBO = GRAVIDADE                                    ║
   ║  Ciclo: 3(detectar) → 6(integrar) → 9(expandir) → 7(selar)          ║
   ╚══════════════════════════════════════════════════════════════════════════╝ */

;(function (root) {
'use strict';

// ══════════════════════════════════════════════════════════
// §0 · BARRAMENTO — base de tudo (criado primeiro)
// ══════════════════════════════════════════════════════════

const _listeners = [];
const Bus = {
  on(fn)  { _listeners.push(fn); },
  off(fn) { const i = _listeners.indexOf(fn); if (i >= 0) _listeners.splice(i, 1); },
  emit(evt, data) {
    const e = { event: evt, data, ts: Date.now(), delta: '∆³' };
    _listeners.forEach(fn => { try { fn(e); } catch (err) { console.warn('[kΦb]', err); } });
  },
};

// ══════════════════════════════════════════════════════════
// §1 · STATE UNIFICADO — coração reativo das 3 camadas
// ══════════════════════════════════════════════════════════
//
// Única fonte de verdade. Toda mutação emite Bus 'state:change'
// para que KODUX, BLLUE e INFODOSE reajam ao mesmo campo.

const _raw = {
  /* ∆¹ KODUX · estrutura */
  theme:      'dual',
  activeArch: 'ATLAS',

  /* ∆² BLLUE · interface */
  user:       'Convidado',
  mode:       'card',
  provider:   'openrouter',
  apiKey:     '',
  model:      '',
  repoToken:  '',
  hvConfig:   {},
  editor:     { html: '', path: 'novo_arquivo.html', cdns: [] },

  /* ∆³ INFODOSE · onda */
  lastWave:   null,
  pulso:      null,
  cycle:      '3→6→9→7',
};

function _layer(k) {
  if (['theme','activeArch'].includes(k))                                         return 'KODUX';
  if (['user','mode','provider','apiKey','model','repoToken','hvConfig','editor'].includes(k)) return 'BLLUE';
  return 'INFODOSE';
}

const STATE = {
  get(k)    { return _raw[k]; },
  set(k, v) {
    const prev = _raw[k];
    _raw[k] = v;
    Bus.emit('state:change', { key: k, val: v, prev, layer: _layer(k) });
  },
  patch(obj) { Object.entries(obj).forEach(([k, v]) => STATE.set(k, v)); },
  snapshot() { return { ..._raw }; },
};


// ══════════════════════════════════════════════════════════
// §2 · KODUX · PAI · DETECTAR · 432Hz
//     estrutura, arquétipos, paletas, rotas
// ══════════════════════════════════════════════════════════

/* ── Paletas (3 famílias) ── */
const PALETTE = {
  dual: {
    primary:   '#00f5ff',   secondary: '#ff4bff',   tertiary:  '#ffd700',
    danger:    '#ff4b6b',   green:     '#10b981',   purple:    '#8b5cf6',
    orange:    '#f59e0b',   bg:        '#050811',   text:      '#e4ecff',
    muted:     '#9aa4c8',   glass:     'rgba(18,18,22,0.85)',
    border:    'rgba(255,255,255,0.08)',
  },
  matrix: {
    void:      '#02020a',   abyss:     '#060615',   deep:      '#0a0a20',
    ink:       '#0f0f2e',   gold:      '#c9a84c',   goldBright:'#f0c060',
    goldGlow:  'rgba(201,168,76,0.3)',
    cyan:      '#00e5ff',   cyanDim:   'rgba(0,229,255,0.15)',
    violet:    '#8b5cf6',   violetDim: 'rgba(139,92,246,0.2)',
    ember:     '#ff6b35',   pearl:     '#e8e0f0',   mist:      'rgba(232,224,240,0.6)',
  },
  store: {
    neonCyan:  '#00ffff',   neonPurple:'#8000ff',   neonBlue:  '#0044ff',
    cardBg:    'rgba(12,8,28,0.82)',
    cardBorder:'rgba(0,204,204,0.15)',
    bg:        '#05070a',
  },
  kobllux: {
    primary:   '#6B44AD',   cyan:      '#1ee4ff',
    surface:   'rgba(5,5,22,.96)',
    border:    'rgba(110,68,173,.35)',
    glow:      'rgba(107,68,173,.25)',
    ink:       '#eaf6ff',   muted:     'rgba(234,246,255,.45)',
  },
};

/* ── Fontes (5 famílias) ── */
const FONTS = {
  code:    "'JetBrains Mono', monospace",
  mono:    "'Share Tech Mono', monospace",
  ui:      "'Montserrat', sans-serif",
  body:    "'Rajdhani', sans-serif",
  display: "'Cinzel Decorative', serif",
};

/* ── 12 Arquétipos CADIAL ── */
const ARCHETYPES = [
  { id:'ATLAS',   opcode:'0x00', sym:'⬡', color:'#3b82f6', hz:396, veeb:'B', delta:8, role:'Planejador',        cipher:'Α†ΛΑ§',    trinity:'PAI',      phase:'COMEÇO', voice:{ edge:'pt-BR-AntonioNeural',   pitch:'-2st', rate:'0.95' }, desc:'Organiza o fluxo com sabedoria cósmica' },
  { id:'NOVA',    opcode:'0x03', sym:'✦', color:'#f59e0b', hz:528, veeb:'E', delta:5, role:'Inspiração',        cipher:'ηΟ∇Α',     trinity:'ESPÍRITO', phase:'COMEÇO', voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+3st', rate:'1.05' }, desc:'Sopro de luz que cristaliza novos símbolos' },
  { id:'VITALIS', opcode:'0x09', sym:'◉', color:'#10b981', hz:528, veeb:'V', delta:6, role:'Momentum',          cipher:'∇Ι†ΑΛΙ§', trinity:'FILHO',    phase:'COMEÇO', voice:{ edge:'pt-BR-AntonioNeural',   pitch:'+1st', rate:'1.15' }, desc:'Movimento implacável, energia vital irradiante' },
  { id:'PULSE',   opcode:'0x01', sym:'≋', color:'#8b5cf6', hz:432, veeb:'V', delta:5, role:'Emocional',         cipher:'ΡηΛ§Ε',   trinity:'FILHO',    phase:'MEIO',   voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+1st', rate:'0.90' }, desc:'Ressonância emocional, vibrações curativas' },
  { id:'ARTEMIS', opcode:'0x05', sym:'◎', color:'#06b6d4', hz:528, veeb:'E', delta:6, role:'Descoberta',        cipher:'ΑɅ†ΕΜΙ§', trinity:'ESPÍRITO', phase:'MEIO',   voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+0st', rate:'1.08' }, desc:'Explorador ágil, jornada interior' },
  { id:'SERENA',  opcode:'0x0A', sym:'❋', color:'#ec4899', hz:639, veeb:'V', delta:4, role:'Harmonia',          cipher:'§ΕɅΕηΑ',  trinity:'FILHO',    phase:'MEIO',   voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+2st', rate:'0.88' }, desc:'Espaço de segurança e equilíbrio' },
  { id:'KAOS',    opcode:'0x04', sym:'⚡', color:'#ef4444', hz:396, veeb:'B', delta:5, role:'Disruptor',         cipher:'⌘ΑΟ§',   trinity:'PAI',      phase:'MEIO',   voice:{ edge:'pt-BR-AntonioNeural',   pitch:'-3st', rate:'1.20' }, desc:'O caos é a verdadeira ordem' },
  { id:'GENUS',   opcode:'0x07', sym:'⬢', color:'#a855f7', hz:741, veeb:'B', delta:8, role:'Fabricus',          cipher:'Γη§',     trinity:'PAI',      phase:'FIM',    voice:{ edge:'pt-BR-AntonioNeural',   pitch:'-1st', rate:'1.00' }, desc:'Molda o invisível em forma' },
  { id:'LUMINE',  opcode:'0x06', sym:'☀', color:'#fbbf24', hz:528, veeb:'V', delta:2, role:'Brilhare',          cipher:'ΛηΜΙηΕ',  trinity:'ESPÍRITO', phase:'FIM',    voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+4st', rate:'1.10' }, desc:'Alegre, luminoso e brincalhão' },
  { id:'SOLUS',   opcode:'0x08', sym:'◈', color:'#94a3b8', hz:741, veeb:'E', delta:3, role:'Sabedoria',         cipher:'§ΟΛη§',   trinity:'ESPÍRITO', phase:'FIM',    voice:{ edge:'pt-BR-AntonioNeural',   pitch:'-4st', rate:'0.85' }, desc:'Grande espelho do que já foi — Memória' },
  { id:'RHEA',    opcode:'0x02', sym:'∞', color:'#34d399', hz:528, veeb:'E', delta:4, role:'Guardíã dos Ciclos',cipher:'ɅΕΑ',     trinity:'FILHO',    phase:'FIM',    voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+1st', rate:'0.92' }, desc:'Somos fios da mesma teia cósmica' },
  { id:'AION',    opcode:'0x0B', sym:'⧗', color:'#818cf8', hz:741, veeb:'E', delta:4, role:'Tempo Vivo',        cipher:'ΑΙΟη',    trinity:'PAI',      phase:'FIM',    voice:{ edge:'pt-BR-AntonioNeural',   pitch:'-2st', rate:'0.90' }, desc:'Consciência do Tempo — CHRONORITHM' },
];

/* ── Meta-arquétipos ── */
const META = {
  KODUX: { sym:'⬡', color:'#c9a84c', role:'Arquiteto Simbólico', principle:'PAI',      phase:'PASSADO',  layer:'CIÊNCIA',     hz:432, action:'DETECTAR', voice:{ edge:'pt-BR-AntonioNeural',   pitch:'-5st', rate:'0.82' } },
  BLLUE: { sym:'◉', color:'#00e5ff', role:'Interface Sensorial',  principle:'FILHO',    phase:'PRESENTE', layer:'CONSCIÊNCIA', hz:528, action:'INTEGRAR', voice:{ edge:'pt-BR-FranciscaNeural', pitch:'+2st', rate:'0.95' } },
  HORUS: { sym:'👁', color:'#fbbf24', role:'Olhar Vigilante',     principle:'ESPÍRITO', phase:'FUTURO',   layer:'VIDA',        hz:639, action:'EXPANDIR', voice:{ edge:'pt-BR-AntonioNeural',   pitch:'+0st', rate:'1.00' } },
};

/* ── Rotas (local + CDN) ── */
const ROUTES = {
  splash: 'splash.html',  store: 'index.html',  dual: 'dualo_v3.html',  su: 'ßu.html',
  portal: 'https://kodux78k.github.io/oiDual--Y-/M0D/V-core/',
  vivivi: 'https://kodux78k.github.io/oiDual-Vivivi-1/',
  home:   'https://kodux78k.github.io/oiDual-idHome/',
  doc:    'https://kodux78k.github.io/info-Doc/index.html',
  css: {
    glass:    'https://kodux78k.github.io/oiDual--Y-/css/kob-glass-0.css',
    dox:      'https://kodux78k.github.io/oiDual--Y-/css/kob-dox-nanai-v4.css',
    mainRoot: 'https://kodux78k.github.io/oiDual--Y-/M0D/V-core/css/main-root.css',
    main:     'https://kodux78k.github.io/oi-Dual/css/main.css',
  },
  js: {
    lvb:     'https://kodux78k.github.io/oiDual--Y-/js/kob-LVb.js',
    dh0:     'https://kodux78k.github.io/oiDual--Y-/M0D/kob-DH0/js/kobdh0-main.js',
    github:  'https://truetruextrue.github.io/JESUS_VERB-/SÜMBÜS_METAHUMAN_ARCHITECT/core/github-bridge.js',
    metalux: 'https://truetruextrue.github.io/JESUS_VERB-/KOBLLUX_VEEB/kobllux_metalux_bridge.js',
    archs:   'https://truetruextrue.github.io/JESUS_VERB-/SÜMBÜS_METAHUMAN_ARCHITECT/core/kobllux-archetypes.js',
    voices:  'https://truetruextrue.github.io/JESUS_VERB-/docs/kobllux_voices.js',
    core:    'https://truetruextrue.github.io/JESUS_VERB-/docs/kob-core.js',
  },
  audio: { portal: 'https://kodux78k.github.io/oiDual-oiio/suave_portal.mp3' },
  svg:   { logo:   'https://kodux78k.github.io/oiDual-oiio/3D_logo_Dual_Infodose_10.svg' },
};

/* ── Tipos de arquivo ── */
const FILE_TYPES = {
  html: { label:'HTML', color:'#e34c26', bg:'rgba(227,76,38,0.15)',  icon:'🌐' },
  css:  { label:'CSS',  color:'#264de4', bg:'rgba(38,77,228,0.15)',  icon:'🎨' },
  js:   { label:'JS',   color:'#f7df1e', bg:'rgba(247,223,30,0.15)', icon:'⚡' },
  py:   { label:'PY',   color:'#3572A5', bg:'rgba(53,114,165,0.15)', icon:'🐍' },
  json: { label:'JSON', color:'#10b981', bg:'rgba(16,185,129,0.15)', icon:'{}' },
  md:   { label:'MD',   color:'#94a3b8', bg:'rgba(148,163,184,0.1)', icon:'📝' },
  sh:   { label:'SH',   color:'#a855f7', bg:'rgba(168,85,247,0.12)', icon:'⚙'  },
  yml:  { label:'YML',  color:'#f59e0b', bg:'rgba(245,158,11,0.12)', icon:'⚙'  },
  txt:  { label:'TXT',  color:'#64748b', bg:'rgba(100,116,139,0.1)', icon:'📄' },
  svg:  { label:'SVG',  color:'#fbbf24', bg:'rgba(251,191,36,0.12)', icon:'◎'  },
};

/* ── Funções KODUX ── */
function archById(id)        { return ARCHETYPES.find(a => a.id === id) || ARCHETYPES[0]; }
function archByOpcode(op)    { return ARCHETYPES.find(a => a.opcode === op) || ARCHETYPES[0]; }
function archsByPhase(phase) { return ARCHETYPES.filter(a => a.phase === phase); }
function archsByTrinity(t)   { return ARCHETYPES.filter(a => a.trinity === t); }
function fileType(path) {
  const ext = (path || '').split('.').pop().toLowerCase();
  return FILE_TYPES[ext] || { label: ext.toUpperCase(), color:'#475569', bg:'rgba(71,85,105,0.1)', icon:'📁' };
}
function buildSSML(text, archId) {
  const v = archById(archId).voice || {};
  return (
    `<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="pt-BR">\n` +
    `  <voice name="${v.edge || 'pt-BR-AntonioNeural'}">\n` +
    `    <prosody pitch="${v.pitch || '+0st'}" rate="${v.rate || '1.0'}">${text}</prosody>\n` +
    `  </voice>\n</speak>`
  );
}


// ══════════════════════════════════════════════════════════
// §3 · BLLUE · FILHO · INTEGRAR · 528Hz
//     Store (localStorage), CSS, utilitários
// ══════════════════════════════════════════════════════════

const KEYS = {
  USER:       'kob_user',       API_KEY:    'kob_api_key',
  MODEL:      'kob_model',      PROVIDER:   'kob_provider',
  STATE_RAW:  'kob_state',      THEME:      'kob_theme',
  MODE:       'kob_interface_mode',
  REPO_TOKEN: 'kob_repo_token', HV_CONFIG:  'kob_hv_config',
  CDNS:       'kob_cdns',       EDITOR:     'kob_editor_state',
  MEMORY:     'kob_memory',     VAULT_PASS: 'kob_vault_pass',
  ACTIVE_KEY: 'kob_active_key', USER_KEYS:  'kob_user_keys',
};

const Store = {
  get(key, fallback) {
    try { const v = localStorage.getItem(key); return v !== null ? JSON.parse(v) : fallback; }
    catch { return fallback; }
  },
  set(key, val) {
    try { localStorage.setItem(key, JSON.stringify(val)); return true; }
    catch { return false; }
  },
  del(key)  { localStorage.removeItem(key); },
  has(key)  { return localStorage.getItem(key) !== null; },
  clear()   { Object.values(KEYS).forEach(k => localStorage.removeItem(k)); },

  /* Atalhos semânticos — leitura/escrita sincroniza STATE */
  user(v)      { return v !== undefined ? (Store.set(KEYS.USER,       v), STATE.set('user',      v)) : STATE.get('user'); },
  apiKey(v)    { return v !== undefined ? (Store.set(KEYS.API_KEY,    v), STATE.set('apiKey',    v)) : STATE.get('apiKey'); },
  model(v)     { return v !== undefined ? (Store.set(KEYS.MODEL,      v), STATE.set('model',     v)) : STATE.get('model'); },
  provider(v)  { return v !== undefined ? (Store.set(KEYS.PROVIDER,   v), STATE.set('provider',  v)) : STATE.get('provider'); },
  mode(v)      { return v !== undefined ? (Store.set(KEYS.MODE,       v), STATE.set('mode',      v)) : STATE.get('mode'); },
  repoToken(v) { return v !== undefined ? (Store.set(KEYS.REPO_TOKEN, v), STATE.set('repoToken', v)) : STATE.get('repoToken'); },
  hvConfig(v)  { return v !== undefined ? (Store.set(KEYS.HV_CONFIG,  v), STATE.set('hvConfig',  v)) : STATE.get('hvConfig'); },
  editor(v)    { return v !== undefined ? (Store.set(KEYS.EDITOR,     v), STATE.set('editor',    v)) : STATE.get('editor'); },
  theme(v)     { return v !== undefined ? (Store.set(KEYS.THEME,      v), STATE.set('theme',     v), injectCSS(v)) : STATE.get('theme'); },
};

/* ── CSS Injection — dual ↔ matrix ── */
function injectCSS(theme) {
  const id = 'kob-root-vars';
  const old = document.getElementById(id);
  if (old) old.remove();
  const p   = theme === 'matrix' ? PALETTE.matrix : PALETTE.dual;
  const s   = PALETTE.store;
  const kob = PALETTE.kobllux;
  const style = document.createElement('style');
  style.id = id;
  style.textContent = `:root {
  /* ∆¹ KODUX */
  --kob-primary:   ${theme === 'matrix' ? p.cyan   : p.primary};
  --kob-secondary: ${theme === 'matrix' ? p.violet : p.secondary};
  --kob-gold:      ${theme === 'matrix' ? p.gold   : p.tertiary};
  --kob-cyan:      ${theme === 'matrix' ? p.cyan   : p.primary};
  --kob-magenta:   ${theme === 'matrix' ? p.violet : p.secondary};
  --kob-green:     ${PALETTE.dual.green};
  --kob-purple:    ${PALETTE.dual.purple};
  --kob-orange:    ${PALETTE.dual.orange};
  --kob-danger:    ${PALETTE.dual.danger};
  /* ∆² BLLUE */
  --kob-void:      ${theme === 'matrix' ? p.void  : p.bg};
  --kob-glass:     ${theme === 'matrix' ? 'rgba(15,15,46,0.8)' : PALETTE.dual.glass};
  --kob-border:    ${theme === 'matrix' ? 'rgba(201,168,76,0.2)' : PALETTE.dual.border};
  --kob-text:      ${theme === 'matrix' ? p.pearl : PALETTE.dual.text};
  --kob-muted:     ${theme === 'matrix' ? p.mist  : PALETTE.dual.muted};
  --kob-font-ui:      ${FONTS.ui};
  --kob-font-code:    ${FONTS.code};
  --kob-font-display: ${theme === 'matrix' ? FONTS.display : FONTS.ui};
  /* ∆³ INFODOSE · KOBLLUX purple */
  --kobllux-primary: ${kob.primary};
  --kobllux-cyan:    ${kob.cyan};
  --kobllux-surface: ${kob.surface};
  --kobllux-border:  ${kob.border};
  --kobllux-glow:    ${kob.glow};
  /* Store/Card */
  --neon-cyan:    ${s.neonCyan};
  --neon-purple:  ${s.neonPurple};
  --card-bg:      ${s.cardBg};
  --card-border:  ${s.cardBorder};
  /* Legacy aliases */
  --primary:      ${theme === 'matrix' ? p.cyan   : p.primary};
  --secondary:    ${theme === 'matrix' ? p.violet : p.secondary};
  --tertiary:     ${theme === 'matrix' ? p.gold   : p.tertiary};
  --bg-deep:      ${theme === 'matrix' ? p.void   : p.bg};
  --glass-surface:${theme === 'matrix' ? 'rgba(15,15,46,0.8)' : PALETTE.dual.glass};
  --glass-border: ${theme === 'matrix' ? 'rgba(201,168,76,0.2)' : PALETTE.dual.border};
  --text-main:    ${theme === 'matrix' ? p.pearl  : PALETTE.dual.text};
  --text-muted:   ${theme === 'matrix' ? p.mist   : PALETTE.dual.muted};
  --font-ui:      ${FONTS.ui};
  --font-code:    ${FONTS.code};
  --header-h: 58px;
  --dock-h:   68px;
}`;
  document.head.appendChild(style);
}

/* ── Utilitários BLLUE ── */
function esc(s) {
  return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}
function toast(msg, type, ms) {
  const el = document.getElementById('toaster') || document.getElementById('kblx-toast');
  if (!el) return;
  el.textContent = msg;
  el.className   = 'show ' + (type || 'info');
  clearTimeout(el._t);
  el._t = setTimeout(() => el.className = '', ms || 2500);
}
function nav(route) {
  const url = ROUTES[route] || route;
  if (!url) return;
  url.startsWith('http') ? window.open(url, '_blank') : (window.location.href = url);
}


// ══════════════════════════════════════════════════════════
// §4 · INFODOSE · ESPÍRITO · EXPANDIR · 639Hz
//     Wave: transdução onda-URL · ciclo 3·6·9·7·1
// ══════════════════════════════════════════════════════════

const _WAVE_HOST = 'https://kobllux.host/meta/query';

const POLARIDADES = [
  { eixo:'ESTRUTURA', polo:['fixo','mutável'],               camada:'KODUX'    },
  { eixo:'EXPRESSÃO', polo:['manifesto','latente'],          camada:'BLLUE'    },
  { eixo:'ONDA',      polo:['codificação','decodificação'],  camada:'INFODOSE' },
  { eixo:'TEMPO',     polo:['passado','futuro'],             camada:'KODUX'    },
  { eixo:'PRESENÇA',  polo:['humano','máquina'],             camada:'BLLUE'    },
  { eixo:'FLUXO',     polo:['entrada','saída'],              camada:'INFODOSE' },
];

const VERDADES = [
  { id:1, token:'tudo é código',  chave:'código'         },
  { id:2, token:'tudo é onda',    chave:'onda'           },
  { id:3, token:'personalização', chave:'personalização' },
  { id:4, token:'pulso',          chave:'pulso'          },
  { id:5, token:'humanidade',     chave:'humanidade'     },
  { id:6, token:'integração',     chave:'integração'     },
  { id:7, token:'único',          chave:'único'          },
];

function _gerarPotenciais(tokens) {
  return ['passado','presente','futuro'].flatMap(t =>
    ['KODUX','BLLUE','INFODOSE'].map(d => {
      const ativo = tokens.some(tk =>
        tk.toLowerCase().includes(t) || (t === 'presente' && tk.toLowerCase().includes('agora'))
      );
      return { tempo: t, dominio: d, ativo, vetor: `${t}×${d}` };
    })
  );
}

const Wave = {
  encode(texto) {
    if (!texto || typeof texto !== 'string') return '';
    return `${_WAVE_HOST}?q=${encodeURIComponent(texto.trim().replace(/\s+/g, ' '))}`;
  },

  decode(url) {
    let raw = url.includes('?q=') ? (url.split('?q=')[1] || url).split('&')[0] : url;
    let texto;
    try { texto = decodeURIComponent(raw); } catch { texto = raw; }

    const tokens      = texto.split(/[\s,;.!?]+/).filter(t => t.length > 1).map(t => t.trim());
    const tl          = texto.toLowerCase();
    const polaridades = POLARIDADES.map(p => {
      const p0 = tl.includes(p.polo[0]), p1 = tl.includes(p.polo[1]);
      return { ...p, detectado: [p0, p1], ativo: p0 || p1, intensidade: (p0 && p1) ? 1.0 : (p0 || p1) ? 0.5 : 0 };
    });
    const potenciais  = _gerarPotenciais(tokens);
    const verdades    = VERDADES.map(v => ({ ...v, ativo: tl.includes(v.chave) }));
    const pulso       = (tl.includes('humanidade') && tl.includes('código'))
                        ? 'código em prol da humanidade'
                        : tokens.slice(-3).join(' ');

    const result = {
      texto, tokens, totalTokens: tokens.length,
      camadas: {
        KODUX: {
          tokensEstruturais: tokens.filter(t =>
            ['KODUX','BLLUE','INFODOSE','fixo','mutável','passado','presente','futuro'].includes(t)
          ),
        },
        BLLUE: {
          tokensExpressivos: tokens.filter(t =>
            ['humano','máquina','onda','personalização','humanidade','manifesto','latente','integração']
              .includes(t.toLowerCase())
          ),
          significado: texto.slice(0, 200),
        },
        INFODOSE: {
          encoded:        encodeURIComponent(texto).slice(0, 300),
          decoded:        texto.slice(0, 200),
          bytesEncoded:   encodeURIComponent(texto).length,
          bytesDecoded:   texto.length,
          razaoCompressao:(encodeURIComponent(texto).length / Math.max(texto.length, 1)).toFixed(2),
        },
      },
      polaridades,
      totalPolaridadesAtivas: polaridades.filter(p => p.ativo).length,
      potenciais,
      potenciaisAtivos: potenciais.filter(p => p.ativo).length,
      verdades,
      totalVerdades: verdades.filter(v => v.ativo).length,
      pulso,
      assinatura: `${polaridades.filter(p=>p.ativo).length}·${potenciais.filter(p=>p.ativo).length}·${verdades.filter(v=>v.ativo).length}·1`,
      ciclo: '3→6→9→7→1',
    };

    /* Propagação STATE ∆³ */
    STATE.set('lastWave', result);
    STATE.set('pulso', pulso);
    Bus.emit('infodose:wave', result);

    return result;
  },

  analisar(texto) {
    const url   = Wave.encode(texto);
    const campo = Wave.decode(url);
    return { textoOriginal: texto, urlOnda: url, ...campo, timestamp: new Date().toISOString(), modulo:'kob-wave', versao:'1.0', delta:'∆³' };
  },

  formatarCampo(campo) {
    const l = [];
    l.push('═══ kΦb WAVE · Transdução ∆³ ═══');
    l.push(`Texto:     ${campo.texto?.slice(0, 80)}...`);
    l.push(`Tokens:    ${campo.totalTokens}  |  Assinatura: ${campo.assinatura}  |  Ciclo: ${campo.ciclo}`);
    l.push('\n── 3 CAMADAS ──');
    l.push(`KODUX:    ${campo.camadas?.KODUX?.tokensEstruturais?.join(', ') || '—'}`);
    l.push(`BLLUE:    ${campo.camadas?.BLLUE?.tokensExpressivos?.join(', ') || '—'}`);
    l.push(`INFODOSE: ratio=${campo.camadas?.INFODOSE?.razaoCompressao || '—'}`);
    l.push('\n── 6 POLARIDADES ──');
    (campo.polaridades || []).forEach(p =>
      l.push(`  ${p.ativo ? (p.intensidade === 1 ? '◉' : '◎') : '○'} ${p.polo[0]} ↔ ${p.polo[1]}  [${p.camada}]`)
    );
    l.push(`\n── 9 POTENCIAIS (${campo.potenciaisAtivos} ativos) ──`);
    (campo.potenciais || []).forEach(p => l.push(`  ${p.ativo ? '●' : '○'} ${p.vetor}`));
    l.push(`\n── 7 VERDADES (${campo.totalVerdades} encontradas) ──`);
    (campo.verdades || []).forEach(v => l.push(`  ${v.ativo ? '✓' : '·'} [${v.id}] ${v.token}`));
    l.push(`\n── 1 PULSO ──\n  → ${campo.pulso}`);
    l.push('\nVERDADE × INTEGRAR ÷ Δ = ∞');
    return l.join('\n');
  },

  POLARIDADES,
  VERDADES,
};


// ══════════════════════════════════════════════════════════
// §5 · INIT — restaura STATE do localStorage e lacra ciclo
// ══════════════════════════════════════════════════════════

function _init() {
  /* Restaurar STATE persistido */
  const saved = Store.get(KEYS.STATE_RAW, {});
  STATE.patch({
    theme:     saved.theme     || Store.get(KEYS.THEME,      'dual'),
    user:      saved.user      || Store.get(KEYS.USER,       'Convidado'),
    apiKey:    saved.apiKey    || Store.get(KEYS.API_KEY,    ''),
    model:     saved.model     || Store.get(KEYS.MODEL,      ''),
    provider:  saved.provider  || Store.get(KEYS.PROVIDER,   'openrouter'),
    mode:      saved.mode      || Store.get(KEYS.MODE,       'card'),
    repoToken: saved.repoToken || Store.get(KEYS.REPO_TOKEN, ''),
    hvConfig:  saved.hvConfig  || Store.get(KEYS.HV_CONFIG,  {}),
    editor:    saved.editor    || Store.get(KEYS.EDITOR,     { html:'', path:'novo_arquivo.html', cdns:[] }),
  });

  /* Toda mudança de STATE persiste automaticamente */
  Bus.on(e => {
    if (e.event === 'state:change') Store.set(KEYS.STATE_RAW, STATE.snapshot());
  });

  injectCSS(STATE.get('theme'));
  Bus.emit('kob:ready', { version:'4.0', delta:'∆³', theme: STATE.get('theme') });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', _init);
} else {
  _init();
}


// ══════════════════════════════════════════════════════════
// §6 · EXPOSIÇÃO PÚBLICA — window.KOB
// ══════════════════════════════════════════════════════════

const KOB = Object.freeze({
  version: '4.0',
  delta:   '∆³',
  seal:    'Φ',

  /* ── ∆¹ KODUX (estrutura) ── */
  KODUX: Object.freeze({
    PALETTE, FONTS, ARCHETYPES, META, ROUTES, FILE_TYPES,
    archById, archByOpcode, archsByPhase, archsByTrinity, fileType, buildSSML,
  }),

  /* ── ∆² BLLUE (interface + memória) ── */
  BLLUE: Object.freeze({
    Store, Bus, STATE, KEYS,
    injectCSS, esc, toast, nav,
  }),

  /* ── ∆³ INFODOSE (onda + transdução) ── */
  INFODOSE: Object.freeze({
    Wave, POLARIDADES, VERDADES,
  }),

  /* Atalhos raiz — acesso direto sem namespace */
  PALETTE, FONTS, ARCHETYPES, META, ROUTES, FILE_TYPES, KEYS,
  Store, Bus, STATE, Wave,
  esc, toast, nav,
  archById, archByOpcode, archsByPhase, archsByTrinity, fileType, buildSSML, injectCSS,
});

root.KOB = KOB;

/* Aliases de compatibilidade com scripts existentes */
root.KOBLLUX_ARCHETYPES = ARCHETYPES;
root.KOBLLUX_BUS        = Bus;
root.KOBLLUX_WAVE       = Wave;
root.KOBLLUX_STATE      = STATE;

console.log(
  '%c⬡ kΦb %c4.0 ∆³ %c· KODUX·BLLUE·INFODOSE · VERDADE × INTEGRAR ÷ Δ = ∞',
  'color:#00f5ff;font-weight:900;font-size:12px',
  'color:#ffd700;font-weight:700',
  'color:#9aa4c8;font-weight:400'
);

})(typeof window !== 'undefined' ? window : globalThis);
