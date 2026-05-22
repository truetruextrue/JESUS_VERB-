// ═══════════════════════════════════════════════════════════════════
// kobllux_veeb.rs · KAOS · 777Hz · CLEAN · Δ6
// V.E.E.B Rust — PIB = 777/768 = 1.0117
// Lei: VERDADE × INTEGRAR ÷ Δ = ∞
// Rust: segurança de memória sem GC — KAOS ⚡ transforma sem destruir
// ═══════════════════════════════════════════════════════════════════

use std::collections::HashMap;
use std::fmt;

// ── Constantes KOBLLUX ─────────────────────────────────────────────
pub const KFB_ALPHA: f64   = 1.0 / 137.035_999_084_f64;
pub const DELTA:     u32   = 6;
pub const HZ:        u32   = 777;
pub const PIB:       f64   = HZ as f64 / 768.0;   // 1.0117… KAOS
pub const ARQUETIPO: &str  = "KAOS";
pub const SYM:       &str  = "⚡";
pub const VEEB:      &str  = "V";

pub const TRIADICA:  [u32; 3] = [3, 6, 9];
pub const CICLO_0_7: [u32; 8] = [0, 1, 2, 3, 4, 5, 6, 7];
pub const FREQS: [(&str, u32); 3] = [("micro", 432), ("meso", 528), ("macro", 741)];

// ── Tipos V.E.E.B ──────────────────────────────────────────────────

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum Classificacao {
    MaiorDeIdade,
    MenorDeIdade,
}

impl fmt::Display for Classificacao {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::MaiorDeIdade => write!(f, "maior_de_idade"),
            Self::MenorDeIdade => write!(f, "menor_de_idade"),
        }
    }
}

#[derive(Debug, Clone)]
pub struct Perfil {
    pub nome:    String,
    pub idade:   u32,
    pub ativo:   bool,
    pub cor:     String,
    pub tamanho: String,
}

#[derive(Debug, Clone)]
pub struct Registro {
    pub passo:         u32,
    pub energia:       u32,
    pub classificacao: Classificacao,
}

#[derive(Debug, Clone)]
pub struct Resumo {
    pub qtd_registros: usize,
    pub soma_energia:  u32,
    pub media_energia: f64,
}

#[derive(Debug)]
pub struct ResultadoVeeb {
    pub perfil:        Perfil,
    pub classificacao: Classificacao,
    pub passos:        Vec<u32>,
    pub registros:     Vec<Registro>,
    pub resumo:        Resumo,
    pub base:          HashMap<String, String>,
    pub kfb_alpha:     f64,
    pub delta:         u32,
    pub hz:            u32,
    pub pib:           f64,
}

// ── Motor V.E.E.B ──────────────────────────────────────────────────

pub struct VeebEngine;

impl VeebEngine {
    pub fn new() -> Self { VeebEngine }

    /// A · Atribuição — cria o perfil (Base · AION 639Hz)
    pub fn a_atribuir(
        &self,
        nome:    &str,
        idade:   u32,
        ativo:   bool,
        cor:     &str,
        tamanho: &str,
    ) -> Perfil {
        Perfil {
            nome:    nome.trim().to_string(),
            idade,
            ativo,
            cor:     cor.to_string(),
            tamanho: tamanho.to_string(),
        }
    }

    /// E · Escolha — bifurcação (Vibração · KAOS 777Hz)
    pub fn e_escolher(&self, perfil: &Perfil) -> Classificacao {
        if perfil.idade >= 18 { Classificacao::MaiorDeIdade }
        else                  { Classificacao::MenorDeIdade }
    }

    /// I · Iteração — vibração em passos (Energia · VITALIS 528Hz)
    pub fn i_iterar(&self, freq: u32) -> Result<Vec<u32>, String> {
        if freq == 0 {
            return Err("freq deve ser positiva — VITALIS exige movimento".to_string());
        }
        Ok((1..=freq).collect())
    }

