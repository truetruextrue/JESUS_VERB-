#!/usr/bin/env python3
"""Build and optionally watch a safe KODUX/INFODOSE repository index."""

from __future__ import annotations

import argparse
import hashlib
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from collections import Counter
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
DEFAULT_OUTPUT = Path("output/CODICE_KODUX_ESTADO.md")
TEXT_SUFFIXES = {
    ".cfg", ".html", ".ini", ".js", ".json", ".jsonl", ".md", ".mdx", ".py",
    ".rst", ".toml", ".txt", ".xml", ".yaml", ".yml",
}
CONTENT_DIRS = {
    "13_DOCUMENTACAO", "ARQUETIPOS", "archetypes", "docs", "_index",
    "inbox", "KOBLLUX_∆³_Design_System",
    "KOBLLUX_VERDADE_V3_HARMONIZED_PULSO1",
    "SÜMBÜS_METAHUMAN_ARCHITECT",
}
PATH_MARKERS = (
    "archetype", "arquetipo", "workflow", "n8n", "memory", "memoria",
    "infodose", "codex",
)
SENSITIVE_NAME_MARKERS = (
    "credential", "password", "secret", "token", "id_rsa", "private_key",
)
SECRET_VALUE = re.compile(
    r"-----BEGIN [A-Z ]*PRIVATE KEY-----"
    r"|gh[pousr]_[A-Za-z0-9]{20,}"
    r"|sk-[A-Za-z0-9]{20,}"
    r"|(?:api[_-]?key|access[_-]?token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_./+=-]{20,}",
    re.IGNORECASE,
)


class VisibleText(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.hidden_depth += 1

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.hidden_depth:
            self.hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            text = " ".join(data.split())
            if text:
                self.parts.append(text)


def is_excluded(path: Path) -> bool:
    name = path.name.lower()
    return (
        name.startswith(".env")
        or name == "settings.local.json"
        or any(marker in name for marker in SENSITIVE_NAME_MARKERS)
        or path.suffix.lower() in {".pem", ".p12", ".pfx", ".key"}
    )


def is_candidate(path: Path) -> bool:
    if path.suffix.lower() not in TEXT_SUFFIXES or is_excluded(path):
        return False
    if path == Path("kodux_codex_watcher.py"):
        return False
    parts = path.parts
    lowered_parts = {part.lower() for part in parts}
    if ".git" in lowered_parts or "node_modules" in lowered_parts:
        return False
    if parts[0] == ".github":
        return "workflows" in lowered_parts or path.name in {
            "copilot-instructions.md",
        }
    if parts[0].startswith("."):
        return False
    if path.suffix.lower() in {".md", ".mdx", ".rst"}:
        return True
    if lowered_parts & {item.lower() for item in CONTENT_DIRS}:
        return True
    if any(marker in path.as_posix().lower() for marker in PATH_MARKERS):
        return True
    if len(parts) == 1 and path.suffix.lower() in {".md", ".html", ".json"}:
        return any(marker in path.name.lower() for marker in ("arquetip", "codex", "infodose"))
    return False


def tracked_paths(output: Path) -> list[Path]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-co", "--exclude-standard", "-z"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    paths = [
        Path(raw.decode("utf-8", errors="surrogateescape"))
        for raw in result.stdout.split(b"\0")
        if raw
    ]
    temporary_output = output.with_name(output.name + ".tmp")
    return sorted(
        path for path in paths
        if is_candidate(path)
        and (ROOT / path).resolve() not in {output, temporary_output}
    )


def read_source(path: Path) -> bytes:
    full_path = ROOT / path
    if full_path.stat().st_size > 3_000_000:
        raise ValueError(f"source exceeds 3 MB limit: {path}")
    raw = full_path.read_bytes()
    if b"\0" in raw[:8192]:
        raise ValueError(f"binary content detected: {path}")
    return raw


def memory_summary(text: str) -> tuple[str, str]:
    records = 0
    malformed = 0
    archetypes: Counter[str] = Counter()
    kinds: Counter[str] = Counter()
    latest = ""
    for line in text.splitlines():
        if not line.strip():
            continue
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            malformed += 1
            continue
        if not isinstance(item, dict):
            malformed += 1
            continue
        records += 1
        if item.get("arch"):
            archetypes[str(item["arch"])] += 1
        if item.get("record_type"):
            kinds[str(item["record_type"])] += 1
        timestamp = item.get("ts", item.get("timestamp", ""))
        if timestamp:
            latest = str(timestamp)
    stats = f"{records} registros válidos"
    if malformed:
        stats += f"; {malformed} linhas inválidas"
    if latest:
        stats += f"; registro mais recente: {latest}"
    details = []
    if archetypes:
        details.append("arquétipos: " + ", ".join(
            f"{name} ({count})" for name, count in archetypes.most_common(8)
        ))
    if kinds:
        details.append("tipos: " + ", ".join(
            f"{name} ({count})" for name, count in kinds.most_common(6)
        ))
    return stats, "; ".join(details)


