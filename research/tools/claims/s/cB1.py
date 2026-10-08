from common import *
RV2='`research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`'
RV3='`research/checks/REVIEW.md#2026-10-07--review-3-sonnet-correctness--two-sided-steelman-of-b1b-b2a-f1`'

add(id='B1',slug='intrinsic-irrelevance-steady-state',title='k = mu is a steady-state identity; finite-time count differs (Intrinsic Irrelevance)',side='day',branch='B',parent='B',
 edges=[('supports','B'),('depends-on','B1a'),('depends-on','B1c')],
 lb=(True,'ROOT as worded ("no mechanism") needs the neutral route closed; B1, B2 and B3 are partial substitutes, so ROOT survives only if at least one holds'),
 sourcing='firsthand',status='reviewed',v=('holds','n/a','contested'),
 quotes=[Q('IR','using the exact transient formula E[F(T)] = μL ∫₀ᵀ F_X(u) du rather than the naive product μLT, the leading-order correction subtracts the mean fixation time from the available window.','p.1 (abstract)'),
   Q('IR','It is a rate, not a count, and converting it to a count requires assumptions the identity itself cannot supply.','§1 The Identity'),
   Q('IR','At generation zero, the subsitution pipeline is empty.','§3 The Empty Pipe (typo "subsitution" is in the source)')],
 formal='''Glossary sense: **throughput k** = substitutions per generation at steady state; **latency** t_fix = generations for one allele to go from arising to fixation.

- Steady state: k = 2Nμ × 1/(2N) = μ per site per generation (`rates` not applicable; textbook identity, accepted by Day: "Kimura's derivation is mathematically correct").
- Finite window T from an **empty** start: E[F(T)] = μL ∫₀ᵀ F_X(u) du, F_X = CDF of the fixation time conditional on fixation, E[X] = 4Nₑ (Kimura & Ohta 1969). For T ≫ E[X], E[F(T)] ≈ μL (T − 4Nₑ).
- Parameters: `generations_available.day_2026` = 252,000; `population.Ne_modern_human` = 1.0e4; μL ≈ 30 (Day's value; **no entry in parameters.yaml**, propose `new: mutation.muL_neutral_per_gen_day_IR = 30`; the pedigree-based haploid figure would be 1.2e-8 × 3.2e9 = 38.4, derived).

Sub-claims: B1a (the formula and its numbers), B1b (size-change statement), B1c (was the start empty?), B1d (Day's later reply: full but short pipe), B1e (Chalub 2022).''',
 a_stated='Population has held one size; the pipeline is empty at generation zero; Nₑ = 10,000 (also 50,000 and 63,000 as sensitivity cases).',
 a_impl='Zero standing variation at the split (an empty start means zero heterozygosity, which contradicts observed human diversity; RESULTS and steelman review C1 frame it as a counterfactual boundary case). Constant Nₑ over the whole window. Counting is of per-lineage fixed substitutions, not pairwise sequence divergence (see B4a/B6).',
 against=rq('MFC','The ‘pipeline’ would have been full from the X generations preceding that point in time.','comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbRHJx-mRP2 (Mansfield)')+'\n  Camestros: see B6b. McCarthy: see B5a (time-adjusted version). Reddit, Dumb-and-Dumber (B5f): '+rq('RED','It needs the elapsed time to be long compared with the fixation time.',loc='post 1wss2wj')+' He accepts the 4Nₑ time and argues 252,000 is long compared with it.',
 support='Exact for an empty start (RESULTS B1, below). Day\'s transient-lag mechanism after a size change is standard theory (B1b). Hössjer (ally) accepts k = dμ as the neutral rate but argues the date is circular (B4f).',
 weak='Against: Mansfield gives no numbers and quotes Day only via a commenter (secondhand). For: the corpus itself contains Day\'s later statement that the pipeline "was full" at the split (B1d), which conflicts with the empty-start premise of this claim; Day does not reconcile the two.',
 lit=[lit_row('Kimura & Ohta 1969','"takes about 4Ne generations until it spreads to the whole population if we disregard the cases in which such a gene is eventually lost" (p.766, after Eq. 15)','accurate for 4Nₑ (ledger)'),
      lit_row('Chalub 2022','see B1e','verified-partial (ledger)')],
 p_claim='(RESULTS B1, P1) With an empty start the simulated count matches U∫F_X, which tends to U(T−4N).',
 p_opp='(RESULTS B1, P2) With an equilibrium start the simulated count matches U·T.',
 p_change='A sourced demographic history (B1c) showing the ancestral population was at equilibrium or shrinking at the split would remove the deficit and move the external verdict to contradicted; one showing a sustained expansion lasting an appreciable fraction of 4Nₑ would support it.',
 check='Script: `research/checks/b1_start_state.py` (seed 11) · Result: both predictions confirmed at every T. N=100, U=0.5: T=400: U·T=200, Day U∫F_X=41.6, empty-start sim 41.3±0.8, equilibrium-start sim 198.5±2.0; T=2000: 1000 / 802.7 / 802.5±3.4 / 1005.1±4.3. Review #2: the empty-start run is Poisson thinning, so it matches by construction (it verifies the code, not the claim). Internal verdict: holds as mathematics. Review: '+RV2,
 sim=['start state (empty | equilibrium | user-set heterozygosity)','Nₑ(t) schedule','T (generations)','μL (neutral destined-to-fix input per generation)','counting mode: per-lineage fixed substitutions vs pairwise divergence'])

