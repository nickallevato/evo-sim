# evo-sim: a briefing for independent assessment

*Status as of 2026-10-09 (X1 fairness audit with one verdict rule for both sides, GAP-07c, the mapping of every critic and ally argument, and the Holocene Nₑ retrieval added; earlier the same day C1c, C1d and D1 added; A3 marked load-bearing; earlier the same day GAP-07b and the corpus refresh; earlier the same day H3 and GAP-04/07/02; earlier 2026-10-08 revision: Day's dated concessions added; milestone posts linked). Repo: <https://github.com/nickallevato/evo-sim> (branch `research`).*

This note is for a team that has not followed the project and wants to form its own view of it. It describes what the project is, what it has found, and where its findings and methods are weakest. It does not argue for any side. Wherever this note and the repo disagree, trust the repo.

## What the project is
evo-sim has two stages.

**1. A research audit (in progress).** The audit examines Vox Day's mathematical argument against evolution, which Day calls MITTENS and develops in the book *Probability Zero* (2025), about 30 Zenodo papers and several years of blog posts. It examines the published rebuttals to that argument with the same rigour. Day's claim is that population genetics rules out natural selection as the explanation for the human–chimp divergence in the time available. The critics, mostly bloggers, Substack writers and YouTubers, say Day's maths is wrong.

**2. A simulator (not started).** The planned output is an open-source evolution simulator. Its controls will be the parameters the dispute actually turns on, so that anyone can test either side's claims. No simulator code exists yet. The project rules hold back simulator work until the audit meets its exit criteria.

## How the audit works
1. **Corpus.** Day's posts and papers from 2019 onward, the primary literature Day cites, and the critics' and allies' responses. In numbers: 154 posts, 32 Zenodo records, 37 papers and 48 critic or ally sources.
2. **Claims.** 233 distinct mathematical or empirical claims, each with a verbatim quote, a source locator and a date. Claims come from both sides.
3. **Argument tree.** Each claim is attached to one of eight branches (A–H) under Day's root claim. Thirty-three nodes are marked as load-bearing (A3, the required-fixation count, was added on 2026-10-09; ROOT-FM, Day's mesa claim, and its conclusion FM10 on 2026-10-10).
4. **Checks.** Each load-bearing equation is tested with an exact Markov chain or a forward simulation. The prediction is written down before the run. Fifty-four checks have been reviewed so far.
5. **Reviews.** Load-bearing checks get three reviews: one for correctness, one steelmanning Day's position, and one steelmanning the critics'. Since 2026-10-09, low-stakes checks (re-confirmations, bookkeeping, tool validation) get one combined review with the same three sections. All reviews so far are by instances of the same AI model family and are not blind; see `docs/research/METHOD-AUDIT-2026-10-12.md` (MA-01).
6. **Verdicts.** Each claim gets three separate verdicts:
   - *Internal:* does the conclusion follow from the author's own premises?
   - *Fidelity:* does the cited source actually say what the author says it does?
   - *External:* are the premises realistic?

The project rules require valid points to be recorded as prominently as errors, whichever side makes them. Each branch has a balance ledger with columns for "best for Day" and "best for critics".

## What it has found so far
These are R4 results. The R5 synthesis has not been done, so every verdict is provisional.

**Points where Day's maths holds up:**
- **Empty pipe.** Day's formula, E[F] = μL∫F_X, is exact for its premise: a population that starts with no standing variation.
- **Timescale.** Nₑ does set the timescale of fixation.
- **Hard Limits tail.** The exponent −π²Nₑ/G is the correct leading-order tail.
- **LTEE rate.** The bacterial figure of about 1,300 generations per fixation is a real throughput measurement, and it reproduces.
- **Balloux–Lehmann effect.** It is real: with overlapping generations and a fluctuating population size, k ≠ μ. The critics' blanket "k = μ" holds only for discrete generations.
- **Cost of selection.** In the audit's reconstruction, soft selection does not make the cost disappear. At human scale (H3), concurrent sweeps do share one reproductive budget, as Day says, and at Haldane's assumed R ≈ 1.1 the long-run sustainable rate is below 1/300 (≈ 1/530–1/1,050).
- **Haldane's arithmetic** (300 and 487) holds.
- **A critic's double count.** The critics' claim that "38M matches 35M SNVs" counts the same differences twice.
- **SNV-only count.** Day's SNV-only figure (17.5M per lineage) is 83% of the directly counted events and brackets the count once polymorphism is removed (16.4–18.1M); his SNV-only shortfall grows slightly on the measured count. His base-pair total is the right order for sequence that does not align one-to-one (GAP-07b).
- **Ancient DNA, in part.** On the real AADR genotypes Day's start-frequency table reproduces to 0.4 points, and his description of the events as completions of alleles already near fixation is right in kind (98.8%) (C1d).
- **Sequence space, at the locus.** Exact-outcome alternatives are about one per needed change, the GB1 landscape is rugged at single-nucleotide steps, and "reduce or destroy" holds as worded for deep mutational scans (D1).
- **LTEE founders.** The founder hazard's size (2.0–2.75% per event against Day's 2.3%) and the relictation chain both reproduce. The route to the 2.3% is wrong, and its consequence for real populations is untested.

