# Milestone 8: The cost of selection at human scale, and three gaps closed
*2026-10-09 · stage: R4 (in progress)*

This milestone covers four checks:
- **GAP-04, GAP-07 and GAP-02:** three of the gaps from milestone 7 that neither side, nor this audit, had addressed;
- **H3:** the cost-of-selection question at human scale. Milestone 7 called it the one place the overall verdict could still go either way.

Each check had its scripts committed with their predictions before the main run. Each went through the usual three reviews: correctness, a Day-side steelman and a critic-side steelman. Every number below is final, after review and a fix pass. The heavy H3 runs ran on a second machine (na-workhorse); the host and script checksums are recorded next to the raw outputs.

## GAP-04: the finite-map limit (Weissman & Barton 2012)
**The question.** Recombination limits how many adaptive substitutions a genome of a given map length can carry at once. The limit was published in 2012, and neither side had cited it. It gives a ceiling per generation of R/4 to R/2, where R is the map length in Morgans, and simulations in the same paper exceed R/2. For humans R ≈ 35–38 M, so the bracket is R/4, R/2, and the simulated maximum of about 3R.

- **For Day:** if every one of his 17.5–20M differences had been adaptive, the requirement is 6.5–9.1× over R/4 and 3.3–4.5× over R/2. Linkage really does cap adaptive throughput, and at that count the cap binds.
- **Against Day:** the requirement is still only 0.54–0.76 of the simulated maximum. And the adaptive count stays under the cap until 13–27% of the differences are adaptive, far more than any estimate.
- **Who decides:** whether most differences were selected at all. That is branch B and GAP-01, not GAP-04.

## GAP-07: events, not base pairs
**The question.** Day's 205M "required fixations" counts base pairs. Many differences are single insertions or deletions spanning many bases.

- **Against Day:** from published mutation rates, 205M is about 9–11× the number of mutational events (≥ 8× on the points consistent with observation). CSAC 2005's 5M indels is a total, not a per-lineage figure.
- **For Day:** the same arithmetic corroborates the size of his SNV-only figures (17.5M and 20M).
- **Next:** a direct count from the human–chimp whole-genome alignment (GAP-07b) is in progress. It will replace the rate-based estimate.

## GAP-02: how far back sweep scans can see
**The question.** Day argues that if selection had driven thousands of fixations, the genome would be full of sweep signatures. Sweep scans can only see sweeps from roughly the last 10,000 generations.

- **For Day:** the argument is fair in kind. Classic sweeps are rare in human data (Hernandez 2011 puts them under 10% of human-specific amino-acid changes), which limits hitchhiking as the main source of fixations.
- **Against Day:** his stated 3,200 sweeps over 325,000 generations predict at most about 98 detectable ones today. The top of his own range (32,000) predicts about 1,000–3,250, so the inference depends on which of his numbers is used.
- **Scan lists** are top-1% candidate lists of mostly incomplete sweeps. They are illustrative, not a count to compare against.
- **Verdict:** pending (range-dependent), softened from the first pass's "non-sequitur".

## H3: Haldane's cost of selection at human scale
**The model.** The environment keeps making the old allele costly (a "treadmill"). Costs add across loci. Population size is regulated by a ceiling. Loads are measured at K = 1,000 to 10,000 diploids on a 36.8 M map. In this model:

> sustainable adaptive rate = φ · (ln R − U_hard) / D

- R is the maximum reproductive excess.
- D ≈ 2 ln 2N is the cost per substitution.
- U_hard is any deleterious load that is hard-selected.
- φ ≤ 1 is what load fluctuations leave of the cap.

**For Day**
- **His structure holds.** Concurrent sweeps share one budget, so running them in parallel does not raise the total beyond it. The pre-registered test of this (D1a) held. This answers the generic "you forgot parallelism" reply for *selected* substitutions.
- **At Haldane's own assumed R ≈ 1.1** the cap is close to 1/300 over 10,000 generations (λ50 = 0.00340, 95% CI 0.00300–0.00379). Over the 252,000-generation lineage it is tighter: about 1/530–1/1,050 at s = 0.01. Load fluctuations remove 27–70% of the cap over that span.
- **Small mutational targets** raise the cost per substitution to D ≈ 15 + 1/M (40–160 at M = 0.01–0.03). There, even R = 2 sustains only about 1/430.
- **A modest adaptive share outside genes is not affordable.** If even 1% of non-coding differences were adaptive, no R in the plausible range (≤ 3–4) pays for it at D ≥ 5.

