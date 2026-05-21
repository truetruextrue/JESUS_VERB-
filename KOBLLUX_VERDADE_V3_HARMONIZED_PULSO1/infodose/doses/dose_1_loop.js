/**
 * INFODOSE · dose_1_loop.js
 * Dose 1: Ativação do Loop Retroalimentativo
 * Ritmo: 3-6-9-7 · DETECTAR → INTEGRAR → EXPANDIR → SELAR
 */

import { salvarDose, getChronorytm } from '../feedback-loop.js'

const CICLO = ['🧠 Memória', '🔵 Inteligência', '🕐 Tempo', '🛠️ Ação', '♻️ Integração']

export function ativarLoop(arquetipo, etapaAtual) {
  const chrono = getChronorytm()
  // 3: detectar
  const dose = salvarDose(arquetipo, etapaAtual, {
    tipo: 'loop',
    fase: mapearFase(chrono.segundo),
  })
  // 6: integrar — notificar DOM se disponível
  if (typeof document !== 'undefined') {
    document.dispatchEvent(new CustomEvent('kobllux:dose', { detail: dose }))
  }
  // 9: expandir — log
  console.log(`[DOSE·1·LOOP] ${arquetipo} @ ${etapaAtual} | ${chrono.timestamp}`)
  // 7: selar — retorna a dose para confirmação
  return dose
}

function mapearFase(segundo) {
  const idx = Math.floor(segundo / 12) // 60s / 5 fases = 12s por fase
  return CICLO[idx % CICLO.length]
}

export function ativarLoopCompleto(arquetipos = []) {
  const resultados = []
  for (let i = 0; i < arquetipos.length; i++) {
    const fase = CICLO[i % CICLO.length]
    resultados.push(ativarLoop(arquetipos[i], fase))
    // ritmo 3-6-9-7
    if ([3, 6, 9].includes(i + 1)) {
      console.log(`[DOSE·1·LOOP] ∆${i + 1} — marco rítmico`)
    }
  }
  return resultados
}
