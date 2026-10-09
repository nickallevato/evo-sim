"""C1c -- Day's binned "21" (Z18525185) with REAL AADR call depth and an ANCESTRY-REPLACEMENT model.

THROWAWAY research check.  Follow-up to c1b_day_binned_statistic.py (REVIEW.md Queue item 6).
Run (always the isolated venv):
    research/.venv/bin/python -I research/checks/c1c_call_depth_replacement.py depth  <anno> <out.json>   # build depth table
    research/.venv/bin/python -I research/checks/c1c_call_depth_replacement.py selftest                  # logic tests, tiny
    research/.venv/bin/python -I research/checks/c1c_call_depth_replacement.py run <rep> [outdir]        # one replicate, all scenarios
    research/.venv/bin/python -I research/checks/c1c_call_depth_replacement.py analyse [rawdir]          # tables from c1c_rep*.json

WHY.  c1b simulated Day's statistic literally but (a) gave every bin an arbitrary genotyped fraction (1.0 / 0.3) and
(b) had one closed panmictic population.  It could not reproduce Day's own table (7000-8000 BP bin ~1,350 vs 4,497;
pre-7000 share 38-60% vs 99.86%), so it was "not a valid null" and the verdict was "not reproducible; cannot
adjudicate".  A reviewer's 1-replicate scratch test suggested per-site call depth (a "handful" of calls in old bins) as
the cause.  This script replaces both guesses with data and a model:
  (1) CALL DEPTH FROM THE PUBLIC AADR v62.0 .anno FILE.  For every individual the file gives "SNPs hit on autosomal
      targets (1240k)" and the genetic-ID suffix (.DG/.HO = diploid calls; everything else = pseudo-haploid).  Per bin we
      build n_pseudohaploid, n_diploid and the mean per-individual hit probability p = hits / 1,150,639 (autosomal 1240k
      targets).  The number of CALLED individuals at a site in a bin is Binomial(n, p*w_s); w_s is a per-site capture
      efficiency (mean 1; Gamma(kappa) heterogeneity as a sensitivity).  n is scaled to Day's own bin n (s3.2).  Sample
      set check: lat 35-72, lon -25..45, excluding Turkey/Armenia/Syria/Georgia/Iraq/N.Africa/Abkhazia/Russia/Crimea gives
      anno counts 167/133/669/579/726/1155/1015/1000/2125/715/524 (oldest->youngest) vs Day's 168/129/668/573/721/1141/
      980/952/2093/688/625 (8,808 vs 8,738), so Day's sample is essentially reproduced from the public file.
  (2) ANCESTRY REPLACEMENT.  A frequency-level Wright-Fisher model (exact binomial drift, 1 generation per step) of the
      pooled European sample as a local population "EU" that receives pulses from two drifting sources:
        W   = Mesolithic/WHG-like local population (EU starts as W at 10,500 BP);
        A   = Anatolian-farmer-like source, 10 equal pulses 9,500..7,250 BP, after which the W share is w_end;
        S   = steppe-like source, 6 equal pulses 5,000..4,500 BP, after which the S share is s_end.
      Panel sites (1,143,671 autosomal x 0.93 = 1,063,614 that are polymorphic in the common ancestor; the other 7% are
      fixed there and cannot register events without recurrent mutation) start with ancestral frequency y0 ~ U(0,1)
      (this is the flat folded density 1.86 per unit q of the c1 chain D2; ascertainment on an African male
      heterozygote).  W, A, S diverge from the ancestor by exact WF drift of 2200/1400/600 generations at Ne = 1e4
      (branch F = 0.11/0.07/0.03, so the Hudson/Patterson pairwise Fst(W,A) ~ 0.09, (W,S) ~ 0.07, (A,S) ~ 0.05; my
      recollection of the order of magnitude for WHG/Anatolian-N/Yamnaya on the 1240k panel, NOT retrieved from a
      source; ASSUMED, with 0.5x and 2x sensitivity).  Then 525 generations
      (20 y/gen; 10,500 BP -> present; 25 y/gen sensitivity) of drift in EU at a scenario Ne(t), with pulses.
      No new mutations (c1: new-in-window substitutions ~5e-151 per site).  Sampling: bin sample frequency = EU frequency
      at the bin's midpoint date (10000+ bin at 10,500 BP, as c1b), binomial over the called chromosomes.
  Statistic, as c1b (Z18525185 s3.3, s3.4, s4.1 quotes are in c1b's docstring): alleles are tracked for BOTH alleles at a
  site (an allele "fixed" = 100% of called chromosomes in that bin).  Readings: E1 = modern bin 100% and pooled
  6000-8000 BP bins <100% (s3.3 sentence 2; PRIMARY because it matches the "22,428 between Neolithic and modern" wording
  and the s4.3 start-frequency table), E2 = modern 100% and some older bin <100%; T2 = oldest bin in which the allele is
  100% (gaps allowed; PRIMARY, the only dating consistent with Day's profile in c1b), T1 = start of the unbroken 100% run
  ending at the present.  "Tracked" = at least one call in every one of the 11 bins (Day: 16,299 of 22,428 = 72.7%
  "had insufficient coverage in intermediate bins", threshold unstated).  Headline model number:
        S21 = tracked E1-T2 events dated 5000-6000 BP or younger  (bins 4..10; Day: "0-6000 BP: 21");
        S23 = same, 6000-7000 BP and younger (Day's table sums to 23).
  Observed (Z18525185 s4.1, s4.3): eligible 22,428; profile 3,038/8,741/4,497/2/9/7/2/1/0/0/2 over the 11 bins
  (oldest first); pre-7000 share 99.86%; start frequencies of the fixed allele in the Neolithic 79.2/20.2/0.5/0.2% in
  [99,100)/[95,99)/[90,95)/<90%.

SCENARIO GRID (per replicate; every scenario runs on the same 1.06M-site panel realisation):
  Ne in {1e4, 2e4, 5e4, 1e5, 3e5, 1e6} constant, and growth 1e4->1e5, 1e4->1e6 (exponential over the window)
  x replacement R0 (none; EU closed) / R1 (w_end 0.4, s_end 0.2) / R2 (0.2, 0.38; literature-central: modern W .12, A .50,
  S .38) / R3 (0.1, 0.55; Britain-like).  Plus Day's d = 0.45 (drift clock x 0.45, i.e. Ne_eff = Ne/0.45) for Ne in {1e4,
  2e4} x {R0, R2}; 25 y/generation for (1e4,R0) and (1e5,R2); Fst scale 0.5x and 2x for R2 at Ne 1e4, 1e5, 1e6.
  Sampling variants on five scenarios: capture heterogeneity kappa in {inf, 2, 0.5}; per-call false-minor error rate
  eps in {0, 1e-3} on pseudo-haploid calls (the latter represents damage/mapping error; it can only ADD polymorphism).

PRE-REGISTERED PREDICTIONS (written before the main run; only structure/timing smoke tests, with the statistic output
not inspected, preceded this commit; the depth table and the anno-vs-Day sample counts were looked at because they are
inputs, not the statistic).  Reference scenario = R0, Ne=1e4, kappa=inf, eps=0, E1-T2, tracked.  Depth derived from the
anno (not a result): chromosomes called per site in the three oldest bins ~ 49 / 62 / 282 (Table 0 of the output), i.e. NOT "a handful".
  P1  CALL DEPTH ALONE DOES NOT REPRODUCE 21.  At real depth, closed-population neutral drift at Ne=1e4 gives S21 in
      [300, 10,000] (central ~2,000), at least 15x the observed 21.  The reviewer's "handful of calls" cause is not the
      real depth.  Falsifier: S21 < 100 for the reference scenario.
  P2  Ne MAP.  S21 falls monotonically with constant window Ne (loss of an allele visible in all three oldest bins needs
      drift).  The constant Ne* at which the R0 mean S21 equals 21 lies in [3e4, 1e6] (central ~2e5); under R2 it lies
      within a factor 3 of the R0 value.  Falsifier: Ne* outside [1e4, 3e6], or non-monotonic.
  P3  THE TENSION (central prediction).  Eligible (E1) scales ~1/Ne in R0: 8k-40k at Ne=1e4, below 5k for Ne >= 2e5.
      So no (R, Ne) cell satisfies BOTH eligible within 3x of 22,428 AND S21 within [7, 63] (3x of 21) AND pre-7000 share
      >= 90%.  Cells with S21 ~ 21 fall short of the eligible count by >= 3x (the structure W-A-S differentiation supplies
      only a few thousand extra eligible alleles at most), and cells with ~22k eligible overshoot S21 by >= 15x.  If P3 holds the
      verdict stays "cannot adjudicate on the full table" but S21 is bracketed by Ne.  Falsifier: any cell passes all
      three conditions (then the replacement + demography model reproduces Day's table and 21 is its neutral value).
  P4  REPLACEMENT IS A SECOND-ORDER LEVER FOR S21.  At fixed Ne, R2 vs R0 changes S21 by less than 2x, but raises eligible
      by >= 1.3x and the pre-7000 share by >= 10 percentage points (events from W/A differentiation fall in the old
      bins).  Steppe bump (medium confidence, ~50%): the share of S21 events in the 4000-6000 BP bins is >= 1.5x larger
      in R2/R3 than in R0 (Day's own 16 of 21 events are in 4000-6000).  Falsifier: S21(R2)/S21(R0) outside [0.5, 2].
  P5  DAY'S d = 0.45 behaves like neutral at Ne/0.45 for eligible and S21 (within 30%).  At Ne=1e4 it gives S21 >= 5x
      the observed 21, so Day's d does not map to 21 either; the "stasis" limit (no frequency movement) gives S21 = 0 by
      construction and cannot be tested by simulation.  Falsifier: Day d=0.45 at Ne=1e4, R0, S21 < 100.
  P6  ERROR FLOOR.  A false-minor-call rate eps=1e-3 per pseudo-haploid call raises S21 by >= 3x in R2 at Ne=1e6 (where
      the drift baseline is tiny).  So the 21 is a floor that assay error alone can exceed; errors push toward LARGER
      model counts, i.e. toward "observed is a deficit".  Falsifier: ratio < 1.5.
  P7  CAPTURE HETEROGENEITY.  kappa=0.5 (strong site-to-site variation in capture efficiency) brings the tracked fraction
      into 55-90% (observed 72.7%) and changes tracked S21 by less than 2x relative to kappa=inf.  Falsifier: tracked
      fraction outside 40-95% at kappa=0.5, or S21 changes >2x.
  P8  WHAT THE 21 MAPS TO (summary of P1-P7).  Under the critic-side model (neutral + replacement + real depth), 21 is
      reached only if the Holocene European Ne is >= ~5e4 (growth well above the textbook 1e4); at Ne <= 2e4 the
      neutral model predicts hundreds to thousands, so 21 is a deficit of >= 15x.  Under Day's d model the map shifts
      to Ne/0.45.  I expect the strict validity gate (P3) to fail, so the sign of the verdict is conditional on the
      Holocene Ne, which is exactly the C4/C5 dispute.
  WHAT EACH SIDE'S MODEL PREDICTS FOR THIS STATISTIC:
    Day (clock stopped / punctuated; Z18525185 abstract, s4.4): essentially no post-7000 events; the only simulable content
      is fewer drift generations (d = 0.45), which gives P5 (thousands at Ne=1e4); the pure stasis reading gives 0.
    Critic (neutral drift + Neolithic/Bronze replacement; C5, C1): the pre-7000 cluster is replacement plus sparse old-bin
      sampling and "neutral also predicts ~0" post-7000; this model says neutral predicts ~0 only if Ne is large (P2/P8),
      not at Ne=1e4 (c1b).  The critic's "no power" reading and the repo's earlier "deficit" wording are both
      conditional on Ne.

Raw output: research/checks/results/raw/c1c_rep<rep>.json (committed by the caller, not by the script).
"""
import os
import sys
import json
import time
import csv

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT_SEED = 20261011
NPANEL = 1_143_671
FRAC_POLY = 0.93                       # flat folded density 1.86/unit q  <=>  93% of panel sites polymorphic in the ancestor
NS = int(os.environ.get("C1C_NS", int(round(NPANEL * FRAC_POLY))))
NAUTO = 1_150_639                      # autosomal 1240k targets (denominator of the anno "SNPs hit" column)
NE_PRE = 10_000                        # Ne of the pre-window branches and of the A/S sources
PRE_GENS = {"W": 2200, "A": 1400, "S": 600}
START_BP = 10_500
# bins oldest -> youngest: name, Day n (Z18525185 s3.2), midpoint BP (10000+ assumed 10,500)
BINS = [("10000+", 168, 10500), ("8000-10000", 129, 9000), ("7000-8000", 668, 7500), ("6000-7000", 573, 6500),
        ("5000-6000", 721, 5500), ("4000-5000", 1141, 4500), ("3000-4000", 980, 3500), ("2000-3000", 952, 2500),
        ("1000-2000", 2093, 1500), ("500-1000", 688, 750), ("0-500", 625, 250)]
