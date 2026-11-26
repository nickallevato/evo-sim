#!/usr/bin/env python3
"""M-304 record (model-choice): identifiability of d in the Bio-Cycle fits.

Object: docs/research/math/objects.yaml M-304 (model-choice, derivation). Day's recursion
p' = p + s p q/(1 + s p) multiplies the odds by (1 + s) per step, so after d G steps
logit(p) = logit(p0) + d G ln(1 + s): a trajectory fixes d ln(1 + s), not d. The record computes:
(i) the three human loci (Z18203514 Table 1 inputs, claim file C2): required d, Table 1's predictions,
    and d under s -/+ 25% (Day's 0.56 / 0.36, Z18202768) by the exact recursion and in the weak limit;
(ii) the C2c ratio of required s between SLC45A2 and TYR across d (Day's Table 3 against the recursion);
(iii) the chicken TSHR (C2d): required d under the additive and recessive recursions over Loog's CI for s,
    and the predicted final frequencies at d = 1 and d = 0.45, against Day's d = 1.02.
Each side's numbers are computed side by side; the record chooses neither. Inputs carry their quote
id or claim file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-304.py [--write]
Without --write it checks that M-304.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
C2, C2C, C2D = CL + "C2-bio-cycle-d.md", CL + "C2c-ratio-crossvalidation.md", CL + "C2d-chicken-tshr.md"


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


def logit(p):
    return math.log(p / (1 - p))


def additive(s):
    return lambda p: p + s * p * (1 - p) / (1 + s * p)


def recessive(s):
    return lambda p: p + s * p * p * (1 - p) / (1 + s * p * p)


def run(step, p0, n):
    p = p0
    for _ in range(n):
        p = step(p)
    return p


def steps_to(step, p0, pf):
    """Steps (fractional in the last one, linear) for the recursion to go from p0 to pf."""
    p, n = p0, 0
    while True:
        q = step(p)
        if q >= pf:
            return n + (pf - p) / (q - p)
        p, n = q, n + 1


def d_exact(p0, pf, G, s):
    """Required d for the additive recursion: d G ln(1 + s) = logit(pf) - logit(p0) (exact)."""
    return (logit(pf) - logit(p0)) / (G * math.log1p(s))


def s_exact(p0, pf, G, d):
    return math.expm1((logit(pf) - logit(p0)) / (d * G))


# ---- inputs -------------------------------------------------------------------------------
Q2 = held(C2, "The effective number of generations is: g_{eff} = g_{nominal} × d")
Q3 = held(C2, "All three loci independently converge on d ≈ 0.45, consistent with Neolithic/Bronze Age demographic structure.")
Q4 = held(C2, "Under base-case parameters, the three loci yield optimal d values of 0.49 (Lactase), 0.49 (SLC45A2), and "
              "0.38 (TYR), with a mean of 0.45. When selection coefficients are reduced by 25%, the mean optimal d "
              "increases to 0.56 (range 0.51–0.59); when increased by 25%, the mean decreases to 0.36 (range 0.31–0.39).")
Q5 = held(C2, "The persistence allele was virtually absent in early Neolithic Europeans 6,000 years ago (less than 1 "
              "percent frequency). Today, about 75 percent of Northern Europeans carry it.")
Q6 = held(C2, "Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2.")
TAB1 = held(C2, "LCT s = 0.05, p0 < 1% (we use 0.01), 6,000 BP; SLC45A2 s = 0.05, p0 = 0.43, 4,000 BP; TYR s = 0.03, "
                "p0 = 0.25, 5,000 BP; generation length not stated in the paper; 25 y/gen reproduces the table exactly.")
PRED = held(C2, "Kimura 99.92% / 99.95% / 99.19% (paper 99.9 / 99.9 / 99.3); Bio-Cycle 66.2% / 96.2% / 82.7% (paper "
                "66.2 / 96.2 / 82.7). Holds.")
ERR = held(C2, "LCT (24.9-8.8)/24.9 = 64.7%; SLC45A2 (2.9-0.8)/2.9 = 72.4%; TYR (23.3-6.7)/23.3 = 71.2%")
TAB4 = held(C2, "do not match Z18203514 Table 4 (0.46, 0.43, 0.46)")
SREQ = held(C2, "Required s at d = 0.45: 0.054, 0.054, 0.025 versus paper 0.048, 0.050, 0.023")
C2CQ = held(C2C, "The ratio remains constant at ~0.49 across all d values. This confirms that the generation overlap "
                 "correction is capturing real population dynamics")
TAB3 = held(C2C, "Table 3 (paper): required s for the observed frequencies at d = 0.40, 0.50, 0.60, 1.00: SLC45A2 0.058, "
                 "0.047, 0.038, 0.023; TYR 0.028, 0.023, 0.019, 0.011; ratio 0.48, 0.49, 0.49, 0.49.")
C2DQ1 = held(C2D, "Inverting the calculation, we find that the chicken data require d ≈ 1.02—essentially unity (Table 4).")
C2DQ3 = held(C2D, "Loog et al. report an ancestral frequency of 0.44, with the derived allele reaching near-fixation (0.97) "
                  "in modern populations over approximately 900 years (~900 chicken generations).")
C2DQ3B = held(C2D, "Under the Bio-Cycle model with d = 0.45, the predicted final frequency would be only ~0.68-0.72—"
                   "inconsistent with observation by nearly 30 percentage points.")
LOOG = held(C2D, "s = 0.0049 (Loog 2017, 95% CI 0.0029-0.0088), the TSHR derived allele is recessive")

d_param = 0.45                                           # parameters selection.turnover_d
LOCI = {"LCT": (0.01, 240, 0.05), "SLC45A2": (0.43, 160, 0.05), "TYR": (0.25, 200, 0.03)}  # p0, G (25 y), s
assert [6_000 / 25, 4_000 / 25, 5_000 / 25] == [240, 160, 200]

# ---- (i) human loci -------------------------------------------------------------------------
# observed final frequency = Kimura prediction - its error; the Bio-Cycle absolute error agrees (Table 1)
obs = {}
for name, bio, e_bio, kim, e_kim in (("LCT", 66.2, 8.8, 99.9, 24.9), ("SLC45A2", 96.2, 0.8, 99.9, 2.9),
                                     ("TYR", 82.7, 6.7, 99.3, 23.3)):
    obs[name] = round(kim - e_kim, 1) / 100
    near(abs(bio - 100 * obs[name]), e_bio, 1e-9)        # TYR: Bio-Cycle overshoots (82.7 vs 76.0)
assert obs == {"LCT": 0.75, "SLC45A2": 0.97, "TYR": 0.76}

pred_bio, pred_kim, d_req = {}, {}, {}
for name, (p0, G, s) in LOCI.items():
    pred_bio[name] = run(additive(s), p0, round(d_param * G))
    pred_kim[name] = run(additive(s), p0, G)
    d_req[name] = d_exact(p0, obs[name], G, s)
    near(steps_to(additive(s), p0, obs[name]) / G, d_req[name], 0.005)   # recursion and closed form agree
for name, printed in (("LCT", 66.2), ("SLC45A2", 96.2), ("TYR", 82.7)):
    near(100 * pred_bio[name], printed, 0.05)            # Table 1 Bio-Cycle column reproduces
for name, printed in (("LCT", 99.92), ("SLC45A2", 99.95), ("TYR", 99.19)):
    near(100 * pred_kim[name], printed, 0.005)
for name, printed in (("LCT", 0.486), ("SLC45A2", 0.481), ("TYR", 0.381)):
    near(d_req[name], printed, 0.0005)
mean_d = sum(d_req.values()) / 3
near(mean_d, 0.449, 0.0005)                              # "converge on d ≈ 0.45"; Z18202768 0.49 / 0.49 / 0.38
table4 = {"LCT": 0.46, "SLC45A2": 0.43, "TYR": 0.46}
near(table4["TYR"] - d_req["TYR"], 0.079, 0.001)         # Table 4's TYR 0.46 is 0.08 off, beyond rounding

# the product d ln(1+s) is what the trajectory fixes: rescale s, d follows
sens = {}
for f in (0.75, 1.25):
    per = {n: d_exact(p0, obs[n], G, s * f) for n, (p0, G, s) in LOCI.items()}
    sens[f] = {"per_locus": per, "mean": sum(per.values()) / 3, "weak_limit_mean": 0.45 / f}
near(sens[1.25]["mean"], 0.3615, 0.0005)                 # Day 0.36 reproduces
near(min(sens[1.25]["per_locus"].values()), 0.306, 0.001)   # Day range 0.31-0.39
near(max(sens[1.25]["per_locus"].values()), 0.391, 0.001)
near(sens[0.75]["mean"], 0.596, 0.001)                   # Day prints 0.56
near(sens[0.75]["mean"] - 0.56, 0.036, 0.001)            # gap 0.036 (6.4%)
near(min(sens[0.75]["per_locus"].values()), 0.506, 0.001)   # Day range 0.51-0.59: the low end reproduces
near(max(sens[0.75]["per_locus"].values()), 0.644, 0.001)   # the high end is 0.64, not 0.59
near(sens[0.75]["weak_limit_mean"], 0.60, 1e-12)
near(sens[1.25]["weak_limit_mean"], 0.36, 1e-12)

# required s at d = 1 (Table 2) and d = 0.45
s_d1 = {n: s_exact(p0, obs[n], G, 1.0) for n, (p0, G, s) in LOCI.items()}
for n, printed in (("LCT", 0.0240), ("SLC45A2", 0.0238), ("TYR", 0.0113)):
    near(s_d1[n], printed, 0.00005)
s_d45 = {n: s_exact(p0, obs[n], G, 0.45) for n, (p0, G, s) in LOCI.items()}
for n, printed in (("LCT", 0.054), ("SLC45A2", 0.054), ("TYR", 0.025)):
    near(s_d45[n], printed, 0.0005)                      # paper 0.048 / 0.050 / 0.023, about 10% lower

# carrier reading of Q5: 75% carriers of a dominant allele is allele frequency 0.5, not 0.75
p_carrier = 1 - math.sqrt(1 - 0.75)
near(p_carrier, 0.5, 1e-12)
d_lct_carrier = d_exact(0.01, p_carrier, 240, 0.05)
near(d_lct_carrier, 0.392, 0.001)

# ---- (ii) the C2c ratio is constant for any d -----------------------------------------------
ratio = {}
for d in (0.2, 0.4, 0.5, 0.6, 1.0, 2.0):
    sl = s_exact(LOCI["SLC45A2"][0], obs["SLC45A2"], LOCI["SLC45A2"][1], d)
    ty = s_exact(LOCI["TYR"][0], obs["TYR"], LOCI["TYR"][1], d)
    ratio[d] = ty / sl
assert all(0.4645 <= r <= 0.4779 for r in ratio.values())   # R4 C2c: 0.4646-0.4778 over d in [0.2, 2]
weak = (logit(0.76) - logit(0.25)) / 200 / ((logit(0.97) - logit(0.43)) / 160)
near(weak, 0.4793, 0.0005)                               # weak-selection limit: independent of d
paper = {0.40: (0.058, 0.028), 0.50: (0.047, 0.023), 0.60: (0.038, 0.019), 1.00: (0.023, 0.011)}
paper_ratio = {d: ty / sl for d, (sl, ty) in paper.items()}
for d, printed in ((0.40, 0.483), (0.50, 0.489), (0.60, 0.500), (1.00, 0.478)):
    near(paper_ratio[d], printed, 0.0005)                # from Table 3's rounded s
for d, (sl, ty) in paper.items():                        # s x d constant within 3-4% (claim file C2c)
    near(sl * d, 0.0232, 0.0005)
    near(ty * d, 0.0112, 0.0003)

# ---- (iii) chicken TSHR -----------------------------------------------------------------
p0c, pfc, Gc = 0.44, 0.97, 900
s_ci = (0.0029, 0.0049, 0.0088)
d_add = {s: steps_to(additive(s), p0c, pfc) / Gc for s in s_ci}
d_rec = {s: steps_to(recessive(s), p0c, pfc) / Gc for s in s_ci}
for s, printed in zip(s_ci, (1.43, 0.845, 0.471)):
    near(d_add[s], printed, 0.005)
for s, printed in zip(s_ci, (1.90, 1.13, 0.63)):
    near(d_rec[s], printed, 0.005)
near(d_add[0.0049], d_exact(p0c, pfc, Gc, 0.0049), 0.002)
assert d_add[0.0049] < 1.02 < d_rec[0.0049]               # Day's 1.02 lies between the two; neither gives it
near(d_rec[0.0049] - 1.02, 0.107, 0.002)
near(1.02 - d_add[0.0049], 0.175, 0.002)
fin = {("add", 1.0): run(additive(0.0049), p0c, Gc), ("add", 0.45): run(additive(0.0049), p0c, round(0.45 * Gc)),
       ("rec", 1.0): run(recessive(0.0049), p0c, Gc), ("rec", 0.45): run(recessive(0.0049), p0c, round(0.45 * Gc))}
near(100 * fin[("add", 1.0)], 98.5, 0.05)
near(100 * fin[("add", 0.45)], 85.0, 0.05)
near(100 * fin[("rec", 1.0)], 95.0, 0.05)
near(100 * fin[("rec", 0.45)], 70.7, 0.05)               # inside Day's "~0.68-0.72"
assert 0.68 <= fin[("rec", 0.45)] <= 0.72 and not 0.68 <= fin[("add", 0.45)] <= 0.72
near(100 * (pfc - fin[("rec", 0.45)]), 26.3, 0.05)       # "nearly 30 percentage points" (recessive)
near(100 * (pfc - fin[("add", 0.45)]), 12.0, 0.05)       # 12 points under the additive recursion of the human loci

finish({
    "object": "M-304",
    "inputs": [
        {"name": "recursion and g_eff = d G", "cite": "C2 q2 (Z18203514 s2.1); claim file C2 Formal statement"},
        {"name": "human loci p0, G, s", "value": LOCI, "cite": "claim file C2 (Z18203514 Table 1; 25 y/gen)"},
        {"name": "observed final frequencies", "value": obs, "cite": "Table 1 predictions and errors (claim file C2 derived)"},
        {"name": "Day d values", "value": {"Z18202768": [0.49, 0.49, 0.38], "Z18203514_Table4": table4, "mean": 0.45,
                                           "s_minus_25": [0.56, 0.51, 0.59], "s_plus_25": [0.36, 0.31, 0.39]},
         "cite": "C2 q3, q4; claim file C2"},
        {"name": "Table 3 required s", "value": {str(k): v for k, v in paper.items()}, "cite": "C2c q1; claim file C2c"},
        {"name": "chicken", "value": {"p0": p0c, "pf": pfc, "G": Gc, "s": 0.0049, "s_ci": [0.0029, 0.0088], "Day_d": 1.02},
         "cite": "C2d q1, q3; claim file C2d (Loog 2017 via Day; not retrieved)"},
    ],
    "values": {
        "human_required_d": {k: g(v) for k, v in d_req.items()}, "human_mean_d": g(mean_d),
        "table1_bio_pct": {k: g(100 * v) for k, v in pred_bio.items()},
        "table1_kimura_pct": {k: g(100 * v) for k, v in pred_kim.items()},
        "s_minus_25pct": {"mean": g(sens[0.75]["mean"]), "range": [g(min(sens[0.75]["per_locus"].values())), g(max(sens[0.75]["per_locus"].values()))],
                          "weak_limit": 0.6, "day_printed": 0.56},
        "s_plus_25pct": {"mean": g(sens[1.25]["mean"]), "range": [g(min(sens[1.25]["per_locus"].values())), g(max(sens[1.25]["per_locus"].values()))],
                         "weak_limit": 0.36, "day_printed": 0.36},
        "required_s_d1": {k: g(v) for k, v in s_d1.items()}, "required_s_d045": {k: g(v) for k, v in s_d45.items()},
        "lct_carrier_reading": {"allele_freq": 0.5, "required_d": g(d_lct_carrier)},
        "c2c_ratio_exact": {str(k): g(v) for k, v in ratio.items()}, "c2c_ratio_weak_limit": g(weak),
        "c2c_ratio_from_table3": {str(k): g(v) for k, v in paper_ratio.items()},
        "chicken_required_d": {"additive": {str(k): g(v) for k, v in d_add.items()}, "recessive": {str(k): g(v) for k, v in d_rec.items()}},
        "chicken_final_pct": {f"{m}_d{d}": g(100 * v) for (m, d), v in fin.items()},
    },
    "positions": {
        "day": {"reading": "d is a demographic constant: three loci converge on 0.45, the ratio is constant across d, "
                           "chickens require d = 1.02",
                "mean_d": g(mean_d), "sensitivity": [0.56, 0.36], "ratio": 0.49,
                "chicken_d_printed": 1.02,
                "note": "1.02 is not reproduced from the held inputs: additive 0.845, recessive 1.13 (also tried: genic "
                        "diploid 1.69, dominant 8.0). Table 4 and its recursion are not held (Z18203514 text absent). "
                        "Day's d = 0.45 prediction 0.68-0.72 reproduces under the recessive recursion (70.7%)"},
        "critic": {"reading": "trajectories fix d ln(1+s); the ratio and the sensitivity are that identity; the chicken d "
                              "depends on dominance and on s inside its CI",
                   "d_times_ln1ps_fixed": True, "ratio_range_d_0.2_to_2": [g(min(ratio.values())), g(max(ratio.values()))],
                   "chicken_d_over_ci": {"additive": [g(d_add[0.0088]), g(d_add[0.0029])], "recessive": [g(d_rec[0.0088]), g(d_rec[0.0029])]}},
    },
    "notes": "Required d reproduces (0.486 / 0.481 / 0.381, mean 0.449) and moves as 1/ln(1+s): +25% on s gives 0.36 "
             "(Day 0.36), -25% gives 0.596 (Day prints 0.56; the weak limit is 0.60). The SLC45A2/TYR ratio of required s "
             "is 0.465-0.478 for every d in [0.2, 2], so constancy is not a test of d. The chicken required d is 0.845 "
             "(additive) or 1.13 (recessive) at s = 0.0049 and 0.47-1.90 over Loog's CI; Day's 1.02 sits between the two "
             "recursions and is not reproduced. Q5 says 75% carry the allele; read as carriers of a dominant allele that "
             "is p = 0.5, and the LCT required d drops to 0.39.",
})
