/* ═══════════════════════════════════════════════════════════
   0x0B · RESSONAR · E2 · D4
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-particle-cosmos-3-6-9-logger/js/L2_0x0B_a_E2_D4.js
   Opcode    : 0x0B · RESSONAR · ◎ · 432Hz
   V.E.E.B.  : Estrutura
   Degrau    : D4 (engine)
   Fórmula   : Estrutura · f_B=432Hz · ressonância UI · nós e ventres
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 2 · REGISTRO
   Opcode Δ  : 0x08 · Carregar na posição 2 da cadeia
   Nota      : Log + identidade — sem DOM
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=432)
     χ = 0  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function applyArchetype(idx) {
    currentArchIdx = (idx + ARCHETYPES_DB.length) % ARCHETYPES_DB.length;
    const a = ARCHETYPES_DB[currentArchIdx];
    const op = KOBLLUX_OPCODES[a.opcode];

    document.documentElement.style.setProperty('--arch-primary',   a.primary);
    document.documentElement.style.setProperty('--arch-secondary', op.cor);
    document.documentElement.style.setProperty('--arch-glow',      a.primary);

    $('#archName').textContent  = a.name;
    $('#archDesc').textContent  = a.desc;
    $('#archCounter').textContent = String(currentArchIdx + 1).padStart(2, '0') + '/' + String(ARCHETYPES_DB.length).padStart(2, '0');

    $('#metaOpcode').textContent = a.opcode;
    $('#metaVerb').textContent   = op.nome;
    $('#metaGeom').textContent   = op.geom;
    $('#metaFreq').textContent   = op.freq + 'Hz';
    $('#metaDim').textContent    = op.dim;

    $('#avatarGlyph').textContent   = op.geom;
    $('#collapsedGlyph').textContent = op.geom;

    // Activation seed
    const userName = localStorage.getItem('di_userName') || 'Convidado';
    $('#actPre').textContent =
      `[${a.name}·${a.opcode}·${op.nome}·${op.freq}Hz·${op.dim}]\n` +
      `> ${a.drk}\n` +
      `> bind ${userName} → ${a.id}.activate()\n` +
      `> S(${a.id}) = Σbᵢ·2^(i-1)  ·  geom: ${op.geom}\n` +
      `> primary:${a.primary}  · opcode:${op.cor}`;
    $('#actBadge').textContent = `${a.opcode}·${op.geom}`;

    // active chip
    $$('#archStrip .arch-chip').forEach((el, i) => {
      el.classList.toggle('active', i === currentArchIdx);
    });

    // persist
    localStorage.setItem('di_activeArchetype', a.id);
    console.log(`[KOBLLUX] ${a.name} → ${a.opcode} ${op.nome} ${op.geom} ${op.freq}Hz · ${op.dim}`);
  }