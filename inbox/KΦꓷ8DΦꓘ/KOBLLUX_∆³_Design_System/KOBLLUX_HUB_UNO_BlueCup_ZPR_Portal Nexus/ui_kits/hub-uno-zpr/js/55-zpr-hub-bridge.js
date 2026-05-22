/* ╔══════════════════════════════════════════════════════════╗
   ║  ZPR × HUB UNO · BRIDGE                                 ║
   ║  • Garante todas as <section.view> permanentemente      ║
   ║    visíveis (override do router original)               ║
   ║  • Intercepta cliques no symbolbar p/ usar navigateToCell║
   ║  • Reroute window.go → window.navigateToView            ║
   ╚══════════════════════════════════════════════════════════╝ */
(function(){
  'use strict';

  // Override router: força todas as .view visíveis na próxima frame e em mutações
  function forceVisible() {
    document.querySelectorAll('main section.view, section.view').forEach(s => {
      s.style.display = 'block';
    });
  }
  // Aplica imediatamente
  document.addEventListener('DOMContentLoaded', forceVisible);
  setTimeout(forceVisible, 50);
  setTimeout(forceVisible, 200);
  setTimeout(forceVisible, 800);

  // Observa mutações no atributo style das views (router pode mexer)
  const mo = new MutationObserver(forceVisible);
  mo.observe(document.documentElement, { attributes: true, subtree: true, attributeFilter: ['style','class'] });

  // Symbolbar bridge: capture os cliques data-nav antes do bridge nativo
  document.addEventListener('click', function(ev){
    const btn = ev.target.closest('#symbolBar .symbol-button[data-nav]');
    if (!btn) return;
    const nav = btn.getAttribute('data-nav');
    if (!nav) return;
    ev.preventDefault();
    ev.stopPropagation();
    if (typeof window.navigateToView === 'function') window.navigateToView(nav);
  }, true); // capture-phase

  console.log('[ZPR-Bridge] views permanently visible · symbolbar wired to navigateToView');
})();
