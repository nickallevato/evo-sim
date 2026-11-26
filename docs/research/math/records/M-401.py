#!/usr/bin/env python3
"""M-401 record: size of protein sequence space against the count of molecules ever.

Object: docs/research/math/objects.yaml M-401 (identity, derivation). Eden's talk (Wistar p.7, claim file
D3 q1) gives 20^250 = 'about 10^325' sequences of length 250; his working paper (p.110, held in claim
file D3) prints 10^350 for 'length 250 or less'; Day (claim file D q1) relays 10^325 against 10^52
'functional proteins'. The record computes 20^250 in exact integers (mantissa and exponent), the sum over
all lengths <= 250 (which does not reach 10^350), and the explored fraction against Eden's printed 10^52,
his working paper's 10^55, the 10^55.02 that his p.7 inputs give (M-402) and his 'say 10^40' species.
Inputs carry their claim file and quote number; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-401.py [--write]
Without --write it checks that M-401.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D, D3 = CL + "D-sequence-space-wistar.md", CL + "D3-eden-sequence-space-arithmetic.md"


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


def log10_int(n):
    """log10 of a big exact integer, without float overflow."""
    s = str(n)
    return len(s) - 1 + math.log10(int(s[:17]) / 10 ** 16)


# ---- inputs -------------------------------------------------------------------------------
DQ1 = held(D, "Eden had already shown this: the space of 250-residue proteins is ~10^325, and the number of functional "
              "proteins that have ever existed is ~10^52.")
D3Q1 = held(D3, "We may think of words which are 250 letters long, constructed from an alphabet of 20 different letters. "
                "There are about 20250 such words or about 10 325 •")
D3WP = held(D3, "Now the space of all polypeptide sequences of length 250 or less contains about 10 350 members. Over the "
                "last billion years a very liberal estimate of the number of genetic couplings is about 1037 • In fact the "
                "number of protein molecules of such size that ever existed on earth can be estimated to be less than 10 55 •")
D3OCR = held(D3, "OCR renders 20^250 as '20250', 10^325 as '10 325 •', 10^52 as '10 52 •', 10^40 as '1040'.")
D3Q2 = held(D3, "The number of protein molecules that ever existed is by this computation about 10 52 •")
D3Q3 = held(D3, "Clearly the number of species of protein molecules is much smaller than this, say 1040, but it would be "
                "immaterial to our purposes to try to make such a reduction.")
A, L = 20, 250

# ---- 20^250 in exact integers --------------------------------------------------------------
S = A ** L
digits = str(S)
assert len(digits) == 326                                # S = m x 10^325
mant = int(digits[:4]) / 1000
near(mant, 1.809, 0.0005)                               # 1.81e325 (claim files D, D3)
logS = log10_int(S)
near(logS, L * math.log10(A), 1e-9)
near(logS, 325.257, 0.0005)                             # object: 10^325.257
assert round(logS) == 325                               # Eden p.7 'about 10^325'

# ---- working paper: 'length 250 or less ... about 10^350' ----------------------------------
S_le = (A ** (L + 1) - A) // (A - 1)                    # sum over lengths 1..250, exact
near(S_le / S, 20 / 19, 1e-12)                          # 1.0526 x 20^250
logS_le = log10_int(S_le)
near(logS_le, 325.280, 0.0005)                          # claim file D3: 10^325.3
gap_wp = 350 - logS_le
near(gap_wp, 24.72, 0.005)                              # the printed 10^350 is 24.7 orders too high
near(math.log2(10) * 350, 1162.7, 0.05)                 # bits for 10^350 (Wright quotes it, M-407)

# ---- explored fraction against the molecule counts ----------------------------------------
counts = {"talk_p7_printed": 52.0, "working_paper_p110_bound": 55.0, "p7_inputs_recomputed_M402": 55.02,
          "species_say_1e40": 40.0}
ratio = {k: v - logS for k, v in counts.items()}
near(ratio["talk_p7_printed"], -273.257, 0.0005)        # object and claim file D: 10^-273.3
near(ratio["working_paper_p110_bound"], -270.257, 0.0005)   # claim file D3: 10^-270
near(ratio["p7_inputs_recomputed_M402"], -270.24, 0.005)
near(ratio["species_say_1e40"], -285.257, 0.0005)
# the comparison is insensitive to the count: every candidate leaves > 270 orders
assert all(r < -270 for r in ratio.values())
near(max(ratio.values()) - min(ratio.values()), 15.02, 1e-9)  # spread across the counts: 15 orders of 273

finish({
    "object": "M-401",
    "inputs": [
        {"name": "alphabet and length", "value": {"A": A, "L": L}, "cite": "claim file D3 q1 (Eden, Wistar p.7)"},
        {"name": "Eden talk figures", "value": {"S": "about 10^325", "molecules": "about 10^52", "species": "say 10^40"},
         "cite": "claim file D3 q1, q2, q3 (Wistar p.7; OCR readings per claim file D3)"},
        {"name": "Eden working paper", "value": {"S_le_250": "about 10^350", "molecules": "less than 10^55"},
         "cite": "claim file D3 (Wistar p.110, preliminary working paper)"},
        {"name": "Day relay", "value": {"S": "~10^325", "functional proteins ever": "~10^52"}, "cite": "claim file D q1"},
        {"name": "molecule count from Eden's p.7 inputs", "value": "10^55.02", "cite": "M-402 record (claim file D3a)"},
    ],
    "values": {
        "S_20_pow_250": {"mantissa": mant, "exponent": 325, "log10": g(logS)},
        "S_lengths_le_250": {"log10": g(logS_le), "over_20_pow_250": g(S_le / S)},
        "working_paper_10_pow_350_gap_orders": g(gap_wp),
        "log10_explored_fraction": {k: g(v) for k, v in ratio.items()},
    },
    "positions": {
        "day": {"reading": "Eden's arithmetic is right and the explored fraction vanishes",
                "S_log10": g(logS), "explored_fraction_log10_at_1e52": g(ratio["talk_p7_printed"])},
        "critic": {"reading": "the size of the space bears on search only if the landscape is rugged (M-407, M-404)",
                   "number": "none: the critic position concedes the arithmetic and disputes its relevance; the search "
                             "count under cumulative selection is M-407"},
    },
    "notes": "20^250 = 1.809e325 (10^325.257) reproduces Eden's 'about 10^325'. The working paper's 10^350 for "
             "'length 250 or less' does not reproduce: all lengths up to 250 give 20/19 x 20^250 = 10^325.28, 24.7 "
             "orders below the printed figure. Against any of the molecule counts in the corpus (10^40 to 10^55.02) the "
             "explored fraction is 10^-270 to 10^-285, so the 273-order comparison does not depend on which count is "
             "used. The arithmetic is not in dispute between the sides; its bearing on search is (M-407).",
})
