#!/usr/bin/env python3
"""M-012 record (model-choice): the factor of two between lineages.

Object: docs/research/math/objects.yaml M-012 (model-choice, derivation). Day halves the required
count to a per-lineage figure; Hancock doubles the achievable count because both lineages fix
mutations. The record computes the shortfall under each convention and under both at once (the
double count) and asserts them; it does not choose a convention. Inputs carry their quote id or
claim file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-012.py [--write]
Without --write it checks that M-012.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def g(x):
    return float(f"{x:.6g}")


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


A3D = CL + "A3d-factor-of-two-both-lineages.md"
# ---- inputs -------------------------------------------------------------------------------
Q15 = held(QD, "for a total of approximately 410 million genomic differences. Apportioned symmetrically to the "
               "human lineage this yields approximately 205 million required fixations.")
Q12 = held(QD, "~40 million single-nucleotide variants; ~20 million fixations required on human lineage.")
Q91 = held(QD, "at most 180 fixations on the human lineage given 252,000 generations and 1,400 generations per fixation")
GG02 = held(A3D, "this basic math is off by a factor of two")                                    # A3d q1
GG02b = held(A3D, "So this really should be at least 360")
Q04 = held(QD, "that would permit 562 total fixed mutations in that time frame. Which is only 29,999,438 short")
Q05 = held(QD, "a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000")
Q17 = held(QD, "At 1,322 gen/fix (non-mutator): 191 achievable.")
G07B = held(A3D, "the gorilla-polarized SNV split is 48.6% human-derived / 51.4% chimp-derived")

R_total, F_one = 410e6, 252_000 / 1400
assert F_one == 180
R_lin = R_total / 2
assert R_lin == 205e6                                   # Q15
assert 40e6 / 2 == 20e6                                 # Q12 (2025)

# ---- Day: required count halved, achievable for one lineage -------------------------------
short_day = R_lin / F_one
near(short_day, 1_138_889, 1)                           # Q91 "1,139,000-fold"
# ---- Hancock: achievable doubled (360) against the total divergence -----------------------
F_two = 2 * F_one
assert F_two == 360                                     # GG-02 "at least 360"
short_hancock = R_total / F_two
assert math.isclose(short_hancock, short_day)          # the two conventions give the same shortfall
# ---- both at once: halved R against doubled F (double count) -----------------------------
short_both = R_lin / F_two
near(short_both, 569_444, 1)
assert math.isclose(short_both, short_day / 2)
# ---- 3.0 headline: unchanged by Hancock's correction if R is already per lineage ------------
near(205e6 / 191, 1_073_298, 1)
assert math.isclose(R_total / (2 * 191), 205e6 / 191)
# ---- 2019: the post uses the other convention (two-lineage F against total R) --------------
f19 = 450_000 / 1600
assert math.floor(2 * f19) == 562
assert 30e6 / (2 * f19) == 15e6 / f19                  # 53,333 either way
# ---- symmetric apportioning: R4 GAP-07b polarised SNV split ------------------------------
human_share = 0.486
near(human_share + 0.514, 1.0, 1e-12)
near(abs(human_share - 0.5) / 0.5, 0.028, 0.001)       # 2.8% from symmetric

finish({
    "object": "M-012",
    "inputs": [
        {"name": "R total and per lineage (3.0)", "value": [410e6, 205e6], "cite": "Q15"},
        {"name": "R per lineage (2025)", "value": [40e6, 20e6], "cite": "Q12"},
        {"name": "F one lineage", "value": "252,000/1,400 = 180", "cite": "Q91 (A2j q1); A2d q3 (DU-02)"},
        {"name": "Hancock doubling", "value": 360, "cite": "A3d q1 (GG-02) and claim file A3d"},
        {"name": "2019 convention", "value": [562, 29_999_438, "15e6 + 15e6"], "cite": "Q04, Q05"},
        {"name": "3.0 achievable", "value": 191, "cite": "Q17"},
        {"name": "polarised SNV split", "value": [0.486, 0.514], "cite": "claim file A3d (R4 GAP-07b)"},
    ],
    "values": {
        "shortfall_day_per_lineage": g(short_day), "shortfall_hancock_total": g(short_hancock),
        "conventions_equal": True, "shortfall_both_double_count": g(short_both),
        "shortfall_3.0_per_lineage_191": g(205e6 / 191), "shortfall_2019_either_convention": g(15e6 / f19),
        "gap07b_human_share": human_share,
    },
    "positions": {
        "day": {"convention": "R halved to the human lineage, F for one lineage", "R": R_lin, "F": F_one, "shortfall": g(short_day)},
        "critic": {"convention": "F doubled for two lineages, valid if R is the total divergence", "R": R_total, "F": F_two,
                   "shortfall": g(short_hancock)},
        "both": {"R": R_lin, "F": F_two, "shortfall": g(short_both), "note": "double count: halves the shortfall"},
    },
    "notes": "The two conventions are the same ratio; Hancock's doubling changes the shortfall only if applied to a "
             "required count that is already per lineage. The 2019 post used the doubled-F convention (562).",
})
