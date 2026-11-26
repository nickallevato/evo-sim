#!/usr/bin/env python3
"""M-125 record (formula, derivation): relictation "about half" of selection, both "under 8%" of total divergence.

Object: docs/research/math/objects.yaml M-125 (formula, derivation). smokescreen@L15 (Day): "In humans, at least,
relictation accounts for about half the total base pairs that natural selection does, although between them they
don't account for eight percent of the total divergence", leaving "the tens of millions of divergent base pairs".
No inputs are given in the post, and no held text gives Day's relictation base-pair count (the Relictation paper,
Z23188201, gives t/4N_e ratios at 2N = 20-50, claim file E4; Day's halving is not derived in held text, M-112), so
"about half" is not checkable here. Asserted from Day's own two figures, R = S/2 and R + S < 0.08 D:
S < 0.0533 D, R < 0.0267 D, remainder > 0.92 D. D is not named; three held readings:
  35e6 (CSAC SNV total, parameters divergence.snv_differences_total.chimp_consortium_2005; M-109): remainder > 32.2M;
  17.5e6 (the same per lineage): > 16.1M; 410e6 bp (MITTENS 3.0, parameters required_fixations.day_2026 x 2):
  > 377.2M. "Tens of millions" fits the 35M reading; per lineage it is ~16M; on the 410M bp count it is hundreds of
  millions. Day's held selection counts are fixations, not base pairs: 152.5 (F_max at d = 0.80, M-107), 487.5
  (Haldane + d, M-802), 6,651.6 (Term 3, M-808); the largest, x 1.5 for relictation, is 0.029% of 35M, so "under 8%"
  holds on every held count with 2-3 orders to spare, and the 8% itself is not reproduced (it would need S of
  1.87M bp, 281x the Term 3 count). Hitchhiking and relictation as routes to substitution (gene-flow@L5): quoted only.
No verdict (E4, F6). Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-125.py [--write]
Without --write it checks that M-125.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"smokescreen": "sources/raw/refresh-2026-11-08/p-the-secret-beneath-the-smokescreen/body.txt",
       "gene-flow": "sources/raw/refresh-2026-11-08/p-neutral-drift-and-gene-flow/body.txt"}
CL = "docs/research/claims/"
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


# ---- the statement ----------------------------------------------------------------------------------------------------
HALF = post("smokescreen", "In humans, at least, relictation accounts for about half the total base pairs that natural "
                           "selection does, although between them they don’t account for eight percent of the total "
                           "divergence.")                                                       # smokescreen@L15
TENS = raw("smokescreen", "So, I don’t think there are likely any more to discover, and even if we do, I don’t think "
                          "they will account for the tens of millions of divergent base pairs.")  # smokescreen@L15
QUANT = post("smokescreen", "I have managed to identify, prove, and quantify an actual evolutionary mechanism.")  # L16
ROUTES = post("gene-flow", "Relictation and hitchhiking are two other ways to accomplish it.")  # gene-flow@L5
held(SM + "smokescreen.md", "Not reproducible from this post (no inputs); the 8% is the only stated figure.")

# ---- what is and is not held for "about half" ----------------------------------------------------------------------------
held(CL + "E4-relictation.md", "Table (paper; ratio t̄/4Ne at 2N = 20 / 30 / 50)")             # the paper gives ratios
assert json.loads((ROOT / REC / "M-112.json").read_text(encoding="utf-8"))["values"][
    "halving_derived_in_held_text"] is False                                                    # M-112

# ---- inputs for D --------------------------------------------------------------------------------------------------------
held(PY, "chimp_consortium_2005: {value: 3.5e7, units: \"single-nucleotide changes")          # 35M SNV
held(PY, "day_2026: {value: 2.05e8, derived: \"410e6 bp / 2 lineages\", source: Z23003785")   # required_fixations
READINGS = {"snv_35M": 35 * 10 ** 6, "snv_per_lineage_17.5M": Fr(35 * 10 ** 6, 2), "bp_410M": 410 * 10 ** 6}

# ---- Day's two figures as bounds: R = S/2, R + S < 0.08 D -------------------------------------------------------------
EIGHT = Fr(8, 100)
S_share, R_share = EIGHT / Fr(3, 2), EIGHT / 3
assert S_share + R_share == EIGHT and R_share == S_share / 2
near(float(S_share), 0.05333, 5e-6); near(float(R_share), 0.02667, 5e-6)
bounds = {}
for k, D in READINGS.items():
    bounds[k] = {"S_plus_R_below": float(EIGHT * D), "S_below": round(float(S_share * D)),
                 "R_below": round(float(R_share * D)), "remainder_above": float((1 - EIGHT) * D)}
assert bounds["snv_35M"]["remainder_above"] == 32_200_000                      # "tens of millions": yes
assert bounds["snv_per_lineage_17.5M"]["remainder_above"] == 16_100_000        # between ten and twenty million
assert bounds["bp_410M"]["remainder_above"] == 377_200_000                     # hundreds of millions
assert bounds["snv_35M"]["S_below"] == 1_866_667 and bounds["snv_35M"]["R_below"] == 933_333

# ---- Day's held selection counts (fixations), cited ------------------------------------------------------------------------
sel = {"F_max_d0.80 (M-107)": cited("M-107", "F_max")["d_0.80"],
       "Haldane+d (M-802)": cited("M-802", "fixations_exact"),
       "Term 3 (M-808)": cited("M-808", "total_260k_closed_form")}
assert sel == {"F_max_d0.80 (M-107)": 152.5, "Haldane+d (M-802)": 487.5, "Term 3 (M-808)": 6651.6}
top = Fr(str(sel["Term 3 (M-808)"])) * Fr(3, 2)                                 # with relictation at half
near(float(top / READINGS["snv_35M"]), 0.000285, 5e-7)                         # 0.029% of 35M, far under 8%
near(float(S_share * READINGS["snv_35M"] / Fr(str(sel["Term 3 (M-808)"]))), 280.6, 0.05)  # 8% edge needs 281x

finish({
    "object": "M-125",
    "inputs": [
        {"name": "relictation share of selection", "value": "about half", "cite": "smokescreen@L15 (no inputs; not held)"},
        {"name": "selection + relictation share of divergence", "value": "under 8%", "cite": "smokescreen@L15"},
        {"name": "D readings", "value": {"snv_35M": 35e6, "snv_per_lineage": 17.5e6, "bp_410M": 410e6},
         "cite": "parameters divergence.snv_differences_total.chimp_consortium_2005 (M-109); required_fixations.day_2026"},
        {"name": "Day's selection counts (fixations)", "value": sel, "cite": "records M-107, M-802, M-808"},
    ],
    "values": {
        "about_half_checkable_from_held_text": False,
        "S_share_of_D_below": 0.05333,
        "R_share_of_D_below": 0.02667,
        "bounds": bounds,
        "largest_held_selection_count_x1.5_share_of_35M": 0.000285,
        "S_at_8pct_edge_over_term3_count": 280.6,
    },
    "positions": {
        "day": {"reading": "relictation is identified, proved and quantified; with selection it covers under 8% of "
                           "the divergence, leaving tens of millions of base pairs no further mechanism will close",
                "holds": "the 'under 8%' bound holds on every held selection count, by 2-3 orders of magnitude; "
                         "the remainder is > 32.2M on the 35M SNV total, which is 'tens of millions'"},
        "critic": {"reading": "no inputs or derivation in either post; the 8% depends on unstated counts and on D",
                   "holds": "'about half' has no held relictation count (E4 gives ratios only; M-112), the 8% is not "
                            "reproduced by any held count, and the remainder is ~16M per lineage or > 377M on the "
                            "410M bp count; hitchhiking moves linked sites with a selected one, quoted here as a "
                            "route only"},
    },
    "notes": "Derivation from Day's own two figures. Bounds and remainders are exact; the relictation count itself "
             "is unreleased. Selection counts in the corpus are fixation events, the post counts base pairs, so the "
             "comparison is order-of-magnitude only.",
})
