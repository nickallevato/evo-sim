# REVIEW of R4 results: critic-side steelman

Scope: R4-H-C2.md, R4-B3b-C1.md, R4-B1c-B4a.md, R4-F2-A.md. Reviewer role: argue the critics' / mainstream position as strongly and honestly as possible, and flag where critics are wrong. Quote IDs refer to `docs/research/sources/quotes-critics.md`. Items marked [outside repo] are mainstream-literature points from memory, not retrieved here; treat as unverified.

Standing observation: several R4 checks test arguments that **no critic in the corpus actually made** (Nunney/Keightley for H; the Euler-Lotka reading of d; the B4a ancestral-Ne numbers). Those are legitimate audit tests of Day, but the balance ledger should not credit "critics" for them. Credit belongs to the auditor or to the literature.

---

## H (Haldane cost) and H1/H2/H5/H7/H8

1. **Critics' strongest response.** Nesslig20 PS-04: Haldane's cost "does not apply to drift"; the cost bounds selected substitutions only. Mansfield MF-08 concedes the selection-specific question is separate. Hancock's null-model argument (GG-12) is likewise neutral-only. Strongest literature-side response: Nunney 2003 (H2): cost "substantially less" for M > 1/2; soft selection reduces or eliminates it. [outside repo] Truncation/threshold selection (Maynard Smith 1968; Sved, Reed & Bodmer 1967) and standing-variation/polygenic adaptation lower the cost further. Kimura's own use of Haldane's dilemma (1968) was to argue most substitutions are neutral, i.e. it is a point *for* the neutral explanation of the 20M.
2. **Engaged?** Partly. R4 tests Nunney with a reconstructed model (his Eq. 3 and 5 are lost), and tests Day's Term 3 arithmetic. It does not engage the critics' scope argument beyond noting Day's 2026-05-07 retraction (Term 3 bounds selected substitutions only) and asking whether H falls under it. It does not engage truncation selection, polygenic adaptation, or Kimura's reply.
3. **What it shows.**
   - For critics: 300 holds only at M <= 0.1 and a 10% budget; at M >= 1 or R >= 5 the hard-selection limit is 8-44 generations per substitution, not 300 (R4 tables: hard n=1, M=1: 84/26/13.6/6 for R=2.2/3/5/40). D = 30 requires p0 = 3e-7 (diploid); for p0 = 1e-2..1e-6, D = 9-28, i.e. 92-278 generations. Hössjer's 15,800 is 10.5x Haldane's own 1,500 (H5), so his cost step is unsupported by Haldane arithmetic. Day's Term 3 vs Haldane comparison contained an inconsistent basis (7.7 vs 17.1). Comparing selected-fixation limits with 20M total differences is a category error (H1 concession).
   - Against critics / weaker than it looks:
     - "Soft selection removes the cost" is **not** reproduced. In Model 1 soft is the worse regime at R <= 3 (a 10% surplus caps the selection differential); in Model 2 soft is worse at R=2.2. The critics' stock reply (soft selection) is therefore model-dependent and should not be cited as settled. Nunney's own caveat (quote in H2) is that soft selection applies only to intraspecific competition, and he says hard selection likely dominates under directional environmental change.
     - Human M is undetermined (R4 derives 2.4e-4 per bp; M >= 0.5 needs ~2,000 bp of target per "locus"). The audit is right to give no verdict, but this means the key regime question is open and **nothing in the repo shows humans are in the M > 1/2 regime**. Critics are not entitled to claim H is refuted, only that it has not been shown to bind.
     - Keightley (H7): hard accounting at U = 2.2 needs ~18 offspring per female. R4 correctly reads this as "hard accounting is implausible", but it does not decide hard vs soft. Humans have well-documented high juvenile mortality, so R in the hard model could be large; this is not a pro-Day point.
