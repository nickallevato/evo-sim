"""D1 FIX PASS (POST HOC; written after the three D1 reviews): RNA first-passage along the neutral network, and a uniform-draw comparator for the
Metropolis-walk sampler.  Committed before its first run.
Run: research/.venv/bin/python -I research/checks/d1_fix_rna_fp.py [--smoke]   -> results/raw/d1_fix_rna_fp.json, d1_fix_rna_fp.out
(workhorse, 6 processes)

FIRST PASSAGE (the critic-review suggestion; answers 'how many neutral substitutions until a background with a one-step route to S2 appears?').
 Targets: the 8 targets with L <= 50.  Genotypes A (pool) and B (start points) are regenerated with the SAME seeds as the main run
 (stream [SEED,2,cfgid,0], K_A=40, K_B=60).  S2 pools (drawn from the one-step neighbourhoods of A, 60 per class): E0 exact (uniform over
 distinct), E1 (within 2 bp, d_bp(S1,S2)>=5), E2g (different shape, helices >= S1's; may be empty at L=30).  From each of 16 start genotypes
 B[i] a neutral walk is run: each ACCEPTED step is a single-nucleotide substitution that leaves the MFE structure unchanged (rejection
 proposals are counted separately).  At every accepted step (including step 0 = the start) the one-step neighbourhood is scanned; for each
 (S2, class) the first step at which a route exists is recorded (censored at 150 steps).  Reported: fraction of (start,S2) pairs with a route by
 step n for n in {0,1,2,5,10,20,50,100,150}; median first-passage step among those found; mean proposals per accepted step.
 Conversion to the Day-family window is done in the write-up: neutral substitutions available in a locus of L sites over T generations =
 L * mu * nu * T (mu = 1.2e-8 per site per generation, nu = neutral fraction), against the steps needed.

UNIFORM COMPARATOR (correctness review finding 4).  For targets with fold frequency f >= 1e-4 (the four L=30 targets, rand50_0, rand50_1,
rand50_2) draw 40 + 40 genotypes UNIFORMLY from the whole neutral set by rejection from pair-compatible sequences (no walk).  Report mean
neutrality nu, mean pairwise Hamming/L (walk samples were 0.40-0.59), and reach and m|reach for E0/E1 exactly as in the main run (pool
from the first 40, evaluated on the other 40), side by side with the same quantities from 40 + 40 walk samples (the main-run chain).
Predictions (stated before the run): uniform pairwise Hamming/L 0.70-0.75; uniform reach 0.6-1.0x the walk reach for E0 and E1;
m|reach unchanged within noise; first passage: E0 median >= 20 accepted steps and < 50% found within 5 steps; E2g found at step 0 for >= 40%.
"""
import os, sys, json, time, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import d1_sequence_space_spike as D

SMOKE = "--smoke" in sys.argv
STEPS = 150
CHECK = [0, 1, 2, 5, 10, 20, 50, 100, 150]


def classes_hit(sts, S2s, cls):
    """boolean array over S2s: does any structure in sts belong to class(S2)?"""
    st_set = set(sts)
    if cls == "E0":
        return np.array([s in st_set for s in S2s])
    if cls == "E1":
        return np.array([any(D.dbp(t, s) <= 2 for t in st_set) for s in S2s])
    shapes = {D.shape5(t) for t in st_set}
    return np.array([D.shape5(s) in shapes for s in S2s])


def make_pools(A_scans, S1, rng, npool):
    sh1, nh1 = D.shape5(S1), D.nhelix(S1)
    distinct = sorted({s for sts in A_scans for s in sts if s != S1})
    cands = {"E0": distinct,
             "E1": [s for s in distinct if D.dbp(s, S1) >= 5],
             "E2g": [s for s in distinct if D.shape5(s) != sh1 and D.nhelix(s) >= nh1]}
    pools = {}
    for c, cand in cands.items():
        if cand:
            pools[c] = [cand[i] for i in rng.choice(len(cand), size=min(npool, len(cand)), replace=False)]
    return pools


