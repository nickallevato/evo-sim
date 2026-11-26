#!/usr/bin/env python3
"""M-605 record (derivation): fixation probability u against substitution rate k = 2N x flux x u.

Object: docs/research/math/objects.yaml M-605 (inference, derivation). Day: 1/(2N) "contains no time variable. It says
nothing about when" (F q3) and "The reviewer has confused fixation probability with fixation rate" (F4a q1, BO-03).
Bowers, secondhand: u is "roughly 2s ... not 1/N" (BO-01). The record states the standard identities claim file F4a
gives: k = (new mutations per generation) x u, so k_neutral = 2N mu x 1/(2N) = mu and k_ben = 2N U_b x 2s = 4N s U_b,
checked symbolically (exact rational arithmetic) and at two test points; Kimura's u = (1 - e^-2s)/(1 - e^-4Ns) at
the RESULTS B0.3 points (0.020171, 0.019801) and its limits 2s (4Ns >> 1) and 1/(2N) (s -> 0); and that u is a
per-mutation probability with no time unit: the same u gives different k at different flux, and the same k
(= mu) comes with mean fixation times 4N that differ 100-fold. Whether Day's reply answers Bowers depends on the
original review, which is not held (Day's repost is the only source).

Run: research/.venv/bin/python -I docs/research/math/records/M-605.py [--write]
Without --write it checks that M-605.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
F = "docs/research/claims/F-kimura-fixation-time-limits-fixations.md"
F4A = "docs/research/claims/F4a-day-reply-fixation-probability-vs-rate.md"
QC = "docs/research/sources/quotes-critics.md"
RES = "research/checks/RESULTS.md"


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
NOTIME = held(F, "It contains no time variable. It says nothing about when.")                 # F q3 (on 1/2N)
REPLY = "The reviewer has confused fixation probability with fixation rate. These are two different things."
held(F4A, REPLY); held(QC, REPLY)                                                              # F4a q1, BO-03
BOW = held(QC, "The correct approximation for a beneficial mutation is roughly 2s (in diploids under weak selection), not 1/N.")  # BO-01
SECOND = held(QC, "**BO-01** | para 3 | branch F | Bowers (as reposted by Day) `secondhand`")
IDENT = held(F4A, "Fixation rate k = (input flux) × (fixation probability). Day's reply gives no equation. Both quantities "
                  "are standard: k_neutral = 2Nμ/(2N) = μ; k_ben = 2N U_b · 2s.")              # F4a formal statement
NOTSEEN = held(F4A, "whether it answers Bowers depends on which quantity the original review addressed (not retrieved)")
B03 = [held(RES, "| B0.3 Kimura u, N=100, s=0.01 | 0.019995 | 0.020171 | −0.56 |"),
       held(RES, "| B0.3 Kimura u, N=500, s=0.01 | 0.019745 | 0.019801 | −0.18 |")]
B05 = held(RES, "B0.5 holds at both N values, consistent with k = U for any N.")


def k(n, flux, u):                                                # substitutions per generation
    return 2 * n * flux * u


def kimura_u(n, s):                                               # new mutant at p = 1/(2N), genic selection
    return math.expm1(-2 * s) / math.expm1(-4 * n * s)            # expm1: no cancellation as s -> 0


# ---- identities: symbolic (exact rationals over a grid) and at two test points --------------------
for n in (Fr(50), Fr(10_000), Fr(123_457)):
    for mu in (Fr(1, 10**8), Fr(3, 7 * 10**5)):
        assert k(n, mu, 1 / (2 * n)) == mu                        # k_neutral = mu, exactly, for any N
    for s, ub in ((Fr(1, 1000), Fr(1, 10**9)), (Fr(1, 100), Fr(7, 10**6))):
        assert k(n, ub, 2 * s) == 4 * n * s * ub                  # k_ben = 2N U_b x 2s = 4N s U_b, exactly
TP = [(1e4, 1e-8, 0.001, 1e-9), (500, 1.2e-8, 0.01, 5e-10)]       # (N, mu, s, U_b) test points
tp_vals = []
for n, mu, s, ub in TP:
    kn = near(k(n, mu, 1 / (2 * n)), mu, 1e-22)
    kb = near(k(n, ub, 2 * s), 4 * n * s * ub, 1e-22)
    tp_vals.append({"N": n, "mu": mu, "s": s, "U_b": ub, "k_neutral": kn, "k_ben": kb})
near(tp_vals[0]["k_ben"], 4e-8, 1e-20); near(tp_vals[1]["k_ben"], 1e-8, 1e-20)

# ---- Kimura u: the B0.3 targets and the two limits -----------------------------------------------
u100 = near(kimura_u(100, 0.01), 0.020171, 5e-7)
u500 = near(kimura_u(500, 0.01), 0.019801, 5e-7)
assert "0.020171" in B03[0] and "0.019801" in B03[1]
near(u500 / (2 * 0.01), 0.990, 0.0005)                            # 2s within 1% at 4Ns = 20
near(kimura_u(1e4, 0.001) / 0.002, 0.999, 0.0005)                 # Day's N, s: 4Ns = 40, u ~ 2s
for n in (50, 10_000):
    near(kimura_u(n, 1e-12) * 2 * n, 1.0, 1e-7)                   # s -> 0: u -> 1/(2N), error ~ 2Ns
near(2 * 0.001 * 2 * 1e4, 40, 1e-9)                               # 2s / (1/2N) = 4Ns: Bowers's "not 1/N" gap at Day's values

# ---- u carries no time: rate needs a flux; fixation time is a separate quantity ------------------
n, s = 1e4, 0.001
u = kimura_u(n, s)
ks = [k(n, f, u) for f in (1e-9, 1e-8)]
near(ks[1] / ks[0], 10, 1e-9)                                     # same u, 10x flux, 10x rate
mu = 1e-8
kn = [k(N, mu, 1 / (2 * N)) for N in (100, 10_000)]
near(kn[0], kn[1], 1e-22)                                         # same k = mu ...
tbar = [4 * N for N in (100, 10_000)]
near(tbar[1] / tbar[0], 100, 0)                                   # ... with mean fixation times 400 and 40,000
assert "k = U for any N" in B05

finish({
    "object": "M-605",
    "inputs": [
        {"name": "Day on 1/(2N)", "value": NOTIME, "cite": "F q3"},
        {"name": "Day's reply", "value": REPLY, "cite": "F4a q1, BO-03"},
        {"name": "Bowers (secondhand)", "value": BOW, "cite": "BO-01 (Day's repost; original not found)"},
        {"name": "identities", "value": "k = 2N x flux x u", "cite": "F4a formal statement"},
        {"name": "Kimura u targets", "value": [0.020171, 0.019801], "cite": "RESULTS B0.3 (N = 100, 500; s = 0.01)"},
    ],
    "values": {
        "k_neutral": "mu (exact, any N)", "k_ben": "4 N s U_b (exact)", "test_points": tp_vals,
        "kimura_u": {"N100_s0.01": round(u100, 6), "N500_s0.01": round(u500, 6), "N1e4_s0.001": round(u, 6)},
        "u_over_1_over_2N_at_day": 40.0,
        "same_k_mean_tfix": tbar,
    },
    "positions": {
        "day": {"reading": "fixation probability and fixation rate are different quantities; 1/(2N) says nothing about when",
                "holds": "u is a per-mutation probability with no time unit; k = flux x u per generation; t_fix is separate"},
        "critic": {"reading": "Bowers gives the textbook u ~ 2s for a beneficial mutation, not 1/N",
                   "holds": "u = 2s is correct (within 1% at 4Ns = 20; 0.1% at Day's 4Ns = 40), 40x 1/(2N) at Day's values"},
    },
    "notes": "Both statements are correct and they answer different questions: u (1/(2N) or about 2s) is a probability "
             "per new mutation; the rate is k = 2N x flux x u per generation; neither fixes when a fixation completes, "
             "which is the fixation time (4N neutral; M-601 beneficial). Day's distinction is accurate as a distinction. "
             "Whether it answers Bowers depends on which quantity the original review addressed; only Day's repost is "
             "held (BO-01 is secondhand), so the record cannot settle that.",
})
