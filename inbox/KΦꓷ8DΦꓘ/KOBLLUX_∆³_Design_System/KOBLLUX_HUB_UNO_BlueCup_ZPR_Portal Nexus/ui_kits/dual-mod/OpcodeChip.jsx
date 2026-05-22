/* ───────────────────────────────────────────────────────────
   OpcodeChip — toggleable camada chip + identity badge
   ─────────────────────────────────────────────────────────── */

function OpcodeChip({ label, on, onClick, color = 'var(--cor-0x01)' }) {
  return (
    <button
      className={`op-chip ${on ? 'on' : ''}`}
      style={on ? {
        borderColor: color,
        color: color,
        background: color === 'var(--cor-0x01)' ? 'rgba(103,230,255,0.07)' : `${color}10`
      } : null}
      onClick={onClick}
    >
      {label}
    </button>
  );
}

function OpcodeBadge({ code, name, color, freq }) {
  return (
    <span
      className="opcode-badge"
      style={{ borderColor: `${color}55`, color }}
    >
      {code} · {name} · {freq}Hz
    </span>
  );
}

Object.assign(window, { OpcodeChip, OpcodeBadge });
