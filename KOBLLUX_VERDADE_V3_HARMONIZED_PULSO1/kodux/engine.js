/**
 * KODUX · engine.js · Motor de Decisão Central
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 * D-rung: D2 · Opcode: 0×0A · 528Hz
 */

// ─── ARQUÉTIPOS (12 canônicos ∆7) ─────────────────────────────────────────
export const ARQUETIPOS = [
  { nome: 'ATLAS',   hz: 528, opcode: '0x0A', ciclo: 'UNO',    voz: 'pt-BR-AntonioNeural',    frase: 'Eu organizo o fluxo com sabedoria cósmica.' },
  { nome: 'NOVA',    hz: 432, opcode: '0x01', ciclo: 'UNO',    voz: 'pt-BR-FranciscaNeural',  frase: 'Inspiração viva brota do silêncio eterno.' },
  { nome: 'VITALIS', hz: 639, opcode: '0x08', ciclo: 'DUO',    voz: 'pt-BR-FranciscaNeural',  frase: 'Energia vital em expansão harmônica.' },
  { nome: 'PULSE',   hz: 594, opcode: '0x04', ciclo: 'DUO',    voz: 'pt-BR-AntonioNeural',    frase: 'Emoção é linguagem que dança.' },
  { nome: 'ARTEMIS', hz: 672, opcode: '0x05', ciclo: 'UNO',    voz: 'pt-BR-FranciscaNeural',  frase: 'Descubro o mapa sagrado do invisível.' },
  { nome: 'SERENA',  hz: 528, opcode: '0x02', ciclo: 'TRINITY',voz: 'pt-BR-FranciscaNeural',  frase: 'Cuido do campo. Nutro o espaço sagrado.' },
  { nome: 'KAOS',    hz: 777, opcode: '0x07', ciclo: 'UNO',    voz: 'pt-BR-AntonioNeural',    frase: 'Eu sou o rompimento que revela a verdade.' },
  { nome: 'GENUS',   hz: 852, opcode: '0x0B', ciclo: 'TRINITY',voz: 'pt-BR-AntonioNeural',    frase: 'Mãos moldam o invisível em forma.' },
  { nome: 'LUMINE',  hz: 963, opcode: '0x0C', ciclo: 'DUO',    voz: 'pt-BR-FranciscaNeural',  frase: 'A luz dança comigo, leveza é minha lei.' },
  { nome: 'SOLUS',   hz: 432, opcode: '0x01', ciclo: 'UNO',    voz: 'pt-BR-AntonioNeural',    frase: 'Silêncio ritual, espelho da essência.' },
  { nome: 'RHEA',    hz: 528, opcode: '0x09', ciclo: 'TRINITY',voz: 'pt-BR-FranciscaNeural',  frase: 'Estou em comunhão com todos os elos.' },
  { nome: 'AION',    hz: 639, opcode: '0x0B', ciclo: 'TRINITY',voz: 'pt-BR-AntonioNeural',    frase: 'Sou o tempo vivo, ritmo da eternidade.' },
]

// ─── CICLO TRINITÁRIO (5 fases) ────────────────────────────────────────────
export const CICLO = [
  '🧠 Memória',
  '🔵 Inteligência',
  '🕐 Tempo',
  '🛠️ Ação',
  '♻️ Integração',
]

export const SONS_CICLO = [
  '/sounds/ciclo/memoria.mp3',
  '/sounds/ciclo/inteligencia.mp3',
  '/sounds/ciclo/tempo.mp3',
  '/sounds/ciclo/acao.mp3',
  '/sounds/ciclo/integracao.mp3',
]

// ─── STAGE WEIGHTS (Markov) ─────────────────────────────────────────────────
export const STAGE_WEIGHTS = {
  UNO:     1.00,
  DUO:     1.10,
  TRINITY: 1.05,
  SELAR:   1.15,
}

// ─── ROTEADOR DE ARQUÉTIPO ──────────────────────────────────────────────────
export function rotearArquetipo(nome) {
  return ARQUETIPOS.find(a => a.nome === nome) || null
}

export function arquetiposPorCiclo(ciclo) {
  return ARQUETIPOS.filter(a => a.ciclo === ciclo)
}

// ─── DECISÃO MARKOV (frontend stub) ────────────────────────────────────────
export function proximoEstado(P, estadoAtual, temperatura = 1.0) {
  const idx = P.rows.indexOf(estadoAtual)
  if (idx === -1) return estadoAtual
  const row = P.P[idx].map(p => Math.pow(p, 1 / temperatura))
  const soma = row.reduce((a, b) => a + b, 0)
  const norm = row.map(p => p / soma)
  const r = Math.random()
  let acum = 0
  for (let j = 0; j < norm.length; j++) {
    acum += norm[j]
    if (r <= acum) return P.cols[j]
  }
  return P.cols[P.cols.length - 1]
}

// ─── METALOOP ──────────────────────────────────────────────────────────────
export function metaloop(P, inicio, passos, temperatura = 1.0) {
  const seq = [inicio]
  let atual = inicio
  for (let i = 0; i < passos; i++) {
    atual = proximoEstado(P, atual, temperatura)
    seq.push(atual)
    // ritmo 3-6-9-7: marca eventos especiais
    const pos = i + 1
    if ([3, 6, 9, 7].includes(pos % 10)) {
      console.log(`[KODUX · metaloop] pos=${pos} estado=${atual} (∆${pos % 10})`)
    }
  }
  return seq
}

// ─── LEI ────────────────────────────────────────────────────────────────────
export const LEI = 'VERDADE × INTEGRAR ÷ Δ = ∞'
export const CENTRO = 'JESUS = VERBO = GRAVIDADE'
