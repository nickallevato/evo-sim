# Standard-form reconstructions (argument map, diagram A)

*Draft 2026-10-08, built from the claim files as of commit 7cc7b27. Data only: the renderer is separate. Verdicts quoted here are the claim files' current R4 verdicts and are provisional until R5.*

**How to read this file.** Each section is one argument in standard form: numbered premises (P1, P2, ...), the inference type, and the conclusion (C). A premise marked **[implicit]** is not stated by the author; it is the premise the conclusion needs and the claim file's "Assumptions → Implicit" line names it. Every premise cites the claim file that holds the verbatim quote. Premise labels are stable: `defeaters.yaml` attacks them by label (`target_part: P2`), by `inference`, or by `C`.

**Steelman rule.** Each argument is reconstructed in the strongest form its own author would accept, from that author's latest dated statement unless an earlier one is stronger (noted). Day's arguments are written as Day would accept them, critics' as the critics would. Where an author later withdrew a premise, the premise is kept in the form the argument was made and the withdrawal is recorded as a defeater (self-defeat), not silently removed.

**Inference types.** *deductive* (conclusion follows necessarily if premises hold), *arithmetic* (a deductive special case: numbers in, number out), *statistical* (an estimate or fit from data), *analogical* (a property transfers from one system to another), *abductive* (inference to the best explanation of an observation). Where one argument mixes types, the weakest link is named first.

**Audit line.** The last line of each form gives the current R4 verdicts (internal / fidelity / external) from the claim file. It is not part of the reconstruction.

---

## Full standard forms: ROOT and the other 30 load-bearing nodes (31 forms)

