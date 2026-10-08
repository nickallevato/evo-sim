"""C1b -- simulate Day's ACTUAL time-binned aDNA statistic (Z18525185: 22,428 "fixations", 21 after 7000 BP).

THROWAWAY research check.  Run:  research/.venv/bin/python -I research/checks/c1b_day_binned_statistic.py [reps]
(runs the simulation with <=3 worker processes, then prints the analysis).  Raw output goes to the session scratchpad.

WHY.  c1_ascertainment_sim.py simulated Z23046531's two-period statistic (Neolithic sample vs modern sample).  It never
simulated Z18525185's statistic: 11 time bins, "first-passage" dating, the 21 post-7000 BP events.  The R4 verdict
"does not rescue Day" for C1/C6 is therefore unsupported until that statistic is simulated.  Disputed readings:
critic "observed 1/3 exceed neutral (P~2e-4)"; Day-side "neutral also predicts ~0, no power"; correctness review "model
never simulated the 21".  This script simulates the 21.

PROCEDURE, quoted from Z18525185 (sources/raw/day/zenodo-18525185.txt; section locators):
  s3.2 bins and n:  "0-500 BP: n = 625 / 500-1000 BP: n = 688 / 1000-2000 BP: n = 2,093 / 2000-3000 BP: n = 952 /
        3000-4000 BP: n = 980 / 4000-5000 BP: n = 1,141 / 5000-6000 BP: n = 721 / 6000-7000 BP: n = 573 /
        7000-8000 BP: n = 668 / 8000-10000 BP: n = 129 / 10000+ BP: n = 168".
  s3.3  "For each of 1,233,013 SNPs, we calculated allele frequency in each time bin. A 'fixation event' was recorded
        when an allele that was polymorphic (<100%) in an earlier bin reached 100% frequency in a later bin."
        "We identified 22,428 alleles that reached fixation between the earliest samples (Neolithic, 6000-8000 BP) and
        modern Europeans (<500 BP)."
  s3.4  "For each fixed allele, we traced its frequency trajectory through time to identify when it first reached 100%.
        This was determined as the oldest time bin in which the allele appeared fixed, working backward from the
        present."
  s4.1  tracked 16,299 of 22,428 ("the remainder had insufficient coverage in intermediate time bins"); by bin: 10000+
        3,038; 8000-10000 8,741; 7000-8000 4,497; 6000-7000 2; 5000-6000 9; 4000-5000 7; 3000-4000 2; 2000-3000 1;
        1000-2000 0; 500-1000 0; 0-500 2.
  s4.4  "Total fixations from polymorphic states: 21" (post-7000 BP).  NB the s4.1 table sums to 23 for 6000-7000 and
        younger and to 21 for 0-6000 BP only ("0-6000 BP: 21 fixations", s1.3).  Both 21 and 23 are reported here.
  s3.1  "AADR v62.0 ... European samples (n = 8,738)"; panel = 1240k ("1,233,013 SNP positions", s2.4).
  Ambiguities, each run as separate READINGS (all combinations are simulated):
   E1  eligible = modern bin 100% AND pooled Neolithic bins (6000-8000) <100%     (s3.3 sentence 2)
   E2  eligible = modern bin 100% AND some older bin <100%                         (s3.3 sentence 1)
   T1  date = start of the unbroken 100% run ending at the present ("working backward from the present")
   T2  date = oldest bin in which the allele is 100%, gaps allowed ("oldest time bin in which the allele appeared fixed")
   k   chromosomes per individual: 1 (pseudo-haploid, most ancient AADR calls) or 2 (diploid)  [text silent]
   cov fraction of the bin's individuals genotyped at a site: 1.0, or 0.3 (Z23046531 s3.3 example locus: neo_n=445 of
        1,372, mod_n=137 of 680, i.e. 0.2-0.3)  [Z18525185 silent on missingness; the 27% "insufficient coverage"
        drop is NOT modelled -- threshold unstated]
  Generation time: 20 y (Appendix A "350 generations (7,000 years)"; main) or 25 y (s2.3 "25-29 years"; sensitivity).
  Bin dates: all individuals of a bin placed at the bin midpoint; the 10000+ bin at 10,500 BP (assumed; open-ended).

MODEL (all neutral, one panmictic population, constant Ne, unlinked sites, UNSCALED Wright-Fisher, 2Ne chromosomes):
  Panel ascertainment: present-day polymorphism (Human Origins: site heterozygous in one African male; Haak 2015).  The
  start-of-window (10,500 BP) distribution of European minority-allele frequency q on the panel is taken from the exact
  scaled chain of c1_ascertainment_sim.py (design D2, Ne=1e4, split 2000 gen; scratch check, Ns=500): density flat in q to
  within 18% down to q=1e-3 and 1% at q>=1e-2, equal to 1.86 per unit q (folded) per panel site, i.e. 1.14M*1.86/(2Ne)
  panel sites per minority copy-count.  Used for all Ne (labelled assumption).  Sites with q<=10% (K=0.1 of 2Ne copies)
  are simulated; q>10% contributes <1% of events (c1 result: 50-90% starts ~0.04 events) and is omitted (K=5% config checks
  sensitivity).  Sites fixed in Europe at the window start (not polymorphic) cannot produce events and are omitted.
  Sampling: each bin draws genotyped individuals ~Bin(n, cov), chromosomes = k*g, allele count ~ Bin(chrom, x_bin).
  DAY's MODEL ("Day"): same neutral process but the drift clock runs at d = 0.45 per nominal generation (blog: "approximately
  158 real generations rather than 350"; parameters.yaml selection.turnover_d = 0.45), i.e. the time between start and each
  bin is multiplied by 0.45.  Day also says the result "predicts that fixation events should be rare, fewer than 20 across
  the entire genome" and (s4.4) "The substitution process effectively stopped 7,000 years ago"; the only simulable content
  of that is "fewer drift generations".  If Day's model is meant to be stasis (no frequency movement), it predicts S=0 by
  construction; that limit is stated, not simulated.
  ADMIXTURE (scenario, NOT a measurement): single pulse of fraction mf in {0.1, 0.3} at 7,500 BP or 5,500 BP from a source
  whose frequency has drifted independently from the window-start frequency for (start-to-pulse + 500) generations
  (labelled; no steppe/Anatolian parameters).  Neutral Ne=1e4, pulse replaces (1-mf)x+mf*y.

PRE-REGISTERED PREDICTIONS (written before any run of the statistic; only a timing test with output discarded was run):
  P1  T1 readings (terminal-run start) cannot reproduce the paper's table: nearly all eligible alleles are dated to the
      youngest bin (0-500 BP), since the preceding 500-1000 BP bin (n=688) is rarely 100% for an allele with q~1e-3;
      so under T1 the 0-500 BP count is >>2 and the pre-7000 count is small.  T2 readings (oldest 100% bin, gaps
      allowed) put most events in the old, small bins (10000+, 8000-10000, 7000-8000), qualitatively like the paper.
      => T2 is the reading consistent with the published profile; T1 is reported but disfavoured.
  P2  Neutral, Ne=1e4, T2 readings, k=1, cov=1: the post-7000 count S23 is NOT ~0.  Rough hand integral (flat panel
      density, stationary q) gives order 10^3; with drift fixations included I predict S21 in 30-3000 (central ~500) and
      the post-7000 share of all eligible events 3-30%, versus the paper's 0.14%.  k=2 and cov=0.3 lower the eligible
      total and S (more chromosome-level resolution lost); I predict S21 stays >> 21 for all T2 readings.
  P3  Consequently the observed 21 (or 23) lies in the LOWER tail of the neutral distribution for T2 (P<0.01), i.e. the
      critic's "neutral predicts 0 so no power" is wrong for this statistic: neutral predicts a large post-7000 count
      and the observation is a deficit, not a surplus.  I do NOT predict that this supports Day's mechanism: the
      pre-7000 totals will be compared (observed ~22,428 eligible, 99.86% before 7000 BP) because a reading that gets
      the early profile wrong is not the paper's procedure.
  P4  Ne dependence: S rises with Ne over {7e3,1e4,2e4} (more panel sites at low copy-count per chromosome sampled)
      by a factor 1-3.
  P5  Day's d=0.45 model gives S between 0.3x and 1x of neutral at the same Ne, comparable to neutral at ~2.2x Ne
      (time-rescaling), so the statistic cannot separate d from Ne: AUC(neutral vs Day at same Ne) >0.9 within a model
      but the neutral Ne range 7e3-2e4 spans the Day-model value (non-identifiable).
  P6  Admixture pulses (mf 0.1-0.3, 7.5 or 5.5 kBP) change S by <2x for T2 and cannot bring S21 down to ~21.
  Falsifiers: if neutral T2 S21 at Ne=1e4 is <~100 with the observed value inside the central 95%, P2/P3 fail and the
  critic/Day-side "no power, consistent" reading holds for this statistic.
"""
import os
import sys
import json
import time

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np
from concurrent.futures import ProcessPoolExecutor
import multiprocessing as mp

