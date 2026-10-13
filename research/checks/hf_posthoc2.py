"""HF second post hoc follow-up (stage `ph2`): long-burn runs at lam 0.8 and 1.6 with the open-locus cap out of reach.
Written 2026-10-13, BEFORE any run of this file (smoke included).

POST HOC.  Written after all of the following had been seen, so nothing here can rescue or sink a pre-registered HF
score, nor a `ph` score:
  * raw/hf_main.jsonl and the scored HF write-up (results/R4-HF.md), including the truncation tau series of the main
    run at R = 1.05 (tau 210 / 361 / 628 / 1,150 / 2,105 at lam 0.0351 to 0.8);
  * raw/hf_ph.jsonl (all 410 rows of stage `ph`), raw/hf_ph_analyse.out, the scored `ph` section of R4-HF.md and
    its fix pass (2026-10-13), in particular the stage L and stage C tables and the post hoc trace table of the
    stage C late window (k/lam over the last 5,000 generations 0.931 / 0.896 at R = 1.05 with the open count still
    rising 2.1-2.4% per 2,500 generations; 0.990 / 0.981 at R = 1.111, K = 1000; 0.991 / 0.981 at K = 4000;
    trunc R = 1.05, lam 1.6: 0.986, +1.8%);
  * while writing this file: the `sec` and `maxrss_mb` fields of the L and C rows per host, and the open counts of
    the stage C traces (rep 0) every 2,500 generations.
It decides item 1 of "Open after `ph`" in R4-HF.md:
  Q1  at R = 1.05, K = 1000: are lam 0.8 and 1.6 sustained by softJ, and by truncation, once the burn is long enough?
  Q2  at R = 1.111: does K = 4000 sustain the same rate as K = 1000 at lam 0.8 and 1.6 (DA2 "the soft limit does not
      grow with K", restated in `ph` as "K = 4000 sustains less, not explained by the fill lag"; critic side "no K
      effect beyond the lag")?
  Q3  does sweep residence time tau keep rising with lam (the Day-side latency point of the `ph` fix pass)?

ENGINE.  `run()` is imported from hf_posthoc.py (md5 5f571634461d29ce0e60722cbc77da37, pre-registered 5c30ed9), which
imports hf_followups.py (md5 446323c4c82f821991d12ec0c2dd431e); neither file is changed.  `smoke` reruns two `ph` jobs
(softJ cell 4 rep 0; trunc cell 68 rep 0) through THIS file's job() with their original seed [20261011, 2, cell, rep]
and requires every field to equal raw/hf_ph.jsonl except `sec` (run time) and `maxrss_mb` (memory of the worker: it
depends on the host and on what the worker ran before, and hf_posthoc.py merge excludes it for the same reason).
Seeds of this stage: SeedSequence([20261013, 3, cell, rep]).  Free recombination, K adults, s per ancestral copy.

NO EXTINCTION IN THESE MODES.  softJ (mode "mix", h = 0) draws J = R N juveniles and keeps K of them by weighted
sampling; truncation keeps the best K of R K.  N = K in every generation, so neither can go extinct in this model:
the run measures sweep speed (tau) and backlog, NOT load, and no result here bears on whether a real population
could pay the cost (Day-1 / steelman-day #1 stands whatever the outcome).

CELLS (cell = part, K, s, b, lam, R, mode, h, label, reps, gens, burn, max_open, g); s = 0.01, b = 0, g = 1
   0, 1  softJ  R = 1.05   K = 1000  lam 0.8, 1.6   4 reps  120,000 generations, 60,000 burn
   2, 3  softJ  R = 1.111  K = 1000  lam 0.8, 1.6   4 reps   80,000 / 40,000
   4     softJ  R = 1.111  K = 4000  lam 0.8        4 reps   80,000 / 40,000
   5     softJ  R = 1.111  K = 4000  lam 1.6        3 reps   80,000 / 40,000   (3, not 4: about 60 h per run)
   6, 7  trunc  R = 1.05   K = 1000  lam 0.8 (control: the main run passed it), 1.6   4 reps   80,000 / 40,000
  8 cells, 31 jobs.  max_open = 40,000 in every cell.  Expected steady open counts are 1,700 to 14,500 (below);
  the largest count seen in stage C was 13,096 and rising, so 20,000 could bind at R = 1.05, lam 1.6 if tau there is
  longer than expected; 40,000 is 2.7x the largest expected count.  The R = 1.05 softJ cells get a longer horizon
  because their residence time (expected 8,000 to 9,000, possibly more) makes a 40,000 burn only 4 tau; 60,000 is
  about 6.5 tau.  No cell was dropped or shrunk for cost; the only cost concession is 3 reps in cell 5.

COST (from `sec` of the workhorse rows of raw/hf_ph_wh.jsonl, 11 busy workers: 6.0e-5 to 6.5e-5 s per generation per
open locus per 1,000 adults; 6.5e-5 used), with expected steady open count n = lam x tau:
  cell  n        s per job   h per job  jobs  CPU-h
   0     6,500     50,700     14.1       4     56
   1    14,500    113,100     31.4       4    126
   2     3,760     19,600      5.4       4     22
   3     8,100     42,100     11.7       4     47
   4     4,750     98,800     27.4       4    110
   5    10,300    214,200     59.5       3    179
   6     1,680      8,700      2.4       4     10
   7     6,200     32,200      9.0       4     36
  Total about 585 CPU-h.  10 workers on na-workhorse (12 threads, 14 GB), dearest job first: wall about 60 h (set by
  the three cell-5 jobs).  Peak RSS per worker: measured 385 MB at K = 4000 with 10,400 loci open (stage C) and
  about 220 MB at K = 1000 with 13,000 open; planned <= 450 MB (K = 4000) and <= 250 MB (K = 1000), total about
  3.5 GB.  Worst case, if runs climb to the cap of 40,000: 1.1 to 1.5 GB per K = 4000 worker (G and its offspring
  array are 40,000 x 8,000 and x 8,889 bytes, with transient copies), under 0.5 GB per K = 1000 worker; the three
  cell-5 jobs and the four cell-1 jobs all at the cap would be about 6.5 GB, the rest about 1.5 GB: under 11 GB.
  (The four cell-4 jobs reaching 40,000 open would need tau near 50,000, eight times the expectation; whoever
  collects should check `free` once if the log shows open counts above 20,000 at K = 4000.)  Jobs are not checkpointed: a host reboot loses the jobs in flight (finished jobs are kept and
  skipped on relaunch).

RULES (unchanged from HF and `ph`; fixed before any run)
  HF's pre-registered steady rule over the recorded window [burn, gens): no failure, k/lam >= 0.9,
  nopen_q4 / nopen_q1 <= 1.15.  Beside it the reviews' stricter rule: k/lam >= 0.95 and q4/q1 <= 1.10.
  lam_max = largest lam with >= 50% of runs passing; tau = nopen / k.
  Late-window columns (the fix pass's trace table, from the trace every 250 generations): kq4/lam = fixation rate
  over the last quarter of the run relative to supply; kq3/lam = the same over the third quarter; dn2500 = relative
  change in the open count over the last 2,500 generations; open count at the end and its peak.
  Accounting identity of the engine: a locus leaves only by fixing (a lost allele is re-seeded), so
  open(t) = arrivals(t) - fixations(t) exactly.  A rate below supply IS a rising open count; "rate below supply
  with a flat open count" cannot occur.  What separates a fill lag from a limit is therefore whether the shortfall
  shrinks: under a lag kq4/lam > kq3/lam and both go to 1; under a limit the shortfall persists or grows and the
  run ends in a backlog.  "Persistent shortfall" below means: cell-mean kq4/lam < 0.95 and kq4/lam - kq3/lam <= 0.01,
  or a backlog failure in at least half of the runs.

PREDICTIONS (post hoc; cell means unless stated; every one can fail)
  Day side (the latency limit is a throughput limit at high supply):
    DP1  softJ R = 1.05, lam 1.6 falls short: fewer than half of its runs pass HF's rule, or it shows a persistent
         shortfall, with k/lam lower at lam 1.6 than at 0.8.
    DP2  restated DA2: at R = 1.111, K = 4000 sustains less than K = 1000: at lam 0.8 or 1.6 fewer than half of the
         K = 4000 runs pass HF's rule where at least half of the K = 1000 runs pass, or k/lam and kq4/lam are both
         lower at K = 4000 by more than 0.02.
    The Day side as the task stated it is "at least one of DP1, DP2, with a late-window rate below 0.95 of supply
    not attributable to an unfilled pipeline"; scored as DP1 or DP2 above (see the accounting identity).
    DP3  latency: tau(1.6) / tau(0.8) >= 1.10 in the softJ R = 1.05 series, and tau at lam 0.8 exceeds the stage L
         value at lam 0.4 in all three softJ series (7,385; 4,508; 5,693).
  Critic side (a fill lag, no limit in this range):
    CP1  every run passes HF's rule (31 of 31), so lam_max is 1.6+ in all four series.
    CP2  K = 4000 equals K = 1000 at R = 1.111 within noise: |difference in k/lam| <= 0.02 at lam 0.8 and at 1.6.
    CP3  the rise of tau with lam costs no throughput: k/lam >= 0.95 in every cell.
  Audit (extrapolated from stage L at lam 0.4, the stage C end counts plus the remaining shortfall, and the main
  run's truncation series):
    A1  k/lam in [0.97, 1.03] and q4/q1 in [0.95, 1.05] in every cell; all runs pass both rules (allowing 2 of 31
        single-run misses of the strict rule, the rate seen in stage L).
    A2  tau (generations):   softJ R = 1.05:        lam 0.8 [7,600, 8,800];  lam 1.6 [8,300, 10,300]
                             softJ R = 1.111 K=1000: lam 0.8 [4,550, 4,950];  lam 1.6 [4,850, 5,400]
                             softJ R = 1.111 K=4000: lam 0.8 [5,750, 6,200];  lam 1.6 [6,150, 6,800]
                             trunc R = 1.05:         lam 0.8 [1,950, 2,300];  lam 1.6 [3,600, 4,300]
    A3  tau(1.6) / tau(0.8) in [1.03, 1.20] in each softJ series (rising, far from proportional) and in [1.6, 2.0]
        for truncation (near proportional to lam).
    A4  late window: kq4/lam in [0.97, 1.03] and |dn2500| <= 3% in every cell.
    A5  K: |k/lam(K = 4000) - k/lam(K = 1000)| <= 0.02 at both lam (as CP2); tau(K = 4000) / tau(K = 1000) in
        [1.20, 1.35] at both lam.
    A6  no backlog; the peak open count over all runs is below 17,000 (so max_open = 40,000 does not bind).
  The audit's `ph` prediction PC-1 (b) (1.6 sustained on the rule at the 20k horizon) missed; A1 is the same
  expectation at a horizon where it should hold, and is recorded as such.

WHAT EACH OUTCOME CHANGES.  No verdict VALUE can move: H, H8 (Term 3 as a rate bound) and H5 stay external
`contested` whatever happens, because the realised rate in every such cell already exceeds 1/300 by two orders of
magnitude and the open questions on h, R and the uncharged cost are untouched.  Only verdict TEXT can change:
  * CP1-CP3 / A1 hold: in H, H8, H5 the clause "the rate is limited only by sweep latency and the open-locus cap"
    stands with "sustained to 1.6 per generation at R = 1.05 and 1.111 on a long burn" and the measured tau and open
    counts replacing "4,300 to 9,300 generations" and "3,600 to 11,800 loci"; the R4-HF sentence "0.8 and 1.6
    remain not shown at R = 1.05" is withdrawn; DA2 and PA4 keep "hold by the letter at the 20k horizon" with "the
    one-step difference was the fill lag" now tested on a new run instead of a trace reading.
  * DP1 holds: the clause gains a measured ceiling, "at R = 1.05 purely relative selection does not sustain 1.6 per
    generation (latency limit between 0.8 and 1.6)", credited to Day's side; the cap is still about 240x 1/300.
  * DP2 holds: DA2 is supported in its restated form and the text records "the sustained rate falls with K between
    1,000 and 4,000 at R = 1.111"; PA4's softJ half is then re-scored.
  * DP3 / A3: the latency sentence of the fix pass ("residence time keeps rising with the number of concurrent
    sweeps") is kept, sharpened or withdrawn according to the measured ratios.
  * An audit band missed is reported as a miss beside the side it favoured.

USAGE  (Python only as research/.venv/bin/python -I; heavy modes on na-workhorse only)
  hf_posthoc2.py plan            cells, jobs, estimated cost (no simulation)
  hf_posthoc2.py smoke           engine identity (2 `ph` jobs, original seeds) -> raw/hf_ph2_smoke.jsonl, then
                                 `analyse` code exercised on a 2-job miniature of stage ph2 (not part of the run)
  [HF_SHARD=x] hf_posthoc2.py ph2 W   run the jobs not yet present in any raw/hf_ph2_*.jsonl (W workers, dearest
                                 first), appending to raw/hf_ph2_<shard>.jsonl (shard default "wh").  Resumable.
  hf_posthoc2.py merge           union of raw/hf_ph2_*.jsonl (not smoke) -> raw/hf_ph2.jsonl, overlaps identity-checked
  hf_posthoc2.py analyse [file]  tables from raw/hf_ph2.jsonl (the columns of hf_posthoc.py analyse plus the
                                 late-window columns)
"""
import collections
import glob
import json
import os
import resource
import sys
import time
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import hf_posthoc as PH  # noqa: E402  (engine run(), build('ph'), ok_steady)