NB = len(BINS)
MOD = NB - 1
OBS = [3038, 8741, 4497, 2, 9, 7, 2, 1, 0, 0, 2]
OBS_ELIG = 22428
OBS_TRACKED = 16299
OBS_START = [79.2, 20.2, 0.5, 0.2]     # % of the Neolithic frequency of the fixed allele in [99,100),[95,99),[90,95),<90
DEPTH_JSON = os.path.join(HERE, "results", "c1c_depth_table.json")
A_PULSES_BP = [9500 - 250 * k for k in range(10)]
S_PULSES_BP = [5000 - 100 * k for k in range(6)]
REPL = {"R0": None, "R1": (0.4, 0.2), "R2": (0.2, 0.38), "R3": (0.1, 0.55)}
NON_EUROPE = {"Turkey", "Armenia", "Syria", "Georgia", "Iraq", "Tunisia", "Algeria", "Morocco", "Abkhazia", "Russia", "Crimea"}


# ----------------------------------------------------------------------------------------------- depth table from anno
def build_depth(anno_path, out_json):
    def fl(x):
        try:
            return float(x)
        except ValueError:
            return None
    edges = [(10000, 1e9), (8000, 10000), (7000, 8000), (6000, 7000), (5000, 6000), (4000, 5000), (3000, 4000),
             (2000, 3000), (1000, 2000), (500, 1000), (0, 500)]
    acc = [dict(ph=[], dip=[]) for _ in edges]
    with open(anno_path, encoding="latin-1", newline="") as f:
        rd = csv.reader(f, delimiter="\t")
        next(rd)
        for row in rd:
            if len(row) < 41:
                continue
            d, la, lo, hit = fl(row[9]), fl(row[16]), fl(row[17]), fl(row[22])
            if None in (d, la, lo, hit) or not (35 <= la <= 72 and -25 <= lo <= 45) or row[15] in NON_EUROPE:
                continue
            for i, (lo_, hi_) in enumerate(edges):
                if lo_ <= d < hi_:
                    gid = row[0]
                    dip = (".DG" in gid) or gid.endswith(".HO")
                    acc[i]["dip" if dip else "ph"].append(hit)
                    break
    out = []
    for i, (name, nday, mid) in enumerate(BINS):
        ph, dp = np.array(acc[i]["ph"]), np.array(acc[i]["dip"])
        na = len(ph) + len(dp)
        sc = nday / na
        out.append(dict(bin=name, n_anno=na, n_day=nday, n_ph=int(round(len(ph) * sc)), n_dip=int(round(len(dp) * sc)),
                        p_ph=float(ph.mean() / NAUTO) if len(ph) else 0.0, p_dip=float(dp.mean() / NAUTO) if len(dp) else 0.0,
                        calls_per_site=float((ph.sum() + dp.sum()) / NAUTO * sc),
                        chrom_per_site=float((ph.sum() + 2 * dp.sum()) / NAUTO * sc)))
    with open(out_json, "w") as f:
        json.dump(out, f, indent=1)
    return out


