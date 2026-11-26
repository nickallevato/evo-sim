#!/usr/bin/env python3
"""M-805 record (derivation): Hossjer's cost step, the three factors 127, 15,800 and 10 million.

Object: docs/research/math/objects.yaml M-805 (inference, derivation). Hossjer p.2-3 (claim file H5): F_max =
(t_div x d)/(g_len x G_f) = 9e6 x 0.45/(20 x 1,600) = 126.6, printed 127 (eq. 2.2); x 1.25e-8/1e-10 = 125 gives
15,820, printed 15,800 (eq. 2.3, his "equation (3)"); x 3e9/4.6e6 = 652.2 gives 10.3 million, printed 10 million
(eq. 2.4, his "equation (4)"). He then writes the selected count is "far less than what equation (4) predicts, perhaps
more in line with equation (3)" (HO-03 = H5 q2). The gap the statement names: no cost step is computed. Eq. (3) is a
mutation-rate scaling; Haldane's limit over the same 450,000 generations is 1,500 (675 with d), so 15,800 is 10.5
times it, and above both cost-based figures in Day's corpus (487, M-802; about 6,650, M-808). Closed forms (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-805.py [--write]
Without --write it checks that M-805.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H5 = CL + "H5-hossjer-cost-step.md"
QC = "docs/research/sources/quotes-critics.md"
PY = "docs/research/parameters.yaml"


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
H5Q1 = held(H5, "Vox Day convincingly argues that if many nucleotides at which fixation takes place have a selective "
                "advantage (so that natural selection acts on all these mutations) there is a reproductive cost of "
                "having many fixations going on in parallel.")                                            # H5 q1 (p.3)
HO03 = ("it implies that the number of fixations with a selective advantage along the supposed human lineage is far "
        "less than what equation (4) predicts, perhaps more in line with equation (3).")
held(H5, HO03); held(QC, HO03)                                       # H5 q2 = HO-03
HO06 = "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli."
held(H5, HO06); held(QC, HO06)                                       # H5 q3 = HO-06
CHAIN = held(H5, "F_max = (t_div x d)/(g_len x G_f) = 9e6 x 0.45/(20 x 1,600) = 127 (eq. 2.2); mutation-rate adjustment "
                 "x (1.25e-8/1e-10) = 15,800 (eq. 2.3, his \"equation (3)\"); genome-length adjustment x (3e9/4.6e6) = "
                 "10 million (eq. 2.4, his \"equation (4)\")")
NOSTEP = held(H5, "His cost step is not computed. The Haldane limit applied to the same window gives 450,000/300 = 1,500 "
                  "selected fixations (675 with d = 0.45; Z18168236's 487 uses 325,000 generations).")
NEUT = held(QC, "Checks: 3e9*1.25e-8=37.5; *0.45=16.9; *450,000 = 7.59e6.")                                # HO-04 note
held(PY, "day_2019: {value: 9.0e6, source: B2019-02-07")            # divergence.t_div_years.day_2019
held(PY, "day_2019: {value: 1600, source: B2019-02-07")             # ltee.gens_per_fixation.day_2019
held(PY, "day_2019: {value: 20, source: B2019-02-07")               # generation_time_years.day_2019
held(PY, "day_2019: {value: 450000, source: B2019-02-07")           # generations_available.day_2019
T_DIV, D, G_LEN, G_F = 9e6, 0.45, 20, 1_600
MU_H, MU_E, L_H, L_E = 1.25e-8, 1e-10, 3e9, 4.6e6
GENS = T_DIV / G_LEN
assert GENS == 450_000

# ---- the three factors -------------------------------------------------------------------------------
f2 = T_DIV * D / (G_LEN * G_F)
near(f2, 126.5625, 1e-9); assert round(f2) == 127                   # eq. 2.2: 126.6, printed 127
mu_x = MU_H / MU_E
near(mu_x, 125, 1e-9)
f3 = f2 * mu_x
near(f3, 15_820.3, 0.05); assert round(f3, -2) == 15_800            # eq. 2.3: 15,820, printed 15,800
near(127 * 125, 15_875, 1e-9)                                       # from the rounded 127: 15,875 (0.5% off 15,800)
len_x = L_H / L_E
near(len_x, 652.17, 0.005)
f4 = 15_800 * len_x
near(f4 / 1e6, 10.30, 0.005)                                        # eq. 2.4 from 15,800: 10.3 million
near(f3 * len_x / 1e6, 10.32, 0.005)                                # from the unrounded 15,820: 10.32 million
assert round(f4, -7) == 1e7                                         # printed "10 million"

# ---- the cost step not computed ------------------------------------------------------------------------
hal = GENS / 300
assert hal == 1_500                                                 # Haldane over 450,000 generations
near(GENS * D / 300, 675, 1e-9)                                     # with d
near(15_800 / hal, 10.53, 0.005)                                    # 15,800 is 10.5 times Haldane's own number
near(15_800 / 487, 32.4, 0.05)                                      # and 32x Haldane + d (M-802)
near(15_800 / 6_650, 2.38, 0.005)                                   # and 2.4x Term 3's ~6,650 (M-808)
near(15_800 / GENS, 0.0351, 5e-5)                                   # 0.035 substitutions per generation
near(GENS / 15_800, 28.5, 0.05)                                     # one per 28 generations against Haldane's 300
assert f3 / f2 == mu_x                                              # eq. (3) is eq. (2.2) times a rate ratio: no cost term
neutral = L_H * D * MU_H * GENS
near(neutral / 1e6, 7.59, 0.005)                                    # his neutral count (HO-04)
near(L_H * MU_H * GENS / 1e6, 16.875, 1e-6)                         # without d
near(2e7 / neutral, 2.63, 0.005); near(2e7 / f4, 1.94, 0.005); near(1 / D, 2.22, 0.005)   # the corrected gaps (H5)

finish({
    "object": "M-805",
    "inputs": [
        {"name": "t_div, d, g_len, G_f", "value": [T_DIV, D, G_LEN, G_F], "cite": "H5 formal statement (Hossjer p.2-3); parameters divergence.t_div_years.day_2019, ltee.gens_per_fixation.day_2019, generation_time_years.day_2019"},
        {"name": "mu human, mu E. coli; L human, L E. coli", "value": [MU_H, MU_E, L_H, L_E], "cite": "H5 formal statement (eq. 2.3, 2.4)"},
        {"name": "printed 127, 15,800, 10 million", "value": [127, 15_800, 1e7], "cite": "H5 formal statement; HO-03 = H5 q2"},
    ],
    "values": {
        "eq2.2_F_max": f2, "eq2.3_x125": round(f3, 1), "eq2.3_from_rounded_127": 15_875,
        "eq2.4_x652.17_from_15800": round(f4), "eq2.4_from_15820": round(f3 * len_x),
        "haldane_450k": hal, "haldane_450k_with_d": 675.0,
        "ratio_15800_to": {"haldane_1500": round(15_800 / hal, 2), "haldane_d_487": round(15_800 / 487, 1), "term3_6650": round(15_800 / 6_650, 2)},
        "rate_15800_per_generation": round(15_800 / GENS, 4),
        "neutral_eq3.1": neutral, "neutral_without_d": L_H * MU_H * GENS,
        "gaps_to_20M": {"neutral": round(2e7 / neutral, 2), "eq2.4": round(2e7 / f4, 2), "1/d": round(1 / D, 2)},
    },
    "positions": {
        "day": {"reading": "ally Hossjer agrees selected fixations are far fewer than the neutral-style count (H5 q2, q3) and "
                           "that a parallel reproductive cost applies (H5 q1)",
                "holds": "the three factors reproduce (126.6, 15,820, 10.3 million); 15,800 is far less than eq. (4)"},
        "critic": {"reading": "15,800 is a rate scaling, not a cost computation, and exceeds both cost-based figures in the corpus",
                   "holds": "eq. (3) is eq. (2.2) x 125, a mutation-rate ratio; Haldane over the same window gives 1,500 "
                            "(675 with d), so 15,800 is 10.5x Haldane, 32x the 487 and 2.4x Term 3's ~6,650"},
    },
    "notes": "The arithmetic of the chain holds within rounding: 126.6 (127), 15,820 (15,800; 15,875 from the rounded "
             "127), 10.3 million (10 million). No step links eq. (3) to the cost of selection: the factor 125 is a "
             "mutation-rate ratio, and a cost-based count over 450,000 generations is 1,500 at 1/300 (675 with d). "
             "'Perhaps more in line with equation (3)' therefore has no derivation; at 0.035 per generation it would "
             "need about one selected fixation per 28 generations. H5's derived line cites Term 3 as 'about 6,690', "
             "while H1 and H8 give 6,650; M-808 asserts the closed form 6,652 (6,690 is the rounded 8.3e-12).",
})