HF = PH.HF
RAW = PH.RAW
RH = PH.RH
SEED2, CODE2 = 20261013, 3
MO2 = 40000
COST = 6.5e-5            # s per generation per open locus per 1,000 adults (workhorse, 11 busy workers)
TAU_EXP = {("mix", 1000, 1.05, 0.8): 8125, ("mix", 1000, 1.05, 1.6): 9060,
           ("mix", 1000, RH, 0.8): 4700, ("mix", 1000, RH, 1.6): 5060,
           ("mix", 4000, RH, 0.8): 5940, ("mix", 4000, RH, 1.6): 6440,
           ("trunc", 1000, 1.05, 0.8): 2100, ("trunc", 1000, 1.05, 1.6): 3875}
TAU_L04 = {("mix", 1000, 1.05): 7385, ("mix", 1000, round(RH, 4)): 4508, ("mix", 4000, round(RH, 4)): 5693}


def build(stage="ph2"):
    c = []
    if stage == "mini":      # exercises job/merge/analyse code only; never part of the run
        c.append(("P2mini", 200, 0.01, 0.0, 0.8, RH, "mix", 0.0, "softJ", 1, 4000, 2000, MO2, 1.0))
        c.append(("P2mini", 200, 0.01, 0.0, 1.6, RH, "mix", 0.0, "softJ", 1, 4000, 2000, MO2, 1.0))
        return c
    assert stage == "ph2"
    for lam in (0.8, 1.6):
        c.append(("P2", 1000, 0.01, 0.0, lam, 1.05, "mix", 0.0, "softJ", 4, 120000, 60000, MO2, 1.0))
    for lam in (0.8, 1.6):
        c.append(("P2", 1000, 0.01, 0.0, lam, RH, "mix", 0.0, "softJ", 4, 80000, 40000, MO2, 1.0))
    c.append(("P2", 4000, 0.01, 0.0, 0.8, RH, "mix", 0.0, "softJ", 4, 80000, 40000, MO2, 1.0))
    c.append(("P2", 4000, 0.01, 0.0, 1.6, RH, "mix", 0.0, "softJ", 3, 80000, 40000, MO2, 1.0))
    for lam in (0.8, 1.6):
        c.append(("P2", 1000, 0.01, 0.0, lam, 1.05, "trunc", 0.0, "trunc", 4, 80000, 40000, MO2, 1.0))
    return c


