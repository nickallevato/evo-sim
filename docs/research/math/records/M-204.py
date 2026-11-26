#!/usr/bin/env python3
"""M-204 record: short-time completion fraction F(T) ~ exp(-pi^2 Ne / T) against the naive fill T/(4Ne).

Object: docs/research/math/objects.yaml M-204 (formula, derivation). F(T) = P(tau <= T | fixation)
(Q147). Its diffusion series is F = sum_{i>=0} (-1)^i (2i+1) exp(-i(i+1) x), x = T/(4Ne). By the
Jacobi theta transformation of theta_1'(0) the same function is, exactly,
F = e^(x/4) (pi/x)^(3/2) sum_{n>=0} (-1)^n (2n+1) exp(-(2n+1)^2 pi^2 / (4x)),
so the leading term is exp(-pi^2 Ne/T) (Day's exponent, Q31) times a prefactor (4 pi Ne/T)^(3/2) e^(T/16Ne)
that Day's form omits. The record checks both forms against each other, Day's simulation count (six
against ~750), the human exponent 10^(-77.15 million) (B2c), the 10^14 rescue, and the window readings
in the B2c claim file. Inputs carry their quote id or claim file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-204.py [--write]
Without --write it checks that M-204.json is current; --write saves it.
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


def f_series(x, terms=400):
    """P(tau <= T | fixation), x = T/(4Ne); converges fast for x >~ 0.05."""
    return sum((-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x) for i in range(terms))


def log10_f_theta(x, terms=6):
    """log10 of the same function via the theta transformation; exact, fast for small x."""
    s = sum((-1) ** n * (2 * n + 1) * math.exp(-((2 * n + 1) ** 2 - 1) * math.pi ** 2 / (4 * x)) for n in range(terms))
    return (x / 4 + 1.5 * math.log(math.pi / x) - math.pi ** 2 / (4 * x) + math.log(s)) / math.log(10)


def log10_day(ne_over_t):
    return -math.pi ** 2 * ne_over_t / math.log(10)


# ---- inputs -------------------------------------------------------------------------------
Q31 = held(CL + "B2a-exp-pi2-ne-over-g.md", "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ The naive fill fraction T/4Nₑ is not just "
                                           "unproven; it is an overstatement, and a vast one.")
Q147 = held(CL + "B2a-exp-pi2-ne-over-g.md", "k(T) = μ · F(T),      F(T) = P(τ ≤ T | fixation)")
SIM = held(CL + "B2a-exp-pi2-ne-over-g.md", "The linear guess says a quarter of them should fix within a quarter of the "
                                           "mean time, some seven hundred fifty fixations; six do.")
SIMIN = held(CL + "B2a-exp-pi2-ne-over-g.md", "Day's simulation: 600,000 runs, 200 genes, ≈3,000 fixed, 6 within a quarter of the mean time")
CHAIN = held(CL + "B2a-exp-pi2-ne-over-g.md", "| 1 | 2.8e−3 | 5.2e−5 | 54× |")
B2C = held(CL + "B2c-one-in-ten-to-78-millionth.md",
           "For modern humans, Nₑ across the four hundred generations of the current-census era gives Nₑ/T ≈ 1.8 × 10⁷, "
           "so the probability that a neutral mutation arising now fixes within that era is of order exp(−π² · 1.8 × 10⁷) "
           "— about one in ten to the seventy-eight-millionth.")
B2C2 = held(CL + "B2c-one-in-ten-to-78-millionth.md",
            "Ten to the fourteenth against a probability of exp(−π²Nₑ/G) leaves the expected number of completed "
            "fixations at ten to the minus seventy-eight-million all the same.")
NE73 = held(CL + "B2c-one-in-ten-to-78-millionth.md", "Nₑ = 7.3e9 (HL Table 3, \"census scale\"), T = 400")
WIN = held(CL + "B2c-one-in-ten-to-78-millionth.md", "With the lineage window G = 260,000")

# ---- the two forms of F agree --------------------------------------------------------------
for x in (0.1, 0.25, 0.5, 1.0, 2.0):
    near(math.log10(f_series(x)), log10_f_theta(x), 1e-5)   # series loses digits to cancellation at small x
assert abs(f_series(1e-4 + 50)) - 1 < 1e-12             # F -> 1 for long windows

# ---- claim-file comparison at G/N = 4, 1, 0.25 (x = G/(4N)) -----------------------------------
diff = {r: 10 ** log10_f_theta(r / 4) for r in (4, 1, 0.25)}
dayf = {r: math.exp(-math.pi ** 2 / r) for r in (4, 1, 0.25)}
near(diff[4], 0.6064, 0.0001)                           # exact chain N=200: 0.61
near(diff[1], 2.452e-3, 0.001e-3)                       # exact chain N=200: 2.8e-3
near(diff[0.25], 2.59e-15, 0.01e-15)                    # exact chain N=200: 1.2e-14 (discrete tail)
near(dayf[1], 5.17e-5, 0.01e-5)
near(dayf[0.25], 7.16e-18, 0.01e-18)
pref1 = (4 * math.pi) ** 1.5 * math.exp(1 / 16)
near(pref1, 47.42, 0.01)                                # omitted prefactor at T = Ne (claim file fit: ~50)
near(diff[1] / dayf[1], pref1, 1e-6)

# ---- Day's simulation: ~3,000 fixed, a quarter of the mean time (x = 1/4) ---------------------
n_fixed = 3000
linear = n_fixed * 0.25
assert linear == 750                                    # "some seven hundred fifty"
exp_diff = n_fixed * diff[1]
near(exp_diff, 7.36, 0.01)                              # diffusion predicts ~7; Day observed 6
exp_day = n_fixed * dayf[1]
near(exp_day, 0.155, 0.001)                             # Day's leading-order form predicts 0.16
near(linear / 6, 125, 0)                                # linear overstates by 125x on Day's count

# ---- humans: Ne/T = 1.8e7 (stated) and 1.825e7 (Ne 7.3e9, T 400) -------------------------------
l_day = log10_day(1.8e7)
near(l_day, -7.7154e7, 0.0001e7)                        # 10^(-77.15 million); Day says "78-millionth"
near(log10_day(7.3e9 / 400), -7.8225e7, 0.0001e7)       # with Ne = 7.3e9 the exponent is -78.2 million
l_exact = log10_f_theta(400 / (4 * 7.3e9))
near(l_exact - log10_day(7.3e9 / 400), 12.54, 0.01)     # prefactor adds 12.5 decades of 7.8e7: no change
rescue = 14 + log10_day(1.8e7)
near(rescue, -7.7154e7, 0.0001e7)                       # 10^14 loci leave 10^(-77.15 million)
assert 30 * 400 == 12_000                               # destined-to-fix input (B2c audit)

# ---- critic: the lineage window, not the 400-generation era (B2c audit) -----------------------
G = 260_000
lin = {"Ne_7.3e9": log10_day(7.3e9 / G), "Ne_4.69e9": log10_day(4.69e9 / G)}
near(lin["Ne_7.3e9"], -1.2035e5, 0.0001e5)              # ~1.2e5 decades
near(lin["Ne_4.69e9"], -7.732e4, 0.001e4)               # ~7.7e4 decades
yoo = {ne: math.exp(-math.pi ** 2 * ne / G) for ne in (1.98e5, 1.32e5, 1e4)}
near(yoo[1.98e5], 5.44e-4, 0.01e-4)
near(yoo[1.32e5], 6.67e-3, 0.01e-3)
near(yoo[1e4], 0.684, 0.001)
yoo_exact = {ne: f_series(G / (4 * ne)) for ne in (1.98e5, 1.32e5, 1e4)}
near(yoo_exact[1.98e5], 0.0175, 0.0001)                 # exact F with Yoo HCB Ne over the lineage
near(yoo_exact[1.32e5], 0.1215, 0.0001)
near(yoo_exact[1e4], 1.0, 1e-5)                         # Ne = 1e4: the pipe completes

finish({
    "object": "M-204",
    "inputs": [
        {"name": "short-time law", "value": "F(T) ~ exp(-pi^2 Ne/T), T << 4Ne", "cite": "Q31 (B2a q1)"},
        {"name": "definition", "value": "F(T) = P(tau <= T | fixation), k(T) = mu F(T)", "cite": "Q147 (B2a q2)"},
        {"name": "Day simulation", "value": "~3,000 fixed, 750 linear, 6 observed", "cite": "B2a q3; claim file B2a"},
        {"name": "human Ne/T", "value": [1.8e7, "Ne 7.3e9, T 400"], "cite": "B2c q1; claim file B2c (HL Table 3)"},
        {"name": "rescue count", "value": 1e14, "cite": "B2c q2"},
        {"name": "lineage window and Ne readings", "value": {"G": G, "Ne": [7.3e9, 4.69e9, 1.98e5, 1.32e5, 1e4]}, "cite": "claim file B2c audit; parameters population.Ne_ancestral_hc.yoo_2025_HCB/HCG, Ne_modern_human"},
    ],
    "values": {
        "F_diffusion_by_G_over_N": {str(k): g(v) for k, v in diff.items()},
        "F_day_by_G_over_N": {str(k): g(v) for k, v in dayf.items()},
        "prefactor_at_T_eq_Ne": g(pref1),
        "sim_expected": {"linear": linear, "diffusion": g(exp_diff), "day_formula": g(exp_day), "observed": 6},
        "human_log10F": {"day_1.8e7": g(l_day), "day_Ne7.3e9": g(log10_day(7.3e9 / 400)), "exact_Ne7.3e9": g(l_exact)},
        "rescue_log10": g(rescue),
        "lineage_window_log10F": {k: g(v) for k, v in lin.items()},
        "lineage_window_F_day": {str(k): g(v) for k, v in yoo.items()},
        "lineage_window_F_exact": {str(k): g(v) for k, v in yoo_exact.items()},
    },
    "positions": {
        "day": {"linear_overstates": True, "linear_over_observed": 125, "log10F_humans": g(l_day),
                "rescue_fails": rescue < -1e7,
                "note": "the exponent is exact; the omitted prefactor (4 pi Ne/T)^1.5 is 47 at T = Ne and 10^12.5 at Ne/T = 1.8e7, which moves nothing at 10^-7.7e7"},
        "critic": {"reading": "the current-census era does not bound lineage fixations",
                   "lineage_F_exact_YooHCB": g(yoo_exact[1.98e5]), "lineage_F_exact_Ne1e4": g(yoo_exact[1e4]),
                   "note": "the lineage-scale fill and its demography are M-207 and M-202"},
    },
    "notes": "Exponent pi^2 Ne/T reproduces; Day's 'seventy-eight-millionth' is 77.15 million decades at Ne/T = 1.8e7 "
             "(78.2 million at Ne = 7.3e9, T = 400), a 1% rounding. The exact diffusion F carries a prefactor that Day's "
             "form omits: 47x at T = Ne, which matches Day's own simulation (7.4 expected, 6 observed; his formula "
             "gives 0.16). Which window and Ne apply is the dispute; under the lineage window F ranges 0.017 to 1.",
})
