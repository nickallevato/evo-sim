# Correctness review of R4 result sets H-C2, B3b-C1, B1c-B4a, F2-A

Reviewer: Sonnet 5.5 (correctness only). Date: 2026-10-07. No existing repo file was edited.
Scratch re-runs (all in the session scratchpad, not committed): `h_cost_of_selection.part_a/part_c`, `c2_ratio_nonident.py` (full), `c2_overlap_vs_standard.py` (full), `h_keightley_load.py` (full), `c1_ascertainment_sim.py` (main block), a burn-in test of `wf2.evolve` (240 reps, N_anc_sim=500), a B4a config-A re-run at Ne_anc=1.98e5 (200 reps). Hand re-derivations of B&L eq (3) for C1/C2. Not re-run: the IBM scans (h_cost b, nunney_gauss*), `f2_multilocus.py`, `f2_fwdpy11.py`, `a_ltee_scaling.py`, `b3b` simulation part (all read line by line; tables checked for internal arithmetic only).

Severity: BLOCKER = a result cannot stand; MAJOR = a stated conclusion or number is wrong or overreaches and must be changed before adoption; MINOR = wording, bookkeeping or small numeric slip; OK = checked and correct.

Summary: no BLOCKERs. The simulation code is sound throughout. The MAJORs are (i) an open-item (a) mis-equation in B4a that produced a spurious "tension" and an invalid alternative (T, Ne_anc) solution, (ii) the HCG-vs-HCB node choice in B4a's "supported" verdict, (iii) F2/A statements phrased as simulated that are extrapolations, (iv) hash()-based seeds that make two scripts non-reproducible, (v) the H-IBM hard-vs-soft mutation-supply confound and post-hoc tuning toward Nunney's 300, and (vi) the C6/C1 "does not rescue Day" conclusion, which compares against a count the model does not simulate.

---

## 1. R4-H-C2.md

### H: cost of selection

