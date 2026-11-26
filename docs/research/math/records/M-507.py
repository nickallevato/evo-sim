#!/usr/bin/env python3
"""M-507 record (derivation): relictation, t/4Ne under the Cannings jackpot chain against the Wright-Fisher chain.

Object: docs/research/math/objects.yaml M-507 (formula, derivation). Day & Athos's jackpot chain (Z23188201 s2, as
claim file E4 states it): haploid 2N copies; in a jackpot generation (probability pj) one uniformly drawn parent copy's
offspring replace m = min(round(f 2N), 2N - 1) of the other copies, drawn without replacement; otherwise nothing
changes. Exact (2N+1)-state chains solved by Gaussian elimination in floats: P_fix from the linear system, mean time to
fixation conditional on fixation from the Doob h-transform t_i = [(I - Q)^-1 u]_i / u_i, Ne as the variance effective
size x(1 - x) / (2 Var(dx)). The record reproduces the paper's table (claim file E4) at 2N = 20 / 30 / 50, its
Wright-Fisher baseline, the three figures the object states (14.9%, 20.4%, 28.8%) and the size of the gap where the
statement's "peak" is not the column maximum. Same chain and rounding as research/checks/e4_relictation_chain.py
(R4 E); this record is stdlib and covers the table sizes plus two small cross-checks.

Run: research/.venv/bin/python -I docs/research/math/records/M-507.py [--write]
Without --write it checks that M-507.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
E4 = "docs/research/claims/E4-relictation.md"
F6 = "docs/research/claims/F6-relictation-ten-percent-replacement.md"
QD = "docs/research/sources/quotes-day.md"
R4E = "research/checks/results/R4-E.md"


def held(rel, quote):
    """The quote, checked verbatim (whitespace-normalised) against a held file."""
    norm = lambda s: " ".join(s.split())
    assert norm(quote) in norm((ROOT / rel).read_text(encoding="utf-8")), (rel, quote[:60])
    return quote


def near(x, target, tol):
    assert abs(x - target) <= tol, (x, target, tol)
    return x


def g(x, d=4):
    return round(x, d)


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
MODEL = held(E4, "Cannings jackpot model: each generation, with probability p_jackpot, one random individual survives and "
                 "its offspring replace round(f x 2N) other gene copies; remaining copies reproduce deterministically.")
TABLE_TXT = held(E4, "Table (paper; ratio t̄/4Ne at 2N = 20 / 30 / 50): f = 5%: 0.950 / 0.983 / 0.993; 10%: 0.968 / 0.999 / "
                     "1.033; 20%: 1.003 / 1.048 / 1.100; 30%: 1.035 / 1.091 / 1.160; 50%: 1.071 / 1.146 / 1.239; 60%: "
                     "1.068 / 1.148 / 1.249; 80%: 0.976 / 1.060 / 1.173; 90%: 0.950 / 0.966 / 1.023; 98%: 0.500 / 0.500 / "
                     "0.500. Plain Wright-Fisher baseline: 0.932 / 0.952 / 0.970.")
DERIVED = held(E4, "derived: peak ratio over WF baseline = 1.071/0.932 = 1.149, 1.146/0.952 = 1.204, 1.249/0.970 = 1.288 "
                   "(paper: \"~15%, ~21%, and ~29%\"; holds).")
Q72 = held(QD, "compression fails and a single family can replace more than ~10% of the population, the formula t̄ = 4Nₑ "
               "breaks in quantifiable ways. Below 10% replacement, the formula holds")
held(F6, "Below 10% replacement, the formula holds")
PFIX = held(E4, "The fixation probability p = 1/(2N) is protected by the martingale property and holds exactly regardless "
                "of offspring distribution.")
R4_LARGE = held(R4E, "Day's large-N numbers reproduce: 1.363 and 1.737 at f = 0.5 (2N = 100, 800)")
R4_FIXED = held(R4E, "For a **fixed family** (m = 6) the excess shrinks: 1.0445 (2N = 60)")
R4_FSTAR = held(R4E, "Exact f* (post hoc bisection) for +5% over the WF chain: 15% (2N = 20), 13% (30), 8% (50)")

SIZES = (20, 30, 50)
FS = (0.05, 0.10, 0.20, 0.30, 0.50, 0.60, 0.80, 0.90, 0.98)
PAPER = {0.05: (0.950, 0.983, 0.993), 0.10: (0.968, 0.999, 1.033), 0.20: (1.003, 1.048, 1.100),
         0.30: (1.035, 1.091, 1.160), 0.50: (1.071, 1.146, 1.239), 0.60: (1.068, 1.148, 1.249),
         0.80: (0.976, 1.060, 1.173), 0.90: (0.950, 0.966, 1.023), 0.98: (0.500, 0.500, 0.500)}
PAPER_WF = (0.932, 0.952, 0.970)
PJ = 0.1                                                  # Day's jackpot probability (R4 E); the ratio does not use it


# ---- chains -----------------------------------------------------------------------------------------
def hg(k, pop, succ, draws):
    if k < 0 or k > succ or draws - k > pop - succ:
        return 0.0
    return math.comb(succ, k) * math.comb(pop - succ, draws - k) / math.comb(pop, draws)


def jackpot(n2, m, pj=PJ):
    P = [[0.0] * (n2 + 1) for _ in range(n2 + 1)]
    for i in range(n2 + 1):
        P[i][i] += 1 - pj
        if i in (0, n2):
            P[i][i] += pj
            continue
        for x in range(m + 1):
            if i + x <= n2:
                P[i][i + x] += pj * (i / n2) * hg(x, n2 - 1, n2 - i, m)    # parent copy A: x non-A copies replaced
            if i - x >= 0:
                P[i][i - x] += pj * ((n2 - i) / n2) * hg(x, n2 - 1, i, m)  # parent copy a: x A copies replaced
    return P


def wright_fisher(n2):
    return [[math.comb(n2, j) * (i / n2) ** j * (1 - i / n2) ** (n2 - j) for j in range(n2 + 1)] for i in range(n2 + 1)]


def solve(A, B):
    """Gaussian elimination with partial pivoting; B is a list of right-hand sides."""
    n = len(A)
    A = [r[:] for r in A]
    B = [b[:] for b in B]
    for k in range(n):
        p = max(range(k, n), key=lambda q: abs(A[q][k]))
        A[k], A[p] = A[p], A[k]
        for b in B:
            b[k], b[p] = b[p], b[k]
        for q in range(k + 1, n):
            fq = A[q][k] / A[k][k]
            if fq:
                Ak, Aq = A[k], A[q]
                for j in range(k, n):
                    Aq[j] -= fq * Ak[j]
                for b in B:
                    b[q] -= fq * b[k]
    out = []
    for b in B:
        x = [0.0] * n
        for k in reversed(range(n)):
            x[k] = (b[k] - sum(A[k][j] * x[j] for j in range(k + 1, n))) / A[k][k]
        out.append(x)
    return out


def analyse(P):
    """P_fix error over every start, conditional mean fixation time from one copy, Ne_var (min, max over i)."""
    n2 = len(P) - 1
    IQ = [[(1.0 if i == j else 0.0) - P[i][j] for j in range(1, n2)] for i in range(1, n2)]
    (u,) = solve(IQ, [[P[i][n2] for i in range(1, n2)]])
    pfix_err = max(abs(u[i - 1] - i / n2) for i in range(1, n2))
    (gt,) = solve(IQ, [u])
    t1 = gt[0] / u[0]
    ne = []
    for i in range(1, n2):
        x = i / n2
        var = sum(P[i][j] * ((j - i) / n2) ** 2 for j in range(n2 + 1))
        ne.append(x * (1 - x) / (2 * var))
    return pfix_err, t1, min(ne), max(ne)


def ratio(P):
    err, t1, ne_lo, ne_hi = analyse(P)
    assert err <= 1e-12, err                              # P_fix(i) = i/2N, every start (martingale)
    assert (ne_hi - ne_lo) / ne_lo <= 1e-10               # Ne_var constant in i
    return t1 / (4 * ne_lo)


def m_of(f, n2):
    return min(round(f * n2), n2 - 1)                     # Python round (R4 E: half-up misses one cell)


# ---- baselines, table, P_fix ----------------------------------------------------------------------
wf = {n2: ratio(wright_fisher(n2)) for n2 in SIZES}
for n2, paper in zip(SIZES, PAPER_WF):
    near(wf[n2], paper, 0.0005)
    assert math.isclose(analyse(wright_fisher(n2))[3], n2 / 2, rel_tol=1e-10)   # WF Ne = N

table = {}
for f in FS:
    for k, n2 in enumerate(SIZES):
        r = ratio(jackpot(n2, m_of(f, n2)))
        near(r, PAPER[f][k], 0.0005)                      # every one of the 27 cells
        table[(f, n2)] = r
for n2 in SIZES:
    near(table[(0.98, n2)], 0.5, 1e-9)                    # complete replacement: one event takes half of 4Ne
    m = m_of(0.5, n2)                                     # Ne_var = 1/(2c), c = pj m(m+1)/(2N(2N-1))
    c = PJ * m * (m + 1) / (n2 * (n2 - 1))
    near(analyse(jackpot(n2, m))[2], 1 / (2 * c), 1e-9 / c)
near(ratio(jackpot(30, 15, pj=0.5)), table[(0.5, 30)], 1e-10)   # ratio independent of pj

# ---- the statement's three figures and its "peak ratios" ---------------------------------------------
stmt_peak = {20: (0.50, 1.071), 30: (0.50, 1.146), 50: (0.60, 1.249)}     # object M-507: "1.071, 1.146, 1.249"
stmt_pct = {20: 14.9, 30: 20.4, 50: 28.8}
paper_pct = {20: 15, 30: 21, 50: 29}                                        # "~15%, ~21%, and ~29%"
excess_printed, col_max, excess_colmax, excess_exact, best_m = {}, {}, {}, {}, {}
for k, n2 in enumerate(SIZES):
    f, v = stmt_peak[n2]
    assert PAPER[f][k] == v
    e = 100 * (v / PAPER_WF[k] - 1)
    near(e, stmt_pct[n2], 0.05)                           # 14.9, 20.4, 28.8 from the printed cells
    excess_printed[n2] = g(e, 2)
    fmax = max(FS, key=lambda q: PAPER[q][k])
    col_max[n2] = (fmax, PAPER[fmax][k])
    excess_colmax[n2] = g(100 * (PAPER[fmax][k] / PAPER_WF[k] - 1), 2)
    near(excess_colmax[n2], paper_pct[n2], 0.65)          # the paper's rounded figures hold
    mbest = max(range(1, n2), key=lambda mm: ratio(jackpot(n2, mm)))           # peak over every integer m
    best_m[n2] = {"m": mbest, "f": g(mbest / n2, 3), "ratio": g(ratio(jackpot(n2, mbest)))}
    excess_exact[n2] = g(100 * (best_m[n2]["ratio"] / wf[n2] - 1), 2)
# 2N = 20 and 50: the statement's cell is the column maximum. 2N = 30: the column maximum is 1.148 at f = 60%, not
# 1.146 at f = 50%, so 20.4% understates the printed peak excess (20.59%) by 0.2 points.
assert col_max == {20: (0.50, 1.071), 30: (0.60, 1.148), 50: (0.60, 1.249)}
near(excess_colmax[30], 20.59, 0.01)
near(excess_colmax[30] - excess_printed[30], 0.21, 0.005)
near(table[(0.6, 30)] - table[(0.5, 30)], 0.002, 0.0006)  # the exact chain agrees: 60% sits above 50% at 2N = 30
assert best_m == {20: {"m": 11, "f": 0.55, "ratio": 1.0716}, 30: {"m": 17, "f": 0.567, "ratio": 1.1499},
                  50: {"m": 30, "f": 0.6, "ratio": 1.249}}
assert excess_exact == {20: 15.0, 30: 20.75, 50: 28.8}

# ---- "no deviation below about 10%": excess over the WF chain at f = 5% and 10%, and f* for +5% --------
low = {f: {n2: g(100 * (table[(f, n2)] / wf[n2] - 1), 1) for n2 in SIZES} for f in (0.05, 0.10)}
assert low == {0.05: {20: 2.0, 30: 3.2, 50: 2.4}, 0.10: {20: 3.9, 30: 4.9, 50: 6.6}}
fstar = {}
for n2 in SIZES:
    m = next(mm for mm in range(1, n2) if ratio(jackpot(n2, mm)) / wf[n2] - 1 >= 0.05)
    fstar[n2] = g(m / n2, 3)
assert fstar == {20: 0.15, 30: 0.133, 50: 0.08}            # R4 E: 15%, 13%, 8%

# ---- outside the table (cross-checks only) -----------------------------------------------------------
r100 = ratio(jackpot(100, 50))
near(r100, 1.363, 0.0005)                                 # f = 0.5 keeps rising past 2N = 50 in this chain
fixed = {n2: g(ratio(jackpot(n2, 6))) for n2 in (60, 120)}
near(fixed[60], 1.0445, 0.00005)                          # fixed family of 6: the excess shrinks with N
assert fixed[120] < fixed[60]

finish({
    "object": "M-507",
    "inputs": [
        {"name": "jackpot chain", "cite": "claim file E4 Formal statement (Z23188201 s2)", "text": MODEL},
        {"name": "paper table t/4Ne and WF baseline at 2N = 20/30/50", "cite": "claim file E4 Formal statement (Z23188201 s2)"},
        {"name": "claim-file derived peak ratios", "cite": "claim file E4", "text": DERIVED},
        {"name": "10% threshold", "cite": "Q72 (E4 q1, F6 q1)", "text": Q72},
        {"name": "P_fix = 1/(2N)", "cite": "E4 q2", "text": PFIX},
        {"name": "jackpot probability pj = 0.1; m = min(round(f 2N), 2N - 1)", "cite": "R4 E (research/checks/e4_relictation_chain.py)"},
        {"name": "cross-checks outside the table", "cite": "R4 E", "text": [R4_LARGE, R4_FIXED, R4_FSTAR]},
    ],
    "values": {
        "wf_ratio": {str(k): g(v) for k, v in wf.items()},
        "table_ratio": {f"{int(round(f * 100))}%": [g(table[(f, n2)]) for n2 in SIZES] for f in FS},
        "max_abs_deviation_from_paper_table": g(max(abs(table[(f, n2)] - PAPER[f][k]) for f in FS
                                                    for k, n2 in enumerate(SIZES)), 5),
        "pfix_times_2N": 1.0,
        "statement_excess_pct_from_printed_cells": {str(k): v for k, v in excess_printed.items()},
        "printed_column_max": {str(k): {"f": v[0], "ratio": v[1]} for k, v in col_max.items()},
        "excess_pct_at_printed_column_max": {str(k): v for k, v in excess_colmax.items()},
        "exact_peak_over_integer_m": {str(k): v for k, v in best_m.items()},
        "exact_peak_excess_pct_over_wf_chain": {str(k): v for k, v in excess_exact.items()},
        "excess_pct_over_wf_at_low_f": {f"{int(f * 100)}%": {str(k): v for k, v in d.items()} for f, d in low.items()},
        "f_star_plus5pct": {str(k): v for k, v in fstar.items()},
        "ratio_2N100_f50": g(r100),
        "fixed_family_m6": {str(k): v for k, v in fixed.items()},
    },
    "positions": {
        "day": {"reading": "above ~10% replacement t = 4Ne breaks (+15%, +21%, +29% over WF at 2N = 20/30/50); below it "
                           "the formula holds; P_fix = 1/(2N)",
                "excess_pct": {str(k): v for k, v in excess_colmax.items()}, "pfix_times_2N": 1.0},
        "critic": {"reading": "the known multiple-merger result; P_fix unchanged; growth with N needs family size "
                              "proportional to N, and a fixed family returns to the drift baseline",
                   "fixed_family_m6": {str(k): v for k, v in fixed.items()},
                   "f_star_plus5pct": {str(k): v for k, v in fstar.items()}},
    },
    "notes": "All 27 table cells and the WF baseline reproduce to 0.00042; P_fix = i/2N to 1e-12 in every chain. The "
             "object's 14.9% and 28.8% are the column maxima over WF; its 20.4% uses the 2N = 30 cell at f = 50% "
             "(1.146), but that column peaks at f = 60% (1.148), giving 20.6% (gap 0.2 points; the claim file's "
             "derived line has the same slip, and the paper's ~21% holds). Over every integer m the exact peak "
             "excess over the exact WF chain is 15.0%, 20.7%, 28.8% (m/2N = 0.55, 0.57, 0.60). 'No deviation "
             "below about 10%' holds at the +5% cut for 2N = 20 and 30 (+3.9%, +4.9% at f = 10%) but not at 2N = 50 (+6.6%; f* = 8%). The table covers "
             "2N = 20-50; in this chain f = 50% gives 1.363 at 2N = 100 (R4 E), while a fixed family of 6 falls "
             "from 1.0445 at 2N = 60 toward the drift baseline.",
})
