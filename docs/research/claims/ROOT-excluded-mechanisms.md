---
id: ROOT-M
title: "Which named mechanisms Day says are excluded, and whether the corpus holds a quantitative argument for each"
side: day
branch: ROOT
parent: ROOT
edges: [{type: depends-on, target: ROOT},{type: supports, target: ROOT}]
load_bearing: true  # ROOT is a universal claim over mechanisms; each row without a computed exclusion is a gap in the quantifier
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # per-row verdicts live in the branch claims
  fidelity: n/a      # catalogue, not a single assertion
  external: pending      # depends on the rows below
---

## Statement (verbatim)
> "my own demonstration of the mathematical impossibility of evolution by natural selection, selective sweeps, neutral sweeps, genetic drift, ILS, biased gene conversion, and every other imagined mechanism"

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, para 3.

> "Defenders of the theory have constructed what we term the post-Darwinian polythesis: a shifting constellation of supplementary mechanisms — neutral drift, parallel fixation, supermutation, hitchhiking, epistasis, clonal interference, compensatory mutation — each invoked ad hoc to answer a specific mathematical objection, but never tested collectively."

Source: MITTENS 3.0 (Z23003785), Abstract, p.1.

> "Each mechanism was invoked to answer a specific objection. None was invoked alongside the others. No calculations of their effects, individual or cumulative, were ever attempted or provided. No efforts were made to show how these various mechanisms were sufficient to supply the observed shortfall."

Source: MITTENS 3.0 (Z23003785), Section 1 'The Post-Darwinian Polythesis', extracted-text line 45.

> "So is any and every evolutionary mechanism, with the exception of three minor ones."

