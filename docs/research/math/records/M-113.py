#!/usr/bin/env python3
"""M-113 record (formula, lookup): Kimura's fixation probability for a new mutation, as Day prints it.

Object: docs/research/math/objects.yaml M-113 (formula, lookup). Day (evo007@L21): "P(fix) = (1 – e^(-2s)) /
(1 – e^(-4Ns))". Standard form: Kimura 1962 Eq. 8, u(p) = (1 - e^(-4Nsp))/(1 - e^(-4Ns)), at p = 1/(2N) gives Eq. 10,
U = (1 - e^(-2s))/(1 - e^(-4Ns)) (claim file B7a; Kimura's single N is the number of reproducing individuals). The
printed form is Eq. 10 term for term; asserted symbolically on a grid (Eq. 8 at p = 1/(2N) equals the printed form)
and at the two limits Kimura states: s -> 0 gives 1/(2N) (N = 1e4, s = 1e-12: 5e-5), and large positive Ns gives
about 2s (N = 1e4, s = 0.001: 0.0019980, 0.1% under 2s). The F4 rows (N = 100 and 500, s = 0.01) reproduce. Where
the effective size differs from N, the general diffusion form is u = (1 - e^(-4 N_e s p))/(1 - e^(-4 N_e s)) with
p = 1/(2N) (as M-222 codes it); the printed form is its N_e = N case, which Day's "N_e is estimated" (evo007@L22)
does not specify. The throughput question is separate (M-106, M-605). Records already using this form: M-106, M-605
(the printed form), M-222 (the N_e, p form). Floats via math.expm1 (no cancellation as s -> 0).

Run: research/.venv/bin/python -I docs/research/math/records/M-113.py [--write]
Without --write it checks that M-113.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
SM = "docs/research/math/sources/"
RAW = {"evo007": "sources/raw/refresh-2026-11-01/p-erika-and-the-evo-avengers-007/body.txt"}
B7A = "docs/research/claims/B7a-kimura-1962-fixation-probability.md"


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


def g(x):
    return float(f"{x:.6g}")


# ---- the source sentences ------------------------------------------------------------------------------
D_FORM = post("evo007", "P(fix) = (1 – e^(-2s)) / (1 – e^(-4Ns))")                           # evo007@L21
D_KIM = raw("evo007", "Kimura’s fixation probability for a new mutation is:")                  # evo007@L20
D_NS = raw("evo007", "You do need N and s.")                                                    # evo007@L22
D_NE = raw("evo007", "N_e is estimated (he’d cite the textbook ~10,000, we’ve calculated ~33,000, but either way it’s "
                     "a number)")                                                               # evo007@L22
ROW21 = held(SM + "evo007.md", "Form matches the standard new-mutation expression (initial frequency 1/2N)")
K_EQ10 = held(B7A, "The probability of fixation of an individual mutant gene is obtained from (8) by putting "
                   "p = 1/(2N).")                                                               # Kimura 1962 p.715
K_S0 = held(B7A, "if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene.")  # p.716
K_2S = held(B7A, "the probability of ultimate survival of an advantageous mutant gene is approximately twice the "
                 "selection coefficient")                                                       # p.716
K_N = held(B7A, "where N is the number of reproducing individuals in the population.")         # p.714 Eq. 6
K_FORMS = held(B7A, "u(p) = (1 − e^{−4Nsp})/(1 − e^{−4Ns}) (Eq. 8); at p = 1/(2N): U = (1 − e^{−2s})/(1 − e^{−4Ns}) "
                    "(Eq. 10)")
F4_ROW = held(SM + "branch-F.md", "Kimura u at N = 100, s = 0.01: sim 0.019995 vs 0.020171; N = 500: 0.019745 vs 0.019801")

# ---- the formula as printed, and Kimura's Eq. 8 ---------------------------------------------------------------
def printed(s, n):
    return math.expm1(-2 * s) / math.expm1(-4 * n * s)


def eq8(p, s, n):
    return math.expm1(-4 * n * s * p) / math.expm1(-4 * n * s)


def general(s, n, ne):                                               # diffusion form with N_e != N, p = 1/(2N)
    return math.expm1(-4 * ne * s / (2 * n)) / math.expm1(-4 * ne * s)


for n in (100, 500, 10_000, 33_000):
    for s in (1e-9, 1e-5, 1e-3, 1e-2, -1e-4):
        a, b = printed(s, n), eq8(1 / (2 * n), s, n)
        assert abs(a - b) <= 1e-12 * abs(b), (n, s)                    # Eq. 8 at p = 1/(2N) is the printed form
        assert abs(general(s, n, n) - a) <= 1e-12 * abs(a)            # the N_e = N case of the general form

# ---- the two limits on stated examples ------------------------------------------------------------------------
N = 10_000
u0 = printed(1e-12, N)
near(u0, 1 / (2 * N), 1e-12)                                         # s -> 0: 1/(2N) = 5e-5
u3 = printed(1e-3, N)                                                # 4Ns = 40
near(u3, 0.0019980013, 1e-10)
near(u3 / (2 * 1e-3), 0.9990007, 1e-7)                               # 2s to 0.1%
near(printed(1e-3, 1e6) / 2e-3, 0.9990007, 1e-7)                     # large N: 1 - e^(-2s), N drops out
assert abs(printed(1e-3, 1e6) - (-math.expm1(-2e-3))) < 1e-15
near(1 / u3, 500.5, 0.05)                                            # ~1 in 500 (Fisher's "500 to 1", D7)
# the F4 rows (Kimura column)
near(printed(0.01, 100), 0.020171, 5e-7); near(printed(0.01, 500), 0.019801, 5e-7)
# a deleterious new mutation, same formula
assert printed(-1e-4, N) < 1 / (2 * N)
# N_e != N moves it: N = 1e4, N_e = 3,300, s = 0.001 (the general form)
ue = general(1e-3, N, 3_300)
near(ue, 0.0006598, 5e-8)                                            # ~2 s N_e/N / (1 - e^(-4 N_e s)): 0.33 x 2s

finish({
    "object": "M-113",
    "inputs": [
        {"name": "formula as printed", "value": "(1 - e^(-2s)) / (1 - e^(-4Ns))", "cite": "evo007@L21"},
        {"name": "standard form", "value": "Kimura 1962 Eq. 8 at p = 1/(2N) = Eq. 10", "cite": "claim file B7a (Kimura 1962 pp.714-716)"},
        {"name": "examples", "value": {"N": [100, 500, 10_000, 1_000_000], "s": [1e-12, 1e-3, 1e-2]}, "cite": "the audit's test points; F4 row (branch-F.md)"},
    ],
    "values": {
        "printed_equals_kimura_eq10": True,
        "s_to_0_N_1e4": g(u0), "one_over_2N": 5e-05,
        "N_1e4_s_1e-3": g(u3), "ratio_to_2s": g(u3 / 2e-3),
        "F4_rows": {"N100_s0.01": g(printed(0.01, 100)), "N500_s0.01": g(printed(0.01, 500))},
        "general_form_N_1e4_Ne_3300_s_1e-3": g(ue),
    },
    "positions": {
        "day": {"reading": "the formula needs N and s and then gives an answer; the throughput question is separate",
                "holds": "the printed form is Kimura's Eq. 10 exactly, with both of Kimura's limits (1/2N, about 2s)"},
        "critic": {"reading": "Hancock agrees N and s determine P(fix); it varies with demography and the DFE",
                   "holds": "the printed form has one N; where N_e differs from N the general form moves it (0.33 x 2s "
                            "at N = 1e4, N_e = 3,300, s = 0.001), so which N is entered is a model choice (M-209)"},
    },
    "notes": "Lookup: the printed formula matches the standard new-mutation expression (initial frequency 1/(2N)) "
             "term for term. Kimura 1962 has a single N (reproducing individuals), so the printed form does not "
             "itself say whether N is census or effective; Day's text says N_e is 'estimated' and names 10,000 or "
             "33,000 (M-114). The throughput claim that the DFE shape cancels is M-106; P(fix) against the "
             "substitution rate is M-605.",
})
