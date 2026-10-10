"""H8 / H5 (and H): Haldane's 1/300 in Haldane's own regime.  Hard-selection cap swept over reproductive excess
R = 1.05 .. 3 with the per-substitution cost D MEASURED in every cell, plus two soft-selection arms.
THROWAWAY research code (no simulator product code).  Self-contained (python -I drops the script directory from
sys.path); the diploid free-recombination engine is the H3 run() (h3_human_scale.py) with the map, deleterious
bins and finite supply removed, and with two soft modes added.
Run:    research/.venv/bin/python -I research/checks/h8_haldane_regime.py smoke|main|analyse [workers]
Seeds:  numpy SeedSequence([SEED, stage_code, cell_index, rep]) -- never hash().
Output: research/checks/results/raw/h8_<stage>.jsonl (one JSON row per run, appended as runs finish) and
        h8_<stage>.out (stdout).  `analyse` reads h8_main.jsonl and prints the tables for R4-H8.md.

Written 2026-10-09 BEFORE any run of this file (smoke included).  Predictions below are fixed; anything changed
after the smoke or main run goes in a separate commit labelled "post hoc".

=====================================================================================================
CLAIMS UNDER TEST (verbatim; locators are the claim files in docs/research/claims/)
  H  (Day, Z18168236 Abstract): "Haldane calculated that mammals could fix no more than approximately one
      beneficial substitution per 300 generations, based on the reproductive cost each substitution imposes
      on a population."
  H  (Day, Z18168236 s2.3): "The 10% selective mortality is a total budget for the population, not a per-locus
      allocation."
  H8 (Day, Z19984826 s3.3): "Selection cannot operate without reproductive differential, and the differential
      available to any individual is bounded by what the organism can physically achieve."
  H8 (Day, Z19984826 s4.3): "ksel = smax . d / [2L . ln(2Ne)] = 1 . 0.45 / [2 . 3.1 x 10^9 . ln(6,600)] ...
      ~ 8.3 x 10^-12"
  H8 (Day, Z19984826 s3.3.1): "None of them raises smax above order unity, and the reason is the same in all
      three cases."   (truncation, soft selection, composite fitness)
  H5 (Hossjer, ally, 2026-09-14 p.3): "the number of fixations with a selective advantage along the supposed
      human lineage is far less than what equation (4) predicts, perhaps more in line with equation (3)."
      (eq. 3 = 15,800 over 450,000 generations = 0.0351 per generation)

WHAT IS NEW RELATIVE TO H2-hard AND H3 (R4-H2-hard.md, R4-H3-human.md)
  H2-hard tested only R >= 1.3 (haploid D ~ 7).  H3 ran R = 1.1 / 1.5 / 2 / 3 on a 36.8 M map with a soft
  deleterious load and reported lambda50 at R = 1.1 as "circular in R by construction".  Here: (i) a fine R grid
  1.05-3 in Haldane's own setting (independent loci, one new copy per substitution, no deleterious load), (ii) D
  measured per cell and checked against K (D-invariance of lambda50*D), (iii) three windows (10k / 20k / 40k
  generations) for H8's window dependence, (iv) two soft-selection arms that H3 left unmodelled, with the
  realised reproductive differential (max and 99th-percentile relative fitness, Crow's I) recorded, which is
  the quantity Day's s_max argument (H8 s3.3, s3.3.1) is about.

MODEL (diploid, K adults at the ceiling, free recombination between all selected loci, log-additive fitness)
  * Treadmill (Haldane's setting): the environment opens a new locus at Poisson(lam) per generation; it opens
    with ONE beneficial copy among 2N (p0 = 1/2N); a lost copy is re-seeded (the time spent re-seeding is paid
    as load and counts in D); the locus closes at fixation (one substitution).  Each ancestral copy at an open
    locus multiplies fitness by exp(-s) (s = 0.01 per copy, as H3; homozygote difference 0.02).
  * HARD: juveniles J = f N with f = min(R, K/N) (ceiling regulation; R = maximum offspring per adult =
    reproductive excess); each juvenile survives with probability w (absolute fitness); extinct if N < 20.
    Haldane's 10% selective mortality maps to R = 1/(1 - 0.10) = 1.111 (ln R = 0.105).
  * softJ (Wallace-type juvenile competition, R-limited): J = R K juveniles, K survivors drawn by fitness-
    weighted sampling WITHOUT replacement (Efraimidis-Spirakis keys).  N = K always; a juvenile's survival
    probability can never exceed 1, so its relative survival is at most R (the "physically achievable
    differential").  Failure = backlog (open loci > max_open, or k_obs/lam < 0.9 with a rising open count).
  * softWF (textbook relative-fitness Wright-Fisher, R-free): each child's two parents drawn with probability
    proportional to w.  No demographic cap by construction; the test is the realised differential it needs.
  Measured per run: survival to 10k / 20k / 40k generations; k_obs (fixations per generation, after burn);
  D_obs = sum_t(-ln wbar_t) / fixations over the recorded window (Haldane's cost in log units; in soft modes the
  same quantity is computed but kills nobody); N/K; open-locus count (first and last quarter of the window);
  Crow's I = var(w)/wbar^2; maxrel = max(w)/wbar and q99 = 99th percentile of w/wbar (expected relative
  offspring number of the fittest individual: Day's "twice as many descendants" is maxrel = 2).

R VALUES: SOURCED vs SWEPT (V17 in docs/research/R5-draft.md; claim files H, H3, H8)
  sourced/anchored: 1.111 = Haldane's 10% selective mortality (via Nunney 2003; Matheson 2025 k = 1.1);
                    2     = Day's s_max "twice as many descendants" read as R (audit reading, H8 Assumptions);
                    e     = Day's s_max = 1 under the audit mapping s_max = ln R (H8 Check);
                    3     = Day's total fertility 6-8 per female -> 3-4 per adult before mortality (upper end).
  swept only (no source): 1.05, 1.2, 1.3, 1.5.  No sourced net reproductive excess for hominids exists in the
  repo (R5-draft V17); "realistic human R" is therefore not a measured input on either side.

STAGES (K = 1000 diploids unless stated; s = 0.01 per copy; Dref(K) = 2 ln(2K) + 2 sets the lam grid only)
  hard:  R in {1.05, 1.111, 1.2, 1.3, 1.5, 2, e, 3}; lam = x ln(R)/Dref, x in {0.4, 0.6, 0.8, 0.9, 1.0, 1.1,
         1.25, 1.5}, plus lam = 1/300 at every R; 6 reps; 40,000 generations (burn 3,000).
  Kscale: hard, K in {500, 4000}, R in {1.111, 2}, x in {0.6, 0.8, 1.0, 1.25}; 4 reps; 20,000 generations.
  softJ: R in {1.05, 1.111, 1.5, 2, 3}; lam in {1/300, 0.0351 (Hossjer), 0.1}; 3 reps; 30,000 gens (burn 10,000);
         max_open 1500.
  softWF: lam in {1/300, 0.0351, 0.1, 0.2}; 3 reps; 30,000 gens (burn 10,000); max_open 1500.
  smoke: five tiny cells (timing and plumbing only; output not used for any conclusion).
ESTIMATORS (fixed now)
  lam50(T) per R: survival fraction to T at each lam; first adjacent pair (lam_i, lam_{i+1}) with surv >= 0.5
  then < 0.5; linear interpolation in log lam.  Reported with the bracket.  phi(T) = lam50(T) D_obs / ln R.
  D_obs(R) = median over persisting reps of the cells with x <= 0.8 (low lam, steady state).
  Rescaling to Haldane's D = 30 (and D = 20, new mutation at Ne = 1e4): lam50 * D_obs / D_target.  This uses the
  invariance lam50 * D = phi ln R, which the Kscale stage tests (it is not assumed).
  Haldane's interval in-model: 1 / [lam50 * D_obs / 30].  Literal Day/Haldane: 300.

PRE-REGISTERED PREDICTIONS
  Day's side (H, H8, H5 as stated):
    PD1  At Haldane's settings (R = 1.111, rescaled to D = 30) the sustainable rate is about 1/300: interval
         within [150, 600] generations.
    PD2  Day's 10% is a total budget independent of R: lam50 does not grow in proportion to ln R (literal reading:
         ~ 1/300 at every R).  Day-in-model variant: lam50 ~ 0.10 / D_obs at every R.
    PD3  Soft selection does not raise the budget (Z19984826 s3.3.1): softJ fails (backlog or k_obs/lam < 0.9) at
         lam well above the hard cap at the same R; softWF needs maxrel > 2 ("twice as many descendants")
         at lam = 0.0351.
    PD4  H8 Term 3 (d = 1 in simulated generations; s_max = 1): 1/(2 ln 2K) = 0.0658 at K = 1000 is the
         sustainable rate (for R = 2, the "twice as many descendants" reading).
  Critics' side (Nunney 2003, Wallace, Kimura/Maynard Smith, McCarthy/Hancock "faster at realistic R / soft"):
    PC1  The hard cap is phi ln R / D: lam50 grows ~ ln R (lam50(R=3)/lam50(R=1.111) ~ 10, phi-corrected 7-12).
    PC2  At R >= 2 the rate is >= 6x Haldane's 1/300 after rescaling to D = 30; in-model at K = 1000 >= 10x.
    PC3  softJ sustains lam = 0.0351 at every R >= 1.111 (k_obs/lam >= 0.9, no backlog); softWF sustains all
         lam to 0.2 with maxrel well below 2 (Crow's I << 1).
  This audit's numeric predictions (mean-field theory from R4-H2-hard / R4-H3):
    P1   D_obs at K = 1000, low lam: 2 ln(2K) + c in [15.5, 20]; slope dD/dlnK = 2 +/- 0.5 (K = 500 -> 4000).
    P2   lam50(10k) * D_obs / ln R = phi(10k) in [0.75, 1.1] at every R; phi(40k) <= phi(10k), with
         phi(40k) in [0.4, 1.0], lowest at the smallest R (fluctuation-driven extinction when ln R is small).
    P3   R = 1.111: lam50(10k) in-model ~ 0.105/17.5 ~ 0.006 (1/170, bracket 1/120-1/250); rescaled to D = 30:
         interval 250-400 generations -> PD1 SUPPORTED as Haldane's arithmetic in his regime (a Day-side point).
         R = 1.05: in-model ~ 1/350; D = 30 rescaled ~ 1/600-1/900.
    P4   PD2 NOT supported: lam50(R=3)/lam50(R=1.111) in [7, 12]; at R = 2 in-model lam50 ~ 0.035-0.04
         (11-13x 1/300); at R = 3 ~ 0.05-0.065.
    P5   H5: Hossjer's 0.0351 per generation is sustained in-model (10k window) from R ~ 1.8-2.3 (D_obs ~ 17);
         at human D = 20 from R ~ 2-2.5; with the 40k window R ~ 2.2-3.  (H3: R ~ 2-3; consistent.)
    P6   H8 Term 3 literal (0.0658 at K = 1000, d = 1): NOT sustained at R = 2 (lam50 ~ 0.04); sustained only at
         R >= e^(0.0658 D_obs / phi) ~ 3-3.5, i.e. not inside the grid's 10k window except marginally at R = 3.
         Term 3 with d = 0.45 (0.0296) IS sustained at R = 2 (as H3 found).  Day's formula equals the
         mean-field critic formula ln R / D with s_max = ln R and D = 2 ln 2Ne (structure agrees; parameter is R).
    P7   softJ: k_obs/lam >= 0.9 without backlog at lam = 0.0351 for R >= 1.111 (selection efficiency
         f ln(1/f)/(1 - f), f = 1 - 1/R, is 0.24 at R = 1.111: sweeps ~4x slower, ~200-300 open loci); lam = 0.1
         sustained at R >= 1.5, backlog or non-steady at R <= 1.111.  R = 1.05 may not reach steady state in
         30k generations (reported as inconclusive, not as a pass or fail).
    P8   softWF: k_obs/lam >= 0.9 at every lam to 0.2; maxrel at lam = 0.0351 in [1.05, 1.4]; Crow's I < 0.01;
         D_obs (log-load per substitution, nobody dies of it) ~ the hard value, i.e. Haldane's cost is incurred as
         variance in relative fitness, not as deaths.
  What would change a verdict: PD1 holding together with PC1 means Haldane's number is right in Haldane's regime
  and the open question is R (H external stays contested, with the flip R stated).  PD2 holding (lam50 flat in R)
  would support Day's budget reading.  PD3 holding (softJ capped at the hard cap) would rebut the critics' soft-
  selection reply in this model.  Failure of P2's D-invariance (Kscale) would void the D = 30 rescaling.
=====================================================================================================
"""
import json
import math
import os
import sys
import time

