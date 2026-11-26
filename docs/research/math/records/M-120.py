#!/usr/bin/env python3
"""M-120 record (model-choice, derivation): what the threshold |s| > 1/(2N_e) says as N_e grows.

Object: docs/research/math/objects.yaml M-120 (model-choice, derivation). evo010@L20-L23: "selection is effective
when |s| > 1/(2Ne)"; at N_e = 10,000 the threshold is 0.00005, at 10 million 0.00000005; with N "approaching 8
billion" and N_e/N = 0.01, N_e = 80 million and 1/(2N_e) is "approximately 0.000000006" ("six parts per billion").
Asserted: 5e-5, 5e-8, 8e7 and 6.25e-9 exactly; the printed 6e-9 is 6.25e-9 truncated (4% low, not material: same
order, same argument); the post's own "typical" N_e/N of 0.1-0.3 gives 6.25e-10 to 2.08e-10. 5e-5 at N_e = 1e4 is the
same 1/(2N) the B9 claim file and record M-222 use. Attribution: L17 says Day "asked Claude Athos to solve the problem
from the Evo-Avengers perspective" and L27 opens "I also asked the Red Team", so L18-L26 (the threshold passage
included) read as Athos output relayed by Day (rule U); the source map lists L22 as Day's own (flag for the map).
The two readings, quoted:
- Day (L22, L25): the threshold falling with N_e means the models predict ever stronger selection in modern humans,
  which is "obviously, empirically wrong"; selection is differential survival, which d measures.
- the visibility reading: the threshold compares s with drift (ChatGPT's relayed answer, L29: "Selection becomes
  ineffective when: Nes≪1"); it sets the smallest s drift does not swamp, not the size of s, so a small realised
  differential is a small s, which the same threshold then marks as drift-dominated. Day's own L13 draws the same
  line: "Ne tells you how fast alleles drift while d tells you whether selection has enough generational turnover".
  In every held formula d enters as the product s x d (record M-107), so under that form the threshold reads
  |s d| > 1/(2N_e): at N_e = 8e7 and d = 0.015 the visible s is 6.25e-9 / 0.015 = 4.17e-7.
No verdict (H10, A4g). Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-120.py [--write]
Without --write it checks that M-120.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"evo010": "sources/raw/refresh-2026-11-01b/evo010/body.txt"}
CL = "docs/research/claims/"


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


# ---- the passage and who speaks it ------------------------------------------------------------------------------
ATHOS = post("evo010", "Just to be sure I wasn’t missing anything, I asked Claude Athos to solve the problem from the "
                       "Evo-Avengers perspective.")                                             # evo010@L17
REDTEAM = raw("evo010", "Just to be fair, I also asked the Red Team. ChatGPT’s answer:")        # evo010@L27
THRESH = raw("evo010", "In the standard framework, selection is effective when |s| > 1/(2Ne). As Ne grows, that "
                       "threshold shrinks. A population with Ne of 10,000 can only see alleles where |s| > 0.00005. A "
                       "population with Ne of 10 million can see alleles where |s| > 0.00000005.")  # evo010@L20
NE_N = raw("evo010", "For modern humans with N approaching 8 billion, even a brutally low Ne/N of 0.01 gives you Ne of "
                     "80 million. The selection threshold 1/(2Ne) at that point is approximately 0.000000006. The "
                     "models say selection should be able to detect fitness differences of six parts per billion.")  # L23
TYPICAL = raw("evo010", "The typical Ne/N ratio for humans is estimated around 0.1 to 0.3")    # evo010@L23
WRONG = post("evo010", "That prediction is obviously, empirically wrong. And the models have no mechanism to account "
                       "for why it’s wrong.")                                                   # evo010@L22
held(SM + "evo010.md", "| evo010@L22 | Vox Day |")                                              # the map's attribution

# ---- the two readings, quoted -----------------------------------------------------------------------------------
DIFF = raw("evo010", "Selection isn’t a mathematical force that acts on allele frequencies directly. It’s a "
                     "consequence of differential survival and reproduction.")                  # evo010@L25 (Day reading)
D13 = post("evo010", "Ne tells you how fast alleles drift while d tells you whether selection has enough generational "
                     "turnover to actually do its job.")                                        # evo010@L13 (Day)
CHATGPT = raw("evo010", "Selection becomes ineffective when: Nes≪1.")                          # evo010@L29 (ChatGPT, rule U)
held("docs/research/math/objects.yaml", "the post does not say whether the threshold concerns drift visibility or "
                                        "realised mortality")                                   # M-120 positions.critic
held(CL + "B9-drift-would-cause-extinction-within-centuries.md", "against 1/(2N) = 5e-5")      # B9, used by M-222
assert record("M-107")["values"]["d_enters_tau_only_as_s_times_d"] is True                     # M-107: d enters as s x d

# ---- arithmetic -------------------------------------------------------------------------------------------------
thr = lambda ne: Fr(1, 2 * ne)
assert thr(10_000) == Fr(5, 10 ** 5)                  # printed 0.00005
assert thr(10 ** 7) == Fr(5, 10 ** 8)                 # printed 0.00000005
NE_80M = Fr(1, 100) * 8 * 10 ** 9
assert NE_80M == 8 * 10 ** 7                          # N_e/N = 0.01 step: 80 million
t80 = thr(int(NE_80M))
assert t80 == Fr(625, 10 ** 11)                       # 6.25e-9
gap = (t80 - Fr(6, 10 ** 9)) / t80
assert gap == Fr(1, 25)                               # printed 6e-9 is 4% below 6.25e-9 (truncation)
t_typ = [thr(int(Fr(r, 10) * 8 * 10 ** 9)) for r in (1, 3)]
assert t_typ[0] == Fr(625, 10 ** 12)                  # N_e/N 0.1: 6.25e-10
near(float(t_typ[1]), 2.0833e-10, 5e-15)              # N_e/N 0.3: 2.08e-10
s_vis = t80 / Fr(15, 1000)
near(float(s_vis), 4.1667e-7, 5e-12)                  # |s d| > 1/(2N_e) at d = 0.015

finish({
    "object": "M-120",
    "inputs": [
        {"name": "threshold", "value": "|s| > 1/(2 N_e)", "cite": "evo010@L20 (Athos output relayed, rule U)"},
        {"name": "N_e values", "value": [10_000, 10_000_000, 80_000_000], "cite": "evo010@L20, L23"},
        {"name": "N and N_e/N", "value": {"N": 8e9, "Ne_over_N": 0.01, "typical": [0.1, 0.3]}, "cite": "evo010@L23"},
        {"name": "d entering as s x d", "value": True, "cite": "record M-107"},
    ],
    "values": {
        "threshold_Ne_1e4": 5e-5,
        "threshold_Ne_1e7": 5e-8,
        "Ne_at_0.01_of_8e9": 80_000_000,
        "threshold_Ne_8e7": 6.25e-9,
        "printed_threshold": 6e-9,
        "printed_gap_relative": 0.04,
        "threshold_typical_Ne_over_N_0.1_0.3": [6.25e-10, 2.0833e-10],
        "visible_s_at_Ne_8e7_if_d_scales_s_d_0.015": 4.1667e-7,
        "passage_attribution": "L18-L26 sit between 'I asked Claude Athos' (L17) and 'I also asked the Red Team' "
                               "(L27): Athos output relayed by Day (rule U); the source map lists L22 as Day",
    },
    "positions": {
        "day": {"reading": "the threshold shrinks as N_e grows, so the models predict the strongest selection ever "
                           "in modern humans, which is empirically wrong; selection works through differential "
                           "survival, which d measures and neither Wright-Fisher nor Moran contains",
                "holds": "the thresholds are correct as stated (5e-5, 5e-8, 6.25e-9 printed as ~6e-9); neither model "
                         "has an N_e at which selection is impossible (L19)"},
        "critic": {"reading": "|s| > 1/(2N_e) is a drift-versus-selection visibility criterion (ChatGPT, L29: N_e s "
                              "<< 1); it says which s drift does not swamp, not how large realised differentials are",
                   "holds": "Day's own L13 assigns N_e to drift and d to selection, the same split; if d enters as "
                            "s x d (M-107) the condition reads |s d| > 1/(2N_e), i.e. 4.2e-7 at N_e = 8e7 and "
                            "d = 0.015, so a small d is a small effective s inside the standard threshold"},
    },
    "notes": "Model-choice. The arithmetic holds on both readings; the dispute is what the threshold measures. "
             "Whether s x d is the right way to carry d into the threshold is not shown in held text beyond the "
             "formulas M-107 cites. The passage is model output relayed by Day (rule U), as is ChatGPT's answer.",
})
