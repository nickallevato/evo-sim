"""POST HOC (review pass on R4-GAPS-04-07-02; NOT pre-registered). THROWAWAY research check, not product code.

Written after the three reviews REVIEW-R4-GAPS-{correctness,steelman-day,steelman-critic}.md. Every number here was
requested by a reviewer or by the coordinator after the pre-registered scripts (commit b812741) had run. Nothing
here changes a pre-registered prediction outcome.

Run: research/.venv/bin/python -I research/checks/gap0x_posthoc_review.py > research/checks/results/raw/gap0x_posthoc_review.out
Writes research/checks/results/raw/gap0x_posthoc_review.json. Deterministic.

Inputs and their sources (see the write-up for quotes):
  W&B 2012 Eq. 7 (c = 2, fixed s), Eq. 13 (c = 4, exponential DFE), asymptote R/c, Fig. 4 simulated maximum
    Lambda/R < 3 at Lambda0/R = 1e3 (s = 0.05, R = 1). Fig. 4 by-eye reading Lambda0/R ~ 30-300 for Lambda/R ~ 2.
  F2 grid: results/raw/f2.out. gaps.md H2-hard cap 1,200-8,700 adaptive substitutions per lineage (audit, R4-H2-hard).
  Day: 99%-neutral scenario "200,000 fixations remain required" (Z18165980 line 66); N_e 10,000-33,000 and
    block range 3,200-32,000 (Z23003785 s8.2 line 598; Z18452504 line 318); MITTENS 3.0 achievable 191 (non-mutator)
    to 2,407 (mutator) (A3b); bonobo effective generations 40,000 (Z18441321 line 69).
  Yoo 2025: SDR 327 Mb average per ape lineage (main text); human-lineage SDR h1/h2 147.8/183.6 Mb (SI Table V.24,
    via claim A3x1); satellite units "32 bp AT-rich satellite ... pCht7" and "171 bp alpha-satellite" (main text).
    2-6 bp microsatellite unit: ASSUMPTION (not sourced). SweepFinder2 per-taxon counts 30, 22, 62, 11, 18.
  Kloosterman 2015: 41 validated de novo SVs in 258 children, max 327 kbp, 4.1 kbp per generation (per child).
"""
import itertools
import json
import math
import os
import re

from scipy.optimize import brentq, minimize_scalar

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'results', 'raw')
out = {}


def p(*a):
    print(*a)


# ---------------------------------------------------------------- A. GAP-04
p('# A. GAP-04 (post hoc)')
rows = []
for line in open(os.path.join(RAW, 'f2.out')):
    m = re.match(r'\| 0\.01 \| (\S+) \| ([0-9.]+) \| \d+ \| ([0-9.e-]+) \| [0-9.e-]+ \| [0-9.e-]+ \| ([0-9.]+) \| ([0-9.]+) \|', line)
    if m:
        rows.append(dict(mode=m.group(1), MU=float(m.group(2)), k0=float(m.group(3)), Rint=float(m.group(4)), seR=float(m.group(5))))
for mp in ('1.5', '0.1'):
    rr = [r for r in rows if r['mode'] == mp]
    R = float(mp)
    sse = lambda c: sum(((r['Rint'] - 1 / (1 + c * r['k0'] / R)) / max(r['seR'], 0.005)) ** 2 for r in rr)
    res = minimize_scalar(sse, bounds=(0.01, 20), method='bounded')
    f = lambda c: sse(c) - res.fun - 1
    lo, hi = brentq(f, 0.01, res.x), brentq(f, res.x, 20)
    p('fit c, map %s M: c = %.3f (Delta chi2 = 1 interval %.3f-%.3f, i.e. +/- %.3f); chi2 min %.1f; chi2 at c = 2: %.1f'
      % (mp, res.x, lo, hi, (hi - lo) / 2, res.fun, sse(2.0)))
    out['fit_' + mp] = dict(c=res.x, lo=lo, hi=hi, chi2=res.fun, chi2_c2=sse(2.0))

