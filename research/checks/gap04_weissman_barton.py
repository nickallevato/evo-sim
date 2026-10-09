"""GAP-04: Weissman & Barton 2012 finite-map limit on adaptive substitution, vs the F2 grid and at human scale.
THROWAWAY research check (not product code).

Run: research/.venv/bin/python -I research/checks/gap04_weissman_barton.py > research/checks/results/raw/gap04.out
Writes research/checks/results/raw/gap04.json. Deterministic (no simulation, no RNG).

SOURCE (read before writing this file; PDF from journals.plos.org, stored under sources/raw/, gitignored):
Weissman DB, Barton NH (2012) PLoS Genet 8(6):e1002740, doi:10.1371/journal.pgen.1002740. Model: N haploid
individuals, genomic beneficial rate U, advantage s, linear map of total length R Morgans (Table 1).
  * Lambda0 = 2 N U <s>                                         (p.2, "baseline rate"; Fig. 4 caption)
  * Eq. (1), unlinked loci, polygamous Wright-Fisher: Dz = v = (1/4) W(4 v0), W = Lambert/product-log,
    v0 = 2 N U <s log(1+s)> ~ s * Lambda0                        (p.3)
  * Eq. (6)-(7), linear map, additive approximation: P ~ 2s(1 - 2 Z Lambda/R), Z = 1.05 (taken as 1);
    Lambda ~ Lambda0 / (1 + 2 Lambda0/R)                        (p.7)
  * Eq. (8), adds loosely linked loci: v/v0 ~ (1 - 2v/(sR)) e^{-4v}, v = Lambda*s (p.7)
  * Eq. (13), exponential DFE: Lambda ~ Lambda0 / (1 + 4 Lambda0/R)  (p.12)
  * "In the limit of a very large density of incoming mutations, Lambda0/R >> 1, Eqs. (7) and (8) imply that
    Lambda tends to an 'upper limit' of R/2" (p.8). Fig. 4 caption (p.7): simulated Lambda/R "continue to
    increase above Eq. (8)'s 'upper limit' of 0.5, they do so only very slowly, remaining <3 even for
    Lambda0/R = 10^3" (s = 0.05, R = 1, N = 1e2..1e6). p.8: back-of-envelope "Lambda/R should grow at least as
    fast as ~log(Lambda0/R)/log(Ns)".
NOTE on the brief: the brief described the cap as "R times a log factor in N*U_b and s". The paper's main cap
(Eq. 7/8) is R/2 with NO dependence on N, U or s; the log factor appears only in the back-of-envelope lower
bound for growth ABOVE R/2. Both are evaluated here.

Mapping to F2 (wf_f2.py): M = 2N = 2000 haploid gene copies = W&B's N; U = 2N*U_b / M per copy; Lambda0 = the
F2 'indep' rate k0 = M*U*u(s) (Kimura u ~ 1.98 s at s = 0.01; W&B use 2s; 1% difference, stated). F2 map modes
R = 0.1 and 1.5 M use Poisson(R) crossovers with obligate outcrossing between two fitness-chosen parents
(polygamous WF in W&B's sense). F2 values are the post-fix rerun in results/raw/f2.out (= R4-F2-A.md table).
Mapping to humans: diploid N_e individuals -> 2 N_e haploid copies; U_b per haploid genome; additive s per copy;
Lambda0 = 2 N_e U_b * 2s. Map length R = 35-38 M sex-averaged incl. X (gaps.md GAP-04; Kong 2002 3,615 cM and
Matise 2007 3,790 cM, both read via secondary sources per the ledger). Total mutation rate per haploid genome
U_tot ~ 36.5 (Besenbacher 2015: "~73 expected de novo SNVs in each newborn", PMC4309431) used only as a
feasibility yardstick for the beneficial supply.

PRE-REGISTERED PREDICTIONS (written before running; values already in gaps.md for two F2 cells (0.54 at 1.5 M,
0.07 at 0.1 M for 2N*U_b = 32) were known, so P2/P3 are not blind for those two cells):
 P1 free recombination: Eq. (1) predicts the five F2 'free' R_int within 0.03 absolute.
    Falsifier: any cell off by > 0.03 (beyond 2 SE).
 P2 map 1.5 M (Lambda0/R <= 0.42): Eq. (7) predicts R_int within 15% relative in all five cells.
    Falsifier: any cell off by > 15%.
 P3 map 0.1 M (R/s = 10, where W&B Fig. 3 caption says Eq. (8) "slightly overestimates the amount of
    interference"): Eq. (7) UNDER-predicts R_int (too much interference) at 2N*U_b >= 8 (Lambda0/R >= 1.6), by
    >= 1.5x at 2N*U_b = 32; and the observed rate at 2N*U_b = 32 EXCEEDS the R/2 asymptote.
    Falsifier: Eq. (7) within 20% of F2 at 2N*U_b = 32, or observed rate < R/2.
 P4 clonal: out of domain (W&B need R >> s). Eq. (7) with R = 0 gives Lambda = 0, which F2 clonal (rate > 0)
    trivially contradicts; recorded as 'not applicable', not as a test of W&B.
 P5 fitted coefficient c in Lambda = Lambda0/(1 + c Lambda0/R): c(1.5 M) within [1.5, 4] (W&B: 2 fixed s,
    4 exponential DFE); c(0.1 M) < 2.
 P6 human, Day's all-fixations readings (17.5M or 20M per lineage over 252,000 or 325,000 generations): the
    required rate exceeds the R/2 asymptote by 3x-5x (R = 35-38 M); it is BELOW the simulated envelope
    Lambda/R < 3 (factor < 1 against 3R). 205M (bp, not events) exceeds R/2 by > 40x.
 P7 human, GAP-01 adaptive range 1e3-1e6 per lineage over 252,000 generations: rate / (R/2) between 2e-4 and
    0.25; interference reduction (1 - Lambda/Lambda0, Eq. 7) < 0.1% at 1e3 and < 25% at 1e6.
 P8 supply feasibility: for the all-fixations reading at 17.5M/252,000, reaching Lambda/R ~ 2 needs (reading
    Fig. 4 by eye) Lambda0/R ~ 30-300, times e^{4 Lambda s} for loosely linked loci (Eq. 8 factor); at
    N_e = 1e4 and every s in {1e-3, 1e-2, 1e-1} the implied U_b per haploid genome is >= 50% of U_tot.
    Falsifier: any s with U_b < 10% of U_tot. (Fig. 4 reading is approximate, +/- 2x; the e^{-4v} factor is
    W&B's for unlinked loci and was checked by them in simulation only for sR << 1 and for complete recombination.)
"""
import json
import math
import os
import re

