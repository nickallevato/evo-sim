#!/usr/bin/env python3
"""M-711 record (derivation): Duffy's 180, 252,000 / 1,400.

Object: docs/research/math/objects.yaml M-711 (formula, derivation). 6.3e6 years / 25 years = 252,000 effective
generations (DZ-02, G2b q2; parameters generations_available.day_2026); divided by the book's G_f of 1,400 (Z23003785
s3.3, as claim file G2b gives it) this is 180 fixations exactly (DU-02, G2b q1); with the 3.0 value 1,322 it is
190.6. Against 205e6 required, the shortfall is 205e6/180 = 1,138,889 (the paper's table s7.2 prints 1,139,000x,
a rounding of 0.01%). Read as T/G_f with a measured throughput, the division is a rate calculation (M-706); read as
T/t_fix it is serial. The "fastest rate ever observed" premise is checked against the LTEE point-mutator range
43-183 gen/fix quoted from claim file G2b (A2d), not recomputed. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-711.py [--write]
Without --write it checks that M-711.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G2B = CL + "G2b-duffy-180-arithmetic.md"
G2G = CL + "G2g-appendix-a-fixation-must-be-sequential.md"
QC = "docs/research/sources/quotes-critics.md"
PY = "docs/research/parameters.yaml"


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


# ---- inputs ---------------------------------------------------------------------------------------
DU02 = ("180 total fixed mutations is all there's time for using the fastest rate of mutational fixation ever "
        "observed in any organism")
held(G2B, DU02); held(QC, DU02)                                   # G2b q1 = DU-02 (t=00:29:42, ASR)
DZ02 = held(G2B, "The length of a generation for humans is 25 years times 1,000 400")   # G2b q2 = DZ-02 (ASR, garbled)
REST = held(G2B, "The arithmetic he restates: 6.3e6/25 = 252,000; /1,400 = 180.")
BOOK = held(G2B, "1,400 is the book's G_f (Z23003785 s3.3; the 3.0 paper replaces it with 1,322 → 190.6).")
TAB = held(G2B, "Table s7.2 row \"Book's original (1,400)\": 180 achievable, shortfall 205e6/180 = 1,138,889 "
                "(paper: 1,139,000×; reconciles).")
FAST = held(G2B, "the LTEE point-mutator populations run faster (43–183 gens/fixation).")
APPA = held(G2G, "yields 180 fixations where 205 million are required.")                # G2g q1
TDIV = 6.3e6; held(PY, "day_2026_mittens3: {value: 6.3e6, source: Z23003785")  # divergence.t_div_years
GLEN = 25; held(PY, "day_2026: {value: 25, source: Z23003785")                   # generation_time_years.day_2026
GENS = 252_000; held(PY, "day_2026: {value: 252000, source: Z23003785")          # generations_available.day_2026
REQ = 2.05e8; held(PY, "day_2026: {value: 2.05e8, derived: \"410e6 bp / 2 lineages\"")   # required_fixations.day_2026
GF3 = 1_322; held(PY, "day_mittens3_nonmutator: {value: 1322")                   # ltee.gens_per_fixation
GF_BOOK = 1_400

# ---- the arithmetic ---------------------------------------------------------------------------------------
assert TDIV / GLEN == GENS                                        # 252,000 effective generations
n_book = GENS / GF_BOOK
assert n_book == 180                                              # exactly
n_3 = GENS / GF3
near(n_3, 190.62, 0.005)
short = REQ / n_book
near(short, 1_138_888.9, 0.05)
printed = 1_139_000
near(printed - short, 111.1, 0.05); near((printed - short) / short, 9.8e-5, 1e-6)   # 0.01%
assert round(short, -3) == printed
short_3 = REQ / n_3
near(short_3, 1_075_437, 1)                                       # with 1,322 (parameters shortfall.mittens3_full 1,075,000)
held(PY, "mittens3_full: {value: 1075000, source: Z23003785")
assert round(short_3, -3) == 1_075_000

# ---- the "fastest rate" premise --------------------------------------------------------------------------
fast = (43, 183)
assert all(g < GF3 < GF_BOOK for g in fast)                       # point-mutator lines run faster than 1,322 or 1,400
n_fast = tuple(GENS / g for g in fast)
near(n_fast[0], 5_860.5, 0.05); near(n_fast[1], 1_377.0, 0.05)    # what the same division gives at those rates

finish({
    "object": "M-711",
    "inputs": [
        {"name": "t_div, g_len", "value": [TDIV, GLEN], "cite": "DZ-02 (G2b q2); parameters divergence.t_div_years.day_2026_mittens3, generation_time_years.day_2026"},
        {"name": "G_f book, 3.0", "value": [GF_BOOK, GF3], "cite": "G2b formal statement (Z23003785 s3.3); parameters ltee.gens_per_fixation.day_mittens3_nonmutator"},
        {"name": "required fixations", "value": REQ, "cite": "parameters divergence.required_fixations.day_2026; G2g q1"},
        {"name": "LTEE point-mutator range", "value": list(fast), "cite": "G2b formal statement (A2d), quoted"},
    ],
    "values": {
        "generations": GENS, "fixations_book": n_book, "fixations_3.0": round(n_3, 2),
        "shortfall_book": round(short, 1), "printed_shortfall": printed, "shortfall_3.0": round(short_3),
        "fixations_at_point_mutator_rates": [round(x, 1) for x in n_fast],
    },
    "positions": {
        "day": {"reading": "180 fixations is all there is time for at the fastest rate ever observed, against 205e6",
                "holds": "252,000 / 1,400 = 180 exactly; shortfall 1,138,889 (printed 1,139,000)"},
        "critic": {"reading": "not the fastest rate observed; dividing by a per-lineage latency is the serial reading",
                   "holds": "point-mutator LTEE lines run at 43-183 gen/fix (A2d); T/G_f is a rate calculation only "
                            "if G_f is read as a throughput (M-706)"},
    },
    "notes": "The arithmetic reproduces exactly. The 1,400 is the book's G_f; the 3.0 paper's 1,322 gives 190.6 and a "
             "shortfall of 1,075,437 (parameters shortfall.mittens3_full 1,075,000). 'Fastest ... in any organism' is "
             "false of the LTEE point-mutator lines (43-183 gen/fix, quoted), which Day excludes as mutators (A2d); "
             "the record only shows what the same division gives at those rates. Serial versus aggregate is M-706.",
})
