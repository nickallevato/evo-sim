#!/usr/bin/env python3
"""M-208 record (model-choice): size-change transient of the neutral substitution count.

Object: docs/research/math/objects.yaml M-208 (model-choice, derivation). After a step from N1 to N2
with the pipe full at N1: the alleles in flight at the step carry mu x 4 N1 eventual fixations
(Little's law; their fixation probabilities are their frequencies, so the step does not change the
total), and new mutations deliver mu int_0^T F2. For T >> 4 max(N1, N2) the cumulative count over mu T
is 1 - 4 (N2 - N1)/T; the finite-T new-pipe term uses the diffusion series of M-201. The record checks
the B1b design (N0 = 500, T = 3 x 4 N0): analytic 0.733 (expansion) and 1.267 (contraction), the numpy
results (claim file B1b) and the fwdpy11 result 0.699 (R4 XT) against them. Inputs carry their quote
id, claim file or result file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-208.py [--write]
Without --write it checks that M-208.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
B1B = CL + "B1b-size-change-transient.md"
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


def int_tail(T, ne, terms=200):
    """int_0^T (1 - F_X(u)) du for a constant-size pipe of effective size ne (diffusion series)."""
    four = 4 * ne
    return four * (1 - sum((-1) ** (i + 1) * (2 * i + 1) / (i * (i + 1)) * math.exp(-i * (i + 1) * T / four)
                           for i in range(1, terms)))


def lead(n1, n2, T):
    return 1 - 4 * (n2 - n1) / T


# ---- inputs -------------------------------------------------------------------------------
Q1 = held(B1B, "it holds only after a population has held one size for the roughly 4N ₑ generations a neutral allele "
               "needs to drift from a single copy to fixation.")
Q2 = held(B1B, "Interrupt that condition and the far end delivers whatever the near end was feeding it 4Nₑ generations "
               "back, not what it is feeding it now.")
SIM = held(B1B, "N0=500, U=0.2, 24 replicates, T = 3×4N0. Cumulative/U·T: constant 0.996; contraction N0→N0/5 1.259 "
                "(analytic 1.267); expansion N0/5→N0 0.733 (analytic 0.733); expansion N0/5→5N0 0.085 (saturating)")
XTROW = held(XT, "| B1b | constant 0.979 (z -2.0); contraction 1.254 (target 1.267, z -1.1); expansion 0.699 (target 0.733, z -4.8) |")

N0 = 500
T = 3 * 4 * N0
assert T == 6000

# ---- leading order ---------------------------------------------------------------------------
exp_lead = lead(N0 / 5, N0, T)
con_lead = lead(N0, N0 / 5, T)
near(exp_lead, 0.7333, 0.0001)                          # "analytic 0.733"
near(con_lead, 1.2667, 0.0001)                          # "analytic 1.267"
assert lead(N0, N0, T) == 1.0                           # constant size: k = mu
assert lead(N0 / 5, 5 * N0, T) < 0                      # N0/5 -> 5N0: 4 N2 > T, formula leaves its regime

# ---- finite-T new pipe (old in-flight mass mu 4 N1 assumed delivered by T) -------------------------
exp_fin = (T - int_tail(T, N0) + 4 * N0 / 5) / T
near(exp_fin, 0.7346, 0.0001)                           # 0.13% above the leading order
con_fin = (T - int_tail(T, N0 / 5) + 4 * N0) / T        # old N0 pipe in flight: 4 N0 = 2000 < T
near(con_fin, 1.2667, 0.0001)
sat_new_only = (T - int_tail(T, 5 * N0)) / T            # lower bound: new mutations alone, x = 0.6
near(sat_new_only, 0.0491, 0.0005)
sat_upper = sat_new_only + 4 * (N0 / 5) / T             # plus all of the old in-flight mass
near(sat_upper, 0.1158, 0.0005)
assert sat_new_only < 0.085 < sat_upper                 # the numpy 0.085 sits between the bounds

# ---- simulated values against the analytic target ---------------------------------------------
numpy = {"constant": 0.996, "contraction": 1.259, "expansion": 0.733, "saturating": 0.085}
fwd = {"constant": 0.979, "contraction": 1.254, "expansion": 0.699}
near(numpy["expansion"], exp_lead, 0.002)
near(numpy["contraction"], con_lead, 0.01)
xt_gap = fwd["expansion"] / exp_lead - 1
near(xt_gap, -0.0468, 0.0005)                           # fwdpy11 4.7% below the target (z -4.8)
const_gap = fwd["constant"] - 1
near(const_gap, -0.021, 1e-9)                           # the same engine is 2.1% low at constant size
near(fwd["expansion"] / fwd["constant"], 0.714, 0.001)  # expansion relative to its own control

finish({
    "object": "M-208",
    "inputs": [
        {"name": "Day: k = mu only after one size held ~4Ne", "cite": "B1b q1 (Z22129121 abstract)"},
        {"name": "Day: far end delivers what near end fed 4Ne back", "cite": "B1b q2 (Z22129121 s Transit Time)"},
        {"name": "B1b design and numpy results", "value": {"N0": N0, "T": T, **numpy}, "cite": "claim file B1b Check (research/checks/b1b_demography.py)"},
        {"name": "fwdpy11 results", "value": fwd, "cite": "R4-XT.md results table, row B1b"},
    ],
    "values": {
        "leading": {"expansion": g(exp_lead), "contraction": g(con_lead), "saturating": g(lead(N0 / 5, 5 * N0, T))},
        "finite_T": {"expansion": g(exp_fin), "contraction": g(con_fin)},
        "saturating_bounds": [g(sat_new_only), g(sat_upper)],
        "xt_expansion_gap": g(xt_gap), "xt_constant_gap": g(const_gap),
    },
    "positions": {
        "day": {"reading": "a transient follows any size change; expansion gives a deficit",
                "expansion_ratio": g(exp_lead), "confirmed_numpy": True},
        "critic": {"reading": "standard theory; the sign reverses for contractions; the human-lineage history is B1c's empirical question",
                   "contraction_ratio": g(con_lead),
                   "xt_expansion": fwd["expansion"], "xt_gap": g(xt_gap),
                   "note": "fwdpy11 is also 2.1% low at constant size (R4 XT: an unlocalised U-dependent engine deficit), so the 0.699 miss is not a test of the theory"},
    },
    "notes": "Leading order 1 - 4(N2 - N1)/T reproduces the B1b analytic targets (0.733, 1.267) and the numpy runs; "
             "N0/5 -> 5N0 is outside the regime and the numpy 0.085 lies inside the computed bounds 0.049-0.116. "
             "R4 XT's fwdpy11 expansion 0.699 is 4.7% below target, with the same engine 2.1% low at constant size.",
})
