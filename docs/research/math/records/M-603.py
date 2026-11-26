#!/usr/bin/env python3
"""M-603 record (lookup): s = 0.001 attributed to Zeng et al. 2021 as the beneficial mean in humans.

Object: docs/research/math/objects.yaml M-603 (parameter, lookup). The record holds, verbatim with a locator, Day's
attribution (F3a q1, Education post para 15; Q44 in the Q&A), Zeng 2021's sentences giving ~0.001 (quotes-literature
Zeng2021; F3a q2) and its negative-selection framing, the parameters.yaml entry (sign negative, verified: true) and
R4 F3a's finding that no held Zeng sentence gives a beneficial mean. The Zeng paper's raw text is not in this
checkout's sources/raw/; the "none beneficial" finding rests on R4 F3a's scan and review, quoted here, and cannot be
repeated by this record. Arithmetic: latency (2/s) ln(2Ne) at 0.001 and 0.01 (19,807, 1,981; M-601) and the band of s
for which latency stays within 25% of the 0.001 value (0.0008 to 0.00133).

Run: research/.venv/bin/python -I docs/research/math/records/M-603.py [--write]
Without --write it checks that M-603.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
F1A = "docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md"
F3A = "docs/research/claims/F3a-s-0-001-zeng-2021-misread.md"
QD = "docs/research/sources/quotes-day.md"
QL = "docs/research/sources/quotes-literature.md"
PY = "docs/research/parameters.yaml"
R4 = "research/checks/results/R4-F3a.md"


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


# ---- Day ------------------------------------------------------------------------------------------
DAY = held(F3A, "at s = 0.001 (the empirical mean for beneficial mutations in humans from Zeng et al. 2021)")  # F3a q1
DAY_QA = held(QD, "s = 0.001 (selection coefficient, Zeng et al 2021)")                                     # Q44
held(F1A, DAY_QA)                                                                                           # F1a q3

# ---- Zeng 2021 (as held in quotes-literature; raw paper not in this checkout) ---------------------
Z_RES = "We detect widespread signatures of negative selection in the genetic architecture across 155 complex " \
        "traits with a predicted mean selection coefficient of ~0.001"
held(QL, Z_RES); held(F3A, Z_RES)                                 # Results, "Evolutionary inference"; F3a q2
Z_ABS = held(QL, "about 1% of human genome sequence are mutational targets with a mean selection coefficient of ~0.001")  # Abstract
Z_NEG = held(QL, "Since we only detected signatures of negative selection in real traits, our evolutionary simulations "
                 "focused on the models of negative selection.")  # Results, simulations
Z_CAT = held(QL, "which was significantly higher than that of 0.0005 for physical measures")               # Fig. 5 discussion
PY_S = held(PY, "s_zeng_2021: {value: 0.001, sign: negative, note: \"mean |s| of variants affecting complex traits under "
                "negative selection; positive selection only as a simulation sensitivity scenario — Day uses as "
                "beneficial\", source: Zeng2021, verified: true")  # selection.s_zeng_2021
P2 = held(R4, "6 sentences with a numeric s (5 in the first run, which missed Z4); none mentions positive or beneficial "
              "selection.")                                       # R4 F3a P2
NOBEN = held(R4, "Zeng reports no measured beneficial mean.")
REPO = held(R4, "the repo holds no sourced human beneficial mean s to put in its place")
P6 = held(R4, "Latency ~ 1/s: replacements outside s in [0.0008, 0.00133] move it > 25%")
FID = held(F3A, "fidelity: misread")
NE = 1.0e4; held(PY, "Ne_modern_human: {value: 1.0e4")           # population.Ne_modern_human

# ---- the lookup -----------------------------------------------------------------------------------
num = lambda q: float(q.rsplit("~", 1)[1])
assert num(Z_RES) == num(Z_ABS) == 0.001                          # Zeng's ~0.001, twice
assert "negative selection" in Z_RES and "negative selection" in Z_NEG and "sign: negative" in PY_S
assert "beneficial" in DAY and "beneficial" not in Z_RES + Z_ABS + Z_NEG
assert "155 complex traits" in Z_RES
near(0.001 / 0.0005, 2.0, 0)                                      # physical-measure category mean (0.0005), half
assert FID.endswith("misread")

# ---- latency arithmetic (M-601) and the 25% band -------------------------------------------------
lat = lambda s: (2 / s) * math.log(2 * NE)
near(lat(0.001), 19807, 0.5); near(lat(0.01), 1981, 0.5)
near(lat(0.01) / lat(0.001), 0.1, 1e-12)                          # 1/s scaling
lo, hi = 0.001 / 1.25, 0.001 / 0.75                               # latency within +-25% of the 0.001 value
near(lo, 0.0008, 1e-12); near(hi, 0.00133, 5e-6)
for s in (lo, hi):
    near(abs(lat(s) / lat(0.001) - 1), 0.25, 1e-12)
for s in (0.00079, 0.00134):
    assert abs(lat(s) / lat(0.001) - 1) > 0.25
near(lat(0.0005), 39614, 0.5); near(lat(0.0005) / (4 * NE), 0.990, 0.0005)     # R4 F3a P6: ratio 0.990 vs 4Ne
assert "[0.0008, 0.00133]" in P6

finish({
    "object": "M-603",
    "inputs": [
        {"name": "Day's attribution", "value": DAY, "cite": "F3a q1 (Education post para 15); Q44 (F1a q3)"},
        {"name": "Zeng 2021", "value": [Z_RES, Z_ABS, Z_NEG], "cite": "quotes-literature Zeng2021 (Results; Abstract; Results, simulations); F3a q2"},
        {"name": "parameter", "value": 0.001, "cite": "parameters selection.s_zeng_2021 (sign negative, verified: true)"},
        {"name": "scan of Zeng's numeric-s sentences", "value": P2, "cite": "R4 F3a P2 (raw Zeng text not in this checkout)"},
    ],
    "values": {
        "zeng_mean_s": 0.001, "zeng_sign": "negative (purifying)", "zeng_beneficial_mean": None,
        "day_label": "beneficial", "fidelity": "misread",
        "latency": {"0.001": round(lat(0.001), 1), "0.01": round(lat(0.01), 1), "0.0005": round(lat(0.0005), 1)},
        "s_band_latency_within_25pct": [round(lo, 6), round(hi, 6)],
    },
    "positions": {
        "day": {"reading": "0.001 is Zeng's empirical mean, a defensible order of magnitude for trait-affecting variants",
                "holds": "Zeng does report a mean |s| of ~0.001; category means 0.0005-0.0010"},
        "critic": {"reading": "Zeng measures negative selection; the beneficial label is a misread and the sign matters",
                   "holds": "no held Zeng sentence gives a beneficial mean; the repo holds no sourced human beneficial s"},
    },
    "notes": "The number is Zeng's; the label is not: Zeng's ~0.001 is a mean |s| under negative selection, and Day calls "
             "it the empirical mean for beneficial mutations. Latency scales as 1/s, so the 19,807 moves by more than "
             "25% for any s outside 0.0008-0.00133; with no sourced beneficial mean in the repo the materiality stays "
             "undetermined (R4 F3a). The steady-state rate does not depend on latency (F1). The 'none beneficial' "
             "finding rests on R4 F3a's scan and review; the Zeng raw text is not in this checkout's sources/raw/.",
})
