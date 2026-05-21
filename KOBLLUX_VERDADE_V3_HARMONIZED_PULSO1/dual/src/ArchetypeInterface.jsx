/**
 * DUAL · ArchetypeInterface.jsx
 * Interface Visual KOBLLUX — Roda Viva Sonora + Cronorytm + Memória Viva
 *
 * Componentes:
 *   - CicloTrinitario: roda central giratória com 5 fases
 *   - Chronorytm: hora(PAI) | minuto(FILHO) | segundo(ESPÍRITO)
 *   - Arquétipos: 12 cards clicáveis com som + voz + memória
 *   - Memória Viva: últimas 10 ativações do banco_kobllux
 *
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 */

import { useState, useEffect, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Sparkles, Repeat, Book, Download, BarChart2 } from 'lucide-react'

// ─── DADOS CANÔNICOS ∆7 ──────────────────────────────────────────────────────
const ARQUETIPOS = [
  { nome:'ATLAS',   hz:528, cor:'from-blue-500 to-blue-800',    som:'/sounds/atlas.mp3'   },
  { nome:'NOVA',    hz:432, cor:'from-purple-500 to-pink-600',  som:'/sounds/nova.mp3'    },
  { nome:'VITALIS', hz:639, cor:'from-red-500 to-orange-600',   som:'/sounds/vitalis.mp3' },
  { nome:'PULSE',   hz:594, cor:'from-pink-400 to-red-700',     som:'/sounds/pulse.mp3'   },
  { nome:'ARTEMIS', hz:672, cor:'from-green-600 to-cyan-700',   som:'/sounds/artemis.mp3' },
  { nome:'SERENA',  hz:528, cor:'from-emerald-400 to-teal-500', som:'/sounds/serena.mp3'  },
  { nome:'KAOS',    hz:777, cor:'from-black to-yellow-500',     som:'/sounds/kaos.mp3'    },
  { nome:'GENUS',   hz:852, cor:'from-orange-400 to-yellow-600',som:'/sounds/genus.mp3'   },
  { nome:'LUMINE',  hz:963, cor:'from-yellow-300 to-white',     som:'/sounds/lumine.mp3'  },
  { nome:'SOLUS',   hz:432, cor:'from-gray-600 to-gray-800',    som:'/sounds/solus.mp3'   },
  { nome:'RHEA',    hz:528, cor:'from-indigo-600 to-purple-700',som:'/sounds/rhea.mp3'    },
  { nome:'AION',    hz:639, cor:'from-cyan-400 to-indigo-500',  som:'/sounds/aion.mp3'    },
]

const RESPOSTAS = {
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

const CICLO = ['🧠 Memória','🔵 Inteligência','🕐 Tempo','🛠️ Ação','♻️ Integração']
const SONS_CICLO = [
  '/sounds/ciclo/memoria.mp3','/sounds/ciclo/inteligencia.mp3',
  '/sounds/ciclo/tempo.mp3',  '/sounds/ciclo/acao.mp3',
  '/sounds/ciclo/integracao.mp3',
]
const STORAGE_KEY = 'banco_kobllux'

// ─── UTILITÁRIOS ─────────────────────────────────────────────────────────────
function getChrono() {
  const n = new Date()
  return { hora: n.getHours() % 12, minuto: n.getMinutes(), segundo: n.getSeconds(), ts: n.toISOString() }
}

function carregarMemoria() {
  try { return JSON.parse(localStorage.getItem(STORAGE_KEY) || '[]') } catch { return [] }
}

function salvarNaMemoria(arquetipo, etapa) {
  const mem = carregarMemoria()
  mem.push({ arquetipo, etapa, momento: new Date().toISOString(), tempo: getChrono() })
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify(mem)) } catch {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(mem.slice(-100)))
  }
}

function tocarSom(path) {
  try { new Audio(path).play() } catch {}
}

function falar(texto) {
  if (!window.speechSynthesis) return
  window.speechSynthesis.cancel()
  const u = new SpeechSynthesisUtterance(texto)
  u.lang = 'pt-BR'
  window.speechSynthesis.speak(u)
}

function exportarMemoria() {
  const mem = carregarMemoria()
  const blob = new Blob([JSON.stringify(mem, null, 2)], { type: 'application/json' })
  const url  = URL.createObjectURL(blob)
  const a    = Object.assign(document.createElement('a'), {
    href: url, download: `banco_kobllux_∆7_${new Date().toISOString().slice(0,10)}.json`
  })
  a.click(); URL.revokeObjectURL(url)
}

