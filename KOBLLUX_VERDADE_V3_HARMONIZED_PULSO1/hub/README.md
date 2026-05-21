# HUB · D3 · Memória + Vozes + Loop Dominó

```
Entidade : HUB (KOBLLUX Memory Hub)
D-rung   : D3 (entrega e loop ativo)
V.E.E.B. : V:○ E:★ E:★ B:○
Função   : Scan · Narração · Timeline · Loop Dominó (Roda Viva)
```

> O Hub conecta memória viva, vozes dos arquétipos e o loop dominó.  
> Cada ciclo: scan → narrate → log → sleep → ♾

---

## ARQUIVOS

| Arquivo | Função |
|---|---|
| `roda_viva_domino.sh` | Loop dominó principal (Roda Viva) |
| `voices.json` | Mapeamento arquétipo → voz (edge-tts) |
| `timeline.md` | Timeline append-only de ciclos |
| `tts/out/` | MP3 gerados por ciclo |
| `logs/timeline.log` | Log raw de todos os eventos |

---

## LOOP DOMINÓ (ciclo 3-6-9-7)

```
1. SCAN    → knot_parser.py lê quicknote.md
2. NARRATE → edge-tts fala o arquétipo ativo
3. LOG     → registra em timeline.log + timeline.md
4. SLEEP   → aguarda CYCLE_SECONDS
5. ♾ REPEAT
```

---

## EXECUTAR

```bash
# Ciclo de 2 minutos
CYCLE_SECONDS=120 IDS="ATLAS SERENA AION" bash hub/roda_viva_domino.sh

# Background (nohup)
nohup bash hub/roda_viva_domino.sh > hub/logs/nohup.log 2>&1 &
```

Navegação: [↑ Raiz](../README.md) · [→ SCRIPTS](../scripts/README.md)
