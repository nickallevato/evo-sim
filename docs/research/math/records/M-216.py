#!/usr/bin/env python3
"""M-216 record (model-choice): reproductive covariance (sweepstakes) and P(fix) = x0.

Object: docs/research/math/objects.yaml M-216 (model-choice, derivation). Exact absorbing Markov
chains on 2N = 20 gene copies, solved by Gaussian elimination: (a) Wright-Fisher; (b) a sweepstakes
chain (with probability psi all copies descend from one uniformly drawn copy, else Wright-Fisher),
with psi set so that N/Ne = 5.6 as in keruru's chain; (c) both chains with a covariance c between
carrying the allele and reproducing (carriers drawn with weight 1 + c). The record computes P(fix)
of one new copy under each, side by side: Day's position names covariance as the disputed parameter
and gives no value for it; the critic position is that a neutral allele has c = 0 by definition.
Inputs carry their quote id or claim file; held() checks each quote verbatim.

Run: research/.venv/bin/python -I docs/research/math/records/M-216.py [--write]
Without --write it checks that M-216.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
QD = "docs/research/sources/quotes-day.md"
B3G = CL + "B3g-day-concession-no-ne-in-kimura-identity.md"
B7C = CL + "B7c-keruru-retraction-census-n-cancels.md"


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


M = 20                                                   # 2N gene copies


def sample_p(i, c):
    """Frequency of the allele among parents drawn for the next generation (weight 1 + c for carriers)."""
    return i * (1 + c) / (i * (1 + c) + M - i)


def row(i, psi, c):
    p = sample_p(i, c)
    r = [math.comb(M, j) * p ** j * (1 - p) ** (M - j) * (1 - psi) for j in range(M + 1)]
    r[M] += psi * p                                      # sweepstakes: one drawn copy parents everyone
    r[0] += psi * (1 - p)
    return r


def p_fix(psi, c):
    """u_i = sum_j P_ij u_j, u_0 = 0, u_M = 1; solved exactly up to float rounding."""
    n = M - 1
    A = [[0.0] * n for _ in range(n)]
    b = [0.0] * n
    for a, i in enumerate(range(1, M)):
        r = row(i, psi, c)
        for j in range(1, M):
            A[a][j - 1] = (1.0 if i == j else 0.0) - r[j]
        b[a] = r[M]
    for k in range(n):                                   # Gaussian elimination with partial pivoting
        piv = max(range(k, n), key=lambda q: abs(A[q][k]))
        A[k], A[piv], b[k], b[piv] = A[piv], A[k], b[piv], b[k]
        for q in range(k + 1, n):
            f = A[q][k] / A[k][k]
            for j in range(k, n):
                A[q][j] -= f * A[k][j]
            b[q] -= f * b[k]
    u = [0.0] * n
    for k in reversed(range(n)):
        u[k] = (b[k] - sum(A[k][j] * u[j] for j in range(k + 1, n))) / A[k][k]
    return [0.0] + u + [1.0]


# ---- inputs -------------------------------------------------------------------------------
FIAT = held(B3G, "his sweepstakes parent is drawn uniformly at random — setting the one parameter in dispute, the "
                 "covariance between who breeds and what they carry, to zero by fiat.")
Q77 = held(QD, "He left out reproductive covariance, so he wrote the wrong equation, so P(fix) = x₀ is a wrong answer to the real question.")
Q78 = held(QD, "the number he got out — fixation equals starting frequency — is false for any real population because "
               "it’s the answer to the frictionless-coin problem, not the breeding one.")
E4 = held(B3G, "\"The fixation probability p = 1/(2N) is protected by the martingale property and holds exactly regardless of offspring distribution\"")
K_CH = held(B7C, "The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places.")
K_56 = held(B7C, "a sweepstakes model with Nₑ 5.6× lower at the same census")

# sweepstakes strength: 1/(2Ne) = (1 - psi)/M + psi  =>  N/Ne = (1 - psi) + M psi
PSI = 4.6 / (M - 1)
near((1 - PSI) + M * PSI, 5.6, 1e-12)

# ---- c = 0: P(fix) = x0 in both chains (martingale) ------------------------------------------------
res = {}
for name, psi in (("wright_fisher", 0.0), ("sweepstakes_Ne_5.6x_lower", PSI)):
    u = p_fix(psi, 0.0)
    for i in range(M + 1):
        near(u[i], i / M, 1e-12)                         # P(fix) = starting frequency, every i
    res[name] = {"c": 0.0, "pfix_x_2N": u[1] * M}
    near(u[1] * M, 1.0, 1e-12)
    for i in range(1, M):                                # E[p'] = p: the frequency is a martingale
        near(sum(j * pr for j, pr in enumerate(row(i, psi, 0.0))) / M, i / M, 1e-12)

# ---- c != 0: the martingale breaks and P(fix) departs from x0 ---------------------------------------
cov = {}
for name, psi in (("wright_fisher", 0.0), ("sweepstakes_Ne_5.6x_lower", PSI)):
    for c in (-0.05, 0.05):
        u = p_fix(psi, c)
        cov[f"{name}_c{c:+.2f}"] = g(u[1] * M)
        assert abs(u[1] * M - 1) > 0.01                  # no longer 1/(2N)
        drift = sum(j * pr for j, pr in enumerate(row(1, psi, c))) / M - 1 / M
        assert (drift > 0) == (c > 0)                    # covariance = directional change = selection
near(cov["wright_fisher_c+0.05"], 2.172, 0.001)          # Kimura (1-e^-0.1)/(1-e^-2) x 20 = 2.20
near(cov["wright_fisher_c+0.05"] / (M * (1 - math.exp(-0.1)) / (1 - math.exp(-2.0))), 1.0, 0.02)  # diffusion check
near(cov["sweepstakes_Ne_5.6x_lower_c+0.05"], 1.184, 0.001)
near(cov["wright_fisher_c-0.05"], 0.319, 0.001)
near(cov["sweepstakes_Ne_5.6x_lower_c-0.05"], 0.844, 0.001)
assert cov["wright_fisher_c-0.05"] < 1 and cov["sweepstakes_Ne_5.6x_lower_c-0.05"] < 1

finish({
    "object": "M-216",
    "inputs": [
        {"name": "Day: covariance set to zero by fiat", "cite": "B3g q3 (blog 2026-08-27 para 3)"},
        {"name": "Athos via Day: P(fix) = x0 wrong for real populations", "cite": "Q77, Q78 (B3g q5, q6)"},
        {"name": "Day Z23188201: 1/(2N) exact for any offspring distribution", "cite": "claim file B3g (E4)"},
        {"name": "keruru exact chains: 1/(2N_census) to 15 decimals; Ne 5.6x lower", "cite": "B7c q2; claim file B7c"},
        {"name": "chain size and sweepstakes psi", "value": {"2N": M, "psi": g(PSI), "N_over_Ne": 5.6}, "cite": "this record (illustrative size)"},
    ],
    "values": {"c0": {k: g(v["pfix_x_2N"]) for k, v in res.items()}, "c_nonzero_pfix_x_2N": cov},
    "positions": {
        "day": {"reading": "real populations have genotype-reproduction covariance; x0 answers the no-covariance problem",
                "number": None,
                "why_none": "Day and Athos name the covariance but give no value; the record shows what any c != 0 does (2.17x and 1.18x at c = +0.05; 0.32x and 0.84x at c = -0.05)"},
        "critic": {"reading": "a neutral allele has c = 0 by definition; then P(fix) = x0 under any offspring distribution",
                   "pfix_x_2N_wright_fisher": 1.0, "pfix_x_2N_sweepstakes": 1.0},
    },
    "notes": "With c = 0, P(fix) = i/2N to 1e-12 in both chains, including the sweepstakes chain with Ne 5.6x below N "
             "(keruru's result; Day's Z23188201 sentence). With c != 0 the allele frequency has a drift term, which "
             "is selection, and P(fix) moves off 1/(2N). The arithmetic of both readings is fixed; whether a neutral "
             "allele can carry covariance is the definitional dispute.",
})
