"""F1a -- Day's serial use of a latency-derived 19,800 vs parallel sweeps, at his own s and N_e (scaled).

Target: F1a (verbatim quotes in the claim file: the Education post para 17-18 'does not assume sequential fixation ... total
throughput', the Q&A 'N_e = 10,000 ... s = 0.001 ... t ~ 19,800 generations per fixation', 'The six-fixation figure ... comes
from the beneficial fixation time at s = 0.001'). Day's inputs: N_e = 1e4, s = 0.001, so 4Ns = 40 and latency
L = (2/s) ln(2N) = 19,807. Scaled to N = 1000, s = 0.01 (same 4Ns = 40; time compressed 10x; same scaling as F1/F1b),
L_sim = 200 ln(2000) = 1,520. Independent loci, genic s, infinite sites (no interference: that is F2; this is a throughput test only).
Serial reading: fixations in a window W = 7 L_sim (Day's 'seven') is W / L_sim = 7 whatever the mutation supply.
Cells: beneficial supply U_b chosen so Kimura rate 2N U_b u(s) = k/L_sim for k = 1 (the serial boundary), 10, 100.

Pre-registered predictions (2026-10-09):
  Day's model (G_f is a throughput that already contains parallelism): count = rate x W, set by supply, not by latency;
    cell k=1 mean in [5.5, 8.5] (Poisson mean 7), k=10 in [63, 77], k=100 in [630, 770].
  Critic's model (latency is not an inter-fixation spacing; divide by it only if supply is exactly serial): same counts;
    the serial count 7 is reproduced only at k=1; ratio observed/serial = ~k (within 10%).
  Shared: latency does not cap the count; the 19,800 'time per fixation' equals the spacing between fixations only when
    mean in-transit L(t) ~ 1 (k=1), where overlap still occurs. Dispersion var/mean of counts across reps in [0.6, 1.6].
  Not tested: interference, cost of selection, human-scale supply (F2, H, GAP-04); the non-sequitur verdict on F1a is unchanged
  by any outcome here unless Day's six/seven is shown to include a width factor (it does not, per the claim file).
"""
import os, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from wf import substitutions_demog, kimura_u

rng = np.random.default_rng(41)
N, s = 1000, 0.01
L = (2 / s) * np.log(2 * N)
W = int(round(7 * L)); reps = 48
u = kimura_u(N, s)
out = {'N': N, 's': s, 'L_sim': L, 'W': W, 'u': u, 'cells': {}}
print(f'N={N} s={s} 4Ns={4*N*s:.0f} Day-latency L_sim={L:.0f} W=7L={W} Kimura u={u:.5f}; real-scale Day latency 19807')
for k in (1, 10, 100):
    Ub = (k / L) / (2 * N * u)
    c = np.array([substitutions_demog(lambda g: N, Ub, W, rng, s=s, burn_in=3000, N_burn=N).sum() for _ in range(reps)])
    m, sd = c.mean(), c.std(ddof=1)
    out['cells'][k] = {'Ub': Ub, 'mean': m, 'sd': sd, 'sem': sd / np.sqrt(reps), 'pred': 7 * k, 'disp': sd**2 / m}
    print(f'k={k:<3} Ub={Ub:.3e} predicted {7*k:>4}  observed {m:7.2f} +- {sd/np.sqrt(reps):.2f}  var/mean {sd**2/m:.2f}  observed/serial(7) = {m/7:.2f}  in-transit ~ rate x ~850 = {k*850/L:.2f}')
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'results', 'raw', 'f1a.json'), 'w'), default=float)
