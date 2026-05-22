/* ───────────────────────────────────────────────────────────
   FileCard — a generated-file row + opcode left-border
   ─────────────────────────────────────────────────────────── */

function FileCard({ path, code, name, color, freq, preview }) {
  const [copied, setCopied] = React.useState(false);
  return (
    <div className="file-card" style={{ borderLeft: `3px solid ${color}` }}>
      <div className="file-card-head">
        <span className="file-card-path" style={{ color }}>{path}</span>
        <span className="file-card-badge" style={{ borderColor: `${color}55`, color }}>
          {code} · {name} · {freq}Hz
        </span>
        <button
          className="file-card-copy"
          onClick={() => { setCopied(true); setTimeout(() => setCopied(false), 1500); }}
        >
          {copied ? '✓ Copiado' : '⊙ Copiar'}
        </button>
      </div>
      {preview && <pre className="file-card-preview">{preview}</pre>}
    </div>
  );
}

window.FileCard = FileCard;
