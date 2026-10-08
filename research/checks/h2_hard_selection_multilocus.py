"""H2: Day's residual claim -- cost of selection / many simultaneous sweeps under HARD selection.
THROWAWAY research code; imports nothing from wf_f2/wf_hc except the Haldane conventions (D = ln(1/p0) for haploid
genic selection, checked in wf_hc.haldane_D_haploid).  Does not modify any existing file.
Run:  research/.venv/bin/python -I research/checks/h2_hard_selection_multilocus.py [validate|grid|all]
Seeds: numpy SeedSequence([SEED, stage, index...]) -- never hash().  Output: research/checks/results/h2_*.json

=====================================================================================================
CLAIMS UNDER TEST (quoted from docs/research/claims, IDs given)
  H  : "Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300
        generations, based on the reproductive cost each substitution imposes on a population."  (Z18168236)
  H  : "The 10% selective mortality is a total budget for the population, not a per-locus allocation."
       (Z18168236 s2.3)  -> parallel loci share the budget: sum s_i <= s_max.
  Gc : "the 'active zone' of intermediate-frequency alleles imposes a hard limit on pipeline capacity of
        approximately 230 simultaneous sweeps."  (Z18167588)
  H1 : 2026-05-07 retraction: Term 3 limits ADAPTIVE substitution only (~1e-12 /site/gen), not total k.
  H7 : Keightley 2012: U ~ 2.2 deleterious/diploid genome/gen (0.35 amino-acid changing); hard-selection
       mean fitness e^-U.  H2 (claim) Nunney 2003: environmental change -> hard selection for adaptation.

MODEL (haploid-equivalent genic bookkeeping, as in wf_f2.py: M = 2N gene copies; s per copy)
  * N_t individuals (cap K = M).  Each adult has a genome of "open loci".  The environment opens a new locus at
    Poisson(lam) per generation (treadmill: at an open locus the ancestral allele costs a factor exp(-s); the
    beneficial allele costs nothing).  Open locus closes when the beneficial allele fixes (a substitution).
    Absolute fitness of individual i:  w_i = exp(-s * (#open loci where i is ancestral)) * exp(-s_d * k_i)
    (multiplicative across loci; w<=1 so it is a genuine survival probability; no sign-cap tricks).
  * Supply: 'inf' (Haldane's setting: new locus opens with ONE beneficial copy present, p0 = 1/N; a lost copy is
    re-seeded) or finite: each ancestral copy at an open locus mutates at rate mu = sv/M per generation
    (sv = M*mu_b = supply per open locus per generation, "2N U_b" of the task); until the first mutant arises the
    locus is 'waiting' and every individual pays s for it (a real hard-selection cost).
  * Reproduction: free recombination (each open locus inherited independently from either random parent),
    random mating, juveniles J = f*N with f = min(R, K/N) (fecundity per adult, so J <= K; R = reproductive
    excess = max offspring per adult; density dependence acts before selection, Nunney-style, but with a
    ceiling form because the Ricker form R^(1-N/K) is unstable for ln R > 2 -- found in V1, see results).
    Equilibrium: N/K = wbar while R*wbar > 1; extinction when wbar < 1/R, i.e. total log-load > ln R.
    HARD: each juvenile survives with probability w (N can shrink, extinct if N < 20).
    SOFT: J = R*K juveniles, K adults drawn with probability proportional to w (relative fitness only).
  * Optional deleterious load: k_i ~ Binomial(k_a,1/2)+Binomial(k_b,1/2)+Poisson(U_del), w *= exp(-s_d k) (genic,
    s_d = 0.02).  U_del=0.35 (Keightley aa-changing) or 2.2 (Keightley whole genome; per DIPLOID genome per
    generation, used here as per-offspring Poisson mean as in wf_hc.mutload_run).
  Measured: substitution rate k_obs (fixed loci per gen, after burn-in); open-locus count; N/K; selective-death
  fraction 1-wbar of juveniles; cost per substitution D_obs = sum_t(-ln wbar_t)/n_subs  [compare Haldane
  haploid D = ln(1/p0)]; realised time-to-fixation vs isolated.

PRE-REGISTERED PREDICTIONS (written BEFORE any run of this file)
  Notation: D = cost per substitution in units of log-mean-fitness: for one sweep from p0, sum_t s(1-p_t) ~
  ln(1/p0) (+~1 for the stochastic early phase).  Haploid, p0 = 1/M.  lam = substitutions demanded per generation.
  P-Day (Day's model, literal): realised substitution rate capped at 0.10/30 = 1/300 = 0.0033 per generation
        regardless of R, s and number of loci ("10% is a total budget", Hc: ~230 concurrent sweeps at s=0.01).
        Operationalised: for lam >> 1/300 the population cannot maintain k = lam (it goes extinct, or k_obs
        saturates near 1/300, or realised death fraction stays <= 10%); parallelism does not help.
        Day-in-model variant: cap lam <= 0.10/D_model (D_model = ln M + 1 ~ 8 for M=1000: lam ~ 0.012).
  P-Std (critics / standard theory): the bound is the reproductive excess, not 10%: total log-load
        L = lam * D_eff (steady state, free recombination, sweeps independent) must satisfy L < ln R for the
        population to persist, because equilibrium N/K = exp(-L) (ceiling form) and extinction at L > ln R.  Hence
            lam_max(R) = ln R / D_model   (R=2: 0.69/8 ~ 0.09 ; R=20: 3.0/8 ~ 0.37 for M=1000),
        i.e. 25x to 100x above 1/300, with realised death fractions 1-e^-L far above 10% while the
        population persists.  Below lam_max, k_obs = lam (R_int = k_obs/lam = 1, no interference), mean
        number of simultaneously open loci n = lam * T_open (T_open = mean time open ~ (2/s) ln(M s)+waiting).
        Finite supply raises n (waiting cost s*n_wait added to L) and lowers lam_max.  Optional deleterious
        load subtracts: persistence needs lam*D_eff + U_del < ln R.
  Predicted flip: Day's regime (cap 1/300) holds only if ln R/D_model <~ 1/300, i.e. R-1 < 0.03 (R < ~1.03) or
        D enormous (D ~ 30*ln R/0.69).  For all R >= 1.3 (ln R >= 0.26) I predict the standard cap is >= 0.03,
        i.e. >= 9x above 1/300.  Dependence on active-locus count n: the standard model fails at n_crit =
        ln R/(s*mean open fraction); Day's 230 sweeps at s=0.01 corresponds to L = sum s*q ~ 2.3*mean-q; with
        mean-q ~ 0.5, L ~ 1.15 -> needs R >= 3.2.  Prediction: 230 concurrent sweeps persist for R=5, not R=2.
  Validation predictions: V1 per-seed fixation probability (single locus) = Kimura-type u=(1-e^-2s)/(1-e^-2Ms)
        divided by offspring-number variance factor; soft and hard-large-R agree within ~15%.
        V2 hard (R=20, tiny lam) k_obs == soft k_obs within sampling error.
  Result may falsify any of these; see results/R4-H2-hard.md.
=====================================================================================================
"""
import os
import sys
import json
import time
import math
import numpy as np
from multiprocessing import Pool

