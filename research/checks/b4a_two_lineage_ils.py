"""Check B4a (THROWAWAY): two-lineage divergence with ancestral polymorphism. Seed 20261009.

PRE-REGISTERED PREDICTION (copied from docs/research/claims/B4a-two-lineage-divergence-with-ils.md):
  Claimant (Day): ancestral term negligible; fixed count is lowered by the empty-pipe correction.
  Opposing (standard theory, CSAC): pairwise divergence includes a coalescent term that does not depend on
  fixation latency; the fixed-substitution count is not the observable.
  Verdict rule: if simulated d matches 2*mu*T + theta_anc to within SE and the fixed-count deficit does not
  alter d, Day's empty-pipe correction does not apply to the observable (B1a internal verdict stands, relevance
  falls). If d falls below the standard prediction by about mu*L*4Ne, Day is supported.
  Formal: E[d] = 2 mu T + 4 Ne_anc mu per site (T generations). Derived (claim file): mu=1.2e-8, T=252,000:
  2muT = 6.05e-3; totals 0.65% (Ne_anc 1e4), 1.24% (1.32e5), 1.56% (1.98e5) vs CSAC 1.23% total, fixed <=1.06%.
  Grid pre-registered in the claim: Ne_anc {1e4,3e4,1.32e5,1.98e5}, lineages 1e4 const, T {50k,100k,252k}
  (no third outgroup/ILS-fraction in the forward run: that needs gene trees; msprime baseline only).
  Added before the run: lineage Ne (1e4, 4.6e4) variant; the polymorphic-but-different part of d should be
  about 4 mu Ne_anc minus the part of ancestral diversity that has sorted, and fixed differences should
  exceed 2mu(T-4Ne_lineage) (Day) because ancestral alleles also sort into fixed differences.
Scaling (E4): N_anc_sim = 1000 (500 for Ne_anc=1e4), f = Ne_anc/N_anc_sim, U_sim = 800/(4 N_anc_sim),
  per-site value = count * mu * f / U_sim. msprime used only as the coalescent baseline for E[d] (2 mu E[tmrca]).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
from wf2 import burn_in, schedule, evolve, pair_stats

MU = 1.2e-8                      # parameters.yaml mutation.mu_per_site_per_gen.pedigree_human
TS = (50_000, 100_000, 252_000)
ANC = (1.0e4, 3.0e4, 1.32e5, 1.98e5)
CFG = {"A both 1e4": (1.0e4, 1.0e4), "B H 1e4 / C 4.6e4": (1.0e4, 4.6e4), "C both = Ne_anc": (None, None)}
SEED = 20261009
THETA = 800.0

def one_rep(args):
    anc, n, seed = args
    rng = np.random.default_rng(seed)
    f = anc / n; U = THETA / (4 * n)
    state = burn_in(n, U, 20 * n, rng)
    out = {}
    for cname, (nh, nc) in CFG.items():
        nh = anc if nh is None else nh; nc = anc if nc is None else nc
        Tmax = max(TS)
        cps = [int(round(t / f)) for t in TS]
        Ah = schedule([(0, nh)], f, Tmax); Ac = schedule([(0, nc)], f, Tmax)
        sh = evolve(state, 2 * n, Ah, U, rng, cps)
        sc = evolve(state, 2 * n, Ac, U, rng, cps)
        k = mu_f = MU * f / U
        for t, g in zip(TS, cps):
            ps = pair_stats(sh[g], sc[g])
            out[(cname, t)] = tuple(ps[x] * k for x in ("d", "fixdiff", "polydiff", "d_pre", "fixdiff_pre", "fixdiff_post"))
    return out

def msprime_d(anc, nh, nc, T, reps=20000, seed=1):
    import msprime
    dem = msprime.Demography()
    dem.add_population(name="H", initial_size=nh)
    dem.add_population(name="C", initial_size=nc)
    dem.add_population(name="A", initial_size=anc)
    dem.add_population_split(time=T, derived=["H", "C"], ancestral="A")
    ts = msprime.sim_ancestry({"H": 1, "C": 1}, demography=dem, ploidy=2, sequence_length=1,
                              num_replicates=reps, random_seed=seed)
    t = np.array([x.first().tmrca(0, 2) for x in ts])
    return 2 * MU * t.mean(), 2 * MU * t.std(ddof=1) / np.sqrt(reps)

if __name__ == "__main__":
    for anc in ANC:
        n = 500 if anc <= 1.0e4 else 1000
        reps = 80 if anc <= 1.0e4 else 150
        ss = np.random.SeedSequence([SEED, int(anc)]).spawn(reps)
        with Pool(3) as p:
            res = p.map(one_rep, [(anc, n, s) for s in ss])
        print(f"\n## Ne_anc = {anc:.3g}  (N_anc_sim={n}, f={anc/n:.0f}, reps={reps}); per-site values in %")
        print("| config | T | d sim | 2muT+theta | d msprime | fixed diffs | poly-but-diff | Day 2mu(T-4Ne_lin) | d - 2muT | theta_anc |")
        print("|---|---|---|---|---|---|---|---|---|---|")
        for cname, (nh, nc) in CFG.items():
            nh_ = anc if nh is None else nh; nc_ = anc if nc is None else nc
            for t in TS:
                a = np.array([r[(cname, t)] for r in res]) * 100
                m = a.mean(0); se = a.std(0, ddof=1) / np.sqrt(reps)
                pred = (2 * MU * t + 4 * anc * MU) * 100
                day = MU * ((t - 4 * nh_) + (t - 4 * nc_)) * 100
                dm, dse = msprime_d(anc, nh_, nc_, t)
                print(f"| {cname} | {t} | {m[0]:.3f}+-{se[0]:.3f} | {pred:.3f} | {dm*100:.3f}+-{dse*100:.3f} | "
                      f"{m[1]:.3f}+-{se[1]:.3f} | {m[2]:.3f}+-{se[2]:.3f} | {max(day,0):.3f} | {m[0]-2*MU*t*100:.3f} | {4*anc*MU*100:.3f} |")