RS = (35.0, 37.9)
T0 = 252000
reqs = [('Day 2019 15M / 450,000 (not in P6)', 15e6, 450000),
        ('Day 2025 20M / 325,000', 20e6, 325000),
        ('Day 20M / 252,000', 20e6, 252000),
        ('Day 3.0 17.5M / 252,000', 17.5e6, 252000),
        ('Day 205M bp / 252,000 (bp, not events)', 205e6, 252000),
        ('Day 99%-neutral 200,000 / 252,000 (Z18165980 l.66)', 2e5, 252000),
        ('Day 99%-neutral 200,000 / 325,000', 2e5, 325000)]
for e in (3, 4, 5, 6):
    reqs.append(('GAP-01 K_a 1e%d' % e, 10.0 ** e, T0))
for frac in (0.01, 0.05, 0.10, 0.125, 0.25, 0.50, 1.0):
    reqs.append(('adaptive share %.1f%% of 17.5M' % (100 * frac), frac * 17.5e6, T0))
H2 = (1200, 8700)
p('\n| requirement | rate/gen | Lambda/R | x over R/4 (Eq.13 asymptote) | x over R/2 (Eq.7 asymptote) | x over 3R (sim. max at Lambda0/R=1e3) | loss Eq.7 | loss Eq.13 | K / H2-hard cap (1,200-8,700) |')
p('|---|---|---|---|---|---|---|---|---|')
hum = []
for name, K, T in reqs:
    L = K / T
    lr = (L / RS[1], L / RS[0])
    x4 = (L / (RS[1] / 4), L / (RS[0] / 4))
    x2 = (L / (RS[1] / 2), L / (RS[0] / 2))
    x3 = (L / (3 * RS[1]), L / (3 * RS[0]))
    l7 = [2 * L / R for R in RS if L < R / 2]
    l13 = [4 * L / R for R in RS if L < R / 4]
    fmt = lambda v: ('%.2g-%.2g' % (min(v), max(v))) if v else 'above asymptote'
    h2 = (K / H2[1], K / H2[0])
    p('| %s | %.4g | %.3g-%.3g | %.3g-%.3g | %.3g-%.3g | %.3g-%.3g | %s | %s | %.3g-%.3g |' % (
        name, L, *lr, *x4, *x2, *x3, fmt(l7), fmt(l13), *h2))
    hum.append(dict(name=name, K=K, T=T, rate=L, x4=x4, x2=x2, x3=x3, loss7=l7, loss13=l13, h2=h2))
out['human'] = hum
p('\nTwo definitions of the interference "loss" for the K_a rows (R = 35-37.9 M):')
p('  (a) fixed supply: baseline Lambda0 = K/T, realised Lambda = Lambda0/(1 + c Lambda0/R) -> loss 1 - 1/(1 + c Lambda0/R)')
p('  (b) realised rate = K/T: supply must be Lambda0 = Lambda/(1 - c Lambda/R) -> loss 1 - Lambda/Lambda0 = c Lambda/R (columns above; pre-registered P7 definition)')
for name, K, T in [r for r in reqs if 'GAP-01' in r[0] or 'share' in r[0] or '99%' in r[0]]:
    L = K / T
    a7 = [1 - 1 / (1 + 2 * L / R) for R in RS]; a13 = [1 - 1 / (1 + 4 * L / R) for R in RS]
    p('  %s: (a) Eq.7 %.3g-%.3g, Eq.13 %.3g-%.3g' % (name, min(a7), max(a7), min(a13), max(a13)))
for L in (0.7, 3.4):
    p('  gaps.md check, rate %.1f/gen, R = 35: (a) %.3f, (b) %.3f' % (L, 1 - 1 / (1 + 2 * L / 35), 2 * L / 35))
p('\nCrossing adaptive share (fraction of 17.5M per lineage at which each asymptote/ceiling is reached):')
cross = {}
for T in (252000, 325000):
    for lab, mult in (('R/4', 0.25), ('R/2', 0.5), ('3R', 3.0)):
        v = [mult * R * T / 17.5e6 for R in RS]
        cross['%s_T%d' % (lab, T)] = v
        p('  T = %d, %s: %.1f%%-%.1f%% (%.3g-%.3g per lineage)' % (T, lab, 100 * v[0], 100 * v[1], mult * RS[0] * T, mult * RS[1] * T))
