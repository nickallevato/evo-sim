"""G2c / B6c -- does a NON-serial sweep model leave standing neutral variation?  (Hancock's standing-variation prediction.)

THROWAWAY research check (queue item 4).  Individual-based, genotype-level Wright-Fisher with FREE recombination between all
loci.  Run on na-workhorse only:
    research/.venv/bin/python -I research/checks/g2c_standing_variation.py smoke
    research/.venv/bin/python -I research/checks/g2c_standing_variation.py main <workers>      # 6 jobs: ctrl/A/B x 2 reps
    research/.venv/bin/python -I research/checks/g2c_standing_variation.py analyse [rawdir]

TARGET CLAIMS.  G2c and B6c (Hancock, Gutsick Gibbon video _Vu0ZVVjwHc, 2026-10-03, t=01:33:59, auto-caption):
  "there would basically be no genetic variation amongst individuals except for the mutation that's increasing in frequency"
  and t=01:31:58 "it assumes that each mutation has to both arise and go to fixation before the next".  Specified in G2c's
  Pre-registered prediction: "forward simulation with sweep rate 1/1,322 per genome per generation (LTEE-rate) and free
  recombination; measure neutral heterozygosity at unlinked sites vs theta ... Result that would change a verdict: heterozygosity
  <10% of theta under free recombination at the stated sweep rate."  Gc/G1 (Day: ~230 simultaneous sweeps; Bernoulli paper) is the
  second model.  A strictly serial model (no new variant arises until the previous fixes) has zero standing variation BY
  CONSTRUCTION, so Hancock's conditional is a tautology and is not simulated; what is tested is whether the models the two sides
  actually state predict it.

MODEL.  N = 10,000 diploids (2N = 20,000 haplotypes; no rescaling, because variance in fitness is not scale-free), genic
multiplicative selection s = 0.01 per beneficial copy (w = (1+s)^copies), each of 2N gametes drawn from a parent chosen
proportionally to fitness, free recombination (each locus independently from either parental haplotype), exactly as wf.py's
independent-loci convention but at genotype level, so fitness variance can act on unlinked loci.  Neutral loci: K = 500 biallelic
loci with symmetric mutation u = 2.5e-5 per haplotype per generation (4Nu = 1; initialised at their stationary law, Beta(1,1)
frequencies, no LD; the ratios are against a control run from the same initial state, so theta's absolute value does not matter).
Beneficial mutations arrive at random haplotypes at rate nu_arr per generation (all arrivals; fixation probability ~2s = 0.02),
each at a fresh locus slot; slots recycle on loss or fixation.
  ctrl  no beneficial mutations.
  A     sweep (fixation) rate 1/1,322 per generation per genome (G2c spec; LTEE rate), so nu_arr = (1/1322)/0.02 = 0.0378/gen.
        Mean sweep duration about (2/s)ln(2N) ~ 1,980 gens, so concurrency ~ 1.5.
  B     Day's ~230 simultaneous sweeps (Gc/G1): fixation rate 230/1,980 = 0.116/gen, nu_arr = 5.8/gen.
Measured (window = generations 3,000-5,999 of 6,000, after the sweeps reach steady state):
  Hn = mean 2p(1-p) over neutral loci (heterozygosity, haplotype-based), ratio to ctrl;
  drift ratio = sum over loci of (delta p)^2 / sum of p(1-p)/(2N) per generation, which estimates N/Ne for the neutral loci
  (1 for plain WF; > 1 if sweeps raise offspring variance);
  concurrency = mean number of beneficial alleles with >= 50 copies and not fixed (established sweeps in transit);
  completed sweeps; dropped arrivals (no free slot).

PRE-REGISTERED PREDICTIONS (written before any run; smoke checks timing and shapes only):
  P1  ctrl: Hn stationary (window mean within 4% of its start value); drift ratio = 1.00 +- 0.01.
  P2  A: Hn(A)/Hn(ctrl) in [0.96, 1.04]; drift ratio in [0.99, 1.01]; concurrency in [0.8, 2.5].  Unlinked neutral diversity is
      about theta: Hancock's falsifier (< 10% of theta) fails by a factor ~10.
  P3  B: concurrency in [150, 300]; Hn(B)/Hn(ctrl) in [0.95, 1.04]; drift ratio in [1.000, 1.03] (derived: Var(log w) =
      conc x 2 s^2 x mean p(1-p) = 230 x 2 x 1e-4 x 0.05 = 0.0023, so offspring variance rises ~0.2%).  Zero dropped arrivals.
  P4  To drive unlinked diversity below 10% of theta through fitness variance alone would need Var(w) of order 10, i.e. about 1e6
      concurrent sweeps at s = 0.01 (derived, not simulated), far beyond anything either side states.
  P5  Linked sites are NOT covered: hitchhiking at neutral sites physically linked to a sweep is the standard-theory reduction
      (not tested here); free recombination is the G2c spec.

WHAT EACH SIDE'S MODEL PREDICTS.
  Hancock: a serial model predicts ~no variation (tautology); the sweep-rate model (A) and a parallel model do not.  He is
    right that observed polymorphism contradicts a literally serial, one-at-a-time genome; the simulation does not test his
    claim about the SFS shape ("doesn't bear out") or any real data.
  Day: nothing predicted for polymorphism (G2c claim file); his models are not strictly serial (Gc: ~230 simultaneous sweeps);
    in that regime the simulation predicts unlinked diversity ~theta.  Whether 230 concurrent sweeps are feasible (selective
    load, linkage, GAP-04) is not tested here, and unlinked-free recombination is the most favourable case for the critics.
  RESULT THAT WOULD CHANGE A VERDICT: Hn ratio < 0.10 in A (then G2c's falsifier fires), or Hn(B)/Hn(ctrl) < 0.9.

Raw output: research/checks/results/raw/g2c_<model>_rep<r>.json.

POST HOC ADDENDUM (review MAJOR-1; commit labelled "post hoc (review MAJOR)").  DIAGNOSIS by reading the code and the committed log
(raw/g2c.out), no new run: the "fixed" counter (fixed_cnt) is CUMULATIVE over all 6,000 generations; the write-up divided it by the
3,000-generation window (539/3000 = 0.18, "1.55x intended").  From the log (B rep0): fixed = 195 at g=3000 and 539 at g=6000, so the
WINDOW rate is 344/3000 = 0.115 per generation = 0.99x the intended 0.116.  The fixation rate was correct; there was no excess.
The real shortfall is concurrency: counted sweeps (>= 50 copies to fixation) last about 146/0.115 = 1,270 generations, not the
1,980 assumed (the count starts at 50 copies and a sweep that fixes runs faster than the unconditional mean), so the realised counted
concurrency was 146 (< floor 150).  FIX: new model B2 = B with arrival rate x 230/146, aiming the counted concurrency at 230, and
fixed_win (fixations inside the window) recorded.  RERUN (post hoc): B2 reps 0-2, A reps 2-5, ctrl reps 2-5 (reps 0-1 of ctrl/A
are the original runs, unchanged code path).  PRE-REGISTERED (before the rerun):
  R1  B2 counted concurrency mean in [190, 280] (floor 150 met); fixed_win/3000 in [0.15, 0.22] per generation (= 0.115 x 1.575 +- 20%).
  R2  B2 Hn ratio to the rep-matched ctrl in [0.95, 1.04] each rep; drift ratio in [1.000, 1.03]; zero dropped arrivals.
  R3  A over 6 reps: mean counted concurrency in [0.8, 2.5]; mean Hn ratio in [0.96, 1.04].
  R4  ctrl over 6 reps: per-rep Hn drift within 4% of its start in at least 5 of 6.
  Verdict rule: external stays pending unless R1, R2 and R3 are met; if any fails, it stays pending and the result is written up.
Run: ... g2c_standing_variation.py main 3 rerun   (one invocation = 11 jobs; launch as 2 invocations of the job list if needed)
POST HOC (review MAJOR follow-up), 2026-10-09; pre-registered before the run, commit labelled "post hoc (review MAJOR follow-up)".
Why: condition A's counted concurrency (6 reps, T = 6,000, window 3,000) averaged 0.6, below the pre-registered [0.8, 2.5]; expected
about 1.0 (0.00076 fixations/gen x ~1,270 counted duration), and with 1-3 sweeps per window the mean is Poisson-limited.  Fix:
model A_long = A (same parameters, same code path) with T = 18,000 and window 6,000-17,999 (12,000 generations, about 9 sweeps per
rep), reps 6, 7.  Run: g2c_standing_variation.py main 2 rerunA   (2 jobs, 2 workers, about 35 min each on na-workhorse).  No new ctrl
runs: the Hn ratio is against the mean Hn_win of the six existing ctrl reps (P1 shows ctrl Hn is stationary within 4%).
  L1  A_long mean counted concurrency over the 2 reps in [0.8, 2.5]; each rep in [0.3, 3.0].
  L2  A_long mean Hn ratio to the 6-rep ctrl mean in [0.96, 1.04].
  L3  A_long drift ratio (N/Ne) in [0.99, 1.01].  Zero dropped arrivals.
  Verdict rule (fixed now): restore the G2c/B6c external verdict ("supported", as a conditional, per review #17) only if L1, L2 and
  L3 all pass; R1 and R2 already passed in the first post hoc rerun.  If any fails, external stays pending and the result is written up.
  If Hn ratio were < 0.10 the Hancock falsifier would fire (not expected).
"""
import os
import sys
import json
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.setdefault("OMP_NUM_THREADS", "1")
import numpy as np

