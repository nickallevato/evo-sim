from gen import *
Z3='[MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04)'
Z6='[Zenodo 18166234](https://zenodo.org/records/18166234) (key Z18166234), pub. 2025-12-24 (modified 2026-01-06)'

claim('A4','turnover-coefficient-d','The Selective Turnover Coefficient d (about 0.45) reduces effective generations for selection','day','A','A',
 [('supports','A'),('depends-on','A4a')],False,'firsthand','extracted',('pending','n/a','pending'),
 q('d = (Actual allele frequency change per generation) / (Change predicted by discrete-generation model)',Z6+', ¶33 (s2.3).')+'\n'+
 q('d = T × d_continuous = T × [∫ μ(x) × l(x) × v(x) dx / ∫ l(x) × v(x) dx]',Z6+', ¶51 (s3.3). μ(x) = −d[ln l(x)]/dx is the mortality force.'),
 '''effective generations = N_gen x d, with d = `selection.turnover_d` = 0.45.   F_max = (t_div x d)/(g_len x G_f).
`derived:` 325,000 x 0.45 = 146,250; 450,000 x 0.45 = 202,500 (the "202,500 generations" Tree of Woe interview figure, TW-01); T x mean mortality force is dimensionless (T in years, μ in 1/y), so the integral form is dimensionally consistent. Day (Q&A 2026-01-19, ¶16): "If l(x) and v(x) were constants, they\'d cancel and you\'d get d = T × ∫μ(x)dx. But they\'re not constants, they\'re age-dependent functions".''',
 '- Stated: overlapping generations make the effective rate of allele-frequency change per nominal generation lower by d.\n- Implicit: the nominal generation length used for N_gen equals the T in the definition; d is constant over the 6.3 My lineage; d is a pure multiplier on G_f, independent of s.',
 '''- Against: Camestros (A4b): d is undefined in the introduction (later corrected: Ch.13, App. A) and would have changed during human history.
- In support: Hössjer reproduces 127 with d = 0.45 (HO-01) and applies d inside a neutral-rate calculation (A5a); Duffy presents the overlapping-generations correction (A4c).
- Weaknesses in the responses: Hössjer\'s use of d in the neutral rate is outside the definition above (d is defined for allele frequency change under selection); Day\'s MITTENS 3.0 dropped d (A4d), so the 3.0 numbers do not depend on it.''',
 NOLIT,
 '''No check has run. Proposed check A4-sim: age-structured Moran or Leslie-matrix model with a human life table (Coale-Demeny West, as cited by Day), allele with fixed s; compare allele-frequency change per mean generation time T with a discrete-generation Wright-Fisher at the same s.
- Under the claimant\'s model: ratio of per-generation frequency change ≈ 0.45.
- Under the opposing model: the ratio is ≈ 1 when T is the mean age of parents (a generation is defined by turnover), so d ≈ 0.45 reflects a definition of T, not a slowdown.
- Result that would change a verdict: a ratio between 0.3 and 0.6 with T = mean age of reproduction.''',
 'Script: none yet. Review: pending.', '- Life table (l(x), v(x) or fertility m(x)), generation time T; output d; toggle d on/off in F_max.')

