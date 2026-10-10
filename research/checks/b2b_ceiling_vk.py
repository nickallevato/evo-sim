"""B2b -- Hard Limits census ceiling X = (Vk+2) G / 16 from N_e = (4N-2)/(Vk+2) and 4 N_e < G: simulate offspring variance.

Target: B2b (verbatim: 'N_e = (4N - 2) / (V_k + 2)', Z22129121 p.4; 'For a large, long-lived vertebrate the effective ceiling
falls to about ten thousand individuals', p.1; 'The human's is thirty-five thousand as a species, a hundred thousand as a
lineage. The elephant's is twenty-eight thousand', p.6).
Model (Cannings, no invention): N diploid parents, p0 = 0.5 exactly (N of 2N copies are A, genotypes shuffled). Parent i
contributes k_i gametes (iid, mean 2, variance Vk), transmits Binomial(k_i, g_i/2) A copies (Mendelian segregation);
p' = sum t_i / sum k_i. N_e(sim) = p0(1-p0) / (2 Var(p')) from 2e5 replicates, N = 100. Vk: Binomial(4,.5) -> 1;
Poisson -> 2; NegBin mean 2 -> 5, 10. Realised Vk is measured. Then the ceiling X = (Vk+2)G/16 is evaluated at Day's G
(algebra) and the Vk needed for Ne/N = 1e-3 (the 'ten thousand' regime) is printed.

Pre-registered predictions (2026-10-09):
  Day/Wright side: sim N_e within 5% of (4N-2)/(Vk_realised+2) at each Vk. X = (Vk+2)G/16 is then exact algebra.
  Critic side: the formula holds for iid Vk, but a Vk giving N_e/N ~ 1e-3 needs Vk ~ 4,000, so human Vk = 5 gives
  N_e/N ~ 0.57 (not 1e-4) and the abstract's 'about ten thousand' does not follow from Wright's formula; the ceiling table
  (35,000-114,000) is consistent with it only by treating census N_e ~ 0.57 N.
  Expected: ratios sim/Wright in [0.95, 1.05]; N_e/N: ~0.67 (Vk=1), 0.50 (2), 0.29 (5), 0.17 (10) (Wright, nominal).
  POST HOC (b2b, same day): those N_e/N values were a slip (I used 2/(Vk+2); Wright gives 4/(Vk+2): 1.33, 1.00, 0.57, 0.33) and the printed
  Vk for N_e/N = 1e-3 used the same slip (1,998 -> 3,998; for 0.1: 18 -> 38). Ratio predictions (sim/Wright) were the pre-registered test and are unaffected.
  Not tested: sourced human Vk, N_e(t), demes, overlapping generations, mean fixation time.
"""
import os, json
import numpy as np

rng = np.random.default_rng(77)
N, REPS = 100, 200000

def draw_k(Vk, size):
    if Vk < 2:
        m = round(2 / (1 - Vk / 2)); return rng.binomial(m, 2.0 / m, size)
    if Vk == 2:
        return rng.poisson(2.0, size)
    r = 4.0 / (Vk - 2.0); return rng.negative_binomial(r, r / (r + 2.0), size)

res = {}
print(f'N={N} reps={REPS}; Wright N_e = (4N-2)/(Vk+2)')
for Vk in (1.0, 2.0, 5.0, 10.0):
    pp = np.empty(REPS)
    kk_all = []
    for r in range(REPS // 1000):
        copies = np.zeros((1000, 2 * N), dtype=np.int8)
        copies[:, :N] = 1
        idx = np.argsort(rng.random((1000, 2 * N)), axis=1)
        copies = np.take_along_axis(copies, idx, axis=1)
        gen = copies[:, :N] + copies[:, N:]              # genotype of each parent (0,1,2), HW-like, sum fixed at N
        k = draw_k(Vk, (1000, N))
        t = rng.binomial(k, gen / 2.0)
        pp[r*1000:(r+1)*1000] = t.sum(1) / k.sum(1)
        kk_all.append(k.ravel())
    k = np.concatenate(kk_all)
    ne = 0.25 / (2 * pp.var(ddof=1))
    vr = k.var(ddof=1)
    w = (4 * N - 2) / (vr + 2)
    res[Vk] = dict(mean_k=k.mean(), var_k=vr, ne=ne, wright_realised=w)
    print(f'Vk nominal {Vk:>4}: realised mean {k.mean():.3f} var {vr:.3f}; N_e sim {ne:7.2f}  Wright(realised) {w:7.2f}  ratio {ne/w:.3f}  N_e/N {ne/N:.3f}')
print('Ceiling X = (Vk+2) G/16 at Day G values (algebra):')
for name, G in (('human lineage', 260000), ('human species', 80000)):
    print('  %-14s G=%d: ' % (name, G) + '  '.join(f'Vk={v:g}: {(v+2)*G/16:,.0f}' for v in (1, 2, 5, 10)))
print('Vk needed for Ne/N = 1e-3 (Wright, Ne/N = 4/(Vk+2)): %.0f ; for 0.1: %.0f' % (4/1e-3 - 2, 4/0.1 - 2))
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', 'raw', 'b2b.json'), 'w'), default=float)
