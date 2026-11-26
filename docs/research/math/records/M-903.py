#!/usr/bin/env python3
"""M-903 record (derivation, inference): one mesa against two genome-wide ceilings (FM5).

Object: docs/research/math/objects.yaml M-903 (inference, derivation). Day's sentence (ROOT-FM q3 = FM5 q1, Q166)
gives no count, unit, window or ceiling value; the record asserts that (no digit in the sentence) and quotes the
claim files' notes that the units and Day's Haldane figure are not given. Day's own comparison is therefore
unscoreable as stated (rule F: unverifiable until he releases the mesa counts). What is held is the audit's reading
(R4 FM, pre-registered in fm_mesa_replication.py): MITTENS ceiling 191 (F_max 190.6, cited from M-713) and Haldane
252,000 / 300 = 840 per lineage (the 300 cited from M-801). The record asserts 840 > 191 (so "exceeds both" reduces
to exceeding 840) and the held R4 FM counts at F0 100 kb, human 32, chimp 29, bonobo 31 and gorilla 19 mesas above 840, which
make the sentence literally true and non-discriminating. Haldane's cost bounds selected substitutions, so the
comparison presupposes the mesa is selected; both positions are quoted. Stdlib only.

Run: research/.venv/bin/python -I docs/research/math/records/M-903.py [--write]
Without --write it checks that M-903.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, re, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
RFM = CL + "ROOT-fm-day-mesas-sigillation.md"
FM5 = CL + "FM5-one-mesa-exceeds-mittens-and-haldane.md"
R4 = "research/checks/results/R4-FM.md"
SCR = "research/checks/fm_mesa_replication.py"
RAW = "research/checks/results/raw/fm_analyse.json"
PY = "docs/research/parameters.yaml"
M713 = "docs/research/math/records/M-713.json"
M801 = "docs/research/math/records/M-801.py"


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


# ---- the source sentence and what it does not give ----------------------------------------------------------
Q = ("A single mesa on a single chromosome shows an excess of human-lineage substitutions that exceeds both the "
     "MITTENS fixation ceiling and the maximum that natural selection can theoretically fix across the entire genome "
     "according to Haldane.")
held(RFM, Q); held(FM5, Q)                                            # ROOT-FM q3 = FM5 q1 (Q166, 2026-10-10, para 4)
assert not re.search(r"\d", Q)                                        # no count, window, unit or ceiling value
NOUNITS = held(RFM, "\"human-lineage substitutions\" in one mesa vs (a) \"the MITTENS fixation ceiling\" and (b) "
                    "Haldane's genome-wide maximum for selection (no counts, units not stated: SNV vs bp, event vs base)")
NOHALD = held(RFM, "the \"maximum that natural selection can theoretically fix across the entire genome\" figure is not "
                   "given in the post: unverifiable")
NEITHER = held(FM5, "Day states neither figure nor units.")
SELECTED = held(FM5, "comparing a regional count with a genome-wide selection ceiling presupposes the mesa is selected.")
UNITS = held(RFM, "(4) One mesa against a genome-wide Haldane maximum is a units step.")
KMU = held(RFM, "(3) Neutral theory predicts k = mu locally, so a high-mu mesa produces excess substitutions on every "
                "lineage; only a human-specific excess discriminates, and the post gives no per-lineage numbers")
DAY_TRUE = held(FM5, "In support (Day): the sentence is literally true on the public data.")

# ---- the audit's ceilings (R4 FM pre-registration), cited from M-713 and M-801 --------------------------------
held(SCR, "FM5 units: MITTENS 3.0 achievable fixations 191 (252,000 / 1,322; parameters.yaml) and Haldane's")
held(SCR, "252,000 / 300 = 840 per lineage.")
held(PY, "day_2026: {value: 252000, source: Z23003785")               # generations_available.day_2026
held(PY, "gens_per_substitution: {value: 300, source: Haldane1957, verified: \"via Nunney2003\"}")
held(M801, "300 generations per beneficial substitution")             # M-801 (the 300, as Nunney 2003 reports it)
FMAX = json.loads((ROOT / M713).read_text(encoding="utf-8"))["values"]["F_max_d1"]   # 190.62 (M-713)
MITTENS = math.ceil(FMAX)
HALDANE = Fr(252_000, 300)
assert MITTENS == 191 and HALDANE == 840
assert HALDANE > MITTENS                                              # exceeding 840 implies exceeding 191: one binding ceiling
near(float(HALDANE / MITTENS), 4.40, 0.005)

# ---- the held R4 FM counts (F0 100 kb; read only, no rerun) -----------------------------------------------------
ROW = held(R4, "| F0 100 kb | 33 | 31 | 33 | 19 | 49% (0.6%) | 1 / 8 | 20-23 | 0 | 33 / 32 | 31 / 29 | 1.25% |")
P6 = held(R4, "F0 100 kb: H 32, C 29 (ratio 0.91) | **hit for both**: Day's sentence is literally true; it is equally "
              "true of the chimp lineage.")
held(R4, "\"> 840\" is the informative count (F0 32/33 H; F2 10/18)")
cells = [c.strip() for c in ROW.strip("|").split("|")]
h_mesas, c_mesas = int(cells[1]), int(cells[2])
h191, h840 = map(int, cells[9].split(" / ")); c191, c840 = map(int, cells[10].split(" / "))
assert (h_mesas, h191, h840, c_mesas, c191, c840) == (33, 33, 32, 31, 31, 29)
assert h840 >= 1                                                      # the literal sentence: some human mesa exceeds both
near(c840 / h840, 0.91, 0.005)                                        # non-discriminating: inside the critics' [0.5, 2]
assert 0.5 <= c840 / h840 <= 2
F2 = held(R4, "| F2 100 kb | 18 | 17 | 18 | 11 | 53% (0.78%) | 0 / 0 | 11-14 | 0 | 18 / 10 | 17 / 5 | 1.75% |")
f2 = [c.strip() for c in F2.strip("|").split("|")]
f2h, f2c = (tuple(map(int, f2[i].split(" / "))) for i in (9, 10))
assert f2h == (18, 10) and f2c == (17, 5) and f2c[1] / f2h[1] == 0.5   # F2 100 kb: 10 H vs 5 C above 840
ALL4 = held(R4, "32 human, 29 chimp, 31 bonobo and 19 gorilla mesas exceed 840 (F0 100 kb)")   # R4 FM verdict, FM5
raw = json.loads((ROOT / RAW).read_text(encoding="utf-8"))["mesa"]["F0|100kb"]   # committed run output (read only)
gt840 = {k: raw[k]["gt_haldane"] for k in "HCBG"}
assert gt840 == {"H": 32, "C": 29, "B": 31, "G": 19}
assert raw["H"]["gt_mittens"] == h191 and raw["C"]["gt_mittens"] == c191
max_x = {k: round(raw[k]["max_excess"]) for k in "HCBG"}
assert max_x["H"] > 20 * HALDANE and max(max_x.values()) == max_x["G"]  # largest human excess about 24x 840; gorilla's larger

finish({
    "object": "M-903",
    "inputs": [
        {"name": "Day's sentence", "value": "no count, unit, window or ceiling", "cite": "ROOT-FM q3 = FM5 q1 (Q166)"},
        {"name": "MITTENS ceiling", "value": MITTENS, "cite": "M-713.json F_max_d1 = 190.62, rounded up; fm_mesa_replication.py docstring"},
        {"name": "Haldane ceiling", "value": int(HALDANE), "cite": "parameters generations_available.day_2026 / haldane gens_per_substitution 300 (M-801)"},
        {"name": "R4 FM mesa counts above 191 / 840", "value": {"F0_100kb": {"H": [h191, h840], "C": [c191, c840]},
                                                              "F2_100kb": {"H": list(f2h), "C": list(f2c)},
                                                              "F0_100kb_above_840_all": gt840},
         "cite": "research/checks/results/R4-FM.md mesa table, P6 row and FM5 verdict; raw/fm_analyse.json"},
    ],
    "values": {
        "day_figures_given": False, "day_comparison_scoreable": False,
        "audit_ceilings": {"MITTENS": MITTENS, "Haldane": int(HALDANE), "ratio": round(float(HALDANE / MITTENS), 2)},
        "F0_100kb_mesas_above_840": {**gt840, "C_over_H": round(c840 / h840, 2)},
        "F0_100kb_max_mesa_excess": max_x,
        "literal_sentence_true_on_audit_reading": True, "human_specific": False,
    },
    "positions": {
        "day": {"reading": "a single mesa already exceeds what selection could fix genome-wide under Haldane and what "
                           "MITTENS allows",
                "holds": "on the audit's 191 / 840 reading the sentence is literally true: 32 of 33 human mesas exceed 840 "
                         "at F0 100 kb"},
        "critic": {"reading": "one mesa against a genome-wide maximum is a units step; Haldane bounds selected substitutions "
                              "only; a high-mu block gives excess on every lineage",
                   "holds": "Day gives no count, unit or ceiling, so his own comparison is unverifiable; on the audit's "
                            "reading 29 chimp, 31 bonobo and 19 gorilla mesas exceed 840 too, so the excess is not "
                            "human-specific"},
    },
    "notes": "Resolved as unscoreable on Day's own figures: the sentence has no numbers, so its comparison cannot be "
             "checked until the mesa counts, units and window are released (fidelity unverifiable, rule F). The audit's "
             "reading (191 and 840 per lineage over 252,000 generations; 252,000 is verified: false in parameters) is "
             "held from R4 FM, not re-run. Since 840 > 191 the MITTENS ceiling adds nothing once the Haldane one is "
             "passed. Comparing a mesa's substitution count with Haldane's cost presupposes the substitutions are "
             "selected (M-801); a neutral high-mutation block meets the same count on every lineage, which is what R4 "
             "FM finds.",
})
