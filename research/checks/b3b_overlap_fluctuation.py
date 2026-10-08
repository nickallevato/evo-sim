"""B3b / B3c -- Day's best case for k != mu: overlapping generations + fluctuating N (Balloux & Lehmann 2012).

THROWAWAY research check. Run:  research/.venv/bin/python -I research/checks/b3b_overlap_fluctuation.py
Seeds fixed (SeedSequence(20261008)); per-scenario replicate SEs reported.  Runtime ~ 5-9 min on 12 cores.

PRE-REGISTERED PREDICTIONS (copied from docs/research/claims/B3b-*.md and B3c-*.md before any run; items marked
[R4] were added by this check, before the first run, from the B&L equations):
  Claim B3b file:
   (i)   s = 0 (no overlap), any N(t): k = mu per generation (B&L, quoted: "population size fluctuations do not
         affect substitution rates at neutral loci in a population with discrete nonoverlapping generations").
   (ii)  s > 0, N constant: k = mu(1 - s) per time step, k = mu per average generation time (1/(1-s)).
   (iii) s > 0 with fluctuating N: k departs from (ii) by an amount set by the N(t) statistics (B&L eq 3, 8, 9).
   Would change verdict: (i) violated (supports Day); (iii) departure <= a few percent for human-like parameters
   (then the effect cannot give factors 0.74 or 32.3).
  Claim B3c file:
   Claimant (Day): k/mu = 0.743 for the human population in 2025.
   Opposing: a neutral lineage in a growing WF population has P_fix = 1/(2 N_i) (N at birth), so the long-run rate
   stays mu; any transient is a lag (B1b), not a rate change. B3b scenario (i) is the direct test of B3c.
   Sensitivity already derived in the claim file: 0.87 (2 cohorts) ... 0.60 (20 cohorts) at ratio 1.485/cohort.
  [R4] additions, derived from B&L eq (3) with pi_j = 1/N_j:
   (a) With a constant survival s that is feasible (s <= N_j/N_i on every transition), k/mu = 1 - s*E[N_i/N_j]
       over transitions; by AM-GM on a cycle E[N_i/N_j] >= 1, so fluctuation REDUCES k below mu(1-s), by roughly
       s*r^2/2 per step for log-size steps +-r.  Human-like (s=0.96/yr, r=1.6%/yr): about -0.3% (negligible).
   (b) Growth (births per capita 1 - s*N_{t-1}/N_t) RAISES the instantaneous arrival rate of eventual fixers;
       for the Day cohort window (1.6%/yr, s=0.96) about +38% during growth, not -26%.  The sign B&L stress is
       positive for realistic demographies ("generally translate into an acceleration").
   (c) B&L cannot give 0.743 at human-like parameters with biologically ordered survival; only an
       "unrealistic" ordering (survival high when shrinking, low when growing) lowers k, bounded by the
       feasibility constraint s_21 <= N_1/N_2.
   (d) RRME's 0.743 is a window artefact: k/mu -> 1/(1+q) as the window lengthens (q = 1/growth ratio per cohort).
   (e) Single-mutant fixation probability for a mutant born in cohort i of a growing population is 1/N_i
       (frequency martingale), not 1/N_t; so P_fix * N_i = 1 (Day: N_i / N_t).
"""
import os
import sys
import time
from multiprocessing import Pool

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import wf_b3c1 as w

SEED = 20261008
U = 0.5


def cyc_path(sizes, last_survival_zero=True, s_grow=1.0):
    c = len(sizes)
    P = np.zeros((c, c))
    for i in range(c):
        P[i, (i + 1) % c] = 1
    S = np.full((c, c), s_grow)
    if last_survival_zero:
        S[c - 1, 0] = 0.0
    return np.array(sizes), P, S


