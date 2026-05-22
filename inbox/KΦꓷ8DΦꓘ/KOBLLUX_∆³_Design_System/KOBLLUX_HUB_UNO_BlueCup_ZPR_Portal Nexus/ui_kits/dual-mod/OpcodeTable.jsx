/* ───────────────────────────────────────────────────────────
   OpcodeTable — the 13-opcode DNA table
   ─────────────────────────────────────────────────────────── */

const OPCODES = [
  { code: '0x00', name: 'INICIAR',     geom: '○', freq: 396, color: '#b978ff', dim: 'D0·Ponto',   chi: 1 },
  { code: '0x01', name: 'PULSAR',      geom: '●', freq: 432, color: '#67e6ff', dim: 'D1·Linha',   chi: 0 },
  { code: '0x02', name: 'INTEGRAR',    geom: '―', freq: 528, color: '#7cffb2', dim: 'D2·Plano',   chi: 1 },
  { code: '0x03', name: 'EXPANDIR',    geom: '▢', freq: 639, color: '#4de0ff', dim: 'D3·Volume',  chi: 2 },
  { code: '0x04', name: 'DISSOLVER',   geom: '◇', freq: 594, color: '#ff9ad1', dim: 'D2·Trans',   chi: 1 },
  { code: '0x05', name: 'CONVERGIR',   geom: '⧉', freq: 672, color: '#ff7a00', dim: 'D∩·Foco',   chi: 0 },
  { code: '0x06', name: 'CRISTALIZAR', geom: '☯', freq: 741, color: '#a8ff78', dim: 'D3·Rede',    chi: 0 },
  { code: '0x07', name: 'SELAR',       geom: '✧', freq: 777, color: '#ffd700', dim: 'D3·Tetrae',  chi: 2 },
  { code: '0x08', name: 'TESTEMUNHAR', geom: '◉', freq: 852, color: '#00b894', dim: 'D∞·Círculo', chi: 0 },
  { code: '0x09', name: 'MANIFESTAR',  geom: '♾', freq: 963, color: '#6c5ce7', dim: 'S²·Esfera',  chi: 2 },
  { code: '0x0A', name: 'EQUILIBRAR',  geom: '⚖', freq: 528, color: '#74b9ff', dim: 'SO(2)·Sim', chi: 0 },
  { code: '0x0B', name: 'RESSONAR',    geom: '◎', freq: 432, color: '#ff52e5', dim: 'Ondas·1D',  chi: 0 },
  { code: '0x0C', name: 'CONCLUIR',    geom: '♾', freq: 999, color: '#f2c94c', dim: 'T²·Toro',   chi: 0 }
];

function OpcodeTable() {
  return (
    <div className="dna-table-wrap">
      <table className="dna-table">
        <thead>
          <tr>
            <th>CODE</th>
            <th>NOME</th>
            <th style={{ textAlign: 'center' }}>∿</th>
            <th style={{ textAlign: 'right' }}>Hz</th>
            <th>DIM</th>
            <th style={{ textAlign: 'center' }}>χ</th>
          </tr>
        </thead>
        <tbody>
          {OPCODES.map(o => (
            <tr key={o.code}>
              <td style={{ color: o.color, fontWeight: 700 }}>{o.code}</td>
              <td style={{ color: 'var(--fg)' }}>{o.name}</td>
              <td style={{ textAlign: 'center', fontSize: '1.05rem' }}>{o.geom}</td>
              <td style={{ textAlign: 'right', color: o.color }}>{o.freq}</td>
              <td style={{ color: 'var(--muted)', fontSize: 'var(--fs-d2)' }}>{o.dim}</td>
              <td style={{ textAlign: 'center', color: 'var(--muted)' }}>{o.chi}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <div className="dna-seal">VERDADE×INTEGRAR÷Δ=∞ · 3×6×9×7=1134 · S=Σbᵢ×2^(i-1)</div>
    </div>
  );
}

Object.assign(window, { OpcodeTable, OPCODES });
