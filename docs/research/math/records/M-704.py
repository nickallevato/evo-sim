#!/usr/bin/env python3
"""M-704 record (derivation): a specific list of fixations against any k of M, and the middle case.

Object: docs/research/math/objects.yaml M-704 (inference, derivation). P_specific(n) = prod p_i for a named list;
P_any(>= k of M) = P(Binomial(M, p) >= k). At McCarthy's inputs (G3 formal statement; MC-02, MC-03: M = 4.5e11 new
mutations, p = 1/20,000, k = 2e7) the mean is 22.5e6 and the SD 4,743, k lies 527 SD below the mean, and the Chernoff
bound puts P(K < k) at <= 10^-62,689, so P_any is about 1 under that neutral k = mu model, against P_specific =
10^-86,020,600 (M-703). The middle case (R4 G1): n_f required changes, each met by any of m interchangeable
alternatives with Poisson mean lambda of successful arisings, P_all = (1 - e^-lambda)^n_f, so lambda at P_all = 0.5
is -ln(1 - 2^(-1/n_f)): 12.33 at n_f = 157,000 and 17.18 at 2e7 (the 12.3-17.2 band), with a 0.05-to-0.95 width of
4.07; closed form, no simulation. The per-locus lambda 0.1-6 and the gene-level pool clearing the flip for about ten
needed changes are R4 D1 measurements, quoted with locators, not recomputed. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-704.py [--write]
Without --write it checks that M-704.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G3 = CL + "G3-specific-vs-any.md"
G3A = CL + "G3a-camestros-lottery.md"
G3B = CL + "G3b-day-either-specific-or-interchangeable.md"
QC = "docs/research/sources/quotes-critics.md"
R4G1 = "research/checks/results/R4-G1.md"
R4D1 = "research/checks/results/R4-D1-spike.md"


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
MC02 = ("But our evolutionary history does not require that an exact group of 20 million mutations become fixed—only "
        "that some 20 million out of an enormous pool of candidate mutations become fixed.")
held(G3, MC02); held(QC, MC02)                                    # G3 q2 = MC-02
MC03 = held(QC, "50,000 x 9 million = 450 billion new mutations altogether.")      # MC-03 (Day's own inputs)
CA09 = held(G3A, "However, the probability that SOME number is picked is close to 1")  # G3a q1 = CA-09
DAY = held(G3B, "Either the specific fixations matter — in which case the Darwillion applies — or they’re "
                "interchangeable — in which case they’re neutral noise that can’t explain the observed functional "
                "divergence.")                                    # G3b q1 (Day, Education post para 28)
G3_FORM = held(G3, "With McCarthy's inputs (M = 4.5e11 new mutations in 9 My, p = 1/20,000 = 5e-5): mean M·p = "
                   "22.5e6, SD = √(M p (1−p)) = 4,743; k = 20e6 is 527σ below the mean")
CHERN = held(R4G1, "(The Chernoff bound puts the failure probability at ≤ 10^−62,689.)")
MIDDLE = held(R4G1, "Then P_all = (1 − (1−q)^m)^{n_f} = (1 − e^{−λ})^{n_f}, where **λ = −m·ln(1−q)**.")
ROW157 = held(R4G1, "| 157,000 | 10.87 | 12.33 | 14.93 | 4.07 |")
ROW2E7 = held(R4G1, "| 2e7 | 15.71 | 17.18 | 19.78 | 4.07 |")
ROW1E3 = held(R4G1, "| 1,000 | 5.81 | 7.28 | 9.88 | 4.07 |")
ADAPT = held(R4G1, "This applies only to the adaptive subset. Neutral differences have no \"required\" function.")
D1_LOC = held(G3B, "Per locus (exact RNA structure, DMS beneficial-proxy per codon): lambda ~0.1-6 at s = 0.01, below "
                   "lambda_50 (7-17), so the specific horn holds at locus granularity.")
D1_GENE = held(R4D1, "So the gene-level pool does clear the flip for a gene needing about ten adaptive changes at s = "
                     "0.01 and not for a gene needing twenty-five or more, and it does not at s = 0.001.")
D1_POOL = held(R4D1, "**51** [0–1,760]; 17% of datasets have zero")
M_POOL, P_FIX, K = 4.5e11, 1 / 20_000, 2.0e7


def lam_at(target, n_f):                                          # lambda with (1 - e^-lambda)^n_f = target
    return -math.log(-math.expm1(math.log(target) / n_f))


# ---- McCarthy's any-k-of-M ---------------------------------------------------------------------------
near(50_000 * 9e6, M_POOL, 0)                                     # MC-03
mean = M_POOL * P_FIX
sd = math.sqrt(M_POOL * P_FIX * (1 - P_FIX))
near(mean, 22.5e6, 1e-6); near(sd, 4_743, 0.5)
zdist = (mean - K) / sd
near(zdist, 527.1, 0.05)                                          # k is 527 SD below the mean
a = K / M_POOL                                                    # Chernoff (KL) bound on P(K <= k)
kl = a * math.log(a / P_FIX) + (1 - a) * math.log((1 - a) / (1 - P_FIX))
log10_fail = -M_POOL * kl / math.log(10)
near(log10_fail, -62_688.8, 0.05); assert math.floor(log10_fail) == -62_689
log10_specific = K * math.log10(P_FIX)
near(log10_specific, -86_020_600, 0.5)                            # P_specific (M-703)

# ---- the middle case: flip points in closed form ------------------------------------------------------
flips = {}
for n_f in (1_000, 157_000, 200_000, 2e7):
    l05, l50, l95 = (lam_at(t, n_f) for t in (0.05, 0.5, 0.95))
    near((1 - math.exp(-l50)) ** n_f, 0.5, 1e-9)                  # the closed form solves P_all = 0.5
    flips[n_f] = (l05, l50, l95, l95 - l05)
    near(l95 - l05, 4.07, 0.005)                                  # band width 4.07 at every n_f shown
near(flips[157_000][1], 12.33, 0.005); near(flips[2e7][1], 17.18, 0.005)      # lambda_50 = 12.3-17.2
near(flips[157_000][0], 10.87, 0.005); near(flips[157_000][2], 14.93, 0.005)
near(flips[2e7][0], 15.71, 0.005); near(flips[2e7][2], 19.78, 0.005)
near(flips[200_000][1], 12.57, 0.005)
near(flips[1_000][1], 7.275, 5e-4)                                # 7.27; R4 G1's table prints 7.28 (rounding, 0.07%)
assert "| 7.28 |" in ROW1E3
near(math.log(math.log(0.05) / math.log(0.95)), 4.0674, 5e-4)     # large-n_f limit of the width
assert lam_at(0.5, 1) < 1                                         # m = 1 (specific horn) cannot reach the flip ...
for lam_locus in (0.1, 6):                                        # ... nor can the per-locus lambda 0.1-6 (R4 D1)
    assert lam_locus < flips[1_000][1] and (1 - math.exp(-lam_locus)) ** 157_000 < 1e-100

finish({
    "object": "M-704",
    "inputs": [
        {"name": "M, p, k (McCarthy)", "value": [M_POOL, P_FIX, K], "cite": "G3 formal statement; MC-02, MC-03"},
        {"name": "middle-case model", "value": "P_all = (1 - e^-lambda)^n_f", "cite": "R4 G1 (middle case formalised)"},
        {"name": "per-locus lambda; gene-level pool", "value": {"lambda_locus": [0.1, 6], "pool_median": 51},
         "cite": "R4 D1 via G3b Check; R4-D1-spike.md Table A and para after Table C (quoted, not rerun)"},
    ],
    "values": {
        "any_k_of_M": {"mean": mean, "sd": round(sd, 1), "sigma_distance": round(zdist, 2),
                       "log10_chernoff_bound_P_K_below_k": round(log10_fail, 1)},
        "log10_P_specific": round(log10_specific, 1),
        "lambda_flip": {str(int(n)): {"l05": round(v[0], 3), "l50": round(v[1], 3), "l95": round(v[2], 3),
                                      "width": round(v[3], 3)} for n, v in flips.items()},
    },
    "positions": {
        "day": {"reading": "either the specific fixations matter (Darwillion) or they are interchangeable and neutral",
                "holds": "at locus granularity lambda 0.1-6 is below the flip (specific horn stands, R4 D1); 'neutral is "
                         "not functional' is valid"},
        "critic": {"reading": "history needs some 20 million out of a large pool, so P_any is about 1",
                   "holds": "527 SD below the mean, P(K < k) <= 10^-62,689 under k = mu; the middle case exists and "
                            "flips at lambda_50 = 12.3-17.2 (adaptive subset only)"},
    },
    "notes": "P_any near 1 holds only under McCarthy's neutral k = mu supply, which branch B contests. Day's dilemma "
             "(G3b) has two horns; the middle case, k of M interchangeable adaptive alternatives, is a third, with a "
             "sharp flip at lambda_50 = -ln(1 - 2^(-1/n_f)): 12.33 at n_f = 157,000, 17.18 at 2e7, band 4.07 wide. "
             "R4 G1's n_f = 1,000 row prints 7.28 where the closed form gives 7.275 (a rounding slip, 0.07%; the "
             "12.3-17.2 band is unaffected). The R4 D1 values (per-locus lambda 0.1-6; a gene-level pool of 51 "
             "proxy-beneficial SNVs clears the flip for about ten needed changes at s = 0.01, not 25, not at s = 0.001) "
             "are measurements quoted with locators.",
})