4. **Realism of hard-selection Haldane.** Fair to treat as a bounding case, not a typical case. Reasons it overstates for humans [outside repo]: (a) adaptation largely from standing variation (low D); (b) polygenic shifts need small frequency changes, not substitutions; (c) pre-reproductive mortality ~40-50% in forager populations gives budgets far above 10%; (d) the 10% was Haldane's illustrative figure. Reasons it is not trivially irrelevant: Nunney's simulations are hard-selection and give extinction at M = 0.1; a mean excess of ~1 substitution/300 gen per locus group is the right order for *new-mutation sweeps in small, low-M populations*. Recommend the audit record "regime-dependent; critics' soft-selection reply unproven".
5. **Additional checks.** (i) Human M estimate from a sourced beneficial-mutation rate (e.g. DFE papers) rather than 2Kmu x target; (ii) truncation selection and quantitative-trait (polygenic) variants of `gauss_run`; (iii) standing-variation start p0 in Nunney model; (iv) K-independence at fixed M (K = 500 only); (v) retrieve Haldane 1957 primary (currently via Nunney).

---

## C2 / C2a / C2c / C2d / A4 (turnover coefficient d)

1. **Critics' strongest response.** Camestros CA-12: d "would clearly have changed during human evolution"; CA-03 (not defined in text, later corrected). Hössjer's gap is created by putting d inside the neutral rate (balance ledger weakness). Mainstream: Euler-Lotka/Hill-Charlesworth treat generation time as T (mean age of mothers) and s as per-generation relative fitness; no extra factor [outside repo, "hypothesis (H-i)" in R4].
2. **Engaged?** Partly. R4's derivation (d s is exact for hazard-scale s; factor 1 for per-generation s) is not a critic's argument but a better one than Camestros's. It does not engage CA-12 (time variation of d) at all, and it does not retrieve how published aDNA papers define s.
3. **What it shows.**
   - For critics: C2 "fails as stated" (d is a unit conversion); Day's own formula does not give d = 1 for discrete generations except at L = 1/e; C2c ratio is an algebraic identity (not a test); d is not identifiable from three trajectories; Day's d = 0.45 is s*d from priors on s.
   - Against critics / to flag:
     - Partial credit to Day is warranted in one narrow place: **if** a paper's s is a hazard-scale mortality coefficient, d s is exactly right. That depends on source definitions not retrieved. The audit says so, but the verdict "C2 fails as stated" is stronger than the unretrieved definitions allow; recommend "fails for per-generation s; holds for hazard-scale s; which applies is unchecked".
     - Observationally equivalent alternatives (selection onset 2,100-3,100 y later; generation length 51-66 y; s lower; dominance) were tested by R4, but they show the trajectory data **do conflict with the published s at d = 1** (required s 0.024 for LCT vs published .04-.10). That is a real anomaly in the source literature; critics have not explained it. The audit should not read "d not identifiable" as "no anomaly".
     - R4 did not reproduce Day's Table 1 d values (Siler 0.79-0.93 vs 0.53 at e0 = 32; 0.13-0.21 vs 0.015 at e0 = 78). Since Siler is a stand-in, this is inconclusive, but it means even the "d = H_bar" reading does not endorse Day's numbers.
     - Hancock/Mansfield/McCarthy never addressed d; "critics refuted d" is the auditor's result.
4. **Additional checks.** (i) Retrieve Mathieson 2015, Loog 2017 etc. and record how s is defined (per-generation logistic slope?) and what generation time is assumed; (ii) Coale-Demeny tables for Table 1; (iii) test CA-12 directly (d varying with e0 over the 5-10 ky window); (iv) the Hill-1972 Ne note ("2/(2+Vk)=0.5 for Poisson") is flagged as from memory; verify or remove.

---

## B3b (Balloux & Lehmann overlap + fluctuation) and B3c (RRME 0.743)

1. **Critics' strongest response.** Kimura 1962 and Kimura & Ohta 1969 (B7a/B7b): fixation probability = initial frequency; keruru KR-01/KR-02 (census N, exact chain 1/(2N_census)); Day's concession B3g that Ne does not appear in the Kimura identity; Mansfield MF-01.
2. **Engaged?** Yes. B3c's mechanism test (P_fix x M_i = 0.97-1.02, martingale) is exactly KR-02 / Kimura 1962, and the B&L reproduction directly tests Day's best-supported ally citation.
3. **What it shows.**
   - For critics: fixation probability is 1/N at birth, not 1/(2N_t); 0.743 is a window artefact (range 0.60-0.87, limit 0.598); B&L's sign for realistic demography is upward (acceleration) while RRME predicts a decrease; Day's "RRME confirms B&L" is false in sign. Fluctuation alone with discrete generations gives k = mu exactly.
   - Against critics / to flag:
     - Day gets real partial credit on B3b: B&L's k != mu **exists** and is reproduced for overlapping generations (e.g. k/mu = 0.458, 0.264). The critics' blanket "k = mu" (Hancock GG-03, MF-01) is a discrete-generation, constant-or-fluctuating-N result; it is not exactly true with overlap. The effect for human parameters is small (-2% to +38% transient) but not zero. Hancock's derivation (Taylor expansion of Kimura formula) does not mention overlap.
     - "Per mean generation time" normalisation varies 0.81-1.11 under strong fluctuation; Lehmann 2014's definition is not retrieved. This remains open and could change the headline size for long-lived species with dramatic demography.
     - The human case is analytic, not simulated.
