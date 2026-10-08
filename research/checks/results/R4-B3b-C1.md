# R4 results: B3b/B3c (overlap + fluctuation) and C1/C6 (aDNA panel ascertainment)

Scripts: `research/checks/b3b_overlap_fluctuation.py` (seeds 20261008+, 16 reps, ~4 min), `c1_ascertainment_sim.py` (exact WF chain, seed 20261009 for MC checks, ~8 min), helpers `wf_b3c1.py`. Run with `research/.venv/bin/python -I <file>`. Pre-registered predictions are in each script docstring (copied from claim files, plus [R4] additions written before the first run). Not committed.

## B3b: Balloux & Lehmann (B&L) 2012 reproduced
Quote (B&L, "Fluctuating demography without overlapping generations"): "population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations". Model: individual-based, haploid, survivors sampled uniformly, newborn parents uniform, mutation at birth, infinite sites; theory = B&L eq (3) with pi_j = 1/N_j. B&L eq (8) transcription checked against generic eq (3) to 1e-9; eq (11) gives ks = 2 - N1/N2 = 1.667.

| Scenario | theory k/mu per step | sim (fixations) | z | k per mean generation time (theory) |
|---|---|---|---|---|
| A0 constant N, s=0 | 1.000 | 1.0016 +/- .0049 | +0.3 | 1.000 |
| A1 constant, s=0.5 | 0.500 | 0.5025 +/- .0033 | +0.8 | 1.000 |
| A2 constant, s=0.9 | 0.100 | 0.0990 +/- .0007 | -1.5 | 1.000 |
| B1 fluctuating {50,150}, no overlap | 1.000 | 1.0006 +/- .0061 | +0.1 | 1.000 |
| B2 5-state growth/bottleneck, no overlap | 1.000 | 1.0092 +/- .0067 | +1.4 | 1.000 |
| C1 {50,150}, overlap s=.5 (feasible) | 0.4583 | 0.4582 +/- .0031 | 0.0 | 0.815 |
| C2 B&L eq (11) extreme | 0.4167 | 0.4149 +/- .0021 | -0.9 | 1.111 |
| C1x3 (all N x3, scaling check) | 0.4583 | 0.4590 +/- .0018 | +0.4 | 0.815 |
| C3 Beverton-Holt cycle + total-adult-death bottleneck | 0.2639 | 0.2637 +/- .0012 | -0.2 | 1.106 |

Predictions (i), (ii), (iii) confirmed; B&L's eq (3) is reproduced by independent simulation (all |z| < 1.6). The control and the no-overlap fluctuation cases give k = mu exactly, so "fluctuation alone" does nothing.

### Human-like magnitude and sign (exact eq 3; s = 0.96/yr, generation 25 y)
- Symmetric exponential growth/decline cycle with feasible constant survival: ks = k/(mu(1-s)) = 0.9997 (0.5%/yr), 0.9969 (1.6%/yr), 0.989 (3%/yr), 0.982 (3.9%/yr; this row uses a hard-coded cycle length L = 40, so its range is e^(0.039*39) = 4.6x, not 3.28x; no effect on the value). Matches 1 - (s/(1-s))(cosh r - 1). Effect is -0.3% to -2%: far below simulation resolution and nowhere near 26%.
- Day's one-way window (2.5 -> 8.2 over 75 y, 1.6%/yr): the arrival rate of eventual fixers is **raised** by 1.38x during growth (births/N = 1 - s/(1+r) = 0.0551 vs 0.040). Total excess over the whole episode is s ln(8.2/2.5) = 1.14 units of U, one-off.
- Growth then total-adult-death bottleneck (B&L eq 14 type, contrived): ks = 1.69.
- Two-state scan, N2/N1 = 3.28, feasibility s21 <= N1/N2: ks in [0.59, 1.70]. Biologically ordered survival (higher when growing): [0.83, 1.70]. ks < 1 needs survival high in contraction and low in expansion, which B&L call unrealistic. B&L's own conclusion (quoted): "under biological realistic situations ... the effect will generally translate into an acceleration".
- Overall range: sign mostly positive for realistic expansions, slightly negative (<2%) for symmetric cycles; magnitude from -2% to +70% only in contrived bottleneck cycles. Day's 0.743 sits within B&L's attainable set only for the unrealistic survival ordering (min 0.59), and not for human-like parameters.
- Caveat: "per mean generation time" (k * N/births) is not exactly 1 under strong fluctuation (0.81 to 1.11 in C1/C2/C3). Lehmann 2014 (not retrieved) uses a finer definition; this is an open item, not a Day win, because Day's formula is not this effect.

