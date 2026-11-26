#!/usr/bin/env python3
"""M-109 record (formula, derivation): which sites the neutral expectation applies to (Duffy's 169,344).

Object: docs/research/math/objects.yaml M-109 (formula, derivation). Duffy (evo008@L90, relayed by Day) scales the
neutral count by the divergent-site share: 76.8 x 201,600 x 35e6/3.2e9 = 169,344. Asserted: the whole-genome count
it is scaled from, 76.8 x 201,600 = 15,482,880 (the post's "15-some-odd-million"), the share 35e6/3.2e9 = 1.09375%
(M-108), and the product 169,344 exactly. Also asserted: Hancock's "38 million" is 2 x 252,000 x 76.8 = 38,707,200
(claim file B5c), and Duffy's first reason (haploid 38.4, evo008@L88) is not carried into his own formula; with 38.4
it gives 84,672. 201,600 is M-110 (cited); u = 76.8/3.2e9 and the like-for-like question are M-108 (cited).
The two positions: WD multiplies the expected count of substitutions by the chance that a site is one of the
35M that did diverge; Hancock (evo009@L57) and Day (evo009@L58) both say the neutral expectation applies to the whole
genome. The 35M divergent sites are the realised substitutions themselves (a single-copy count, polymorphism
included, CSAC), so the comparator for the observed 35M is the whole-genome count (2 lineages), not 1.09% of it.
Read WD's way, the neutral model would predict 169,344 divergent sites where 35M are observed (0.48%), so the
scaling cannot be the neutral prediction for the observed divergence. No verdict here (claim files). Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-109.py [--write]
Without --write it checks that M-109.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo008": "sources/raw/refresh-2026-11-01/p-erica-and-the-evo-avengers-008/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt"}
B5C = "docs/research/claims/B5c-hancock-76-8-per-generation.md"
PY = "docs/research/parameters.yaml"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def post(src, quote):
    """A source-map quote (committed), re-checked against the held post body when sources/raw is in this checkout."""
    held(SM + src + ".md", quote)
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def raw(src, quote):
    """A sentence from the held post body that the source map does not copy; checked when sources/raw is present."""
    if (ROOT / RAW[src]).exists():
        held(RAW[src], quote)
    return quote


def cited(rec, key):
    """A value from a settled record's JSON (cited, not recomputed)."""
    return json.loads((ROOT / REC / f"{rec}.json").read_text(encoding="utf-8"))["values"][key]


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


# ---- the source sentences ------------------------------------------------------------------------------
WD_169 = post("evo008", "So Zach’s original 38 million number is in actuality just 169,344.")        # evo008@L90, relay
ROW90 = held(SM + "evo008.md", "P: 76.8 x 201,600 x 35e6/3.2e9. C: 169,344.")
WD_FORM = raw("evo008", "In reality, the divergent sites are only 1.09% of the genome. So statistically, only 1.09% of "
                        "the neutral substitutions would end up in the divergent zone. The proper formula would be: "
                        "15-some-odd-million × 35 million ÷ 3.2 billion (the size of the genome).")    # evo008@L90
WD_CIRC = raw("evo008", "Zach is using circular reasoning in assuming the neutral prediction of 35 million "
                        "differences all fall perfectly into the divergent sites.")                    # evo008@L90
WD_HAP = raw("evo008", "First, the calculation is being run on the diploid genome size (76.8) instead of the haploid "
                       "genome (38.4).")                                                               # evo008@L88
WD_D = raw("evo008", "Second, minor: he’s using 252,000 generations instead of the d-coded size of 201,600.")  # L89
H_RERUN = post("evo009", "Rerun the clock, and a different 1.09% would fix.")                          # evo009@L57, relay
if (ROOT / RAW["evo009"]).exists():
    held(RAW["evo009"], "The fact that only 1.09% have fixed is a testament of the recency of our divergence, not that "
                        "those were the only one’s that could fix.")                                   # evo009@L57
    held(RAW["evo009"], "About 90% of the human genome lacks signs of selective constraint.")         # evo009@L57
D_WHOLE = post("evo009", "First, WE are the ones who pointed out that the neutral mutations have to apply to the entire "
                         "genome.")                                                                    # evo009@L58
if (ROOT / RAW["evo009"]).exists():
    held(RAW["evo009"], "HE is the one who tried to apply all of them to the 1.09 percent SNP divergence.")  # evo009@L58
B5C_38 = held(B5C, "2 lineages × 252,000 × 76.8 = 38.7M (the quoted \"about 38 million\")")
held(PY, "chimp_consortium_2005: {value: 3.5e7, units: \"single-nucleotide changes (one genome per species; "
         "includes polymorphism)\"")                                  # divergence.snv_differences_total

