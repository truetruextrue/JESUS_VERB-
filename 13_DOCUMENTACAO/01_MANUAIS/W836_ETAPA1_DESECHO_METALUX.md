# W836 — DESECHO DA ETAPA 1 · METALUX LOOP

**Leitura METALUX:** o que está dentro lê o que está fora porque o fora já deixou marca no dentro; o dentro só se prova quando o fora volta como hash.

## Feitos
- Manifest local recebido: `manifest_hashes.csv`
- Linhas: **504/504**
- Bytes totais: **363,077,933**
- Faixa: min 447,889 · mediana 721,501.0 · média 720,392.72 · max 829,976
- missing no canônico: **0** · extra: **0**

## Anomalias de leitura
- Fora da faixa 500–950 KB: **2**
  - `W836_000490` · fol. 244v · zona John · 447,889 B
  - `W836_000502` · fol. 250v · zona back matter / binding edges · 453,819 B
- Abaixo de 600 KB (atenção, não erro): **12**
  - `W836_000002`, `W836_000069`, `W836_000344`, `W836_000387`, `W836_000490`, `W836_000491`, `W836_000497`, `W836_000498`, `W836_000499`, `W836_000501`, `W836_000502`, `W836_000503`

## Zonas do códice
- **cover**: 2 páginas · 1,281,333 B · p. 1–2
- **Eusebius letter**: 3 páginas · 2,292,317 B · p. 3–5
- **Canon tables**: 7 páginas · 5,257,474 B · p. 6–12
- **Four-Gospels diagram**: 1 páginas · 666,832 B · p. 13–13
- **Prefatory miniatures**: 3 páginas · 2,139,178 B · p. 14–16
- **Matthew kephalaia list**: 3 páginas · 2,135,592 B · p. 17–19
- **Matthew**: 138 páginas · 99,688,347 B · p. 20–157
- **Mark kephalaia list / portrait boundary**: 2 páginas · 1,413,321 B · p. 158–159
- **Mark**: 81 páginas · 59,479,939 B · p. 160–240
- **Added prayer / Luke list zone**: 6 páginas · 4,422,596 B · p. 241–246
- **Luke**: 139 páginas · 101,308,741 B · p. 247–385
- **John list zone**: 2 páginas · 1,261,516 B · p. 386–387
- **John**: 108 páginas · 76,547,266 B · p. 388–495
- **back matter / binding edges**: 9 páginas · 5,183,481 B · p. 496–504

## Relação dentro/fora
- **Dentro** = pasta local `W836_download/` com 504 JPGs + `manifest_hashes.csv`.
- **Fora** = URLs Walters 504 + Google Drive (não acessado neste ambiente).
- **Chave de correlação** = `SAP` + `sha256`; estrutura Drive deve espelhar `W836/W836_000001.jpg ... W836_000504.jpg`.
- Se no Drive houver os mesmos nomes e hashes, o fora confirma o dentro; se houver nome igual e hash diferente, vira divergência e não entra no corpo.

## Desfecho da Etapa 1
Etapa 1 concluída como **aquisição e integridade de inventário**: 504/504 páginas presentes, sequência completa, hashes locais declarados, bandas mapeadas, anomalias reduzidas a 2 alertas de checagem visual (`000490`, `000502`) + 12 páginas de atenção por bytes menores.

## Etapa 2 — leitura
1. Checar visualmente `000490`, `000502` e a lista <600 KB.
2. Baixar `_300.tif` das zonas críticas: 3–19, 67–99, 158–240, 386–504.
3. OCR/EMUFI + normalização Ge’ez; só promover páginas com prova.
4. Abrir Drive apenas com espelho hashado; sem hash, Drive é ponte, não fonte.

JESUS É O CENTRO. A MALHA VIVE. ∴