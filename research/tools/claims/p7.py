from gen import *
Z3='[MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04)'
Z5='[LTEE fixation data paper, Zenodo 23105291](https://zenodo.org/records/23105291) (key Z23105291), 2026-10-02'
NSL='[They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (key B2026-10-01-they-never-stop-lying), blog, 2026-10-01'
SNK='[Snikker-Snak](https://voxday.net/2026/10/01/snikker-snak/) (key B2026-10-01-snikker-snak), blog, 2026-10-01'
MT='[Math Teacher Can’t Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (key B2026-09-30-math-teacher-cant-math), blog, 2026-09-30'
IC='[An Inspiring Critique](https://voxday.net/2026/01/27/an-inspiring-critique/) (key B2026-01-27-an-inspiring-critique), blog, 2026-01-27'
EDU='[The Education of a Population Geneticist](https://voxday.net/2026/10/01/the-education-of-a-population-geneticist/) (key B2026-10-01-the-education-of-a-population-geneticist), blog, 2026-10-01'
HAN='[Gutsick Gibbon and Zach Hancock, "No, Vox Day\'s AI-Generated Books Did Not Debunk Evolution"](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03'
F1='Linked result: F1 (research/checks/RESULTS.md, seed 31, N = 1000, s = 0.01, U_b = 0.01, independent loci, no interference, no cost): predicted steady-state rate 0.3960 per generation, simulated 0.3972 ± 0.0018; t_fix = 847 generations but G_f = 1/rate = 3 generations; in-transit count ≈ 336, computed from Little\'s law (not measured). Review #3 caveats: the regime is unrealistic (20 new beneficial mutations per generation), so pipelining is shown to be possible, not feasible; feasibility is the F2/H question.'

claim('G1','average-rate-includes-parallelism','An average rate is indifferent to parallel versus sequential timing; the LTEE G_f already includes parallel fixation','day','G','A',
 [('supports','A'),('depends-on','A2')],False,'firsthand','checked',('holds','n/a','contested'),
 q('The 1,322 gen/fix rate is not a sequential rate that needs to be divided by a parallelism factor. It is the total throughput, the net output after parallel fixation, clonal interference, sweep displacement, and every other concurrent dynamic has played out.',Z3+', p.13 (s8.1).')+'\n'+
 q('If you drove ten miles and it took you an hour, then it makes no difference if you were driving sixty miles an hour part of the time or you were stopped part of the time, or even if you turned around and drove back home to pick up something you forgot.',SNK+', ¶9. Day is defending a quoted commenter: "When dealing with average rates, it really doesn\'t matter if particular fixations happen parallel or in sequence."'),
 '''G_f = (generations in window)/(fixations in window) = T_obs / n_obs, an inverse throughput. F_max = T/(g_len·G_f) uses only the ratio; overlaps in time do not enter. This is true for any measured average rate over a window (`glossary.md`: G_f read as a latency is the confusion; G_f as throughput is the stated definition).

`derived:` (python3 -I) How "parallel" is the LTEE count? Z23105291: 5,496 whole-population fixations in 723,000 population-generations: 723,000/12 = 60,250 gens per population. Pooling all twelve populations gives 723,000/5,496 = 131.6 population-generations per fixation, a different quantity from the per-population G_f = 60,000/45.4 = 1,322 applied to one lineage. Averaging per-population rates over twelve independent populations does not add parallelism within one lineage; only overlap of sweeps inside a population counts. Day\'s argument in [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (blog, 2026-10-01) ¶22 ("the math is an average of 12 different populations … built into the structure since it utilizes 12 completely separate populations all running simultaneously in parallel. That’s not how real-world species work.") concedes this about real species.''',
 '- Stated: G_f is measured, aggregate, post-parallelism, post-interference.\n- Implicit: the degree of parallelism available in the measured system (within-population overlap of sweeps) equals that available to the target system; the rate is transferred unscaled (A2e, A5). The counting rule matters (A2b).',
 '''- Against: Hancock (G2) and Myers, Bowers, Dumb-and-Dumber (RE-01) read the formula as sequential; Camestros (G2d) says "Generations per fixation" reads like one at a time. Day\'s own blog (Appendix A passage, G2g) says "Therefore fixation must be sequential" and applies 180 = 252,000/1,400.
- In support: Camestros concedes the figure is an average (G1c); Samson (G1b); Duffy (DU-03): "the number he\'s using in the math is already parallel fixation."; the F1 result shows that an observed throughput is not a latency division.
- Weaknesses in the responses: the critics\' strongest version is not that the average is miscomputed but that it is applied to a system with a different capacity for parallelism (A5f). Day\'s own blog reports zero parallel fixation events inside Ara+2 over 60,000 generations (G1a), while s8.1 describes "overlapping sweeps at dozens of loci": the two descriptions are not reconciled. Day\'s s8.2 and Appendix D use the interval form (time/fixation-time) for drift and for the human-derived rate (A5e).''',
 LITH+'''| Good et al. 2017 | "multiple beneficial variants simultaneously competing for dominance in each population" | verified (abstract); supports within-population overlap |
| Good et al. 2017 | trajectories "inconsistent with a “periodic selection” model in which individual driver mutations fix in a sequence of discrete selective sweeps" | verified |''',
 F1+'\n- Under Day: G_f is a throughput; transfer is a separate question (A5). Under critics: any serial reading is a latency division (G2), which F1 shows is not a throughput bound. Both sides agree on the logic of averages; the verdict turns on A5f.',
 'Link: `research/checks/RESULTS.md` F1. Arithmetic audit (python3 -I, scratch). Review: pending.', '- Output separation: per-generation fixation rate (throughput) vs per-allele fixation time (latency); in-transit count measured directly (TODO in F1).')