- **OK** `h_cost_of_selection.py:36-67`, re-run. 30/0.10 = 300; 146,250/300 = 487.5; D_haploid = ln(1/p0); D_diploid additive = 2 ln(1/p0) (9.23, 13.87, 18.50, 23.13, 27.76 for p0 = 1e-2..1e-6; s = 0.01 and 0.001 agree to 0.5%); p0 for D = 30 is 9.4e-14 (haploid) and 3.1e-7 (diploid). All match the .md.
- **OK (e), adjudicated.** `part_c` lines 61-62 give Term 3/(Haldane+d) = 17.1 and Term 3/(Haldane without d) = 7.7. Term 3 = 0.45/(2 ln 6600) = 0.02558/gen (1 per 39.1). Haldane+d = 0.45/300 = 1/667. So the "7.7" in `claims/H8-kimura-calculator-term3.md:41,65` and `claims/H1-term3-retraction.md:42` ("a factor of about 7.7 ... (300/39)") mixes bases: it divides a nominal-generation rate that includes d by a Haldane rate that excludes d. The correct same-basis ratio is 17.1 (17.06 either way with or without d on both sides). Also, 487 in 146,250 is already the d-adjusted count, so the 300 in "300/39" is per effective generation. **Fix:** correct H8 lines 41 and 65 and H1 line 42 to 17.1x; note that the unscaled Term 3 figure for 260,000 generations is 6,652 (H1 says 6,690, which uses 0.0257/gen; 0.02558 is the unrounded value).
- **MINOR** R4-H-C2.md H1 suggested update: "the 2.7x between '7.7' and '17.1'". 17.1/7.7 = 2.22 = 1/0.45. Fix: "2.2x (= 1/d)".
- **MINOR** `h_cost_of_selection.py:7-8` vs R4-H-C2.md (a). The docstring prediction already says "diploid additive about twice the haploid value", which at p0 = 1e-3..1e-6 gives D = 14-28, i.e. 140-280 gens. The "70-140" interval in the same sentence is the haploid figure. The .md says "the prediction was low for the diploid case"; more accurate: the prediction was internally inconsistent (haploid interval, diploid caveat) and the diploid half was right.
- **MAJOR** `wf_hc.py:78-79,93` (treadmill_run) mutation-supply confound. Mutations are applied to the J juvenile gametes, so mutants per locus per generation = 2*J*u = (f/2) * M, not M = 2*K*u as defined. Soft selection has f = R, so the effective M is inflated by R/2 (5x at R = 10, 20x at R = 40); hard selection inflates by about 1/mean-survival (<= R/2). Consequences: (1) the "R-scan" (soft T50 163 -> 82 as R goes 2.2 -> 40) mixes surplus and supply; (2) the M-scan statement "soft is within about 15% of hard" compares soft at effective M = 5M against hard at about 1-2M, so at the low M that matter (0.1-0.5) the two are not at equal supply; (3) `gauss_run` (wf_hc.py:128-143) has the same construction, and the "M = 0.1, R = 2.2 gives 285" match is least affected (R/2 = 1.1) but the R = 10 comparisons with Nunney are. **Fix:** define u from adult count (u = M/(2 K f_eff)) or mutate gametes of the K adults, then rerun the M-scan and the R-scan; at minimum state the confound in the .md and withdraw "soft within 15% of hard".
- **MAJOR** post-hoc tuning toward Nunney's number. Docstrings of `h_nunney_gauss.py:1-20` and `h_nunney_gauss_lowR.py:1-10` say they were written after seeing the earlier model's output ("after seeing that the constant-s treadmill ... gave only a gradual M-dependence"; "after seeing h_nunney_gauss.py give T50 ~8-25 at R=10 ... below Nunney's values"). The same-R (R = 10) test of Nunney's headline (M = 0.1 -> ~300) fails by about 12x (25 vs 300); the match (285) appears only after switching to R = 2.2, a parameter chosen after the failure. This is a legitimate exploration but not a confirmation. The .md's "Reading" bullet ("300 appears only at roughly 10% budget AND M <= 0.1") and the H suggested update ("1/300 appears only at M <= 0.1 and a 10% budget") read as findings; they are properties of a reconstructed model tuned until one number matched. **Fix:** label Model 2 results "exploratory, 2 rounds of model adjustment after seeing results" and drop the "appears only at" sentences from the verdict text; keep "qualitative M-dependence reproduced".
- **MINOR** success criteria. `wf_hc.py:107-109` (lag < 0.5) and `h_nunney_gauss.py:102` (dev2 < 0.5, no extinction): hard-selection populations that persist at a small fraction of K count as successes (N/K is not part of the criterion), while the cost to a hard population is exactly that depression. This favours hard over soft at R <= 3 and could explain why "soft is the worse regime" there. dev2 < 0.5 also allows a lag of about 0.7 allele steps. **Fix:** report N/K at the T50 point, or add N/K > 0.5 to success.
- **MINOR** T50 has no uncertainty. `h_cost_of_selection.py:73-98`: 8 reps per T (fractions in steps of 0.125), log-linear interpolation on a coarse grid (ratio ~1.3-1.5 between points). A 50% crossing from 4/8 vs 5/8 is uncertain by one grid step (30-50%). Statements such as "hard s=.10, R=3 is 30 vs soft 54" and "within 10%" (staggered loci) are below resolution. **Fix:** add a binomial CI on the 50% crossing (or 24+ reps) before quoting differences of less than 1.5x.
- **MINOR** `h_cost_of_selection.py:106` seeds are `spawn(1)[0].generate_state(1)[0] + cid`; deterministic, fine.
- **OK** P-b3 (hard T50 independent of s) correctly reported as not supported.

### H7: Keightley (`h_keightley_load.py`, full re-run)
- **OK** All table rows reproduce exactly (extinct 6/6 for Fmax = 4..20 hard; Fmax = 30: N/K 0.174 +/- 0.009, pred 0.188; Fmax = 60: 0.344 +/- 0.004, pred 0.353; synergistic hard persists from 12 with N/K 0.201). Prediction N/K = 1 - U/ln(Fmax/2) derives from f*e^-U = 2 and f = 2 exp(r(1-N/K)); correct.
- **MINOR** observed N/K is 1.5-2 SE below prediction at K = 1000 (N = 170 at Fmax = 30 is ratchet territory, mean k ~ 43.5 < 44 expected from U/s). Fine, but "predicted 0.188" vs "0.174" should be quoted with the ratchet caveat. 6 reps; extinction at Fmax = 20 (predicted N = 45) is expected.
- **OK** Conclusion stays within "hard accounting implausible at natural fertility; does not decide whether adaptation is hard or soft".

