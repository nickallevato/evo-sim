#!/usr/bin/env python3
"""M-101 record (inference, derivation): does an average rate X/Y exist, and what does it mean, for a stochastic process.

Object: docs/research/math/objects.yaml M-101 (inference, derivation). Day (evo006, evo007): if X events occur over Y
time, X/Y is the average rate; it exists whatever the variance, a mean does not need a Gaussian, and 4N_e is itself an
average. Relayed critics: Maddie (evo006@L10, wind speed: "an average rate ... it's like meaningless") and Hancock
(evo007@L12, "meaningless because it's not a Gaussian distribution"). The record separates three questions. (1)
Existence: X/Y exists for any count and duration; both sides accept it (G1b, G1c). (2) Gaussianity: a mean is defined
for any distribution with a finite mean; a constructed bimodal sample has a mean that no member attains, which is the
true part of the critics' point (the mean is not a typical event), not a proof that it does not exist. (3) As a
bound: an average from one set of conditions bounds nothing elsewhere without a transfer model; that is settled in
M-005 (an average includes faster events) and M-006 (the LTEE ceiling holds only under a stated transfer factor), and
the spread of 4N_e is M-606 (SD 0.538 x 4N_e). Those values are read from the cited JSON records, not recomputed.
Day's own reply (evo007@L31) concedes that rates require their parameters. Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-101.py [--write]
Without --write it checks that M-101.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo006": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-006/body.txt",
       "evo007": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-007/body.txt"}
CL = "docs/research/claims/"
G1B = CL + "G1b-samson-total-over-time.md"
G1C = CL + "G1c-camestros-average-concession.md"
REC = "docs/research/math/records/"


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


# ---- the source sentences ------------------------------------------------------------------------------
D_EXISTS = post("evo006", "if something happens multiple times over a period of time, then an average rate for that "
                          "activity or process must necessarily exist")                       # evo006@L4
D_XY = post("evo006", "If X events occur over Y time, then X/Y is the average rate.")             # evo006@L30
D_4NE = post("evo006", "It’s the average time to fixation for a neutral mutation.")               # evo006@L17
D_GAUSS = post("evo007", "An average does not require a Gaussian distribution to be meaningful.")  # evo007@L27
D_SUM = post("evo007", "as I’ve previously pointed out all rates with the same denominator, in this case, time, can "
                       "be summed and averaged")                                                  # evo007@L34
D_PARAM = post("evo007", "Her analogy doesn’t show that rates are incalculable, it shows that rates require "
                         "specifying the relevant parameters.")                                   # evo007@L31
C_MADDIE = post("evo006", "There just so much variance that it’s like an average rate doesn’t, it’s like "
                          "meaningless.")                                                         # evo006@L10, relay (rule U)
C_HANCOCK = post("evo007", "So there’s just actually no way like you could take an average, but it would be "
                           "meaningless because it’s not a Gaussian distribution")                # evo007@L12, relay (rule U)
UJ = held(G1B, "And dividing “total” by “amount of time” gives a simple, unweighted average number. The rate.")  # UJ-02
CA = held(G1C, "He is correct that when he calculated the number it was an average. It isn’t intended to be a time "
               "for an individual chromosome.")                                                   # CA-10

# ---- (1) existence: X/Y for any count and duration ---------------------------------------------------------
for x, y in ((45, 60_000), (1, 7), (0, 10)):
    rate = Fr(x, y)
    assert rate * y == x                                       # the quotient exists and reproduces the count

# ---- (2) a non-Gaussian (bimodal) sample: the mean exists and no member attains it -------------------------
# constructed test point: 7 events at 40,000 and 1 at 5,000 generations (two modes, nothing in between)
sample = [Fr(40_000)] * 7 + [Fr(5_000)]
mean = sum(sample) / len(sample)
assert mean == Fr(71_250, 2) and mean not in sample          # 35,625: defined, but no event takes that long
median = sorted(sample)[len(sample) // 2]
assert median == 40_000 and median != mean                    # the mean is not the typical event
var = sum((v - mean) ** 2 for v in sample) / len(sample)
assert var > 0 and near(float(var) ** 0.5 / float(mean), 0.3249, 1e-4)
# the average rate over the window equals count / total time, whatever the shape
assert Fr(len(sample)) / sum(sample) == 1 / mean

# ---- (3) as a bound: cite the settled records ---------------------------------------------------------------
cv_4ne = near(cited("M-606", "cv"), 0.538, 0.001)              # SD of the conditional neutral time / 4N_e
f_1322 = near(cited("M-005", "F_at_1322"), 190.6, 0.05)        # 252,000 / 1,322: an average, faster ones inside it
fastest = cited("M-005", "fastest_day_nonmutator_figure")
assert fastest == 893 and fastest < 1_322                      # a faster per-population value exists (M-005)
f_noscale = cited("M-006", "F_no_scaling")
assert f_noscale == 191                                        # the LTEE ceiling with no transfer factor (M-006)

finish({
    "object": "M-101",
    "inputs": [
        {"name": "Day's identity", "value": "rate = X / Y", "cite": "evo006@L30, @L4; evo007@L27, @L34"},
        {"name": "critics' objection (relayed)", "value": ["wind-speed variance (Maddie)", "not Gaussian (Hancock)"],
         "cite": "evo006@L10, evo007@L12 (relays, rule U)"},
        {"name": "bimodal test sample", "value": {"40000": 7, "5000": 1}, "cite": "constructed test point"},
        {"name": "settled values", "value": {"M-606 cv": cv_4ne, "M-005 F_at_1322": f_1322,
                                             "M-005 fastest non-mutator": fastest, "M-006 F_no_scaling": f_noscale},
         "cite": "records M-606, M-005, M-006 (cited, not recomputed)"},
    ],
    "values": {
        "bimodal_mean": float(mean), "bimodal_median": int(median), "bimodal_cv": round(float(var) ** 0.5 / float(mean), 4),
        "mean_attained_by_a_member": False,
        "neutral_time_cv": cv_4ne,
    },
    "positions": {
        "day": {"reading": "X/Y exists for any count and duration; a mean needs no Gaussian; 4N_e is itself an average",
                "holds": "existence and the Gaussian point hold as arithmetic; both sides accept existence (G1b UJ-02, "
                         "G1c CA-10). Day concedes rates need their parameters (evo007@L31)"},
        "critic": {"reading": "the average is uninformative without the distribution and the conditions",
                   "holds": "the mean need not be a typical event (bimodal test: mean 35,625, no member near it; 4N_e has "
                            "CV 0.538, M-606), and an average from one system bounds another only under a transfer "
                            "model (M-005, M-006). 'Meaningless' read literally (does not exist) fails; read as "
                            "'not a bound or a typical time' it holds"},
    },
    "notes": "Inference object; no number is printed in the rows. Existence is arithmetic and not in dispute. The relayed "
             "critic sentences say 'meaningless', not 'does not exist'; under the reading 'not informative as a bound "
             "or a typical time' they are correct, and that reading is the one Day answers with 'rates require "
             "specifying the relevant parameters'. Whether an observed average bounds a rate elsewhere is the transfer "
             "question of M-006 and M-103, not this object. The bimodal sample is a constructed test point.",
})