def load_depth():
    with open(DEPTH_JSON) as f:
        return json.load(f)


# ----------------------------------------------------------------------------------------------- simulation
def drift(x, N2, rng):
    return rng.binomial(N2, x) / N2


def make_panel(rng, fs=1.0):
    """Ancestral frequency y0 ~ U(0,1) -> W, A, S by exact WF drift; then A and S evolve on to their pulse dates."""
    y0 = rng.random(NS)
    N2 = 2 * NE_PRE
    src = {}
    for k in ("W", "A", "S"):
        x = y0.copy()
        for _ in range(int(round(PRE_GENS[k] * fs))):
            x = drift(x, N2, rng)
        src[k] = x
    return src


def fst(p1, p2):
    """Hudson/Patterson pairwise Fst, ratio of averages."""
    return float(np.mean((p1 - p2) ** 2) / np.mean(p1 * (1 - p2) + p2 * (1 - p1)))


def source_trajectories(src, gy, rng):
    """A and S drift (Ne_src = NE_PRE) from START_BP to their last pulse; return {step: freq array}."""
    traj = {}
    N2 = 2 * NE_PRE
    for key, times in (("A", A_PULSES_BP), ("S", S_PULSES_BP)):
        steps = sorted(set(int(round((START_BP - t) / gy)) for t in times))
        x = src[key].copy()
        d = {}
        t = 0
        for st in steps:
            while t < st:
                x = drift(x, N2, rng)
                t += 1
            d[st] = x.copy()
        traj[key] = d
    return traj


