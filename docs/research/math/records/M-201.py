#!/usr/bin/env python3
"""M-201 record: finite-window neutral count from an empty start, E[F(T)] = mu L int_0^T F_X(u) du.

Object: docs/research/math/objects.yaml M-201 (formula, derivation). F_X is the CDF of the neutral
fixation time conditional on fixation. Its diffusion form for a new mutant is
F_X(t) = 1 + sum_{i>=1} (-1)^i (2i+1) exp(-i(i+1) t / (4 Ne)), mean 4 Ne (Kimura & Ohta 1969 Eq. 15),
so int_0^T F_X = T - 4 Ne (1 - tail), tail ~ 1.5 exp(-T/(2 Ne)). The record checks Day's naive count
(Q36), the leading-order T - 4Ne rows of the IR table (claim file B1a), the exact integral at the row
T = 4 Ne that the table prints as 0, and the equilibrium-start count (mu L T) under the critic reading.
Inputs carry their quote id or claim file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-201.py [--write]
Without --write it checks that M-201.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
QD = "docs/research/sources/quotes-day.md"
CL = "docs/research/claims/"


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


def int_tail(T, ne, terms=200):
    """int_0^T (1 - F_X(u)) du for the diffusion conditional fixation-time law (exact series).
    Uses sum_{i>=1} (-1)^(i+1) (2i+1)/(i(i+1)) = 1 (telescoping 1/i + 1/(i+1)), so only the fast terms remain."""
    four = 4 * ne
    return four * (1 - sum((-1) ** (i + 1) * (2 * i + 1) / (i * (i + 1)) * math.exp(-i * (i + 1) * T / four)
                           for i in range(1, terms)))


# ---- inputs -------------------------------------------------------------------------------
Q34 = held(QD, "using the exact transient formula E[F(T)] = μL ∫₀ᵀ F_X(u) du rather than the naive product μLT, "
               "the leading-order correction subtracts the mean fixation time from the available window.")
Q35 = held(CL + "B1a-eF-formula-and-numbers.md", "∫₀ᵀ F_X(u) du = T − ∫₀ᵀ (1 − F_X(u)) du ≈ T − 4Nₑ")
Q36 = held(CL + "B1a-eF-formula-and-numbers.md",
           "Using 252,000 generations since the split (approximately 6.3 million years at 25 years per generation) "
           "and μL ≈ 30 neutral mutations per generation: Steady-state calculation (k = μ applied naively): "
           "30 × 252,000 = 7,560,000 fixations")
ROWS = held(CL + "B1a-eF-formula-and-numbers.md",
            "| Nₑ = 10⁴: 30 × (252,000 − 40,000) | 6,360,000 (loss 1.2M, 15.9%) |")
ROW63 = held(CL + "B1a-eF-formula-and-numbers.md", "| Nₑ = 63,000 (4Nₑ = T) | 0 (100%) |")
CRIT = held(CL + "B1a-eF-formula-and-numbers.md", "From an equilibrium start the count is μL·T; the formula applies only to the empty case.")

muL, T = 30, 252_000
assert 6_300_000 / 25 == T                              # Q36 "6.3 million years at 25 years"
naive = muL * T
assert naive == 7_560_000                               # Q36

# ---- the mean of F_X is 4 Ne (series check) -----------------------------------------------
mean_series = sum((-1) ** (i + 1) * (1 / i + 1 / (i + 1)) for i in range(1, 200_001))
near(mean_series, 1.0, 1e-5)                            # int_0^inf (1 - F_X) = 4 Ne x 1 (telescopes to 1)
near(int_tail(1e9, 10_000), 40_000, 1e-6)               # the mean is 4 Ne

# ---- Day: leading order mu L (T - 4 Ne), IR table rows ------------------------------------
lead = {}
for ne, printed, loss_pct in ((10_000, 6_360_000, 15.87), (50_000, 1_560_000, 79.37), (63_000, 0, 100.0)):
    c = muL * (T - 4 * ne)
    assert c == printed, (ne, c)
    near(100 * (naive - c) / naive, loss_pct, 0.005)
    lead[ne] = c
assert naive - lead[10_000] == 1_200_000                # "loss 1.2M"

# ---- exact integral (diffusion series) against the leading order --------------------------
exact = {ne: muL * (T - int_tail(T, ne)) for ne in (10_000, 50_000, 63_000)}
near(exact[10_000], 6_360_006, 1)                       # tail 1.5 e^-12.6 adds 6: invisible at Ne = 1e4
near(exact[50_000], 1_560_000 + muL * 4 * 50_000 * 1.5 * math.exp(-T / 100_000), 6_000)
near(exact[50_000], 2_281_533, 1)                       # T/4Ne = 1.26: 46% above the leading order
near(100 * (naive - exact[50_000]) / naive, 69.82, 0.01)  # exact loss 69.8%, not 79.4%
near(exact[63_000], 1_519_113, 1)                       # T = 4 Ne: exact count is positive, not 0
assert exact[63_000] > 0 == lead[63_000]                # the table's 0 is outside T >> 4Ne (B1a)
near(exact[63_000] / naive, 0.2009, 0.0002)

# ---- critic: equilibrium (full) start delivers mu L per generation ------------------------
full = muL * T                                          # stationary pipe: flux out = flux in = mu L
assert full == naive

finish({
    "object": "M-201",
    "inputs": [
        {"name": "formula", "value": "E[F(T)] = mu L int_0^T F_X(u) du", "cite": "Q34"},
        {"name": "asymptote", "value": "int F_X ~ T - 4 Ne", "cite": "Q35 (B1a q1)"},
        {"name": "T, mu L, naive count", "value": [T, muL, naive], "cite": "Q36 (B1a q2); parameters generations_available.day_2026"},
        {"name": "IR table rows", "value": {"1e4": 6_360_000, "5e4": 1_560_000, "6.3e4": 0}, "cite": "claim file B1a arithmetic audit"},
        {"name": "F_X diffusion series, mean 4 Ne", "value": "1 + sum (-1)^i (2i+1) exp(-i(i+1) t/4Ne)", "cite": "standard (Kimura & Ohta 1969 Eq. 15 for the mean; B7b q1)"},
    ],
    "values": {
        "naive_muLT": naive,
        "leading_order": {str(k): v for k, v in lead.items()},
        "exact_series": {str(k): g(v) for k, v in exact.items()},
        "loss_pct_leading": {"1e4": 15.87, "5e4": 79.37, "6.3e4": 100.0},
        "exact_over_naive_at_T_eq_4Ne": g(exact[63_000] / naive),
    },
    "positions": {
        "day": {"reading": "empty start: count = mu L int F_X ~ mu L (T - 4Ne)",
                "count_Ne_1e4": lead[10_000], "count_Ne_5e4": lead[50_000], "count_T_eq_4Ne_printed": 0,
                "exact_T_eq_4Ne": g(exact[63_000])},
        "critic": {"reading": "exact for the empty start (a point for Day); from a full start the count is mu L T",
                   "count_full_start": full,
                   "note": "whether the start is empty is M-202 (data-check); pairwise divergence is M-219"},
    },
    "notes": "The algebra is exact for an empty start and the leading-order rows reproduce. Rows outside T >> 4Ne "
             "understate the exact count: Ne = 5e4 gives 2.28M (loss 69.8%, table 79.4%), and the printed 0 at "
             "T = 4Ne is 1.52M exact (20% of mu L T). The start state, not this formula, decides between the two "
             "counts (M-202).",
})