claim('A4a','d-empirical-estimate','d ≈ 0.45 ± 0.08 estimated from ancient-DNA time series at three loci (loci differ between two papers)','day','A','A4',
 [('depends-on','A4')],False,'firsthand','checked',('pending','unverifiable','contested'),
 q('Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2.','[Zenodo 18165980](https://zenodo.org/records/18165980) (key Z18165980), pub. 2025-12-28, ¶69 (Methods).')+'\n'+
 q('Day and Athos (2025a) estimated d empirically from ancient DNA time series, finding d ≈ 0.45 from three independent loci (LCT, SLC45A2, TYR).',Z6+', ¶5.'),
 '''d = 0.45 ± 0.08 (`selection.turnover_d`). Two papers published four days apart give the same value from different locus sets: {LCT, SLC24A5, HERC2} (Z18165980) and {LCT, SLC45A2, TYR} (Z18166234). The record cannot say whether one is a typo or whether both sets give 0.45 (versions ledger).''',
 '- Stated: aDNA allele-frequency time series (Mathieson et al. 2015 panel).\n- Implicit: d is estimated by comparing observed frequency change with a predicted discrete-generation change, so it requires a known s per locus; the s values are not given in the quotes.',
 '''- Against: Mathieson 2015 states the SLC24A5 rise "mostly" reflects migration, not selection, so SLC24A5 cannot supply a selection-based d. The main text of Mathieson gives no s values.
- In support: none in corpus.
- Weaknesses in the responses: the critics have not recomputed d. Day has not reconciled the two locus lists.''',
 LITH+'''| Mathieson et al. 2015 | "The strongest signal of selection is at the SNP (rs4988235) responsible for lactase persistence in Europe"; SLC24A5 "was mostly due to migration" | verified; no s values in main text or ED legends: **unverified** for Day\'s use |''',
 'Not run. Prediction (claimant): recomputing d from the Mathieson 2015 or AADR data at LCT gives 0.45 ± 0.1. Prediction (opposing): the estimate depends on the assumed s and on migration, with a range spanning 0.2–1.',
 'No script. Review: pending.', '- None directly.')

claim('A4b','d-critique-camestros','Camestros: d is not defined where it is introduced and would have changed over human history','critic','A','A4',
 [('attacks','A4')],False,'firsthand','extracted',('pending','partial','pending'),
 q('As this figure would clearly have changed during human evolution (and indeed demonstrably changed during human history), it doesn’t make a lot of sense.',
   '[Camestros Felapton, Reading Vox Day 2026 [5]](https://camestrosfelapton.wordpress.com/2026/01/29/reading-vox-day-so-you-dont-have-to-2026-5/), 2026-01-29, para 25 (CA-12).')+'\n'+
 q('Day does not say in the introduction, nor does he say what it is in Chapter 1 or indeed any of the actual chapters.',
   '[Camestros Felapton, Reading Vox Day 2026 [2]](https://camestrosfelapton.wordpress.com/2026/01/25/reading-vox-day-so-you-dont-have-to-2026-2/), 2026-01-24/25, para 32 (CA-03). The author later corrected this: d is defined in Ch.13 and App. A.'),
 'Qualitative: d(t) not constant. If d varies between 0.3 and 1, N_gen x d varies by 3.3x; the shortfall moves by the same factor (derived).',
 '- Stated: d is time-dependent.\n- Implicit: Day\'s 0.45 is a constant applied to the whole lineage.',
 '''- Against (Day): not answered in the corpus; the 3.0 paper drops d (A4d).
- In support: the definition (A4) is a function of the life table, which varies with population.
- Weaknesses in the responses: the CA-03 complaint was withdrawn in the post (d is defined in Ch.13 and App. A); the time variation claim is not quantified.''',
 NOLIT, 'No prediction needed (qualitative).', 'No script.', '- Allow d(t) as a time series.')

claim('A4c','overlap-80pct-25-generations','Duffy (presenting Day): at 80% selection efficiency the fixation time is about 25 generations','ally','A','A4',
 [('depends-on','A4')],False,'secondhand','extracted',('pending','unverifiable','pending'),
 q('the actual fixation time in a population where selection operates at 80% efficiency will take approximately 25 generations.',
   '[Gutsick Gibbon, Will Duffy livestream, Human Evolution #2](https://www.youtube.com/live/6jXiwrcC5PQ), 2026-09-22, t=00:25:11 (DU-01; auto-caption). Duffy presenting Day\'s overlapping-generations claim; Day\'s own statement of it was not located.'),
 '''Unclear what "25 generations" refers to; the units are not stated in the quote. Day\'s 2019 Gariépy follow-up has a related statement: "This rate reduced the average fixed mutation propagation time from 1,600 to 15.7 generations" (GA-02, [Whopping the floor](https://voxday.net/2019/02/11/whopping-the-floor/), 2019-02-11, ¶10; Day\'s minimum-viable-population model). `derived:` 1,600/15.7 = 101.9; 1,600/25 = 64. Neither reconciles with d = 0.45 (1,600 x 0.45 = 720).''',
 '- Stated: selection efficiency of 80%.\n- Implicit: efficiency is related to d or to the Bio-Cycle correction.',
 '''- Against: none in corpus.
- In support: none in corpus.
- Weaknesses: secondhand; no Day equation harvested; Duffy states in Q&A that he is "not a mathematician" (DU-04).''',
 NOLIT, 'No prediction: claim not formalised.', 'No script.', '- None until a formulation is sourced.')

