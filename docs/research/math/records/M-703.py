#!/usr/bin/env python3
"""M-703 record (derivation): joint probability of a pre-specified set of fixations, P = p^n.

Object: docs/research/math/objects.yaml M-703 (formula, derivation). Three (p, n) pairs, each in log10 because the
values underflow: Ga (Z18165980 para 24, Q11) p = 0.02 = 2s at s = 0.01, n = 2e7: 10^-33,979,400 (printed
10^-34,000,000, an exponent gap of 20,600, 0.06%); Gb (Z18167588 s4.1, Q28) p = 0.5, n = 157,000: 10^-47,261.7
(printed 10^-47,262); the Darwillion as McCarthy renders it (MC-01, Q71, secondhand) (1/20,000)^(2e7):
10^-86,020,600. Timing-independence is asserted on rationals: the product of the n factors is the same under any
order or schedule of the events. The independence check (joint/product 1.03 at free recombination; 0.84 / 0.65
linked) is a simulation result quoted from R4 G1, not rerun. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-703.py [--write]
Without --write it checks that M-703.json is current; --write saves it.
"""
import hashlib, itertools, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G = CL + "G-bernoulli-barrier.md"
GA = CL + "Ga-p-to-the-n-0p02.md"
GB = CL + "Gb-half-to-157000.md"
G3 = CL + "G3-specific-vs-any.md"
G4 = CL + "G4-darwillion-definition.md"
QD = "docs/research/sources/quotes-day.md"
QC = "docs/research/sources/quotes-critics.md"
PY = "docs/research/parameters.yaml"
R4G1 = "research/checks/results/R4-G1.md"


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
Q11 = ("For n = 20,000,000 fixations (human-chimp divergence, human lineage) and p = 0.02: P(all) ≈ 0.02^20,000,000 "
       "≈ 10^−34,000,000")
held(GA, Q11); held(QD, Q11)                                      # Ga q1 = Q11 (Z18165980 para 24)
Q28 = "P(all beneficial) = (0.5)¹⁵⁷'⁰⁰⁰ = 10⁻⁴⁷'²⁶²"
held(GB, Q28); held(QD, Q28)                                      # Gb q1 = Q28 (Z18167588 para 45, s4.1)
MC01 = ("What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list "
        "of 20 million mutations (or 20 million mutations in a row) would all become fixed.")
held(G3, MC01); held(QC, MC01)                                    # G3 q1 = MC-01 (exponent flattened in the HTML)
Q71 = held(QD, "What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified "
               "list of 20 million mutations")                     # G4 q2 = Q71 (Day relaying McCarthy, secondhand)
held(G4, Q71)
KIM = held(G, "the probability of ultimate survival of an advantageous mutant gene is approximately twice the "
              "selection coefficient")                            # Kimura 1962, G Primary literature
TWO_S = held(GA, "The value p = 0.02 = 2s for s = 0.01")
NREQ = 2.0e7; held(PY, "day_2025: {value: 2.0e7, source: Z18165980")   # divergence.required_fixations.day_2025
IND = held(GA, "independence holds with free recombination (joint/product 1.03 +/- 0.02); joint < product when "
               "linked (0.84 / 0.65) or clonal (0), Day's stated direction. p^n is timing-independent.")
G1_TIME = held(R4G1, "p^n does not depend on timing, so it cannot force sequential fixation.")


def log10_pn(p, n):
    return n * math.log10(p)


# ---- the three pairs -------------------------------------------------------------------------------
S = 0.01
assert 2 * S == 0.02                                              # p = 2s (Kimura 1962)
ga = log10_pn(0.02, NREQ)
near(ga, -33_979_400, 0.5)                                        # 10^-33,979,400
printed_ga = -34_000_000
near(ga - printed_ga, 20_600, 0.5)                                # exponent gap to the printed figure
near((ga - printed_ga) / printed_ga, -0.000606, 5e-6)             # 0.06% of the exponent
assert round(ga, -6) == printed_ga                                # rounds to the printed 10^-34,000,000
gb = log10_pn(0.5, 157_000)
near(gb, -47_261.7, 0.05); assert round(gb) == -47_262            # printed 10^-47,262
dw = log10_pn(1 / 20_000, NREQ)
near(dw, -86_020_600, 0.5)                                        # Darwillion as rendered: 10^-86,020,600
near(dw / ga, 2.532, 5e-4)                                        # the two 2e7-fixation figures differ 2.5x in log
assert len({(0.02, NREQ), (0.5, 157_000), (1 / 20_000, NREQ)}) == 3   # three different (p, n) pairs

# ---- timing-independence, exact on rationals -------------------------------------------------------
ps = [Fr(1, 50), Fr(1, 2), Fr(1, 20_000), Fr(3, 7)]               # heterogeneous p_i, product of four events
prods = {math.prod(order) for order in itertools.permutations(ps)}
assert len(prods) == 1                                            # any order (serial or simultaneous): one value
for n in (3, 10):                                                 # homogeneous case: p^n has no T or schedule term
    assert math.prod([Fr(1, 50)] * n) == Fr(1, 50) ** n
assert "1.03" in IND and "0.84 / 0.65" in IND                     # independence (quoted from R4 G1, not rerun)

finish({
    "object": "M-703",
    "inputs": [
        {"name": "Ga p, n", "value": [0.02, NREQ], "cite": "Ga q1 = Q11; parameters divergence.required_fixations.day_2025; p = 2s (Kimura 1962, G)"},
        {"name": "Gb p, n", "value": [0.5, 157000], "cite": "Gb q1 = Q28"},
        {"name": "Darwillion p, n (secondhand)", "value": [1 / 20000, NREQ], "cite": "G3 q1 = MC-01; G4 q2 = Q71"},
        {"name": "joint/product under free recombination", "value": 1.03, "cite": "R4 G1 via Ga Check (quoted, not rerun)"},
    ],
    "values": {
        "log10_P": {"Ga_0.02^2e7": round(ga, 1), "Gb_0.5^157000": round(gb, 2), "Darwillion_(1/20000)^2e7": round(dw, 1)},
        "Ga_printed_gap": {"exponent": round(ga - printed_ga, 1), "fraction": round((ga - printed_ga) / printed_ga, 6)},
        "Darwillion_over_Ga_log_ratio": round(dw / ga, 4),
    },
    "positions": {
        "day": {"reading": "P(all) = p^n is the probability that all required fixations occur",
                "holds": "every printed power reproduces (Ga to 0.06% of the exponent; Gb and the Darwillion exactly)"},
        "critic": {"reading": "p^n prices a pre-specified set of arisings and has no timing term",
                   "holds": "the product is order- and schedule-invariant (exact), so it cannot force sequential fixation"},
    },
    "notes": "The three figures are three (p, n) pairs, not one quantity: 0.02^(2e7), 0.5^157,000 and (5e-5)^(2e7). "
             "Each is a product of per-event probabilities and so is the same for any ordering or overlap of the events "
             "(asserted on rationals). Independence is a modelling premise; R4 G1's simulation gives joint/product 1.03 "
             "at free recombination and below 1 when linked (Day's direction), quoted here. Which event the history "
             "requires (a named list or any k of M) is M-704.",
})