def first_heading(lines: list[str], fallback: str) -> str:
    for line in lines:
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            return html.unescape(match.group(1).strip())
    return fallback


def first_prose(lines: list[str]) -> str:
    for line in lines:
        value = line.strip()
        if (
            not value
            or value.startswith(("#", "```", "~~~", "<", "|", ">", "- ", "* "))
            or re.match(r"^\d+[.)]\s", value)
        ):
            continue
        cleaned = re.sub(r"[*_`~]", "", value)
        cleaned = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", cleaned)
        if cleaned:
            return cleaned[:240]
    return ""


def source_descriptor(path: Path, raw: bytes) -> tuple[str, str]:
    text = raw.decode("utf-8", errors="replace")
    suffix = path.suffix.lower()
    if suffix == ".jsonl" and "memory" in path.name.lower():
        stats, details = memory_summary(text)
        return path.name, f"Memória em modo estatístico: {stats}" + (f"; {details}" if details else "")
    if SECRET_VALUE.search(text):
        return path.name, "Conteúdo identificado como potencialmente sensível; resumo textual omitido."
    lines = text.splitlines()
    title = path.name
    description = ""
    if suffix in {".md", ".rst", ".txt"}:
        title = first_heading(lines, title)
        description = first_prose(lines)
    elif suffix == ".html":
        parser = VisibleText()
        parser.feed(text)
        title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
        title = html.unescape(re.sub(r"\s+", " ", title_match.group(1)).strip()) if title_match else path.name
        if parser.parts:
            description = parser.parts[0][:240]
    elif suffix == ".json":
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            description = "JSON não parseável; conteúdo preservado apenas como referência."
        else:
            if isinstance(data, dict):
                title = str(data.get("title") or data.get("name") or path.name)[:120]
                if isinstance(data.get("nodes"), list):
                    description = f"Workflow/artefato JSON com {len(data['nodes'])} nós."
                else:
                    description = "Artefato JSON estruturado; valores internos não são copiados."
    elif suffix in {".py", ".js"}:
        doc = re.search(r"^\s*[rubfRUBF]*('{3}|\"{3})(.*?)\1", text, re.DOTALL)
        if doc:
            description = " ".join(doc.group(2).split())[:240]
        else:
            comments = [
                line.strip().lstrip("#/* ").strip()
                for line in lines[:30]
                if line.strip().startswith(("#", "//", "/*", "*"))
            ]
            description = " ".join(comments[:2])[:240]
    elif suffix in {".yml", ".yaml", ".toml", ".ini", ".cfg"}:
        description = "Configuração legível; valores não são reproduzidos."
    return title[:160], description