def pulse_fractions(r):
    wend, send = REPL[r]
    return 1 - wend ** (1 / len(A_PULSES_BP)), 1 - (1 - send) ** (1 / len(S_PULSES_BP))


def ancestry_shares(r, bp, gy=20):
    """analytic W, A, S share of EU at date bp (after pulses at times >= bp)."""
    if REPL[r] is None:
        return 1.0, 0.0, 0.0
    mA, mS = pulse_fractions(r)
    w = (1 - mA) ** sum(1 for t in A_PULSES_BP if t >= bp)
    s_keep = (1 - mS) ** sum(1 for t in S_PULSES_BP if t >= bp)
    return w * s_keep, (1 - w) * s_keep, 1 - s_keep


def ne_schedule(scen, T):
    ne0, ne1, d = scen["Ne0"], scen["Ne1"], scen["d"]
    t = np.arange(T + 1)
    ne = ne0 * (ne1 / ne0) ** (t / T)
    return np.maximum(2, np.rint(2 * ne / d)).astype(np.int64)


def simulate_scenario(src, traj, scen, rng):
    gy = scen["gy"]
    T = int(round(START_BP / gy))
    N2 = ne_schedule(scen, T)
    x = src["W"].copy()
    pulses = {}
    if REPL[scen["R"]] is not None:
        mA, mS = pulse_fractions(scen["R"])
        for t in A_PULSES_BP:
            pulses.setdefault(int(round((START_BP - t) / gy)), []).append((mA, traj["A"][int(round((START_BP - t) / gy))]))
        for t in S_PULSES_BP:
            pulses.setdefault(int(round((START_BP - t) / gy)), []).append((mS, traj["S"][int(round((START_BP - t) / gy))]))
    rec_steps = {int(round((START_BP - b[2]) / gy)): i for i, b in enumerate(BINS)}
    Trun = max(rec_steps)
    xb = np.empty((NB, len(x)), dtype=np.float32)
    if 0 in rec_steps:
        xb[rec_steps[0]] = x
    for t in range(1, Trun + 1):
        x = rng.binomial(N2[t], x) / N2[t]
        for m, y in pulses.get(t, ()):
            x = (1 - m) * x + m * y
        if t in rec_steps:
            xb[rec_steps[t]] = x
    return xb