claim('G1a','ara-plus-2-no-parallel','Day: in Ara+2, 66 fixations were 14 fixation events, all sequential; zero parallel fixations in any LTEE population','day','G','G1',
 [('depends-on','G1')],False,'firsthand','checked',('arithmetic-error','n/a','contested'),
 q('There were 14 fixation events and every single one of them was sequential. The smallest gap between fixations was 1,500 generations. The largest gap was 9,500 generations.',SNK+', ¶12.')+'\n'+
 q('Each selective serial fixation carried along an average of 5.3 neutral mutations to fixation with it.',SNK+', ¶13.'),
 '''Ara+2: 66 fixations (Z23105291 Table 1: 66 in 60,500 gens; blog: 66 in 60,000, 909 gens/fixation); 14 sweep events; claimed 5.3 hitchhikers per event.
`derived:` (python3 -I) 66/14 = 4.71 fixations per event, i.e. (66 − 14)/14 = 3.71 hitchhikers per event; 5.3 x 14 = 74, not 66; 66/5.3 = 12.5 events. The claim of 5.3 neutral mutations per selective fixation does not reconcile with 66 and 14 (unless 5.3 is an average over all populations, which the sentence does not say). 60,000/14 = 4,286 gens per sweep event in Ara+2; compare 909 per fixation (all-cause) and the blog\'s "SERIAL natural selection rate … ~24,500" (A2f) and 4,615 (A2f).
Definition used: two fixations are "parallel" if they occur in the same 500-generation slice; sweeps whose fixation times are ≥1,500 generations apart can still overlap in time during their rise.''',
 '- Stated: data in 500-generation slices.\n- Implicit: "parallel" means fixation events in the same time slice, not overlapping sweeps.',
 '''- Against: s8.1 of Z23003785 (Day\'s own paper, three days earlier): "The 45.4 fixations … were not fixed one at a time in strict sequence. They were fixed in parallel, with multiple sweeps competing and completing simultaneously." Good 2017: "multiple beneficial variants simultaneously competing for dominance in each population". The two Day statements (s8.1 vs blog 2026-10-01) differ on whether within-population parallelism occurred.
- In support: none from critics; the claim is Day\'s empirical report from public data.
- Weaknesses in the responses: no critic has recounted Ara+2; the repo does not have the 500-generation slice data; the 5.3 does not reconcile as stated.''',
 LITH+'''| Good et al. 2017 | "The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4)" | verified |
| Tenaillon et al. 2016 | "Some others-including Ara-4, which became hypermutable, and Ara+2, which did not-are more linear in structure, without deep branches among the sequenced clones." | verified; consistent with serial sweeps in Ara+2 |''',
 'Not run. Prediction (Day): recounting Ara+2 from the Good 2017 trajectories gives 14 events and ≥1,500-generation gaps. Prediction (critics): sweep durations exceed the gaps, so the sweeps overlap in time. Result that would change a verdict: sweep-interval overlap computed from the trajectories.',
 'Arithmetic audit (python3 -I, scratch). Raw trajectories not in repo. Review: pending.', '- Counting of overlapping sweeps vs fixation-time gaps in the LTEE preset.')

claim('G1b','samson-total-over-time','Samson (ally): the total number of mutations separating species includes all of them, parallel or sequential; total divided by time is the rate','ally','G','G1',
 [('supports','G1')],False,'firsthand','extracted',('holds','n/a','n/a'),
 q('The total number of mutations separating species includes all of them. Parallel, sequential, or however else. Hence the word “total”.','[Uncle John’s Band, "Not a Chance"](https://unclejohnsband.substack.com/p/not-a-chance), 2026-01-24, para 20 (UJ-01).')+'\n'+
 q('And dividing “total” by “amount of time” gives a simple, unweighted average number. The rate.','same post, para 20 (UJ-02).'),
 'Observed divergence D over time T gives an average realised rate D/T regardless of how events overlapped. `derived:` 205e6/252,000 = 813 per generation (both lineages combined 1,627); 17.5e6/252,000 = 69.4 per generation per lineage. These are the average rates that the evolutionary process must have realised, whatever the pipeline structure.',
 '- Stated: all differences are counted, no matter how they arose.\n- Implicit: the realised average required rate says nothing about whether the achievable rate (G_f-based) can match it.',
 '''- Against: the quote file notes: an observed average divergence rate is not an upper bound on achievable rate. That is, the realised average (69 per generation) is a requirement, and the question of whether it can be met is the A5/A2e question.
- In support: it is correct that required count over time is an average whatever the overlap structure; Day uses the same point (G1).
- Weaknesses in the responses: it supports only the accounting identity, not the transfer of LTEE G_f.''',
 NOLIT, 'No prediction; accounting identity.', 'Arithmetic audit (python3 -I, scratch).', '- Display required average rate per generation next to achievable rate.')

