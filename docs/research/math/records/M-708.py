#!/usr/bin/env python3
"""M-708 record (derivation): the 230-sweep cap of Z18167588 s7.8.

Object: docs/research/math/objects.yaml M-708 (formula, derivation). t_transit = (2/s) ln 9 = 439.4, about 440: the
exact logistic time from p = 0.1 to 0.9 under dp/dt = s p (1 - p). Fixations <= (T / t_transit) x C with T =
300,000: 681.8 x 230 = 156,818, about 157,000 (Q27). The C that reproduces the paper's own n = 157,000 is
157,000 x 440 / 300,000 = 230.3, so the "match" (Q27) is the input read back (circular). The paper's own criterion
applied to n loci (Gc formal statement: available additive differential 2 z sqrt(n/4) s >= required n s, z = 3.72 at
N = 10,000) gives n <= z^2 = 13.8. Near candidates: 200 (additive halving, n s p = 1 at p = 0.5, R4 G1) and 100-200
(s6.1 reproductive ceiling, sum of s <= 1.0-2.0 at s = 0.01). Requirements used elsewhere: 20e6 and 205e6, 127x and
1,306x of 157,000. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-708.py [--write]
Without --write it checks that M-708.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, statistics, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
GC = CL + "Gc-pipeline-cap-230-sweeps.md"
QD = "docs/research/sources/quotes-day.md"
PY = "docs/research/parameters.yaml"
R4G1 = "research/checks/results/R4-G1.md"


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


# ---- inputs ---------------------------------------------------------------------------------------
Q25 = ("the \"active zone\" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of "
       "approximately 230 simultaneous sweeps.")
held(GC, Q25); held(QD, Q25)                                      # Gc q1 = Q25 (abstract)
Q26 = ("Working backward from the constraint, the active zone can sustain approximately 200–300 simultaneous sweeps "
       "before the Bernoulli Barrier compresses variance below the threshold required for effective selection.")
held(GC, Q26); held(QD, Q26)                                      # Gc q2 = Q26 (s7.8, para 111)
Q27 = ("Maximum fixations ≈ (300,000 / 440) × 230 ≈ 157,000 This appears to match the requirement for "
       "human-chimpanzee divergence.")
held(GC, Q27); held(QD, Q27)                                      # Gc q3 = Q27 (s7.8, para 63)
TT = held(GC, "t_transit = (2/s)·ln 9 = 200 x 2.197 = 439.4 ≈ 440 generations (s = 0.01, 0.1 < p < 0.9)")
CRIT = held(GC, "The paper's own criterion (available additive differential 2z·√(n/4)·s ≥ required n·s, with z = 3.72 "
                "for N = 10,000) gives n ≤ z² = 13.8, not 230")
S61 = held(GC, "The paper's separate \"reproductive ceiling\" (s6.1: Σs ≤ 1.0–2.0) gives 100–200 loci at s = 0.01")
HALF = held(R4G1, "Additive-fitness halving at n·s·p̄ = 1, i.e. n = 200 at p̄ = 0.5.")
REQ = held(GC, "20e6/157,000 = 127; 205e6/157,000 = 1,306.")
R20 = 2.0e7; held(PY, "day_2025: {value: 2.0e7, source: Z18165980")       # divergence.required_fixations.day_2025
R205 = 2.05e8; held(PY, "day_2026: {value: 2.05e8")                       # divergence.required_fixations.day_2026
S, T, C, N_PAPER, N_POP = 0.01, 300_000, 230, 157_000, 10_000

# ---- transit time and the product ---------------------------------------------------------------------
logit = lambda p: math.log(p / (1 - p))
t_tr = (logit(0.9) - logit(0.1)) / S                              # exact logistic time 0.1 -> 0.9
near(t_tr, (2 / S) * math.log(9), 1e-9)
near(t_tr, 439.4, 0.05); assert round(t_tr, -1) == 440
periods = T / 440
near(periods, 681.8, 0.05)
cap_product = periods * C
near(cap_product, 156_818, 0.5); assert round(cap_product, -3) == N_PAPER
near(T / t_tr * C, 157_016, 1)                                   # with the unrounded 439.4

# ---- 230 is the n = 157,000 read back -------------------------------------------------------------------
c_back = N_PAPER * 440 / T
near(c_back, 230.27, 0.005); assert round(c_back) == C            # the C that reproduces 157,000
near(N_PAPER * t_tr / T, 229.98, 0.005)                          # with 439.4

# ---- the paper's own criterion, applied to n loci -----------------------------------------------------------
Z = 3.72
near(statistics.NormalDist().inv_cdf(1 - 1 / N_POP), Z, 0.0015)   # 1 - 1/N normal quantile 3.719
avail = lambda n: 2 * Z * math.sqrt(n / 4) * S                    # additive best-minus-worst differential
need = lambda n: n * S
n_max = Z ** 2
near(n_max, 13.84, 0.005)
near(avail(n_max), need(n_max), 1e-12)                            # equality at n = z^2
assert avail(13) >= need(13) and avail(14) < need(14)             # criterion holds to n = 13 only
assert avail(C) < need(C)                                         # it fails at 230: 0.564 against 2.3
near(avail(C), 0.5642, 5e-4)
near(C / n_max, 16.6, 0.05)                                       # 230 is 16.6x the criterion's bound

# ---- near candidates and the other requirements ----------------------------------------------------------
near(1 / (S * 0.5), 200, 1e-9)                                    # additive halving n s p = 1 at p = 0.5
assert (1.0 / S, 2.0 / S) == (100, 200)                           # s6.1 ceiling: sum s <= 1.0-2.0
near(R20 / N_PAPER, 127.4, 0.05); assert round(R20 / N_PAPER) == 127
near(R205 / N_PAPER, 1305.7, 0.05); assert round(R205 / N_PAPER) == 1306

finish({
    "object": "M-708",
    "inputs": [
        {"name": "s, T, C, n", "value": [S, T, C, N_PAPER], "cite": "Gc q1-q3 = Q25-Q27 (Z18167588 abstract, s7.8)"},
        {"name": "z at N = 10,000", "value": Z, "cite": "Gc formal statement (paper +-3.72 sigma); M-701"},
        {"name": "requirements elsewhere", "value": [R20, R205], "cite": "parameters divergence.required_fixations.day_2025, day_2026"},
    ],
    "values": {
        "t_transit": round(t_tr, 2), "transit_periods_at_440": round(periods, 2), "max_fixations": round(cap_product),
        "C_reproducing_157000": round(c_back, 2),
        "own_criterion": {"n_max_z2": round(n_max, 3), "available_at_230": round(avail(C), 4), "required_at_230": need(C),
                          "230_over_n_max": round(C / n_max, 2)},
        "near_candidates": {"additive_halving": 200, "s6.1_ceiling": [100, 200]},
        "requirement_ratios": {"20e6/157000": round(R20 / N_PAPER, 1), "205e6/157000": round(R205 / N_PAPER, 1)},
    },
    "positions": {
        "day": {"reading": "working backward from the constraint, the active zone sustains 200-300 sweeps; 230 x 681.8 matches",
                "holds": "the product 156,818 reproduces 157,000; 230 sits inside the stated 200-300"},
        "critic": {"reading": "230 is the constant that makes the product 157,000, so the match is circular",
                   "holds": "157,000 x 440 / 300,000 = 230.3; the paper's own criterion gives n <= 13.8"},
    },
    "notes": "No derivation of 230 is printed; the record shows it equals the paper's n = 157,000 read back through "
             "T / t_transit, so the 'appears to match the requirement' is circular if 230 was fitted (Gc non-sequitur). "
             "The paper's own s3 criterion applied to n loci bounds n at z^2 = 13.8 (it fails at 230: 0.56 against 2.3). "
             "The 200 (additive halving) and 100-200 (s6.1) are different constraints that land near 230. The "
             "requirement used elsewhere is 20e6 (127x) or 205e6 (1,306x), not 157,000.",
})