4. **Additional checks.** (i) Retrieve Lehmann 2014 and recompute per-generation-time rate; (ii) simulate a human-like overlapping model with the Holocene growth; (iii) test whether the overlap result survives age-structured fecundity (R4 used uniform parent choice, no senescence).

---

## C / C1 / C1a / C6 (ancient DNA, ascertainment)

1. **Critics' strongest response.** keruru KR-03 (~10^-29 expected fixations from intermediate frequencies in 240 generations; later withdrawn as a *claim against Day's data* but the computation stands, KR-04). Repo's C1 point 1 (new substitutions are not on a panel built from present-day polymorphism) and point 2 (panel ascertained on polymorphism). Haak 2015 design (discovered in Yoruba/San heterozygotes).
2. **Engaged?** Yes for KR-03, C1 point 1 and Haak design; partly for Day's actual statistic (first-passage binning "21 events"; not modelled).
3. **What it shows.**
   - For critics: zero fixations from < 50% and 0-3 from 50-90% is the neutral expectation (0.04-0.11 at Ne = 1e4), so the headline does not discriminate. New-in-window fixations ~5e-151 per site. Sample-level newly-100% (13.8-18.2k predicted) brackets v62 observed 17.8k. C1a's stated mechanism (bias toward European modern polymorphism) is **wrong in sign** for the same-population design D1 (zero), and right only for intermediate starts under African discovery (D2/D3) by factor 1-3.
   - Does C1 "understate" the damage to Day? Somewhat, in three ways: (a) the repo's "non-discriminating" headline is too soft: observed 1 and 3 completions at 50-90% **exceed** the Ne = 1e4 expectation (Poisson P(>=3|0.11) = 2e-4), i.e. direction is *faster* than neutral at that Ne, not a stopped clock; matching needs Ne ~ 7,000 or admixture. (b) Panel ascertainment raises the expected number of true fixations from 5.2 to ~1,100-1,850; Day's "630 expected vs 21 observed" and the repo's own rescaling of 5.2 are both wrong comparators, so the shortfall claim collapses on its denominator. (c) Event rate overall suppressed 20-30x for >=90% bands by D2/D3, so C1a's "favors detection" is wrong where most true completions live.
   - Against critics / to flag:
     - v66 (3,469) is 3.8x below the model (13.3k) and unexplained; the sim does not fit both releases. Some of the "match" is v62 only.
     - The 1 and 3 anomalies are explained by "admixture/error, not modelled". Real Europe had large admixture pulses (farmer/steppe/WHG) in the 7,000 y window. That would affect frequency trajectories far more than drift, so the "single closed population" model is the main structural weakness; it is a caveat on *both* directions. Critics (keruru) never modelled it either.
     - Ne = 1e4 is parameters.yaml unverified; keruru's temporal estimates are 8.1-9.8k. Day's circularity charge (KR-06: Ne from theta presupposes k = mu) is not answered by the sim, which assumes the same Ne. A sourced Ne by a method not using the clock (temporal/IBD) would answer it; the tail results show Ne 7k-10k spans 1.5 to 0.04 expected 50-90% completions, a 40x swing.
     - Split time 2,000 gens is an assumption (12.5-15.3k variation).
     - C6 "630 verified" arithmetic is credited to critics; 150M x 1.2e-8 x 350 = 630 holds.
4. **Additional checks.** (i) Reproduce Day's actual first-passage statistic on simulated time series at the real sampling times and bin sizes; (ii) admixture model (three-way) with sourced proportions; (iii) Ne from an independent method (IBD/temporal) in place of 1e4; (iv) investigate the v62 vs v66 gap (filtering); (v) selection-free vs selection-allowed (known sweeps like LCT would be fixations-in-progress that Day counts as "adaptive").