### C2 / C2a / A4: d
- **OK** Derivation, `c2_overlap_vs_standard.py`, full re-run. d_Day = sum_x mu(x) * tail(x) = sum_y l b H_full(y) (H includes the full hazard in the year of birth); `mean_cum_hazard` uses mid-class H; the two differ by 0.5*mu at the mother's age, 0.789 vs 0.784 as reported. Table in the .md reproduces: V1 0.01557/0.01557; V3 0.01982/0.01980; V4 0.02022/0.02020; V5 0.00924/0.00925; V2 0.00574/0.00574. Projection and Euler-Lotka agree to 5 digits.
- **OK** discrete control: mu0 = -ln L, b1 = 1/L gives d = sum mu*tail = -ln L analytically; code agrees (0.105/0.693/0.994/2.303). The claim "d = 1 only at L = 1/e" is correct for this formula. Note Siler e0 = 25 gives d = 1.014 > 1, so "d ranges from 0 to 1" also fails on its own terms.
- **MINOR** `R4-H-C2.md` IBM line: "400,000 individuals per type". `cohort_ibm(..., N0=400_000)` sets each type to 0.5*N0 = 200,000 (wf_hc.py:285; the script label also says 2e5). Fix: "200,000 per type (400,000 total)".
- **MINOR** "Day's d*s is 22% off for V3/V4": 0.01578 vs 0.01982 = 20.4% low (or 25.6% in the other direction); vs V4 0.02022 = 22.0%. State "20-22% below".
- **MINOR** `V1 T*dr/s = 0.778` vs d_Day 0.789 (1.4%): the .md says "exactly"; the pre-registration says "EXACTLY". It is first-order in s (s = 0.02); mid-class H also differs by 0.7%. Say "to within 1.5%".
- **MINOR** "mean age of mothers 29.7 y" is T = sum (x+1) l b / sum l b, so the mean age is 28.7 by the code's x+1 convention (newborn appears next step). Cosmetic.
- **OK** Table 1 non-reproduction is reported honestly (Siler d = 0.79/0.93 at e0 = 32 vs Day 0.53; 0.13/0.21 at e0 = 78 vs 0.015). This is a fidelity gap of 1.5-14x that should be listed as unresolved, not as "monotone decline confirmed".
- **OK/MINOR** Interpretation: "d is a unit conversion between hazard-scale s and per-generation s" is correct within the model. The residual issue is external: which s the aDNA papers estimate (not retrieved); the .md says so.

### C2c / C2d (`c2_ratio_nonident.py`, full re-run)
- **OK** All numbers reproduce (ratio 0.4646 at d = 0.2 ... 0.4778 at d = 2; synthetic pairs vary by 0.2-2.4% over d in [0.2, 2]; d interval [0.481, 0.568]; x0.75 -> [0.638, 0.756]; x1.25 -> [0.387, 0.456]; LCT dominant 0.745, SLC45A2 recessive 0.646; chicken table). Recursions (additive, dominant, recessive) re-derived by hand and correct.
- **MINOR** "Paper's 0.48 to 0.49 is rounded from 0.47 to 0.48": the exact ratios at d = 0.5..1.0 are 0.4734-0.4763, which round to 0.47-0.48, not 0.49. Say "the paper's 0.49 is 0.01 (about 2%) above the exact recursion; likely logit approximation".
- **MINOR** Dominance rows compare s as a homozygote advantage (dominant/recessive models) against s as per-copy genic advantage (additive), so the "d needed" across models is not at an equal-strength s. Say so.
- **OK** "C2c is not a test of d" stands: the invariance holds for random pairs.

---

## 2. R4-B3b-C1.md

