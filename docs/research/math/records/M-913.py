#!/usr/bin/env python3
"""M-913 record (derivation): M-912's JC69 two-lineage divergence at Paul Rimmer's bacteria-like inputs.

Object: docs/research/math/objects.yaml M-913 (formula, derivation, variant_of M-912). Source: PR-1 (Paul, Substack,
2026-11-08), section 2 and the CORRECTION section; source map docs/research/math/sources/paul-rimmer-2026-11-08.md.
Inputs (his): L = 4.6e6, kappa = 1e-10 ("1 mutation for every 10 billion bases"), tau = 15 h (corrected from 30 min);
year = 365.25 d (365 d changes no rounded figure). The record asserts the EVOA-102 review's numbers: D/L = 10.8% at
1 My, 59% at 10 My, 75.0% at 100 My; the superseded 30-min tau gives 74% at 1 My. It adds the reading of Paul's
"75% difference is the maximum difference any two alien genomes could possibly have": 3/4 is the limit of the expected
fraction; the possible maximum is 1 (every site), and at L = 4.6e6 the per-genome SD at saturation is
sqrt(0.75 x 0.25 / L) = 0.0002, so 75% is the practical ceiling of the realised fraction too.

Run: research/.venv/bin/python -I docs/research/math/records/M-913.py [--write]
Without --write it checks that M-913.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
MAP = "docs/research/math/sources/paul-rimmer-2026-11-08.md"
RAW = "sources/raw/paulnottheapostle-2026-11-26/text.txt"     # gitignored; checked when present
M912 = "docs/research/math/records/M-912.json"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def paul(quote):
    """A quote from Paul's post: in the committed source map, and in the held fetch when this checkout has it."""
    held(MAP, quote)
    if (ROOT / RAW).exists():
        held(RAW, quote)
    return quote


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
paul("Slower mutation rates, only 1 mutation for every 10 billion bases.")
paul("One new generation EDIT: every 15 hours")
paul("And a shorter genome, only 4.6 million base pairs.")
paul("It turns out in 100 million years, there’d be maximal divergence.")
paul("75% difference is the maximum difference any two alien genomes could possibly have.")
paul("This is still way faster than any evolutionary model would predict.")
paul("I used 30 minutes, when I should have used 15 hours.")
assert json.loads((ROOT / M912).read_text(encoding="utf-8"))["values"]["derivation_exact_n_1_to_5"] is True

# ---- the arithmetic -----------------------------------------------------------------------------------
L, KAP = 4.6e6, 1e-10
H_PER_Y = 365.25 * 24


def frac(kap, n):
    """D/L after n generations (M-912): (3/4)[1 - (1 - 4 kap/3)^(2n)]."""
    return 0.75 * -math.expm1(2 * n * math.log1p(-4 * kap / 3))


def pct(tau_h, my, hpy=H_PER_Y):
    return 100 * frac(KAP, math.floor(my * 1e6 * hpy / tau_h))


got = {my: round(pct(15, my), 1) for my in (1, 10, 100)}
assert got == {1: 10.8, 10: 59.2, 100: 75.0}, got                      # review: 10.8%, 59%, 75.0%
assert {my: round(pct(15, my, 365 * 24), 1) for my in (1, 10, 100)} == {1: 10.8, 10: 59.2, 100: 75.0}
assert 75 - pct(15, 100) < 1e-4                                         # saturated at 100 My
gens_1my = math.floor(1e6 * H_PER_Y / 15)
assert gens_1my == 584_400_000
old = round(pct(0.5, 1), 1)
assert old == 74.3                                                     # superseded 30 min: 74% at 1 My
sd_sat = math.sqrt(0.75 * 0.25 / L)
assert abs(sd_sat - 2.02e-4) < 1e-6                                    # SD of D/L at saturation
assert 0.75 + 50 * sd_sat < 0.77 < 1                                   # 75% is the practical ceiling; 100% is possible

finish({
    "object": "M-913",
    "variant_of": "M-912",
    "inputs": [
        {"name": "L", "value": L, "cite": "PR-1 (paul@L46): 'only 4.6 million base pairs'"},
        {"name": "kappa", "value": KAP, "cite": "PR-1 (paul@L46): '1 mutation for every 10 billion bases'"},
        {"name": "tau_hours", "value": {"corrected": 15, "superseded": 0.5}, "cite": "PR-1 (paul@L46, paul@L169)"},
        {"name": "hours_per_year", "value": H_PER_Y, "cite": "Julian year; 365 d gives the same rounded figures"},
    ],
    "values": {
        "generations_per_My": gens_1my,
        "D_over_L_pct_tau_15h": {"1My": got[1], "10My": got[10], "100My": got[100]},
        "D_over_L_pct_tau_30min_1My": old,
        "saturation_expected": 0.75, "saturation_possible_max": 1.0, "sd_at_saturation": round(sd_sat, 6),
    },
    "positions": {
        "day": {"reading": "the model saturates bacteria within 100 My, which no real genome shows; what stops real "
                           "genomes saturating is constraint and fixation dynamics the model leaves out",
                "holds": "D/L = 10.8% at 1 My, 59.2% at 10 My, 75.0% at 100 My; 'the maximum' is the expected "
                         "saturation value, not the possible maximum (1.0)"},
        "critic": {"reading": "Paul's point is that copying errors alone produce too much divergence, not too little; "
                              "the figure illustrates supply, not a prediction for real bacteria",
                   "holds": "the numbers reproduce; at L = 4.6e6 the realised fraction sits within 0.0002 (one SD) of "
                            "0.75, so '75% is the maximum' is a practical ceiling and a wording slip only"},
    },
    "notes": "Every bacteria number in the EVOA-102 review reproduces from Paul's inputs (59.2% is the review's '59%'). "
             "The 30-min figure (74.3% at 1 My) is superseded by Paul's own CORRECTION (rule SC). 'This is still way "
             "faster than any evolutionary model would predict' has no model named; neutral models at unconstrained "
             "sites also saturate over 100 My at these inputs.",
})
