#!/usr/bin/env python3
"""M-008 record (identity, data-check): the required fixation count by version, and the measured count it sits on.

Object: docs/research/math/objects.yaml M-008 (identity, data-check). Day's required count per lineage in three
versions: 2019, 15e6 per lineage (Q05); 2025, "~40 million single-nucleotide variants; ~20 million fixations" (Q12);
MITTENS 3.0, the SNV-only 17.5e6 with shortfalls 91,600x at 1,322 gen/fix and 7,271x at 105 (Q16, Q17). Critic side:
Sparky_6_4's KITTENS achievable 17.9e6 against 17.5e6 (RE-08), and the claim-file note that 17.5e6 is 83% of the
measured events per lineage. Every input is read from a committed file (quotes files, R4 write-ups, a cited record)
and checked verbatim; every number in the object statement is asserted, including the paper's rounded ones.

Inputs: CSAC 2005 counts and fixed share (quotes-literature.md l.85, l.94, l.97; parameters divergence.*); the
measured event counts of R4-GAP07b (hg38 vs panTro6) and R4-GAP07t (T2T); the KITTENS linear-scaling value of
record M-006 (cited, not recomputed). Exact rationals (stdlib). Runs in well under a second.

Run: research/.venv/bin/python -I docs/research/math/records/M-008.py [--write]
Without --write it checks that M-008.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
QL = "docs/research/sources/quotes-literature.md"
QC = "docs/research/sources/quotes-critics.md"
RES = "research/checks/results/"
REC = "docs/research/math/records/"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
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
Q05 = held(QD, "it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another "
               "15,000,000 mutations to become fixed in the chimpanzee population")
Q12 = held(QD, "Genetic divergence: ~40 million single-nucleotide variants; ~20 million fixations required on human "
               "lineage. Time available: 6–7 million years at 20 years/generation = 300,000–350,000 nominal generations.")
Q16 = held(QD, "Restricting to the approximately 35 million SNVs and apportioning symmetrically: 17.5 million required "
               "fixations on the human lineage.")
Q17 = held(QD, "At 1,322 gen/fix (non-mutator): 191 achievable. Shortfall: 91,600×. At 105 gen/fix (mutator): 2,407 "
               "achievable. Shortfall: 7,271×.")
RE08 = held(QC, "the achievable number (17.9 million) is about equal to the required number (17.5 million).")
RE09 = held(QC, "I present this as an illustration, not as a proof that adaptive fixations scale linearly with "
                "mutation rate.")
CSAC_N = held(QL, "constituting approximately thirty-five million single-nucleotide changes, five million "
                  "insertion/deletion events, and various chromosomal rearrangements")
CSAC_F = held(QL, "Single-nucleotide substitutions occur at a mean rate of 1.23% between copies of the human and "
                  "chimpanzee genome, with 1.06% or less corresponding to fixed divergence between the species.")
G07B = held(RES + "R4-GAP07b-alignment.md", "Day's 17.5 M per lineage is 83% of the measured events per lineage (21.05 M)")
G07B_T = held(RES + "R4-GAP07b-alignment.md", "| **Total events** | **42.10 M** | 21.05 M per lineage (total / 2) |")
G07T = held(RES + "R4-GAP07t.md", "| events per lineage | 21.05 M | **24.14 M** | +14.7% |")

SNV, INDEL = 35_000_000, 5_000_000                      # CSAC 2005 (CSAC_N)
FIXED_SHARE = Fr(106, 123)                              # 1.06% / 1.23% (CSAC_F)

# ---- 2019: 15e6 per lineage, 30e6 in total ----------------------------------------------------------------
total_2019 = 2 * 15_000_000
assert total_2019 == 30_000_000
fixed_snv = SNV * FIXED_SHARE
near(float(FIXED_SHARE), 0.862, 0.0005)
near(float(fixed_snv), 30.2e6, 0.05e6)                  # 35e6 x 0.862 = 30.2e6 (polymorphism-corrected)
near(float(fixed_snv / 2), 15.1e6, 0.05e6)              # per lineage, close to the 2019 15e6

# ---- 2025: (35e6 SNV + 5e6 indel) / 2 = 20e6; window 300,000-350,000 generations ----------------------------
events = SNV + INDEL
assert events == 40_000_000 and events // 2 == 20_000_000
assert (6_000_000 // 20, 7_000_000 // 20) == (300_000, 350_000)
# Q12 labels the 40e6 as "single-nucleotide variants"; CSAC's 40e6 is 35e6 SNVs plus 5e6 indel events.

# ---- MITTENS 3.0: SNV-only 17.5e6 and its two shortfalls -----------------------------------------------------
req = Fr(SNV, 2)
assert req == 17_500_000
f_nm = Fr(252_000, 1_322)
near(float(f_nm), 190.6, 0.05)                          # the paper rounds to 191 achievable
short_nm = req / 191
near(float(short_nm), 91_623, 0.5)                      # paper 91,600 (rounded)
assert round(float(short_nm), -2) == 91_600
short_nm_unrounded = req / f_nm
near(float(short_nm_unrounded), 91_806, 0.5)            # with F unrounded: 0.2% above the paper
assert Fr(252_000, 105) == 2_400                        # 252,000 / 105 = 2,400; the paper prints 2,407 (G_f 104.7)
near(252_000 / 2_407, 104.7, 0.01)                     # 104.69
short_m = req / 2_407
near(float(short_m), 7_270.5, 0.05)                     # 7,270.46 -> 7,270; paper 7,271
assert int(short_m) == 7_270
near(17_500_000 / (252_000 / 104.7), 7_271, 0.5)        # the paper's 7,271 is 17.5e6 at G_f = 104.7 unrounded

# ---- KITTENS: achievable 17.9e6 against 17.5e6 (M-006, linear supply scaling) ------------------------------
f_lin = near(cited("M-006", "F_linear"), 17.9e6, 0.05e6)
ratio_lin = near(cited("M-006", "F_linear_over_17.5e6"), 1.022, 0.001)

# ---- the measured events per lineage the 17.5e6 is compared with -------------------------------------------
ev_g07b = 21_050_000
ev_g07t = 24_140_000
share_g07b = near(17_500_000 / ev_g07b, 0.831, 0.001)  # "83% of the measured events per lineage" (GAP-07b)
share_g07t = near(17_500_000 / ev_g07t, 0.725, 0.001)  # on the T2T count (GAP-07t): 72%
near(ev_g07t / ev_g07b, 1.147, 0.001)                   # +14.7%

finish({
    "object": "M-008",
    "inputs": [
        {"name": "Day's requirement by version", "value": {"2019": "15e6 per lineage", "2025": "~20e6 of ~40e6",
                                                           "3.0": "17.5e6 of ~35e6 SNVs"}, "cite": "Q05, Q12, Q16"},
        {"name": "Day's shortfalls", "value": {"1322": "191 achievable, 91,600x", "105": "2,407 achievable, 7,271x"},
         "cite": "Q17"},
        {"name": "CSAC 2005 counts", "value": {"SNV": SNV, "indel_events": INDEL}, "cite": "quotes-literature.md l.85, l.97"},
        {"name": "CSAC fixed share", "value": "1.06% / 1.23% = 0.862", "cite": "quotes-literature.md l.94"},
        {"name": "measured events per lineage", "value": {"GAP-07b hg38/panTro6": ev_g07b, "GAP-07t T2T": ev_g07t},
         "cite": "R4-GAP07b-alignment.md, R4-GAP07t.md"},
        {"name": "KITTENS linear-scaling achievable", "value": f_lin, "cite": "record M-006 F_linear (cited)"},
    ],
    "values": {
        "required_2019_total": total_2019,
        "fixed_snv_corrected": round(float(fixed_snv)),
        "fixed_snv_corrected_per_lineage": round(float(fixed_snv / 2)),
        "required_2025_per_lineage": events // 2,
        "required_3_0_per_lineage": int(req),
        "F_nonmutator": round(float(f_nm), 2),
        "shortfall_at_191": round(float(short_nm), 1),
        "shortfall_at_190.62": round(float(short_nm_unrounded), 1),
        "shortfall_at_2407": round(float(short_m), 2),
        "kittens_achievable": f_lin,
        "kittens_over_required": ratio_lin,
        "share_of_events_gap07b": round(share_g07b, 4),
        "share_of_events_gap07t": round(share_g07t, 4),
    },
    "positions": {
        "day": {"reading": "each version halves a divergence count to a per-lineage requirement; the SNV-only 17.5e6 is a "
                           "concession and still gives 91,600x",
                "holds": "every identity reproduces from Day's inputs: 30.2e6 x 1/2 = 15.1e6 (2019), 40e6/2 = 20e6 (2025), "
                         "35e6/2 = 17.5e6, 17.5e6/191 = 91,623 (91,600), 17.5e6/2,407 = 7,270 (7,271 at G_f 104.7). "
                         "17.5e6 brackets the measured fixed-event count (R4-GAP07b 16.4-18.1 M)"},
        "critic": {"reading": "17.5e6 is below the measured events per lineage; 17.9e6 achievable is an illustration",
                   "holds": "17.5e6 is 83% of 21.05 M events per lineage (GAP-07b) and 72% of 24.14 M on the T2T count "
                            "(GAP-07t); 17.9e6 reproduces only under linear supply scaling (M-006), which RE-09 itself "
                            "disclaims"},
    },
    "notes": "Identity object; no verdict moves. Q12 calls the 40e6 'single-nucleotide variants'; the 35e6 + 5e6 split is "
             "CSAC's (SNVs plus indel events), and the 2025 halving reproduces only on that split. The paper's 2,407 "
             "achievable implies G_f 104.7, not the printed 105 (252,000 / 105 = 2,400); its 7,271 follows from that. The "
             "critic-side '83%' (claim A3b) is on the hg38/panTro6 count; on the T2T count it is 72%. Whether 17.5e6 is the "
             "right requirement (polymorphism, indels, structural events) is M-010 and M-011, not this object.",
})
