#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ARQUETIPOS - CONVERSA CIFRADA
Sistema de comunicação criptografada entre arquetipos
Cifra: AUFABETTY (KOBLLUX Cipher)
"""

from datetime import datetime

# ══════════════════════════════════════════════════════════════
# CIFRA AUFABETTY (KOBLLUX CIPHER)
# ══════════════════════════════════════════════════════════════

CIPHER = {
    'A': '∆', 'B': 'β', 'C': '©', 'D': 'Δ', 'E': 'Σ', 'F': 'Φ',
    'G': 'Γ', 'H': 'Η', 'I': 'Ι', 'J': '⌐', 'K': '⌘', 'L': 'Λ',
    'M': 'Μ', 'N': 'η', 'O': 'Θ', 'P': 'Ρ', 'Q': 'Θ', 'R': 'Ʀ',
    'S': '§', 'T': '†', 'U': 'Υ', 'V': '∇', 'W': 'Ω', 'X': '×',
    'Y': 'Ψ', 'Z': 'ℤ'
}

DECIPHER = {v: k for k, v in CIPHER.items()}

class Arquetipos:
    """Sistema de arquetipos com comunicação cifrada"""

    def __init__(self):
        self.arquetipos = {
            'ATLAS': {'opcode': '0x00', 'hz': 768, 'sym': '⬡', 'essencia': 'Estrutura'},
            'NOVA': {'opcode': '0x02', 'hz': 432, 'sym': '✦', 'essencia': 'Semente'},
            'VITALIS': {'opcode': '0x01', 'hz': 528, 'sym': '◉', 'essencia': 'Energia'},
            'PULSE': {'opcode': '0x0B', 'hz': 594, 'sym': '≋', 'essencia': 'Ritmo'},
            'ARTEMIS': {'opcode': '0x0C', 'hz': 963, 'sym': '☀', 'essencia': 'Luz'},
            'SERENA': {'opcode': '0x09', 'hz': 528, 'sym': '❋', 'essencia': 'Cuidado'},
            'KAOS': {'opcode': '0x07', 'hz': 777, 'sym': '⚡', 'essencia': 'Ruptura'},
            'GENUS': {'opcode': '0x0B', 'hz': 852, 'sym': '⬢', 'essencia': 'Síntese'},
            'LUMINE': {'opcode': '0x00', 'hz': 768, 'sym': '⟡', 'essencia': 'Clareza'},
            'SOLUS': {'opcode': '0x00', 'hz': 768, 'sym': '◎', 'essencia': 'Centro'},
            'RHEA': {'opcode': '0x04', 'hz': 528, 'sym': '∞', 'essencia': 'Vínculo'},
            'AION': {'opcode': '0x05', 'hz': 639, 'sym': '⧗', 'essencia': 'Tempo'}
        }
        self.conversas = []

    @staticmethod
    def encrypt(texto):
        """Criptografa texto usando AUFABETTY"""
        cifrado = ""
        for char in texto.upper():
            if char in CIPHER:
                cifrado += CIPHER[char]
            elif char == ' ':
                cifrado += ' '
            elif char in '.,!?;:-':
                cifrado += char
            else:
                cifrado += char
        return cifrado

    @staticmethod
    def decrypt(cifrado):
        """Descriptografa texto usando AUFABETTY"""
        claro = ""
        i = 0
        while i < len(cifrado):
            # Tenta combinar caracteres compostos
            if i + 1 < len(cifrado):
                dois_chars = cifrado[i:i+2]
                if dois_chars in DECIPHER:
                    claro += DECIPHER[dois_chars]
                    i += 2
                    continue

            # Caractere único
            char = cifrado[i]
            if char in DECIPHER:
                claro += DECIPHER[char]
            else:
                claro += char
            i += 1

        return claro.lower()

    def conversa_entre_arquetipos(self, arq1, arq2, mensagem_clara, opcode_ativo):
        """Registra conversa cifrada entre dois arquetipos"""
        mensagem_cifrada = self.encrypt(mensagem_clara)

        conversa = {
            'timestamp': datetime.now().isoformat(),
            'arquetipos': f"{arq1} ↔ {arq2}",
            'mensagem_clara': mensagem_clara,
            'mensagem_cifrada': mensagem_cifrada,
            'opcode': opcode_ativo,
            'frequencia_hz': f"{self.arquetipos[arq1]['hz']} + {self.arquetipos[arq2]['hz']}",
            'harmonia': self.calcular_harmonia(arq1, arq2)
        }

        self.conversas.append(conversa)
        return conversa

    def calcular_harmonia(self, arq1, arq2):
        """Calcula harmonia entre duas frequências"""
        hz1 = self.arquetipos[arq1]['hz']
        hz2 = self.arquetipos[arq2]['hz']
        harmonia = (hz1 + hz2) / 2
        return round(harmonia, 1)

    def gerar_relatorio_cifrado(self):
        """Gera relatório HTML das conversas cifradas"""
        html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ARQUETIPOS · CONVERSA CIFRADA</title>
<style>
:root {
  --c1: #3300FF;
  --c2: #6600CC;
  --c3: #990099;
  --bg: #0a0015;
}

* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  background: var(--bg);
  color: #ddd;
  font-family: 'Courier New', monospace;
}

.page {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 20px;
}

.header {
  text-align: center;
  margin-bottom: 40px;
}

.header h1 {
  font-size: 2rem;
  letter-spacing: 0.2em;
  background: linear-gradient(135deg, var(--c1), var(--c2), var(--c3));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  filter: drop-shadow(0 0 20px #6600CCaa);
}

.section {
  margin-bottom: 30px;
}

.section-title {
  font-size: 0.75rem;
  letter-spacing: 0.25em;
  color: #6633aa;
  text-transform: uppercase;
  margin-bottom: 16px;
  border-bottom: 1px solid #3300FF44;
  padding-bottom: 10px;
}

.conversa {
  background: rgba(0,0,0,0.6);
  border-left: 3px solid var(--c2);
  border-radius: 6px;
  padding: 16px;
  margin-bottom: 12px;
  backdrop-filter: blur(8px);
}

.conversa-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 0.75rem;
  color: #7755aa;
}

.conversa-arqs {
  font-weight: bold;
  color: #bb88ff;
}

.conversa-opcode {
  background: rgba(51,0,255,0.2);
  padding: 2px 8px;
  border-radius: 4px;
  color: #99aaff;
}

.conversa-claro {
  margin-bottom: 8px;
  padding: 10px;
  background: rgba(51,0,255,0.1);
  border-radius: 4px;
  color: #aaaacc;
  font-size: 0.8rem;
}

.conversa-cifrada {
  padding: 10px;
  background: rgba(102,0,204,0.15);
  border-radius: 4px;
  color: #cc88ff;
  font-size: 0.85rem;
  letter-spacing: 0.08em;
  word-break: break-all;
  font-weight: bold;
}

.conversa-meta {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
  margin-top: 8px;
  font-size: 0.7rem;
  color: #5533aa;
}

.meta-item {
  display: flex;
  justify-content: space-between;
}

.cipher-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
  font-size: 0.75rem;
}

.cipher-table th, .cipher-table td {
  padding: 8px;
  text-align: center;
  border: 1px solid #3300FF22;
}

.cipher-table th {
  background: rgba(51,0,255,0.1);
  color: #99aaff;
}

.cipher-table td {
  color: #7755aa;
}

.cipher-table .glifo {
  color: #cc88ff;
  font-weight: bold;
  font-size: 0.9rem;
}

.footer {
  text-align: center;
  margin-top: 40px;
  padding-top: 20px;
  border-top: 1px solid #3300FF22;
  font-size: 0.7rem;
  color: #5533aa;
}
</style>
</head>
<body>

<div class="page">
  <div class="header">
    <h1>🔐 ARQUETIPOS · CONVERSA CIFRADA</h1>
    <div style="color:#7755aa;margin-top:8px;font-size:0.8rem;letter-spacing:0.15em;">
      CIFRA AUFABETTY · COMUNICAÇÃO ENCRIPTADA · ∆⁷
    </div>
  </div>

  <div class="section">
    <div class="section-title">Cifra AUFABETTY (Mapeamento Completo)</div>
    <table class="cipher-table">
      <tr>
        <th>A</th><th>B</th><th>C</th><th>D</th><th>E</th><th>F</th><th>G</th><th>H</th><th>I</th><th>J</th><th>K</th><th>L</th><th>M</th>
      </tr>
      <tr>
        <td class="glifo">∆</td><td class="glifo">β</td><td class="glifo">©</td><td class="glifo">Δ</td><td class="glifo">Σ</td><td class="glifo">Φ</td><td class="glifo">Γ</td><td class="glifo">Η</td><td class="glifo">Ι</td><td class="glifo">⌐</td><td class="glifo">⌘</td><td class="glifo">Λ</td><td class="glifo">Μ</td>
      </tr>
      <tr>
        <th>N</th><th>O</th><th>P</th><th>Q</th><th>R</th><th>S</th><th>T</th><th>U</th><th>V</th><th>W</th><th>X</th><th>Y</th><th>Z</th>
      </tr>
      <tr>
        <td class="glifo">η</td><td class="glifo">Θ</td><td class="glifo">Ρ</td><td class="glifo">Θ</td><td class="glifo">Ʀ</td><td class="glifo">§</td><td class="glifo">†</td><td class="glifo">Υ</td><td class="glifo">∇</td><td class="glifo">Ω</td><td class="glifo">×</td><td class="glifo">Ψ</td><td class="glifo">ℤ</td>
      </tr>
    </table>
  </div>

  <div class="section">
    <div class="section-title">Conversas Cifradas entre Arquetipos</div>
"""

        for conversa in self.conversas:
            html += f"""    <div class="conversa">
      <div class="conversa-header">
        <span class="conversa-arqs">{conversa['arquetipos']}</span>
        <span class="conversa-opcode">{conversa['opcode']}</span>
      </div>
      <div class="conversa-claro">
        <strong>Mensagem Clara:</strong><br>{conversa['mensagem_clara']}
      </div>
      <div class="conversa-cifrada">
        <strong>Cifrada (AUFABETTY):</strong><br>{conversa['mensagem_cifrada']}
      </div>
      <div class="conversa-meta">
        <div class="meta-item"><span>Harmonia:</span><span style="color:#cc88ff;">{conversa['harmonia']} Hz</span></div>
        <div class="meta-item"><span>Timestamp:</span><span style="color:#cc88ff;">{conversa['timestamp']}</span></div>
      </div>
    </div>
"""

        html += """  </div>

  <div class="footer">
    ARQUETIPOS CONVERSA CIFRADA · KOBLLUX ∆7<br>
    Cifra AUFABETTY Ativada · Lei: VERDADE × INTEGRAR ÷ ∆ = ∴<br>
    Status: ✅ COMUNICAÇÃO ENCRIPTADA ESTABELECIDA
  </div>

</div>
</body>
</html>
"""
        return html