def scenario_list():
    sc = []
    sc.append(("A0 constant N=100, s=0 (control)",) + (np.array([100]), np.array([[1.0]]), np.array([[0.0]])))
    sc.append(("A1 constant N=100, s=0.5",) + (np.array([100]), np.array([[1.0]]), np.array([[0.5]])))
    sc.append(("A2 constant N=100, s=0.9",) + (np.array([100]), np.array([[1.0]]), np.array([[0.9]])))
    Ns, P, S = w.two_state(50, 150, .5, .5, 0, 0, 0, 0)
    sc.append(("B1 fluctuating {50,150} alpha=.5, NO overlap",) + (Ns, P, S))
    Ns, P, S = cyc_path([40, 60, 90, 135, 160], last_survival_zero=False, s_grow=0.0)
    sc.append(("B2 fluctuating 5-state growth/bottleneck cycle, NO overlap",) + (Ns, P, S))
    Ns, P, S = w.two_state(50, 150, .5, .5, .5, .5, .5, 1 / 3)
    sc.append(("C1 {50,150} alpha=.5, overlap s=.5 (feasible: s21=1/3)",) + (Ns, P, S))
    Ns, P, S = w.two_state(50, 150, .5, .5, 1, 1, 1, 0)
    sc.append(("C2 {50,150} B&L eq(11) extreme (s21=0, else 1)",) + (Ns, P, S))
    Ns, P, S = w.two_state(150, 450, .5, .5, .5, .5, .5, 1 / 3)
    sc.append(("C1x3 same as C1 with all N x3 (scaling check)",) + (Ns, P, S))
    # Beverton-Holt cycle, B&L eq (15): N_{i+1} = s N_i + r N_i/(1+eta N_i), then bottleneck (all adults die)
    s_, r_, eta = 0.8, 0.4, 0.01
    K = (s_ + r_ - 1) / (eta * (1 - s_))
    sizes = [20]
    while sizes[-1] < 0.9 * K:
        n = sizes[-1]
        sizes.append(int(round(s_ * n + r_ * n / (1 + eta * n))))
    Ns, P, S = cyc_path(sizes, True, s_)
    sc.append((f"C3 Beverton-Holt cycle (s={s_}, r={r_}, eta={eta}, K={K:.0f}, c={len(sizes)}) + total-adult-death bottleneck",)
              + (Ns, P, S))
    return sc


def timescales(Ns, P, S):
    S2 = w.realize_survival(Ns, S)
    b, nbar = w.bl_births_and_size(Ns, P, S2)
    tau = 4 * nbar * nbar / max(b, 1e-9)   # 4*N*Tg steps, with Tg = N/b
    return tau, b, nbar, S2


