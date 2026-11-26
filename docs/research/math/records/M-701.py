#!/usr/bin/env python3
"""M-701 record (derivation): the Bernoulli Barrier fitness differential, 14.7x against 1,570x.

Object: docs/research/math/objects.yaml M-701 (formula, derivation). Z18167588 (abstract, Q24 = G q1): n = 157,000
loci at p = 0.5, N = 10,000, s = 0.01. The count of beneficial alleles per individual is Binomial(n, 0.5): mean
78,500, SD 198.1, CV 0.252%. The extremes of N = 10,000 draws sit near the 1 - 1/N normal quantile (3.719, the
paper's +-3.72 sigma): 79,237 and 77,763, 1,474 alleles = 7.44 sigma apart. The paper prints "(1.01)^1474 = 14.7"
against a required "157,000 x 0.01 = 1,570" and a shortfall of 107. The record asserts the reconciling numbers and
the printed figures the statement says are mislabelled: (1.01)^1,474 = 2.34e6 (gap of 1.6e5-fold to the printed
14.7), 1.01^157,000 = 10^678.4, while 14.7 = 1,474 x 0.01 (additive; ln of the ratio is 14.67) and 1,570/14.74 =
106.5 (printed 107, 0.5%). Closed forms only (stdlib). The figures cover the Z18167588 abstract and s3.1 only.

Run: research/.venv/bin/python -I docs/research/math/records/M-701.py [--write]
Without --write it checks that M-701.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, statistics, sys

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G = CL + "G-bernoulli-barrier.md"
GE = CL + "Ge-bb-omitted-from-3-0.md"
QD = "docs/research/sources/quotes-day.md"


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
Q24 = ("the fitness differential between the \"best\" and \"worst\" genotypes in a population of 10,000 is only "
       "14.7×—while the required differential is 1,570×, a shortfall exceeding 100-fold.")
held(G, Q24); held(QD, Q24)                                       # G q1 = Q24 (Z18167588 para 6, abstract)
FORM = held(G, "n = 157,000 loci at p = 0.5, N = 10,000, s = 0.01 per locus (uniform).")   # G formal statement
BIN = held(G, "Count per individual ~ Binomial(n, 0.5): mean 78,500, SD √(n·p·(1−p)) = 198.1, CV = 0.252% "
              "(paper: 198.1, 0.25%).")
EXT = held(G, "Extreme genotypes in N = 10,000 (normal order statistics): ±3.72σ → 79,237 / 77,763, difference "
              "1,474 = 7.44σ.")
PR_RATIO = held(G, "Paper: \"Fitness ratio = (1.01)¹⁴⁷⁴ ≈ 14.7×\".")
PR_REQ = held(G, "Required: \"157,000 × 0.01 = 1,570×\". Shortfall = 1,570/14.7 ≈ 107×.")
MULT = held(G, "multiplicative fitness (s3.1)")
R4X1 = held(G, "ln = 14.67 and additive 14.74 give 106.5 against the printed 107 (0.5%), so the stated conclusion "
               "survives: ledger.")
F2 = held(G, "no saturation of throughput at n_mid = 272 with r = 1/2 (rate linear in supply, R_int 0.975)")
GE_Q = held(GE, "even though both of them remain entirely correct.")      # Ge q1 (Day, 2026-10-01 para 26)
N_LOCI, P, N, S = 157_000, 0.5, 10_000, 0.01
assert "n = 157,000" in FORM and "p = 0.5" in FORM and "N = 10,000" in FORM and "s = 0.01" in FORM

# ---- binomial count and order statistics ---------------------------------------------------------
mean = N_LOCI * P
var = N_LOCI * P * (1 - P)
sd = math.sqrt(var)
cv = sd / mean
assert mean == 78_500 and var == 39_250
near(sd, 198.1, 0.05); near(100 * cv, 0.252, 5e-4)
z_q = statistics.NormalDist().inv_cdf(1 - 1 / N)                  # 1 - 1/N quantile, the paper's 3.72
near(z_q, 3.719, 5e-4)
Z = 3.72
hi, lo = mean + Z * sd, mean - Z * sd
assert round(hi) == 79_237 and round(lo) == 77_763
diff = 2 * Z * sd
assert round(diff) == 1_474 and abs(2 * Z - 7.44) < 1e-12
D = 1_474

# ---- the printed fitness numbers -------------------------------------------------------------------
ln_ratio = D * math.log1p(S)                                      # ln (1.01)^1474
near(ln_ratio, 14.67, 0.005)
mult_ratio = math.exp(ln_ratio)
near(mult_ratio / 1e6, 2.34, 0.005)                               # (1.01)^1,474 = 2.34e6, not 14.7
near(mult_ratio / 14.7, 1.59e5, 0.01e5)                           # the printed value is 1.6e5-fold short of its formula
log10_req_mult = N_LOCI * math.log10(1 + S)
near(log10_req_mult, 678.45, 0.01)                                # 1.01^157,000 = 10^678
add_avail = D * S
near(add_avail, 14.74, 1e-9)                                      # 14.7 is the additive 1,474 x 0.01
add_req = N_LOCI * S
near(add_req, 1570, 1e-9)                                         # 1,570 is the additive 157,000 x 0.01
short_add = add_req / add_avail
near(short_add, 106.5, 0.05)                                      # 1,570 / 14.74 = 106.5
short_printed = add_req / 14.7
near(short_printed, 106.8, 0.05); assert round(short_printed) == 107      # the printed 107
near(short_printed / short_add - 1, 0.0027, 5e-4)                 # 107 vs 106.5: within 0.5%
near(add_req / ln_ratio, 107.04, 0.01)                            # same figure via the log ratio 14.67
near(N_LOCI / D, short_add, 1e-9)                                 # = ln(1.01^n)/ln(1.01^1474): a log ratio, scale-free
assert short_add > 100                                            # the "exceeding 100-fold" holds on both readings
near(log10_req_mult - math.log10(mult_ratio), 672.08, 0.01)       # multiplicative counterpart of the shortfall: 10^672

finish({
    "object": "M-701",
    "inputs": [
        {"name": "n, p, N, s", "value": [N_LOCI, P, N, S], "cite": "G formal statement; Z18167588 abstract and s3.1 (Q24)"},
        {"name": "printed 14.7x, 1,570x, 107x", "value": [14.7, 1570, 107], "cite": "G q1 = Q24; G formal statement (paper's s3 formulas)"},
        {"name": "z for extremes of N", "value": Z, "cite": "G formal statement (paper +-3.72 sigma); 1 - 1/N normal quantile 3.719"},
    ],
    "values": {
        "binomial": {"mean": mean, "var": var, "sd": round(sd, 2), "cv_percent": round(100 * cv, 4)},
        "extremes": {"z_quantile_1_minus_1_over_N": round(z_q, 4), "high": round(hi), "low": round(lo),
                     "difference_alleles": round(diff, 1), "difference_sigma": 7.44},
        "multiplicative": {"ln_1.01^1474": round(ln_ratio, 3), "1.01^1474": f"{mult_ratio:.3e}",
                           "log10_1.01^157000": round(log10_req_mult, 2),
                           "log10_shortfall": round(log10_req_mult - math.log10(mult_ratio), 2)},
        "additive": {"available_1474x0.01": round(add_avail, 2), "required_157000x0.01": add_req,
                     "shortfall_1570/14.74": round(short_add, 2), "shortfall_1570/14.7": round(short_printed, 2),
                     "shortfall_via_ln_14.67": round(add_req / ln_ratio, 2)},
    },
    "positions": {
        "day": {"reading": "best-to-worst differential 14.7x against 1,570x required, shortfall above 100-fold",
                "holds": "binomial and order-statistic numbers reproduce; shortfall 106.5 (additive) or 107.0 (log) > 100"},
        "critic": {"reading": "14.7 and 1,570 are additive differences labelled as ratios; all-beneficial target not needed",
                   "holds": "(1.01)^1474 = 2.34e6 and 1.01^157000 = 10^678.4, so the printed 'ratio' is a label slip (ledger)"},
    },
    "notes": "The printed equation (1.01)^1474 = 14.7 is false as written: its left side is 2.34e6. 14.7 is the additive "
             "1,474 x 0.01 = 14.74 (or ln of the ratio, 14.67), and 1,570 the additive 157,000 x 0.01; their quotient "
             "106.5 (107.0 via 14.67) matches the printed 107 within 0.5%, so the shortfall exceeding 100-fold survives "
             "on the additive or log reading (R4 X1: label slip, ledger). On the multiplicative reading the paper's s3.1 "
             "states, the gap is 10^672. The +-3.72 sigma is the 1 - 1/N normal quantile (3.719), not the expected "
             "maximum of N draws. Whether the all-beneficial genotype is the required target (critic) is a modelling "
             "question this record does not settle; R4 F2 found no saturation at 272 active loci with r = 1/2. Day's "
             "'remain entirely correct' (Ge q1) is about G's external verdict (contested), not this arithmetic.",
})