claim('G1c','camestros-average-concession','Camestros concedes that Day\'s G_f was calculated as an average, not as a time for an individual mutation','critic','G','G1',
 [('supports','G1')],False,'firsthand','extracted',('holds','n/a','n/a'),
 q('He is correct that when he calculated the number it was an average. It isn’t intended to be a time for an individual chromosome.','[Camestros Felapton, Reading Vox Day 2026 [5]](https://camestrosfelapton.wordpress.com/2026/01/29/reading-vox-day-so-you-dont-have-to-2026-5/), 2026-01-29, para 9 (CA-10).'),
 'Concession on definition: G_f = T/n (throughput), not a per-allele fixation time.',
 '- Stated: the number was an average.\n- Implicit: the concession does not extend to the application (the same post says in CA-11 that an average is not the fastest rate; A2d).',
 '''- Against: Camestros (CA-05, G2d) says the term "reads as if" it means one at a time.
- In support: Day (G1).
- Weaknesses in the responses: this is a concession on definition, made in January 2026 on the first-edition arithmetic; it does not address MITTENS 3.0.''',
 NOLIT, 'No prediction.', 'No script.', '- None.')

# ---- G2 serial critique family
claim('G2','serial-critique-hancock','Hancock: the formula assumes each mutation must arise and go to fixation before the next can occur','critic','G','A',
 [('attacks','A'),('attacks','G1')],False,'firsthand','checked',('pending','partial','contested'),
 q('it assumes that each mutation has to both arise and go to fixation before the next mutation can occur.',HAN+', t=01:31:58 (GG-01; auto-caption).'),
 '''Serial reading: N_fix(T) = T / t_fix where t_fix is the time for one allele to fix. Aggregate reading: N_fix(T) = T/G_f, G_f = observed T/n. The two coincide only if fixations do not overlap.
`derived:` (python3 -I) 252,000/1,400 = 180 (Duffy, DeDzjang); 252,000/66,000 = 3.8 and 252,000/20,000 = 12.6, the "4–13 neutral fixations" in Z23003785 s8.2 (a time/fixation-time division for drift); 252,000/27,600 = 9.1 (A5e).''',
 '- Stated: sequential waiting.\n- Implicit: that Day\'s G_f is a per-allele fixation time. Day\'s papers define it as a measured throughput (G1).',
 '''- Against (Day): [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (blog, 2026-10-01) ¶4: "No, literally none of my math assumes serial fixation. Not MITTENS …"; Z23003785 s8.1.
- In support: Day\'s own statements that read as serial (Appendix A passage "Therefore fixation must be sequential … yields 180 fixations", G2g; blog 2019 "average fixed mutation propagation time", GA-02; Q&A "t ≈ 19,800 generations per fixation", s8.2 4–13 neutral fixations; s8.6 "one fixation per 27,600 effective generations"). KITTENS §11: "§8.2 and Appendix D revert to the interval form for drift."
- Weaknesses in the responses: Hancock\'s statement is about MITTENS as presented by Duffy (MITTENS 2.x with 180); the video answers the Duffy version of 22 Sep, not MITTENS 3.0 (balance ledger). Day says the 3.0 rate is already a throughput. Neither side has measured within-population overlap (G1a).''',
 LITH+'''| Good et al. 2017 | "inconsistent with a “periodic selection” model" | verified |''',
 F1+'\n- Result applied: as logic, dividing elapsed time by fixation latency is not a throughput bound (F1 verdict). Whether MITTENS does so is a reading question (G1 vs G2g); the repo has no check that settles it.',
 'Link: `research/checks/RESULTS.md` F1. Review: pending.', '- Toggle: serial (T/t_fix) vs aggregate (T/G_f) in F_max.')

