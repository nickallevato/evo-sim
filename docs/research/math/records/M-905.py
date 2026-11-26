#!/usr/bin/env python3
"""M-905 record (empirical, data-check): genome-wide human-chimp dN/dS, Day's 0.80 against the measured values.

Object: docs/research/math/objects.yaml M-905. Day (claim files DN1-DN3, Q172-Q176): 0.80 on 20,400 GENCODE v46
genes; single-SNV codons 71.6% nonsynonymous, 28.4% synonymous, dN/dS 0.71; 'no combination of quality filters moves
the number below 0.65' with a full stack at 0.64 on 10 genes; the Consortium's 0.23 on 13,454 genes, 6,946 'thrown
out', '51.6% more genes'. Measured (R4 L1 on hg38/panTro5, R4 L1b on T2T hs1/mPanTro3 Cactus): all genes 0.271,
one2one 0.207 (L1) and 0.238 (L1b), 0.214-0.283 over the 32 filter stacks (L1b), correct-frame values 0.15-0.45
in every gene set, filter stack and aggregation (L1). The record checks each figure verbatim in its held file and
asserts the arithmetic between them: Day's implied site ratio, the gene-set sums, the gene-set effect.

Inputs: claim files DN1, DN2, DN3 (Day's sentences); quotes-literature.md CSAC2005 (held text); R4-L1.md and
R4-L1b.md result rows (cited, not recomputed). Exact rationals (stdlib). Runs in well under a second.

Run: research/.venv/bin/python -I docs/research/math/records/M-905.py [--write]
Without --write it checks that M-905.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
DN1 = CL + "DN1-dnds-080-on-20400-genes.md"
DN2 = CL + "DN2-filters-cannot-move-below-065.md"
DN3 = CL + "DN3-consortium-gene-set-artefact.md"
QL = "docs/research/sources/quotes-literature.md"
L1 = "research/checks/results/R4-L1.md"
L1B = "research/checks/results/R4-L1b.md"


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


# ---- Day's sentences ---------------------------------------------------------------------------------------
held(DN1, "Not 0.23. 0.80.")
held(DN1, "We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46")
held(DN1, "Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for single-SNV codons alone.")
held(DN2, "No combination of quality filters moves the number below 0.65.")
held(DN2, "still produced dN/dS = 0.64 on 10 remaining genes.")
held(DN3, "The Consortium used 13,454.")
held(DN3, "They threw out 6,946 genes, one-third of the relevant data")
held(DN3, "Our dataset includes 51.6% more genes than theirs.")

# ---- the Consortium's text (CSAC 2005, held) -------------------------------------------------------------------
held(QL, "The K A/K S ratio for the human–chimpanzee lineage (q hominid) is 0.23.")
held(QL, "We began by identifying a set of 13,454 pairs of human and chimpanzee genes with unambiguous 1:1 orthology")
held(QL, "A total of 19,277 human RefSeq transcripts157, representing 16,045 distinct genes, were indirectly aligned")

# ---- the audit's measurements (cited rows) -----------------------------------------------------------------------
held(L1, "| V0 ALL (correct frame) | 23,183 | **0.271** |")
held(L1, "| V0 O121 (Ensembl one2one) | 16,766 | **0.207** |")
held(L1, "| Correct NG, any gene set (O121, ALL, NON121), any of the 32 filter stacks | 0.20-0.45 |")
held(L1, "| Mean or median of per-gene ratios (correct frame) | 0.15-0.44 |")
held(L1B, "| L1 V0 ALL (hg38/panTro5) | 23,183 | 0.271 | 0.913 | 3.34 |")
held(L1B, "| **V0 ALL** | 19,310 | **0.271** | 0.919 | 3.36 |")
held(L1B, "| V0 O121 (Ensembl one2one) | 16,824 | **0.238** |")
held(L1B, "| V0 ALL | 0.214 (S+G+L+O, 16,298) | 0.283 (M, 13,023) |")
held(L1B, "| Day: no 32-stack combination below 0.65 | all 32 below 0.65 (max 0.283) | **miss** |")

# ---- Day's implied site ratio: dN/dS = (Nd/Sd) / (N/S) ------------------------------------------------------------
nd_sd = Fr(716, 284)
near(float(nd_sd), 2.521, 0.0005)
ns_implied = nd_sd / Fr(71, 100)
near(float(ns_implied), 3.551, 0.0005)                 # (71.6/28.4)/0.71 = 3.55
ns_l1, ns_l1b = Fr(334, 100), Fr(336, 100)             # Nei-Gojobori N/S measured on human-chimp CDS (L1, L1b)
near(float(ns_implied / ns_l1), 1.063, 0.0005)         # Day's pair implies a site ratio 6.3% above the measured one
near(float(nd_sd / ns_l1), 0.755, 0.0005)              # his 71.6% at the measured 3.34 gives 0.75, not 0.71

# ---- the filter sentence against itself and against L1b ---------------------------------------------------------
assert Fr(64, 100) < Fr(65, 100)                        # Day's own 0.64 is below his 'no combination below 0.65'
near(float(1 - Fr(64, 65)), 0.0154, 0.0001)             # a 1.5% slip (DN2 S-DN2-1)
assert Fr(283, 1000) < Fr(65, 100) and Fr(214, 1000) < Fr(65, 100)   # L1b: all 32 stacks 0.214-0.283

# ---- gene-set arithmetic (DN3 q-text and CSAC Methods) --------------------------------------------------------------
day_n, csac_n, csac_start = 20_400, 13_454, 16_045
assert day_n - csac_n == 6_946
near(float(Fr(6_946, day_n)), 0.3405, 0.00005)          # 34.05%, 'one-third'
near(float(Fr(day_n, csac_n)), 1.5163, 0.00005)         # '51.6% more genes'
assert csac_start - csac_n == 2_591                      # what CSAC's curation removed, from its own 16,045-gene start
near(float(Fr(2_591, csac_start)), 0.1615, 0.00005)

# ---- the gene-set effect and the distance to 0.80 ------------------------------------------------------------------
all_l1, o121_l1, all_l1b, o121_l1b = Fr(271, 1000), Fr(207, 1000), Fr(271, 1000), Fr(238, 1000)
assert all_l1 - o121_l1 == Fr(64, 1000)                  # +0.064
near(float(all_l1 / o121_l1), 1.309, 0.0005)            # +31% on hg38/panTro5 (L1)
near(float(all_l1b / o121_l1b), 1.139, 0.0005)          # +14% on T2T (L1b)
near(float(Fr(80, 100) / all_l1), 2.952, 0.0005)        # Day's 0.80 is 2.95x the all-gene value
near(float(o121_l1 / Fr(23, 100)), 0.900, 0.0005)       # 0.207 is 10% below CSAC's 0.23; 0.238 is 3.5% above
near(float(o121_l1b / Fr(23, 100)), 1.035, 0.0005)
lo, hi = Fr(15, 100), Fr(45, 100)                        # correct-frame range over L1's rows 83-84
assert hi < Fr(65, 100) < Fr(80, 100)

finish({
    "object": "M-905",
    "inputs": [
        {"name": "Day's headline", "value": "0.80 on 20,400 GENCODE v46 genes", "cite": "DN1 (Q172-Q173)"},
        {"name": "Day's single-SNV codons", "value": "71.6% N, 28.4% S, dN/dS 0.71", "cite": "DN1"},
        {"name": "Day's filter sentence", "value": "none below 0.65; full stack 0.64 on 10 genes", "cite": "DN2 (Q175)"},
        {"name": "Day's gene-set arithmetic", "value": "13,454; 6,946 thrown out; 51.6% more", "cite": "DN3"},
        {"name": "CSAC 2005", "value": "Ka/Ks 0.23 on 13,454 1:1 orthologs, from 16,045 genes", "cite": "quotes-literature.md CSAC2005"},
        {"name": "R4 L1 (hg38/panTro5)", "value": {"ALL": 0.271, "one2one": 0.207, "N/S": 3.34, "correct-frame range": "0.15-0.45"},
         "cite": "R4-L1.md Results and rows 83-84"},
        {"name": "R4 L1b (T2T hs1/mPanTro3 Cactus)", "value": {"ALL": 0.271, "one2one": 0.238, "32 stacks": "0.214-0.283"},
         "cite": "R4-L1b.md Results and Filters tables"},
    ],
    "values": {
        "day_implied_N_over_S": round(float(ns_implied), 3),
        "measured_N_over_S": float(ns_l1),
        "day_share_at_measured_N_over_S": round(float(nd_sd / ns_l1), 3),
        "genes_not_in_csac_set": day_n - csac_n,
        "share_not_in_csac_set": round(float(Fr(6_946, day_n)), 4),
        "day_over_csac_genes": round(float(Fr(day_n, csac_n)), 4),
        "csac_removed_from_own_start": csac_start - csac_n,
        "gene_set_effect_L1": round(float(all_l1 / o121_l1), 3),
        "gene_set_effect_L1b": round(float(all_l1b / o121_l1b), 3),
        "day_over_measured_all": round(float(Fr(80, 100) / all_l1), 3),
        "filter_stacks_L1b": [0.214, 0.283],
        "correct_frame_range_L1": [float(lo), float(hi)],
    },
    "positions": {
        "day": {"reading": "0.80 is a property of the full gene set and the 0.23 an artefact of a curated subset",
                "holds": "his gene-set arithmetic is right (6,946 = 34.05%, 1.516); the gene-set effect has his sign on both "
                         "assemblies (+31% on hg38, +14% on T2T); CSAC did select on alignment quality and coverage"},
        "critic": {"reading": "a correct extraction gives about 0.27 on all genes and 0.21-0.24 on one2one genes",
                   "holds": "0.80 is 2.95x the measured all-gene value; no correct-frame computation reaches it (0.15-0.45); "
                            "all 32 filter stacks sit at 0.214-0.283; Day's own two single-SNV figures imply N/S 3.55 against "
                            "a measured 3.34, and his full stack (0.64) is already below his 0.65 floor"},
    },
    "notes": "Data-check object; no verdict moves. What Day's pipeline did to reach 0.80 cannot be settled without his code, "
             "gene list or per-gene table (unreleased; DN1 internal stays pending), but that is DN1's internal verdict, not "
             "this object's measurement: the genome-wide value and its sensitivity to gene set and filters are measured twice "
             "(L1, L1b). Day's '6,946 thrown out' sets his 20,400 against CSAC's 13,454; CSAC's own start was 16,045 genes, "
             "of which its curation removed 2,591 (16.2%). L1's 0.207 is the one2one value on hg38/panTro5; the T2T value "
             "is 0.238 (L1b).",
})
