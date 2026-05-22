/* SÜMBÜS FUSION · ΔUAL 3.0 — editor surface */
const { useState: useStateF } = React;

function FusionTabs({ active, setActive }) {
  const tabs = [
    { id: "html", name: "index", ext: "html", icon: "📄" },
    { id: "css",  name: "style", ext: "css",  icon: "🎨" },
    { id: "js",   name: "kobllux", ext: "js", icon: "⚡" },
  ];
  return (
    <div className="fusion-tabs">
      {tabs.map(t => (
        <div key={t.id} className={"ftab " + (active === t.id ? "active" : "")}
             onClick={() => setActive(t.id)}>
          <span>{t.icon}</span>
          <span>{t.name}.</span>
          <span className="ext">{t.ext}</span>
        </div>
      ))}
    </div>
  );
}

function FusionToolbar() {
  const btns = ["↶","↷","≡","↩","⌫"];
  return (
    <div className="fusion-toolbar">
      {btns.map((b, i) => <button key={i} className="toolbtn">{b}</button>)}
      <span className="spacer"/>
      <button className="save-btn">⚡ SALVAR · FUSÃO</button>
    </div>
  );
}

const SAMPLES = {
  html: [
    [`<span class="tk-com">&lt;!-- KOBLLUX_VIVO ∆³ · 369 --&gt;</span>`],
    [`<span class="tk-tag">&lt;html</span> <span class="tk-attr">lang</span>=<span class="tk-str">"pt-BR"</span> <span class="tk-attr">data-frequency</span>=<span class="tk-str">"369"</span><span class="tk-tag">&gt;</span>`],
    [`<span class="tk-tag">&lt;head&gt;</span>`],
    [`  <span class="tk-tag">&lt;meta</span> <span class="tk-attr">charset</span>=<span class="tk-str">"UTF-8"</span><span class="tk-tag">&gt;</span>`],
    [`  <span class="tk-tag">&lt;title&gt;</span>SÜMBÜS FUSION<span class="tk-tag">&lt;/title&gt;</span>`],
    [`<span class="tk-tag">&lt;/head&gt;</span>`],
    [`<span class="tk-tag">&lt;body</span> <span class="tk-attr">data-organism</span>=<span class="tk-str">"sumbus"</span><span class="tk-tag">&gt;</span>`],
    [`  <span class="tk-tag">&lt;div</span> <span class="tk-attr">class</span>=<span class="tk-str">"nebula-layer"</span><span class="tk-tag">&gt;&lt;/div&gt;</span>`],
    [`  <span class="tk-tag">&lt;main&gt;</span>VERDADE × INTEGRAR ÷ Δ = ∞<span class="tk-tag">&lt;/main&gt;</span>`],
    [`<span class="tk-tag">&lt;/body&gt;</span>`],
    [`<span class="tk-tag">&lt;/html&gt;</span>`],
  ],
  css: [
    [`<span class="tk-com">/* ⚡ 369 · 528 · 963 — trinity */</span>`],
    [`<span class="tk-css-sel">:root</span> {`],
    [`  <span class="tk-css-prop">--primary</span>: <span class="tk-css-val">#00f5ff</span>;`],
    [`  <span class="tk-css-prop">--secondary</span>: <span class="tk-css-val">#ff4bff</span>;`],
    [`  <span class="tk-css-prop">--tertiary</span>: <span class="tk-css-val">#ffd700</span>;`],
    [`}`],
    [``],
    [`<span class="tk-css-sel">.brand</span> {`],
    [`  <span class="tk-css-prop">background</span>: <span class="tk-css-val">linear-gradient(135deg, var(--primary), var(--secondary))</span>;`],
    [`  <span class="tk-css-prop">color</span>: <span class="tk-css-val">transparent</span> <span class="tk-imp">!important</span>;`],
    [`  <span class="tk-css-prop">animation</span>: <span class="tk-css-val">pulse 6s ease-in-out infinite</span>;`],
    [`}`],
  ],
  js: [
    [`<span class="tk-com">// VEEB · 12 archetypes data bus</span>`],
    [`<span class="tk-key">const</span> <span class="tk-fn">KOBLLUX</span> = {`],
    [`  <span class="tk-attr">atlas</span>:   { <span class="tk-attr">hz</span>: <span class="tk-num">768</span>, <span class="tk-attr">verb</span>: <span class="tk-str">"STRUCTURE"</span> },`],
    [`  <span class="tk-attr">vitalis</span>: { <span class="tk-attr">hz</span>: <span class="tk-num">528</span>, <span class="tk-attr">verb</span>: <span class="tk-str">"ENERGIZE"</span> },`],
    [`  <span class="tk-attr">genus</span>:   { <span class="tk-attr">hz</span>: <span class="tk-num">852</span>, <span class="tk-attr">verb</span>: <span class="tk-str">"SYNTH"</span> },`],
    [`  <span class="tk-attr">lumine</span>:  { <span class="tk-attr">hz</span>: <span class="tk-num">963</span>, <span class="tk-attr">verb</span>: <span class="tk-str">"RENDER"</span> },`],
    [`};`],
    [``],
    [`<span class="tk-key">function</span> <span class="tk-fn">pulse</span>(arch) {`],
    [`  <span class="tk-key">return</span> KOBLLUX[arch].hz / <span class="tk-num">3</span>;`],
    [`}`],
  ],
};

function EditorPane({ active }) {
  const lines = SAMPLES[active] || SAMPLES.html;
  return (
    <div className="editor-pane">
      <div className="linenums">
        {lines.map((_, i) => <div key={i}>{i + 1}</div>)}
      </div>
      <div className="code">
        {lines.map((tokens, i) => (
          <div key={i} dangerouslySetInnerHTML={{ __html: tokens[0] }} />
        ))}
      </div>
    </div>
  );
}

function FusionStatusbar({ active }) {
  return (
    <div className="fusion-statusbar">
      <span className="pill live">● LIVE</span>
      <span>{active.toUpperCase()}</span>
      <span>UTF-8</span>
      <span>Ln 1, Col 1</span>
      <span className="ml">GENUS · 852Hz · SYNTH</span>
    </div>
  );
}

function FusionEditor() {
  const [active, setActive] = useStateF("html");
  return (
    <div className="fusion-shell">
      <FusionTabs active={active} setActive={setActive}/>
      <FusionToolbar/>
      <EditorPane active={active}/>
      <FusionStatusbar active={active}/>
    </div>
  );
}

Object.assign(window, { FusionEditor, FusionTabs, FusionToolbar, EditorPane, FusionStatusbar });