def single_stats(A, B, S1, rng, npool=60):
    """reach / m|reach for E0, E1, E2g, pool from A, evaluated on B."""
    sA = [[D.fold(m) for m in D.neighbors(x)] for x in A]
    pools = make_pools(sA, S1, rng, npool)
    sB = [[D.fold(m) for m in D.neighbors(x)] for x in B]
    res = {}
    for c, S2s in pools.items():
        M = np.zeros((len(B), len(S2s)), int)
        for i, sts in enumerate(sB):
            cnt = collections.Counter(sts)
            if c == "E0":
                M[i] = [cnt.get(s, 0) for s in S2s]
            elif c == "E1":
                M[i] = [sum(v for t, v in cnt.items() if D.dbp(t, s) <= 2) for s in S2s]
            else:
                shc = collections.Counter()
                for t, v in cnt.items():
                    shc[D.shape5(t)] += v
                M[i] = [shc.get(D.shape5(s), 0) for s in S2s]
        pos = M[M > 0]
        res[c] = dict(reach=float((M > 0).mean()), m_pos=float(pos.mean()) if pos.size else None, m_all=float(M.mean()), n_pool=len(S2s))
    return res


def uniform_samples(rng, S1, n, maxtries):
    out, tries = [], 0
    while len(out) < n and tries < maxtries:
        tries += 1
        s = D.compat_seq(rng, S1)
        if D.fold(s) == S1:
            out.append(s)
    return out, tries


def fp_job(job):
    cfgid, name, L, S1, seed = job
    t0 = time.time()
    KA, KB = (40, 60)
    nstart = 2 if SMOKE else 16
    steps = 5 if SMOKE else STEPS
    rng = np.random.default_rng(np.random.SeedSequence([D.SEED, 2, cfgid, 0]))
    cur = D.neutral_walk(rng, seed, S1, 50 * L)
    smp = []
    for _ in range(KA + KB):
        cur = D.neutral_walk(rng, cur, S1, 10 * L)
        smp.append(cur)
    A, B = smp[:KA], smp[KA:]
    rng2 = np.random.default_rng(np.random.SeedSequence([D.SEED, 12, cfgid, 0]))
    sA = [[D.fold(m) for m in D.neighbors(x)] for x in A]
    pools = make_pools(sA, S1, rng2, 10 if SMOKE else 60)
    res = dict(name=name, L=L, kind="fp", n_pool={c: len(v) for c, v in pools.items()})
    first = {c: [] for c in pools}  # per class list of arrays (start, S2) first-passage step (inf = censored)
    props, accs = 0, 0
    for i in range(nstart):
        seq = B[i]
        fp = {c: np.full(len(S2s), np.inf) for c, S2s in pools.items()}
        for step in range(steps + 1):
            sts = [D.fold(m) for m in D.neighbors(seq)]
            for c, S2s in pools.items():
                hit = classes_hit(sts, S2s, c)
                fp[c][hit & np.isinf(fp[c])] = step
            if step == steps:
                break
            # one accepted neutral substitution
            while True:
                props += 1
                j = int(rng.integers(L))
                nb = D.BASES[int(rng.integers(4))]
                if nb == seq[j]:
                    continue
                cand = seq[:j] + nb + seq[j + 1:]
                if D.fold(cand) == S1:
                    seq = cand
                    accs += 1
                    break
        for c in pools:
            first[c].append(fp[c])
    res["proposals_per_accept"] = props / max(accs, 1)
    res["curves"] = {}
    for c, lst in first.items():
        F = np.concatenate(lst)
        found = F[np.isfinite(F)]
        res["curves"][c] = dict(by_step={str(n): float((F <= n).mean()) for n in CHECK if n <= steps}, median_found=float(np.median(found)) if found.size else None,
                                found_by_end=float(np.isfinite(F).mean()), n_pairs=int(F.size))
    res["wall"] = time.time() - t0
    D.say("fp done", name, round(res["wall"]))
    return res