### ROOT — No evolutionary mechanism can produce the human–chimp divergence in the available time (Day)
Steelman source: [ROOT](../claims/ROOT-no-mechanism-suffices.md) (Best They've Got I, 2026-10-05; MITTENS 3.0, 2026-09-28; Z18452504, 2026-02-02).
- P1. The observed divergence requires F_req lineage-specific fixations: 20 million (2025), 205 million (2026), or 17.5 million on the SNV-only count Day accepts as a variant ([A3](../claims/A3-required-fixations-2019-2025.md), [A3a](../claims/A3a-205m-headline.md), [A3b](../claims/A3b-snv-only-concession.md)).
- P2. The time available is about 252,000 generations (6.3 My at 25 y) ([A1](../claims/A1-generations-available.md)).
- P3. For each named mechanism M, the number of fixations M can deliver in that time is far below F_req: selection at the LTEE rate ([A](../claims/A-mittens-formula.md)), the cost of selection ([H](../claims/H-haldane-limit.md)), neutral drift ([B](../claims/B-neutral-theory-cannot-rescue.md), [F](../claims/F-kimura-fixation-time-limits-fixations.md)), parallel fixation ([G](../claims/G-bernoulli-barrier.md)), mutators and punctuated change ([E](../claims/E-hypermutation-hazard.md)), and search in sequence space ([D](../claims/D-sequence-space-wistar.md)).
- P4. [implicit] The named mechanisms exhaust the candidates, or any unnamed mechanism carries the burden of showing it can do the work ([ROOT-M](../claims/ROOT-excluded-mechanisms.md)).
- P5. [implicit] Mechanisms do not add up to more than their joint performance in the LTEE, which already runs them together ([A2e](../claims/A2e-ltee-as-ceiling.md), [G1](../claims/G1-average-rate-includes-parallelism.md)).
- Inference: deductive (elimination over an enumerated set), with P3 resting on arithmetic and statistical sub-arguments.
- C. No evolutionary mechanism, alone or combined, produces the observed divergence in the available time.
- Audit: pending / n/a / pending ([ROOT](../claims/ROOT-no-mechanism-suffices.md)).

### ROOT-M — The named mechanisms, and whether each has a quantitative exclusion (Day)
Steelman source: [ROOT-M](../claims/ROOT-excluded-mechanisms.md) (MITTENS 3.0 §1; Math Teacher Can't Math, 2026-09-30; Best They've Got I, 2026-10-05).
- P1. Day names the excluded mechanisms: selection (hard and soft sweeps), parallel fixation, drift, neutral sweeps, hitchhiking, ILS, biased gene conversion, hypermutation, interference-type mechanisms, recombination, HGT, introgression, duplication-type events, punctuated change, cost-limited selection ([ROOT-M](../claims/ROOT-excluded-mechanisms.md)).
- P2. Each named mechanism either has a computed bound in the corpus or operates inside the LTEE, whose aggregate rate bounds it ([ROOT-M](../claims/ROOT-excluded-mechanisms.md), [A2e](../claims/A2e-ltee-as-ceiling.md)).
- P3. [implicit] For mechanisms not named, the burden of computing a rescue lies with the proponent ("burden of the alternative", Z18452504) ([ROOT](../claims/ROOT-no-mechanism-suffices.md)).
- Inference: deductive (enumeration) plus a dialectical burden rule (P3).
- C. ROOT's universal quantifier is discharged.
- Audit: pending / n/a / pending ([ROOT-M](../claims/ROOT-excluded-mechanisms.md)); the R2 survey found five named rows asserted, not computed (rows 5, 8, 12, 13, 14).

### A — MITTENS: F_max = (t_div × d) / (g_len × G_f) (Day)
Steelman source: [A](../claims/A-mittens-formula.md) (formula, blog 2026-02-04); numbers from MITTENS 3.0 (Z23003785).
- P1. G_f, generations per fixation, is a measured total throughput from the LTEE that already includes parallel fixation and every concurrent mechanism: 1,600 (2019), 1,322 (2026) ([A2](../claims/A2-ltee-gf.md), [G1](../claims/G1-average-rate-includes-parallelism.md)).
- P2. That LTEE rate is an upper bound on the per-generation fixation rate of a sexual mammal ([A2e](../claims/A2e-ltee-as-ceiling.md)).
- P3. Generations available = t_div / g_len, multiplied by d when d is used (2025: 325,000 × 0.45 = 146,250; 3.0: 252,000, no d) ([A1](../claims/A1-generations-available.md), [A4](../claims/A4-turnover-coefficient-d.md), [A4d](../claims/A4d-d-dropped-in-mittens-3.md)).
- P4. The required number of fixations per lineage is R (20M in 2025; 205M in 3.0; 17.5M SNV-only) ([A3](../claims/A3-required-fixations-2019-2025.md), [A3a](../claims/A3a-205m-headline.md), [A3b](../claims/A3b-snv-only-concession.md)).
- P5. [implicit] Fixations accumulate linearly with time at the constant rate 1/G_f (no depletion of standing variation, no change of regime).
- Inference: arithmetic.
- C. F_max ≈ 191 (3.0) against R; the shortfall is about 10⁵–10⁶ (1,075,000× for 205M; 91,600× SNV-only).
- Audit: holds / n/a / contested ([A](../claims/A-mittens-formula.md)).

### A2e — The LTEE rate is an empirical ceiling (Day)
Steelman source: [A2e](../claims/A2e-ltee-as-ceiling.md) (MITTENS 3.0 pp.2, 4).
- P1. The LTEE runs under conditions more favourable to fast fixation than any mammal: larger Nₑ, shorter generations, strong selection, no mate-finding cost, no recombination overhead, and "an effectively unlimited mutation supply" ([A2e](../claims/A2e-ltee-as-ceiling.md)).
- P2. Every mechanism in evolution's kit operates at once in the LTEE ([A2e](../claims/A2e-ltee-as-ceiling.md), [ROOT-M](../claims/ROOT-excluded-mechanisms.md)).
- P3. [implicit] A system that is more favourable on every relevant dimension bounds the per-generation fixation rate of any less favourable system (a fortiori transfer).
- P4. [implicit] No dimension on which humans are more favourable (per-genome mutation supply, recombination) raises the human rate above the bacterial one.
- Inference: analogical (a fortiori).
- C. rate_human ≤ 1/G_f, so the human shortfall in A is a lower bound.
- Audit: non-sequitur / pending / contested ([A2e](../claims/A2e-ltee-as-ceiling.md)).

### A3 — Required fixations per lineage: 15M (2019), 20M (2025) (Day)
Steelman source: [A3](../claims/A3-required-fixations-2019-2025.md) (blog 2019-02-07; MITTENS 2025, Z18165980); the 2026 bp version is [A3a](../claims/A3a-205m-headline.md), the SNV-only variant [A3b](../claims/A3b-snv-only-concession.md). Promoted to load-bearing 2026-10-09: ROOT P1 and A P4 rest on it.
- P1. The human–chimp divergence comprises about 40M differences, 35M single-nucleotide changes plus 5M insertion/deletion events (CSAC 2005); 30M in the 2019 version ([A3](../claims/A3-required-fixations-2019-2025.md)).
- P2. Each difference is one fixation that some mechanism has to explain ([A3](../claims/A3-required-fixations-2019-2025.md)).
- P3. The differences split symmetrically between the human and chimp lineages ([A3](../claims/A3-required-fixations-2019-2025.md)).
- P4. [implicit] Differences between one human and one chimp genome are fixed differences, not polymorphism within either species ([A3c](../claims/A3c-csac-polymorphism.md)).
- Inference: arithmetic.
- C. 15M + 15M (2019) / 20M (2025) fixations required per lineage.
- Audit: holds / partial / contested ([A3](../claims/A3-required-fixations-2019-2025.md)).

### B — Neutral theory (k = μ) cannot rescue the shortfall (Day)
Steelman source: [B](../claims/B-neutral-theory-cannot-rescue.md) (blog 2026-02-04; Hard Limits abstract 2026-08-27).
- P1. k = μ is a steady-state identity; over a finite window from the split the expected count falls short of μLT ([B1](../claims/B1-intrinsic-irrelevance-steady-state.md)).
- P2. Drift cannot complete fixations above a census ceiling; for large vertebrates the domain of k = μ is empty ([B2](../claims/B2-hard-limits-domain-of-k-mu.md)).
- P3. In real populations k ≠ μ ([B3](../claims/B3-k-neq-mu-values-umbrella.md)).
- P4. The divergence date used to check k = μ is itself derived from k = μ ([B4](../claims/B4-clock-recalibration-200-580-kya.md), [B4d](../claims/B4d-clock-circularity-day.md)).
- P5. [implicit] Any one of P1–P3 is enough to deny the neutral rescue (independent, convergent routes).
- Inference: deductive (convergent: each route claimed sufficient).
- C. Neutral drift cannot supply the fixations missing in A.
- Audit: pending / partial / contested ([B](../claims/B-neutral-theory-cannot-rescue.md)).

### B1 — Intrinsic Irrelevance: k = μ is a rate, the finite-time count is smaller (Day)
Steelman source: [B1](../claims/B1-intrinsic-irrelevance-steady-state.md), [B1a](../claims/B1a-eF-formula-and-numbers.md) (Z22903977, 2026-09-22).
- P1. k = μ is a rate, not a count; turning it into a count needs a window and a start state ([B1](../claims/B1-intrinsic-irrelevance-steady-state.md)).
- P2. From an empty start, E[F(T)] = μL ∫₀ᵀ F_X(u) du ≈ μL(T − 4Nₑ) ([B1a](../claims/B1a-eF-formula-and-numbers.md)).
- P3. At the split the substitution pipeline was empty ([B1](../claims/B1-intrinsic-irrelevance-steady-state.md); restated "functionally nonexistent" in [B1c](../claims/B1c-ancestral-pipeline-state-ne-history.md)).
- P4. Inputs: T = 252,000, μL ≈ 30, Nₑ = 10⁴ (sensitivity 5×10⁴, 6.3×10⁴) ([B1a](../claims/B1a-eF-formula-and-numbers.md)).
- Inference: deductive (exact transient formula) plus arithmetic.
- C. The expected neutral count is below the naive μLT (7.56M), so the critics' k = μ totals overstate what drift delivered.
- Audit: holds / n/a / contested ([B1](../claims/B1-intrinsic-irrelevance-steady-state.md)).

### B1c — The ancestral pipeline was empty at the split (Day, 2026-10-01 first answer)
Steelman source: [B1c](../claims/B1c-ancestral-pipeline-state-ne-history.md) (Education post ¶22, 2026-10-01).
- P1. Day: the pipeline is "functionally nonexistent and empirically confirmed to be empty" ([B1c](../claims/B1c-ancestral-pipeline-state-ne-history.md)).
- P2. The European ancient-DNA record shows no advancement of allele frequencies over ~7,000 years ([C](../claims/C-adna-zero-fixations.md), [B1d](../claims/B1d-full-but-short-pipe-revision.md)).
- P3. [implicit] What the aDNA window shows about recent allele dynamics also describes the ancestral population's state at the human–chimp split.
- Inference: abductive.
- C. The pipeline was empty at the split, so B1's deficit applies to the human–chimp window.
- Audit: holds (arithmetic for an empty start) / n/a / contradicted ([B1c](../claims/B1c-ancestral-pipeline-state-ne-history.md)). Day replaced P1 in the same post with "full, but much shorter" ([B1d](../claims/B1d-full-but-short-pipe-revision.md)).

### B2 — Hard Limits: drift cannot complete fixations above a census ceiling (Day)
Steelman source: [B2](../claims/B2-hard-limits-domain-of-k-mu.md), [B2a](../claims/B2a-exp-pi2-ne-over-g.md), [B2b](../claims/B2b-ceiling-x-vk-g-over-16.md), [B2d](../claims/B2d-parallel-fixation-second-objection.md) (Z22129121, 2026-08-27).
- P1. k = μ holds at steady state; the paper "accepts it throughout" ([B2](../claims/B2-hard-limits-domain-of-k-mu.md), [B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).
- P2. The mean transit time 4Nₑ is the length of the pipe: the far end delivers what the near end fed it 4Nₑ generations earlier ([B1b](../claims/B1b-size-change-transient.md), [B2](../claims/B2-hard-limits-domain-of-k-mu.md)).
- P3. Nₑ = (4N − 2)/(Vₖ + 2) ([B2b](../claims/B2b-ceiling-x-vk-g-over-16.md)).
- P4. When 4Nₑ exceeds the lineage window G, P(τ ≤ G | fixation) ~ exp(−π²Nₑ/G) ([B2a](../claims/B2a-exp-pi2-ne-over-g.md)).
- P5. [implicit] The pipeline cannot fill within the window, so steady-state throughput is never reached ([B2d](../claims/B2d-parallel-fixation-second-objection.md)).
- Inference: deductive (asymptotic analysis) plus arithmetic.
- C. Above X = (Vₖ + 2)G/16 drift cannot complete fixations; the domain of k = μ excludes every non-endangered large vertebrate.
- Audit: pending / unverifiable / contested ([B2](../claims/B2-hard-limits-domain-of-k-mu.md)).

### B2b — Census ceiling X = (Vₖ + 2)G/16 (Day)
Steelman source: [B2b](../claims/B2b-ceiling-x-vk-g-over-16.md).
- P1. Wright: Nₑ = (4N − 2)/(Vₖ + 2) ≈ 4N/(Vₖ + 2) ([B2b](../claims/B2b-ceiling-x-vk-g-over-16.md)).
- P2. Fixation by drift within the lineage needs 4Nₑ < G ([B2b](../claims/B2b-ceiling-x-vk-g-over-16.md), [B2](../claims/B2-hard-limits-domain-of-k-mu.md)).
- P3. Inputs: human Vₖ ≈ 5; G = 80,000 (species) to 260,000 (lineage) ([B2b](../claims/B2b-ceiling-x-vk-g-over-16.md)).
- Inference: arithmetic.
- C. N < X = (Vₖ + 2)G/16: 35,000–114,000 for humans (abstract: "about ten thousand" for a large long-lived vertebrate).
- Audit: holds / unverifiable / contested ([B2b](../claims/B2b-ceiling-x-vk-g-over-16.md)).

### B3 — k ≠ μ: the family of k/μ values (Day)
Steelman source: [B3](../claims/B3-k-neq-mu-values-umbrella.md) (Z18429937, Z18525262, blogs 2026-05-07 and 2026-10-01).
- P1. k = μN/Nₑ, with N/Nₑ of 19–46 in mammals ([B3a](../claims/B3a-fixation-probability-1-over-2ne.md)).
- P2. Under overlapping generations with fluctuating size, k ≠ μ (Balloux & Lehmann 2012) ([B3b](../claims/B3b-balloux-lehmann-overlap-and-fluctuation.md)).
- P3. Human census history 1950–2025 gives k = 0.743μ ([B3c](../claims/B3c-rrme-k-0743-mu.md)).
- P4. Pedigree μ (Bergeron 2023) against the substitution rate Yoo 2025 requires gives k = 32.3μ; across 55 vertebrates the median factor is 25 ([B3d](../claims/B3d-k-32-3-mu-and-factor-25.md)).
- Inference: convergent; P1 deductive, P2 deductive from literature, P3 arithmetic, P4 statistical.
- C. k ≠ μ in real populations, so k = μ cannot be used to count the expected fixations.
- Audit: pending / partial / contradicted ([B3](../claims/B3-k-neq-mu-values-umbrella.md)).

### B3a — k = 2Nμ × 1/(2Nₑ) = μN/Nₑ (Day, Jan–Apr 2026)
Steelman source: [B3a](../claims/B3a-fixation-probability-1-over-2ne.md) (Z18525547 eq. 1, 2026-02-08; blog 2026-02-04).
- P1. Mutation supply per generation is 2Nμ with census N: every individual can mutate ([B3a](../claims/B3a-fixation-probability-1-over-2ne.md)).
- P2. The fixation probability of a new neutral mutant is 1/(2Nₑ), because drift operates on Nₑ ([B3a](../claims/B3a-fixation-probability-1-over-2ne.md)).
- Inference: deductive (algebra).
- C. k = μN/Nₑ, so with N ≫ Nₑ the clock runs fast and dates collapse.
- Audit: holds / misread / contradicted ([B3a](../claims/B3a-fixation-probability-1-over-2ne.md)). Withdrawn by Day 2026-08-27 ([B3g](../claims/B3g-day-concession-no-ne-in-kimura-identity.md)).

### B3g — Kimura's identity never needed Nₑ (Day's concession, 2026-08-27)
Steelman source: [B3g](../claims/B3g-day-concession-no-ne-in-kimura-identity.md).
- P1. Supply is 2Nμ in census N ([B3g](../claims/B3g-day-concession-no-ne-in-kimura-identity.md)).
- P2. The fixation probability of a new copy is 1/(2N) in the same N ([B3g](../claims/B3g-day-concession-no-ne-in-kimura-identity.md), [B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).
- Inference: deductive.
- C. The two cancel (k = μ, no Nₑ); the N/Nₑ claim was an error that needs a third edition of Probability Zero.
- Audit: holds / accurate / supported ([B3g](../claims/B3g-day-concession-no-ne-in-kimura-identity.md)).

### B4a — Pairwise divergence = 2μT + θ_anc (literature; audit check)
Steelman source: [B4a](../claims/B4a-two-lineage-divergence-with-ils.md) (CSAC 2005 t₁/t₂ decomposition; Day's own IR §3 θ = 4Nₑμ).
- P1. Pairwise human–chimp divergence counts mutations on both branches back to the coalescence of the two sampled haplotypes ([B4a](../claims/B4a-two-lineage-divergence-with-ils.md)).
- P2. That coalescence lies in the ancestral population, on average 2Nₑ,anc generations before the split ([B4a](../claims/B4a-two-lineage-divergence-with-ils.md), [A3c](../claims/A3c-csac-polymorphism.md)).
- P3. Neutral mutations accrue at μ per site per generation along each branch, independent of how long any of them takes to fix ([B4a](../claims/B4a-two-lineage-divergence-with-ils.md), [B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).
- Inference: deductive (coalescent expectation), confirmed by forward simulation.
- C. E[d] = 2μT + 4Nₑ,anc·μ per site; an empty-pipe deficit in fixed substitutions does not reduce raw divergence.
- Audit: holds / accurate / contested ([B4a](../claims/B4a-two-lineage-divergence-with-ils.md)).

### B5 — Critics: 2Nμ × 1/(2N) = μ, independent of N (critics)
Steelman source: [B5](../claims/B5-critics-k-equals-mu-cancellation.md) (Hancock 2026-10-03; Mansfield; DarwinZDF42), with totals from [B5a](../claims/B5a-mccarthy-22-5-million.md)–[B5f](../claims/B5f-reddit-9-7-million-haploid.md).
- P1. 2Nμ new neutral mutations arise per generation (census N) ([B5](../claims/B5-critics-k-equals-mu-cancellation.md)).
- P2. Each has fixation probability 1/(2N) ([B5](../claims/B5-critics-k-equals-mu-cancellation.md), [B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).
- P3. [implicit] The process is at steady state over the window: the ancestral pipeline was full and 252,000 generations is long compared with 4Nₑ ([B5f](../claims/B5f-reddit-9-7-million-haploid.md), [B6](../claims/B6-ancestral-pipeline-full-mansfield.md)).
- P4. The neutral per-genome mutation count per generation is of order 30–77 ([B5a](../claims/B5a-mccarthy-22-5-million.md), [B5c](../claims/B5c-hancock-76-8-per-generation.md), [B5e](../claims/B5e-nesslig20-37-8-million.md)).
- Inference: deductive (identity) plus arithmetic for the totals.
- C. k = μ; neutral fixations over the window are about μ_G·T per lineage (9.7M–38M in the critics' figures), the same order as the observed differences.
- Audit: holds / accurate / contested ([B5](../claims/B5-critics-k-equals-mu-cancellation.md)).

### B6 — The ancestral pipeline was full at the split (Mansfield)
Steelman source: [B6](../claims/B6-ancestral-pipeline-full-mansfield.md) (Mansfield comment; CSAC 2005 for the polymorphism term).
- P1. The ancestral population existed for many generations before the split ([B6](../claims/B6-ancestral-pipeline-full-mansfield.md)).
- P2. A population at long-run equilibrium carries alleles at every stage of transit (a full pipeline) ([B6](../claims/B6-ancestral-pipeline-full-mansfield.md)).
- Inference: deductive.
- C. The pipeline was full at the split: there is no empty-start deficit, and expected divergence ≈ 2μT + θ_anc.
- Audit: holds / n/a / supported ([B6](../claims/B6-ancestral-pipeline-full-mansfield.md)).

### B7 — Neutral fixation probability is 1/(2N), not 1/(2Nₑ) (critics; Day's own 2026 texts)
Steelman source: [B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md), [B7a](../claims/B7a-kimura-1962-fixation-probability.md), [B7b](../claims/B7b-kimura-ohta-1969-4ne-and-fraction-1-over-2n.md), [B7c](../claims/B7c-keruru-retraction-census-n-cancels.md).
- P1. A new neutral mutation starts as one copy, at frequency 1/(2N) ([B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).
- P2. A neutral allele's frequency is a martingale that is absorbed at 0 or 1, so its fixation probability equals its starting frequency ([B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).
- P3. Kimura 1962 and Kimura & Ohta 1969 give 1/2N for a neutral gene, with Nₑ entering only the time ([B7a](../claims/B7a-kimura-1962-fixation-probability.md), [B7b](../claims/B7b-kimura-ohta-1969-4ne-and-fraction-1-over-2n.md)).
- Inference: deductive (optional stopping).
- C. P_fix = 1/(2N); Nₑ sets the timescale, not the probability.
- Audit: holds / accurate / supported ([B7](../claims/B7-neutral-fixation-probability-is-1-over-2n.md)).

### C2 — Bio-Cycle: d ≈ 0.45 halves the generations available to selection (Day)
Steelman source: [C2](../claims/C2-bio-cycle-d.md) (Z18203514, 2026-01-09; Z18165980).
- P1. In an age-structured population the allele-frequency change per nominal generation is d times the discrete-generation change ([C2](../claims/C2-bio-cycle-d.md), [A4](../claims/A4-turnover-coefficient-d.md)).
- P2. Fitting d to three ancient-DNA loci with published selection coefficients gives d ≈ 0.45 ([C2](../claims/C2-bio-cycle-d.md), [A4a](../claims/A4a-d-empirical-estimate.md)).
- P3. The TYR/SLC45A2 ratio stays at ~0.49 for every d, which a fitting artefact would not produce ([C2c](../claims/C2c-ratio-crossvalidation.md)).
- P4. Chicken TSHR, a discrete-generation case, needs d ≈ 1.02 ([C2d](../claims/C2d-chicken-tshr.md)).
- Inference: statistical (fit), with P3–P4 as abductive cross-validation.
- C. Effective generations = 0.45 × nominal generations.
- Audit: non-sequitur / unverifiable / contested ([C2](../claims/C2-bio-cycle-d.md)).

### C2a — d from life tables (Day)
Steelman source: [C2a](../claims/C2a-d-life-table-derivation.md) (Z18166234, 2025-12-24).
- P1. d = (actual allele-frequency change per generation) / (change predicted by a discrete-generation model) ([C2a](../claims/C2a-d-life-table-derivation.md), [A4](../claims/A4-turnover-coefficient-d.md)).
- P2. For a stable age distribution, d = T × ∫μ(x) l(x) v(x) dx / ∫ l(x) v(x) dx ([C2a](../claims/C2a-d-life-table-derivation.md)).
- P3. Coale-Demeny West tables give d from 0.53 (Neolithic) to 0.015 (2020) ([C2a](../claims/C2a-d-life-table-derivation.md)).
- Inference: deductive (derivation) plus empirical inputs.
- C. d ≈ 0.45 has a theoretical grounding and is distinct from Hill's Nₑ/(N₁T).
- Audit: holds (hazard-scale s) / unverifiable / contested ([C2a](../claims/C2a-d-life-table-derivation.md)).

### E5 — MITTENS 3.0's estimator gives −906 and 38 → 0 (critics)
Steelman source: [E5](../claims/E5-ara2-ara5-counts.md) (Dumb-and-Dumber 2026-09-28; KITTENS 2026-10-04).
- P1. MITTENS 3.0's correction formula gives −906 "true fixations" in Ara−2 ([E5](../claims/E5-ara2-ara5-counts.md)).
- P2. Its Ara+5 count drops from 38 at 30,000 generations to 0 at 60,000 ([E5](../claims/E5-ara2-ara5-counts.md)).
- P3. [implicit] A true count of fixed mutations is non-negative and cannot fall once mutations have fixed.
- Inference: deductive (reductio).
- C. The estimator, not biology, produces these values; the 1,322 and 104.7 headline rates that average them are unreliable.
- Audit: pending / accurate / pending ([E5](../claims/E5-ara2-ara5-counts.md)).

### E6 — Strict lineage-aware counts revise G_f (Day, 2026-10-02)
Steelman source: [E6](../claims/E6-strict-vs-95-counts.md) (Z23105291).
- P1. By a strict lineage-aware definition the twelve populations contain 5,496 whole-population fixations over 723,000 population-generations ([E6](../claims/E6-strict-vs-95-counts.md)).
- P2. The naive ≥95% first-crossing rule returns 8,679; the difference is within-lineage sweeps that never reach the whole population ([E6](../claims/E6-strict-vs-95-counts.md)).
- P3. Under overlapping, nested sweeps the number of fixation events and the intervals between them are not well defined ([E6](../claims/E6-strict-vs-95-counts.md)).
- Inference: statistical (measurement under a stated counting rule).
- C. The strict non-mutator rate (about 1,587 gen/fix, derived) replaces the ≥95% figure of 1,322.
- Audit: holds / unverifiable / pending ([E6](../claims/E6-strict-vs-95-counts.md)).

### F — Kimura's fixation-time equations limit how many fixations can complete (Day)
Steelman source: [F](../claims/F-kimura-fixation-time-limits-fixations.md) (Education post 2026-10-01; IR §2).
- P1. 1/(2N) and k = μ contain no time variable; they say nothing about when ([F](../claims/F-kimura-fixation-time-limits-fixations.md)).
- P2. Kimura's time equations: 4Nₑ generations for a neutral allele, t ≈ (2/s)ln(2Nₑ) for a beneficial one ([F](../claims/F-kimura-fixation-time-limits-fixations.md), [F3](../claims/F3-beneficial-fixation-time-2-over-s-ln-2ne.md)).
- P3. The fixation time is a start-up cost before any output appears ([F](../claims/F-kimura-fixation-time-limits-fixations.md)).
- P4. [implicit] The pipeline starts empty, or the window is short relative to the start-up time ([B1c](../claims/B1c-ancestral-pipeline-state-ne-history.md)).
- Inference: deductive (from P3–P4). The weaker reading, window ÷ latency as a bound on the count ([F1a](../claims/F1a-day-reply-throughput-and-serial-use-19800.md)), is the version the audit judged.
- C. Fixation times cap the number of fixations that can complete in the window.
- Audit: non-sequitur / partial / contested ([F](../claims/F-kimura-fixation-time-limits-fixations.md)).

### F1 — Latency is not throughput (Mansfield, McCarthy)
Steelman source: [F1](../claims/F1-latency-not-throughput-mansfield.md), [F1b](../claims/F1b-mccarthy-parallel-not-one-at-a-time.md).
- P1. The time to fix one allele (latency) differs from the time between successive fixations (throughput) ([F1](../claims/F1-latency-not-throughput-mansfield.md)).
- P2. Mutations need not rise in frequency one at a time; many are in transit together ([F1](../claims/F1-latency-not-throughput-mansfield.md), [F1b](../claims/F1b-mccarthy-parallel-not-one-at-a-time.md)).
- P3. [implicit] For independent loci, throughput = arrivals × fixation probability, whatever the latency (Little's law: number in flight = rate × latency).
- Inference: deductive (with an analogy: trucks between New York and Los Angeles).
- C. Dividing elapsed time by fixation time does not bound the number of fixations.
- Audit: holds / n/a / contested ([F1](../claims/F1-latency-not-throughput-mansfield.md)).

### F1a — MITTENS does not assume sequential fixation (Day, 2026-10-01)
Steelman source: [F1a](../claims/F1a-day-reply-throughput-and-serial-use-19800.md).
- P1. The LTEE G_f is a total throughput measurement that already includes parallel fixation ([F1a](../claims/F1a-day-reply-throughput-and-serial-use-19800.md), [G1](../claims/G1-average-rate-includes-parallelism.md)).
- P2. Dividing total generations by a per-fixation time "is also a throughput calculation", not an assumption of sequential processing ([F1a](../claims/F1a-day-reply-throughput-and-serial-use-19800.md)).
- Inference: deductive.
- C. The serial-reading objection misreads MITTENS.
- Audit: non-sequitur / n/a / pending ([F1a](../claims/F1a-day-reply-throughput-and-serial-use-19800.md)).

### F2 — Pipelining is capped by interference, the Bernoulli Barrier and cost (Day)
Steelman source: [F2](../claims/F2-multi-locus-interference-feasibility.md), [Gc](../claims/Gc-pipeline-cap-230-sweeps.md), [H](../claims/H-haldane-limit.md).
- P1. Simultaneous sweeps interfere with each other ([F2](../claims/F2-multi-locus-interference-feasibility.md)).
- P2. The active zone sustains only about 230 simultaneous sweeps ([Gc](../claims/Gc-pipeline-cap-230-sweeps.md)).
- P3. The cost of selection caps how many selected substitutions can run in parallel ([H](../claims/H-haldane-limit.md)).
- Inference: deductive from the caps, with P2 stated as obtained by "working backward from the constraint".
- C. Parallel width is bounded, so throughput cannot reach the required rate.
- Audit: holds (interference exists) / n/a / contested ([F2](../claims/F2-multi-locus-interference-feasibility.md)).

### F3a — s = 0.001 is the empirical beneficial s in humans (Day)
Steelman source: [F3a](../claims/F3a-s-0-001-zeng-2021-misread.md).
- P1. Zeng et al. 2021 report a mean selection coefficient of about 0.001 across 155 complex traits ([F3a](../claims/F3a-s-0-001-zeng-2021-misread.md)).
- P2. [implicit] That mean applies to beneficial mutations in humans.
- Inference: statistical (parameter transfer).
- C. s = 0.001 is the beneficial s; with Nₑ = 10⁴ the sweep time is about 19,800 generations.
- Audit: pending / misread / contested ([F3a](../claims/F3a-s-0-001-zeng-2021-misread.md)).

### H — Haldane's cost caps adaptive substitutions at ~1 per 300 generations (Day)
Steelman source: [H](../claims/H-haldane-limit.md) (Z18168236, 2026-01-05).
- P1. Each substitution costs about 30N selective deaths ([H](../claims/H-haldane-limit.md)).
- P2. Only about 10% of mortality per generation can be selective ([H](../claims/H-haldane-limit.md)).
- P3. The 10% is a population-wide budget shared by all loci, not a per-locus allowance ([H](../claims/H-haldane-limit.md)).
- P4. Effective generations = 325,000 × d = 146,250 ([H](../claims/H-haldane-limit.md), [C2](../claims/C2-bio-cycle-d.md)).
- P5. [implicit] Most of the 20 million differences are selected (adaptive), so the bound applies to them.
- Inference: arithmetic.
- C. At most one beneficial substitution per 300 generations: 487 achievable, a 41,068-fold shortfall.
- Audit: holds / partial / contested ([H](../claims/H-haldane-limit.md)).

### H1 — 2026-05-07 retraction: Term 3 bounds adaptive substitutions only (Day)
Steelman source: [H1](../claims/H1-term3-retraction.md).
- P1. The Term 3 mathematics is correct for the quantity to which it actually applies ([H1](../claims/H1-term3-retraction.md)).
- P2. Term 3 bounds selectively driven substitutions, not total k ([H1](../claims/H1-term3-retraction.md)).
- Inference: deductive (scope restriction).
- C. Total substitution rate is set by Terms 1 and 2 only; the adaptive rate is still limited (~10⁻¹² per site); the CHLCA estimate moves to 250 kya–1.3 Mya.
- Audit: holds / n/a / supported ([H1](../claims/H1-term3-retraction.md)).

### H2 — Nunney 2003: the cost depends on M and on hard vs soft selection (literature)
Steelman source: [H2](../claims/H2-nunney-2003.md).
- P1. The cost of substitution depends on M = 2Ku, the new mutations per generation ([H2](../claims/H2-nunney-2003.md)).
- P2. In hard-selection simulations the cost is substantially less than Haldane's for M > ½ and rises steeply for M < ½ ([H2](../claims/H2-nunney-2003.md)).
- P3. Soft selection reduces or eliminates the cost, but only where selection is driven by intraspecific competition ([H2](../claims/H2-nunney-2003.md)).
- Inference: statistical (simulation results).
- C. Haldane's 300 binds at small M under hard selection (e.g. M = 0.1) and is not a general bound.
- Audit: n/a / accurate / contested ([H2](../claims/H2-nunney-2003.md)).

### H5 — Hössjer: after rescaling, cost keeps MITTENS's conclusion (ally)
Steelman source: [H5](../claims/H5-hossjer-cost-step.md), [A5a](../claims/A5a-hossjer-127-15800-10m.md) (Hössjer PDF, 2026-09-14).
- P1. MITTENS with 2019 inputs and d gives F = 127 ([H5](../claims/H5-hossjer-cost-step.md)).
- P2. Scaling for mutation rate gives 15,800; scaling also for genome length gives about 10 million, a factor ~2 below 20 million ([A5a](../claims/A5a-hossjer-127-15800-10m.md)).
- P3. Haldane's cost of parallel selected fixations keeps the selected count near 15,800 rather than 10 million ([H5](../claims/H5-hossjer-cost-step.md)).
- P4. [implicit] Most differences on the human lineage are selected.
- Inference: arithmetic (P1–P2) with an asserted premise (P3).
- C. The MITTENS conclusion stands after rescaling.
- Audit: non-sequitur / pending / contested ([H5](../claims/H5-hossjer-cost-step.md)).

### H8 — Kimura's Fixation Calculator, Term 3 (Day, 2026-05-02)
Steelman source: [H8](../claims/H8-kimura-calculator-term3.md) (Z19984826).
- P1. The selective differential is bounded: Σ s_i ≤ s_max ≈ 1 ([H8](../claims/H8-kimura-calculator-term3.md)).
- P2. Each sweep takes τ = (2/(s̄ d)) ln(2Nₑ) generations ([H8](../claims/H8-kimura-calculator-term3.md)).
- P3. So n_max = s_max/s̄ concurrent sweeps and K_sel = n_max/τ ([H8](../claims/H8-kimura-calculator-term3.md)).
- P4. The realised rate is k_real = min(Term 1, Term 2, Term 3) ([H8](../claims/H8-kimura-calculator-term3.md)).
- Inference: arithmetic.
- C. k_sel ≈ 8.3 × 10⁻¹² per site per generation for humans, which caps k (scope later narrowed to adaptive substitutions, [H1](../claims/H1-term3-retraction.md)).
- Audit: holds / pending / contested ([H8](../claims/H8-kimura-calculator-term3.md)).

---

## Mini-forms: attacked claims that are not load-bearing

These are reduced to the premise(s) a defeater actually targets. Same conventions; one row per claim. Side in brackets.

| ID | Premises | Conclusion | Inference |
|---|---|---|---|
| A1 | P1: 6.3 My divergence at 25 y per generation ([A1](../claims/A1-generations-available.md)) | 252,000 generations available | arithmetic |
| A2 | P1: snapshot counts at ≥95% pooled frequency give 45.4 non-mutator fixations at 60K ([A2](../claims/A2-ltee-gf.md)); P2: [implicit] that count measures fixations | G_f = 1,322 (cross-validated 893) [day] | statistical |
| A2a | P1: 25 fixed mutations in ~40,000 LTEE generations (Nature 2009 / Good 2017) ([A2a](../claims/A2a-gf-datum-source-2019.md)) | G_f = 1,600 [day] | statistical |
| A2b | P1: strict lineage-aware count 5,496; P2: the ≥95% rule overcounts ([A2b](../claims/A2b-gf-counting-rule-1322-vs-1587.md)) | revised counts and rate [day] | statistical |
| A2d | P1: G_f is an average, so it includes faster fixations ([A2d](../claims/A2d-gf-average-not-fastest.md)) | it is not the fastest rate, so not shown to be a ceiling [critic] | deductive |
| A3a | P1: 35M SNVs + 1,140 inversions + 187 Mb SDR ≈ 410M differences (Yoo 2025); P2: each base pair counts as one fixation; P3: halve per lineage ([A3a](../claims/A3a-205m-headline.md)) | 205M required [day] | arithmetic |
| A3x | P1: 35M SNVs + 5M indel events (CSAC) + 1,140 inversions ≈ 40M events; P2: one structural change can affect many base pairs ([A3x](../claims/A3x-bp-vs-events.md)) | ~20M events per lineage, not 205M [critic] | arithmetic |
| A4 | P1: overlapping generations slow allele-frequency change per nominal generation; P2: d is that ratio ([A4](../claims/A4-turnover-coefficient-d.md)) | effective generations = d × nominal [day] | deductive |
| A5 | P1: the human genome is ~690× larger with far more new mutations per generation ([A5](../claims/A5-genome-size-mutation-supply.md)); P2: [implicit] fixation rate depends on per-genome supply | the LTEE rate does not transfer to humans unscaled [critic] | analogical |
| A5a | P1: F = 127 (2019 inputs with d); P2: ×125 for mutation rate, ×652 for genome length ([A5a](../claims/A5a-hossjer-127-15800-10m.md)) | ~10M, a factor ~2 below 20M [ally] | arithmetic |
| A5b | P1: per-genome supply ratio ~94,000; P2: bases-vs-events factor 11.7; P3: [implicit] adaptive fixations scale linearly with supply ([A5b](../claims/A5b-kittens-94000x11p7.md)) | shortfall decomposes; 17.9M achievable vs 17.5M required [critic] | arithmetic |
| A5c | P1: bacterial neutral supply with μ ≈ 10⁻¹¹ per bp ([A5c](../claims/A5c-neutral-supply-ecoli-vs-human.md)) | ~4×10⁻⁵ neutral fixations per generation, ~22,000 gens each [critic] | arithmetic |
| A5d | P1: a 100× mutator gives 8.5–17× throughput ([A5d](../claims/A5d-supermutation-sublinear.md)) | fixation is not bottlenecked by mutation supply [day] | abductive |
| A5e | P1: Kimura's fixation-time formula with human parameters gives one fixation per 27,600 effective generations ([A5e](../claims/A5e-human-derived-rate-27600.md)) | 8 achievable fixations [day] | arithmetic |
| A5f | P1: the LTEE is nonrecombining, one clone, one environment; P2: sex and population-size variability change fixation rates ([A5f](../claims/A5f-clonal-lineage-vs-recombining.md)) | the bacterial rate does not transfer to mammals [critic] | analogical |
| A5g | P1: the E. coli study was cited for its fixation rate, not its mutation rate; P2: no human or mammalian fixation faster than 1,600 gens has been observed ([A5g](../claims/A5g-mutation-supply-irrelevant-reply.md)) | mutation-supply scaling is irrelevant [day] | deductive |
| A6 | P1: 3,200+ sweeps over 325,000 generations, about one every 100 generations; P2: [implicit] signatures of completed sweeps persist over the lineage and scans detect them with high power; P3: scans find dozens to hundreds of candidate regions, not thousands ([A6](../claims/A6-sweep-signatures-absent.md)) | sweep signatures are absent at the required scale, so 3,200+ sweeps did not occur [day] | abductive (predicted signature not observed) |
| B1a | P1: ∫₀ᵀF_X ≈ T − 4Nₑ; P2: μL ≈ 30, T = 252,000; P3: [implicit] empty start ([B1a](../claims/B1a-eF-formula-and-numbers.md)) | the naive 7.56M overstates the count [day] | arithmetic |
| B2c | P1: Nₑ/T ≈ 1.8×10⁷ for the current-census era; P2: tail exp(−π²Nₑ/T) ([B2c](../claims/B2c-one-in-ten-to-78-millionth.md)) | ~1 in 10^78,000,000 per neutral mutation [day] | arithmetic |
| B2d | P1: steady-state flux is μ whatever the transit time; P2: the pipeline cannot fill ([B2d](../claims/B2d-parallel-fixation-second-objection.md)) | the drift limit does not rest on "nothing finishes" [day] | deductive |
| B2e | P1: measured temporal Nₑ for Bronze Age Europe is 6,933–8,139; P2: Wright's 4N/(Vₖ+2) at a census of ~10⁷ gives Nₑ/N ≈ 0.57 ([B2e](../claims/B2e-keruru-measured-ne-vs-wright.md)) | Wright's input to the census ceiling is wrong by about three orders where it can be tested [critic] | statistical |
| B3c | P1: k_i = μN_i/N_t (fixation probability 1/(2N_t)); P2: four human census cohorts ([B3c](../claims/B3c-rrme-k-0743-mu.md)) | k = 0.743μ [day] | arithmetic |
| B3d | P1: Bergeron pedigree μ against Yoo's required rate; P2: [implicit] the gap measures k/μ and nothing else ([B3d](../claims/B3d-k-32-3-mu-and-factor-25.md)) | k = 32.3μ; median factor 25 [day] | statistical |
| B3e | P1: supply 132 billion × fixation 1/(16 billion) under N/Nₑ ([B3e](../claims/B3e-corrected-calculation-8-25-fixations.md)) | 8.25 fixations; shortfall 2,424,242× [day] | arithmetic |
| B3f | P1: N = 8×10⁹, Nₑ = 10⁴; P2: k = μN/Nₑ ([B3f](../claims/B3f-800000-mu-grok-exchange.md)) | k = 800,000μ [day, via Grok] | arithmetic |
| B3h | P1: Nₑ ≈ 10⁴ comes from θ = 4Nₑμ; P2: θ = 4Nₑμ presupposes k = μ ([B3h](../claims/B3h-ne-10000-presupposes-k-mu.md)) | arguments using Nₑ ≈ 10⁴ are circular [day] | deductive |
| B4 | P1: k = μN/Nₑ; P2: clock dates scale by 2/(N_h/Nₑ,h + N_c/Nₑ,c) ([B4](../claims/B4-clock-recalibration-200-580-kya.md)) | CHLCA 200–580 kya [day] | arithmetic |
| B4d | P1: the divergence date was computed from k = μ; P2: no independent measurement enters ([B4d](../claims/B4d-clock-circularity-day.md)) | the dating is circular [day] | deductive |
| B4g | P1: pedigree rate ~1.2×10⁻⁸; P2: fossil-calibrated rate ~2× higher ([B4g](../claims/B4g-keruru-pedigree-vs-fossil-calibrated-twice.md)) | unreconciled factor 2 [critic; keruru rule, 2026-08-26 post] | statistical |
| B5a | P1: 450 billion new mutations over 9 My (N = 10,000); P2: each fixes with probability 1/20,000 ([B5a](../claims/B5a-mccarthy-22-5-million.md)) | 22.5M fixed mutations [critic] | arithmetic |
| B5b | P1: if 2% of ~100 de novo mutations are neutral, 2N new neutral alleles per generation; P2: × 1/(2N) ([B5b](../claims/B5b-mansfield-one-fixation-per-generation.md)) | about 1 neutral fixation per generation [critic] | arithmetic |
| B5c | P1: ~76 new mutations fixed per generation (haploid, SV-inclusive); P2: × 2 lineages × 252,000 ([B5c](../claims/B5c-hancock-76-8-per-generation.md)) | ~38M, matching 35–40M observed [critic] | arithmetic |
| B5d | P1: 6 My / 25 y × 30 mutations per generation ([B5d](../claims/B5d-relayed-7-2-million.md)) | 7.2M neutral differences with no selection [critic, relayed] | arithmetic |
| B5e | P1: μ_G = 75, so k = 75; P2: × 2 × 252,000 ([B5e](../claims/B5e-nesslig20-37-8-million.md)) | ~37.8M neutral fixed differences [critic] | arithmetic |
| B5f | P1: 38.4 per generation × 252,000; P2: elapsed time long compared with fixation time ([B5f](../claims/B5f-reddit-9-7-million-haploid.md)) | ~9.7M per lineage [critic] | arithmetic |
| B6a | P1: θ = 4Nₑμ at Nₑ = 10⁴ gives 1.44M; P2: the empty-pipe correction removes 2.4M ([B6a](../claims/B6a-day-ancestral-polymorphism-rounding-error.md)) | ancestral polymorphism is a rounding error [day] | arithmetic |
| B6c | P1: a strictly serial model leaves no standing variation except the sweeping allele; P2: observed standing variation exists ([B6c](../claims/B6c-hancock-no-standing-variation-prediction.md)) | the serial model is falsified [critic] | deductive |
| B7c | P1: supply 2Nμ with census N; P2: exact chains give P_fix = 1/(2N_census) ([B7c](../claims/B7c-keruru-retraction-census-n-cancels.md)); P3: [implicit, aDNA leg] zero aDNA fixations is the neutral expectation at Nₑ ~ 10⁴ ([C5](../claims/C5-keruru-neutral-zero.md)) | the substitution-rate and aDNA claims are withdrawn [critic; keruru rule, 2026-08-26 post] | deductive |
| B9 | P1: drift fixes neutral mutations only when selection is not operating; P2: harmful mutations outnumber neutral ones 3:1 ([B9](../claims/B9-drift-would-cause-extinction-within-centuries.md)) | if drift changed the genome, humans would have gone extinct within centuries [day] | deductive |
| C | P1: zero (blog) / one and three (paper) completions from intermediate frequency in ~7,000 years; P2: the standard model predicts more ([C](../claims/C-adna-zero-fixations.md)) | the data falsify the standard rate [day] | statistical |
| C1 | P1: the 1240k panel was built from present-day polymorphic sites; P2: new and recently fixed sites are under-represented ([C1](../claims/C1-1240k-ascertainment.md)) | near-zero fixations are expected regardless [audit-raised, no published critic; hierarchy side 'literature' since 2026-10-08] | deductive |
| C1a | P1: ascertainment favours alleles polymorphic in modern Europeans; P2: that favours detecting recent fixations ([C1a](../claims/C1a-day-ascertainment-reply.md)) | the absence of fixations strengthens Day's conclusion [day] | deductive |
| C2c | P1: the TYR/SLC45A2 ratio is ~0.49 at every d; P2: a fitting artefact would give inconsistent ratios ([C2c](../claims/C2c-ratio-crossvalidation.md)) | d reflects real dynamics [day] | abductive |
| C2d | P1: chicken TSHR needs d ≈ 1.02; P2: chickens have discrete generations ([C2d](../claims/C2d-chicken-tshr.md)) | the cross-species validation is decisive [day] | abductive |
| C4 | P1: drift variance varied 3.3–4.6-fold across the Holocene ([C4](../claims/C4-holocene-ne.md)) | Nₑ varied at least 3.3-fold [day] | statistical |
| C5 | P1: Nₑ ~ 10⁴; P2: neutral transit from intermediate frequency in 240 generations ([C5](../claims/C5-keruru-neutral-zero.md)) | ~10⁻²⁹ expected fixations; zero is the prediction [critic] | arithmetic |
| C5a | P1: Nₑ ≈ 10⁴ comes from θ = 4Nₑμ, which presupposes k = μ; P2: rs35619459 29.3% → 91.3% implies a drift-variance Nₑ near 2 ([C5a](../claims/C5a-day-ne-circularity.md)) | keruru's zero-prediction is circular [day] | deductive |
| C5b | P1: the temporal method takes allele frequencies from two dated ancient samples, the sample sizes and the generations between them, with no μ and no coalescent; P2: it gives Nₑ 8,139 (102 generations) and 9,835 (250) ([C5b](../claims/C5b-keruru-temporal-ne.md)) | Nₑ ≈ 10⁴ is measured, not presupposed by the clock [critic] | statistical |
| C6 | P1: the clock predicts ~630 fixations per 350 generations (150M sites); P2: 21 are observed after 7,000 BP; P3: [implicit] panel sites register new substitutions at the genome-wide rate ([C6](../claims/C6-molecular-clock-stopped.md)) | the constant-rate clock is falsified [day] | statistical |
| C7 | P1: ~zero completed fixations from intermediate frequency in ~7,000 years (C) ([C7](../claims/C7-no-drift-last-7000-years.md)) | genetic drift is not happening at all [day] | abductive |
| D | P1: sequence space ~10^325 (Eden); P2: functional proteins ever ~10^52; P3: time is insufficient for random search; P4: no biologist calculated otherwise ([D](../claims/D-sequence-space-wistar.md)) | functional sequences are unreachable in the time available [day] | arithmetic + abductive |
| D1 | P1: the Wistar critiques were refuted; P2: creationists misrepresent the conference ([D1](../claims/D1-rosenhouse-wistar-critiques-refuted.md)) | Wistar gives no support to anti-evolution arguments [critic, secondhand] | deductive |
| D10 | P1: ~1 in 10^64 signature-consistent sequences forms a working domain; P2: combined with fold prevalence ([D10](../claims/D10-axe-2004-1-in-1e77.md)) | specific function by any fold may be as rare as 1 in 10^77 [literature] | statistical |
| D1a | P1: the geometry of protein space has been learned since 1966 ([D1a](../claims/D1a-rosenhouse-eden-naive-combinatorics.md)) | Eden's combinatorics are naive [critic, secondhand] | deductive |
| D1b | P1: simulations of evolution are now commonplace ([D1b](../claims/D1b-rosenhouse-simulations-commonplace.md)) | Schützenberger's argument has not held up [critic, secondhand] | deductive |
| D2 | P1: Rosenhouse ch.4 gives no quantitative refutation and no citations ([D2](../claims/D2-day-rosenhouse-ch4-no-quantification.md)) | Eden, Ulam and Schützenberger stand unchallenged [day] | deductive |
| D2a | P1: Ulam said "What I am going to do will come to Eden's conclusions" ([D2a](../claims/D2a-day-ulam-sides-with-eden.md)) | Ulam sided with Eden [day] | deductive |
| D2b | P1: Lewontin answered "That is a very good question. I don't know." ([D2b](../claims/D2b-day-lewontin-cannot-justify-continuity.md)) | Lewontin could not justify the continuity assumption [day] | deductive |
| D2f | P1: Mayr: "We are comforted by knowing that evolution has occurred" ([D2f](../claims/D2f-day-mayr-argument-from-existence.md)) | Mayr retreated to an argument from existence [day] | deductive |
| D2g | P1: Eden computed the space and Ulam the rate; P2: no biologist computed a smaller space or faster rate ([D2g](../claims/D2g-day-no-biologist-produced-a-calculation.md)) | the mathematicians were not answered [day] | deductive |
| D2h | P1: deep mutational scanning shows single-residue changes mostly reduce or destroy function ([D2h](../claims/D2h-day-deep-mutational-scanning-shows-ruggedness.md)) | the landscape is rugged; Eden is confirmed [day] | statistical |
| D2j | P1: Eden: "I must apologize for being so vague on the nature of R" ([D2j](../claims/D2j-day-eden-apologises-for-vagueness-ch6.md)) | Eden demanded the math and Waddington could not supply it [day] | deductive |
| D3 | P1: 20^250 ≈ 10^325 sequences; P2: ~10^52 protein molecules ever ([D3](../claims/D3-eden-sequence-space-arithmetic.md)) | either function is common or the topology supplies paths [literature] | arithmetic |
| D3c | P1: hemoglobin α→β needs ≥120 point mutations through viable intermediates ([D3c](../claims/D3c-eden-hemoglobin-2.7-million-generations.md)) | Eden showed the time "vastly exceeds" what is available [day] | arithmetic |
| D4 | P1: 10⁶ successive improvements, each ~10⁷ generations to spread ([D4](../claims/D4-ulam-sequential-improvements-10-to-13-generations.md)) | ~10^13 generations needed [literature] | arithmetic |
| D4a | P1: random construction of molecules "is not the problem at all"; P2: selection sieves the population ([D4a](../claims/D4a-ulam-random-construction-is-not-the-problem.md)) | the random-chain framing is the wrong model [literature] | deductive |
| D5 | P1: meaning-preserving typographic changes are rare; P2: no known principle maps typographic to functional space ([D5](../claims/D5-schutzenberger-gap-between-typographic-and-functional-space.md)) | there is a gap neo-Darwinism cannot bridge [literature] | deductive |
| D6 | P1: by twenty questions, < 1,250 steps reach a specified 250-residue protein ([D6](../claims/D6-wright-twenty-questions-1250.md)) | selection does not need ~10^325 operations [literature] | analogical |
| D9 | P1: N = 10,000, 12 offspring, s = 0.001 give ~20,000 generations per letter; P2: letters fix in sequence ([D9](../claims/D9-weasel-540000-generations.md)) | ~540,000 generations for the phrase [day] | arithmetic |
| D9a | P1: the D9 figures ([D9a](../claims/D9a-weasel-demonstrates-the-opposite.md)) | the Weasel demonstrates the opposite of its purpose [day] | deductive |
| E | P1: a founder event captures two or more mutator carriers about 6% of the time; P2: such an event yields a homozygote with probability about 0.39 ([E](../claims/E-hypermutation-hazard.md)) | about 2.3% of founder events produce a hypermutator homozygote [day] | arithmetic |
| E3 | P1: a WF simulation at N = 100, G = 50 with full selection gives P(homozygote) = 2.33% ([E3](../claims/E3-cmmrd-simulation.md)) | the hazard is independently sufficient against punctuated equilibrium [day] | statistical |
| E4 | P1: when one family can replace more than ~10% of the population, t̄ = 4Nₑ fails; P2: P_fix = 1/(2N) holds regardless of offspring distribution ([E4](../claims/E4-relictation.md)) | relictation is a third evolutionary mechanism [day] | deductive |
| E7 | P1: a 100× mutation rate gives 8.5–17× (mean 12.75×) fixation throughput ([E7](../claims/E7-mutator-sublinear.md)) | fixation is bottlenecked by sweep dynamics, not supply [day] | abductive |
| F3 | P1: t ≈ (2/s)ln(2Nₑ) is Kimura's equation for a beneficial sweep ([F3](../claims/F3-beneficial-fixation-time-2-over-s-ln-2ne.md)) | the sweep time at s = 0.001 is ~19,800 generations [day] | arithmetic |
| F4 | P1: beneficial fixation probability ≈ 2s, not 1/N ([F4](../claims/F4-bowers-fixation-probability-2s.md)) | Day's fixation probability is wrong [critic, secondhand] | deductive |
| G | P1: the best/worst fitness differential at N = 10,000 is 14.7×; P2: the required differential is 1,570× ([G](../claims/G-bernoulli-barrier.md)) | parallel fixation is limited (>100× short) [day] | arithmetic |
| G1 | P1: G_f is total throughput after all concurrent dynamics; P2: an average rate is indifferent to parallel vs serial timing ([G1](../claims/G1-average-rate-includes-parallelism.md)) | no parallelism divisor applies [day] | deductive |
| G1a | P1: Ara+2's 14 fixation events were all sequential ([G1a](../claims/G1a-ara-plus-2-no-parallel.md)) | there was no parallel fixation in the LTEE [day] | statistical |
| G2 | P1: MITTENS divides time by generations per fixation; P2: that assumes each mutation arises and fixes before the next ([G2](../claims/G2-serial-critique-hancock.md)) | the formula is serial [critic] | deductive |
| G2a | P1: 60,000 runners × 4 h = 240,000 h only if run serially ([G2a](../claims/G2a-marathon-analogy.md)) | the same holds for fixation [critic] | analogical |
| G2g | P1: the Bernoulli Barrier rules out parallel fixation ([G2g](../claims/G2g-appendix-a-fixation-must-be-sequential.md)) | fixation must be sequential: 180 fixations vs 205M [day] | deductive |
| G3 | P1: (1/20,000)^20M prices a pre-specified list; P2: evolution needs some 20M out of a large pool ([G3](../claims/G3-specific-vs-any.md)) | the Darwillion does not measure evolution's probability [critic] | deductive |
| G3b | P1: either the specific fixations matter or they are interchangeable neutral noise ([G3b](../claims/G3b-day-either-specific-or-interchangeable.md)) | the Darwillion applies, or neutral theory must explain function [day] | deductive (dilemma) |
| G4 | P1: the Darwillion is the reciprocal of the probability of the pre-specified fixations ([G4](../claims/G4-darwillion-definition.md)) | a rhetorical device showing how far off biologists are [day] | deductive |
| G4b | P1: raising 1,600 to 40,000 generations per fixation raises the improbability ([G4b](../claims/G4b-darwillion-25x-reply.md)) | McCarthy increased the Darwillion 25× [day] | arithmetic |
| Ga | P1: p = 0.02 per fixation; P2: n = 20M independent fixations ([Ga](../claims/Ga-p-to-the-n-0p02.md)) | P(all) ≈ 10^−34,000,000 [day] | arithmetic |
| Gc | P1: the active zone sustains ~230 simultaneous sweeps; P2: transit ~440 generations ([Gc](../claims/Gc-pipeline-cap-230-sweeps.md)) | at most ~157,000 fixations in 300,000 generations [day] | arithmetic |
| H6 | P1: Haldane's limit applies to selection, not drift ([H6](../claims/H6-nesslig20-cost-vs-drift.md)) | the cost cannot bound neutral differences [critic] | deductive |
| H7 | P1: genome-wide deleterious U ≈ 2.2 ([H7](../claims/H7-keightley-deleterious-load.md)) | intolerable under hard selection, tolerable under soft [literature] | deductive |
| H9 | P1: Kimura & Ohta 1969 established that fixation time does not depend on recombination ([H9](../claims/H9-kimura-ohta-recombination.md)) | the recombination objection fails [day] | deductive |