SEED = 20261030
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "results")


def run(M, s, lam, R, sv, mode, gens, burn, rng, U_del=0.0, s_d=0.02, max_open=700):
    """One replicate. sv=None -> infinite supply (seed at p0=1/N). Returns dict."""
    K = M
    N = M
    G = np.zeros((0, N), dtype=np.uint8)       # segregating open loci x individuals (1 = beneficial)
    t_open = []                                # open time of each segregating locus
    wait_t = []                                # open times of waiting loci
    kd = np.zeros(N, dtype=np.int32)
    mu = (sv / M) if sv is not None else 0.0
    lnR = math.log(R)
    n_fix = 0
    ttf = []
    acc = dict(sw=0.0, nopen=0.0, nfrac=0.0, nrec=0, dead=0.0, nseg=0.0)
    lnw_sum = 0.0
    fixes_rec = 0
    ext = False
    for t in range(burn + gens):
        if N < 20:
            ext = True
            break
        rec = t >= burn
        # ---- environment opens loci
        for _ in range(rng.poisson(lam)):
            if sv is None:
                col = np.zeros((1, N), dtype=np.uint8)
                col[0, rng.integers(0, N)] = 1
                G = np.vstack([G, col])
                t_open.append(t)
            else:
                wait_t.append(t)
        if len(t_open) + len(wait_t) > max_open:
            ext = True
            break
        # ---- reproduction
        if mode == "hard":
            f = min(R, K / N)
            J = int(f * N)
            J += int(rng.random() < f * N - J)
        else:
            J = int(R * K)
        if J < 2:
            ext = True
            break
        a = rng.integers(0, N, J)
        b = rng.integers(0, N, J)
        if G.shape[0] > 0:
            mask = rng.integers(0, 2, size=(G.shape[0], J), dtype=np.uint8).astype(bool)
            C = np.where(mask, G[:, a], G[:, b])
            nanc = (1 - C).sum(axis=0, dtype=np.int32) + len(wait_t)
        else:
            C = G[:, :J] if False else np.zeros((0, J), dtype=np.uint8)
            nanc = np.full(J, len(wait_t), dtype=np.int32)
        logw = -s * nanc
        kc = None
        if U_del > 0:
            kc = rng.binomial(kd[a], 0.5) + rng.binomial(kd[b], 0.5) + rng.poisson(U_del, J)
            logw = logw - s_d * kc
        w = np.exp(logw)
        wbar = w.mean()
        if mode == "hard":
            keep = rng.random(J) < w
        else:
            if J <= K:
                keep = np.ones(J, bool)
            else:
                keys = -np.log(rng.random(J)) / np.maximum(w, 1e-300)
                keep = np.zeros(J, bool)
                keep[np.argpartition(keys, K)[:K]] = True
        G = C[:, keep]
        if kc is not None:
            kd = kc[keep]
        else:
            kd = np.zeros(int(keep.sum()), dtype=np.int32)
        N = G.shape[1] if G.shape[0] > 0 else int(keep.sum())
        if N < 20:
            ext = True
            break
        # ---- mutation
        if sv is not None:
            if wait_t:
                # P(first beneficial arises at a waiting locus this gen) = 1-exp(-N mu)
                p = 1.0 - math.exp(-N * mu)
                hit = rng.random(len(wait_t)) < p
                if hit.any():
                    new_cols, keep_w = [], []
                    for tw, h in zip(wait_t, hit):
                        if h:
                            col = np.zeros((1, N), dtype=np.uint8)
                            col[0, rng.integers(0, N)] = 1
                            new_cols.append(col)
                            t_open.append(tw)
                        else:
                            keep_w.append(tw)
                    wait_t = keep_w
                    G = np.vstack([G] + new_cols) if G.shape[0] else np.vstack(new_cols)
            if G.shape[0] > 0 and mu > 0:
                nold = N - G.sum(axis=1, dtype=np.int64)
                nm = rng.binomial(nold, mu)
                for j in np.flatnonzero(nm):
                    idx = np.flatnonzero(G[j] == 0)
                    G[j, rng.choice(idx, size=min(nm[j], len(idx)), replace=False)] = 1
        # ---- fixation / loss
        if G.shape[0] > 0:
            cnt = G.sum(axis=1, dtype=np.int64)
            fixed = cnt == N
            lost = cnt == 0
            if fixed.any() or lost.any():
                for j in np.flatnonzero(fixed):
                    n_fix += 1
                    if rec:
                        fixes_rec += 1
                    ttf.append(t - t_open[j])
                newG = []
                newt = []
                for j in range(G.shape[0]):
                    if fixed[j]:
                        continue
                    if lost[j]:
                        if sv is None:
                            col = np.zeros(N, dtype=np.uint8)
                            col[rng.integers(0, N)] = 1
                            newG.append(col)
                            newt.append(t_open[j])
                        else:
                            wait_t.append(t_open[j])
                    else:
                        newG.append(G[j])
                        newt.append(t_open[j])
                G = np.array(newG, dtype=np.uint8).reshape(len(newG), N)
                t_open = newt
        if rec:
            acc["nrec"] += 1
            acc["nopen"] += len(t_open) + len(wait_t)
            acc["nseg"] += len(t_open)
            acc["nfrac"] += N / K
            acc["dead"] += 1.0 - wbar
            lnw_sum += -math.log(max(wbar, 1e-300))
    n = max(acc["nrec"], 1)
    return dict(ext=ext, k=fixes_rec / max(gens, 1), nopen=acc["nopen"] / n, nseg=acc["nseg"] / n,
                nfrac=acc["nfrac"] / n if not ext else 0.0, dead=acc["dead"] / n,
                D=(lnw_sum / fixes_rec) if fixes_rec > 0 else float("nan"),
                ttf=float(np.mean(ttf)) if ttf else float("nan"), nfix=n_fix, gens_run=acc["nrec"])


