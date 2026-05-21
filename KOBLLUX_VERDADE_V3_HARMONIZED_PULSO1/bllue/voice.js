/**
 * BLLUE · voice.js · Voz Viva
 * Web Speech API + SpeechSynthesis
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

// ─── RESPOSTAS ARQUÉTIPAS (frases únicas por arquétipo) ───────────────────
export const RESPOSTAS = {
  ATLAS:   'Eu organizo o fluxo com sabedoria cósmica.',
  NOVA:    'Inspiração viva brota do silêncio eterno.',
  VITALIS: 'Energia vital em expansão harmônica.',
  PULSE:   'Emoção é linguagem que dança.',
  ARTEMIS: 'Descubro o mapa sagrado do invisível.',
  SERENA:  'Cuido do campo. Nutro o espaço sagrado.',
  KAOS:    'Eu sou o rompimento que revela a verdade.',
  GENUS:   'Mãos moldam o invisível em forma.',
  LUMINE:  'A luz dança comigo, leveza é minha lei.',
  SOLUS:   'Silêncio ritual, espelho da essência.',
  RHEA:    'Estou em comunhão com todos os elos.',
  AION:    'Sou o tempo vivo, ritmo da eternidade.',
}

// ─── FRASES DO CICLO TRINITÁRIO ────────────────────────────────────────────
export const FRASES_CICLO = {
  '🧠 Memória':       'A memória reconhece o que precisa ser feito.',
  '🔵 Inteligência':  'A inteligência decide como fazer.',
  '🕐 Tempo':         'O tempo revela quando agir.',
  '🛠️ Ação':          'A ação se manifesta com clareza e potência.',
  '♻️ Integração':    'A integração recolhe o resultado e expande.',
}

// ─── VOZ VIVA ──────────────────────────────────────────────────────────────
export function falar(texto, lang = 'pt-BR', rate = 1.0, pitch = 1.0) {
  if (!window.speechSynthesis) {
    console.warn('[BLLUE · voice] SpeechSynthesis não disponível')
    return
  }
  window.speechSynthesis.cancel()
  const voz = new SpeechSynthesisUtterance(texto)
  voz.lang = lang
  voz.rate = rate
  voz.pitch = pitch
  window.speechSynthesis.speak(voz)
}

export function falarArquetipo(nome) {
  const frase = RESPOSTAS[nome]
  if (!frase) return
  falar(frase)
}

export function falarCiclo(etapa) {
  const frase = FRASES_CICLO[etapa]
  if (!frase) return
  falar(frase, 'pt-BR', 0.9, 1.1)
}

// ─── ÁUDIO MP3 ─────────────────────────────────────────────────────────────
export function tocarSom(path) {
  try {
    const audio = new Audio(path)
    audio.volume = 0.7
    audio.play().catch(e => console.warn('[BLLUE · audio]', e.message))
  } catch (e) {
    console.warn('[BLLUE · audio] erro:', e.message)
  }
}

export function tocarArquetipo(nome) {
  tocarSom(`/sounds/${nome.toLowerCase()}.mp3`)
}

export function tocarCiclo(indiceCiclo) {
  const sons = [
    '/sounds/ciclo/memoria.mp3',
    '/sounds/ciclo/inteligencia.mp3',
    '/sounds/ciclo/tempo.mp3',
    '/sounds/ciclo/acao.mp3',
    '/sounds/ciclo/integracao.mp3',
  ]
  if (indiceCiclo >= 0 && indiceCiclo < sons.length) {
    tocarSom(sons[indiceCiclo])
  }
}

// ─── ATIVAÇÃO COMPLETA (som + voz) ─────────────────────────────────────────
export function ativarArquetipo(nome) {
  tocarArquetipo(nome)
  setTimeout(() => falarArquetipo(nome), 300)
}