import numpy as np
from scipy.optimize import brentq, minimize_scalar
from scipy.special import lambertw

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'results', 'raw')


def eq1_free(L0, s):
    """W&B Eq. (1): v = W(4 v0)/4, v0 = s*L0 (s small) -> Lambda = v/s."""
    v0 = s * L0
    return float(np.real(lambertw(4 * v0))) / 4 / s


def eq7(L0, R, c=2.0):
    return L0 / (1 + c * L0 / R)


def eq8(L0, R, s):
    """Solve L/L0 = (1 - 2L/R) exp(-4 L s) for L in (0, min(L0, R/2))."""
    f = lambda L: L - L0 * (1 - 2 * L / R) * math.exp(-4 * L * s)
    hi = min(L0, R / 2) * (1 - 1e-12)
    return brentq(f, 0.0, hi) if f(hi) > 0 else hi


def eq8_inverse(L, R, s):
    """Lambda0 needed for realized Lambda (only defined for L < R/2)."""
    if L >= R / 2:
        return float('inf')
    return L / ((1 - 2 * L / R) * math.exp(-4 * L * s))


def load_f2():
    rows = []
    for line in open(os.path.join(RAW, 'f2.out')):
        m = re.match(r'\| ([0-9.]+) \| (\S+) \| ([0-9.]+) \| \d+ \| ([0-9.e-]+) \| ([0-9.e-]+) \| ([0-9.e-]+) \| ([0-9.]+) \| ([0-9.]+) \| ([0-9.]+) \|', line)
        if m:
            s, mode, MU, k0, rate, se, Rint, seR, nmid = m.groups()
            rows.append(dict(s=float(s), mode=mode, MU=float(MU), k0=float(k0), rate=float(rate), se=float(se),
                             Rint=float(Rint), seR=float(seR), n_mid=float(nmid)))
    return rows


