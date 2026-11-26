#!/usr/bin/env python3
"""M-901 record (derivation, inference): ROOT as a universal over mechanisms and its operational form.

Object: docs/research/math/objects.yaml M-901 (inference, derivation). ROOT (claim files ROOT, ROOT-M) quantifies over
every mechanism; its operational form is MITTENS 3.0's F_max = T_gen / G_f against F_req. F_max = 252,000 / 1,322 =
190.6 is cited from the M-713 record (not recomputed) and its inputs are checked against parameters.yaml; the record
asserts the shortfall 2.05e8 / 190.6 = 1.0754e6 (6.03 orders) against the stated 1,075,000 (parameters
shortfall.mittens3_full), that 6.03 orders lies above Z18452504's "3-5 orders" (a different version), and the older
2025 220,000x (2e7 / 91 = 219,780; held in quotes-day.md row 14 and PLAN.md, not in ledgers/versions.md as the object
says). The ROOT-M catalogue is parsed from the claim file as held: 18 named rows, 9 computed or bounded, 3 partial,
5 asserted not computed, 1 (relictation) accepted by Day, and the asserted rows match the table's own tags. The two
post dates (2026-09-30 exempts recombination, ILS and HGT; 2026-10-05 names ILS as excluded) are quoted. Hancock's
covariance objection and her concession are quoted; both readings of 'impossible' are recorded. Stdlib only.

Run: research/.venv/bin/python -I docs/research/math/records/M-901.py [--write]
Without --write it checks that M-901.json is current; --write saves it.
"""
import datetime, hashlib, json, math, pathlib, re, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
RT = CL + "ROOT-no-mechanism-suffices.md"
RM = CL + "ROOT-excluded-mechanisms.md"
COV = CL + "ROOT-cov-hancock-selection-is-a-covariance.md"
RFM = CL + "ROOT-fm-day-mesas-sigillation.md"
FM10 = CL + "FM10-neither-selection-nor-drift-viable.md"
PY = "docs/research/parameters.yaml"
QD = "docs/research/sources/quotes-day.md"
PLAN = "docs/research/PLAN.md"
M713 = "docs/research/math/records/M-713.json"


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
Q1 = ("my own demonstration of the mathematical impossibility of evolution by natural selection, selective sweeps, "
      "neutral sweeps, genetic drift, ILS, biased gene conversion, and every other imagined mechanism")
held(RT, Q1); held(RM, Q1)                                            # ROOT q1 = ROOT-M q1 (2026-10-05, para 3)
held(RT, "[The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05")
Q2 = held(RT, "Alternative mechanisms—incomplete lineage sorting, soft sweeps, standing variation, hitchhiking—do not "
              "rescue the model. Each alternative, when subjected to quantitative analysis, fails to close gaps of 3-5 "
              "orders of magnitude.")                                  # ROOT q2 (Z18452504 s4.3-4.4)
Q4 = held(RT, "evolution by natural selection not only never happened, but was never even possible")   # ROOT q4 (2024-04-25)
RM2 = held(RM, "a shifting constellation of supplementary mechanisms — neutral drift, parallel fixation, supermutation, "
               "hitchhiking, epistasis, clonal interference, compensatory mutation — each invoked ad hoc to answer a "
               "specific mathematical objection, but never tested collectively.")                     # ROOT-M q2
RM3 = held(RM, "No calculations of their effects, individual or cumulative, were ever attempted or provided.")  # ROOT-M q3
RM4 = held(RM, "So is any and every evolutionary mechanism, with the exception of three minor ones.")  # ROOT-M q4
EXEMPT = held(RM, "[Math Teacher Can't Math](https://voxday.net/2026/09/30/math-teacher-cant-math/), 2026-09-30, para 6; "
                  "the three are named later in the post as sexual recombination, incomplete lineage sorting and "
                  "horizontal gene transfer.")
CV1 = held(COV, "natural selection is a statistical co-variance between a trait value and how many offspring you leave, "
                "right?")                                              # ROOT-COV q1 (t=00:29:09)
CV2 = held(COV, "So to say it's a statistically impossible is like to misunderstand the basics of like what a covariance "
                "is.")                                                 # ROOT-COV q2 (t=00:29:29)
CONC = held(COV, "\"Now, you can claim you don't think natural selection can explain the diversity of life or whatever. "
                 "That's fine.\"")
TBR = held(COV, "ROOT is operationalised as a time budget (A, F_max vs F_req), not a statement about covariance")
FMQ = ("What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable "
       "candidates.")