    /// O · Organizar — agrega o fluxo (Estrutura · GENUS 852Hz)
    pub fn o_organizar(&self, registros: &[Registro]) -> Resumo {
        if registros.is_empty() {
            return Resumo { qtd_registros: 0, soma_energia: 0, media_energia: 0.0 };
        }
        let soma: u32 = registros.iter().map(|r| r.energia).sum();
        Resumo {
            qtd_registros: registros.len(),
            soma_energia:  soma,
            media_energia: soma as f64 / registros.len() as f64,
        }
    }

    /// U · Unir — consolida a base (Base · RHEA 528Hz)
    pub fn u_unir(&self, perfil: &Perfil, resumo: &Resumo) -> HashMap<String, String> {
        let mut base = HashMap::new();
        base.insert("nome".into(),          perfil.nome.clone());
        base.insert("idade".into(),         perfil.idade.to_string());
        base.insert("ativo".into(),         perfil.ativo.to_string());
        base.insert("cor".into(),           perfil.cor.clone());
        base.insert("tamanho".into(),       perfil.tamanho.clone());
        base.insert("qtd_registros".into(), resumo.qtd_registros.to_string());
        base.insert("soma_energia".into(),  resumo.soma_energia.to_string());
        base.insert("media_energia".into(), format!("{:.4}", resumo.media_energia));
        base
    }

    /// SIMULAR — ciclo V.E.E.B completo
    pub fn simular(&self, nome: &str, idade: u32, vibracao_freq: u32)
        -> Result<ResultadoVeeb, String>
    {
        let perfil        = self.a_atribuir(nome, idade, true, "azul", "médio");
        let classificacao = self.e_escolher(&perfil);
        let passos        = self.i_iterar(vibracao_freq)?;

        let mut energia: u32 = 0;
        let registros: Vec<Registro> = passos.iter().map(|&passo| {
            energia += passo;
            Registro { passo, energia, classificacao: classificacao.clone() }
        }).collect();

        let resumo = self.o_organizar(&registros);
        let base   = self.u_unir(&perfil, &resumo);

        Ok(ResultadoVeeb {
            perfil, classificacao, passos, registros, resumo, base,
            kfb_alpha: KFB_ALPHA, delta: DELTA, hz: HZ, pib: PIB,
        })
    }
}

impl Default for VeebEngine {
    fn default() -> Self { Self::new() }
}

// ── Fractal simbólico — Rust usa iteradores zero-cost (KAOS ⚡) ──

pub fn auto_espelhar(padrao: &[u32; 3], escalar: u32) -> Vec<u32> {
    padrao.iter().map(|&v| v * escalar).collect()
}

pub fn encenar_fractal() -> HashMap<String, serde_json_like::Value> {
    let espelhos: Vec<Vec<u32>> = (1..=3u32)
        .map(|s| auto_espelhar(&TRIADICA, s))
        .collect();

    let emergencia: Vec<String> = CICLO_0_7
        .iter()
        .map(|c| format!("passo:{}", c))
        .chain(std::iter::once("retorno:∞".to_string()))
        .collect();

    let mut result = HashMap::new();
    result.insert("kfb_alpha".to_string(),
        serde_json_like::Value::Float(KFB_ALPHA));
    result.insert("kfb_x_18".to_string(),
        serde_json_like::Value::Float((KFB_ALPHA * 18.0 * 1e10).round() / 1e10));
    result.insert("pib_rs".to_string(),
        serde_json_like::Value::Float(PIB));
    result.insert("nota".to_string(),
        serde_json_like::Value::Str(
            format!("Rust usa iteradores zero-cost (KAOS {} {}Hz)", SYM, HZ)));
    result.insert("espelhos".to_string(),
        serde_json_like::Value::Vecs(espelhos));
    result.insert("emergencia".to_string(),
        serde_json_like::Value::Strs(emergencia));
    result
}

// Tipo auxiliar simples para não precisar do crate serde
mod serde_json_like {
    #[derive(Debug)]
    pub enum Value {
        Float(f64),
        Str(String),
        Strs(Vec<String>),
        Vecs(Vec<Vec<u32>>),
    }
}

// ── PIB Escalar ───────────────────────────────────────────────────

