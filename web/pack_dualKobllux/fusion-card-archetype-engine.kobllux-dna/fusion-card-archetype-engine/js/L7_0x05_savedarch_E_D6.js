/* ═══════════════════════════════════════════════════════════
   0x05 · CONVERGIR · E · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-archetype-engine/js/L7_0x05_savedarch_E_D6.js
   Opcode    : 0x05 · CONVERGIR · ⧉ · 672Hz
   V.E.E.B.  : Energia
   Degrau    : D6 (section)
   Fórmula   : Energia · f₅=672Hz · fluxo convergente · L₁∩L₂=P*
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 7 · ORQUESTRADOR
   Opcode Δ  : 0x0C · Carregar na posição 7 da cadeia
   Nota      : Init — espera DOM + todos os scripts
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 62  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=672)
     χ = -14  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
    if (window.lucide) lucide.createIcons();

    buildStrip();

    const savedArch = localStorage.getItem('di_activeArchetype');
    const idx = ARCHETYPES_DB.findIndex(a => a.id === savedArch);
    applyArchetype(idx >= 0 ? idx : 0);

    const savedName = localStorage.getItem('di_userName') || localStorage.getItem('userName');
    di_syncNameUI(savedName || 'Convidado');

    $('#inputUser')?.addEventListener('input', e => di_syncNameUI(e.target.value));
    $('#infodoseNameInput')?.addEventListener('input', e => di_syncNameUI(e.target.value));

    $('#archPrev')?.addEventListener('click', prevArchetype);
    $('#archNext')?.addEventListener('click', nextArchetype);

    // orb colapsado → reabre
    $('#collapsedOrb')?.addEventListener('click', toggleCard);
    // avatar header → cofre
    $('#avatarTarget')?.addEventListener('click', () => openModal('#keysModal'));

    // duplo clique no header colapsa
    $('#cardHeader')?.addEventListener('dblclick', toggleCard);

    $('#closeKeysBtn')?.addEventListener('click', () => closeModal('#keysModal'));
    $('#lockVaultBtn')?.addEventListener('click', () => {
      closeModal('#keysModal'); openModal('#vaultModal');
    });
    $('#vaultCancelBtn')?.addEventListener('click', () => closeModal('#vaultModal'));
    $('#vaultUnlockBtn')?.addEventListener('click', () => {
      closeModal('#vaultModal');
      console.log('[KOBLLUX] Cofre desbloqueado');
    });

    $('#copyActBtn')?.addEventListener('click', async () => {
      const text = $('#actPre')?.textContent || '';
      try {
        await navigator.clipboard.writeText(text);
        const btn = $('#copyActBtn');
        const original = btn.textContent;
        btn.textContent = 'COPIADO!';
        setTimeout(() => btn.textContent = original, 1500);
      } catch (e) { console.error(e); }
    });

    $('#saveSystemBtn')?.addEventListener('click', () => {
      const name  = $('#infodoseNameInput')?.value;
      const key   = $('#apiKeyInput')?.value;
      const model = $('#modelSelect')?.value;
      console.log('[KOBLLUX] Config salva:', { name, key: key ? '***' : '', model });
      const btn = $('#saveSystemBtn');
      const original = btn.textContent;
      btn.textContent = '✓ SALVO';
      setTimeout(() => btn.textContent = original, 1400);
    });

    // teclado: ←/→ navega arquétipos · espaço colapsa
    document.addEventListener('keydown', (e) => {
      if (e.target.matches('input, textarea, select')) return;
      if (e.key === 'ArrowRight') { nextArchetype(); e.preventDefault(); }
      if (e.key === 'ArrowLeft')  { prevArchetype(); e.preventDefault(); }
      if (e.key === ' ')          { toggleCard();     e.preventDefault(); }
    });

    setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 100);
  });

  // expor API
  window.KOBLLUX_CARD = {
    applyArchetype, nextArchetype, prevArchetype,
    toggleCard, toggleSection, setMode,
    di_syncNameUI, openModal, closeModal,
    ARCHETYPES_DB, KOBLLUX_OPCODES
  };