def main():
    out = {}
    f2 = load_f2()
    print('## A. W&B formulas vs the F2 grid (s = 0.01, N = M = 2000 haploid copies)')
    print('| map | 2N*U_b | Lambda0 | Lambda0/R | F2 R_int (SE) | Eq7 | Eq8 | Eq13 | Eq1(free) | F2/Eq7 | F2 rate / (R/2) |')
    print('|---|---|---|---|---|---|---|---|---|---|---|')
    tab = []
    for r in f2:
        if r['s'] != 0.01:
            continue
        L0 = r['k0']
        row = dict(r)
        if r['mode'] in ('0.1', '1.5'):
            R = float(r['mode'])
            row.update(R=R, x=L0 / R, eq7=eq7(L0, R) / L0, eq8=eq8(L0, R, 0.01) / L0, eq13=eq7(L0, R, 4.0) / L0,
                       eq1=None, rate_over_halfR=r['rate'] / (R / 2))
            row['ratio7'] = r['Rint'] / row['eq7']
            print('| %s M | %g | %.4g | %.3g | %.3f (%.3f) | %.3f | %.3f | %.3f | - | %.2f | %.2f |' % (
                r['mode'], r['MU'], L0, row['x'], r['Rint'], r['seR'], row['eq7'], row['eq8'], row['eq13'],
                row['ratio7'], row['rate_over_halfR']))
        elif r['mode'] == 'free':
            row.update(R=None, eq1=eq1_free(L0, 0.01) / L0)
            print('| free | %g | %.4g | - | %.3f (%.3f) | - | - | - | %.4f | - | - |' % (
                r['MU'], L0, r['Rint'], r['seR'], row['eq1']))
        else:
            row.update(R=0.0)
            print('| clonal | %g | %.4g | inf | %.3f (%.3f) | 0 (R=0) | out of domain | - | - | - | - |' % (
                r['MU'], L0, r['Rint'], r['seR']))
        tab.append(row)
    out['f2_table'] = tab

    # fit c per map
    fits = {}
    for mp in ('0.1', '1.5'):
        rr = [t for t in tab if t['mode'] == mp]
        R = float(mp)

        def sse(c):
            return sum(((t['Rint'] - 1 / (1 + c * t['k0'] / R)) / max(t['seR'], 0.005)) ** 2 for t in rr)
        res = minimize_scalar(sse, bounds=(0.01, 20), method='bounded')
        fits[mp] = dict(c=res.x, chi2=res.fun, n=len(rr))
        print('fit Lambda = Lambda0/(1 + c Lambda0/R), map %s M: c = %.3f (chi2 %.1f on %d cells)' % (mp, res.x, res.fun, len(rr)))
    out['fit_c'] = fits

    # predictions P1-P5
    preds = {}
    fr = [t for t in tab if t['mode'] == 'free']
    preds['P1'] = all(abs(t['Rint'] - t['eq1']) <= 0.03 for t in fr)
    m15 = [t for t in tab if t['mode'] == '1.5']
    preds['P2'] = all(abs(t['ratio7'] - 1) <= 0.15 for t in m15)
    m01 = {t['MU']: t for t in tab if t['mode'] == '0.1'}
    preds['P3'] = (all(m01[mu]['ratio7'] > 1 for mu in (8, 32)) and m01[32]['ratio7'] >= 1.5
                   and m01[32]['rate_over_halfR'] > 1)
    preds['P5'] = (1.5 <= fits['1.5']['c'] <= 4) and fits['0.1']['c'] < 2
    print('max |F2 - Eq1| free = %.4f; max |F2/Eq7 - 1| at 1.5 M = %.3f; F2/Eq7 at 0.1 M: %s' % (
        max(abs(t['Rint'] - t['eq1']) for t in fr), max(abs(t['ratio7'] - 1) for t in m15),
        ', '.join('%g: %.2f' % (mu, m01[mu]['ratio7']) for mu in sorted(m01))))

    print('\n## B. Human scale')
    Rs = [35.0, 36.15, 37.9]
    reqs = [('Day 2019: 15M / 450,000', 15e6, 450000),
            ('Day 2025: 20M / 325,000', 20e6, 325000),
            ('Day 20M / 252,000', 20e6, 252000),
            ('Day 3.0 SNV-only: 17.5M / 252,000', 17.5e6, 252000),
            ('Day 3.0 headline: 205M (bp) / 252,000', 205e6, 252000)]
    reqs += [('GAP-01 K_a = 1e%d / 252,000' % e, 10.0 ** e, 252000) for e in (3, 4, 5, 6)]
    print('| requirement | rate/gen | Lambda/R (R=35-37.9) | x over R/2 | x over sim. envelope 3R | Eq7 interference loss (1-Lambda/Lambda0) |')
    print('|---|---|---|---|---|---|')
    hum = []
    for name, K, T in reqs:
        L = K / T
        xs_half = [L / (R / 2) for R in Rs]
        xs_env = [L / (3 * R) for R in Rs]
        losses = []
        for R in Rs:
            if L < R / 2:
                L0 = L / (1 - 2 * L / R)
                losses.append(1 - L / L0)
        loss_s = ('%.2g-%.2g' % (min(losses), max(losses))) if losses else 'n/a (above R/2)'
        print('| %s | %.4g | %.3g-%.3g | %.3g-%.3g | %.3g-%.3g | %s |' % (
            name, L, L / Rs[-1], L / Rs[0], min(xs_half), max(xs_half), min(xs_env), max(xs_env), loss_s))
        hum.append(dict(name=name, K=K, T=T, rate=L, x_half=xs_half, x_env=xs_env, loss=losses))
    out['human'] = hum
    d = {h['name']: h for h in hum}
    allfix = [d['Day 2025: 20M / 325,000'], d['Day 20M / 252,000'], d['Day 3.0 SNV-only: 17.5M / 252,000']]
    preds['P6'] = (all(3 <= min(h['x_half']) and max(h['x_half']) <= 5 for h in allfix)
                   and all(max(h['x_env']) < 1 for h in allfix)
                   and min(d['Day 3.0 headline: 205M (bp) / 252,000']['x_half']) > 40)
    g1 = [d['GAP-01 K_a = 1e%d / 252,000' % e] for e in (3, 6)]
    preds['P7'] = (min(g1[0]['x_half']) >= 2e-4 and max(g1[1]['x_half']) <= 0.25
                   and max(g1[0]['loss']) < 1e-3 and max(g1[1]['loss']) < 0.25)

    print('\n## C. Beneficial supply needed (Lambda0 = 2 N_e U_b 2s; U_tot ~ 36.5 per haploid genome)')
    Utot = 36.5
    print('| target | N_e | s | Lambda0 needed | U_b per haploid genome | U_b / U_tot |')
    print('|---|---|---|---|---|---|')
    sup = []
    R = 35.0
    for name, K, T in [('Day 17.5M / 252,000 (Lambda/R ~ 2; Fig. 4 by eye Lambda0/R ~ 30-300)', 17.5e6, 252000)]:
        L = K / T
        for Ne in (1e4, 1e5):
            for s in (1e-3, 1e-2, 1e-1):
                lo, hi = 30 * R * math.exp(4 * L * s), 300 * R * math.exp(4 * L * s)
                ub = (lo / (2 * Ne * 2 * s), hi / (2 * Ne * 2 * s))
                print('| %s | %g | %g | %.3g-%.3g | %.3g-%.3g | %.3g-%.3g |' % (name, Ne, s, lo, hi, ub[0], ub[1], ub[0] / Utot, ub[1] / Utot))
                sup.append(dict(target=name, Ne=Ne, s=s, L0=(lo, hi), Ub=ub, frac=(ub[0] / Utot, ub[1] / Utot)))
    for e in (3, 4, 5, 6):
        L = 10.0 ** e / 252000
        for Ne in (1e4,):
            for s in (1e-3, 1e-2):
                L0 = eq8_inverse(L, R, s)
                ub = L0 / (2 * Ne * 2 * s)
                print('| GAP-01 1e%d / 252,000 (Eq. 8 inverse) | %g | %g | %.3g | %.3g | %.3g |' % (e, Ne, s, L0, ub, ub / Utot))
                sup.append(dict(target='GAP-01 1e%d' % e, Ne=Ne, s=s, L0=L0, Ub=ub, frac=ub / Utot))
    out['supply'] = sup
    day_ne4 = [x for x in sup if x['target'].startswith('Day') and x['Ne'] == 1e4]
    preds['P8'] = all(x['frac'][0] >= 0.5 for x in day_ne4)
    preds['P8_falsifier_hit'] = any(x['frac'][0] < 0.1 for x in day_ne4)

    print('\n## D. Back-of-envelope growth above R/2: Lambda/R >~ log(Lambda0/R)/log(N s) (W&B p.8)')
    for Ne in (1e4, 1e5):
        for s in (1e-3, 1e-2):
            for x in (10, 100, 1000):
                lb = math.log(x) / math.log(2 * Ne * s) if 2 * Ne * s > 1 else float('nan')
                print('N(haploid copies) = %g, s = %g, Lambda0/R = %g: lower bound Lambda/R >= %.2f' % (2 * Ne, s, x, lb))

    print('\n## Predictions')
    for k, v in preds.items():
        # cosmetic print fix (review pass, after the main run; prediction logic unchanged): numpy bools printed
        # as 'True', and a False falsifier flag printed as 'FAILED'
        if k.endswith('_falsifier_hit'):
            print(k, 'hit' if bool(v) else 'not hit')
        elif isinstance(v, (bool, np.bool_)):
            print(k, 'HELD' if v else 'FAILED')
        else:
            print(k, v)
    out['predictions'] = preds
    json.dump(out, open(os.path.join(RAW, 'gap04.json'), 'w'), indent=1, default=float)


if __name__ == '__main__':
    main()