Source: [Math Teacher Can't Math](https://voxday.net/2026/09/30/math-teacher-cant-math/), 2026-09-30, para 6; the three are named later in the post as sexual recombination, incomplete lineage sorting and horizontal gene transfer.

## Formal statement
Table of the mechanisms Day names as excluded. "Computed" means the corpus contains an equation, a worked number or a dataset-based count that targets that mechanism (whether or not it is right). "Asserted, not computed" means the only support found is a sentence of assertion. Searches were run over every Day blog post and Zenodo text in `sources/raw/day/` (keywords listed per row); a negative result means "not found in the harvested corpus" and excludes the paywalled books (Probability Zero 1st/2nd ed., The Frozen Gene, Hardcoded) which were not accessed.

| # | Mechanism (Day's term) | Where Day excludes it (key, locator) | Quantitative argument in corpus? | Hierarchy / claim ID | Notes |
|---|---|---|---|---|---|
| 1 | Natural selection, hard sweeps | MITTENS (Z18165980; Z23003785) | **Computed**: F_max = T_gen/G_f, G_f from LTEE | A, A1-A5, F, H | Inputs and scaling contested (A3x, A5, B7 fidelity findings). |
| 2 | Parallel fixation | Bernoulli paper Z18167588; MITTENS 3.0 | **Computed** (Bernoulli product; ~230 simultaneous-sweep cap "working backward from the constraint"); LTEE G_f is an empirical aggregate that includes parallelism | G, G1-G3 | The ~230 cap is stated as derived from the constraint, not independently (versions ledger). |
| 3 | Soft sweeps / standing variation | Z18452504 section 4.3 | **Computed**: t ~ (2/s)ln(1/p0); ratio ln(20)/ln(10,000) = 0.325 (recomputed: ln 20 = 2.996, ln 10^4 = 9.210, ratio 0.3253) -> "factor of ~3" | G / A | Deterministic approximation; Wistar-era and modern sweep-time results not compared (B0.4 found (2/s)ln(2N) overshoots the conditional time by ~2.3x at Day's parameters). |
| 4 | Neutral drift | Z22129121 Hard Limits; Z18441321 section 3.2; blog 2026-09-30 'Math Teacher Can't Math'; Z18429937 | **Computed**: X = (Vk+2)G/16 ceiling; 4Ne latency; 'Drift Deathmarch' load argument (75% harmful mutations; collapse in 9 generations) | B, B1-B3, B2, F, F1 | Latency vs throughput (F1) and N vs Ne (B3/B7) disputes apply. Load argument: assumed share of harmful mutations and damage per mutation are unsourced here (to extract). |
| 5 | Neutral sweeps | Named only in Best They've Got I (para 3) | **Asserted, not computed**: no occurrence of 'neutral sweep' anywhere else in the Day corpus | ROOT-M | The term may refer to hitchhiking (row 6) or to drift (row 4); no separate argument found. |
| 6 | Hitchhiking / linked neutral fixations | Z18452504 section 4.3 ('Linkage and Hitchhiking'); MITTENS 3.0 section on hitchhikers | **Computed**: block size r/s (r=1e-8, s=0.01 -> 1e-6/bp -> 1 Mb; recomputed); 3,200-32,000 blocks; ~20.5 neutral hitchhikers per 50,000 gens in the LTEE counted inside the 56.0 fixations | E1, A2, A6, A6a | Static-block calculation; the LTEE count is an empirical subset of the fixations. Item (4), the sweep-signature corollary, is claim A6 (bonobo version A6a); R4 GAP-02 (2026-10-08): saturation does not follow at the stated 3,200 with a ~10,000-generation detection window; classic sweeps are rare (Hernandez 2011), which constrains hitchhiking as the main source of fixations. |
| 7 | Incomplete lineage sorting (ILS) | Z18452504 section 4.3; Z18441321 section 3.3; blog 2026-04-28 'Less Than Zero' ('four independent reasons' in the first edition, not retrieved) | **Computed**: 4*Ne*mu*L = 4*1e5*1.5e-8*3.2e9 = 1.92e7 (recomputed 1.92e7), x 0.15 mean reciprocal-sorting probability = 2.88e6 ('~2.9 million') | B / C (new ILS claim to extract) | Ne 50k-100k used, versus 132k-198k in Yoo 2025 (parameters.yaml). 4*Ne*mu*L is theta*L (expected pairwise-difference scale), not the number of segregating sites; whether this is the right ceiling is for the branch-B owner. The 0.15 average is an assumption. Yoo's 39.5% ILS (blog 2026-04-28) is not reconciled with the 2.9M ceiling in any retrieved Day text. |
| 8 | Biased gene conversion (gBGC) | Named only in Best They've Got I (para 3) | **Asserted, not computed**: searched 'gene conversion', 'gBGC', 'BGC' in all Day blog and Zenodo texts; only that sentence | ROOT-M | No argument, no equation, no citation. |
| 9 | Hypermutation / supermutation | MITTENS 3.0 abstract and sections; Z23020792; Z23034852 | **Computed/empirical**: mutator populations achieve 8.5-17x, not 100x, throughput; 'three independent lines of genomic evidence' that no supermutational phase occurred | E | Empirical LTEE statistic; the three 'lines of evidence' are in Z23003785 (to be extracted under E). |
| 10 | Epistasis, clonal interference, compensatory mutation, frequency-dependent selection, eco-evolutionary dynamics | MITTENS 3.0 section 1 and LTEE argument; blog 2026-10-01 'They Never Stop Lying' | **Bounded empirically, not computed individually**: all operate in the LTEE, so the aggregate G_f is said to include them; Day states of the defenders' mechanisms: 'No calculations of their effects, individual or cumulative, were ever attempted or provided.' | A2, G1 | Day does not compute their separate effects either; the argument is that the aggregate is a ceiling. LTEE-to-vertebrate transfer is A5. |
| 11 | Sexual recombination | blog 2026-09-30 ('only recombination could even theoretically speed things up, and the reproductive constraints ... more than compensate'); Z18637297 transmission-channel-capacity survey | **Partly computed**: Z18637297 surveys mu/r across six taxa; the net-effect sentence in the blog is **asserted, not computed** | B / G (new) | Z18637297 argues recombination is saturated in mammals (mu/r ~ 1-1.5); not extracted yet. |
| 12 | Horizontal gene transfer | blog 2026-09-30 ('populations are maintained in isolation'; 'Of those three, only recombination could even theoretically speed things up') | **Asserted, not computed** | ROOT-M | For a human-chimpanzee comparison HGT is not claimed by critics in the corpus; row kept for completeness. |
| 13 | Hybridization / introgression / gene flow | blog 2026-01-07 ('Hybridization and introgression ... actively work against the fixation of lineage-specific mutations') | **Asserted, not computed** | ROOT-M | Day treats it as opposing fixation, not as a source of divergence. |
| 14 | Gene duplication, whole-genome duplication, de novo genes, exon shuffling, regulatory evolution | blog 2026-05-13 (WGD 'totally irrelevant to the throughput argument, for three reasons'); blog 2026-03-04 (critic's list) | **Asserted/argued in prose, not computed** for the human lineage | A3x (event vs bp) | The structural-variant bp-vs-event dispute (A3x) is the quantitative handle. |
| 15 | Punctuated equilibrium / founder events | Z23020792; Z23034852; blog 2026-09-29 | **Computed** (hazard ~2.3% per founder event; strong-s zones, per hierarchy.yaml; not re-verified here) | E | Not extracted here. |
| 16 | Non-random (biased) mutation | blog 2026-01-19 Q&A | Day **adds it as a further penalty**: 209,500 -> 157,125 effective generations (ratio 0.750) | A | Direction: Day treats non-random mutation as hurting evolution, i.e. a constraint, not a mechanism. |
| 17 | Cost of selection (Haldane) | Z18168236, Z19984826 | **Computed** but partially retracted 2026-05-07 (Term 3) | H, H1 | See versions ledger. |
| 18 | Relictation (bottleneck family replacement) | Z23188201, 2026-10-06 | Day **does not exclude it**: presented as a 'third evolutionary mechanism' alongside selection and drift | ROOT-M | Its effect on divergence timing relative to ROOT is not computed in the retrieved text; the abstract says fixation operates on haplotype blocks. This is Day-side material that sits awkwardly with a universal exclusion; flagged, not judged. |
| 19 | 'Every other imagined mechanism' | Best They've Got I | **Open**: unbounded set; cannot be computed | ROOT-M | A universal over unnamed mechanisms is untestable until each is named (Z18452504 'burden of the alternative' places the burden on critics). |
| - | Intelligent Genetic Manipulation (IGM) | blog 2024-05-06 | **Not excluded** by Day: 'not mathematically ruled out by MITTENS' | ROOT-M | ROOT is a claim about unguided mechanisms; Day's alternative is outside it. |

Totals (rows 1-18 named mechanisms): computed or empirically bounded: 1, 2, 3, 4, 6, 7, 9, 15, 17 (9 rows) plus partial: 10, 11, 16; **asserted, not computed: 5, 8, 12, 13, 14** (5 rows); Day-accepted: 18.

## Assumptions
- Stated: each mechanism either fails the same rate bound (LTEE G_f) or is separately bounded.
- Implicit: a mechanism with no named quantitative bound is covered by the aggregate LTEE bound (rows 10-12) or by the burden of the alternative (row 19). Both are positions on who must compute, not computations.

## Responses
- Against: no critic engages the table as such. For rows 3-4 and 7 critics argue ILS and drift differently (Mansfield B5/B6; McCarthy; Yoo 2025's 39.5% ILS figure quoted by Day), but the corpus has no critic calculation of ILS.
- In support: Day points to the LTEE as a single experiment in which rows 1, 2, 4, 6, 9, 10 all operate. This is a real strength of the design and equally a limit: the LTEE is asexual, so rows 7, 11, 12 are outside it (Day says so himself: blog 2026-09-30).
- Weaknesses: counts of rows are by keyword search over harvested text; paywalled books may contain computations for the five 'asserted' rows (esp. the first-edition 'bestiary of failed defenses' with 'four independent reasons' for ILS, which Day says exists in print).

## Primary literature
| Cited work | What it actually says | Fidelity |
|---|---|---|
| Yoo 2025 | ILS 39.5% of the autosomal genome (as cited by Day, blog 2026-04-28) | not verified in this file |
| Takahata 1993; Chen & Li 2001 (Ne 50-100k, cited in Z18452504) | not retrieved | unverified |
| Yoo 2025 ancestral Ne | 132k-198k (parameters.yaml) | verified (ledger) |

## Pre-registered prediction
Written before any per-row check.
- Under the claimant's model: every 'computed' row's check returns a shortfall > 10^2 once scaling is validated; the 'asserted' rows contribute negligible divergence in T (gBGC, HGT and introgression cannot supply 10^7-10^8 differences).
- Under the opposing model: ILS plus neutral substitution along a full pipeline supplies most of the observed differences with no shortfall (B6), because the ancestral Ne was 132k-198k and the ancestral polymorphism budget is far above 1.9e7; hitchhiking and recombination change what counts as an independent fixation.
- Result that would change a verdict: a forward simulation under Day's own T and a validated scaling in which any single row delivers >= F_req changes ROOT; a computed bound for rows 5, 8, 12, 13, 14 would remove the 'asserted' tag.

## Check
Arithmetic recomputed in this file (python3 -I): 4*1e5*1.5e-8*3.2e9 = 1.92e7; 1.92e7*0.15 = 2.88e6; ln(20)/ln(1e4) = 0.3253; 1e-8/0.01 = 1e-6 per bp (1.0 Mb); 157125/209500 = 0.7500. All reproduce Day's stated values. No simulation run.

R4 GAP-02 (research/checks/results/R4-GAPS-04-07-02.md): row 6's sweep-signature corollary is now claims A6 (Z18452504 §4.3(4)) and A6a (Z18441321 §3.1). Expected detectable completed sweeps (power 1): ~98 at Day's stated 3,200 in the sourced ~10,000-generation window, up to ~1,000-3,250 at the top of his block and N_e ranges; the cited scans are threshold-limited lists of mostly incomplete sweeps. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

## Simulator variables implied
Mechanism switches (sweep/hitchhike/drift/ILS/gBGC/recombination), ancestral Ne and polymorphism budget (4*Ne*mu*L vs S), reciprocal-sorting probability distribution, recombination rate r and block size, per-mechanism fixation counts reported separately, event-vs-bp unit.
