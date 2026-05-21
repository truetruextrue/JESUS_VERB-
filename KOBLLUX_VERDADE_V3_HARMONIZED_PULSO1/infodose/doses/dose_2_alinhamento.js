/**
 * INFODOSE · dose_2_alinhamento.js
 * Dose 2: Alinhamento dos Eixos TRINITY
 * Alinha: Memória(🧠) + Inteligência(🔵) + Tempo(🕐)
 */

import { getChronorytm, salvarDose } from '../feedback-loop.js'

const EIXOS = {
  PAI:      { simbolo: '🧠', nome: 'Memória',      arquetipo: 'ATLAS'  },
  FILHO:    { simbolo: '🔵', nome: 'Inteligência',  arquetipo: 'ARTEMIS' },
  ESPIRITO: { simbolo: '🕐', nome: 'Tempo',          arquetipo: 'AION'  },
}

export function alinharEixos() {
  const chrono = getChronorytm()
  const alinhamento = {
    ts: chrono.timestamp,
    PAI: {
      ...EIXOS.PAI,
      valor: chrono.hora,
      nota: `Hora simbólica: ${chrono.hora}`,
    },
    FILHO: {
      ...EIXOS.FILHO,
      valor: chrono.minuto,
      nota: `Minuto ativo: ${chrono.minuto}`,
    },
    ESPIRITO: {
      ...EIXOS.ESPIRITO,
      valor: chrono.segundo,
      nota: `Segundo pulsante: ${chrono.segundo}`,
    },
    score: calcularScore(chrono),
  }

  // salva nos três arquétipos de eixo
  for (const eixo of Object.values(EIXOS)) {
    salvarDose(eixo.arquetipo, `🕐 Alinhamento · ${eixo.nome}`, { tipo: 'alinhamento', alinhamento })
  }

  console.log('[DOSE·2·ALINHAMENTO]', alinhamento)
  return alinhamento
}

function calcularScore(chrono) {
  // score 0-1: quão alinhados estão os três eixos
  const h = chrono.hora / 12
  const m = chrono.minuto / 60
  const s = chrono.segundo / 60
  // máximo alinhamento quando h+m+s ≈ 1.5 (metade de cada ciclo)
  const media = (h + m + s) / 3
  return Math.round((1 - Math.abs(media - 0.5) * 2) * 100) / 100
}

export function alinhamentoParaTexto(al) {
  const { PAI, FILHO, ESPIRITO, score } = al
  return [
    `⚖️ ALINHAMENTO TRINITY (score: ${score})`,
    `  ${PAI.simbolo} ${PAI.nome} (PAI · ${PAI.arquetipo}): ${PAI.valor}`,
    `  ${FILHO.simbolo} ${FILHO.nome} (FILHO · ${FILHO.arquetipo}): ${FILHO.valor}`,
    `  ${ESPIRITO.simbolo} ${ESPIRITO.nome} (ESPÍRITO · ${ESPIRITO.arquetipo}): ${ESPIRITO.valor}`,
  ].join('\n')
}
