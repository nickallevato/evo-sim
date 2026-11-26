#!/usr/bin/env python3
"""M-305 record: the regression d = -2.242 k + 1.229 and its consequences.

Object: docs/research/math/objects.yaml M-305 (formula, derivation). The fit (k in units of mu) was run
by an unidentified "doctor" and relayed by Day (C2b q1, q2); its 24 data points are not held, so the
record does not refit it. It checks what the printed line implies at its ends (k = 0, d = 1, d = 0,
k = mu, k = 0.5 mu, d = 0.45), whether r = -0.991 and R^2 = 0.981 agree, Day's Delta-p example
(d s p (1 - p) at d = 0.08, s = 0.01, p = 0.01) and the direction of Day's "never reaches k = mu since
d < 1" against the line's own slope. Inputs carry their claim file and quote number; held() checks
each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-305.py [--write]
Without --write it checks that M-305.json is current; --write saves it.
"""
import hashlib, json, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
C2B = "docs/research/claims/C2b-d-k-regression.md"


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
Q1 = held(C2B, "This is a near-perfect linear relationship: d = −2.242k + 1.229.")
Q2 = held(C2B, "The Pearson correlation is r = −0.991 with R² = 0.981, p < 0.001.")
Q3 = held(C2B, "At d = 0.08 and initial frequency p = 0.01, that works out to a frequency change of approximately "
               "0.000008 per generation.")
Q4 = held(C2B, "The data show that k in humans has been approximately 0.5μ or less throughout the entire modern period "
               "for which we have reliable demographic data")
Q5 = held(C2B, "it never actually reaches k = μ even under pre-agricultural conditions, since d never reaches 1.0 for "
               "any human population.")
UNITS = held(C2B, "k in units of mu: \"k converges toward half the mutation rate\", ¶5")

a, b = -2.242, 1.229
d_of = lambda k: a * k + b
k_of = lambda d: (d - b) / a

# ---- ends of the line ---------------------------------------------------------------------
near(d_of(0), 1.229, 1e-12)                              # k = 0 gives d > 1, outside (0, 1] (C2a)
assert d_of(0) > 1
k_d1 = k_of(1.0)
near(k_d1, 0.102, 0.0005)                                # d = 1 (Kimura's case per the post) gives k = 0.102 mu, not mu
near(k_of(0.0), 0.548, 0.0005)                          # d = 0 gives k = 0.548 mu
near(k_of(0.45), 0.347, 0.0005)                         # d = 0.45 (parameters selection.turnover_d) gives 0.347 mu
d_k1 = d_of(1.0)
near(d_k1, -1.013, 1e-9)                                 # k = mu needs d = -1.013
d_khalf = d_of(0.5)
near(d_khalf, 0.108, 1e-9)                               # Day's "0.5 mu ceiling" is d = 0.108
assert a < 0                                             # k falls as d rises: along the line, d -> 1 moves k away from mu

# ---- r and R^2 ---------------------------------------------------------------------------
near(0.991 ** 2, 0.98208, 0.00001)                       # 0.991^2 = 0.982, printed R^2 0.981
lo, hi = 0.9905 ** 2, 0.9915 ** 2                        # r = -0.991 as rounded
assert lo <= 0.9815 and hi >= 0.9805                     # overlaps R^2 = 0.981 as rounded: consistent (|r| 0.9905-0.9907)
near(lo, 0.98109, 0.00001)

# ---- Delta-p example ----------------------------------------------------------------------
dp = 0.08 * 0.01 * 0.01 * (1 - 0.01)
near(dp, 7.92e-6, 1e-15)                                 # "approximately 0.000008"
near(dp / 8e-6, 0.99, 1e-9)

finish({
    "object": "M-305",
    "inputs": [
        {"name": "fit", "value": {"slope": a, "intercept": b, "r": -0.991, "R2": 0.981}, "cite": "C2b q1, q2 (relayed; data not held)"},
        {"name": "Delta-p example", "value": {"d": 0.08, "s": 0.01, "p": 0.01}, "cite": "C2b q3"},
        {"name": "k ceiling", "value": "0.5 mu or less", "cite": "C2b q4 (Q42)"},
        {"name": "never reaches mu", "value": "since d < 1", "cite": "C2b q5"},
        {"name": "d = 0.45", "value": 0.45, "cite": "parameters selection.turnover_d"},
    ],
    "values": {
        "d_at_k0": 1.229, "k_at_d1": g(k_d1), "k_at_d0": g(k_of(0.0)), "k_at_d045": g(k_of(0.45)),
        "d_at_k_mu": g(d_k1), "d_at_k_half_mu": g(d_khalf),
        "r_squared_from_r": 0.982081, "r_R2_consistent_range_abs_r": [0.9905, 0.9907],
        "delta_p": dp,
    },
    "positions": {
        "day": {"reading": "k has been 0.5 mu or less; it never reaches mu because d never reaches 1; selection at "
                           "d = 0.08 is negligible",
                "k_half_mu_gives_d": g(d_khalf), "delta_p": dp,
                "note": "the Delta-p arithmetic holds; the fit itself cannot be checked (24 points not held)"},
        "critic": {"reading": "the line, extrapolated, gives k = 0.102 mu at d = 1 and needs d = -1.013 for k = mu",
                   "k_at_d1": g(k_d1), "d_at_k_mu": g(d_k1), "d_at_k0": 1.229,
                   "note": "the slope is negative, so on the fit k approaches mu as d falls below 0, not as d rises "
                           "to 1; 'd never reaches 1' does not bear on k reaching mu"},
    },
    "notes": "Every consequence in the statement reproduces from the printed line: k = 0 -> d = 1.229, d = 1 -> k = "
             "0.102 mu, k = mu -> d = -1.013, k = 0.5 mu -> d = 0.108; r = -0.991 and R^2 = 0.981 agree within "
             "rounding; Delta-p = 7.92e-6. The data and fit are secondhand and not held, so the record checks "
             "implications only. Whether d = 1 is the discrete-generation case is C2a (M-107).",
})
