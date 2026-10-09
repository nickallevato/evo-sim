# REVIEW R4-D1: critic-side steelman

Reviewer role: argue as strongly as honestly possible for Day's critics (Camestros, McCarthy, Rosenhouse, Mansfield, Nesslig20, Bowers, KITTENS), then judge whether `R4-D1-spike.md` gives them their due. Read: `R4-D1-spike.md`, `d1_sequence_space_spike.py`, `d1_posthoc_refine.py`, `d1_posthoc_gb1_snv.py`, `raw/d1_aggregate.txt`, `raw/d1_posthoc.out`, `raw/d1_gb1.json`, `raw/d1_posthoc_gb1_snv.json`, `R4-G1.md`, claims D1, D1a, D1b, D1c, D1d, D2h, D2i, D9a, and `quotes-critics.md`. Nothing under `sources/raw` was opened. No file other than this one was edited. Line numbers below refer to `R4-D1-spike.md`.

Where I do arithmetic of my own it is marked "(reviewer arithmetic)". Where a number comes from memory rather than the corpus it is marked "(from memory, unverified)".

## Overall judgement

The measurements look sound and mostly well labelled. The write-up credits the critics in the right places, but it does so in a §6 list and not in the headline. Its two main conclusions need re-scoping, for four reasons.

1. "Locus- and exact-outcome alternatives sit far below the flip, so Day's p^n regime stands" is largely true by construction. The classes behind it (exact MFE structure; tolerance at one codon) are the specific-outcome reading itself. They are not tests of the critics' claim.
2. The measurement that does match the critics' claim (an any-n-of-M comparison against a measured beneficial fraction) was pre-registered as P10 and then never reported against G1's requirement.
3. "Far below" rests on s·T = 3,000. The sensitivity is shown only downward (s = 0.001).
4. The multi-step neutral-exploration argument is dismissed by a one-line label ("population quantity") and never turned into a calculation, either for or against.

The critics are not named once in the write-up. Their specific-versus-any argument (Camestros CA-09, McCarthy MC-02) is never connected to what was measured. Critic errors are recorded once (the "strong form" sentence), and that sentence has no quoted source.

---

## MAJOR findings

### M1. "Exact structure S2" is Day's specific horn by construction, so "Day's p^n regime stands there" is close to a tautology

Quote, §0 bullet 1 (line 27): "**Site-level or exact-outcome needs sit well below the flip.** Every exact, ≤2 bp, or non-degrading-topology RNA class and every single-codon DMS class has λ of about 1–6, against a flip of 7–17. At those granularities Day's p^n regime stands (G1: P ≈ 10^−176 for n_f = 1e3 at λ = 1.1)."

Quote, §6 (line 245): "The p^n regime is binding if the n_f requirements are site-specific."

- **What m_E0 is.** The script's own definition (`d1_sequence_space_spike.py` docstring, DEFINITIONS): "number of distinct single-nucleotide mutants of a genotype x … whose MFE structure is EXACTLY a named target S2 … 'Specific outcome' reading." So E0 is G1's m = 1 horn, re-measured at the phenotype level. Finding m∣reach = 2.3 instead of 1 is useful. Concluding that the "specific-outcome regime stands" from it is circular.
- **What the DMS "one codon" row measures.** The row (line 20) is "Functional alternatives at one codon (nonsynonymous SNVs, s*≥0.5) … 5.1 of 7.0". That is the number of substitutions the site tolerates. It is not the number of alternative ways to supply a benefit.
  - A tolerated substitution at the WT codon is, in Day's G3b words, "neutral noise" (R4-G1 §1, G3b: "they're interchangeable — in which case they're neutral noise that can't explain the observed functional divergence").
  - The same row cannot also be the measure of "alternatives to a needed change". The write-up uses it for both, to conclude "below".
  - The class that matches an adaptive need is the beneficial proxy, which sits on a different row.