def main():
    t0 = time.time()
    print("=== Part 1: verify B&L eq (8) transcription against generic eq (3) ===")
    for args in [(50, 150, .5, .5, .5, .5, .5, 1 / 3), (50, 150, .3, .6, .7, .4, .9, .1), (20, 200, .5, .5, 1, 1, 1, 0)]:
        Ns, P, S = w.two_state(*args)
        a = w.bl_k_over_mu(Ns, P, S)
        b = w.bl_two_state_eq8(*args)
        print(f"  args={args}: generic={a:.6f} eq8={b:.6f}")
        assert abs(a - b) < 1e-9
    # B&L eq (11): ks = 2 - N1/N2
    Ns, P, S = w.two_state(50, 150, .5, .5, 1, 1, 1, 0)
    Ns_c, P_c, S_c = w.two_state(50, 50, .5, .5, 1, 1, 1, 0)
    print("  eq(11) check: ks =", w.bl_k_over_mu(Ns, P, S) / w.bl_k_over_mu(Ns_c, P_c, S_c), "expected", 2 - 50 / 150)

    print("\n=== Part 2: simulation vs B&L eq (3) (k/mu per time step; U=%.2f per newborn; 16 reps) ===" % U)
    rows = []
    with Pool(12) as pool:
        for name, Ns, P, S in scenario_list():
            tau, b, nbar, S2 = timescales(Ns, P, S)
            T = int(10 * tau)
            burn = int(8 * tau)
            T = max(T, 3000)
            kth = w.bl_k_over_mu(Ns, P, S2)
            res = w.run_reps(Ns, P, S2, U, T, burn, 16, SEED + len(rows), pool)
            sm = w.summarize(res, U)
            Tg = nbar / b
            kgen = kth * Tg
            ks = sm["k"] / kth
            z = (sm["k"] - kth) / sm["k_se"]
            rows.append((name, kth, sm, kgen, Tg, z))
            print(f"{name}\n   N-bar={nbar:.1f} births/step={b:.2f} Tg={Tg:.2f} steps; steps={T}(+{burn} burn)"
                  f"\n   theory k/mu per step = {kth:.4f}; sim fixations/(U T) = {sm['k']:.4f} +/- {sm['k_se']:.4f} (z={z:+.2f});"
                  f" arrivals/(U T) = {sm['arr']:.4f} +/- {sm['arr_se']:.4f}"
                  f"\n   per average generation time: theory k*Tg/mu = {kgen:.4f}; sim = {sm['k'] * Tg:.4f}"
                  f"   [elapsed {time.time() - t0:.0f}s]", flush=True)

    print("\n=== Part 3: human-like demographies, exact B&L eq (3) (no simulation; effects below sim resolution) ===")
    s = 0.96   # annual survival; mean generation time 1/(1-s) = 25 y
    print(f"  annual survival s={s} (Tg={1 / (1 - s):.0f} y); constant-demography k/mu per step = {1 - s:.3f}")
    print("  (a) symmetric exponential growth/decline cycle, rate r per year, constant feasible survival:")
    for r in (0.005, 0.016, 0.03, 0.039):
        L = int(round(np.log(3.28) / r)) if r < 0.03 else 40
        up = [np.exp(r * i) for i in range(L)]
        sizes = np.concatenate([up, up[::-1][1:-1]]) * 1e6  # big N; rounding irrelevant for analytics
        c = len(sizes)
        Ns, P, S = cyc_path(list(sizes), False, s)
        # decline steps need s <= N_j/N_i
        for i in range(c):
            j = (i + 1) % c
            S[i, j] = min(s, Ns[j] / Ns[i])
        k = w.bl_k_over_mu(Ns, P, S, check=False)
        print(f"     r={r:.3f}/yr: range x{Ns.max() / Ns.min():.2f}; k/mu = {k:.5f}; standardized ks = k/(1-s) = {k / (1 - s):.5f};"
              f" theory 1-(s/(1-s))(cosh r-1) = {1 - s / (1 - s) * (np.cosh(r) - 1):.5f}")
    print("  (b) Day's window: ONE-WAY growth 2.5->8.2 (1.6%/yr, 75 y). Instantaneous eventual-fixer arrival rate relative to mu(1-s):")
    rr = (8.2 / 2.5) ** (1 / 75) - 1
    print(f"      growth rate {rr:.4f}/yr; births/N = 1 - s/(1+r) = {1 - s / (1 + rr):.4f} vs constant {1 - s:.4f}; ratio = {(1 - s / (1 + rr)) / (1 - s):.3f}")
    print(f"      total excess over the whole episode, in units of U: s*ln(N_end/N_start) = {s * np.log(8.2 / 2.5):.3f} (one-off, finite)")
    print("  (c) growth then catastrophic bottleneck (all adults die), 75 y growth at 1.6%/yr, s=0.96 (B&L eq 14 type):")
    Nsg = 2.5 * np.exp(np.log(8.2 / 2.5) * np.arange(76) / 75)
    Ns, P, S = cyc_path(list(Nsg), True, s)
    k = w.bl_k_over_mu(Ns, P, S, check=False)
    print(f"      k/mu per step = {k:.4f}; ks = {k / (1 - s):.3f}  (positive, contrived: a cycle that kills every adult once per 75 y)")
    print("  (d) B&L 2-state, N2/N1 = 3.28: scan survival (s11,s22,s12,s21 in [0,1], feasibility s21<=N1/N2), alpha=.5; ks range:")
    N1, N2 = 1.0, 3.28
    best_lo, best_hi = (9, None), (-9, None)
    ref_lo = None
    grid = np.linspace(0, 1, 11)
    for s11 in grid:
        for s22 in grid:
            for s12 in grid:
                for s21 in np.linspace(0, N1 / N2, 6):
                    Ns, P, S = w.two_state(N1, N2, .5, .5, s11, s22, s12, s21)
                    Nc, Pc, Sc = w.two_state(N1, N1, .5, .5, s11, s22, s12, s21)
                    kc = w.bl_k_over_mu(Nc, Pc, Sc, check=False)
                    if kc < 1e-6:
                        continue
                    ks = w.bl_k_over_mu(Ns, P, S, check=False) / kc
                    if ks < best_lo[0]:
                        best_lo = (ks, (s11, s22, s12, s21))
                    if ks > best_hi[0]:
                        best_hi = (ks, (s11, s22, s12, s21))
    print(f"      min ks = {best_lo[0]:.3f} at (s11,s22,s12,s21)={tuple(round(x, 2) for x in best_lo[1])}")
    print(f"      max ks = {best_hi[0]:.3f} at (s11,s22,s12,s21)={tuple(round(x, 2) for x in best_hi[1])}")
    print("      biologically ordered subset (survival higher when growing, s12>=s11,s22>=s21): ")
    lo_o, hi_o = 9, -9
    for s11 in grid:
        for s22 in grid:
            for s12 in grid:
                for s21 in np.linspace(0, N1 / N2, 6):
                    if not (s12 >= max(s11, s22) - 1e-9 and s21 <= min(s11, s22) + 1e-9):
                        continue
                    Ns, P, S = w.two_state(N1, N2, .5, .5, s11, s22, s12, s21)
                    Nc, Pc, Sc = w.two_state(N1, N1, .5, .5, s11, s22, s12, s21)
                    kc = w.bl_k_over_mu(Nc, Pc, Sc, check=False)
                    if kc < 1e-6:
                        continue
                    ks = w.bl_k_over_mu(Ns, P, S, check=False) / kc
                    lo_o, hi_o = min(lo_o, ks), max(hi_o, ks)
    print(f"      ordered range of ks: [{lo_o:.3f}, {hi_o:.3f}]")

    print("\n=== Part 4 (B3c): Day's RRME k/mu = (sum N_i^2 / sum N_i)/N_t ===")
    N4 = [2.5, 4.0, 6.1, 8.2]
    print(f"  4 cohorts as published: {w.rrme(N4):.4f}  (paper: 0.743)")
    g = (8.2 / 2.5) ** (1 / 3)
    print(f"  growth ratio per 25-y cohort g={g:.4f}")
    for nc in (2, 3, 4, 6, 10, 20, 100):
        print(f"    window of {nc:>3} cohorts: k/mu = {w.rrme_geometric(g, nc):.3f}")
    print(f"  limit 1/(1+1/g) = {1 / (1 + 1 / g):.3f};  for constant N: {w.rrme([5, 5, 5, 5]):.3f}")
    print("  alternative published-data windows (ratio from actual census, e.g. 1900-2025 not in the paper; not used)")

    rng = np.random.default_rng(SEED + 1000)
    print("\n  B3c-(e) single-mutant P_fix, NON-overlapping, N follows cohort series x10 (diploid N = 25,40,61,82 then 82)")
    Ncoh = [25, 40, 61, 82]
    M = [2 * n for n in Ncoh]  # gene copies, WF haploid-equivalent
    reps = 400000
    for i0 in range(4):
        path = M[i0:] + [M[-1]] * 3000
        surv = [0] * (len(path) - 1)
        pf, nfix = w.single_mutant_pfix(path, surv, reps, rng)
        se = pf / np.sqrt(max(nfix, 1))
        print(f"    mutant born in cohort {i0} (M={M[i0]}): P_fix = {pf:.5f} +/- {se:.5f}; P_fix*M_i = {pf * M[i0]:.3f} (martingale: 1)"
              f"; Day's 1/M_t implies {M[i0] / M[-1]:.3f}")

    print("\n  B3c-(e2) single-mutant P_fix WITH overlap: s=0.96/yr, N grows 1.6%/yr from 100 to 328 over 75 steps, then constant")
    N0 = 100
    path = [int(round(N0 * (1 + rr) ** t)) for t in range(76)]
    tail = [path[-1]] * 60000
    path = path + tail
    surv = [int(round(0.96 * path[t])) for t in range(len(path) - 1)]
    surv = [min(sv, path[t + 1]) for t, sv in enumerate(surv)]
    pf, nfix = w.single_mutant_pfix(path, surv, 150000, rng)
    se = pf / np.sqrt(max(nfix, 1))
    print(f"    newborn mutant at t=0 (N={path[0]}): P_fix = {pf:.5f} +/- {se:.5f}; P_fix*N_0 = {pf * path[0]:.3f} (martingale: 1);"
          f" Day-type 1/N_final would give {path[0] / path[75]:.3f}")
    print(f"\n[total elapsed {time.time() - t0:.0f}s]")


if __name__ == "__main__":
    main()