ROOT = 20261010
NPANEL = 1_143_671
DENS = 1.86                  # panel sites per unit minority frequency q (folded), from the D2 chain (see docstring)
BINS = [("10000+", 168, 10500), ("8000-10000", 129, 9000), ("7000-8000", 668, 7500), ("6000-7000", 573, 6500),
        ("5000-6000", 721, 5500), ("4000-5000", 1141, 4500), ("3000-4000", 980, 3500), ("2000-3000", 952, 2500),
        ("1000-2000", 2093, 1500), ("500-1000", 688, 750), ("0-500", 625, 250)]
OBS = [3038, 8741, 4497, 2, 9, 7, 2, 1, 0, 0, 2]
NB = len(BINS)
NB_N = np.array([b[1] for b in BINS])
READINGS = [(e, t, k, c) for e in (1, 2) for t in (1, 2) for k in (1, 2) for c in (1.0, 0.3)]
RNAME = lambda r: "E%d-T%d-k%d-cov%.1f" % r

# config: name, Ne, gen_years, d, admix (pulse BP, frac) or None, Kfrac
CONFIGS = []
for ne in (7000, 10000, 20000):
    CONFIGS.append(dict(name="neutral Ne=%d" % ne, Ne=ne, gy=20, d=1.0, adm=None, K=0.10))
