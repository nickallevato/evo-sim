#!/usr/bin/env python3
"""M-209 record (model-choice): which population size enters the neutral substitution rate.

Object: docs/research/math/objects.yaml M-209 (model-choice, derivation). Day's original form
k = 2N mu x 1/(2Ne) = mu N/Ne (B3a) against the cancellation k = 2N mu x 1/(2N) = mu in the same N
(critics; Day's concession, B3g; keruru's retraction, B7c). The record computes k/mu under both forms
for the (N, Ne) pairs in the statement, Matev's sum over the 2N copies at a site (B3i), and the
Grok-exchange 800,000 (B3f), and sets them beside the fwdpy11 P_fix x 2N of R4 XT row B3. It does not
choose a form; the exact chains for the offspring-distribution question are M-216. Inputs carry their
quote id or claim file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-209.py [--write]
Without --write it checks that M-209.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
XT = "research/checks/results/R4-XT.md"


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


def k_day(n, ne):           # supply 2N mu (census), P_fix 1/(2Ne)
    return Fr(2 * n) * Fr(1, 2 * ne)


def k_cancel(n, ne):        # supply 2N mu, P_fix 1/(2N): Ne drops out
    return Fr(2 * n) * Fr(1, 2 * n)


# ---- inputs -------------------------------------------------------------------------------
B3A = held(CL + "B3a-fixation-probability-1-over-2ne.md", "k = 2Nμ × 1/(2N_{e}) = μ × (N/N_{e}) (1)")
Q39 = held(CL + "B3a-fixation-probability-1-over-2ne.md", "k = 2Nμ × 1/(2Nₑ) = μ(N/Nₑ)")
CONC = held(CL + "B3g-day-concession-no-ne-in-kimura-identity.md",
            "Supply is 2Nμ in the census N, the fixation probability of a new copy is 1/(2N) in the same N, the two correctly cancel")
GROK = held(CL + "B3f-800000-mu-grok-exchange.md", "This equals 800,000 μ, not μ.")
GROKIN = held(CL + "B3f-800000-mu-grok-exchange.md", "N = 8×10⁹, Nₑ = 10⁴ ⇒ 8×10⁵ μ")
MATEV = held(CL + "B3i-matev-sum-over-alleles-exceeds-one.md",
             "the probability that some allele from this set will eventually fix would be 2N/(2Nₑ) = N/Nₑ, which is "
             "greater than one and therefore not even a valid probability when N > Nₑ.")
KERURU = held(CL + "B7c-keruru-retraction-census-n-cancels.md", "k = 2Nμ × 1/(2Ne) = (N/Ne)μ")
KRET = held(CL + "B7c-keruru-retraction-census-n-cancels.md", "The claim about the substitution rate is withdrawn.")
MARU = held(CL + "B7-neutral-fixation-probability-is-1-over-2n.md",
            "Maruyama’s invariance principle (1970, 1974) holds that under conservative migration the neutral "
            "substitution rate is exactly μ and the neutral fixation probability exactly 1/(2N)")
XTB3 = held(XT, "P_fix*2N = 0.985, 0.974, 0.981, 0.995 (Day's N/Ne would give 1.00, 1.52, 2.91, 7.40)")

# ---- the two forms --------------------------------------------------------------------------
pairs = [(8_000_000_000, 10_000), (1_000_000, 10_000), (100_000, 3_300), (100_000, 57_143), (10_000, 10_000)]
day = {f"{n:.0e}/{ne:.0e}": k_day(n, ne) for n, ne in pairs}
cancel = {f"{n:.0e}/{ne:.0e}": k_cancel(n, ne) for n, ne in pairs}
assert k_day(8_000_000_000, 10_000) == 800_000          # B3f "800,000 mu"
assert all(v == 1 for v in cancel.values())             # cancellation: k = mu for every pair
assert k_day(10_000, 10_000) == 1                       # the forms agree only when N = Ne
near(float(k_day(100_000, 3_300)), 30.30, 0.01)         # Z18525547 human census 1e5, Ne 3,300 (M-217)
near(float(k_day(100_000, 57_143)), 1.75, 0.001)        # HL's Wright Ne at Vk = 5 (M-203)

# ---- Matev: the 2N copies at a site are exhaustive and exclusive ---------------------------------
for n, ne in pairs:
    s_day = 2 * n * Fr(1, 2 * ne)                        # sum of per-copy P_fix under 1/(2Ne)
    s_std = 2 * n * Fr(1, 2 * n)
    assert s_std == 1                                    # exactly one copy's descendants fix
    assert s_day == Fr(n, ne) and (s_day > 1) == (n > ne)
assert 2 * 1_000_000 * Fr(1, 2 * 10_000) == 100         # claim file example: sum = 100

# ---- fwdpy11 (R4 XT row B3): P_fix x 2N against Day's N/Ne --------------------------------------
xt_obs = [0.985, 0.974, 0.981, 0.995]
xt_day = [1.00, 1.52, 2.91, 7.40]
dev_std = max(abs(o - 1) for o in xt_obs)
dev_day = [abs(o - d) / d for o, d in zip(xt_obs, xt_day)]
near(dev_std, 0.026, 1e-9)                               # within 2.6% of 1/(2N) in every cell
assert min(dev_day[1:]) > 0.35                           # 36-87% below Day's form where N != Ne
near(dev_day[3], 0.8655, 0.0001)

finish({
    "object": "M-209",
    "inputs": [
        {"name": "Day original", "value": "k = mu N/Ne", "cite": "B3a q1 (Z18525547 eq. 1), Q39 (blog 2026-02-04)"},
        {"name": "Day concession", "value": "supply 2N mu and P_fix 1/(2N) in the same N cancel", "cite": "B3g q1 (blog 2026-08-27)"},
        {"name": "Grok exchange", "value": {"N": 8e9, "Ne": 1e4, "k_over_mu": 800_000}, "cite": "B3f q1; claim file B3f"},
        {"name": "Matev sum", "value": "2N x 1/(2Ne) = N/Ne", "cite": "B3i q1 (RF-2)"},
        {"name": "keruru pre-retraction and retraction", "cite": "B7c q4, q3"},
        {"name": "Maruyama invariance in Day's Hard Limits", "cite": "B7 q1"},
        {"name": "fwdpy11 P_fix x 2N at Ne/N 1, .66, .35, .14", "value": xt_obs, "cite": "R4-XT.md row B3"},
    ],
    "values": {
        "k_over_mu_day_form": {k: g(float(v)) for k, v in day.items()},
        "k_over_mu_cancelled": {k: int(v) for k, v in cancel.items()},
        "matev_sum_1e6_1e4": 100,
        "xt_max_dev_from_1": dev_std, "xt_dev_from_day_form": [g(x) for x in dev_day],
    },
    "positions": {
        "day": {"original": "k/mu = N/Ne", "values": {k: g(float(v)) for k, v in day.items()},
                "later": "conceded 2026-08-27: no Ne on either side; 3rd edition needed (B3g q2)"},
        "critic": {"reading": "supply and fixation share the same N; k/mu = 1 for every pair",
                   "matev": "sum of per-copy probabilities is N/Ne > 1 under the 1/(2Ne) form, so that form is not a probability"},
    },
    "notes": "Both forms are algebraically correct for their premises; they agree only at N = Ne. Under 1/(2Ne) the "
             "per-site sum over 2N copies is N/Ne (100 at N = 1e6, Ne = 1e4), which exceeds 1. fwdpy11 P_fix x 2N "
             "stays within 2.6% of 1 at Ne/N down to 0.14, 36-87% below Day's N/Ne. Whether offspring-number "
             "covariance changes this is M-216.",
})