**Against Day**
- **The 10% is a parameter, not a law.** It is Haldane's assumed R ≈ 1.1. The budget is ln R. Day's own later anchor ("twice as many descendants as the average") is R ≈ 2. His own natural-fertility figure (total fertility 6–8) allows R up to 3–4 before mortality.
- **A coding-only adaptive count is affordable.** The minimum R for 10³ / 10⁴ adaptive substitutions in 252,000 generations is 1.22 / 2.98. That covers GAP-01's coding-only range (≈ 1.3×10³–1.2×10⁴).
- **Day's 17.5M–205M fail under every cost model.** That says nothing about Day's live argument (that *all* fixations are rate-limited), which branch B decides.
- **The first pass's "R = 20 goes extinct under a hard load" was an artefact** of K = 1,000. At K = 4,000 and 10,000 it persists.

**Why it cannot be settled here**
- **The adaptive share.** The answer flips when about 0.01–0.6% of non-coding differences are adaptive. That is below the resolution of every α estimate in the corpus: the coding estimate's interval alone spans −0.30 to 0.24, and no genome-wide non-coding estimate exists. "Coding-only fits" is therefore *undetermined*, not a finding for the critics.
- **R is unsourced.** No source gives a net hominid value.
- **The model is one choice among several.** Hard selection on the adaptive loci with a soft load is the audit's construction; no party argued it. Soft selection (Wallace, Nunney), adaptation without prior deterioration, and truncation or synergistic epistasis would all lower the cost. None is modelled at human scale. Each is named, with its direction, in the write-up.

**Credit, both ways**
- **Hancock** (the Gutsick Gibbon video) made four of H3's distinctions in words: hard vs soft scope, poorly vs well adapted, the replacement mechanism, and the intermediate-frequency route. None of them quantified.
- **Nesslig20** pointed to Matheson et al. 2025, the right source for the missing selective-death share.
- **Hössjer's** conditional (if many fixations were selected, a shared cost applies) is mechanically confirmed. His 15,800 is payable at R ≈ 2–3.
- **keruru** ran the adaptive-count comparison in January (KR-09, superseded), so the first pass's "nobody has stated this" was withdrawn.

**Verdicts.** Only the comments changed, and every one now states its condition. H stays holds / partial / contested.

## What the reviews changed
| Quantity | First pass | After review |
|---|---|---|
| Rate at R = 1.1 | "1/300 reproduced" | ≈ 1/300 over 10k generations; ≈ 1/530–1/1,050 over the lineage |
| φ at R = 2 | 0.78 (10k) | 0.59 (lineage) |
| Minimum R, 10⁴ adaptive substitutions | ≈ 2.7 | 2.98 |
| Hard load U = 2.2, R = 20 | extinct | persists at K ≥ 4,000 |
| GAP-07 headline | 9–21× | ≈ 9–11× |
| GAP-02 "tension with scans at K_a ≥ 10⁵" | stated | withdrawn |

## In progress
Four checks were started on 2026-10-09:
- **GAP-07b:** a direct count of insertion/deletion events and base pairs from the UCSC human–chimp alignment.
- **D spike:** how many interchangeable routes exist per needed change. It uses RNA folding (ViennaRNA) and deep mutational scans (MaveDB/ProteinGym), measured against G1's threshold of 12–17. It engages Day's D2h directly: Day says deep mutational scans show ruggedness.
- **C1c:** Day's ancient-DNA "21", using realistic per-site sequencing coverage from AADR plus the major ancestry turnovers in Europe.
- **Corpus refresh:** new material on both sides since 2026-10-07.

## Where things stand
```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
- **Argument map:** 258 typed objections, 185 dated versions, 196 claims.
- **Surviving their objections:** 95 as argued; 146 under a strict reading of the audit's verdicts; 104 under a lenient one.