- **The critics' claim is not a claim about m per locus.**
  - Camestros (CA4 para 10, 2026-01-29): "the probability that SOME number is picked is close to 1".
  - McCarthy (MC1 para 48): "our evolutionary history does not require that an exact group of 20 million mutations become fixed—only that some 20 million out of an enormous pool of candidate mutations become fixed."
  - Both argue about which loci, drawn from a pool M. R4-G1 §3 formalised this as "any n of M" (P_any) and found the pool requirement is 1.7e-5 to 4.3e-4 of new mutations for n ≤ 2e5.
  - The D1 write-up never mentions this argument or its authors. It measures only the middle-case m per locus.
- **Suggested fix.**
  - Re-title §0 bullet 1 along the lines of: "When the requirement is defined as one named outcome (or as tolerance at the same codon), alternatives per change are 2–5. This reproduces Day's horn at m ≈ 1–5; it does not test whether requirements are site-specific."
  - Add a column "tests: Day's horn / critics' middle case / critics' any-n-of-M" to the §0 table.
  - Add one sentence stating that the specific-versus-any question (Camestros, McCarthy) is untouched by D1 and rests on G1 §3.

### M2. The pre-registered "any n of M" comparison (P10) is not reported

Quote, docstring P10 (`d1_sequence_space_spike.py`): "beneficial proxy fraction (s*>=1.2) 0.5-6% of singles (upper bound), compare to G1's required beneficial fraction 2e-5..4e-4 (n_f <= 2e5) and 2e-3..4e-2 (n_f = 2e7)".

Quote, write-up §4.1 (line 172): "Beneficial proxy fraction (s* ≥ 1.2, upper bound) | 3.6% [0.6–9.2] | 0.5–6%". The scorecard (line 224) says "P10 … **Held** (3.6%)". §6 never makes the stated comparison.

R4-G1 §3 closed on: "The DFE evidence that would settle this is not in the corpus." D1 produced the first measured DFE proxy in the corpus. The comparison is therefore the most decision-relevant output of the spike for the critics, and it is missing.

Reviewer arithmetic, using G1 §3's required-fraction table (supply 4.5e11 or 2.3e11):

| n required | p | Required beneficial fraction | 3.6% over required |
|---|---|---|---|
| ≤ 2e5 | 0.02 | 2.2e-5 to 4.3e-5 | 840× to 1,600× |
| ≤ 2e5 | 0.002 | 2.2e-4 to 4.3e-4 | 84× to 160× |
| 2e7 | 0.02 | 2.2e-3 to 4.3e-3 | 8× to 16× |
| 2e7 | 0.002 | 2.2e-2 to 4.3e-2 | 0.8× to 1.6× |

- This is the input G1's any-n-of-M result needed. It should be stated whether or not it favours the critics.
- Honest limits that must travel with it:
  - The 3.6% is an upper bound (assay noise).
  - It is measured inside genes chosen for function, in lab assays.
  - A genome-wide fraction is the within-gene fraction multiplied by the share of the genome that can matter.
  - Illustratively, for a share of 1% the product is 3.6e-4, which is still inside the 2.2e-5 to 4.3e-4 band for n ≤ 2e5 (reviewer arithmetic; the 1% is illustrative, not sourced).
  - Nothing here covers noncoding or regulatory sequence (D15), which the write-up lists as open.
- **Suggested fix.**
  - Add a §6 item 2b: "Any-n-of-M, direct comparison", with the table above, the noise and genome-share caveats, and the statement "this comparison was pre-registered (P10) and was omitted from the first write-up".
  - Say which side it helps. On these numbers it favours the critics for n ≤ 2e5 and is borderline for n = 2e7 at s = 0.001.

### M3. The gene-level beneficial row is the one DMS quantity that matches "needed change = improvement", and it is under-weighted against an easier flip threshold

Quote, §0 bullet 2 (line 28): "**Gene-level "any beneficial change in this region" needs sit at or above the flip, but the number is soft.** It is an upper bound (assay noise inflates it), it depends on s and T, and it changes the unit of a "required change" from a locus to a gene."

Quote, §6 (line 246): "If one gene-level need counts as one requirement, n_f is also limited by the number of genes, so the relevant λ₅₀ is lower than 17.2."

