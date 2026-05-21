# sons_ciclo/ · Áudios por Fase do Ciclo Trinitário

Coloque aqui os arquivos MP3 correspondentes às 5 fases do ciclo:

| Arquivo | Fase | Sugestão de som |
|---|---|---|
| `memoria.mp3` | 🧠 Memória | Água suave, eco de memória |
| `inteligencia.mp3` | 🔵 Inteligência | Som elétrico/sintético de decisão |
| `tempo.mp3` | 🕐 Tempo | Relógio, eco cósmico |
| `acao.mp3` | 🛠️ Ação | Metal, clique ritual |
| `integracao.mp3` | ♻️ Integração | Digitalização, absorção |

## Geração via edge-tts (Termux)

```bash
pip install edge-tts

# Alternativa: gerar silêncio como placeholder
python3 -c "
import wave, struct, os
os.makedirs('sons_ciclo', exist_ok=True)
fases = ['memoria','inteligencia','tempo','acao','integracao']
for f in fases:
    with wave.open(f'sons_ciclo/{f}.mp3', 'w') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(44100)
        w.writeframes(struct.pack('<h', 0) * 44100)
    print(f'✓ {f}.mp3 criado')
"
```

## Também necessário: sons por arquétipo

Em `../public/sounds/` ou `/sounds/`:

```
atlas.mp3 · nova.mp3 · vitalis.mp3 · pulse.mp3 · artemis.mp3
serena.mp3 · kaos.mp3 · genus.mp3 · lumine.mp3 · solus.mp3
rhea.mp3 · aion.mp3
```

Navegação: [↑ BLLUE](../README.md) · [↑↑ Raiz](../../README.md)
