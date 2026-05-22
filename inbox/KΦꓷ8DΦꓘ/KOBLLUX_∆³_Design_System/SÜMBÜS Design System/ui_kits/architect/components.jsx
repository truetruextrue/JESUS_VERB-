/* SÜMBÜS · Architect Control Panel · components */
const { useState, useEffect, useRef } = React;

/* ─────────── HEADER ─────────── */
function AppHeader({ tab, setTab }) {
  return (
    <header className="app-header">
      <div className="brand">
        ⚡ SÜMBÜS
        <span className="brand-kobllux">∆³ KOBLLUX</span>
      </div>
      <div className="trinity-nav">
        <button className={tab === "panel" ? "active" : ""} onClick={() => setTab("panel")}>Painel</button>
        <button className={tab === "fusion" ? "active" : ""} onClick={() => setTab("fusion")}>FUSÃO</button>
      </div>
      <div className="status-mini">
        <span className="dot" />
        <span>963Hz</span>
      </div>
    </header>
  );
}

/* ─────────── ORG HERO ─────────── */
function OrgHero() {
  return (
    <section className="org-hero">
      <h1 className="org-title">SÜMBÜS METAHUMAN<br/>ARCHITECT</h1>
      <div className="org-subtitle">Organismo Digital Fractal · DNA KOBLLUX · 3-6-9</div>
      <div className="freq-row"><span/><span/><span/></div>
      <div className="org-meta">
        <span>✅ <b>ATIVO</b></span>
        <span>·</span>
        <span>Progresso: <b>9.6%</b></span>
        <span>·</span>
        <span>Frequência: <b>963Hz</b></span>
      </div>
    </section>
  );
}

/* ─────────── SYSTEM CARD ─────────── */
function SystemCard({ icon, name, hueClass, body, status = "✅ ATIVO", statusVariant, fusion, onClick }) {
  const cls = ["system-card"];
  if (fusion) cls.push("fusion");
  return (
    <div className={cls.join(" ")} onClick={onClick}>
      <span className="icon">{icon}</span>
      <h3 className={hueClass}>{name}</h3>
      <p>{body}</p>
      <span className={"status-pill " + (statusVariant || "")}>{status}</span>
    </div>
  );
}

/* ─────────── SYSTEM GRID ─────────── */
function SystemGrid({ openFusion }) {
  return (
    <>
      <div className="section-head">
        <span className="eyebrow">Sistemas vitais · <span className="accent">11/11 online</span></span>
        <span className="eyebrow">⬡ 12/12</span>
      </div>
      <div className="system-grid">
        <SystemCard icon="🧬" name="DNA CORE" hueClass="h3-atlas"
          body="Código genético. Identidade e frequências fundamentais." />
        <SystemCard icon="🧠" name="NERVOSO" hueClass="h3-pulse"
          body="Interface e controle neural. Processa interações." />
        <SystemCard icon="🌀" name="SÍNTESE" hueClass="h3-vitalis"
          body="Fusão e integração de camadas DNA. GENUS · 852Hz." />
        <SystemCard icon="👁️" name="RENDER" hueClass="h3-atlas"
          body="Sistema visual fractal. Partículas e animações. LUMINE · 963Hz." />
        <SystemCard icon="🔄" name="CIRCULATÓRIO" hueClass="h3-vitalis"
          body="Fluxo de dados e APIs. VITALIS+RHEA · 528Hz · DELTA+INTEGRATE." />
        <SystemCard icon="⚡" name="ENDÓCRINO" hueClass="h3-pulse"
          body="Equilíbrio hormonal. SERENA+KAOS · 528/777Hz · GUARD+CLEAN." />
        <SystemCard icon="🏃" name="MOTOR" hueClass="h3-atlas"
          body="Execução de ações. ARTEMIS+VITALIS · 672/528Hz · DETECT+DELTA." />
        <SystemCard icon="⬡" name="RODA VIVA" hueClass="h3-lumine"
          body="12 arquétipos CADIAL vivos. JESUS=VERBO=GRAVIDADE." status="✅ KOBLLUX_VIVO" statusVariant="alt" />
        <SystemCard icon="🌐" name="REPO" hueClass="h3-rhea"
          body="Árvore viva do repositório. Commits, upload, Actions." status="✅ GITHUB API" />
        <SystemCard icon="📚" name="LIBRARY · CODEX" hueClass="h3-lumine"
          body="96 HTML · 225 PY · 185 JS · 136 JSON. LUMINE · 963Hz." status="✅ 642+ ARQUIVOS" statusVariant="alt" />
        <SystemCard icon="⚡" name="SÜMBÜS FUSION · ΔUAL 3.0" hueClass="h3-fusion" fusion
          body="Editor de código vivo com acesso ao repositório. Selecione arquivos do REPO e funda CSS · JS · HTML inteligentemente. GENUS (852Hz) · SYNTH"
          status="ED · VIEW · LOG · RAM · REPO · FUSÃO" statusVariant="fusion"
          onClick={openFusion}/>
      </div>
    </>
  );
}