import numpy as np
from multiprocessing import Pool

SEED = 20261009
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "results", "raw")
EXT_N = 20
S = 0.01
HOSSJER = 15800 / 450000          # 0.0351 per generation (H5, eq. 3 over 450,000 generations)
CHECKS = (10000, 20000, 40000)
RS = (1.05, 1.0 / 0.9, 1.2, 1.3, 1.5, 2.0, math.e, 3.0)
XS = (0.4, 0.6, 0.8, 0.9, 1.0, 1.1, 1.25, 1.5)


def Dref(K):
    return 2 * math.log(2 * K) + 2


def D_det(p0, s=S):
    """Deterministic diploid genic sweep cost sum_t -ln wbar_t from p0 to 1-p0 (= H3 D_det); ~ 2 ln(1/p0)."""
    p, D = p0, 0.0
    es = math.exp(-s)
    while p < 1 - p0:
        m = p + (1 - p) * es
        D += -2.0 * math.log(m)
        p = p / m
    return D


def run(K, s, lam, R, mode, gens, burn, rng, max_open=1500):
    N = K
    G = np.zeros((0, 2 * N), dtype=np.uint8)            # open loci x haplotypes (1 = beneficial)
    t_open = []
    fixes_rec = 0
    ttf = []
    acc = dict(rec=0, La=0.0, I=0.0, maxrel=0.0, q99=0.0, nfrac=0.0, nopen=0.0)
    rec_len = gens - burn
    q1, q4 = [0.0, 0], [0.0, 0]
    alive_at = {T: False for T in CHECKS}
    fail, t_fail = None, None
    for t in range(gens):
        for T in CHECKS:
            if t == T - 1:
                alive_at[T] = True
        for _ in range(rng.poisson(lam)):
            col = np.zeros((1, 2 * N), dtype=np.uint8)
            col[0, rng.integers(0, 2 * N)] = 1
            G = np.vstack([G, col])
            t_open.append(t)
        nl = G.shape[0]
        if nl > max_open:
            fail, t_fail = "backlog", t
            break
        if mode == "hard":
            f = min(R, K / N)
            J = int(f * N)
            J += int(rng.random() < f * N - J)
            if J < 2:
                fail, t_fail = "extinct", t
                break
            pa = rng.integers(0, N, J)
            pb = (pa + rng.integers(1, N, J)) % N
        elif mode == "softJ":
            J = int(round(R * K))
            pa = rng.integers(0, N, J)
            pb = (pa + rng.integers(1, N, J)) % N
        else:                                            # softWF: parents drawn proportional to adult w
            J = K
            ancA = 2 * nl - G.reshape(nl, N, 2).sum(axis=(0, 2), dtype=np.int64) if nl else np.zeros(N, np.int64)
            wA = np.exp(-s * ancA)
            pw = wA / wA.sum()
            pa = rng.choice(N, size=J, p=pw)
            pb = rng.choice(N, size=J, p=pw)
            same = pb == pa
            while same.any():
                pb[same] = rng.choice(N, size=int(same.sum()), p=pw)
                same = pb == pa
        par = np.empty(2 * J, dtype=np.int64)
        par[0::2] = pa
        par[1::2] = pb
        if nl:
            o = rng.integers(0, 2, size=(nl, 2 * J), dtype=np.uint8)
            C = np.take_along_axis(G, 2 * par[None, :] + o, axis=1)        # nl x 2J
            anc = 2 * nl - C.reshape(nl, J, 2).sum(axis=(0, 2), dtype=np.int64)
        else:
            C = np.zeros((0, 2 * J), dtype=np.uint8)
            anc = np.zeros(J, dtype=np.int64)
        w = np.exp(-s * anc) if mode != "softWF" else wA
        wbar = float(w.mean())
        if mode == "hard":
            keep = rng.random(J) < w
        elif mode == "softJ":
            keys = rng.exponential(size=J) / w
            keep = np.zeros(J, bool)
            keep[np.argpartition(keys, K - 1)[:K]] = True
        else:
            keep = np.ones(J, bool)
        surv = np.flatnonzero(keep)
        Nn = len(surv)
        if t >= burn:
            rel = w / wbar
            acc["rec"] += 1
            acc["La"] += -math.log(max(wbar, 1e-300))
            acc["I"] += float(rel.var())
            acc["maxrel"] += float(rel.max())
            acc["q99"] += float(np.quantile(rel, 0.99))
            acc["nfrac"] += Nn / K
            acc["nopen"] += nl
            if t < burn + rec_len // 4:
                q1[0] += nl; q1[1] += 1
            elif t >= gens - rec_len // 4:
                q4[0] += nl; q4[1] += 1
        if Nn < EXT_N:
            fail, t_fail = "extinct", t
            break
        N = Nn
        hidx = (2 * surv[:, None] + np.arange(2)[None, :]).ravel()
        G = np.ascontiguousarray(C[:, hidx]) if nl else np.zeros((0, 2 * N), dtype=np.uint8)
        if nl:
            cnt = G.sum(axis=1, dtype=np.int64)
            fixed = cnt == 2 * N
            lost = cnt == 0
            if fixed.any():
                for j in np.flatnonzero(fixed):
                    ttf.append(t - t_open[j])
                    fixes_rec += int(t >= burn)
            for j in np.flatnonzero(lost):
                G[j, rng.integers(0, 2 * N)] = 1
            if fixed.any():
                kr = np.flatnonzero(~fixed)
                G = G[kr]
                t_open = [t_open[j] for j in kr]
    if fail is None:
        for T in CHECKS:
            if gens >= T:
                alive_at[T] = True
    n = max(acc["rec"], 1)
    return dict(fail=fail, t_fail=t_fail, alive={str(T): alive_at[T] for T in CHECKS if T <= gens},
                k=fixes_rec / n, fixes_rec=fixes_rec, gens_rec=acc["rec"],
                D=acc["La"] / fixes_rec if fixes_rec else float("nan"), La=acc["La"] / n,
                I=acc["I"] / n, maxrel=acc["maxrel"] / n, q99=acc["q99"] / n, nfrac=acc["nfrac"] / n,
                nopen=acc["nopen"] / n, nopen_q1=q1[0] / max(q1[1], 1), nopen_q4=q4[0] / max(q4[1], 1),
                ttf=float(np.mean(ttf)) if ttf else float("nan"), nfix_all=len(ttf))


