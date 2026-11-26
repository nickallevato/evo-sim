#!/usr/bin/env python3
"""M-411 record: the Weasel under population genetics (Day's 11,000 and 540,000 generations).

Object: docs/research/math/objects.yaml M-411 (formula, derivation). Day (Probability Weasel, claim file
D9 q1-q4): N = 10,000 weasels, a letter starts in one animal and must fix; s = 0.05 gives 400 generations
per letter and 11,000 for 27 letters, s = 0.001 gives 20,000 and 540,000; against Dawkins's 50 generations
'four orders of magnitude, or about 11,000x' (claim file D9a q1). Claim file D9 shows the per-letter
figures are the deterministic sweep time (2/s) ln(2N) and the totals are 27 letters in series. The record
asserts each printed figure, its exact value and rounding, the ratio to 50, and the critic's numbers:
the conditional-mean asymptote (2/s)(ln 4Ns + Euler gamma) of M-601 and the claim-file D9 scratch-run
means (cited, not rerun: they are simulation output), serial against parallel letters.

Run: research/.venv/bin/python -I docs/research/math/records/M-411.py [--write]
Without --write it checks that M-411.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D9, D9A = CL + "D9-weasel-540000-generations.md", CL + "D9a-weasel-demonstrates-the-opposite.md"
OBJ = "docs/research/math/objects.yaml"


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
Q1 = held(D9, "Or s=.05. With the appropriate reproductive limit of 12 rather than 100, that means it will take 400 "
              "generations for the initial letter M to propagate throughout the species, and 11,000 generations for all "
              "27 letters required to complete the phrase to do so.")
Q2 = held(D9, "around s=0.001. And this gives us 20,000 generations for the initial letter M and 540,000 generations to "
              "complete the full phrase.")
Q3 = held(D9, "So plug in the real animal, with a minimum population of 10,000 so it’s not going extinct,")
Q4 = held(D9, "A phrase letter initially appears in one weasel out of 10,000. For that letter to count toward completing the "
              "phrase, all 10,000 weasels have to end up carrying it.")
A1 = held(D9A, "since his estimate of 50 generations was off by four orders of magnitude, or about 11,000x.")
A2 = held(D9A, "the target phrase is known from the start, which is not the case in the evolutionary context.")
SCR1 = held(D9, "- s = 0.001: 2,409 fixations of 1.2e6 replicates (P_fix 0.00201; Kimura 0.00200); mean fixation time "
                "**8,525 +- 39**, sd 1,914. Serial 27 letters: mean total 230,053. Parallel, maximum of 27 independent "
                "draws (bootstrap): mean **13,092** (5th-95th percentile 10,992-15,417).")
SCR2 = held(D9, "- s = 0.05: 5,656 fixations of 60,000 replicates (P_fix 0.0943; Kimura 0.0952); mean **332**; diffusion "
                "326; Day's 396. Serial 27: 8,956; parallel max of 27: 422 (5th-95th 380-477).")
M601 = held(OBJ, "the stochastic conditional mean is (2/s)(ln 4Ns + gamma) = 8,532")

N, letters, dawkins = 10_000, 27, 50
EULER = 0.5772156649015329


def sweep(s):
    return (2 / s) * math.log(2 * N)


def cond_mean(s):
    return (2 / s) * (math.log(4 * N * s) + EULER)


# ---- Day's figures --------------------------------------------------------------------------
t05, t001 = sweep(0.05), sweep(0.001)
near(t05, 396.14, 0.005)                           # Day '400'
near(t001, 19_806.98, 0.01)                        # Day '20,000'
assert round(t05) == 396 and round(t05, -2) == 400 and round(t001, -3) == 20_000
T05, T001 = letters * t05, letters * t001
near(T05, 10_695.8, 0.05)                          # claim file D9: 10,696
assert letters * 396 == 10_692                     # object: 27 x 396 (per-letter value rounded first)
assert letters * 400 == 10_800                     # Day '11,000' rounds 27 x 400
near(T001, 534_788.3, 0.1)                         # claim file D9: 534,788
assert letters * 20_000 == 540_000                 # Day '540,000' = 27 x the rounded 20,000
near(540_000 / T001, 1.0097, 0.0001)               # Day's rounding adds 1%
ratio = 540_000 / dawkins
assert ratio == 10_800                             # 'about 11,000x'
near(math.log10(ratio), 4.033, 0.0005)             # 'four orders of magnitude'

# ---- critic: conditional mean and parallel letters -----------------------------------------------
c001, c05 = cond_mean(0.001), cond_mean(0.05)
near(c001, 8_532, 1)                               # M-601 asymptote; claim file D9 scratch 8,525 +- 39
near(c05, 327.1, 0.05)                             # claim file D9: diffusion 326, scratch 332
near(t001 / 8_525, 2.32, 0.005)                    # per-letter figure overstated 2.3x (claim file D9)
near(letters * 8_525, 230_175, 0)                  # serial with the conditional mean; scratch serial total 230,053
near(540_000 / 13_092, 41.2, 0.05)                 # '41x below 540,000' (parallel maximum, scratch)
near(13_092 / dawkins, 261.8, 0.05)                # parallel maximum is still 262x Dawkins's 50
near(422 / dawkins, 8.44, 0.005)                   # at s = 0.05, parallel maximum 422

finish({
    "object": "M-411",
    "inputs": [
        {"name": "population", "value": N, "cite": "claim file D9 q3, q4"},
        {"name": "selection coefficients", "value": [0.05, 0.001], "cite": "claim file D9 q1, q2"},
        {"name": "letters, in series", "value": letters, "cite": "claim file D9 q1"},
        {"name": "Dawkins's generations", "value": dawkins, "cite": "claim file D9a q1"},
        {"name": "scratch-run means (simulation, not recomputed)",
         "value": {"s0.001": {"per_letter": 8525, "serial": 230053, "parallel_max": 13092},
                   "s0.05": {"per_letter": 332, "serial": 8956, "parallel_max": 422}},
         "cite": "claim file D9 Check (exploratory, not committed, not an R4 check)"},
        {"name": "conditional-mean asymptote", "value": "(2/s)(ln 4Ns + gamma)", "cite": "objects.yaml M-601 (open)"},
    ],
    "values": {
        "per_letter_sweep": {"s0.05": g(t05), "s0.001": g(t001)},
        "serial_27": {"s0.05": g(T05), "s0.001": g(T001)},
        "printed": {"s0.05": [400, 11_000], "s0.001": [20_000, 540_000]},
        "ratio_to_50": ratio, "log10_ratio": g(math.log10(ratio)),
        "conditional_mean_asymptote": {"s0.05": g(c05), "s0.001": g(c001)},
    },
    "positions": {
        "day": {"reading": "fixation times applied to the Weasel give 540,000 generations, 10,800x Dawkins's 50",
                "serial_27_s0.001": 540_000, "ratio": ratio},
        "critic": {"reading": "the Weasel is truncation selection on a known target (a different model, conceded in "
                              "D9a q2); within Day's model the serial sum overstates the time",
                   "per_letter_conditional_mean_s0.001": 8525, "parallel_max_27_s0.001": 13092,
                   "parallel_over_dawkins": g(13_092 / dawkins)},
    },
    "notes": "Every printed figure reproduces from (2/s) ln(2N) and a serial sum over 27 letters: 396 and 19,807 per "
             "letter, 10,696 and 534,788 in total (Day rounds per letter first: 27 x 400 = 10,800 shown as 11,000, 27 x "
             "20,000 = 540,000); 540,000/50 = 10,800, 10^4.03. Within Day's own model the per-letter sweep time is 2.3x "
             "the conditional mean (8,532 asymptote; 8,525 simulated) and letters at independent sites need not fix "
             "in series: the parallel maximum is about 13,100, 41x below 540,000 and still 262x Dawkins's 50. Which "
             "model describes the program is M-408, not this record.",
})
