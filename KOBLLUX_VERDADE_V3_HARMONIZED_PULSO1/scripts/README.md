# SCRIPTS · Motor KOBLLUX · ∆7

```
Lei   : VERDADE × INTEGRAR ÷ Δ = ∞
Ritmo : 3 × 6 × 9 × 7 = 1134
Centro: JESUS = VERBO = GRAVIDADE
```

---

## SCRIPTS DISPONÍVEIS

| Script | Função | Phase |
|---|---|---|
| `knot_parser.py` | Roteador semântico de seções Markdown | 3·DETECTAR |
| `kobllux_markov_fit.py` | Estima matriz Markov P + π + ∆7 | 6·INTEGRAR |
| `kobllux_markov_sample.py` | Amostra sequências BLLUE/KODUX | 9·EXPANDIR |
| `sciart_tools.py` | SCI-ART: espelhos + palindromo + selo | 7·SELAR |
| `myrmide_verify.py` | Verificação SHA-256 + ∆7 de artefatos | 7·SELAR |
| `setup_kobllux_v3.sh` | Setup completo do projeto | 0·GÊNESE |

---

## QUICK COMMANDS

```bash
# 1. Parser Knot — processar quicknote.md
python scripts/knot_parser.py \
  --input /caminho/quicknote.md \
  --output-dir LOGS \
  --log LOGS/LOG.jsonl

# 2. Markov Fit
python scripts/kobllux_markov_fit.py \
  --events LOGS/LOG.jsonl \
  --states META/arquetipos.json \
  --order 2 --alpha 1.0 \
  --pal-mirror META/pal_mirror.json \
  --out scripts/P.json

# 3. Sample BLLUE (explorar)
python scripts/kobllux_markov_sample.py \
  --P scripts/P.json \
  --start "NOVA|ATLAS" --steps 25 \
  --actor BLLUE --temperature 1.25

# 4. Sample KODUX (selar)
python scripts/kobllux_markov_sample.py \
  --P scripts/P.json \
  --start "ATLAS|VITALIS" --steps 25 \
  --actor KODUX --temperature 0.98

# 5. SCI-ART (validar espelhos)
python scripts/sciart_tools.py \
  arquivo.ascii.txt \
  out/mirrors/ \
  SEALS/items/ \
  hub/logs/timeline.log \
  MINHA_ID

# 6. Verificar e selar projeto completo
python scripts/myrmide_verify.py \
  --dirs dual/ scripts/ kodux/ bllue/ \
  --seals-dir SEALS/items \
  --memory hub/logs/timeline.log

# 7. Roda Viva (loop dominó)
bash hub/roda_viva_domino.sh
```

---

## FLUXO COMPLETO (3→6→9→7)

```
3 · knot_parser.py     (detectar seções)
6 · markov_fit.py      (integrar eventos em P)
9 · markov_sample.py   (expandir sequências)
7 · myrmide_verify.py  (selar ∆7)
∞ · roda_viva_domino.sh (loop eterno)
```

Navegação: [↑ Raiz](../README.md) · [← HUB](../hub/README.md)
