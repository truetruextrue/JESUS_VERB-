/* ───────────────────────────────────────────────────────────
   ArchetypeOrb — circular media slot for Nova/Infodose etc.
   ─────────────────────────────────────────────────────────── */

function ArchetypeOrb({ name, role, desc, color, opcode, freq, media, mediaType = 'video' }) {
  return (
    <div className="archetype-tile" style={{ borderColor: color + '33' }}>
      <div
        className="archetype-orb"
        style={{ background: `radial-gradient(circle at center, ${color}33 0%, #000 70%)` }}
      >
        {media ? (
          mediaType === 'video' ? (
            <video
              src={media}
              autoPlay
              loop
              muted
              playsInline
              style={{ borderColor: color + '55', boxShadow: `0 0 24px ${color}55` }}
            />
          ) : (
            <img
              src={media}
              alt={name}
              style={{ borderColor: color + '55', boxShadow: `0 0 24px ${color}55` }}
            />
          )
        ) : (
          <div
            className="archetype-placeholder"
            style={{ background: `radial-gradient(circle, ${color}66 0%, transparent 70%)`, borderColor: color + '55', boxShadow: `0 0 24px ${color}55` }}
          >
            <span style={{ color }}>△</span>
          </div>
        )}
        <span className="archetype-opcode" style={{ color }}>{opcode} · {freq}Hz</span>
      </div>
      <div className="archetype-meta">
        <div className="archetype-name" style={{ color }}>{name}</div>
        <div className="archetype-role">{role}</div>
        <div className="archetype-desc">{desc}</div>
      </div>
    </div>
  );
}

window.ArchetypeOrb = ArchetypeOrb;