def job(a):
    """a = (seed base, seed code, cell index, cell, rep).  Same row fields as hf_posthoc.job, plus `stage`."""
    base, code, ci, cell, rep = a
    part, K, s, b, lam, R, mode, h, lab, reps, gens, burn, mo, g = cell
    rng = np.random.default_rng(np.random.SeedSequence([base, code, ci, rep]))
    t0 = time.time()
    r = PH.run(K, s, b, lam, R, mode, h, gens, burn, rng, max_open=mo, g=g)
    r.update(dict(part=part, cell=ci, K=K, s=s, b=b, lam=lam, R=R, mode=mode, h=h, g=g, label=lab, rep=rep,
                  gens=gens, burn=burn, max_open=mo, sec=time.time() - t0,
                  maxrss_mb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024))
    return r


def est_cost(cell):
    part, K, s, b, lam, R, mode, h, lab, reps, gens, burn, mo, g = cell
    tau = TAU_EXP.get((mode, K, R, lam), 5000)
    return COST * gens * lam * tau * K / 1000


def all_jobs():
    jobs = [(SEED2, CODE2, ci, cell, rep) for ci, cell in enumerate(build()) for rep in range(cell[9])]
    jobs.sort(key=lambda j: -est_cost(j[3]))
    return jobs


def run_files():
    return sorted(p for p in glob.glob(os.path.join(RAW, "hf_ph2_*.jsonl"))
                  if not os.path.basename(p).startswith(("hf_ph2_smoke", "hf_ph2_mini")))