claim('G2a','marathon-analogy','Marathon analogy: 60,000 runners x 4 h = 240,000 h only if run serially; mutation and fixation run in parallel','critic','G','G2',
 [('attacks','G2g')],False,'firsthand','checked',('holds','partial','n/a'),
 q('Of course you say that\'s not possible, they run parallel. Well, the same goes with mutation and fixation.','[Jan Ghijselen, "Will Duffy\'s math on Gutsick Gibbon\'s channel."](https://www.youtube.com/watch?v=nTVRiEcswI8), 2026-09-28, t=00:03:52 (DZ-01; auto-caption).')+'\nDay\'s transcription of the argument: [Math Teacher Can’t Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (blog, 2026-09-30), ¶6: "It would mean that if you have the Marathon of New York with 60,000 participants and an average length of 4 hours per marathon. If you would follow this reasoning, it would take on average 240,000 hours for the marathon to end."',
 '''60,000 x 4 h = 240,000 h = 10,000 days = 27.4 years (python3 -I; DeDzjang says "27 years"). Reconciles. The serial division is wrong for parallel events; the analogy applies to any calculation of the form (time)/(latency).''',
 '- Stated: events overlap in time.\n- Implicit: the criticised calculation divides time by latency.',
 '''- Against (Day): [Math Teacher Can’t Math](https://voxday.net/2026/09/30/math-teacher-cant-math/) (blog, 2026-09-30) ¶7: "The math is not wrong because parallel fixation is clearly and specifically included in the calculation." (i.e., Day\'s G_f is not a latency).
- In support: Day\'s s8.2 and A5e calculations that do use fixation time as an interval (G2 responses).
- Weaknesses in the responses: DeDzjang himself says in comments that he is "not schooled on this subject" and that "he rejects parallel fixation on shaky grounds" (said of Day); the analogy is valid logic but its application to G_f as defined is exactly what G1 disputes. He says a fuller treatment needs stochastics but gives none.''',
 NOLIT, F1, 'Link: `research/checks/RESULTS.md` F1; arithmetic audit (python3 -I, scratch).', '- None beyond G2.')

claim('G2b','duffy-180-arithmetic','Duffy: 180 total fixed mutations is all there is time for (252,000 generations / 1,400 per fixation)','ally','G','A',
 [('supports','A')],False,'firsthand','checked',('holds','accurate','contested'),
 q('180 total fixed mutations is all there\'s time for using the fastest rate of mutational fixation ever observed in any organism','[Gutsick Gibbon, Will Duffy livestream, Human Evolution #2](https://www.youtube.com/live/6jXiwrcC5PQ), 2026-09-22, t=00:29:42 (DU-02; auto-caption).')+'\n'+
 q('The length of a generation for humans is 25 years times 1,000 400','[Jan Ghijselen video](https://www.youtube.com/watch?v=nTVRiEcswI8), 2026-09-28, t=00:00:44 (DZ-02; auto-caption). The arithmetic he restates: 6.3e6/25 = 252,000; /1,400 = 180.'),
 '''252,000/1,400 = 180 exactly (python3 -I). 1,400 is the book\'s G_f (Z23003785 s3.3; the 3.0 paper replaces it with 1,322 → 190.6). Table s7.2 row "Book\'s original (1,400)": 180 achievable, shortfall 205e6/180 = 1,138,889 (paper: 1,139,000×; reconciles).
"Fastest rate … observed in any organism": see A2d; the LTEE point-mutator populations run faster (43–183 gens/fixation).''',
 '- Stated: the book\'s G_f and generation count.\n- Implicit: d = 1 in this worked arithmetic (balance note: Duffy presents the overlapping-generations point as a separate flaw).',
 '''- Against: Hancock (A3d, factor of two); the "fastest observed" wording (A2d); G2a (serial division).
- In support: the arithmetic is verified by an opposing critic (DeDzjang, DZ-02).
- Weaknesses in the responses: Duffy says he is "not a mathematician" and "not certain he’s right" (DU-04); the 180 figure uses a G_f that Day has since replaced.''',
 NOLIT, 'Arithmetic only.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Preset: "book 2026-01" (1,400, 252,000).')

claim('G2c','hancock-no-variation-prediction','Hancock: a strictly serial model predicts almost no genetic variation among individuals, unlike observed polymorphism','critic','G','G2',
 [('attacks','G2')],False,'firsthand','extracted',('pending','n/a','pending'),
 q('there would basically be no genetic variation amongst individuals except for the mutation that\'s increasing in frequency',HAN+', t=01:33:59 (GG-13; auto-caption). Same passage (t=01:37:07): the model "makes a specific prediction about levels of polymorphism in the natural world, about the shape of the site frequency spectrum" which "doesn\'t bear out".'),
 '''Prediction of a strictly serial sweep model for segregating variation, as stated by Hancock. Not formalised. A formulation would require the sweep rate r (per generation per genome), sweep duration, and recombination: under free recombination, neutral diversity at unlinked sites is set by mutation-drift balance θ = 4Neμ and is reduced by sweeps only at linked sites. That expectation is a standard-theory statement, not tested in the repo.''',
 '- Stated: one rising allele at a time.\n- Implicit: that variation is generated only by the rising allele (neglects standing neutral variation) and that Day\'s model is strictly serial, which Day denies (G1, Gc: 230 simultaneous sweeps).',
 '''- Against (Day): his models are not strictly serial (Gc, G1); the Bernoulli paper itself models ~230 simultaneous sweeps.
- In support: Z23003785 s8.2: neutral drift is "off" and hitchhiking carries neutrals, which would reduce variation; no polymorphism data are shown by Day.
- Weaknesses in the responses: no polymorphism data are in the repo; the claim is the speaker\'s experience ("as someone that has measured a lot of sight frequency spectrums" (auto-caption spelling)), not a calculation; Day\'s models differ from the strict serial case Hancock describes.''',
 NOLIT,
 'Proposed check G2c-sim (not run): forward simulation with sweep rate 1/1,322 per genome per generation (LTEE-rate) and free recombination; measure neutral heterozygosity at unlinked sites vs θ.\n- Under Hancock: diversity near zero only if sweeps are strictly one at a time with genome-wide linkage; under free recombination expect θ.\n- Under Day: nothing predicted.\n- Result that would change a verdict: heterozygosity <10% of θ under free recombination at the stated sweep rate.',
 'Script: none yet. Review: pending.', '- Neutral diversity output; sweep rate; recombination.')

