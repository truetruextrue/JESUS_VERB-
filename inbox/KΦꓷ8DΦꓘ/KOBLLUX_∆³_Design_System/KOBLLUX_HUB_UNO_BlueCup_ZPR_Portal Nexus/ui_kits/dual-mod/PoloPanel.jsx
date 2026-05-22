/* ───────────────────────────────────────────────────────────
   PoloPanel — one half of the K↔B Δ Analyzer
   ─────────────────────────────────────────────────────────── */

function PoloPanel({ letter, name, color, langs, defaultLang, value, onChange }) {
  return (
    <div className="polo-panel">
      <div className="polo-header">
        <div className="polo-dot" style={{ background: color, boxShadow: `0 0 6px ${color}` }} />
        <span className="polo-label" style={{ color }}>{letter} · {name}</span>
        <select className="polo-lang" defaultValue={defaultLang}>
          {langs.map(l => <option key={l}>{l}</option>)}
        </select>
      </div>
      <textarea
        className="polo-area"
        value={value}
        onChange={e => onChange(e.target.value)}
        placeholder={`# Polo ${letter} · cole aqui o código`}
      />
      <div className="polo-footer">
        <span style={{ color, fontSize: 'var(--fs-d1)' }}>
          {letter === 'K' ? '⌂' : '≈'} POLO {letter} · {letter === 'K' ? 'x=K=α' : 'y=B=β'}
        </span>
        <span className="polo-chars">{value.length}</span>
      </div>
    </div>
  );
}

window.PoloPanel = PoloPanel;
