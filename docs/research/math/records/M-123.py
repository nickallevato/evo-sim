#!/usr/bin/env python3
"""M-123 record (inference, lookup): is the LTEE fixation rate "observably slowing down", and is that missing from the literature.

Object: docs/research/math/objects.yaml M-123 (inference, lookup). pykf@L16 (Day): "the fixation rate is observably
slowing down over time" and this is "missing from the literature"; pykf@L8 (Athos, relayed, rule U): diminishing-
returns epistasis. Day's "detailed spreadsheets" (pykf@L2) are not named and not held. Held instead, from the same
LTEE data his own method cites (Good et al. 2017 metagenomic timecourses; Z23003785 s4.1, via R4-L6):
  (a) Good's HMM "fixed" counts per population at 10K..60K (research/checks/results/raw/l6_undone.json, R4-L6);
  (b) Day's own >=95% snapshot table for five non-mutators (Z23003785 s4.1, copied in l6_ltee_undone.py).
Rate = new fixations per 10,000-generation interval; "slowing" = the mean over intervals after 30K is below the mean
over 0-30K (one fixed split; Ara+5 has no 60K sample). Asserted:
- HMM, all 12: 6 slow, 6 do not. Six non-mutators pooled: 9.17 -> 13.71 per population-interval (no slowdown);
  six mutators pooled: 190.9 -> 151.0 (slowdown).
- Day's five-population table (net >=95% count, 10K-30K vs 30K-60K): 10.4 -> 4.0 (slowdown); the HMM counts for the
  same five populations: 6.4 -> 13.1 (no slowdown). The direction turns on the counting rule, the R4-L6 split
  (a >=95% snapshot is not a fixation call; snapshot counts can fall).
Literature (held quotes, quotes-literature): Barrick 2009, "adaptation decelerated sharply, genomic evolution was
nearly constant for 20,000 generations"; Tenaillon 2016, "the fraction of beneficial mutations declines as fitness
rises, and neutral mutations accumulate at a constant rate". So a slowing of adaptation, and the declining
beneficial supply the Athos inference names, are reported; a slowing of the total fixation count is not (both report
near-constant genomic change). The "prove that evolution ... cannot work" sentence is hedged rhetoric (map row
pykf@L16); quoted only. Day's own spreadsheets, if they differ from Good's data, reopen the rate part. No verdict.
Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-123.py [--write]
Without --write it checks that M-123.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"pykf": "sources/raw/refresh-2026-11-08/p-the-pykf-anomaly/body.txt"}
QL = "docs/research/sources/quotes-literature.md"
L6 = "research/checks/results/raw/l6_undone.json"
L6PY = "research/checks/l6_ltee_undone.py"
R4L6 = "research/checks/results/R4-L6.md"


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


# ---- the claim ---------------------------------------------------------------------------------------------------
SLOW = post("pykf", "One thing I’ve noticed that is missing from the literature is the fact that the fixation rate is "
                    "observably slowing down over time.")                                       # pykf@L16
PROVE = post("pykf", "I was wondering if the LTEE might not accomplish the precise opposite of its original intention, "
                     "and prove that evolution by natural selection cannot work even in the laboratory.")  # pykf@L16
EPI = post("pykf", "each successive fixation event captures a smaller fitness gain than the one before it, meaning "
                   "each subsequent beneficial mutation has a lower selection coefficient")    # pykf@L8 (Athos)
SHEETS = raw("pykf", "I was reviewing the detailed spreadsheets of the LTEE’s twelve populations")  # pykf@L2, unnamed

# ---- held data: Good 2017 HMM fixed counts, and Day's own snapshot table --------------------------------------------
held(L6PY, "Good's HMM well-mixed #fixed at the same marks")
held(L6PY, "Ara+2 19 25 31 45 55 64; Ara+4 4 31 36 38 28 68; Ara+5 16 13 38 34 14 0; Ara-5 9 16 36 7 63 60; "
           "Ara-6 15 22 26 24 24 35")                                                           # Z23003785 s4.1
held(QL, "six populations (Ara-1, Ara-2, Ara-3, Ara-4, Ara+3 and Ara+6) had 96.5% of the point mutations, having "
         "evolved hypermutable phenotypes")                                                     # Tenaillon 2016
held(R4L6, "Good's HMM fixed count never declines (0 of 12)")
L6_SHA = hashlib.sha256((ROOT / L6).read_bytes()).hexdigest()
per = json.loads((ROOT / L6).read_text(encoding="utf-8"))["per_pop"]
MUT = {"Ara-1", "Ara-2", "Ara-3", "Ara-4", "Ara+3", "Ara+6"}
DAY = {"Ara+2": [19, 25, 31, 45, 55, 64], "Ara+4": [4, 31, 36, 38, 28, 68], "Ara+5": [16, 13, 38, 34, 14, 0],
       "Ara-5": [9, 16, 36, 7, 63, 60], "Ara-6": [15, 22, 26, 24, 24, 35]}
assert all(per[p]["snapshot"][:5] == DAY[p][:5] for p in DAY if p != "Ara+4")   # recount = Day's cells (R4-L6:
assert per["Ara+4"]["snapshot"][4] == 0 != DAY["Ara+4"][4]                       # 28 of 29; Ara+4 50K differs)
held(R4L6, "28 of 29 comparable cells match within 20% or 3. The exception is Ara+4 at 50K")
assert len(per) == 12 and MUT < set(per)


def hmm(p):
    h = [int(x) for x in per[p]["hmm_fixed"] if x is not None]
    return h, [h[0]] + [h[i] - h[i - 1] for i in range(1, len(h))]   # cumulative from generation 0


inc = {p: hmm(p)[1] for p in per}
assert all(min(v) >= 0 for v in inc.values())                       # HMM counts never fall
early = {p: Fr(sum(v[:3]), 3) for p, v in inc.items()}
late = {p: Fr(sum(v[3:]), len(v) - 3) for p, v in inc.items()}
slow = sorted(p for p in per if late[p] < early[p])
assert slow == ["Ara+1", "Ara+4", "Ara+5", "Ara+6", "Ara-1", "Ara-4"]
assert len(slow) == 6 and len(set(slow) - MUT) == 3                  # 3 of 6 non-mutators, 3 of 6 mutators


def pooled(pops):
    e = Fr(sum(sum(inc[p][:3]) for p in pops), 3 * len(pops))
    l = Fr(sum(sum(inc[p][3:]) for p in pops), sum(len(inc[p]) - 3 for p in pops))
    return e, l


non = [p for p in per if p not in MUT]
ne, nl = pooled(non)
assert (ne, nl) == (Fr(165, 18), Fr(233, 17))
near(float(ne), 9.1667, 5e-5); near(float(nl), 13.7059, 5e-5)      # non-mutators: no slowdown
me, ml = pooled(sorted(MUT))
assert (me, ml) == (Fr(3436, 18), Fr(2718, 18))
near(float(me), 190.889, 5e-4); near(float(ml), 151.0, 5e-4)       # mutators: slowdown

# Day's table: net change 10K->30K (2 intervals) vs 30K->60K (3 intervals), five populations
d_e = Fr(sum(DAY[p][2] - DAY[p][0] for p in DAY), 2 * 5)
d_l = Fr(sum(DAY[p][5] - DAY[p][2] for p in DAY), 3 * 5)
assert (d_e, d_l) == (Fr(104, 10), Fr(60, 15))                       # 10.4 -> 4.0
d_l_wo = Fr(sum(DAY[p][5] - DAY[p][2] for p in DAY if p != "Ara+5"), 3 * 4)
d_e_wo = Fr(sum(DAY[p][2] - DAY[p][0] for p in DAY if p != "Ara+5"), 2 * 4)
near(float(d_e_wo), 10.25, 1e-12); near(float(d_l_wo), 8.1667, 5e-5)  # without Ara+5's unsampled 60K cell: still slower
# HMM for the same five, same marks (Ara+5 ends at 50K)
h = {p: hmm(p)[0] for p in DAY}
h_e = Fr(sum(h[p][2] - h[p][0] for p in DAY), 2 * 5)
h_l = Fr(sum(h[p][-1] - h[p][2] for p in DAY), sum(len(h[p]) - 3 for p in DAY))
assert (h_e, h_l) == (Fr(64, 10), Fr(184, 14))
near(float(h_l), 13.1429, 5e-5)

# ---- literature, held quotes -----------------------------------------------------------------------------------------
BARRICK = held(QL, "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 "
                   "generations.")                                                              # Barrick 2009 abstract
TENAILLON = held(QL, "the fraction of beneficial mutations declines as fitness rises, and neutral mutations accumulate "
                     "at a constant rate")                                                      # Tenaillon 2016 abstract
GOOD = held(QL, "molecular evolution continues to be characterized by signatures of rapid adaptation")  # Good 2017

finish({
    "object": "M-123",
    "inputs": [
        {"name": "Good 2017 HMM fixed counts at 10K..60K, 12 populations", "value": "l6_undone.json per_pop.hmm_fixed",
         "cite": f"{L6} (sha256 {L6_SHA}); R4-L6"},
        {"name": "Day's >=95% snapshot table, five non-mutators", "value": DAY, "cite": "Z23003785 s4.1 via l6_ltee_undone.py"},
        {"name": "mutator populations", "value": sorted(MUT), "cite": "Tenaillon 2016 (quotes-literature)"},
    ],
    "values": {
        "days_spreadsheets_held": False,
        "hmm_increments_per_10k": {p: inc[p] for p in sorted(per)},
        "hmm_slowing_after_30k": slow,
        "hmm_pooled_nonmutators_per_pop_interval": [round(float(ne), 4), round(float(nl), 4)],
        "hmm_pooled_mutators_per_pop_interval": [round(float(me), 3), round(float(ml), 3)],
        "day_table_net_per_pop_interval_10k30k_vs_30k60k": [10.4, 4.0],
        "day_table_without_ara+5": [10.25, round(float(d_l_wo), 4)],
        "hmm_same_five": [6.4, round(float(h_l), 4)],
        "literature_reports_adaptation_slowing": True,
        "literature_reports_total_fixation_rate_slowing": False,
    },
    "positions": {
        "day": {"reading": "the LTEE fixation rate falls over time, each later fixation gains less, and the literature "
                           "does not say so",
                "holds": "on Day's own >=95% table the net rate falls (10.4 -> 4.0 per population-interval; 10.25 -> "
                         "8.17 without Ara+5's 0); on Good's HMM, half the populations slow, and the six mutators "
                         "pooled slow (190.9 -> 151.0); a falling beneficial share is in Tenaillon 2016"},
        "critic": {"reading": "a slowdown is not shown for fixations as called by the data's authors, and the "
                              "literature reports the related facts",
                   "holds": "Good's HMM counts for the same five populations rise (6.4 -> 13.1) and the six "
                            "non-mutators pooled rise (9.17 -> 13.71); Barrick 2009 and Tenaillon 2016 report "
                            "decelerating adaptation and a declining beneficial fraction, with near-constant genomic "
                            "change, so the slowdown of adaptation is in the literature"},
    },
    "notes": "Lookup on held data. The direction depends on the counting rule (>=95% snapshot vs HMM fixed call), "
             "the definitional split R4-L6 put on the record, and on mutator status. 'Missing from the literature' "
             "fails for the adaptation reading (Barrick, Tenaillon); for the total-fixation reading, the held "
             "literature reports a near-constant rate instead. Day's own spreadsheets are not named or held. "
             "Rate vs window for MITTENS's G_f is M-115 (cited, not recomputed).",
})
