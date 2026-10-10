"""B2/B post hoc diffusion table -- post hoc, after reviews f55e1ca (correctness, steelman-day, steelman-critic).

Not pre-registered; no prediction scored.  Kimura (1955) neutral diffusion conditional on fixation, p -> 0:
  F(T) = 1 + sum_i (-1)^i (2i+1) exp(-i(i+1) T / 4N_e)  (end-of-window flux / mu, HL's k(T)/mu)
  delivered fraction from an empty start = (1/T) int_0^T F du  (Day's own E = mu L int F, Q34, Z22903977)
  computed by Simpson quadrature (the termwise closed form converges too slowly at small T/N_e).
Rows: H8 census 1e5, V_k 5 (N_e 57,143) at 2 My and at HL's lineage window 6.5 My (l.252); at the ceiling X
(T = 4N_e); field coalescent N_e 1e4 / 2.5e4 at 2 and 6.5 My (external rows); 25 y generations.
Also the exact/exp ratio F / exp(-pi^2 N_e/T) at T/N_e = 1, 2 (diffusion, for the P3 prefactor note).
"""
import math

def F(x, n=400):  # x = T / N_e
    return 1 + sum((-1) ** i * (2 * i + 1) * math.exp(-i * (i + 1) * x / 4) for i in range(1, n))

def Favg(x, m=20000):  # Simpson on [0, x]; F(u) set to 0 for u < 0.02 (true value < 1e-200)
    h = x / m
    f = [0.0 if k * h < 0.02 else F(k * h) for k in range(m + 1)]
    return h / 3 * (f[0] + f[-1] + 4 * sum(f[1:-1:2]) + 2 * sum(f[2:-1:2])) / x

rows = [("H8 census 1e5, V_k 5, 2 My", 2e6 / 25 / 57143), ("H8 census 1e5, V_k 5, 6.5 My (HL l.252)", 6.5e6 / 25 / 57143),
        ("at ceiling X (T = 4N_e)", 4.0), ("field N_e 1e4, 2 My [external]", 8.0), ("field N_e 2.5e4, 6.5 My [external]", 10.4),
        ("field N_e 1e4, 6.5 My [external]", 26.0)]
print("| input | T/N_e | F(T) flux | (1/T) int F delivered |")
for lab, x in rows:
    print(f"| {lab} | {x:.2f} | {F(x):.4f} | {Favg(x):.4f} |")
for x in (1.0, 2.0):
    print(f"exact/exp at T/N_e = {x}: {F(x) / math.exp(-math.pi ** 2 / x):.1f}")