add(id='B1a',slug='eF-formula-and-numbers',title='E[F(T)] ≈ muL(T − 4Ne) and its numerical application',side='day',branch='B',parent='B1',
 edges=[('supports','B1')],lb=(False,'B1 stands or falls on the start-state question (B1c), not on this algebra, which is exact'),
 sourcing='firsthand',status='reviewed',v=('holds','n/a','pending'),
 quotes=[Q('IR','∫₀ᵀ F_X(u) du = T − ∫₀ᵀ (1 − F_X(u)) du ≈ T − 4Nₑ','p.2 (§3)'),
   Q('IR','Using 252,000 generations since the split (approximately 6.3 million years at 25 years per generation) and μL ≈ 30 neutral mutations per generation: Steady-state calculation (k = μ applied naively): 30 × 252,000 = 7,560,000 fixations','p.3 (§4 The Numbers)')],
 formal='''E[F(T)] ≈ μL (T − 4Nₑ), valid for T ≫ E[X] = 4Nₑ.

**Arithmetic audit (derived, python3 -I):**
| Case | Day's figure | Recomputed | Note |
|---|---|---|---|
| steady state 30 × 252,000 | 7,560,000 | 7,560,000 | matches |
| Nₑ = 10⁴: 30 × (252,000 − 40,000) | 6,360,000 (loss 1.2M, 15.9%) | 6,360,000; loss 1,200,000 = 15.87% | matches |
| Nₑ = 5×10⁴: 30 × 52,000 | 1,560,000 (loss 79.4%) | 1,560,000; 6.0M/7.56M = 79.37% | matches |
| Nₑ = 63,000 (4Nₑ = T) | 0 (100%) | 0 | T = 4Nₑ is **outside** the stated regime T ≫ 4Nₑ; the exact integral is positive, so 0 is a lower bound |
| §6 prose | "reaches nearly 50% at the upper end of human estimates" | table reaches 100% | internal inconsistency of wording |
| per-lineage count vs requirement | 7.56M | 7.56M vs 17.5M SNV (Z23003785) = 2.3× short; vs 20M = 2.6×; vs 205M = 27× | the uncorrected neutral expectation is already below the SNV requirement at μL = 30 |
Relayed critic figure: see B5d (6 My ÷ 25 × 30 = 7.2M).''',
 a_stated='T ≫ E[X]; stochastic transit-time distribution with mean 4Nₑ; μL ≈ 30.',a_impl='Empty start (B1c). μL = 30 is unsourced (pedigree-based haploid μL = 38.4, derived). F_X is the conditional-on-fixation CDF, so μL must be the destined-to-fix flux, which equals the total neutral input L μ only because 2Nμ × 1/(2N) = μ.',
 against='Mansfield (B6/B1c) disputes the start state only; no one in the corpus disputes the algebra.',support='RESULTS B1: Day\'s U∫F_X reproduced to within SE at T = 200–2000 (N=100).',
 weak='The support check cannot confirm the premise (it is constructed from it).',
 lit=[lit_row('Kimura & Ohta 1969','mean time to fixation (conditional) = 4Nₑ; first moment only, no SD','accurate; the SD ≈ 0.538×4Nₑ in IR §3 is not in this paper (see F5)')],
 p_claim='Simulated expected count from an empty start equals μL∫F_X, tending to μL(T−4Nₑ).',p_opp='From an equilibrium start the count is μL·T; the formula applies only to the empty case.',
 p_change='Exact (non-asymptotic) evaluation at T = 4Nₑ would change the 63,000 row from 0 to a positive value, not the verdict.',
 check='Script: `research/checks/b1_start_state.py` · Result: see B1. Arithmetic audit above: computed with python3 -I, this session. Review: '+RV2,
 sim=['Nₑ','T','μL','exact vs asymptotic integral'])

