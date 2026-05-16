/* ═══════════════════════════════════════════════════════════
   0x09 · MANIFESTAR · V · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : chat-cinematic-kobllux/js/L7_0x09_savedarch_V_D6-4.js
   Opcode    : 0x09 · MANIFESTAR · ♾ · 963Hz
   V.E.E.B.  : Vibração
   Degrau    : D6 (section)
   Fórmula   : Vibração · f₉=963Hz · campo→forma visual · S² χ=2
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 7 · ORQUESTRADOR
   Opcode Δ  : 0x0C · Carregar na posição 7 da cadeia
   Nota      : Init — espera DOM + todos os scripts
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 62  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=963)
     χ = -13  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
    const savedArch = localStorage.getItem('di_activeArchetype');
    const idx = ARCHETYPES_DB.findIndex(a => a.id === savedArch);
    applyArchetype(idx >= 0 ? idx : 0);
    initParticles();
    setTimeout(syncParticles, 400);
    bootTypewriter();

    // arquétipo stamp → cicla
    $('#archStamp').addEventListener('click', () => nextArchetype());

    // controles principais
    $('#sendBtn').addEventListener('click', onSend);
    $('#userInput').addEventListener('keypress', e => {
      if (e.key === 'Enter') onSend();
    });
    $('#voiceBtn').addEventListener('click', () => {
      KOBLLUX_LOG.emit('USR·VOICE');
      try {
        const SR = window.SpeechRecognition || window.webkitSpeechRecognition;
        if (!SR) { KOBLLUX_LOG.emit('USR·VOICE', { detail: 'sem suporte' }); return; }
        const rec = new SR();
        rec.lang = 'pt-BR';
        rec.start();
        rec.onresult = evt => {
          $('#userInput').value = evt.results[0][0].transcript;
          onSend();
        };
      } catch(e) {}
    });

    // copy/paste
    $('.copy-button').addEventListener('click', () => {
      const blocks = $$('.response-block');
      const txt = Array.from(blocks).map(b => b.innerText).join('\n\n');
      navigator.clipboard?.writeText(txt);
      KOBLLUX_LOG.emit('CHAT·COPY', { detail: blocks.length + ' blocos' });
    });
    $('.paste-button').addEventListener('click', async () => {
      try {
        const txt = await navigator.clipboard.readText();
        $('#userInput').value = txt;
        KOBLLUX_LOG.emit('CHAT·PASTE');
      } catch(e) {}
    });

    // toggle/kitty/history (alterna estados visuais + log)
    ['toggleBtn','kittyBtn','historyBtn'].forEach(id => {
      $('#' + id).addEventListener('click', (e) => {
        const btn = e.currentTarget;
        const active = btn.classList.toggle('active');
        if (id === 'toggleBtn' && active) {
          $('#loginBox').classList.add('active');
        } else if (id === 'toggleBtn') {
          $('#loginBox').classList.remove('active');
        }
        KOBLLUX_LOG.emit('CHAT·MODE', { detail: `${id}=${active ? 'ON' : 'OFF'}` });
      });
    });

    // pagination
    document.querySelector('.pagination').addEventListener('click', e => {
      if (e.target.dataset.action === 'prev') changePage(-1);
      if (e.target.dataset.action === 'next') changePage(1);
      STATE.autoAdvance = false;
    });

    // login form
    $('#loginForm').addEventListener('submit', e => {
      e.preventDefault();
      const u = $('#userName').value.trim();
      const a = $('#assistantInput').value.trim();
      if (!u || !a) return;
      localStorage.setItem('userName', u);
      localStorage.setItem('assistantBase', a);
      $('#assistantName').textContent = (a + ' · DUAL.INFODOSE').toUpperCase();
      $('#loginBox').classList.remove('active');
      KOBLLUX_LOG.emit('USR·LOGIN', { detail: `${u} / ${a}` });
    });

    // footer collapse
    document.querySelector('.footer-text').addEventListener('click', (e) => {
      $('.pages-wrapper').classList.toggle('collapsed');
      e.currentTarget.classList.toggle('active');
      KOBLLUX_LOG.emit('CHAT·FOOTER');
    });

    // teclado: ←/→ navega arquétipos quando não está digitando
    document.addEventListener('keydown', e => {
      if (e.target.matches('input, textarea')) return;
      if (e.key === 'ArrowRight') { nextArchetype(); e.preventDefault(); }
      if (e.key === 'ArrowLeft')  { prevArchetype(); e.preventDefault(); }
    });

    setTimeout(() => KOBLLUX_LOG.emit('CHAT·BOOT', { detail: 'Chat Cinematic · ' + STATE.archetype.name }), 80);
  });

  window.KOBLLUX_CHAT = { applyArchetype, nextArchetype, prevArchetype, renderResponse };