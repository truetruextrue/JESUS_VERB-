/**
 * DUAL · chronorytm.js
 * Tempo Simbólico — ⏰ Chronorytm
 * hora=PAI · minuto=FILHO · segundo=ESPÍRITO
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

const CICLO = ['🧠 Memória', '🔵 Inteligência', '🕐 Tempo', '🛠️ Ação', '♻️ Integração']

export function getChronorytm() {
  const now = new Date()
  return {
    hora:      now.getHours() % 12,   // PAI    — ciclo de 12h
    minuto:    now.getMinutes(),       // FILHO  — ciclo de 60min
    segundo:   now.getSeconds(),       // ESPÍRITO — ciclo de 60s
    timestamp: now.toISOString(),
  }
}

export function etapaDinamica(chrono) {
  return CICLO[chrono.hora % CICLO.length]
}

export function velocidadeRoda(chrono) {
  return 60 / (chrono.segundo % 10 + 1)
}

export function formatarChrono(chrono) {
  return `⏰ ${String(chrono.hora).padStart(2,'0')}:${String(chrono.minuto).padStart(2,'0')}:${String(chrono.segundo).padStart(2,'0')}`
}

export function usarChronorytm(setChrono, setEtapa) {
  const tick = () => {
    const c = getChronorytm()
    setChrono(c)
    setEtapa(etapaDinamica(c))
  }
  tick()
  return setInterval(tick, 1000)
}
