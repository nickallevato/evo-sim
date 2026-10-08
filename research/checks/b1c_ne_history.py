"""Check B1c (THROWAWAY): per-lineage neutral fixed substitutions under sourced Ne histories, equilibrium
ancestral start, versus U*T.   Seed 20261008.

PRE-REGISTERED PREDICTION (copied from docs/research/claims/B1c-ancestral-pipeline-state-ne-history.md):
  Day (IR): E[count] ~ mu*L*(T - 4Ne) with a deficit of order mu*L*4Ne_eff for any Ne_eff reflecting expansion.
  Standard theory (B1b): from an equilibrium ancestral state a later contraction gives an excess >= 0, constant
  Ne gives exactly mu*L*T, only sustained expansion gives a deficit bounded by mu*L*4*dN.
  Sign pre-registered: if PSMC shows decline from >=1.3e5 to ~1e4 before the split-to-present window,
  dK >= 0 (excess), which falsifies Day's deficit for that scenario; a deficit appears only if Ne rises by dN with
  4dN a sizeable fraction of T.
  Added here (written before the run): analytic telescoped estimate K/(U T) ~ 1 + 4(N_anc - N_end)/T when the final
  relaxation (~4 N_end) fits inside T; the excess consists of ANCESTRAL alleles fixing in the lineage and so is
  not by itself a human-chimp difference count (see B4a).
Scaling (E4): N_anc_sim = 1000 (f = N_anc/1000), U_sim = theta/(4 N_anc_sim) with theta = 800 held fixed,
  T_sim = T/f; validated below at N_anc_sim in {500,1000,2000} and against wf.substitutions_demog.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from multiprocessing import Pool
from wf import substitutions_demog
from wf2 import burn_in, schedule, evolve

T_REAL = 252_000          # parameters.yaml generations_available.day_2026 (6.3 My / 25 y)
THETA = 800.0
REPS = 150
SEED = 20261008

# Ne pieces in real generations since split. Anc = Yoo 2025 value. Sourced numbers in comments.
def human(anc):
    return {
        "H0 const at ancestral (control)": [(0, anc)],
        "H1 step to 1.0e4 at split (textbook 1e4)": [(0, 1.0e4)],
        "H2 step to 1.5e4 (PM2013 Table1 humans 13.1-16.2k)": [(0, 1.5e4)],
        "H3 Takahata-like: 1e5 first half, then 1e4": [(0, 1.0e5), (T_REAL // 2, 1.0e4)],
        "H4 1e4 then growth to 5e4 in last 2% (sensitivity, unsourced)": [(0, 1.0e4), (int(T_REAL * 0.98), 5.0e4)],
    }

def chimp(anc):
    return {
        "C0 const at ancestral (control)": [(0, anc)],
        "C1a step to 3.09e4 (PM2013 Table1 common chimp low)": [(0, 3.09e4)],
        "C1b step to 6.18e4 (PM2013 Table1 common chimp high)": [(0, 6.18e4)],
        "C2 PSMC-text: anc to 3 Mya, 1.8e4 to 1 Mya, 4.6e4 last 1 My": [(0, anc), (132_000, 1.8e4), (212_000, 4.6e4)],
        "C3 bonobo-like constant 1.785e4 (PM2013 Table1 bonobo mid)": [(0, 1.785e4)],
    }

def analytic(pieces, anc):
    n_end = pieces[-1][1]
    return 1 + 4 * (anc - n_end) / T_REAL

def one_rep(args):
    anc, n_anc_sim, seed, scen = args
    rng = np.random.default_rng(seed)
    f = anc / n_anc_sim
    U = THETA / (4 * n_anc_sim)
    state = burn_in(n_anc_sim, U, 20 * n_anc_sim, rng)
    out = {}
    for name, pieces in scen.items():
        Narr = schedule(pieces, f, T_REAL)
        s = evolve(state, 2 * n_anc_sim, Narr, U, rng)[len(Narr)]
        ut = U * len(Narr)
        out[name] = (s["pre_fixed"] / ut, s["post_fixed"] / ut)
    return out

def run(anc, n_anc_sim, scen, reps, seed):
    ss = np.random.SeedSequence([SEED, seed]).spawn(reps)
    with Pool(3) as p:
        res = p.map(one_rep, [(anc, n_anc_sim, s, scen) for s in ss])
    rows = {}
    for name in scen:
        a = np.array([r[name] for r in res])
        tot = a.sum(1)
        rows[name] = (tot.mean(), tot.std(ddof=1) / np.sqrt(reps), a[:, 0].mean(), a[:, 1].mean())
    return rows

def validate_demog_ref(anc=1.98e5, n=500, reps=40):
    """Cross-check evolve() vs wf.substitutions_demog for scenario H1 (equilibrium start)."""
    f = anc / n; U = THETA / (4 * n)
    Narr = schedule([(0, 1.0e4)], f, T_REAL)
    vals = []
    for i in range(reps):
        rng = np.random.default_rng(np.random.SeedSequence([SEED, 99, i]))
        fix = substitutions_demog(lambda g: int(Narr[g]), U, len(Narr), rng, burn_in=20 * n, N_burn=n)
        vals.append(fix.sum() / (U * len(Narr)))
    return np.mean(vals), np.std(vals, ddof=1) / np.sqrt(reps)

if __name__ == "__main__":
    print(f"T={T_REAL} gens, theta={THETA}, reps={REPS}, seed={SEED}")
    print("\n## Scale validation (E4): H1 = step 1.98e5 -> 1e4 at split; K/(U T) total")
    H1 = {"H1": [(0, 1.0e4)]}
    for n in (500, 1000, 2000):
        r = run(1.98e5, n, H1, 60, n)["H1"]
        print(f"N_anc_sim={n:5d}  K/UT = {r[0]:.3f} +- {r[1]:.3f}   (pre {r[2]:.3f}, post {r[3]:.3f})   analytic 1+4dN/T = {1+4*(1.98e5-1e4)/T_REAL:.3f}")
    print("\nSecond validation: constant control at N_anc_sim 500/2000 (expect 1)")
    for n in (500,):
        r = run(1.98e5, n, {"c": [(0, 1.98e5)]}, 60, 10 + n)["c"]
        print(f"N_anc_sim={n:5d}  K/UT = {r[0]:.3f} +- {r[1]:.3f}")
    m, se = validate_demog_ref()
    print(f"\nCross-check vs wf.substitutions_demog (N_anc_sim=500, 40 reps, H1): {m:.3f} +- {se:.3f}")
    r = run(1.98e5, 500, H1, 60, 500)["H1"]
    print(f"evolve() same setting: {r[0]:.3f} +- {r[1]:.3f}")

    for anc, label in ((1.98e5, "HCB 1.98e5"), (1.32e5, "HCG 1.32e5")):
        for lin, fn in (("HUMAN", human), ("CHIMP", chimp)):
            scen = fn(anc)
            rows = run(anc, 1000, scen, REPS, int(anc) + len(lin))
            print(f"\n## {lin} lineage, ancestral Ne {label}; K_lineage/(U T), equilibrium start")
            print("| scenario | K/UT +- SE | from ancestral alleles | from new mutations | telescoped analytic | verdict |")
            print("|---|---|---|---|---|---|")
            for name, pieces in scen.items():
                m, se, pre, post = rows[name]
                v = "excess" if m - 2 * se > 1 else ("deficit" if m + 2 * se < 1 else "none")
                print(f"| {name} | {m:.3f} +- {se:.3f} | {pre:.3f} | {post:.3f} | {analytic(pieces, anc):.3f} | {v} |")
