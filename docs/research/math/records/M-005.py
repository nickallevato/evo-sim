#!/usr/bin/env python3
"""M-005 record (inference): G_f as an average, not a fastest rate; the observation window.

Object: docs/research/math/objects.yaml M-005 (inference, derivation). The record computes the
numbers under each side's reading side by side and asserts them; it does not choose a reading
(that stays with the claim verdicts, A2d, A2j, A5g). Inputs carry their quote id or claim file;
held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-005.py [--write]
Without --write it checks that M-005.json is current; --write saves it.
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


A2D = CL + "A2d-gf-average-not-fastest.md"
# ---- inputs -------------------------------------------------------------------------------
CA11 = held(A2D, "If the figure is an average then it includes some mutations that fixed quicker and so is not the "
                 "fastest fixed mutation rate.")                                   # A2d q1
CA10 = held(A2D, "He is correct that when he calculated the number it was an average.")   # A2d q2
DU02 = held(A2D, "180 total fixed mutations is all there's time for using the fastest rate of mutational fixation "
                 "ever observed in any organism")                                  # A2d q3
Q91 = held(QD, "1,400 generations per fixation (the fastest empirical rate ever measured in any organism)")
A5G2 = held(CL + "A5g-mutation-supply-irrelevant-reply.md",
            "No one has ever observed any human or even mammalian fixation faster than 1,600 generations.")  # A5g q2
TAB = held(A2D, "point-mutator populations are 43 to 183 generations per fixation (Ara-4: 43; Ara-3: 183; the "
                "IS-element mutator Ara+1 is 452; mean over seven 104.7) and the metagenomic mutator average at 60K is 78")
Q58 = held(QD, "45.4 fixations, yielding a cumulative rate of 1,322 generations per fixation")
Q13 = held(QD, "cross- validated at 893 generations per fixation by clone-pair analysis at 50,000 generations")
Q18 = held(QD, "At 25 years per human generation")

nonmut_mean, clone_pair = 1322, 893
pm_fast, pm_slow, mut_mean7, mut_meta = 43, 183, 104.7, 78

# ---- critic reading: a mean is not the fastest rate --------------------------------------
assert pm_fast < pm_slow < nonmut_mean                  # faster rates exist inside the LTEE
r_fast = near(nonmut_mean / pm_fast, 30.7, 0.05)
r_slow = near(nonmut_mean / pm_slow, 7.22, 0.005)
r_clone = near(clone_pair / mut_mean7, 8.53, 0.005)    # "8.5x"
r_meta = near(nonmut_mean / mut_meta, 16.95, 0.005)    # "17x" (claim file A2d prints 16.9, truncated)
# a mean over fixations is at least its fastest member: the min of any set <= its mean
sample = [pm_fast, pm_slow, mut_mean7]
assert min(sample) <= sum(sample) / len(sample)

# ---- Day's reading: "fastest" = throughput of the applicable (non-mutator) class ----------
n_gen = 252_000
F_1322 = near(n_gen / nonmut_mean, 190.6, 0.05)
F_1400 = n_gen / 1400
assert F_1400 == 180                                    # DU-02 / Q91 "180"
fastest_nonmutator = min(nonmut_mean, clone_pair, 1400, 1587, 1600)
assert fastest_nonmutator == clone_pair                # within Day's own non-mutator figures, 893 is the fastest
near(nonmut_mean / clone_pair, 1.48, 0.005)
near(1400 / clone_pair, 1.568, 0.001)

# ---- observation window: 1,600 generations at 25 y ---------------------------------------
window_y = 1600 * 25
assert window_y == 40_000

finish({
    "object": "M-005",
    "inputs": [
        {"name": "Camestros: average is not fastest", "cite": "A2d q1 (CA-11)", "quote": CA11},
        {"name": "Camestros concession: an average", "cite": "A2d q2 (CA-10)", "quote": CA10},
        {"name": "Duffy relaying Day: 180 at the fastest rate", "cite": "A2d q3 (DU-02)", "quote": DU02},
        {"name": "2nd-edition abstract: 1,400 the fastest", "cite": "Q91", "quote": Q91},
        {"name": "no mammalian fixation faster than 1,600", "cite": "A5g q2", "quote": A5G2},
        {"name": "mutator rates in the 3.0 tables", "value": [43, 183, 104.7, 78], "cite": "claim file A2d formal statement (Z23003785 s5.1, s7.2)"},
        {"name": "non-mutator G_f 1,322 and clone pair 893", "value": [1322, 893], "cite": "Q58, Q13"},
        {"name": "g_len", "value": 25, "cite": "Q18"},
    ],
    "values": {
        "1322_over_43": g(r_fast), "1322_over_183": g(r_slow), "893_over_104.7": g(r_clone), "1322_over_78": g(r_meta),
        "F_at_1322": g(F_1322), "F_at_1400": F_1400,
        "fastest_day_nonmutator_figure": fastest_nonmutator, "1322_over_893": g(nonmut_mean / clone_pair),
        "window_years_1600_gen_at_25y": window_y,
    },
    "positions": {
        "day": {"reading": "'fastest' means the throughput rate of the applicable non-mutator class; an average is the right "
                           "quantity to multiply by time (Camestros concedes the average, CA-10)",
                "F_at_1322": g(F_1322), "F_at_1400": F_1400,
                "caveat": "among Day's own non-mutator figures the clone-pair 893 is faster than 1,322 (1.48x) and 1,400 (1.57x)"},
        "critic": {"reading": "a mean cannot be the fastest rate; the LTEE's point-mutator populations fix at 43-183 gen/fix",
                   "faster_by": [g(r_slow), g(r_fast)], "mutator_means_faster_by": [g(r_clone), g(r_meta)]},
        "window": "1,600 generations at 25 y is 40,000 y, longer than any direct observation of human allele-frequency "
                  "change, so 'no faster fixation observed' cannot separate a slow rate from a short window",
    },
})
