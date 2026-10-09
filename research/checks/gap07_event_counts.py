"""GAP-07: expected indel and structural-variant EVENT counts per lineage since the human-chimp split, from
published germline rates with k = mu; compared with Day's base-pair totals (410M / 205M) and observed counts.
THROWAWAY research check (not product code).

Run: research/.venv/bin/python -I research/checks/gap07_event_counts.py > research/checks/results/raw/gap07.out
Writes research/checks/results/raw/gap07.json. Deterministic.

SOURCES (all read in full text for this check; downloads under sources/raw/, gitignored):
  SNV  Kong 2012 (corpus txt/Kong2012.txt, abstract): 1.20e-8 per nucleotide per generation.
       Besenbacher 2015 (Nat Commun 6:5969, PMC4309431): 1.27e-8 (95% CI 1.16e-8 to 1.38e-8) per nt per
       generation, "~73 expected de novo SNVs in each newborn" -> 36.5 per haploid genome.
  Indel Besenbacher 2015: 1.5e-9 (95% CI 1.2e-9 to 1.9e-9) per nt per generation, "~9 autosomal de novo indels
       in each newborn" -> 4.5 per haploid genome.
       Kloosterman 2015 (Genome Res 25:792, PMC4448676): "2.94 indels (1-20 bp) ... per generation" (per child)
       = "0.68 x 10^-9 indel (1-20 bp) per base per generation" -> 1.47 per haploid genome; prior estimates
       "range from 0.53 to 1.5 x 10^-9 per base per generation".
  SV   Kloosterman 2015: "0.08 SVs (>20 bp) per haploid genome (or 0.16 SVs per generation)"; "De novo structural
       changes affect on average 4.1 kbp of genomic sequence ... per generation" (per child -> 2.05 kbp per
       haploid genome; dominated by rare large events, max 327 kbp).
       Belyeu 2021 (AJHG 108:597, PMC8059337): "at least 0.160 events per genome" (lower bound) -> 0.080/haploid.
       Collins 2020 (Nature 581:444, PMC7334194): Watterson projection "0.29 de novo SVs (95% CI 0.13-0.44) per
       generation", "roughly one new SV every 2-8 live births"; "certainly underestimates"; SV size is "a key
       determinant of selection against most SVs" -> 0.145 (0.065-0.22) per haploid genome.
  Observed (corpus): CSAC 2005 (txt/CSAC2005.txt) p.73: "~32 Mb of human-specific sequence and ~35 Mb of
       chimpanzee-specific sequence, contained in ~5 million events in each species" and, same page, "the number of
       indel events is far fewer than the number of substitution events (~5 million compared with ~35 million,
       respectively)" -> two readings: 5M indel events per lineage, or 5M total (2.5M per lineage). ~35M SNV
       differences total (both lineages, incl. 14-22% polymorphism, A3c). Species-specific euchromatic sequence
       "40-45 Mb" each (p.73).
       Yoo 2025 (txt/Yoo2025.txt, A3x1): "an average of 327 Mb of sequence (10%) per ape lineage" in SDRs.
  Day: 410M "genomic differences"/"base pairs" total, 205M per lineage (A3a, MITTENS 3.0 / blog 2026-04-28);
       17.5M SNV-only per lineage (A3b); generations 252,000 (A1, 3.0) and 325,000 (2025), range 169,231-450,000.
  Ancestral polymorphism: per-lineage expected differences = mu (T + 2 N_anc) for a diploid ancestral population
       (coalescent; textbook, labelled `derived:`); N_anc sensitivity {0, 5e4, 1e5, 1.98e5}; 1.98e5 is Yoo 2025's
       "human-chimpanzee-bonobo ancestral population size (average Ne = 198,000)".

THREE METHODS
  M1 rate x T (post-split only, k = mu):        E = r_hap * T
  M2 rate x (T + 2 N_anc):                       E = r_hap * (T + 2 N_anc)
  M3 calibrated to observed SNV divergence:      E = S_obs_lineage * r_class / r_SNV   (clock-free; no T, no N_anc)
     with S_obs_lineage = 17.5M (Day's SNV-only basis = CSAC 35M / 2).

PRE-REGISTERED PREDICTIONS (written before running; gaps.md GAP-07 already gave M1 indel 0.37-1.17M, SV 2.0-7.3e4
and total 1.04-1.13x SNV at T = 252,000, so P1 is a re-derivation, not blind):
 P1 M1 at T = 252,000: total events per lineage (SNV + indel + SV) in 9-13M; ratio to SNVs in [1.03, 1.15].
 P2 Day's 205M exceeds every event estimate at Day's own T (252,000 and 325,000) without the ancestral term
    (M1) and with M3 by >= 8x; and by >= 4x everywhere on the full grid (mu CIs, T 169,231-450,000, N_anc up to
    1.98e5). Falsifier: any grid point < 4x.
 P3 SV events per lineage (M1, T = 252,000) in 1.5e4-6e4; SV base pairs under k = mu (2.05 kbp per haploid
    genome per generation x T) within 3x of Yoo's 327 Mb per lineage (i.e. 109-981 Mb).
    Falsifier: outside that band. (Under k = mu this is an UPPER bound for bp, since large SVs are selected against.)
 P4 Rate-based indel events (M1 and M3) fall below CSAC's observed per-lineage indel events under BOTH readings
    (2.5M and 5M). Falsifier: any rate-based value >= 2.5M at T = 252,000.
 P5 Sensitivity: across mu CIs and T range (M1), total events per lineage stay < 25M (i.e. < 205M/8).
"""
import itertools
import json
import os

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'results', 'raw')