# ------------------------------------------------------------------------------------------------ cells
def build(stage):
    """Cells: (arm, K, lam, R, x_label, mode, reps, gens, burn, max_open)."""
    c = []
    if stage == "smoke":
        c.append(("smoke", 1000, 0.105 / Dref(1000), 1 / 0.9, "x=1", "hard", 1, 3000, 500, 1500))
        c.append(("smoke", 1000, math.log(3) / Dref(1000), 3.0, "x=1", "hard", 1, 3000, 500, 1500))
        c.append(("smoke", 1000, HOSSJER, 1.05, "H5", "softJ", 1, 2000, 500, 1500))
        c.append(("smoke", 1000, 0.1, float("nan"), "lam=0.1", "softWF", 1, 2000, 500, 1500))
        c.append(("smoke", 4000, math.log(2) / Dref(4000), 2.0, "x=1", "hard", 1, 1000, 300, 1500))
        return c
    if stage == "main":
        for R in RS:
            for x in XS:
                c.append(("hard", 1000, x * math.log(R) / Dref(1000), R, f"x={x}", "hard", 6, 40000, 3000, 1500))
            c.append(("hard", 1000, 1 / 300, R, "1/300", "hard", 6, 40000, 3000, 1500))
        for K in (500, 4000):
            for R in (1 / 0.9, 2.0):
                for x in (0.6, 0.8, 1.0, 1.25):
                    c.append(("Kscale", K, x * math.log(R) / Dref(K), R, f"x={x}", "hard", 4, 20000, 3000, 1500))
        for R in (1.05, 1 / 0.9, 1.5, 2.0, 3.0):
            for lam, lab in ((1 / 300, "1/300"), (HOSSJER, "H5"), (0.1, "lam=0.1")):
                c.append(("softJ", 1000, lam, R, lab, "softJ", 3, 30000, 10000, 1500))
        for lam, lab in ((1 / 300, "1/300"), (HOSSJER, "H5"), (0.1, "lam=0.1"), (0.2, "lam=0.2")):
            c.append(("softWF", 1000, lam, float("nan"), lab, "softWF", 3, 30000, 10000, 1500))
        # POST HOC grid extension (2026-10-09, after the first 19 main rows): K = 4000, R = 1.111 went extinct at
        # x = 0.6-0.8 within 20k generations (load fluctuations over ~1,400-generation sweeps), so lam50 at low R
        # would be unbracketed below x = 0.4.  Lower x values are APPENDED (existing cell indices and seeds are
        # unchanged).  No prediction is changed.
        for R in RS:
            for x in (0.1, 0.2, 0.3):
                c.append(("hard", 1000, x * math.log(R) / Dref(1000), R, f"x={x}", "hard", 6, 40000, 3000, 1500))
        for K in (500, 4000):
            for R in (1 / 0.9, 2.0):
                for x in (0.2, 0.3, 0.45):
                    c.append(("Kscale", K, x * math.log(R) / Dref(K), R, f"x={x}", "hard", 4, 20000, 3000, 1500))
        return c
    raise SystemExit("unknown stage " + stage)


