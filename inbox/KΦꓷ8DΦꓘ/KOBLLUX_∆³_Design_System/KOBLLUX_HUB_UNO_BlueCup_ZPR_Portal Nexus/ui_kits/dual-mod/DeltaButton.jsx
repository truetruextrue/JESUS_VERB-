/* ───────────────────────────────────────────────────────────
   DeltaButton — the gold "CONVERGIR · CALCULAR Δ" CTA
   ─────────────────────────────────────────────────────────── */

function DeltaButton({ running, onClick, disabled, children }) {
  return (
    <button
      className={`btn-delta ${running ? 'running' : ''}`}
      onClick={onClick}
      disabled={disabled}
    >
      {children || '⧉ · 0x05 · CONVERGIR · CALCULAR Δ'}
    </button>
  );
}

window.DeltaButton = DeltaButton;
