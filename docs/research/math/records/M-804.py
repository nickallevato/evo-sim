#!/usr/bin/env python3
"""M-804 record (derivation): deleterious-mutation load under hard selection, W = e^(-U) (Keightley 2012).

Object: docs/research/math/objects.yaml M-804 (formula, derivation). Under hard selection ("one deleterious mutation,
one genetic death") mean fitness relative to a mutation-free genotype is W = e^(-U). Keightley 2012 Abstract (as the
claim file H7 quotes it): U = 2.2 for the whole diploid genome (W = 0.1108, paper 0.11) and 0.35 for amino-acid-
changing mutations (W = 0.7047, paper 0.7); with 20 offspring per female, 20 x (1 - 0.1108) = 17.8 selective deaths
(paper "18"). mu about 1.1e-8 and about 70 new mutations per diploid genome (H7 q3; parameters
mutation.mu_per_site_per_gen.keightley_2012): 70 / (2 x 1.1e-8) = 3.18e9 sites per haploid genome. The sqrt(N)
truncation purge (H4 q3, via a commenter) is on this deleterious side; the record asserts no number for it.
Closed forms only (stdlib). The Keightley text is held as the claim file and quotes-literature quote it.

Run: research/.venv/bin/python -I docs/research/math/records/M-804.py [--write]
Without --write it checks that M-804.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H4 = CL + "H4-worden-speed-limit.md"
H7 = CL + "H7-keightley-deleterious-load.md"
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
H7Q1 = held(H7, "A genome-wide deleterious mutation rate of 2.2 seems higher than humans could tolerate if natural "
                "selection is “hard,” but could be tolerated if selection acts on relative fitness differences between "
                "individuals or if there is synergistic epistasis.")                                      # H7 q1 (Abstract)
H7Q2 = held(H7, "I argue that in the foreseeable future, an accumulation of new deleterious mutations is unlikely to "
                "lead to a detectable decline in fitness of human populations.")                          # H7 q2 (Abstract)
H7Q3 = ("Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is about "
        "twofold lower than estimates based on the human-chimp divergence. This implies that an average of ~70 new "
        "mutations arise in the human diploid genome per generation.")
held(H7, H7Q3); held(QL, H7Q3)                                       # H7 q3 (Abstract, Europe PMC)
U_Q = held(H7, "estimates are U ≈ 2.2 for the whole diploid genome per generation and 0.35 for mutations that change an "
               "amino acid of a protein-coding gene")                                                     # Abstract, in H7 formal
W_F = held(H7, "Under hard selection (\"one deleterious mutation, one genetic death\"), mean fitness relative to a "
               "mutation-free genotype W̄ = e^(-U).")
R2 = held(H7, "e^-2.2 = 0.1108 (paper 0.11; holds); e^-0.35 = 0.7047 (paper 0.7; holds); with 20 offspring per "
              "female, 20 x (1 - 0.1108) = 17.8 selective deaths (paper \"18\"; holds).")
SCOPE = held(H7, "The paper does not address beneficial substitutions or Haldane's 1957 limit.")
H4Q3 = held(H4, "The sqrt(N) trick helps with mutational load, not with the speed of adaptation.")      # H4 q3 (Day)
held(PY, "keightley_2012: {value: 1.1e-8, note: \"abstract only; ~70 new mutations per genome\"")
U_ALL, U_AA, OFFSPRING, MU, NEW = 2.2, 0.35, 20, 1.1e-8, 70
assert "2.2" in H7Q1 and "1.1 × 10(-8)" in H7Q3 and "~70" in H7Q3

# ---- load -------------------------------------------------------------------------------------------
w_all, w_aa = math.exp(-U_ALL), math.exp(-U_AA)
near(w_all, 0.1108, 5e-5); assert round(w_all, 2) == 0.11           # paper 0.11
near(w_aa, 0.7047, 5e-5); assert round(w_aa, 1) == 0.7              # paper 0.7
deaths = OFFSPRING * (1 - w_all)
near(deaths, 17.78, 0.005); assert round(deaths) == 18              # 17.8 (paper "18")
near(OFFSPRING * (1 - round(w_all, 4)), 17.784, 1e-9)               # the claim file's 20 x (1 - 0.1108)
near(1 / w_all, 9.03, 0.005)                                        # each female must leave 9x the replacement number
near(OFFSPRING * (1 - w_aa), 5.91, 0.005)                           # amino-acid class alone: 5.9 deaths per 20
near(OFFSPRING * w_all, 2.22, 0.005); assert U_ALL < math.log(OFFSPRING / 2)   # 2.2 survivors of 20: just above replacement (2)
# ---- mu and new mutations --------------------------------------------------------------------------
sites = NEW / (2 * MU)
near(sites / 1e9, 3.18, 0.005)                                      # 70 per diploid genome at 1.1e-8: 3.18e9 sites per haploid genome
near(MU * 2 * 3.2e9, 70.4, 1e-6)                                    # at 3.2e9 bp (parameters mutation.new_mutations_per_haploid_genome base)
assert U_ALL / NEW < 0.05                                           # 2.2 of ~70 new mutations (3.1%) count as deleterious

finish({
    "object": "M-804",
    "inputs": [
        {"name": "U whole diploid genome, amino-acid class", "value": [U_ALL, U_AA], "cite": "Keightley 2012 Abstract as quoted in H7 formal statement; H7 q1"},
        {"name": "offspring per female", "value": OFFSPRING, "cite": "claim file H7 derived (Keightley's illustration)"},
        {"name": "mu, new mutations per diploid genome", "value": [MU, NEW], "cite": "H7 q3; parameters mutation.mu_per_site_per_gen.keightley_2012"},
    ],
    "values": {
        "W_U2.2": round(w_all, 4), "W_U0.35": round(w_aa, 4), "deaths_per_20_U2.2": round(deaths, 2),
        "deaths_per_20_U0.35": round(OFFSPRING * (1 - w_aa), 2), "replacement_multiple_1/W": round(1 / w_all, 2),
        "haploid_sites_implied_70/(2mu)": f"{sites:.3e}", "deleterious_share_of_new": round(U_ALL / NEW, 4),
    },
    "positions": {
        "day": {"reading": "the sqrt(N) trick helps with mutational load, not the speed of adaptation (H4 q3); the deleterious "
                           "side is separate from Haldane's cost of beneficial fixation",
                "holds": "the record's numbers are all on the deleterious side; Keightley states the paper does not "
                         "address beneficial substitutions or Haldane 1957"},
        "critic": {"reading": "U = 2.2 is too high for hard selection but tolerable under relative-fitness selection or synergistic "
                              "epistasis (H7 q1); no detectable fitness decline is expected (H7 q2)",
                   "holds": "W = 0.11 needs 17.8 selective deaths per 20 offspring (1/W = 9.0), which is the 'one mutation, "
                            "one death' arithmetic Keightley rejects as a description of human selection"},
    },
    "notes": "All printed figures reproduce: e^-2.2 = 0.1108 (0.11), e^-0.35 = 0.7047 (0.7), 20 x (1 - 0.1108) = 17.8 "
             "(18). The 70 new mutations per diploid genome at mu = 1.1e-8 imply about 3.2e9 sites per haploid genome. "
             "No raw Keightley text is in sources/raw/ in this checkout; the inputs are the Abstract as quoted in H7 "
             "and quotes-literature. parameters mutation.new_mutations_per_genome.common_citation is [60, 100], not "
             "the 70 the H7 link line attributes to it (70 is inside the range). The sqrt(N) purge has no held number.",
})
