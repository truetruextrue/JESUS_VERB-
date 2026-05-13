/* ═══════════════════════════════════════════════════════════
   CADIAL COUPLER · KOBΦ-NODE · ∆7
   Acopla os 12 arquétipos ao motor ZPR + shell iFSw
   Regra: nunca altera classes, IDs ou opcodes existentes
   Lei: VERDADE × INTEGRAR ÷ Δ = ∞
   ═══════════════════════════════════════════════════════════ */
(function () {
  "use strict";

  /* ── 1. Registro dos 12 Arquétipos CADIAL ─────────────────────────── */
  const CADIAL = [
    { id: "atlas",   name: "ATLAS",   hz: 528,  icon: "⬡", color: "#9bb3ff", tag: "Estrutura",  snip: "./ARQUETIPOS/atlas/index.html"   },
    { id: "nova",    name: "NOVA",    hz: 528,  icon: "✦", color: "#00e5ff", tag: "Criação",    snip: "./ARQUETIPOS/nova/index.html"    },
    { id: "vitalis", name: "VITALIS", hz: 639,  icon: "◉", color: "#39ff14", tag: "Força",      snip: "./ARQUETIPOS/vitalis/index.html" },
    { id: "pulse",   name: "PULSE",   hz: 741,  icon: "≋", color: "#ff6ec7", tag: "Emoção",     snip: "./ARQUETIPOS/pulse/index.html"   },
    { id: "artemis", name: "ARTEMIS", hz: 432,  icon: "◎", color: "#ffd700", tag: "Precisão",   snip: "./ARQUETIPOS/artemis/index.html" },
    { id: "serena",  name: "SERENA",  hz: 639,  icon: "❋", color: "#c8f4b2", tag: "Cuidado",    snip: "./ARQUETIPOS/serena/index.html"  },
    { id: "kaos",    name: "KAOS",    hz: 396,  icon: "⚡", color: "#ff4500", tag: "Ruptura",    snip: "./ARQUETIPOS/kaos/index.html"    },
    { id: "genus",   name: "GENUS",   hz: 528,  icon: "⬢", color: "#d4af37", tag: "Gênese",     snip: "./ARQUETIPOS/genus/index.html"   },
    { id: "lumine",  name: "LUMINE",  hz: 852,  icon: "☀", color: "#fff176", tag: "Luz",        snip: "./ARQUETIPOS/lumine/index.html"  },
    { id: "solus",   name: "SOLUS",   hz: 963,  icon: "◈", color: "#b39ddb", tag: "Silêncio",   snip: "./ARQUETIPOS/solus/index.html"   },
    { id: "rhea",    name: "RHEA",    hz: 639,  icon: "∞", color: "#80deea", tag: "Fluxo",      snip: "./ARQUETIPOS/rhea/index.html"    },
    { id: "aion",    name: "AION",    hz: 963,  icon: "⧗", color: "#ce93d8", tag: "Tempo",      snip: "./ARQUETIPOS/aion/index.html"    }
  ];

  /* ── 2. Mapa 3×3 do ZPR → Arquétipos (primeiros 9, +3 no dock) ─────── */
  const ZPR_MAP = [
    ["atlas",   "nova",    "vitalis"],
    ["pulse",   "artemis", "serena" ],
    ["kaos",    "genus",   "lumine" ]
  ];
  const DOCK_EXTRA = ["solus", "rhea", "aion"]; // aparecem no dock lateral

  /* ── 3. Helpers ─────────────────────────────────────────────────────── */
  function archById(id) {
    return CADIAL.find(a => a.id === id);
  }

  function openArchSnip(arch) {
    if (typeof window.createSessionWindow === "function") {
      window.createSessionWindow(arch.snip, arch.icon, arch.name + " · " + arch.tag);
    }
  }

  /* ── 4. Injetar dados CADIAL no ZPR via dataset ──────────────────────
     O ZPR lê data-url de cada .screen para saber o que carregar.
     Aguardamos o ZPR construir o grid e então remapeamos as células. */
  function patchZprGrid() {
    const grid = document.getElementById("ZPR");
    if (!grid) return;

    const screens = grid.querySelectorAll(".screen");
    screens.forEach(screen => {
      const r = parseInt(screen.dataset.row, 10);
      const c = parseInt(screen.dataset.col, 10);
      if (isNaN(r) || isNaN(c)) return;

      const archId = ZPR_MAP[r] && ZPR_MAP[r][c];
      if (!archId) return;
      const arch = archById(archId);
      if (!arch) return;

      // Atualiza metadados sem recriar o elemento (preserva listeners do ZPR)
      screen.dataset.url   = arch.snip;
      screen.dataset.title = arch.name;
      screen.dataset.tag   = arch.tag;
      screen.style.setProperty("--arch-color", arch.color);

      // Injeta badge visual sem sobrescrever HTML interno existente
      const badge = document.createElement("div");
      badge.className = "cadial-badge";
      badge.textContent = arch.icon + " " + arch.name;
      badge.style.cssText = [
        "position:absolute","bottom:8px","left:50%","transform:translateX(-50%)",
        "background:rgba(0,0,0,.65)","backdrop-filter:blur(6px)",
        "color:" + arch.color,"font-size:11px","font-weight:700",
        "letter-spacing:1.5px","padding:3px 10px","border-radius:20px",
        "pointer-events:none","white-space:nowrap","z-index:2"
      ].join(";");
      screen.style.position = "relative";
      screen.appendChild(badge);
    });
  }

  /* ── 5. Dock EXTRA: SOLUS / RHEA / AION ─────────────────────────────
     Injeta 3 botões na topbar .top-actions para os arquétipos extras.  */
  function injectDockExtras() {
    const actions = document.querySelector(".top-actions");
    if (!actions) return;

    const wrap = document.createElement("div");
    wrap.id = "cadial-extra-btns";
    wrap.style.cssText = "display:flex;gap:6px;align-items:center;margin-left:8px";

    DOCK_EXTRA.forEach(id => {
      const arch = archById(id);
      if (!arch) return;
      const btn = document.createElement("button");
      btn.className = "soft-btn";
      btn.title = arch.name + " · " + arch.tag + " · " + arch.hz + "Hz";
      btn.innerHTML = arch.icon + "<small style='font-size:9px;display:block;opacity:.7'>" + arch.name + "</small>";
      btn.style.cssText = "color:" + arch.color + ";border-color:" + arch.color + "44;min-width:36px";
      btn.addEventListener("click", () => openArchSnip(arch));
      wrap.appendChild(btn);
    });

    actions.appendChild(wrap);
  }

  /* ── 6. Painel lateral de arquétipos (snip rápido) ───────────────────
     Barra colapsável na lateral direita com todos os 12 arquétipos.    */
  function buildArchPanel() {
    const panel = document.createElement("div");
    panel.id = "cadial-arch-panel";
    panel.setAttribute("aria-label", "CADIAL Arquétipos");
    panel.innerHTML = `
      <button id="cadial-panel-toggle" title="CADIAL · 12 Arquétipos">
        ∆<span>7</span>
      </button>
      <nav id="cadial-arch-list"></nav>`;
    document.body.appendChild(panel);

    const list = panel.querySelector("#cadial-arch-list");
    CADIAL.forEach(arch => {
      const btn = document.createElement("button");
      btn.className = "cadial-arch-btn";
      btn.dataset.arch = arch.id;
      btn.title = arch.name + " · " + arch.tag + " · " + arch.hz + "Hz";
      btn.innerHTML = `<span class="cadial-icon">${arch.icon}</span><span class="cadial-lbl">${arch.name}</span>`;
      btn.style.setProperty("--ac", arch.color);
      btn.addEventListener("click", () => {
        openArchSnip(arch);
        // Sincroniza com ENGINE do ZPR se disponível
        if (typeof window.navigateTo === "function") {
          const row = ZPR_MAP.findIndex(r => r.includes(arch.id));
          const col = row >= 0 ? ZPR_MAP[row].indexOf(arch.id) : -1;
          if (row >= 0 && col >= 0) window.navigateTo(row, col);
        }
      });
      list.appendChild(btn);
    });

    // Toggle colapso
    panel.querySelector("#cadial-panel-toggle").addEventListener("click", () => {
      panel.classList.toggle("open");
    });
  }

  /* ── 7. CSS injetado (sem sobrescrever estilos externos) ─────────────*/
  function injectStyles() {
    const s = document.createElement("style");
    s.id = "cadial-coupler-css";
    s.textContent = `
      /* CADIAL Arch Panel */
      #cadial-arch-panel {
        position: fixed;
        right: 0; top: 50%;
        transform: translateY(-50%);
        z-index: var(--z-widget, 500);
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 0;
        transition: transform .3s ease;
      }
      #cadial-panel-toggle {
        background: rgba(8,10,14,.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255,255,255,.1);
        border-right: none;
        border-radius: 10px 0 0 10px;
        color: #C9A84C;
        font-size: 14px;
        font-weight: 900;
        width: 32px;
        padding: 10px 4px;
        cursor: pointer;
        writing-mode: vertical-rl;
        letter-spacing: 2px;
      }
      #cadial-arch-list {
        display: none;
        flex-direction: column;
        gap: 2px;
        background: rgba(5,7,10,.92);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255,255,255,.08);
        border-radius: 10px 0 0 10px;
        padding: 8px 4px;
        max-height: 90vh;
        overflow-y: auto;
      }
      #cadial-arch-panel.open #cadial-arch-list { display: flex; }
      .cadial-arch-btn {
        background: transparent;
        border: 1px solid transparent;
        border-radius: 8px;
        color: var(--ac, #fff);
        font-size: 11px;
        font-weight: 700;
        padding: 6px 10px;
        cursor: pointer;
        display: flex;
        align-items: center;
        gap: 6px;
        white-space: nowrap;
        transition: background .2s, border-color .2s;
        letter-spacing: .5px;
      }
      .cadial-arch-btn:hover {
        background: color-mix(in srgb, var(--ac) 15%, transparent);
        border-color: color-mix(in srgb, var(--ac) 40%, transparent);
      }
      .cadial-icon { font-size: 14px; }
      .cadial-lbl  { opacity: .9; }

      /* Badge sobre células ZPR */
      .screen .cadial-badge { transition: opacity .2s; }
      .screen:hover .cadial-badge { opacity: 0; }
    `;
    document.head.appendChild(s);
  }

  /* ── 8. Init ─────────────────────────────────────────────────────────*/
  function init() {
    injectStyles();
    buildArchPanel();
    injectDockExtras();

    // ZPR constrói o grid assincronamente — esperamos o DOM estar pronto
    // e depois tentamos remapear (com retry se grid ainda não montou)
    let attempts = 0;
    function tryPatch() {
      const screens = document.querySelectorAll("#ZPR .screen");
      if (screens.length > 0) {
        patchZprGrid();
      } else if (attempts++ < 20) {
        setTimeout(tryPatch, 150);
      }
    }
    setTimeout(tryPatch, 300);

    // Expõe API para console/debug
    window.CADIAL = { archetypes: CADIAL, open: openArchSnip, zprMap: ZPR_MAP };
    console.info("∆7 CADIAL Coupler ativo · 12 arquétipos · VERDADE × INTEGRAR ÷ Δ = ∞");
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