- **The threshold is lower than the one shown.** The sentence says "lower" and stops. With about 2e4 genes, λ₅₀ = ln(n_f/ln 2) = 10.3 (reviewer arithmetic: ln(2e4/0.6931) = 10.27; gene count not sourced in the corpus). The write-up's table compares λ ≈ 24 to 12.3–17.2. Against ≈ 10.3, λ ≈ 24 is about 2.3 times the flip. Even the d-corrected T value of 12 sits above it.
- **Two noise directions, one applied.** §7 (line 280) tags the beneficial proxy "Favours Day … upper bounds" because of measurement noise. §7 (line 279) separately says lab assays are "saturating selection, WT buffered by design". A ceiling at WT hides improvements, so it biases the beneficial count down. The second effect is not applied to the beneficial row. It should appear as an opposing bias, or the row should be called "bracketed" instead of "upper bound".
- **Heterogeneity and the 0.** The range [0–1,760] (line 22) means some genes offer none. G1 §3 says the sharp flip "holds only for homogeneous λ". The write-up does not say what share of datasets have zero beneficial SNVs. That share matters for a per-gene product and should be given. It does not help the critics.
- **Suggested fix.**
  - Add a column to the §0 table: "λ₅₀ for n_f = number of genes".
  - Report the share of datasets with m_gene,ben = 0.
  - Present the saturation bias alongside the noise bias.
  - Reword §0 bullet 2 to "at or above the flip on the Day-family basis; below it at s = 0.001", which is more informative than "soft".

### M4. "Far below" is one-sided in s, and λ is exactly linear in s

For the Day-family basis, λ_alt = −ln(1−q) = 2N(μ/3)T·2s. Check: 2·1e4·(1.2e-8/3)·3e5·0.02 = 0.480, matching the 0.48 in line 3 (reviewer arithmetic). So λ scales exactly in proportion to s at fixed N, μ and T.

The sensitivity reported runs only downward (s = 0.001). It is not run upward. For the DMS one-codon class (m = 5.06):

| s | λ | G1 flip for n_f = 1e3 | G1 flip for n_f = 1e4 |
|---|---|---|---|
| 0.01 | 2.4 | 7.3 | 9.6 |
| 0.03 | 7.3 | 7.3 (at flip) | 9.6 |
| 0.05 | 12.1 | 7.3 (above) | 9.6 (above) |

- The write-up's §0 statement "λ of about 1–6, against a flip of 7–17" holds for s ≤ 0.01 and Day's p = 0.02. It is not robust to s of 0.03 to 0.05.
- At larger s the Haldane 2s approximation overstates q. So 0.05 is a stress test, not a prediction. The point is that the conclusion carries an unstated s ≈ 0.01 qualifier.
- R4-G1's m* table shows the same one-sidedness: there are rows for 0.001 only.
- I do not claim s = 0.05 is typical. I claim the write-up cannot say "far below" without stating the s range over which it holds.
- **Suggested fix.** Add the upward s column to the §0 table or to §6. State "far below for s ≲ 0.01; at the flip near s ≈ 0.03 for one-codon DMS at n_f ≈ 1e3". Say that this is a model-dependence, not a measured fact.

### M5. Multi-step neutral exploration is not measured, and the "pooled" numbers are dismissed in one line while mixing two different quantities

Quote, §0 (line 24): "Pooling over the K = 40–60 neutral genotypes I sampled raises the RNA counts: exact S2 2.1 (uniform) to 30 (frequency-weighted); topology-class E2g 207; E2rare 43. That is a population quantity (it presumes many distinct neutral genotypes segregating at once), not the per-genotype m."

