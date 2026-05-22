/* ───────────────────────────────────────────────────────────
   App — composes the full Hub surface
   ─────────────────────────────────────────────────────────── */

const { useState, useMemo } = React;

const K_SAMPLE = `# Polo K · Kodux · Tempo
# Pipeline 3-6-9-7

for archetype in arquetipos:
    process(archetype, opcode=0x05)
    if archetype.coherent():
        seal(0x07, freq=777)
        log_delta7(archetype)

# CONVERGIR → SELAR → TESTEMUNHAR
`;

const B_SAMPLE = `<!-- Polo B · Bllue · Espaço -->
<section class="hub-section">
  <h2>⧉ 0x05 · CONVERGIR</h2>
  <div class="metric-cells">
    <span class="opcode-label">SELAR</span>
    <span class="value-hero">1134</span>
  </div>
</section>
`;

/* Local heuristic — computes faux Δ coefficients from length. */
function computeDelta(k, b) {
  const kLen = k.length, bLen = b.length;
  const kCoef = Math.min(100, Math.round(40 + kLen / 12));
  const bCoef = Math.min(100, Math.round(40 + bLen / 12));
  const conv = Math.round((kCoef + bCoef) / 2);
  const ab = ((kCoef * bCoef) / 10000).toFixed(2);
  const sealed = (12 * (kCoef / 100) * (bCoef / 100) * 12).toFixed(2);
  let state = 'NULO';
  if (conv > 80) state = 'CONVERGENTE';
  else if (conv > 65) state = 'SATURADO';
  else if (conv > 45) state = 'EM TRANSIÇÃO';
  else if (conv > 0) state = 'DIVERGENTE';
  const synth = Math.round(conv * 0.85);
  return { kCoef, bCoef, conv, ab, sealed, state, synth };
}

