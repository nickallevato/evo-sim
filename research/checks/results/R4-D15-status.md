# R4 D15 status: Hössjer's "far exceeds 9 My" (partial; main sweep NOT run)

Scope of this note: the baseline reproductions and the engine validation are done. The 714-cell sweep that
answers the claim has not been launched, so **no verdict on D15 is proposed here** and no claim file was touched.

## Files
- Pre-registered script: `research/checks/d15_waiting_time.py`, commit **b74b6d6** (md5 `455430cd77c187446a1b9ff22f4ada9b`, identical on na-workhorse). Predictions P1–P9 are in its docstring. The docstring discloses that the analytic reproductions were prototyped in scratch before the commit.
- Run on na-workhorse (4 workers): `analytic`, `ds_moran`, `valid`. Outputs `results/raw/d15_{analytic,ds_moran,valid}.{out,json,jsonl}`, host record `raw/d15.host`.
- Fetched sources (untrusted, gitignored, in `sources/raw/`): `d15-hossjer2021/hossjer2021.pdf` (CC BY, sha256 8933f93e…), `d15-durrett2008/` (author preprint of the Genetics paper, PMC page), `d15-behe2004/`, `d15-lynch2005/` (PMC pages), `d15-panda/` (Panda's Thumb, not yet read).

## The claim as fixed
Hössjer MITTENS review p.8 (HO-12): "…my prediction is that the waiting time for several genes to change expression (so that their expressions match that of humans rather than chimps) far exceeds 9 million years." Model: Hössjer, Bechly & Gauger 2021, haploid Moran, m genes, L=1000, binding site W (6–10), K targets, mismatches d_max, μ=1e-8, N=1e4, fitness by number of genes done, back-mutation c, fixed-state phase-type approximation. 9 My = 360,000 generations at 25 y (450,000 at 20 y).

## Baselines: all pass
| Baseline | Result |
|---|---|
| B1 Hössjer 2021 Tables 4, 5, 9 (fixed-state chain, 37 printed entries) | worst deviation 0.3% (e.g. m=1: 5.3813e7; m=4 c=1: 2.3985e9; W=6 d_max=1: 4.527e4; K=3 W=6: 1.10e7) |
| B2 Durrett & Schmidt 2008, Theorem 1 | human 8.70e6 generations = 218 My at 25 y (paper: 8.66e6, 216 My); ×0.747 = 163 My (paper 162); Drosophila 34,800 generations (paper 34,600); neutral-B factor 2236; Thm 4 factor 2.20 |
| B3 D&S Table 2 by an independent Moran implementation (n=1000, 2000 reps) | Sim/Pred: case1 1.583 (pub 1.565), case2 1.144 (1.150), case3 1.034 (1.048), case4 0.986 (0.997), case5 0.817 (0.781), Drosophila 1.291 (1.273): all within the ±0.12 tolerance |
| B4 Behe & Snoke 2004 rate model (my CTMC reading; equations are not in the extracted text) | λ=3: 1.8e11 / 5.1e16 vs text ~1e11 / 1e17; λ=6: 2.2e21 vs ~1e22 (ratio 0.21), but 5.3e31 vs ~1e30 at 1e6 generations (ratio 52, **outside** the one-order tolerance); λ=7: 5.2e24 vs >1e25. Their abstract's 1e9 bound is not contradicted (λ=2 gives 8.8e7 for 1e8 generations, so it is not reproduced as a value) |
| B5 Lynch 2005 | asymptote 2Nμ n/(20+n) = 1.43e-6 N reproduces. The 10^6 yr headline rests on figure data and is not numerically reproduced |

Reading: Hössjer's printed numbers are arithmetically correct under his stated model. D&S's own numbers say a specific inactivate-then-create pair takes ~160–220 My in humans (N=1e4), so the two sides agree on that arithmetic and differ on what the target is.

## What `valid` shows
- **Engine vs theory (P8, neutral): pass.** WF engine, f=100, stationary start, R=300, against the chain: ratios 0.966–1.043 for all m=1–4, c=0/1 (m=4, c=1: 2.41e9 vs 2.40e9).
- **Tunneling check (P9): pass.** Three-type chain, M=2000: sim/Theorem 1 (2N=M) = 0.70; with a deleterious intermediate (1-r=0.02), sim/Theorem 4 = 1.10. R=60 (SE ~13%).
- **Scaling (Ne=1e4, f=1/3/10/100, R=60):**
  - Neutral (m=2, k=30): mean 3.38e6 / 3.39e6 / 4.48e6 / 3.12e6. Invariant within the noise (f=10 is +32%, about 2 SE).
  - V4 valley (1e-4): 1.18e7 / 1.17e7 / 1.11e7 / 1.40e7, invariant for f ≤ 10.
  - Final-only benefit (Fin2, k=3): 7.1e6 / 8.9e6 / 7.8e6 / 9.8e6: within ~25% to f=10, +37% at f=100.
  - Stepping stones S2 (1%/step, m=2, k=1): 2.45e5 / 3.0e5 / 3.1e5 / 5.9e5; p9 0.82 / 0.65 / 0.65 / 0.35. **Scaling is not valid for strong selection**: f=10 turns s=0.01 into 0.1 (+27% in mean, p9 0.82→0.65) and f=100 breaks it.
  - V3, V2 valleys: essentially never finish by 900 My at any f (V3 m=2: 1–2 of 60 finish; V2: 0), so scaling for deep valleys is untestable at this cap.
- **Predictions that failed:** P8's claim that valley cells with N_e·d ≥ 3 lengthen by >30% at f=10 was not seen (V4 flat; V3/V2 undetermined). P8's "S cells within 25% for f ≤ 10" fails marginally for S2 at f=10 (+27%).
- **Consequence for the sweep as pre-registered:** N_e=1e5 runs at f=10. For the S2/S3/Fin2/Fin3 cells that inflates s to 0.1/0.01, so those N_e=1e5 cells will be biased long (conservative for Hössjer, i.e. they understate how fast beneficial stepping stones are). Fix before launch: run N_e=1e5 selected cells at f=3 or report them with this bias flagged; label any change as post hoc with its own commit.
- **Chain vs engine:** the single-mutation no-ST chain overstates the time when intermediates are deleterious (Fin2 k=3: chain 1.15e7, sim 7.1e6; V4 k=30: chain 1.77e7, sim 1.2e7; V3/V2: chain 1e21–1e178, sim finite or censored at 3.6e7). Tunneling and not only the printed no-ST column matters there.

## Early reads (not verdicts)
- Neutral m=2, k=30 (any of 30 equivalent targets): mean ~3.4e6 generations (85 My), p9 ≈ 0.02: still "exceeds 9 My".
- Stepping stones of +1% per step, specific W=6 site, N_e=1e4, m=2: mean 2.45e5 generations (6 My), p9 = 0.82. This is where "far exceeds" fails: it needs intermediates that are not beneficial.

## Cost and next-session command
Sweep = **714 cells × 60 reps**, N_e = 1e4 unscaled (M = 2e4), N_e = 1e5 at f = 10. Reference timings from `valid` (4 workers, shared host): unscaled V-type cells at k=30 took 800–1500 s each; scaled f=10 cells 40–110 s. Expect several hours; the slow cells are N_e=1e4, high k_mult, valley or neutral with m ≥ 3. Each cell has a 1500 s wall guard (unfinished replicates are censored at their clock; `complete_at_900My` flags cells whose p9/p90 are still valid).

```sh
cd /home/na/projects/evo-sim
ssh -o BatchMode=yes na-workhorse 'uptime'    # check load first
rsync -a research/checks/d15_waiting_time.py na-workhorse:projects/evo-sim/research/checks/
ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup research/.venv/bin/python -I research/checks/d15_waiting_time.py sweep 4 > research/checks/results/raw/d15_sweep.out 2>&1 &'
# afterwards: rsync -a --include='d15_*' --exclude='*' na-workhorse:projects/evo-sim/research/checks/results/raw/ research/checks/results/raw/
```
Decide the N_e=1e5 scale factor (see above) and commit any script change before launching.

## Not done
The sweep (m=1–4 × redundancy × intermediate fitness × N_e × recombination), the flip table, the "who this helps" section, the review trio, and all claim/argmap integration.
