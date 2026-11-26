#!/usr/bin/env python3
"""M-912 record (derivation): Jukes-Cantor (JC69) divergence of two lineages in Paul Rimmer's one-child-per-parent model.

Object: docs/research/math/objects.yaml M-912 (formula, derivation). Source: PR-1 (Paul, Substack, 2026-11-08), end
section "The Mathematical Model"; source map docs/research/math/sources/paul-rimmer-2026-11-08.md. Model: every alien
leaves exactly one child, so there is no drift, no lineage loss and no fixation; each site mutates with probability
kappa per generation to one of the other three bases. His exact answer is
    D(t) = (3L/4) [1 - (1 - 4 kappa/3)^(2 floor(t/tau))],
with early-time limit D ~ 2 L kappa t / tau (the two-lineage 2 mu t). Inputs (his): kappa = 1 per 50 million bases =
2e-8, tau = 20 y; L = 3e9 is the review's reading of "a few billion base pairs" (D/L does not depend on L). The record
asserts every number the EVOA-102 review states for this model: the derivation steps (exact rationals), the early slope
2 L kappa = 120 per generation, D/L = 1.2% at 302,426 generations (6.05 My), 1.37% at 6.9 My, 0.20/0.99/1.97% at
1/5/10 My, the E2 ratio against human pairwise diversity (parameters population.pi_human_pairwise, Zhao2000) and the
section-5 steelman count at Day's 3.0 inputs (M-001.json: 252,000 generations, F_max 190.62).

Run: research/.venv/bin/python -I docs/research/math/records/M-912.py [--write]
Without --write it checks that M-912.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
MAP = "docs/research/math/sources/paul-rimmer-2026-11-08.md"
RAW = "sources/raw/paulnottheapostle-2026-11-26/text.txt"     # gitignored; checked when present
PY = "docs/research/parameters.yaml"
M001 = "docs/research/math/records/M-001.json"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def paul(quote):
    """A quote from Paul's post: in the committed source map, and in the held fetch when this checkout has it."""
    held(MAP, quote)
    if (ROOT / RAW).exists():
        held(RAW, quote)
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
paul("Every alien leaves exactly one child, after exactly τ years, and then then dies.")
paul("around one mutation per 50 million bases, on average")
paul("These aliens reproduce asexually, every 20 years")
paul("A few billion base pairs.")
paul("So somewhere between 1 and 10 million years.")
paul("given known mutation rates, the rate equation predicts too much variation, not too little.")
paul("the population size really doesn’t matter anymore.")
paul("This looks surprisingly (or unsurprisingly?) similar to Beale’s equation.")
held(PY, "pi_human_pairwise: {value: 8.8e-4")                         # population.pi_human_pairwise (Zhao2000)
held(PY, "'a low nucleotide diversity ( approximately 0.1%) in humans'")

# ---- the derivation, exactly (rationals in kappa at a test value) ------------------------------------
k = Fr(1, 50_000_000)                                                  # kappa = 2e-8
assert k == Fr(2, 10**8)
lam = 1 - Fr(4, 3) * k                                                 # one-generation factor
p = Fr(1)                                                              # p_0 = 1
for n in range(1, 6):                                                  # recursion = closed form, n = 1..5
    p = (1 - k) * p + k / 3 * (1 - p)
    assert p == Fr(1, 4) + Fr(3, 4) * lam**n
    d_match = 1 - (p**2 + 3 * ((1 - p) / 3) ** 2)                      # 1 - P(match), independent lineages
    assert d_match == 1 - p**2 - (1 - p) ** 2 / 3
    assert d_match == Fr(3, 4) * (1 - lam ** (2 * n))                  # d_n = (3/4)[1 - (1 - 4k/3)^(2n)]
c = Fr(1, 4)
assert c == (1 - Fr(4, 3) * k) * c + k / 3                              # fixed point c = 1/4

# ---- Paul's human-like inputs -------------------------------------------------------------------------
KAP, TAU, L = 2e-8, 20, 3e9


def frac(kap, n):
    """D/L after n generations: (3/4)[1 - (1 - 4 kap/3)^(2n)], computed stably."""
    return 0.75 * -math.expm1(2 * n * math.log1p(-4 * kap / 3))


def at_years(kap, tau_y, years):
    return frac(kap, math.floor(years / tau_y))