# per haploid genome per generation (events), with sourced ranges
SNV = dict(Kong2012=1.20e-8 * 36.5 / 1.27e-8, Besenbacher2015=36.5)          # Kong scaled to Besenbacher's accessible genome
SNV_CI = (36.5 * 1.16 / 1.27, 36.5 * 1.38 / 1.27)
INDEL = dict(Kloosterman2015=1.47, Besenbacher2015=4.5)
INDEL_CI = (1.47 * 0.53 / 0.68, 4.5 * 1.9 / 1.5)                              # 0.53e-9 (Kloosterman's prior range low) .. 1.9e-9 (Besenbacher CI high)
SV = dict(Kloosterman2015=0.08, Belyeu2021=0.080, Collins2020=0.145)
SV_CI = (0.065, 0.22)
SV_BP_PER_HAP = 2050.0                                                       # Kloosterman 4.1 kbp per child / 2
T_DAY = (252000, 325000)
T_RANGE = (169231, 450000)
NANC = (0, 5e4, 1e5, 1.98e5)
S_OBS_LIN = 17.5e6
DAY_BP_LIN = 205e6
CSAC_INDEL_LIN = (2.5e6, 5e6)
YOO_SDR_LIN = 327e6


def main():
    out = {}
    r, T, Na, Sobs, rs = sp.symbols('r T N_anc S_obs r_SNV', positive=True)
    M1 = r * T
    M2 = r * (T + 2 * Na)
    M3 = Sobs * r / rs
    print('Symbolic: M1 =', M1, '; M2 =', M2, '; M3 =', M3)
    print('Sensitivity (elasticities): dlnM1/dln r =', sp.simplify(sp.diff(M1, r) * r / M1),
          '; dlnM1/dln T =', sp.simplify(sp.diff(M1, T) * T / M1),
          '; dlnM2/dln T =', sp.simplify(sp.diff(M2, T) * T / M2))
    f1 = sp.lambdify((r, T), M1)
    f2 = sp.lambdify((r, T, Na), M2)
    f3 = sp.lambdify((Sobs, r, rs), M3)

    print('\n## A. Point estimates per lineage, T = 252,000 (M1) and calibrated (M3)')
    print('| class | source | per haploid genome per gen | M1 events (T=252k) | M1 (T=325k) | M3 events (calibrated to 17.5M SNV) |')
    print('|---|---|---|---|---|---|')
    pts = []
    for cls, dct in (('SNV', SNV), ('indel', INDEL), ('SV', SV)):
        for src, val in dct.items():
            e1 = f1(val, 252000); e1b = f1(val, 325000); e3 = f3(S_OBS_LIN, val, SNV['Besenbacher2015'])
            pts.append(dict(cls=cls, src=src, r=val, M1_252k=e1, M1_325k=e1b, M3=e3))
            print('| %s | %s | %.3g | %.3g | %.3g | %.3g |' % (cls, src, val, e1, e1b, e3))
    out['points'] = pts

    def totals(snv, ind, sv, Tg, nanc=0.0):
        return f2(snv, Tg, nanc) + f2(ind, Tg, nanc) + f2(sv, Tg, nanc)

    print('\n## B. Totals per lineage (SNV + indel + SV events)')
    lo1 = totals(SNV['Besenbacher2015'], INDEL['Kloosterman2015'], SV['Kloosterman2015'], 252000)
    hi1 = totals(SNV['Besenbacher2015'], INDEL['Besenbacher2015'], SV['Collins2020'], 252000)
    snv1 = f1(SNV['Besenbacher2015'], 252000)
    print('M1 T=252k: %.4g - %.4g events; SNV %.4g; ratio to SNV %.3f - %.3f; 205M / total = %.1f - %.1f' % (
        lo1, hi1, snv1, lo1 / snv1, hi1 / snv1, DAY_BP_LIN / hi1, DAY_BP_LIN / lo1))
    lo3 = S_OBS_LIN * (1 + INDEL['Kloosterman2015'] / 36.5 + SV['Kloosterman2015'] / 36.5)
    hi3 = S_OBS_LIN * (1 + INDEL['Besenbacher2015'] / 36.5 + SV['Collins2020'] / 36.5)
    print('M3 calibrated: %.4g - %.4g events; 205M / total = %.1f - %.1f' % (lo3, hi3, DAY_BP_LIN / hi3, DAY_BP_LIN / lo3))
    obs_lo = S_OBS_LIN + CSAC_INDEL_LIN[0] + 1140 / 2
    obs_hi = S_OBS_LIN + CSAC_INDEL_LIN[1] + 1140 / 2
    print('Observed-count basis (CSAC SNV 17.5M + indel 2.5M or 5M per lineage + inversions): %.4g - %.4g; 205M / = %.1f - %.1f' % (
        obs_lo, obs_hi, DAY_BP_LIN / obs_hi, DAY_BP_LIN / obs_lo))
    out['totals'] = dict(M1_252k=(lo1, hi1), M1_ratio_snv=(lo1 / snv1, hi1 / snv1), M3=(lo3, hi3), observed=(obs_lo, obs_hi))

    print('\n## C. Full sensitivity grid (M2 incl. M1 at N_anc = 0): SNV CI x indel CI x SV CI x T x N_anc')
    grid = []
    for snv, ind, sv, Tg, na in itertools.product(SNV_CI, INDEL_CI, SV_CI, (169231, 252000, 325000, 450000), NANC):
        tot = totals(snv, ind, sv, Tg, na)
        grid.append(dict(snv=snv, indel=ind, sv=sv, T=Tg, N_anc=na, total=tot, day_over=DAY_BP_LIN / tot))
    mn = min(grid, key=lambda g: g['day_over'])
    mx = max(grid, key=lambda g: g['day_over'])
    print('205M / events: min %.2f at %s; max %.1f at %s' % (mn['day_over'], {k: mn[k] for k in ('snv', 'indel', 'sv', 'T', 'N_anc')},
                                                           mx['day_over'], {k: mx[k] for k in ('snv', 'indel', 'sv', 'T', 'N_anc')}))
    print('| T | N_anc | total events per lineage (min-max over rate CIs) | 205M / total (min-max) |')
    print('|---|---|---|---|')
    for Tg in (169231, 252000, 325000, 450000):
        for na in NANC:
            g = [x for x in grid if x['T'] == Tg and x['N_anc'] == na]
            print('| %d | %g | %.3g - %.3g | %.1f - %.1f |' % (Tg, na, min(x['total'] for x in g), max(x['total'] for x in g),
                                                           min(x['day_over'] for x in g), max(x['day_over'] for x in g)))
    out['grid_min'] = mn; out['grid_max'] = mx

    print('\n## D. Indel and SV detail')
    ind_m1 = [f1(v, 252000) for v in INDEL.values()]
    ind_m3 = [f3(S_OBS_LIN, v, 36.5) for v in INDEL.values()]
    sv_m1 = [f1(v, 252000) for v in (SV_CI[0], SV['Kloosterman2015'], SV['Collins2020'], SV_CI[1])]
    sv_bp = {Tg: SV_BP_PER_HAP * Tg for Tg in (169231, 252000, 325000, 450000)}
    print('indel events per lineage: M1 %.3g - %.3g; M3 %.3g - %.3g; CSAC observed 2.5M (total reading) or 5M (per-species reading)' % (
        min(ind_m1), max(ind_m1), min(ind_m3), max(ind_m3)))
    print('  observed / rate-based: %.1f - %.1f' % (CSAC_INDEL_LIN[0] / max(ind_m1 + ind_m3), CSAC_INDEL_LIN[1] / min(ind_m1 + ind_m3)))
    print('SV events per lineage (M1, T=252k): CI-low %.3g, Kloosterman %.3g, Collins %.3g, CI-high %.3g' % tuple(sv_m1))
    print('SV bp per lineage if k = mu (2.05 kbp/haploid/gen x T): ' + ', '.join('T=%d: %.3g Mb' % (k, v / 1e6) for k, v in sv_bp.items()))
    print('  Yoo SDR 327 Mb per lineage; CSAC species-specific indel sequence 40-45 Mb per species.')
    print('  mean bp per de novo SV (Kloosterman 4.1 kbp / 0.16) = %.3g kbp; events needed for 327 Mb at that mean = %.3g' % (
        4100 / 0.16 / 1e3, YOO_SDR_LIN / (4100 / 0.16)))
    out['indel'] = dict(M1=ind_m1, M3=ind_m3); out['sv'] = dict(M1=sv_m1, bp=sv_bp)

    preds = {}
    preds['P1'] = (9e6 <= lo1 and hi1 <= 13e6 and 1.03 <= lo1 / snv1 and hi1 / snv1 <= 1.15)
    m1_day = [DAY_BP_LIN / totals(snv, ind, sv, Tg) for snv, ind, sv, Tg in itertools.product(SNV_CI, INDEL_CI, SV_CI, T_DAY)]
    preds['P2'] = (min(m1_day) >= 8 and DAY_BP_LIN / hi3 >= 8 and mn['day_over'] >= 4)
    preds['P2_detail'] = dict(min_M1_dayT=min(m1_day), M3_min=DAY_BP_LIN / hi3, grid_min=mn['day_over'])
    preds['P3'] = (1.5e4 <= min(sv_m1) and max(sv_m1) <= 6e4 and 109e6 <= sv_bp[252000] <= 981e6)
    preds['P4'] = max(ind_m1 + ind_m3) < CSAC_INDEL_LIN[0]
    p5 = [totals(snv, ind, sv, Tg) for snv, ind, sv, Tg in itertools.product(SNV_CI, INDEL_CI, SV_CI, T_RANGE)]
    preds['P5'] = max(p5) < 25e6
    preds['P5_detail'] = dict(max_total_M1=max(p5))
    print('\n## Predictions')
    for k, v in preds.items():
        print(k, 'HELD' if v is True else ('FAILED' if v is False else v))
    out['predictions'] = preds
    json.dump(out, open(os.path.join(RAW, 'gap07.json'), 'w'), indent=1, default=float)


if __name__ == '__main__':
    main()
