# R4 results: F2 (multi-locus interference) and A-sim (LTEE scaling)
Scripts: `research/checks/wf_f2.py` (helpers), `f2_multilocus.py` (seed 4242; seeds now derived deterministically via zlib.crc32, rerun 74 min on 3 cores), `f2_fwdpy11.py` (seed 777), `a_ltee_scaling.py` (seed 20261008, crc32 seeds, rerun 11 min on 3 cores). Pre-registered predictions are in each script docstring (copied from the claim files before the runs, plus my own additions, labelled). Reviewed once; review corrections applied (see last section). Tables below are from the post-fix rerun. THROWAWAY.

## Model and scaling
- Haploid-equivalent WF, M = 2N gene copies, genic selection exp(sum s), soft selection, infinite sites. Equivalent single-locus dynamics to the diploid h=0.5 case (u = (1-e^{-2s})/(1-e^{-2Ms}) = `wf.kimura_u(N,s)`). Cross-checked against fwdpy11 diploid below.
- Recombination: `clonal`; `free` (r = 1/2 between all loci); or a genome map of R Morgans (Poisson(R) uniform crossovers). R = 0.1 ("low") and 1.5 (a single human-length chromosome-like map; pessimistic for humans, whose between-chromosome recombination is free).
- F2 runs at N = 1000 (M = 2000), s = 0.01 (2Ns = 20) and s = 0.001 (2Ns = 2, near-neutral; weak test). The unscaled N = 10^4 grid in the claim file was not run (cost). Supply is expressed as 2N*U_b.
- **Interference factor** R_int = (fixations per generation)/(2N*U_b*u(s)). "n_mid" = time-averaged number of loci with 0.1 < p < 0.9 (the Bernoulli-Barrier "active zone"); n_seg = all segregating loci.

## F2 results (SE across 4 replicates; ~10^3 events per cell at higher supply)
s = 0.01, N = 1000:

| 2N*U_b | clonal R_int (n_mid) | map 0.1 M | map 1.5 M | free |
|---|---|---|---|---|
| 0.1 | 0.645 ± 0.002 (1.0) | 0.94 ± 0.01 | 1.04 ± 0.04 | 1.05 ± 0.03 |
| 0.5 | 0.37 ± 0.01 (3.3) | 0.87 ± 0.02 | 0.97 ± 0.01 | 1.01 ± 0.04 |
| 2 | 0.215 ± 0.006 (6.8) | 0.62 ± 0.01 | 0.98 ± 0.03 | 1.00 ± 0.01 |
| 8 | 0.132 ± 0.003 (15) | 0.372 ± 0.003 | 0.83 ± 0.01 | 0.98 ± 0.01 |
| 32 | 0.088 ± 0.002 (32) | 0.204 ± 0.001 (75) | 0.572 ± 0.004 (208) | 0.975 ± 0.005 (272) |

Absolute clonal rate: 0.0013 → 0.056 per generation as 2N*U_b goes 0.1 → 32 (a 320-fold supply increase gives 44x; exponent ≈ 0.66 overall). Asexual saturation is gradual (logarithmic), not a hard ceiling. Free recombination: rate is linear in supply (exponent 1.00) up to 0.618/gen at 2N*U_b = 32 with 272 loci in the active zone.
s = 0.001, N = 1000 (2Ns = 2, weak): 2N*U_b = 0.5: clonal 0.68 ± 0.02, free 0.99 ± 0.05; 2N*U_b = 4: clonal 0.55 ± 0.03, free 0.99 ± 0.04 (n_mid 27).
Desai-Fisher formula (recalled from memory, unverified) is far off at these small L = ln(s/U) (overestimates by up to 5x at 2N*U_b = 32); not used for any conclusion.

**fwdpy11 cross-check** (diploid, N = 1000, s = 0.01 per copy, h = 0.5, 8 replicates; 12,000 generations after 3,000 burn): R_int = 1.089 ± 0.089 (2N*U_b = 0.1, map 20 M), 0.951 ± 0.018 (2N*U_b = 2, map 1.5 M; wf_f2 0.946 ± 0.012), 0.997 ± 0.016 (2N*U_b = 2, map 20 M; wf_f2 free 0.963 ± 0.016, z = 1.5). Agreement. A first fwdpy11 run was mis-specified (fwdpy11 het = 1 + h*S, hom = 1 + scaling*S, so I had half the intended s) and gave R_int = 0.50 exactly; it was diagnosed and fixed (S = 2s, scaling 1), and the numbers above are from the corrected run. Counting fixations in fwdpy11 uses two same-seed runs (length burn+T and burn) and differences the count of mutations at frequency 1.