add(id='B1b',slug='size-change-transient',title='k = mu holds only after one size is held for ~4Ne generations (size-change transients)',side='day',branch='B',parent='B1',
 edges=[('supports','B1'),('depends-on','B1c')],lb=(False,'the direction (deficit vs excess) is empirical (B1c); the mechanism is standard theory'),
 sourcing='firsthand',status='reviewed',v=('holds','n/a','pending'),
 quotes=[Q('HL','it holds only after a population has held one size for the roughly 4N ₑ generations a neutral allele needs to drift from a single copy to fixation.','p.1 (abstract)'),
   Q('HL','Interrupt that condition and the far end delivers whatever the near end was feeding it 4Nₑ generations back, not what it is feeding it now.','§The Transit Time')],
 formal='''After a step change in size, the per-window substitution rate k_w/μ departs from 1 for ≈ 4N_new generations; the cumulative excess or deficit ≈ μL·4ΔN (expansion: deficit; contraction/bottleneck: excess), long-run mean = μ.

Day's claim, read narrowly (a statement about transients), is the standard result. Read broadly (a deficit whenever N has not been constant for about 4Nₑ generations) it holds only for expansions (RESULTS B1b).''',
 a_stated='Population size history determines the fill state of the pipeline.',a_impl='The relevant history is a monotone expansion; the pipeline emptied by past events is not refilled by contractions.',
 against='RESULTS B1b: contractions give an excess, bottlenecks and founder events net ≈ 0; no critic in the corpus engaged this directly.',support='Expansion lag confirmed: cumulative/UT 0.733 for N0/5→N0 (analytic 0.733).',
 weak='Only a within-lineage fixation count is tested; the human–chimp observable is pairwise divergence (B4a).',
 lit=[],p_claim='(RESULTS B1b) Deficit whenever N has not been constant for ≈4Nₑ.',p_opp='(RESULTS B1b) Contraction gives a transient excess, expansion a transient deficit of about 4N_new generations; long-run k = U.',
 p_change='Sourced history (B1c) showing contraction or constancy over the 252,000-generation window.',
 check='Script: `research/checks/b1b_demography.py` (seed 21) · Result: N0=500, U=0.2, 24 replicates, T = 3×4N0. Cumulative/U·T: constant 0.996; contraction N0→N0/5 1.259 (analytic 1.267); expansion N0/5→N0 0.733 (analytic 0.733); expansion N0/5→5N0 0.085 (saturating); bottleneck 0.999; founder 0.996. Verdict: half right (right for expansions, wrong in sign for contractions); mechanism is standard theory. Review: '+RV3,
 sim=['Nₑ(t) piecewise schedule','scenario presets: bottleneck, expansion, contraction, founder','window length in units of 4Nₑ'])

