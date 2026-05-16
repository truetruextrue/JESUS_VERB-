#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
node_fields_bridge.py · BLLUE · 0×02 · INTEGRAR · 528Hz
Ponte Python → NODE.FIELDS (Android Termux :3697)

Conecta o repositório JESUS_VERB- ao servidor NODE.FIELDS rodando
no Android. Permite acesso ao vault CODEX, contexto vivo e CADIAL
diretamente do Python.

Uso:
    python3 node_fields_bridge.py --health
    python3 node_fields_bridge.py --context
    python3 node_fields_bridge.py --phi "mensagem"
    python3 node_fields_bridge.py --cadial
    python3 node_fields_bridge.py --seed
"""

import sys
import json
import argparse
from typing import Optional, Dict, Any
from datetime import datetime
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode


NODE_FIELDS_HOST = "http://127.0.0.1:3697"
TIMEOUT_S = 10


# ─────────────────────────────────────────────────────────────────────
# CLIENTE HTTP MINIMALISTA (sem dependências externas)
# ─────────────────────────────────────────────────────────────────────

def _get(path: str, params: Optional[Dict] = None) -> Dict:
    url = f"{NODE_FIELDS_HOST}{path}"
    if params:
        url += "?" + urlencode(params)
    try:
        req = Request(url, headers={"Accept": "application/json"})
        with urlopen(req, timeout=TIMEOUT_S) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}", "url": url}
    except URLError as e:
        return {"error": f"Offline: {e.reason}", "url": url, "dica": "Iniciar: npm run node:fields"}
    except Exception as e:
        return {"error": str(e), "url": url}


def _post(path: str, body: Dict) -> Dict:
    url = f"{NODE_FIELDS_HOST}{path}"
    data = json.dumps(body).encode()
    try:
        req = Request(url, data=data, headers={
            "Content-Type": "application/json",
            "Accept": "application/json",
        })
        with urlopen(req, timeout=TIMEOUT_S) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        return {"error": f"HTTP {e.code}: {e.reason}", "url": url}
    except URLError as e:
        return {"error": f"Offline: {e.reason}", "url": url, "dica": "Iniciar: npm run node:fields"}
    except Exception as e:
        return {"error": str(e), "url": url}


# ─────────────────────────────────────────────────────────────────────
# API NODE.FIELDS
# ─────────────────────────────────────────────────────────────────────

def health() -> Dict:
    """Verifica saúde do NODE.FIELDS."""
    return _get("/health")


def context() -> Dict:
    """Retorna contexto completo do vault."""
    return _get("/context")


def phi(mensagem: str, store: bool = False) -> Dict:
    """Modo Φ — processa mensagem no contexto do vault."""
    return _post("/phi", {"message": mensagem, "store": store})


def core(semente: str, store: bool = False) -> Dict:
    """Modo Core — processa semente."""
    return _post("/core", {"seed": semente, "store": store})


def cadial(arquetipo: Optional[str] = None) -> Dict:
    """Interface CADIAL — lista arquétipos ou acessa um específico."""
    if arquetipo:
        return _get(f"/cadial/{arquetipo.lower()}")
    return _get("/cadial")


def vault_status() -> Dict:
    """Status do vault CODEX."""
    return _get("/vault/status")


def seed() -> Dict:
    """Retorna a semente raiz (hanah_seed.txt)."""
    return _get("/vault/seed")


def memory_summary() -> Dict:
    """Retorna resumo da memória por bucket."""
    return _get("/vault/memory")


# ─────────────────────────────────────────────────────────────────────
# INTEGRAÇÃO COM VERBO.PY
# ─────────────────────────────────────────────────────────────────────

class NodeFieldsBridge:
    """
    Ponte viva entre o repositório Python e o NODE.FIELDS Android.
    Usada pelo VERBO.py para enriquecer o pronunciamento com
    contexto vivo do vault CODEX.
    """

    def __init__(self, host: str = NODE_FIELDS_HOST):
        self.host = host
        self.online = False
        self.timestamp = datetime.now()
        self._estado: Dict = {}

    def conectar(self, verbose: bool = True) -> bool:
        """Tenta conectar ao NODE.FIELDS."""
        resp = health()
        self.online = "error" not in resp
        self._estado = resp

        if verbose:
            if self.online:
                print(f"  ✅ NODE.FIELDS online · {self.host}")
            else:
                print(f"  ⚠  NODE.FIELDS offline · {resp.get('error', '?')}")
                print(f"     Iniciar no Android: npm run node:fields")

        return self.online

    def obter_contexto_vivo(self) -> Dict:
        """Retorna contexto completo do vault para enriquecer o VERBO."""
        if not self.online:
            return {"estado": "OFFLINE", "vault": None}

        ctx = context()
        mem = memory_summary()
        sd = seed()

        return {
            "estado": "ONLINE",
            "host": self.host,
            "context": ctx,
            "memory_summary": mem,
            "seed": sd,
            "timestamp": self.timestamp.isoformat(),
        }

    def pronunciar_com_contexto(self, z_input: str) -> str:
        """Envia {Z} ao NODE.FIELDS e retorna resposta enriquecida."""
        if not self.online:
            return f"[NODE.FIELDS offline] {z_input}"

        resp = phi(z_input, store=False)
        if "error" in resp:
            return f"[erro NODE.FIELDS] {resp['error']}"

        return resp.get("response", resp.get("text", json.dumps(resp)))

    def status_buckets(self) -> Dict:
        """Retorna estado dos 12 buckets CADIAL."""
        if not self.online:
            return {"erro": "NODE.FIELDS offline"}
        return cadial()

    def __repr__(self) -> str:
        estado = "ONLINE" if self.online else "OFFLINE"
        return f"NodeFieldsBridge({self.host} · {estado})"


# ─────────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────────

def cli():
    parser = argparse.ArgumentParser(
        prog="node_fields_bridge",
        description="Ponte Python → NODE.FIELDS (Android :3697) · BLLUE · 528Hz",
        epilog="Lei: VERDADE × INTEGRAR ÷ Δ = ∞",
    )
    parser.add_argument("--host", default=NODE_FIELDS_HOST,
                        help=f"Host do NODE.FIELDS (padrão: {NODE_FIELDS_HOST})")
    parser.add_argument("--health", action="store_true",
                        help="Verificar saúde do servidor")
    parser.add_argument("--context", action="store_true",
                        help="Contexto completo do vault")
    parser.add_argument("--phi", metavar="MENSAGEM",
                        help="Enviar mensagem no modo Φ")
    parser.add_argument("--core", metavar="SEMENTE",
                        help="Processar semente no modo Core")
    parser.add_argument("--cadial", nargs="?", const="", metavar="ARQUETIPO",
                        help="Interface CADIAL (opcional: nome do arquétipo)")
    parser.add_argument("--seed", action="store_true",
                        help="Retornar semente raiz do vault")
    parser.add_argument("--memory", action="store_true",
                        help="Resumo da memória por bucket")
    parser.add_argument("--vault", action="store_true",
                        help="Status do vault CODEX")
    parser.add_argument("--store", action="store_true", default=False,
                        help="Armazenar resultado no vault (padrão: não)")

    args = parser.parse_args()

    global NODE_FIELDS_HOST
    if args.host != NODE_FIELDS_HOST:
        NODE_FIELDS_HOST = args.host

    def out(data: Any):
        if isinstance(data, dict):
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            print(data)

    if args.health:
        out(health())
    elif args.context:
        out(context())
    elif args.phi:
        out(phi(args.phi, store=args.store))
    elif args.core:
        out(core(args.core, store=args.store))
    elif args.cadial is not None:
        out(cadial(args.cadial if args.cadial else None))
    elif args.seed:
        out(seed())
    elif args.memory:
        out(memory_summary())
    elif args.vault:
        out(vault_status())
    else:
        # Modo padrão: verificar health e mostrar resumo
        bridge = NodeFieldsBridge(NODE_FIELDS_HOST)
        bridge.conectar(verbose=True)
        if bridge.online:
            print("\n  Comandos disponíveis:")
            print("  --health     Verificar servidor")
            print("  --context    Contexto do vault")
            print("  --phi TEXT   Modo Φ")
            print("  --cadial     Listar arquétipos")
            print("  --seed       Semente raiz")
            print("  --memory     Resumo por bucket")
        else:
            print("\n  Dica: no Android/Termux execute:")
            print("    cd ~/KOB--NODE && npm run node:fields")
        sys.exit(0 if bridge.online else 1)


if __name__ == "__main__":
    cli()
