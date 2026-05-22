/* ───────────────────────────────────────────────────────────
   MetricCells — 6-cell coefficient grid
   ─────────────────────────────────────────────────────────── */

function MetricCells({ ck, cb, conv, ab, sealed, state }) {
  const cells = [
    { lbl: 'Coef. K', val: ck, sub: 'Estrutura/Lógica', color: 'var(--polo-k)' },
    { lbl: 'Coef. B', val: cb, sub: 'Interface/Fluxo', color: 'var(--polo-b)' },
    { lbl: 'Δ Convergência', val: conv + '%', sub: 'K×B / Δ', color: 'var(--cor-0x07)' },
    { lbl: 'α × β', val: ab, sub: 'Simetria Dual', color: 'var(--cor-0x01)' },
    { lbl: '12_K×B_12', val: sealed, sub: 'Fórmula Selada', color: 'var(--cor-0x0B)' },
    { lbl: 'Estado Δ', val: state, sub: 'Sistema', color: 'var(--cor-0x07)' }
  ];
  return (
    <div className="metric-cells">
      {cells.map(c => (
        <div key={c.lbl} className="metric-cell">
          <span className="metric-lbl">{c.lbl}</span>
          <span className="metric-val" style={{ color: c.color }}>{c.val}</span>
          <span className="metric-sub">{c.sub}</span>
        </div>
      ))}
    </div>
  );
}

function MetricBars({ ck, cb, conv, synth }) {
  const bars = [
    { lbl: 'K · ESTRUTURA', pct: ck, color: 'var(--polo-k)' },
    { lbl: 'B · SEMÂNTICA', pct: cb, color: 'var(--polo-b)' },
    { lbl: 'Δ · CONVERGÊNCIA', pct: conv, color: 'var(--cor-0x07)' },
    { lbl: '∞ · SÍNTESE', pct: synth, color: 'var(--cor-0x01)' }
  ];
  return (
    <div className="metric-bars">
      {bars.map(b => (
        <div key={b.lbl} className="bar-row">
          <span className="bar-lbl" style={{ color: b.color }}>{b.lbl}</span>
          <div className="bar-track">
            <div className="bar-fill" style={{ width: b.pct + '%', background: b.color }} />
          </div>
          <span className="bar-pct">{b.pct}%</span>
        </div>
      ))}
    </div>
  );
}

Object.assign(window, { MetricCells, MetricBars });