for ne in (7000, 10000, 20000):
    CONFIGS.append(dict(name="Day d=0.45 Ne=%d" % ne, Ne=ne, gy=20, d=0.45, adm=None, K=0.10))
CONFIGS.append(dict(name="neutral Ne=10000 gy25", Ne=10000, gy=25, d=1.0, adm=None, K=0.10))
CONFIGS.append(dict(name="Day d=0.45 Ne=10000 gy25", Ne=10000, gy=25, d=0.45, adm=None, K=0.10))
CONFIGS.append(dict(name="neutral Ne=10000 K=5%", Ne=10000, gy=20, d=1.0, adm=None, K=0.05))
for pbp in (7500, 5500):
    for mf in (0.1, 0.3):
        CONFIGS.append(dict(name="admix %d BP m=%.1f Ne=10000" % (pbp, mf), Ne=10000, gy=20, d=1.0, adm=(pbp, mf), K=0.10))


def simulate_rep(cfg, rng):
    Ne, gy, d, adm, Kf = cfg["Ne"], cfg["gy"], cfg["d"], cfg["adm"], cfg["K"]
    M = 2 * Ne
    K = int(Kf * M)
    lam = NPANEL * DENS / M
    cnt = rng.poisson(lam, size=K)
    m = np.repeat(np.arange(1, K + 1, dtype=np.int64), cnt)
    tstart = BINS[0][2] / gy
    steps = [int(round((tstart - b[2] / gy) * d)) for b in BINS]
    S = len(m)
    rec = np.empty((NB, S), dtype=np.float32)
    rec[0] = 1.0 - m / M
    ms = None
    pstep = None
    if adm is not None:
        pstep = int(round((tstart - adm[0] / gy) * d))
        ms = m.copy()
        for _ in range(500):             # extra independent divergence of the source
            ms = rng.binomial(M, ms / M)
    for t in range(1, steps[-1] + 1):
        m = rng.binomial(M, m / M)
        if ms is not None:
            ms = rng.binomial(M, ms / M)
        if adm is not None and t == pstep:
            m = np.rint((1 - adm[1]) * m + adm[1] * ms).astype(np.int64)
            ms = None
        for b in range(1, NB):
            if steps[b] == t:
                rec[b] = 1.0 - m / M
    return rec