held(RFM, FMQ); held(FM10, FMQ)                                       # ROOT-FM q5 = FM10 q1 (2026-10-10, para 8)
BURDEN = held(RM, "Z18452504 'burden of the alternative' places the burden on critics")
GEST = held(RT, "they gesture at alternative mechanisms without demonstrating that any alternative can accomplish the "
                "required work")
NOCRIT = held(RT, "No critic in the corpus addresses ROOT as a whole")

# ---- inputs (parameters.yaml) and F_max cited from M-713 ------------------------------------------------
held(PY, "day_2026: {value: 252000, source: Z23003785")               # generations_available.day_2026
held(PY, "day_2026: {value: 2.05e8, derived: \"410e6 bp / 2 lineages\"")  # required_fixations.day_2026
held(PY, "day_mittens3_nonmutator: {value: 1322")                     # ltee.gens_per_fixation
held(PY, "mittens3_full: {value: 1075000, source: Z23003785, verified: true}")   # shortfall.mittens3_full
T_GEN, F_REQ, G_F, STATED = 252_000, Fr(205_000_000), 1_322, 1_075_000
m713 = json.loads((ROOT / M713).read_text(encoding="utf-8"))
tdiv, glen, gf, _ = m713["inputs"][1]["value"]
assert tdiv / glen == T_GEN and gf == G_F                             # M-713's inputs are this object's T_gen, G_f
FMAX = m713["values"]["F_max_d1"]                                     # 190.62 (M-713; = 252,000 / 1,322, M-711)
near(FMAX, 190.6, 0.05)

# ---- the shortfall and its orders --------------------------------------------------------------------------
short = float(F_REQ) / FMAX
near(short, 1.0754e6, 50)                                             # 2.05e8 / 190.62 = 1.07544e6
near(float(F_REQ * G_F / T_GEN), 1.0754e6, 50)                        # same with F_max unrounded (1.07540e6)
assert abs(short - STATED) / STATED < 0.001                           # reproduces 1,075,000 to 3 s.f. (0.04%)
orders = near(math.log10(short), 6.03, 0.005)
assert orders > 5                                                     # above Z18452504's "3-5 orders"; a different version
assert "3-5 orders" in Q2

# ---- the older 220,000x (2025 paper) -----------------------------------------------------------------------
V25 = held(QD, "2025: 1600, d=0.45, 146,250, 20M, 220,000x")          # quotes-day.md row 14
held(QD, "Confirmed (2025 shortfall 219,780-fold; 3.0 1,075,000-fold)")
held(PLAN, "| 2025 paper | 1600 | 0.45 | 146,250 | 20M | 220,000× |")
f25 = Fr(146_250, 1_600)                                              # 91.40625
assert round(2e7 / 91) == 219_780                                     # with F_max rounded to 91
near(float(2 * 10**7 / f25), 218_803, 1)                              # unrounded F_max
near(2e7 / 91 / 2.2e5, 1, 0.01)                                       # 220,000x is 219,780 rounded
assert "220,000" not in (ROOT / "docs/research/ledgers/versions.md").read_text(encoding="utf-8")  # locator in statement

# ---- the ROOT-M catalogue, parsed from the claim file -----------------------------------------------------
TOT = held(RM, "Totals (rows 1-18 named mechanisms): computed or empirically bounded: 1, 2, 3, 4, 6, 7, 9, 15, 17 "
               "(9 rows) plus partial: 10, 11, 16; **asserted, not computed: 5, 8, 12, 13, 14** (5 rows); Day-accepted: 18.")
ints = lambda s: {int(x) for x in re.findall(r"\d+", s)}
computed = ints("1, 2, 3, 4, 6, 7, 9, 15, 17"); partial = ints("10, 11, 16")
asserted = ints("5, 8, 12, 13, 14"); accepted = {18}
assert (len(computed), len(partial), len(asserted), len(accepted)) == (9, 3, 5, 1)
groups = [computed, partial, asserted, accepted]
assert set().union(*groups) == set(range(1, 19)) and sum(map(len, groups)) == 18     # disjoint, covers rows 1-18
rows = {}
for line in (ROOT / RM).read_text(encoding="utf-8").splitlines():
    m = re.match(r"\| (\d+) \| ([^|]+) \|[^|]*\| ([^|]+) \|", line)
    if m:
        rows[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())
assert set(rows) == set(range(1, 20))                                 # 18 named rows plus row 19 (the unnamed rest)
tagged_asserted = {k for k, (_, q) in rows.items() if q.startswith("**Asserted")}
assert tagged_asserted == asserted                                    # the table's own tags match the totals line
assert rows[18][0].startswith("Relictation") and "does not exclude" in rows[18][1]
assert all(rows[k][1].startswith("**Computed") for k in computed - {9}) and "Computed/empirical" in rows[9][1]
assert rows[19][1].startswith("**Open**")

