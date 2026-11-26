#!/usr/bin/env python3
"""M-003 record (lookup): provenance of Day's headline G_f values (1,600; 1,322; 893; 1,400; 1,587).

Object: docs/research/math/objects.yaml M-003 (parameter, lookup). Each value is quoted verbatim
from held text with its locator (quote id in docs/research/sources/quotes-day.md, or the claim
file's Statement blockquote); held() checks the quote against that file. The arithmetic behind
each figure is asserted, and so is the gap between figures that the statement says do not match.

Run: research/.venv/bin/python -I docs/research/math/records/M-003.py [--write]
Without --write it checks that M-003.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

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


# ---- 1,600: 25 fixations in about 40,000 generations; the citation drifts ----------------
look("G_f 1,600 (2019), cited to Nature 2009", 1600, QD,
     "Source: Sequencing of 19 whole genomes detected 25 mutations that were fixed in the 40,000 generations "
     "of the experiment. NATURE, 2009", "Q02, B2019-02-07 ¶9")
look("G_f 1,600 (2025 paper)", 1600, QD,
     "Sequencing detected 25 mutations that were fixed over approximately 40,000 bacterial generations, yielding "
     "an average of 1,600 generations per fixed mutation.", "Q64, Z18168236 ¶29")
look("citation of the 1,600 datum in the 2025 papers", "Good et al. 2017 / 'Nature in 2017'", QD,
     "Z18165980 cites Good et al. 2017 (60,000 gens) for the fixation time; Z18168236 says 25 in ~40,000 gens "
     "\"reported in Nature in 2017\"", "quotes-day.md discrepancy table, row 10")
look("Barrick et al. 2009 genome span", 20_000, CL + "A2g-ltee-neutral-clock-literature.md",
     "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations.",
     "A2g q2, Barrick et al. 2009 Abstract")
assert 40_000 / 25 == 1600
assert 40_000 / 20_000 == 2                            # the cited 2009 genomes span half the 40,000 generations

# ---- 1,322 and 893 (MITTENS 3.0) ---------------------------------------------------------
look("G_f 1,322 (non-mutators, 60,000 gens, mean 45.4 fixations)", 1322, QD,
     "The average across all five non-mutator populations at 60,000 generations is 45.4 fixations, yielding a "
     "cumulative rate of 1,322 generations per fixation.", "Q58, Z23003785 p.6")
look("G_f 893 (clone pair, 50,000 gens)", 893, QD,
     "cross- validated at 893 generations per fixation by clone-pair analysis at 50,000 generations.",
     "Q13, Z23003785 p.1")
gf1322 = 60_000 / 45.4
near(gf1322, 1321.6, 0.05)
assert round(gf1322) == 1322
near(50_000 / 893, 56.0, 0.05)                         # 893 implies 56.0 clone-pair fixations (Q132 prints 56.0)
held(QD, "Subtracting from the clone-pair total of 56.0 fixations")

# ---- 1,400 (2nd-edition abstract, 180 fixations) -----------------------------------------
look("G_f 1,400 (2nd-edition abstract)", 1400, QD,
     "we calculate that natural selection can accomplish at most 180 fixations on the human lineage given "
     "252,000 generations and 1,400 generations per fixation (the fastest empirical rate ever measured in any "
     "organism). This represents 0.000088% of the approximately 205 million fixations required on the human "
     "lineage. The shortfall is 1,139,000-fold.", "Q91, McCarthy thread comment 340102853 (2026-09-18)")
assert 252_000 / 1400 == 180
near(180 / 205e6 * 100, 0.000088, 0.0000005)
assert round(205e6 / 180, -3) == 1_139_000
near(205e6 / 180, 1_138_889, 1)

# ---- 1,587 (strict count; stated by Day in the AI Central post) --------------------------
look("G_f 1,587 (strict count)", 1587, QD,
     "go to the high-resolution data set for all 273,000 generations across the 12 populations, then run the "
     "numbers, is 1,587 generations per fixation.", "Q85, AI Central An Intelligent Groove ¶16 (2026-10-03)")
look("strict per-population non-mutator counts (Z23105291)", [66, 73, 14, 9, 27], QD,
     "per-population non-mutator counts 66, 73, 14, 9, 27 (sum 189, avg 37.8; 60,000/37.8 = 1,587, derived)",
     "quotes-day.md discrepancy table, row 9")
counts = [66, 73, 14, 9, 27]
assert sum(counts) == 189 and sum(counts) / 5 == 37.8
assert round(60_000 / 37.8) == 1587

# ---- the version drift: 1,400 matches neither count ---------------------------------------
r_1400_1322 = near(1400 / 1322, 1.059, 0.001)
r_1587_1400 = near(1587 / 1400, 1.134, 0.001)
r_1587_1322 = near(1587 / 1322, 1.200, 0.001)
for v in (1322, 1587, 893, 1600):
    assert abs(1400 - v) / v > 0.05                    # 1,400 is more than 5% from every other headline

finish({
    "object": "M-003",
    "inputs": L,
    "values": {
        "1600": {"derivation": "40,000/25", "value": 1600, "citations": ["Nature 2009 (2019 post)", "Good et al. 2017 (2025 papers)"],
                 "barrick_2009_span_gens": 20_000},
        "1322": {"derivation": "60,000/45.4", "value": g(gf1322)},
        "893": {"derivation": "clone pair at 50,000", "implied_fixations": g(50_000 / 893)},
        "1400": {"F": 180, "share_pct": g(180 / 205e6 * 100), "shortfall": g(205e6 / 180), "printed_shortfall": 1_139_000},
        "1587": {"derivation": "60,000/(189/5)", "value": g(60_000 / 37.8)},
        "ratios": {"1400/1322": g(r_1400_1322), "1587/1400": g(r_1587_1400), "1587/1322": g(r_1587_1322)},
    },
    "positions": {
        "day": "cites the LTEE for its fixation rate and updates the figure as data improve: 1,600 -> 1,322 (893) -> 1,587",
        "critic": "1,400 matches neither 1,322 (+5.9%) nor 1,587 (-11.8%); the 1,600 citation moves from Nature 2009 to Good 2017",
    },
    "notes": "Provenance only: every figure's arithmetic reproduces from its own stated counts; the origin of 1,400 is not in held text.",
})