def tally(rec, rng):
    out = {}
    S = rec.shape[1]
    for k in (1, 2):
        for cov in (1.0, 0.3):
            if cov >= 1.0:
                g = np.broadcast_to(NB_N[:, None], (NB, S))
            else:
                g = rng.binomial(NB_N[:, None], cov, size=(NB, S))
            ch = g * k
            s = rng.binomial(ch, rec.astype(np.float64))
            fx = (s == ch) & (ch > 0)
            mod = fx[NB - 1]
            E1 = mod & ~(fx[2] & fx[3])
            E2 = mod & ~fx[:NB - 1].all(axis=0)
            L = np.cumprod(fx[::-1], axis=0).sum(axis=0)
            T1 = NB - L
            T2 = np.argmax(fx, axis=0)
            for e, Em in ((1, E1), (2, E2)):
                for t, T in ((1, T1), (2, T2)):
                    out[RNAME((e, t, k, cov))] = np.bincount(T[Em], minlength=NB)[:NB].tolist()
    return out


def task(args):
    ci, rep = args
    cfg = CONFIGS[ci]
    rng = np.random.default_rng(np.random.SeedSequence([ROOT, ci, rep]))
    t0 = time.time()
    rec = simulate_rep(cfg, rng)
    res = tally(rec, rng)
    return ci, rep, res, time.time() - t0


def run(reps, raw_path, only=None):
    jobs = [(ci, r) for r in range(reps) for ci in range(len(CONFIGS)) if only is None or ci in only]
    res = {}
    with ProcessPoolExecutor(max_workers=3, mp_context=mp.get_context("forkserver")) as ex:
        for ci, rep, out, dt in ex.map(task, jobs, chunksize=1):
            res.setdefault(ci, []).append(out)
    with open(raw_path, "w") as f:
        json.dump(res, f)
    return res


def pois_cdf(k, mu):
    from math import exp
    if mu <= 0:
        return 1.0
    term = exp(-mu)
    tot = term
    for i in range(1, int(k) + 1):
        term *= mu / i
        tot += term
    return min(tot, 1.0)


def pois_sf(k, mu):
    return 1.0 - pois_cdf(k - 1, mu)