# ---- the two post dates on ILS ------------------------------------------------------------------------------
d_exempt, d_named = datetime.date(2026, 9, 30), datetime.date(2026, 10, 5)
assert "incomplete lineage sorting" in EXEMPT and "ILS" in Q1          # exempted on 09-30, named as excluded on 10-05
assert (d_named - d_exempt).days == 5
assert "recombination" not in Q1 and "horizontal" not in Q1           # the other two exempt mechanisms are not named on 10-05

finish({
    "object": "M-901",
    "inputs": [
        {"name": "T_gen, F_req, G_f", "value": [T_GEN, float(F_REQ), G_F],
         "cite": "parameters generations_available.day_2026, required_fixations.day_2026, ltee.gens_per_fixation.day_mittens3_nonmutator"},
        {"name": "F_max", "value": FMAX, "cite": "docs/research/math/records/M-713.json (F_max_d1; M-711)"},
        {"name": "stated shortfall", "value": STATED, "cite": "parameters shortfall.mittens3_full (Z23003785)"},
        {"name": "2025 version", "value": {"F_max": 91.4, "F_req": 2e7, "stated": "220,000x"},
         "cite": "quotes-day.md row 14; PLAN.md version table"},
        {"name": "mechanism catalogue", "value": {"computed_or_bounded": sorted(computed), "partial": sorted(partial),
                                                 "asserted": sorted(asserted), "day_accepted": [18]},
         "cite": "claim ROOT-M table and Totals line"},
        {"name": "quotes", "value": ["ROOT q1", "ROOT q2", "ROOT q4", "ROOT-M q2", "ROOT-M q3", "ROOT-M q4",
                                     "ROOT-COV q1", "ROOT-COV q2", "ROOT-FM q5 = FM10 q1"], "cite": "claim files"},
    ],
    "values": {
        "F_max": FMAX, "shortfall": round(short), "orders": round(orders, 2),
        "reproduces_stated_1075000": True, "relative_gap_to_stated": round(abs(short - STATED) / STATED, 5),
        "above_Z18452504_3_to_5_orders": True,
        "shortfall_2025": {"F_max_rounded_91": 219_780, "F_max_unrounded": 218_803, "stated": 220_000},
        "catalogue_counts": {"named_rows": 18, "computed_or_bounded": 9, "partial": 3, "asserted_not_computed": 5,
                             "day_accepted_relictation": 1},
        "ILS_dates": {"exempted": "2026-09-30", "named_excluded": "2026-10-05", "days_apart": 5},
    },
    "positions": {
        "day": {"reading": "'impossibility' is the time budget: every mechanism with a computed bound fails F_max < F_req; "
                           "the unnamed remainder is the critics' burden (Z18452504)",
                "holds": "the operational form reproduces: 2.05e8 / 190.6 = 1.0754e6, 6.03 orders, the stated 1,075,000; "
                         "9 of 18 named rows carry a computation or empirical bound"},
        "critic": {"reading": "a universal over unnamed mechanisms is untestable; 'statistically impossible' is a category "
                              "error for a covariance (ROOT-COV q1, q2)",
                   "holds": "5 of 18 named rows are asserted, not computed, and 3 are partial; Day accepts relictation; ILS "
                            "is exempted on 2026-09-30 and named as excluded on 2026-10-05; Hancock concedes the live "
                            "question in her next sentence, so her point is about wording, not the time budget"},
    },
    "notes": "The arithmetic is settled; the quantifier is not. The shortfall is the MITTENS 3.0 value (6.03 orders), "
             "above Z18452504's '3-5 orders' and about 4.9x the 2025 paper's 220,000x (2e7 / 91 = 219,780). The object "
             "statement locates 220,000x in ledgers/versions.md; that ledger does not contain it; it is held in "
             "quotes-day.md row 14 and PLAN.md. Catalogue counts are the claim file's keyword-search counts over the "
             "harvested corpus; the paywalled books may hold computations for the asserted rows (ROOT-M Weaknesses). "
             "Row 10 (bounded empirically by the LTEE aggregate) and row 16 (a penalty, not a mechanism) are in the "
             "'partial' group as the claim file places them. Whether 'impossible' is the time budget or an intensifier "
             "is the owner's open RH call (claim ROOT); both readings are recorded, none chosen.",
})
