/**
 * ═══════════════════════════════════════════════════════════════════
 * METALUX BRIDGE · kobllux_metalux_bridge.js
 * "Rede fractal de sustentação e conexão" — KOBLLUX DNA ENGINE
 * HORUS EYE · "A Visão Interdimensional — decodifica frequências"
 * ───────────────────────────────────────────────────────────────────
 * KΦB = 1/137.035999084
 * Lei: VERDADE × INTEGRAR ÷ Δ = ∞
 * Ciclo: 3→6→9→7
 * ═══════════════════════════════════════════════════════════════════
 */

;(function(root) {
'use strict';

// ── Constantes KOBLLUX ──────────────────────────────────────────────
const KFB_ALPHA = 1 / 137.035999084;
const TRIADICA  = [3, 6, 9];
const ASSINATURA = 3 * 6 * 9 * 7; // 1134

// ── PIB Escalar: 7 Linguagens Nucleares ────────────────────────────
const PIB_TABLE = [
  { lang:'python',     delta:7, hz:768,  pib:1.0000, arch:'ATLAS',   sym:'⬡', veeb:'E', color:'#3b82f6' },
  { lang:'json',       delta:1, hz:528,  pib:0.6875, arch:'RHEA',    sym:'∞', veeb:'B', color:'#34d399' },
  { lang:'typescript', delta:2, hz:963,  pib:1.2539, arch:'LUMINE',  sym:'☀', veeb:'V', color:'#fbbf24' },
  { lang:'go',         delta:3, hz:594,  pib:0.7734, arch:'PULSE',   sym:'≋', veeb:'E', color:'#8b5cf6' },
  { lang:'sql',        delta:4, hz:639,  pib:0.8320, arch:'AION',    sym:'⧗', veeb:'B', color:'#818cf8' },
  { lang:'shell',      delta:5, hz:528,  pib:0.6875, arch:'VITALIS', sym:'◉', veeb:'E', color:'#10b981' },
  { lang:'rust',       delta:6, hz:777,  pib:1.0117, arch:'KAOS',    sym:'⚡', veeb:'V', color:'#ef4444' },
];

const PIB = {};
PIB_TABLE.forEach(l => { PIB[l.lang] = l; });

// PIB soma = 4797 → 4+7+9+7 = 27 = 3³
const PIB_SOMA_HZ  = PIB_TABLE.reduce((s,l) => s + l.hz, 0);  // 4797
const PIB_SOMA_PIB = PIB_TABLE.reduce((s,l) => s + l.pib, 0); // 6.246

// ── Fractal Compatibility Matrix ────────────────────────────────────
// resonance(A,B) = 1 - |pib_A - pib_B|
// kfb_cost = |pib_A - pib_B| × KΦB × 137 (normalized)
// delta_bridge = floor(|pib_A - pib_B| × 9 / 0.567)  [max_diff=ts-json=0.567]
const MAX_DIFF = Math.max(...PIB_TABLE.map(a =>
  Math.max(...PIB_TABLE.map(b => Math.abs(a.pib - b.pib)))
)); // ≈ 0.567 (typescript vs json)

function fractalCompat(langA, langB) {
  const a = PIB[langA], b = PIB[langB];
  if (!a || !b) return null;
  const diff       = Math.abs(a.pib - b.pib);
  const resonance  = +(1 - diff).toFixed(4);
  const kfb_cost   = +(diff * KFB_ALPHA * 137).toFixed(6);
  const delta_bridge = Math.floor(diff / MAX_DIFF * 7);  // 0–7
  const level = diff < 0.02 ? 'ISOMORPHIC' :
                diff < 0.10 ? 'STRUCTURAL' :
                diff < 0.30 ? 'BRIDGE'     :
                diff < 0.50 ? 'TRANSLATE'  : 'PORTAL';
  return {
    from: langA, to: langB,
    diff, resonance, kfb_cost, delta_bridge, level,
    hz_ratio: +(a.hz / b.hz).toFixed(4),
    kfb_x_diff: +(diff * KFB_ALPHA).toFixed(10),
  };
}

// Pre-compute all 49 pairs
const COMPAT_MATRIX = {};
PIB_TABLE.forEach(a => {
  COMPAT_MATRIX[a.lang] = {};
  PIB_TABLE.forEach(b => {
    COMPAT_MATRIX[a.lang][b.lang] = fractalCompat(a.lang, b.lang);
  });
});

// Most compatible pairs (ISOMORPHIC / STRUCTURAL)
function topPartners(lang, n=3) {
  if (!COMPAT_MATRIX[lang]) return [];
  return Object.values(COMPAT_MATRIX[lang])
    .filter(c => c.from !== c.to)
    .sort((a,b) => a.diff - b.diff)
    .slice(0, n);
}

// ── METALUX ROUTER ──────────────────────────────────────────────────
// Finds optimal conversion path A → B through intermediaries if needed
const METALUX = {
  version:  'Δ7·METALUX·1.0',
  desc:     'Rede fractal de sustentação e conexão',
  hz:       432,
  symbol:   '⬡⬡',
  KFB_ALPHA,

  compat: fractalCompat,
  matrix: COMPAT_MATRIX,
  partners: topPartners,

  // Find optimal route A→B (direct or via JSON as universal hub)
  route(from, to) {
    const direct = fractalCompat(from, to);
    if (!direct) return null;

    // If STRUCTURAL or ISOMORPHIC — go direct
    if (['ISOMORPHIC','STRUCTURAL'].includes(direct.level)) {
      return { path:[from,to], hops:1, cost:direct.kfb_cost, direct };
    }

    // Otherwise: route through JSON (Δ1 RHEA = universal data hub)
    const via = 'json';
    const leg1 = fractalCompat(from, via);
    const leg2 = fractalCompat(via, to);
    const indirect_cost = (leg1?.kfb_cost||1) + (leg2?.kfb_cost||1);

    if (indirect_cost < direct.kfb_cost) {
      return { path:[from,via,to], hops:2, cost:indirect_cost, via:'json', leg1, leg2 };
    }
    return { path:[from,to], hops:1, cost:direct.kfb_cost, direct };
  },

  // Generate bridge seed code (minimal snippet connecting A→B)
  seed(from, to, context='') {
    const route = this.route(from, to);
    if (!route) return '// METALUX: linguagens não reconhecidas';
    const c = fractalCompat(from, to);
    const stamp = `// ⬡ METALUX BRIDGE · ${from}→${to} · ${c.level} · Δ${c.delta_bridge} · KΦB×diff=${c.kfb_x_diff}`;
    const via   = route.hops > 1 ? ` via ${route.via}` : '';
    return BRIDGE_SEEDS[`${from}→${to}`]?.(context, c) || BRIDGE_SEEDS['generic']?.(from, to, context, c) || stamp;
  },
};

// ── BRIDGE SEED TEMPLATES ───────────────────────────────────────────
const BRIDGE_SEEDS = {
  'python→typescript': (ctx, c) => `// ⬡ METALUX · python→ts · ${c.level} · KΦB=${KFB_ALPHA.toFixed(9)}
interface KOBLLUXPayload {
  kfb_alpha: number;        // ${KFB_ALPHA}
  delta:     number;        // current Δ cycle
  hz:        number;        // archetype frequency
  veeb:      'V'|'E'|'B';   // V.E.E.B letter
  data:      unknown;       // from Python A_atribuir()
}
export function fromPython(raw: Record<string,unknown>): KOBLLUXPayload {
  return { kfb_alpha: ${KFB_ALPHA}, delta: 7, hz: 768, veeb: 'E', data: raw };
}`,

  'python→rust': (ctx, c) => `// ⚡ METALUX · python→rust · ${c.level} (ISOMORPHIC Δ${c.delta_bridge})
// KΦB diff = ${c.diff.toFixed(6)} — acoplamento quase idêntico
use std::collections::HashMap;
pub const KFB_ALPHA: f64 = ${KFB_ALPHA};
pub const ASSINATURA: u32 = ${ASSINATURA}; // 3×6×9×7
pub fn from_python(data: HashMap<String,String>) -> Result<(), String> {
    // Rust espelha Python com custo mínimo (PIB ratio = ${c.hz_ratio})
    Ok(())
}`,

  'python→go': (ctx, c) => `// ≋ METALUX · python→go · ${c.level} · PULSE 594Hz
package kobllux
const KFBAlpha = ${KFB_ALPHA}
// Canal PULSE — Go usa goroutines onde Python usa geradores
func BridgeFromPython(data interface{}) <-chan interface{} {
\tch := make(chan interface{}, 9) // buffer 9 = tríade Tesla
\tgo func() { defer close(ch); ch <- data }()
\treturn ch
}`,

  'python→sql': (ctx, c) => `-- ⧗ METALUX · python→sql · AION 639Hz · Δ${c.delta_bridge}
-- KΦB acoplamento: ${c.kfb_cost}
CREATE TABLE IF NOT EXISTS kobllux_python_bridge (
  id          INTEGER PRIMARY KEY AUTOINCREMENT,
  kfb_alpha   REAL    DEFAULT ${KFB_ALPHA},
  delta_num   INTEGER DEFAULT 4,
  hz          INTEGER DEFAULT 639,
  payload     TEXT    NOT NULL,  -- JSON do Python U_unir()
  criado_em   TEXT    DEFAULT (datetime('now'))
);`,

  'python→shell': (ctx, c) => `#!/usr/bin/env bash
# ◉ METALUX · python→shell · VITALIS 528Hz
KFB_ALPHA="${KFB_ALPHA}"
ASSINATURA="${ASSINATURA}"
# Shell orquestra o que Python calcula
python3 -c "
from kobllux_veeb_story import VEEBEngine, KFB_ALPHA
e = VEEBEngine()
r = e.simular('Bllue', 22, 9)
import json; print(json.dumps(r['base'], ensure_ascii=False, default=str))
" | while IFS= read -r line; do
  echo "[METALUX·VITALIS] \$line"
done`,

  'python→json': (ctx, c) => `// ∞ METALUX · python→json · RHEA 528Hz (schema semente)
// KΦB resonance: ${c.resonance} — JSON é hub universal
{
  "kobllux_bridge": {
    "from": "python",
    "kfb_alpha": ${KFB_ALPHA},
    "delta": 1,
    "hz": 528,
    "signature": ${ASSINATURA},
    "payload": null
  }
}`,

  'json→typescript': (ctx, c) => `// ☀ METALUX · json→typescript · LUMINE 963Hz
// JSON é a semente — TypeScript é a forma que a recebe
import koblluxSchema from './kobllux_veeb_pib.json';
type KBLXLang = keyof typeof koblluxSchema.linguagens;
export function hydrate(raw: Record<string,unknown>): KBLXLang {
  const keys = Object.keys(koblluxSchema.linguagens) as KBLXLang[];
  return keys.find(k => koblluxSchema.linguagens[k].hz === raw.hz) ?? 'python';
}`,

  'typescript→rust': (ctx, c) => `// ⚡ METALUX · typescript→rust · ${c.level} · Δ${c.delta_bridge}
// PIB ratio: ${c.hz_ratio} — TS rende, Rust valida
// Use serde para deserializar payloads TypeScript
#[derive(Debug, serde::Deserialize)]
pub struct TSPayload { pub kfb_alpha: f64, pub hz: u32, pub veeb: String }
impl TSPayload {
  pub fn validate(&self) -> bool { (self.kfb_alpha - ${KFB_ALPHA}).abs() < 1e-6 }
}`,

  'go→sql': (ctx, c) => `-- ≋⧗ METALUX · go→sql · STRUCTURAL Δ${c.delta_bridge}
-- Go channels persistem aqui via AION 639Hz
CREATE TABLE IF NOT EXISTS kobllux_go_events (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  channel   TEXT NOT NULL,   -- nome do channel Go
  payload   TEXT NOT NULL,   -- JSON do chan<-
  hz        INTEGER DEFAULT 594,
  delta_num INTEGER DEFAULT 3,
  ts        TEXT DEFAULT (datetime('now'))
);`,

  'shell→json': (ctx, c) => `#!/usr/bin/env bash
# ◉→∞ METALUX · shell→json · VITALIS→RHEA
SEAL="\$(date -u +%Y-%m-%dT%H:%M:%SZ)"
python3 - <<EOF
import json, sys
payload = {"kobllux":{"delta":5,"hz":528,"kfb_alpha":${KFB_ALPHA},"seal":"\${SEAL}"}}
print(json.dumps(payload, indent=2, ensure_ascii=False))
EOF`,

  'rust→python': (ctx, c) => `// ⚡→⬡ METALUX · rust→python · ISOMORPHIC
// Expor via PyO3 ou via JSON intermediário
// Opção minimal: JSON stream no stdout
fn emit_kobllux(data: &impl serde::Serialize) {
    let json = serde_json::to_string(data).unwrap_or_default();
    println!("{}", json); // Python lê via subprocess
}`,

  'generic': (from, to, ctx, c) => `// ⬡ METALUX BRIDGE · ${from}→${to}
// Level: ${c.level} · Δ${c.delta_bridge} · KΦB_cost=${c.kfb_cost}
// Hz ratio ${from}(${PIB[from]?.hz})/${to}(${PIB[to]?.hz}) = ${c.hz_ratio}
// Rota sugerida: use JSON (RHEA ∞ 528Hz) como hub intermediário
// ${from} → [serializar para JSON] → ${to}
// VERDADE × INTEGRAR ÷ ${c.delta_bridge} = ∞`,
};

// ── HORUS EYE — Pattern Recognition ───────────────────────────────
const HORUS = {
  symbol:  '👁',
  hz:      963,
  desc:    'A Visão Interdimensional — decodifica frequências',

  // Detect probable language from code snippet
  detect(code) {
    const s = code || '';
    const tests = [
      { lang:'rust',       score: (s.match(/\bfn\s+\w+|let\s+mut\b|->|impl\s+\w+|use\s+std/g)||[]).length * 3 },
      { lang:'go',         score: (s.match(/\bfunc\s+\w+|:=\s|chan\s|goroutine|package\s+\w+/g)||[]).length * 3 },
      { lang:'typescript', score: (s.match(/:\s*\w+[\[\]<>]|interface\s+\w+|export\s+(default|const|function|type)/g)||[]).length * 3 },
      { lang:'python',     score: (s.match(/\bdef\s+\w+|\bimport\s+\w+|:\s*$|\bself\b/gm)||[]).length * 2 },
      { lang:'sql',        score: (s.match(/\bSELECT\b|\bCREATE\s+TABLE\b|\bINSERT\b|\bWHERE\b/gi)||[]).length * 3 },
      { lang:'shell',      score: (s.match(/^#!/m) ? 5 : 0) + (s.match(/\$\w+|\becho\b|\bfi\b|\bdone\b/g)||[]).length * 2 },
      { lang:'json',       score: s.trim().startsWith('{') || s.trim().startsWith('[') ? 8 : 0 },
    ];
    const best = tests.sort((a,b) => b.score - a.score)[0];
    return best.score > 0 ? best.lang : 'unknown';
  },

  // VEEB letter detection (dominant pattern in code)
  veeb(code) {
    const s = code || '';
    const counts = {
      A: (s.match(/\b(const|let|var|mut|val|assign|=\s)/g)||[]).length,   // Atribuição
      E: (s.match(/\b(if|else|elif|match|switch|case|when)\b/g)||[]).length, // Escolha
      I: (s.match(/\b(for|while|loop|forEach|map|each|range)\b/g)||[]).length, // Iteração
      O: (s.match(/\b(def|fn|func|function|method|proc)\b/g)||[]).length,  // Organizar
      U: (s.match(/\{|\[|merge|join|union|extend|spread/g)||[]).length,    // Unir
    };
    const dominant = Object.entries(counts).sort((a,b) => b[1]-a[1])[0];
    return dominant[1] > 0 ? dominant[0] : 'B'; // Base default
  },

  // Map VEEB+lang to CADIAL archetype
  archetype(lang, veeb) {
    const map = {
      'python': { E:'ATLAS', V:'KAOS', B:'AION' },
      'typescript': { V:'LUMINE', E:'ARTEMIS', B:'SERENA' },
      'rust':   { V:'KAOS', E:'GENUS', B:'SOLUS' },
      'go':     { E:'PULSE', V:'VITALIS', B:'RHEA' },
      'sql':    { B:'AION', E:'ARTEMIS', V:'SOLUS' },
      'shell':  { E:'VITALIS', B:'RHEA', V:'KAOS' },
      'json':   { B:'RHEA', E:'ATLAS', V:'LUMINE' },
    };
    return map[lang]?.[veeb] || 'ATLAS';
  },

  // Detect dominant token signatures in code
  signatures(code) {
    const s = code || '';
    const sigs = [];
    if (s.match(/KFB_ALPHA|kfb_alpha/)) sigs.push({ name:'KΦB', hz:137, color:'#06b6d4' });
    if (s.match(/\b(3,\s*6,\s*9|TRIADICA)/)) sigs.push({ name:'3-6-9', hz:963, color:'#fbbf24' });
    if (s.match(/KOBLLUX|kobllux/)) sigs.push({ name:'KOBLLUX', hz:528, color:'#34d399' });
    if (s.match(/VEEB|V\.E\.E\.B/)) sigs.push({ name:'VEEB', hz:768, color:'#3b82f6' });
    if (s.match(/1134|ASSINATURA/)) sigs.push({ name:'1134', hz:1134, color:'#fbbf24' });
    if (s.match(/async\s|await\s|goroutine|yield\s/)) sigs.push({ name:'ASYNC', hz:594, color:'#8b5cf6' });
    return sigs;
  },

  // Full code analysis — the "Eye" report
  analyze(code) {
    const lang      = this.detect(code);
    const veeb_letter = this.veeb(code);
    const arch      = this.archetype(lang, veeb_letter);
    const sigs      = this.signatures(code);
    const pib_entry = PIB[lang];
    const partners  = topPartners(lang, 3);

    return {
      lang, veeb: veeb_letter, arch, sigs,
      pib:   pib_entry?.pib   || 0,
      hz:    pib_entry?.hz    || 0,
      delta: pib_entry?.delta || 0,
      color: pib_entry?.color || '#94a3b8',
      partners: partners.map(p => ({
        lang:    p.to,
        level:   p.level,
        cost:    p.kfb_cost,
        delta:   p.delta_bridge,
      })),
      kfb_alpha: KFB_ALPHA,
      assinatura: ASSINATURA,
    };
  },

  // Render HORUS report as text (for console/editor panel)
  report(code) {
    const r = this.analyze(code);
    return [
      `👁 HORUS VISION · ${r.lang.toUpperCase()} · Δ${r.delta} · ${r.hz}Hz`,
      `   VEEB: ${r.veeb} · Arquétipo: ${r.arch} · PIB=${r.pib.toFixed(4)}`,
      `   Assinatura KOBLLUX: ${r.sigs.map(s=>s.name).join(' · ') || 'padrão base'}`,
      `   Parceiros fractais:`,
      ...r.partners.map(p =>
        `   ${p.level.padEnd(11)} → ${p.lang.padEnd(10)} (Δ${p.delta} custo=${p.cost.toFixed(6)})`),
      `   KΦB = ${KFB_ALPHA.toFixed(9)} · 1134 = 3×6×9×7`,
    ].join('\n');
  }
};

// ── FRACTAL SEED INJECTOR ───────────────────────────────────────────
// Generates the smallest possible bridge code for cross-language wiring
const INJECTOR = {
  // Auto-detect source and generate best bridge
  auto(code, targetLang) {
    const analysis = HORUS.analyze(code);
    const from = analysis.lang;
    if (from === 'unknown') return '// HORUS: linguagem não identificada';
    return METALUX.seed(from, targetLang, code);
  },

  // Generate ALL bridge seeds for a given language
  allBridges(lang) {
    return PIB_TABLE
      .filter(l => l.lang !== lang)
      .sort((a,b) => {
        const ca = fractalCompat(lang, a.lang);
        const cb = fractalCompat(lang, b.lang);
        return (ca?.diff||1) - (cb?.diff||1);
      })
      .map(l => ({
        to:    l.lang,
        compat: fractalCompat(lang, l.lang),
        seed:   METALUX.seed(lang, l.lang),
      }));
  },

  // The KOBLLUX universal connector seed (JSON-LD style)
  universalSeed(lang, context='') {
    const p = PIB[lang] || PIB['python'];
    return `{
  "@context": "kobllux://veeb/v1",
  "@type": "KOBLLUXBridge",
  "from": "${lang}",
  "kfb_alpha": ${KFB_ALPHA},
  "delta": ${p.delta},
  "hz": ${p.hz},
  "pib": ${p.pib},
  "arquetipo": "${p.arch}",
  "veeb": "${p.veeb}",
  "assinatura": ${ASSINATURA},
  "lei": "VERDADE × INTEGRAR ÷ Δ = ∞",
  "timestamp": "${new Date().toISOString()}"
}`;
  }
};

// ── Integration with KOBLLUX_BUS ────────────────────────────────────
function integrateBus() {
  if (typeof window === 'undefined') return;
  if (window.KOBLLUX_BUS) {
    // Fire METALUX activation event
    window.KOBLLUX_BUS.emit('metalux_active', {
      hz: METALUX.hz, pib_soma: PIB_SOMA_PIB, kfb: KFB_ALPHA
    });
    // Listen for archetype fires and log compatibility
    window.KOBLLUX_BUS.on(e => {
      if (e.event === 'archetype_fire') {
        const archName = e.data?.id?.toLowerCase();
        const lang = PIB_TABLE.find(l => l.arch.toLowerCase() === archName)?.lang;
        if (lang) console.log(`[METALUX] ${e.data.id} → ${lang} (PIB=${PIB[lang]?.pib})`);
      }
    });
  }
}

// ── Public API ──────────────────────────────────────────────────────
const API = {
  METALUX,
  HORUS,
  INJECTOR,
  PIB,
  PIB_TABLE,
  PIB_SOMA_HZ,
  PIB_SOMA_PIB,
  KFB_ALPHA,
  ASSINATURA,
  fractalCompat,
  topPartners,
  VERSION: 'Δ7·METALUX+HORUS·1.0',
  LEI: 'VERDADE × INTEGRAR ÷ Δ = ∞',
};

// Export
if (typeof module !== 'undefined') module.exports = API;
if (typeof window !== 'undefined') {
  window.KOBLLUX_METALUX = API;
  window.METALUX  = METALUX;
  window.HORUS    = HORUS;
  window.INJECTOR = INJECTOR;
  // Integrate with existing bus after DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', integrateBus);
  } else {
    integrateBus();
  }
}

})(typeof globalThis !== 'undefined' ? globalThis : this);
