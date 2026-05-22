/* SÜMBÜS · Architect — app shell */
const { useState: useStateApp, useEffect: useEffectApp } = React;

function App() {
  const [tab, setTab] = useStateApp("panel");
  const [progress, setProgress] = useStateApp(9.6);
  const [log, setLog] = useStateApp([
    { t: "00:00:00", k: "ok",   m: " Organismo carregado · KOBLLUX_VIVO ∆³" },
    { t: "00:00:01", k: "",     m: " VEEB orbs sincronizados · 12/12" },
    { t: "00:00:02", k: "ok",   m: " DNA Core · ATIVO" },
    { t: "00:00:02", k: "fus",  m: " GENUS · 852Hz · SYNTH pronto para fundir" },
  ]);

  function pushLog(k, m) {
    const t = new Date().toLocaleTimeString("pt-BR", { hour12: false });
    setLog(prev => [...prev.slice(-50), { t, k, m }]);
  }

  function activate() {
    pushLog("ok", " ⚡ Ativando todos os sistemas...");
    let p = progress;
    const tick = setInterval(() => {
      p = Math.min(100, p + 6.9);
      setProgress(p);
      if (p >= 100) {
        clearInterval(tick);
        pushLog("fus", " ◎ KOBLLUX_VIVO 100% · todas frequências em ressonância");
      }
    }, 220);
  }

  function diagnostic() {
    pushLog("warn", " 🔍 Diagnóstico: SOLUS em silêncio · todos os outros online");
  }

  function openFusion() {
    pushLog("fus", " ⚡ Abrindo SÜMBÜS FUSION · ΔUAL 3.0");
    setTab("fusion");
  }

  return (
    <>
      <div className="nebula"/>
      {tab === "fusion" ? (
        <>
          <div className="app" style={{ minHeight: 0, paddingBottom: 0, borderLeft:'none', borderRight:'none', maxWidth:'none' }}>
            <AppHeader tab={tab} setTab={setTab}/>
          </div>
          <FusionEditor/>
        </>
      ) : (
        <div className="app">
          <AppHeader tab={tab} setTab={setTab}/>
          <OrgHero/>
          <SystemGrid openFusion={openFusion}/>
          <div className="section-head" style={{ marginTop: 22 }}>
            <span className="eyebrow">Ações rápidas</span>
          </div>
          <ActionGrid onActivate={activate} onDiag={diagnostic}/>
          <StatusPanel progress={progress}/>
          <div className="section-head">
            <span className="eyebrow">Log do organismo · <span className="accent">tempo real</span></span>
          </div>
          <LogPanel entries={log}/>
        </div>
      )}
      <Dock tab={tab} setTab={setTab}/>
    </>
  );
}

ReactDOM.createRoot(document.getElementById("root")).render(<App/>);