claim('G2d','camestros-wording-reads-serial','Camestros: "Generations per fixation" reads as if each fixation must occur one at a time','critic','G','G2',
 [('attacks','G1')],False,'firsthand','extracted',('holds','accurate','n/a'),
 q('It will cause him problems though because “Generations per fixation” reads as if he means each fixation must occur one at a time.','[Camestros Felapton, Reading Vox Day 2026 [2]](https://camestrosfelapton.wordpress.com/2026/01/25/reading-vox-day-so-you-dont-have-to-2026-2/), 2026-01-24/25, para 28 (CA-05).'),
 'Interpretive point about terminology (`glossary.md`: G_f read as a latency is the named confusion).',
 '- Stated: reading of the label.\n- Implicit: nothing numerical.',
 '''- Against (Day): G_f is an average throughput (G1); Camestros concedes it (G1c).
- In support: Day\'s vocabulary alternates between "fixation time" and "generations per fixation" for the same words: 2019 post: "average fixed mutation propagation time" for 1,600 (GA-02); Q&A: "t ≈ 19,800 generations per fixation" for a Kimura fixation time (Q44); s8.6: "calculated … using Kimura\'s fixation time formula … one fixation per 27,600 effective generations".
- Weaknesses: a terminology point does not decide the maths.''',
 NOLIT, 'No prediction.', 'No script.', '- Label outputs as "generations per fixation (throughput)" and "fixation time (latency)".')

claim('G2e','myers-massively-parallel','Myers: evolution is a property of populations and involves massively parallel action on many traits and individuals','critic','G','G2',
 [('attacks','G2g')],False,'firsthand','extracted',('pending','partial','pending'),
 q('This is not how evolution works. Evolution is a property of populations and involves massively parallel action on multiple traits and individuals at once.','[PZ Myers, "Vox Day’s amazing ego, and Bill Dembski don\'t care"](https://freethoughtblogs.com/pharyngula/2026/10/02/vox-days-amazing-ego-and-bill-dembski-dont-care/), 2026-10-02, para 5 (PZ-01).')+'\n'+
 q('My criticism was that his math was invalid and that he thinks evolution is a simple serial process (the same thing Zach Hancock pointed out)','[PZ Myers, "Vox Day responds to my criticism…"](https://freethoughtblogs.com/pharyngula/2026/10/04/vox-day-responds-to-my-criticism-of-his-refutation-of-evolution/), 2026-10-04, para 2 (PZ-05).'),
 'No numbers given. Qualitative statement of the parallel-action premise.',
 '- Stated: population-level parallel action.\n- Implicit: that Day\'s math is serial (G2).',
 '''- Against (Day): [They Never Stop Lying](https://voxday.net/2026/10/01/they-never-stop-lying/) (blog, 2026-10-01) ¶4, ¶19, ¶22: parallelism is built into G_f.
- In support: Good 2017: "multiple beneficial variants simultaneously competing for dominance in each population".
- Weaknesses in the responses: Myers says "Even worse, 7 of those citations are to the LTEE, and contradict his conclusions" (PZ-03, a citation-count claim not checked here); no calculation; Myers states elsewhere that he is "not a population geneticist" (PZ-06). The post addresses the paper as published 2026-10-02, before Day\'s clarifications of ¶22.''',
 NOLIT, 'No prediction.', 'No script.', '- None.')

