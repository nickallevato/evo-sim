#!/usr/bin/env python3
"""M-403 record (empirical, data-check): the prevalence of function in random sequence, three measurements.

Object: docs/research/math/objects.yaml M-403. Axe 2004 (claim file D10): about 1 in 10^64 signature-consistent
sequences forms a working domain, overall 'as low as 1 in 10^77'; against Eden's 10^52 molecules ever (Day's relay,
claim file D q1) that is 10^-25 expected hits. Taylor et al. 2001 (D11): a required library of 4,500 x 17,500 x 20^6
x 10^2 x 10^2 x 10^4, printed '5 x 10^23', in a space of 20^100 (printed 1.3 x 10^130), so a frequency of about
2e-24 among fully randomised 100-mers. Keefe & Szostak 2001 (D12): four ATP binders from 6 x 10^12 random 80-mers,
a frequency of at least 4 / 6e12 = 6.7e-13. The record asserts each printed figure and the spread between the
three: about 53 orders of magnitude (Axe against Taylor) and about 65 (Axe against Keefe & Szostak).

Inputs: the verbatim abstract and page quotes held in claim files D10, D11, D12 and D (each checked by held());
the papers themselves are abstracts or a user-downloaded PDF outside git (claim files name them). Exact integers
and log10 (stdlib). Runs in well under a second.

Run: research/.venv/bin/python -I docs/research/math/records/M-403.py [--write]
Without --write it checks that M-403.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
D = CL + "D-sequence-space-wistar.md"
D10 = CL + "D10-axe-2004-1-in-1e77.md"
D11 = CL + "D11-taylor-2001-1-in-5e23.md"
D12 = CL + "D12-keefe-szostak-2001-atp-binding.md"


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


def lg(x):
    """log10 of a positive Fraction or int, exact enough for order-of-magnitude statements."""
    x = Fr(x)
    return math.log10(x.numerator) - math.log10(x.denominator)


# ---- the source sentences ------------------------------------------------------------------------------
DQ1 = held(D, "the number of functional proteins that have ever existed is ~10^52.")
AXE1 = held(D10, "roughly one in 10(64) signature-consistent sequences forms a working domain.")
AXE2 = held(D10, "this implies the overall prevalence of sequences performing a specific function by any domain-sized "
                 "fold may be as low as 1 in 10(77)")
AXE_SCOPE = held(D10, "the difficulty of specifying a working beta-lactamase domain is assessed here.")
TAY1 = held(D11, "However, a 100-residue protein has 20100 (1.3 ⫻ 10130) possible sequences.")
TAY2 = held(D11, "a library of ⬇1024 members would have been needed to obtain AroQ mutases.")
TAY3 = held(D11, "4,500 (binary patterned H1) ⫻ 17,500 (binary patterned H2兾H3) ⫻ 206 (randomized active site "
                 "residues) ⫻ 102 (fully randomized L1) ⫻ 102 (fully randomized L2) ⫻ 104 (templating effects) ⫽ 5 ⫻ 1023.")
TAY4 = held(D11, "it will not be possible to isolate enzymes from unbiased random libraries in a single step.")
KS1 = held(D12, "Starting from a library of 6 x 1012 proteins each containing 80 contiguous random amino acids")
KS2 = held(D12, "This selection yielded four new ATP-binding proteins")

# ---- Axe 2004: 1e-64 per signature-consistent sequence, 1e-77 overall, 1e52 x 1e-77 = 1e-25 -------------------
f_sig = Fr(1, 10 ** 64)
f_axe = Fr(1, 10 ** 77)
n_ever = 10 ** 52                                      # Eden via Day (D q1)
assert n_ever * f_axe == Fr(1, 10 ** 25)               # expected hits among 1e52 molecules
assert f_axe / f_sig == Fr(1, 10 ** 13)                # the pattern and fold factors Axe multiplies in

# ---- Taylor 2001: the required library and the implied frequency ----------------------------------------------
n_req = 4_500 * 17_500 * 20 ** 6 * 10 ** 2 * 10 ** 2 * 10 ** 4
assert n_req == 504 * 10 ** 21                          # 5.04e23 exactly; Taylor prints '5 x 10^23'
assert round(n_req, -23) == 5 * 10 ** 23
assert 10 ** 23 < n_req < 10 ** 24                      # the '~10^24' of the p.10600 summary sentence is the round-up
f_tay = Fr(1, n_req)
near(float(f_tay), 1.984e-24, 0.001e-24)                # 'about 2e-24'
space100 = 20 ** 100
near(space100 / 1e130, 1.2677, 0.0001)                  # 1.27e130; Taylor prints 1.3 x 10^130
assert round(space100 / 1e130, 1) == 1.3

# ---- Keefe & Szostak 2001: 4 binders in 6e12 -------------------------------------------------------------------
f_ks = Fr(4, 6 * 10 ** 12)                              # a lower bound: all four present in the starting library
near(float(f_ks), 6.67e-13, 0.005e-13)

# ---- the spread between the three --------------------------------------------------------------------------------
spread_tay = near(lg(f_tay / f_axe), 53.30, 0.005)      # 'about 53 orders' (Axe 1e-77 against Taylor 2e-24)
spread_ks = near(lg(f_ks / f_axe), 64.82, 0.005)        # 'about 65' with Keefe & Szostak
spread_tay_sig = near(lg(f_tay / f_sig), 40.30, 0.005)  # on Axe's per-signature 1e-64 instead: about 40
spread_ks_tay = near(lg(f_ks / f_tay), 11.53, 0.005)    # Taylor against Keefe & Szostak: about 11.5
hits_tay = near(float(n_ever * f_tay), 1.98e28, 0.01e28)  # D11's 'expected hits 2e28' at Eden's 1e52 (different length)

finish({
    "object": "M-403",
    "inputs": [
        {"name": "Axe 2004 prevalence", "value": {"per_signature_consistent": "1e-64", "overall": "1e-77 ('as low as')"},
         "cite": "claim file D10 (abstract)", "scope": "one beta-lactamase domain, extrapolated to any domain-sized fold"},
        {"name": "Eden's molecules ever", "value": "1e52", "cite": "claim file D q1 (Day relaying Eden)"},
        {"name": "Taylor 2001 required library", "value": "4,500 x 17,500 x 20^6 x 10^2 x 10^2 x 10^4 (printed 5 x 10^23)",
         "cite": "claim file D11 q3 (p.10600)", "scope": "AroQ chorismate mutase, 100-mer, catalysis"},
        {"name": "Taylor 2001 sequence space", "value": "20^100 (printed 1.3 x 10^130)", "cite": "claim file D11 q1 (p.10596)"},
        {"name": "Keefe & Szostak 2001", "value": "4 ATP binders from 6 x 10^12 random 80-mers", "cite": "claim file D12 (abstract)",
         "scope": "ATP binding, 80-mer, not catalysis"},
    ],
    "values": {
        "axe_expected_hits_in_1e52": "1e-25",
        "taylor_required_library": float(n_req),
        "taylor_frequency": float(f"{float(f_tay):.4g}"),
        "space_20_100": float(f"{space100:.4g}"),
        "keefe_szostak_frequency_lower_bound": float(f"{float(f_ks):.4g}"),
        "orders_axe77_to_taylor": round(spread_tay, 2),
        "orders_axe77_to_keefe_szostak": round(spread_ks, 2),
        "orders_axe64_to_taylor": round(spread_tay_sig, 2),
        "orders_taylor_to_keefe_szostak": round(spread_ks_tay, 2),
        "taylor_expected_hits_in_1e52": float(f"{hits_tay:.3g}"),
    },
    "positions": {
        "day": {"reading": "functional sequences are so rare that random search fails; Taylor says one-step isolation from "
                           "unbiased libraries is impossible",
                "holds": "every printed figure reproduces: 1e52 x 1e-77 = 1e-25 expected hits; Taylor's product is 5.04e23 "
                         "(printed 5 x 10^23), a frequency of 2e-24 among fully randomised 100-mers; Taylor's own conclusion "
                         "(D11 q4) is the one-step impossibility"},
        "critic": {"reading": "the three frequencies are for different proteins, lengths and functions and differ by many orders",
                   "holds": "Axe 1e-77 to Taylor 2e-24 is 53.3 orders; to Keefe & Szostak's lower bound 6.7e-13 it is 64.8; "
                            "binding (Keefe & Szostak) is not catalysis (Taylor), and Axe's 1e-77 is a bound extrapolated from "
                            "one domain; per-sequence prevalence is not connectivity (R4 D1-spike leaves this regime untouched)"},
    },
    "notes": "Data-check object; no verdict moves. The 53 and 65 orders compare unlike quantities (lengths 80, 100 and "
             "domain-sized; binding against catalysis; Axe's figure an 'as low as' bound, Keefe & Szostak's a lower bound "
             "on frequency), so they bound the disagreement and do not average to one prevalence. On Axe's per-signature "
             "1e-64 the gap to Taylor is 40.3 orders. Taylor prints both '5 x 10^23' (the product, 5.04e23) and '~10^24' "
             "(the summary sentence); both are the same estimate rounded. No Day text in the corpus cites Axe (D10).",
})
