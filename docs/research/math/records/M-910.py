#!/usr/bin/env python3
"""M-910 record (derivation): required time as a multiple of the age of the Universe (Keen, ROOT-K).

Object: docs/research/math/objects.yaml M-910 (formula, derivation). Keen's preface (ROOT-K q1, q2) gives no equation;
the claim file's reading is T_required = T_div x shortfall at a fixed per-fixation rate: 6.3e6 y x 1.075e6 = 6.7725e12 y
(parameters divergence.t_div_years.day_2026_mittens3 and shortfall.mittens3_full; the shortfall is M-901's), against
13.8e9 y (the claim file's 1.38e10) = 490.8 universe-ages, 2.69 orders. The older 220,000x gives 6.3e6 x 2.2e5 =
1.386e12 y = 100.4 universe-ages. The record adds two held comparisons: the break-even multiplier 1.38e10 / 6.3e6 =
2,190 (any shortfall below it gives less than one universe-age), and Day's own SNV-only shortfall 91,600 (parameters
shortfall.mittens3_snv_only) = 5.77e11 y = 41.8 universe-ages; the critics' scaled 10-100 gives 6.3e7-6.3e8 y, 0.005-
0.046 universe-ages. Exact rationals, stdlib.

Run: research/.venv/bin/python -I docs/research/math/records/M-910.py [--write]
Without --write it checks that M-910.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
K = CL + "ROOT-k-keen-time-is-the-reason.md"
PY = "docs/research/parameters.yaml"
QD = "docs/research/sources/quotes-day.md"
M901 = "docs/research/math/records/M-901.json"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


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


# ---- the source sentences ---------------------------------------------------------------------------
Q1 = held(K, "The reason it fails, as Vox Day and Claude Athos show in this book, is time.")          # ROOT-K q1 (KE-01)
Q2 = held(K, "is orders of magnitude greater than the age of the Universe, let alone the age of the Earth.")  # ROOT-K q2 (KE-05)
TRUNC = held(K, "The sentence's subject is truncated in the extracted quote; the full sentence is in the source.")
NOEQ = held(K, "the preface has no equations.")
SCOPE = held(K, "fidelity: partial      # endorses The Frozen Gene, not the MITTENS papers; scope differs")
FORM = held(K, "`T_required = T_div * shortfall = 6.3e6 y * 1.075e6 = 6.77e12 y`")
UNIV = held(K, "`6.77e12 / 1.38e10 = 491` universe-ages")
ONLY = held(K, "'Orders of magnitude greater' holds (2.7 orders) only if the shortfall is read as a time multiplier at a "
               "fixed per-fixation rate.")
OLD = held(K, "For the older 220,000x shortfall: 6.3e6 * 2.2e5 = 1.4e12 y (100 universe-ages).")
CRIT = held(K, "with validated scaling (A5) and SNV-only counts (A3x) the time multiplier falls to ~10-10^2, i.e. well "
               "below universe-ages.")

# ---- inputs -------------------------------------------------------------------------------------------------
held(PY, "day_2026_mittens3: {value: 6.3e6, source: Z23003785")       # divergence.t_div_years.day_2026_mittens3
held(PY, "mittens3_full: {value: 1075000, source: Z23003785, verified: true}")    # shortfall.mittens3_full
held(PY, "mittens3_snv_only: {value: 91600")                          # shortfall.mittens3_snv_only
held(QD, "2025: 1600, d=0.45, 146,250, 20M, 220,000x")                # the older version (quotes-day row 14; M-901)
T_DIV, SHORT, SNV, OLD_S = Fr(6_300_000), Fr(1_075_000), Fr(91_600), Fr(220_000)
T_U = Fr(13_800_000_000)                                              # 1.38e10 y, ROOT-K formal statement
m901 = json.loads((ROOT / M901).read_text(encoding="utf-8"))
assert abs(m901["values"]["shortfall"] - SHORT) / SHORT < Fr(1, 1000)   # M-901: 1.0754e6 reproduces the stated 1.075e6

# ---- the arithmetic -------------------------------------------------------------------------------------------
t_req = T_DIV * SHORT
assert t_req == Fr(6_772_500_000_000)                                 # 6.7725e12 y
ages = near(float(t_req / T_U), 490.76, 0.005)                        # 490.8 universe-ages
orders = near(math.log10(ages), 2.691, 0.0005)                        # 2.69 orders ("2.7")
t_old = T_DIV * OLD_S
assert t_old == Fr(1_386_000_000_000)                                 # 1.386e12 y ("1.4e12")
near(float(t_old / T_U), 100.43, 0.005)                               # about 100 universe-ages
breakeven = near(float(T_U / T_DIV), 2190.5, 0.05)                    # shortfall needed for one universe-age
t_snv = T_DIV * SNV
near(float(t_snv), 5.7708e11, 1e7); near(float(t_snv / T_U), 41.82, 0.005)   # SNV-only: 41.8 universe-ages
assert SNV > breakeven                                                # Day's own SNV-only figure still exceeds one age
for m in (10, 100):
    assert T_DIV * m < T_U                                            # the critics' 10-100 multiplier: below one age
near(float(T_DIV * 100 / T_U), 0.0457, 0.0005); near(float(T_DIV * 10 / T_U), 0.00457, 0.00005)

finish({
    "object": "M-910",
    "inputs": [
        {"name": "T_div", "value": float(T_DIV), "cite": "parameters divergence.t_div_years.day_2026_mittens3"},
        {"name": "shortfall", "value": {"mittens3_full": int(SHORT), "older_2025": int(OLD_S), "snv_only": int(SNV)},
         "cite": "parameters shortfall.mittens3_full, shortfall.mittens3_snv_only; quotes-day.md row 14; M-901.json"},
        {"name": "age of the Universe", "value": float(T_U), "cite": "claim ROOT-K formal statement (1.38e10)"},
        {"name": "Keen", "value": ["ROOT-K q1", "ROOT-K q2"], "cite": "claim ROOT-K (KE-01, KE-05)"},
    ],
    "values": {
        "T_required_y": float(t_req), "universe_ages": round(ages, 1), "orders": round(orders, 2),
        "older_220000x": {"T_required_y": float(t_old), "universe_ages": round(float(t_old / T_U), 1)},
        "snv_only_91600": {"T_required_y": float(t_snv), "universe_ages": round(float(t_snv / T_U), 1)},
        "breakeven_multiplier": round(breakeven, 1),
        "critic_multiplier_10_to_100": {"T_required_y": [6.3e7, 6.3e8],
                                        "universe_ages": [round(float(T_DIV * 10 / T_U), 4), round(float(T_DIV * 100 / T_U), 4)]},
    },
    "positions": {
        "day": {"reading": "each fixation takes a fixed LTEE time, so the required time is the divergence time times the "
                           "shortfall: orders of magnitude beyond the age of the Universe",
                "holds": "6.3e6 x 1.075e6 = 6.7725e12 y = 490.8 universe-ages (2.69 orders); even Day's SNV-only 91,600 "
                         "gives 41.8 universe-ages; any shortfall above 2,190 exceeds one age"},
        "critic": {"reading": "the arithmetic holds only if the shortfall is a time multiplier at a fixed rate; Keen gives "
                              "no equation and endorses The Frozen Gene, not the MITTENS papers",
                   "holds": "with a validated scaling and SNV-only counts the multiplier falls to about 10-100, i.e. "
                            "6.3e7-6.3e8 y, 0.005-0.046 universe-ages; the 205M counts bp of structural variants"},
    },
    "notes": "Keen's sentence is checkable only under the claim file's reading (T_required = T_div x shortfall at a fixed "
             "per-fixation rate); the preface has no equation and its subject is truncated in the extracted quote. "
             "Under that reading it holds at Day's figures (490.8 ages; 100.4 at the older 220,000x). The question is "
             "the shortfall, not this multiplication: the break-even is 2,190, so the critics' 10-100 falls below one "
             "age and Day's SNV-only 91,600 does not. Whether the shortfall is 1e6, 9e4 or 1e1-1e2 is A, A3x and A5's "
             "external question, not settled here.",
})
