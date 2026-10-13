# Milestone 11: A second simulator, Haldane's regime, 32.3 and Hard Limits, and Day's "Fourth Mechanism"
*2026-10-10 · stage: R4 (in progress) · commits `dfbcbc1`, `b8516fa`, `409378f`, `32df9cf`, refresh `48021bd`*

> **[Update 2026-10-11, see [milestone 13](2026-10-11-1-dnds-ten-of-twelve-410m-and-alpha.md): A2e-alpha compared published alpha estimates with the roughly 191 threshold behind the A2e entry below. Bias-corrected estimates (Boyko, Eyre-Walker) all land above it; the lowest value is an uncorrected null, not a count. A2e external moves from contested to contested, leaning contradicted. Internal verdict unchanged.]**

> **Update (2026-10-13):** see [milestone 14](2026-10-13-1-t2t-dnds-alignment-method-overdispersion-null-adna-power-and-hf-final.md). **Fourth Mechanism:** the null model listed below as absent has been run (FMnull); Day's overdispersion sentence is true of the data and not anomalous against a neutral band where it is true, the test is weak against small mechanisms, and no verdict value moved. **H8 / H5:** the H follow-ups are final, external still `contested`, turning on the unsourced hardness h and excess R. **A2e:** external is now `contradicted`, scoped to the any-effect-size count (Uricchio full text, 2026-10-11); strong-only and fitness-weighted readings stay `contested`.

This milestone covers everything since [milestone 10](2026-10-09-10-fairness-audit.md):
- **XT:** the core results re-run in a second simulator (fwdpy11);
- **G2c:** the standing-variation check restored after a longer rerun;
- **D15:** Hössjer's claim that coordinated regulatory changes take far more than 9 million years;
- **H8/H5:** Haldane's 1/300 tested in Haldane's own regime, including a post hoc run at 16,000 individuals;
- **A2e:** how sensitive the LTEE-to-human transfer is to its inputs;
- **B3g, B3:** what Day's 2026-08-27 concession removes, and where "32.3" comes from;
- **B2/B:** Hard Limits checked against its own text;
- **F3a:** Zeng 2021 and s = 0.001;
- **independent re-reviews** of three earlier self-reviewed checks;
- **Day's "The Fourth Mechanism"** (2026-10-10), scored against the pre-registration committed before it appeared.

Each check had its script and predictions committed before the main run, and the load-bearing ones (D15, H8/H5, A2e, B2/B, B3) went through three reviews (correctness, Day-side steelman, critic-side steelman) and a fix pass. Low-stakes checks (XT, B3g, F3a) had one combined review. Reviews #22 to #42 are logged in `research/checks/REVIEW.md`. Nothing here has been peer-reviewed.

