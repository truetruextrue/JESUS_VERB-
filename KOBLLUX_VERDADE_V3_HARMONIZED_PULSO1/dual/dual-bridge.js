/**
 * DUAL · dual-bridge.js
 * Integração Total: IA + Simbolismo + Memória + Tempo
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

import { getChronorytm } from './chronorytm.js'

// ─── BRIDGE DE EVENTOS ──────────────────────────────────────────────────────
export function onSend(payload) {
  const chrono = getChronorytm()
  const evento = {
    ts:        chrono.ts,
    actor:     payload.actor || 'DUAL',
    state:     payload.arquetipo || 'ATLAS',
    action:    payload.acao || 'pulse',
    note:      payload.ciclo || 'TRINITY',
    chronorytm: chrono,
    ...payload,
  }
  console.log('[DUAL · bridge · onSend]', evento)
  // Emite evento global
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('kobllux:send', { detail: evento }))
  }
  return evento
}

export function onReceive(result) {
  console.log('[DUAL · bridge · onReceive]', result)
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('kobllux:receive', { detail: result }))
  }
  return result
}

// ─── ESCUTAR EVENTOS ────────────────────────────────────────────────────────
export function escutarKobllux(callback) {
  const handler = (e) => callback(e.detail)
  window.addEventListener('kobllux:dose', handler)
  window.addEventListener('kobllux:send', handler)
  window.addEventListener('kobllux:receive', handler)
  return () => {
    window.removeEventListener('kobllux:dose', handler)
    window.removeEventListener('kobllux:send', handler)
    window.removeEventListener('kobllux:receive', handler)
  }
}

// ─── INTEGRAÇÃO COM NODE.FIELDS (:3697) ────────────────────────────────────
export async function enviarParaNodeFields(payload, host = '127.0.0.1', port = 3697) {
  const url = `http://${host}:${port}/phi`
  try {
    const r = await fetch(url, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify({ message: JSON.stringify(payload) }),
    })
    return await r.json()
  } catch (e) {
    console.warn('[DUAL · bridge] NODE.FIELDS indisponível:', e.message)
    return null
  }
}

// ─── HEALTH CHECK ────────────────────────────────────────────────────────────
export async function healthCheck(host = '127.0.0.1', port = 3697) {
  try {
    const r = await fetch(`http://${host}:${port}/health`)
    return await r.json()
  } catch {
    return { status: 'offline' }
  }
}