add(id='B1c',slug='ancestral-pipeline-state-ne-history',title='Was the ancestral pipeline empty or full at the split? (sourced Ne history)',side='day',branch='B',parent='B1',
 edges=[('depends-on','B1'),('attacks','B1a')],lb=(True,'decides whether the B1 deficit exists at all for the human-chimp case'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','pending'),
 quotes=[Q('EDU','The pipeline isn’t partially empty. It’s functionally nonexistent and empirically confirmed to be empty.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt',note='Day, replying to Mansfield'),
   Q('EDU','That’s absolutely wrong. The pipeline was full, but it was much shorter.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt',note='Same post, later UPDATE answering Mansfield\'s rejoinder; see B1d')],
 formal='''Question: sign and size of ΔK = K_true − μL·T for the human lineage given a sourced Nₑ(t) with ancestral Nₑ = 1.98e5 (human–chimp–bonobo ancestor) or 1.32e5 (human–chimp–gorilla ancestor) (Yoo 2025; `population.Ne_ancestral_hc.yoo_2025_HCB`, `.yoo_2025_HCG`) and PSMC histories (Prado-Martinez 2013; extraction pending, fidelity ledger "still to do").

Derived context (python3 -I): 4Nₑ_anc = 5.3e5–7.9e5 generations, i.e. 2.1–3.1 × T (252,000). Analytic B1b bound for a contraction to 1e4: μL·4ΔN = 30 × 4 × (1.98e5 − 1e4) = 22.6M > μL·T = 7.56M, so the bound saturates and a simulation is needed. HL itself places the census-scale era (8 billion) at ~400 generations of the 252,000.''',
 a_stated='Day: empty (IR §3, EDU first answer); Mansfield: full. Day later: full but 228,000 generations long (B1d).',a_impl='Nₑ history is the same on both lineages; PSMC and coalescent Nₑ(t) scale with the assumed μ and generation time (the circularity Day raises in B3h), so they are treated as inputs to compare under both values of μ, not as ground truth.',
 against=rq('MFC','Vox’s response was basically an assumption that at the time of split between humans and chimps the ‘pipeline’ as he calls it was empty.',file=None,loc='quoted inside Day\'s post (UPDATE)',sh='Mansfield, as pasted into Day\'s post of 2026-10-01'),
 support='Day: ancient-DNA data show "absolutely no advancement" of allele frequencies (branch C; not assessed here). RESULTS B1 caveat: an empty start contradicts observed diversity.',
 weak='Day\'s evidence for emptiness is the aDNA analysis (branch C) whose panel is ascertained on present-day variable sites (Mathieson 2015; C1 queued) and which uses Nₑ ≈ 10⁴ that Day himself calls circular (B3h). Mansfield offers no sourced demography.',
 lit=[lit_row('Yoo 2025','"we estimated that the human-chimpanzee-bonobo ancestral population size (average Ne = 198,000) is larger than that of the human-chimpanzee-gorilla ancestor (Ne = 132,000)"','verified (ledger)'),
      lit_row('Prado-Martinez 2013','"Inferred effective population sizes have varied radically over time in different lineages" (abstract only; PSMC curves not yet extracted)','unverified for numbers')],
 p_claim='Day (IR): E[count] ≈ μL(T − 4Nₑ) with a deficit of order μL·4Nₑ_eff for any Nₑ_eff reflecting expansion.',
 p_opp='Standard theory (B1b): from an equilibrium ancestral state, a later contraction gives an excess ≥ 0, constant Nₑ gives exactly μLT, only sustained expansion gives a deficit bounded by μL·4ΔN.',
 p_change='Proposed check **B1c** (not yet run): forward Poisson-thinning/Wright–Fisher runs with Nₑ(t) piecewise from Yoo ancestral Nₑ (1.32e5–1.98e5) to human-lineage PSMC Nₑ, lineage by lineage, reporting per-lineage fixed substitutions vs μLT and pairwise divergence vs 2μT+θ_anc. Sign pre-registered: if PSMC shows decline from ≥1.3e5 to ≈1e4 before the split-to-present window, ΔK ≥ 0 (excess), which falsifies Day\'s deficit for that scenario; a deficit appears only if Nₑ rises by ΔN with 4ΔN a sizeable fraction of T.',
 check='Script: proposed `research/checks/b1c_ne_history.py` (queued; seed to be fixed before the run) · Result: none yet. Related done checks: B1, B1b.',
 sim=['Nₑ(t) loaded from file (PSMC/MSMC curves) or presets from Yoo 2025','lineage-specific histories','start state','counting mode (fixed substitutions vs pairwise divergence)'])

add(id='B1d',slug='full-but-short-pipe-revision',title='Day (blog 2026-10-01): the pipeline was full but short (228,000 generations); 29-billion pipe at 8 billion',side='day',branch='B',parent='B1',
 edges=[('revises','B1'),('revises','B1c'),('revises','B1a')],lb=(False,'it concedes the full-pipe premise at the split; the remaining claim is the post-split lengthening, which is B2'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','pending'),
 quotes=[Q('EDU','At the time of the CHLCA split, we can assume that it was full and 228,000 generations long, so fixations can be reached around now.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('EDU','Back then, at the ancestral census of ~100,000, the pipe was 4Nₑ ≈ 228,000 generations long.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt'),
   Q('EDU','At census 8 billion, it’s 29 billion generations long.',file='day/blog-2026-10-01-the-education-of-a-population-geneticist.txt')],
 formal='''Day now grants a full pipe at the split, with transit 4Nₑ = 228,000 at census ~100,000, scaling with census thereafter.

**Arithmetic audit (derived, python3 -I):**
- 4Nₑ = 228,000 → Nₑ = 57,000 = 0.57 × census 100,000. This equals Wright's Nₑ = (4N−2)/(Vₖ+2) with Vₖ = 5: (4×10⁵−2)/7 = 57,143, 4Nₑ = 228,570 (Z22129121 p.4; human Vₖ = 5 in its Table 1). Census 1,000,000 → 2.2857M, matching "2.28 million".
- Census 8×10⁹ with the **same** Nₑ/N = 0.571 gives 4Nₑ = 1.83×10¹⁰, not 2.9×10¹⁰. 29 billion requires Nₑ ≈ 7.3×10⁹ = 0.91 N, the value in HL Table 3. Ratio stated/reproduced = 1.59. Inputs for the 8-billion figure are not stated in the post.
- Cross-paper: Z18525547 uses Nₑ = 3,300 for the same census range (N/Nₑ = 30 at N = 100,000); this post and Z22129121 imply Nₑ/N = 0.57 at the same census. The two cannot both hold.
- With a full pipe of length 228,000 against T = 252,000, IR's own formula (empty start) would give 30 × (252,000 − 228,000) = 720,000; the post asserts instead that the ancestral fill is delivered, so the IR deficit does not apply to the pre-expansion window.''',
 a_stated='Ancestral census ~100,000 and a full pipe at the split; the pipe lengthens with census thereafter.',a_impl='Nₑ/N ≈ 0.57 (Wright, Vₖ = 5); the lengthening post-expansion pipe is relevant to divergence accumulated before the expansion (it is not: the 8-billion era is a few hundred generations of 252,000).',
 against=rq('MFC','The ‘pipeline’ would have been full from the X generations preceding that point in time.','comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbRHJx-mRP2 (Mansfield)')+' (this post concedes the point at the split)',
 support='Day: "Only a relatively small number of fixations have taken place in 280 generations because those mutations were already in most of the modern European population from their common ancestors." (aDNA, branch C).',
 weak='Conceding a full pipe at the split removes the IR deficit for the divergence window; the post does not recompute 7.56M with a full pipe. Critics have not quantified post-expansion drainage either (B1b: saturating deficit after large expansions).',
 lit=[lit_row('Wright (Nₑ formula, via Z22129121 p.4)','Nₑ = (4N − 2)/(Vₖ + 2)','unverified (original not retrieved)')],
 p_claim='Pre-expansion fixed substitutions are delivered from a full ancestral pipe; post-expansion flux is depressed (B2).',
 p_opp='Full pipe at the split and a late (few-hundred-generation) expansion mean the 252,000-generation count is ≈ μLT with at most a small late deficit.',
 p_change='B1c run with Nₑ(t) reaching census-scale values only in the last ≈400 generations would confirm the opposing reading for the divergence count.',
 check='Script: none yet. Arithmetic computed in python3 -I (this session). Version-ledger entry proposed: B1 start state, empty (IR 2026-09-22) then full but 228,000 generations long (blog 2026-10-01).',
 sim=['census N(t)','Nₑ/N ratio or Vₖ','pipe length 4Nₑ(t) display'])

add(id='B1e',slug='chalub-2022-reading',title='Chalub 2022 shows k = mu is an asymptote / 1/(2N) is imported from Wright-Fisher',side='day',branch='B',parent='B1',
 edges=[('supports','B1'),('supports','B7')],lb=(False,'cited as support, not as a step in any calculation'),
 sourcing='firsthand',status='extracted',v=('pending','partial','pending'),
 quotes=[Q('IR','Chalub (2022), solving the neutral Kimura equation explicitly in terms of Gegenbauer polynomials, derives the time-dependent fixation probability as a series of exponential decay terms that converge to the steady-state value only as t → ∞.','§1 The Identity'),
   Q('CHB','Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model. It is not a result produced by the mathematics.',file='day/blog-2026-08-23-chalub-and-the-kimura-cancellation.txt')],
 formal='''Chalub 2022: PDE for a two-allele neutral population "without mutation or selection", classical solution decays; two point masses at the boundaries plus integral constraints (probability conservation, conservation of mean frequency) fix the split between fixation and loss. Day's reading: the 1/(2N) is imported, not derived.

Note (derived reasoning, not a verdict): conservation of mean frequency is the definition of neutrality (equal expected offspring), so it is the neutral assumption itself rather than an extra premise. Day's point that the PDE alone does not fix the boundary split is consistent with the paper's abstract.''',
 a_stated='The diffusion machinery cannot independently confirm P_fix = p₀.',a_impl='Chalub\'s model (no mutation, no selection) bears on k = μ only through P_fix and time-dependence; k also needs mutation input, which the paper does not model.',
 against='Ledger: math correct but the paper does not address the substitution rate k. The Day post itself says Chalub "gives no sign that he is even aware that anyone is contesting neutral theory".',support='The literature quote below confirms the integral-constraint structure.',
 weak='Day\'s own post also states the outcome: "Impose that assumption and the fixation probability comes out equal to the starting frequency", which agrees with the critics\' P_fix = 1/(2N) at the census start (B7); the same author later conceded N/Nₑ (B3g).',
 lit=[lit_row('Chalub 2022','"we consider a population of two types evolving without mutation or selection, the so-called neutral evolution"','verified-partial (ledger): relevant to finite-time P_fix, not to k vs μ'),
      lit_row('Chalub 2022','"Its solution is required to satisfy not only the equation but a series of conservation laws formulated as integral constraints."','accurate'),
      lit_row('Chalub 2022','"Finally, the time-dependent fixation probability is given by"','finite-time P_fix is given for a stated initial condition')],
 p_claim='If the 1/(2N) were an assumption absent from the mathematics, exact finite chains with a different offspring law could give a different P_fix.',
 p_opp='Any exchangeable neutral model has P_fix = p₀ by the martingale property; exact chains give 1/(2N_census) (keruru KR-02; B3 check).',
 p_change='A neutral, non-exchangeable model with E[Δp] = 0 but P_fix ≠ p₀ would support Day; none is in the corpus.',
 check='Script: none specific. Related: `research/checks/b3_N_vs_Ne.py` (B3).',
 sim=['neutral model class selector (exchangeable Cannings | non-exchangeable)'])
