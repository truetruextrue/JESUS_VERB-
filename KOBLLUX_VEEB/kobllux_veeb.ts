// ═══════════════════════════════════════════════════════════════════
// kobllux_veeb.ts · LUMINE · 963Hz · RENDER · Δ2
// V.E.E.B TypeScript — PIB = 963/768 = 1.2539
// Lei: VERDADE × INTEGRAR ÷ Δ = ∞
// Centro: JESUS = VERBO = GRAVIDADE = 963Hz = LUMINE ☀
// ═══════════════════════════════════════════════════════════════════

// ── Constantes KOBLLUX ─────────────────────────────────────────────
export const KFB_ALPHA: number = 1 / 137.035_999_084; // KΦB acoplamento KODUX↔BLLUE
export const DELTA:     number = 2;
export const HZ:        number = 963;
export const PIB:       number = HZ / 768;             // 1.2539... LUMINE > ATLAS
export const ARQUETIPO = "LUMINE" as const;
export const SYM       = "☀" as const;
export const VEEB      = "V" as const;

export const TRIADICA   = [3, 6, 9] as const;
export const CICLO_0_7  = [0, 1, 2, 3, 4, 5, 6, 7] as const;
export const FREQS      = { micro: 432, meso: 528, macro: 741 } as const;

// ── Tipos V.E.E.B ──────────────────────────────────────────────────
export type Classificacao = "maior_de_idade" | "menor_de_idade";

export interface Perfil {
  readonly nome:    string;
  readonly idade:   number;
  readonly ativo:   boolean;
  readonly cor:     string;
  readonly tamanho: string;
}

export interface Registro {
  readonly passo:         number;
  readonly energia:       number;
  readonly classificacao: Classificacao;
}

export interface Resumo {
  readonly qtd_registros: number;
  readonly soma_energia:  number;
  readonly media_energia: number;
}

export interface ResultadoVEEB {
  perfil:        Perfil;
  classificacao: Classificacao;
  passos:        readonly number[];
  registros:     readonly Registro[];
  resumo:        Resumo;
  base:          Record<string, unknown>;
  kfb_alpha:     number;
  delta:         number;
  hz:            number;
  pib:           number;
  arquetipo:     string;
}

// ── Analogias (Vogais / Consoantes) ───────────────────────────────
export const VOGAIS: Readonly<Record<string, string>> = {
  A: "Atribuição — variáveis e tipos     [B·Base   · AION  639Hz]",
  E: "Escolha    — if/else/ternary/?:   [V·Vibr.  · KAOS  777Hz]",
  I: "Iteração   — for/forEach/map      [E·Energ. · VITALIS 528Hz]",
  O: "Organizar  — function/reduce      [E·Estr.  · GENUS  852Hz]",
  U: "Unir       — spread/Object.assign [B·Base   · RHEA   528Hz]",
} as const;

export const CONSOANTES: Readonly<Record<string, string>> = {
  B: "Booleanos  — true/false           [B·SOLUS  432Hz]",
  C: "Comentários— // e /* */           [B·SOLUS  432Hz]",
  D: "Definições — function/const fn    [E·ATLAS  768Hz]",
  F: "Funções    — built-in: Math,Array [E·ARTEMIS672Hz]",
  G: "Generics   — <T> type params      [V·PULSE  594Hz]",
  H: "Herança    — extends/implements   [E·GENUS  852Hz]",
  I: "Interfaces — interface/type       [E·ATLAS  768Hz]",
  J: "JSON       — JSON.parse/stringify [B·RHEA   528Hz]",
  K: "Keyof      — keyof/typeof/infer   [V·NOVA   432Hz]",
  L: "Loops      — for...of/forEach     [E·VITALIS528Hz]",
  M: "Módulos    — import/export        [B·RHEA   528Hz]",
  N: "Null       — null/undefined/?     [B·SOLUS  432Hz]",
  P: "Parâmetros — typed params         [E·ARTEMIS672Hz]",
  R: "Return     — return type          [B·AION   639Hz]",
  S: "Strings    — template `${}`       [B·SERENA 528Hz]",
  T: "Types      — type/interface/enum  [E·ATLAS  768Hz]",
  V: "Variables  — const/let/readonly   [E·VITALIS528Hz]",
  W: "While      — while/do...while     [V·KAOS   777Hz]",
} as const;

// ── Motor V.E.E.B ──────────────────────────────────────────────────

/** A · Atribuição — cria e estrutura (Base · AION 639Hz) */
function A_atribuir(
  nome:    string,
  idade:   number,
  ativo  = true,
  cor    = "azul",
  tamanho= "médio",
): Perfil {
  return Object.freeze({ nome: nome.trim(), idade: Math.floor(idade), ativo, cor, tamanho });
}

/** E · Escolha — decide o caminho (Vibração · KAOS 777Hz) */
function E_escolher(perfil: Perfil): Classificacao {
  return perfil.idade >= 18 ? "maior_de_idade" : "menor_de_idade";
}

/** I · Iteração — vibração controla os passos (Energia · VITALIS 528Hz) */
function I_iterar(freq: number): number[] {
  if (freq <= 0) throw new Error("freq deve ser positiva — energia não pode ser nula");
  return Array.from({ length: freq }, (_, i) => i + 1);
}