def job(a):
    stage_code, ci, cell, rep = a
    arm, K, lam, R, lab, mode, reps, gens, burn, mo = cell
    rng = np.random.default_rng(np.random.SeedSequence([SEED, stage_code, ci, rep]))
    t0 = time.time()
    r = run(K, S, lam, R, mode, gens, burn, rng, max_open=mo)
    r.update(dict(arm=arm, cell=ci, K=K, lam=lam, R=R, label=lab, mode=mode, rep=rep, gens=gens, burn=burn,
                  sec=time.time() - t0))
    return r


def run_stage(stage, workers):
    cells = build(stage)
    code = {"smoke": 0, "main": 1}[stage]
    jobs = [(code, ci, cell, rep) for ci, cell in enumerate(cells) for rep in range(cell[6])]
    jobs.sort(key=lambda j: -(j[2][7] * (j[2][1] / 1000) * (2.0 if j[2][5] != "hard" else 1.0)))  # long first
    os.makedirs(RAW, exist_ok=True)
    path = os.path.join(RAW, f"h8_{stage}.jsonl")
    done = set()
    if os.path.exists(path):
        for line in open(path):
            d = json.loads(line)
            done.add((d["cell"], d["rep"]))
    jobs = [j for j in jobs if (j[1], j[3]) not in done]
    print(f"stage {stage}: {len(cells)} cells, {len(jobs)} jobs to run ({len(done)} already done), "
          f"workers {workers}", flush=True)
    t0 = time.time()
    with Pool(workers) as pool, open(path, "a") as fh:
        for i, r in enumerate(pool.imap_unordered(job, jobs, chunksize=1)):
            fh.write(json.dumps(r) + "\n")
            fh.flush()
            if stage == "smoke" or i % 20 == 0:
                print(f"[{time.time() - t0:7.0f}s] {i + 1}/{len(jobs)} {r['arm']} K={r['K']} R={r['R']:.3f} "
                      f"{r['label']} rep{r['rep']} fail={r['fail']} k={r['k']:.4g} D={r['D']:.3g} "
                      f"nopen={r['nopen']:.0f} maxrel={r['maxrel']:.3g} sec={r['sec']:.0f} "
                      f"sec/gen={r['sec'] / max(r['gens_rec'] + r['burn'], 1):.2e}", flush=True)
    print(f"stage {stage} done in {time.time() - t0:.0f} s", flush=True)