def done_set():
    done = set()
    for p in run_files():
        for line in open(p):
            d = json.loads(line)
            done.add((d["cell"], d["rep"]))
    return done


def plan():
    cells = build()
    print("| cell | mode | K | R | lam | reps | gens | burn | est. h per job | est. CPU-h |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for ci, c in enumerate(cells):
        e = est_cost(c) / 3600
        print(f"| {ci} | {c[8]} | {c[1]} | {c[5]:.3f} | {c[4]} | {c[9]} | {c[10]} | {c[11]} | {e:.1f} | {e * c[9]:.0f} |")
    jobs = all_jobs()
    print(f"{len(cells)} cells, {len(jobs)} jobs, est. CPU-h {sum(est_cost(j[3]) for j in jobs) / 3600:.0f}, "
          f"longest job {est_cost(jobs[0][3]) / 3600:.1f} h; already done {len(done_set())}")


def run_stage(workers):
    sh = os.environ.get("HF_SHARD", "wh")
    jobs = all_jobs()
    done = done_set()
    todo = [j for j in jobs if (j[2], j[4]) not in done]
    path = os.path.join(RAW, f"hf_ph2_{sh}.jsonl")
    print(f"stage ph2 shard {sh}: {len(build())} cells, {len(jobs)} jobs, {len(todo)} to run, workers {workers}; "
          f"est. CPU-h {sum(est_cost(j[3]) for j in todo) / 3600:.0f}", flush=True)
    t0 = time.time()
    with Pool(workers) as pool, open(path, "a") as fh:
        for i, r in enumerate(pool.imap_unordered(job, todo, chunksize=1)):
            r["stage"] = "ph2"
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            os.fsync(fh.fileno())
            print(f"[{time.time() - t0:7.0f}s] {i + 1}/{len(todo)} {r['label']} K={r['K']} R={r['R']:.3f} "
                  f"lam={r['lam']:.4g} rep{r['rep']} fail={r['fail']}@{r['t_fail']} k/lam={r['k'] / r['lam']:.3f} "
                  f"nopen={r['nopen']:.0f} sec={r['sec']:.0f} rss={r['maxrss_mb']:.0f}MB", flush=True)
    print(f"stage ph2 shard {sh} done in {time.time() - t0:.0f} s", flush=True)


def smoke():
    """Engine identity: two `ph` jobs through this file's job() with their original seeds; then the mini stage."""
    ph_cells = PH.build("ph")
    ref = {}
    for d in map(json.loads, open(os.path.join(RAW, "hf_ph.jsonl"))):
        if (d["cell"], d["rep"]) in ((4, 0), (68, 0)):
            ref[(d["cell"], d["rep"])] = d
    assert len(ref) == 2, "reference rows (4,0) and (68,0) not found in raw/hf_ph.jsonl"
    picks = [(PH.SEED, 2, ci, ph_cells[ci], 0) for ci in (4, 68)]
    ok = True
    t0 = time.time()
    with Pool(2) as pool:
        rows = pool.map(job, picks, chunksize=1)
    for r in rows:
        d = ref[(r["cell"], r["rep"])]
        skip = ("sec", "maxrss_mb")
        keys = (set(r) | set(d)) - set(skip)
        diff = {k: (r.get(k), d.get(k)) for k in keys if json.dumps(r.get(k)) != json.dumps(d.get(k))}
        ok &= not diff
        print(f"identity ph cell {r['cell']} rep 0 {r['label']} K={r['K']} R={r['R']:.3f} lam={r['lam']:.4g} "
              f"gens={r['gens']}: {len(keys)} fields compared (trace {len(r['trace'])} points), "
              f"{'OK' if not diff else {k: str(v)[:120] for k, v in diff.items()}} "
              f"(sec {r['sec']:.0f} vs {d['sec']:.0f}; rss {r['maxrss_mb']:.0f} MB)", flush=True)
    print("ENGINE IDENTITY:", "PASS" if ok and len(rows) == 2 else "FAIL", f"({time.time() - t0:.0f} s)", flush=True)
    with open(os.path.join(RAW, "hf_ph2_smoke.jsonl"), "w") as fh:
        for r in rows:
            fh.write(json.dumps(r) + "\n")
    mini = os.path.join(RAW, "hf_ph2_mini.jsonl")
    with open(mini, "w") as fh:
        for ci, c in enumerate(build("mini")):
            r = job((SEED2, 9, ci, c, 0))
            r["stage"] = "mini"
            fh.write(json.dumps(r) + "\n")
    print("\nmini stage (K = 200, 4,000 generations; code path only, not a result):", flush=True)
    analyse(mini)
    if not ok:
        raise SystemExit(1)


def merge():
    rows, src = {}, {}
    nboth = mism = 0
    for fp in run_files():
        for d in map(json.loads, open(fp)):
            k = (d["cell"], d["rep"])
            strip = json.dumps({a: v for a, v in d.items() if a not in ("sec", "maxrss_mb")}, sort_keys=True)
            if k in rows:
                nboth += 1
                mism += strip != rows[k][0]
                continue
            rows[k] = (strip, d)
            src[k] = os.path.basename(fp)
    exp = {(ci, rep) for ci, c in enumerate(build()) for rep in range(c[9])}
    print(f"merged {len(rows)} unique of {len(exp)} expected; missing {len(exp - set(rows))}; extra "
          f"{len(set(rows) - exp)}; on two files {nboth}, mismatches {mism}; by file "
          f"{dict(collections.Counter(src.values()))}")
    with open(os.path.join(RAW, "hf_ph2.jsonl"), "w") as fh:
        for k in sorted(rows):
            fh.write(json.dumps(rows[k][1]) + "\n")


# ------------------------------------------------------------------------------------------------ analysis
def late(r):
    """kq3/lam, kq4/lam (third and last quarter of the run), dn2500, open count at the end, peak open count.
    None for the window values if the run failed before its end."""
    tr = {x[0]: x for x in r["trace"]}
    peak = max(x[1] for x in r["trace"])
    T = r["gens"]
    if r["fail"] is not None or T not in tr:
        return None, None, None, None, peak
    a, b, c = T // 2, 3 * T // 4, T - 2500
    q = T - b
    kq3 = (tr[b][2] - tr[a][2]) / (b - a) / r["lam"]
    kq4 = (tr[T][2] - tr[b][2]) / q / r["lam"]
    dn = tr[T][1] / max(tr[c][1], 1) - 1
    return kq3, kq4, dn, tr[T][1], peak


def mean(xs):
    xs = [x for x in xs if x is not None]
    return float(np.mean(xs)) if xs else float("nan")


def analyse(path=None):
    rows = [json.loads(l) for l in open(path or os.path.join(RAW, "hf_ph2.jsonl"))]
    print(f"rows {len(rows)}; peak worker RSS {max(r['maxrss_mb'] for r in rows):.0f} MB; "
          f"CPU-h {sum(r['sec'] for r in rows) / 3600:.1f}; HF rule passes {sum(PH.ok_steady(r) for r in rows)} of "
          f"{len(rows)}; strict {sum(PH.ok_steady(r, True) for r in rows)}; backlog "
          f"{sum(r['fail'] == 'backlog' for r in rows)}; peak open count {max(late(r)[4] for r in rows)}")
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["mode"], r["K"], round(r["R"], 4), r["lam"])].append(r)
    series = collections.defaultdict(list)
    for k, v in g.items():
        series[k[:3]].append((k[3], v))
    summ = {}
    for key in sorted(series, key=str):
        mode, K, R = key
        pts = sorted(series[key])
        v0 = pts[0][1][0]
        print(f"\n## {v0['label']} ({mode}) K={K} s={v0['s']} R={R} gens={v0['gens']} burn={v0['burn']} "
              f"max_open={v0['max_open']}")
        print("| lam | HF rule | strict rule | fails (type@t) | k/lam | q4/q1 | nopen | tau = nopen/k | maxrel | D | RSS MB "
              "| kq3/lam | kq4/lam (last quarter) | dn2500 | open at end | peak open | k/lam per run |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        frs = []
        for lam, v in pts:
            n = len(v)
            a = sum(PH.ok_steady(r) for r in v)
            st = sum(PH.ok_steady(r, True) for r in v)
            frs.append((lam, a / n))
            fl = ",".join(f"{r['fail']}@{r['t_fail']}" for r in v if r["fail"]) or "-"
            kl = mean([r["k"] / lam for r in v])
            qr = mean([r["nopen_q4"] / max(r["nopen_q1"], 1e-9) for r in v])
            nop = mean([r["nopen"] for r in v])
            tau = mean([r["nopen"] / r["k"] for r in v if r["k"] > 0])
            lw = [late(r) for r in v]
            k3, k4, dn, end = (mean([x[i] for x in lw]) for i in range(4))
            pk = max(x[4] for x in lw)
            summ[key + (lam,)] = dict(kl=kl, qr=qr, tau=tau, k3=k3, k4=k4, dn=dn, pas=a / n)
            print(f"| {lam:.4g} | {a}/{n} | {st}/{n} | {fl} | {kl:.3f} | {qr:.3f} | {nop:.0f} | {tau:.0f} | "
                  f"{mean([r['maxrel'] for r in v]):.2f} | {float(np.nanmean([r['D'] for r in v])):.1f} | "
                  f"{max(r['maxrss_mb'] for r in v):.0f} | {k3:.3f} | {k4:.3f} | {100 * dn:+.1f}% | {end:.0f} | {pk} | "
                  + " ".join(f"{r['k'] / lam:.3f}" for r in sorted(v, key=lambda r: r["rep"])) + " |")
        lmax = max([lam for lam, f in frs if f >= 0.5], default=float("nan"))
        nxt = [lam for lam, f in frs if lam > lmax] if lmax == lmax else [frs[0][0]]
        capped = bool(nxt) and any(r["fail"] == "backlog" for r in dict(pts)[min(nxt)])
        top = lmax == pts[-1][0]
        t3 = HF.lam_T3(R, K)
        print(f"lam_max {lmax:.4g}{'+' if top else ''}{' (cap: next lam backlogs)' if capped else ''}; "
              f"x Term3 {lmax / t3:.1f}; x 1/300 {lmax * 300:.0f}")
        lams = [p[0] for p in pts]
        if len(lams) == 2:
            lo, hi = summ[key + (lams[0],)], summ[key + (lams[1],)]
            l04 = TAU_L04.get(key)
            print(f"tau({lams[1]}) / tau({lams[0]}) = {hi['tau'] / lo['tau']:.3f}; k/lam {lo['kl']:.3f} -> {hi['kl']:.3f}; "
                  f"kq4 - kq3: {lo['k4'] - lo['k3']:+.3f}, {hi['k4'] - hi['k3']:+.3f}"
                  + (f"; tau({lams[0]}) / stage L tau(0.4) = {lo['tau'] / l04:.3f}" if l04 else ""))
    print("\n## K = 4000 against K = 1000 (softJ, R = 1.111)")
    for lam in (0.8, 1.6):
        a, b = summ.get(("mix", 1000, round(RH, 4), lam)), summ.get(("mix", 4000, round(RH, 4), lam))
        if a and b:
            print(f"lam {lam}: k/lam {b['kl']:.3f} against {a['kl']:.3f} (difference {b['kl'] - a['kl']:+.3f}); kq4/lam "
                  f"{b['k4']:.3f} against {a['k4']:.3f} ({b['k4'] - a['k4']:+.3f}); tau ratio {b['tau'] / a['tau']:.3f}; "
                  f"HF rule share {b['pas']:.2f} against {a['pas']:.2f}")


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "plan"
    if which == "plan":
        plan()
    elif which == "smoke":
        smoke()
    elif which == "ph2":
        run_stage(int(sys.argv[2]) if len(sys.argv) > 2 else 3)
    elif which == "merge":
        merge()
    elif which == "analyse":
        analyse(sys.argv[2] if len(sys.argv) > 2 else None)
    else:
        raise SystemExit("usage: plan | smoke | ph2 W | merge | analyse [file]")
