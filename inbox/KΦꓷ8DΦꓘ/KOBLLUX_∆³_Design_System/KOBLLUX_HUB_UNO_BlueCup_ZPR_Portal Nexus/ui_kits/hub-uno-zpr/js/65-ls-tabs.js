/* ╔══════════════════════════════════════════════════════════╗
   ║  LS PANEL · TABS                                        ║
   ║  Adiciona aba "BlueCup · Apps" ao #ls-panel              ║
   ║  Aba 1: BRAIN (LocalStorage viewer original)            ║
   ║  Aba 2: BLUECUP (painel de apps locais do BlueCup)     ║
   ╚══════════════════════════════════════════════════════════╝ */
(function(){
  'use strict';

  function inject() {
    const panel = document.getElementById('ls-panel');
    if (!panel) { console.warn('[LS-Tabs] #ls-panel não encontrado'); return; }
    if (panel.querySelector('.ls-tabs')) return; // already injected

    const header = panel.querySelector('header');
    const grid   = panel.querySelector('#ls-grid');
    if (!header || !grid) return;

    // Build tabbar
    const tabbar = document.createElement('div');
    tabbar.className = 'ls-tabs';
    tabbar.innerHTML = `
      <button class="ls-tab active" data-tab="brain">⌬ BRAIN</button>
      <button class="ls-tab" data-tab="bluecup">⌘ BLUECUP</button>
    `;
    header.after(tabbar);

    // Wrap original grid into tabpanel
    const brainPanel = document.createElement('div');
    brainPanel.className = 'ls-tabpanel ls-tabpanel-brain active';
    grid.parentNode.insertBefore(brainPanel, grid);
    brainPanel.appendChild(grid);

    // BlueCup tabpanel — clones the BlueCup card structure WITHOUT IDs
    // (the real card lives in v-apps; here we mount a 2nd instance with fresh IDs)
    const bcPanel = document.createElement('div');
    bcPanel.className = 'ls-tabpanel ls-tabpanel-bluecup';
    bcPanel.innerHTML = `
      <div class="bluecup-local-shell" data-source="LS_PANEL_TAB">
        <div class="card localAppsCard">
          <details open>
            <summary>
              <span class="appsSummary">
                <span class="appsSummary-dot"></span>
                <span class="appsSummary-title">APPS · LOCAIS (LS)</span>
                <span class="appsSummary-sub">upload / editar / abrir #local:</span>
              </span>
              <span class="chev">▾</span>
            </summary>
            <div class="content">
              <div class="appsToolbar">
                <div class="btnRow" style="margin:0">
                  <button class="appBtn primary lsbc-upload" type="button">Upload HTML</button>
                  <button class="appBtn lsbc-new" type="button">Novo Local</button>
                  <button class="appBtn lsbc-export" type="button">Exportar</button>
                  <button class="appBtn lsbc-import" type="button">Importar</button>
                </div>
                <input class="lsbc-upload-input" type="file" accept=".html,text/html" multiple hidden />
                <input class="lsbc-import-input" type="file" accept=".json,application/json" hidden />
              </div>
              <div class="lsbc-grid appsGrid"></div>
              <div class="appsFooter tiny lsbc-hint">
                Mesma fonte de dados do painel APPS — sincronizado.
              </div>
            </div>
          </details>
        </div>
      </div>
    `;
    brainPanel.after(bcPanel);

    // Tab switching
    tabbar.addEventListener('click', e => {
      const btn = e.target.closest('.ls-tab');
      if (!btn) return;
      const tab = btn.dataset.tab;
      tabbar.querySelectorAll('.ls-tab').forEach(b => b.classList.toggle('active', b === btn));
      panel.querySelectorAll('.ls-tabpanel').forEach(p => {
        p.classList.toggle('active', p.classList.contains('ls-tabpanel-' + tab));
      });
      if (tab === 'bluecup') renderBlueCup();
      if (tab === 'brain' && typeof window.lsRender === 'function') window.lsRender();
    });

    // ── BlueCup renderer (usa os mesmos helpers loadLocalAppFiles/saveLocalAppFiles)
    const grid2 = bcPanel.querySelector('.lsbc-grid');
    const hint  = bcPanel.querySelector('.lsbc-hint');

    function load() {
      try {
        if (window.loadLocalAppFiles) return window.loadLocalAppFiles();
        return JSON.parse(localStorage.getItem('kobllux_apps_files_v1') || '{}');
      } catch(e) { return {}; }
    }
    function save(obj) {
      if (window.saveLocalAppFiles) return window.saveLocalAppFiles(obj);
      localStorage.setItem('kobllux_apps_files_v1', JSON.stringify(obj||{}));
    }
    function escHtml(s){ return String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

    function renderBlueCup() {
      const raw = load();
      const keys = Object.keys(raw);
      grid2.innerHTML = '';
      if (!keys.length) {
        hint.textContent = 'Nenhum app local. Use Upload HTML ou Novo Local.';
        return;
      }
      hint.textContent = keys.length + ' app(s) local(is) sincronizado(s) com o painel APPS.';
      keys.sort().forEach(key => {
        const v = raw[key];
        const entry = (typeof v === 'string') ? { title:key, desc:'', icon:'', html:v }
                                              : (v || { title:key });
        const card = document.createElement('div');
        card.className = 'appCard';
        card.innerHTML = '<div class="appIcon">' + (entry.icon ? '<img src="' + escHtml(entry.icon) + '" alt="">' : '⌘') + '</div>'
                       + '<div class="appBody">'
                       + '<div class="appTitle">' + escHtml(entry.title || key) + '</div>'
                       + '<div class="appDesc">' + escHtml(entry.desc || '') + '</div>'
                       + '<div class="appActions">'
                       + '<button class="appBtn primary" data-act="open">Open</button>'
                       + '<button class="appBtn" data-act="del">Del</button>'
                       + '</div></div>';
        card.querySelector('[data-act="open"]').onclick = () => {
          if (window.openApp) window.openApp({key,title:entry.title||key,desc:entry.desc||'',icon:entry.icon||'',url:'#local:'+key,_local:true});
        };
        card.querySelector('[data-act="del"]').onclick = () => {
          if (!confirm('Apagar "' + (entry.title||key) + '"?')) return;
          const r = load(); delete r[key]; save(r); renderBlueCup();
        };
        grid2.appendChild(card);
      });
    }

    bcPanel.querySelector('.lsbc-upload').onclick = () => bcPanel.querySelector('.lsbc-upload-input').click();
    bcPanel.querySelector('.lsbc-upload-input').onchange = async function(){
      const files = Array.from(this.files||[]);
      if (!files.length) return;
      const raw = load();
      for (const f of files) {
        const html = await f.text();
        const base = (f.name||'app').replace(/\.html?$/i,'');
        const m = String(html).match(/<title[^>]*>([\s\S]*?)<\/title>/i);
        const title = (m ? m[1].trim() : base).slice(0,80);
        const key = (window.makeSafeKey ? window.makeSafeKey(title) : base.toLowerCase().replace(/[^a-z0-9]+/g,'-'));
        raw[key] = { title, desc:'', icon:'', html };
      }
      save(raw); this.value = ''; renderBlueCup();
    };
    bcPanel.querySelector('.lsbc-new').onclick = () => {
      const title = prompt('Nome do novo app local?', 'Novo App Local');
      if (!title) return;
      const key = (window.makeSafeKey ? window.makeSafeKey(title) : title.toLowerCase().replace(/[^a-z0-9]+/g,'-'));
      const raw = load();
      raw[key] = { title, desc:'', icon:'', html: '<!doctype html><html><head><title>'+title+'</title></head><body><h1>'+title+'</h1></body></html>' };
      save(raw); renderBlueCup();
    };
    bcPanel.querySelector('.lsbc-export').onclick = () => {
      if (window.downloadJson) return window.downloadJson('local_apps.json', load());
      const blob = new Blob([JSON.stringify(load(), null, 2)], { type:'application/json' });
      const a = document.createElement('a');
      a.href = URL.createObjectURL(blob); a.download = 'local_apps.json'; a.click();
    };
    bcPanel.querySelector('.lsbc-import').onclick = () => bcPanel.querySelector('.lsbc-import-input').click();
    bcPanel.querySelector('.lsbc-import-input').onchange = async function(){
      const f = this.files?.[0]; if (!f) return;
      try {
        const j = JSON.parse(await f.text());
        const r = load(); Object.assign(r, j); save(r);
        renderBlueCup();
        window.kblxToast && window.kblxToast('✓ Apps locais importados');
      } catch(e){ alert('JSON inválido: ' + e.message); }
      this.value = '';
    };

    console.log('[LS-Tabs] BRAIN | BLUECUP tabs injected into #ls-panel');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', inject);
  } else {
    inject();
  }
})();
