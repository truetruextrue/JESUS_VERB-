#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
KOBLLUX TRINITY SYSTEM · main.py
Ponto de entrada unificado — delega ao VERBO central.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from VERBO import cli

if __name__ == "__main__":
    cli()
