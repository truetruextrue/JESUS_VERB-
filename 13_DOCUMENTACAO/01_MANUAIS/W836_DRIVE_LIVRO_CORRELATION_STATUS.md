# W836 × Google Drive × Livro da Vida — status de correlação

Tentei abrir a pasta do Google Drive fornecida; o acesso falhou neste ambiente (`audit rejected`). Portanto, não afirmei leitura do Drive. O que faço agora é travar a correlação local:

1. `W836_504_MANIFEST_CANONICAL.csv` — manifest canônico 504 páginas com SAP, fólio, zona, banda do Livro da Vida e URLs.
2. `verify_w836_download_livro.py` — verificador que cruza `manifest_hashes.csv` do download com o manifest e separa dado de `Livro da Vida`.
3. Regra de correlação: **número/tabela = índice de navegação**, não prova textual; promoção exige hash + imagem + OCR + normalização.

Sequência:
```bash
python download_w836_504.py --quality sap --start 1 --end 504 --out ./W836_download
python verify_w836_download_livro.py --csv ./W836_download/manifest_hashes.csv --out ./W836_verify_livro --files-dir ./W836_download
```

Assinatura: VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134 → ∆9
