"""GAP-02: how many completed sweeps should scans detect per lineage, given a detection window, vs Day's
"sweep signatures absent / scans would be saturated" argument. THROWAWAY research check (not product code).

Run: research/.venv/bin/python -I research/checks/gap02_sweep_window.py > research/checks/results/raw/gap02.out
Writes research/checks/results/raw/gap02.json. Deterministic.

CLAIMS (verbatim, sources/raw/day):
  Z18452504 (The Universal Failure of Fixation) s4.3(4), extracted lines 325-331: "If 3,200+ sweeps occurred in the
  human lineage over 325,000 generations, approximately one sweep completes every 100 generations. ... Scans for
  positive selection in humans (Voight et al. 2006; Sabeti et al. 2007; Pickrell et al. 2009) identify dozens to
  hundreds of candidate sweep regions-not thousands. If 3,200+ sweeps had occurred, selection scans would be
  saturated with signals. They are not."
  Z18441321 (The Pan Paradox) s3.1 "Third", line 119: "If 326,000 loci fixed by selection in bonobos over 930,000
  years, the entire genome should be a mosaic of overlapping sweep signatures." (46,500 generations at 20 y,
  line 69; "N_e ~ 20,000", line 123.)

SOURCES (read for this check; downloads under sources/raw/, gitignored):
  Hernandez et al. 2011, Science 331:920 (PMC3669691, author manuscript): "In humans, the effects of sweeps are
    expected to persist for approximately 10,000 generations or about 250,000 years (4)" [ref 4 = Przeworski 2002];
    "approximately 5% of human-specific substitutions could have left a detectable sweep in their wake (i.e., have
    occurred in the past 250,000 years)"; "even if only 10% of human-specific amino acid substitutions were strongly
    favored ... there should be a significant decrease in the diversity levels" (not seen); "over 2000 genes as
    potential targets of positive selection" (ref 2 = Akey 2009); "~10% of the human genome ... affected by linkage
    to recent sweeps (e.g., (5))".
  Przeworski 2002, Genetics 160:1179 (PMC1462030): abstract only (full text is a scanned PDF behind a bot check):
    high-frequency derived alleles and LD "do not persist long after the sweep ends". No number read.
    The brief's 0.1-0.25 x 4N_e: 0.25 x 4N_e = 10,000 at N_e = 1e4 matches Hernandez; the 0.1 x 4N_e lower end is
    NOT sourced here and is used only as a sensitivity value (labelled).
  Voight et al. 2006, PLoS Biol 4:e72 (PMC1382018): iHS scan "in favor of variants that have not yet reached
    fixation"; "the strongest ~250 signals of recent selection in each population"; candidates = 100-kb windows "in
    the highest 1% of the empirical distribution"; "iHS has reduced power for alleles near fixation".
  Sabeti et al. 2007, Nature 449:913 (PMC2687721): "more than 300 strong candidate regions", 22 strongest; XP-EHH
    "detects selected alleles that have risen to near fixation in one but not all populations".
  Pickrell et al. 2009, Genome Res 19:826 (PMC2675971): outlier (1% tail) approach; no total count given.
  Akey 2009, Genome Res 19:711 (PMC3647533): across nine scans "5110 distinct regions were identified in one or more
    study", "~14% of the genome"; "only 722 regions (14.1%) were identified in two or more studies"; scans "only
    have reasonable power to detect fairly strong selective effects (4Nes ~400)".
  Yoo et al. 2025 (corpus; SI Note VII p.52-53): SweepFinder2 hard-sweep candidates "30, 22, 62, 11, and 18" in
    bonobo, central, eastern, western chimpanzee, western lowland gorilla; saltiLASSI "4-18" per taxon; 143 and 86
    in total over 10 taxa.
  GAP-01 adaptive range K_a = 1e3-1e6 per lineage (gaps.md); Uricchio 2019 "72% from weakly adaptive variants"
    (abstract, as recorded in gaps.md) -> strong fraction ~0.28 used as one power scenario.

MODEL (`derived:`): sweeps uniform in time over T generations. A completed hard sweep is detectable by SFS/diversity
scans only if it completed within the last W generations and is strong enough (4 N_e s >~ 400, Akey 2009).
  E_detect = K * (W/T) * f_strong * [(1 - f_soft) + f_soft * q_soft]
W in {4,000 (brief's 0.1 x 4N_e, unsourced), 10,000 (Hernandez/Przeworski)}; N_e = 1e4; T in {252,000, 325,000};
f_strong in {1, 0.28, 0.1}; f_soft in {0, 0.5}; q_soft = 0.2 (ASSUMPTION: relative power of SFS scans for soft
sweeps; not sourced). Haplotype scans (iHS, XP-EHH) target incomplete or population-specific sweeps and are not
counted as detectors of completed lineage-wide sweeps.

PRE-REGISTERED PREDICTIONS (written before running; the 86-100 figure for Day's own rate is already in gaps.md):
 P1 Day's own 3,200 sweeps over 325,000 generations: E_detect (power 1) = 39-98 over W = 4,000-10,000, i.e.
    "dozens to hundreds"; the "saturated" inference does not follow from his own number. Falsifier: E > 1,000.
 P2 Coding-scale K_a (1e3-1e4): E_detect <= 400 at power 1 for every W, T -> not distinguishable from per-scan
    counts (hundreds); no saturation expected. Falsifier: E > 722 (Akey's replicated count).
 P3 K_a >= 1e5 with f_strong >= 0.28 and W = 10,000: E_detect >= 1,000 completed strong sweeps, above Akey's 722
    replicated regions -> such scenarios ARE in tension with scan data and with Hernandez's null trough (Day's leg).
    Falsifier: E < 722 for K = 1e5, f_strong = 0.28, W = 10,000, T = 252,000.
 P4 Day's all-fixations reading (17.5M per lineage treated as selective sweeps; MITTENS uses LTEE G_f, "selection-
    driven sweeps"): E_detect >= 2e5 -> decisively contradicted by scans; but critics do not hold that reading.
 P5 Bonobo (Z18441321): W = 0.25 x 4 x 20,000 = 20,000 of 46,500 generations (43%); 326,000 selective sweeps would
    give E >= 1e5 at power 1 vs Yoo's 30 SweepFinder2 candidates in bonobos -> the window does NOT rescue that
    count (Day's point holds against 326,000 selective fixations, which no critic asserts).
 P6 Hernandez bound: with < 10% of human-specific amino-acid substitutions being strong classic sweeps, and
    1.3e4-3e4 amino-acid substitutions per lineage (GAP-01), strong coding classic sweeps per lineage < 1.3e3-3e3
    (constant-rate extrapolation from the last 250,000 years).
"""
import itertools
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'results', 'raw')