slope = 2 * L * KAP
assert abs(slope - 120) < 1e-9                                         # 120 differences per generation
n12 = math.ceil(math.log1p(-0.012 / 0.75) / (2 * math.log1p(-4 * KAP / 3)))
assert n12 == 302_426 and frac(KAP, n12) >= 0.012 > frac(KAP, n12 - 1)  # first generation at 1.2%
t12 = n12 * TAU
assert t12 == 6_048_520                                                # 6.05 My
pct = {my: round(100 * at_years(KAP, TAU, my * 1e6), 2) for my in (1, 5, 6.9, 10)}
assert pct == {1: 0.2, 5: 0.99, 6.9: 1.37, 10: 1.97}, pct              # 0.20, 0.99, 1.37, 1.97 %
assert 1e6 < t12 < 1e7                                                 # inside "between 1 and 10 million years"
early = 2 * KAP * n12                                                  # linear 2 kappa n at the same n
near(early / frac(KAP, n12), 1.008, 0.001)                             # linear form 0.8% above exact at 1.2%

# ---- E2: within-population prediction against human pairwise diversity ----------------------------------
PI_H = 8.8e-4                                                          # Zhao2000, 0.088%
r_pi = near(0.012 / PI_H, 13.64, 0.01)                                 # about 14x the measured human value
r_01 = near(0.012 / 0.001, 12.0, 1e-9)                                 # 12x the rounded "approximately 0.1%"
assert 10 <= r_01 < r_pi < 20                                          # "roughly an order of magnitude"

# ---- E4 / section 5: the two rates, and the steelman count at Day's 3.0 inputs --------------------------
m001 = json.loads((ROOT / M001).read_text(encoding="utf-8"))["values"]["3.0"]
N30, FMAX, GF = m001["N_gen"], m001["F_max"], m001["G_f"]
assert N30 == 252_000 and round(FMAX) == 191 and round(GF) == 1322
per_lineage = L * KAP * N30                                            # mu L T, one lineage, k = mu (B5)
near(per_lineage, 1.512e7, 1)                                          # "about 1.5e7"
factor = near(per_lineage / FMAX, 79_320, 5)                           # "about 79,000"
near(slope * GF, 158_590, 5)                                           # 120 per gen against 1 per 1,322 gens

finish({
    "object": "M-912",
    "inputs": [
        {"name": "kappa", "value": KAP, "cite": "PR-1 (paul@L43): 'around one mutation per 50 million bases'"},
        {"name": "tau_years", "value": TAU, "cite": "PR-1 (paul@L43): 'every 20 years'"},
        {"name": "L", "value": L, "cite": "review reading of PR-1 'A few billion base pairs' (D/L does not depend on L)"},
        {"name": "pi_human_pairwise", "value": PI_H, "cite": "parameters population.pi_human_pairwise (Zhao2000)"},
        {"name": "MITTENS 3.0", "value": {"N_gen": N30, "F_max": FMAX, "G_f": GF}, "cite": "M-001.json values.3.0"},
    ],
    "values": {
        "derivation_exact_n_1_to_5": True,
        "early_slope_per_generation": slope,
        "generations_to_1.2pct": n12, "years_to_1.2pct": t12,
        "D_over_L_pct": {"1My": pct[1], "5My": pct[5], "6.9My": pct[6.9], "10My": pct[10]},
        "linear_over_exact_at_1.2pct": round(early / frac(KAP, n12), 4),
        "E2_ratio_to_pi_0.088pct": round(r_pi, 2), "E2_ratio_to_0.1pct": r_01,
        "steelman_mu_L_T_per_lineage": per_lineage, "steelman_over_F_max": round(factor),
        "mutation_rate_over_fixation_rate": round(slope * GF),
    },
    "positions": {
        "day": {"reading": "the model has no drift, so nothing fixes: D(t) counts differences between two individuals of "
                           "one population, not fixed differences between species, and its zero transit time assumes "
                           "the full-pipeline start Day disputes (M-202)",
                "holds": "the within-population prediction, 1.2% at 6.05 My, is about 14x measured human pairwise "
                         "diversity (0.088%), so the model as a model of one population is falsified, as Paul concedes"},
        "critic": {"reading": "read the two aliens as two isolated lineages with no ancestral polymorphism: the early "
                              "limit 2 L kappa t is the neutral 2 mu T of B4a with theta_anc = 0, and k = mu (B5, M-209)",
                   "holds": "at Day's 3.0 inputs the neutral rate gives 1.512e7 substitutions per lineage against "
                            "F_max 190.62, a factor of about 79,300; mutation supply (120 per generation) is not "
                            "limiting against 1 fixation per 1,322 generations"},
    },
    "notes": "Every number in the EVOA-102 review's section 2 for the human-like model reproduces from Paul's inputs; the "
             "algebra is exact for n = 1..5. The review's '6.05 My (302,426 generations)' is the first generation at "
             "which D/L reaches 1.2%. E2: 1.2% against 0.088% is 13.6x (12x against the rounded 0.1%). Section 5: "
             "1.512e7 / 190.62 = 79,320, stated 'about 79,000'. Whether D(t) speaks to fixed differences is the model "
             "question (E1, E3), not settled by this arithmetic.",
})
