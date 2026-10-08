from common import *
B04='`research/checks/beneficial_fix_time.py` (seed 7)'
RV2='`research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`'
RV3='`research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`'

add(id='F',slug='kimura-fixation-time-limits-fixations',title='Kimura\'s fixation-time equations (4Ne neutral; (2/s) ln 2Ne beneficial) limit how many fixations can complete; 1/(2N) says nothing about when',side='day',branch='F',parent='B',
 edges=[('supports','B'),('depends-on','F1'),('depends-on','F3')],lb=(True,'F is the conceptual bridge from per-allele fixation time to a cap on the count; if latency does not bound throughput (F1), only the fill-state argument (B1/B2) remains'),
 sourcing='firsthand',status='reviewed',v=('pending','partial','contested'),
 quotes=[Q('EDU','The Kimura equation Brian should have used is Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('IR','k = μ gives the output rate once the process is running. t̄ = 4Nₑ gives the startup cost before any output appears.','§2 The Missing Equation'),
   Q('EDU','It contains no time variable. It says nothing about when.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt',note='on 1/2N')],
 formal='''Glossary sense: throughput k = substitutions per generation; latency t_fix = generations per allele. Day's position, in its strongest form (Education blog; IR §2): latency is the "startup cost" (fill time), and the count over a window is rate × (window − startup) (B1). Weaker form (Q&A, F1a): window ÷ latency bounds the count.
Sub-claims: F1 (critic: latency ≠ throughput), F1a (Day's reply and his own serial use), F1b (McCarthy, parallel), F2 (interference/feasibility check), F3 (beneficial time formula), F3a (s = 0.001), F4/F4a (Bowers 2s and Day's reply), F5 (Kimura & Ohta SD), F6 (relictation).''',
 a_stated='Kimura\'s own framework supplies the time equations.',a_impl='The (2/s)ln(2Nₑ) formula is Kimura\'s (the Zenodo calculator cites Charlesworth 1994; not found in Kimura & Ohta 1969 or Kimura 1962); fill-state is empty (B1c).',
 against=rq('MFC','The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important.',loc='comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbR9n0iZNuQ (Mansfield)'),support='Day: the Hard Limits paper treats the 4Nₑ transit as the length of the pipe (B2).',
 weak='Mansfield\'s comment predates Day\'s reply and answers a different sentence; Day\'s reply in turn depends on the fill state, which neither side has sourced (B1c).',
 lit=[lit_row('Kimura & Ohta 1969','4Nₑ (Eq. 15); no (2/s)ln(2Nₑ) formula','accurate for 4Nₑ; not found for the beneficial formula (it is attributed to Charlesworth 1994 in Z19984826)'),
      lit_row('Kimura 1962','U = 1/2N, ≈2s','accurate (B7a)')],
 p_claim='Latency enters the count only through the fill state.',p_opp='Latency does not bound throughput; the count is rate × window once the pipeline is full.',p_change='B1c, F2.',
 check='See F1 (done), F2 (proposed), F3 (done: '+B04+').',sim=['latency model per allele','throughput mode (parallel | serial)','fill state'])

add(id='F1',slug='latency-not-throughput-mansfield',title='Mansfield: time to fix one allele is not important; the time between successive fixations is (latency is not throughput)',side='critic',branch='F',parent='F',
 edges=[('attacks','F'),('attacks','B2d')],lb=(True,'if latency bounded throughput, Day\'s serial reading would hold; F1 says it does not'),
 sourcing='firsthand',status='reviewed',v=('holds','n/a','contested'),
 quotes=[Q('MFC','The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important.','comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbR9n0iZNuQ (Mansfield; truck analogy NY–LA follows)'),
   Q('MC2','Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time.','para 22 (McCarthy)')],
 formal='''Little's law: in-flight count = arrival rate × latency; throughput = arrivals × P_fix independent of latency. For independent loci, rate = 2N·U_b·u(s) (Kimura 1962) and G_f = 1/rate.
RESULTS F1 (N = 1000, s = 0.01, U_b = 0.01): predicted 0.3960 per generation; simulated 0.3972 ± 0.0018; t_fix = 847 generations but G_f = 3; in-transit ≈ 336 (computed as rate × latency, **not measured**).''',
 a_stated='Many alleles in transit at once (truck analogy).',a_impl='Independent loci, no interference, no cost of selection (RESULTS caveats).',
 against='Day (F1a): his throughput number already includes parallelism; feasibility is limited by cost/interference (F2).',support='RESULTS F1.',
 weak='RESULTS caveat: the parameters (20 new beneficial mutations per generation, 0.4 substitutions per generation) are far above any realistic regime and avoid selective load by construction, so pipelining is shown possible, not feasible. Mansfield\'s comment was made before Day\'s reply, and quotes Day only via a paste.',
 lit=[lit_row('Kimura 1962','u(s) formula used for the rate','accurate')],
 prereg_note='Pre-registered prediction (copied from RESULTS F1; the check has run).',
 p_claim='(Mansfield) Steady-state rate = 2N·U_b·u(s), independent of latency.',p_opp='(Day, weak form) Count ≤ window / latency.',p_change='In-transit count measured directly (TODO); F2 for interference.',
 check='Script: `research/checks/f1_throughput.py` (seed 31) · Result: rate confirmed (0.3972 ± 0.0018 vs 0.3960); spacing vs latency 3 vs 847 generations; in-transit count is Little\'s law, not measured. Verdict: as logic, dividing elapsed time by latency is not a throughput bound; feasibility is untested (F2). Review #3 caveats (unrealistic regime; serial reading must be tied to a quote → F1a). Review: '+RV3,
 sim=['number of independent loci','U_b','s','latency/in-transit display (measure, not compute)'])

add(id='F1a',slug='day-reply-throughput-and-serial-use-19800',title='Day: LTEE G_f is a throughput measurement; yet the Q&A divides by a latency-derived 19,800 "generations per fixation"',side='day',branch='F',parent='F1',
 edges=[('attacks','F1'),('depends-on','F3')],lb=(True,'decides whether the serial reading is a straw man or Day\'s own usage'),
 sourcing='firsthand',status='extracted',v=('non-sequitur','n/a','pending'),
 quotes=[Q('EDU','The MITTENS calculation does not assume sequential fixation. The LTEE rate of 1,322 gen/fix is a total throughput measurement',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('EDU','The Probability Zero derivation at s = 0.001 does compute a per-fixation time, but dividing total generations by per-fixation time to get maximum achievable fixations is not an assumption of sequential processing. It is also a throughput calculation',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('QA','N_e = 10,000 (standard effective population constant) T = 22 years (generation, Gurven & Kaplan 2007) L = 51 years (lifespan based on Coale-Demeny-West life tables) s = 0.001 (selection coefficient, Zeng et al 2021) t ≈ 19,800 generations per fixation','¶5 (the formula is not printed in the Q&A)'),
   Q('QA','It probably won’t escape your attention that 19,800 > 1,600. So using the 1,600 generations rate was extremely generous to the Modern Synthesis model.','¶6'),
   Q('EDU','The six-fixation figure (now seven at updated parameters) comes from the beneficial fixation time at s = 0.001, not from neutral drift.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt')],
 formal='''**Arithmetic audit (derived, python3 -I):** (2/0.001) × ln(2 × 10,000) = 2000 × 9.9035 = 19,807 ✓ (19,800). This is a *latency* (deterministic sweep time of one allele, F3). The Q&A calls it "generations per fixation", i.e. G_f = 19,807, a throughput of 1/19,807 = 5.05×10⁻⁵ per generation — the serial reading.
Day confirms in the Education post that the six-fixations-over-9-My figure (Mansfield quotes it) comes from this latency (quote 3). Reconstruction (derived; Day does not print the inputs): 9×10⁶ y / 32.5 y × 0.45 / 19,807 = 6.3; and 146,250 / 19,807 = 7.4 ("now seven at updated parameters"). Neither contains a parallel-width factor, so the figure is window × d ÷ latency. Other readings of the same divisor: 252,000/19,807 = 12.7; 252,000 × 0.45/19,807 = 5.7.
The Education post (quote 2) describes the division as a throughput calculation "adjusted for parallelism" but does not identify a width factor in the six/seven figure. The 2026-02-14 post: the human rate "works out to 19,800" (and 40,787 with corrections).
Z18167588 (Bernoulli) §7.8 multiplies by a parallel width instead: (300,000/440) × 230 = 157,000, where 440 ≈ (2/0.01) ln 9 = 439 is a latency and 230 is a number of simultaneous sweeps (not derived; the paper says it works backward from the constraint). That paper is branch G.
(Note: Z18441321 uses "19,800 effective generations" for a different quantity, 23,000 × 0.86; the coincidence of numbers is not related.)''',
 a_stated='G_f from the LTEE is parallelism-adjusted; the human value (19,800) is computed from consensus numbers.',a_impl='The 19,800 figure is a per-allele sweep time at s = 0.001, Nₑ = 10⁴ and is equated with a spacing between fixations; realistic sweeps in parallel require a width factor (Bernoulli paper: 230).',
 against=rq('MFC','The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important.',loc='Mansfield')+'; RESULTS F1 (spacing 3 vs latency 847).',support='Camestros concedes the LTEE number is an average (CA-10 in the harvest): "He is correct that when he calculated the number it was an average."',
 weak='Mansfield and Hancock (GG-01, tied to Duffy\'s 180-interval slide) read F_max as serial; the Education post disowns that, while also confirming that the six/seven-fixation figure and the Q&A 19,800 come from a latency. Neither side has shown whether interference (F2) makes the effective width near 1.',
 lit=[lit_row('Zeng 2021','see F3a','verified-misread (ledger)'),
      lit_row('Good 2017','"We find that the trajectories in Fig. 1 are inconsistent with a "periodic selection" model in which individual driver mutations fix in a sequence of discrete selective sweeps."','verified (ledger): the LTEE shows overlapping sweeps, i.e. parallelism in the measured G_f')],
 p_claim='LTEE G_f = 1,322 already contains parallelism; 19,800 shows humans are slower than E. coli.',p_opp='A latency of 19,807 generations is not a spacing; realistic parallel width (hundreds) puts the human spacing well below 19,807 (F1, F2).',
 p_change='F2 (interference) with human-like parameters; or Day stating that 19,800 enters no count.',check='Script: none (arithmetic computed with python3 -I). Related: `research/checks/f1_throughput.py`.',sim=['G_f as latency or as spacing (explicit toggle)','parallel width'])

add(id='F1b',slug='mccarthy-parallel-not-one-at-a-time',title='McCarthy: mutations do not increase in frequency one at a time; the expected count has no queue',side='critic',branch='F',parent='F1',
 edges=[('attacks','F')],lb=(False,'same logical point as F1, embedded in McCarthy\'s time-adjusted calculation (B5a)'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','contested'),
 quotes=[Q('MC2','Obviously, mutations, whether neutral or not, do not have to increase in frequency throughout a population one at a time.','para 22')],
 formal='''McCarthy\'s time-adjusted count: (450,000 − 50,000) × 50 = 20M (B5a). Day\'s reply (R2) restates it and answers with the Bernoulli Barrier (branch G) and the N/Nₑ correction (B3e, retracted B3g).''',
 a_stated='Fixations overlap in time.',a_impl='Independent loci.',against='Day (G): the probability that millions of in-transit mutations all complete is astronomically small (Bernoulli Barrier; not assessed here).',support='RESULTS F1.',
 weak='Day\'s argument that "expected value is the average over infinite trials" confuses the expected count with the requirement; for 20M fixations, the Poisson sd is ≈ 4.5 thousand (derived), so the count is concentrated (branch G).',
 lit=[],p_claim='Overlap is routine.',p_opp='(Day) overlap capped by selection cost/variance (G, H).',p_change='F2.',check='Script: `research/checks/f1_throughput.py`.',sim=['parallel width'])

add(id='F2',slug='multi-locus-interference-feasibility',title='Feasibility of pipelining: multi-locus sweeps under linkage, interference and cost (proposed check)',side='day',branch='F',parent='F',
 edges=[('depends-on','F1'),('depends-on','F1a')],lb=(True,'Day\'s strongest remaining form of the throughput argument rests on parallel width being capped at ~230 or by cost'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','pending'),
 quotes=[Q('BERN','the "active zone" of intermediate-frequency alleles imposes a hard limit on pipeline capacity of approximately 230 simultaneous sweeps.',file='day/zenodo-18167588.txt',note='abstract'),
   Q('GOOD','molecular evolution continues to be characterized by signatures of rapid adaptation, with multiple beneficial variants simultaneously competing for dominance in each population','Abstract')],
 formal='''Claim: the number of simultaneous sweeps is bounded (230 in Z18167588; obtained by working backward from the constraint, no derivation shown) or capped by the cost of selection (branch H); critics: independent loci pipeline freely (F1). Good 2017 shows overlapping sweeps in the LTEE.
**Proposed check F2 (not yet run; pre-registered here):** forward Wright–Fisher with L loci, Poisson beneficial-mutation supply U_b per genome per generation, selection coefficient s, soft selection (fixed N), recombination r ∈ {0.5 (free), 0.01, 0 (asexual)}; N ∈ {1,000, 10,000}; s ∈ {0.001, 0.01}; U_b ∈ {0.001, 0.01, 0.1}. Report R = (observed substitutions/generation)/(2N·U_b·u(s)), and the time-averaged number of sweeping loci n_sw.
- Predictions: (a) r = 0.5, U_b = 0.01, N = 1000, s = 0.01: R ≈ 1 (RESULTS F1: 0.3972 vs 0.3960). (b) r = 0, and N·U_b·s large: R < 1 (clonal interference), with n_sw bounded by ≈ the number of segregating beneficial lineages. (c) With realistic human values (N ≈ 10⁴, s ≈ 0.001–0.01, U_b per genome from a stated DFE) R is the quantity that tests Day\'s ~230 cap and the cost-of-selection cap; no prediction is pre-registered for the cap itself because its derivation is not in the corpus.
- Would change the verdict: R ≥ 0.5 at human-like parameters falsifies a binding cap of order 230 for the neutral-plus-beneficial count; R ≪ 0.5 with r = 0.5 and soft selection would support Day.''',
 a_stated='Day: parallel width limited to ~230 sweeps.',a_impl='Hard selection (cost) applies (H); linkage as in asexuals for the LTEE, but humans recombine.',
 against='Camestros / Myers / Hancock (serial reading; no numbers on the cap).',support='Good 2017 (LTEE interference).',weak='The LTEE is asexual and largely nonrecombining (Reddit RE-07, A5), so LTEE interference does not transfer to humans without the check.',
 lit=[lit_row('Good 2017','"This striking separation of timescales between inter- and intra-clade fixations cannot be explained by clonal interference"','verified (ledger)')],
 p_claim='Parallel width is capped.',p_opp='Parallel width in free-recombination populations is limited only by cost/variance, not by interference.',p_change='See Formal statement.',check='Script: proposed `research/checks/f2_multilocus.py` (not yet written) · Result: none. Queued in REVIEW.md.',
 sim=['number of loci','recombination rate','soft vs hard selection','selection coefficient distribution','U_b'])

add(id='F3',slug='beneficial-fixation-time-2-over-s-ln-2ne',title='t ≈ (2/s) ln(2Ne) for a beneficial allele (called "Kimura\'s equation")',side='day',branch='F',parent='F',
 edges=[('supports','F'),('depends-on','F3a')],lb=(False,'used in the Q&A (19,800) and "six/seven fixations"; the throughput question dominates (F1)'),
 sourcing='firsthand',status='reviewed',v=('holds','partial','contested'),
 quotes=[Q('EDU','Kimura’s equation for fixation time: 4Nₑ generations for a neutral allele, or t ≈ (2/s) × ln(2Nₑ) for a beneficial one.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('Z166426','Time to fixation calculated using t ≈ (2/s_eff) × ln(2N_e) for N_e = 10,000, from initial frequency p = 0.01 to p = 0.99.',file='day/zenodo-18166426.txt')],
 formal='''Deterministic logistic sweep: time from p₀ to 1 − p₀ at selection s (per Day\'s parametrisation) is (2/s) ln((1−p₀)/p₀) ≈ (2/s) ln(2Nₑ) when p₀ = 1/(2Nₑ). The stochastic conditional mean time is (2/s)(ln(4Ns) + γ) (RESULTS review #2 correction). Derived (python3 -I) at N = 10⁴: s = 0.001: (2/s)ln(2N) = 19,807 vs (2/s)(ln 4Ns + γ) = 8,532; s = 0.01: 1,981 vs 1,314; s = 0.0005: 39,614 vs 14,292.
Zenodo calculator Z19984826 writes the selected-sweep time as (2/(s̄·d)) ln(2Nₑ) and cites Charlesworth 1994 for it; the blog attributes the formula to Kimura.''',
 a_stated='Kimura; Nₑ = 10⁴; s = 0.001 (F3a).',a_impl='Deterministic path from 1/(2Nₑ) (or 0.01) to near fixation; unconditional on loss; the 0.01→0.99 version in Z18166426 omits the stochastic early phase.',
 against='RESULTS B0.4: overshoot 1.6–2.2× at tested points, ≈2.3× at Day\'s parameters.',support='RESULTS B0.4: (2/s)ln(2N) is a standard deterministic sweep-time approximation, used legitimately as such.',
 weak='Attribution to Kimura is not supported by Kimura & Ohta 1969 (4Nₑ only) in this corpus; Z19984826 cites Charlesworth 1994. The overshoot concerns the conditional mean latency, which is not the quantity that sets throughput (F1).',
 lit=[lit_row('Charlesworth 1994 (cited in Z19984826)','sweep time (2/(s̄ d)) ln(2Nₑ)','not retrieved; unverified'),
      lit_row('Kimura & Ohta 1969','4Nₑ (neutral); selected cases presented numerically in the paper','accurate for 4Nₑ')],
 prereg_note='Pre-registered prediction (copied from RESULTS B0.4; the check has run).',
 p_claim='(Day) t ≈ (2/s) ln(2Nₑ).',p_opp='Simulated t_fix ≈ the Kimura–Ohta diffusion integral (tolerance 5%); (2/s)ln(2N) overshoots both.',p_change='n/a (done).',
 check='Script: '+B04+' · Result: confirmed. N = 500, s = 0.01: sim 698±3, diffusion 703, (2/s)ln2N 1382, (2/s)(ln4Ns+γ) 715; N = 1000, s = 0.005: 1405±9 / 1407 / 3040 / 1429; N = 2500, s = 0.01: 1043±6 / 1033 / 1703 / 1036; N = 5000, s = 0.01: 1177±7 / 1173 / 1842 / 1175; N = 10⁴, s = 0.001: diffusion 8,480, (2/s)ln2N 19,807, corrected asymptote 8,532. Review #2: asymptote corrected from ln(2Ns) to ln(4Ns). Review: '+RV2,
 sim=['s','N, Nₑ','p₀ (1/2N or 0.01)','deterministic vs conditional mean time'])

add(id='F3a',slug='s-0-001-zeng-2021-misread',title='s = 0.001 "the empirical mean for beneficial mutations in humans from Zeng et al. 2021"',side='day',branch='F',parent='F3',
 edges=[('supports','F3')],lb=(True,'the input that sets the 19,800 latency; halving or doubling s doubles or halves it'),
 sourcing='firsthand',status='reviewed',v=('pending','misread','contested'),
 quotes=[Q('EDU','at s = 0.001 (the empirical mean for beneficial mutations in humans from Zeng et al. 2021)',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('ZENG','We detect widespread signatures of negative selection in the genetic architecture across 155 complex traits with a predicted mean selection coefficient of ~0.001','Results, evolutionary inference')],
 formal='''Parameter key: `selection.s_zeng_2021` = 0.001, sign negative, positive selection appears only as a simulation sensitivity scenario and Day uses the value as beneficial (parameters.yaml note, verified). Zeng: "Since we only detected signatures of negative selection in real traits, our evolutionary simulations focused on the models of negative selection." Latency scales as 1/s (F3): derived t(s = 0.01, N = 10⁴) = 1,981 vs 19,807 at s = 0.001 for the deterministic formula.''',
 a_stated='s = 0.001 is the mean for beneficial mutations in humans.',a_impl='A mean over trait-affecting variants under negative selection is a proxy for the beneficial coefficient.',
 against='Fidelity ledger: verified-misread.',support='None found; Z18166426 uses s_eff.',weak='Neither side has a human beneficial-s distribution; Zeng itself says about 1% of the genome are mutational targets with mean 0.001, which does not inform sweep speed of rare beneficial alleles.',
 lit=[lit_row('Zeng 2021','"about 1% of human genome sequence are mutational targets with a mean selection coefficient of ~0.001"','verified-misread when used for beneficial mutations'),
      lit_row('Zeng 2021','"Since we only detected signatures of negative selection in real traits, our evolutionary simulations focused on the models of negative selection."','nuance: positive selection only a sensitivity scenario')],
 p_claim='s_ben = 0.001.',p_opp='s is an unmeasured distribution; sweep latency spans 10²–10⁴ generations.',p_change='A sourced human beneficial-s distribution.',check='Script: none. Related: B0.4 in F3.',sim=['s (distribution)','sign convention'])

add(id='F4',slug='bowers-fixation-probability-2s',title='Bowers (via Day\'s repost): the correct approximation for a beneficial mutation is roughly 2s, not 1/N',side='critic',branch='F',parent='F',
 edges=[('attacks','F')],lb=(False,'correct textbook statement; no calculation in the review, and Day\'s use is of rates (F4a)'),
 sourcing='secondhand',status='extracted',v=('holds','accurate','supported'),
 quotes=[Q('BOW','The correct approximation for a beneficial mutation is roughly 2s (in diploids under weak selection), not 1/N.','para 3',sh='Bowers\'s seven-point review as reposted by Day; the original was not found')],
 formal='''u ≈ 2s (Haldane 1927/Kimura 1962), so per-generation adaptive substitution rate k_ben = 2N·U_b·2s = 4N s U_b. B0.3 check: Kimura u at N=100, s=0.01: sim 0.019995 vs 0.020171 (z = −0.56); N=500: 0.019745 vs 0.019801; N=1000, s=0.005: 0.010225 vs 0.009950 (z = +1.22).''',
 a_stated='Fixation probability of a beneficial mutation under weak selection ≈ 2s.',a_impl='Large N, additive.',against='Day (F4a): confusion of probability with rate.',support='Kimura 1962; RESULTS B0.3.',weak='Known only through Day\'s repost; contains no calculation (Day\'s reply is accurate on that).',
 lit=[lit_row('Kimura 1962','"the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient"','verified-accurate')],
 prereg_note='Pre-registered prediction (copied from RESULTS B0.3; the check has run).',
 p_claim='u ≈ 2s.',p_opp='n/a',p_change='n/a',check='Script: `research/checks/baseline_textbook.py` (seed 20261007) · Result: B0.3 all pass (z = −0.56, −0.18, +1.22).',sim=['s','N','dominance'])

add(id='F4a',slug='day-reply-fixation-probability-vs-rate',title='Day: the reviewer confused fixation probability with fixation rate',side='day',branch='F',parent='F4',
 edges=[('attacks','F4')],lb=(False,'correct distinction; does not engage the 2s point'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','pending'),
 quotes=[Q('BOW','The reviewer has confused fixation probability with fixation rate. These are two different things.','para 11 (Day)')],
 formal='''Fixation rate k = (input flux) × (fixation probability). Day\'s reply gives no equation. Both quantities are standard: k_neutral = 2Nμ/(2N) = μ; k_ben = 2N U_b · 2s. The reply is accurate as a distinction; whether it answers Bowers depends on which quantity the original review addressed (not retrieved).''',
 a_stated='—',a_impl='Bowers\'s point concerns probability only.',against='Bowers (F4).',support='Standard theory.',weak='No equation; original review not seen; Day\'s repost is the only source; Day\'s own comment on the review is that it has no calculation (accurate for the reposted text per the harvest).',
 lit=[],p_claim='—',p_opp='—',p_change='The original Bowers text.',check='Script: none.',sim=['—'])

add(id='F5',slug='kimura-ohta-sd-not-in-paper',title='Mean 4Ne with SD ≈ 0.538 × 4Ne "under Kimura\'s diffusion treatment"',side='day',branch='F',parent='F',
 edges=[('supports','B1a')],lb=(False,'the SD is used to describe the breadth of the fixation-time distribution; the E[F(T)] formula needs only the mean'),
 sourcing='firsthand',status='reviewed',v=('holds','unverifiable','n/a'),
 quotes=[Q('IR','a broad distribution around that mean (SD ≈ 0.538 × 4Nₑ under Kimura\'s diffusion treatment)','§3 The Empty Pipe')],
 formal='''0.538 × 4 = 2.152, i.e. SD ≈ 2.15 Nₑ. Our simulation (RESULTS B0.2): SD of t_fix/N = 2.105 (N=50) and 2.108 (N=200) vs diffusion ≈ 2.15 (derived consistency). The figure is not in Kimura & Ohta 1969, which derives the first moment and says higher moments can be obtained step by step (fidelity ledger).''',
 a_stated='Kimura\'s diffusion treatment gives SD ≈ 0.538 × 4Nₑ.',a_impl='Conditional on fixation, p₀ → 0.',against='n/a',support='RESULTS B0.2.',weak='Fidelity: the attribution is to a later or derived source; the paper contains the first moment (Eq. 15) only.',
 lit=[lit_row('Kimura & Ohta 1969','Eq. 15: t̄(0) = 4Nₑ; no SD','not-found in this paper (ledger)')],
 p_claim='SD ≈ 2.15Nₑ.',p_opp='n/a',p_change='n/a',check='Script: `research/checks/baseline_textbook.py` · Result: SD 2.105, 2.108 vs ≈2.15 (diffusion). Review #2 corrected the mean target.',sim=['fixation-time SD display'])

add(id='F6',slug='relictation-ten-percent-replacement',title='Relictation: below ~10% replacement the 4Ne formula holds; beyond it, it breaks',side='day',branch='F',parent='F',
 edges=[('supports','F')],lb=(False,'a new mechanism claim (published 2026-10-06); not engaged by any critic in the corpus'),
 sourcing='firsthand',status='extracted',v=('pending','unverifiable','pending'),
 quotes=[Q('REL','compression fails and a single family can replace more than ~10% of the population, the formula t̄ = 4Nₑ breaks in quantifiable ways. Below 10% replacement, the formula holds','p.1 (abstract)')],
 formal='''The corpus contains the abstract-level claim only; the Zenodo record was modified 2026-10-07 (versions ledger note: check for changes before quoting). No equation is extracted here.''',
 a_stated='Replacement fraction r per generation determines whether t̄ = 4Nₑ holds.',a_impl='Not extracted.',against='None.',support='None.',weak='Not assessed (full text not read in this pass).',lit=[],
 p_claim='—',p_opp='—',p_change='A reading of the full paper and a Cannings-model check with large family-replacement events (B3b/sweepstakes).',check='Script: none.',sim=['family replacement fraction (sweepstakes)'])
