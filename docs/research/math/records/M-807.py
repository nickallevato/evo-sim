#!/usr/bin/env python3
"""M-807 record (derivation, units): Worden's O(1) bits per generation against the Haldane-scale limit.

Object: docs/research/math/objects.yaml M-807 (inference, derivation). Day (H4 q1): "O(1) bits per generation is
exactly the the same as the Haldane-scale limit." Haldane's limit is 1/300 = 0.0033 substitutions per generation
(M-801). An information rate of c bits per generation equals that substitution rate only if each substitution carries
b = 300c bits: about 300 bits at c = 1. At one bit per substitution the information limit allows c substitutions per
generation, 300 times faster at c = 1. Haldane counts deaths (30 N per substitution), Worden counts information; the
quoted sentence gives no bits-per-substitution conversion. Worden 1995 is not retrieved (the claim file H4 paraphrases
it through Day). Exact rationals (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-807.py [--write]
Without --write it checks that M-807.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
H4 = CL + "H4-worden-speed-limit.md"
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
H4Q1 = held(H4, "Worden’s O(1) bits per generation. Yudkowsky doesn’t refute it. And O(1) bits per generation is "
                "exactly the the same as the Haldane-scale limit.")                                       # H4 q1 (para 9)
H4Q2 = held(H4, "Each beneficial fixation still requires selective deaths to drive it to fixation.")     # H4 q2 (para 7)
NOTRET = held(H4, "Worden 1995 (as paraphrased by Day; the text was not retrieved)")
UNITS = held(H4, "O(1) bits per generation, with the constant unspecified, equals Haldane's 1/300 substitutions per "
                 "generation (0.0033/gen) only if each substitution carries about 300 bits (if one substitution is one "
                 "bit the limit is 300 times faster).")
held(PY, "gens_per_substitution: {value: 300")                     # haldane.gens_per_substitution (M-801)
HALDANE = Fr(1, 300)                                                # substitutions per generation

# ---- the unit conversion -------------------------------------------------------------------------------
near(float(HALDANE), 0.0033, 5e-5)                                  # 1/300 = 0.0033
bits_needed = lambda c: c / HALDANE                                 # bits per substitution for equality at c bits/gen
assert bits_needed(1) == 300                                        # O(1) with c = 1: 300 bits per substitution
assert bits_needed(Fr(1, 2)) == 150 and bits_needed(3) == 900       # the constant c is unspecified: any 300c fits
subs_rate = lambda c, b: Fr(c) / b                                  # substitutions per generation at b bits each
assert subs_rate(1, 1) / HALDANE == 300                             # one bit per substitution: 300 times faster
assert subs_rate(1, 300) == HALDANE                                 # equality only at b = 300c
assert all(subs_rate(1, b) != HALDANE for b in (1, 2, 10, 100, 299, 301))   # no other b at c = 1
# Haldane's unit is deaths: 30 N per substitution, 0.1 N per generation; N appears, bits do not
deaths_per_sub = lambda n: 30 * n
assert deaths_per_sub(10_000) / (Fr(1, 10) * 10_000) == 300         # the death budget fixes 300 with no bit count

finish({
    "object": "M-807",
    "inputs": [
        {"name": "Haldane rate", "value": "1/300 per generation", "cite": "M-801; parameters haldane.gens_per_substitution"},
        {"name": "Worden bound", "value": "O(1) bits per generation, constant unspecified", "cite": "H4 q1 (Day's paraphrase; Worden 1995 not retrieved)"},
    ],
    "values": {
        "haldane_per_generation": round(float(HALDANE), 5),
        "bits_per_substitution_for_equality": {"c=1/2": 150, "c=1": 300, "c=3": 900},
        "speedup_at_1_bit_per_substitution": 300,
    },
    "positions": {
        "day": {"reading": "Worden's O(1) bits per generation is exactly the same as the Haldane-scale limit",
                "holds": "both are O(1)-scale ceilings on adaptive change, and they coincide if a substitution carries about 300 bits"},
        "critic": {"reading": "the equivalence needs a bits-per-substitution conversion the post does not give",
                   "holds": "equality holds only at b = 300c; at one bit per substitution the information limit is 300x faster; "
                            "Haldane counts deaths (30 N), Worden counts bits"},
    },
    "notes": "Units only. O(1) bits per generation equals 1/300 substitutions per generation only when each substitution "
             "carries 300c bits, with c the unstated constant; nothing in the quoted sentence or the held paraphrase "
             "fixes c or b. At b = 1 the information bound allows 300 times the Haldane rate. 'Exactly the same' is "
             "therefore a conditional equivalence. Worden 1995 is not retrieved, so the bound's own derivation is not "
             "checked here.",
})