# ----------------------------------------------------------------------------------------------- sampling
def sample_bins(xb, depth, rng, kappa=None, eps=0.0):
    S = xb.shape[1]
    a = np.empty((NB, S), dtype=np.int32)
    c = np.empty((NB, S), dtype=np.int32)
    if kappa is None:
        w_anc = w_mod = 1.0
    else:
        w_anc = rng.gamma(kappa, 1.0 / kappa, size=S)
        w_mod = rng.gamma(kappa, 1.0 / kappa, size=S)
    for b in range(NB):
        w = w_mod if b == MOD else w_anc
        dd = depth[b]
        ph = rng.binomial(dd["n_ph"], np.minimum(1.0, dd["p_ph"] * w), size=S) if dd["n_ph"] else np.zeros(S, dtype=np.int64)
        dp = rng.binomial(dd["n_dip"], np.minimum(1.0, dd["p_dip"] * w), size=S) if dd["n_dip"] else np.zeros(S, dtype=np.int64)
        x = np.clip(xb[b].astype(np.float64), 0.0, 1.0)
        xe = x * (1 - eps) + (1 - x) * eps if eps > 0 else x
        a[b] = rng.binomial(ph, xe) + rng.binomial(2 * dp, x)
        c[b] = ph + 2 * dp
    return a, c


# ----------------------------------------------------------------------------------------------- statistic
def statistic(a, c):
    """Return dict: for E in {E1,E2}, T in {T1,T2}: bin counts for 'all' sites and for 'trk' (data in all 11 bins);
    plus start-frequency categories for E1 and the number of eligible sites."""
    S = a.shape[1]
    obs = c > 0
    trk = obs.all(axis=0)
    cnt = {k: {"all": np.zeros(NB, dtype=np.int64), "trk": np.zeros(NB, dtype=np.int64)}
           for k in ("E1T1", "E1T2", "E2T1", "E2T2")}
    start = {"all": np.zeros(4, dtype=np.int64), "trk": np.zeros(4, dtype=np.int64)}
    ap, cp = a[2].astype(np.int64) + a[3], c[2].astype(np.int64) + c[3]
    for j in (1, 0):
        fx = obs & ((a == c) if j == 1 else (a == 0))
        poly = obs & ~fx
        mod = fx[MOD]
        pooled_fx = (cp > 0) & ((ap == cp) if j == 1 else (ap == 0))
        E1 = mod & (cp > 0) & ~pooled_fx
        E2 = mod & poly[:MOD].any(axis=0)
        T2 = fx.argmax(axis=0)
        L = np.cumprod(fx[::-1].astype(np.uint8), axis=0).sum(axis=0)
        T1 = NB - L
        for ename, E in (("E1", E1), ("E2", E2)):
            for tname, T in (("T1", T1), ("T2", T2)):
                k = ename + tname
                cnt[k]["all"] += np.bincount(T[E], minlength=NB)[:NB]
                cnt[k]["trk"] += np.bincount(T[E & trk], minlength=NB)[:NB]
        with np.errstate(divide="ignore", invalid="ignore"):
            fneo = np.where(cp > 0, (ap / np.maximum(cp, 1)) if j == 1 else 1 - ap / np.maximum(cp, 1), 0.0)
        cat = np.where(fneo >= 0.99, 0, np.where(fneo >= 0.95, 1, np.where(fneo >= 0.90, 2, 3)))
        for key, mask in (("all", E1), ("trk", E1 & trk)):
            start[key] += np.bincount(cat[mask], minlength=4)[:4]
    out = {k: {kk: v.tolist() for kk, v in d.items()} for k, d in cnt.items()}
    out["start"] = {k: v.tolist() for k, v in start.items()}
    out["n_trk_sites"] = int(trk.sum())
    return out


# ----------------------------------------------------------------------------------------------- scenario list
def scenario_list():
    L = []

    def add(name, ne0, ne1, R, d=1.0, gy=20, fs=1.0, variants=None):
        L.append(dict(name=name, Ne0=ne0, Ne1=ne1, R=R, d=d, gy=gy, fs=fs,
                      variants=variants or [("base", None, 0.0)]))
    full = [("base", None, 0.0), ("k2", 2.0, 0.0), ("k0.5", 0.5, 0.0), ("e1e-3", None, 1e-3), ("k0.5e1e-3", 0.5, 1e-3)]
    central = {("R0", 1e4), ("R0", 1e5), ("R2", 1e4), ("R2", 1e5), ("R2", 1e6)}
    for R in REPL:
        for ne in (1e4, 2e4, 5e4, 1e5, 3e5, 1e6):
            add("%s_Ne%g" % (R, ne), ne, ne, R, variants=full if (R, ne) in central else None)
        add("%s_grow1e4-1e5" % R, 1e4, 1e5, R)
        add("%s_grow1e4-1e6" % R, 1e4, 1e6, R)
    for ne in (1e4, 2e4):
        for R in ("R0", "R2"):
            add("%s_Ne%g_Day0.45" % (R, ne), ne, ne, R, d=0.45)
    add("R0_Ne1e4_gy25", 1e4, 1e4, "R0", gy=25)
    add("R2_Ne1e5_gy25", 1e5, 1e5, "R2", gy=25)
    for ne in (1e4, 1e5, 1e6):
        add("R2_Ne%g_F0.5" % ne, ne, ne, "R2", fs=0.5)
        add("R2_Ne%g_F2" % ne, ne, ne, "R2", fs=2.0)
    return L


