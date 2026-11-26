#!/usr/bin/env python3
"""M-212 record: expected neutral fixations on the human lineage as supply x P_fix x generations.

Object: docs/research/math/objects.yaml M-212 (formula, derivation). One product, eight versions:
McCarthy 22.5M (20M time-adjusted), Mansfield 1 per generation, Hancock 76.8 per generation,
Nesslig20 37.8M, Dumb-and-Dumber/justatest90 9.7M, the relayed 7.2M, Hossjer's d x mu 7.6M, and Day's
corrected 8.25. Each is recomputed from its own stated inputs and set against the requirement it is
compared with (17.5M SNV per lineage, 20M). Day's 8.25 is also checked against the k/mu the same post
states (M-209). Genome-size and lineage factors are M-213. Inputs carry their claim file and quote
number; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-212.py [--write]
Without --write it checks that M-212.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
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


# ---- inputs -------------------------------------------------------------------------------
B5A = CL + "B5a-mccarthy-22-5-million.md"
MC1 = held(B5A, "50,000 x 9 million = 450 billion new mutations altogether.")
MC2 = held(B5A, "450 billion x 1/20,000 = 22.5 million fixed mutations.")
MC3 = held(B5A, "400 billion x 1/20,000 =20 million fixations.")
MC_IN = held(B5A, "100 × 10,000 / 20 y = 50,000 new mutations per year")
B5B = CL + "B5b-mansfield-one-fixation-per-generation.md"
MA1 = held(B5B, "then in a population of size N there are about 2*N new neutral alleles introduced each generation.")
MA2 = held(B5B, "So, the expectation is that there will be on average 1 neutral fixation every generation if just 2% of new mutations are neutral.")
B5C = CL + "B5c-hancock-76-8-per-generation.md"
HA1 = held(B5C, "that's about 76.8 uh new mutations that are fixed in the population every single generation.")
HA4 = held(B5C, "we'll say about 38 million.")
B5E = CL + "B5e-nesslig20-37-8-million.md"
NE1 = held(B5E, "Let’s assume a conservative neutral mutation rate of [ μ_G = 75 ]. That means [ k = 75 ] mutations will fix per generation.")
NE2 = held(B5E, "So, the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million based on this rough calculation.")
B5F = CL + "B5f-reddit-9-7-million-haploid.md"
DD = held(B5F, "or about 9.7 million over its proposed 252,000 generations.")
JT = held(B5F, "The gap is under a factor of two (much of which is solved with the CHLCA point above), not a factor of 91,600.")
REQ175 = held(B5F, "states the SNV-only requirement of 17.5M")
B5D = CL + "B5d-relayed-7-2-million.md"
RL = held(B5D, "Under neutrality, 6 million years divided by 25 generations um or 25 year generation times 30 mutations per "
               "generation is equal to 7.2 million differences.")
DAY30 = held(B5D, "The population geneticist on call confused mutations with fixations. 30 mutations cannot fixate per generation.")
B5H = CL + "B5h-hossjer-neutral-d-mu-7-6-million.md"
HO = held(B5H, "which still is less than 20 million, but only by a factor of 2.")
HO_IN = held(B5H, "3×10⁹ × 0.45 × 1.25×10⁻⁸ × 450,000 = 7.6M")
B3E = CL + "B3e-corrected-calculation-8-25-fixations.md"
DY1 = held(B3E, "Expected fixations: 132 billion × 1/16,000,000,000 = 8.25 fixations")
DY2 = held(B3E, "Thus the shortfall increases from 133x to 2,424,242x when we go from the theoretical to the actual.")
DY_IN = held(B3E, "Nₑ = 3,300 (\"actual ancient effective population size\"), N = 8×10⁹, 100 mutations per individual, 400,000 generations")

R20, R175 = 20e6, 17.5e6

# ---- McCarthy -------------------------------------------------------------------------------
per_year = 100 * 10_000 / 20
assert per_year == 50_000
total = per_year * 9e6
assert total == 4.5e11
mc = total / 20_000
assert mc == 22.5e6
assert 4.0e11 / 20_000 == 20e6                          # time-adjusted: last 50,000 generations removed
assert (450_000 - 50_000) * 50 == 20e6                  # same, per generation x 50 fixed per generation
mc_day_corr = (450_000 - 40_000) * 50                   # Day's own T - 4Ne with 4Ne = 40,000
assert mc_day_corr == 20.5e6

# ---- Mansfield ------------------------------------------------------------------------------
N = 10_000                                              # any N: 2N x 1/(2N) = 1
assert 2 * N * (1 / (2 * N)) == 1
near(R20 / 450_000, 44.44, 0.01)                        # 1 per generation x 450,000 against 20M
near(R175 / 252_000, 69.44, 0.01)                       # against 17.5M over 252,000
near(R20 / (450_000 * 50), 0.889, 0.001)                # neutral fraction needed (of 100) for 20M

# ---- Hancock --------------------------------------------------------------------------------
ha = 6.4e9 * 1.2e-8
near(ha, 76.8, 1e-9)
ha_total = 2 * ha * 252_000
near(ha_total, 38.71e6, 0.01e6)                         # "about 38 million" needs the x2 lineages

# ---- Nesslig20 ------------------------------------------------------------------------------
ns = 2 * 75 * 252_000
assert ns == 37.8e6

# ---- Dumb-and-Dumber / justatest90 ------------------------------------------------------------
dd = 3.2e9 * 1.2e-8 * 252_000
near(dd, 9.677e6, 0.001e6)
assert round(dd / 1e5) / 10 == 9.7
near(R175 / dd, 1.808, 0.001)                           # "under a factor of two"
near(91_600 / (R175 / dd), 50_660, 10)                  # Day's SNV shortfall is ~5e4x this ratio

# ---- relayed 7.2M -----------------------------------------------------------------------------
rl = 6e6 / 25 * 30
assert rl == 7.2e6
near(R175 / rl, 2.43, 0.005)

# ---- Hossjer ------------------------------------------------------------------------------------
ho = 3e9 * 0.45 * 1.25e-8 * 450_000
near(ho, 7.594e6, 0.001e6)
near(R20 / ho, 2.634, 0.001)                            # quote says "only by a factor of 2"
ho_nod = 3e9 * 1.25e-8 * 450_000
near(ho_nod, 16.875e6, 1)
near(R20 / ho_nod, 1.185, 0.001)                        # without d: within 1.2x

# ---- Day corrected 8.25 -------------------------------------------------------------------------
supply = 100 * 3_300
assert supply == 330_000
muts = supply * 400_000
assert muts == 1.32e11
day = muts / (2 * 8e9)
assert day == 8.25
near(R20 / day, 2_424_242.4, 0.1)
near(R20 / 150_000, 133.3, 0.05)                        # "133x" from 150,000 (input not recomputed here)
k_over_mu_used = 3_300 / 8e9                            # supply in Ne, P_fix in census N
near(k_over_mu_used, 4.125e-7, 1e-12)
k_over_mu_post = 8e9 / 3_300                            # the same post's k = mu N/Ne (M-209)
near(k_over_mu_post, 2.424e6, 0.001e6)
near(k_over_mu_post / k_over_mu_used, 5.877e12, 0.001e12)

counts = {"mccarthy": mc, "mccarthy_time_adj": 20e6, "hancock_x2": ha_total, "nesslig20": ns,
          "dd_haploid": dd, "relayed": rl, "hossjer_d": ho, "day_corrected": day}
critic_counts = [v for k, v in counts.items() if k != "day_corrected"]
assert all(R175 / v < 2.5 for v in critic_counts) and all(R20 / v < 2.8 for v in critic_counts)

finish({
    "object": "M-212",
    "inputs": [
        {"name": "McCarthy", "value": "100 x 1e4 / 20 y x 9e6 y x 1/20,000", "cite": "B5a q1-q3; claim file B5a"},
        {"name": "Mansfield", "value": "2N neutral x 1/(2N)", "cite": "B5b q1, q2"},
        {"name": "Hancock", "value": "6.4e9 x 1.2e-8 per generation, about 38 million", "cite": "B5c q1, q4"},
        {"name": "Nesslig20", "value": "mu_G = 75, 2 x 252,000", "cite": "B5e q1, q2"},
        {"name": "Dumb-and-Dumber / justatest90", "value": "3.2e9 x 1.2e-8 x 252,000; gap under 2", "cite": "B5f q1, q3; claim file B5f"},
        {"name": "relayed", "value": "6e6/25 x 30", "cite": "B5d q1"},
        {"name": "Hossjer", "value": "3e9 x 0.45 x 1.25e-8 x 450,000", "cite": "B5h q2; claim file B5h (Eq. 3.1)"},
        {"name": "Day corrected", "value": "100 x 3,300 x 400,000 / 1.6e10", "cite": "B3e q1, q2; claim file B3e"},
        {"name": "requirements", "value": {"snv_per_lineage": R175, "mccarthy_day": R20}, "cite": "claim files B5f (17.5M, Z23003785), B5a/B3e (20M)"},
    ],
    "values": {
        "counts": {k: g(v) for k, v in counts.items()},
        "mansfield_per_gen": 1, "mansfield_short_20M_450k": g(R20 / 450_000), "mansfield_short_17.5M_252k": g(R175 / 252_000),
        "hancock_per_gen": g(ha), "ratio_17.5M_over": {k: g(R175 / v) for k, v in counts.items()},
        "hossjer_20M_ratio": g(R20 / ho), "hossjer_no_d": g(ho_nod),
        "day_shortfall": g(R20 / day), "day_k_over_mu_used": g(k_over_mu_used), "day_k_over_mu_stated_eq": g(k_over_mu_post),
    },
    "positions": {
        "day": {"count": day, "shortfall": g(R20 / day), "claim": "30 mutations cannot fixate per generation",
                "note": "8.25 uses supply in Ne and P_fix in census N (k/mu = Ne/N = 4.1e-7), the inverse of the same post's k = mu N/Ne"},
        "critic": {"counts": {k: g(v) for k, v in counts.items() if k != "day_corrected"},
                   "within_factor": g(max(R20 / v for v in critic_counts)),
                   "note": "Mansfield's 1 per generation (2% neutral) is 44-69x short; the others are within 2.8x of 17.5-20M"},
    },
    "notes": "Every stated product reproduces from its own inputs. Hancock's 38M needs x2 lineages (M-213). Hossjer's "
             "7.6M is 2.6x below 20M (the quote says 'a factor of 2'). Day's 8.25 is arithmetic-correct but uses "
             "k/mu = Ne/N, 5.9e12x below the k/mu = N/Ne his post states.",
})
