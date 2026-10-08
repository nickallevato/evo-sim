# R4 results: H (cost of selection) and C2 (turnover coefficient d)

Scripts (all under `research/checks/`, run with `research/.venv/bin/python -I <file>`): `wf_hc.py` (helpers), `h_cost_of_selection.py` (seed 20261008), `h_nunney_gauss.py` (20261010), `h_nunney_gauss_lowR.py` (20261020+), `h_keightley_load.py` (20261009), `c2_overlap_vs_standard.py` (20261011), `c2_ratio_nonident.py` (deterministic). Pre-registered predictions are in each docstring (claim-file text copied; extras marked with the date written). Status: reviewed; review corrections applied (see section at end).

## H: cost of selection

### (a) Haldane's 300, reproduced
- 30 / 0.10 = 300 generations. D = 30 is Haldane's input, not derived here. With sum (w_max - wbar)/wbar, haploid D = ln(1/p0) exactly. Diploid additive D is about 2 ln(1/p0) and is independent of s (s = 0.01 and 0.001 agree to <1%).
- D = 30 needs p0 = 9e-14 (haploid) or 3e-7 (diploid additive).
- For standing variation p0 = 1e-2 to 1e-6, diploid D = 9.2 to 27.8, i.e. 92 to 278 generations at 10% mortality. So 300 is the upper end, not typical, of Haldane's own accounting. (Prediction said 70-140 for p0 1e-3..1e-6 haploid-ish; the diploid values are about twice haploid, so the prediction was low for the diploid case.)
- 146,250/300 = 487.5 (the paper truncates to 487; holds).

### (b) Individual-based hard vs soft selection (K = 500, T50 = interval at 50% persistence, 8 reps per T)
**Rerun after the mutation-timing fix (see "Review corrections applied"); all numbers below are post-fix.** Life cycle in both regimes and both models: reproduction (hard: f = min(R, 2e^{r(1-N/K)}) per female; soft: R per female) -> mutation of the J juvenile gametes at per-gamete rate u*K/J, so the juvenile cohort receives M = 2Ku new mutations per locus per generation regardless of J -> selection/regulation (hard: independent survival w; soft: K adults drawn with probability proportional to w). The pre-fix code used a flat u per juvenile gamete, which inflated effective M by J/K (about R/2 under soft selection).

Model 1 (`treadmill_run`, constant s per step, optimum jumps every T generations at n loci). Success = no extinction and mean pre-shift lag < 0.5 steps (N/K not part of the criterion; see Caveats).

| Condition (n=1, M=2) | hard T50 | soft T50 |
|---|---|---|
| s=.03, R=2.2 / 3 / 5 / 10 / 40 | 51 / 73 / 76 / 78 / 43 | 177 / 128 / 151 / 142 / 305 |
| s=.10, R=2.2 / 3 / 5 / 10 / 40 | fails (T<=1024) / 28 / 35 / 37 / 24 | 96 / 64 / 55 / 60 / 106 |
| R=3, s=.01 / .03 / .10 / .30 | 157 / 84 / 28 / 15 | 242 / 139 / 60 / 28 |

- Does "soft is worse at low R" survive? Yes, and it is now stronger: soft T50 exceeds hard T50 at every R tested (about 2x at R=3, 3.5x at R=2.2 for s=.03) and also at high R (R=40). Before the fix, soft and hard were equal at R >= 5; that equality was produced by the extra soft-regime mutation supply. The fix also removes the claim that soft selection becomes "faster with s" relative to hard: the ratio soft/hard is about 1.5 to 2 at all s in the R=3 row.
- s-dependence: T50 falls with s in both regimes. Hard selection no longer fails at s=.3 (R=3) after the fix (T50 = 15); the earlier failure was probably also a mutation-supply artefact in part, and this was not investigated further. Prediction P-b3 (hard T50 independent of s) is not supported.
- M-scan (R=10, s=.1, n=1), hard T50, M=10 / 2 / 1 / .5 / .25 / .1 = 19.6 / 36.6 / 39.2 / 50.8 / 73.3 / 111; soft = 36.6 / 55.4 / 78.4 / 106 / 128 / 314. The earlier statement "soft is within about 15% of hard" is **withdrawn**: at equal mutation supply soft is 1.5x to 2.8x slower than hard, and the gap widens as M falls.
- n-scan (R=10, s=.2/n, M=2, synchronous), hard T50 for n=1/2/3/5 = 20 / 38 / 40 / 78; soft = 35 / 58 / 84 / 116. Staggered loci: hard n=3/5 = 48 / 76, soft = 81 / 139. At M=10, hard n=1..5 = 12 / 20 / 25 / 37, soft = 20 / 39 / 53 / 76.
- Hard and soft differ in this construction at every R. This is not the expectation that soft selection removes the cost. Possible reasons: soft selection as implemented draws K adults from R*N/2 juveniles and so has no density-dependent mortality, but the strict proportional draw loses rare beneficial mutants to drift in the one-generation bottleneck more than independent survival does. This was not tested.