## B3c: RRME k = mu (sum N^2/sum N)/N_t
- Arithmetic reproduces: 0.7428. Window dependence confirmed: 2 cohorts 0.868, 3: 0.780, 4: 0.720 (at the paper's geometric ratio 1.486), 6: 0.653, 10: 0.609, 20+: 0.598. Closed-form limit 1/(1+1/g) = 0.598 at g = 1.486 (-> 1 as g grows; -> 0.5 as g -> 1, i.e. slow growth). Claim file's 0.60-0.87 range confirmed. 0.743 is a property of the chosen 4-cohort window, not of the population.
- Mechanism test (RRME assumes fixation probability 1/(2N_t)). Non-overlapping WF with cohort sizes x10, single mutant born in cohort i: P_fix*M_i = 0.989 +/- .011, 0.973, 1.018, 0.986 (martingale prediction 1); Day's implied 0.305, 0.488, 0.744, 1.0. With overlap (s=.96, growth 1.6%/yr, 100 -> 328): P_fix*N_0 = 1.034 +/- .026 vs Day-type 0.305. Fixation probability is 1/N at birth; RRME's step "frequency 1/(2N_t)" is falsified. (The mapping "RRME assumes fixation probability 1/(2N_t)" is the audit's reconstruction of Day's derivation from Z18525262 eq. 1 and 3; to be confirmed against the quoted equation.)
- B&L comparison: Day says RRME "confirm[s] Balloux and Lehmann's finding". Sign is opposite: B&L-type growth effect is an increase (+38%), RRME a decrease (-26%). 0.743 does not appear in B&L.

## C1 / C1a / C6
Method: exact neutral WF chain (scaled N_s=1000, f=10, theta=4 Ne mu = 4.8e-4 fixed), Ne=1e4 (parameters.yaml, unverified; keruru temporal 8.1k-9.8k), window 280 gens (7,000 y/25), equilibrium SFS theta/i, Z23046531 sample sizes (v62: 1372 Neolithic / 680 modern; v66: 395/441), "newly 100%" = either allele reaching 100% in modern sample while not 100% in Neolithic sample (Z23046531 §2.4: "Fixation was defined as an allele reaching 100% frequency in the modern period"). Designs: D1 same-population MAF>=5% in 2,345 diploids (array-like); D2 site heterozygous in one African male (Haak 2015 "discovered as heterozygous in a Yoruba male"); D3 African MAF>=5% in 100 diploids. Split time 2000 gens is an ASSUMPTION (not in parameters.yaml); result varies 12.5k-15.3k for 3000-1000.

Validation: scaling N_s=500/2000 gives D2 totals within 1% (50-90% band varies +/-25%, tail-sensitive); independent forward MC of the whole D2 pipeline agrees with the chain algebra (total 1.202e-2 vs 1.178e-2; 90-99% z=-0.3, >=99% z=+1.6); unscaled N=1e4 MC vs scaled chain for sample-100% probability differs 4-7% in the tail (z 2-4, scaled overestimates); flux ratio fix/(mu G) = 1.034 (N_s=1000), 1.021 (2000): P1 pre-registered 2% only met at N_s=2000.

Counts on the 1,143,671-SNP panel, Ne=1e4, G=280, v62 sizes:
| Design | newly-100% (sample) | of which 50-90% start | true population fixations |
|---|---|---|---|
| D1 MAF>=5% same pop | 0 (1e-29) | ~0 | 0 |
| D1b polymorphic in 2,345 same pop | 7,574 | 0.017 | 0 |
| D2 African single male het | 13,807 | 0.038 | 1,135 |
| D3 African MAF>=5% | 18,157 | 0.043 | ~1,400 |
| observed v62 / v66 | 17,806 / 3,469 | 1 / 3 | not defined |
Blog-style event (<10% -> >90%): ~1e-48 under all designs. New-in-window mutations fixing inside the window: 5e-151 per site (P2 confirmed): essentially all mu*G fixations are completions of standing, mostly >90% variants.

- **Enrichment (C1a sign):** D2/D3 enrich the 10-90% start bands by 1.2-3.4x but suppress the >=90% bands by 5-30x (total per-site event rate 0.05x of all polymorphic sites). D1 (same-population MAF threshold) suppresses to zero. So C1a's sign is right only for intermediate starts under African discovery, and the effect is a factor of order 1-3, immaterial because the absolute count there is ~0.04.
- **Observed 50-90% completions (1 and 3):** expected 0.04 (v62) and 0.11 (v66) at Ne=1e4; they equal expectation at Ne ~7,000 (1.55 / 2.76); at Ne=5,000 expected 22. Tail extremely Ne-sensitive. With a single closed population the observed 1 and 3 are mild anomalies at Ne=1e4 (Poisson P(>=3 | 0.11) = 2e-4), attributable to admixture/error (not modelled) or Ne near 7-8k.
- v62 total (17,806) is within 1.3x of D2 (13.8k) and D3 (18.2k); v66 (3,469) is 3.8x below the prediction (13.3k), unexplained (filtering/annotation).
- **Statistic identity.** The observed 17,806 / 3,469 / 1 / 3 are Z23046531's two-period (Neolithic vs modern) statistic. C6's "21 fixations after 7000 BP" is Z18525185's first-passage-in-time-bins statistic, which this chain does **not** simulate; it was simulated separately in C1b (`R4-C1b.md`), which supersedes this section for C6.
- **C6 denominator:** 630 = 150M x 1.2e-8 x 350 verified. Uniform scaling to 1,233,013 sites = 5.2 (a random-site sample gives 5.3 true fixations by chance; my chain gives 5.33). But the panel is not random: fixations occur at previously polymorphic sites and the panel is polymorphism-ascertained, so the model expectation of true fixations on the panel is ~1,500-1,850 (D2/D3, 350 gens), and sample-level newly-100% events ~18-24k. So neither "630 expected" nor the critic's 5.2 is the right comparator for a polymorphism-ascertained panel. The ~1.5e3 figure is not comparable with the 21 either, because the 21 is a first-time-100% count in post-7000 BP bins (Day's definition, not modelled here). The earlier sentence "this does not rescue Day" is withdrawn as unsupported (correctness review MAJOR): this chain cannot say whether the 21 is a deficit or not. See C1b.

