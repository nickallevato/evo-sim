# R4 X1: arithmetic and internal-validity audit of every quantitative critic and ally claim

Script `research/checks/x1_critic_arithmetic.py`, pre-registered in commit `fa0bc9b` (predictions in the docstring, before the run). Raw output `results/raw/x1_results.{json,out}`. Three post hoc scripts, all labelled and committed separately: `x1_posthoc_wf_convergence.py` (cedc86a), `x1_posthoc_missing_rows.py` (1f3dd12, eb7617a). No claim file, argmap file, README, RESULTS.md, REVIEW.md or R5 draft was edited. Written 2026-10-09. Reviews (correctness, Day-side steelman, critic-side steelman) are still to come.

## 1. Result in one paragraph

Of the 66 claim files on the critic and ally side, 45 carry a number or a derivation and were recomputed; 21 carry none (section 8). Of the 45: **34 reproduce from the author's own inputs with no flag; 9 reproduce with a flagged basis, unit, input or can't be determined; 2 do not reproduce (keruru's C5 probabilities; the Milton lottery analogy)**. At the row level the script made 67 pre-registered predictions (70 recomputation rows once keruru's four sub-values are split, plus 5 text-fidelity greps) and all 67 predicted letters match the outcomes (of the 70 rows: 52 reproduce, 12 reproduce with a caveat, 6 do not; the 5 greps are all confirmed). One pre-registered numeric band was missed (keruru's p = 0.5 value: predicted 1e-47..1e-45, exact 5.1e-45). The errors found are real but small and cluster in the **fidelity column** (basis, units, uncited or low inputs), not in arithmetic from stated inputs. Under the strict standard used for Day ("any stated number that does not follow from the author's own inputs is an arithmetic-error, material or not") the critic and ally side gets **2 arithmetic-error suggestions (B5a comment-level, C5) and keeps 1 non-sequitur (H5)**, against 0 / 0 recorded now. Only one of the slips changes a conclusion's strength and none reverses one. The critics' pivotal identities (k = mu, P_fix = 1/(2N_census), Matev's N/Ne reductio) verify exactly.

## 2. Standard and method

- **Internal** (same rule as for Day): `arithmetic-error` if a stated number is wrong from the author's own stated inputs; `non-sequitur` if the conclusion does not follow from the author's own premises; otherwise `holds`.
- **Fidelity:** inputs cited and read correctly (quote against raw text, unit, basis). Questions about whether the model is right (external) are not scored.
- **Material?** A slip is material only if it changes a headline or a conclusion by more than ~2x, or carries an argument.
- Recomputation by sympy (exact rationals and limits) and numpy. Two heavy items: (a) keruru's C5 absorption probabilities by an **exact Wright-Fisher (binomial) backward recursion**, 2N = 20,000 copies, 240 generations, band +-700 copies (10 binomial sd; W = 1,000 gives identical digits); (b) Nesslig20's quoted fixation-time CDF against the same exact recursion at 2N = 1,000, plus exact linear solves of absorption probabilities for a neutral Wright-Fisher and a sweepstakes model with Ne about 0.15 N (Matev, keruru).
- Raw texts were read as plain text only (McCarthy comments JSON, Mansfield's YouTube comment JSON, Peaceful Science topics 18094 and 18095, the Reddit tree 1wss2wj, Day's Z23003785 text, the Hössjer PDF through the PDF viewer, Camestros posts by grep). Hancock's video exists locally only as the harvested auto-caption quotes, so every Hancock row is on the quotes, not the full transcript.

## 3. Pre-registration scorecard

| Prediction | Result | Note |
|---|---|---|
| 67 R / P / N letters | 67 of 67 match | includes M02 (units mix) and K-03 (keruru not reproduced), both predicted |
| keruru exact value at p = 0.5 within 1e-47..1e-45 | **missed:** exact 5.1e-45 | 41x above the repo's Brownian value 1.2e-46, 5x above the top of my band. Convergence at fixed t/(2N) is monotone and slow (M = 5,000: 5.1e-44; 10,000: 1.2e-44; 20,000: 5.1e-45; 40,000: 3.2e-45; post hoc), so the diffusion limit is probably about 2e-45. The call "keruru's 4e-35 does not reproduce" stands (too large by 9.9 orders) |
| "0.99 has a few percent" | exact 0.19 | the qualitative claim "meaningful chance only near 0.99" holds (0.9: 3.7e-8; 0.95: 2.2e-4) |
| a first draft of the post hoc convergence script used a band of 0.035 M (3 sd at M = 2,000) and gave non-monotone numbers | discarded | the committed version uses 10 sd |

## 4. Main table (45 numeric claims; current verdicts in the claim files, suggested verdicts here)

Columns: suggested internal / fidelity; **bold** = suggested change; "credit" = a correct critic or ally result worth recording prominently.

| Claim | Author | Stated | Recomputed | Suggested internal / fidelity | Comment |
|---|---|---|---|---|---|
| A2c | Dumb-and-Dumber | -906 Ara-2; Ara+5 38 to 0 | Day's tables: seven-mutator mean with -906 = 477.6, 50,000/477.6 = 104.7; non-mutator 227/5 = 45.4, 60,000/45.4 = 1,321.6 | holds / accurate | credit: the quote is exact and Day's own means reproduce. Artefact vs biology is external |
| A2d | Camestros (and Duffy's phrase) | G_f is an average, not the fastest | 1,322/78 = 16.9; 893/104.7 = 8.5 in Day's table | holds / accurate | credit |
| A2h | Dumb-and-Dumber | 3.2e9 x 1.2e-8 x 100 = 3,840, not 38,400 | 3,840; Day's s6.4 prints 38,400 (confirmed in raw Z23003785) | holds / accurate | credit: critic right, Day wrong |
| A3d | Hancock | achievable doubles (180 to 360) | arithmetic fine; 205e6/191 = 1.073M and 410e6/(2 x 191) = 1.073M (invariant). Day's text: "apportioned symmetrically to the human lineage" (confirmed) | holds / partial | the correction does not change Day's per-lineage ratio. See B5c on the same unit |
| A3x | McCarthy, Dumb-and-Dumber, Nesslig20, Mansfield | 410M bp are not 410M events | Nesslig20 toy 1/60, 9/60, 16.7%, "10 bp vs 2 mutations" reproduce; 14% x 3 Gbp = 420 Mbp, /2 = 210M; 410e6/40e6 = 10.25; Mansfield "around 25M" vs 1% x 3.1e9 = 31M | holds / partial | credit; the unit point matches Day's own wording (A3a). Mansfield's 25M is uncited and loose |
| A4c | Duffy (presenting Day) | 25 generations at 80% efficiency | 1,600/25 = 64; 1,600/15.7 = 102; 1,600 x 0.45 = 720 | pending / unverifiable | cannot be recomputed: units and derivation not in the quote |
| A5 | McCarthy | genome "roughly 690x" E. coli | 3.1e9/4.6e6 = 674 (689 for 4.5 Mb) | holds / **accurate** | 2.4% under "roughly"; immaterial |
| A5a | Hössjer | 127; 15,800; 10M; factor 2 | 126.6; x125 = 15,820; x652 = 10.32M; 20/10.32 = 1.94; "three orders" 1,266; "five orders" 157,480 | holds / n/a | reproduces; 125 x 127 = 15,875 vs printed 15,800 is rounding |
| A5b | KITTENS (Sparky_6_4) | 94,000 x 11.7 = 1.1M; 17.9M vs 17.5M | 38.4/4.1e-4 = 93,659; 205/17.5 = 11.714; product 1.097M vs paper 1.075M (2.1%); 191 x 93,659 = 17.89M | holds / accurate | credit; inputs found in Z23003785. The paper's SNV-only shortfall is 91,600, so "94,000 x 11.7" is exact only at parity (2.6%); immaterial. Linear scaling flagged by the author as an illustration |
| A5c | Hancock | 4e-5 per generation; 22,000 generations | 4.6e6 x 1e-11 = 4.6e-5 ("4e-5" is 13% low); 1/4.6e-5 = 21,739; at the measured 8.9e-11: 4.1e-4 and 2,439 generations | holds / **partial** | **input slip carrying a sub-argument:** 1e-11 is 8.9x below the measured LTEE value, so the neutral expectation is 2,439 generations (1.8x slower than the observed 1,322), not 22,000 (17x) |
| B2e | keruru | measured Ne/N 7e-4 to 8e-4 vs Wright 0.57 | 4/7 = 0.571; 705x and 828x; 4Ne/260,000 = 1.4, 10.7, 12.5, 15.1% | holds / n/a | reproduces. The draft states the ratio three ways (1e-4, 4e-4, 8e-4; 6,933/1e7 = 6.9e-4); the author flags "[CHECK]" |
| B3i | Matev | sum over 2N copies = N/Ne > 1 | N/Ne = 100 at N = 1e6, Ne = 1e4; exact chains: absorption probability i/2N to 3e-15 in both models, sum over copies = 1 | holds / n/a | credit: exact, including a sweepstakes model with Ne about 0.15 N |
| B4g | keruru | fossil-calibrated rate about 2x pedigree | 1.23%/(2 x 252,000) = 2.44e-8 = 2.03 x 1.2e-8; minus theta_anc 6.3e-3: 1.19e-8 | **holds** / unverifiable | reproduces; the factor 2 disappears once the ancestral term is subtracted (B4a). Keightley's "twofold" not rechecked |
| B5 | Hancock, Mansfield, DarwinZDF42 | k = mu | sympy: limit s to 0 of Kimura u(p0) = p0, so k = 2N mu x 1/(2N) = mu | holds / accurate | credit |
| B5a | McCarthy | 450 billion; 22.5M; 20M; 35M | post: 100 x 1e4/20 = 50,000/yr; 4.5e11; 22.5M reproduces. Comment 337116873: "9 My / 25 = 360,000" but "50,000/yr" (a 20 y figure): 25 y throughout gives 16.0M, 20 y throughout 20.5M (stated 20.0M). Comment 340149310: 4e11/2e4 = **2e7, not 3.5e7** | **arithmetic-error (comment-level; the post figure holds)** / **accurate** | M03 is a plain slip (75% off; the 35M headline vs 180 is unaffected). M02 mixes two generation times; 2.4% from the 20 y reading, 20% from the 25 y reading. Prose also says "40,000 years" for 40,000 generations. His own 60 to 100 range with 97% non-deleterious gives 13.1 to 21.8M, so 22.5M uses the top of his range (it is Day's input) |
| B5b | Mansfield | 1 neutral fixation per generation from 2% of 100 | 2 per zygote x N = 2N; x 1/(2N) = 1 exactly; 450,000 over 450,000 generations (44.4x short of 20M); f needed 0.889 | holds / **partial** | credit: exact. The 44x is the illustration's own limit (he says the neutral share is "much higher"); the share needed (0.89) and McCarthy's 97% are both uncited. "genome only about 10 times" 200M is 15.5x, imprecise, immaterial |
| B5c | Hancock | 76.8; 38M | 6.4e9 x 1.2e-8 = 76.8 (diploid basis; corrected on screen to 38.4); 2 x 252,000 x 76.8 = 38.7M; retained 76 = 152/2 (98 to 206 range): 38.3M; SNV null 19.35M + ancestral 20.3M = 39.6M | holds / **partial** | first-pass basis slip was self-corrected (immaterial). The "38M matches 35 to 40M" is right on an event basis and a coincidence on an SNV basis (19M + about 20M, not 38M), conclusion survives. **Unit slip:** "407 per generation" divides Day's per-lineage 205M by both lineages' generations; per lineage it is 813, so the gap to 76.8 is 10.6x (the repo's harvest note says "about 5x"; Hancock's verbatim only gives 407). GG-12 ("account even for the highest end") cannot be assessed without the transcript |
| B5d | relayed geneticist (via Gutsick Gibbon) | 7.2M | 6e6/25 = 240,000; x 30 = 7.20M (7.56M at 6.3 My); 2.4x below 17.5M; Day's "7.2 < 410" = 1.8% | holds / **unverifiable** | arithmetic reproduces; the 30 per generation is uncited and relayed. Day's own B1a uses the same product |
| B5e | Nesslig20 | 2 x 75 x 252,000 = 37.8M | 37.8M; 18.9M if 75 is a zygote count; 75 is 1.95x the SNV pedigree haploid value 38.4; 1 to 2% of 3.1e9 = 31 to 62M | holds / **partial** | arithmetic reproduces. The basis of 75 is not stated ("per haploid genome" is defined; "100 to 200 per generation" is unlabelled and uncited). As a haploid event count (150 per newborn) it sits inside the 98 to 206 range Hancock cites; as SNVs it is 2x the pedigree rate. His own plot shows the 4Ne lag (N05) and he sets it aside |
| B5f | Dumb-and-Dumber | 9.7M; gap under 2 | 38.4 x 252,000 = 9.68M; 17.5/9.68 = 1.81; with his own lag (252,000 - 40,000 or - 132,000): 8.14M or 4.61M, gap 2.2x or 3.8x | holds / **accurate** | inputs match Day's s6 and s4.3. "well under 252,000" is loose for 132,000 (52%); he says the residual is largely closed by the ancestral-pipeline point. Immaterial |
| B5h | Hössjer | 7.6M | 3e9 x 0.45 x 1.25e-8 x 450,000 = 7.59M (gap 2.63); without d 16.9M (1.19x); G_neutral 2,174 ("2,170") | holds / accurate | reproduces. d is carried into the neutral supply and accounts for most of the gap; the step is not derived (C2 series) |
| B6 | Mansfield (formula is the hierarchy's) | pipe full at the split | E[d] = 2muT + theta_anc: 0.65% (Ne_anc 1e4), 1.24% (1.32e5), 1.56% (1.98e5) vs 1.23% observed | holds / n/a | the full pipe needs 4 Ne_anc generations before the split (4e4 to 7.9e5) |
| B6b | Camestros | all differences counted as post-split | Day 2019: 15M + 15M; CSAC fixed share 0.78 to 0.86 of 35M = 27.3 to 30.1M | holds / accurate | credit: qualitatively right (B4a quantifies) |
| B6c | Hancock | serial model predicts no variation | theta = 4 Ne mu = 4.8e-4 per site, 1.5e6 differences per genome pair | **holds** / n/a | reproduces; whether Day's model is serial is G1/F1a |
| B7 | critic reading of Day's own text | P_fix = 1/(2N) | martingale; exact chains | holds / accurate | credit |
| B7c | keruru | P_fix = 1/(2N_census) to 15 decimals | exact solves: max error 3e-15 (WF), 5e-16 (sweepstakes, Ne_var/N = 0.15) | holds / accurate | credit: the retraction is correct and I reproduced the exactness independently (his code not retrieved) |
| C5 | keruru | 4e-35 at p = 0.5; 6e-93 at 0.1; expected count near 1e-29 over a million loci | exact WF: **5.1e-45**; **5.9e-113**; at 0.9: 3.7e-8, 0.95: 2.2e-4, 0.99: 0.19; all loci at 0.5: 5.1e-39; uniform 0.1 to 0.5: 4.9e-41; uniform 0.1 to 0.9: 2.6e-4; uniform 0.1 to 0.99: 1.3e3 | **arithmetic-error (immaterial: direction conservative)** / pending | his per-locus value is 10 orders too large and "1e-29" is 1e6 x 4e-35. The conclusion (zero is expected unless loci start above about 0.9) holds, but the expected count is set by the frequency spectrum's top edge, not by a spectrum "starting from intermediate frequencies". The repo's own 1.2e-46 (Brownian, arcsine) was 41x too low; the repo number should be replaced by the exact one |
| C5b | keruru | Ne 8,139 (102 gens), 9,835 (250) | E[F] = 250/(2 x 9,835) = 0.0127; Ne = 2 gives 62.5 (saturated) | pending / n/a | arithmetic only; the estimator is C1d's, not rerun here |
| D8 | Day quoting Milton (unattributed) | 1e-65 "equivalent to winning the lottery every week for a thousand years" | 52,143 weekly wins of a 1-in-1.4e8 lottery = 10^-424,764; 1e-65 is 8.0 weeks; 20^50 = 10^65.05 | n/a / unverifiable | the analogy is off by about 420,000 orders of magnitude; rhetorical, author unidentified, no calculation depends on it. Not scored internal because the speaker is unclear |
| D14 | Davis (relaying Eden) | 1e36 transfers | 1/(1e-15 x 1e-21) = 1e36; population 1e36/(1e12 x 1e-6) = 1e30 | holds / accurate | relay is correct. Eden's "1e13 tons" needs 1e-11 g per cell (10x a typical E. coli, 1e-12 g); inputs unsourced and called "very rough" by Eden |
| E5 | Dumb-and-Dumber, KITTENS | -906 is not a count | same as A2c | **holds** / accurate | arithmetic reproduces; the estimator-artefact reading is external |
| F1 | Mansfield | latency vs throughput (trucks) | 20,000 x 1/20,000 = 1 per hour; 100 arrivals = 100 hours | holds / n/a | exact at steady state (full pipe, B6) |
| F1b | McCarthy | no one-at-a-time queue | as B5a (time-adjusted 20M) | holds / n/a | inherits M02 |
| F4 | Bowers (via Day) | u about 2s | Kimura u(N = 100, s = 0.01) = 0.02017; 2s = 0.02 | holds / accurate | credit (original review not found) |
| G1b | Samson (ally) | total/time = average | 205e6/252,000 = 813; 17.5e6/252,000 = 69.4 per generation | holds / n/a | |
| G2 | Hancock | serial reading | 252,000/1,400 = 180; /66,000 = 3.8; /20,000 = 12.6; /27,600 = 9.1 | holds / partial | reproduces; scope question is G1 |
| G2a | Ghijselen | marathon | 60,000 x 4 h = 240,000 h = 27.4 y | holds / partial | reproduces; applies to a latency division, not to G_f |
| G2b | Duffy | 180 | 252,000/1,400 = 180; 205e6/180 = 1,138,889 (paper 1,139,000x) | holds / accurate | |
| G2c | Hancock | serial predicts no variation | as B6c | **holds** / n/a | |
| G3 | McCarthy | specific vs any | supply 22.5M, sd 4,743, 20M is 527 sd below; (5e-5)^2e7 = 10^-86,020,600 | holds / accurate | credit: Day's 10^-86,000,000 is exact |
| G5 | Matev | CV falls, variance rises | n = 157,000, p = 0.5: Var 39,250, sd 198.1, CV 0.252%; at 2n Var 78,500, CV 0.178% | holds / n/a | credit |
| H5 | Hössjer (ally) | cost step 15,800 | Haldane window 450,000/300 = 1,500; 15,800/1,500 = 10.5; "650x" = 652 | non-sequitur (unchanged) / pending | arithmetic reproduces; the 15,800 is a rate scaling, not a cost computation (existing verdict stands) |
| H6 | Nesslig20 | 30 Ne/(0.1 Ne) = 300 | 300; T_fix(p) tends to 4Ne as p tends to 0 (sympy) | holds / partial | |
| ROOT-H | Hössjer (ally) | agrees after rescaling | composite of A5a, H5, B5h | see those | |
| ROOT-K | Keen (ally) | "orders of magnitude" beyond the age of the universe | 6.3e6 y x 1.075e6 = 6.77e12 y = 491 universe ages, if the shortfall is a time multiplier | pending / partial | no numbers in the preface; inherits A2e's premise |

## 5. Statements not in any claim file, recomputed (candidates for new claims)

| Source | Stated | Recomputed | Outcome |
|---|---|---|---|
| Nesslig20 s3.3 | conditional fixation-time CDF F(t) = 1 + sum (-1)^i (2i+1) exp(-i(i+1) t/(4Ne)); 50% at 3.48 Ne, 60.6% at 4 Ne, 95% at 8.19 Ne, 99% at 11.41 Ne, 99.9% at 16.01 Ne | series: 3.48, 60.6%, 8.19, 11.41, 16.01 (all match). Exact WF (2N = 1,000): F(3.48 Ne) = 0.502, F(4 Ne) = 0.608, F(8.19 Ne) = 0.950, F(11.41 Ne) = 0.990; mean = 4 Ne (telescoping series) | credit: correct |
| Nesslig20 s3.4 | the lag to a constant rate is "exactly 4Ne" | integral of (1 - F) = 4 Ne = 40,000; applied, 2 x 75 x 212,000 = 31.8M | credit: the post reproduces Day's B1a subtraction itself and sets it aside on standing variation |
| Nesslig20 s3.5 | G_f 444 and 23; 1/444 = 0.0023; mu L < 0.0046; 37.8M | 20,000/45 = 444; 13,500/593 = 22.8; 0.0023; 0.0046; 25/75 = 0.3333 (he writes 0.33) | reproduces; Barrick year printed 2019 where the link is the 2009 paper (typo) |
| Nesslig20 s1.1 | lottery n = 69,314,717; P = 0.86, 0.98, 0.51 | 69,314,717; 0.865; 0.982; 0.503 | reproduces; "0.51" should read 0.50 (rounding) |
| Nesslig20 Part II | 504 fused chromosomes = 1/500 x 252,000; P_fix = 1/Ne = 0.00005 | 504; 1/(2 x 1e4) = 5e-5 (1/Ne = 1e-4) | arithmetic fine; symbol slip; the 1/500 is a birth prevalence used as a new-mutation rate in k = mu. Used only as a reductio |
| Camestros [3] | "1500/35 = 429"; "1051 fixed mutations in Day's model"; fastest range 1,000; 1,600 consistent with 10 to 20 in 20,000 | 15,000/35 = 428.6 (numerator typo, result right); 450,000/428.6 = 1,050 (one off; d omitted, with d = 0.45: 472); 20,000/20 = 1,000; 20,000/12.5 = 1,600 | immaterial slips |
| Camestros [1]/[2] | F_max = t d/(g G_f); "the arithmetic itself isn't wrong" | 9e6 x 0.45/(20 x 1,600) = 126.6 | credit: concession reproduces |
| Mansfield | "genome only about 10 times" 200M | 15.5x | imprecise; immaterial |
| CSAC as read by Day, Hancock | "~5M indel events vs ~35M" | two-lineage total (GAP-07/07b; direct count 4.30M); not recomputed here | 40M = 35M + 5M is a total, 20M per lineage; Hancock's 76 events x 2 x 252,000 = 38.3M compares correctly to the 40M event total |

## 6. Known slips, confirmed or refuted

| Slip named in the brief | Verdict |
|---|---|
| McCarthy "400 billion x 1/20000 = 35 million" | **Confirmed** (2.0e7). Raw JSON checked. Immaterial: his post and his other comment give 20M. A second, previously unrecorded slip sits in the other comment (25 y vs 20 y, M02) |
| Hancock and Nesslig20 double-count the "38M match" | **Confirmed on an SNV basis, not an arithmetic error.** Post-split supply 2 mu T L = 19.35M plus ancestral polymorphism about 20M (Ne_anc 1.32e5) is 39.6M; the observed total contains both, so "38M from supply alone matches 35M" lands on the right value for the wrong reason. On an event basis (Hancock's retained 76) the comparison to the 40M event total is fine. Both authors flag part of the issue (Hancock cites the CSAC polymorphism sentence; Nesslig20 writes "not all of the differences ... are actually fixed") |
| Mansfield 44x shortfall; "1 per generation" | **Both confirmed, neither is Mansfield's error.** 1 per generation is exact (N cancels). The 44.4x is what his 2% illustration gives (450,000 vs 20M); he says the real share is "much higher", and 20M needs f = 0.89 at 100 per zygote |
| Nesslig20 "75 per haploid genome" | **Neither refuted nor confirmed.** Taken as haploid events it equals Hancock's 76 (150 per newborn, inside 98 to 206); taken as SNVs it is 1.95x the pedigree haploid value 38.4; taken as a zygote count the product is 18.9M. The post does not decide |
| the rate route comes out about 2x low | **Confirmed.** 38.4 per haploid generation gives 19.35M = 0.55 of the 35M SNV total (1.8x low); the fossil-calibrated rate is 2.03x pedigree (keruru's "twice" reproduces); adding theta_anc (20.3M) brings the null to 39.6M, so the factor 2 is the ancestral term |
| keruru 1e-29 vs repo 1e-46 | **Both wrong, in different directions.** Exact WF at p = 0.5, 240 generations: 5.1e-45 (keruru's 4e-35 is 10 orders too high; the repo's 1.2e-46 is 41x too low). The million-locus 1e-29 is 1e6 x 4e-35 (all loci at 0.5); the exact figure for that spectrum is 5e-39, and a spectrum reaching 0.9 gives 2.6e-4 |
| CSAC "5M" | **Resolved elsewhere** as a two-lineage total (GAP-07/07b); not recomputed |

## 7. Immaterial slips vs slips that carry an argument

**Immaterial (no conclusion changes):** McCarthy 35M (A: 20M elsewhere in the same thread) and 690 vs 674; Mansfield "about 10 times" (15.5x); Hancock "4e-5" for 4.6e-5, his self-corrected diploid 76.8, and the "38M" that needs the event reading; Nesslig20 0.51 for 0.50, 0.33 for 0.3333, "1/Ne" for "1/(2Ne)", the Barrick year; Camestros 1500 for 15,000 and 1051 for 1050; KITTENS 94,000 for 91,600 (2.6%); Hössjer 125 x 127 = 15,875 printed 15,800; keruru's inconsistent Ne/N ratio in a draft that flags "[CHECK]"; Milton/Day lottery analogy (rhetorical, author unclear).

**Slips that carry (part of) an argument, none reversing a conclusion:**
1. **keruru C5, 10 orders too large** (and the integrated 1e-29). The conclusion survives, but the stated *mechanism* (the count is tiny because loci start at intermediate frequency) depends on a spectrum he does not state: for any spectrum reaching 0.9 the expected count is 1e-4 or more. This is the quantity C1, C1b and C1c actually test.
2. **Hancock's bacterial rate 1e-11** (8.9x below the measured 8.9e-11). It carries the sub-argument that the LTEE's 1,322 generations per fixation is far from neutral-limited (22,000 vs 1,322, 17x). At the measured rate the neutral expectation is 2,439, only 1.8x slower than observed, which is closer to Day's view that hitchhiking neutrals are inside G_f (A2e, E1). The larger argument (human supply) is not touched.
3. **Hancock's treatment of Day's 205M as a two-lineage total** (A3d, the 407 per generation, the harvest note's "about 5x"). Day's text apportions symmetrically, so the gap on an event basis is 10.6x, not about 5x. The slip understates the gap against the critic's own interest, and it does not affect the shortfall ratio.
4. **Nesslig20's basis of 75** (2x). It sets whether the 37.8M is 37.8M or 18.9M and whether it "matches" 35M. It is flagged in the balance ledger already.
5. **McCarthy's 25 y / 20 y mix** in the time-adjusted 20M: 2.4% under the 20 y reading (Day's book inputs), 20% under the 25 y reading. His "exact correct result" is exact only on the 20 y reading, which is the reading Day's own 9 My / 20 y inputs imply.

## 8. Claim files with no number or derivation (not recomputed)

A2i (logic only: X = A x B), A4b, A5f, B4e, B4f, B5g, D1, D1a, D1b, D1c, D1d, D13, D15, E1, G1c, G2d, G2e, G2f, G3a, ROOT-DE, ROOT-T (21). For B4e and B4f the claim is that the dates are circular with the clock; that is logic plus literature, covered by B4 and B4a. D15 states a prediction with no parameters.

## 9. Suggested verdict changes (for the lead; no claim file edited)

| Claim | Now (internal / fidelity) | Suggested |
|---|---|---|
| B5a | holds / n/a | **arithmetic-error** (comment-level, M02 and M03; the post's 22.5M holds) / accurate |
| F1b | holds / n/a | holds, comment "inherits B5a M02" |
| C5 | pending / pending | **arithmetic-error** (immaterial, conservative direction) / pending; replace the repo's derived 1.2e-46 by the exact 5.1e-45 |
| B5c | holds / n/a | holds / **partial** (205M per lineage; 407 per generation) |
| B5e | holds / n/a | holds / **partial** (basis of 75 unstated, uncited) |
| B5b | holds / n/a | holds / partial (100 per zygote and the neutral share are uncited) |
| B5d | holds / n/a | holds / unverifiable (relayed, 30 per generation uncited) |
| B5f | holds / n/a | holds / accurate |
| A5c | holds / n/a | holds / **partial** (1e-11 vs 8.9e-11) |
| A5 | holds / n/a | holds / accurate |
| B4g | pending / unverifiable | **holds** / unverifiable |
| B6c, G2c | pending / n/a | **holds** / n/a |
| E5 | pending / accurate | **holds** / accurate |
| D8 | n/a / unverifiable | n/a (record the analogy mismatch; author unidentified) |
| H5 | non-sequitur / pending | unchanged |

Policy question for the lead: a slip the author corrected on screen in the same source (Hancock 76.8) is recorded here as `holds` plus a comment. If the rule is "every uncorrected stated number that fails", then Hancock's final numbers pass, McCarthy's 35M and the keruru probabilities fail. Apply the same rule to Day's slips. One is currently logged only on the critic side: s6.4's 38,400 (and the 3,840 deleterious, 0.02 and 1e-17 figures built on it) is the target of A2h, which is itself `holds`; the Day-side node A5d carries `non-sequitur` for a different reason, so no Day node records this arithmetic-error. The text read here (Z23003785, modified 2026-10-04) still prints 38,400.

## 10. Who this helps

**Critics and allies (credited first).**
- The core identities hold exactly: k = mu (sympy, and exact chains), P_fix = 1/(2N_census) to 3e-15 in a Wright-Fisher and a sweepstakes model, and Matev's N/Ne reductio (the sum over 2N copies must be 1). keruru's retraction is correct, and independently reproduced.
- Specific critic catches are correct: Dumb-and-Dumber's 3,840 (Day's s6.4 prints 38,400, confirmed in the raw text); the Reddit reconstruction of Day's 410M as 2 x 187 + 35 = 409M; Camestros's "average, not the fastest" (Day's own table has 8.5x to 17x faster rates), his "the arithmetic itself isn't wrong", and his all-post-split reading of Day's 2019 count (27.3 to 30.1M fixed SNVs at CSAC's share); Matev's variance and CV statement (39,250; 0.252%); Bowers's 2s (u = 0.02017 at N = 100, s = 0.01).
- The longest critic derivation, Nesslig20's Part I, reproduces almost entirely (CDF percentiles agree with an exact Wright-Fisher recursion to 0.002; the 4Ne lag; the lottery and G_f arithmetic). Mansfield's 1 per generation is exact; McCarthy's 22.5M and 527-sd statement reproduce; KITTENS's decomposition reproduces to 2.1%; Hössjer's chain reproduces (127, 15,800, 10.3M, 7.59M).
- 34 of 45 numeric claims reproduce with no flag; slips cluster in inputs and units, are small, and often run against the arguer (Hancock's 205M halving understates the gap).

**Day (credited too).**
- The strict count is not zero: McCarthy's 35M, his 25 y / 20 y mix, and keruru's probabilities (off by 10 orders though conservative) are arithmetic slips by the rebutters. Day's reply that critics sometimes use sloppy numbers has support in these rows.
- Hancock misreads the unit of Day's 205M (Day's text is explicit: apportioned symmetrically), so Day's "MITTENS counts per lineage" (A3d) is confirmed by the text. Hancock's bacterial mutation rate is 8.9x below the measured LTEE value; at the measured rate the neutral expectation (2,439 generations) is close to the observed 1,322, which weakens the "the LTEE is nowhere near neutral" point and fits Day's hitchhiker reading.
- The critics' headline illustrations are weaker than their phrasing: Mansfield's 1 per generation is 44x short of 20M unless the neutral share is about 0.9, a share nobody cites except McCarthy's uncited 3% deleterious figure. keruru's "1e-29" is a stated spectrum-free number that depends on the spectrum's top edge.
- Hössjer carries Day's d into a neutral supply (which accounts for most of the 2.63x gap); the ally result is therefore less independent than its framing, and H5 stays non-sequitur.

**Neither side.** The "38M matches 35M" is a double count on an SNV basis (post-split 19M plus ancestral about 20M); it does not hurt the critics' conclusion (the correct null, 39.6M, still reaches the observed total) and does not help Day's B6a ("ancestral polymorphism is a rounding error": it is half). The audit's own earlier C5 number (1.2e-46) was 41x too low and is corrected here.

**Does this close the balance gap?** Partly. Under the strict standard the internal-verdict count on critics and allies moves from 0 to 2 arithmetic-error suggestions (plus the existing H5 non-sequitur), against 22 of 112 for Day. The denominators are not comparable: Day's 112 include long derivations with many steps, while most critic claims are one-line identities. A like-for-like rate needs the number of numeric Day nodes, which was not computed here. What X1 establishes is that critic-side errors exist and are recorded; that they live mostly in fidelity (basis, unit, uncited inputs); and that no critic claim recomputed here fails as badly as the Day-side verdicts A3a, A5e, G1a, C6.

## 11. Limits

- Hancock's video: auto-caption quotes only; GG-12 and the "5x" cannot be tied to the full sentence. Bowers's original, McCarthy's paid posts (only free repost and comments), the Gariepy debate and Day's book are not available, so those rows use the harvested quotes. Camestros posts were searched for arithmetic, not read end to end; Myers, Tipler, Del Arroz and Tree of Woe carry no numbers. Matheson 2025 (cited by Nesslig20) was not read.
- Hössjer's own d-in-the-neutral-supply step and the Haldane step are the repo's existing findings; not re-derived.
- Predictions that lean on claim-file arithmetic are marked `[cf]` in the docstring (40 of 67) and are not independent; 26 are marked `[new]`, including all the exact-chain ones.
- The exact Wright-Fisher value for keruru's p = 0.5 changes with M at fixed t/(2N); I report the value at the stated 2N = 20,000 (5.1e-45) and the trend (3.2e-45 at 2N = 40,000).
