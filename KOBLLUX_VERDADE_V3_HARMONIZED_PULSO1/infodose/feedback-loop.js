/**
 * INFODOSE · feedback-loop.js
 * Registro e retroalimentação ativa
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

const STORAGE_KEY = 'banco_kobllux'

// ─── CHRONORYTM ────────────────────────────────────────────────────────────
export function getChronorytm() {
  const now = new Date()
  return {
    hora:    now.getHours() % 12,   // PAI
    minuto:  now.getMinutes(),       // FILHO
    segundo: now.getSeconds(),       // ESPÍRITO
    timestamp: now.toISOString(),
  }
}

// ─── SALVAR DOSE (memória viva) ─────────────────────────────────────────────
export function salvarDose(arquetipo, etapa, extra = {}) {
  const memoria = carregarMemoria()
  const dose = {
    arquetipo,
    etapa,
    momento:  new Date().toISOString(),
    tempo:    getChronorytm(),
    ...extra,
  }
  memoria.push(dose)
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(memoria))
  } catch (e) {
    console.warn('[INFODOSE] localStorage cheio — limpando doses antigas')
    const recentes = memoria.slice(-100)
    localStorage.setItem(STORAGE_KEY, JSON.stringify(recentes))
  }
  return dose
}

// ─── CARREGAR MEMÓRIA ───────────────────────────────────────────────────────
export function carregarMemoria() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY)
    return raw ? JSON.parse(raw) : []
  } catch {
    return []
  }
}

// ─── EXPORTAR MEMÓRIA (JSON download) ──────────────────────────────────────
export function exportarMemoria() {
  const memoria = carregarMemoria()
  const blob = new Blob([JSON.stringify(memoria, null, 2)], { type: 'application/json' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `banco_kobllux_∆7_${new Date().toISOString().slice(0, 10)}.json`
  a.click()
  URL.revokeObjectURL(url)
}

// ─── ESTATÍSTICAS ──────────────────────────────────────────────────────────
export function estatisticasMemoria() {
  const mem = carregarMemoria()
  const total = mem.length
  const por_arquetipo = {}
  const por_etapa = {}
  for (const dose of mem) {
    por_arquetipo[dose.arquetipo] = (por_arquetipo[dose.arquetipo] || 0) + 1
    por_etapa[dose.etapa] = (por_etapa[dose.etapa] || 0) + 1
  }
  return { total, por_arquetipo, por_etapa }
}

// ─── LIMPAR MEMÓRIA ─────────────────────────────────────────────────────────
export function limparMemoria() {
  localStorage.removeItem(STORAGE_KEY)
}

// ─── LOOP DE RETROALIMENTAÇÃO ───────────────────────────────────────────────
export function iniciarFeedbackLoop(intervaloMs = 30000, onTick = null) {
  const id = setInterval(() => {
    const stats = estatisticasMemoria()
    const chrono = getChronorytm()
    const info = {
      ts: chrono.timestamp,
      total_doses: stats.total,
      arquetipo_dominante: dominante(stats.por_arquetipo),
      etapa_dominante: dominante(stats.por_etapa),
      chronorytm: chrono,
    }
    console.log('[INFODOSE · feedback]', info)
    if (onTick) onTick(info)
  }, intervaloMs)
  return () => clearInterval(id)
}

function dominante(obj) {
  if (!obj || Object.keys(obj).length === 0) return null
  return Object.entries(obj).sort(([, a], [, b]) => b - a)[0][0]
}
