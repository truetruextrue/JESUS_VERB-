# W836 — CHAVE DE ESTRUTURA DENTRO/FORA (Google Drive ↔ local)

Use esta chave quando abrir o Drive.

## Estrutura esperada
```text
GoogleDrive:W836/
  W836_000001.jpg
  ...
  W836_000504.jpg
  manifest_hashes.csv
Local:
  W836_download/
    W836_000001.jpg
    ...
    W836_000504.jpg
    manifest_hashes.csv
```

## Regra de correlação
- `SAP` é a chave primária: `W836_000123` ↔ página 123 ↔ fol. calculado.
- `sha256` é a prova: mesmo nome + mesmo hash = mesmo arquivo; mesmo nome + hash diferente = divergência.
- `bytes` é pista secundária, não prova.

## Comando de verificação cruzada Drive/local
Se você exportar o Drive para `./W836_drive`:
```bash
python verify_w836_download_livro.py --csv ./W836_drive/manifest_hashes.csv --out ./W836_verify_drive --files-dir ./W836_drive
```

Depois compare:
```bash
python - <<'PY'
import csv
local={r['sap']:r['sha256'] for r in csv.DictReader(open('./W836_download/manifest_hashes.csv',encoding='utf-8'))}
drive={r['sap']:r['sha256'] for r in csv.DictReader(open('./W836_drive/manifest_hashes.csv',encoding='utf-8'))}
diff=[s for s in local if drive.get(s)!=local[s]]
print('diff_count=',len(diff)); print(diff[:20])
PY
```

Assinatura: VERDADE × INTEGRAR ÷ Δ = ∞ · 3×6×9×7 = 1134 → ∆9