---

## B1c / B1 / B6 (ancestral pipeline state, Ne history)

1. **Critics' strongest response.** Mansfield MF-05 ("pipeline would have been full"), Camestros CA-04 (all differences treated as post-split), Hancock GG-13 / B6c (no standing variation). Ally-adjacent: Yoo 2025 ancestral Ne 132k-198k.
2. **Engaged?** Yes.
3. **What it shows.**
   - For critics: with sourced ancestral Ne and any sourced descendant Ne, K/UT is 1.9x-3.9x (excess), never a deficit; equilibrium start gives k = mu within 1.4%; empty-start premise unsupported.
   - Against critics / to flag:
     - The excess is mostly **ancestral alleles fixing in the lineage**, which are shared across lineages and are not human-chimp differences. So B1c does not support "the 20M are easily accounted for"; it rebuts only Day's "empty" premise. The audit says this; the suggested verdict "contradicted" should be limited to the premise.
     - The excess also shows that **simple k = mu (McCarthy 22.5M, Hancock, KITTENS 9.7M) is not the correct model for a contracting lineage**. Critics' stated numbers all assume stationarity. They are right in steady state (control 0.986) and wrong by 2-4x in the sourced non-stationary case (although the observable is d, handled in B4a). So the critics' arithmetic is "right for the wrong reason" if the real history is non-stationary.
     - Human Ne trajectory is a scenario; PSMC numeric curve was not extracted (PM2013 Table S5 not retrieved). Takahata and Charlesworth values come from abstract snippets. Prado-Martinez Ne depends on mu (factor 2).
     - Day's U(T - 4Ne) formula is shown correct for **post-split new mutations** (0.84 matches 0.84). That is a point for Day's internal validity, properly recorded.
4. **Additional checks.** (i) Retrieve PM2013 Supplementary Table S5 / PSMC numeric curve; (ii) with linked sites (recombination map) and background selection; (iii) isolate the stationary special case to show critics' numbers reproduce there (they do: control).

---

## B4a (two-lineage divergence with ILS) and the CSAC 14-22% vs 51-61% tension

