#!/usr/bin/env python3
"""M-410 record: Spetner's chain, 300,000^500 to 1, and the 0.9727 per step for a 1e-6 overall chance.

Object: docs/research/math/objects.yaml M-410 (formula, derivation). Day relays Spetner (claim file D7a
q1): 1/600 for a specific change at a step, 1/500 for it to take over, 1/300,000 per step, 500 steps,
'approximately 3.6 x 10^2738 to 1' and '2.7 x 10^-2739'. The same post (claim file D7b q1, q2) works back
from a 1 in 1,000,000 target: 0.9727 per step, from 1,080,000 candidate beneficial mutations per step.
And it says (claim file D7a q2) that one cannot assume only one mutation is available at each step.
The record computes 300,000^500 in exact integers (mantissa and exponent), the reciprocal, the per-step
probability and candidate count for exactly 1e-6, and Day's printed 0.9727 and 1,080,000.

Run: research/.venv/bin/python -I docs/research/math/records/M-410.py [--write]
Without --write it checks that M-410.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D7A, D7B = CL + "D7a-spetner-chain-3.6e2738-to-1.md", CL + "D7b-0.9727-needs-1.08-million-beneficial-mutations-per-step.md"


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


# ---- inputs -------------------------------------------------------------------------------
CHAIN = held(D7A, "The chance that a specific change to a specific nucleotide will occur during a step is thus 1/600, and the "
                  "odds that it will also take over the population is 1/500. The total odds are thus 1/600 * 1/500 or "
                  "1/300,000. This needs to happen 500 times in a row (the number of steps required to arrive at a new "
                  "species). We thus need to multiply 1/300,000 by itself 500 times. The odds against this happening are "
                  "approximately 3.6 x 102738 to 1, or viewed the other way round, the chance of this happening is 2.7 x "
                  "10-2739.")
DISOWN = held(D7A, "Of course, one cannot simply assume that only one mutation is available at every step.")
STEP = held(D7B, "The smallest number that will do this is 0.9727 as 1 – (1 – 1/300,000 ) 1,080,000 = 0.9727")
CANDS = held(D7B, "So if the odds that a specific nucleotide will mutate and take over a population are to be 0.9727 for "
                  "each step, there must be 1,080,000 potential positive adaptive copying errors for each of the 500 steps "
                  "to arrive at a 1 in a 1,000,000 chance for the development of a new species.")
a, b, steps, target = 600, 500, 500, 1e-6

# ---- the chain in exact integers --------------------------------------------------------------
per = a * b
assert per == 300_000
odds = per ** steps
digits = str(odds)
assert len(digits) == 2739                         # odds = m x 10^2738
mant = int(digits[:4]) / 1000
near(mant, 3.636, 0.0005)                          # 'approximately 3.6 x 10^2738 to 1'
log_odds = steps * math.log10(per)
near(log_odds, 2738.56, 0.005)                     # object: 10^2738.56
rmant = 10 ** (1 - (log_odds - 2738))              # chance = rmant x 10^-2739
near(rmant, 2.750, 0.0005)                         # Day prints 2.7 x 10^-2739 (truncated; 2.75 rounds to 2.7/2.8)

# ---- the back-calculation of claim file D7b ------------------------------------------------------
q = 1 / per
P1_exact = 10 ** (math.log10(target) / steps)
near(P1_exact, 0.972747, 5e-7)                     # per-step success for exactly 1e-6 overall
n_exact = math.log1p(-P1_exact) / math.log1p(-q)
near(n_exact, 1_080_778, 1)                        # candidates needed for exactly 1e-6
n_day_p = math.log1p(-0.9727) / math.log1p(-q)
near(n_day_p, 1_080_259, 1)                        # candidates for Day's 0.9727
P1_day = -math.expm1(1_080_000 * math.log1p(-q))
near(P1_day, 0.972676, 5e-7)                       # 1 - (1 - 1/300,000)^1,080,000; Day prints 0.9727
near(0.9727 ** steps, 9.76e-7, 0.005e-7)           # Day's 0.9727 over 500 steps, about 1e-6
near(P1_day ** steps, 9.64e-7, 0.005e-7)           # the 1,080,000 candidates exactly
near(1_080_000 * q, 3.6, 1e-12)
near(1 - math.exp(-3.6), 0.97268, 5e-6)            # Poisson form of the same step
near((n_exact - 1_080_000) / n_exact, 7.2e-4, 0.05e-4)  # 1,080,000 is 0.07% below the exact count

finish({
    "object": "M-410",
    "inputs": [
        {"name": "per-step chance", "value": {"occur": "1/600", "take_over": "1/500"}, "cite": "claim file D7a q1"},
        {"name": "steps", "value": steps, "cite": "claim file D7a q1"},
        {"name": "target overall chance", "value": target, "cite": "claim file D7b q1, q2"},
        {"name": "candidates per step", "value": 1_080_000, "cite": "claim file D7b q1, q2"},
        {"name": "single path disowned", "value": "one cannot simply assume that only one mutation is available",
         "cite": "claim file D7a q2 (same post)"},
    ],
    "values": {
        "odds_against": {"mantissa": mant, "exponent": 2738, "log10": g(log_odds)},
        "chance": {"mantissa": g(rmant), "exponent": -2739, "printed": "2.7 x 10^-2739"},
        "per_step_for_exactly_1e-6": g(P1_exact), "candidates_for_exactly_1e-6": round(n_exact),
        "candidates_for_0.9727": round(n_day_p), "per_step_at_1080000": g(P1_day),
        "overall_at_0.9727": g(0.9727 ** steps), "overall_at_1080000": g(P1_day ** steps),
    },
    "positions": {
        "day": {"reading": "sequential specific mutations are vanishingly improbable",
                "odds_against_log10": g(log_odds), "candidates_per_step_for_1e-6": 1_080_000},
        "critic": {"reading": "the same post says the single-specific-path model is not the real count; the chain is "
                              "not a model of evolution",
                   "number": "none: the critic position rejects the model rather than offering another count; the "
                             "back-calculation (0.9727, 1,080,000) is the post's own"},
    },
    "notes": "300,000^500 = 3.636e2738 (exact integer, 2,739 digits) reproduces '3.6 x 10^2738 to 1'; the chance is "
             "2.750e-2739 against the printed 2.7 (truncated). For exactly 1e-6 overall the step must succeed with "
             "0.972747, which needs 1,080,778 candidate beneficial mutations per step; Day's 0.9727 and 1,080,000 "
             "reproduce to 0.07%. All of it assumes one specific path, which the post itself says cannot be assumed.",
})
