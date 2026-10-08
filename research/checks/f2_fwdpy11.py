"""F2 cross-check with fwdpy11 (diploid, h=0.5, genic) against wf_f2 (haploid-equivalent) at one point. THROWAWAY.

Run: research/.venv/bin/python -I research/checks/f2_fwdpy11.py   (seed 777)

PRE-REGISTERED PREDICTION (written before the run): the substitution rate from an independent diploid
implementation (fwdpy11, N=1000, s=0.01 per copy, h=0.5, selected mutations only, U_b=0.001*... see POINTS)
agrees with wf_f2's rate within combined 2 SE at (i) low supply, r=free-ish (R_map=20 Morgans, i.e. effectively
unlinked): R ~ 1; (ii) 2N*U_b = 2 at R_map=1.5 where wf_f2 gives R ~ 0.9 (see results/R4-F2-A.md).
A disagreement > 2.5 SE would flag a bug in wf_f2.
NOTE (found in a first run, which gave R=0.50 exactly): in fwdpy11 het = 1+h*S, hom = 1+scaling*S, so per-copy s
requires S=2s, h=0.5, scaling=1. The first (mis-specified) run is reported in results/R4-F2-A.md as a spec error.
fwdpy11 model: positions uniform on [0,1); recombination = PoissonInterval(0,1,R_map) crossovers per meiosis
(same as wf_f2 map mode); mutation rate U_b per gamete, multiplicative fitness, soft selection (Wright-Fisher,
fixed N). Fixations = pop.fixations after burn.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import fwdpy11
import wf_f2 as w
from multiprocessing import Pool

N = 1000
s = 0.01
POINTS = [(0.1, 20.0), (2.0, 1.5), (2.0, 20.0)]   # (2N*U_b, R_map)
BURN, T = 3000, 12000


def nfixed_after(MU, R, seed, L):
    """Number of selected mutations at frequency 1 after L generations (identical seed => identical
    trajectory prefix, so differences between two L's count fixations in the interval)."""
    U = MU / (2 * N)
    pop = fwdpy11.DiploidPopulation(N, 1.0)
    rng = fwdpy11.GSLrng(seed)
    params = fwdpy11.ModelParams(nregions=[], sregions=[fwdpy11.ConstantS(0, 1, 1, 2 * s, 0.5)],
                                 recregions=[fwdpy11.PoissonInterval(0, 1, R)],
                                 rates=(0, U, None), gvalue=fwdpy11.Multiplicative(1.0),
                                 demography=fwdpy11.ForwardDemesGraph.tubes([N], burnin=L, burnin_is_exact=True),
                                 simlen=L, prune_selected=False)
    fwdpy11.evolvets(rng, pop, params, 100)
    return int((np.array(pop.mcounts) == 2 * N).sum()) + len(pop.fixations)


def run(args):
    MU, R, seed = args
    return (nfixed_after(MU, R, seed, BURN + T) - nfixed_after(MU, R, seed, BURN)) / T


if __name__ == "__main__":
    reps = 8
    for MU, R in POINTS:
        tasks = [(MU, R, 777 + i) for i in range(reps)]
        with Pool(6) as p:
            rates = p.map(run, tasks)
        m, se = w.mean_se(rates)
        k0 = w.indep_rate(2 * N, MU / (2 * N), s)
        print("fwdpy11 2NU_b=%g R_map=%g: rate %.4g +- %.2g, indep %.4g, R=%.3f +- %.3f" % (MU, R, m, se, k0, m / k0, se / k0))