- **Critic argument.** The network has 10^33 members spread over 0.56·L positions on average (line 91). Single-step reach is 1.8% for E0 and 59% for E2g. A population does not sit on one genotype. Waiting for a permissive background is a first-passage problem on the network, and the write-up measures only the ingredients: ν = 0.30, spread 0.56L, reach per genotype.
- **Pooled counts compared with the flip.** On the Day-family basis m* = 15 (n_f = 1e3) to 36 (n_f = 2e7). The pooled medians are: E0 frequency-weighted 30 [8–100] (`d1_aggregate.txt`, E0_freqw `mpop(K=KB)`), E2rare 43, E2g 207. All are at or above m* for most n_f. Only the uniform E0 value (2.1) is clearly below. None of this appears in the §0 table.
- **A defect in the pooled figure, which must be stated.** Pooling is not a valid multiplier on λ. If K backgrounds partition a population of N, a route in background k is supplied at rate proportional to its frequency f_k. So the expected number of successful arisings is λ_alt·Σ_k f_k·m_k, a frequency-weighted mean of per-genotype m, not their sum (reviewer arithmetic). The correct unconditional quantity is therefore `m_all` (E0 uniform 0.05; E0 frequency-weighted 0.53; E2 uniform 24.9, `d1_aggregate.txt`), and the headline "m∣reach" is conditional on the route existing. Both directions of this error exist in the write-up. Calling the pooled figure a "population quantity" does not say that it overstates.
- **A fact that cuts against the critics.** At Day-family per-site μ, a 76-nt locus acquires about 76 × 1.2e-8 × 3e5 ≈ 0.27 mutations over the window, fewer still neutral, so a single lineage cannot walk far across the network, and standing diversity in so short a region is thin (reviewer arithmetic). Neutral-network exploration therefore needs many loci in parallel, or larger μ·L (bacterial or viral scale), to matter. The critic argument is valid in principle but can fail at the parameters under test.
- **What is missing.** A time-resolved calculation. `neutral_walk` already exists. A first-passage run would yield: the expected number of neutral substitutions until a background with a route to S2 appears (about 1/reach ≈ 55 for E0, about 2 for E2g). That could be set beside μ·ν·L·T and the standing-variation supply. It could favour either side, and it is the calculation the critics' argument needs.
- **Suggested fix.**
  - Replace "population quantity" by one sentence on the supply-sharing problem and on whose side the unconditional m_all falls.
  - Add the first-passage run, labelled post hoc.
  - Put the frequency-weighted pooled E0 value in the §0 table with the caveat.

### M6. E2rare is low by construction; the refined classes were chosen after the E2 result; the headline gives E2g and E2rare equal weight

Quote, §0 table (line 18): "Same topology, rare shapes only (post hoc E2rare) | RNA | 4.5 [1–6.6] | 21% | 2.2 | below".

Quote, `d1_posthoc_refine.py` header: "E2rare : shape5(S2) != shape5(S1) AND that shape accounts for <= 1% of all non-neutral neighbour instances of the A-sample".

- **Selection effect.** E2rare selects S2 from shapes that are seldom reached in the sampled neighbourhoods. The measured m on independent genotypes B is then small because the class was chosen for being seldom reached. Its use as a "topology-equivalent" bound for what evolution needs is a selection artefact in the Day-favourable direction. The write-up flags the E2 artefact (lost helices) at length in §3.3 and does not flag this one.
- **E2g is the defensible class.** It excludes helix loss, which is reasonable. Its numbers (m∣reach 7.2; L ≥ 76: 11.8; λ 3.4 and 5.7) are on the table. But the per-target output for L = 100 shows `mean_all` (unconditional) of 14.96, 7.53 and 19.67 for E2g (`d1_posthoc.out`), i.e. λ about 7.2, 3.6 and 9.4 at the Day-family basis. For n_f = 1e3 (flip 7.3) and 1e4 (flip 9.6), two of three L = 100 targets are at the flip. The write-up reports "One L = 100 target (rand100_2) reaches m∣reach 25 and λ 12.2, the lower edge of the flip band" and summarises "below". Real proteins have hundreds of sites, so the L trend belongs in the headline.
- **The refined classes were designed after seeing E2.** They are labelled post hoc, which is correct. The write-up should say that the refined definitions were chosen to remove the one critic-favourable result (E2 = 13.4, "in the band"), and that the filter was not applied to any Day-favourable result.
- **Suggested fix.** Flag E2rare as a selection artefact. Give E2g m_all and λ by L. Move the L ≥ 76 E2g line to the §0 table.

---

## MINOR findings

### m7. GB1: the criterion "reach the global maximum" is the exact-outcome reading again, and critic-favourable GB1 numbers are not quoted

Quote, §4.2 (line 195): "Functional variants with a strictly uphill path to the global maximum | **98.5%** | **44%**". Day credit (line 200): "At SNV granularity, 56% of functional variants cannot reach the best variant by a monotone path."

