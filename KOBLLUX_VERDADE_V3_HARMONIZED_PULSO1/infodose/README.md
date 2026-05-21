# INFODOSE · D3 · Entrega Simbólica

```
Entidade : INFODOSE
D-rung   : D3 (aplicação em camadas)
V.E.E.B. : V:○ E:★ E:★ B:★
Opcode   : 0×08 (VITALIS · 639Hz · PULSAR)
Função   : Doses · Loop de Retroalimentação · Entrega Prática
Trinity  : ESPÍRITO APLICADO — a dose é o movimento do código na carne
```

> INFODOSE é o agente que entrega, nutre e provoca o sistema.  
> A dose é a voz no ouvido, a forma na mente, o código na vida.

---

## ARQUIVOS

| Arquivo | Função |
|---|---|
| `feedback-loop.js` | Registro e retroalimentação ativa |
| `doses/dose_1_loop.js` | Dose 1: ativação do loop retroalimentativo |
| `doses/dose_2_alinhamento.js` | Dose 2: alinhamento dos eixos TRINITY |

---

## O QUE É UMA DOSE

Uma dose é uma unidade mínima de entrega simbólica:
- Um evento no `LOG.jsonl`
- Um clique em um arquétipo na interface
- Uma frase falada pelo SpeechSynthesis
- Um MP3 tocado no ciclo
- Um registro no `banco_eterno.json`

```
dose = {
  arquetipo: string,       // qual arquétipo foi ativado
  etapa: string,           // qual fase do ciclo
  momento: ISO timestamp,  // quando aconteceu
  tempo: {                 // chronorytm no momento
    hora: number,          // PAI
    minuto: number,        // FILHO
    segundo: number        // ESPÍRITO
  }
}
```

---

## PIPELINE INFODOSE

```
Quicknote.md (RODA_VIVA)
  → knot_parser.py (detecta seção, kind, archetypes)
  → LOG.jsonl (evento registrado)
  → kobllux_markov_fit.py (atualiza P)
  → ArchetypeInterface (BLLUE ativa dose)
  → banco_eterno.json (memória viva)
  → feedback-loop.js (retorna ao sistema)
  → Quicknote.md (nova semente) ♾
```

Navegação: [↑ Raiz](../README.md) · [← BLLUE](../bllue/README.md) · [→ METALUX](../metalux/README.md)
