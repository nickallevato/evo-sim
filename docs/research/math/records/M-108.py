#!/usr/bin/env python3
"""M-108 record (model-choice, derivation): a mutation rate with structural variants against an SNV-only divergence.

Object: docs/research/math/objects.yaml M-108 (model-choice, derivation). Hancock (evo009@L37, relayed) restates the
rate as u = 76.8 per haploid genome per generation over 3e9 sites = 2.56e-8, "which includes structural variants"
(Perubski et al., as spelled in the post). Day (evo009@L43): a total rate cannot be validated against "a fraction of
the genome that omits 98.91 percent of the total"; Duffy (evo008@L83): an SNP-only calculation cannot be validated
with a number that includes structural variation. Asserted: 76.8/3e9 = 2.56e-8 (as written the comment's product is
2.304e11, a slip in the relay, not scored), 76.8/3.2e9 = 2.4e-8, the 1.09% as 35e6/3.2e9 = 1.094% and 100 - 1.09 =
98.91. Like for like: no. The rate counts mutation events of every type; the comparator counts SNV events only. The
matching comparator is all events: CSAC 35M SNV + 5M indel = 40M (B5c, A3x) or R4 GAP-07b's 42.10M. On that basis
the SNV-only count leaves out 12.5% (CSAC) or 10.3% (GAP-07b) of the events, not 98.91%: the 98.91% is the share of
genome sites that are not SNV differences, a site share, not a share of the mutations or of the divergence. On Day's
own base-pair total (398,673,272) SNVs are 8.8% of divergent bp (91.2% left out), but a per-event rate cannot be set
against base pairs (A3x). So Day and Duffy are right that the units are mixed; the size of the mix is about 1.1x in
events, not the 1/0.0109 = 91x the 98.91% suggests. Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-108.py [--write]
Without --write it checks that M-108.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo008": "sources/raw/refresh-2026-11-01/p-erica-and-the-evo-avengers-008/body.txt",
       "evo009": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-009/body.txt"}
CL = "docs/research/claims/"
B5C = CL + "B5c-hancock-76-8-per-generation.md"
A3X = CL + "A3x-bp-vs-events.md"
R1015 = "docs/research/sources/refresh-2026-10-15.md"
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
H_U = post("evo009", "u = (3e9)*(76.8) = 2.56e-8")                                                    # evo009@L37, relay
if (ROOT / RAW["evo009"]).exists():
    held(RAW["evo009"], "76.8 mutations per haploid genome per generation (from Perubski et al.), which includes "
                        "structural variants.")
D_9891 = post("evo009", "You cannot use a total mutation rate as the input and then validate the output against a "
                        "fraction of the genome that omits 98.91 percent of the total.")              # evo009@L43
ROW43 = held(SM + "evo009.md", "P: rate includes SVs; divergence counted is SNP-only (1.09%). C: mixed denominators.")
WD_SNP = post("evo008", "You can’t validate a SNP-only calculation with a number that includes large structural "
                        "variation.")                                                                 # evo008@L83, relay
B5C_152 = held(B5C, "The retained 76 is a different quantity: a cited de novo count of 98–206 per generation (mean "
                    "152, including structural variants), halved to the haploid genome: 152/2 = 76")
B5C_EV = held(B5C, "That is a count of mutation *events* of all types, so the matching comparator is the CSAC event "
                   "total (35M SNV + 5M indel events ≈ 40M, derived), not the SNV count alone.")
B5C_768 = held(B5C, "6.4e9 × 1.2e-8 = 76.8 ✓ (diploid bases, the first-pass figure)")
GAP07B = held(A3X, "37.77M SNVs, 4.30M indel events (2.17M extra-human-base, 2.09M extra-chimp-base, 35k both-sided), "
                   "42.10M events, 21.05M per lineage")
UNITS = held(A3X, "a base-pair numerator against G_f's events is a unit mismatch")
TOTAL_Q = held(R1015, "\"the total chimpanzee-human divergence from the human perspective is 398,673,272 base-pairs, "
                      "or 12.79 percent of the human genome\"")
held(PY, "chimp_consortium_2005: {value: 3.5e7")                     # divergence.snv_differences_total
held(PY, "chimp_consortium_2005: {value: 5.0e6, units: events")      # divergence.indel_events_total
held(PY, "pedigree_human: {value: 1.2e-8")                           # mutation.mu_per_site_per_gen.pedigree_human

# ---- the rate ---------------------------------------------------------------------------------------------
R, L3, L32 = Fr(768, 10), 3 * 10 ** 9, 32 * 10 ** 8
assert R / L3 == Fr(256, 10 ** 10)                                   # 2.56e-8, the relayed result
assert L3 * R == 2304 * 10 ** 8                                      # 2.304e11: the product as written (relay slip)
assert R / L32 == Fr(24, 10 ** 9)                                    # 2.4e-8 on 3.2e9
assert Fr(64, 10) * 10 ** 9 * Fr(12, 10 ** 9) == R                   # 76.8 is also 6.4e9 x 1.2e-8 (B5c)
assert Fr(152, 2) == 76                                              # the event count, halved (B5c)
near(float((R / L3) / Fr(12, 10 ** 9)), 2.133, 5e-4)                 # u against the pedigree SNV rate

# ---- the ratio the source draws ------------------------------------------------------------------------------
SNV, INDEL = 35 * 10 ** 6, 5 * 10 ** 6
site_share = Fr(SNV, L32)
assert site_share == Fr(35, 3200)                                    # 1.09375%
assert round(float(site_share) * 100, 2) == 1.09
assert Fr(100) - Fr(109, 100) == Fr(9891, 100)                        # 98.91, as printed
near(1 / float(site_share), 91.43, 0.005)                            # the factor the 98.91% implies

# ---- like for like: events against events --------------------------------------------------------------------
ev_csac = Fr(SNV, SNV + INDEL)
assert ev_csac == Fr(7, 8) and 1 - ev_csac == Fr(1, 8)               # SNVs 87.5% of CSAC events; 12.5% left out
ev_g7 = Fr(3777, 4210)
near(float(1 - ev_g7), 0.1029, 5e-5)                                 # 10.3% on GAP-07b's 42.10M
near(float(1 / ev_csac), 1.1429, 5e-5); near(float(1 / ev_g7), 1.1146, 5e-5)
bp_share = Fr(SNV, 398_673_272)
near(float(bp_share), 0.08779, 5e-6); near(float(1 - bp_share), 0.9122, 5e-5)  # on Day's bp total
assert 1 - ev_csac < Fr(9891, 10_000) and 1 - bp_share < Fr(9891, 10_000)

finish({
    "object": "M-108",
    "inputs": [
        {"name": "events per haploid genome per generation", "value": 76.8, "cite": "evo009@L37 (Hancock, relayed); B5c (76.8 = 6.4e9 x 1.2e-8; 152/2 = 76 events incl. SVs)"},
        {"name": "sites", "value": [3e9, 3.2e9], "cite": "evo009@L37; evo008@L90"},
        {"name": "SNV differences", "value": SNV, "cite": "parameters divergence.snv_differences_total.chimp_consortium_2005"},
        {"name": "indel events", "value": INDEL, "cite": "parameters divergence.indel_events_total.chimp_consortium_2005"},
        {"name": "measured events", "value": {"snv": 37.77e6, "all": 42.10e6}, "cite": "claim file A3x, R4 GAP-07b"},
        {"name": "Day's bp total", "value": 398_673_272, "cite": "refresh-2026-10-15 (Day, 'Evo-Avengers 002')"},
    ],
    "values": {
        "u_on_3e9": 2.56e-8, "u_on_3.2e9": 2.4e-8, "product_as_written": 2.304e11,
        "u_over_pedigree_snv_rate": round(float((R / L3) / Fr(12, 10 ** 9)), 4),
        "snv_site_share": float(site_share), "printed_omitted": 98.91,
        "omitted_share_of_events": {"csac": float(1 - ev_csac), "gap07b": round(float(1 - ev_g7), 4)},
        "all_events_over_snv": {"csac": round(float(1 / ev_csac), 4), "gap07b": round(float(1 / ev_g7), 4)},
        "omitted_share_of_bp_on_day_total": round(float(1 - bp_share), 4),
        "like_for_like": False,
    },
    "positions": {
        "day": {"reading": "a total mutation rate must be compared with a total divergence, not the SNV fraction",
                "holds": "the units are mixed: the rate counts events of every type, the 35M counts SNVs only; Duffy "
                         "(evo008@L83) was right to flag it"},
        "critic": {"reading": "the fixation equation does not distinguish mutation types; the swap of rate is a point "
                              "against Hancock's whiteboard, not against neutral theory",
                   "holds": "in events the mismatch is 1.11-1.14x (SNVs are 87.5-89.7% of events); the 98.91% is a "
                            "share of genome sites, not of the mutations, so it overstates the mismatch about 80-fold"},
    },
    "notes": "Not like for like, as Day and Duffy say; the matching comparator for an all-events rate is all events "
             "(40M CSAC, 42.10M GAP-07b), not SNVs and not base pairs. The ratio the post draws (98.91% omitted) is "
             "100 - 1.09, where 1.09% = 35e6/3.2e9 is the SNV share of genome sites; read as a share of the "
             "divergence it would be 12.5% (events) or 91.2% (Day's bp), and bp cannot be set against an event rate "
             "(A3x). The relay's 'u = (3e9)*(76.8)' is a slip for 76.8/3e9. 76.8 is numerically the diploid SNV "
             "product 6.4e9 x 1.2e-8 (B5c), while the post calls it a haploid all-events rate (152/2 = 76); which one "
             "Hancock meant is not settled here. Duffy's 169,344 is M-109.",
})