NE = 1e4
WINDOWS = {'0.1x4Ne (brief, unsourced)': 0.1 * 4 * NE, '0.25x4Ne = 10,000 (Hernandez 2011 / Przeworski 2002)': 0.25 * 4 * NE}
TS = (252000, 325000)
F_STRONG = (1.0, 0.28, 0.1)
F_SOFT = (0.0, 0.5)
Q_SOFT = 0.2
OBS = {'Voight 2006 strongest per population (incomplete sweeps)': 250,
       'Sabeti 2007 candidate regions': 300,
       'Akey 2009 replicated (>=2 scans)': 722,
       'Akey 2009 union of 9 scans': 5110}


def E(K, W, T, fs=1.0, fsoft=0.0):
    return K * (W / T) * fs * ((1 - fsoft) + fsoft * Q_SOFT)


def main():
    out = {}
    Ks = [('Day Z18452504: 3,200 sweeps', 3200, (325000,)),
          ('GAP-01 K_a 1e3', 1e3, TS), ('GAP-01 K_a 1e4', 1e4, TS), ('GAP-01 K_a 1e5', 1e5, TS), ('GAP-01 K_a 1e6', 1e6, TS),
          ('Day all-fixations 17.5M as sweeps', 17.5e6, (252000,))]
    print('## A. Expected detectable completed sweeps per lineage')
    print('| scenario | T | W | f_strong | f_soft | E_detect |')
    print('|---|---|---|---|---|---|')
    rows = []
    for name, K, Tset in Ks:
        for T, (wn, W), fs, fsoft in itertools.product(Tset, WINDOWS.items(), F_STRONG, F_SOFT):
            e = E(K, W, T, fs, fsoft)
            rows.append(dict(name=name, K=K, T=T, W=W, f_strong=fs, f_soft=fsoft, E=e))
            if fsoft == 0.0 or fs == 0.28:
                print('| %s | %d | %d | %.2f | %.1f | %.4g |' % (name, T, W, fs, fsoft, e))
    out['rows'] = rows
    print('\nObserved comparators:', OBS)

    preds = {}
    day = [r for r in rows if r['name'].startswith('Day Z18452504') and r['f_strong'] == 1 and r['f_soft'] == 0]
    preds['P1'] = all(39 <= r['E'] <= 98.5 for r in day) and max(r['E'] for r in day) <= 1000
    cod = [r for r in rows if r['K'] in (1e3, 1e4) and r['f_strong'] == 1 and r['f_soft'] == 0]
    preds['P2'] = max(r['E'] for r in cod) <= 400
    preds['P2_detail'] = max(r['E'] for r in cod)
    p3 = E(1e5, 10000, 252000, 0.28, 0.0)
    preds['P3'] = p3 >= 1000
    preds['P3_detail'] = p3
    p4 = min(r['E'] for r in rows if r['K'] == 17.5e6 and r['f_strong'] == 1 and r['f_soft'] == 0)
    preds['P4'] = p4 >= 2e5
    preds['P4_detail'] = p4

    print('\n## B. Bonobo (Z18441321)')
    Wb = 0.25 * 4 * 20000
    Tb = 46500
    eb = E(326000, Wb, Tb)
    print('W = %d of T = %d generations (%.0f%%); E_detect(326,000 strong sweeps) = %.4g; f_strong 0.1 -> %.4g; Yoo SweepFinder2 bonobo = 30' % (
        Wb, Tb, 100 * Wb / Tb, eb, E(326000, Wb, Tb, 0.1)))
    preds['P5'] = eb >= 1e5
    out['bonobo'] = dict(W=Wb, T=Tb, E=eb)

    print('\n## C. Hernandez 2011 bound translated to a lineage count (constant-rate extrapolation)')
    aa = (1.3e4, 3e4)
    bound = (0.10 * aa[0], 0.10 * aa[1])
    print('AA substitutions per lineage %.3g-%.3g (GAP-01 derived); strong classic sweeps < 10%% -> < %.3g-%.3g per lineage' % (aa[0], aa[1], *bound))
    print('In the 250,000-year window (5%% of substitutions per Hernandez): < %.3g-%.3g strong coding sweeps' % (0.05 * bound[0], 0.05 * bound[1]))
    preds['P6'] = bound == (1.3e3, 3e3)
    out['hernandez_bound'] = bound

    print('\n## D. K_a that would saturate scans: K such that E_detect = 722 (Akey replicated) or 5,110 (union), W = 10,000, T = 252,000')
    for target in (722, 5110):
        for fs in F_STRONG:
            K = target * 252000 / 10000 / fs
            print('target %d, f_strong %.2f -> K_a = %.3g' % (target, fs, K))

    print('\n## Predictions')
    for k, v in preds.items():
        print(k, 'HELD' if v is True else ('FAILED' if v is False else v))
    out['predictions'] = preds
    json.dump(out, open(os.path.join(RAW, 'gap02.json'), 'w'), indent=1, default=float)


if __name__ == '__main__':
    main()
