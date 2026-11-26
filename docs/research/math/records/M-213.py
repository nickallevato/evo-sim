#!/usr/bin/env python3
"""M-213 record (identity): genome-size and lineage-count factors in a neutral-count formula.

Object: docs/research/math/objects.yaml M-213 (identity, derivation). Writes each count with both
factors explicit, count = (haploid or diploid sites) x mu x generations x (1 or 2 lineages), and checks
Hancock's on-screen correction (6.4e9 -> 3.2e9, 152 -> 76), the x2 that turns per-lineage counts into
38M and 37.8M, Nesslig20's 75 under its two readings, and Day's 2019 15M + 15M = 30M against the CSAC
total and fixed shares. Inputs carry their claim file and quote number or parameters.yaml key; held()
checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-213.py [--write]
Without --write it checks that M-213.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QD = "docs/research/sources/quotes-day.md"
QL = "docs/research/sources/quotes-literature.md"
PY = "docs/research/parameters.yaml"


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


def count(sites, mu, gens, lineages):
    return sites * mu * gens * lineages


# ---- inputs -------------------------------------------------------------------------------
B5C = CL + "B5c-hancock-76-8-per-generation.md"
HA2 = held(B5C, "use 6.4. This is the diploid genome size for the fixation rate because you fix on a hloid genome. So, it should be 3.2 e to the 9.")
HA3 = held(B5C, "Um so that's 152 on average. If we divide that in half to take the")
HA4 = held(B5C, "we'll say about 38 million.")
HA152 = held(B5C, "a cited de novo count of 98–206 per generation (mean 152, including structural variants)")
NE2 = held(CL + "B5e-nesslig20-37-8-million.md", "So, the expected number of fixed neutral mutations that separates humans and chimps is ~37.8 million")
NE_DEF = held(CL + "B5e-nesslig20-37-8-million.md", "\"the neutral mutation rate per haploid genome per generation\" (§2.1)")
DD = held(CL + "B5f-reddit-9-7-million-haploid.md", "or about 9.7 million over its proposed 252,000 generations.")
Q05 = held(QD, "it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another "
               "15,000,000 mutations to become fixed in the chimpanzee population")
CSAC = held(QL, "constituting approximately thirty-five million single-nucleotide changes")
POLY = held(QL, "we estimate that polymorphism accounts for 14-22% of the observed divergence rate")
PY_HAP = held(PY, "new_mutations_per_haploid_genome: {value: 38.4, derived: \"3.2e9 bp x 1.2e-8\"")
PY_MU = held(PY, "pedigree_human: {value: 1.2e-8")

MU, T = 1.2e-8, 252_000

# ---- Hancock: diploid first pass, haploid correction ----------------------------------------------
dip = count(6.4e9, MU, 1, 1)
hap = count(3.2e9, MU, 1, 1)
near(dip, 76.8, 1e-9)
near(hap, 38.4, 1e-9)
near(dip / hap, 2, 1e-12)
assert 152 / 2 == 76                                    # cited de novo mean halved to the haploid genome
near(count(6.4e9, MU, T, 2), 38.71e6, 0.01e6)           # 76.8 x 2 x 252,000
near(76 * 2 * T, 38.30e6, 0.01e6)                       # retained 76 (all mutation types) x 2 lineages
near(count(3.2e9, MU, T, 2), 19.35e6, 0.01e6)           # SNV haploid, two lineages
near(count(3.2e9, MU, T, 1), 9.677e6, 0.001e6)          # SNV haploid, one lineage ("9.7 million")
# "about 38 million" needs (diploid and x2) or (76 and x2); haploid SNV with x2 gives 19.35M

# ---- Nesslig20: the basis of 75 ---------------------------------------------------------------------
assert 2 * 75 * T == 37.8e6                             # as written: 75 per haploid genome, two lineages
assert 2 * 37.5 * T == 18.9e6                           # if 75 is a zygote count, haploid 37.5
near(18.9e6 / 35e6, 0.54, 0.001)

# ---- Day 2019: 15M per lineage, two lineages ----------------------------------------------------------
assert 15e6 + 15e6 == 30e6
fixed_share = (1 - 0.22, 1 - 0.14)                      # CSAC: polymorphism 14-22% of observed divergence
fixed = tuple(35e6 * f for f in fixed_share)
near(fixed[0], 27.3e6, 1)
near(fixed[1], 30.1e6, 1)
per_lineage = tuple(f / 2 for f in fixed)
near(per_lineage[0], 13.65e6, 1)
near(per_lineage[1], 15.05e6, 1)
assert per_lineage[0] < 15e6 < per_lineage[1]          # Day's 15M per lineage sits at the top of the fixed share
near(35e6 / 2, 17.5e6, 0)                                # the 17.5M per lineage is the unfiltered half

finish({
    "object": "M-213",
    "inputs": [
        {"name": "Hancock correction", "value": "6.4e9 -> 3.2e9; 152 -> 76; about 38 million", "cite": "B5c q2, q3, q4; claim file B5c"},
        {"name": "Nesslig20 37.8M and mu_G definition", "cite": "B5e q2; claim file B5e (s2.1)"},
        {"name": "Dumb-and-Dumber 9.7M", "cite": "B5f q1"},
        {"name": "Day 2019 15M + 15M", "cite": "Q05 (B6b q2)"},
        {"name": "CSAC 35M SNV, polymorphism 14-22%", "cite": "quotes-literature CSAC2005; parameters divergence.snv_differences_total"},
        {"name": "mu, haploid count", "value": [MU, 38.4], "cite": "parameters mutation.mu_per_site_per_gen.pedigree_human, mutation.new_mutations_per_haploid_genome"},
    ],
    "values": {
        "per_gen": {"diploid": g(dip), "haploid": g(hap), "cited_halved": 76},
        "counts": {"diploid_x2": g(count(6.4e9, MU, T, 2)), "76_x2": 76 * 2 * T, "haploid_x2": g(count(3.2e9, MU, T, 2)),
                   "haploid_x1": g(count(3.2e9, MU, T, 1)), "nesslig_as_written": 37.8e6, "nesslig_zygote_reading": 18.9e6},
        "csac_fixed_total": [g(f) for f in fixed], "csac_fixed_per_lineage": [g(f) for f in per_lineage],
    },
    "positions": {
        "day": {"reading": "each lineage counted separately: 15M fixed in humans and 15M in chimps",
                "per_lineage": 15e6, "total": 30e6},
        "critic": {"reading": "write the formula with haploid sites and the lineage count explicit",
                   "haploid_one_lineage": g(count(3.2e9, MU, T, 1)), "haploid_two_lineages": g(count(3.2e9, MU, T, 2)),
                   "csac_fixed_per_lineage": [g(f) for f in per_lineage]},
    },
    "notes": "Factor 2 (diploid vs haploid) and factor 2 (one vs two lineages) are independent; Hancock's 38M keeps the "
             "x2 lineages after the haploid correction only through the 76 that counts all mutation types. Nesslig20's "
             "37.8M halves to 18.9M if 75 is a zygote count. Day's 15M per lineage is at the top of CSAC's fixed share "
             "(13.65-15.05M).",
})