S = 0.01
U = 2.5e-5
SEED = 20261013
MODELS = {"ctrl": 0.0, "A": (1.0 / 1322.0) / 0.02, "B": (230.0 / 1980.0) / 0.02}
SLOTS = {"ctrl": 0, "A": 40, "B": 450}
# POST HOC (review MAJOR-1): model B2 = B with the arrival rate scaled by 230/146 = 1.575 (B's measured counted concurrency was 146),
# aiming the COUNTED concurrency (>= 50 copies, not fixed) at Day's 230.  Slots raised so arrivals are not dropped.
MODELS["B2"] = MODELS["B"] * 230.0 / 146.0
SLOTS["B2"] = 800
MODELS["A_long"] = MODELS["A"]    # POST HOC (review MAJOR follow-up): A with a long window; see docstring
SLOTS["A_long"] = SLOTS["A"]


def run(model, rep, N=10_000, K=500, T=6000, win=(3000, 6000), rec_every=20, seed_extra=0):
    M = 2 * N
    Lsel = SLOTS[model]
    nu = MODELS[model]
    ncol = Lsel + K
    rng = np.random.default_rng(np.random.SeedSequence([SEED, rep, seed_extra]))
    init = np.random.default_rng(np.random.SeedSequence([SEED, rep, 99]))     # same neutral start for every model at this rep
    pk = init.beta(4 * N * U, 4 * N * U, size=K)
    Hn0 = (init.random((M, K)) < pk).astype(np.uint8)
    H = np.zeros((M, ncol), dtype=np.uint8)
    H[:, Lsel:] = Hn0
    active = []                       # occupied selected slots
    free = list(range(Lsel))
    fixed_cnt = dropped = 0
    rec = []
    t0 = time.time()
    pprev = H[:, Lsel:].mean(axis=0, dtype=np.float64)
    for g in range(T):
        if active:
            sub = H[:, active]
            copies = sub[0::2].sum(axis=1, dtype=np.int16) + sub[1::2].sum(axis=1, dtype=np.int16)
            w = (1.0 + S) ** copies
        else:
            w = np.ones(N)
        cum = np.cumsum(w)
        par = np.searchsorted(cum, rng.random(M) * cum[-1])
        par = np.minimum(par, N - 1)
        bits = (np.frombuffer(rng.bytes(M * ncol), dtype=np.uint8) & 1).reshape(M, ncol).astype(bool)
        H = np.where(bits, H[2 * par + 1], H[2 * par])
        nm = rng.poisson(M * K * U)
        if nm:
            r = rng.integers(0, M, nm)
            c = Lsel + rng.integers(0, K, nm)
            H[r, c] ^= 1
        if nu > 0:
            for _ in range(rng.poisson(nu)):
                if free:
                    sl = free.pop()
                    H[rng.integers(0, M), sl] = 1
                    active.append(sl)
                else:
                    dropped += 1
        if active:
            cnt = H[:, active].sum(axis=0, dtype=np.int64)
            gone = [(sl, c) for sl, c in zip(active, cnt) if c == 0 or c == M]
            for sl, c in gone:
                if c == M:
                    fixed_cnt += 1
                H[:, sl] = 0
                active.remove(sl)
                free.append(sl)
        else:
            cnt = np.empty(0)
        p = H[:, Lsel:].mean(axis=0, dtype=np.float64)
        dp2 = float(((p - pprev) ** 2).sum())
        exp_dp2 = float((pprev * (1 - pprev)).sum() / M)
        pprev = p
        if g % rec_every == 0 or g == T - 1:
            est = int(((cnt >= 50) & (cnt < M)).sum()) if len(cnt) else 0
            rec.append(dict(g=g, Hn=float((2 * p * (1 - p)).mean()), dp2=dp2, exp_dp2=exp_dp2, conc=est, fixed=fixed_cnt))
        else:
            rec.append(dict(g=g, dp2=dp2, exp_dp2=exp_dp2))
        if g % 500 == 0:
            print("%s rep%d g=%d t=%.0fs Hn=%.4f conc=%s fixed=%d dropped=%d" % (
                model, rep, g, time.time() - t0, float((2 * p * (1 - p)).mean()), (rec[-1].get("conc")), fixed_cnt, dropped), flush=True)
    lo, hi = win
    full = [r for r in rec if "Hn" in r and lo <= r["g"] < hi]
    allw = [r for r in rec if lo <= r["g"] < hi]
    out = dict(model=model, rep=rep, N=N, K=K, T=T, Hn_start=float((2 * pk * (1 - pk)).mean()),
               Hn_win=float(np.mean([r["Hn"] for r in full])), conc_win=float(np.mean([r["conc"] for r in full])),
               drift_ratio=float(sum(r["dp2"] for r in allw) / sum(r["exp_dp2"] for r in allw)),
               fixed=fixed_cnt, fixed_win=(lambda f: (f[-1]["fixed"] - f[0]["fixed"], f[-1]["g"] - f[0]["g"]))(full),
               dropped=dropped, secs=time.time() - t0,
               Hn_series=[(r["g"], r["Hn"]) for r in rec if "Hn" in r and r["g"] % 200 == 0])
    return out


