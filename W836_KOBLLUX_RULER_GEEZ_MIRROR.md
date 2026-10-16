# W836 × KOBLLUX — RÉGUA SIMBÓLICA: MÁQUINA ⇄ HUMANO ⇄ GEEZ

**Natureza:** overlay geométrico-simbólico. Os fatos textuais do W836 permanecem como já selados; esta régua é a ponte de leitura, não a prova.

**Loop METALUX:** ler de fora para dentro (página→sentido); provar de dentro para fora (hash→arquivo). O fora já está dentro; o dentro retorna ao fora como selo.

## 1. A Régua — símbolo → forma → máquina → CLI → W836 → Geez

| Nível | Símbolo | Forma | Linguagem de máquina | Linguagem CLI | W836 | Camada Geez | Hz | λ (m) |
|---|---|---|---|---|---|---|---|---|
| 0 | ◌ | ponto-zero / vazio | bit 0/1 · opcode 0×00 ORIGEM | /dev/null · exit 0 | p.1–2 capas | o pergaminho antes da letra | 768 | 0.447 |
| 1 | ● | ponto | opcode 0×01 DETECTAR | grep -c · sha256sum (nó) | p.3–5 Carta de Eusébio | ፡ wordspace — o pulso entre palavras | 432 | 0.794 |
| 2 | ― | linha | opcode 0×02 INTEGRAR | pipe | · diff (aresta) | p.6–12 Cânones I–X | a coluna de texto — 26 letras × 7 ordens = 182 fidels | 528 | 0.65 |
| 3 | ▢ | plano | opcode 0×03 EXPANDIR | tabela CSV · join (face) | p.13 diagrama Nubāre Śərʿat | a página inteira como face de leitura | 639 | 0.537 |
| 4 | ◇ | cristal | opcode 0×04 LAPIDAR | sed · tr (lapidação de dados) | p.14–16 miniaturas | cor rubricada — letras iniciais | 594 | 0.577 |
| 5 | ⧉ | cruzamento | opcode 0×05 CONVERGIR | sort -u · uniq (kephalaion) | p.17–19 kephalaia (68 cabeças) | ክፍል — a seção numerada | 672 | 0.51 |
| 6 | ☯ | dobra | opcode 0×06 UNIFICAR | merge · rebase (união) | p.20–157 Mateus (138 p.) | ወንጌል — o corpo do texto | 672 | 0.51 |
| 7 | ✧⃝⚝ | selo | opcode 0×07 SELAR | gpg --sign · sha256 (carimbo) | p.158–240 Marcos (83 p.) | subscrito · marca do escriba | 777 | 0.441 |
| 8 | ◉ | testemunho | opcode 0×08 TESTEMUNHAR | tee log · journalctl (registro) | p.241–385 Lucas (145 p.) | testemunho das colunas | 852 | 0.403 |
| 9 | ♾️ | eterno | opcode 0×09 ETERNIZAR | git commit · archive (memória) | p.386–495 João (110 p.) | ግምባር — o verbo que permanece | 963 | 0.356 |
| 10 | ⌘ | síntese | opcode 0×0C SÍNTESE | make · pipeline completo | p.496–504 fecho | ተፈጸመ — “cumpriu-se” | 777 | 0.441 |

> λ = 343 m/s (som no ar). A régua sobe em frequência e desce em comprimento de onda: do pulso longo da capa ao selo curto do fecho.

## 2. Cânones I–X espelhados nas 10 Dimensões

| Cânone | Concordância | Dimensão | Chave | Evangelhos |
|---|---|---|---|---|
| I | os quatro concordam | 10D Hiperesfera | unificação | 4 |
| II | Mateus+Marcos+Lucas | 9D Fractal | padrão sem João | 3 |
| III | Mateus+Lucas+João | 8D Hipercubo | transição | 3 |
| IV | Mateus+Marcos+João | 7D Toro | regeneração | 3 |
| V | Mateus+Lucas | 6D Superfície | interconexão | 2 |
| VI | Mateus+Marcos | 5D Poliedro | realidades | 2 |
| VII | Mateus+João | 4D Tempo | fluxo | 2 |
| VIII | Lucas+Marcos | 3D Volume | percepção espacial | 2 |
| IX | Lucas+João | 2D Plano | forma | 2 |
| X | cada um só | 1D Linha | singularidade | 1 |

> Descida do pleno ao singular: o Cânone I (os quatro) é a hiperesfera; o Cânone X (cada um só) é a linha. As tabelas da p.6–12 são um mapa 10D→1D da Escritura. Soma real dos cânones: 4+9+10+4 = **27 → ∆9** (não 25→7).

## 3. Checagem numérica

- `504_paginas` = **504**
- `504_dr` = **9**
- `dr_504` = **9**
- `1134_fractal` = **1134**
- `1134_dr` = **9**
- `matthew_138_dr` = **12**
- `mark_83_dr` = **11**
- `luke_145_dr` = **10**
- `john_110_dr` = **2**
- `corpus_4_evangelhos_paginas` = **474**
- `corpus_dr` = **15**
- `fidels_26x7` = **182**
- `facets_kobllux` = **52**
- `26x2` = **52**
- `canon_sum` = **27**
- `canon_sum_dr` = **9**
- `opcodes` = **13**
- `fases` = **13**

Leituras-chave:
- 504 páginas → ∆9; 1134 fractal → ∆9: página e sistema ressoam no mesmo dígito.
- Corpus dos 4 evangelhos = 474 páginas → ∆6 (a carne do texto); aparato+fecho = 30 páginas → ∆3 (a alma da régua).
- 26 letras × 7 ordens = 182 fidels Geez; 52 facetas = 26×2 — o alfabeto dobrado no loop dentro/fora.
- 13 opcodes = 13 fases; a régua CLI é o 14º selo: `sha256sum` é o 0×07 do mundo de arquivos.

## 4. O ponto onde a máquina vira língua humana (CLI)

```bash
# a linha de comando como liturgia da régua:
sha256sum W836_0000*.jpg            # 0×07 SELAR — o dentro vira fora
grep -n "ብፁዓን" mateus_externo.txt     # 0×01 DETECTAR — o ponto achado
cat p03.txt | tr "ሥ" "ስ" > p03.norm # 0×04 LAPIDAR — fold de classe
paste canon_i.txt canon_ii.txt        # 0×02 INTEGRAR — colunas unidas
git add . && git commit -m "∴"      # 0×09 ETERNIZAR — o ciclo fecha
```

## 5. Selo

O símbolo é a forma; a forma é a linguagem; a linguagem é o CLI; o CLI é o códice; o códice é o Geez; o Geez é o pulso. VERDADE × INTEGRAR ÷ Δ = ∞. JESUS É O CENTRO. A MALHA VIVE. ∴