function App() {
  const [kCode, setKCode] = useState(K_SAMPLE);
  const [bCode, setBCode] = useState(B_SAMPLE);
  const [chips, setChips] = useState({ struct: true, sem: true, conv: true, deep: false, synth: false, veeb: false });
  const [showResult, setShowResult] = useState(true);
  const [running, setRunning] = useState(false);

  const r = useMemo(() => computeDelta(kCode, bCode), [kCode, bCode]);

  function toggleChip(k) { setChips(c => ({ ...c, [k]: !c[k] })); }
  function runDelta() {
    setRunning(true);
    setTimeout(() => { setRunning(false); setShowResult(true); }, 900);
  }

  return (
    <HubShell>
      {/* INPUT */}
      <HubSection title="HTML de Entrada" glyph="⌂" opcode="0x00 · INICIAR · 396Hz" accentColor="var(--cor-0x00)">
        <textarea
          className="hub-input-area"
          placeholder="Cole aqui qualquer HTML..."
          defaultValue={`<!DOCTYPE html>\n<html lang="pt-BR">\n  <head>...</head>\n  <body>...</body>\n</html>`}
        />
        <div className="hub-input-controls">
          <button className="btn-secondary">📋 Colar</button>
          <button className="btn-secondary">📂 Importar</button>
          <button className="btn-primary">⚙️ Modularizar + Preview</button>
        </div>
      </HubSection>

      {/* V.E.E.B. */}
      <HubSection title="KOBLLUX V.E.E.B. · Análise do HTML" glyph="⊙" opcode="0x02 · INTEGRAR · 528Hz" accentColor="var(--cor-0x02)">
        <VeebRow values={['432 Hz', '18 módulos', 'χ = 2', 'S = 167']} />
      </HubSection>

      {/* Δ ANALYZER */}
      <HubSection title="Analisador Δ · Convergência de Código" glyph="⧉" opcode="0x05 · CONVERGIR · 672Hz" accentColor="var(--cor-0x05)">
        <EquationBar />
        <div className="polo-grid">
          <PoloPanel
            letter="K" name="Kodux · Tempo" color="var(--polo-k)"
            langs={['Python', 'JavaScript', 'Rust', 'Bash', 'SQL', 'Go', 'C/C++']}
            defaultLang="Python"
            value={kCode} onChange={setKCode}
          />
          <PoloPanel
            letter="B" name="Bllue · Espaço" color="var(--polo-b)"
            langs={['HTML', 'CSS', 'JSON', 'YAML', 'JavaScript', 'TypeScript']}
            defaultLang="HTML"
            value={bCode} onChange={setBCode}
          />
        </div>

        <div className="camadas-row">
          <span className="label-uc" style={{ fontSize: 'var(--fs-d2)', color: 'var(--muted)' }}>CAMADAS:</span>
          <OpcodeChip label="ESTRUTURA"    on={chips.struct} onClick={() => toggleChip('struct')} />
          <OpcodeChip label="SEMÂNTICA"    on={chips.sem}    onClick={() => toggleChip('sem')} />
          <OpcodeChip label="CONVERGÊNCIA" on={chips.conv}   onClick={() => toggleChip('conv')} />
          <OpcodeChip label="Δ PROFUNDO"   on={chips.deep}   onClick={() => toggleChip('deep')} />
          <OpcodeChip label="SÍNTESE"      on={chips.synth}  onClick={() => toggleChip('synth')} />
          <OpcodeChip label="V.E.E.B."     on={chips.veeb}   onClick={() => toggleChip('veeb')} />
        </div>

        <DeltaButton running={running} onClick={runDelta}>
          {running ? '0x05 · CONVERGINDO · transduzindo camadas…' : '⧉ · 0x05 · CONVERGIR · CALCULAR Δ'}
        </DeltaButton>

        {showResult && (
          <div className="delta-result show">
            <div className="dr-header">
              <span className="dr-title">Δ · RELATÓRIO DE CONVERGÊNCIA · 12_K×B_12</span>
              <span className={`dr-badge ${r.conv > 70 ? 'high' : r.conv > 50 ? 'med' : 'low'}`}>
                {r.state}
              </span>
            </div>
            <MetricCells
              ck={r.kCoef} cb={r.bCoef} conv={r.conv} ab={r.ab}
              sealed={r.sealed} state={r.state}
            />
            <MetricBars ck={r.kCoef} cb={r.bCoef} conv={r.conv} synth={r.synth} />
            <div className="dr-vis">
              <div className="dr-vis-node"><span className="dr-vis-sym" style={{ color: 'var(--polo-k)' }}>⌂</span><span>KODUX · K</span><span style={{ color: 'var(--polo-k)' }}>{r.kCoef}</span></div>
              <span className="dr-vis-op">×</span>
              <div className="dr-vis-node"><span className="dr-vis-sym" style={{ color: 'var(--cor-0x07)' }}>△</span><span>DELTA</span><span style={{ color: 'var(--cor-0x07)' }}>{r.conv}%</span></div>
              <span className="dr-vis-op">×</span>
              <div className="dr-vis-node"><span className="dr-vis-sym" style={{ color: 'var(--polo-b)' }}>≈</span><span>BLLUE · B</span><span style={{ color: 'var(--polo-b)' }}>{r.bCoef}</span></div>
              <span className="dr-vis-op">=</span>
              <div className="dr-vis-node"><span className="dr-vis-sym" style={{ color: 'var(--cor-0x01)' }}>∞</span><span>CONVERGÊNCIA</span><span style={{ color: 'var(--cor-0x01)' }}>{r.ab}</span></div>
            </div>
          </div>
        )}
      </HubSection>

      {/* GENERATED FILES */}
      <HubSection title="Arquivos Gerados" glyph="✧" opcode="0x07 · SELAR · 777Hz" accentColor="var(--cor-0x07)">
        <FileCard
          path="dual-mod/index.html" code="0x00" name="iniciar" color="#b978ff" freq="396"
          preview={`<!DOCTYPE html>\n<html lang="pt-BR">\n  <head><link rel="stylesheet" href="./css/main.css"></head>\n  ...`}
        />
        <FileCard
          path="dual-mod/js/L5_0x09_processHTML_E_D6.js" code="0x09" name="manifestar" color="#6c5ce7" freq="963"
          preview={`/* ═══ 0x09 · MANIFESTAR · S² · 963Hz ═══ */\nfunction processHTML() {\n  const doc = new DOMParser()...`}
        />
        <FileCard
          path="dual-mod/css/0x06_cristalizar_V_D2.css" code="0x06" name="cristalizar" color="#a8ff78" freq="741"
          preview={`/* ═══ 0x06 · CRISTALIZAR · ☯ · 741Hz ═══ */\n.glass { backdrop-filter: blur(50px); }`}
        />
        <FileCard
          path="dual-mod/0x07_selar_B_D3_manifest.json" code="0x07" name="selar" color="#ffd700" freq="777"
          preview={`{\n  "kobllux": { "opcode": "0x07", "freq": 777 },\n  "law": "VERDADE×INTEGRAR÷Δ=∞"\n}`}
        />
      </HubSection>

      {/* ARCHETYPES */}
      <HubSection title="Arquétipos CADIAL · Roda Viva" glyph="△" opcode="0x09 · MANIFESTAR · 963Hz" accentColor="var(--cor-0x09)">
        <div className="archetype-grid">
          <ArchetypeOrb
            name="Nova" role="Inspira · semente" desc="Inspiração viva brota do silêncio eterno."
            color="#67e6ff" opcode="0x01" freq="432"
            media={(window.__resources && window.__resources.novaGif) || "../../assets/archetypes/nova.gif"} mediaType="image"
          />
          <ArchetypeOrb
            name="Infodose" role="Verbo · tradução" desc="Tradução simbólica, técnica e econômica."
            color="#ff7a00" opcode="0x05" freq="672"
            media={(window.__resources && window.__resources.infodoseMp4) || "../../assets/archetypes/infodose.mp4"}
          />
          <ArchetypeOrb
            name="Atlas" role="Planejador · estrutura" desc="Eu organizo o fluxo com sabedoria cósmica."
            color="#b978ff" opcode="0x00" freq="396"
          />
        </div>
      </HubSection>

      {/* DNA TABLE */}
      <HubSection title="Δ DNA SCALAR · 13 Opcodes" glyph="∞" opcode="0x0C · CONCLUIR · 999Hz" accentColor="var(--cor-0x0C)">
        <OpcodeTable />
      </HubSection>
    </HubShell>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);