**Points where the critics' maths holds up:**
- **Neutral rate.** The neutral substitution rate is k = μ for any Nₑ, because fixation probability is set by the census size 1/2N, not by 1/2Nₑ. Day conceded this on 2026-08-27, but a figure of k = 32.3μ reappeared on 2026-10-01 without a derivation. The earlier Zenodo papers that give k = μN/Nₑ were not revised.
- **Start state.** The ancestral population was not an empty pipe. Day has since withdrawn the empty-start premise: on 2026-10-01 Day called the pipe "full, but much shorter".
- **Latency vs throughput.** The time a single fixation takes is not the rate at which fixations happen. Many sweeps can be in flight at once.
- **Recombination.** In the tested regime, recombination removes the clonal-interference ceiling.
- **Divergence.** Human–chimp divergence includes ancestral polymorphism: d = 2μT + θ_anc.
- **Hard-selection cap.** The cap is ln R / D, not a flat 1/300. At human scale (H3, hard adaptive selection with a soft load), a coding-only adaptive count of 10³–10⁴ is payable at R ≈ 1.2–3. Day's 17.5M–205M fail under any cost model, which says nothing about whether most differences were neutral.
- **Event counts.** A direct count from the human–chimp genome alignment finds about 42M mutational events (21M per lineage). Day's 205M is 9.7× that, within a bracket of about 7–14× depending on assumptions; the alignment uses older, non-T2T assemblies (GAP-07b). With the polymorphic share measured on the human side (GAP-07c: 15.6% of human-derived differences are still variable), 205M is 10.6–12.6× the *fixed* events per lineage, about 8–13× combined.
- **Required fixations.** The "205M required fixations" figure counts base pairs rather than mutation events.
- **A misread citation.** A selection coefficient Day cites (s = 0.001, from Zeng 2021) is for negative selection, not beneficial.
- **Ancient DNA, the 21.** Day's statistic does not reproduce from his stated method on the real genotypes (thousands of post-6000 BP events, not 21; his own documented two-period pipeline is 3.6× off; no code found). keruru's measured temporal Nₑ replicates within 4%, and Day's Nₑ ≈ 2 is excluded (C1d).
- **Sequence space, within genes.** 71% of single substitutions keep at least half of function and "destroy" alone is rare; GB1's functional variants form one connected network; within genes the beneficial fraction exceeds G1's requirement for up to ~2×10⁵ needed changes (D1).
- **Bernoulli barrier.** 0.02^(2×10⁷) prices one pre-specified list of outcomes, and its value doesn't depend on timing. No cap near 230 concurrent sweeps appears under multiplicative fitness. One earlier audit objection to Day's 14.7× was itself withdrawn.

