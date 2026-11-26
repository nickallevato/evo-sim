#!/usr/bin/env python3
"""M-014 record (lookup): the d = 0.45 +/- 0.08 estimate and its two locus sets.

Object: docs/research/math/objects.yaml M-014 (empirical, lookup). Each value is quoted verbatim
from held text with its locator (quote id in docs/research/sources/quotes-day.md, or a claim
file); held() checks the quote against that file. The record fixes the two locus sets, their
overlap, the publication gap and the effective-generation products; it cannot say which locus
set is a typo (no held text says).

Run: research/.venv/bin/python -I docs/research/math/records/M-014.py [--write]
Without --write it checks that M-014.json is current; --write saves it.
"""
import datetime, hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def g(x):
    return float(f"{x:.6g}")


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


L = []


def look(name, value, rel, quote, locator):
    L.append({"name": name, "value": value, "quote": held(rel, quote), "locator": locator})
    return value


d_a = look("d and loci, Z18165980 (Methods)", {"d": 0.45, "pm": 0.08, "loci": ["LCT", "SLC24A5", "HERC2"]}, QD,
           "Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2.", "Q10, Z18165980 ¶69")
d_b = look("d and loci, Z18166234 (citing Day and Athos 2025a)", {"d": 0.45, "loci": ["LCT", "SLC45A2", "TYR"]}, QD,
           "Day and Athos (2025a) estimated d empirically from ancient DNA time series, finding d ≈ 0.45 from three "
           "independent loci (LCT, SLC45A2, TYR).", "Q22, Z18166234 ¶5")
pub_a = look("Z18165980 publication date", "2025-12-28", QD,
             "`Z18165980` (Zenodo pub. 2025-12-28, record modified 2026-01-06)", "quotes-day.md Q10 source line")
pub_b = look("Z18166234 publication date", "2025-12-24", QD,
             "`Z18166234` (Zenodo pub. 2025-12-24, record modified 2026-01-06)", "quotes-day.md Q22 source line")
look("2025 effective generations", 146_250, QD, "Effective generations = 325,000 × 0.45 = 146,250", "Q09, Z18165980 ¶37")
look("2019 generations", 450_000, QD, "there have been 450,000 chimp and human generations since the CHLCA", "Q04")
look("202,500 (Tree of Woe, TW-01)", 202_500, CL + "A4-turnover-coefficient-d.md",
     "450,000 x 0.45 = 202,500 (the \"202,500 generations\" Tree of Woe interview figure, TW-01)", "claim file A4 formal statement")

# ---- the two locus sets ------------------------------------------------------------------
A, B = set(d_a["loci"]), set(d_b["loci"])
assert d_a["d"] == d_b["d"] == 0.45
assert A & B == {"LCT"}                                 # one locus shared
assert A ^ B == {"SLC24A5", "HERC2", "SLC45A2", "TYR"}  # four differ
gap_days = (datetime.date.fromisoformat(pub_a) - datetime.date.fromisoformat(pub_b)).days
assert gap_days == 4                                    # "four days apart"

# ---- effective-generation products ---------------------------------------------------------
assert 325_000 * 0.45 == 146_250
assert 450_000 * 0.45 == 202_500
lo, hi = 0.45 - 0.08, 0.45 + 0.08
near(325_000 * lo, 120_250, 1e-6)
near(325_000 * hi, 172_250, 1e-6)

finish({
    "object": "M-014",
    "inputs": L,
    "values": {
        "d": 0.45, "pm": 0.08, "loci_Z18165980": sorted(A), "loci_Z18166234": sorted(B),
        "shared": sorted(A & B), "differing": sorted(A ^ B), "days_apart": gap_days,
        "N_eff_325000": 146_250, "N_eff_450000": 202_500, "N_eff_325000_band": [g(325_000 * lo), g(325_000 * hi)],
    },
    "positions": {
        "day": "d about 0.45 from three independent loci",
        "critic": "the two papers list different locus sets (one shared, LCT) for the same value; held text cannot say which is a typo",
    },
    "notes": "The '^2' after 0.08 in Q10 is printed as in the extracted text (footnote marker or exponent; not resolved here).",
})
