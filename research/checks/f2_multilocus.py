"""F2 -- multi-locus interference (Day's strongest form of the throughput limit). THROWAWAY check.

Run: research/.venv/bin/python -I research/checks/f2_multilocus.py   (seed 4242; ~25-40 min on 11 cores;
set F2_QUICK=1 for a reduced grid)

PRE-REGISTERED PREDICTIONS (copied from docs/research/claims/F2-multi-locus-interference-feasibility.md,
written before this run; the sub-numbering below is my reading of its (a)-(c)):
 (a) r=1/2 (free), low supply (2N*U_b ~ 0.1), s=0.01: R = observed/(2N*U_b*u(s)) ~ 1
     (RESULTS F1: 0.3972 vs 0.3960 at a much higher supply, no interference).
 (b) r=0 (clonal) and N*U_b*s large: R < 1 (clonal interference); n_sw bounded by the number of
     segregating beneficial lineages. Extra (mine, from Desai-Fisher successional-mutations theory, recalled
     from memory): clonal k saturates ~ logarithmically in U_b, k = s(2ln(2Ns)-ln(s/U))/ln^2(s/U).
 (c) realistic human values: no pre-registered prediction for Day's cap (derivation not in corpus).
 Falsifiers stated in the claim: R >= 0.5 at human-like parameters falsifies a binding cap of order 230;
 R << 0.5 with r = 0.5 and soft selection supports Day.
 My additional pre-registration: with free recombination R stays ~1 until the number of loci in the 0.1<p<0.9
 'active zone' is large enough that the fitness variance of the population (sum of 2*s^2*p(1-p) over active
 loci, Robertson/Hill-Robertson effect) is comparable with s^2/..., i.e. R<0.8 needs n_mid of order 10^2-10^3 at
 s=0.01; low linkage (R_map=0.1 Morgan) behaves between clonal and free; R(clonal) falls with 2N*U_b.
Scale: N=1000 (M=2N=2000 copies) for s=0.01; same N for s=0.001 (2Ns=4, near-neutral-ish; stated limitation).
Selection: genic exp(sum s), soft; h=0.5 equivalent to additive per-copy s (see wf_f2 docstring).
"""
import os, sys, time, json, zlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import wf_f2 as w

SEED = 4242
QUICK = bool(os.environ.get("F2_QUICK"))


def job(args):
    s, M, mode, MU, rep, burn, T = args
    ss = np.random.SeedSequence([SEED, int(s * 1e4), M, int(MU * 100), rep, zlib.crc32(str(mode).encode()) % 9973])
    rng = np.random.default_rng(ss)
    r = w.sim(M, MU / M, s, mode, T, burn, rng)
    return (s, M, str(mode), MU, rep, r)


def main():
    tasks = []
    reps = 2 if QUICK else 4
    cfg = []
    modes = ['clonal', 0.1, 1.5, 'free']
    MUs = [0.1, 0.5, 2, 8] if QUICK else [0.1, 0.5, 2, 8, 32]
    M = 2000
    for mode in modes:
        for MU in MUs:
            k0 = w.indep_rate(M, MU / M, 0.01)
            T = int(np.clip(250 / k0, 10000, 120000))
            for rep in range(reps):
                tasks.append((0.01, M, mode, MU, rep, 3000, T))
    for mode in ['clonal', 'free']:
        for MU in [0.5, 4]:
            k0 = w.indep_rate(M, MU / M, 0.001)
            T = int(np.clip(250 / k0, 30000, 120000))
            for rep in range(reps):
                tasks.append((0.001, M, mode, MU, rep, 20000, T))
    tasks.sort(key=lambda t: -(t[6] + t[3] * 2000))   # heavy first
    t0 = time.time()
    with Pool(int(os.environ.get("NPROC", "3"))) as p:
        out = p.map(job, tasks, chunksize=1)
    print("elapsed %.0f s" % (time.time() - t0))
    cells = {}
    for s, M, mode, MU, rep, r in out:
        cells.setdefault((s, mode, MU), []).append(r)
    print("| s | mode | 2N*U_b | T_obs | indep 2NUu | sim rate | SE | R=sim/indep | SE(R) | n_mid | n_seg | DF clonal k (if valid) |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|")
    res = []
    for (s, mode, MU), rs in sorted(cells.items(), key=lambda kv: (-kv[0][0], str(kv[0][1]), kv[0][2])):
        k0 = w.indep_rate(2000, MU / 2000, s)
        rates = [r['rate'] for r in rs]
        m, se = w.mean_se(rates)
        nm = np.mean([r['n_mid'] for r in rs]); ns = np.mean([r['n_seg'] for r in rs])
        L = np.log(s / (MU / 2000))
        df = w.desai_fisher_k(2000, MU / 2000, s) if (mode == 'clonal' and 2 * np.log(2000 * s) > L) else float('nan')
        print("| %g | %s | %g | %d | %.3g | %.3g | %.2g | %.3f | %.3f | %.1f | %.0f | %s |" % (
            s, mode, MU, rs[0]['T_obs'], k0, m, se, m / k0, se / k0, nm, ns,
            "%.3g" % df if df == df else "n/a"))
        res.append(dict(s=s, mode=mode, MU=MU, k0=k0, rate=m, se=se, n_mid=nm, n_seg=ns))
    json.dump(res, open(os.environ.get("F2_OUT", "/dev/null"), "w"))


if __name__ == "__main__":
    main()