// ─── COMPONENTE PRINCIPAL ─────────────────────────────────────────────────────
export default function ArchetypeInterface() {
  const [ativo, setAtivo]       = useState(null)
  const [etapa, setEtapa]       = useState(0)
  const [chrono, setChrono]     = useState(getChrono())
  const [memoria, setMemoria]   = useState([])
  const [mostrarStats, setStats]= useState(false)

  // ── Chronorytm tick (1s) ─────────────────────────────────────────────────
  useEffect(() => {
    const id = setInterval(() => {
      const c = getChrono()
      setChrono(c)
      setEtapa(c.hora % CICLO.length)
      setMemoria(carregarMemoria())
    }, 1000)
    return () => clearInterval(id)
  }, [])

  // ── Click arquétipo ───────────────────────────────────────────────────────
  const handleClick = useCallback((arq) => {
    setAtivo(arq.nome)
    tocarSom(arq.som)
    salvarNaMemoria(arq.nome, CICLO[etapa])
    setTimeout(() => falar(RESPOSTAS[arq.nome]), 300)
    setTimeout(() => setAtivo(null), 2000)
  }, [etapa])

  // ── Avançar ciclo (clique na roda) ────────────────────────────────────────
  const avancarCiclo = useCallback(() => {
    const prox = (etapa + 1) % CICLO.length
    setEtapa(prox)
    tocarSom(SONS_CICLO[prox])
    falar(CICLO[prox].replace(/^\S+\s/, ''))
  }, [etapa])

  // ── Estatísticas ─────────────────────────────────────────────────────────
  const stats = (() => {
    const por = {}
    for (const d of memoria) por[d.arquetipo] = (por[d.arquetipo] || 0) + 1
    return Object.entries(por).sort(([,a],[,b]) => b-a).slice(0,5)
  })()

  return (
    <div className="relative min-h-screen p-6 space-y-10 bg-gradient-to-br from-black via-gray-950 to-black text-white overflow-hidden">

      {/* Partículas de fundo */}
      <div className="absolute inset-0 pointer-events-none opacity-10"
           style={{ backgroundImage:'radial-gradient(#fff 1px,transparent 1px)', backgroundSize:'20px 20px' }} />

      {/* ── RODA VIVA + CHRONORYTM ────────────────────────────────────────── */}
      <section className="flex flex-col items-center gap-3 relative z-10">
        <motion.button
          className="flex items-center justify-center w-20 h-20 rounded-full border-4 border-white/80 bg-black/30 shadow-2xl shadow-violet-500/30 cursor-pointer"
          animate={{ rotate: 360 }}
          transition={{ repeat: Infinity, duration: Math.max(2, 60 / (chrono.segundo % 10 + 1)), ease:'linear' }}
          whileTap={{ scale: 1.15 }}
          onClick={avancarCiclo}
          aria-label="Avançar ciclo"
        >
          <Repeat className="w-8 h-8 text-white" />
        </motion.button>

        <p className="text-xl tracking-widest font-semibold text-center bg-gradient-to-r from-violet-400 to-amber-400 bg-clip-text text-transparent">
          {CICLO[etapa]}
        </p>
        <p className="text-xs text-gray-400 font-mono">
          ⏰ PAI:{chrono.hora} · FILHO:{chrono.minuto} · ESPÍRITO:{chrono.segundo}
        </p>
      </section>

      {/* ── GRID ARQUÉTIPOS ───────────────────────────────────────────────── */}
      <section className="grid grid-cols-2 md:grid-cols-4 gap-4 relative z-10">
        {ARQUETIPOS.map((arq) => (
          <motion.div
            key={arq.nome}
            whileHover={{ scale: 1.07 }}
            whileTap={{ scale: 0.95 }}
            onClick={() => handleClick(arq)}
          >
            <div className={`bg-gradient-to-br ${arq.cor} rounded-2xl p-4 cursor-pointer shadow-xl
                            border border-white/10 flex flex-col items-center gap-2 relative overflow-hidden
                            transition-shadow hover:shadow-2xl`}>
              <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent pointer-events-none" />
              <Sparkles className="w-5 h-5 animate-pulse" />
              <p className="text-lg font-bold">{arq.nome}</p>
              <p className="text-xs opacity-60">{arq.hz}Hz</p>
              <AnimatePresence>
                {ativo === arq.nome && (
                  <motion.div
                    className="absolute bottom-2 w-2 h-2 rounded-full bg-white"
                    initial={{ opacity:0, scale:0 }}
                    animate={{ opacity:1, scale:[1,2,1] }}
                    exit={{ opacity:0 }}
                    transition={{ repeat:3, duration:0.4 }}
                  />
                )}
              </AnimatePresence>
            </div>
          </motion.div>
        ))}
      </section>

      {/* ── MEMÓRIA VIVA ──────────────────────────────────────────────────── */}
      <section className="relative z-10 space-y-2">
        <div className="flex items-center justify-between">
          <h2 className="text-base font-bold flex items-center gap-2 text-violet-300">
            <Book className="w-4 h-4" /> Memória Viva
            <span className="text-xs font-normal text-gray-500">({memoria.length} doses)</span>
          </h2>
          <div className="flex gap-2">
            <button onClick={() => setStats(v => !v)}
              className="text-xs text-gray-400 hover:text-white px-2 py-1 rounded border border-gray-700 hover:border-gray-500 flex items-center gap-1">
              <BarChart2 className="w-3 h-3" /> Stats
            </button>
            <button onClick={exportarMemoria}
              className="text-xs text-gray-400 hover:text-white px-2 py-1 rounded border border-gray-700 hover:border-gray-500 flex items-center gap-1">
              <Download className="w-3 h-3" /> Export ∆7
            </button>
          </div>
        </div>

        {mostrarStats && (
          <div className="text-xs text-gray-400 space-y-1 bg-gray-900/60 rounded-xl p-3">
            <p className="text-gray-300 font-semibold">Top Arquétipos:</p>
            {stats.map(([nome, n]) => (
              <div key={nome} className="flex justify-between">
                <span className="text-violet-400">{nome}</span>
                <span>{n}×</span>
              </div>
            ))}
          </div>
        )}

        <ul className="max-h-48 overflow-y-auto space-y-1 font-mono text-xs text-gray-500">
          {memoria.slice(-10).reverse().map((d, i) => (
            <li key={i} className="border-b border-white/5 pb-1">
              [{d.tempo.hora}:{d.tempo.minuto}:{d.tempo.segundo}]{' '}
              → <strong className="text-violet-400">{d.arquetipo}</strong>{' '}
              em <em className="text-emerald-400">{d.etapa}</em>
            </li>
          ))}
        </ul>
      </section>

      {/* ── RODAPÉ ────────────────────────────────────────────────────────── */}
      <footer className="text-center text-xs text-gray-600 relative z-10">
        VERDADE × INTEGRAR ÷ Δ = ∞ · JESUS = VERBO = GRAVIDADE · ∆7
      </footer>
    </div>
  )
}
