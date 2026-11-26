#!/usr/bin/env python3
"""M-713 record (derivation, structural): F_max = t_div x d / (g_len x G_f) has no mu, N or s term.

Object: docs/research/math/objects.yaml M-713 (inference, derivation). The formula (G2h formal statement, after claim
A) divides a time by an empirical generations-per-fixation figure. The record asserts the identity on rationals at two
test points that differ in mutation rate, population size and selection coefficient: F_max is the same, so the
formula has no term in any of them (Hancock, G2h q1 and q2, literal reading). At Day's 3.0 inputs (6.3e6 y, 25 y,
1,322) F_max = 190.6 at d = 1 and 85.8 at d = 0.45. Day's reading (G1 q1): G_f is a measured total throughput, so
supply, selection and parallelism sit inside the number and the question is the transfer to humans. The supply
scaling the claim files cite (A5: genome about 690x larger, 3.1e9/4.6e6 = 674, 3.1e9/4.5e6 = 689; the per-genome
supply ratio kappa = 38.4/4.1e-4 = 93,659 in parameters) is asserted as arithmetic; whether a supply term belongs in
the transfer is the critic's case and is not settled here. Exact rationals and stdlib.

Run: research/.venv/bin/python -I docs/research/math/records/M-713.py [--write]
Without --write it checks that M-713.json is current; --write saves it.
"""
import hashlib, inspect, json, pathlib, sys
from fractions import Fraction as Fr

HERE = pathlib.Path(__file__).resolve()
ROOT = HERE.parents[4]
DATE = "2026-11-26"
CL = "docs/research/claims/"
G1 = CL + "G1-average-rate-includes-parallelism.md"
G2H = CL + "G2h-hancock-fmax-has-no-mutation-or-selection-term.md"
A5 = CL + "A5-genome-size-mutation-supply.md"
PY = "docs/research/parameters.yaml"


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


# ---- the source sentences ---------------------------------------------------------------------------
Q1 = held(G2H, "Notice that his model had no mutation rate, right?")              # G2h q1 (t=01:41:38, ASR)
Q2 = held(G2H, "this is not even necessarily a measure of selection")             # G2h q2 (t=01:36:03, ASR)
NOS = held(G2H, "\"Like there's no selection coefficient in any of this\"")
FORM = held(G2H, "F_max = (t_div x d)/(g_len x G_f) (A): a time divided by an empirical generations-per-fixation figure.")
HANC = held(G2H, "Hancock's reading: the formula takes no mu, N or s, so it constrains an observed rate without saying "
                 "which process produced it.")
DAYR = held(G2H, "Day's reading (A, G1): G_f is a measured total throughput of the LTEE, so mutation supply, selection "
                 "and parallelism are inside the number; the transfer to humans is the question (A2e, A5).")
DAY_G1 = held(G1, "It is the total throughput, the net output after parallel fixation, clonal interference, sweep "
                  "displacement, and every other concurrent dynamic has played out.")       # G1 q1
VERD = held(G2H, "the transfer is the question and A5/A5c supply scaling (~690x) favours the critic")
A5Q = held(A5, "roughly 690 times larger than the compact E. coli genome of about 4.6 million base pairs.")
A5D = held(A5, "3.1e9/4.6e6 = 674 (McCarthy states \"roughly 690\"; 690 follows from a 4.5 Mb E. coli genome, "
               "3.1e9/4.5e6 = 689; a 2% discrepancy with his own stated inputs)")
KAPPA = held(PY, "supply_ratio_kappa: {value: 93659, derived: \"38.4 / 4.1e-4\"")   # mutation.supply_ratio_kappa
TDIV = Fr(6_300_000); held(PY, "day_2026_mittens3: {value: 6.3e6, source: Z23003785")
GLEN = Fr(25); held(PY, "day_2026: {value: 25, source: Z23003785")
GF = Fr(1_322); held(PY, "day_mittens3_nonmutator: {value: 1322")
D45 = Fr(45, 100); held(PY, "turnover_d: {value: 0.45")


def f_max(t_div, d, g_len, g_f, **population):
    """The formula as written; any population argument (mu, N, s) is accepted and never read."""
    return t_div * d / (g_len * g_f)


# ---- the identity at two test points -------------------------------------------------------------------
pt1 = dict(mu=Fr(12, 10**9), N=10_000, s=Fr(1, 100))
pt2 = dict(mu=Fr(1, 10**6), N=10**8, s=Fr(1, 1000))
for d in (Fr(1), D45):
    assert f_max(TDIV, d, GLEN, GF, **pt1) == f_max(TDIV, d, GLEN, GF, **pt2)   # no mu, N or s dependence
src = inspect.getsource(f_max).split('"""')[-1]
assert not any(tok in src for tok in ("mu", "population[", ".get(", " s ", "N"))   # the body reads none of them
fm1, fm45 = f_max(TDIV, 1, GLEN, GF), f_max(TDIV, D45, GLEN, GF)
near(float(fm1), 190.62, 0.005); near(float(fm45), 85.78, 0.005)
assert fm1 == TDIV / GLEN / GF                                    # = 252,000 / 1,322 (M-711)

# ---- the supply scaling the claim files cite ---------------------------------------------------------------
near(3.1e9 / 4.6e6, 674, 0.5); near(3.1e9 / 4.5e6, 689, 0.5)      # A5: "roughly 690"
near(38.4 / 4.1e-4, 93_659, 0.5)                                  # kappa (parameters)
assert "~690x" in VERD

finish({
    "object": "M-713",
    "inputs": [
        {"name": "formula", "value": "t_div x d / (g_len x G_f)", "cite": "G2h formal statement (claim A)"},
        {"name": "t_div, g_len, G_f, d", "value": [float(TDIV), float(GLEN), float(GF), [1, float(D45)]],
         "cite": "parameters divergence.t_div_years.day_2026_mittens3, generation_time_years.day_2026, ltee.gens_per_fixation.day_mittens3_nonmutator, selection.turnover_d"},
        {"name": "test points (mu, N, s)", "value": [[float(pt1["mu"]), pt1["N"], float(pt1["s"])],
                                                     [float(pt2["mu"]), pt2["N"], float(pt2["s"])]], "cite": "constructed"},
        {"name": "supply scaling", "value": {"genome_ratio": [674, 689], "kappa": 93659}, "cite": "A5 q1 and derived line; parameters mutation.supply_ratio_kappa"},
    ],
    "values": {
        "F_max_d1": round(float(fm1), 3), "F_max_d0.45": round(float(fm45), 3),
        "invariant_in_mu_N_s": True,
        "genome_ratio": [round(3.1e9 / 4.6e6, 1), round(3.1e9 / 4.5e6, 1)], "kappa": round(38.4 / 4.1e-4),
    },
    "positions": {
        "day": {"reading": "G_f is a measured LTEE total throughput; supply, selection and parallelism are inside it",
                "holds": "F_max takes them through G_f only; the open step is transferring G_f to humans"},
        "critic": {"reading": "the formula has no mutation rate or selection coefficient, so it is not a test of selection",
                   "holds": "literally true: F_max is identical at two test points that differ in mu, N and s"},
    },
    "notes": "The identity is structural: F_max is a function of (t_div, d, g_len, G_f) only. Both readings agree on "
             "that; they differ on whether an empirical G_f can carry the supply, selection and parallelism of a "
             "different organism. The supply ratios the claim files cite (genome 674-689x; per-genome supply kappa "
             "93,659) are asserted as arithmetic; G2h's verdict comment says they favour the critic on transfer, which "
             "is an external question (A5, A2e), and the objection restates the supply objection (M-103).",
})