def uni_job(job):
    cfgid, name, L, S1, seed, f = job
    t0 = time.time()
    n = 4 if SMOKE else 40
    rng = np.random.default_rng(np.random.SeedSequence([D.SEED, 13, cfgid, 0]))
    U, tries = uniform_samples(rng, S1, 2 * n, int(2 * n / max(f, 1e-6) * 3) + 100)
    res = dict(name=name, L=L, kind="uni", n_uniform=len(U), tries=tries)
    if len(U) < 2 * n:
        res["note"] = "not enough uniform samples"
        return res
    nus = [np.mean([D.fold(m) == S1 for m in D.neighbors(x)]) for x in U]
    ham = [sum(a != b for a, b in zip(U[i], U[j])) / L for i in range(len(U)) for j in range(i + 1, len(U))]
    res["uniform"] = dict(nu=float(np.mean(nus)), nu_se=float(np.std(nus) / np.sqrt(len(nus))), hamming=float(np.mean(ham)))
    rng3 = np.random.default_rng(np.random.SeedSequence([D.SEED, 14, cfgid, 0]))
    res["uniform"]["single"] = single_stats(U[:n], U[n:], S1, rng3)
    # walk comparator, same sizes
    rngw = np.random.default_rng(np.random.SeedSequence([D.SEED, 2, cfgid, 0]))
    cur = D.neutral_walk(rngw, seed, S1, 50 * L)
    W = []
    for _ in range(2 * n):
        cur = D.neutral_walk(rngw, cur, S1, 10 * L)
        W.append(cur)
    nusw = [np.mean([D.fold(m) == S1 for m in D.neighbors(x)]) for x in W]
    hamw = [sum(a != b for a, b in zip(W[i], W[j])) / L for i in range(len(W)) for j in range(i + 1, len(W))]
    res["walk"] = dict(nu=float(np.mean(nusw)), nu_se=float(np.std(nusw) / np.sqrt(len(nusw))), hamming=float(np.mean(hamw)))
    res["walk"]["single"] = single_stats(W[:n], W[n:], S1, np.random.default_rng(np.random.SeedSequence([D.SEED, 14, cfgid, 0])))
    res["wall"] = time.time() - t0
    D.say("uni done", name, round(res["wall"]))
    return res


def dispatch(x):
    kind, job = x
    return fp_job(job) if kind == "fp" else uni_job(job)


def main():
    specs = D.make_targets(SMOKE)
    nn = json.load(open(os.path.join(D.RAW, "d1_nn.json")))
    tasks = []
    for ci, (name, L, db, seed) in enumerate(specs):
        if L > 50:
            continue
        tasks.append(("fp", (ci, name, L, db, seed)))
        f = nn[name]["f"] if name in nn else 0
        if f >= 1e-4 or SMOKE:
            tasks.append(("uni", (ci, name, L, db, seed, f if f > 0 else 0.01)))
    tasks.sort(key=lambda t: -t[1][2])
    out = {"fp": {}, "uni": {}}
    with Pool(2 if SMOKE else 6, maxtasksperchild=1) as p:
        for r in p.imap_unordered(dispatch, tasks):
            out[r["kind"]][r["name"]] = r
    tag = "_smoke" if SMOKE else ""
    json.dump(out, open(os.path.join(D.RAW, f"d1_fix_rna_fp{tag}.json"), "w"), indent=1, default=float)
    for k, v in sorted(out["fp"].items()):
        D.say(k, "L", v["L"], "props/accept", round(v["proposals_per_accept"], 2))
        for c, cv in v["curves"].items():
            D.say("   ", c, "n_pairs", cv["n_pairs"], "by_step", {a: round(b, 3) for a, b in cv["by_step"].items()}, "median_found", cv["median_found"])
    for k, v in sorted(out["uni"].items()):
        if "uniform" not in v:
            D.say(k, v.get("note"))
            continue
        D.say(k, "uniform nu", round(v["uniform"]["nu"], 3), "hamming", round(v["uniform"]["hamming"], 3), "| walk nu", round(v["walk"]["nu"], 3), "hamming", round(v["walk"]["hamming"], 3))
        for c in v["uniform"]["single"]:
            u, w = v["uniform"]["single"][c], v["walk"]["single"].get(c)
            D.say("    ", c, "uniform reach", round(u["reach"], 3), "m|reach", u["m_pos"], "| walk reach", w and round(w["reach"], 3), "m|reach", w and w["m_pos"])


if __name__ == "__main__":
    main()