# ----------------------------------------------------------------------------------- validation V1
def seed_fix_prob(args):
    M, s, R, mode, trials, tag = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 1, tag, int(s * 1e4), int(R * 10), 0 if mode == "hard" else 1]))
    fixed = 0
    for _ in range(trials):
        N = M
        n1 = 1
        # single locus, haploid, genome = one site; track frequency exactly via two-parent sampling (free recomb is moot)
        g = np.zeros(N, dtype=np.uint8)
        g[0] = 1
        while True:
            f = min(R, M / N) if mode == "hard" else R
            J = int(f * N) if mode == "hard" else int(R * M)
            J += int(mode == "hard" and rng.random() < f * N - int(f * N))
            if J < 2:
                break
            par = rng.integers(0, N, J)
            ch = g[par]
            w = np.where(ch == 1, 1.0, math.exp(-s))
            if mode == "hard":
                keep = rng.random(J) < w
                g = ch[keep]
            else:
                if J <= M:
                    g = ch
                else:
                    keys = -np.log(rng.random(J)) / w
                    g = ch[np.argpartition(keys, M)[:M]]
            N = len(g)
            if N < 20:
                break
            c = int(g.sum())
            if c == 0:
                break
            if c == N:
                fixed += 1
                break
    return dict(M=M, s=s, R=R, mode=mode, trials=trials, fixed=fixed)