### F2 interpretation
- (a) confirmed: free recombination at low supply R_int ≈ 1 (1.05 ± 0.03).
- (b) confirmed: clonal R_int < 1 and falls with supply (0.65 → 0.09). n_sw (n_mid) is bounded far below the independent expectation.
- Day's best form (interference) is real but is a property of linkage. Free recombination keeps R_int ≈ 1 (0.975 ± 0.005) at 272 active-zone loci, i.e. above the claimed Bernoulli cap of ~230 with no collapse in the tested regime, and the rate keeps scaling linearly. This is the falsifier stated in the claim (R ≥ 0.5 at 230 loci with r = 1/2 and soft selection).
- Linkage matters quantitatively: with only 0.1 M of map R_int is 0.20 at 2N*U_b = 32 (a clonal-like regime), and with a single 1.5 M linkage group it is 0.57 at 208 active loci, i.e. close to the 0.5 line. A real human genome is 22 autosomes plus X, so free between chromosomes; a single 1.5 M group is a pessimistic bound.
- Not tested: hard selection / cost of selection (branch H, which binds first at high U_b in a real organism: here soft selection means no demographic cost); N = 10^4; DFE; epistasis; diploid dominance beyond h = 0.5; sub-neutral s at larger N; x-axis reaches only 2N*U_b = 32 and n_mid ≈ 270 (the human regime is 2N*U_b ≫ 100).
- Day's G_f: the clonal sim reproduces the order of magnitude of sublinearity but is not a measurement of the human ceiling.

## A-sim / LTEE scaling results
Method note: for clonal fixed-s, the exact multinomial fitness-class process (same stochastic model) reaches Ne = 3.3e7; rate = d<k>/dt, k = mutation count (every fixation adds one to everybody).
**Validation:** class process vs individual-based (wf_f2, M = 2000, s = 0.01): rates 0.00365 vs 0.00353, 0.00840 vs 0.00827, 0.02076 vs 0.02075 (|z| < 0.7). **Standard scaling (M/c, c*s, c*U) validated (E4)** over c = 1..8 (M = 128,000 → 16,000, s = 0.00125 → 0.01, 2Ns = 320): k/c 0.00053-0.00055 (M*U = 2) and 0.00180-0.00182 (M*U = 20), within ~4%.
**LTEE calibration** (Ne = 3.3e7: UNSOURCED ASSUMPTION, roughly N0·log2(100) = 5e6 × 6.64, not in parameters.yaml; a source would need to give the LTEE effective population size (harmonic-mean size over the daily dilution cycle) from a retrieved PDF, e.g. Lenski et al. 1991 or Wiser et al. 2013; sensitivity below; fixed s per mutation): the beneficial supply U_b giving G_f = 1,322 asexually is 6.7e-7 (s = 0.003), 8.4e-9 (s = 0.01), 6.3e-10 (s = 0.03) per genome per generation, i.e. 1.6e-3, 2e-5, 1.5e-6 of the total LTEE mutation supply 4.1e-4 (G_f = 1,587 at s = 0.01: U_b = 4.1e-9). So the order-of-magnitude G_f (1,322-1,587) is reproducible with plausible parameters, but the model is underdetermined (3 orders of magnitude in U_b).
**Sensitivity to Ne** (s = 0.01, U_b fixed): G_f = 7,306 (1e6), 2,929 (3.3e6), 1,744 (1e7), 1,337 (3.3e7), 1,159 (1e8): logarithmic dependence on Ne.

**Supply response, asexual, LTEE Ne (assumed, see above)** (4 replicates each; rows from the output; G_f = 1/k):

| s | U_b x1 → x100 | ratio for 100x | exponent a (100x) | ratio for 94,000x | a (94,000x) | local a at x1 |
|---|---|---|---|---|---|---|
| 0.003 | G_f 1,293 → 272 | 4.76x | 0.34 | 216x | 0.47 | 0.30 |
| 0.01 | 1,316 → 449 | 2.93x | 0.23 | 30x | 0.30 | 0.22 |
| 0.03 | 1,269 → 324 | 3.91x | 0.30 | 23x | 0.27 | 0.51 |

