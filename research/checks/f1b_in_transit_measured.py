"""F1b -- MEASURE the number of fixations in transit directly (not Little's law as an identity).

THROWAWAY research check (queue item 3); follow-up to f1_throughput.py (F1; RESULTS.md: "In-transit count, computed, not
measured ... track_transit is unused. Measuring it directly is a TODO").  Reuses wf.kimura_u and wf.diffusion_cond_fix_time.
Run on na-workhorse only:
    research/.venv/bin/python -I research/checks/f1b_in_transit_measured.py smoke
    research/.venv/bin/python -I research/checks/f1b_in_transit_measured.py main <workers>
    research/.venv/bin/python -I research/checks/f1b_in_transit_measured.py analyse [rawdir]

TARGET CLAIMS.  F1 (Mansfield latency vs throughput; his truck/pipelining comment), F1b (McCarthy, "Vox Day Responds" para 22:
"Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time."),
F1a (Day: G_f is a throughput that already includes parallelism; 19,800 from a latency formula), B6c/G2c (the serial reading).
Day's weak form as recorded in F1's pre-registered prediction: "Count <= window / latency".

WHAT IS MEASURED.  Infinite-sites Wright-Fisher, N diploid (M=2N copies), independent loci (no interference, no cost of
selection: F2/H cover those), genic s, beneficial mutations at rate Ub per gamete per generation.  Every allele carries an id
and birth generation.  When an allele fixes at generation g its birth b is known, so it was "in transit" (born, destined to
fix) at every generation in [b, g-1].  The time series L(t) = number of alleles in transit at t is accumulated post hoc by a
difference array over ALL alleles that fixed; no formula is used.  L is averaged over a window that excludes the start (burn-in
1x) and the last 4,000 generations (right-censoring: alleles born then and not yet fixed).  Also measured:
latency of each fixation, fixations per generation lambda_hat, mean latency W_hat, and the segregating-allele count with no
hindsight.  Little's law is then a COMPARISON (L_direct vs lambda_hat x W_hat), not an input.

CELLS (N=1000, s=0.01, 30,000 generations: 5,000 burn-in, 21,000 measured window, last 4,000 excluded as tail):
  A  Ub=0.01      (F1's cell: predicted rate 0.3960, t_fix 847; ~336 in transit)
  B  Ub=0.0005    (rate ~0.0198, ~17 in transit; G_f ~50 << latency)
  C  Ub=0.00003   (rate ~0.0012, ~1.0 in transit; the serial boundary: G_f ~ latency)
Replicates: 12 (A), 24 (B), 96 (C).

PRE-REGISTERED PREDICTIONS (arithmetic from F1's constants; written before any run):
  P1  Cell A: mean L_direct within 5% of lambda_hat x W_hat and within 8% of 335 (= 0.3960 x 847).
  P2  Variance-to-mean of L(t) in [0.7, 1.6] in every cell (arrivals of eventual fixers are Poisson; M/G/infinity).
  P3  Cell A: min over generations of L(t) >= 230 (mean 335, sd ~18); fixers born in the 21,000-generation window ~ 8,300
      (0.396 x 21,000) vs the serial cap window/latency = 24.8: ratio > 100 (expected ~330).
  P4  Cell B: mean L in [15, 19]; fraction of generations with L >= 2 greater than 0.999; fixations / serial cap greater than 15.
  P5  Cell C (serial boundary): mean L in [0.8, 1.3]; fixations / serial cap in [0.75, 1.35]; fraction of generations with L >= 2
      in [0.15, 0.40] (Poisson(1.0): 0.26).  So even at the boundary where throughput equals window/latency, overlap is
      common; the weak form "count <= window/latency" is an equality there, not a bound.
  P6  Day's weak form "count <= window / latency" is violated in A and B by the measured counts (Day-side: it was never a
      claim about the no-cost, no-interference regime; its feasibility argument is F2/H, untested here).

WHAT EACH SIDE'S MODEL PREDICTS.
  Critics (Mansfield, McCarthy): many fixations in flight at once; L_direct ~ rate x latency; count >> window/latency when
    mutation supply is high (P1-P4).
  Day: G_f is a throughput that already includes parallelism (F1a), so he does not predict a serial cap on count; his weak form
    (count <= window / latency) is falsified here only in the free regime; his strong claim is feasibility at realistic
    parameters, where the supply is low (cell C is the nearest) or interference/cost bind.  This check does NOT address that.
  RESULT THAT WOULD CHANGE A VERDICT: L_direct deviating from lambda_hat x W_hat by more than 10% (then the Little's-law
    reading in RESULTS F1 would be wrong), or L(t) variance far from Poisson.

Raw output: research/checks/results/raw/f1b_<cell>.json (per-replicate summaries).
"""
import os
import sys
import json
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np
from wf import kimura_u, diffusion_cond_fix_time

N, S = 1000, 0.01
BURN, WIN, TAIL = 5000, 25000, 4000
CELLS = {"A": (0.01, 12), "B": (0.0005, 24), "C": (0.00003, 96)}
SEED = 20261012


