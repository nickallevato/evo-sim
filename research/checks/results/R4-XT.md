# R4 XT: cross-tool replication of the k-vs-mu and fixation-time results in fwdpy11

**Status: run, written up, combined review done (`REVIEW-R4-XT-combined.md`).** All statements are dialectic (rule RH). Low-stakes tier (tool validation).

## Files
- Script `research/checks/xt_cross_tool.py`, pre-registered at **da1c178**; post hoc size/bootstrap edit committed before any main run (see its docstring). Run `all 1` on na-workhorse (host record `raw/xt_all.host`, md5 dceff1ec...; log `raw/xt_all.out`; data `raw/xt_{b0n,b0s,b3,b1,b1b,b1c,fluct,cohort}.json`). fwdpy11 0.24.7 is the independent tool; SLiM was not available.
- Not expressible in fwdpy11 (Wright-Fisher only): the overlapping-generation rows of B3b/B3c; they stay numpy-only.

## Results against the pre-registered predictions
Criteria: |z| < 3 on the between-chunk SE (plus the stated tolerances); "agrees with numpy" needs tolerance to the exact target AND within 3 combined SE of the recorded numpy value.

| Item | fwdpy11 result | Verdict |
|---|---|---|
| B0.1 neutral P_fix = 1/2N | N=50 0.009706 (z -12.8), N=100 0.004917 (z -4.6), N=200 0.002483 (z -1.3) | **N=50, 100 miss** by 2.9% and 1.7%; N=200 met |
| B0.2 neutral mean t_fix | N=50 3.911N (z -3.3), N=100 3.953N (-2.2), N=200 3.970N (-1.2); SD within 2.3 SE | met except N=50 (0.6% low, z -3.3) |
| B0.3 Kimura u(s,N) | -1.2%, -1.3%, -1.9%, -4.9% (n=57) from target; all inside the 2% / MC tolerance | met (as the pre-registered 2% allowance; z -1.1 to -1.4) |
| B0.4 beneficial t_fix | 333.0 (target 333.9), 710.4 (703.0, +1.0%, z +5.2), 1417.9 (1407.1), N=1e4: 8417 (8480, -0.7%); Day's (2/s)ln2N is 1.9-3.2x higher | **met** at the 5% / 10% tolerance and well below Day's; N=500 differs from numpy 698+-3 by z_cross +3.7 |
| B0.5 neutral k/U at equilibrium | N=50 0.971 (z -12), N=100 0.983 (-4.7), N=200 0.993 (-1.4) | **N=50, 100 miss** (3% and 1.7% deficits) |
| B2a exact-chain F_cond | within 1.5% of the exact chain at G/N = 1-4 for N=50, 100, 200 (z up to +4.4 at N=50, G/N=3); r=0.5 too rare (0/145,590) | met in substance; Day's exp(-pi^2/r) is 1-2 orders below the simulated value at r=1 to 2 |
| B1 empty-start counts | T=200 2.75 (target 2.53, z +1.0); T=400 37.1 (41.1, -5.3); T=1000 249 (304, -29); T=2000 639 (802, -67) | **miss** from T=400, 10-20% low |
| B1 equilibrium counts | 79.0 / 157.6 / 392.8 / 789.1 vs UT = 100 / 200 / 500 / 1000: **21% deficit at every T** | **miss** (numpy 99.3-1005) |
| B1b | constant 0.979 (z -2.0); contraction 1.254 (target 1.267, z -1.1); expansion 0.699 (target 0.733, z -4.8) | contraction met; **expansion misses** by 4.7% |
| B1c | H0 0.962 (z -1.7), H1 3.88 (-2.0), H2 3.77 (-3.3), H3 3.86 (-2.9) vs 3.98 / 3.90 / 3.98 | **excess reproduced (3.8-3.9, not a deficit)**; 2-4% below numpy (H2, H3 just outside 3 SE) |
| B3 (Ne/N = 1, .66, .35, .14) | P_fix*2N = 0.985, 0.974, 0.981, 0.995 (Day's N/Ne would give 1.00, 1.52, 2.91, 7.40); mean t_fix / 4Ne = 0.98-0.995 (inside the 10% tolerance); k/U 0.975-0.995 | **qualitative predictions met** (1/2N not 1/2Ne; time scales with Ne; flat in Ne/N), 2 of 4 P_fix cells outside |z| < 3 (-4.7, -3.5) at 1-3% |
| B3b non-overlapping fluctuating N | k/U 0.961, 0.955, 0.948 (z -5 to -7.6); numpy 1.00-1.01 | **miss** (4-5% deficit; B&L "do not affect" is not contradicted in form: the deficit is the same as in the constant-N control 0.961) |
| B3c(e) cohort | P_fix*M_i = 0.639, 0.629, 0.637, 0.639 (target 1.0; numpy 0.97-1.02; Day's M_i/164 would give 0.305, 0.488, 0.744, 1.0) | **miss by a constant factor 0.64**: independent of cohort size, so it matches neither the target nor Day's cohort-proportional prediction |

## What this does and does not settle
- **Replicated in an independent engine:** Kimura u(s,N) to 2%, the beneficial fixation time (diffusion integral, 2-3x below Day's (2/s)ln2N at his own N, s), the neutral SD of t_fix, the exact-chain B2a values, the sign of the contraction and expansion transient, the B1c excess (3.8-3.9 versus 1.0 at ancestral size), and the B3 qualitative results (P_fix = 1/2N regardless of Ne, time scales with Ne, k/U flat in Ne/N).
- **Not replicated numerically, not localised:** every k/U-type count is low in fwdpy11, and the deficit tracks the per-gamete mutation rate U in the runs: 0.7% (U=0.0125), 1.7% (0.025), 2.9% (0.05), 2-4% (0.04, B1b constant and B1c H0), 21% (0.5, B1 equilibrium), 36% (1.0, cohort). That pattern is a hypothesis about a harness or engine effect at large U (many simultaneous mutations per gamete), **not tested here**. Per the pre-registered rule, a disagreement in one tool is a bug in that tool until localised, and is never resolved by picking the side it favours. The numpy numbers are therefore neither overturned nor independently confirmed at the failing rows (B1 counts, B1b expansion, B3b non-overlap, B3c cohort).
- **What a disagreement does not support:** the fwdpy11 deficit is flat across Ne/N in B3 (0.975-0.995 for Ne/N from 1 to 0.14) where Day's k = mu N/Ne would give 1.0 to 7.4, and the cohort deficit is constant in cohort size where Day's M_i/164 would vary 0.3 to 1. So the misses do not take Day's form. The B1 equilibrium deficit (21%) is the same magnitude as in the Day-direction "deficit" language, but arises at Ne = N, where Day's formula gives none.
- Follow-up (not run): rerun B1 equilibrium and the cohort at lower U with more generations (U-scaling test), or in SLiM 4 (not available on either host).

## Who this helps
- **Critics:** the headline results (1/2N, k tracks mu in form, t_fix scaling with Ne, expansion/contraction excess, beneficial fixation time well under Day's formula) hold in an engine that shares no code with the repo's numpy WF, so they are not a bug of one implementation.
- **Day:** the numeric agreement is not clean. B1, B3b and B3c rows fail at a U-dependent deficit that nobody has localised, so "replicated in both tools" cannot be claimed for them; and his empty-start formula and the sign of the expansion lag stand as confirmed in direction (the transient is real in both tools).

## Review resolution
See `REVIEW-R4-XT-combined.md`. No verdict changes.