out['crossing'] = cross

p('\nR/2 per lineage vs Day MITTENS 3.0 achievable 191-2,407: %.3g-%.3g per lineage = %.0fx-%.0fx' % (
    17.5 * T0, 18.95 * T0, 17.5 * T0 / 2407, 18.95 * T0 / 191))
for s in (0.001, 0.01):
    p('mean log-fitness gain v = Lambda*s: at R/2 (17.5/gen) s=%g -> %.3g/gen; at K_a=1e6 (3.97/gen) -> %.3g/gen' % (s, 17.5 * s, 3.968 * s))

p('\nSupply for Day 17.5M/252,000 (Lambda ~ 69.4/gen, Lambda/R ~ 2 at R = 35): U_tot = 36.5 per haploid genome')
p('Lambda0/R read by eye from W&B Fig. 4 at s = 0.05, R = 1 (sR = 0.05): 30-300 (+/-2x); s- and R/s-dependence NOT tested by W&B.')
p('| N_e | s | no-interference U_b (Lambda/(2Ne*2s)) | U_b, Fig.4 only (finite-map) | U_b x e^{4 Lambda s} (soft-selection variance factor, extrapolated) | share of U_tot (Fig.4 only) | share (with factor) | log-heuristic max Lambda0/R for Lambda/R=2: (Ns)^2 |')
p('|---|---|---|---|---|---|---|---|')
L = 17.5e6 / T0
sup = []
for Ne in (1e4, 3.3e4, 1e5, 2e5):
    for s in (0.001, 0.01):
        base = L / (2 * Ne * 2 * s)
        u_fm = (30 * 35 / (2 * Ne * 2 * s), 300 * 35 / (2 * Ne * 2 * s))
        fac = math.exp(4 * L * s)
        u_ex = (u_fm[0] * fac, u_fm[1] * fac)
        heur = (2 * Ne * s) ** 2
        p('| %g | %g | %.3g | %.3g-%.3g | %.3g-%.3g | %.2g-%.2g | %.2g-%.2g | %.3g |' % (
            Ne, s, base, *u_fm, *u_ex, u_fm[0] / 36.5, u_fm[1] / 36.5, u_ex[0] / 36.5, u_ex[1] / 36.5, heur))
        sup.append(dict(Ne=Ne, s=s, base=base, u_fm=u_fm, u_ex=u_ex))
out['supply'] = sup

p('\nConcurrent active-zone sweeps n_mid = Lambda * ln(81)/s (x up to 2 from W&B Fig. 5, simulated at s = 0.1, Lambda0/R ~ 14.5, R = 1, N = 1e4-1e5)')
conc = []
for name, L in [('R/2, R = 35 M', 17.5), ('R/2, R = 37.9 M', 18.95), ('R/4, R = 35 M', 8.75),
                ('Day 200,000 / 252,000', 2e5 / T0)] + [('K_a 1e%d / 252,000' % e, 10.0 ** e / T0) for e in (3, 4, 5, 6)]:
    for s in (0.001, 0.01):
        n = L * math.log(81) / s
        p('  %s, s = %g: n_mid = %.3g (to %.3g with 2x slowing); x Day 230 = %.3g; sum of s over active loci = %.3g' % (
            name, s, n, 2 * n, n / 230, n * s))
        conc.append(dict(name=name, s=s, n=n))
out['concurrency'] = conc
lam = [smax / math.log(81) for smax in (1.0, 2.0)]
p('Day s6.1 reproductive ceiling (Z18167588 l.60: sum of s over simultaneously segregating loci <= s_max ~ 1.0-2.0):')
p('  active-zone sum of s = Lambda * ln 81 (independent of s) -> Lambda <= %.3f-%.3f/gen -> K <= %.3g-%.3g per lineage at T = 252,000 '
  '(active zone only; counting all segregating loci would lower it; validity of the ceiling is branch H, not tested here)' % (lam[0], lam[1], lam[0] * T0, lam[1] * T0))