### B3b/B3c (`b3b_overlap_fluctuation.py`, `wf_b3c1.py`)
- **OK** Hand re-derivation of B&L eq (3) for C1: 0.4583 = 0.125 + 0.2083 + 0 + 0.125; C2: 0.4167, ks = 2 - N1/N2 = 1.667. `sim_overlap` is correct: survivors by hypergeometric from the Ni pre-transition individuals, newborn parents drawn uniform from Ni (cnt/Ni), mutation at birth as Poisson(U*births), count to Nj, fixation = count == Nj, arrival = U*births/Nj. Haploid M = N throughout, consistent with pi_j = 1/N_j. Burn-in 8*tau and T = 10*tau are adequate for a 1/(4N Tg) relaxation. Seeds are SeedSequence-derived.
- **OK** Analytic Part 3: s/(1-s)(cosh r - 1) matches (0.9969 at r = 0.016, 0.9817 at r = 0.039); births/N = 1 - s/(1+r) = 0.0552 vs 0.04 (ratio 1.38).
- **MINOR** `b3b:134` for r = 0.039 the cycle uses a hard-coded L = 40 (range e^{0.039*39} = 4.6x, not 3.28x). Result still matches the cosh formula so no numeric effect on the quoted 0.982, but the label "range x3.28" for that row is wrong.
- **MINOR** The "-> 0.5 as g grows" aside in the B3c bullet is the wrong direction: 1/(1+1/g) -> 1 as g grows and -> 0.5 as g -> 1 (long window, slow growth). 0.598 at g = 1.486 is right.
- **MINOR** 16 replicates, SE = std/sqrt(16); z values are fine, but no multiplicity correction over nine scenarios (all |z| < 1.6 so no issue).
- **OK** C1x3 (scaling) and the P_fix * M_i = 0.989/0.973/1.018/0.986 checks (SE = pf/sqrt(nfix)) are valid. e2: the 60,000-step constant tail is about 3.6 absorption times (b = 13, N = 328: decay exp(-7)), so truncation bias is below 0.1%.
- **MINOR** The mapping "RRME assumes fixation probability 1/(2N_t)" is a reconstruction of Day's derivation. The simulation falsifies P_fix = 1/N_t for a mutant born in cohort i; whether that is Day's step should be confirmed against the quoted equation (not checked here).
- **Overreach? No.** The B3b/B3c verdicts (B&L effect real, sign upward for realistic growth, 0.743 a window artefact) are supported. One honesty point: C1 shows k per mean generation time 0.815 (-18%) and C2 1.111, so "per generation time" is not preserved under strong fluctuation. The .md lists it as open; keep it prominent.

### C1/C1a/C6 (`c1_ascertainment_sim.py`, main block re-run)
- **OK** Main numbers reproduce: D0 353,358; D1 0.0 (1e-29); D1b 7,574 (50-90% band 0.0165); D2 13,807 (50-90% 0.0379; true fixations 1,135); D3 18,157 (50-90% 0.0432; 1,393); flux ratio 1.0335; new-in-window 4.9e-151; v66 sizes 13,254 and 50-90% 0.112. Enrichment ratios 1.25/3.39 for D2 and the 5-30x suppression of >=90% bands reproduce.
- **OK** Algebra: inclusion indicator applied at the modern frequency for D1 (discovery in present-day samples), at the African frequency after P_A for D2/D3; Neolithic band matrix Bd/Ba excludes 100% samples; derived and ancestral alleles are mutually exclusive events. SFS theta/i with M = 2*Ns copies and theta = 4 Ne mu fixed is the right scaled equilibrium.
- **MINOR (explains P1 miss)** the 3.4% flux excess (ratio 1.0335 at N_s = 1000, 1.021 at 2000) comes from using theta/i as the starting SFS of the finite chain. Fine for the totals (13.8k vs 17.8k observed), but the tail-sensitive 50-90% band carries 4-25% error as the .md notes. Not a correctness bug.
- **MINOR** `analyse` uses only ancestral polymorphism: African-private mutations arising after the split (up to 2,000 generations) are in the panel (single heterozygous male) but not in the denominator `wt @ IA`, so P(event | in panel) is slightly overestimated and counts on a fixed-size panel are an upper bound. Likely a few percent given the 2y(1-y) weighting; state it.
- **MAJOR** C6/C verdict wording. The .md compares model expectations against the later paper's "observed 17,806 / 3,469 / 1 / 3" (Z23046531, Neolithic-vs-modern sample comparison) but the C6 claim concerns Z18525185's "21 fixations post-7000 BP" among time bins of small ancient samples (claims/C6 Formal statement: bins as small as n = 129, first-time 100% in a later bin). The simulation does not model that statistic. Therefore (i) "this does not rescue Day" (C6 paragraph) and (ii) "C6 external: not like-for-like" are fine as caveats, but the table row "observed v62/v66" as a comparator for C6 is not like-for-like, and the sentence "model expectation of true fixations is ~1,500-1,850 vs 21 observed" would, if the 21 were comparable, support a larger deficit than Day claims. The .md cannot have it both ways. **Fix:** state explicitly that the 21-count statistic is not simulated; do not list C6 as "arithmetic-error stands, neutral model explains the data" until a first-passage-in-bins version is run (n_bin = 129..1372, bins from the claim file).
- **MINOR** Split time (2,000 gens) and equal African/European Ne are assumptions, disclosed. The unscaled-N = 1e4 MC differs from the scaled chain by 4-7% (z 2-4, scaled overestimates) in the 99%+ tail; disclosed.
- **OK** Conclusion that C1 point 1 (new mutations not on the panel) holds and C1a's sign is mixed is supported.