Model 2 (`gauss_run`, Nunney-style Gaussian optimum moving continuously; his Eq. 3 and 5 are lost in the text extraction, so w = exp(-r * mean (Av - t/T)^2) and f = 2e^{r(1-N/K)} are reconstructions). Success = no extinction and adult mean squared deviation < 0.5 (10 reps per T). **EXPLORATORY.** This model was adjusted twice after seeing results (h_nunney_gauss.py was written after the constant-s Model 1 gave only a gradual M-dependence; h_nunney_gauss_lowR.py was written after Model 2 at R=10 fell far below Nunney's values). R=10:

| M | 10 | 1 | 0.5 | 0.25 | 0.1 |
|---|---|---|---|---|---|
| hard n=1 | 6.0 | 8.0 | 10.0 | 16.6 | 25 |
| hard n=7 | 17.9 | 44.7 | 59.6 | 83.7 | 161 |
| soft n=1 | 6.5 | 13.7 | 17.5 | 27.1 | 54 |
| soft n=7 | 34.8 | 77.1 | 119 | 185 | 357 |

At the Haldane-like budget R=2.2 (ln(R/2)=0.095, about 10%), n=1: hard T50 = 25 / 47 / 114 / **170** for M = 10 / 1 / 0.25 / 0.1; soft T50 = 89 / 211 / 400 / 1000 (grid maximum). Before the mutation fix the hard M=0.1 value was 285; it is now 170, 1.8x below Nunney's ~300.

Nunney (quotes): "For M > 1/2, the cost of natural selection is substantially less than Haldane's estimate; however, when M < 1/2, the cost (and particularly the fixed cost) increases in an accelerating fashion as M is lowered." "a simulated population with M = 10 can tolerate environmental change that requires allelic substitution at 7 loci ... every 40 generations. With M = 1, ... a single trait ... could still undergo allelic turnover every 20 generations." "In large part the difference reflects the fact that in populations with density-dependent regulation, mortality (including unfulfilled fecundity) can shift from being primarily random to being primarily selective".

Reading (EXPLORATORY; reconstructed model tuned twice):
- The qualitative M-dependence is reproduced: T50 rises as M falls, more steeply for n=7 and in the soft regime.
- Absolute values at R=10 are 2 to 12 times lower than Nunney's (his M=1, n=1 is about 20; mine 8; M=0.1: 25 vs about 300, a 12x miss). The approach to Nunney's 300 occurs only after switching to R=2.2, a parameter chosen after the R=10 failure, and post-fix reaches 170, not 300. This is an exploration, not a confirmation of Nunney's number or of Haldane's 300.
- Prediction P-b2 (hard T50 falls with R roughly as 1/ln(R/2), then saturates) is supported in Model 2: n=1, M=1, hard T50 = 64 / 19 / 10 / 6 for R = 2.2 / 3 / 5 / 40. Not supported in Model 1, where the cost was masked by sweep time at R >= 3.
- Soft selection did not remove or reduce the cost in either model at equal mutation supply (soft T50 > hard T50 throughout). The critics' reading of Nunney ("soft selection removes the cost") did not reproduce.
- Human M is unknown. A rough derivation: M = 2 * K_eff * mu * (target bp) = 2.4e-4 per bp for K=1e4, mu=1.2e-8. M >= 0.5 needs about 2,000 bp of target per "locus" at K=1e4. M is undetermined by the repo's sources, so I give no verdict on which side of M=1/2 humans fall.

### (c) Day's cost figures
- Term 3: 0.45 / (2 * ln 6600) = 8.25e-12 per site, 0.0256 per genome per generation, one per 39.1 generations (holds). Implied per-substitution cost 2 ln(2Ne) = 17.6 against budget s_max = 1.0 (Haldane: D = 30, m = 0.10).
- **Correction to R2/H8:** "Term 3 allows 7.7 times more than Haldane + d" compares Term 3 with d (1/39) against Haldane without d (1/300). At the same d the ratio is 17.1 (1/39 against 1/667). Without d on both sides it is also 17.1 (10x from budget, 1.7x from D).
- Counts over 260,000 generations: Haldane 867, Haldane + d 390, Term 3 6,652. Over 450,000: Haldane 1,500, Haldane + d 675.
- 2026-05-07 retraction: Term 3's output bounds *selected* substitutions only. The same scope argument applies to H, which sets the Haldane count of selected fixations (487) against all 20M differences. Neutral substitution rate = mu (B0.5: k = U, z = +0.13 and -0.64). H1 does not say whether H falls under the retraction.
- Hössjer: his "perhaps more in line with equation (3)" 15,800 is 10.5x Haldane's own 1,500 over 450,000 generations (1,500 / 675 with d). The 15,800 comes from a mutation-rate scaling, not a cost computation, so the cost step is unsupported by the Haldane arithmetic.

### (d) Keightley U = 2.2 (K = 1000, 500 generations, 6 reps)
- Hard, multiplicative s = 0.05: extinct in 6/6 runs for Fmax = 4 to 20. Persists at Fmax = 30 with N/K = 0.174 +- 0.009 (predicted 0.188) and Fmax = 60 with 0.344 +- 0.004 (predicted 0.353). The threshold is 2e^U = 18.1 offspring per female. At Fmax = 20 the predicted N/K is 0.045, i.e. about 45 individuals, and all 6 runs went extinct stochastically.
- Soft: persists at every Fmax tested (4 to 60) with N/K = 1. Mean absolute fitness is 0.036 at Fmax = 4 and 0.11 to 0.12 at Fmax >= 20, with mutation load k from 68 down to 44.
- Synergistic epistasis (w = exp(-0.01k - 0.0004k^2)): hard selection persists from Fmax = 12 (N/K = 0.20); fails at 8.
- Keightley's "20 offspring" statement is consistent: hard accounting is implausible at natural-fertility levels.

## C2 / C2a / A4: the turnover coefficient d

### Derivation (verified numerically)
For a stationary population, the integral of l(x) v(x) dx equals T. So Day's d = int(mu l v) dx, which equals the mean cumulative hazard at the age of mothers, H_bar (numerically 0.789 against 0.784 on a yearly grid; the two agree within about 1%). First-order Euler-Lotka gives T*dr = Delta ln R0 = s_gen.

Therefore d s is exactly the generation-scale selection when s is the fractional change in the mortality hazard at all ages. For any s defined as a per-generation relative difference (fecundity, survival to maturity), the factor is 1. Day's d is a unit conversion between "hazard-scale" and "per-generation" s, not a correction to the speed of selection.

Day-side point (steelman): d*s is exact for hazard-scale s, and Day's definition of s (fractional change in mortality, the force-of-mortality scale) is exactly that case (V1: T*dr/s = 0.778 against d = 0.789, within 1.5%, first-order in s). So the formula is correct for the quantity Day defines. What is open is only which s the cited aDNA papers estimate (not retrieved).

### Simulation results (e0 = 32 Siler table, T = 29.7, s = 0.02)
| Scenario | T*dr (exact) | s_gen | T*dr / s_gen | Day's d*s |
|---|---|---|---|---|
| V1 hazard x(1-s) | 0.01557 | 0.01557 | 1.000 | 0.01578 |
| V3 fecundity x(1+s) | 0.01982 | 0.01980 | 1.001 | 0.01578 |
| V4 pre-maturity survival | 0.02022 | 0.02020 | 1.001 | 0.01578 |
| V5 adult survival 15-45 | 0.00924 | 0.00925 | 0.999 | 0.01578 |
| V2 additive hazard | 0.00574 | 0.00574 | 1.000 | not defined |

- Deterministic two-type projection (logit slope per year x T) reproduces T*dr to 5 digits. The stochastic age-class IBM (200,000 individuals per type, 400,000 total, 24 reps) gives V1 0.01548 +- 0.00027, V3 0.01982 +- 0.00030, V4 0.02018 +- 0.00028 (exact 0.01557 / 0.01982 / 0.02022).
- Prediction [add-1] confirmed: only V1 returns "d s"; V3 and V4 return s; Day's d*s is 20 to 22% below the exact value for V3/V4 here.
- Discrete-generation control: Day's formula gives d = -ln L for a semelparous annual organism (L = survival to breeding): 0.105 / 0.693 / 0.994 / 2.303 for L = 0.9 / 0.5 / 0.37 / 0.1, matching the hazard-scale T*dr/s. Day's statement that "d = 1 corresponds to discrete generations" and "d ranges from 0 to 1" holds only at L = 1/e.
- Table 1 d values: the Siler family gives d(e0=32) = 0.79 and 0.93 (two shape families) against Day's 0.53, and 0.13 to 0.21 at e0 = 78 against 0.015. I did not reproduce the Table 1 values. The cause is the unretrieved Coale-Demeny West tables (my Siler family is a stand-in), not an error shown in Day's calculation; this is an unresolved fidelity gap of 1.5x to 14x, not a refutation. Only the monotone decline is confirmed.
- Equivalence: g_eff = d g_nominal is the same as standard theory with generation length T/d (55.6 y for d = 0.45, T = 25), against 29.7 y mean age of mothers on the e0 = 32 table. Calendar-year logit gain is s_gen t/T (standard) against d s t/T (Day).
- Published aDNA s values are estimated as per-generation logistic slopes, so d = 1 for them under this derivation. That is the key external-validity question; I did not retrieve how each cited paper defines s.

### C2c ratio identity (exact recursion, Table 1 inputs)
- TYR / SLC45A2 required-s ratio: 0.4646 (d = 0.2), 0.4727 (0.45), 0.4763 (1.0), 0.4778 (2.0). Constant within 3% over d in [0.2, 2]; it departs only at s ~ 0.25 to 0.6 (d = 0.05: 0.421).
- Synthetic random locus pairs show the same invariance (≤ 6% across d = 0.2 to 2). The odds multiply by (1+s) each generation, so ln(1+s) d G is fixed.
- The exact ratios at d = 0.5 to 1.0 are 0.4734 to 0.4763; the paper's 0.49 is about 0.01 (2%) above the exact recursion, likely a logit approximation.
- C2c is not a test of d.

### C2d / identifiability
- Three trajectories, four unknowns: exact fit for every d (residual < 1e-11). Required s: d = 0.2: 0.126 / 0.125 / 0.058; d = 1: 0.024 / 0.024 / 0.011.
- Day's own published s ranges (LCT .04-.10, SLC45A2 .04-.05, TYR .02-.04) give d in [0.481, 0.568]. d = 1 would need s below all three ranges. Scaling all ranges by 0.75 or 1.25 moves the interval to [0.638, 0.756] or [0.387, 0.456]. The interval comes from priors on s, not from the trajectories.
- Observationally equivalent explanations of the same d = 0.49 / 0.48 / 0.38: selection starting about 2,100 to 3,100 y later than the stated date, a generation length of 51 to 66 y, s lower than published by that factor, or a dominance model. Dominant advantage at the paper's s=0.05 for LCT needs d = 0.745 instead of 0.486; recessive for SLC45A2 needs 0.646.
- Chicken (p 0.44 to 0.97, G = 900): required d additive 1.43 / 0.845 / 0.471 at s = 0.0029 / 0.0049 / 0.0088; recessive 1.90 / 1.13 / 0.63; dominant 13.5 / 8.0 / 4.5. The paper's 1.02 depends on dominance and s; the CI spans d = 0.45 to 0.63 for the recessive model at its upper bound. Loog's posterior is not in the repo.

## Suggested three-verdict updates
(I = internal validity, F = fidelity, E = external validity.)

- **H**: I: **fails as a comparison to the 20M total**, holds for arithmetic (300, 487, 41,068). Haldane's 300 holds for D = 30 and 10% only (a bounding case, not a typical value); D is p0-dependent (92 to 278 for p0 1e-2 to 1e-6, diploid). The compare-to-total step is a category error of the kind H1 concedes. F: partial (300 accurate via Nunney only; primary not retrieved; "d" is Day's addition). E: contested; in my exploratory reconstruction the hard-selection limit ranges from about 6 to 170 generations depending on M and R, and no run exceeded Haldane's 300. Haldane's 300 is a bounding case (consistent with M <= 0.1 and a 10% budget, not a finding of this reconstruction).
- **H1**: I: holds (arithmetic 39 gens; same-basis ratio 17.1; the 2.2x (= 1/d) between "7.7" and "17.1" is a comparison-basis issue). F: not testable (no revised Zenodo). E: scope concession applies to H as well; no basis for a verdict on whether Day intended it.
- **H2** (Nunney): F: accurate quotes. I: qualitative M-dependence reproduced; absolute T not reproduced (reconstructed model). E: contested; the M-regime for humans is not determined from the repo.
- **H5** (Hössjer): I: fails for the cost step (15,800 is 10.5x Haldane's own 1,500, derived from rate scaling, not cost). F: pending. E: depends on H.
- **H8** (Term 3): I: holds arithmetic. Not reconciled with H: at the same d the ratio is 17.1, and the effective D (17.6) and budget (1.0) differ from Haldane's (30, 0.10). E: s_max = 1 corresponds to a very large reproductive excess (R in the hard model) and is not Haldane's 10%.
- **H7** (Keightley): simulation supports I, F (hard selection at U = 2.2 needs about 18 offspring per female); E: does not decide whether adaptation is hard or soft.
- **C2**: I: **fails as stated** ("d is a demographic correction to the rate of selection"); d is a conversion between hazard-scale and per-generation s (exact numerically). F: the claim that d = 1 for discrete generations is not met by his own formula. E: d cannot be estimated separately from s, onset time, T and dominance; contested.
- **C2a**: I: derivation is correct for hazard-scale s (d = H_bar); the claim that it is a distinct correction for selection fails. F: Charlesworth/Hill are not retrieved, but the Euler-Lotka result is standard theory (hypothesis (H-i), (H-ii)). Table 1 values not reproduced.
- **C2c**: I: arithmetic holds, inference fails (algebraic identity). **C2d**: I: partially holds (1.02 at the point estimate with the paper's recursion, as recomputed in R2); E: not identifiable.
- **A4** (turnover d): I: the empirical d = 0.45 is s * d, not d; the application to the Haldane count (g_eff) multiplies a death budget by a conversion factor between two scales of s, without justification.

## Caveats
- The IBM is a reconstruction. Nunney's Eq. 3 and 5 are not recoverable. K = 500 only (Nunney reports K-independence at fixed M). Persistence rules differ (8 to 10 reps, 50% crossing, a lag/deviation criterion added so that soft selection can fail).
- Success criteria do not include N/K, which favours hard selection at R <= 3 (hard populations may persist well below K). T50 has no confidence interval (8 to 10 reps; differences under 1.5x are below resolution).
- Soft selection is implemented as global competition for K slots with probability proportional to w. Other forms of soft selection (Wallace's local soft selection) are not simulated.
- Life tables are a Siler family, not Coale-Demeny. Clonal/haploid age-structured model; diploid Mendelian transmission was not simulated.
- Hill (1972) / Felsenstein (1971) Ne formulas were not tested; Day's Ne/(N1T) = 2/(2+Vk) gives 0.5 for Poisson reproduction where the discrete Wright-Fisher limit should give 1 (stated as a hypothesis from memory, to check against Hill 1972 when retrieved).
- Keightley's K = 1000 hard persistence near the threshold (Fmax = 20) is dominated by stochastic extinction.
- Nothing here was run by a second reviewer.

## Overall framing of H (both steelmen)
- Haldane's 300 is a bounding case: it holds for D = 30 and a 10% budget, and in the exploratory model only at the lowest M (<= 0.1) and R near 2.2 does the hard limit approach the low hundreds. D ranges 92 to 278 generations for standing-variation p0.
- The critics' claim that soft selection removes the cost did not reproduce here: at equal mutation supply soft T50 exceeded hard T50 in both models.
- Human M is undetermined by the repo, so H is neither refuted nor shown to be binding. The scope question (selected vs all substitutions, H1) is separate and stands.

## Review corrections applied
1. H-IBM mutation timing: mutation was applied to J juveniles at a flat rate u, inflating effective M by about J/K (about R/2 under soft selection). Fixed in `wf_hc.py` (`treadmill_run`, `gauss_run`): life cycle is reproduction -> mutation at rate u*K/J (M = 2Ku per locus per generation in both regimes) -> selection. Reran `h_cost_of_selection.py`, `h_nunney_gauss.py`, `h_nunney_gauss_lowR.py` (Pool reduced to 3). Result: "soft is worse at low R" survives and strengthens (soft worse at all R and M); "soft within 15% of hard" withdrawn; hard M=0.1, R=2.2 moved from 285 to 170; Model 1 hard at s=.3 now succeeds. `mutload_run` (Keightley) uses a per-offspring Poisson(U) and was not affected.
2. Model 2 match to Nunney's 300 marked EXPLORATORY (two post-hoc adjustments; R=10 misses about 12x; post-fix R=2.2 gives 170).
3. Ratio: 7.7 was Term 3 with d over Haldane without d; same-basis ratio is 17.1 (verified: 0.0256 / 0.00150; 17.1 / 7.7 = 2.22 = 1/d, so "2.7x" corrected to 2.2x). Claims H8 and H1 fixed (H1 also 0.0256/gen, about 6,650 over 260,000 generations).
4. C2: added the Day-side point that d*s is exact for hazard-scale s, which Day's definition satisfies; Table 1 non-reproduction attributed to unretrieved Coale-Demeny tables.
5. H framed as a bounding case (see above). Other minor wording fixes from the correctness review (200,000 per type, 20 to 22% below, 0.49 vs exact recursion) applied.
6. Not done: binomial CIs on T50 and N/K in the success criterion (stated as caveat).