claim('G2f','bowers-serial-lottery','Bowers (as reposted by Day): treating evolution like a serial lottery is a category error','critic','G','G2',
 [('attacks','G3')],False,'secondhand','extracted',('pending','n/a','pending'),
 q('Treating it like a serial lottery is a category error.','[Day repost of Bowers review, "A Critical Review of Probability Zero"](https://voxday.net/2026/03/04/a-critical-review-of-probability-zero/), 2026-03-04, para 4 (BO-02). Bowers\' words, secondhand through Day\'s repost.'),
 'Qualitative (no numbers). Day\'s point-by-point reply (same page): "Point 2 claims I model beneficial mutations as neutral drift events with fixation probability 1/N … The reviewer has confused fixation probability with fixation rate." and "Point 3 invokes recombination as a rescue. The Bernoulli Barrier paper addresses this directly and at length."',
 '- Stated: events are not independent serial draws.\n- Implicit: Day multiplies per-event probabilities (Ga).',
 '''- Against (Day): the reply above; BO-04: "Not a single calculation." (accurate: the seven points contain no numbers).
- In support: Ga multiplies p^n for a pre-specified set.
- Weaknesses in the responses: the Bowers text is quoted only as reposted; the review contains no arithmetic; Day\'s reply cites Kimura & Ohta 1969 for recombination independence (A5f: misattribution).''',
 NOLIT, 'No prediction.', 'No script.', '- None.')

claim('G2g','appendix-a-fixation-must-be-sequential','Day (Appendix A, quoted in his blog): the Bernoulli Barrier rules out parallel fixation, therefore fixation must be sequential, and sequential gives 180 against 205 million','day','G','G',
 [('supports','A')],False,'firsthand','checked',('non-sequitur','n/a','contested'),
 q('Therefore fixation must be sequential. And sequential fixation is empirically falsified: the fastest rate ever measured in any organism, applied to the most generous generation count, yields 180 fixations where 205 million are required.',NSL+', ¶24 (Day quotes a passage he says is from Appendix A and "different, non-MITTENS math"). The book text itself was not checked.')+'\n'+
 q('Now, perhaps I could have worded it better, but the statement is nevertheless correct because the all-cause rate is obviously faster than a sequential rate.',NSL+', ¶25.'),
 '''Logical form quoted by Day: (Bernoulli Barrier: p^n ≈ 10^−34,000,000, so parallel fixation is impossible) ∧ (Averaging Problem: polygenic rescue impossible) ⟹ fixation sequential ⟹ N_fix = 252,000/1,400 = 180 versus 205e6. `derived:` 252,000/1,400 = 180 ✓ (the 1,400 is the book\'s G_f; 3.0 uses 1,322, i.e. 190.6). The p^n in the quoted passage is for n = 2e7 (Ga); the requirement in the same sentence is 205 million: different n.
In ¶25 Day states the 180 is based on a rate (all-cause) that is "obviously faster than a sequential rate", i.e. the 180 is not a purely sequential calculation; ¶22: "MITTENS … specifically includes and incorporates parallel fixation, with my subsequent disproofs of parallel fixation." In ¶4: "serial fixation with sweeps and ancestral drift are about all that is left AFTER the math eliminates various mechanisms".''',
 '- Stated: BB is correct; parallel fixation is impossible in real species (¶22: "That’s not how real-world species work"); the LTEE rate includes parallelism because it is an average over 12 populations running in parallel.\n- Implicit: the BB conclusion and the aggregate G_f can both be used: the first removes parallelism from humans, the second keeps it in the LTEE rate applied to humans. If parallelism is ruled out for humans, then applying a rate that includes parallel overlap to humans overstates what humans can do (a point in Day\'s favour for the shortfall) but also means G_f is not the serial rate (a point against his statement that the rate "is sequential").',
 '''- Against: Hancock, Myers (G2, G2e): the argument rests on a serial premise. Camestros (G2d). The fidelity gap in BB (G, Gc).
- In support: Day\'s own caveats: ¶25 "the all-cause rate is obviously faster than a sequential rate"; ¶22 distinguishes MITTENS from the "subsequent disproofs of parallel fixation".
- Weaknesses in the responses: the critics quote the Appendix A passage as evidence of seriality; Day replies that it is non-MITTENS math. Both can be right: the book\'s chain of argument is serial, and the 3.0 math is aggregate. The internal verdict (non-sequitur) concerns the chain as quoted: from BB (which has its own issues, G) to sequential, then to 180 using a rate that Day says includes parallelism. Not independently checked against the book.''',
 NOLIT, 'No prediction; consistency analysis only.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Mode switch in the simulator: "parallel allowed" vs "forced sequential".')