def one_run(Ub, seed, burn=BURN, win=WIN, tail=TAIL):
    rng = np.random.default_rng(seed)
    M = 2 * N
    Ttot = burn + win
    counts = np.empty(0, dtype=np.int64)
    birth = np.empty(0, dtype=np.int64)
    diff = np.zeros(Ttot + 2, dtype=np.int64)
    fix_g, fix_b = [], []
    nseg = np.zeros(Ttot, dtype=np.int32)
    for g in range(Ttot):
        new = rng.poisson(M * Ub)
        if new:
            counts = np.concatenate([counts, np.ones(new, dtype=np.int64)])
            birth = np.concatenate([birth, np.full(new, g, dtype=np.int64)])
        p = counts / M
        p = p * (1 + S) / (1 + S * p)
        counts = rng.binomial(M, p)
        fx = counts == M
        if fx.any():
            for b in birth[fx]:
                fix_g.append(g)
                fix_b.append(int(b))
                diff[b] += 1
                diff[g] -= 1
        keep = (counts > 0) & (counts < M)
        counts, birth = counts[keep], birth[keep]
        nseg[g] = len(counts)
    L = np.cumsum(diff[:Ttot])
    lo, hi = burn, Ttot - tail
    Lw = L[lo:hi]
    fg, fb = np.array(fix_g), np.array(fix_b)
    inwin = (fg >= lo) & (fg < hi)
    # arrivals: alleles BORN in the window that eventually fix (tail of 4,000 gens makes right-censoring negligible)
    sel = (fb >= lo) & (fb < hi)
    lat = (fg[sel] - fb[sel]).astype(float)
    nwin = hi - lo
    lam = sel.sum() / nwin
    W = float(lat.mean()) if len(lat) else float("nan")
    return dict(L_mean=float(Lw.mean()), L_var=float(Lw.var()), L_min=int(Lw.min()), L_max=int(Lw.max()),
                frac_ge2=float((Lw >= 2).mean()), frac_ge1=float((Lw >= 1).mean()), n_fix=int(sel.sum()), n_fix_fixing_in_window=int(inwin.sum()),
                lam_hat=float(lam), W_hat=W, little=float(lam * W) if len(lat) else float("nan"),
                nseg_mean=float(nseg[lo:hi].mean()), window=int(nwin))


def _job(a):
    cell, rep, Ub = a
    t0 = time.time()
    r = one_run(Ub, np.random.SeedSequence([SEED, ord(cell), rep]))
    r.update(cell=cell, rep=rep, secs=time.time() - t0)
    return r


def main(workers, smoke=False):
    import multiprocessing as mp
    jobs = []
    for cell, (Ub, nrep) in CELLS.items():
        for rep in range(2 if smoke else nrep):
            jobs.append((cell, rep, Ub))
    out = {c: [] for c in CELLS}
    with mp.get_context("spawn").Pool(workers) as pool:
        for r in pool.imap_unordered(_job, jobs):
            out[r["cell"]].append(r)
            print(r["cell"], r["rep"], "L=%.2f little=%.2f nfix=%d (%.0fs)" % (r["L_mean"], r["little"], r["n_fix"], r["secs"]), flush=True)
    od = os.path.join(HERE, "results", "raw" if not smoke else os.path.join("raw", "smoke_f1b"))
    os.makedirs(od, exist_ok=True)
    for c, v in out.items():
        with open(os.path.join(od, "f1b_%s.json" % c), "w") as fh:
            json.dump(v, fh)
    analyse(od)


def analyse(rawdir):
    lat = diffusion_cond_fix_time(N, S)
    for c, (Ub, _) in CELLS.items():
        p = os.path.join(rawdir, "f1b_%s.json" % c)
        if not os.path.exists(p):
            continue
        v = json.load(open(p))
        rate_pred = 2 * N * Ub * kimura_u(N, S)
        g = lambda k: np.array([x[k] for x in v], dtype=float)
        L, lit = g("L_mean"), g("little")
        win = v[0]["window"]
        cap = win / lat
        print("cell %s Ub=%g reps=%d: pred rate %.5f (G_f %.0f), diffusion latency %.0f, pred L=%.2f" % (c, Ub, len(v), rate_pred, 1 / rate_pred, lat, rate_pred * lat))
        print("   L_direct = %.3f +- %.3f ; lambda_hat*W_hat = %.3f ; ratio L/little = %.3f ; W_hat = %.0f ; lambda_hat = %.5f" %
              (L.mean(), L.std(ddof=1) / np.sqrt(len(L)), np.nanmean(lit), L.mean() / np.nanmean(lit), np.nanmean(g("W_hat")), g("lam_hat").mean()))
        print("   var/mean of L(t) = %.3f ; min L = %d ; max L = %d ; frac(L>=1) = %.4f ; frac(L>=2) = %.4f" %
              ((g("L_var") / g("L_mean")).mean(), g("L_min").min(), g("L_max").max(), g("frac_ge1").mean(), g("frac_ge2").mean()))
        print("   fixations in window = %.1f ; serial cap window/latency = %.1f ; ratio = %.2f ; segregating (no hindsight) = %.1f" %
              (g("n_fix").mean(), cap, g("n_fix").mean() / cap, g("nseg_mean").mean()))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    if cmd == "smoke":
        main(1, smoke=True)
    elif cmd == "main":
        main(int(sys.argv[2]) if len(sys.argv) > 2 else 1)
    elif cmd == "analyse":
        analyse(sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "results", "raw"))