def analyse(res):
    R = {int(k): v for k, v in res.items()}
    lines = []
    P = lines.append

    def arr(ci, rd, lo, hi=NB):
        return np.array([sum(rep[rd][lo:hi]) for rep in R[ci]])

    def prof(ci, rd):
        return np.mean([rep[rd] for rep in R[ci]], axis=0)

    nrep = {ci: len(v) for ci, v in R.items()}
    P("## Table A. Eligible total and bin profile (mean over reps), neutral Ne=10000, gy 20, all 16 readings")
    P("obs profile: " + str(OBS) + "  (eligible 22,428; tracked 16,299)")
    P("| reading | eligible | pre-7000 (bins 10000+,8-10k,7-8k) | S23 (6-7k and younger) | S21 (0-6k) | 0-500 bin |")
    P("|---|---|---|---|---|---|")
    ci = 1
    for rd in READINGS:
        p = prof(ci, RNAME(rd))
        P("| %s | %.0f | %.0f | %.1f | %.1f | %.1f |" % (RNAME(rd), p.sum(), p[:3].sum(), p[3:].sum(), p[4:].sum(), p[10]))
    P("")
    P("## Table B. S21 and S23 distribution by config for the T2 readings (reps=%s)" % sorted(set(nrep.values())))
    P("Entries: mean [2.5%, 97.5%] over replicates; pL = Poisson P(S <= obs | mean).  obs S21 = 21, S23 = 23.")
    for rdset in [(2, 2, 1, 1.0), (2, 2, 2, 1.0), (2, 2, 1, 0.3), (2, 2, 2, 0.3),
                  (1, 2, 1, 1.0), (1, 2, 2, 1.0), (1, 2, 1, 0.3), (1, 2, 2, 0.3)]:
        rd = RNAME(rdset)
        P("")
        P("### reading %s" % rd)
        P("| config | eligible | pre-7000 | S23 | S21 | pL(S23<=23) | pL(S21<=21) | frac reps S21<=21 |")
        P("|---|---|---|---|---|---|---|---|")
        for ci in sorted(R):
            a23 = arr(ci, rd, 3)
            a21 = arr(ci, rd, 4)
            el = arr(ci, rd, 0)
            pre = arr(ci, rd, 0, 3)
            P("| %s | %.0f | %.0f | %.0f [%.0f, %.0f] | %.0f [%.0f, %.0f] | %.2g | %.2g | %.2f |" % (
                CONFIGS[ci]["name"], el.mean(), pre.mean(), a23.mean(), np.percentile(a23, 2.5), np.percentile(a23, 97.5),
                a21.mean(), np.percentile(a21, 2.5), np.percentile(a21, 97.5),
                pois_cdf(23, a23.mean()), pois_cdf(21, a21.mean()), (a21 <= 21).mean()))
    P("")
    P("## Table C. T1 readings (terminal-run dating), S21/S23 and 0-500 BP bin")
    P("| config | reading | eligible | S23 | S21 | 0-500 bin |")
    P("|---|---|---|---|---|---|")
    for ci in sorted(R):
        for rdset in [(2, 1, 1, 1.0), (1, 1, 1, 1.0)]:
            rd = RNAME(rdset)
            p = prof(ci, rd)
            P("| %s | %s | %.0f | %.1f | %.1f | %.1f |" % (CONFIGS[ci]["name"], rd, p.sum(), p[3:].sum(), p[4:].sum(), p[10]))
    P("")
    P("## Table D. Power: AUC = P(S_A > S_B) + 0.5 P(tie) over replicate pairs (S21, T2, E2)")
    names = {c["name"]: i for i, c in enumerate(CONFIGS)}
    pairs = [("neutral Ne=10000", "Day d=0.45 Ne=10000"), ("neutral Ne=7000", "neutral Ne=20000"),
             ("Day d=0.45 Ne=20000", "neutral Ne=10000"), ("Day d=0.45 Ne=7000", "neutral Ne=7000"),
             ("Day d=0.45 Ne=10000", "neutral Ne=7000")]
    P("| A | B | reading | AUC | mean A | mean B |")
    P("|---|---|---|---|---|---|")
    for A, B in pairs:
        if names[A] in R and names[B] in R:
            for rdset in [(2, 2, 1, 1.0), (2, 2, 2, 0.3)]:
                rd = RNAME(rdset)
                a = arr(names[A], rd, 4)
                b = arr(names[B], rd, 4)
                auc = ((a[:, None] > b[None, :]).mean() + 0.5 * (a[:, None] == b[None, :]).mean())
                P("| %s | %s | %s | %.3f | %.0f | %.0f |" % (A, B, rd, auc, a.mean(), b.mean()))
    P("")
    P("## Table E. Full bin profile (mean) for T2/E2/k1/cov1.0 vs observed")
    P("| config | " + " | ".join(b[0] for b in BINS) + " |")
    P("|---|" + "---|" * NB)
    P("| observed | " + " | ".join(str(o) for o in OBS) + " |")
    for ci in sorted(R):
        p = prof(ci, RNAME((2, 2, 1, 1.0)))
        P("| %s | " % CONFIGS[ci]["name"] + " | ".join("%.1f" % v for v in p) + " |")
    return "\n".join(lines)


if __name__ == "__main__":
    reps = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    scratch = os.environ.get("C1B_RAW", "/tmp/claude-1000/-home-na-projects-evo-sim/1a09d35c-0829-4a9e-9e1c-591add0b31de/scratchpad/c1b_raw.json")
    if len(sys.argv) > 2 and sys.argv[2] == "analyse":
        with open(scratch) as f:
            res = json.load(f)
    elif len(sys.argv) > 2 and sys.argv[2] == "timing":
        rng = np.random.default_rng(1)
        for ci in (1, 4, 9, 10):
            t0 = time.time()
            task((ci, 999))
            print("timing cfg", ci, round(time.time() - t0, 1), "s")   # statistic output discarded
        sys.exit()
    else:
        t0 = time.time()
        res = run(reps, scratch)
        print("sim time %.0f s" % (time.time() - t0))
    print(analyse(res))
