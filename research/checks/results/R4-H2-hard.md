# R4-H2: hard-selection multilocus test of Day's residual cost-of-selection claim

Script: `research/checks/h2_hard_selection_multilocus.py` (seed 20261030, SeedSequence; run `research/.venv/bin/python -I ... all`, ~8.5 min on 3 workers). Raw/summary: `results/h2_raw_{A..D}.json`, `h2_summary_{A..D}.json`, `h2_validate.json`. Pre-registered predictions and the quoted claims (H, Gc, H1, H7) are in the script docstring, written before the grid but after the V1 validation run: docstring lines 31-33 cite the V1 result (the Ricker fix), so the docstring was edited after V1 (review REVIEW-R4-new).

## Model (what is and is not tested)
Haploid-equivalent genic model, M = 2N gene copies, s per copy, random mating, FREE recombination, multiplicative fitness, hard selection (juvenile survives with probability w; N shrinks; extinct if N < 20). Treadmill: the environment opens a new locus at rate lam per generation; the ancestral allele costs exp(-s); the locus closes at fixation. So lam is the substitution rate the environment demands, and the question is whether the population can supply it (Haldane's setting: new locus opens with a single beneficial copy, p0 = 1/N; finite-supply variants also run). Fecundity per adult f = min(R, K/N) (R = reproductive excess). Optional Keightley deleterious load (U = 0.35 / 2.2, s_d = 0.02). 2-3 replicates per cell (M=4000: 2). Not tested: linkage, age structure, sex, pleiotropy, distributions of s, human N.

## Validation
- V1 seed fixation probability, M=1000, s=0.02, 6000 trials/cell, Kimura u = 0.0392: hard R=2/5/20: 0.0397/0.0388/0.0398 (ratios 1.01/0.99/1.02, SE ~6%). Soft R=4: 0.0327 (ratio 0.83, SE 6%, a mild 2.7 sigma shortfall; soft sampling of K from RK juveniles has extra offspring variance). Hard matches Kimura at low supply.
- **Model bug found and fixed**: first version used the Nunney-style f = R^(1-N/K); at R=20 (ln R=3 > 2) this is a Ricker map and oscillates, giving p_fix 0.0085 (ratio 0.22). Replaced by the ceiling form above (stable). All results below use the fixed form.
- Soft vs hard at large R: at lam=0.03, k = 0.0269 (soft, R=4) vs 0.0324/0.0308/0.0295 (hard R=20/5/10); lam=0.1: 0.102 vs 0.097-0.103; lam=0.2: 0.183 vs 0.191-0.198. Converge within ~15% (soft slightly slower, consistent with its lower u).
- Cost per substitution D (= sum -ln wbar / n_subs) in the Haldane setting: 7.0 (M=1000), 5.9 (M=500), 8.5 (M=4000) at lam=0.03 vs ln M = 6.9/6.2/8.3: matches Haldane's haploid D = ln(1/p0) (wf_hc), not 30.

## Results (s = 0.01, M = 1000, infinite supply, 3 reps; k_obs/lam = R_int; N/K and dead = selective-death fraction 1-wbar of juveniles)
| lam (per gen) | R=2 | R=5 | R=10 | R=20 |
|---|---|---|---|---|
| 0.0033 (=1/300) | N/K .97, dead .03, R_int 1.17 | .97, .03, 1.17 | .97, .03, 1.09 | .98, .02, 1.01 |
| 0.01 | .94, .06, 0.77 | .93, .07, 1.00 | .92, .08, 1.09 | .91, .09, 1.21 |
| 0.03 (~35 open loci) | .79, .21, 1.07 | .80, .20, 1.03 | .81, .19, 0.98 | .79, .21, 1.08 |
| 0.1 (~95 open) | .53, .46, 0.96 | .50, .50, 0.98 | .51, .49, 0.97 | .50, .50, 1.03 |
| 0.2 (~167 open) | EXTINCT 3/3 | .30, .70, 0.99 | .30, .70, 0.98 | .30, .70, 0.96 |
| 0.4 (~260 open) | EXTINCT | EXTINCT 3/3 | .15, .85, 0.99 | .14, .86, 1.03 |

Findings:
1. **Rate**: wherever the population persists, k_obs = lam within noise (R_int 0.9-1.1). Free-recombination parallel sweeps do not interfere, up to ~260 simultaneous open loci (lam=0.4, R=10: 256 open, k=0.397). Nothing saturates near 1/300 or near 230 concurrent sweeps. Observed rates reached 0.4/gen = 120x Haldane's 1/300.
2. **Realised death**: dead fraction at lam=1/300 is 2-3% (D~7, not 30), and a population persists with 46-86% selective deaths. 10% is not a general bound under hard selection; 1-wbar = 0.10 is reached at lam ~ 0.012.
3. **Where it flips**: persistence fails when the total log-load lam*D exceeds ln R, i.e. N/K = e^-L falls below 1/R (pre-registered P-Std). Observed boundary (last persisting / first extinct lam): R=2: 0.1 / 0.2 (pred ln2/7 = 0.10); R=5: 0.2 / 0.4 (pred 0.23); R=10: 0.4 / >0.4 (pred 0.33; D falls to ~4.8 at lam=0.4, so the linear prediction is slightly conservative); R=1.6: 0.06 persists (pred 0.067); R=1.3: 0.03 persists, 0.06 extinct (pred 0.037). In every case the flip is at 9x to 100x the Day cap of 1/300; no tested R>=1.3 flips at or below 1/300. P-Day (literal 1/300 cap; also the Day-in-model variant 0.10/D = 0.014) is **not supported** in the tested range (R >= 1.3, haploid D ~ 7, imposed lam, free recombination: the critic-favourable choices). This is not a falsification of Haldane's literal 1/300: his own regime (R ~ 1.1, i.e. ln R ~ 0.095 = the 10% budget, with diploid D ~ 20-30) gives 0.095/30 ~ 1/300 and was not tested. The supported statement is: 10% is not a general bound; the bound is ln R / D. The flip brackets have factor-2 spacing and 2-3 replicates, so "9x to 100x" is a bracket, not a measurement. Note that lam*D < ln R is partly an identity (D is defined as sum(-ln wbar)/n_subs, so lam*D = mean(-ln wbar)); the independent content is D ~ ln M + 1 (7.0 vs 6.9, 5.9 vs 6.2, 8.5 vs 8.3). The R=10 flip was predicted at 0.33 and observed above 0.4, and the n_crit ~ 70 estimate at R=2 conflicts with 90 open loci persisting. The open-locus count at the flip is n_crit ~ ln R / (s * mean q) : ~70 loci at R=2, ~165 at R=5, ~255 at R=10-20 (s = 0.01), i.e. Day's ~230 concurrent sweeps persist for R=5 and above, not for R=2 only marginally (R=2: 90 open persisted, 167 did not). Pre-registered "230 persists for R=5, not R=2" is supported.
4. **s and N**: s=0.03, R=2: lam=0.06 persists, 0.2 extinct (same flip, ln R / D); s=0.003 shows R_int 0.4-0.7 but those runs were not at steady state (time-to-fix ~1900 gens vs burn 1500; open-locus count still rising), so treat as unreliable. M=500/1000/4000, R=2: lam=0.1 persists at M<=1000, 50% extinct at M=4000 (D grows with ln M, so lam_max shrinks only logarithmically).
5. **Finite supply** (sv = 2N mu_b per open locus per gen = 0.5 or 0.05): waiting loci add a uniform cost s per locus. sv=0.5: R_int 0.8-1.07, dead 1-11% at lam<=0.03. sv=0.05: R_int 0.71-0.81 (partly transient, ttf ~1450 vs burn 2000), D 11-21, N/K down to 0.61 at lam=0.03; all persisted. Low supply raises the load but did not make the rate collapse in the tested range; lam_max drops (not scanned to the flip).
6. **Keightley load (hard)**: dead fraction 1-e^-U as expected (U=0.35: ~31% at lam=1/300; N/K=0.69; U=2.2: N/K=0.10-0.11). U=0.35: persists for all R>=5 and lam to 0.1 (N/K 0.37-0.39). U=2.2: extinct for R=5 (and R=10, e^-2.2 = 0.11 only just above 1/R = 0.10) at every lam; persists at R=20/50 with N/K ~0.1, where lam=0.1 gave 33% extinction at R=20. Combined condition: lam*D + U < ln R.

## Verdict on Day's residual claim (within this model)
10% is not a general bound: under hard selection the cap on the substitution rate is ln R / D. At reproductive excess R >= 1.3, haploid D ~ 7 and free recombination, the observed flip lies 9-100x (bracketed) above 1/300 and parallelism is free up to the load limit. Day's 1/300 is recovered when (ln R - U) / D ~ 0.003: Haldane's own regime (R ~ 1.1, diploid D ~ 20-30) or ln R barely exceeding the deleterious load. That regime was not tested, so the literal 1/300 is untested, not falsified. The model's ceiling regulation (fecundity rises whenever N < K) is itself the compensatory-reproduction premise of the critics' reply; it does not bias the arithmetic, but it assumes excess fecundity is available at no cost (review REVIEW-R4-new, MAJOR).

## Extrapolation to human parameters (NOT simulated; formula from the validated scaling lam_max = (ln R - U)/D, D ~ ln(2N) + 1, doubled for diploid additive per wf_hc)
Ne=1e4 gives D ~ 11 haploid, ~20 diploid (wf_hc: diploid D ~ 2 ln(1/p0)). R per adult unknown; Keightley's example is 20 offspring per female (R ~ 10 per adult).
- U=0.35, R=10: (2.3-0.35)/20 ~ 0.10 per gen (~30x Haldane).
- U=2.2, R=10: (2.3-2.2)/20 ~ 0.005 (close to 1/300, almost no margin); U=2.2, R=20: (3.0-2.2)/20 ~ 0.04.
So Day's cap reappears only when (a) the whole-genome U=2.2 is treated as hard-selected deleterious mutation load and (b) R is near e^U. H7 (Keightley) itself says much human selection must be soft or the load is implausible, so (a) and (b) are mutually in tension with using hard selection for the beneficial side. This is a calculation under the model, not a human-validated result.

## Caveats
Treadmill demand lam is imposed, not emergent from a mutation supply (infinite-supply runs); free recombination removes Hill-Robertson interference (the critic-favourable assumption: with tight linkage the cap would fall); single s; haploid-equivalent; 2-3 reps (extinction at the boundary is stochastic); stage B s=0.003 and sv=0.05 R_int not at steady state; V1 soft ratio 0.83.

## Review corrections applied (REVIEW-R4-new)
1. MAJOR (framing): "P-Day falsified" downgraded to "not supported" for R >= 1.3, D ~ 7; Haldane's regime (R ~ 1.1, diploid D ~ 20-30, 0.095/30 ~ 1/300) stated as untested; ceiling regulation identified as the critics' compensatory-reproduction premise.
2. MINOR: lam*D < ln R noted as partly an identity; the independent test is D ~ ln M + 1.
3. MINOR: pre-registration timing corrected (docstring edited after V1, before the grid).
4. MINOR: flip brackets are factor-2, 2-3 replicates; R=10 prediction miss and n_crit conflict noted.
5. Not done: an R ~ 1.1, diploid run; linkage; max_open=700 counted as extinction (not reached).
