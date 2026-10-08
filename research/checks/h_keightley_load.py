"""Check H7 (THROWAWAY): Keightley (2012) U = 2.2 deleterious load under HARD vs SOFT selection.
Seed: SeedSequence(20261009). Run: research/.venv/bin/python -I research/checks/h_keightley_load.py

PRE-REGISTERED PREDICTION (claim H7, written before the run):
 - Literature (Keightley): hard selection, multiplicative fitness: mean fitness W = e^-U = 0.11 for U = 2.2
   ("if each female were capable of producing 20 offspring, 18 of these progeny, on average, would need to
   undergo genetic death"); real populations can tolerate U if selection acts on relative fitness ("soft") or
   with synergistic epistasis.
 - Simulation predictions: (P1) HARD, multiplicative: population persists iff Fmax * e^-U > 2, i.e. Fmax > 18.1
   offspring per female; equilibrium N/K = 1 - U/ln(Fmax/2) (density-dependent fecundity before selection, same
   rule as treadmill_run); at Fmax <= 18 it goes extinct. (P2) SOFT: persists for any Fmax > 2; N/K = 1; mean
   absolute fitness need not equal e^-U (relative selection with limited surplus). (P3) synergistic epistasis
   raises W above e^-U and lowers the required Fmax.
 - Link to H: the same accounting (one genetic death per mutation, hard selection) that Haldane's cost uses gives an
   impossible requirement for the deleterious side; it is therefore not evidence that hard accounting is the right
   one for the beneficial side either. What this check cannot say: whether adaptation specifically is hard or soft.
 - Verdict-changing: if the hard accounting persisted at Fmax ~ 6-8 (natural fertility) with U = 2.2, H7's
   'implausible' claim would be wrong.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
import wf_hc as h

U = 2.2
K = 1000
reps = 6
gens = 500


def one(a):
    Fmax, regime, s, e, seed = a
    return h.mutload_run(K, U, s, Fmax, regime, gens, np.random.default_rng(np.random.SeedSequence(seed)), epistasis=e)


def summarize(outs):
    ext = sum(o["extinct"] for o in outs)
    live = [o for o in outs if not o["extinct"]]
    if not live:
        return f"extinct {ext}/{len(outs)}"
    f = lambda key: (np.mean([o[key] for o in live]), np.std([o[key] for o in live], ddof=1) / np.sqrt(len(live)) if len(live) > 1 else np.nan)
    N, W, k = f("Nfrac"), f("w"), f("kbar")
    return f"extinct {ext}/{len(outs)}  N/K={N[0]:.3f}±{N[1]:.3f}  mean w(adults)={W[0]:.4f}±{W[1]:.4f}  mean k={k[0]:.1f}"


if __name__ == "__main__":
    print(f"U={U}, e^-U={np.exp(-U):.4f}; hard persistence threshold Fmax > {2*np.exp(U):.1f}; K={K}, {reps} reps, {gens} gens", flush=True)
    jobs, keys, c = [], [], 0
    for (s, e, lab) in [(0.05, 0.0, "multiplicative s=0.05 (k_eq ~ U/s = 44)"),
                        (0.01, 0.0004, "synergistic w=exp(-0.01k-0.0004k^2)")]:
        for Fmax in (4, 8, 12, 17, 20, 30, 60):
            for reg in ("hard", "soft"):
                for r in range(reps):
                    c += 1
                    jobs.append((Fmax, reg, s, e, 20261009 * 1000 + c))
                keys.append((lab, s, e, Fmax, reg))
    with Pool(12) as p:
        res = p.map(one, jobs, chunksize=1)
    last = None
    for i, (lab, s, e, Fmax, reg) in enumerate(keys):
        if lab != last:
            print("\n##", lab); last = lab
        pred = ""
        if e == 0 and reg == "hard" and Fmax > 2 * np.exp(U):
            pred = f"  [pred N/K={1 - U/np.log(Fmax/2):.3f}]"
        print(f" Fmax={Fmax:<3} {reg:4s}: {summarize(res[i*reps:(i+1)*reps])}{pred}")
