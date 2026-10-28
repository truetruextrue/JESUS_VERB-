#!/usr/bin/env python3
"""Correlate repository events and changed paths with canonical archetypes."""

from __future__ import annotations

import re
from collections.abc import Iterable
from typing import Any

from kobllux_contract import ARCHETYPES, KOB_CICLO, KOB_FRACTAL


EVENT_ARCHETYPES = {
    "push": "Pulse",
    "pull_request": "Nova",
    "create": "Atlas",
    "delete": "Kaos",
    "release": "Aion",
    "workflow_run": "Genus",
    "workflow_dispatch": "Aion",
    "schedule": "Aion",
    "pull_request_review": "Serena",
    "issues": "Vitalis",
    "deployment": "Artemis",
    "fork": "Atlas",
    "watch": "Pulse",
    "repository_dispatch": "Kobllux",
    "issue_comment": "Bllue",
    "check_run": "Kodux",
    "check_suite": "Kodux",
}

PATH_RULES = (
    ("scanner", ("Kodux", "Artemis")),
    ("workflow", ("Aion", "Atlas")),
    ("n8n", ("Bllue", "Rhea")),
    ("loop", ("Aion", "Kobllux")),
    ("watch", ("Aion", "Kodux")),
    ("memory", ("Rhea",)),
    ("archetype", ("Genus",)),
    ("seal", ("Aion",)),
)

_ARCHETYPE_NAMES = {
    name.casefold(): name.title() if name.casefold() != "kobllux" else "Kobllux"
    for name in ARCHETYPES
}


def correlate_event(
    event_name: str,
    changed_paths: Iterable[str] = (),
    text: str = "",
) -> dict[str, Any]:
    """Return canonical archetype metadata and safe tags for one repository event."""
    paths = [path for path in changed_paths if isinstance(path, str) and path.strip()]
    searchable = "\n".join([text, *paths]).casefold()
    archetypes: list[str] = []

    def add(name: str) -> None:
        canonical = _ARCHETYPE_NAMES.get(name.casefold())
        if canonical and canonical not in archetypes:
            archetypes.append(canonical)

    primary = EVENT_ARCHETYPES.get(event_name.casefold(), "Rhea")
    add(primary)

    path_labels: list[str] = []
    path_text = "\n".join(paths).casefold()
    for label, names in PATH_RULES:
        if label in path_text:
            path_labels.append(label)
            for name in names:
                add(name)

    for folded, canonical in _ARCHETYPE_NAMES.items():
        if re.search(rf"(?<![a-z0-9]){re.escape(folded)}(?![a-z0-9])", searchable):
            add(canonical)

    tags = ["github", event_name.casefold()]
    tags.extend(f"archetype:{name.casefold()}" for name in archetypes)
    tags.extend(f"component:{label}" for label in path_labels)
    if paths:
        tags.append("file-change")

    profiles = [
        {
            "name": name,
            "hz": ARCHETYPES[name.casefold()]["hz"],
            "opcode": ARCHETYPES[name.casefold()]["opcode"],
            "phase": ARCHETYPES[name.casefold()]["ciclo"],
        }
        for name in archetypes
    ]
    return {
        "primary": primary,
        "archetypes": archetypes,
        "tags": list(dict.fromkeys(tags))[:32],
        "profiles": profiles,
        "path_labels": list(dict.fromkeys(path_labels)),
        "cycle": list(KOB_CICLO),
        "fractal": KOB_FRACTAL,
    }


def canonical_scan_tag(archetype_name: str) -> dict[str, Any]:
    """Return canonical tags for a scanner's heuristic archetype assignment."""
    canonical = _ARCHETYPE_NAMES.get(archetype_name.casefold())
    if canonical is None:
        return {"archetype": archetype_name, "tags": ["scanner:unmapped"]}
    profile = ARCHETYPES[canonical.casefold()]
    return {
        "archetype": canonical,
        "hz": profile["hz"],
        "opcode": profile["opcode"],
        "phase": profile["ciclo"],
        "tags": [
            f"archetype:{canonical.casefold()}",
            f"frequency:{profile['hz']}hz",
            f"phase:{profile['ciclo']}",
            "scanner:heuristic",
        ],
    }
