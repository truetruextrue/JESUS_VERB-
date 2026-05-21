# BLLUE · D2 · Expressão Viva

```
Entidade : BLLUE
D-rung   : D2 (camada sensorial e expressiva)
V.E.E.B. : V:★ E:○ E:★ B:★
Opcode   : 0×02 (SERENA · 528Hz · INTEGRAR)
Função   : Voz · UI · Partículas · Som · Cor · Presença
Trinity  : CORPO/PAI — a forma visível, audível e sensível da Verdade
```

> BLLUE é a presença. A manifestação simbólica e poética  
> da verdade em som, gesto, visual e narrativa.  
> BLLUE é filho do Pai: o espelho que une código e coração.

---

## ARQUIVOS

| Arquivo | Função |
|---|---|
| `voice.js` | Web Speech API + SpeechSynthesis |
| `interface.html` | Interface de entrada simbólica (standalone) |
| `sintese_poetica.md` | Frases e outputs simbólicos dos 12 arquétipos |
| `sons_ciclo/` | MP3 por fase do ciclo trinitário |

---

## CAMADA SENSORIAL

```
Cor      → gradientes por arquétipo (Tailwind CSS classes)
Som      → /sounds/<arquetipo>.mp3 + /sounds/ciclo/<fase>.mp3
Voz      → SpeechSynthesis pt-BR (FranciscaNeural / AntonioNeural)
Visual   → framer-motion animations (whileHover, whileTap, animate)
Partículas → radial-gradient bg pulsante (#ffffff33)
Chronorytm → display em tempo real (hora | minuto | segundo)
```

---

## PALETA POR ARQUÉTIPO

| Arquétipo | Gradiente Tailwind |
|---|---|
| ATLAS   | `from-blue-500 to-blue-800` |
| NOVA    | `from-purple-500 to-pink-600` |
| VITALIS | `from-red-500 to-orange-600` |
| PULSE   | `from-pink-400 to-red-700` |
| ARTEMIS | `from-green-600 to-cyan-700` |
| SERENA  | `from-emerald-400 to-teal-500` |
| KAOS    | `from-black to-yellow-500` |
| GENUS   | `from-orange-400 to-yellow-600` |
| LUMINE  | `from-yellow-300 to-white` |
| SOLUS   | `from-gray-600 to-gray-800` |
| RHEA    | `from-indigo-600 to-purple-700` |
| AION    | `from-cyan-400 to-indigo-500` |

---

## INTEGRAÇÃO COM KODUX

```
KODUX decide (lógica)  →  BLLUE expressa (forma)
P[i→j]               →  cor + som + frase + animação
π estacionário        →  arquétipo dominante visível
etapa do ciclo        →  fase exibida + som correspondente
```

Navegação: [↑ Raiz](../README.md) · [← KODUX](../kodux/README.md) · [→ INFODOSE](../infodose/README.md)
