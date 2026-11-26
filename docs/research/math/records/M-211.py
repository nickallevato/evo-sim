#!/usr/bin/env python3
"""M-211 record (inference): does Ne = 10,000 from theta = 4 Ne mu presuppose k = mu?

Object: docs/research/math/objects.yaml M-211 (inference, derivation). Ne = theta/(4 mu). The record
fixes the diversity theta implied by the standard pair (Ne 1e4, pedigree mu 1.2e-8), then inverts it
under each side's source for mu: a pedigree mu (measured in parent-offspring trios, no k = mu step) and
a phylogenetic mu (observed divergence over twice the split time, which is k = mu by construction). It
computes both and chooses neither: the dispute is which mu the standard 10,000 used. No held text
quotes a measured human diversity value, so theta here is the implied one. Inputs carry their quote
id, claim file or parameters.yaml key; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-211.py [--write]
Without --write it checks that M-211.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
PY = "docs/research/parameters.yaml"
B3H = CL + "B3h-ne-10000-presupposes-k-mu.md"


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
Q1 = held(B3H, "The arithmetic holds given one number: Nₑ ≈ 10,000 — which comes from θ = 4Nₑμ, which presupposes "
               "k = μ, the identity under test.")
Q2 = held(B3H, "The standard N₂ ≈ 10,000 is itself problematic, as it is derived from genetic diversity via θ = 4N₂μ "
               "— a formula that presupposes k = μ.")
HL = held(B3H, "Z22129121 states \"The equilibrium heterozygosity relation θ = 4Nₑμ is untouched.\"")
IR5 = held(B3H, "IR §5 itself says μ \"was initially estimated phylogenetically\"")
KEIGHT = held(CL + "B3a-fixation-probability-1-over-2ne.md",
              "pedigree μ ≈ 1.1e-8 is \"about twofold lower than estimates based on the human-chimp divergence\"")
PY_MU = held(PY, "pedigree_human: {value: 1.2e-8")
PY_NE = held(PY, "Ne_modern_human: {value: 1.0e4")
PY_D = held(PY, "csac_2005_total: {value: 0.0123")
PY_T = held(PY, "day_2026: {value: 252000")

NE_STD, MU_PED, D_OBS, T = 1.0e4, 1.2e-8, 0.0123, 252_000

# ---- theta implied by the standard pair -------------------------------------------------------
theta = 4 * NE_STD * MU_PED
near(theta, 4.8e-4, 1e-15)                              # B4a q3 "4 x 1e4 x 1.2e-8 = 4.8e-4 per site"

# ---- critic: pedigree mu (no k = mu step) ---------------------------------------------------------
ne_ped = theta / (4 * MU_PED)
near(ne_ped, 10_000, 1e-9)

# ---- Day: a phylogenetic mu is k = mu by construction (d = 2 mu T) ---------------------------------
mu_phy = D_OBS / (2 * T)
near(mu_phy, 2.440e-8, 0.001e-8)
near(mu_phy / MU_PED, 2.03, 0.01)                       # cf. Keightley "about twofold"
ne_phy = theta / (4 * mu_phy)
near(ne_phy, 4_917, 1)
near(ne_ped / ne_phy, 2.03, 0.01)                       # the mu source moves Ne by the same factor
# the dependence is on the mu source only: theta = 4 Ne mu itself is an equilibrium diversity relation
for mu in (MU_PED, mu_phy):
    near(4 * (theta / (4 * mu)) * mu, theta, 1e-18)

finish({
    "object": "M-211",
    "inputs": [
        {"name": "Day: Ne 10,000 from theta = 4 Ne mu presupposes k = mu", "cite": "B3h q1 (blog 2026-08-27 para 3), q2 (Z18525547 para 4)"},
        {"name": "Day's HL: theta = 4 Ne mu untouched", "cite": "claim file B3h (Z22129121)"},
        {"name": "IR s5: mu initially estimated phylogenetically", "cite": "claim file B3h"},
        {"name": "Ne, pedigree mu", "value": [NE_STD, MU_PED], "cite": "parameters population.Ne_modern_human, mutation.mu_per_site_per_gen.pedigree_human"},
        {"name": "observed divergence, generations", "value": [D_OBS, T], "cite": "parameters divergence.snv_divergence_fraction.csac_2005_total, generations_available.day_2026"},
        {"name": "Keightley twofold", "cite": "claim file B3a"},
    ],
    "values": {"theta_implied": theta, "Ne_pedigree_mu": g(ne_ped), "mu_phylogenetic": g(mu_phy),
               "Ne_phylogenetic_mu": g(ne_phy), "ratio": g(ne_ped / ne_phy)},
    "positions": {
        "day": {"reading": "the standard Ne was derived with a phylogenetic mu, which uses k = mu",
                "Ne_if_mu_phylogenetic": g(ne_phy)},
        "critic": {"reading": "theta = 4 Ne mu is the equilibrium diversity formula; with a pedigree mu no k = mu step enters",
                   "Ne_if_mu_pedigree": g(ne_ped)},
    },
    "notes": "theta = 4 Ne mu does not itself contain k = mu (Day's HL says it is 'untouched'). Whether a given Ne "
             "estimate does depends on how its mu was obtained: with the pedigree 1.2e-8 the implied Ne is 10,000; "
             "with a phylogenetic mu from 1.23% over 2 x 252,000 generations it is 4,917 (2.0x lower). theta here is "
             "the implied value; no held text quotes a measured human diversity.",
})