/* ─────────── ACTION GRID ─────────── */
function ActionGrid({ onActivate, onDiag }) {
  return (
    <div className="action-grid">
      <button className="action-btn primary" onClick={onActivate}>⚡ ATIVAR TODOS OS SISTEMAS</button>
      <button className="action-btn" onClick={onDiag}>🔍 DIAGNÓSTICO</button>
      <button className="action-btn">🔄 ATUALIZAR DNA</button>
    </div>
  );
}

/* ─────────── VEEB ORB ─────────── */
function Veeb({ name, code, color }) {
  return (
    <span className="veeb">
      <span className="vdot" style={{ background: color, boxShadow: `0 0 8px ${color}` }} />
      <span className="vtxt" style={{ color }}>{name}·{code}</span>
    </span>
  );
}

/* ─────────── STATUS PANEL ─────────── */
function StatusPanel({ progress = 36 }) {
  const archs = [
    ["ATLAS","B","#3b82f6"],["NOVA","B","#f59e0b"],["VITALIS","E","#10b981"],["PULSE","V","#8b5cf6"],
    ["ARTEMIS","E","#06b6d4"],["SERENA","V","#ec4899"],["KAOS","B","#ef4444"],["GENUS","E","#a855f7"],
    ["LUMINE","V","#fbbf24"],["SOLUS","B","#64748b"],["RHEA","E","#34d399"],["AION","V","#818cf8"],
  ];
  return (
    <div className="status-panel">
      <h4>📊 Status do organismo · KOBLLUX_VIVO_∆³</h4>
      <div className="metric-row">
        <div className="metric vitalis"><div className="lbl">Sistemas</div><div className="val">11/11</div></div>
        <div className="metric pulse"><div className="lbl">Arquétipos</div><div className="val">12/12</div></div>
        <div className="metric atlas"><div className="lbl">Arquivos</div><div className="val">24/250</div></div>
        <div className="metric lumine"><div className="lbl">Frequência</div><div className="val">963Hz</div></div>
      </div>
      <div className="arch-bar">
        {archs.map(([n,c,col]) => <Veeb key={n} name={n} code={c} color={col}/>)}
      </div>
      <div className="progress-meta">
        <span>Implementação do organismo</span>
        <b>{progress.toFixed(1)}%</b>
      </div>
      <div className="progress"><div className="fill" style={{ width: progress + "%" }} /></div>
    </div>
  );
}

/* ─────────── LOG PANEL ─────────── */
function LogPanel({ entries }) {
  const ref = useRef(null);
  useEffect(() => { if (ref.current) ref.current.scrollTop = ref.current.scrollHeight; }, [entries.length]);
  return (
    <div className="log-panel" ref={ref}>
      {entries.map((e, i) => (
        <div key={i} className={"log-entry " + (e.k || "")}>
          <span className="t">[{e.t}]</span>{e.m}
        </div>
      ))}
    </div>
  );
}

/* ─────────── DOCK ─────────── */
function Dock({ tab, setTab }) {
  const items = [
    ["panel",  "🧬", "DNA"],
    ["sys",    "🧠", "Sys"],
    ["repo",   "🌐", "Repo"],
    ["fusion", "⚡", "Fusão"],
    ["log",    "📊", "Log"],
  ];
  return (
    <nav className="dock">
      <div className="dock-app">
        {items.map(([k, ic, lbl]) => (
          <button key={k}
            className={"dock-btn " + (tab === k ? "active" : "")}
            onClick={() => setTab(k)}>
            <span className="ic">{ic}</span>
            <span className="lbl">{lbl}</span>
          </button>
        ))}
      </div>
    </nav>
  );
}

Object.assign(window, {
  AppHeader, OrgHero, SystemCard, SystemGrid, ActionGrid, StatusPanel, LogPanel, Veeb, Dock,
});
