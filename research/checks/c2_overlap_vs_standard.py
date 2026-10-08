"""Check C2 / C2a / A4 (THROWAWAY): what is Day's turnover coefficient d relative to standard
overlapping-generation theory?   Seed: SeedSequence(20261011).
Run: research/.venv/bin/python -I research/checks/c2_overlap_vs_standard.py

PRE-REGISTERED PREDICTIONS (copied from claims C2 and C2a, 2026-10-07; plus two derivation-based additions
written 2026-10-08 BEFORE the simulation was run, marked [add]):
 Claimant (Day): in an age-structured population the change per nominal generation is d x s p q with d from
   d = T x int(mu l v)/int(l v) (Z18166234 eq. 3.3; Neolithic e0=32: d=0.53), 'a real demographic correction'.
 Opposing/standard (hypothesis, Charlesworth 1994 not retrieved): "the per-generation change of an allele
   frequency under selection is governed by the intrinsic fitness difference and the generation time, and when
   s is defined as the per-generation fitness difference (mean-generation-time scale) no further factor d<1 is
   needed ... d = 0.45 cannot then be estimated separately from s."  Standard expectations stated as hypotheses:
   (H-i) asymptotic frequency change per year is the Malthusian-fitness difference, logit slope = r_B - r_A
   (Fisher/Charlesworth); (H-ii) to first order, per generation T: T*(r_B - r_A) = Delta ln R0 = s_gen, the
   lifetime-reproductive-output difference, for ANY life table (r ~ ln R0 / T, T = mean age of mothers).
 Decision rule (from the claim): measured logit change per T years equals d*s*(...) for d from Day's formula over
   several life tables (supports C2a as a result) or equals s_gen for all of them (d is a rescaling of s).
 [add-1] Algebra: for a stationary population (R0=1) int(l v) = T, so Day's d = int(mu l v) dx, which equals the mean
   cumulative hazard to the age of mothers (H_bar, derived by integration by parts). Predict: d = H_bar, and
   Delta logit per T = d*s EXACTLY when s is the fractional reduction of the mortality hazard at all ages (V1), but
   = s when s is a relative survival/fecundity difference per generation (V3, V4): d is a UNIT CONVERSION between
   hazard-scale s and per-generation s, not a slowing of selection. Calendar-year rate = s_gen/T (no d).
 [add-2] Day's Table 1 d values (0.53 at e0=32 ... 0.015 at e0=78) are not reproduced exactly by a Siler family
   (Coale-Demeny West tables not retrieved); predict only the monotone decline and the order of magnitude.
 What this check cannot say: whether published aDNA s values were estimated per generation (almost certainly:
 logistic slope per generation), nor anything about hard/soft selection.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import wf_hc as h

ss = np.random.SeedSequence(20261011)
DAY_D = {32: 0.53, 37: 0.44, 42: 0.35, 47: 0.27, 52: 0.21, 60: 0.12, 67: 0.06, 78: 0.015}

# ---------------------------------------------------------------- 1. d vs mean cumulative hazard
print("== 1. Day's d on Siler life tables (R0=1, fertility 15-45) vs mean cumulative hazard H_bar ==")
print(" e0   T(y)   d_Day(formula)   H_bar    Day Table 1 d")
for fam, kw in [("Siler default", {}), ("forager-like (high infant, low adult)", dict(a1=0.25, b1=0.5, a2=0.002, a3=3e-5, b3=0.085))]:
    print(" family:", fam)
    for e0 in (25, 28, 32, 37, 42, 47, 52, 60, 67, 78):
        try:
            mu = h.life_table_for_e0(e0, **kw)
        except ValueError:
            print(f" {e0:3d}  (cannot fit)"); continue
        b = h.fert_schedule(mu)
        d, T = h.day_d(mu, b)
        print(f" {e0:3d}  {T:5.1f}   {d:8.3f}        {h.mean_cum_hazard(mu, b):7.3f}   {DAY_D.get(e0, float('nan'))}")
# discrete-generation control: annual semelparous organism, survival l to breeding, b = 1/l, then dies.
# Analytic Day d = -ln(l)  (NOT 1): his 'd = 1 for discrete generations' holds only if l = 1/e.
print(" discrete-generation control (survive to breeding with prob L, breed once at age 1, die); analytic d = -ln L:")
for L in (0.9, 0.5, 0.37, 0.1):
    mu_c = np.zeros(len(h.AGES)); mu_c[0] = -np.log(L); mu_c[2:] = 50.0
    b_c = np.zeros(len(h.AGES)); b_c[1] = 1.0 / L
    d_c, T_c = h.day_d(mu_c, b_c)
    sc_ = 0.02
    mB = mu_c.copy(); mB[0] *= (1 - sc_)
    dr = h.euler_lotka_r(mB, b_c) - h.euler_lotka_r(mu_c, b_c)
    print(f"   L={L:4.2f}: d_Day={d_c:6.3f} (-ln L={-np.log(L):6.3f}); hazard-scale s=0.02 -> T*dr/s = {T_c*dr/sc_:6.3f}")

# ---------------------------------------------------------------- 2. selection scenarios, exact Euler-Lotka
print("\n== 2. Malthusian growth difference vs d*s and s_gen (e0=32 Siler table; s=0.02) ==")
mu = h.life_table_for_e0(32)
b = h.fert_schedule(mu)
d_day, T = h.day_d(mu, b)
Hbar = h.mean_cum_hazard(mu, b)
R0A = h.R0_of(mu, b)
rA = h.euler_lotka_r(mu, b)
s = 0.02
print(f" wild type: R0={R0A:.6f}, r={rA:.2e}, T={T:.2f}, d_Day={d_day:.4f}, H_bar={Hbar:.4f}")
# Define advantage direction explicitly: advantaged type has (1-s)*hazard etc.
adv = {
    "V1 hazard x(1-s), all ages   (s = fractional hazard change)": (mu * (1 - s), b),
    "V4 pre-maturity viability: l(15) x(1+s'), s' such that l(15) rises by factor 1/(1-s)": (np.where(h.AGES < 15, mu - (-np.log(1 - s)) / 15.0, mu), b),
    "V5 adult viability 15-45: l(45) factor 1/(1-s)": (np.where((h.AGES >= 15) & (h.AGES < 45), mu - (-np.log(1 - s)) / 30.0, mu), b),
    "V3 fecundity x(1+s) at all ages": (mu, b * (1 + s)),
    "V2 additive hazard -0.01*s per year, all ages": (mu - 0.01 * s, b),
}
print(f" {'scenario':78s} {'T*dr':>8s} {'s_gen':>8s} {'T*dr/s':>7s} {'T*dr/s_gen':>10s} {'d_Day*s':>8s}")
res2 = {}
for name, (muB, bB) in adv.items():
    rB = h.euler_lotka_r(muB, bB)
    R0B = h.R0_of(muB, bB)
    sgen = np.log(R0B / R0A)
    Tdr = T * (rB - rA)
    res2[name] = (Tdr, sgen)
    print(f" {name:78s} {Tdr:8.5f} {sgen:8.5f} {Tdr/s:7.3f} {Tdr/sgen:10.4f} {d_day*s:8.5f}")
print(" (V1: T*dr/s should equal d_Day and H_bar; V3,V4,V5: T*dr/s ~ 1 when s is a per-generation relative difference)")

# deterministic two-type projection cross-check of the logit slope (calendar years)
print("\n deterministic 2-type projection, logit slope per YEAR x T  (years 150-450):")
for name, (muB, bB) in adv.items():
    lg = h.project_types([mu, muB], [b, bB], 500)
    yrs = np.arange(150, 450)
    slope = np.polyfit(yrs, lg[yrs], 1)[0]
    rB = h.euler_lotka_r(muB, bB)
    print(f"  {name[:60]:60s} slope*T={slope*T:.5f}  (Euler-Lotka T*dr={T*(rB-rA):.5f})")

# ---------------------------------------------------------------- 3. stochastic cohort IBM
print("\n== 3. Stochastic age-class IBM (e0=32 table; N0=2e5 per type; 24 reps; logit slope yrs 100-400) ==")
for name in list(adv)[:1] + list(adv)[3:4] + list(adv)[1:2]:
    muB, bB = adv[name]
    s_hat = []
    for _ in range(24):
        rng = np.random.default_rng(ss.spawn(1)[0])
        lg = h.cohort_ibm([mu, muB], [b, bB], 400, 400_000, rng)
        yrs = np.arange(100, 400)
        s_hat.append(np.polyfit(yrs, lg[yrs], 1)[0] * T)
    s_hat = np.array(s_hat)
    rB = h.euler_lotka_r(muB, bB)
    print(f"  {name[:60]:60s} IBM T*slope = {s_hat.mean():.5f} ± {s_hat.std(ddof=1)/np.sqrt(len(s_hat)):.5f}   exact {T*(rB-rA):.5f}")

# ---------------------------------------------------------------- 4. calendar-year vs per-generation, Day's recursion
print("\n== 4. Day's g_eff = d x g_nominal equals standard theory with generation time T/d ==")
for d in (0.45, 0.53):
    for T0 in (25.0, 27.7, 29.2):
        print(f"  d={d}, nominal T={T0}: equivalent generation length T/d = {T0/d:.1f} y (mean age of mothers on the e0=32 table: {T:.1f} y)")
print("  Calendar logit gain over t years: standard s_gen*t/T; Day's d*s*t/T. Identical iff the published s is read as hazard-scale.")
