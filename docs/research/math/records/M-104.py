#!/usr/bin/env python3
"""M-104 record (parameter, lookup): mean s of fixed substitutions, 0.875 x 0 + 0.125 x 0.0012 = 1.5e-4.

Object: docs/research/math/objects.yaml M-104 (parameter, lookup). evo005@L52-L55: Tataru et al. give N_e s ~ 12 for
beneficial amino-acid mutations, so s+ = 12/10,000 = 0.0012 at N_e = 10,000; the McDonald-Kreitman alpha for hominids
is about 12.5%; the weighted mean over fixations is 0.875 x 0 + 0.125 x 0.0012 = 1.5e-4. The arithmetic is exact. The
lookup: neither input is held verbatim. Tataru 2017 (PMC5676230) is in bib-literature as "human numbers not read" and
refresh-2026-10-10b says its human numbers "were not located by grep and were not read"; Day names no source for the
12.5%. Both are held only as Day's relay. The held human alpha values (prior-art PA-19, quotes-literature) bracket it:
Uricchio 2019 alpha = 0.135 (verbatim, held), Boyko 2008 0.10-0.20, CSAC 2005 about 0; at Uricchio's 0.135 the same
formula gives 1.62e-4 (+8%). Scope recorded: every held alpha is for protein-coding amino-acid substitutions (PA-19),
and s+ = 12/N_e moves with the N_e chosen (0.0012 at 1e4, 1.2e-4 at 1e5). Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-104.py [--write]
Without --write it checks that M-104.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo005": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-005/body.txt"}
SRC = "docs/research/sources/"
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


# ---- Day's inputs and arithmetic (relayed) --------------------------------------------------------------
TATARU = post("evo005", "Tataru et al. estimated that less than 0.5% of new amino acid mutations are beneficial, with "
                        "a scaled selection strength of N_e·s ≈ 12.")                                    # evo005@L52
MEAN = post("evo005", "0.875 × 0 + 0.125 × 0.0012 = 1.5 × 10⁻⁴")                                         # evo005@L55
ROW = held(SM + "evo005.md", "P: Tataru estimate. I: s+ = 12/10,000. C: 0.0012.")
if (ROOT / RAW["evo005"]).exists():                                   # the alpha sentence is in the body, not the map
    held(RAW["evo005"], "The direct McDonald-Kreitman estimate of α — the proportion of amino acid substitutions "
                        "driven by positive selection — is approximately 12.5% in hominids")
    held(RAW["evo005"], "For human N_e ≈ 10,000, that gives s+ ≈ 0.0012 for the beneficial mutations that do arise.")
held(SM + "evo005.md", "P: alpha 12.5%, s+ 0.0012. I: weighted mean s. C: s about 0.00015.")

# ---- what is and is not held ------------------------------------------------------------------------------
NOT_READ = held(SRC + "bib-literature.md", "| Tataru2017 | Genetics (2017) | PMC5676230 | OA retrieved; human numbers "
                                           "not read | DFE and alpha |")
NOT_FOUND = held(SRC + "refresh-2026-10-10b.md", "Tataru et al., Genetics 2017 (PMC5676230) estimates DFE and alpha "
                                                 "jointly; its human numbers were not located by grep and were not read.")
URICCHIO = held(SRC + "quotes-literature.md", "estimate α = 0.135 in human protein-coding sequences, 72% of which is "
                                              "contributed by weakly-adaptive variants")
BOYKO = held(SRC + "prior-art.md", "| 0.10–0.20 | Boyko 2008 |")
CSAC = held(SRC + "prior-art.md", "| ≈ 0 | CSAC 2005;")
SCOPE = held(SRC + "prior-art.md", "**All values are for protein-coding amino-acid substitutions.**")
held(PY, "Ne_modern_human: {value: 1.0e4")                            # population.Ne_modern_human

# ---- arithmetic ---------------------------------------------------------------------------------------------
ALPHA, NES, NE = Fr(1, 8), 12, 10_000
s_plus = Fr(NES, NE)
assert s_plus == Fr(12, 10_000) == Fr(3, 2500)                       # 0.0012
assert 1 - ALPHA == Fr(7, 8)                                         # 0.875 neutral share
s_bar = (1 - ALPHA) * 0 + ALPHA * s_plus
assert s_bar == Fr(3, 20_000)                                        # 1.5e-4 exactly, as printed
assert Fr(NES, 100_000) == Fr(3, 25_000)                             # s+ at Ne = 1e5: 1.2e-4 (N_e dependence)

# ---- the held alpha values against 12.5% ---------------------------------------------------------------------
s_uricchio = Fr(135, 1000) * s_plus
assert s_uricchio == Fr(81, 500_000)                                 # 1.62e-4
near(float(s_uricchio / s_bar), 1.08, 1e-12)                         # +8%
assert Fr(1, 10) <= ALPHA <= Fr(1, 5)                                 # inside Boyko's 0.10-0.20
near(float(ALPHA / Fr(135, 1000)), 0.926, 5e-4)                      # 7.4% below Uricchio
s_range = [float(Fr(1, 10) * s_plus), float(Fr(1, 5) * s_plus)]
assert s_range == [1.2e-4, 2.4e-4]                                   # Boyko bracket on the same formula

finish({
    "object": "M-104",
    "inputs": [
        {"name": "alpha (MK, hominids)", "value": 0.125, "held": "relayed only (evo005@L52 body sentence; no source named)",
         "cite": "evo005@L52-L55; source map row L55"},
        {"name": "N_e s (Tataru et al.)", "value": 12, "held": "relayed only (Tataru 2017 human numbers not read)",
         "cite": "evo005@L52; bib-literature Tataru2017; refresh-2026-10-10b"},
        {"name": "N_e", "value": NE, "cite": "evo005@L52; parameters population.Ne_modern_human"},
        {"name": "held alpha comparators", "value": {"Uricchio2019": 0.135, "Boyko2008": [0.10, 0.20], "CSAC2005": "about 0"},
         "held": "Uricchio verbatim (quotes-literature); Boyko and CSAC as summarised in prior-art PA-19",
         "cite": "quotes-literature Uricchio2019; prior-art PA-19"},
    ],
    "values": {
        "s_plus": float(s_plus), "s_bar": float(s_bar),
        "s_bar_at_uricchio_alpha": float(s_uricchio), "uricchio_over_day": 1.08,
        "s_bar_boyko_range": s_range,
        "s_plus_at_Ne_1e5": float(Fr(NES, 100_000)),
    },
    "positions": {
        "day": {"reading": "empirical mean s of human fixations is about 1.5e-4, two orders below s = 0.01",
                "holds": "the arithmetic is exact; 12.5% sits inside the held human alpha range (Boyko 0.10-0.20) and "
                         "7% below Uricchio's 0.135, which gives 1.62e-4"},
        "critic": {"reading": "a neutral/adaptive mixture mean is a modelling choice, and the inputs are unchecked",
                   "holds": "neither input is held verbatim (both relayed); the held alpha values are protein-coding "
                            "only, CSAC finds about 0, and s+ = 12/N_e depends on the N_e chosen. Using the mixture "
                            "mean inside the sweep formula is M-105's question"},
    },
    "notes": "Lookup resolved as far as held material allows: the arithmetic reproduces exactly and the two inputs are "
             "recorded as relayed, not verified. Not blocked, because the object's number is Day's derivation from "
             "stated inputs, and the held literature brackets alpha (0 to 0.20, Uricchio 0.135). Verifying N_e s = 12 "
             "would need Tataru 2017's human numbers (bib-literature: retrieved, not read; not under sources/raw in this "
             "checkout). Day's L15 'approximately 10⁻⁴' and L55 1.5e-4 agree in order.",
})
