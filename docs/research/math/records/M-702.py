#!/usr/bin/env python3
"""M-702 record (derivation): coefficient of variation against variance of the beneficial-allele count.

Object: docs/research/math/objects.yaml M-702 (inference, derivation). For K ~ Binomial(n, p): Var K = n p (1 - p)
rises with n and CV = sqrt((1 - p)/(n p)) falls as 1/sqrt(n). At n = 157,000, p = 0.5: Var 39,250, SD 198.1, CV
0.252% (G formal statement, G5 = RF-1). Doubling n doubles Var and divides CV by sqrt 2 (asserted exactly on
rationals). Under the paper's own multiplicative fitness w = (1 + s)^K, Var(ln w) = Var K (ln(1 + s))^2 also rises
with n (3.89 at n = 157,000, s = 0.01). Z18167588's own s7.10 example (1,000 loci: variance 250, mean 500) and its
s7.6 premise (response proportional to variance, per Fisher) are held from claim file G: on that premise the
quantity that sets the response, the variance, rises with n, so the falling CV does not give a falling response.
The infinitesimal-model question (G6) is a literature question; Fisher 1918 is not held, so the record states the
algebra and leaves G6's verdict where it is. Closed forms only (stdlib).

Run: research/.venv/bin/python -I docs/research/math/records/M-702.py [--write]
Without --write it checks that M-702.json is current; --write saves it.
"""
import hashlib, json, math, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G = CL + "G-bernoulli-barrier.md"
G5 = CL + "G5-matev-cv-falls-variance-rises.md"
G6 = CL + "G6-panel-infinitesimal-model-answer.md"
QC = "docs/research/sources/quotes-critics.md"
R4G1 = "research/checks/results/R4-G1.md"


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
RF1 = ("While this coefficient of variation does go to zero as n increases, the variance of the beneficial allele "
       "count of an individual just increases as n increases.")
held(G5, RF1); held(QC, RF1)                                      # G5 q1 = RF-1 (Matev, comment 338963242)
GGR44 = held(G6, "this is literally called the infinite decimal model. It's the fundamental model of quantitative "
                 "genetics.")                                     # G6 q1 = GGR-44 (ASR)
G6_OPEN = held(G6, "The audit has **not** checked whether the infinitesimal model answers the coefficient-of-variation step")
FISHER_NA = held(G6, "| Fisher 1918 (infinitesimal model) | not retrieved | unverified |")
S76 = held(G, "\"fitness variance decreases as the number of segregating loci increases\"")      # Z18167588 s7.6
S710 = held(G, "\"the variance in total beneficial allele count is 250, but the mean is 500\" for 1,000 loci")  # s7.10
FISH = held(G, "Fisher: response proportional to variance (s7.6)")
G_DER = held(G, "Absolute variance of the allele count grows with n (n/4 = 39,250); only the coefficient of variation "
                "(SD/mean) falls as 1/√n.")
G5_DER = held(G5, "Doubling n doubles Var and divides CV by sqrt(2).")
G1_RESP = held(R4G1, "Under multiplicative fitness (Day's stated s3.1 model) the expected per-locus response does not "
                     "fall with n. No cap appears near 230.")
G1_CV = held(R4G1, "The CV of the beneficial-allele count does fall as 1/√n, as Day says.")
N_LOCI, P, S = 157_000, Fr(1, 2), 0.01                            # G formal statement (Z18167588 s3)


def var(n, p):
    return n * p * (1 - p)


def cv2(n, p):                                                    # CV^2 = (1 - p)/(n p), exact on rationals
    return var(n, p) / (n * p) ** 2


# ---- the algebra, exact on rationals ---------------------------------------------------------------
for n in (1_000, 157_000, 2 * 157_000):
    assert cv2(n, P) == (1 - P) / (n * P)
for n in (1_000, 157_000):
    assert var(2 * n, P) == 2 * var(n, P)                         # doubling n doubles Var
    assert cv2(2 * n, P) == cv2(n, P) / 2                         # ... and halves CV^2: CV / sqrt 2
for p in (Fr(1, 10), Fr(1, 2), Fr(9, 10)):                        # the direction holds at any fixed p
    assert var(2_000, p) > var(1_000, p) and cv2(2_000, p) < cv2(1_000, p)

# ---- the figures at n = 157,000 -----------------------------------------------------------------------
v = var(N_LOCI, P)
assert v == 39_250 == Fr(N_LOCI, 4)
sd = math.sqrt(v); cv = math.sqrt(cv2(N_LOCI, P))
near(sd, 198.1, 0.05); near(100 * cv, 0.252, 5e-4)
near(math.sqrt(cv2(N_LOCI, P) / cv2(2 * N_LOCI, P)), math.sqrt(2), 1e-12)
assert var(1_000, P) == 250 and 1_000 * P == 500                  # Z18167588 s7.10's own example
var_lnw = float(v) * math.log1p(S) ** 2                           # Var(ln w) under w = (1 + s)^K
near(var_lnw, 3.886, 5e-4)
near(float(var(2 * N_LOCI, P)) * math.log1p(S) ** 2, 2 * var_lnw, 1e-9)   # rises linearly in n
sd_lnw = math.sqrt(var_lnw); near(sd_lnw, 1.971, 5e-4)

finish({
    "object": "M-702",
    "inputs": [
        {"name": "n, p, s", "value": [N_LOCI, float(P), S], "cite": "G formal statement (Z18167588 s3); G5 formal statement"},
        {"name": "s7.10 example", "value": {"loci": 1000, "variance": 250, "mean": 500}, "cite": "G formal statement (quoted s7.10)"},
        {"name": "response premise", "value": "Fisher: response proportional to variance", "cite": "G Assumptions (s7.6)"},
    ],
    "values": {
        "var_K": float(v), "sd_K": round(sd, 2), "cv_percent": round(100 * cv, 4),
        "doubling_n": {"var_factor": 2, "cv_factor": round(1 / math.sqrt(2), 6)},
        "var_ln_w_multiplicative": round(var_lnw, 4), "sd_ln_w": round(sd_lnw, 4),
    },
    "positions": {
        "day": {"reading": "fitness variance compresses as n grows; selection response needs that variance",
                "holds": "the CV does fall as 1/sqrt(n) (0.252% at n = 157,000), as Day says (R4 G1)"},
        "critic": {"reading": "only the CV falls; the variance that sets the response rises with n",
                   "holds": "Var K = n/4 = 39,250 and Var(ln w) = 3.89 both rise linearly in n (exact on rationals)"},
    },
    "notes": "Algebra settled: Var K = n p(1 - p) rises with n and CV = sqrt((1 - p)/(n p)) falls as 1/sqrt(n), both "
             "exactly. The paper's own s7.10 (variance 250, mean 500 at 1,000 loci) and its stated premise that response "
             "is proportional to variance (s7.6) mean the 'variance decreases' wording of s7.6 holds for the CV only; on "
             "that premise the falling CV does not imply a falling response (R4 G1: no per-locus fall under "
             "multiplicative fitness). Not settled here: whether the infinitesimal model (Fisher 1918, not retrieved) is "
             "the standard regime that answers the Barrier (G6, verdict pending); the record adds no literature.",
})