def run_rep(rep, outdir, only=None, nsamp=2):
    depth = load_depth()
    t0 = time.time()
    res = {"meta": {"rep": rep, "NS": NS, "depth": depth}}
    panels = {}
    scens = scenario_list()
    if only:
        scens = [s for s in scens if s["name"] in only]
    for si, scen in enumerate(scens):
        fs = scen["fs"]
        if fs not in panels:
            prng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, rep, 1, int(fs * 10)]))
            src = make_panel(prng, fs)
            res["meta"]["fst_fs%g" % fs] = dict(WA=fst(src["W"], src["A"]), WS=fst(src["W"], src["S"]), AS=fst(src["A"], src["S"]))
            panels[fs] = (src, {})
        src, trajs = panels[fs]
        if scen["gy"] not in trajs:
            trng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, rep, 2, int(fs * 10), scen["gy"]]))
            trajs[scen["gy"]] = source_trajectories(src, scen["gy"], trng)
        rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, rep, 3, si]))
        xb = simulate_scenario(src, trajs[scen["gy"]], scen, rng)
        out = {"modern_fixed_frac": float(np.mean((xb[MOD] == 0) | (xb[MOD] == 1)))}
        for vi, (vname, kappa, eps) in enumerate(scen["variants"]):
            out[vname] = []
            for sr in range(nsamp):
                srng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, rep, 4, si, sr, vi]))
                a, c = sample_bins(xb, depth, srng, kappa, eps)
                out[vname].append(statistic(a, c))
        res[scen["name"]] = out
        print("rep %d scen %d/%d %s done, t=%.0fs" % (rep, si + 1, len(scens), scen["name"], time.time() - t0), flush=True)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "c1c_rep%d.json" % rep), "w") as f:
            json.dump(res, f)
    return res


# ----------------------------------------------------------------------------------------------- self test
def selftest():
    # toy statistic: 11 bins, 3 sites.  site0: allele 1 100% in bins 0,1,3..10; polymorphic in bin 2 (7-8k) -> E1 needs pooled
    # 6-8k poly (bin2 poly, bin3 100% => pooled poly) -> T2 = 0.  site1: polymorphic in bins 0,1,2 ; 100% from bin 3 -> T2=3 (post-7000).
    # site2: not eligible (modern polymorphic).
    S = 3
    c = np.full((NB, S), 10, dtype=np.int32)
    a = np.full((NB, S), 10, dtype=np.int32)
    a[2, 0] = 9
    a[0, 1], a[1, 1], a[2, 1] = 8, 9, 9
    a[MOD, 2] = 9
    r = statistic(a, c)
    assert r["E1T2"]["all"][0] == 1 and r["E1T2"]["all"][3] == 1 and sum(r["E1T2"]["all"]) == 2, r["E1T2"]
    assert r["E1T1"]["all"][3] == 2, r["E1T1"]   # T1: unbroken 100% run to the present starts at bin 3 for both sites
    # allele-0 symmetry: complement counts
    r0 = statistic(c - a, c)
    assert r0["E1T2"]["all"] == r["E1T2"]["all"]
    # tracked: zero calls in a bin -> not tracked, not 100%
    c2 = c.copy(); a2 = a.copy(); c2[5, 1] = 0; a2[5, 1] = 0
    r2 = statistic(a2, c2)
    assert r2["E1T2"]["trk"][3] == 0 and r2["E1T2"]["all"][3] == 1
    # pulses conserve share; ancestry composition of R2
    w, aa, s = ancestry_shares("R2", 0)
    assert abs(w + aa + s - 1) < 1e-12 and abs(s - 0.38) < 1e-9 and abs(w - 0.2 * 0.62) < 1e-9
    w9, a9, s9 = ancestry_shares("R2", 9000)
    assert 0.5 < w9 < 0.7, w9
    # drift preserves mean and absorbs
    rng = np.random.default_rng(1)
    x = np.full(100000, 0.3)
    for _ in range(200):
        x = drift(x, 2000, rng)
    assert abs(x.mean() - 0.3) < 0.005 and abs(x.var() / (0.21 * (1 - np.exp(-200 / 2000))) - 1) < 0.05, x.var()
    # depth sampling reproduces the table's mean calls (needs depth json)
    if os.path.exists(DEPTH_JSON):
        depth = load_depth()
        xb = np.full((NB, 20000), 0.5, dtype=np.float32)
        aa_, cc_ = sample_bins(xb, depth, rng)
        for b in range(NB):
            exp = depth[b]["n_ph"] * depth[b]["p_ph"] + 2 * depth[b]["n_dip"] * depth[b]["p_dip"]
            assert abs(cc_[b].mean() - exp) < 0.05 * exp + 1, (b, cc_[b].mean(), exp)
            assert abs(aa_[b].mean() / cc_[b].mean() - 0.5) < 0.02
    print("selftest ok")


# ----------------------------------------------------------------------------------------------- analysis
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


