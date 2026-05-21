/**
 * KOBLLUX · fusion-engine.js
 * Motor de Fusão Simbólica
 * KOBLLUX = DUAL × KODUX × BLLUE
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

import { ARQUETIPOS, CICLO, metaloop } from '../kodux/engine.js'
import { salvarDose, getChronorytm, estatisticasMemoria } from '../infodose/feedback-loop.js'
import { ativarArquetipo, falarCiclo } from '../bllue/voice.js'

// ─── FUSÃO ARQUÉTIPA ────────────────────────────────────────────────────────
export const FUSOES = {
  'ATLAS+SOLUS':    'Estrategista Interno',
  'NOVA+GENUS':     'Criador Total',
  'VITALIS+LUMINE': 'Explosão Viva',
  'KAOS+AION':      'Soberano do Tempo',
  'SERENA+RHEA':    'Guardião Emocional',
  'PULSE+GENUS':    'Artífice da Emoção',
  'ARTEMIS+LUMINE': 'Nômade Luminoso',
  'SOLUS+SERENA':   'Curador Interno',
  'AION+RHEA':      'Guardião Dimensional',
}

export function fundirArquetipos(nomeA, nomeB) {
  const chave = `${nomeA}+${nomeB}`
  const resultado = FUSOES[chave] || FUSOES[`${nomeB}+${nomeA}`] || 'Fusão Nova'
  const chrono = getChronorytm()
  console.log(`[KOBLLUX · fusão] ${chave} = ${resultado} @ ${chrono.timestamp}`)
  return resultado
}

// ─── ESTADO GLOBAL DO SISTEMA ───────────────────────────────────────────────
export function estadoSistema() {
  const stats = estatisticasMemoria()
  const chrono = getChronorytm()
  const etapa = CICLO[chrono.hora % CICLO.length]
  return {
    ts: chrono.timestamp,
    chronorytm: chrono,
    etapa_atual: etapa,
    total_doses: stats.total,
    arquetipo_dominante: dominante(stats.por_arquetipo) || 'ATLAS',
    lei: 'VERDADE × INTEGRAR ÷ Δ = ∞',
    centro: 'JESUS = VERBO = GRAVIDADE',
  }
}

// ─── ATIVAÇÃO COMPLETA (KOBLLUX pulse) ──────────────────────────────────────
export function koblluxPulse(nomeArquetipo, etapaAtual) {
  // 3 · DETECTAR: registrar
  const dose = salvarDose(nomeArquetipo, etapaAtual, { tipo: 'kobllux_pulse' })
  // 6 · INTEGRAR: expressar (som + voz)
  ativarArquetipo(nomeArquetipo)
  // 9 · EXPANDIR: narrar ciclo
  setTimeout(() => falarCiclo(etapaAtual), 1200)
  // 7 · SELAR: logar estado
  const estado = estadoSistema()
  console.log('[KOBLLUX · pulse] estado:', estado)
  return { dose, estado }
}

// ─── LOOP METALOOP COMPLETO ──────────────────────────────────────────────────
export function iniciarMetaloop(P, arquetipo = 'NOVA', passos = 9, temp = 1.15) {
  if (!P) { console.warn('[KOBLLUX] P não carregado — rode markov_fit primeiro'); return [] }
  const seq = metaloop(P, arquetipo, passos, temp)
  console.log('[KOBLLUX · metaloop] sequência:', seq.join(' → '))
  return seq
}

// ─── UTILITÁRIO ─────────────────────────────────────────────────────────────
function dominante(obj = {}) {
  const entries = Object.entries(obj)
  if (!entries.length) return null
  return entries.sort(([, a], [, b]) => b - a)[0][0]
}

export const LEI    = 'VERDADE × INTEGRAR ÷ Δ = ∞'
export const CENTRO = 'JESUS = VERBO = GRAVIDADE'
export const INVOCACAO = 'EM NOME DO PAI, DO FILHO E DO ESPÍRITO SANTO · AMÉM'