def _job(a):
    model, rep = a
    r = run(model, rep, T=18000, win=(6000, 18000)) if model == "A_long" else run(model, rep)
    od = os.path.join(HERE, "results", "raw")
    with open(os.path.join(od, "g2c_%s_rep%d.json" % (model, rep)), "w") as fh:
        json.dump(r, fh)
    return r


def analyse(rawdir):
    import glob
    R = {}
    for f in sorted(glob.glob(os.path.join(rawdir, "g2c_*_rep*.json"))):
        r = json.load(open(f))
        R.setdefault(r["model"], []).append(r)
    ctrl = np.mean([r["Hn_win"] for r in R.get("ctrl", [])]) if "ctrl" in R else float("nan")
    for m in ("ctrl", "A", "B", "B2", "A_long"):
        for r in R.get(m, []):
            print("%-4s rep%d: Hn_start=%.4f Hn_win=%.4f ratio_to_ctrl=%.3f drift_ratio(N/Ne)=%.4f conc=%.1f fixed_total=%d fixed_win=%s dropped=%d (%.0fs)" % (
                m, r["rep"], r["Hn_start"], r["Hn_win"], r["Hn_win"] / ctrl, r["drift_ratio"], r["conc_win"], r["fixed"], r.get("fixed_win"), r["dropped"], r["secs"]))
    for m in ("ctrl", "A", "B", "B2", "A_long"):
        if R.get(m):
            print("MEAN %-4s n=%d Hn ratio %.3f (per-rep ctrl-matched: %s) conc %.1f drift %.4f" % (m, len(R[m]), np.mean([r["Hn_win"] for r in R[m]]) / ctrl,
                  [round(r["Hn_win"] / np.mean([c["Hn_win"] for c in R["ctrl"] if c["rep"] == r["rep"]]), 3) for r in R[m] if any(c["rep"] == r["rep"] for c in R["ctrl"])],
                  np.mean([r["conc_win"] for r in R[m]]), np.mean([r["drift_ratio"] for r in R[m]])))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    if cmd == "smoke":
        for m in ("ctrl", "A", "B"):
            r = run(m, 0, N=500, K=40, T=400, win=(200, 400), rec_every=10)
            print("smoke", m, "secs=%.1f Hn_win=%.3f drift_ratio=%.3f conc=%.1f" % (r["secs"], r["Hn_win"], r["drift_ratio"], r["conc_win"]))
    elif cmd == "main":
        import multiprocessing as mp
        w = int(sys.argv[2]) if len(sys.argv) > 2 else 3
        jobs = [(m, r) for m in ("B", "A", "ctrl") for r in (0, 1)]
        if len(sys.argv) > 3 and sys.argv[3] == "rerun":      # POST HOC (review MAJOR-1): see docstring addendum
            jobs = [("B2", r) for r in (0, 1, 2)] + [(m, r) for r in (2, 3, 4, 5) for m in ("A", "ctrl")]
        if len(sys.argv) > 3 and sys.argv[3] == "rerunA":     # POST HOC (review MAJOR follow-up): see docstring addendum
            jobs = [("A_long", r) for r in (6, 7)]
        with mp.get_context("spawn").Pool(w) as pool:
            for r in pool.imap_unordered(_job, jobs):
                print("done", r["model"], r["rep"], flush=True)
        analyse(os.path.join(HERE, "results", "raw"))
    elif cmd == "analyse":
        analyse(sys.argv[2] if len(sys.argv) > 2 else os.path.join(HERE, "results", "raw"))