# ---------------------------------------------------------------- B. GAP-07
p('\n# B. GAP-07 (post hoc)')
SNVH = 36.5
ind = {'Kloosterman': 1.47, 'Besenbacher': 4.5}
m3 = {k: 17.5e6 * v / SNVH for k, v in ind.items()}
for reading, obs in (('total reading (2.5M/lineage)', 2.5e6), ('per-species reading (5M/lineage)', 5e6)):
    p('Indels, like-for-like M3 (clock-free) vs CSAC observed, %s: observed / M3 = %.2f (Besenbacher) - %.2f (Kloosterman)' % (
        reading, obs / m3['Besenbacher'], obs / m3['Kloosterman']))
p('Indel:SNV ratio: CSAC total reading 5/35 = %.3f; per-species reading 10/35 = %.3f; germline Kloosterman %.3f, Besenbacher %.3f' % (
    5 / 35, 10 / 35, 1.47 / SNVH, 4.5 / SNVH))

# observation-consistent grid
SNV_CI = (36.5 * 1.16 / 1.27, 36.5 * 1.38 / 1.27)
IND_CI = (1.47 * 0.53 / 0.68, 4.5 * 1.9 / 1.5)
SV_CI = (0.065, 0.22)
grid = []
for snv, i, sv, T, na in itertools.product(SNV_CI, IND_CI, SV_CI, (169231, 252000, 325000, 450000), (0, 5e4, 1e5, 1.98e5)):
    eff = T + 2 * na
    grid.append(dict(snv_lin=snv * eff, tot=(snv + i + sv) * eff, T=T, na=na))
ok = [g for g in grid if g['snv_lin'] <= 1.3 * 17.5e6]
mn_all = min(205e6 / g['tot'] for g in grid)
mn_ok = min(205e6 / g['tot'] for g in ok)
p('Grid: %d points; min 205M/events %.2f overall; %d points with predicted SNV <= 1.3 x 17.5M, min %.2f' % (
    len(grid), mn_all, len(ok), mn_ok))
out['gap07_grid'] = dict(n=len(grid), min_all=mn_all, n_ok=len(ok), min_ok=mn_ok)

p('\nRepeat-unit-scale reading of SDR base pairs (events = SDR bp / unit size); totals add 17.5M SNV + 2.5M indel events per lineage')
p('| SDR bp per lineage | unit | unit events | total events | 205M / total |')
p('|---|---|---|---|---|')
ru = []
for lab, bp in (('Yoo human h1/h2 147.8-183.6 Mb (SI T.V.24 via A3x1)', (147.8e6, 183.6e6)), ('Day 187 Mb', (187e6, 187e6)),
                ('Yoo cross-ape average 327 Mb', (327e6, 327e6))):
    for ulab, u in (('171 bp alpha-satellite (Yoo)', 171), ('32 bp pCht7 satellite (Yoo)', 32), ('6 bp microsatellite (ASSUMPTION)', 6), ('2 bp microsatellite (ASSUMPTION)', 2)):
        ev = (bp[0] / u, bp[1] / u)
        tot = (20e6 + ev[0], 20e6 + ev[1])
        p('| %s | %s | %.3g-%.3g | %.3g-%.3g | %.3g-%.3g |' % (lab, ulab, *ev, *tot, 205e6 / tot[1], 205e6 / tot[0]))
        ru.append(dict(sdr=lab, unit=u, events=ev, total=tot))
out['repeat_unit'] = ru
p('(Upper bound: every SDR bp counted as unit-scale events; most SDR sequence is not a tandem array of that unit.)')

tot_kb = 4.1 * 258
p('\nKloosterman SV bp heavy tail: total ~ 4.1 kbp x 258 children = %.0f kbp; the 327 kbp event = %.0f%%; without it %.2f kbp per child -> %.0f Mb per lineage at T = 252,000 (vs %.0f Mb with it)' % (
    tot_kb, 100 * 327 / tot_kb, (tot_kb - 327) / 258, (tot_kb - 327) / 258 / 2 * 1e3 * T0 / 1e6, 2050 * T0 / 1e6))