## Suggested verdicts (internal / fidelity / external)
- **B3b:** internal: holds (B&L effect exists, reproduced); fidelity: partial (B&L effect real but Day's use of it for k=0.743 or 32.3 is not in the paper; B&L sign for realistic demography is upward); external: effect size at human-like parameters -2% to +38% transient, not -26%; cannot give 0.743 or 32.3.
- **B3c:** internal: arithmetic holds but derivation fails (fixation probability taken as 1/(2N_t); simulation gives 1/(2N_i)); fidelity: misread/not in B&L (opposite sign); external: 0.743 is a window artefact (0.60-0.87, limit 0.598). Verdict: refuted by direct simulation.
- **C1:** internal: critic's point 1 (new substitutions not on panel) holds trivially, and stronger: new-in-window fixations are ~0 genome-wide anyway; point 2 sign: mixed (C1a right for 10-90% bands by factor 1-3, wrong for >=90%); fidelity: accurate (panel built on present-day polymorphism; Haak African-male discovery); external: v62 panel counts are neutral-compatible (D2 within 1.3x of v62 observed); v66 is 3.8x below the model, unexplained.
- **C:** (Z23046531's two-period statistic, not the Z18525185 21-count) headline "0 from <50%, 0-3 from 50-90%" is the neutral expectation at Ne ~1e4 (0.04-0.11) up to Ne ~7k (1.5-2.8), so it does not discriminate; 1 and 3 mildly high (admixture/error).
- **C6:** internal: arithmetic-error stands (denominator mismatch), but the repo's own 5.2 rescaling is also wrong for an ascertained panel; external: unresolved here (the 21-count statistic is not simulated in this chain). C1b then simulated it: not reproducible from the published procedure; cannot adjudicate.

## Both steelman positions on C1/C1a/C (recorded, not adjudicated beyond the numbers)
- **Day-side (REVIEW-R4-steelman-day):** C1a's sign is right for the 10-90% start bands Day's headline uses (African discovery enriches them 1.2-3.4x); the >=90% suppression is irrelevant to that headline. The headline test has no power because neutral also predicts ~0 there. The 1 and 3 observed 50-90% completions are anomalies at Ne = 1e4 (P = 2e-4) and their attribution to admixture/error is an assumption, not modelled. v66 (3,469) is 3.8x below the model, unexplained. The tail is extremely Ne-sensitive (Ne 7k-10k spans 1.5 to 0.04), and Ne = 1e4 is an unverified input that Day calls circular (B3h/C5a).
- **Critic-side (REVIEW-R4-steelman-critic):** the observed 1 and 3 exceed the Ne = 1e4 expectation, i.e. the direction is *faster* than neutral, not a stopped clock. C1a's mechanism is wrong in sign for the same-population design D1 (zero) and for the >=90% bands where most true completions live. Panel ascertainment raises the expected true fixations on the panel far above 5.2, so the 630-vs-21 shortfall collapses on its denominator. The 630 arithmetic itself (150M x 1.2e-8 x 350) is correct.
- **Status:** the dispute over the 21-count is superseded by C1b (not reproducible; cannot adjudicate; call-depth follow-up queued).

## Review corrections applied (REVIEW-R4-correctness, steelman reviews)
1. MAJOR: C6 "does not rescue Day" withdrawn; the 21-count statistic is stated as not simulated here; the v62/v66 comparator is restricted to Z23046531's statistic; C1b supersedes.
2. MINOR: r = 0.039 row range label (4.6x, not 3.28x); B3c limit direction (-> 1 as g grows); RRME mapping marked as a reconstruction.
3. MINOR: the panel denominator omits African-private post-split mutations, so per-panel counts are a slight upper bound (likely a few percent); the 3.4% flux excess comes from the theta/i starting SFS (tail bands carry 4-25% error).
4. Both steelman positions recorded above.

## Caveats
Single panmictic population with constant Ne=1e4, no admixture/structure/selection, unlinked sites, no genotype error or missing data; split time and African Ne assumed equal; discovery designs simplified (no 610-Quad/archaic panels; true panel is a union); sample-level band classification uses the Neolithic sample only; discretisation error 2-7% (tails up to 25%). B&L model: haploid, no senescence, parent choice uniform; per-generation-time normalisation not Lehmann 2014's exactly; human-like cases are analytic (eq 3 validated by simulation elsewhere). Python 3.14 multiprocessing used (forkserver).