**Still open:**
- **Slightly deleterious fixations (GAP-05).** Computed on a sourced coding DFE (R4 GAP05): about 15,000-21,000 fixations per lineage; log-fitness decline 0.29-0.43 on the pre-registered base and about 0.8-1.1 on a divergence-calibrated base (post hoc), against ln 3 = 1.10. Day's premise is supported, a collapse is not; the noncoding class is unsourced and compensation untestable.
- **Cost of selection** at human scale is decided only conditionally. The answer flips at an adaptive non-coding share of about 0.01–0.6%, below what any estimate resolves. R is unsourced. Soft selection, absolute-fitness gain and epistasis are untested at human scale.
- **Haldane's regime (H8 / H5).** In Haldane's own regime (R about 1.1, D rescaled to 30) 1/300 is confirmed and no critic contested it; the budget's size is ln R, so the answer moves with R. "Slower than 1/300" is shown only conditional on K (tested to 16,000: at K = 16,000 the D = 30 interval is 473-631, indeterminate against the pre-registered 480 line, and the finite-size explanation is not supported). Soft selection sustains far higher rates only if fitness is purely relative. Day's premise that the summed selective differential is bounded by s_max is contradicted in-model under soft selection.
- **LTEE-to-human transfer (A2e).** Per generation, with an adaptive-only supply-limited model, the human rate exceeds the LTEE's by about 2-7x even under Day's cost caps, but the flip depends on a beneficial-fraction times effect-size ratio nobody has measured; on Day's own total-throughput basis the factor is about 50,000 and stands or falls with the human neutral rate k = mu. On the per-generation count of adaptive fixations of any effect size (A2e's formal statement) the external verdict is now **contradicted** (scoped; reading-dependent): Uricchio 2019's human-lineage, bias-corrected alpha (0.135, lower HPD 0.096) gives 798 on the most Day-charitable row, 4.2 times the 191 that flips A2e. Strong-effect-only and fitness-weighted readings stay contested. Non-coding adaptation is unsourced (gaps RG-03).
- **Regulatory waiting time (D15).** Hössjer's "far exceeds 9 My" holds in every cell inside his own stated premises (specific site, several genes, non-beneficial intermediates) and flips under beneficial intermediates, redundant sites or a non-specific gene set. No critic engages it; the literature leads are unread (gaps RG-02). External verdict provisional.
- **The 32.3 and the Hard Limits internal check (B3d, B2, B).** Day's k = 32.3 mu is his own arithmetic on his own inputs and holds on his basis (32.93); it appears only when SDR base pairs are divided by a point-mutation rate (events give 2.3-3.4, base pairs like for like 0.4-0.6, and after the ancestral term the residual is about 0.9-1.65, the "about twofold" calibration gap Keightley describes). Its "median 25 across 55 vertebrates" cites Bergeron 2023 and is not yet recomputed. Hard Limits' definition, exponent and 600,000-run demonstration all reproduce; its asymptotic prefactor is a power law, not "order one"; and it concedes the steady-state flux and a partial ancestral load, so whether the closing line "the neutral channel closes" follows turns on the reading of "the pipe was nearly empty" (reading-dependent, rule RD): rhetoric on the 6.5 My flux fill (0.697), giving B internal holds scoped to B2 with the lineage conclusion unsupported; dialectic on the delivered share (0.256), Takahata N_e 1e5 (0.281) and HL's 2 My window (0.025), giving non-sequitur. Day's concession that N/N_e never enters k removes the whole N/N_e family and B4's 200-580 kya (the latter an audit inference). Zeng 2021's "0.001" is a mean |s| under negative selection, not a beneficial mean, though Day's latency arithmetic is exact and its materiality is undetermined.
- **Day's "The Fourth Mechanism" (2026-10-10, ROOT-FM).** Day reports that substitution density across the six T2T ape genomes is "massively overdispersed", clusters into "mesas" with a human-lineage excess, and proposes sigillation (deliberate modification) as a possible fourth mechanism; he says neither selection nor drift "can still be considered viable". No code, coordinates, window size or statistic is released. A pre-registered per-lineage replication on the public alignment (R4 FM, five reviews, two fix passes) finds the overdispersion, clustering and mesas Day describes, but the pattern is shared across lineages and a shared-rate null reproduces most of it; the unmasked human-heavy excess follows the reference genome (a projection effect), and the one remaining Day-side cell (chrX) is one window in a centromeric transition region. External verdict on the conclusion: contested, leaning critic; the internal verdict on the step to "neither selection nor drift" stays pending (no premise is stated; Day's corpus has no text defending a uniform rate). "Sharp boundaries" is pending; "dominant source of divergence" is contradicted for single-nucleotide divergence on alignable sequence and untested for structural divergence. No critic has replied yet.
- **Day's dN/dS post (2026-10-11; L1, L6, L7, claims DN1-DN5, E10, A3z).** On hg38/panTro5 the human-chimp dN/dS is 0.207 on one2one genes and 0.271 on all genes, not 0.80; the gene-set effect is real (+31%) but a fraction of what 0.80 needs, and Day's own single-SNV count (2.52 nonsynonymous per synonymous against 0.85) points to an unidentified extraction/alignment problem. His inference from dN/dS to adaptive evolution is a non-sequitur on his own definitions. Open: a T2T rerun (L1b, after `ph`), CSAC 2005 and an independent ML estimate (DN5 fidelity), his per-gene table, Good 2017 SI 5.2 and the clade-level HMM states (E10), and the route to 410 M (A3z; reconstructs as base pairs, route unconfirmed).
- **Ancient DNA.** Day's "21" is contradicted as stated, but what it means turns on the Holocene Nₑ. The published estimates are now retrieved (`research/sources/holocene-ne.md`): they agree on recent growth of 100× or more but disagree on its timing, so the literature does not decide it; C1e will run the model on each published trajectory. The neutral comparison for the damage-resistant transversion class is also open.
- **Ancestral Nₑ.** The value needed to fit the observed divergence has three free parameters, so no side gets a clean fit.
- **Sequence space (D).** D1 found about 1–6 routes per needed change per locus (below G1's flip of ~7–17); a gene's shared pool of beneficial mutations clears the flip for about ten needed changes, not 25 or more. Per-sequence prevalence (Axe, Taylor) and cross-family connectivity are untouched.
- **Adaptive fraction.** How many differences needed selection at all. Nobody on either side has put this in the argument ([gaps](arguments/README.md#4-what-everyone-missed)).

**Fairness audit (X1).** The audit's own first synthesis found 22 of 112 Day claims carrying an "arithmetic error" or "doesn't follow" verdict, against 0 of 51 critic claims, and only one check aimed at a critic claim. It then recomputed every numeric critic and ally claim, wrote [one verdict rule](../research/checks/results/R4-X1-verdict-rule.md) for both sides, re-scored every numeric claim on both sides, and had the rule's application checked by a blind audit. Result under the final rule:

| Error verdicts (counts) | Day | Critics |
|---|---|---|
| claims with a number in the author's quoted words (primary) | 13 of 81 | 1 of 20 |
| claims with a number in the formal statement | 16 of 82 | 1 of 31 |
| all claims | 18 of 114 | 1 of 51 |

Raw counts per side are shown, but rates are not comparable between sides: the two sides differ in volume, in the precision of their claims, in the share of claims checked, and in how claims were routed (method audit MA-06, [`METHOD-AUDIT-2026-10-12.md`](research/METHOD-AUDIT-2026-10-12.md)). No test of difference is reported. Three earlier Day error verdicts were withdrawn under the rule, one critic claim gained one (Hancock's 38M match, on his own event basis), and the audit's own figure for keruru's tail probability was found 41× too low and corrected.

**Overall verdict counts** (all sides combined, n/a omitted):

| Verdict | Counts |
|---|---|
| Internal | 131 hold, 19 non-sequitur, 2 arithmetic error, 51 pending |
| Fidelity | 43 accurate, 38 partial, 10 misread, 58 unverifiable, 12 pending |
| External | 34 supported, 114 contested, 18 contradicted, 6 untestable, 48 pending |

Of these, **4 claims carry a reading-dependent verdict** (7 reading-dependent verdicts in all with the 3 RH tags below; rule RD, owner 2026-10-11, consistency fix same day: the verdict field takes the reading under which the quoted statement is most defensible, not the reading best for the speaker; the other readings are in the claim file's Readings table): DN6 external (2026-10-12: reading a, the 0.23 was produced by a protein-guided alignment, is contradicted by the CSAC 2005 methods text; reading b, such pipelines bias dN/dS down, is pending L1c; field pending), B9 internal (holds on the mutation-load reading, non-sequitur on the literal fixation reading), C7 internal and external, and B internal (field non-sequitur, where the Hard Limits peroration is read as dialectic; holds scoped to B2 if it is rhetoric, recorded alongside). A2e external is **SCOPED**, not reading-dependent (contradicted for the any-effect-size count, which is its formal statement; contested for strong-only and fitness-weighted). **3 further claims carry a reading-dependent RH tag with no verdict change** (Hancock RH-15 on ROOT-PG, Myers RH-20 on G2e, Mansfield RH-18 on B5).

Note that the largest external category is *contested*.

## Things a reader should weigh
These are the limits of the project itself, not of either side:

- **AI-driven work.** Nearly all of the harvesting, claim extraction, simulation code and reviewing was done by AI agents (Anthropic's Claude models), directed by one person. The steelman reviews are AI reviewing AI. Day's Zenodo papers list an AI co-author ("Claude Athos"), so the same model family appears on both sides of the audit.
- **No independent review.** Nothing has been peer-reviewed, and no human population geneticist has checked the simulations.
- **Possible lean.** The project's own planning notes record that the first-pass summaries leaned toward the mainstream view. The balance ledgers are meant to correct for that. Whether they succeed is for the reader to judge.
- **Incomplete sources.**
  - *Probability Zero* has not been purchased, so claims that appear only in the book are tagged `secondhand`.
  - Some sources could not be accessed and are listed as such.
  - Full texts are not in the repo, for copyright reasons. Readers must fetch them to check quotes.
  - None of the authors on either side has been contacted, so no one has had a right of reply.
- **Untested regimes.** Several conclusions hold only in the regimes tested: N = 1000, s = 0.01, and a single closed population. Human-scale cost of selection (H3) has been run only for hard adaptive selection with K up to 10⁴; the number of loci under selection at once at human scale has not been run. "Holds in the tested regime" is weaker than "holds".
- **A moving target.** The critics are informal and have not engaged several branches, and Day's numbers change between versions. A verdict on one version may not apply to the next.
- **Branding.** The project icon combines a double helix with a Christian cross. That was the maintainer's choice. Readers may weigh it as they see fit when judging the claim of neutrality.

## How to check it yourself
- **Start here:** `README.md` (scorecard, maths and figures), then `docs/research/ledgers/balance.md` (strongest and weakest points per side), then `research/checks/RESULTS.md` and `REVIEW.md`. For the structure of the debate, see [`docs/arguments/`](arguments/README.md): standard forms, typed objections, a genealogy and the gaps.
- **Spot-check a claim:** open any file in `docs/research/claims/`, follow its source locator, and compare the quote with the original.
- **Re-run a check:** every check runs with a fixed seed using `research/.venv/bin/python -I research/checks/<file>.py`. The textbook baselines (`baseline_textbook.py`) must pass first.
- **Questions worth asking:**
  - Does each check test the claim as its author stated it, or a convenient variant?
  - Are the "tested regime" caveats load-bearing for the headline conclusions?
  - Is the scrutiny actually symmetric? (The X1 fairness audit above is the audit's own attempt to answer this; its rule and re-score are in `research/checks/results/R4-X1-*.md`.)
- **Corrections** from either side are invited as GitHub issues, with a locator.

## Milestone posts
These dated posts tell the story in order:
1. [2026-10-07: The question, the rules, the scaffold](2026-10-07-1-kickoff.md)
2. [2026-10-07: First checks and three rounds of review](2026-10-07-2-first-checks.md)
3. [2026-10-07: Reading everything, from both sides](2026-10-07-3-reading-everything.md)
4. [2026-10-07: 193 claims, one tree](2026-10-07-4-claims-and-tree.md)
5. [2026-10-08: R4 round two, the load-bearing checks](2026-10-08-5-r4-round-two.md)
6. [2026-10-08: Making it inspectable](2026-10-08-6-going-public.md)
7. [2026-10-08: Founders, the Bernoulli barrier, and a map of the argument](2026-10-08-7-argument-map.md)
8. [2026-10-09: The cost of selection at human scale, and three gaps closed](2026-10-09-8-cost-of-selection-and-gaps.md)
9. [2026-10-09: Day's 21 on real genomes, and how many routes a mutation has](2026-10-09-9-ancient-dna-and-sequence-space.md)
10. [2026-10-09: Auditing the audit: one rule for both sides](2026-10-09-10-fairness-audit.md)
11. [2026-10-10: A second simulator, Haldane's regime, 32.3 and Hard Limits, and Day's "Fourth Mechanism"](2026-10-10-11-replication-haldane-hard-limits-and-the-fourth-mechanism.md)
12. [2026-10-10: Day's "mesas" replicated, the "median 25" recomputed, and Haldane's limit to K = 64,000](2026-10-10-12-mesas-replicated-median-25-and-k-to-64000.md)
13. [2026-10-11: Day's dN/dS post checked, "ten of twelve" and 410 M recounted, and published alpha against the 191 flip](2026-10-11-1-dnds-ten-of-twelve-410m-and-alpha.md)

## Not yet decided
- The final verdicts and the sensitivity table (R5).
- Whether the audit's conclusions bear on the root claim as a whole, or only on individual branches.
- The simulator's design.