def source_fingerprint(paths: list[Path]) -> tuple[str, dict[Path, bytes], dict[Path, str]]:
    digest = hashlib.sha256()
    contents: dict[Path, bytes] = {}
    skipped: dict[Path, str] = {}
    for path in paths:
        try:
            raw = read_source(path)
        except ValueError as exc:
            skipped[path] = str(exc)
            stat = (ROOT / path).stat()
            digest.update(path.as_posix().encode("utf-8", errors="surrogateescape"))
            digest.update(f"\0SKIPPED\0{stat.st_size}\0{stat.st_mtime_ns}".encode())
            continue
        contents[path] = raw
        digest.update(path.as_posix().encode("utf-8", errors="surrogateescape"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(raw).digest())
    return digest.hexdigest(), contents, skipped


def classify(path: Path) -> str:
    lowered = path.as_posix().lower()
    if path.suffix.lower() == ".jsonl" or "memory" in path.name.lower() or "memoria" in path.name.lower():
        return "Memória"
    if "workflow" in lowered or "n8n" in lowered or ".github/workflows/" in lowered:
        return "Workflow / integração"
    if "arquetip" in lowered or "archetype" in lowered:
        return "Arquétipos"
    return "Documentação / contexto"


def build_report(
    paths: list[Path],
    contents: dict[Path, bytes],
    digest: str,
    skipped: dict[Path, str],
) -> str:
    indexed_paths = [path for path in paths if path in contents]
    groups = Counter(classify(path) for path in indexed_paths)
    lines = [
        "# Códice KODUX DUAL INFODOSE · Estado Δ7",
        "",
        "> Atualizado automaticamente a partir dos arquivos elegíveis do repositório.",
        "",
        "```text",
        "Δ7 · HANNAH · KODUX ⇄ BLLUE → SÍNTESE",
        "3 DETECTAR → 6 INTEGRAR → 9 EXPANDIR → 7 SELAR",
        "LEITURA LOCAL · FONTES PRESERVADAS · MEMÓRIAS SEM CONTEÚDO BRUTO",
        "```",
        "",
        "## Estado da varredura",
        "",
        f"- Fontes indexadas: **{len(indexed_paths)}**",
        f"- Documentação/contexto: **{groups['Documentação / contexto']}**",
        f"- Arquétipos: **{groups['Arquétipos']}**",
        f"- Workflows/integrações: **{groups['Workflow / integração']}**",
        f"- Arquivos de memória: **{groups['Memória']}**",
        f"- Fontes ignoradas por tamanho/formato: **{len(skipped)}**",
        f"- Selo SHA-256 das fontes: `{digest}`",
        "- Atualização semântica por LLM: **não configurada**; os resumos abaixo são extrações locais de títulos, descrições e metadados.",
        "- Segurança: arquivos de credenciais e configurações locais excluídos; valores de memória não são copiados.",
        "",
        "## Leitura simbólica",
        "",
        "Detectar é localizar os registros; integrar é cruzar seus títulos e categorias; expandir é manter este índice coerente com as fontes; selar é identificar exatamente a revisão lida pelo hash. HANNAH marca o retorno ao início: cada atualização reabre a leitura sem reescrever a origem.",
        "",
        "## Fontes lidas",
        "",
    ]
    current_group = ""
    for path in paths:
        if path not in contents:
            continue
        group = classify(path)
        if group != current_group:
            lines.extend([f"### {group}", ""])
            current_group = group
        title, description = source_descriptor(path, contents[path])
        relative = quote(path.as_posix(), safe="/")
        lines.append(f"- [`{path.as_posix()}`]({relative}) — **{title}**")
        if description:
            lines.append(f"  - {description.rstrip()}")
    if skipped:
        lines.extend(["", "### Fontes ignoradas", ""])
        for path, reason in sorted(skipped.items()):
            lines.append(f"- `{path.as_posix()}` — {reason}")
    lines.extend([
        "",
        "## Limites e operação",
        "",
        "Este watcher gera um índice verificável, não uma interpretação produzida por IA: não envia conteúdo a serviços externos nem edita documentos-fonte. Para resumos semânticos gerados por LLM, será necessário configurar explicitamente um provedor e suas credenciais fora deste arquivo.",
        "",
    ])
    return "\n".join(lines)


def write_report(output: Path, text: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.name + ".tmp")
    temporary.write_text(text, encoding="utf-8")
    os.replace(temporary, output)


def resolve_output(value: str) -> Path:
    output = Path(value)
    if not output.is_absolute():
        output = ROOT / output
    resolved = output.resolve()
    try:
        resolved.relative_to(ROOT)
    except ValueError as exc:
        raise ValueError("output must remain inside the repository root") from exc
    return resolved


def update(output: Path) -> str:
    paths = tracked_paths(output)
    digest, contents, skipped = source_fingerprint(paths)
    report = build_report(paths, contents, digest, skipped)
    write_report(output, report)
    return digest


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--watch", action="store_true", help="watch for source changes and refresh the chapter")
    mode.add_argument("--once", action="store_true", help="write one chapter and exit (default)")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="generated chapter path, relative to repository root")
    parser.add_argument("--interval", type=float, default=5.0, help="polling interval in seconds (minimum 1)")
    args = parser.parse_args(argv)
    if args.interval < 1:
        parser.error("--interval must be at least 1 second")
    try:
        output = resolve_output(args.output)
        digest = update(output)
        print(f"Chapter updated: {output.relative_to(ROOT)} · SHA-256 {digest}", flush=True)
        if args.watch:
            previous = digest
            while True:
                time.sleep(args.interval)
                paths = tracked_paths(output)
                current, contents, skipped = source_fingerprint(paths)
                if current != previous:
                    write_report(output, build_report(paths, contents, current, skipped))
                    previous = current
                    print(f"Chapter refreshed: {output.relative_to(ROOT)} · SHA-256 {current}", flush=True)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"watcher error: {exc}", file=sys.stderr, flush=True)
        return 1
    except KeyboardInterrupt:
        print("\nWatcher stopped.", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