1. **Critics' strongest response.** Camestros CA-04; CSAC 2005 ("polymorphism accounts for 14-22% of the observed divergence rate"); Hancock/Nesslig20/McCarthy numerical agreement with ~35M.
2. **Engaged?** Yes for Camestros; partly for the numeric critics (see below).
3. **What it shows.**
   - For critics: d = 2muT + theta_anc to ~1%; Day's empty-pipe term does not reduce d at all; Day's "rounding error" (7%) holds only at Ne_anc = 1e4, which fails to reach observed d (0.65% vs 1.23%, needs T ~ 492k gens).
   - **Is the CSAC tension a real problem?** Mostly no, but it is a real caveat on the headline. (a) The two numbers measure different things: CSAC's 14-22% is d minus *fixed* divergence, which is the sim's "poly-but-diff" (8-25% across A/B configs; 25% for B at Yoo's Ne), not theta_anc, which includes ancestral alleles that have since sorted into fixed differences. The repo's own derived number (1.23 - 1.06)/1.23 = 14% is the low end of CSAC's range and follows from the "fixed <= 1.06%" bound. (b) Even the low CSAC figure (14% of 35M ≈ 5M sites) is ~3x Day's 1.5M sites, so the qualitative critic point (ancestral term is not negligible) survives on any reading. (c) The unresolved part: CSAC's own t2 of 1-2 My implies Ne_anc around 2-4e4 at their mu, versus Yoo's 1.3-2.0e5. High Ne_anc is thus not independently supported; the data fix only 2muT + 4Ne_anc mu. So the critics' claim "half the divergence is ancestral" (51-61%) is **model-dependent** and should not be quoted as a result.
   - Against critics / to flag:
     - **Critics' own numbers are contradicted, not reproduced.** Hancock GG-04 ... GG-09 (76.8 x 2 x 252,000 = 38.7M) uses the diploid genome size (GG-05 corrects to haploid but keeps 76). Haploid SNV rate gives 38.4 per generation per lineage, so 2 lineages x 252,000 = **19.4M**, which is what B4a's 2muT (0.60%) delivers. Hancock's and Nesslig20's (PS-02, 37.8M) match to 35-40M observed is a double count that happens to hit the observed value. The correct reading is ~19M fixed neutral differences (essentially Day's own required 20M) plus ~15M from ancestral polymorphism at Yoo-like Ne. KITTENS/Reddit 9.7M (RE-06) is one lineage. McCarthy's 22.5M (MC-04) lands near the same place via 9 My x 20 y x N = Ne = 1e4 and does not mention ancestral polymorphism.
     - Camestros's CA-04 is vindicated qualitatively, but the "Day treats all differences as post-split" claim is true only for the fixed-count; the 2muT in the day-side formula already reproduces ~19M. So the neutral argument against Day's 20M is that **the neutral rate already supplies ~19M fixed differences**, not that ancestral polymorphism fills a gap.
     - Unlinked sites; ILS discordance fraction and outgroup not run; scaled-model bias -1.3% unexplained.
     - Time T and mu: if T = 450k gens (Day's 9 My / 20 y) the ancestral share falls to ~14% automatically, so the critic claim "needs high Ne_anc" depends on T = 252k. The data cannot separate them.
4. **Additional checks.** (i) Rerun with T in {252k, 350k, 450k} and mu in {1.2e-8, 2e-8} and report the (T, mu, Ne_anc) surface that fits 1.23% d and <= 1.06% fixed simultaneously; (ii) the ILS discordance fraction (Scally 2012 ~30%) as an independent constraint on Ne_anc; (iii) linked-sites model.

---

## F2, G, Gc (multi-locus interference, Bernoulli Barrier)

1. **Critics' strongest response.** Hancock GG-01/GG-13 (sequential model implies no standing variation); Myers PZ-01 (massively parallel); Bowers BO-02; Mansfield MF-04 (interval between fixations, not latency); McCarthy MC-08.
2. **Engaged?** Yes, as a feasibility test, but with a specific scope: soft selection, genic, s = 0.01, N = 1000, four replicates.
3. **What it shows.**
   - For critics: R_int ≈ 1 (0.97 ± 0.004) with free recombination at 269 active loci; rate linear in supply; Gc's falsifier (>=50% reduction at ~230 loci) not met; fwdpy11 agrees. A 1.5 M single linkage group gives 0.58 at 208 loci (pessimistic bound for a 23-chromosome genome).
   - Against critics / to flag:
     - **Soft selection only.** The binding constraint for a real organism is cost (H), not interference. F2 shows nothing about the combination of 230 simultaneous sweeps *and* a fixed reproductive budget. Critics (Myers, Bowers, Hancock) argue "parallel" without addressing this; Mansfield concedes the selection question is separate (MF-08). F2 therefore supports "parallel is feasible" but not "20M adaptive substitutions are feasible"; critics should not claim the latter.
     - Day gets partial credit on interference being real: R_int clonal 0.09-0.6; tight linkage (0.1 M) 0.20. The critic phrase "fixations do not queue" is true only given sufficient recombination.
     - N = 1000 only; s = 0.01 only (and s = 0.001 weak test); no DFE or epistasis; 2NU_b range to 32 versus a human regime that may be higher; unscaled N = 1e4 not run; 4 replicates.
     - The R_int normalisation by single-locus u(s) assumes the single-locus formula applies; for Day's G specifically (p^n barrier), independence implies the joint-success probability multiplies, which is the G3 specific-vs-any distinction rather than a barrier. R4 treats it correctly but does not state it in these terms.
4. **Additional checks.** (i) N = 1e4, s = 0.005 and 0.02, 20+ replicates; (ii) combined hard-selection x multi-locus with a real reproductive budget (merge H and F2); (iii) 23-chromosome map with human-length chromosomes; (iv) DFE with deleterious background.

---

## A / A2 / A2e / A5 / A5b / A5d / A5f (LTEE scaling)

1. **Critics' strongest response.** RE-07 (LTEE largely non-recombining, one clone, one environment); Camestros CA-08 (E. coli vs apes); CA-10/CA-11 (G_f is an average, not the fastest); KITTENS RE-08 (94,000 x 11.7); McCarthy MC-05..MC-07 (genome size and mutation rate).
2. **Engaged?** Yes for RE-07 and CA-08; partly for KITTENS (linearity is tested only in the free-recombination range).
3. **What it shows.**
   - For critics: an asexual population shows logarithmic saturation (a = 0.24-0.35 per 100x supply); free recombination gives a = 1.00 over the validated range; the LTEE "ceiling" is substantially clonal interference; recombination raises the rate 1.6x-174x at LTEE-calibrated parameters.
   - **Is "partial credit to Day: asexual rate saturates" fair?** Not as phrased. That asexual populations saturate is the critics' own prediction (RE-07, CA-08 "if humans reproduced the way E. coli reproduce"), so the sim confirms critics, not Day. The result is a point against Day's application: Day uses the LTEE rate as a ceiling for a recombining genome, and the sim shows his a ≈ 0.5 does not carry over (a = 1.00 under free recombination). Fair credit to Day is narrower: his statement that the LTEE rate is *sublinear* in supply is right, and his mutator-line exponent (0.47-0.61) is stronger than the sim's one-s asexual result only because the sim lacks a DFE.
   - Against critics / to flag:
     - **KITTENS' linearity is not established** at the claimed scale. Free recombination a = 1.00 is verified to 2NU_b = 32 (269 active loci). KITTENS's 94,000x is 3 orders beyond; the sim itself calls the extrapolation unvalidated. The factor 94,000 is also total mutation supply per genome, not the beneficial supply that actually drives adaptive fixations, and RE-09 flags the assumption. Hössjer's "concession" of A5 (127 → 15,800 → 10M) uses the same linearity and the same untested genome-length scaling, so it is not independent evidence for the critics.
     - Calibration is underdetermined: U_b varies 3 orders of magnitude for the same G_f; Ne = 3.3e7 is from memory; G_f scales logarithmically with Ne (1,157-7,619 across 1e8-1e6).
     - Hancock's bacterial mu = 1e-11 vs 8.9e-11 measured (balance ledger) makes the neutral-vs-LTEE comparison closer than he shows (within ~2x). Critics who say "LTEE rate >> neutral" overstate; R4's calibration shows the LTEE adaptive fraction is tiny (1e-3 to 1e-6 of total supply) which is consistent with mostly-neutral or near-neutral substitutions.
     - The sim's free-recombination factors at LTEE parameters are extrapolations of F2, not simulations.
     - Day's A5d explanation ("bottlenecked by sweep dynamics") is correct for linked loci; the sim agrees, which is a legitimate Day-side point to retain.
4. **Additional checks.** (i) Free-recombination run at larger 2NU_b (>= 100) with DFE to test whether linearity actually holds beyond 32; (ii) separate beneficial from total supply in the KITTENS decomposition; (iii) retrieve LTEE Ne from a source; (iv) test A5's genome-length ×650 scaling with a finite pool of beneficial targets (saturation of available beneficial sites).

---

## Cross-cutting findings

- **Critics' numbers.** McCarthy 22.5M: arithmetic reproduces (450e9/20,000); consistent with 38.4/gen/lineage only if one lineage at 450k gens; assumes N = Ne and 100% neutral. Mansfield: not tested; his 2% illustration is ~44x short (opponent file). Hancock 38M: contradicted by B4a (double count; correct fixed total ~19M). Nesslig20 37.8M: same. KITTENS 9.7M: one lineage, consistent. Hössjer (ally): 127 → 15,800 reproduces arithmetically; cost step not supported (10.5x Haldane's own 1,500); d inside the neutral rate manufactures the 2.2x gap.
- **Where critics' published arguments go wrong, as revealed by R4:** (1) diploid/haploid double counting in the 38M agreement; (2) "k = mu" is exact only in steady state with discrete generations; (3) soft-selection rescue of cost is model-dependent; (4) parallel-sweep feasibility was shown only for soft selection; (5) KITTENS linear extrapolation beyond tested range; (6) keruru's 10^-29 uses a circularly derived Ne; (7) aDNA anomalies at 50-90% (1 and 3 vs 0.04-0.11) are unexplained by the critics' own model.
- **Concessions to Day that are legitimate:** B&L overlap effect is real; U(T - 4Ne) is right for post-split new mutations; interference is real with linkage; d s is right for hazard-scale s; Haldane's 300 holds at M <= 0.1 and 10%.
- **Concessions that go too far:** none observed that are standard-theory-false; the phrasing "partial credit: asexual saturates" and the verdict "d fails as stated" should be narrowed as noted above.
