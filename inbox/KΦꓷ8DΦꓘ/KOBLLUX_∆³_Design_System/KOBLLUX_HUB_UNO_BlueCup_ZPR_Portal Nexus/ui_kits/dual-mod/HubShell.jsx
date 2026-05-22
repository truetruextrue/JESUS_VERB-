/* ───────────────────────────────────────────────────────────
   HubShell — the outer chrome
   Header (sticky) + main column. Children render as sections.
   ─────────────────────────────────────────────────────────── */
const { useState } = React;

function HubShell({ children, modelLabel = "claude-sonnet-4-20250514" }) {
  return (
    <div className="hub-root">
      <header className="hub-header">
        <span className="hub-brand">dual.mod — Hub Monolith (v1.1) · Δ³</span>
        <button className="hub-cfg-btn">⚙ API Config</button>
      </header>
      <main className="hub-main">{children}</main>
      <div className="hub-status-strip">
        <span style={{ color: 'var(--cor-0x08)' }}>●</span>
        <span style={{ letterSpacing: '.15em', color: 'var(--muted)' }}>Aguardando · modelo:</span>
        <span style={{ color: 'var(--cor-0x07)', fontFamily: 'var(--font-mono)' }}>{modelLabel}</span>
      </div>
    </div>
  );
}

function HubSection({ title, glyph, opcode, children, accentColor }) {
  return (
    <section className="hub-section" style={accentColor ? { borderLeft: `3px solid ${accentColor}` } : null}>
      <div className="hub-section-head">
        {glyph && <span className="hub-section-glyph" style={{ color: accentColor }}>{glyph}</span>}
        <h2 className="hub-section-title">{title}</h2>
        {opcode && <span className="hub-section-opcode" style={{ borderColor: accentColor + '55', color: accentColor }}>{opcode}</span>}
      </div>
      <div className="hub-section-body">{children}</div>
    </section>
  );
}

Object.assign(window, { HubShell, HubSection });
