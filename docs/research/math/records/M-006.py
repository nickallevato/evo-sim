#!/usr/bin/env python3
"""M-006 record (inference): the LTEE as an empirical ceiling, rate_human <= 1/G_f with no scaling.

Object: docs/research/math/objects.yaml M-006 (inference, derivation). The record computes the
supply figures the statement claims (38.4, 4.1e-4, ratio 93,659) and the achievable count under
each side's transfer assumption side by side: no scaling (Day, kappa^0), linear supply scaling
(the critics' illustration, kappa^1), and the LTEE's own mutator response exponent (an audit
sensitivity from claim file A5b). It does not choose one. The supply-limited model result is
R4 A2e's and is cited, not recomputed.

Run: research/.venv/bin/python -I docs/research/math/records/M-006.py [--write]
Without --write it checks that M-006.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"


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


A2E = CL + "A2e-ltee-as-ceiling.md"
A5B = CL + "A5b-kittens-94000x11p7.md"
# ---- inputs -------------------------------------------------------------------------------
Q131 = held(A2E, "Whatever number the LTEE produces, it is the empirical ceiling on what evolution can accomplish "
                 "when every tool in its kit is deployed simultaneously under ideal conditions.")       # A2e q1
Q132 = held(QD, "neutral hitchhikers ≈ 4.1 × 10⁻⁴ × 50,000 = 20.5")                                      # U_E
Q135 = held(QD, "(3.2 × 10⁹ bp × 1.2 × 10⁻⁸ × 100)")                                                    # U_h x 100
KAPPA = held(PY, "supply_ratio_kappa: {value: 93659, derived: \"38.4 / 4.1e-4\"")
Q58 = held(QD, "1,322 generations per fixation")
Q17 = held(QD, "At 1,322 gen/fix (non-mutator): 191 achievable.")
RE08 = held(A5B, "the achievable number (17.9 million) is about equal to the required number (17.5 million)")  # A5b q2
RE09 = held(A5B, "I present this as an illustration, not as a proof that adaptive fixations scale linearly with mutation rate.")
MUT = held(CL + "A2d-gf-average-not-fastest.md", "mean over seven 104.7) and the metagenomic mutator average at 60K is 78")
Q13 = held(QD, "893 generations per fixation by clone-pair analysis")
R4A2E = held(A2E, "the flip kappa* is a threshold on supply x beneficial-fraction x effect-size (central 217, corners 3.9-13,050)")

# ---- supply per genome per generation ----------------------------------------------------
U_E = 4.1e-4
U_h = 3.2e9 * 1.2e-8
near(U_h, 38.4, 1e-9)
kappa = U_h / U_E
assert round(kappa) == 93_659

# ---- Day: no scaling (kappa^0); the ceiling rate_human <= 1/G_f ---------------------------
G_f = 1322
rate_ceiling = 1 / G_f
near(rate_ceiling, 7.564e-4, 0.0005e-4)
F_day = 191                                            # the paper's rounded achievable (Q17); 252,000/1,322 = 190.6
near(252_000 / G_f, F_day, 0.5)

# ---- critics: linear supply scaling (kappa^1), an illustration (RE-09) ---------------------
F_lin = F_day * kappa
near(F_lin, 17.89e6, 0.005e6)                          # "17.9 million"
near(F_lin / 17.5e6, 1.02, 0.005)                      # about equal to the SNV-only 17.5e6

# ---- audit sensitivity (claim file A5b): the LTEE's own 100x mutator response --------------
a_lo = math.log(893 / 104.7) / math.log(100)
a_hi = math.log(1322 / 78) / math.log(100)
near(a_lo, 0.47, 0.005)
near(a_hi, 0.61, 0.005)
fac_lo, fac_hi = kappa ** a_lo, kappa ** a_hi
near(fac_lo, 206, 1)
near(fac_hi, 1136, 1)
F_lo, F_hi = F_day * fac_lo, F_day * fac_hi
near(F_lo, 39_370, 100)
near(F_hi, 217_006, 300)
near(17.5e6 / F_lo, 445, 1)
near(17.5e6 / F_hi, 81, 0.5)
near(205e6 / F_lo, 5_207, 15)
near(205e6 / F_hi, 945, 2)

finish({
    "object": "M-006",
    "inputs": [
        {"name": "ceiling statement", "cite": "A2e q1 (Q131)", "quote": Q131},
        {"name": "U_E, LTEE per genome per generation", "value": U_E, "cite": "Q132; parameters ltee.mu_genome_ancestral"},
        {"name": "U_h factors 3.2e9 bp x 1.2e-8", "value": [3.2e9, 1.2e-8], "cite": "Q135 (printed with x100); parameters mutation.new_mutations_per_haploid_genome"},
        {"name": "kappa", "value": 93_659, "cite": "parameters mutation.supply_ratio_kappa"},
        {"name": "G_f and achievable", "value": [1322, 191], "cite": "Q58, Q17"},
        {"name": "linear-scaling illustration", "cite": "A5b q2 (RE-08), caveat A5b q3 (RE-09)", "quote": RE08},
        {"name": "mutator G_f 104.7 and 78, clone pair 893", "cite": "claim file A2d; Q13"},
        {"name": "supply-limited model result (not recomputed)", "cite": "claim file A2e, R4 A2e", "quote": R4A2E},
    ],
    "values": {
        "U_h": g(U_h), "U_E": U_E, "kappa": g(kappa), "rate_ceiling_per_gen": g(rate_ceiling),
        "F_no_scaling": F_day, "F_linear": g(F_lin), "F_linear_over_17.5e6": g(F_lin / 17.5e6),
        "mutator_exponents": [g(a_lo), g(a_hi)], "scale_factors": [g(fac_lo), g(fac_hi)],
        "F_sublinear": [g(F_lo), g(F_hi)],
        "shortfall_sublinear_vs_17.5e6": [g(17.5e6 / F_lo), g(17.5e6 / F_hi)],
        "shortfall_sublinear_vs_205e6": [g(205e6 / F_lo), g(205e6 / F_hi)],
    },
    "positions": {
        "day": {"transfer": "none (kappa^0): the LTEE is the best case, so human rate <= 1/G_f", "F": F_day,
                "shortfall_vs_205e6": g(205e6 / F_day)},
        "critic": {"transfer": "unstated; supply gap 93,659x unscaled; linear scaling is an illustration only (RE-09)",
                   "F_linear": g(F_lin), "shortfall_vs_17.5e6_linear": g(17.5e6 / F_lin)},
        "sensitivity_not_a_side": {"transfer": "LTEE 100x mutator response, exponent 0.47-0.61 (claim file A5b)",
                                   "F": [g(F_lo), g(F_hi)]},
    },
    "notes": "The ceiling holds only under a stated transfer factor; Day states none. The arithmetic of each transfer "
             "is fixed here; the supply-limited model's flip point is R4 A2e's (kappa* central 217), cited not recomputed.",
})