def kimura_u(M, s):
    return (1 - math.exp(-2 * s)) / (1 - math.exp(-2 * M * s))


def validate(pool):
    M, s, trials = 1000, 0.02, 1500
    jobs = []
    for mode, R in (("soft", 4), ("hard", 20), ("hard", 5), ("hard", 2)):
        for tag in range(4):
            jobs.append((M, s, R, mode, trials, tag))
    res = pool.map(seed_fix_prob, jobs)
    agg = {}
    for r in res:
        k = (r["mode"], r["R"])
        a = agg.setdefault(k, [0, 0])
        a[0] += r["fixed"]
        a[1] += r["trials"]
    u = kimura_u(M, s)
    out = []
    for (mode, R), (fx, tr) in agg.items():
        p = fx / tr
        out.append(dict(mode=mode, R=R, p_fix=p, se=math.sqrt(p * (1 - p) / tr), ratio_to_kimura=p / u, kimura_u=u,
                        fixed=fx, trials=tr))
    return out


# ----------------------------------------------------------------------------------- grid
def job(args):
    tag, M, s, lam, R, sv, mode, U_del, rep, gens, burn = args
    rng = np.random.default_rng(np.random.SeedSequence([SEED, 2, tag, rep]))
    t0 = time.time()
    r = run(M, s, lam, R, sv, mode, gens, burn, rng, U_del=U_del)
    r.update(dict(tag=tag, M=M, s=s, lam=lam, R=R, sv=sv, mode=mode, U_del=U_del, rep=rep, sec=time.time() - t0))
    return r