- **Wrong benchmark for evolution.** Evolution needs a good variant, not the single best. The global maximum here is 8.76× WT (`d1_gb1.json`, `global_max_fitness`).
- **What the JSON shows and the text does not quote.** `frac_functional_with_improving_nbr_SNV` = 0.985: 98.5% of functional variants have a strictly improving SNV neighbour. Local maxima are 87 of 5,822 (1.5%). The write-up reports the 87 but not the 98.5%.
- **The WT's own single mutants.** `wt_singles_frac_ge1.2` = 0.197, i.e. about 15 of the 76 single mutants beat WT by the beneficial-proxy threshold. `wt_singles_frac_ge0.5` = 0.355. The write-up quotes the Day-favourable 53% below 0.2 (line 199) and omits the critic-favourable 20% beneficial and 36% functional. (Both are for one subspace chosen for epistasis, §7 line 282.)
- **Missing outputs.** The fitness distribution of the 87 local maxima; and the share of functional variants that can reach any variant with fitness ≥ 1 or ≥ 1.2 by a monotone SNV path.
- **Suggested fix.** Add those outputs and the 98.5% and 20% figures. Tag "reach the global maximum" as an exact-outcome criterion. Keep the Day credit for the 87 maxima and for the 44%.

### m8. Walks "never get stuck" are a known-target construction (D2i); the write-up does not say so, and no walk was run on a measured landscape

Quote, §3.4 (line 151): "Trapped with no move: 0 in every case." The RNA fitness is "minus the base-pair distance to S*" (line 137).

- **D2i applies.** Fitness = −d_bp to a named S* is a programmer-defined target (Day, D2i: "it works because Dawkins specified the target string, the fitness function, and the selection rule"; D9a quotes the same objection). The RNA walks are Weasel-like. The write-up concedes only the "bookkeeping" problem (line 148), not the D2i objection.
- **The claim files name the decisive test.** D1b: "Result that would change a verdict: success of selection on an empirical, designer-independent landscape (DMS-derived)." D2i: "success/failure on DMS-derived landscapes (D2h step S2/S3)". The spike has such a landscape (GB1, complete) and no walk on it. Only reachability was computed (m7).
- **Fix for the critics' benefit.** Run random-uphill and greedy walks on the GB1 SNV graph from WT and from random functional starts. That is the D1b/D2i test and the cheapest way to turn "no strict traps" from a known-target result into a measured-landscape result.
- **Fix for balance.** In §6's critic credit, add "(known-target fitness; see D2i)" to the RNA walk item.

### m9. Critic-favourable results sit in §6 "Credit", not in §0 "Reading, kept neutral"

Quote, §6 (lines 258–264): "The neutral networks are enormous: 10^33 sequences for a tRNA cloverleaf, spread across sequence space. Destroyed singles are a median 11% (a majority in 2% of datasets). Fully intolerant sites are rare (4%). The functional set in GB1 is one giant component. The RNA graded landscape has almost no strict traps away from the target…"