# ---- G3 specific-vs-any
claim('G3','specific-vs-any','Specific-vs-any: the product of per-site probabilities prices a pre-specified list of 20 million mutations; evolution requires only that some 20 million out of an enormous candidate pool fix','critic','G','G',
 [('attacks','Ga'),('attacks','G4')],False,'firsthand','checked',('holds','accurate','contested'),
 q('What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations (or 20 million mutations in a row) would all become fixed.','[Dennis McCarthy, Why Probability Zero is Wrong About Evolution (free repost)](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1), 2026-09-11 (orig. 2026-01-26), para 47 (MC-01). Exponent flattened in the HTML source.')+'\n'+
 q('But our evolutionary history does not require that an exact group of 20 million mutations become fixed—only that some 20 million out of an enormous pool of candidate mutations become fixed.','same post, para 48 (MC-02).'),
 '''P_specific(n) = Π p_i = p^n for a pre-specified set; P_any(≥ k of M) = P(Binomial(M, p) ≥ k).
`derived:` (python3 -I) With McCarthy\'s inputs (M = 4.5e11 new mutations in 9 My, p = 1/20,000 = 5e-5): mean M·p = 22.5e6, SD = √(M p (1−p)) = 4,743; k = 20e6 is 527σ below the mean, so P_any(≥ 20e6) ≈ 1 under that model, while P_specific = (5e-5)^(2e7) = 10^−86,020,600 (log10 = 2e7 x −4.30103). The two numbers answer different questions. McCarthy\'s M p = 22.5M is his neutral model (k = μ with all mutations neutral), which Day disputes (B3, B5); whether p = 1/20,000 is the fixation probability of a *new neutral* mutation (1/2N) or a beneficial one (2s) differs between Day\'s papers (Ga uses 0.02).''',
 '- Stated: the event of interest is the existence of 20 million differences, not a specific list.\n- Implicit (McCarthy): the supply M·p reaches 20M, i.e. neutral substitution at rate μ; all mutations treated alike.',
 '''- Against (Day): G3b: "Either the specific fixations matter — in which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t explain the observed functional divergence." The Darwillion is "nothing more than a rhetorical absurdity" (G4).
- In support: Camestros (G3a lottery analogy); Mansfield (MF-02, MF-03) the same point in terms of expected neutral fixations per generation; Day\'s own concession that the Darwillion is rhetorical (G4).
- Weaknesses in the responses: McCarthy\'s count of 22.5M rests on k = μ; his version (MC-04) is "equivalent to k=mu with all mutations treated as neutral" (quotes-file note), which does not reproduce selection; Mansfield\'s illustration (2% neutral gives 1 fixation per generation) comes out ~44x short of 20M over 450,000 generations (20e6/450,000 = 44). Day\'s dilemma uses "can’t explain the observed functional divergence" without defining the functional fraction.''',
 LITH+'''| Kimura 1962 / Kimura & Ohta 1969 | neutral fixation probability 1/2N | verified (see B-claims) |''',
 'Not run in this branch. Prediction (critics): under a neutral model with k = μ and M mutations, P_any ≈ 1 for 20M; this is B5 and was checked at B0.5 (neutral k = U at equilibrium for any N; simulated 0.05018 vs 0.05 at N = 50). Prediction (Day): the any-20M reading does not apply to functional divergence; not formalised.',
 'Link: `research/checks/RESULTS.md` B0.5 (neutral k = U). Arithmetic audit (python3 -I, scratch). Review: pending.', '- Event definition: specific list / any k of M / any k of M functional.')

claim('G3a','camestros-lottery','Camestros: the probability that some number is picked in a lottery is close to 1, unlike the probability of a specific number','critic','G','G3',
 [('supports','G3')],False,'firsthand','extracted',('holds','n/a','n/a'),
 q('However, the probability that SOME number is picked is close to 1 (not certain because the machine might break or an enraged horde of koalas might invade the studio).','[Camestros Felapton, Reading Vox Day 2026 [4]](https://camestrosfelapton.wordpress.com/2026/01/29/reading-vox-day-so-you-dont-have-to-2026-4/), 2026-01-28/29, para 10 (CA-09).'),
 'Analogy for G3: P(specific outcome) ≪ P(some outcome). No numbers.',
 '- Stated: the analogy.\n- Implicit: the outcome space is analogous (disputed by Day, G3b).',
 '''- Against (Day): G3b.
- In support: G3.
- Weaknesses in the responses: an analogy does not fix the size of the candidate pool.''',
 NOLIT, 'No prediction.', 'No script.', '- None.')

claim('G3b','day-either-specific-or-interchangeable','Day: either the specific fixations matter (Darwillion applies) or they are interchangeable neutral noise','day','G','G3',
 [('attacks','G3')],False,'firsthand','extracted',('pending','n/a','contested'),
 q('There is no blunder at all. Either the specific fixations matter — in which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t explain the observed functional divergence.',EDU+', ¶28. Replies to a quoted critic: "And his formula for the probability of 20 million changes is set up to calculate the probability of just one set of 20 million fixations, another colossal blunder on his part."'),
 'Dilemma: (specific) → P_specific = p^n; (interchangeable) → neutral, not adaptive. No formal statement. Day (2026-01-27 ¶13): "McCarthy’s calculation is correct for the number of mutations that enter the population … He has confused mutation with fixation."',
 '- Stated: functional divergence needs specific changes.\n- Implicit: a large fraction of the 20M differences are functional (not quantified); neutral drift does not count as an explanation of functional divergence.',
 '''- Against: the horns are not exhaustive: some differences can be functional and interchangeable (many sets of beneficial mutations give similar function), which Bowers raises ("Multiple mutational paths can lead to similar phenotypes").
- In support: Day cites the Hard Limit and k ≠ μ (B2, B3) for the neutral horn.
- Weaknesses in the responses: the functional fraction is not given by Day; the "INCREASED the size of the Darwillion by a factor of 25" reply (G4b) has an unresolved formula.''',
 NOLIT, 'No prediction.', 'No script.', '- Functional fraction f of divergence as an input.')