def build_jobs(stage):
    jobs = []
    tag = 0
    reps = 3
    if stage in ("A", "all"):
        # A: Haldane setting (inf supply), s=0.01, M=1000; lam scan x R
        for R in (2, 5, 10, 20):
            for lam in (0.0033, 0.01, 0.03, 0.06, 0.1, 0.2, 0.4):
                tag += 1
                for rep in range(reps):
                    jobs.append((tag, 1000, 0.01, lam, R, None, "hard", 0.0, rep, 2500, 1500))
        for lam in (0.0033, 0.03, 0.1, 0.2):          # soft reference
            tag += 1
            for rep in range(reps):
                jobs.append((tag, 1000, 0.01, lam, 4, None, "soft", 0.0, rep, 2500, 1500))
    if stage in ("B", "all"):
        # B: s dependence and finite supply (sv = M mu_b per open locus per gen)
        for s in (0.003, 0.03):
            for R in (2, 10):
                for lam in (0.01, 0.06, 0.2):
                    tag += 1
                    for rep in range(reps):
                        jobs.append((tag, 1000, s, lam, R, None, "hard", 0.0, rep, 2500, 1500))
        for sv in (0.5, 0.05):
            for R in (2, 10):
                for lam in (0.003, 0.01, 0.03):
                    tag += 1
                    for rep in range(reps):
                        jobs.append((tag, 1000, 0.01, lam, R, sv, "hard", 0.0, rep, 3000, 2000))
    if stage in ("C", "all"):
        # C: Keightley deleterious load on top
        for U in (0.35, 2.2):
            for R in (5, 10, 20, 50):
                for lam in (0.0033, 0.03, 0.1):
                    tag += 1
                    for rep in range(reps):
                        jobs.append((tag, 1000, 0.01, lam, R, None, "hard", U, rep, 2000, 1500))
    if stage in ("D", "all"):
        # D: N dependence (D grows with ln M)
        for M in (500, 4000):
            for R in (2, 10):
                for lam in (0.03, 0.1, 0.2):
                    tag += 1
                    for rep in range(2):
                        jobs.append((tag, M, 0.01, lam, R, None, "hard", 0.0, rep, 2500 if M < 4000 else 2000, 1500))
        # low R, human-like reproductive excess
        for R in (1.3, 1.6):
            for lam in (0.0033, 0.01, 0.03, 0.06):
                tag += 1
                for rep in range(reps):
                    jobs.append((tag, 1000, 0.01, lam, R, None, "hard", 0.0, rep, 2500, 1500))
    return jobs


def summarize(rows):
    import collections
    g = collections.defaultdict(list)
    for r in rows:
        g[(r["M"], r["s"], r["lam"], r["R"], r["sv"], r["mode"], r["U_del"])].append(r)
    out = []
    for k, rs in sorted(g.items(), key=lambda kv: tuple(str(x) for x in kv[0])):
        def m(key):
            v = [r[key] for r in rs if not (isinstance(r[key], float) and math.isnan(r[key]))]
            return float(np.mean(v)) if v else float("nan")
        out.append(dict(M=k[0], s=k[1], lam=k[2], R=k[3], sv=k[4], mode=k[5], U_del=k[6], reps=len(rs),
                        ext_frac=float(np.mean([r["ext"] for r in rs])), k_obs=m("k"),
                        R_int=m("k") / k[2], nopen=m("nopen"), nseg=m("nseg"), nfrac=m("nfrac"),
                        dead=m("dead"), D=m("D"), ttf=m("ttf"), sec=m("sec")))
    return out


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    os.makedirs(OUT, exist_ok=True)
    t0 = time.time()
    with Pool(3) as pool:
        if which in ("validate", "all"):
            v = validate(pool)
            json.dump(v, open(os.path.join(OUT, "h2_validate.json"), "w"), indent=1)
            for x in v:
                print("V1", x, flush=True)
            print("validate sec", time.time() - t0, flush=True)
        if which in ("A", "B", "C", "D", "grid", "all"):
            for st in (("A", "B", "C", "D") if which in ("grid", "all") else (which,)):
                jobs = build_jobs(st)
                rows = pool.map(job, jobs, chunksize=1)
                json.dump(rows, open(os.path.join(OUT, f"h2_raw_{st}.json"), "w"))
                sm = summarize(rows)
                json.dump(sm, open(os.path.join(OUT, f"h2_summary_{st}.json"), "w"), indent=1)
                print("stage", st, "jobs", len(jobs), "elapsed", time.time() - t0, flush=True)
                for x in sm:
                    print(st, {k: (round(v, 4) if isinstance(v, float) else v) for k, v in x.items()}, flush=True)
