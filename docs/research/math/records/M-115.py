#!/usr/bin/env python3
"""M-115 record (inference, derivation): rate vs latency, Duffy's highway (3,600 s / 360 cars = 10 s per car).

Object: docs/research/math/objects.yaml M-115 (inference, derivation). Duffy (evo008@L95-98, relayed by Day): an
observed generations-per-fixation figure is total generations over total fixations, "regardless of whether those
fixations occurred sequentially or overlapped"; MITTENS is "a rate calculation", not a latency calculation; highway:
3,600 s / 360 cars = 10 s per car. Hancock (evo008@L93, relayed; B6c q2): "it assumes that each mutation has to both
arise and go to fixation before the next". The only number is 3,600/360 = 10, asserted exactly. The rate-vs-latency
point is already settled in M-706 (over a window the serial and aggregate counts coincide only with no overlap) and
M-101 (an average exists whatever the distribution); the transfer of a rate from one system to another is M-103 and
M-006. Cited, not recomputed: M-706's test points and Day's own two serial divisions (252,000/66,000 and /20,000,
drift fixation times, Z23003785 s8.2). New here only a highway check: 360 cars that each take 100 s on the road,
one every 10 s, overlap 10 at a time and still give 10 s per car; the same 360 bunched into the first 600 s give the
same 10 s average, so a count over a window says nothing about latency and needs none. Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-115.py [--write]
Without --write it checks that M-115.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo008": "sources/raw/refresh-2026-11-01/p-erica-and-the-evo-avengers-008/body.txt"}


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


def record(rec):
    return json.loads((ROOT / REC / f"{rec}.json").read_text(encoding="utf-8"))


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
WD_RATE = post("evo008", "Vox Day’s calculation is a rate calculation. Zach thinks it is a latency calculation.")  # L96
ROW96 = held(SM + "evo008.md", "Reproduces: 3,600 / 360 = 10 s per car.")
WD_DEF = raw("evo008", "This tells you how many generations elapsed per fixation on average, regardless of whether "
                       "those fixations occurred sequentially or overlapped.")                # evo008@L95
WD_HWY = raw("evo008", "The numerator is the time (3,600 seconds), the denominator is the number of cars (360). So "
                       "3,600 ÷ 360 = 10 seconds per car.")                                   # evo008@L97
WD_BOOK = raw("evo008", "Vox Day’s calculation is not a latency calculation and is not assuming one fixation happens "
                        "before another one starts.")                                         # evo008@L98
H_SERIAL = raw("evo008", "One is that it assumes that each mutation has to both arise and go to fixation before the "
                         "next mutation can occur.")                                          # evo008@L93, relay
held(SM + "branch-B.md", "it assumes that each mutation has to both arise and go to fixation before the next")  # B6c q2
D_START = held(SM + "branch-F.md", "k = μ gives the output rate once the process is running. t̄ = 4Nₑ gives the "
                                   "startup cost before any output appears.")                 # F q2 (Day)
D_THRU = held(SM + "branch-G.md", "The 1,322 gen/fix rate is not a sequential rate that needs to be divided by a "
                                  "parallelism factor.")                                      # G1 q1 (Z23003785 s8.1)
MANS = held(SM + "branch-F.md", "The time it takes for one allele to get fixed is not important, it is the time "
                                "BETWEEN successive fixations that is important.")            # F1 q1 (Mansfield)

# ---- the only number -----------------------------------------------------------------------------------------
assert Fr(3600, 360) == 10

# ---- a highway check: overlap and bunching leave the average unchanged ------------------------------------------
W, LAT = 3600, 100
even = [10 * i for i in range(360)]                                  # one car every 10 s
assert len([t for t in even if t < W]) == 360 and Fr(W, len(even)) == 10
on_road = max(sum(1 for t in even if t <= x < t + LAT) for x in range(W))
assert on_road == LAT // 10 == 10                                    # 10 cars on the road at once: overlap
bunched = [Fr(600 * i, 360) for i in range(360)]                     # all 360 in the first 600 s
assert len(bunched) == 360 and Fr(W, len(bunched)) == 10             # same average; spacing is not the average
serial_reading = Fr(W, LAT)
assert serial_reading == 36 and serial_reading != 360                # dividing the window by a latency: 36, not 360

# ---- cited: the settled rate-vs-latency identity and Day's own serial divisions ----------------------------------
tp = record("M-706")["values"]["test_points"]
assert tp["back_to_back"]["serial"] == tp["back_to_back"]["aggregate"] == 60
assert tp["overlap_x3"]["aggregate"] == 178 and tp["overlap_x3"]["serial"] == 60   # overlap: aggregate > serial
assert tp["gapped_x2"]["aggregate"] == 30                                          # gaps: aggregate < serial
g2 = record("M-706")["values"]["G2_arithmetic"]
assert g2["252000/66000"] == 3.82 and g2["252000/20000"] == 12.6 and g2["252000/1322"] == 190.6

finish({
    "object": "M-115",
    "inputs": [
        {"name": "highway window and count", "value": [3600, 360], "cite": "evo008@L97 (Duffy, relayed)"},
        {"name": "rate-vs-latency identity", "value": "M-706 test points", "cite": "M-706"},
        {"name": "Day's divisions by a fixation time", "value": {"66000": 3.82, "20000": 12.6}, "cite": "M-706 (Z23003785 s8.2)"},
    ],
    "values": {
        "seconds_per_car": 10, "cars_on_road_at_100s_latency": 10,
        "bunched_average": 10, "window_over_latency": 36,
    },
    "positions": {
        "day": {"reading": "MITTENS divides a window by an observed throughput, so it is a rate, not a latency, "
                           "calculation; anticipated in the book",
                "holds": "3,600/360 = 10 for serial, overlapping or bunched arrivals; T/G_f with a measured G_f is the "
                         "aggregate form and owes no parallelism factor (M-706, G1 q1)"},
        "critic": {"reading": "Hancock: the arithmetic assumes each mutation arises and fixes before the next; the LTEE "
                              "regime may not transfer",
                   "holds": "where a fixation time is the divisor the count is serial: Day's own 252,000/66,000 and "
                            "/20,000 are drift fixation times (M-706); and a rate measured on one road says nothing "
                            "about another without a transfer model (M-103, M-006)"},
    },
    "notes": "Inference. The highway arithmetic holds and the rate/latency distinction is correct for a count over a "
             "window. Whether it follows that the LTEE rate applies to the human divergence time is not a rate-vs-"
             "latency question but a transfer question (M-103, M-006), not settled here. Day's own F q2 treats 4 N_e "
             "as a startup cost before output (M-201's empty start), which is a latency entering the count. Both "
             "the Mansfield (F1) and Day (G1 q1) wordings state the throughput reading.",
})