> **[Update 2026-10-10, see [milestone 12](2026-10-10-12-mesas-replicated-median-25-and-k-to-64000.md): the mesa replication, the median-25 recomputation and the K = 64,000 run named as pending or queued below are done. FM replicated Day's description but not a human-specific mechanism (external contested, leaning critic); median 25 reproduces exactly from Bergeron 2023 but the terminal-branch and lineage-average readings differ by about 1.9 times; no K trend to 64,000.]**

## XT: does a second simulator agree?
The plan required the core results to be re-run in an independent tool (fwdpy11 0.24.7; SLiM was not available).
- **Replicated:** Kimura's fixation probability within 2%; fixation probability 1/(2N) and fixation time scaling with N<sub>e</sub> (not N/N<sub>e</sub>); the exact-chain conditional fixation fraction; the excess under sourced human N<sub>e</sub> histories (3.8 to 3.9).
- **Beneficial fixation time** came out 2 to 3 times shorter than Day's (2/s)·ln(2N) latency.
- **Not replicated, and not localised:** the equilibrium deficit (21%), the expansion factor (0.699 against 0.733), and two Balloux–Lehmann rows (k/U 0.95 to 0.96; cohort 0.64). The shortfall rises with per-gamete mutation rate (a hypothesis, not tested).
- **Reading.** The qualitative findings that decide the k = μ dispute replicate. The numeric rows that Day's empty-pipeline argument uses (B1, B3b) carry an unexplained simulator-dependent deficit. Open follow-up: a U-scaling rerun or SLiM. **No verdict changed.**

## G2c / B6c: standing variation, restored
This was left "pending" after an accounting error was diagnosed. The pre-registered longer rerun (two 12,000-generation replicates) met all three criteria (concurrency 0.7 and 1.2; heterozygosity ratio 0.988; drift 1.001; no dropped sweeps). **External verdict restored to supported, as a conditional**: parallel sweeps at Day's rates do not remove standing neutral variation in these models. This is a point for the critics' side of the Hancock exchange; it still says nothing about linked-site hitchhiking, which remains untested.

## D15: Hössjer's "far exceeds 9 My"
Ola Hössjer (an ally of Day's case) predicted that the wait for several human regulatory changes far exceeds the 9 My available. The audit swept 714 parameter cells (N<sub>e</sub>, recombination, step type, redundancy, generation length) and reproduced his published tables first.
- **Inside his stated premises** (at least two new sites, a specific target, neutral or valley intermediates; 96 cells) his prediction holds in every cell: P(done within 9 My) = 0.
- **Outside them it flips:** if each intermediate step is even 1% beneficial, 9 My is reached in 57 to 77% of runs at N<sub>e</sub> = 10<sup>4</sup> and in all runs at 10<sup>5</sup>. The same is true for redundant sites, for a non-specific gene set (any m of M genes; this matters from M of order 1,000), and for his own Table 5 rows that start with the site already present.
- **Reviewers' fixes.** A "5 to 11 times" simulation-versus-chain gap was a censoring artefact; the N<sub>e</sub> = 10<sup>5</sup> neutral excess is the omitted fixation sojourn of about 4N<sub>e</sub>. The first scorecard mixed in cells outside his premises and was re-presented as an assumption map.
- **Verdicts (provisional):** internal **holds**, fidelity **accurate**, external **contested**. No critic in the corpus engages this claim, so there is no critic rebuttal to score.
- **Who this helps:** Day's side, on the arithmetic of the claim as stated. The critics' side, on the premises: the result depends on whether the real target is a valley or a path of stepping stones, and on which genes count.

## H8 / H5: Haldane's 1/300 in Haldane's regime
Milestone 8 left open whether the cost-of-selection limit really sits near 1/300 and who is right about its size. This check ran hard selection and two soft-selection models at reproductive excess R from 1.05 to 3 (726 jobs on na-workhorse).
- **Haldane's 1/300 is confirmed** at R = 1.111 with his D rescaled to 30 (interval 484 to 673 generations per substitution at K = 1,000). The budget's size is ln R: the achievable rate grows 16 to 21 times from R = 1.111 to R = 3.
- **For Day:** his verbatim statement is an upper bound and holds in every window tested; his Term 3 is 12 to 18% short at R = e, inside the audit's 25% materiality line. His premise that selection coefficients sum to at most s<sub>max</sub> holds under hard selection through the death budget.
- **For the critics:** the same premise is contradicted under soft (purely relative) selection in these models. **Hössjer's** conditional is confirmed: his 15,800 is payable from R of about 2 to 2.7 under hard selection.
- **"Slower than 1/300" is conditional on population size K.** A post hoc run at K = 16,000 (60 of 60 jobs; 409378f) scored two misses, one indeterminate and one hit against predictions made after the first run. The finite-size explanation is not supported, and the claim stays *conditional on K, tested to 16,000*. A K = 64,000 stage was proposed and not approved.
- **Verdicts unchanged:** H holds / contested; H8 holds / contested; H5 non-sequitur / contested.

## A2e: how far does the LTEE transfer to humans?
Day's LTEE-as-ceiling argument carries the E. coli substitution rate to humans. A2e varied the inputs that the transfer depends on.
- **Per generation, in an adaptive-only supply-limited model**, the human-to-LTEE rate ratio F is at most 0.104 when the supply ratio κ = 1. At κ = 93,659 (derived from Day's stated factors) F is 7.3 to 8,970 uncapped and 1.98 to 7.1 capped.
- **The flip point κ\*** is 3.9 to 13,050 (central 217): a threshold on supply times beneficial fraction times effect size, which this check cannot set. With effect sizes decoupled, the gap closes in only 6 of 96 reviewer cells (Day-side steelman).
- **On Day's own total-throughput basis** F = 50,765 per generation, conditional on k = μ (the critics' side of that dispute).
- **Verdict:** internal non-sequitur (unchanged), external **contested, with two named dependencies**. Not contradicted: the model that makes F > 1 is a supply-limited model Day rejects.

## B3g and B3: where "32.3" comes from
- **B3g (Day's concession).** On 2026-08-27 Day wrote that N<sub>e</sub> "never enters the Kimura identity". The audit confirmed this removes the whole N/N<sub>e</sub> family of k/μ factors (9.1 times to 800,000 times) and B4's 200 to 580 kya clock (back to 6 to 7 My, an inference from his equation 7). It does **not** remove 0.743 or 32.3. Credit to Day for the public correction. Verdicts unchanged.
- **B3 (32.3).** Day's 32.3 is his own arithmetic and reproduces from his inputs: 205 M over 252,000 generations, divided by Bergeron's 7.97×10<sup>-9</sup> × 3.1 Gb, gives 32.93 (1.95% off). It appears only when SDR **base pairs** are divided by a **point-mutation** rate. With measured events the ratio is 2.3 to 3.4; with base pairs like for like 0.39 to 0.56; after adding the ancestral-polymorphism term at the mandated ancestral size, 0.87 to 1.65.
- **Verdicts (B3d):** internal **holds** (on Day's basis), fidelity **misread** (the Yoo attribution: Yoo has no 187 or 205 Mb figure), external **contradicted** (as a per-site k/μ). "Median 25 across 55 vertebrates" cites Bergeron 2023; its fidelity and external verdicts are pending, and a recomputation from Bergeron's open data is queued. A prediction of the audit's own (P6, "no source") was wrong and is withdrawn.
- **The reviews changed the scoring.** The first draft scored 32.3 as an arithmetic error by applying the R1 materiality rule on the scorer's basis; all three reviews held that the rule applies on the author's basis, so it is "holds" with the unit dispute scored as external.

## B2 / B: Hard Limits against its own text
- **Found:** the definition Hard Limits needs, k(T) = μ·F(T) with F = P(fixed within T | fixation), a conditional reading.
- **Day's demonstration is reproduced** (exact mean 396.5 against his 391; of 3,000 expected by t = 100, 9.3, and his six lie inside). The exponent and the X-ceiling algebra hold. The asymptotic law understates the exact F by a power-law prefactor (17.8 to 47 times), not an order-one constant.
- **Where the audit's predictions failed.** Two sub-parts of the pre-registered P6 missed (exact F 0.029, below the predicted 0.05 to 0.30; ratio 33 against 50), and the numeric part of P7 missed. Day is credited only for his "generous" label on the linear bound. On Hard Limits' own 6.5 My window the H8 census fills the pipe to 0.70 (delivered 0.26), and its B1d grants a full pipe, so the "3% best-case fill" rests on premises Hard Limits itself drops (critic-side review).
- **Verdicts:** B2 internal **holds** (confined to current size by the abstract); fidelity stays unverifiable (uncited inputs). **B internal stays pending**: the peroration (l.453-457) is non-sequitur if read as dialectic and holds if read as rhetoric, and the tag is not clear from the text. The owner may tag it.

## F3a: Zeng 2021 and s = 0.001
Day's latency (2/s)·ln(2N<sub>e</sub>) = 19,807 at s = 0.001 is exact, and is faster than 4N<sub>e</sub> for N<sub>e</sub> ≥ 4,559. But Zeng's 0.001 is a mean |s| under negative selection; the paper has no measured beneficial mean. Verdicts: internal pending to **holds**, fidelity **misread** (re-confirmed from the raw text), external **contested** because R1 materiality cannot be decided without a sourced human beneficial mean.

## Other checks integrated since milestone 10 (no new post)
P1 (machine-checked derivations: 17 identity groups and 33 Day-arithmetic rows as predicted), B5b (Mansfield's supply: 20.7 M over 450,000 generations at an upper-bound neutral fraction, but 0.66 of 17.5 M over 252,000), F1b (in-transit count measured: F1b external **contested to supported**), C1e (the C1c model on four published N<sub>e</sub> trajectories: Day's 21 against 710 to 3,387 neutral expected on three, 31 on Nelson's), E5/E6, F1a, B2b. Independent re-reviews of E5/E6, F1a and B2b (#23 to #25) confirmed the arithmetic; the F1a re-review found that its design was near-circular, so "predictions met" is by construction.

## Day's "The Fourth Mechanism" (2026-10-10)
Refresh `48021bd`. The post appeared at 07:37 MDT; the pre-registration (`9c97fcd`) was committed on 2026-10-09 before it.
- **What it says.** Substitution density across the six T2T ape genomes is "massively overdispersed" (80 times a uniform-rate process) and clusters into "mesas" with a human-lineage excess. Day proposes **sigillation** (deliberate genomic modification) as a possible further mechanism, hedged ("may", "initial evidence"), and writes that natural selection and drift cannot "still be considered viable candidates" [sic; in context "can no longer"].
- **Released:** the data are public (T2T Primate Consortium; Progressive Cactus). **Not released:** code, mesa coordinates, window size, dispersion statistic, per-lineage counts, the "Haldane" figure, any Zenodo record. What was said on air remains unread.
- **Score against the pre-registration.** Form A (T2T comparative genomics) partial hit. The expected adaptive-share headline, total re-size, assembly-size trap and forward simulations were not reported (misses). The predicted failure mode, concluding "selection and drift not viable" without a winning branch-B argument, is a hit pending the data. The note's "conclusively proven" prediction was too harsh: Day hedges the sigillation claim. The note's form list lacked a distribution-of-substitutions variant (a gap in the note, credit to neither side).
- **For Day:** the claim is testable on public data, hedged, and revises his own relictation mechanism downward ("not the whole story"). A lineage-asymmetric excess in contiguous blocks is a pattern shape that uniform-rate neutral theory does not predict.
- **For the critics:** overdispersion is the standard signature of mutation-rate heterogeneity (CpG, replication timing), alignment error and incomplete lineage sorting; neutral theory predicts k = μ locally, so only a human-specific excess discriminates, and no per-lineage numbers are given. Units (SNV against base pair) are not stated.
- **Status:** new claim ROOT-FM, `pending / pending / pending`. A replication on the public alignment against a heterogeneous-μ neutral null is queued (load-bearing tier, pre-register first). No critic or ally reaction was found yet. *Update: replicated; see milestone 12.*

## Verdict changes
| Claim | Before | After |
|---|---|---|
| B3d (k = 32.3μ, "factor 25") | pending / unverifiable / contested | **holds / misread / contradicted** |
| B2 (Hard Limits domain) | pending / unverifiable / n/a | **holds** / unverifiable (internal only) |
| F3a (Zeng s = 0.001) | pending / misread / contested | **holds** / misread / contested |
| D15 (Hössjer, 9 My) | pending / pending / pending | **holds / accurate / contested** (provisional) |
| G2c, B6c (standing variation) | external pending | external **supported (conditional)** |
| F1b (parallel, not one at a time) | external contested | external **supported** |
| H, H5, H8 (cost of selection) | contested | unchanged; now conditional on K, tested to 16,000 |
| A2e (LTEE ceiling) | non-sequitur / contested | unchanged; two named dependencies |
| B (Hard Limits peroration) | pending | unchanged; RH tag open |
| B3, B3g | n/a | unchanged (N/N<sub>e</sub> leg withdrawn by its author) |
| ROOT-FM (new) | n/a | pending / pending / pending |

Totals after integration (218 claims): internal 113 hold, 18 non-sequitur, 2 arithmetic error, 61 pending; fidelity 40 accurate, 34 partial, 10 misread, 52 unverifiable, 22 pending; external 29 supported, 102 contested, 12 contradicted, 6 untestable, 57 pending.

## Who this helps
| Result | Helps Day | Helps the critics |
|---|---|---|
| XT | Qualitative agreement is not enough to dismiss the empty-pipeline numbers: an unexplained deficit remains | k = μ, 1/(2N), N<sub>e</sub> sets time replicate in a second tool |
| D15 | Prediction holds inside Hössjer's premises (all 96 cells) | It flips with beneficial intermediates, redundancy or a non-specific gene set |
| H8/H5 | 1/300 confirmed at Haldane's R; Day's statement is a valid upper bound | The budget is ln R; Hössjer's 15,800 payable at R of about 2 to 2.7; soft selection contradicts the premise sum |
| A2e | His total-throughput basis gives F = 50,765 | F > 1 under a supply-limited model; the gap closes in few cells only if effect sizes decouple |
| B3, B3g | 32.3 reproduces from his inputs; public self-correction credited | Units: bp over a point rate; events give 2 to 3.4; N/N<sub>e</sub> leg withdrawn |
| B2/B | The conditional definition, exponent, X algebra and demonstration all hold | Prefactor 17.8 to 47 times; Hard Limits itself grants a full pipe in B1d |
| F3a | Latency arithmetic exact | Zeng's 0.001 is negative selection |
| G2c | (neutral) | Standing variation survives parallel sweeps in these models |
| Fourth Mechanism | Public data, hedged, testable | Null model absent; no per-lineage numbers |

Reading across the table: on four claims (B3d, B2, F3a, D15) Day's own arithmetic was upgraded from pending to holds, and in the same cases the open disputes moved to units, sources or premises (B3d contradicted externally, F3a misread, D15 contested).

## What stays uncertain
- XT's unexplained deficit.
- Whether "slower than 1/300" survives at human K (tested only to 16,000). *Update: now tested to 64,000; no K trend, horizon matters (milestone 12).*
- The RH tag on the Hard Limits peroration (B internal).
- The median-25 recomputation. *Done (milestone 12).*
- Everything about mesas until a replication is run; the Fourth Mechanism claim is untested.

## Next
- **FM replication:** per-lineage mesa density against a heterogeneous-μ neutral null (pre-register first). *Done: milestone 12.*
- **Bergeron 2023** open data: recompute the "median 25 across 55 vertebrates". *Done: milestone 12.*
- **Queued:** review of the 12 new mapping claims; RH pass; E leftovers; C1d, D and GAP-07 follow-ups.
- **Stage R5** begins when the load-bearing claims without a reviewed check are resolved.

```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