claim('A4d','d-dropped-in-mittens-3','MITTENS 3.0 drops d and uses 252,000 nominal generations','day','A','A4',
 [('revises','A4'),('supersedes','A')],False,'firsthand','checked',('holds','n/a','pending'),
 q('Applied to human-chimpanzee divergence (205 million required fixations on the human lineage across 252,000 available generations), the shortfall is 1,075,000-fold for non-mutators and 104,873-fold across all twelve populations including hypermutators.',
   Z3+', p.1 (abstract). The 3.0 text has no d term (searched "turnover" and "d =").'),
 '''F_max(3.0) = 252,000 / 1,322 = 190.6, with no d. `derived:` had d = 0.45 been applied: 252,000 x 0.45 = 113,400; /1,322 = 85.8; shortfall 205e6/85.8 = 2.39e6 (2.2x larger than 1.075e6). Dropping d is therefore conservative with respect to the claim. The versions ledger notes d = 0.45 in both Zenodo papers of Dec 2025 computed on different loci (A4a).''',
 '- Stated: none (d is not mentioned).\n- Implicit: nominal generations are the right unit; or the d correction is subsumed into the empirical G_f (the LTEE is asexual and discrete).',
 '''- Against: Hössjer (HO-01, HO-04) still uses d = 0.45 in his reproduction (published 2026-09-14, before 3.0).
- In support: Camestros\'s objection to d (A4b) no longer applies to the 3.0 numbers.
- Weaknesses in the responses: the 3.0 paper offers no reason for dropping d; the later "Appendix D" human-derived rate (A5e) cites the "Bio-Cycle correction for overlapping generations", so the correction is still invoked in 3.0 elsewhere.''',
 NOLIT, 'Arithmetic only (above).', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- d toggle (already specified in A4).')

claim('A5','genome-size-mutation-supply','The LTEE rate does not transfer to humans: the human genome is ~690x larger and has far more new mutations per generation','critic','A','A2',
 [('attacks','A2e'),('attacks','A2')],False,'firsthand','checked',('holds','n/a','contested'),
 q('The human nuclear genome contains approximately 3.1 billion base pairs, roughly 690 times larger than the compact E. coli genome of about 4.6 million base pairs.',
   '[Dennis McCarthy, Why Probability Zero is Wrong About Evolution (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (orig. paid 2026-01-26), para 60 (MC-05).')+'\n'+
 q('As clear, the expected rate of fixed mutations has to be determined according to the particular circumstances of the population in question—its genome size, mutation rate, etc.',
   'same post, para 62 (MC-07).'),
 '''supply_ratio = (μ_human · L_human) / (μ_E · L_E).
`derived:` (python3 -I) 3.1e9/4.6e6 = 674 (McCarthy states "roughly 690"; 690 follows from a 4.5 Mb E. coli genome, 3.1e9/4.5e6 = 689; a 2% discrepancy with his own stated inputs). Per-site rate ratio 1.2e-8/8.9e-11 = 135 (8.9e-11 is the Wielgoss 2011 figure via McCarthy; not in the quote files). Per-genome ratio 38.4/4.1e-4 = 93,659 using the numbers in MITTENS 3.0 (4.1e-4 from s4.3; 38.4 = 3.2e9 x 1.2e-8 from the s6.4 product, where the paper prints only the 100x value 38,400). Neutral expectation for supply scaling alone: E. coli 4.1e-4 per generation vs human 38.4 per haploid genome per generation.''',
 '- Stated: the expected fixation rate depends on genome size and mutation rate.\n- Implicit: fixation rate of adaptive mutations scales (linearly or otherwise) with supply; recombination and clonal interference do not reverse the direction.',
 '''- Against (Day): blog 2026-01-27 ¶22: "I didn\'t cite the E. coli study for its mutation rate but for its fixation rate" (A5g); 3.0 s5.1 mutators give only sublinear gains (A5d).
- In support: Hössjer (A5a), Sparky_6_4 (A5b), Hancock (A5c), Dembski (interviewer, DE-01) asks the question to Day; Duffy concedes "the mammal fixation rate is slower" (DU-06) without numbers.
- Weaknesses in the responses: McCarthy\'s uncited "60 to 100 de novo mutations" is a diploid per-newborn count (MC-06) while the E. coli figure is haploid per division; the 690 factor has a 2% internal discrepancy; the critic gives no dependence of adaptive fixations on supply.''',
 LITH+'''| Kong et al. 2012 | "with an average father\'s age of 29.7, the average de novo mutation rate is 1.20×10-8 per nucleotide per generation" | verified (abstract) |
| Keightley 2012 | "μ is about 1.1 × 10(-8) … an average of ~70 new mutations arise in the human diploid genome per generation" | verified-partial (abstract) |''',
 '''See A5b for the scaling arithmetic and the proposed A-sim (pre-registered in file A).
- Under the claimant\'s (critic\'s) model: the rate scales with supply to within a factor 2 at least.
- Under Day\'s model: the LTEE rate is a ceiling (A2e).''',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- `mu_per_site_per_gen`, `genome_length`, `new_mutations_per_genome` as inputs to the supply term.')

claim('A5a','hossjer-127-15800-10m','Hössjer: scaling the MITTENS bound for mutation rate and genome length gives about 10 million, only a factor 2 below 20 million','ally','A','A5',
 [('revises','A5'),('supports','A')],False,'firsthand','checked',('holds','n/a','contested'),
 q('This is a lot larger than the previous upper bound 127 of 𝐹 , but still more than three orders of magnitude smaller than 20 million fixations.',
   '[Hössjer, MITTENS - Convincing Arguments Against Neo-Darwinism (PDF attached to Dembski post)](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf), 2026-09-14, p.3 (HO-01).')+'\n'+
 q('which still is less than 20 million, but only by a factor of 2.','same PDF, p.3 (HO-02).')+'\n'+
 q('I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli.','same PDF, p.3 (HO-06).'),
 '''F_127 = 9e6 · 0.45 / (20 · 1,600) = 126.6;  F' = F_127 · (1.25e-8/1e-10) = 126.6 · 125 = 15,820 ("15,800");  F'' = F' · (3e9/4.6e6) = 15,820 · 652 = 10.3e6 vs R = 20e6 (ratio 1.94).
`derived:` (python3 -I) all steps reconcile. With the measured E. coli rate 8.9e-11 instead of 1e-10: ratio 140, F'' = 11.6e6, gap 1.7x. His neutral cross-check: 3e9 · 0.45 · 1.25e-8 · 450,000 = 7.59e6 (reconciles, eq. 3.1); without d the same product is 16.9e6, ratio 0.84 to 20e6. Total scaling in Hössjer: 125 x 652 = 81,500; in KITTENS (A5b): 93,659. Same method, different inputs.''',
 '- Stated: F is proportional to mutation rate and to genome length (eq. 2.4 assumes F ∝ L); both calculations assume parallel fixation between loci.\n- Implicit: d = 0.45 multiplies the neutral rate (not part of the neutral identity); the Haldane step (HO-03) restores a gap without a calculation.',
 '''- Against: KITTENS (A5b) goes further and finds parity with the SNV-only count. Day\'s A5d says supply scaling is sublinear.
- In support: Dembski\'s abridgement (HO-08) says the calculation "yields a number very close to Day\'s genome-size-adjusted bound"; Hössjer agrees with Day\'s conclusion (HO-06).
- Weaknesses in the responses: the 2.2x gap comes entirely from d inside the neutral rate (without it 16.9M vs 20M); the Haldane/cost step is asserted, not computed (HO-03); Hössjer advocates "uncommon descent" (HO-10), a different explanation than Day\'s.''',
 LITH+'''| Haldane 1957 (via Nunney 2003) | one substitution per 300 generations | verified-accurate via Nunney only |
| Nunney 2003 | cost "substantially less than Haldane\'s estimate" for M > 1/2; soft selection "eliminates" it | verified; no critic engaged it |''',
 'See A (A-sim). Prediction (Hössjer): adaptive fixations scale linearly with supply and genome length until a cost-of-selection limit (H) binds; this is not computed. Prediction (critic): no such limit binds at the required rate.',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Mutation rate, genome length, and an optional cost-of-selection limit (H).')

claim('A5b','kittens-94000x11p7','KITTENS: the 1.075M shortfall factors into 94,000 (mutation-supply ratio) x 11.7 (bases counted as events)','critic','A','A5',
 [('attacks','A2e'),('attacks','A3a')],False,'firsthand','checked',('holds','accurate','contested'),
 q('The claimed shortfall is 94,000 × 11.7, or about 1.1 million.',
   '[r/DebateEvolution, Sparky_6_4 (AI-assisted), "KITTENS: rebuttal to Vox Day\'s MITTENS 3.0 by Clauwd Meowgorithm"](https://www.reddit.com/r/DebateEvolution/comments/1wxgsjm/), 2026-10-04, s3 "The headline shortfall decomposes into two artifacts". Verified in raw copy `sources/raw/critics/arctic-title-Vox%20Day.json`.')+'\n'+
 q('Once one scales the LTEE rate for the mutation supply per genome and counts SNVs as events, the achievable number (17.9 million) is about equal to the required number (17.5 million).','same post (RE-08).')+'\n'+
 q('I present this as an illustration, not as a proof that adaptive fixations scale linearly with mutation rate.','same post (RE-09).'),
 '''Shortfall = R/F with F = N_gen/G_f. KITTENS: S = (U_h/U_E) · (R_205/R_SNV) where U_h = 3.2e9 · 1.2e-8 = 38.4 (KITTENS cites s6.3–6.4; the paper prints the product only for the 100x case, 38,400), U_E = 4.1e-4 (s4.3), R_205 = 205e6, R_SNV = 17.5e6.
`derived:` (python3 -I) U_h/U_E = 93,659; R_205/R_SNV = 11.714; product = 1,097,143 vs paper 1,075,000 (2.1% above, from rounding F = 190.6). 191 x 93,659 = 17.89e6 ("17.9 million", reproduces); 17.89/17.5 = 1.02. Table inputs found in Z23003785: 4.1e-4, 191, 17.5M, 205M, 1,075,000. The 38.4 is not printed in the paper; it is the 1x value of the product 3.2e9 x 1.2e-8 printed in s6.4 as 38,400 for 100x.
**Sensitivity (derived, this audit, not in KITTENS):** KITTENS assumes fixation rate ∝ supply (exponent 1). Day\'s own mutator data (A5d) give a response of 8.5x (clone-pair) to 16.9x (metagenomic) for 100x supply, an exponent a = ln(f)/ln(100) of 0.47 to 0.61. Applying that exponent to a 93,659-fold supply gives a factor of 206 to 1,136, achievable 39,370 to 217,006, and a shortfall against 17.5M of 445x to 81x (against 205M: 5,207x to 945x). Extrapolating an exponent measured over 100x to 94,000x is itself an assumption; mutator lines also carry deleterious load and are asexual.''',
 '- Stated: only the paper\'s own numbers; a linear-scaling illustration (RE-09). AI-assisted; citations from memory (RE-11).\n- Implicit: units of U_h (per haploid genome) match U_E; the SNV-only requirement is the right event count; linear scaling.',
 '''- Against (Day): Z23003785 s5.1 and s8.6: a 100x mutation increase gives 8.5x–17x, "Supermutation does not scale linearly"; s8.6 Appendix D gives 27,600 generations per fixation from human parameters (A5e).
- In support: Hössjer\'s independent calculation reaches within 2x (A5a); Day concedes the SNV-only variant is legitimate (A3b).
- Weaknesses in the responses: with the sublinear exponent the gap reopens to 81x–445x for SNV-only, so the parity conclusion rests on linear scaling; the critic did not verify Day\'s mutator exponent; the critic\'s 94,000 treats LTEE and human U as the same kind of quantity (haploid-genome new mutations per generation).''',
 LITH+'''| Wielgoss 2011 (via McCarthy; not in repo) | E. coli per-site rate 8.9e-11 | unverified |
| Kong 2012 | 1.20e-8 per nucleotide per generation | verified (abstract) |''',
 '''Pre-registered here, check not yet run (A-sim, see file A).
- Under the critic\'s model: forward simulation with human-scale supply and free recombination fixes ≥ 1e7 adaptive substitutions per 252,000 generations at the same s as the LTEE.
- Under Day\'s model: fixations saturate at ~190 per 252,000 generations regardless of supply.
- Third possibility (this audit): sublinear scaling with exponent 0.5–0.6, leaving a 80–450x gap.
- Result that would change a verdict: measured response exponent of fixation rate to supply in a recombining simulation.''',
 'Arithmetic audit (python3 -I, scratch): decomposition reproduces; sensitivity computed in the scratch session. Review: pending.',
 '- Exponent a in rate ∝ U^a as a user parameter (0.5 / 0.6 / 1).')

claim('A5c','neutral-supply-ecoli-vs-human','Hancock: on neutral supply alone E. coli expects ~4e-5 fixations per generation (22,000 gens per fixation) and humans dozens per generation','critic','A','A5',
 [('attacks','A2e')],False,'firsthand','checked',('holds','n/a','contested'),
 q('you only expect four e to the neg5 mutations to fix per generation.',
   '[Gutsick Gibbon and Zach Hancock video](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:53:50 (GG-07; auto-caption).')+'\n'+
 q('under neutrality, it should take like 22,000 generations to fix one mutation.','same video, t=01:54:12 (GG-08).'),
 '''E. coli neutral rate = μ_E · L_E: with μ = 1e-11 per site (Hancock) and L = 4.6e6, 4.6e-5 per generation → 1/4.6e-5 = 21,739 generations per fixation (reproduces "22,000"). With the measured 8.9e-11 (McCarthy via Wielgoss 2011): 4.1e-4 per generation → 2,439 generations per fixation.
`derived:` (python3 -I) The MITTENS 3.0 s4.3 text itself uses the neutral identity for the LTEE: "expected number of neutral hitchhikers is μ_genome × G" = 4.1e-4 x 50,000 = 20.5 (Z23003785 p.7). The same formula for humans: 38.4 x 252,000 = 9.68e6 neutral substitutions per lineage over 252,000 generations, the figure KITTENS also reports (9.7M). Against R_SNV = 17.5M: 0.55 (factor 1.8). Day contests k = μ for humans (B3, B5).''',
 '- Stated: neutral substitutions occur at the mutation rate per genome per generation (k = μ).\n- Implicit: all mutations are neutral for the neutral estimate (an upper bound on the neutral share); the human rate 1e-8 per site per generation is per haploid genome.',
 '''- Against (Day): 3.0 s8.2 argues the drift channel is "off" in the LTEE (Ne ≈ 3e7) and that k = μ holds in the LTEE through hitchhiking; in humans Ne = 10,000–33,000 gives 4–13 neutral fixations over 252,000 generations (serial division of time by fixation time, G2); k ≠ μ in humans (B3).
- In support: Day\'s own s4.3 hitchhiker formula; Tenaillon 2016 constant-rate accumulation.
- Weaknesses in the responses: Hancock\'s 1e-11 is below the measured 8.9e-11 (balance ledger); his "back of the napkin" calculation (GG-16) has no confidence interval; Day\'s 4–13 neutral fixations over 252,000 generations is a serial calculation (252,000/66,000 = 3.8, 252,000/20,000 = 12.6).''',
 LITH+'''| Tenaillon 2016 | neutral mutations accumulate at a constant rate in non-mutators | verified |
| Kimura 1962 / Kimura & Ohta 1969 | neutral fixation probability 1/2N; time 4Ne | verified (see B-claims) |''',
 'Covered by B-branch checks (B0.5: neutral k = U at equilibrium; B1/B1b). Result from RESULTS.md B0.5: simulated neutral k 0.05018 (N=50) and 0.04964 (N=200) vs U = 0.05 (z = +0.13, −0.64), i.e. k = U for any N at equilibrium. B1b: expansion produces a transient deficit of about 4N_new generations (cumulative 0.733 of U·T at N0/5→N0); contraction an excess.',
 'Link: `research/checks/RESULTS.md` B0.5, B1, B1b. Arithmetic audit (python3 -I, scratch).', '- Mutation rate, genome length, N, demographic history (B1b), neutral fraction.')

claim('A5d','supermutation-sublinear','Hypermutators: a 100x mutation rate gives only 8.5x–17x faster fixation, so fixation is not bottlenecked by mutation supply','day','A','A5',
 [('attacks','A5b')],False,'firsthand','checked',('non-sequitur','n/a','contested'),
 q('Supermutation does not scale linearly with mutation rate. It cannot, because fixation is not bottlenecked by mutation supply. It is bottlenecked by the dynamics of sweeps:',Z3+', p.8 (s5.1). The headline result is "a 100-fold increase in mutation rate produces only an approximately 8.5-fold increase in fixation throughput by clone-pair analysis at 50K (from 893 gen/fix to 104.7 gen/fix), or a 17-fold increase by metagenomics at 60K (from 1,322 gen/fix to 78 gen/fix)".'),
 '''response f = G_f(non-mutator)/G_f(mutator): 893/104.7 = 8.53 (clone-pair); 1,322/78 = 16.95 (metagenomic); 1,322/105 = 12.6 (the 105 used in s7.3). Exponent a = ln f/ln 100 = 0.47 (clone-pair), 0.61 (metagenomic). `derived:` (python3 -I) a < 1 (sublinear) is supported by the paper\'s own table; a = 0 (no dependence on supply) is not: f > 8 for 100x supply. Also: Ara-2 (−906) is a failure mode (A2c); the mutator average row ("Average (all 7)": 477.6 fixations, 104.7 gen/fix) includes it.
A related s5.3 table shows mutator advantage rising from 7.6x at 10K to ~20x at 40–50K and 16.9x at 60K (non-mutator: 794 → 1,322).''',
 '- Stated: sweep dynamics, clonal interference, and finite carrying capacity of the selective environment bottleneck fixation; "More mutations … produce more competition between mutations, most of which cancel each other out."\n- Implicit: the mutator populations\' response (asexual, deleterious load) generalises to the response of a recombining genome to a 94,000x supply increase.',
 '''- Against: the response is positive and large (8.5x–17x); "not bottlenecked by mutation supply" does not follow from a positive sublinear response. A2h: the paper\'s s6.4 supermutator arithmetic contains a tenfold slip. Recombination (A5f) is a mechanism by which supply-limited and interference-limited regimes differ.
- In support: the KITTENS author flags linear scaling as an illustration (RE-09), consistent with sublinearity; Day\'s s6 argues a mutator allele in a sexual organism cannot hitchhike with its beneficial products.
- Weaknesses in the responses: the critics (A5b) do not use Day\'s exponent; Day does not apply his own exponent to a 94,000x supply difference (which gives 206–1,136x, A5b), so the data are consistent with both a large and a small gap.''',
 LITH+'''| Tenaillon et al. 2016 | "six populations (…) had 96.5% of the point mutations, having evolved hypermutable phenotypes" | verified |''',
 '''Pre-registered in A (A-sim): measured exponent a of fixation rate versus supply in a simulated asexual vs recombining population.
- Under Day: a ≈ 0.5 in both; supply-limited regime never reached.
- Under critics: a → 1 in the recombining case at low supply, falling below 1 only at high supply.''',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Fixation rate vs supply curve for asexual vs recombining populations (output of A-sim).')