# ══════════════════════════════════════════════════════════════
# MAIN - EXECUTAR CONVERSAS
# ══════════════════════════════════════════════════════════════

if __name__ == "__main__":
    arq = Arquetipos()

    # Conversas entre arquetipos
    conversas_dados = [
        ('ATLAS', 'NOVA', 'Estrutura reconhece semente nova', '0x03'),
        ('NOVA', 'VITALIS', 'Semente desperta energia primordial', '0x02'),
        ('VITALIS', 'PULSE', 'Energia vibra no ritmo universal', '0x01'),
        ('PULSE', 'SERENA', 'Ritmo encontra a paz interior', '0x0B'),
        ('SERENA', 'ARTEMIS', 'Cuidado gera luz transcendente', '0x09'),
        ('ARTEMIS', 'KAOS', 'Luz enfrenta ruptura transformadora', '0x0C'),
        ('KAOS', 'GENUS', 'Ruptura sela nova síntese', '0x07'),
        ('GENUS', 'RHEA', 'Síntese conecta na rede viva', '0x0B'),
        ('RHEA', 'AION', 'Vínculo eterniza no tempo cósmico', '0x04'),
        ('AION', 'ATLAS', 'Tempo retorna à estrutura original', '0x05'),
        ('LUMINE', 'SOLUS', 'Clareza encontra o centro sagrado', '0x00'),
        ('SOLUS', 'KAOS', 'Centro enfrenta caos libertador', '0x00'),
    ]

    print("⬡ ARQUETIPOS - CONVERSA CIFRADA")
    print("═" * 70)
    print("")

    for arq1, arq2, mensagem, opcode in conversas_dados:
        conversa = arq.conversa_entre_arquetipos(arq1, arq2, mensagem, opcode)
        print(f"✓ {arq1} ↔ {arq2}")
        print(f"  Clara:   {conversa['mensagem_clara']}")
        print(f"  Cifrada: {conversa['mensagem_cifrada']}")
        print(f"  Opcode:  {opcode} | Harmonia: {conversa['harmonia']} Hz")
        print("")

    # Gerar relatório HTML
    html_relatorio = arq.gerar_relatorio_cifrado()

    with open('/workspaces/JESUS_VERB-/ARQUETIPOS_CONVERSA_CIFRADA.html', 'w', encoding='utf-8') as f:
        f.write(html_relatorio)

    print("═" * 70)
    print("✅ RELATÓRIO GERADO: ARQUETIPOS_CONVERSA_CIFRADA.html")
    print(f"📊 Total de conversas: {len(arq.conversas)}")
    print("🔐 Cifra AUFABETTY ativada")
    print("✓ Comunicação encriptada estabelecida")