# ---------------------------------------------------------------- C. GAP-02
p('\n# C. GAP-02 (post hoc)')
E = lambda K, W, T, fs=1.0: K * W / T * fs
p('Day block range (Z18452504 l.318) over 325,000 generations, power 1, f_strong 1:')
p('| K | W = 4,000 (unsourced) | W = 10,000 (Hernandez; N_e = 1e4) | W = 20,000 (unsourced) | W = 33,000 (0.25 x 4 x 33,000; Day N_e upper) |')
p('|---|---|---|---|---|')
dayk = []
for K in (3200, 10000, 32000):
    v = [E(K, W, 325000) for W in (4000, 10000, 20000, 33000)]
    p('| %d | %.3g | %.3g | %.3g | %.3g |' % (K, *v))
    dayk.append(dict(K=K, E=v))
out['day_block'] = dayk

p('\nMinimum detection power p* = 722 / E_detect(power 1) for tension with Akey replicated count (ILLUSTRATIVE: threshold-limited list)')
p('| K_a | f_strong | T | W=4,000 | W=10,000 | W=20,000 |')
p('|---|---|---|---|---|---|')
pstar = []
for K in (1e4, 1e5, 1e6):
    for fs in (1.0, 0.28):
        for T in (252000, 325000):
            v = [722 / E(K, W, T, fs) for W in (4000, 10000, 20000)]
            p('| %g | %.2f | %d | %s |' % (K, fs, T, ' | '.join(('%.2g' % x) if x <= 1 else ('>1 (%.2g)' % x) for x in v)))
            pstar.append(dict(K=K, fs=fs, T=T, p=v))
out['pstar'] = pstar
p('K_a at which E_detect (power 1) = 722, band over W in {4,000, 10,000, 20,000} and T in {252,000, 325,000}:')
for fs in (1.0, 0.28, 0.1):
    ks = [722 * T / W / fs for W in (4000, 10000, 20000) for T in (252000, 325000)]
    p('  f_strong %.2f: %.3g - %.3g' % (fs, min(ks), max(ks)))

yoo = sorted([30, 22, 62, 11, 18])
p('\nSFS-type comparator, Yoo 2025 SweepFinder2 per ape taxon %s (median %d; power-limited: 5 of 10 taxa, n = 11-27, q-value regions merged within 1 Mb)' % (yoo, yoo[2]))
for K in (1e3, 1e4):
    for fs in (1.0, 0.28):
        e = E(K, 10000, 252000, fs)
        p('  K_a %g, f_strong %.2f, W 10,000: E = %.3g = %.2gx median, %.2gx-%.2gx range' % (K, fs, e, e / 22, e / 62, e / 11))

p('\nGenome coverage of detectable completed sweeps (footprint 0.1 or 1 Mb, Day r/s range; non-overlapping upper bound) vs Hernandez "~10% of the human genome"')
for name, K, T in (('Day 3,200', 3200, 325000), ('Day 32,000', 32000, 325000), ('K_a 1e4', 1e4, 252000), ('K_a 1e5', 1e5, 252000), ('K_a 1e6', 1e6, 252000)):
    e = E(K, 10000, T)
    p('  %s (W 10,000, power 1): E = %.3g; coverage %.2g%%-%.2g%% of 3.1 Gb (capped at 100)' % (name, e, min(100, 100 * e * 1e5 / 3.1e9), min(100, 100 * e * 1e6 / 3.1e9)))

p('\nBonobo with Day effective generations 40,000 (d = 0.86): window 20,000 = %.0f%%; E(326,000) = %.3g; with W = 2,000 (10x smaller) E = %.3g vs Yoo 30' % (
    100 * 20000 / 40000, 326000 * 20000 / 40000 if 20000 < 40000 else 326000, 326000 * 2000 / 40000))

json.dump(out, open(os.path.join(RAW, 'gap0x_posthoc_review.json'), 'w'), indent=1, default=float)