**EXTRAPOLATION, not a simulation result.** The "independent-sites" rate is the closed form 2N·U_b·u(s), i.e. it assumes R_int ≈ 1 (as F2 found for free recombination) at ~1,000+ active loci, beyond the tested ≤ 272. Under that assumption it is 1.5-172x the simulated asexual rate (G_f 8 at s = 0.003; 183 at s = 0.01; 831 at s = 0.03), i.e. R_int^-1 = 7.2 (s = 0.01), 172 (s = 0.003), 1.5 (s = 0.03); at 100x supply the factor is 39-3,600. At s = 0.003 a sweep lasts ~(2/s)ln(2Ns) ≈ 8,000 generations, so ~1,000 loci would be in the 0.1-0.9 zone at once, about 4x F2's tested maximum. Caveat: the extrapolation lies beyond F2's validated range (2N*U_b up to 32; here 0.02-22 at 1x and up to 2×10^6 at 94,000x, n_mid unknown). Direction (asexual interference lowers the rate) is supported; magnitude is not simulated. Also, calibrating a single-s beneficial-only process to the LTEE total substitution rate (1/1322 per generation; the neutral expectation 4.1e-4 is already ~54% of it) conflates neutral and adaptive fixations.

### A interpretation
- Asexual response is sublinear, as Day says (critics also predict it), but *more* sublinear than his mutator data: simulated 100x → 2.9-4.8x (a = 0.23-0.34), below Day's 8.5-17x (a = 0.47-0.61) and strict 19.7x. A one-s model without a DFE is the likely reason; mutator lines also have a DFE, hitchhiking and, in LTEE, diminishing-returns epistasis. So the exponent is not reproduced quantitatively; the qualitative sublinear (a < 1, declining with supply at fixed s, rising slightly with supply as the system saturates) is.
- KITTENS' linear scaling (a = 1) is **not supported for an asexual genome**: the sim gives a = 0.23-0.34 at 100x. It is supported for a recombining one only in F2's tested regime (a = 1.00, free recombination, up to 272 active loci, N = 1000, s = 0.01, soft selection). Day's a ≈ 0.5 sits between. The Day-side claim that a ≈ 0.5 holds "in both" asexual and recombining populations is not reproduced for free recombination in that regime; the critics' "a → 1 with recombination" is supported there but not shown at human scale (active loci likely 10^4-10^5, far above tested).
- Asexual-specificity of the LTEE ceiling: at the LTEE-calibrated supply and s = 0.01, free recombination would (EXTRAPOLATED, assuming R_int ≈ 1) multiply the rate by ~7 (G_f 183 vs 1,316) and by ~170 at s = 0.003 (the dominant uncertainty is s and U_b which the calibration cannot pin). So a large part of the LTEE "ceiling" is asexual interference, but the factor is parameter dependent (1.5x to 172x, extrapolated).
- Linking to Day's stated 94,000x gap: using the asexual exponent (0.28-0.47) rather than 1 gives 23-216x, close to Day's/this audit's 206-1,136x range for his exponent; with free recombination exponent 1 gives 94,000x. The truth for humans depends on how many chromosomes/linkage groups and the DFE, not tested.

