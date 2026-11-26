#!/usr/bin/env python3
"""M-909 record (lookup): the evidential weight of endorsements and credentials (ROOT-T, -EP, -DE, -H, -K).

Object: docs/research/math/objects.yaml M-909 (inference, lookup). A lookup, not a score. Each endorsement (Tipler's
endorsement and appendix as Dembski relays them, Keen's preface, Hossjer's agreement and its scope, Dembski's own
position) and each counter (Hancock and the host: no population-genetics background, ID association to be disclosed,
"similar blunders") is quoted verbatim from its claim file and tagged held or not retrieved. Held: every quote in the
object's sources (8) plus the scope sentences around them. Not retrieved: Tipler's foreword and appendix (in the
paywalled book; ROOT-T fidelity unverifiable), Hossjer's population-genetics record (not examined), Hossjer, Bechly
and Gauger 2021 (not retrieved) and the paper behind "similar blunders" (none named). The audit rule (FP-01: a
credential count is not a rebuttal) and the scope limits (Keen endorses The Frozen Gene, not the MITTENS papers;
Dembski: Hossjer's remarks apply to the main argument, not the book; Hossjer's own rescaled gap is about 2x, M-805)
are quoted. No numeric score is given. Stdlib only.

Run: research/.venv/bin/python -I docs/research/math/records/M-909.py [--write]
Without --write it checks that M-909.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
T = CL + "ROOT-t-tipler-endorsement.md"
EP = CL + "ROOT-ep-hancock-endorsers-lack-popgen-background.md"
DE = CL + "ROOT-de-dembski-own-arguments.md"
H = CL + "ROOT-h-hossjer-agrees-with-main-argument.md"
K = CL + "ROOT-k-keen-time-is-the-reason.md"
M805 = "docs/research/math/records/M-805.json"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


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


# ---- endorsements (Day side) ------------------------------------------------------------------------------
END = [
    {"id": "ROOT-T q2", "who": "Dembski relaying Tipler", "role": "endorsement",
     "quote": held(T, "Tipler gave it a glowing endorsement and also contributed an appendix to the book."),
     "status": "held as a relay; the endorsement's text and the appendix are in the paywalled book, not retrieved"},
    {"id": "ROOT-K q1", "who": "Keen", "role": "endorsement",
     "quote": held(K, "The reason it fails, as Vox Day and Claude Athos show in this book, is time."),
     "status": "held (public preface); endorses The Frozen Gene, not the MITTENS papers"},
    {"id": "ROOT-H q1", "who": "Hossjer", "role": "endorsement",
     "quote": held(H, "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation "
                      "rates of humans and E. coli."),
     "status": "held (review PDF p.3)"},
    {"id": "ROOT-H q3", "who": "Hossjer", "role": "position of the endorser",
     "quote": held(H, "I rather advocate uncommon descent between the two species."),
     "status": "held (Dembski Substack review para 75)"},
    {"id": "ROOT-H q4", "who": "Dembski about Hossjer", "role": "scope of the endorsement",
     "quote": held(H, "Note that his positive remarks apply to Vox Day’s main argument, not to the book as a whole."),
     "status": "held (same review para 34)"},
    {"id": "ROOT-DE q1", "who": "Dembski", "role": "own position",
     "quote": held(DE, "As an intelligent design proponent, I have my own arguments for thinking that evolutionary "
                       "mechanisms face serious explanatory shortfalls."),
     "status": "held (Dembski Substack 2026-09-28 para 3); the arguments themselves are not given there"},
]
# ---- counters (critic side) --------------------------------------------------------------------------------
CTR = [
    {"id": "ROOT-EP q1", "who": "Gutsick Gibbon (host)", "role": "credentials",
     "quote": held(EP, "Generally, none of them have a particularly prevalent biology or population genetics background"),
     "status": "held (video t=03:04:48, auto-caption)"},
    {"id": "ROOT-EP q3", "who": "Gutsick Gibbon (host)", "role": "disclosure",
     "quote": held(EP, "I think if you're going to include Tipler's quote in your rebuttal here, you probably should "
                       "Google him and see that he's an ID proponent."),
     "status": "held (video t=00:31:35)"},
]
assert len(END) + len(CTR) == 8                                       # the object's eight sources, all held
assert {e["id"] for e in END + CTR} == {"ROOT-T q2", "ROOT-EP q1", "ROOT-EP q3", "ROOT-DE q1", "ROOT-H q1",
                                         "ROOT-H q3", "ROOT-H q4", "ROOT-K q1"}

# ---- context sentences (held) ------------------------------------------------------------------------------
FOCUS = held(EP, "\"These guys all have focuses in statistics, physics, or mathematics.\"")
NOTWRONG = held(EP, "\"I don't think that creationist necessarily means wrong, but I do think that those associations "
                    "ought to be disclosed.\"")
BLUNDER = held(EP, "\"And in fact, Hosture has made blunders very similar\"")
BYLINE = held(EP, "Hossjer's byline is \"Professor of Mathematical Statistics, Stockholm University\" (HO-09)")
FP01 = held(EP, "Del Arroz: \"A headcount of degrees isn't a rebuttal\" (FP-01)")
WEAK = held(EP, "internal: holds   # internal: holds only in the weak form (credentials bear on weight of endorsement, "
                "not on arithmetic; FP-01).")
KEEN_SCOPE = held(K, "fidelity: partial      # endorses The Frozen Gene, not the MITTENS papers; scope differs")
KEEN_CRED = held(K, "Credentials (economics PhD, evolutionary programming) self-described.")
TWO = held(H, "which still is less than 20 million, but only by a factor of 2.")      # HO-02
TENSION = held(H, "the agreement 'also after adjusting' and the 2x gap are in tension in the same review")
m805 = json.loads((ROOT / M805).read_text(encoding="utf-8"))
assert m805["object"] == "M-805"                                      # Hossjer's arithmetic is M-805's record, not redone here

# ---- not retrieved (named, not estimated around) --------------------------------------------------------------
NR = [
    {"item": "Tipler's foreword and appendix", "where": "Probability Zero (paywalled book)",
     "quote": held(T, "the foreword and appendix are in the paywalled book; contents unknown.")},
    {"item": "Hossjer's population-genetics publication record", "where": "not examined in the corpus",
     "quote": held(EP, "his publication record in population genetics was not examined in the corpus")},
    {"item": "Hossjer, Bechly & Gauger 2021 (J. Theor. Biol. 524:110657)", "where": "not retrieved (D15)",
     "quote": held(EP, "| Hossjer, Bechly & Gauger 2021 (J. Theor. Biol. 524:110657) | not retrieved (see D15) | pending |")},
    {"item": "the paper behind 'similar blunders'", "where": "none named",
     "quote": held(EP, "the \"similar blunders\" claim names no paper")},
    {"item": "Dembski's own arguments", "where": "not given in the interview; 'Jason Rosenhouse's Whoppers' not retrieved",
     "quote": held(DE, "Dembski's own earlier critique of Rosenhouse ('Jason Rosenhouse's Whoppers') is linked by Day but "
                       "was not retrieved (see D13).")},
]
held(T, "fidelity: unverifiable      # Tipler's own foreword/appendix not retrieved")

finish({
    "object": "M-909",
    "inputs": [
        {"name": "endorsements", "value": [e["id"] for e in END], "cite": "claims ROOT-T, ROOT-K, ROOT-H, ROOT-DE"},
        {"name": "counters", "value": [c["id"] for c in CTR], "cite": "claim ROOT-EP"},
        {"name": "audit rule", "value": "FP-01: a credential count is not a rebuttal", "cite": "claim ROOT-EP"},
        {"name": "Hossjer's rescaled gap", "value": "about 2x", "cite": "ROOT-H HO-02; docs/research/math/records/M-805.json"},
    ],
    "values": {
        "endorsements": END, "counters": CTR,
        "held_quotes": len(END) + len(CTR), "not_retrieved": NR,
        "numeric_score": None,
    },
    "positions": {
        "day": {"reading": "endorsements by a physicist, a mathematical statistician and an economist carry independent "
                           "weight and add the endorsers' own arguments",
                "holds": "the endorsements exist as quoted; Hossjer agrees with the main argument 'also after adjusting' "
                         "and Dembski states his own ID arguments; credentials do not decide arithmetic (FP-01), which "
                         "cuts against the counter as much as for the endorsers"},
        "critic": {"reading": "the endorsers lack population-genetics training and ID associations should be disclosed, "
                              "so the endorsements carry little weight on the assumptions",
                   "holds": "each endorsement is scoped: Keen endorses The Frozen Gene, Hossjer's remarks cover the main "
                            "argument not the book and his own rescaled gap is about 2x, Tipler's text is not retrieved, "
                            "Dembski's arguments are not given; Hossjer advocates uncommon descent"},
    },
    "notes": "Lookup only. Under FP-01 an endorsement of a rate calculation is evidence about the arithmetic, not the "
             "biology, and the arithmetic is checked in the repo regardless (A, A5, M-001, M-805); a credential count is "
             "no rebuttal either way, and the same standard applies to critic credentials. What is not held is listed "
             "under not_retrieved and is not estimated around: Tipler's foreword and appendix (paywalled book), "
             "Hossjer's population-genetics record, Hossjer, Bechly & Gauger 2021, the paper behind 'similar "
             "blunders', and Dembski's own arguments. No numeric weight is assigned.",
})
