#!/usr/bin/env python3
"""M-803 record (derivation, model choice): does a cost-of-selection budget exist (Nunney 2003, Hancock, Keightley).

Object: docs/research/math/objects.yaml M-803 (model-choice, derivation). No numeric fit decides it. Held text gives
Nunney's M = 2Ku and C = C_0(M) + n C_1(M) only as structure (H2 formal statement, from the Abstract and Discussion);
the functions C_0, C_1 are not held, so the record asserts what the held numbers fix: M = 2 x 10,000 x 5e-6 = 0.1,
the K for M = 1/2 at u = 5e-6 is 50,000 (Abstract "must be 50 000 for M = 1/2"), and Nunney's reported tolerable
intervals rise as M falls (M = 10: 40/7 = 5.7 generations per locus; M = 1: 20; M = 0.1: about 300; M = 0.05,
K = 5,000: about 700), which is the "below Haldane's for M > 1/2, accelerating below" structure of H2 q1. The R4 H3
M-dependence (D about 6.5 at M = 1 up to 99-163 at M = 0.01, about 15 + 1/M at low M) is asserted against its own
printed predictions (48, 115). Hancock's intermediate-frequency reply (H2a q2) is asserted in its held form, D falls
as p0 rises (2 ln(1/p0): 9.2 at p0 = 1e-2). The positions rest on quoted sentences (H2 q3, q5; H2a q1-q3; H7 q1),
recorded both ways as M-706 and M-713 do. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-803.py [--write]
Without --write it checks that M-803.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H = CL + "H-haldane-limit.md"
H2 = CL + "H2-nunney-2003.md"
H2A = CL + "H2a-hancock-cost-of-selection-hard-selection-only.md"
H7 = CL + "H7-keightley-deleterious-load.md"
QL = "docs/research/sources/quotes-literature.md"
H3R = "research/checks/results/R4-H3-human.md"
HC2 = "research/checks/results/R4-H-C2.md"


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
H2Q1 = ("For M > 1/2, the cost of natural selection is substantially less than Haldane's estimate; however, when "
        "M < 1/2, the cost (and particularly the fixed cost) increases in an accelerating fashion as M is lowered.")
held(H2, H2Q1); held(QL, H2Q1)                                       # H2 q1 (Nunney Abstract)
H2Q3 = ("As a result, soft selection inevitably reduces or eliminates the cost of substitution. However, given "
        "directional environmental change, it is likely that hard selection will dominate the adaptive process")
held(H2, H2Q3); held(QL, H2Q3)                                       # H2 q3 (Introduction)
H2Q4 = held(H2, "This relatively large population will become extinct if the environmental change requires allelic "
                "substitution faster than about every 300 generations")                                   # H2 q4 (Discussion)
H2Q5 = held(H2, "Unfortunately, soft selection is only important when natural selection is driven by intraspecific "
                "competition.")                                                                           # H2 q5 (Discussion)
MDEF = held(H2, "M = 2Ku: the number of new mutations per generation, with K carrying capacity and u mutation rate "
                "(Nunney's definition, \"approximated by M = 2Ku\"). Cost C = C_0(M) + n C_1(M) for n loci selected "
                "simultaneously (fixed cost plus per-locus cost)")
REP = held(H2, "Reported results (Discussion): M = 10 tolerates substitutions at 7 loci every 40 generations; M = 1 a "
               "single locus every 20 generations; K = 10,000, u = 5e-6 gives M = 0.1 and extinction when substitutions "
               "come faster than about every 300 generations; K = 5,000 about every 700 generations.")
K50 = held(H2, "matches the abstract's \"must be 50 000 for M = 1/2\"")
GA1 = held(H2A, "the cost of selection is only applicable for hard selection models where selection's effect is "
                "independent of the genotypes")                                                           # H2a q1 (Hancock)
GA2 = held(H2A, "the frequency doesn't have to be very low. It could have been a neutral alil and so it could have been "
                "at intermediate frequencies, right?")                                                    # H2a q2
GA3 = held(H2A, "that's important in populations that are really small in size and most of the issues come from uh "
                "being poorly adapted to your environment.")                                              # H2a q3
H7Q1 = held(H7, "A genome-wide deleterious mutation rate of 2.2 seems higher than humans could tolerate if natural "
                "selection is “hard,” but could be tolerated if selection acts on relative fitness differences between "
                "individuals or if there is synergistic epistasis.")                                      # H7 q1 (Keightley)
R4M = held(H3R, "M-dependence reproduced in both directions: D ≈ 6.5 (M = 1), 10.5 (0.3), 17–22 (0.1), 39–52 (0.03), "
                "99–163 (0.01), i.e. ≈ 15 + 1/M at low M.")
R4P = held(H3R, "(predicted 48 and 115; observed 39–52 and 99–163)")
STAND = held(HC2, "For standing variation p0 = 1e-2 to 1e-6, diploid D = 9.2 to 27.8, i.e. 92 to 278 generations at "
                  "10% mortality.")

# ---- Nunney's M = 2Ku at his numbers (exact) ----------------------------------------------------------------
M = lambda K, u: 2 * K * u
U = Fr(5, 10**6)
assert M(10_000, U) == Fr(1, 10)                                    # K = 10,000, u = 5e-6 -> M = 0.1 (H2 q4 example)
assert M(5_000, U) == Fr(1, 20)                                     # K = 5,000 -> M = 0.05
assert Fr(1, 2) / (2 * U) == 50_000                                 # K for M = 1/2 at u = 5e-6 ("50 000")
assert M(50_000, U) == Fr(1, 2)

# ---- the reported intervals rise as M falls: the threshold structure of H2 q1 ------------------------------
reported = [(10, Fr(40, 7)), (1, 20), (Fr(1, 10), 300), (Fr(1, 20), 700)]    # (M, generations per substitution)
near(float(reported[0][1]), 5.714, 5e-4)
assert all(a[1] < b[1] for a, b in zip(reported, reported[1:]))     # monotone: lower M, slower tolerable rate
above = [g for m, g in reported if m > Fr(1, 2)]
below = [g for m, g in reported if m < Fr(1, 2)]
assert all(g < 300 for g in above)                                  # M > 1/2: faster than Haldane's 1 per 300
assert max(below) > 300 and min(below) == 300                       # M < 1/2: at or slower than 300
near(300 / float(reported[0][1]), 52.5, 1e-9); assert 300 / reported[1][1] == 15    # 52.5x and 15x Haldane's rate
assert Fr(700, 300) > Fr(1, 10) / Fr(1, 20)                         # halving M (0.1 -> 0.05) more than doubles it: 2.33x

# ---- R4 H3 M-dependence: D_eff about 15 + 1/M at low M ------------------------------------------------------
r4 = {1: (6.5, 6.5), 0.3: (10.5, 10.5), 0.1: (17, 22), 0.03: (39, 52), 0.01: (99, 163)}
ms = sorted(r4, reverse=True)
assert all(r4[a][1] < r4[b][0] for a, b in zip(ms, ms[1:]))        # D rises as M falls, no overlap between rows
for m, (lo, hi) in r4.items():
    if m <= 0.03:
        assert lo <= 15 + 1 / m <= hi                               # 48.3 in 39-52; 115 in 99-163
pred = {0.03: 2 * math.log(2 * 1000) + 1 / 0.03, 0.01: 2 * math.log(2 * 1000) + 1 / 0.01}   # 2 ln 2N + 1/M at K = 1000
near(pred[0.03], 48.5, 0.1); near(pred[0.01], 115.2, 0.1)           # the printed predictions 48 and 115
assert all(15 + 1 / m > 300 / 10 for m in (0.03, 0.01))             # low M: D above Haldane's 30 (Day-favourable)
assert all(r4[m][1] < 30 for m in (1, 0.3, 0.1))                    # M >= 0.1: D below 30 (critic-favourable)

# ---- Hancock: intermediate starting frequency lowers D --------------------------------------------------------
D = lambda p0: 2 * math.log(1 / p0)
near(D(1e-2), 9.21, 0.001); near(D(1e-2) / 0.1, 92, 0.2)             # p0 = 1e-2: 92 generations at 10%
near(D(1e-6), 27.63, 0.005)                                         # p0 = 1e-6: 27.6 (R4 H-C2 prints 27.8, 278)
near(27.8 / D(1e-6) - 1, 0.0061, 1e-4)                              # printed upper end 0.6% above 2 ln(1/p0)
assert D(0.3) < D(1e-2) < D(1e-6)                                   # higher p0, lower cost (H2a q2's direction)

finish({
    "object": "M-803",
    "inputs": [
        {"name": "M = 2Ku; C = C_0(M) + n C_1(M)", "value": "structure only (C_0, C_1 not held)", "cite": "H2 formal statement (Nunney Abstract, Discussion)"},
        {"name": "Nunney K, u and reported intervals", "value": {"K": [10_000, 5_000], "u": 5e-6, "M=10": "7 loci / 40 gen", "M=1": 20, "M=0.1": 300, "M=0.05": 700},
         "cite": "H2 formal statement; H2 q4"},
        {"name": "R4 H3 D_eff by M", "value": {str(k): list(v) for k, v in r4.items()}, "cite": "research/checks/results/R4-H3-human.md (H2 row; stage M)"},
        {"name": "standing-variation p0", "value": [1e-2, 1e-6], "cite": "research/checks/results/R4-H-C2.md; H2a q2"},
    ],
    "values": {
        "M_K1e4_u5e-6": 0.1, "M_K5e3_u5e-6": 0.05, "K_for_M_half": 50_000,
        "nunney_generations_per_substitution": {"M=10": round(40 / 7, 3), "M=1": 20, "M=0.1": 300, "M=0.05": 700},
        "speedup_vs_300": {"M=10": 52.5, "M=1": 15.0},
        "r4_15_plus_1_over_M": {"M=0.03": round(15 + 1 / 0.03, 1), "M=0.01": 115.0},
        "r4_pred_2ln2N_plus_1_over_M_K1000": {k: round(v, 1) for k, v in pred.items()},
        "D_2ln_1_over_p0": {"p0=1e-2": round(D(1e-2), 2), "p0=1e-6": round(D(1e-6), 2), "printed_upper": 27.8},
    },
    "positions": {
        "day": {"reading": "Nunney confirms hard selection imposes the cost and that directional change makes hard selection "
                           "dominate (H2 q3); soft relief is limited to intraspecific competition (H2 q5); at M = 0.1 a "
                           "population dies faster than 1 per 300 (H2 q4)",
                "holds": "at M < 1/2 the reported intervals are 300-700 and R4 H3 gives D 39-163 at M <= 0.03, above Haldane's 30"},
        "critic": {"reading": "the cost is not a general bound: it needs hard selection (H2a q1), shrinks at M > 1/2 (H2 q1) "
                              "and with standing variation (H2a q2); Keightley reads U = 2.2 as intolerable under hard "
                              "selection (H7 q1)",
                   "holds": "at M > 1/2 the reported intervals are 5.7-20 generations, 15-52x faster than 300; D falls "
                            "with p0; R4 H3 gives D 6.5-22 at M >= 0.1"},
    },
    "notes": "Model choice, not settled by arithmetic. The held numbers fix the structure of Nunney's result: M = 2Ku "
             "(0.1 at K = 1e4, u = 5e-6; M = 1/2 needs K = 50,000), tolerable intervals that rise monotonically as M "
             "falls, below 300 for M > 1/2 and at or above it below. Which side applies to ancestral humans turns on "
             "two inputs no held source gives: human M (K and per-locus beneficial u) and the hard/soft split "
             "(claim file H2a; L2 brackets h at 0.125-0.641 but h is not M). C_0(M) and C_1(M) are not held as "
             "formulas, so no threshold is computed. R4 H-C2's '9.2 to 27.8' for 2 ln(1/p0) has an upper end 0.6% "
             "above the closed form (27.63); its '278' would be 276.",
})
