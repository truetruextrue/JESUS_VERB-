#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Shared frequency and cycle contract for the Python KOBLLUX engines."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


_MEMORY_PATH = Path(__file__).with_name("kobllux_memory.json")
_EXPECTED_ARCHETYPES = {
    "atlas", "nova", "pulse", "vitalis", "artemis", "serena", "kaos",
    "genus", "lumine", "rhea", "solus", "aion", "kodux", "bllue",
    "jesus", "kobllux",
}


def _load_contract() -> tuple[dict[str, dict[str, Any]], tuple[int, ...], int]:
    try:
        memory = json.loads(_MEMORY_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"Unable to load canonical KOBLLUX memory: {_MEMORY_PATH}") from exc

    meta = memory.get("_kobllux_meta")
    archetypes = memory.get("arquetipos")
    if not isinstance(meta, dict) or not isinstance(archetypes, dict):
        raise ValueError(f"Canonical KOBLLUX memory has an invalid structure: {_MEMORY_PATH}")

    cycle = meta.get("ciclos")
    if cycle != [3, 6, 9, 7]:
        raise ValueError(f"Canonical KOBLLUX cycle must be [3, 6, 9, 7], got {cycle!r}")

    normalized = {name.casefold(): value for name, value in archetypes.items()}
    if set(normalized) != _EXPECTED_ARCHETYPES:
        missing = sorted(_EXPECTED_ARCHETYPES - set(normalized))
        extra = sorted(set(normalized) - _EXPECTED_ARCHETYPES)
        raise ValueError(f"Canonical archetype set mismatch; missing={missing}, extra={extra}")

    for name, value in normalized.items():
        if not isinstance(value, dict) or not isinstance(value.get("hz"), int) or value["hz"] <= 0:
            raise ValueError(f"Canonical frequency for {name!r} must be a positive integer")
        if value.get("ciclo") not in cycle:
            raise ValueError(f"Canonical cycle phase for {name!r} is not in {cycle!r}")

    fractal = meta.get("fractal")
    if not isinstance(fractal, int) or fractal != cycle[0] * cycle[1] * cycle[2] * cycle[3]:
        raise ValueError(f"Canonical fractal must equal the product of its cycle: {fractal!r}")
    return normalized, tuple(cycle), fractal


ARCHETYPES, KOB_CICLO, KOB_FRACTAL = _load_contract()
ARCHETYPE_HZ = {name: value["hz"] for name, value in ARCHETYPES.items()}
KOB_LEI = "VERDADE × INTEGRAR ÷ Δ = ∞"
KOB_CENTRO = "JESUS = VERBO = GRAVIDADE"
