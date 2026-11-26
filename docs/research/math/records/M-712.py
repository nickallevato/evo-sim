#!/usr/bin/env python3
"""M-712 record (derivation): what a strictly serial sweep model predicts for segregating variation.

Object: docs/research/math/objects.yaml M-712 (empirical, derivation). Hancock (GG-13, G2c q1): under strictly serial
sweeps there would be basically no variation except the rising mutation. Standard theory (G2c formal statement):
under free recombination, neutral diversity at unlinked sites is set by mutation-drift balance, theta = 4 Ne mu, and
reduced by sweeps only at linked sites. Closed form: theta = 4 x 1e4 x 1.2e-8 = 4.8e-4 per site (expected
heterozygosity theta/(1 + theta) = 4.798e-4); the formula has no sweep-rate term. The size of the fitness-variance
route the R4 G2c write-up derives (P4) is re-derived in closed form: one logistic sweep contributes on average
2 s^2 <p(1-p)> = 1.0e-5 to Var(w), so Var(w) of order 10 needs about 1e6 concurrent sweeps. The simulated
heterozygosity ratios (0.97-1.03 of the no-sweep control at 1/1,322 per generation; 1.00-1.01 at about 146
concurrent sweeps; falsifier below 0.10) are quoted from R4 G2c, not re-simulated. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-712.py [--write]
Without --write it checks that M-712.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
G2C = "docs/research/claims/G2c-hancock-no-variation-prediction.md"
QC = "docs/research/sources/quotes-critics.md"
PY = "docs/research/parameters.yaml"
R4 = "research/checks/results/R4-G2c.md"


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
GG13 = "there would basically be no genetic variation amongst individuals except for the mutation that's increasing in frequency"
held(G2C, GG13)                                                   # G2c q1 = GG-13 (t=01:33:59, ASR)
assert "GG-13" in (ROOT / QC).read_text(encoding="utf-8")
THETA = held(G2C, "under free recombination, neutral diversity at unlinked sites is set by mutation-drift balance "
                  "θ = 4Neμ and is reduced by sweeps only at linked sites.")
SETUP = held(R4, "N = 10,000 diploids, s = 0.01, free recombination, 500 neutral loci, 6,000 generations, window "
                 "3,000-5,999.")
ROW_A = held(R4, "| A (1/1,322 per gen) rep0 / rep1 | 0.3425; 0.3219 | 1.030 / 0.968 |")
ROW_B = held(R4, "| B (about 230 concurrent) rep0 / rep1 | 0.3364; 0.3339 | 1.012 / 1.004 | 1.0035 / 1.0017 | 146.1 / 146.7 |")
VERD = held(R4, "Hn ratio is 0.97 to 1.03 in A (falsifier < 0.10) and 1.00 to 1.01 in B (< 0.9).")
P4 = held(R4, "Var(w) of order 10 needs about 1e6 concurrent sweeps at s = 0.01: re-derived in review (each sweep "
              "contributes 2 s^2 p(1-p) of about 1e-5).")
G2C_CHK = held(G2C, "About 146 concurrent sweeps (0.64x of Day's 230; realised rate 0.18 fixations per generation): "
                    "1.00-1.01 of control")
B2 = held(R4, "| B2 (3) | 0.981, 0.979, 0.970 |")                 # post hoc rerun at about 228 concurrent (R4 G2c)
LINKED = held(G2C, "linked sites (hitchhiking) are not covered")
NE = 1.0e4; held(PY, "Ne_modern_human: {value: 1.0e4")            # population.Ne_modern_human (= R4 G2c N)
MU = 1.2e-8; held(PY, "pedigree_human: {value: 1.2e-8")          # mutation.mu_per_site_per_gen.pedigree_human
S, GF3 = 0.01, 1_322

# ---- theta at unlinked sites ----------------------------------------------------------------------------
theta = lambda ne, mu: 4 * ne * mu                                # no sweep-rate argument
theta_h = theta(NE, MU)
near(theta_h, 4.8e-4, 1e-12)
het = theta_h / (1 + theta_h)
near(het, 4.798e-4, 5e-8)
assert theta.__code__.co_varnames == ("ne", "mu")

# ---- the fitness-variance route (R4 G2c P4), closed form ------------------------------------------------
p0 = 1 / (2 * NE)
mean_pq = (1 - 2 * p0) / (2 * math.log((1 - p0) / p0))           # time-average of p(1-p) over a logistic sweep
near(mean_pq, 0.0505, 5e-4)
per_sweep = 2 * S ** 2 * mean_pq
near(per_sweep, 1.01e-5, 0.01e-5)                                 # "about 1e-5"
need = 10 / per_sweep
near(need / 1e6, 0.99, 0.01)                                      # about 1e6 concurrent sweeps for Var(w) ~ 10

# ---- the simulated ratios (quoted, not rerun) -------------------------------------------------------------
ratios_a, ratios_b = (1.030, 0.968), (1.012, 1.004)
assert "1.030 / 0.968" in ROW_A and "1.012 / 1.004" in ROW_B
assert round(min(ratios_a), 2) == 0.97 and round(max(ratios_a), 2) == 1.03
assert round(min(ratios_b), 2) == 1.00 and round(max(ratios_b), 2) == 1.01
assert min(ratios_a + ratios_b) > 0.9                             # at least 9x Hancock's falsifier (< 0.10)
near(1 / GF3, 7.56e-4, 0.005e-4)                                  # sweep rate in A
near(146.1 / 230, 0.635, 0.001); near(146.7 / 230, 0.638, 0.001)   # 0.64x of Day's 230

finish({
    "object": "M-712",
    "inputs": [
        {"name": "Ne, mu", "value": [NE, MU], "cite": "parameters population.Ne_modern_human, mutation.mu_per_site_per_gen.pedigree_human"},
        {"name": "theta", "value": "4 Ne mu", "cite": "G2c formal statement"},
        {"name": "simulated Hn ratios", "value": {"A_1/1322": list(ratios_a), "B_146_concurrent": list(ratios_b)},
         "cite": "R4 G2c Results table and verdict line (quoted, not re-simulated)"},
    ],
    "values": {
        "theta_per_site": theta_h, "expected_heterozygosity": round(het, 9),
        "fitness_variance_route": {"mean_pq_over_sweep": round(mean_pq, 5), "var_w_per_sweep": f"{per_sweep:.3e}",
                                   "sweeps_for_var_w_10": round(need)},
        "Hn_ratio_ranges": {"A": [0.97, 1.03], "B": [1.00, 1.01]}, "falsifier": 0.10,
        "concurrency_vs_230": [round(146.1 / 230, 3), round(146.7 / 230, 3)],
    },
    "positions": {
        "day": {"reading": "MITTENS models parallel fixation, so a strictly serial premise does not describe it",
                "holds": "neither 1/1,322 per generation nor ~146 concurrent sweeps erodes unlinked diversity (0.97-1.03)"},
        "critic": {"reading": "a strictly serial sweep model predicts almost no standing variation",
                   "holds": "true by construction of a strictly serial model; unlinked diversity is set by theta = 4 Ne mu"},
    },
    "notes": "theta = 4 Ne mu has no sweep-rate term, so unlinked neutral diversity is not removed by sweeps; only linked "
             "sites (hitchhiking, not in R4 G2c) are. The fitness-variance route would need about 1e6 concurrent sweeps "
             "for Var(w) of order 10 (closed form here; R4 G2c P4). The ratios are simulation results quoted from R4 "
             "G2c: 0.97-1.03 (A) and 1.00-1.01 (B, 146 concurrent, 0.64x of 230); the post hoc B2 rerun at about 228 "
             "concurrent gave 0.970-0.981. The conditional is correct for a strictly serial model, which neither side's "
             "stated model is.",
})