# ------------------------------------------------------------------------------------------------ analysis
def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (c - h, c + h)


def lam50(pts):
    """pts: sorted [(lam, surv_frac)]. First crossing from >= 0.5 to < 0.5, log-linear interpolation."""
    if not pts:
        return float("nan"), "none"
    if pts[0][1] < 0.5:
        return float("nan"), f"< {pts[0][0]:.4g}"
    for (l1, f1), (l2, f2) in zip(pts, pts[1:]):
        if f1 >= 0.5 > f2:
            u = (f1 - 0.5) / (f1 - f2)
            return math.exp(math.log(l1) + u * (math.log(l2) - math.log(l1))), f"[{l1:.4g}, {l2:.4g}]"
    return float("nan"), f"> {pts[-1][0]:.4g}"


def analyse():
    rows = [json.loads(l) for l in open(os.path.join(RAW, "h8_main.jsonl"))]
    import collections
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["arm"], r["K"], round(r["lam"], 8), None if r["R"] != r["R"] else round(r["R"], 6), r["label"])].append(r)
    print(f"rows {len(rows)}; D_det(1/2K): K=500 {D_det(1/1000):.2f}, K=1000 {D_det(1/2000):.2f}, "
          f"K=4000 {D_det(1/8000):.2f}; 2 ln(2K): {2*math.log(1000):.2f}, {2*math.log(2000):.2f}, {2*math.log(8000):.2f}")
    out = {}
    for arm, K in (("hard", 1000), ("Kscale", 500), ("Kscale", 4000)):
        Rs = sorted({k[3] for k in g if k[0] == arm and k[1] == K})
        print(f"\n## {arm} K={K}")
        print("| R | ln R | D_obs | T | lam50 | bracket | phi | lam50*D/30 -> interval at D=30 | at D=20 | x 1/300 (in-model) |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for R in Rs:
            cells = sorted([(k[2], v) for k, v in g.items() if k[0] == arm and k[1] == K and k[3] == R])
            lnR = math.log(R)
            Ds = [r["D"] for lam, v in cells for r in v
                  if lam <= 0.8 * lnR / Dref(K) * 1.0001 and r["fail"] is None and r["D"] == r["D"]]
            Dm = float(np.median(Ds)) if Ds else float("nan")
            for T in CHECKS:
                pts = []
                for lam, v in cells:
                    vv = [r for r in v if str(T) in r["alive"]]
                    if vv:
                        pts.append((lam, sum(r["alive"][str(T)] for r in vv) / len(vv)))
                if not pts:
                    continue
                l50, br = lam50(pts)
                phi = l50 * Dm / lnR
                out[(arm, K, R, T)] = dict(lam50=l50, D=Dm, phi=phi)
                print(f"| {R:.3f} | {lnR:.3f} | {Dm:.2f} | {T} | {l50:.4g} | {br} | {phi:.2f} | "
                      f"{1 / (l50 * Dm / 30):.0f} | {1 / (l50 * Dm / 20):.0f} | {l50 * 300:.1f} |")
        print("\ncells (survival 10k/20k/40k with Wilson CI on 40k; mean k/lam, D, N/K, nopen over persisting reps):")
        for k, v in sorted(g.items(), key=lambda kv: (str(kv[0][3]), kv[0][2])):
            if k[0] != arm or k[1] != K:
                continue
            al = {T: [r["alive"].get(str(T)) for r in v if str(T) in r["alive"]] for T in CHECKS}
            ok = [r for r in v if r["fail"] is None]
            m = lambda key: float(np.mean([r[key] for r in ok])) if ok else float("nan")
            sv = " / ".join(f"{sum(a)}/{len(a)}" for a in al.values() if a)
            print(f"  R={k[3]:.3f} {k[4]:>6} lam={k[2]:.4g}: surv {sv}; k/lam={m('k') / k[2]:.2f} D={m('D'):.2f} "
                  f"N/K={m('nfrac'):.2f} nopen={m('nopen'):.0f} I={m('I'):.2e} maxrel={m('maxrel'):.3f}")
    for arm in ("softJ", "softWF"):
        print(f"\n## {arm}")
        print("| R | lam | label | fails | k/lam | nopen q1 -> q4 | D_obs | I | maxrel | q99 | verdict |")
        print("|---|---|---|---|---|---|---|---|---|---|---|")
        for k, v in sorted(g.items(), key=lambda kv: (str(kv[0][3]), kv[0][2])):
            if k[0] != arm:
                continue
            fails = sum(r["fail"] is not None for r in v)
            m = lambda key: float(np.mean([r[key] for r in v]))
            kl = m("k") / k[2]
            rise = m("nopen_q4") / max(m("nopen_q1"), 1e-9)
            verdict = ("FAIL backlog" if fails else ("sustained" if kl >= 0.9 and rise <= 1.15 else
                       ("not steady" if rise > 1.15 else "below 0.9")))
            print(f"| {k[3]} | {k[2]:.4g} | {k[4]} | {fails}/{len(v)} | {kl:.2f} | {m('nopen_q1'):.0f} -> "
                  f"{m('nopen_q4'):.0f} | {m('D'):.2f} | {m('I'):.2e} | {m('maxrel'):.3f} | {m('q99'):.3f} | {verdict} |")
    # headline checks against the pre-registered predictions
    print("\n## prediction checks")
    Rh = round(1 / 0.9, 6)
    for T in CHECKS:
        a = out.get(("hard", 1000, Rh, T))
        b = out.get(("hard", 1000, 3.0, T))
        c = out.get(("hard", 1000, 2.0, T))
        if a and b and c:
            print(f"T={T}: R=1.111 interval at D=30 = {1 / (a['lam50'] * a['D'] / 30):.0f} (PD1 [150,600]; P3 [250,400]); "
                  f"lam50(3)/lam50(1.111) = {b['lam50'] / a['lam50']:.2f} (P4 [7,12]); lam50(R=2) = {c['lam50']:.4g} "
                  f"(P4 0.035-0.04; Term 3 literal {1 / (2 * math.log(2000)):.4f}; with d=0.45 {0.45 / (2 * math.log(2000)):.4f}; "
                  f"Hossjer {HOSSJER:.4f})")
    for T in CHECKS:
        ok = sorted((k[2], v["lam50"]) for k, v in out.items() if k[0] == "hard" and k[3] == T and v["lam50"] == v["lam50"])
        rmin = next((R for R, l in ok if l >= HOSSJER), None)
        print(f"T={T}: smallest grid R with lam50 >= Hossjer 0.0351 (in-model D~17): {rmin}")
    for R in (round(1 / 0.9, 6), 2.0):
        for T in (10000, 20000):
            ds = [(K, out.get(((("hard" if K == 1000 else "Kscale")), K, R, T))) for K in (500, 1000, 4000)]
            print(f"D-invariance R={R:.3f} T={T}: " + "; ".join(
                f"K={K}: D={d['D']:.2f} lam50={d['lam50']:.4g} lam50*D={d['lam50'] * d['D']:.4f}" for K, d in ds if d))


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "smoke"
    workers = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    if which == "analyse":
        analyse()
    else:
        run_stage(which, workers)
