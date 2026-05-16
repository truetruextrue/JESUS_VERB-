/* ═══════════════════════════════════════════════════════════
   0x05 · CONVERGIR · E · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-core-isolado/js/L7_0x05_savedname_E_D6-2.js
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
     χ = -12  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
document.addEventListener('DOMContentLoaded', () => {
      if (window.lucide) lucide.createIcons();

      const savedName = localStorage.getItem('di_userName') || localStorage.getItem('userName');
      di_syncNameUI(savedName || 'Convidado');

      $('#inputUser')?.addEventListener('input', e => di_syncNameUI(e.target.value));
      $('#infodoseNameInput')?.addEventListener('input', e => di_syncNameUI(e.target.value));

      $('#smallPreview')?.addEventListener('click', toggleCard);
      $('#avatarTarget')?.addEventListener('click', () => openModal('#keysModal'));

      $('#closeKeysBtn')?.addEventListener('click', () => closeModal('#keysModal'));
      $('#lockVaultBtn')?.addEventListener('click', () => {
        closeModal('#keysModal');
        openModal('#vaultModal');
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
        } catch (e) { console.error('Erro ao copiar:', e); }
      });

      $('#saveSystemBtn')?.addEventListener('click', () => {
        const name  = $('#infodoseNameInput')?.value;
        const key   = $('#apiKeyInput')?.value;
        const model = $('#modelSelect')?.value;
        console.log('[KOBLLUX] Config salva:', { name, key: key ? '***' : '', model });
        alert('Configuração salva! ✓');
      });

      $('.drag-handle')?.addEventListener('mousedown', (e) => {
        e.preventDefault();
        const card = $('#mainCard');
        const startX = e.clientX, startY = e.clientY;
        const startLeft = card.offsetLeft, startTop = card.offsetTop;
        function onMove(e) {
          card.style.position = 'absolute';
          card.style.left = `${startLeft + (e.clientX - startX)}px`;
          card.style.top  = `${startTop  + (e.clientY - startY)}px`;
        }
        function onUp() {
          document.removeEventListener('mousemove', onMove);
          document.removeEventListener('mouseup', onUp);
        }
        document.addEventListener('mousemove', onMove);
        document.addEventListener('mouseup', onUp);
      });

      $('#orbMenuTrigger')?.addEventListener('click', () => {
        console.log('[KOBLLUX] Menu orbital ativado');
      });

      setTimeout(() => { if (window.lucide) lucide.createIcons(); }, 100);
    });

    // expor API global
    window.KOBLLUX_CARD = {
      toggleCard, toggleSection, setMode, di_syncNameUI,
      makeOrbAvatar, openModal, closeModal
    };