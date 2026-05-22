/* ───────────────────────────────────────────────────────────
   VeebRow — V.E.E.B. layer cards (V/E/E/B)
   ─────────────────────────────────────────────────────────── */

const VEEB_LAYERS = [
  { letter: 'V', name: 'Vibração', eq: 'f = 432 + 7.83·sin(θ)', color: '#00e5ff' },
  { letter: 'E', name: 'Energia', eq: 'E = ∫₀ᵀ Φ(t)·ω(t)dt', color: '#f0c060' },
  { letter: 'E', name: 'Estrutura', eq: 'χ = V−E+F', color: '#8b5cf6' },
  { letter: 'B', name: 'Base', eq: 'S = Σ bᵢ × 2^(i-1)', color: '#39ff5a' }
];

function VeebRow({ values = ['432 Hz', '— mód.', 'χ = 0', 'S = 0'] }) {
  return (
    <div className="veeb-row">
      {VEEB_LAYERS.map((l, i) => (
        <div key={i} className="veeb-cell" style={{ borderColor: l.color + '33', borderLeftColor: l.color }}>
          <div className="veeb-label" style={{ color: l.color }}>{l.letter} · {l.name}</div>
          <div className="veeb-val">{values[i]}</div>
          <div className="veeb-eq">{l.eq}</div>
        </div>
      ))}
    </div>
  );
}

window.VeebRow = VeebRow;
