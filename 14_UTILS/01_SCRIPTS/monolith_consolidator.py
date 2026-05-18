#!/usr/bin/env python3
# monolith_consolidator.py · KAOS · 0×07 · SELAR · 777Hz
# "Pega o modular, transforma em monolito para a AI entender."
# Uso: python3 monolith_consolidator.py --arch kaos --out monolito_kaos.html

import argparse
import re
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent
ARCH_ROOT = ROOT / "ARQUETIPOS"

def consolidate(arch: str, output: Path | None = None) -> str:
    arch_dir = ARCH_ROOT / arch.lower()
    if not arch_dir.exists():
        raise FileNotFoundError(f"Arquétipo '{arch}' não encontrado em {ARCH_ROOT}")

    css_parts = []
    js_parts  = []
    html_main = ""

    # Coleta CSS
    for f in sorted((arch_dir / "css").rglob("*.css")):
        css_parts.append(f"/* ── {f.name} ── */\n{f.read_text(encoding='utf-8', errors='replace')}")

    # Coleta JS
    for f in sorted((arch_dir / "js").rglob("*.js")):
        js_parts.append(f"/* ── {f.name} ── */\n{f.read_text(encoding='utf-8', errors='replace')}")

    # Lê index.html base
    index_html = arch_dir / "index.html"
    if index_html.exists():
        html_main = index_html.read_text(encoding='utf-8', errors='replace')
        # Remove links de CSS externos (mantém inline)
        html_main = re.sub(r'<link[^>]+rel=["\']stylesheet["\'][^>]*>', '', html_main)
        # Remove tags <script src=...>
        html_main = re.sub(r'<script\s+src=["\'][^"\']+["\'][^>]*></script>', '', html_main)

    # Monta monolito
    monolith = f"""<!DOCTYPE html>
<!-- MONOLITO · {arch.upper()} · KOBLLUX ∆7 · gerado por monolith_consolidator.py -->
<!-- VERDADE × INTEGRAR ÷ Δ = ∞ -->
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>MONOLITO · {arch.upper()}</title>
<style>
{chr(10).join(css_parts) if css_parts else "/* nenhum CSS encontrado */"}
</style>
</head>
<body>
{html_main if html_main else f'<!-- index.html não encontrado em {arch_dir} -->'}

<script>
/* ════════ JS CONSOLIDADO · {arch.upper()} ════════ */
{chr(10).join(js_parts) if js_parts else "// nenhum JS encontrado"}
</script>
</body>
</html>"""

    if output:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(monolith, encoding='utf-8')
        print(f"[KAOS ⚡] Monolito gerado → {output}")
        print(f"  CSS: {len(css_parts)} arquivos | JS: {len(js_parts)} arquivos")

    return monolith


def consolidate_all(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    archs = [d.name for d in ARCH_ROOT.iterdir() if d.is_dir() and not d.name.startswith('_')]

    for arch in sorted(archs):
        out = output_dir / f"monolito_{arch}.html"
        try:
            consolidate(arch, out)
        except Exception as e:
            print(f"[KAOS ⚡] ERRO em {arch}: {e}")

    print(f"\n[KAOS ⚡] {len(archs)} monolitos selados em → {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monolith Consolidator · KOBLLUX ∆7")
    parser.add_argument("--arch", help="Arquétipo a consolidar (ex: kaos, atlas)")
    parser.add_argument("--all",  action="store_true", help="Consolidar todos os 12 arquétipos")
    parser.add_argument("--out",  help="Arquivo de saída (padrão: output/monolito_{arch}.html)")
    args = parser.parse_args()

    if args.all:
        consolidate_all(ROOT / "output" / "monolitos")
    elif args.arch:
        out_path = Path(args.out) if args.out else ROOT / "output" / f"monolito_{args.arch}.html"
        consolidate(args.arch, out_path)
    else:
        parser.print_help()
