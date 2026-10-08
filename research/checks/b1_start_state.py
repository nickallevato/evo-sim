"""Check B1 (THROWAWAY): neutral substitutions over a finite window — empty vs full 'pipeline'.

Claim B1 (Day, Zenodo 22903977 'Intrinsic Irrelevance', pass-1 wording; verbatim pending R1p2):
  E[F(T)] = mu*L * int_0^T F_X(u) du  ≈ mu*L*(T - 4Ne), "rather than the naive product mu*L*T".
Counter-claim B6 (critics): the ancestral population was already at mutation-drift equilibrium,
  so the pipeline was full at the split and expected substitutions = U*T.

PRE-REGISTERED PREDICTIONS (2026-10-07, before first run):
  P1 Empty start: simulated E[C(T)] matches U*int_0^T F_X(u)du (F_X = CDF of conditional fixation
     time, estimated independently), i.e. Day's formula is internally valid for an empty start, and
     approaches U*(T-4N) for T >> 4N.
  P2 Equilibrium start: E[C(T)] = U*T at all T (stationarity); the -4N deficit is absent.
  P3 Therefore the B1 correction is a statement about the initial condition, not about k=mu.
"""
import numpy as np
from wf import neutral_substitutions, single_locus

rng = np.random.default_rng(11)
N, U = 100, 0.5
T = 20 * N
reps = 60
grid = np.array([N // 2, N, 2 * N, 4 * N, 6 * N, 10 * N, 20 * N]) - 1

# F_X from independent single-locus runs
fixed, t = single_locus(N, 0.0, 2_000_000, rng)
tf = np.sort(t[fixed])
F = lambda x: np.searchsorted(tf, x, side="right") / len(tf)
intF = np.cumsum([F(u) for u in range(1, T + 1)])

emp = np.array([neutral_substitutions(N, U, T, rng, start="empty") for _ in range(reps)])
eq = np.array([neutral_substitutions(N, U, T, rng, start="equilibrium") for _ in range(reps)])

print(f"N={N}, U={U}/gen, reps={reps}; conditional mean t_fix={tf.mean():.0f} (4N={4*N}); n_fix_samples={len(tf)}")
print(f"{'T':>6} {'U*T':>8} {'U*intF':>8} {'U(T-4N)+':>9} | {'empty sim':>14} | {'equil sim':>14}")
ok = True
for g in grid:
    Tg = g + 1
    e_m, e_se = emp[:, g].mean(), emp[:, g].std(ddof=1) / np.sqrt(reps)
    q_m, q_se = eq[:, g].mean(), eq[:, g].std(ddof=1) / np.sqrt(reps)
    pred_empty = U * intF[g]
    print(f"{Tg:>6} {U*Tg:>8.1f} {pred_empty:>8.1f} {max(U*(Tg-4*N),0):>9.1f} | {e_m:>8.1f}±{e_se:<5.1f} | {q_m:>8.1f}±{q_se:<5.1f}")
    ok &= abs(e_m - pred_empty) < 3 * e_se + 1e-9 or e_se == 0
    ok &= abs(q_m - U * Tg) < 3 * q_se + 1e-9
print("P1/P2:", "CONSISTENT" if ok else "INCONSISTENT — inspect")