def analyse(rawdir):
    import glob
    files = sorted(glob.glob(os.path.join(rawdir, "c1c_rep*.json")))
    reps = [json.load(open(f)) for f in files]
    names = [k for k in reps[0] if k != "meta"]
    L = []
    P = L.append

    def collect(scen, variant, key, kind):
        out = []
        for r in reps:
            if scen not in r or variant not in r[scen]:
                continue
            for s in r[scen][variant]:
                out.append(np.array(s[key][kind], dtype=float))
        return np.array(out)

    P("reps: %d files %s; NS=%s; sampling reps per file: %d" % (len(reps), [os.path.basename(f) for f in files], reps[0]["meta"]["NS"],
                                                              len(next(v for k, v in reps[0].items() if k != "meta")["base"])))
    P("")
    dep = reps[0]["meta"]["depth"]
    P("## Table 0. Depth from the AADR v62.0 anno (inputs)")
    P("| bin | n anno | n Day | n pseudo-haploid | n diploid | calls/site | chromosomes/site |")
    P("|---|---|---|---|---|---|---|")
    for d in dep:
        P("| %s | %d | %d | %d | %d | %.1f | %.1f |" % (d["bin"], d["n_anno"], d["n_day"], d["n_ph"], d["n_dip"], d["calls_per_site"], d["chrom_per_site"]))
    P("")
    fs_keys = [k for k in reps[0]["meta"] if k.startswith("fst_")]
    P("Source Fst at 10,500 BP (panel; mean over reps): " + "; ".join(
        "%s: %s" % (k, {kk: round(float(np.mean([r['meta'][k][kk] for r in reps])), 3) for kk in ("WA", "WS", "AS")}) for k in fs_keys))
    P("")

    def row(scen, variant="base", E="E1T2"):
        arr = collect(scen, variant, E, "trk")
        arr_all = collect(scen, variant, E, "all")
        if len(arr) == 0:
            return None
        m = arr.mean(axis=0)
        ma = arr_all.mean(axis=0)
        s21 = arr[:, 4:].sum(axis=1)
        s23 = arr[:, 3:].sum(axis=1)
        tot = m.sum()
        tot_all = ma.sum()
        pre = m[:3].sum() / tot if tot > 0 else float("nan")
        l1 = np.abs(m / tot - np.array(OBS) / sum(OBS)).sum() / 2 if tot > 0 else float("nan")
        return dict(m=m, elig_all=tot_all, elig_trk=tot, trk_frac=tot / tot_all if tot_all else float("nan"), pre=pre, l1=l1,
                    s21=s21.mean(), s21_n=len(s21), s21_sum=s21.sum(), s23=s23.mean(), s21_lo=np.percentile(s21, 2.5), s21_hi=np.percentile(s21, 97.5))

    P("## Table 1. Main grid: E1-T2, tracked.  eligible_all = all eligible sites; S21 = events dated 5000-6000 BP or younger; pL = Poisson P(S<=21 | mean)")
    P("| scenario | eligible (all) | eligible (tracked) | tracked frac | pre-7000 share | profile TV dist | S21 mean | [min,max over runs] | S21/21 | pL(21) | S23 |")
    P("|---|---|---|---|---|---|---|---|---|---|---|")
    rows = {}
    for n in names:
        r = row(n)
        if r is None:
            continue
        rows[n] = r
        P("| %s | %.0f | %.0f | %.2f | %.3f | %.2f | %.1f | [%.0f, %.0f] | %.2g | %.2g | %.1f |" % (
            n, r["elig_all"], r["elig_trk"], r["trk_frac"], r["pre"], r["l1"], r["s21"], r["s21_lo"], r["s21_hi"], r["s21"] / 21.0,
            pois_cdf(21, r["s21"]), r["s23"]))
    P("")
    P("Observed (Day): eligible 22,428; tracked 16,299 (0.727); pre-7000 share 0.9986; S21 = 21; S23 = 23. TV dist = total-variation distance of the 11-bin profile shares from the observed profile (0 = identical).")
    P("")
    # Ne* map
    P("## Table 2. Ne* map: constant window Ne at which the mean S21 (tracked, E1-T2) crosses 21 (log-log interpolation)")
    P("| replacement | Ne grid -> S21 | Ne* (S21 = 21) | eligible at Ne* (log interp) |")
    P("|---|---|---|---|")
    nes = [1e4, 2e4, 5e4, 1e5, 3e5, 1e6]
    for R in REPL:
        xs, ys, es = [], [], []
        for ne in nes:
            n = "%s_Ne%g" % (R, ne)
            if n in rows:
                xs.append(ne)
                ys.append(rows[n]["s21"])
                es.append(rows[n]["elig_trk"])
        star, estar = "outside grid", "-"
        for i in range(len(xs) - 1):
            if ys[i] >= 21 >= ys[i + 1] and ys[i + 1] > 0:
                f = (np.log(21) - np.log(ys[i])) / (np.log(ys[i + 1]) - np.log(ys[i]))
                star = "%.3g" % np.exp(np.log(xs[i]) + f * (np.log(xs[i + 1]) - np.log(xs[i])))
                estar = "%.0f" % np.exp(np.log(max(es[i], 1)) + f * (np.log(max(es[i + 1], 1)) - np.log(max(es[i], 1))))
        if ys and ys[-1] > 21:
            star = ">1e6 (S21 still %.0f at 1e6)" % ys[-1]
        if ys and ys[0] < 21:
            star = "<1e4"
        P("| %s | %s | %s | %s |" % (R, "; ".join("%g:%.0f" % (x, y) for x, y in zip(xs, ys)), star, estar))
    P("")
    # Validity gate
    P("## Table 3. Validity gate (pre-registered P3): eligible(all) within 3x of 22,428, pre-7000 share >= 0.90, S21 within [7, 63]")
    P("| scenario | eligible ok | pre-7000 ok | S21 ok | all three |")
    P("|---|---|---|---|---|")
    npass = 0
    for n, r in rows.items():
        e_ok = OBS_ELIG / 3 <= r["elig_all"] <= OBS_ELIG * 3
        p_ok = r["pre"] >= 0.90
        s_ok = 7 <= r["s21"] <= 63
        npass += int(e_ok and p_ok and s_ok)
        P("| %s | %s | %s | %s | %s |" % (n, e_ok, p_ok, s_ok, "PASS" if (e_ok and p_ok and s_ok) else ""))
    P("")
    P("cells passing all three: %d of %d" % (npass, len(rows)))
    P("")
    # profiles
    P("## Table 4. Bin profiles (tracked, E1-T2, mean) for selected scenarios")
    P("| scenario | " + " | ".join(b[0] for b in BINS) + " |")
    P("|---|" + "---|" * NB)
    P("| observed | " + " | ".join(str(o) for o in OBS) + " |")
    for n in ["R0_Ne10000", "R0_Ne100000", "R0_Ne1e+06", "R2_Ne10000", "R2_Ne100000", "R2_Ne1e+06", "R3_Ne100000"]:
        if n in rows:
            P("| %s | " % n + " | ".join("%.1f" % v for v in rows[n]["m"]) + " |")
    P("")
    # all readings for key scenarios
    P("## Table 5. Reading sensitivity (all four readings), tracked S21 / eligible, key scenarios")
    P("| scenario | E1T2 | E2T2 | E1T1 | E2T1 |")
    P("|---|---|---|---|---|")
    for n in names:
        if n.endswith(("Ne10000", "Ne100000", "Ne1e+06")) and n[:2] in ("R0", "R2"):
            cells = []
            for E in ("E1T2", "E2T2", "E1T1", "E2T1"):
                r = row(n, "base", E)
                cells.append("S21 %.0f / elig %.0f / 0-500BP %.0f" % (r["s21"], r["elig_trk"], r["m"][10]))
            P("| %s | %s |" % (n, " | ".join(cells)))
    P("")
    # start frequency
    P("## Table 6. Start-frequency table of the eligible allele (pooled 6000-8000 BP; %) vs Day s4.3 (79.2/20.2/0.5/0.2)")
    P("| scenario | [99,100) | [95,99) | [90,95) | <90 |")
    P("|---|---|---|---|---|")
    for n in names:
        if n.endswith(("Ne10000", "Ne100000", "Ne1e+06")) and n[:2] in ("R0", "R2"):
            st = np.array([s["start"]["all"] for r in reps if n in r for s in r[n]["base"]], dtype=float).mean(axis=0)
            if st.sum() > 0:
                P("| %s | %s |" % (n, " | ".join("%.1f" % v for v in 100 * st / st.sum())))
    P("")
    # variants
    P("## Table 7. Sampling variants (capture heterogeneity kappa, error eps): tracked E1-T2")
    P("| scenario | variant | eligible (all) | tracked frac | pre-7000 | S21 | S21/21 |")
    P("|---|---|---|---|---|---|---|")
    for n in names:
        if "k2" in reps[0][n]:
            for v in ("base", "k2", "k0.5", "e1e-3", "k0.5e1e-3"):
                r = row(n, v)
                if r:
                    P("| %s | %s | %.0f | %.2f | %.3f | %.1f | %.2g |" % (n, v, r["elig_all"], r["trk_frac"], r["pre"], r["s21"], r["s21"] / 21))
    P("")
    # share of S21 in 4000-6000
    P("## Table 8. Where do the post-7000 events fall? share of S23 events in 6000-7000 / 4000-6000 / <4000 BP bins (tracked E1-T2)")
    P("| scenario | S23 | 6000-7000 | 4000-6000 | <4000 | (Day: 2 / 16 / 5 of 23) |")
    P("|---|---|---|---|---|---|")
    for n in names:
        if n.endswith(("Ne10000", "Ne100000", "Ne1e+06")) and n[:2] in ("R0", "R2", "R3"):
            r = rows.get(n)
            if r and r["s23"] > 0:
                m = r["m"]
                tot = m[3:].sum()
                P("| %s | %.1f | %.2f | %.2f | %.2f | |" % (n, tot, m[3] / tot, m[4:6].sum() / tot, m[6:].sum() / tot))
    return "\n".join(L)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if cmd == "depth":
        out = build_depth(sys.argv[2], sys.argv[3])
        for d in out:
            print(d)
    elif cmd == "selftest":
        selftest()
    elif cmd == "run":
        rep = int(sys.argv[2])
        outdir = sys.argv[3] if len(sys.argv) > 3 else os.path.join(HERE, "results", "raw")
        only = set(sys.argv[4].split(",")) if len(sys.argv) > 4 else None
        run_rep(rep, outdir, only)
    elif cmd == "analyse":
        print(analyse(sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "results", "raw")))
