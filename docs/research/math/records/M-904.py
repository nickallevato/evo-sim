#!/usr/bin/env python3
"""M-904 record (derivation, inference): from the mesa pattern to the mechanism (sigillation, FM10).

Object: docs/research/math/objects.yaml M-904 (inference, derivation). Day's step (ROOT-FM q4 = FM7 q1, sigillation,
hedged by Q170; ROOT-FM q5 = FM10 q1, "neither natural selection nor neutral diffusive drift") needs the implicit
premise that neutral diffusive drift implies a uniform per-window rate. The rule-N grep finding is quoted as recorded
in claim ROOT-FM and repeated on quotes-day.md: "uniform-rate" occurs once, in the FM3 sentence. The R4 FM results
are read as committed (no rerun): the pre-registered discriminating cells P3 (phi_res H/C 1.11, below Day's > 3),
P4 (phi_HC 1.81, below Day's > 10), P5 (null reproduces 12.4 / 18 = 0.69 of human mesas, above the critics' 0.5) and
P7 (1.25% of DHC in human mesas, below the critics' 20%) are each asserted against both sides' registered cuts; all
four fall on the critics' side. The single Day-side cell, chrX F1 100 kb, is asserted as printed (R 18.16 / 4.84 =
3.76 on hs1; 16.38 / 4.84 = 3.39 chimp-referenced; both above Day's > 3, consistent with the printed figures within
rounding) and without its one orthologous window (1.16, 1.11). Both positions on relictation are recorded: the
object statement says relictation contradicts the premise; the claim file says FM10's "diffusive" excludes
relictation, so N2b is not triggered. Stdlib only.

Run: research/.venv/bin/python -I docs/research/math/records/M-904.py [--write]
Without --write it checks that M-904.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
RFM = CL + "ROOT-fm-day-mesas-sigillation.md"
FM7 = CL + "FM7-sigillation-lineage-specific-mesas.md"
FM10 = CL + "FM10-neither-selection-nor-drift-viable.md"
QD = "docs/research/sources/quotes-day.md"
R4 = "research/checks/results/R4-FM.md"


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


def ratio_range(a, b, dp=2):
    """Bounds of a / b when a and b are printed to dp decimals."""
    h = 0.5 * 10 ** -dp
    return (a - h) / (b + h), (a + h) / (b - h)


# ---- the source sentences ---------------------------------------------------------------------------
SIG = ("I propose the term sigillation for the hypothesis that some of these mesa regions represent deliberate genomic "
       "modification: discrete engineering events that wrote contiguous blocks of change into one dominate lineage.")
held(RFM, SIG); held(FM7, SIG)                                        # ROOT-FM q4 = FM7 q1 (Q168, para 6)
HEDGE = held(FM7, "\"Sigillation is no more proof of IGM than relictation is. But it may be initial evidence of IGM.\"")  # Q170
FMQ = ("What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable "
       "candidates. And there is no need to take my word for anything with regards to this, all of the data has been "
       "provided by the T2T Primate Consortium (Yoo et al. 2025) aligned with Progressive Cactus (Armstrong et al. 2020).")
held(RFM, FMQ); held(FM10, FMQ)                                       # ROOT-FM q5 = FM10 q1 (Q171, para 8)
PREM = held(FM10, "The step from FM3-FM5 requires a premise of the form \"neutral diffusive drift implies a uniform "
                  "per-window rate and a lineage-symmetric excess\".")
AFTER = held(RFM, "sigillation is introduced after the data, so the data do not test it.")
DAYPAT = held(RFM, "(4) A lineage-asymmetric excess confined to contiguous blocks is a pattern uniform-rate neutral theory "
                   "does not predict, and the critics' own k = mu argument assumes a uniform mutation rate.")

# ---- the rule-N grep, as recorded and repeated on quotes-day.md ----------------------------------------------
GREP = held(RFM, "The only occurrence of \"uniform-rate\" is the FM3 sentence itself (Q164); no harvested Day text "
                 "states, defends or uses that premise.")
RELIC = held(RFM, "His own material does carry time-varying drift (relictation, Z23188201, \"technically a form of "
                  "non-diffusive drift ... produced by a very different and much faster process\")")
EXCL = held(RFM, "but FM10's wording is \"neutral diffusive drift\", which excludes relictation")
N2B = held(RFM, "So N2b (\"needs a premise the author's own text contradicts\") is not triggered; the open question is "
                "N2d (\"stronger than the premises support\"), which needs a deliberate call because the post states no "
                "premise at all.")
OWNER = held(FM10, "Owner decision 2026-10-10: stays pending until Day releases his method/window/statistic")
qd = (ROOT / QD).read_text(encoding="utf-8")
assert qd.count("uniform-rate") == 1                                  # one occurrence in the Day quotes file ...
line = next(l for l in qd.splitlines() if "uniform-rate" in l)
assert "more than 80 times more variable than a uniform-rate process predicts" in line   # ... the FM3 sentence (Q164)

# ---- R4 FM pre-registered discriminating cells (as committed) ------------------------------------------------
P3 = held(R4, "| P3 het-μ null | φ_res H/C > 3 | φ_res(H) ≤ 0.3 φ(H); ratio in [0.5, 2] | φ_res 1.5-15; ratio 0.6-1.6 | "
              "F2 100 kb: 2.68 vs 4.29 bound; ratio 1.11 | **critic hit, Day miss**; audit hit |")
held(R4, "| auto | 100 kb | F2 | 9,520 | 14.3 | 14.7 | 12.5 | 38.0 | **2.68 / 2.41** | **1.81** |")
p3 = near(2.68 / 2.41, 1.11, 0.005)
near(0.3 * 14.3, 4.29, 1e-9)
assert p3 <= 3 and 0.5 <= p3 <= 2 and 2.68 <= 0.3 * 14.3              # Day miss (> 3); critic hit on both parts

P4 = held(R4, "| P4 human specificity | φ_HC > 10; H/C-specific > 3 | φ_HC 1-5; ratio [0.5, 2] | 0.6-1.7 | φ_HC 1.81;")
held(R4, "**critic hit on φ_HC; Day miss**")
held(R4, "specific mesas 0 / 0 (F2 100 kb; ratio undefined), 2 / 2 (F2 10 kb), 1 / 8 and 35 / 70 (F0)")
phi_hc = 1.81
assert not phi_hc > 10 and 1 <= phi_hc <= 5                          # Day miss; critic hit
assert all(h / c <= 1 for h, c in ((2, 2), (1, 8), (35, 70)))         # specific-mesa ratio <= 1 wherever defined

P5 = held(R4, "| P5 null reproduction | M/obs < 0.2 | ≥ 0.5 | 0.4-1.2 | 12.4 / 18 = 0.69; uniform null 0 | **critic hit, "
              "Day miss**")
p5 = near(12.4 / 18, 0.69, 0.005)
assert not p5 < 0.2 and p5 >= 0.5                                     # Day miss; critic hit

P7 = held(R4, "| P7 FM8b \"dominant source\" | > 50% of DHC in H mesas | < 20% | 2-15% | 1.25% (F0 100 kb), 1.3-2.5% "
              "elsewhere | **critic hit, Day miss**")
p7 = (1.25, 1.3, 2.5)
assert all(not x > 50 and x < 20 for x in p7)                          # Day miss; critic hit in every cell

cells = {"P3": "critic", "P4": "critic", "P5": "critic", "P7": "critic"}
assert all(v == "critic" for v in cells.values()) and len(cells) == 4

# ---- the single Day-side cell: chrX F1 100 kb ---------------------------------------------------------------
CX = held(R4, "| chrX* | 100 kb | F1 | 1,328 | **44.9** | **18.0** | 29.8 | 59.3 | **18.16 / 4.84 (3.76)** | 4.54 |")
M3 = held(R4, "| M3 chrX F1 100 kb | R > 3 persists | R ≤ 1.5 | 16.38 / 4.84, **R 3.39** [3.76]; 10 kb R 1.51 [2.47]; "
              "1 Mb 1.24 | **Day hit, critic miss**")
T2A = held(R4, "R 3.39 → **1.11** (top window chimp chrX 58.1 Mb carries 70% of Σr_H²; rep share 0.99)")
T2B = held(R4, "3.76 → **1.16** (72% of Σr_H²)")
ONE = held(R4, "The chrX F1 Day-side cell is one orthologous window in the chrX centromeric transition region, on both "
               "references; without it chrX is symmetric (1.11-1.16).")
NOTREG = held(R4, "chrX rows are reported, not registered discriminating cells (P3 was registered on autosomes).")
r_hs1, r_chimp = 3.76, 3.39
lo, hi = ratio_range(18.16, 4.84); assert lo <= r_hs1 + 0.005 and r_hs1 - 0.005 <= hi   # 3.752 printed as 3.76: within rounding
lo, hi = ratio_range(16.38, 4.84); assert lo <= r_chimp + 0.005 and r_chimp - 0.005 <= hi  # 3.384 printed as 3.39
near(18.16 / 4.84, 3.752, 0.0005); near(16.38 / 4.84, 3.384, 0.0005)
assert r_hs1 > 3 and r_chimp > 3                                      # crosses Day's registered P3 cut on both references
assert all(r <= 1.5 for r in (1.11, 1.16))                            # without the one window: inside the critics' bound

finish({
    "object": "M-904",
    "inputs": [
        {"name": "Day's step", "value": "sigillation (hedged, Q170); neither selection nor neutral diffusive drift viable",
         "cite": "ROOT-FM q4 = FM7 q1 (Q168); ROOT-FM q5 = FM10 q1 (Q171)"},
        {"name": "rule-N grep", "value": "'uniform-rate' only in Q164 (FM3)", "cite": "claim ROOT-FM (2026-10-10); quotes-day.md count 1"},
        {"name": "R4 FM cells P3, P4, P5, P7", "value": {"P3_phi_res_ratio": 1.11, "P4_phi_HC": 1.81, "P5_null_over_obs": 0.69,
                                                        "P7_DHC_share_pct": [1.25, 1.3, 2.5]},
         "cite": "research/checks/results/R4-FM.md 'Against the predictions' table (read only, no rerun)"},
        {"name": "chrX F1 100 kb", "value": {"hs1": [18.16, 4.84, r_hs1], "chimp_ref": [16.38, 4.84, r_chimp],
                                             "without_top_window": {"hs1": 1.16, "chimp_ref": 1.11}},
         "cite": "R4-FM.md headline table, M3, T2a, T2b"},
    ],
    "values": {
        "registered_cells": {"P3": {"value": round(p3, 3), "day_cut": "> 3", "critic_cut": "[0.5, 2] and <= 0.3 phi(H)", "side": "critic"},
                             "P4": {"value": phi_hc, "day_cut": "> 10", "critic_cut": "1-5", "side": "critic"},
                             "P5": {"value": round(p5, 3), "day_cut": "< 0.2", "critic_cut": ">= 0.5", "side": "critic"},
                             "P7": {"value_pct": list(p7), "day_cut": "> 50%", "critic_cut": "< 20%", "side": "critic"}},
        "cells_on_critic_side": 4,
        "chrX_F1_100kb": {"R_hs1_printed": r_hs1, "R_hs1_from_printed_parts": round(18.16 / 4.84, 3),
                          "R_chimp_printed": r_chimp, "R_chimp_from_printed_parts": round(16.38 / 4.84, 3),
                          "day_side": True, "without_one_window": [1.11, 1.16], "registered": False},
        "uniform_rate_occurrences_in_quotes_day": 1,
    },
    "positions": {
        "day": {"reading": "a lineage-asymmetric excess in contiguous blocks is a pattern uniform-rate neutral theory does "
                           "not predict; sigillation is an open, hedged hypothesis; the data are public",
                "holds": "chrX F1 100 kb crosses the registered > 3 cut on both references (3.76, 3.39); the hedge "
                         "('initial evidence') is real; FM10 invited a replication that was workable"},
        "critic": {"reading": "a pattern both selection and drift can contain excludes neither; sigillation was introduced "
                              "after the data, so the data do not test it",
                   "holds": "all four registered discriminating cells (P3, P4, P5, P7) fall on the critics' side; the "
                            "chrX cell is one orthologous centromeric-transition window, 1.11-1.16 without it"},
        "relictation": {"object_statement": "Day's relictation (time-varying, non-diffusive drift) contradicts the "
                                            "uniform-rate premise",
                        "claim_file": "FM10 says 'neutral diffusive drift', which excludes relictation, so N2b is not "
                                      "triggered; N2d is open and FM10 internal stays pending by owner decision"},
    },
    "notes": "The step from the mesa pattern to 'neither selection nor drift' rests on a premise no harvested Day text "
             "states (one 'uniform-rate' occurrence, in Q164 itself). On the committed R4 FM results the pre-registered "
             "discriminating cells all fall on the critics' side; the only Day-side cell is unregistered (chrX) and is "
             "one window. The printed 3.76 and 3.39 are 0.008 and 0.006 above the ratio of their printed parts (3.752, "
             "3.384), inside the rounding of those parts; the ratios were taken from unrounded values. The object "
             "statement's 'which Day's own relictation contradicts' is stronger than claim ROOT-FM, which finds N2b not "
             "triggered because FM10 names diffusive drift; both are recorded and no verdict moves (FM10 internal "
             "pending, owner 2026-10-10).",
})
