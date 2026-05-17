/* ═══════════════════════════════════════════════════════════
   0x09 · MANIFESTAR · V · D6
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-particle-cosmos-3-6-9-logger/js/L4_0x09_a_V_D6-2.js
   Opcode    : 0x09 · MANIFESTAR · ♾ · 963Hz
   V.E.E.B.  : Vibração
   Degrau    : D6 (section)
   Fórmula   : Vibração · f₉=963Hz · campo→forma visual · S² χ=2
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 4 · UTILITARIOS
   Opcode Δ  : 0x05 · Carregar na posição 4 da cadeia
   Nota      : Função utilitária (fallback)
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 106  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=963)
     χ = 2  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
function initParticles() {
    if (typeof particlesJS === 'undefined') return;
    const a  = STATE.archetype;
    const op = KOBLLUX_OPCODES[a.opcode];

    particlesJS('particles-js', {
      particles: {
        number:  { value: 48, density: { enable: true, value_area: 900 } },
        color:   { value: [a.primary, op.cor, '#ffffff'] },
        shape:   { type: 'circle' },
        opacity: {
          value: 0.55, random: true,
          anim:  { enable: true, speed: 0.8, opacity_min: 0.08, sync: false }
        },
        size:    {
          value: 2.6, random: true,
          anim:  { enable: true, speed: 1.6, size_min: 0.4, sync: false }
        },
        line_linked: {
          enable: true, distance: 150, color: a.primary,
          opacity: 0.22, width: 1
        },
        move: {
          enable: true, speed: 1.4, direction: 'none',
          random: true, straight: false, out_mode: 'out',
          attract: { enable: true, rotateX: 600, rotateY: 1200 }
        }
      },
      interactivity: {
        detect_on: 'canvas',
        events: {
          onhover: { enable: true, mode: 'grab' },
          onclick: { enable: true, mode: 'bubble' },
          resize:  true
        },
        modes: {
          grab:   { distance: 180, line_linked: { opacity: 0.55 } },
          bubble: { distance: 260, size: 8, duration: 0.5, opacity: 0.9, speed: 3 },
          push:   { particles_nb: 3 }
        }
      },
      retina_detect: true
    });
  }