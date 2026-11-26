#!/usr/bin/env python3
"""M-112 record (model-choice, derivation): neutral fixation when a species lives fewer than 4 N_e generations.

Object: docs/research/math/objects.yaml M-112 (model-choice, derivation). A reader ("EF") relays Gemini (mailvox@L7-8,
rule U: a model output, not a derivation): mammalian species last 1-2 My, and if that is shorter than 4 N_e
generations "almost nothing" fixes by drift within the species. Day (mailvox@L13-14): neutral drift is not a retreat,
and a bottleneck "at the optimal population level" at most halves the fixation time; "I've done the math on that as
well". The halving is NOT asserted: no held text gives its derivation (the post gives none; "optimal population
level" is not defined in it). Recorded as unreleased.
What the record does compute is the premise on stated inputs: 4 N_e generations in years against 1-2 My, at the
textbook N_e (1e4, g 25: 1.0 My), Day's 10-23 set (33,000, g 29: 3.83 My) and Yoo's ancestral HCB N_e (1.98e5, g 25:
19.8 My); and it cites M-203 for T/4N_e over the 252,000-generation window. The premise holds or fails with N_e.
Day's own Hard Limits paper (Z22129121, the paper EF ran past Gemini; claim file B2d) says the "nothing finishes in the
species lifetime" reading is "simply wrong as a claim about throughput" and narrows the claim to "the pipeline cannot
fill": the relayed Gemini premise and Day's paper are not the same claim. Steady-state throughput and the fill state
are M-111/M-201 and M-202 (cited, not redone). Exact rationals.

Run: research/.venv/bin/python -I docs/research/math/records/M-112.py [--write]
Without --write it checks that M-112.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
REC = "docs/research/math/records/"
RAW = {"mailvox": "sources/raw/refresh-2026-11-01/p-mailvox-gemini-and-the-hard-limits/body.txt",
       "evo007": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-007/body.txt"}
B2D = "docs/research/claims/B2d-parallel-fixation-second-objection.md"
PY = "docs/research/parameters.yaml"


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
G_4NE = post("mailvox", "If a species’ lifespan is shorter than (4N_{e}) generations, almost nothing that arises during "
                        "that species’ existence will ever actually fix via drift while that species exists.")  # L8, relay
G_LIFE = raw("mailvox", "Many mammalian species only exist in the fossil record for 1 to 2 million years before going "
                        "extinct or splitting into new daughter species.")                    # mailvox@L7, relay
D_RETREAT = post("mailvox", "A lot of people haven’t understood yet that Neutral Drift aka substitution is not a viable "
                            "retreat from the impossibility of evolution by natural selection.")  # mailvox@L13
D_HALF = held(SM + "mailvox.md", "The most a bottleneck accomplishes at the optimal population level, on the "
                                 "low-percentage chance that the species survives, is to reduce the fixation time by "
                                 "one-half, which isn’t enough to make a difference.")       # mailvox@L14
raw("mailvox", "The most a bottleneck accomplishes at the optimal population level, on the low-percentage chance that "
               "the species survives, is")                                                    # the held body splits
raw("mailvox", "to reduce the fixation time by one-half")                                     # the sentence over L14-16
D_MATH = raw("mailvox", "because I’ve done the math on that as well.")                       # mailvox@L14: no derivation
ROW14 = held(SM + "mailvox.md", "P: Day's own calculation (unreleased here).")
HL_THRU = held(B2D, "“Nothing finishes in the species lifetime” is simply wrong as a claim about throughput, and the "
                    "drift limit does not depend on it.")                                     # Z22129121, Second Objection
HL_FILL = held(B2D, "The correct interpretation is narrower: the pipeline cannot fill.")
HL_FLUX = held(B2D, "At steady state the total flux out is μ per site regardless of how long any individual site took "
                    "to traverse.")
D_33 = post("evo007", "when you set human parameters (N_e ≈ 33,000, s̄ ≈ 0.001, generation time ≈ 29 years, "
                      "d ≈ 0.45), you get an answer")                                         # evo007@L32
held(PY, "Ne_modern_human: {value: 1.0e4, source: textbook")          # population.Ne_modern_human
held(PY, "yoo_2025_HCB: {value: 1.98e5")                              # population.Ne_ancestral_hc.yoo_2025_HCB
held(PY, "day_2026: {value: 25, source: Z23003785")                   # generation_time_years.day_2026

# ---- the premise: 4 N_e generations in years against a 1-2 My species life ---------------------------------------
LIFE = (10 ** 6, 2 * 10 ** 6)
pipe = {"Ne_1e4_g25": 4 * 10_000 * 25, "Ne_33000_g29": 4 * 33_000 * 29, "Ne_198000_g25": 4 * 198_000 * 25}
assert pipe == {"Ne_1e4_g25": 1_000_000, "Ne_33000_g29": 3_828_000, "Ne_198000_g25": 19_800_000}
assert LIFE[0] <= pipe["Ne_1e4_g25"] < LIFE[1]                       # textbook N_e: 4 N_e is inside the 1-2 My range
assert pipe["Ne_33000_g29"] > LIFE[1] and pipe["Ne_198000_g25"] > LIFE[1]   # premise holds on these
lo_ne = Fr(LIFE[0], 4 * 25); hi_ne = Fr(LIFE[1], 4 * 25)
assert (lo_ne, hi_ne) == (10_000, 20_000)                            # at g = 25 the premise needs N_e > 10,000-20,000
t4 = cited("M-203", "T_over_4Ne")                                    # T = 252,000 generations over 4 N_e (M-203)
assert t4["10000"] == 6.3 and near(t4["33000"], 1.90909, 1e-5) and near(t4["198000"], 0.318182, 1e-6)
# the halving: no held derivation, so nothing is asserted about it
HALVING_DERIVED_IN_HELD_TEXT = False

finish({
    "object": "M-112",
    "inputs": [
        {"name": "species lifespan", "value": "1-2 My", "cite": "mailvox@L7 (Gemini via EF, relay, rule U)"},
        {"name": "N_e", "value": [10_000, 33_000, 198_000], "cite": "parameters population.Ne_modern_human; evo007@L32 (Day 10-23); parameters population.Ne_ancestral_hc.yoo_2025_HCB"},
        {"name": "generation length (years)", "value": [25, 29], "cite": "parameters generation_time_years.day_2026; evo007@L32 (no held source, M-114)"},
        {"name": "T/4N_e over 252,000 generations", "value": t4, "cite": "M-203"},
    ],
    "values": {
        "four_Ne_years": pipe,
        "Ne_needed_at_g25_for_premise": [10_000, 20_000],
        "halving_derived_in_held_text": HALVING_DERIVED_IN_HELD_TEXT,
    },
    "positions": {
        "day": {"reading": "neutral drift is no retreat; bottlenecks or deme replacement at best halve the fixation time "
                           "(\"done the math\")",
                "holds": "the premise holds at N_e of 33,000 (3.83 My) or 198,000 (19.8 My) against 1-2 My; the "
                         "halving is unreleased here (no derivation held), so it is neither confirmed nor refuted"},
        "critic": {"reading": "Gemini's concessions are an LLM output; the lifespan premise and what counts as one "
                              "lineage are open",
                   "holds": "at the textbook N_e = 1e4, 4 N_e = 1.0 My, inside the 1-2 My range, so the premise depends "
                            "on N_e; Day's own Hard Limits paper calls 'nothing finishes in the species lifetime' "
                            "'simply wrong as a claim about throughput' (B2d), and narrows to the fill state (M-202)"},
    },
    "notes": "Model-choice: no single number settles it. The halving at 'the optimal population level' has no held "
             "derivation (mailvox@L14 'I've done the math on that as well'); it is recorded as unreleased, not "
             "asserted. The relayed Gemini sentence is rule U. Whether a species boundary ends a lineage for fixation "
             "counting (daughter species inherit the 'unresolved pipeline', mailvox@L8) is not settled by any held "
             "derivation. Steady-state throughput (mu per site) versus fill state is M-111/M-201 and M-202.",
})