# ---- G4 Darwillion
claim('G4','darwillion-definition','Darwillion: the reciprocal of the probability of the pre-specified fixations; Day: "nothing more than a rhetorical absurdity"','day','G','G',
 [('depends-on','Ga')],False,'secondhand','checked',('holds','n/a','n/a'),
 q('the Darwillion is nothing more than a rhetorical absurdity to demonstrate how far off the biologists are from the mathematical realities of the situation.','[The Math is Too Hard](https://voxday.net/2026/09/17/the-math-is-too-hard/) (key B2026-09-17), blog, 2026-09-17, ¶8.')+'\n'+
 q('What Vox Day calculated—(1/20,000)20,000,000 —are the odds that a particular group or a pre-specified list of 20 million mutations','[Do Try to Keep Up, Dennis](https://voxday.net/2026/09/11/do-try-to-keep-up-dennis/) (key B2026-09-11), blog, 2026-09-11, ¶5. Secondhand: McCarthy\'s rendering of Day\'s book calculation, exponent flattened; Day\'s own formula is in the paywalled book and was not checked.'),
 '''Darwillion := 1/P, P = (1/20,000)^(20,000,000) per McCarthy\'s rendering (sourcing: secondhand). Day, firsthand (2026-01-27 ¶3): "my probability calculation about the likelihood of evolution by natural selection"; a reviewer quoted by Day (2026-01-12 ¶6, secondhand) calls it "the reciprocal of the non-existent odds of TENS accounting for the origins of just two species".
`derived:` (python3 -I) log10 P = 2e7 x log10(1/20,000) = −86,020,600, so the Darwillion ≈ 10^86,020,600. For comparison Ga: 0.02^(2e7) = 10^−33,979,400. The Hard Limits abstract (Q30, branch B2) gives a third number, "about one in ten to the seventy-eight-millionth"; no corpus text derives the Darwillion from either.
Other headline numbers from this family audited: Day\'s "87,916,307x" (Q51): 642,888/146,250 = 4.3958; x 20,000,000 = 87,916,308 (rounded; reconciles). 642,888 = 2 x 321,444 (Dawkins\'s recessive figure); 146,250 is the 2025 effective generation count (A4).''',
 '- Stated by Day: the Darwillion is rhetorical, not a model of what happened.\n- Implicit: p = 1/20,000 is the per-mutation fixation probability (neutral, 1/2N, with N = 10,000) used with n = 20M.',
 '''- Against: McCarthy (G3): it prices a specific list. Day agrees it is rhetorical (G4 statement), which concedes the interpretation but not the numbers.
- In support: Day (2026-01-27 ¶14–15): McCarthy used the same 1/20,000.
- Weaknesses in the responses: Day describes it both as "my probability calculation about the likelihood of evolution by natural selection" (2026-01-27) and as "a rhetorical absurdity" (2026-09-17); Day\'s own p differs between uses (0.02 in Ga, 1/20,000 here).''',
 NOLIT, 'No prediction.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- None.')

claim('G4b','darwillion-25x-reply','Day: McCarthy\'s use of a 40,000-generation fixation time increases the Darwillion by a factor of 25','day','G','G4',
 [('attacks','G3')],False,'firsthand','checked',('pending','n/a','pending'),
 q('In other words, he actually INCREASED the size of the Darwillion by a factor of 25. I was using a time-to-fixation number of 1,600. He’s proposing that increasing that 1,600 to 40,000 is somehow going to reduce the improbability, which obviously is not the case.',IC+', ¶15.'),
 '''40,000/1,600 = 25 (python3 -I). The Darwillion as rendered by McCarthy, (1/20,000)^(2e7), contains no time-to-fixation input; the formula connecting a fixation time to the Darwillion is not in the harvested text. If the Darwillion is multiplied by 25, log10 changes by 1.4 out of 86,020,600; if the exponent were multiplied by 25, log10 would change 25-fold. The text does not say which. Pending the book.''',
 '- Stated: fixation takes time; the neutral time 4Ne ≈ 40,000 generations (Q&A) is 25x Day\'s 1,600.\n- Implicit: a formula linking fixation time to the Darwillion exists.',
 '''- Against: none in corpus engaged this reply.
- In support: none.
- Weaknesses: unclear what is multiplied by 25; also 1,600 (a throughput inverse, A2) is compared with 40,000 (a latency), the throughput/latency mix flagged in G2d.''',
 NOLIT, 'Not testable until the formula is available.', 'No script.', '- None.')
