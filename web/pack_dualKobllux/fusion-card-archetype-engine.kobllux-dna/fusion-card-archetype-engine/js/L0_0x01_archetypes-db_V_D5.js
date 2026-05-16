/* ═══════════════════════════════════════════════════════════
   0x01 · PULSAR · V · D5
   ═══════════════════════════════════════════════════════════
   Arquivo   : fusion-card-archetype-engine/js/L0_0x01_archetypes-db_V_D5.js
   Opcode    : 0x01 · PULSAR · ● · 432Hz
   V.E.E.B.  : Vibração
   Degrau    : D5 (block)
   Fórmula   : Vibração · f₁=432Hz · P(t)=A·sin(2π·432·t) · impulso sonoro
   ─────────────────────────────────────────────────────────────
   ORQUESTRAÇÃO:
   Nível     : 0 · DADOS_PUROS
   Opcode Δ  : 0x00 · Carregar na posição 0 da cadeia
   Nota      : Constantes e DNA — nada depende de nada
   ─────────────────────────────────────────────────────────────
   Métricas  :
     S = 75  (Σbᵢ·2^(i-1) · bytes[0..7] mod 2)
     V(1) = 0.0000  (V₀·cos(3π/6), V₀=432)
     χ = 0  (V-E+F = funções-arrows+returns)
   ─────────────────────────────────────────────────────────────
   VERDADE × INTEGRAR ÷ Δ = ∞  ·  3×6×9×7=1134  ·  α=1/137
═══════════════════════════════════════════════════════════ */
const ARCHETYPES_DB = [
    { id: 'ATLAS',   name: 'ATLAS',   desc: 'Estrutura & Governo',    opcode: '0x02', primary: '#38BDF8', drk: 'A ordem externa reflete a clareza interna.' },
    { id: 'NOVA',    name: 'NOVA',    desc: 'Inovação & Fluxo',       opcode: '0x01', primary: '#F97316', drk: 'O erro é apenas um dado não processado.' },
    { id: 'VITALIS', name: 'VITALIS', desc: 'Energia & Ação',         opcode: '0x03', primary: '#22C55E', drk: 'O corpo sabe antes da mente duvidar.' },
    { id: 'PULSE',   name: 'PULSE',   desc: 'Ritmo & Emoção',         opcode: '0x0B', primary: '#EC4899', drk: 'Sinta a batida do caos e dance com ela.' },
    { id: 'ARTEMIS', name: 'ARTEMIS', desc: 'Foco & Caça',            opcode: '0x05', primary: '#A855F7', drk: 'Defina o alvo. O resto é apenas ruído.' },
    { id: 'SERENA',  name: 'SERENA',  desc: 'Paz & Harmonia',         opcode: '0x0A', primary: '#7DD3FC', drk: 'No centro do furacão, existe um ponto imóvel.' },
    { id: 'KAOS',    name: 'KAOS',    desc: 'Mudança & Entropia',     opcode: '0x04', primary: '#FACC15', drk: 'Quebre o padrão hoje. Amanhã nasce o novo.' },
    { id: 'GENUS',   name: 'GENUS',   desc: 'Criação & Arte',         opcode: '0x09', primary: '#E5E7EB', drk: 'A excelência habita nos detalhes.' },
    { id: 'LUMINE',  name: 'LUMINE',  desc: 'Brilho & Carisma',       opcode: '0x07', primary: '#FDE047', drk: 'Irradie sem medo.' },
    { id: 'SOLUS',   name: 'SOLUS',   desc: 'Vazio & Verdade',        opcode: '0x08', primary: '#0EA5E9', drk: 'O silêncio revela mais que mil estímulos.' },
    { id: 'RHEA',    name: 'RHEA',    desc: 'Cuidado & Raiz',         opcode: '0x06', primary: '#16A34A', drk: 'Nutra a raiz e o fruto virá.' },
    { id: 'HORUS',   name: 'HORUS',   desc: 'Visão & Estratégia',     opcode: '0x0C', primary: '#5500FF', drk: 'Observe o todo antes de agir.' }
  ];

  // ═══════════════════════════════════════════════════════════
  // [STATE]
  // ═══════════════════════════════════════════════════════════