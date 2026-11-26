#!/usr/bin/env python3
"""M-907 record (derivation, inference): dN/dS = 0.80 read as a measure of selection strength (DN4).

Object: docs/research/math/objects.yaml M-907 (inference, derivation). Day (DN4 q2, Q177 para 20) reads 1 - dN/dS as
the share of nonsynonymous mutations purifying selection removes: 1 - 0.80 = 0.20, "only about 20%" (and the
refresh's 1 - 0.7989 = 20.1%, Q187); from it he concludes (DN4 q1, para 21) "natural selection is not the primary
mechanism of adaptive evolution". The record asserts the removal arithmetic for 0.80 and for the published 0.23
(1 - 0.23 = 0.77; 77 / 20.1 = 3.8, Q187) and the held A2e-alpha band (bias-corrected Boyko 9.3%, 95% CL 5.4-12.8%;
Uricchio 0.135, HPD 0.096-0.17; DN4's "~9-13%"). Two quantities: 1 - dN/dS is purifying removal over all coding
sites; alpha is the adaptive share of fixed differences. Under the standard split dN/dS = omega_na + omega_a with
alpha = omega_a / (dN/dS), the same alpha fits either ratio, so the ratio does not fix the adaptive share; alpha's
lower bounds are above 0 (adaptive change occurs) and its upper bounds below 0.5 (most coding substitutions are not
adaptive) at 0.80 and at 0.23 alike. Both readings are recorded (rule N2d, own source). Stdlib, exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-907.py [--write]
Without --write it checks that M-907.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
DN4 = CL + "DN4-selection-not-primary-at-080.md"
DN1 = CL + "DN1-dnds-080-on-20400-genes.md"
A2E = CL + "A2e-ltee-as-ceiling.md"


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


# ---- the source sentences ---------------------------------------------------------------------------
Q1 = held(DN4, "At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution.")   # DN4 q1 (para 21)
Q2 = held(DN4, "A dN/dS of 0.80 means purifying selection is removing only about 20% of nonsynonymous mutations. At "
               "that level, selection is barely distinguishable from neutral evolution.")                # DN4 q2 (para 20)
P6 = held(DN4, "'If natural selection is purifying and removes harmful mutation then Ka/Ks should be well below 1.0'")  # para 6
N2D = held(DN4, "Charitable reading 'most coding substitutions are not selection-driven' follows from 0.80 but equally "
                "from 0.23 under neutral theory, so it does not carry the stated words")
TEXT = held(DN4, "his reading of 1 - dN/dS as the purged fraction is the textbook reading, and it is applied consistently "
                 "to both 0.23 and 0.80.")
NOT23 = held(DN1, "> Not 0.23. 0.80.")
Q187 = held(DN4, "Q187 arithmetic holds (1 - 0.7989 = 20.1%; 77/20.1 = 3.8) under the standard simplification.")
BAND = held(DN4, "human alpha estimates (A2e-alpha, bias-corrected ~9-13%) show it occurs")
BOYKO = held(A2E, "Boyko full text 9.3%, 95% CL 5.4-12.8%")
URI = held(A2E, "alpha 0.135 (95% HPD 0.096-0.17) against 0.076 for aMK")

# ---- the removal arithmetic -----------------------------------------------------------------------------
W_DAY, W_REF, W_REFRESH = Fr(80, 100), Fr(23, 100), Fr(7989, 10000)
assert 1 - W_DAY == Fr(1, 5)                                          # 0.20, "only about 20%"
assert 1 - W_REFRESH == Fr(2011, 10000)                               # 20.1% (Q187)
assert 1 - W_REF == Fr(77, 100)                                       # 0.77 removed at the published 0.23
near(77 / 20.1, 3.83, 0.005)                                          # Q187's 3.8x
near(float((1 - W_REF) / (1 - W_DAY)), 3.85, 1e-9)                    # same ratio at 0.80 exactly

# ---- the alpha band (A2e-alpha) ------------------------------------------------------------------------------
alpha = {"Boyko": (Fr(93, 1000), Fr(54, 1000), Fr(128, 1000)), "Uricchio": (Fr(135, 1000), Fr(96, 1000), Fr(17, 100))}
centrals = [a[0] for a in alpha.values()]
assert min(centrals) >= Fr(9, 100) and abs(max(centrals) - Fr(13, 100)) <= Fr(5, 1000)   # "~9-13%" (13.5 at the top)
assert all(lo > 0 for _, lo, _ in alpha.values())                     # adaptive substitutions occur (lower bounds > 0)
assert all(hi < Fr(1, 2) for _, _, hi in alpha.values())              # most coding substitutions are not adaptive

# ---- the ratio does not fix the adaptive share --------------------------------------------------------------
# standard split: dN/dS = omega_na + omega_a, alpha = omega_a / (dN/dS); the same alpha fits either ratio
for w in (W_DAY, W_REF):
    for a in centrals:
        w_a, w_na = a * w, (1 - a) * w
        assert w_a + w_na == w and 0 < w_a < w_na                     # non-adaptive part dominates at either ratio
assert 1 - W_DAY not in [a for t in alpha.values() for a in t]        # 0.20 removal is not an alpha value
assert all(not (lo <= 1 - W_DAY <= hi) for _, lo, hi in alpha.values())   # 0.20 lies outside both alpha intervals
w_a = {str(float(w)): [round(float(a * w), 4) for a in centrals] for w in (W_DAY, W_REF)}

finish({
    "object": "M-907",
    "inputs": [
        {"name": "dN/dS", "value": {"Day": 0.80, "Day_refresh": 0.7989, "published": 0.23},
         "cite": "DN4 q1, q2 (Q177); DN4 R-refresh (Q187); DN1 q ('Not 0.23. 0.80.')"},
        {"name": "alpha, bias-corrected", "value": {"Boyko": [0.093, 0.054, 0.128], "Uricchio": [0.135, 0.096, 0.17]},
         "cite": "claim A2e (R4 A2e-alpha paragraphs); DN4 external comment '~9-13%'"},
    ],
    "values": {
        "removed_at_0.80": 0.20, "removed_at_0.7989": 0.2011, "removed_at_0.23": 0.77,
        "removal_ratio_0.23_vs_0.80": 3.85, "Q187_77_over_20.1": round(77 / 20.1, 2),
        "alpha_band_central": [0.093, 0.135], "alpha_lower_bounds_above_0": True, "alpha_upper_bounds_below_0.5": True,
        "omega_a_under_alpha_band": w_a,
    },
    "positions": {
        "day": {"reading": "1 - dN/dS is the share purifying selection removes; at 0.80 that is about 20%, so selection is "
                           "barely distinguishable from neutral evolution in coding sequence",
                "holds": "the arithmetic: 1 - 0.80 = 0.20 (20.1% at 0.7989); the reading is the textbook one and Day "
                         "applies it to 0.23 (0.77) as well"},
        "critic": {"reading": "the genome-wide ratio averages purifying removal; it does not measure the adaptive share, "
                              "which is alpha",
                   "holds": "bias-corrected alpha is 9.3-13.5% (lower bounds 5.4% and 9.6%, above 0), so adaptive change "
                            "occurs; the same alpha fits 0.80 and 0.23, and 'most coding substitutions are not adaptive' "
                            "(alpha < 0.5) holds at either ratio, so it cannot carry 'selection is not the primary "
                            "mechanism of adaptive evolution'"},
    },
    "notes": "The 0.20 is purifying removal (Day's own para 6 definition); the conclusion in para 21 is about adaptive "
             "evolution, a different quantity (rule N2d, own source; DN4 internal non-sequitur stands). The charitable "
             "reading follows from 0.23 as well as from 0.80, so it does not discriminate. DN4's '~9-13%' rounds the "
             "upper central (Uricchio 0.135) down; the held figures are 9.3% and 13.5%. Whether 0.80 is right is M-905 "
             "(data-check), not this record. The omega_a figures use the standard McDonald-Kreitman split as an "
             "illustration that a given alpha is compatible with either ratio; no held source estimates omega_a at 0.80.",
})
