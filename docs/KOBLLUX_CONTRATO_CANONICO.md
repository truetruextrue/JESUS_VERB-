# KOBLLUX canonical contract

The Python engines share their canonical archetype frequencies and cycle
through `kobllux_contract.py`. Its source is the `arquetipos` table and
`_kobllux_meta.ciclos` in `kobllux_memory.json`.

The cycle is fixed as `3 → 6 → 9 → 7` (detect, integrate, expand, seal), and
the fractal value must equal its product, `1134`. The contract validates both
invariants when imported and fails explicitly if the source data is malformed.

Archetype frequencies in the contract are:

| Archetype | Hz | Cycle phase |
|---|---:|---:|
| Atlas | 594 | 3 |
| Nova | 432 | 3 |
| Pulse | 639 | 3 |
| Vitalis | 528 | 3 |
| Artemis | 672 | 6 |
| Serena | 528 | 6 |
| Kaos | 741 | 6 |
| Genus | 594 | 6 |
| Lumine | 432 | 9 |
| Rhea | 528 | 9 |
| Solus | 963 | 9 |
| Aion | 777 | 9 |
| Kodux | 741 | 9 |
| Bllue | 639 | 6 |
| Jesus | 963 | 9 |
| Kobllux | 1134 | 9 |

Opcode numbers remain local, versioned aliases. A consumer may retain a
different opcode for the same archetype, but must not use that difference to
change its canonical frequency or the cycle. This initial integration covers
the central Python engines; HTML and JavaScript copies are not rewritten in
bulk.

Run the focused checks with:

```sh
python3 -m unittest discover -s tests -p 'test_kobllux*.py'
```