---

## 3. R4-B1c-B4a.md

### (b) The ~1.3% low bias: explained
- **Cause (confirmed by re-run): ancestral burn-in of only 10 N_sim generations.** `b1c_ne_history.py:146` and `b4a_two_lineage_ils.py:240` call `burn_in(n, U, 10*n, rng)`. `REVIEW.md` item 6 (review #2) already found that a 10N burn-in leaves a ~2% flux deficit and raised B1 to 20N; the new scripts reverted to 10N. Test in scratchpad (`wf2.burn_in/evolve`, constant Ne = 1.98e5, N_anc_sim = 500, 240 reps): K/UT = **0.985 +/- 0.004 with 10N** (matches the .md's 0.984-0.988 controls) and **1.004 +/- 0.004 with 20N**. The B1c "from ancestral alleles" column in H0 is 3.103 vs theta/UT = 3.143 (-1.3%), and B4a d (config A, 1.98e5, 200 reps) is 1.5493 +/- 0.0028 vs formula 1.5552 (-0.4%); both are the ancestral theta term being ~1.3-2% short. The .md says "cause not isolated" and "O(1/N_sim) discretization"; both are wrong. **Fix:** rerun with `burn_in(..., 20*n)` or higher (40N is cleaner), delete the "unexplained" caveat, and drop "does not alter any conclusion" as the justification (it is now unnecessary). Severity: MINOR (no conclusion changes; the small effects are > 40%).

### (a) CSAC 14-22% polymorphism vs ancestral term 51-61%: not the same quantity
- **MAJOR (resolve the "tension").** theta_anc/d is the fraction of divergence contributed by the extra ancestral coalescent time (2*Ne_anc generations of extra branch length). Most of it ends up as sites that are now fixed differences (config A at Ne_anc = 1.32e5: fixed 1.140 of d = 1.235, while theta_anc = 0.634). CSAC's 14-22% is the fraction of the 1.23% that is still polymorphic within a species (so that fixed differences are <= 1.06%). The comparable simulated column is the **poly-but-diff** one: 7.7% (A), 25% (B: human 1e4 / chimp 4.6e4) at Ne_anc = 1.32e5; 7% (A) and 21-22% (B) at 1.98e5 (0.096/1.544, 0.334/1.549). This brackets 14-22% (the sourced lineage Ne pair, config B, gives 21-25%). There is no tension. **Fix:** delete "Tension, not resolved here", state that the comparable observable is poly-but-diff, and add a note that config B reproduces CSAC's polymorphic share to within about 4 points.
- **MAJOR** the follow-on in the same bullet ("If one instead requires theta_anc/d = 14-22% ... T = 400-440k generations ... Ne_anc 3-4e4") is built on the mis-equation and is invalid; the equation to match is poly-but-diff/d, which already fits at sourced Ne. Remove.

### Node choice and "supported" verdict
- **MAJOR** `R4-B1c-B4a.md` §2 and §3 table: "supported at Yoo's Ne_anc (1.32e5 reproduces 1.23%)". Per `parameters.yaml:49-50` and the ledger, 1.98e5 is the human-chimp-**bonobo** ancestor, i.e. the population that actually split into the human and Pan lineages; 1.32e5 is the human-chimp-**gorilla** ancestor (the older node, ancestral to H+C+B and gorilla). The right Ne_anc for the H-C split is 1.98e5, which gives d = 1.54-1.55%, **25% above** CSAC's 1.23%. The .md lists the 25% overshoot but the verdict uses the node that fits. **Fix:** state that the matching value is for the wrong node, that the pedigree mu / T / Ne_anc combination at the correct node overshoots, and that the overshoot is itself unresolved (Yoo's Ne is an average over the ancestor's lifetime, not Ne at split; mu and T both uncertain).
- **MINOR** `b4a_two_lineage_ils.py` docstring/claim file say ancestral burn-in 8Ne; the code uses 10 N_sim (and see above).

### B1c
- **OK** Code: `schedule` (centred generation times, `rint(N/f)`), `evolve` (Poisson(M_prev*U) new alleles, binomial resampling at the new size, pre-split ids tracked), K counts all fixations in the lineage. The analytic 1 + 4(N_anc - N_end)/T = 3.984 (H1) is right; the 1% shortfall is the burn-in bias above.
- **MINOR** `rint(1e4/198)` = 51 for N_end (1.0% up on 50.5); likewise HCG 76 vs 75.8. Shifts the quoted telescoped analytic by < 0.5%.
- **MAJOR (framing)** "Every sourced history gives an excess" is true by construction: every scenario is an instantaneous step (or two) from the Yoo average ancestral Ne, which is an average over the ancestor's existence, not the size at the split; no gradual decline and no sustained expansion of the human lineage was sourced (PSMC trajectory not extracted, as the .md says). The result is the B1b telescoping identity restated, not an independent empirical finding. **Fix:** rename the section "excess follows from ancestral Ne >> descendant Ne under any step history", keep the caveat that a deficit needs a sustained lineage Ne above Ne_anc.
- **OK** The reading that Day's (T-4Ne)/T applies to the post-split new-mutation column (0.84 for H1) is a correct and fair concession to Day. Keep it.
- **OK** Prado-Martinez quote L197-200 and Table 1 values (13.1-16.2; 30.9-61.8) verified against `sources/raw/sources/manual/PradoMartinez2013.txt` (lines wrapped; locators approximate). Takahata/Charlesworth numbers are secondhand, correctly marked `verified: partial/false`.

### B4a
- **OK** `pair_stats`: d = sum over ancestral alleles f_H(1-f_C) + f_C(1-f_H) plus private post-split segregating and fixed alleles; fixed differences = (1,0)/(0,1) ancestral pairs plus post-split fixed; `k = MU*f/U` converts counts to per-site (L_eff = U/(mu f)). msprime `tmrca(0, 2)` between H and C nodes is right. d matches 2 mu T + theta to within 0.4-0.7% after the burn-in bias, and msprime agrees to 0.1-0.2%.
- **OK** "Day's 2mu(T-4Ne_lin)" columns: 0.509 (Ne = 1e4), 0.336 (config B); computed as sum over both lineages; correct.
- **MINOR** SEs reflect ~1e7 effective unlinked loci; the .md says real SEs are larger. Fine.
- **Not run (disclosed):** the ILS discordance fraction and outgroup lineage.

---

## 4. R4-F2-A.md

### F2 (`wf_f2.py`, `f2_multilocus.py`)
- **OK** `wf_f2.sim`: haploid-equivalent genic selection, fitness-proportional parent sampling, 'clonal' copy / 'free' per-site mask / Poisson(R) uniform crossovers with sorted-position parity trick (verified by hand: odd count of breaks before a column means "from b"; start parent a is symmetric). Mutations are added after reproduction at U = MU/M per copy, new count 1; fixation counted when count == M. `indep_rate = M*U*kimura_u(M//2, s)` is the correct reference: for M = 2N copies u = (1-e^{-2s})/(1-e^{-2Ms}).
- **OK** Table arithmetic: 0.087*0.634 = 0.0551/gen; 0.0012/0.0551 gives exponent ~0.66; free 0.97*0.634 = 0.615.
- **OK** fwdpy11: `ConstantS(0, 1, 1, 2*s, 0.5)` with `Multiplicative(1.0)` gives het = 1 + h*S = 1 + s, hom = 1 + S = 1 + 2s: per-copy additive s. The two-run difference counting (same seed, mcounts == 2N plus `pop.fixations`) is sound given identical RNG prefix. The three cross-check points agree (0.951 +/- 0.018 vs 0.946 +/- 0.012; z for the third 1.5).
- **MAJOR (reproducibility)** `f2_multilocus.py:35` and `a_ltee_scaling.py:76` seed with `hash(str(mode)) % 9973` / `hash(tag) % 100003`. Python's str hash is salted per process (`-I` does not disable it; verified: `python -I -c "print(hash('clonal'))"` gives different values on two invocations). The documented "seed 4242" and "seed 20261008" therefore do not reproduce the tables. **Fix:** replace with a fixed lookup (e.g. `zlib.crc32(tag.encode())`) and re-run, or state that the tables are a single non-reproducible draw. Statistical conclusions are unaffected (cells are independent draws).
- **MINOR** 4 replicates per cell: the quoted SEs (e.g. 0.97 +/- 0.004) are from 3 d.f.; a t(3) interval is 3.2x wider. Differences of < 0.03 in R_int should not be interpreted.
- **MINOR** burn-in 3,000 generations from a monomorphic start (s = 0.01) should be enough (sweep time ~ 600 generations), but the high-supply clonal cells approach steady state slowly; the .md already flags it.
- **MAJOR (overreach, wording)** F2 verdict "external: **contradicted for r = 1/2**" and G/Gc "falsifier not met". The tested regime is N = 1000 (2Ns = 20), s = 0.01 only, soft selection, 2N*U_b <= 32, n_mid <= 270. Day's cap (~230 loci) is a claim about human-scale parameters at 2N*U_b >> 100; the .md itself says so in its list of untested items. Within the tested regime R_int = 0.97 at 269 active loci is a clean falsification of "R < 0.5 by ~230 loci" for this parameter set only. **Fix:** "not reproduced in the tested regime (N = 1000, s = 0.01, soft, <= 270 active loci)", and keep the Bernoulli Barrier "not falsified or confirmed at human scale".
- **MINOR** Desai-Fisher: the code's formula is the standard v = s^2 [2 ln(Ns) - ln(s/U)]/ln^2(s/U), but it requires U << s; at 2N*U_b >= 2, U/s > 0.1 and ln(s/U) < 0 near 32, so the "overestimates by up to 5x" statement describes an out-of-domain evaluation, not a defect of the theory. Harmless since unused.

### A-sim (`a_ltee_scaling.py`)
- **OK** `class_rate`: exact multinomial over fitness classes, selection then mutation (U per copy), shift of the lowest class, rate = d<k>/dt from block marks; M here is the haploid count (Ne = 3.3e7 copies), `indep_rate(int(Ne), U, s)` uses N = M/2, consistent. Table arithmetic checks: ln(4.90)/ln(100) = 0.345; ln(2.97)/ln(100) = 0.236; ln(219)/ln(94000) = 0.47; U_b as fraction of 4.1e-4: 1.6e-3, 2.0e-5, 1.5e-6.
- **MINOR** `class_rate` takes at most one new mutation per copy per generation; at 94,000x supply U reaches 0.063 (s = 0.003), a ~3% truncation. Not material to the exponents.
- **MINOR** `calib_task`: 7 bisection steps over a 1e4 range gives ~7% resolution in U_b, and the target is met to 1.4% (G_f 1,309/1,340/1,313 vs 1,322). Fine.
- **(c) LTEE Ne = 3.3e7.** Plausible and in common use (harmonic-mean size over the daily dilution cycle, about N0 * log2(100) = 5e6 * 6.64), but the .md and docstring label it "from memory, unverified". It is not a number in `parameters.yaml`. **MINOR:** add the source to the ledger (Lenski et al. 1991, Wiser et al. 2013 use this value; confirm from a PDF before relying on it). Sensitivity table already shows logarithmic dependence (G_f 7,619 at 1e6 to 1,157 at 1e8 at fixed U_b), and the calibrated U_b, not Ne, carries the 3-orders-of-magnitude indeterminacy.
- **MAJOR (d) the 1.6-174x is an extrapolation, not a simulation, and is quoted as one.** The "G_f indep" column is `indep_rate`, i.e. the assumption R_int = 1 for free recombination at Ne = 3.3e7. At s = 0.003, the independent rate is 1/8 per generation with sweep durations ~ (2/s) ln(2Ns) ~ 8,000 generations, so ~1,000 loci are in the 0.1 < p < 0.9 zone at once, 4x beyond F2's tested n_mid (270, at s = 0.01, N = 1000). In the A2e verdict line "(sim: free recombination 1.6x-170x above clonal at the same supply)" and the A interpretation bullet, call it "extrapolated from F2 (R_int ~ 1) outside its validated range", not "sim". Also drop the "(= free recombination, validated regime)" header in the A-sim table; it is not validated at these parameters. The direction (asexual interference reduces the rate) is supported; the magnitude is not.
- **MINOR** Calibrating a single-s beneficial-only process to the LTEE total substitution rate (1/1322 per generation, of which the neutral expectation 4.1e-4 is already ~54%) conflates neutral and adaptive fixations; the .md notes absence of a DFE but not this. Add one sentence.
- **MINOR** Comparison with Day's 8.5-17x (mutator data) is for total mutation supply including neutral and deleterious mutations; a beneficial-only fixed-s model gives a different exponent for reasons other than "no DFE". The .md's explanation is reasonable but should say the exponent comparison is qualitative only.
- **OK** "KITTENS linear (a = 1) not supported for an asexual genome (a = 0.24-0.35)" is supported in the model; "supported for free recombination within F2's range" is correct.

---

## Per-claim table

| claim ID | result stands? | required corrections |
|---|---|---|
| H (Haldane 300; cost vs 20M) | yes-with-fixes | arithmetic OK (300, 487, D table). Remove "1/300 appears only at M<=0.1 and 10% budget" as a finding (post-hoc tuned reconstruction); fix prediction-vs-result wording on 70-140 |
| H1 (Term 3 retraction) | yes-with-fixes | correct "7.7" to 17.1 at claims/H1 line 42; 6,690 vs 6,652 rounding |
| H2 (Nunney) | yes-with-fixes | label Model 2 exploratory; address mutation-supply confound (M defined on adults, applied to juveniles); no absolute-T reproduction; N/K not in success criterion |
| H5 (Hössjer 15,800 = 10.5x Haldane's 1,500) | yes | none |
| H7 (Keightley) | yes | optional ratchet note on N/K 1.5-2 SE below prediction |
| H8 (Term 3 vs Haldane+d) | yes-with-fixes | claims/H8 lines 41 and 65: 7.7 -> 17.1 (same-basis); "2.7x" slip in the .md should be 2.2x |
| C2 / C2a (d is a unit conversion) | yes-with-fixes | derivation and simulation correct; IBM N is 200,000 per type; "22%" -> 20-22%; "exactly" -> within 1.5%; Table 1 non-reproduction listed as open fidelity gap, not just "monotone decline" |
| C2c (ratio identity) | yes-with-fixes | paper's 0.49 is ~2% above exact 0.476, not "rounded from 0.47-0.48" |
| C2d (non-identifiability, chicken) | yes-with-fixes | note differing s conventions across additive vs dominant/recessive |
| A4 (turnover d) | yes | none beyond C2 |
| B3b (B&L overlap + fluctuation) | yes | r = 0.039 row label; keep C1/C2 per-generation-time deviations visible |
| B3c (RRME 0.743) | yes | fix "-> 0.5 as g grows" direction; confirm P_fix = 1/N_t is Day's actual step |
| C1 / C1a (ascertainment) | yes-with-fixes | note African-private post-split mutations omitted from the panel denominator (slight overcount); 3.4% flux excess from the SFS start |
| C (headline 0/1/3 vs neutral expectation) | yes-with-fixes | stands at Ne ~ 7-10k as the .md says; state it is Z23046531's statistic, not the 21-count of Z18525185 |
| C6 (630 vs 21) | yes-with-fixes (verdict wording changes) | arithmetic error (denominator mismatch) stands; delete or soften "does not rescue Day" until the first-passage-in-bins statistic with real bin sizes is simulated; do not use the 17,806 comparator for it |
| B1c (empty pipeline premise) | yes-with-fixes | recompute with 20N-40N burn-in (explains the 1.3% bias); note the excess is a restatement of the B1b telescoping under step histories, not an independent empirical result |
| B1 (finite-time count) | yes | as stated in the .md |
| B4a (d = 2 mu T + theta_anc) | yes-with-fixes | resolve CSAC 14-22% as the poly-but-diff column (7-27%), not theta_anc/d; delete the T = 400-440k alternative; use HCB (1.98e5) as the relevant node and report the 25% overshoot; burn-in bias explained |
| B6 (Mansfield, pipe full) | yes | controls recover 1.0 with 20N burn-in |
| F2 (multi-locus interference) | yes-with-fixes | restrict "contradicted at r = 1/2" to the tested regime (N = 1000, s = 0.01, soft, <= 270 loci); fix hash() seeds |
| F (latency vs throughput) | yes | none |
| G / Gc (Bernoulli Barrier ~230) | yes-with-fixes | "falsifier not met" in the tested regime only; hard selection, N = 1e4 and human-scale supply untested |
| A (MITTENS formula, A-sim) | yes-with-fixes | state that free-recombination comparison at LTEE scale is extrapolated; Ne = 3.3e7 sourcing; fix hash() seeds |
| A2 (LTEE G_f) | yes | order of magnitude reproducible; calibration underdetermined (disclosed) |
| A2e (LTEE as ceiling) | yes-with-fixes | replace "sim: 1.6x-170x" with "extrapolated, outside F2's validated range" |
| A5b (KITTENS linear) | yes-with-fixes | asexual a = 0.24-0.35 supported; free-recombination linearity supported only to 2N*U_b = 32 at N = 1000 |
| A5d (supermutation sublinear) | yes | exponent comparison with Day's mutator data is qualitative |
| A5f (clonal vs recombining) | yes-with-fixes | direction supported; magnitude at LTEE scale not simulated |
