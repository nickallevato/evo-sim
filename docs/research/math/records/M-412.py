#!/usr/bin/env python3
"""M-412 record: Eden's genetic-transfer count (10^36) and the population it needs (10^30).

Object: docs/research/math/objects.yaml M-412 (formula, derivation). Eden (Wistar p.9, claim file D14 q2)
estimates 'something like 10^36 genetic transfers' for a single ordered pair of genes; Davis relays it
(claim file D14 q1, RD-03). Claim file D14 states his chain: a transposition with frequency 1e-15 per
sequential pair of transfers and a specific transposition with probability 1e-21, and for E. coli 1e12
two-hour periods with 1e-6 of the population mating at any instant. The record computes 1/(1e-15 x
1e-21) and 1e36/(1e12 x 1e-6) in exact fractions. The inputs are unsourced in the volume (claim file
D14); the record checks only the arithmetic.

Run: research/.venv/bin/python -I docs/research/math/records/M-412.py [--write]
Without --write it checks that M-412.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as F

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
D14 = "docs/research/claims/D14-davis-relays-eden-1e36-genetic-transfers.md"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def finish(rec):
    rec = {"id": HERE.stem, "date": DATE, "script": f"docs/research/math/records/{HERE.name}",
           "script_sha256": hashlib.sha256(HERE.read_bytes()).hexdigest(), **rec}
    out = json.dumps(rec, indent=2, ensure_ascii=False) + "\n"
    js = HERE.with_suffix(".json")
    if "--write" in sys.argv:
        js.write_text(out, encoding="utf-8")
    elif js.exists():
        assert js.read_text(encoding="utf-8") == out, f"{js.name} is stale; rerun with --write"
    print(f"{HERE.stem}: all asserts pass")


# ---- inputs -------------------------------------------------------------------------------
DAVIS = held(D14, "it would take about 10 to the 36th power of genetic transmissions to do that.")
EDEN = held(D14, "Then to achieve a single ordered pair of genes on these assumptions would require something like 1036 "
                 "genetic transfers.")
OCR = held(D14, "Source: Eden, Wistar p.9 ('1036' = 10^36).")
CHAIN = held(D14, "a transposition of chromosomal material 'should occur in an unselected environment with a frequency of "
                  "10^-15 for each sequential pair of genetic transfers'; a specific transposition has probability 10^-21 "
                  "(uniform chain segmenting); so a single ordered gene pair needs 1/(10^-15 * 10^-21) = 10^36 genetic "
                  "transfers. E. coli: 10^12 two-hour periods since life began, 10^-6 of the population mating at any "
                  "instant, so the required population is 10^36/(10^12 * 10^-6) = 10^30 cells")
ROUGH = held(D14, "Stated (Eden): 'a very rough estimate'; unselected environment; uniform chain segmenting.")
UNSRC = held(D14, "Implicit: no selection for intermediate rearrangements; transposition frequency 10^-15 and 10^-21 are unsourced.")

p_trans, p_spec = F(1, 10 ** 15), F(1, 10 ** 21)
periods, mating = 10 ** 12, F(1, 10 ** 6)

transfers = 1 / (p_trans * p_spec)
assert transfers == 10 ** 36                       # Eden p.9 'something like 10^36'; Davis 'about 10 to the 36th'
population = transfers / (periods * mating)
assert population == 10 ** 30                      # claim file D14: 10^30 cells
assert periods * mating == 10 ** 6                 # transfers per cell over the whole period
years = periods * 2 / (24 * 365.25)
assert 2.28e8 < years < 2.29e8                     # 1e12 two-hour periods = 2.3e8 years (flag, not reconciled)

finish({
    "object": "M-412",
    "inputs": [
        {"name": "transposition frequency per sequential pair", "value": "1e-15", "cite": "claim file D14 formal statement (Eden p.9)"},
        {"name": "specific transposition", "value": "1e-21", "cite": "claim file D14 formal statement (Eden p.9)"},
        {"name": "E. coli two-hour periods since life began", "value": "1e12", "cite": "claim file D14 formal statement"},
        {"name": "fraction mating at any instant", "value": "1e-6", "cite": "claim file D14 formal statement"},
        {"name": "printed counts", "value": {"eden": "something like 10^36", "davis": "about 10 to the 36th power"},
         "cite": "claim file D14 q2 (Wistar p.9), q1 (RD-03)"},
    ],
    "values": {"genetic_transfers": "1e36", "population_cells": "1e30", "transfers_per_cell": "1e6"},
    "positions": {
        "day": {"reading": "about 10^36 genetic transfers for one ordered pair of genes (Davis relaying Eden)",
                "transfers": "1e36", "population": "1e30"},
        "critic": {"reading": "the probabilities are unsourced and the mechanism is transposition, not point mutation",
                   "number": "none: the critic position disputes the inputs, not the arithmetic; no alternative "
                             "frequency is in the corpus"},
    },
    "notes": "The arithmetic reproduces exactly: 1/(1e-15 x 1e-21) = 1e36 transfers and 1e36/(1e12 x 1e-6) = 1e30 "
             "cells. Both inputs are unsourced in the volume and Eden calls the result a very rough estimate. The "
             "inputs are read from claim file D14's statement of Eden's chain; Eden's p.9 wording of the E. coli "
             "inputs is not held verbatim, and 1e12 two-hour periods is about 2.3e8 years, which this record does not "
             "reconcile with 'since life began'.",
})