- The same facts have no line in §0. §0 bullets 1–3 contain three sentences: "Day's p^n regime stands", the soft gene-level reading, and "Neither side's strong form is supported".
- The Day-favourable facts (70% of RNA singles change the structure; 95% of GB1's four-site space is nonfunctional; 87 local maxima) are likewise only in §6. So the placement is symmetric.
- A reader who stops at §0 still leaves with the Day-favourable reading, because it is the only substantive bottom line. The gene-level critic-favourable reading is hedged as "soft" (M3).
- **Suggested fix.** Add one balanced bullet to §0: "Connectivity: neutral networks are huge and spread (10^33, 0.56·L); 71% of DMS singles functional; GB1 functional set 99.8% one component; 'destroy' is not supported (11%). Ruggedness: 70% of RNA singles change the structure; 87 local maxima in GB1; 95% of the four-site space is nonfunctional."

### m10. "Neither side's strong form is supported": the critics' "strong form" is unsourced

Quote, §0 (line 29): "The critics' "plenty of interchangeable alternatives, so the barrier vanishes" is not supported at the locus level."

- No critic in `quotes-critics.md` is quoted saying this. The nearest are Camestros CA-09 (any number is picked), McCarthy MC-02 (some 20 million out of a pool) and Bowers (R4-G1 §7: "Multiple mutational paths can lead to similar phenotypes", secondhand). None quantifies m per locus.
- A reader will take "the critics' strong form" as something a named critic said. If no one did, the sentence records a critic error that nobody made, which is a fairness problem under the project's "record critic errors" rule.
- **Suggested fix.** Either quote a critic with a locator, or reword to "an unstated middle-case premise (m ≥ m* per locus)". Keep, as a separate valid point, that Bowers' "multiple paths" is supported qualitatively (m∣reach 2–5 for exact structures; more under looser equivalence).

### m11. Claims D1, D1a, D1b, D1d, D9a, D2i are not listed as touched, and D1a's pre-registered test is answered without credit

Quote, the header (line 5): "Claims touched or informed: D, D2h (directly), D2c, D3, D4, D10–D12, D15 (context), and the G3b dilemma."

- **D1a's own prediction.** D1a (Rosenhouse p.124): "published measurements of protein-space geometry (e.g. neutral-network sizes, fraction of functional single mutants) show connectivity sufficient for selection." D1 now supplies exactly those: 10^33 network, 71% of singles functional, a 99.8% GB1 component. At the level of local connectivity, "their results make Eden's simplistic combinatorial calculations look hopelessly naive" (Rosenhouse, D1a) is partly borne out.
- **What D1 does not support.** The same D1a sentence is an unquantified overstatement of what D1 can show. D1 measures one-step neighbourhoods of extant optimised proteins and does not touch Eden's cross-family 20^250 sequence arithmetic (the write-up says so at line 281). So D1a deserves: credit for the direction; a record that "hopelessly naive" goes beyond the evidence.
- **Other claims.**
  - D1b: the RNA part is known-target (m8); the GB1 part has no walk.
  - D1d (Camestros): D1's DMS and GB1 data are the "developments since 1966" he asks about; the D1d external verdict could cite them.
  - D2i and D9a: shared issue with m8.
- **Suggested fix.** In §9, add suggestions for D1a (external stays `contested`, with a note that local connectivity is supported and the cross-family claim is untested), D1b/D2i (landscape-provenance caveat), D1d (post-1966 literature now harvested). No claim file should be edited by the reviewer.

### m12. The bias-direction table (§7) uses "Favours X" without defining it, and one row points the wrong way under its own convention

Quote, §7 (line 278): "Single genotype per m. Real populations carry many neutral variants. | **Favours the critics** (pooled counts are tens to thousands)."

- By the convention used elsewhere in the table, "Favours X" means the artefact flatters X. For example "Equal s is assumed … **Favours the critics** (flatters m)" and "Structure identity is a stricter definition … **Favours Day** … (m too low)".
- A per-genotype m understates the population-level supply. That is an artefact that flatters Day, not the critics. The row conflicts with the convention (or with M5's correction that pooled counts overstate).
- The row on S2 being drawn from accessible structures (line 276) is correctly an inflation of reach in the critics' direction, but a reader cannot tell, because "Favours the critics" can also read as "this consideration helps the critics".
- **Suggested fix.** Add one line defining the convention ("Favours X = the measurement artefact makes X look better than it is"). Re-tag the single-genotype row, and net the rows into a short "net direction of the measurement bias" summary.

### m13. Neutral-network connectedness: the write-up understates what the sampling method shows

Quote, §3.1 (line 91): "The network is spread across sequence space. This is not proof of one connected component."

- In `target_job`, the samples come from one Metropolis chain started at a single seed genotype, with `neutral_walk(rng, cur, S1, 10*L)` between successive samples. Each accepted move is a real single-nucleotide change that preserves the MFE structure.
- So every sample is joined to the seed by an explicit neutral path. A mean Hamming distance of 0.56·L between samples (random pairs: 0.75·L) is direct evidence of a neutral path of that extent through the seed's component. It is not proof that every S1-folding sequence lies in the component. That second point is what the sentence refers to, and the wording should say which claim is open.
- This is the strongest critic-favourable fact about neutral exploration, and it contradicts the ν-based percolation reading that the write-up treats as the primary evidence (line 94, "ν alone does not show percolation here").
- **Suggested fix.** Reword to: "Samples are joined to the seed by explicit neutral paths and differ from each other at 0.56·L positions on average. This shows a spread-out connected region. It does not show that all S1-folding sequences are in one component."

### m14. The "reduced" cut-off makes "supports 'reduce'" soft, and the unconditional m_all is not shown next to m∣reach

- **"Reduce".** §4.1 and §9 say D2h "reduce" is "supported" (61% of datasets have a majority with s* < 0.8). The 0.8 cut-off, the Ŵ estimator (median of the most tolerant quartile of sites) and assay noise are all the author's choices (§2, §8). A noisy WT-like variant scores below 0.8 by chance, which inflates "reduced". The result is Day-favourable and should carry that bias tag; it currently does not appear in §7.
- **m∣reach versus m_all.** Day's "m ≈ 1 is too low even for exact-structure RNA (m∣reach about 2)" (line 29) holds only given a route exists. For a random pair the mean is m_all = 0.05, far below 1 (`d1_aggregate.txt`, E0_uniform). This is Day-favourable and honest to show beside the critic-favourable 2.3. The §0 table gives reach in its own column but not m_all.
- **Suggested fix.** Add the tag in §7. Add an m_all column to the §0 table.

---

## What the check gets right for the critics (to avoid overcorrection)

- The pre-registered E2 miss (m = 28, λ = 13.4, "in the band") is reported, not buried. Disclosures on look-ahead (GB1 quantiles, DMS metadata, smoke-run ν) are explicit.
- §4.1 states "'Destroy': not supported as a majority statement" (line 182), with the 11% and 2% figures. §4.1 also notes "Mean-effect "deleterious" does not equal "rugged" in either direction here" (line 178), which is Rosenhouse-side logic.
- §3.4 and §4.2 give the critics' graded-landscape and giant-component points (lines 144–152, 204–206).
- §7 labels the bias direction of 13 caveats: five critic-flattering, four or five Day-flattering, the rest unknown or small. That is a real effort at balance.
- The post hoc GB1 SNV run (87 maxima, 44%) is Day-favourable and was reported at full strength, even though it reversed a pre-registered critic-favourable result.

## Counterweights the critics' case must accept (honest limits)

1. Exact-structure reach is 1.8% per genotype (tRNA 0.5%), and double mutants add only 3.8%. Single-step access to a named structure is rare.
2. At Day-family per-site μ, a short locus cannot walk far on its neutral network within the window (M5).
3. Tolerance (71% functional) is not benefit. The beneficial proxy is 3.6% as an upper bound, and lab benefit is not natural fitness.
4. RNA secondary structure is a toy. The partner-redundancy inflation in m_E0 (line 273) is conceded in the write-up.
5. GB1 is a four-site subspace chosen for epistasis, and its 87 local maxima and 44% are real.

## Does the check credit Camestros's specific-versus-any argument?

No, not in this document. R4-G1 credits it (G3a: "The lottery logic is correct, but has no numbers"). R4-D1 does not mention Camestros, McCarthy, Mansfield, Nesslig20, Bowers or Rosenhouse. It measures a different quantity and does not say that this quantity is not the one in dispute. The fix is one paragraph in §0 (see M1) and a cross-reference to R4-G1 §3 and §7. Critic errors recorded in the write-up: one, and it is unsourced (m10). No critic error from the D claims is carried in (e.g. D1a "hopelessly naive" is an unquantified overstatement relative to the D1 evidence, m11).

## Summary of requested changes (priority order)

1. M2: report the P10 comparison against G1's required beneficial fraction.
2. M1: re-scope the headline sentence and add the "tests" column and the specific-versus-any cross-reference.
3. M4: add upward s sensitivity; state the s range for "far below".
4. M3: add the gene-count λ₅₀ and the saturation bias.
5. M5: replace "population quantity" with the supply-sharing statement and the unconditional m_all; run a first-passage calculation (post hoc).
6. M6, m7, m8: flag E2rare; add GB1 outputs and walks on a measured landscape.
7. m9–m14: balance §0, source or reword the "strong form", extend the claims list, fix the §7 labels, reword the connectedness sentence, add the two tags and the m_all column.
