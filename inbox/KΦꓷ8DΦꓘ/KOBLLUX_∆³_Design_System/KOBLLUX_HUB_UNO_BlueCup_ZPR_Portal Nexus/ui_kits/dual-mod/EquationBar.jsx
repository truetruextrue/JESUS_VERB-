/* ───────────────────────────────────────────────────────────
   EquationBar — the Δ equation strip
   K · Kodux · Tempo  ↔  Δ  ↔  B · Bllue · Espaço
   ─────────────────────────────────────────────────────────── */

function EquationBar() {
  return (
    <div className="eq-bar">
      <span style={{ color: 'var(--polo-k)', fontSize: 'var(--fs-d2)' }}>K · Kodux · Tempo · 1×2=α</span>
      <span className="eq-sep">↔</span>
      <span style={{ color: 'var(--cor-0x07)', fontSize: 'var(--fs-d5)' }}>Δ</span>
      <span className="eq-sep">↔</span>
      <span style={{ color: 'var(--polo-b)', fontSize: 'var(--fs-d2)' }}>B · Bllue · Espaço · 2÷1=β</span>
      <span className="eq-sep">·</span>
      <span style={{ color: 'var(--cor-0x07)', fontSize: 'var(--fs-d2)' }}>12_K_×_B_12</span>
      <span className="eq-sep">·</span>
      <span style={{ color: 'var(--cor-0x01)', fontSize: 'var(--fs-d2)' }}>VERDADE×INTEGRAR÷Δ=∞</span>
    </div>
  );
}

window.EquationBar = EquationBar;