# ---- the arithmetic as printed ----------------------------------------------------------------------------
R, G_EFF, G_NOM, SNV, L = Fr(768, 10), 201_600, 252_000, 35 * 10 ** 6, 32 * 10 ** 8
assert cited("M-108", "snv_site_share") == float(Fr(SNV, L)) == 0.0109375   # 1.09375% (M-108)
whole = R * G_EFF
assert whole == 15_482_880                                           # "15-some-odd-million", the whole-genome count
assert 15 * 10 ** 6 < whole < 16 * 10 ** 6
wd = whole * Fr(SNV, L)
assert wd == 169_344                                                 # exact, as printed
# Hancock's 38 million and Duffy's own first correction
h38 = 2 * G_NOM * R
assert h38 == 38_707_200                                             # B5c: "about 38 million"
hap = Fr(384, 10)
assert hap * 2 == R and hap * G_EFF * Fr(SNV, L) == 84_672           # with the haploid 38.4 Duffy calls for
assert G_NOM * Fr(80, 100) == G_EFF                                  # 201,600 = 252,000 x 0.80 (M-110)

# ---- the comparison each position implies ----------------------------------------------------------------
# whole-genome reading (Hancock; Day at evo009@L58): expected substitutions over both lineages against the observed 35M
both_eff, both_nom = 2 * whole, h38
assert both_eff == 30_965_760
near(float(both_eff / SNV), 0.8847, 5e-5); near(float(both_nom / SNV), 1.1059, 5e-5)
# WD's reading: the neutral prediction for the divergent sites is 169,344; the divergence it predicts is 35M
near(float(wd / SNV), 0.004838, 5e-7)                                # 0.48% of the observed count
near(float(SNV / wd), 206.68, 0.005)                                 # the observed divergence is 207x WD's figure
assert wd * Fr(L, SNV) == whole                                      # scaling only undoes itself: no new information

finish({
    "object": "M-109",
    "inputs": [
        {"name": "events per genome per generation", "value": 76.8, "cite": "evo008@L90 (Duffy, relayed); M-108 for u and its meaning"},
        {"name": "effective generations", "value": 201_600, "cite": "evo008@L89; M-110 (252,000 x 0.80)"},
        {"name": "nominal generations", "value": 252_000, "cite": "parameters generations_available.day_2026; B5c"},
        {"name": "SNV differences", "value": SNV, "cite": "parameters divergence.snv_differences_total.chimp_consortium_2005"},
        {"name": "genome size", "value": 3.2e9, "cite": "evo008@L90"},
        {"name": "haploid rate Duffy calls for", "value": 38.4, "cite": "evo008@L88"},
    ],
    "values": {
        "whole_genome_count_one_lineage": int(whole), "divergent_share": float(Fr(SNV, L)),
        "wd_scaled": int(wd), "wd_scaled_with_38_4": 84_672, "hancock_38M": int(h38),
        "whole_genome_two_lineages_at_201600": int(both_eff),
        "ratio_to_observed": {"two_lineages_201600": round(float(both_eff / SNV), 4),
                              "two_lineages_252000": round(float(both_nom / SNV), 4),
                              "wd_scaled": round(float(wd / SNV), 6)},
    },
    "positions": {
        "wd": {"reading": "only 1.09% of the neutral substitutions land in the divergent sites, so the prediction to set "
                          "against them is 169,344",
               "holds": "the arithmetic reproduces exactly (15,482,880 x 35e6/3.2e9); his first correction (38.4) is "
                        "not used in it (84,672 with it)"},
        "day": {"reading": "the neutral expectation applies to the entire genome (evo009@L58); Hancock put all of it on "
                           "the 1.09%",
                "holds": "the whole-genome reading is the one Hancock also states; Day does not restate 169,344 in "
                         "evo009"},
        "critic": {"reading": "which sites fix is random; the 1.09% marks recency, not the only sites that could fix "
                              "(Hancock, evo009@L57)",
                   "holds": "the 35M are the realised substitutions, so the whole-genome count is their comparator: "
                            "30.97M at 201,600 or 38.71M at 252,000 (0.88x, 1.11x of 35M); WD's scaling predicts "
                            "169,344 divergent sites against 35M observed (1/207)"},
    },
    "notes": "Arithmetic as printed holds. The object is which sites the expectation applies to: multiplying the "
             "expected count by the share of sites that turned out divergent counts the predicted substitutions "
             "that would hit a site set fixed in advance; the divergent set is not fixed in advance but is the "
             "realised substitutions, so both Hancock and Day (evo009) apply the expectation to the whole genome. "
             "Whether 76.8 is a haploid events rate or the diploid SNV product (and so one lineage or two) is M-108; "
             "the d = 0.80 input is M-110. The 35M includes polymorphism (CSAC, one genome per species).",
})