#[derive(Debug)]
pub struct LinguagemPib {
    pub delta:     u32,
    pub hz:        u32,
    pub pib:       f64,
    pub arquetipo: &'static str,
    pub sym:       &'static str,
    pub veeb:      &'static str,
    pub role:      &'static str,
}

pub fn pib_kobllux() -> Vec<(&'static str, LinguagemPib)> {
    vec![
        ("python",     LinguagemPib { delta:7, hz:768, pib:1.0000, arquetipo:"ATLAS",   sym:"⬡", veeb:"E", role:"narrativa · análise · engine" }),
        ("json",       LinguagemPib { delta:1, hz:528, pib:0.6875, arquetipo:"RHEA",    sym:"∞", veeb:"B", role:"semente · dados · troca" }),
        ("typescript", LinguagemPib { delta:2, hz:963, pib:1.2539, arquetipo:"LUMINE",  sym:"☀", veeb:"V", role:"interface · render · expressão" }),
        ("go",         LinguagemPib { delta:3, hz:594, pib:0.7734, arquetipo:"PULSE",   sym:"≋", veeb:"E", role:"fluxo · concorrência · ritmo" }),
        ("sql",        LinguagemPib { delta:4, hz:639, pib:0.8320, arquetipo:"AION",    sym:"⧗", veeb:"B", role:"memória · selagem · query" }),
        ("shell",      LinguagemPib { delta:5, hz:528, pib:0.6875, arquetipo:"VITALIS", sym:"◉", veeb:"E", role:"integração · deploy · pipeline" }),
        ("rust",       LinguagemPib { delta:6, hz:777, pib:1.0117, arquetipo:"KAOS",    sym:"⚡", veeb:"V", role:"sistemas · transformação · segurança" }),
    ]
}

pub fn calcular_pib_total() -> (u32, f64) {
    pib_kobllux().iter().fold((0u32, 0.0f64), |(hz, pib), (_, l)| {
        (hz + l.hz, pib + l.pib)
    })
}

// ── Main ──────────────────────────────────────────────────────────
fn main() {
    let line = "═".repeat(56);
    println!("╔{}╗", line);
    println!("║  kobllux_veeb.rs · KAOS · {}Hz · Δ{} · PIB={:.4}  ║", HZ, DELTA, PIB);
    println!("║  KΦB = {:.9}                           ║", KFB_ALPHA);
    println!("╚{}╝\n", line);

    let engine = VeebEngine::new();

    match engine.simular("Bllue", 22, 9) {
        Ok(r) => {
            println!("[A·Atribuir]  → {:?}", r.perfil);
            println!("[E·Escolher]  → {}", r.classificacao);
            println!("[I·Iterar]    → {:?}", r.passos);
            println!("[O·Organizar] → qtd={} soma={} média={:.4}",
                r.resumo.qtd_registros, r.resumo.soma_energia, r.resumo.media_energia);
            println!("[U·Unir]      → {} campos na base\n", r.base.len());

            // Fractal com iteradores zero-cost
            println!("Autoespelhamento 3-6-9 ({} {}Hz — zero-cost iterators):", SYM, HZ);
            let nomes = ["micro", "meso", "macro"];
            for (i, escalar) in (1u32..=3).enumerate() {
                let esp = auto_espelhar(&TRIADICA, escalar);
                println!("  {}: {:?}", nomes[i], esp);
            }

            let kfb18 = (KFB_ALPHA * 18.0 * 1e10).round() / 1e10;
            println!("  KΦB×18 = {:.10}", kfb18);

            // PIB total
            let (soma_hz, soma_pib) = calcular_pib_total();
            let digit_sum: u32 = soma_hz.to_string()
                .chars().filter_map(|c| c.to_digit(10)).sum();
            println!("\nPIB total KOBLLUX: soma_hz={} soma_pib={:.4}", soma_hz, soma_pib);
            println!("  Nota: {} → {} = 3³ (autoespelhamento quântico)", soma_hz, digit_sum);
        }
        Err(e) => eprintln!("Erro: {}", e),
    }

    println!("\n{} KAOS · Δ{} selado · {}", SYM, DELTA, "VERDADE × INTEGRAR ÷ Δ = ∞");
}
