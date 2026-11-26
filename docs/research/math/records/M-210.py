#!/usr/bin/env python3
"""M-210 record: census fluctuation with overlapping generations, RRME k = 0.743 mu against Balloux-Lehmann.

Object: docs/research/math/objects.yaml M-210 (formula, derivation). RRME (Z18525262):
k = mu (sum N_i^2 / sum N_i)/N_t over four census cohorts. The record recomputes 6.091/8.2 = 0.743, the
per-cohort column, the 25.7%, and the window sensitivity at the same growth ratio (claim file B3c), then
B&L's effect sizes as recomputed in R4 B3b: eq. (11) ks = 2 - N1/N2, the symmetric-cycle form
1 - (s/(1-s))(cosh r - 1) at human survival s = 0.96, and the arrival-rate factor during Day's growth
window. It sets R4 XT's fwdpy11 misses beside them. Inputs carry their quote id, claim file or result
file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-210.py [--write]
Without --write it checks that M-210.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QL = "docs/research/sources/quotes-literature.md"
PY = "docs/research/parameters.yaml"
RB = "research/checks/results/R4-B3b-C1.md"
XT = "research/checks/results/R4-XT.md"


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


def rrme(ns):
    return sum(n * n for n in ns) / sum(ns) / ns[-1]


# ---- inputs -------------------------------------------------------------------------------
Q40 = held(CL + "B3c-rrme-k-0743-mu.md", "k = μ × 6.091/8.2 = 0.743μ (3)")
KI = held(CL + "B3c-rrme-k-0743-mu.md", "k_{i} = M_{i} × 1/(2N_{t}) = 2N_{i}μ × 1/(2N_{t}) = μN_{i}/N_{t}")
SHORT = held(CL + "B3c-rrme-k-0743-mu.md", "The 25.7% shortfall is not an approximation error or a boundary effect")
COH = held(CL + "B3c-rrme-k-0743-mu.md", "cohorts 1950–2025 at 25-year spacing: N = 2.5, 4.0, 6.1, 8.2 (billions)")
PY743 = held(PY, "day_k_over_mu_0_743: {value: 0.743")
BL_OV = held(CL + "B3b-balloux-lehmann-overlap-and-fluctuation.md",
             "we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations")
BL_NO = held(CL + "B3b-balloux-lehmann-overlap-and-fluctuation.md",
             "population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations")
DAY_BL = held(CL + "B3b-balloux-lehmann-overlap-and-fluctuation.md",
              "Balloux and Lehmann (2012) demonstrated that under the joint conditions of fluctuating demography and "
              "overlapping generations, conditions which are satisfied by every natural population of interest, k ≠ μ.")
EQ11 = held(RB, "eq (11) gives ks = 2 - N1/N2 = 1.667")
CYC = held(RB, "Matches 1 - (s/(1-s))(cosh r - 1).")
HUM = held(RB, "### Human-like magnitude and sign (exact eq 3; s = 0.96/yr, generation 25 y)")
WIN = held(RB, "births/N = 1 - s/(1+r) = 0.0551 vs 0.040")
XTROW = held(XT, "| B3b non-overlapping fluctuating N | k/U 0.961, 0.955, 0.948 (z -5 to -7.6); numpy 1.00-1.01 |")
XTCOH = held(XT, "P_fix*M_i = 0.639, 0.629, 0.637, 0.639 (target 1.0; numpy 0.97-1.02; Day's M_i/164 would give 0.305, 0.488, 0.744, 1.0)")

# ---- RRME -----------------------------------------------------------------------------------
N = [2.5, 4.0, 6.1, 8.2]
near(sum(n * n for n in N), 126.70, 1e-9)
near(sum(N), 20.8, 1e-9)
near(sum(n * n for n in N) / sum(N), 6.091, 0.0005)
k = rrme(N)
near(k, 0.7428, 0.0001)
assert round(k, 3) == 0.743
near(1 - round(k, 3), 0.257, 1e-12)                     # "25.7% shortfall"
col = [n / N[-1] for n in N]
assert [round(c, 3) for c in col] == [0.305, 0.488, 0.744, 1.0]
# window sensitivity at the paper's growth ratio per cohort
gr = (8.2 / 2.5) ** (1 / 3)
near(gr, 1.485, 0.001)
sens = {n: rrme([gr ** i for i in range(n)]) for n in (2, 3, 4, 6, 10, 20)}
for n, v in zip((2, 3, 4, 6, 10, 20), (0.87, 0.78, 0.72, 0.65, 0.61, 0.60)):
    near(sens[n], v, 0.005)
near(gr / (gr + 1), 0.5977, 0.0001)                     # long-window limit g/(g+1)

# ---- Balloux-Lehmann effect sizes (R4 B3b) ------------------------------------------------------
eq11 = 2 - 50 / 150
near(eq11, 1.667, 0.0005)
s = 0.96
cyc = {r: 1 - (s / (1 - s)) * (math.cosh(r) - 1) for r in (0.005, 0.016, 0.03)}
near(cyc[0.005], 0.9997, 0.0001)
near(cyc[0.016], 0.9969, 0.0001)
near(cyc[0.03], 0.9892, 0.0001)
births = 1 - s / (1 + 0.016)
near(births, 0.0551, 0.0001)
near(births / (1 - s), 1.378, 0.001)                    # arrival of eventual fixers raised 1.38x in growth
near(s * math.log(8.2 / 2.5), 1.140, 0.001)             # one-off excess, units of U
non_overlap = 1.0                                       # B&L: no overlap, any fluctuation -> k = mu

# ---- R4 XT misses (fwdpy11) beside their targets --------------------------------------------------
xt_b3b = [0.961, 0.955, 0.948]
assert all(0.94 < v < 0.97 for v in xt_b3b) and non_overlap == 1.0
xt_coh = [0.639, 0.629, 0.637, 0.639]
near(sum(xt_coh) / 4, 0.636, 0.001)                     # constant factor, not Day's cohort-proportional column
assert max(xt_coh) - min(xt_coh) < 0.011 and col[0] < 0.31

finish({
    "object": "M-210",
    "inputs": [
        {"name": "RRME k", "value": "mu x 6.091/8.2 = 0.743 mu", "cite": "Q40 (B3c q1); parameters rates.day_k_over_mu_0_743"},
        {"name": "cohort census (billions)", "value": N, "cite": "claim file B3c formal statement (Z18525262)"},
        {"name": "B&L with and without overlap", "cite": "B3b q2, q3 (Balloux & Lehmann 2012)"},
        {"name": "Day on B&L", "cite": "B3b q1 (Z22903977 s6)"},
        {"name": "B&L effect sizes", "value": {"eq11": "2 - N1/N2, N 50/150", "cycle": "1 - (s/(1-s))(cosh r - 1)", "s": s}, "cite": "R4-B3b-C1.md (B3b section)"},
        {"name": "fwdpy11 B3b and cohort rows", "value": {"b3b": xt_b3b, "cohort": xt_coh}, "cite": "R4-XT.md"},
    ],
    "values": {
        "rrme_k_over_mu": g(k), "per_cohort": [round(c, 3) for c in col], "shortfall": 0.257,
        "window_sensitivity": {str(n): g(v) for n, v in sens.items()}, "growth_ratio": g(gr),
        "bl_eq11": g(eq11), "bl_cycle_s096": {str(r): g(v) for r, v in cyc.items()},
        "bl_growth_arrival_factor": g(births / (1 - s)),
    },
    "positions": {
        "day": {"k_over_mu": 0.743, "shortfall": 0.257, "reading": "a mathematical consequence of real census sizes, confirmed by B&L"},
        "critic": {"reading": "B&L's effect needs overlap plus fluctuation; RRME is a four-cohort window",
                   "bl_no_overlap": non_overlap, "bl_human_cycle_range": [g(cyc[0.03]), g(cyc[0.005])],
                   "rrme_by_window": {str(n): g(v) for n, v in sens.items()},
                   "xt_not_reproduced": {"b3b_non_overlap": xt_b3b, "cohort_factor": 0.636}},
    },
    "notes": "RRME arithmetic reproduces (0.7428; column 0.305/0.488/0.744/1). The value is a property of the window: "
             "0.87 to 0.60 for 2 to 20 cohorts at the same growth. B&L give k = mu without overlap; with overlap at "
             "human survival the cycle effect is -0.03% to -1.1% and growth raises arrivals 1.38x. fwdpy11 misses "
             "(B3b 0.95-0.96, cohort 0.64) track an unlocalised engine deficit (R4 XT), not RRME's form.",
})
