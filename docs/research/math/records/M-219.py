#!/usr/bin/env python3
"""M-219 record: pairwise human-chimp divergence D = 2 mu T + theta_anc, theta = 4 Ne mu per site.

Object: docs/research/math/objects.yaml M-219 (formula, derivation). The record recomputes Day's
ancestral term 4 x 1e4 x 1.2e-8 x 3e9 = 1.44M and "0.35% of 410M" (B6a), sets it against the empty-pipe
removal in IR's own table (1.2M per lineage, 2.4M only for two lineages) and checks "less than half"
and "the net adjustment still reduces the expected count". It then computes D under the critic reading
(2 mu T + theta_anc, B4a) for the Ne values in play against CSAC's 1.23% total and 1.06% fixed, and the
2019 15M + 15M against CSAC's fixed share (Camestros, B6b). Inputs carry their quote id, claim file or
parameters.yaml key; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-219.py [--write]
Without --write it checks that M-219.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QD = "docs/research/sources/quotes-day.md"
QL = "docs/research/sources/quotes-literature.md"
PY = "docs/research/parameters.yaml"
B6A = CL + "B6a-day-ancestral-polymorphism-rounding-error.md"
B4A = CL + "B4a-two-lineage-divergence-with-ils.md"


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
DAY = held(B6A, "At Nₑ = 10,000 and μ = 1.2 × 10⁻⁸, this yields approximately 1.44 million differences across the "
                "genome, less than half of the 2.4 million fixations the empty-pipe correction removes from the naive "
                "prediction. The net adjustment still reduces the expected count.")
ROUND = held(B6A, "The ancestral polymorphism objection is not merely trivial. It is a rounding error.")
Q37 = held(B4A, "Under coalescent theory, the expected pairwise divergence contributed by ancestral polymorphism is θ = 4Nₑμ per site.")
TWO = held(B4A, "where D is the number of neutral differences and the factor of 2 accounts for both lineages.")
CSAC_T = held(QL, "t 1 is constant across loci (,6-7 million years38), t 2 is a random variable that fluctuates across "
                  "loci (with a mean that depends on population size and here may be on the order of 1-2 million years39)")
CSAC_D = held(QL, "Single-nucleotide substitutions occur at a mean rate of 1.23% between copies of the human and chimpanzee "
                  "genome, with 1.06% or less corresponding to fixed divergence between the species.")
CSAC_P = held(QL, "The differences between one copy of the human genome and one copy of the chimpanzee genome include both "
                  "the sites of fixed divergence between the species and some polymorphic sites within each species.")
CAM = held(CL + "B6b-camestros-all-differences-post-split.md",
           "So Day is treating ALL the genetic differences between chimps and humans as mutations that initially only "
           "occurred after the point of divergence of the two species.")
Q05 = held(QD, "it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another "
               "15,000,000 mutations to become fixed in the chimpanzee population")
PY_410 = held(PY, "day_2026: {value: 2.05e8, derived: \"410e6 bp / 2 lineages\"")
PY_YOO = held(PY, "yoo_2025_HCG: {value: 1.32e5")

MU, T, L3, L32 = 1.2e-8, 252_000, 3e9, 3.2e9

# ---- Day: the ancestral term and the empty-pipe removal -----------------------------------------
theta = 4 * 1e4 * MU
near(theta, 4.8e-4, 1e-15)
anc = theta * L3
near(anc, 1.44e6, 1e-6)
near(anc / 410e6, 0.00351, 0.00001)                     # "0.35%" of 410M ("rounding error")
near(anc / 35e6, 0.0411, 0.0001)                        # 4.1% of the SNV-only 35M
removal_1 = 30 * 4 * 1e4                                # IR table: mu L x 4Ne, one lineage
assert removal_1 == 1.2e6
removal_2 = 2 * removal_1
assert removal_2 == 2.4e6                               # Day's 2.4M is two lineages
near(anc / removal_2, 0.6, 1e-12)                       # "less than half" of 2.4M: false (0.6)
near(anc / removal_1, 1.2, 1e-12)                       # against the per-lineage removal: theta exceeds it
net_per_lineage = anc - removal_1
assert net_per_lineage == 240_000                       # sign of "net adjustment reduces" reverses per lineage
near(2 * 30 * T / 1e6, 15.12, 1e-9)                    # if 2.4M is two lineages, the base is pairwise 2 mu L T

# ---- critic: D = 2 mu T + theta_anc against CSAC --------------------------------------------------
two_mu_t = 2 * MU * T
near(two_mu_t, 6.048e-3, 1e-9)
D = {ne: two_mu_t + 4 * ne * MU for ne in (1e4, 1.32e5, 1.98e5)}
near(D[1e4], 0.006528, 1e-6)
near(D[1.32e5], 0.012384, 1e-6)
near(D[1.98e5], 0.015552, 1e-6)
obs, fixed_max = 0.0123, 0.0106
assert D[1e4] < fixed_max < obs < D[1.32e5]             # Yoo HCG Ne brackets the observed total
T_needed = (obs - 4 * 1e4 * MU) / (2 * MU)
near(T_needed, 492_500, 1)                              # with Ne = 1e4 the split must be ~12.3 My at 25 y
near(T_needed * 25 / 1e6, 12.31, 0.01)
anc_sites = {ne: 4 * ne * MU * L32 for ne in (1.32e5, 1.98e5)}
near(anc_sites[1.32e5], 20.3e6, 0.05e6)
near(anc_sites[1.98e5], 30.4e6, 0.05e6)

# ---- Camestros / Day 2019: all 30M as post-split fixations -----------------------------------------
assert 15e6 + 15e6 == 30e6
fixed_total = (35e6 * 0.78, 35e6 * 0.86)
near(fixed_total[0], 27.3e6, 1)
near(fixed_total[1], 30.1e6, 1)

finish({
    "object": "M-219",
    "inputs": [
        {"name": "Day ancestral term and 2.4M removal", "cite": "B6a q1, q2 (Z22903977 s3)"},
        {"name": "theta = 4 Ne mu; factor 2 for two lineages", "cite": "Q37 (B4a q3), B4a q2"},
        {"name": "CSAC t1, t2; 1.23% total, 1.06% fixed; differences include polymorphism", "cite": "B4a q1, B6 q2; quotes-literature CSAC2005; parameters divergence.snv_divergence_fraction"},
        {"name": "Camestros; Day 2019 15M + 15M", "cite": "B6b q1; Q05 (B6b q2)"},
        {"name": "mu, T, L", "value": [MU, T, L3, L32], "cite": "parameters mutation.mu_per_site_per_gen.pedigree_human, generations_available.day_2026; B6a (3e9), B4a (3.2e9)"},
        {"name": "Ne values", "value": [1e4, 1.32e5, 1.98e5], "cite": "parameters population.Ne_modern_human, Ne_ancestral_hc.yoo_2025_HCG/HCB"},
    ],
    "values": {
        "theta_1e4": theta, "ancestral_sites": anc, "share_of_410M": g(anc / 410e6), "share_of_35M": g(anc / 35e6),
        "removal_per_lineage": removal_1, "removal_two_lineages": removal_2,
        "anc_over_removal": {"two_lineages": 0.6, "per_lineage": 1.2}, "net_per_lineage": net_per_lineage,
        "D_by_Ne": {str(k): g(v) for k, v in D.items()}, "T_needed_Ne_1e4": g(T_needed),
        "anc_sites_yoo": {str(k): g(v) for k, v in anc_sites.items()},
    },
    "positions": {
        "day": {"ancestral_term": anc, "share_of_410M": g(anc / 410e6), "stated_less_than_half_of_2.4M": False,
                "note": "1.44M / 2.4M = 0.6; against the per-lineage 1.2M the term is 1.2x the removal, so the net is +0.24M"},
        "critic": {"reading": "pairwise D = 2 mu T + theta_anc; the empty-pipe term does not reduce D",
                   "D_by_Ne": {str(k): g(v) for k, v in D.items()}, "observed": obs, "fixed_max": fixed_max},
    },
    "notes": "1.44M and 0.35% reproduce. 'Less than half of 2.4M' is false (0.6), and against IR's own per-lineage "
             "removal (1.2M) the ancestral term is larger, reversing the stated sign. With Ne = 1e4, D = 0.65% "
             "against 1.23% observed (a fit needs 12.3 My); with Yoo's ancestral Ne, 1.24-1.56%.",
})
