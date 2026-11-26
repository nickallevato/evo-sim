#!/usr/bin/env python3
"""M-502 record (lookup): which LTEE populations are mutators, and by what route.

Object: docs/research/math/objects.yaml M-502 (empirical, lookup). The record holds, verbatim with a locator, the six
mutator populations Tenaillon 2016 names at 50,000 generations (E8 q1) and their 96.5% share of point mutations; the
seven-population classification Day's Z23003785 and Z23105291 use at 60,000 generations (claim files E, E6, E7, E8:
Ara+1 added, an IS-element mutator of about 5x); and Day's split of the six into four mutS/mutL and two mutT (E q1).
It checks the counts and the set difference, and recomputes the Clopper-Pearson interval for 6 of 12 (stdlib
bisection on the binomial tail). Held text names the route for Ara+1 only; the per-population gene route behind the
4 + 2 split is not in the quoted Tenaillon passage and its cited sources (Couce 2017, Maddamsetti & Grant 2020) are not
retrieved, so the split is held as Day's wording, not as a verified lookup.

Run: research/.venv/bin/python -I docs/research/math/records/M-502.py [--write]
Without --write it checks that M-502.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, re, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
E = CL + "E-hypermutation-hazard.md"
E5 = CL + "E5-ara2-ara5-counts.md"
E6 = CL + "E6-strict-vs-95-counts.md"
E7 = CL + "E7-mutator-sublinear.md"
E8 = CL + "E8-tenaillon-hypermutators.md"
QL = "docs/research/sources/quotes-literature.md"


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


POP = re.compile(r"Ara[+-]\d")

# ---- inputs ---------------------------------------------------------------------------------------
TEN = "six populations (Ara-1, Ara-2, Ara-3, Ara-4, Ara+3 and Ara+6) had 96.5% of the point mutations, having evolved " \
      "hypermutable phenotypes"
held(QL, TEN)                                                     # Tenaillon 2016, Results, "Genome evolution"
held(E8, TEN)                                                     # E8 q1
TEN_GEN = held(E8, "Tempo and mode of genome evolution in a 50,000-generation experiment")
DAY = held(E, "Six of the twelve populations independently evolved hypermutator phenotypes through destruction of DNA "
              "repair systems: four via mismatch repair defects (mutS/mutL) and two via oxidative damage repair defects "
              "(mutT).")                                          # E q1, Z23020792 Abstract
DAY_SIX = held(E, "this paper says six (Ara-1, -2, -3, -4, +3, +6)")
SEVEN = held(E, "Z23003785 and Z23105291 use seven mutator populations (adding Ara+1, an IS-element mutator of about 5x "
                "per Z23003785 §5.1)")
ARA1 = held(E7, "Ara+1 is an IS-element mutator \"~5×\" (Z23003785 §5.1 table)")
CLASS60 = held(E8, "7 per Wielgoss 2013 / Consuegra 2021 used in Z23105291 for 60,000 generations")
SIMPLE = held(E8, "Z23105291 acknowledges the binary classification \"is a simplification\"")
T1 = held(E6, "Ara+2 66/0/66; Ara+4 73/0/80; Ara+5 14/105/63; Ara-5 9/173/96; Ara-6 27/107/59 (non-mutators); Ara+1 "
              "98/50/115; Ara+3 1,572/447/1,838; Ara+6 1,601/1,756/2,594; Ara-1 268/1,692/621; Ara-2 94/1,816/1,094; "
              "Ara-3 796/0/820; Ara-4 878/1,020/1,233.")          # Z23105291 Table 1 as claim file E6 gives it
FIVE = held(E6, "The average across all five non-mutator populations at 60,000 generations is 45.4 fixations")   # E6 q4
SEVEN_CP = held(E5, "Mean over the seven mutator populations with Ara-2 = -906: (110 + 932 + 803 + 978 - 906 + 273 + "
                    "1,153)/7 = 477.6, so 50,000/477.6 = 104.7 gen/fix")                                   # Z23003785 s5.1
CP_TXT = held(E, "Clopper-Pearson 95% interval for 6/12: 0.211 to 0.789 (paper \"21-79%\": holds).")
CP_PAPER = held(E, "\"exact binomial 95% confidence interval ... approximately 21-79%\"")
SPLIT_GAP = held(E, "accurate for the six; the mutS/mutL versus mutT split is not in the quoted passage (unverified)")
SPLIT_SRC = held(E, "4+2 split sourced to Couce 2017 / Maddamsetti & Grant 2020, not retrieved")
SPLIT_TEST = held(E8, "a gene-level table (mutS/mutL/mutT) from the Tenaillon SI contradicting the 4 + 2 split in Z23020792")

# ---- six at 50,000 (Tenaillon) ---------------------------------------------------------------------
six = POP.findall(TEN)
assert six == ["Ara-1", "Ara-2", "Ara-3", "Ara-4", "Ara+3", "Ara+6"] and len(set(six)) == 6
day_six = {"Ara" + s for s in re.findall(r"[+-]\d", DAY_SIX.split("(")[1])}
assert day_six == set(six)                                        # Day's six are Tenaillon's six
assert "50,000-generation" in TEN_GEN
share = 96.5
near(100 - share, 3.5, 1e-9)                                      # the other populations' share (derived)

# ---- seven at 60,000 (Z23003785, Z23105291) --------------------------------------------------------
cells = [c.strip() for c in T1.rstrip(".").split(";")]
pops = [POP.match(c).group() for c in cells]
assert len(pops) == 12 and len(set(pops)) == 12
non_mut = pops[:5]
assert cells[4].endswith("(non-mutators)")
seven = pops[5:]
assert non_mut == ["Ara+2", "Ara+4", "Ara+5", "Ara-5", "Ara-6"] and "five non-mutator" in FIVE
assert sorted(seven) == sorted(six + ["Ara+1"]) and len(seven) == 7
assert set(seven) - set(six) == {"Ara+1"} and set(six) <= set(seven)
cp_terms = [110, 932, 803, 978, -906, 273, 1153]                  # Z23003785 clone-pair table, one value per mutator
assert len(cp_terms) == 7
near(sum(cp_terms) / 7, 477.6, 0.05)
near(50000 / (sum(cp_terms) / 7), 104.7, 0.05)
assert "seven" in SEVEN and "IS-element" in SEVEN and "~5×" in ARA1 and "60,000" in CLASS60

# ---- routes ---------------------------------------------------------------------------------------
m = re.search(r"four via mismatch repair defects \((mutS/mutL)\) and two via oxidative damage repair defects \((mutT)\)", DAY)
split = {"mismatch repair (mutS/mutL)": 4, "oxidative damage repair (mutT)": 2}
assert m and sum(split.values()) == len(six) == 6
assert "mutS" not in TEN and "mutT" not in TEN                    # the Tenaillon quote names no gene
route = {"Ara+1": "IS-element mutator, about 5x (Z23003785 s5.1, claim files E, E7)"}
route_unheld = sorted(six)                                         # no held text assigns a gene to any of the six


# ---- Clopper-Pearson 95% interval for 6 of 12 ------------------------------------------------------
def tail_ge(k, n, p):
    return sum(math.comb(n, j) * p ** j * (1 - p) ** (n - j) for j in range(k, n + 1))


def bisect(fn, lo=0.0, hi=1.0):
    for _ in range(200):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if fn(mid) else (lo, mid)
    return (lo + hi) / 2


k, n = 6, 12
cp_lo = bisect(lambda p: tail_ge(k, n, p) < 0.025)                # P(X >= 6 | p_lo) = 0.025
cp_hi = bisect(lambda p: 1 - tail_ge(k + 1, n, p) > 0.025)        # P(X <= 6 | p_hi) = 0.025
near(cp_lo, 0.211, 0.0005)
near(cp_hi, 0.789, 0.0005)
near(cp_lo + cp_hi, 1.0, 1e-12)                                   # symmetric at k = n/2
assert round(100 * cp_lo) == 21 and round(100 * cp_hi) == 79      # paper: "approximately 21-79%"

finish({
    "object": "M-502",
    "inputs": [
        {"name": "Tenaillon 2016: six mutators, 96.5% of point mutations", "cite": "E8 q1; quotes-literature.md Tenaillon2016", "text": TEN},
        {"name": "Day Z23020792: six, four mutS/mutL and two mutT", "cite": "E q1 (Z23020792 Abstract)", "text": DAY},
        {"name": "seven mutators at 60,000 incl. Ara+1 (IS element, ~5x)", "cite": "claim files E, E7, E8 (Z23003785 s5.1; Z23105291)",
         "text": [SEVEN, ARA1, CLASS60]},
        {"name": "Z23105291 Table 1 populations by class", "cite": "claim file E6 (Z23105291 Table 1)", "text": T1},
        {"name": "five non-mutators at 60,000", "cite": "E6 q4 (Q58; Z23003785 s4.1)", "text": FIVE},
        {"name": "Clopper-Pearson 6/12", "cite": "claim file E (Z23020792)", "text": [CP_PAPER, CP_TXT]},
        {"name": "4+2 split not in the Tenaillon passage; sources not retrieved", "cite": "claim files E, E8",
         "text": [SPLIT_GAP, SPLIT_SRC, SPLIT_TEST]},
    ],
    "values": {
        "mutators_50k_tenaillon": six, "point_mutation_share_pct": share, "other_populations_share_pct": 3.5,
        "mutators_60k_day": sorted(seven), "non_mutators_60k_day": non_mut, "added_at_60k": ["Ara+1"],
        "count_50k": 6, "count_60k": 7,
        "route_held": route, "day_split_of_six": split, "route_per_population_held_for_the_six": False,
        "clopper_pearson_6_of_12": [round(cp_lo, 4), round(cp_hi, 4)],
    },
    "positions": {
        "day": {"reading": "six of twelve became mutators through loss of DNA repair (four mismatch, two oxidative)",
                "count": 6, "split": split, "ci95": [round(cp_lo, 3), round(cp_hi, 3)]},
        "critic": {"reading": "the six and 96.5% match Tenaillon 2016; the 4+2 split is not in the quoted passage; "
                              "six (50,000, Tenaillon) and seven (60,000, Wielgoss 2013 / Consuegra 2021) are two "
                              "classifications at two endpoints, not one count",
                   "count_50k": 6, "count_60k": 7, "route_per_population_held_for_the_six": False},
    },
    "notes": "The six populations and the 96.5% share match Tenaillon 2016 verbatim, and Day's Z23020792 six are the "
             "same six. Day's Z23003785 and Z23105291 count seven at 60,000 generations; the seventh is Ara+1, an "
             "IS-element mutator of about 5x, so the six-versus-seven difference is a later endpoint and a different "
             "classifier (Wielgoss 2013 / Consuegra 2021), not a recount of the same set. Clopper-Pearson 95% for 6/12 "
             "is 0.2109-0.7891 (Day: about 21-79%). Day's 4 mutS/mutL + 2 mutT split sums to the six but is held only "
             "as Day's wording: the Tenaillon passage names no gene and the cited sources are not retrieved, so the "
             "gene route of each of the six is not in held text (lookup limit, not a contradiction).",
})