## Suggested verdicts (three-verdict) for the claim files
- **F2** (feasibility of pipelining): internal: holds in form (interference exists; asexual R_int 0.09-0.65); external: **Day's cap (R < 0.5 by ~230 loci) not reproduced for r = 1/2 in the tested regime** (N = 1000, s = 0.01 single s, soft selection, ≤ 272 active loci, 2N·U_b ≤ 32; R_int 0.975 at 272). The human-scale active-locus count (rough Little's-law estimates 10^4-10^5) is far above tested, so the Bernoulli Barrier is neither confirmed nor falsified at human scale. Supported for tight linkage (R_int 0.2 at 0.1 M); cost-of-selection (H) not tested.
- **F** (Kimura fixation time limits fixations): reinforces F1 verdict: latency does not bound throughput; interference bounds it only with linkage.
- **A** (MITTENS formula, A-sim): arithmetic unchanged; external: the formula's use of LTEE G_f as a global constant is not supported for recombining genomes in F2's tested regime (magnitude extrapolated); for asexual genomes a ceiling-like saturation is real but logarithmic.
- **A2** (LTEE G_f): G_f order of magnitude (1,300-1,600) reproducible in a plausible clonal model, but any such fit is a statement about ~Ne*U_b*s combination, not a universal constant.
- **A2e** (LTEE as ceiling): internal: as stated in the corpus (supply 94,000x larger) it is a *non sequitur* if the LTEE is clonal-interference-limited; external: **not supported for recombining organisms** (extrapolation from F2 assuming R_int ≈ 1, not a simulation: free recombination 1.5x-172x above clonal at the same supply). Credit to Day is narrower than "asexual saturation" (critics predicted that too): his sublinearity claim and the reality of interference under linkage are borne out.
- **A5b** (KITTENS linear): linear scaling holds for free recombination within F2's range, fails for asexual (a = 0.23-0.34). Verdict: external: partially supported; "parity" depends on assuming free recombination across all selected loci.
- **A5d** (supermutation sublinear): sublinear confirmed for asexual (a 0.23-0.34, somewhat lower than Day's 0.47-0.61); Day's explanation "bottlenecked by sweep dynamics" is right for linked loci, not for unlinked ones; generalization to recombining genomes not supported in F2's tested regime (a = 1.00).
- **A5f** (clonal vs recombining): supported, direction quantified: recombination raises the rate (R_int clonal 0.09 → free 0.97 at 2N*U_b = 32). Day's "recombination won't speed up fixation" is contradicted for rate (Kimura-Ohta 1969 is single-locus).
- **G / Gc** (Bernoulli Barrier ~230): no saturation of throughput or per-locus success at n_mid = 272 with r = 1/2 in the tested regime (rate linear in supply, R_int 0.975); falls short only with tight linkage. Gc falsifier (P_fix < 50% of 2s at n_active ≈ 230, soft selection, free recombination) **not met in the tested regime**; not tested at human-scale active loci. Not tested: hard selection, per-locus P_fix measured directly (I used throughput R_int, which is the same quantity averaged), s = 0.01 only at ≥ 230 loci.

## Caveats
- N = 1000 (not 10^4), 4 replicates, single-s, no DFE, no epistasis, no deleterious mutations or mutator load, soft selection only, haploid-equivalent (cross-checked with fwdpy11 at three points only).
- LTEE Ne = 3.3e7 and s are assumptions; the calibration yields U_b ranging over 3 orders of magnitude.
- The free-recombination values at LTEE-calibrated parameters are extrapolations of the F2 pattern (R_int ≈ 1), not simulations at Ne = 3.3e7.
- LTEE Ne = 3.3e7 is unsourced (≈ N0·log2(100)); not retrieved from a PDF.
- Burn-in 3,000 generations (s = 0.01) may leave a small non-stationary bias at the highest supply; the "n_mid" at 2N*U_b = 32 was 75-272 depending on linkage.
- The "A interpretation" first bullet's wording should be read as: simulated sublinearity is stronger (lower exponent) than Day's mutator exponent; the model lacks a DFE.
- Desai-Fisher formula recalled from memory and found inaccurate in this regime; not used.

## Review corrections applied
Source: REVIEW-R4-correctness, -steelman-day, -steelman-critic.
1. Seeds: `hash(str)` (salted per process) replaced by `zlib.crc32(...)` in f2_multilocus.py and a_ltee_scaling.py; both reran (3 worker processes, `python -I`); a small cell (F2 free and 1.5 M, one LTEE class-process task) gave identical rates in two separate processes. All tables above are from the reruns. Headlines moved only within noise (F2 free R_int 0.97 to 0.975 at 272 loci; clonal 0.087 to 0.088; LTEE asexual exponents a = 0.24-0.35 to 0.23-0.34; G_f at 1x 1,309-1,340 to 1,269-1,316).
2. The free-recombination 1.5-172x (previously 1.6-174x) is labelled an EXTRAPOLATION (R_int ≈ 1 assumed at ~1,000+ active loci, beyond tested ≤ 272), not a simulation. The script's table header "(=free recombination, F2-validated regime)" must not be read as validation at LTEE parameters.
3. "Contradicted at r = 1/2" softened to "not reproduced in the tested regime" (N = 1000, s = 0.01, single s, soft selection, ≤ 272 active loci, 2N·U_b ≤ 32); the human-scale active-locus count is far above tested.
4. "Partial credit to Day: asexual saturates" reworded: critics predicted saturation too; Day's credit is sublinearity and real interference under linkage.
5. LTEE Ne = 3.3e7 marked unsourced (≈ N0·log2(100)); a retrieved source on LTEE effective size is needed.
6. Added a note that the single-s calibration conflates neutral and adaptive fixations.
Not done: DFE, hard selection, N = 10^4, 2N·U_b ≥ 100 runs (reviewer-suggested further checks).