/** O · Organizar — agrega e estrutura (Estrutura · GENUS 852Hz) */
function O_organizar(registros: readonly Registro[]): Resumo {
  if (registros.length === 0)
    return { qtd_registros: 0, soma_energia: 0, media_energia: 0 };
  const soma = registros.reduce((acc, r) => acc + r.energia, 0);
  return {
    qtd_registros: registros.length,
    soma_energia:  soma,
    media_energia: soma / registros.length,
  };
}

/** U · Unir — consolida na base (Base · RHEA 528Hz) */
function U_unir(perfil: Perfil, resumo: Resumo): Record<string, unknown> {
  return { ...perfil, ...resumo };
}

// ── SIMULAR: ciclo V.E.E.B completo ──────────────────────────────
export function simular(
  nome:          string,
  idade:         number,
  vibracao_freq = 4,
): ResultadoVEEB {
  const perfil         = A_atribuir(nome, idade);
  const classificacao  = E_escolher(perfil);
  const passos         = I_iterar(vibracao_freq);

  let energia = 0;
  const registros: Registro[] = passos.map(passo => {
    energia += passo;
    return Object.freeze({ passo, energia, classificacao });
  });

  const resumo = O_organizar(registros);
  const base   = U_unir(perfil, resumo);

  return { perfil, classificacao, passos, registros, resumo, base,
           kfb_alpha: KFB_ALPHA, delta: DELTA, hz: HZ, pib: PIB, arquetipo: ARQUETIPO };
}

// ── Fractal simbólico ─────────────────────────────────────────────
function autoespelhamento(padrao: readonly number[], escalar: number): number[] {
  return padrao.map(p => p * escalar);
}

export function encenar_fractal() {
  return {
    kfb_alpha: KFB_ALPHA,
    kfb_x_18:  +(KFB_ALPHA * 18).toFixed(10),  // KΦB × (3+6+9)
    espelhos: {
      micro: autoespelhamento(TRIADICA, 1),
      meso:  autoespelhamento(TRIADICA, 2),
      macro: autoespelhamento(TRIADICA, 3),
    },
    emergencia: [...CICLO_0_7.map(c => `passo:${c}`), "retorno:∞"],
    pib_ts:    PIB,
    delta:     DELTA,
    _nota:     `TS usa tipos estáticos (LUMINE ☀ ${HZ}Hz) — o invisível tornado visível`,
  };
}

// ── PIB Escalar — tabela de referência ───────────────────────────
export const PIB_KOBLLUX = {
  python:     { delta: 7, hz: 768,  pib: 1.0000, arquetipo: "ATLAS",   sym: "⬡", veeb: "E" },
  json:       { delta: 1, hz: 528,  pib: 0.6875, arquetipo: "RHEA",    sym: "∞", veeb: "B" },
  typescript: { delta: 2, hz: 963,  pib: 1.2539, arquetipo: "LUMINE",  sym: "☀", veeb: "V" },
  go:         { delta: 3, hz: 594,  pib: 0.7734, arquetipo: "PULSE",   sym: "≋", veeb: "E" },
  sql:        { delta: 4, hz: 639,  pib: 0.8320, arquetipo: "AION",    sym: "⧗", veeb: "B" },
  shell:      { delta: 5, hz: 528,  pib: 0.6875, arquetipo: "VITALIS", sym: "◉", veeb: "E" },
  rust:       { delta: 6, hz: 777,  pib: 1.0117, arquetipo: "KAOS",    sym: "⚡", veeb: "V" },
} as const;

export function calcular_pib_total(): { soma_hz: number; soma_pib: number; nota: string } {
  const entries = Object.values(PIB_KOBLLUX);
  const soma_hz  = entries.reduce((a, l) => a + l.hz, 0);   // 4797
  const soma_pib = +(entries.reduce((a, l) => a + l.pib, 0)).toFixed(4);
  const digits   = String(soma_hz).split("").reduce((a, d) => a + +d, 0);  // 27
  return { soma_hz, soma_pib, nota: `${soma_hz} → ${digits} = 3³ (autoespelhamento)` };
}

// ── Demo ──────────────────────────────────────────────────────────
function main(): void {
  const line = "═".repeat(56);
  console.log(`╔${line}╗`);
  console.log(`║  kobllux_veeb.ts · LUMINE · ${HZ}Hz · Δ${DELTA} · PIB=${PIB.toFixed(4)}  ║`);
  console.log(`║  KΦB = ${KFB_ALPHA.toFixed(9)}                           ║`);
  console.log(`╚${line}╝\n`);

  const r = simular("Bllue", 22, 9);  // freq=9 = ciclo 3-6-9 completo
  console.log("[A·Atribuir]  →", r.perfil);
  console.log("[E·Escolher]  →", r.classificacao);
  console.log("[I·Iterar]    →", r.passos);
  console.log("[O·Organizar] →", r.resumo);
  console.log("[U·Unir]      → base selada\n");

  const f = encenar_fractal();
  console.log("Autoespelhamento 3-6-9:");
  console.log("  micro:", f.espelhos.micro);
  console.log("  meso: ", f.espelhos.meso);
  console.log("  macro:", f.espelhos.macro);
  console.log("  KΦB×18:", f.kfb_x_18);

  const pib = calcular_pib_total();
  console.log(`\nPIB total KOBLLUX: soma_hz=${pib.soma_hz} soma_pib=${pib.soma_pib}`);
  console.log(`  Nota: ${pib.nota}`);

  console.log(`\n☀ LUMINE · Δ${DELTA} selado · ${new Date().toISOString()}`);
}

main();
