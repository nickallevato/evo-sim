#!/usr/bin/env python3
"""M-013 record (identity): definition and units of d.

Object: docs/research/math/objects.yaml M-013 (identity, derivation). The record checks, with a
small unit algebra, that d = T x d_continuous is dimensionless (T in years, mortality force in
1/y), that F_max is then a pure count, and that Hancock's d = 25 (a generation count) cancels
g_len = 25 but leaves F_max with a 'gen' unit. The hazard-scale result (d x s exact for
hazard-scale s, factor 1 for per-generation s) is R4 C2's simulation; its figures are cited and
their stated agreement asserted, not recomputed.

Run: research/.venv/bin/python -I docs/research/math/records/M-013.py [--write]
Without --write it checks that M-013.json is current; --write saves it.
"""
import collections, hashlib, json, pathlib, sys

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


A4 = CL + "A4-turnover-coefficient-d.md"
A4F = CL + "A4f-hancock-d-not-a-selection-coefficient.md"
# ---- inputs -------------------------------------------------------------------------------
Q20 = held(QD, "d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model)")
Q21 = held(QD, "d = T × d_continuous = T × [∫ μ(x) × l(x) × v(x) dx / ∫ l(x) × v(x) dx]")
Q22 = held(QD, "finding d ≈ 0.45 from three independent loci")
Q18 = held(QD, "At 25 years per human generation")
Q06 = held(QD, "F_max = (t_div × d) / (g_len × G_f)")
GG21 = held(A4F, "I don't know what D is like there is no equivalent term in population genetics.")   # A4f q1
GG22 = held(A4F, "if you plugged in 25 there then you also have 25 in the denominator and cancel")    # A4f q2
C2a = held(A4, "Day's d = mean cumulative hazard at the age of mothers (0.789 vs 0.784)")
C2b = held(A4, "d*s is exact (V1, T*dr/s = 0.778 vs d = 0.789, within 1.5%)")
C2c = held(A4, "For per-generation s (fecundity, pre-maturity survival) the factor is 1 (V3/V4: Day's d*s 20-22% below exact)")
Q09 = held(QD, "Effective generations = 325,000 × 0.45 = 146,250")


# ---- unit algebra --------------------------------------------------------------------------
class Q:
    def __init__(self, v, **u):
        self.v, self.u = v, collections.Counter(u)

    def __mul__(self, o):
        u = collections.Counter(self.u); u.update(o.u)
        return Q(self.v * o.v, **{k: n for k, n in u.items() if n})

    def __truediv__(self, o):
        u = collections.Counter(self.u); u.subtract(o.u)
        return Q(self.v / o.v, **{k: n for k, n in u.items() if n})

    def dims(self):
        return {k: n for k, n in self.u.items() if n}


T = Q(25, y=1)                                          # generation time, years
mu_bar = Q(0.45 / 25, y=-1)                             # l v weighted mean mortality force, 1/y
d = T * mu_bar
assert d.dims() == {} and abs(d.v - 0.45) < 1e-12      # dimensionless, 0.45
near(mu_bar.v, 0.018, 1e-12)                            # implied mean force 0.018/y (claim file A4f)

t_div = Q(6.3e6, y=1)
g_len = Q(25, y=1, gen=-1)                              # years per generation
G_f = Q(1322, gen=1, fix=-1)                            # generations per fixation
F_day = (t_div * d) / (g_len * G_f)
assert F_day.dims() == {"fix": 1}                       # a pure count of fixations
near(F_day.v, 85.78, 0.005)

d_gen = Q(25, gen=1)                                    # Hancock's hypothetical: d as a generation count
F_hyp = (t_div * d_gen) / (g_len * G_f)
near(F_hyp.v, 6.3e6 / 1322, 1e-6)                       # 25 cancels g_len: F = t_div/G_f numerically
assert F_hyp.dims() == {"fix": 1, "gen": 1}             # but the result is not a count unless d is dimensionless

# ---- effective generations: hazard-scale (Day) against per-generation s (factor 1) ----------
assert 325_000 * 0.45 == 146_250                        # Q09
n_eff_day = 252_000 * 0.45
assert n_eff_day == 113_400
n_eff_pergen = 252_000 * 1
near(n_eff_pergen / n_eff_day, 2.222, 0.001)

# ---- R4 C2 figures (cited, not recomputed) -------------------------------------------------
near(abs(0.789 - 0.784) / 0.784, 0.0064, 0.0001)
assert abs(0.778 - 0.789) / 0.789 < 0.015               # "within 1.5%"

finish({
    "object": "M-013",
    "inputs": [
        {"name": "verbal definition", "cite": "Q20 (Z18166234 ¶33)", "quote": Q20},
        {"name": "integral definition", "cite": "Q21 (Z18166234 ¶51)", "quote": Q21},
        {"name": "d = 0.45", "cite": "Q22; parameters selection.turnover_d"},
        {"name": "g_len 25, G_f 1,322, t_div 6.3 My", "cite": "Q18, Q58"},
        {"name": "Hancock cancellation", "cite": "A4f q2 (GG-22)", "quote": GG22},
        {"name": "R4 C2 hazard-scale results", "cite": "claim file A4 (R4-H-C2)", "quote": [C2a, C2b, C2c]},
    ],
    "values": {
        "d_dims": "dimensionless", "implied_mean_mortality_force_per_y": g(mu_bar.v),
        "F_max_with_d_0.45": g(F_day.v), "F_max_units": "fix",
        "F_max_hancock_d_25": g(F_hyp.v), "F_max_hancock_units": "fix x gen",
        "N_eff_hazard_scale_d_0.45": n_eff_day, "N_eff_per_generation_s": n_eff_pergen,
        "r4_c2": {"d_vs_mean_cum_hazard": [0.789, 0.784], "T_dr_over_s_vs_d": [0.778, 0.789], "per_gen_s_factor": 1,
                  "day_ds_below_exact_per_gen": "20-22%"},
    },
    "positions": {
        "day": {"reading": "d is defined (Ch.13, App. A, Z18166234) and dimensionless; Hancock's d = 25 is not Day's d",
                "F_max": g(F_day.v), "N_eff": n_eff_day},
        "critic": {"reading": "no equivalent term in population genetics; for per-generation s the correction is 1",
                   "N_eff": n_eff_pergen, "F_max_at_factor_1": g(252_000 / 1322)},
    },
    "notes": "d x s is exact for hazard-scale s and the factor is 1 for per-generation s (R4 C2); which scale the aDNA s "
             "values use was not retrieved, so the choice stays with the claim verdicts (A4, A4f).",
})
