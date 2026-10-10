# Milestone 12: Day's "mesas" replicated, the "median 25" recomputed, and Haldane's limit to K = 64,000
*2026-10-10 · stage: R4 (in progress) · commits `d723064` (FM pre-registration), `5f05791`, `e201384`, `455f22b` (integration); B3m `5ca5f2e`, `4442c99`; kscale64 `15e4941`, `6f8eaa0`*

This milestone covers what was pending or running at the end of [milestone 11](2026-10-10-11-replication-haldane-hard-limits-and-the-fourth-mechanism.md):
- **H8 kscale64:** the post hoc run of the cost-of-selection check at population sizes up to K = 64,000;
- **B3m:** Day's "median 25 across 55 vertebrates", recomputed from Bergeron 2023;
- **FM:** the replication of Day's "The Fourth Mechanism" on the public T2T ape alignment, with a mirror test and two fix passes.

FM is a load-bearing check (three reviews, then a combined re-review and a light review of the second fix pass); B3m and kscale64 are low-stakes (one combined review each). Reviews #43 to #49 are logged in `research/checks/REVIEW.md`. Nothing here has been peer-reviewed.

## H8 kscale64: does "slower than 1/300" depend on population size?
Milestone 11 left this as "conditional on K, tested to 16,000". A post hoc run at K = 64,000 (60 of 60 jobs on na-workhorse; predictions K1' to K4' committed first, `15e4941`) scored one miss, one indeterminate and two hits (one of them with a marginal miss at R = 2).
- **No K trend.** The survival intervals at D = 30 and the 10,000-generation horizon are 566, 484, 441, 546 and 348 generations per substitution across the five population sizes from K = 500 to 64,000. They are not monotone.
- **The horizon matters as much as K.** The same K = 64,000 runs give 348 at a 10,000-generation horizon and 490 at 20,000. The bracket for the 10,000-generation value (294 to 368) straddles 300, so the claim "slower than 1/300" is indeterminate there, not refuted and not confirmed.
- **R = 2 is about 5.7 times faster than 1/300 at every K tested** (hit). Day's statement as an upper bound holds in every window.
- **Reading.** "Slower than 1/300" stays *conditional on K (now to 64,000) and on the survival horizon*. The finite-size explanation is still not supported. **No verdict changed** (H, H5, H8 stay contested).

## B3m: Day's "median 25 across 55 vertebrates"
Day's k/μ = 32.3 appeals to a median of 25 across 55 vertebrates, citing Bergeron 2023. The audit recomputed it from the open Table 9 (pre-registered `5ca5f2e`).
- **Reproduced exactly.** The median k/μ is 25.4 (n = 55, matched per year and per generation). Fidelity **accurate**; credit to Day for a citation that checks out.
- **Terminal branches against lineage averages.** The tabulated rates are terminal-edge rates (chronos λ = 0) that cover about 21 My of a 416 My root depth. A lineage-average k computed from the same tree is at least about 2 times μ (a lower bound), against 25 for the terminal-edge figure. A ratio of roughly 1.9 separates the two readings of the same data.
- **The 2-versus-25 gap is unexplained.** Which reading Day's argument needs is not stated, and which species failed the tree match (67 of 68 matched) is open. Two major review findings were answered in the fix pass.
- **Verdicts:** fidelity pending to **accurate**; external **contested**. The internal verdict is n/a (a reported statistic, no derivation by Day).
- **For Day:** the number he cites is in the paper and reproduces. **For the critics:** it is a terminal-branch quantity; averaged along lineages the same tree gives about 2.

## FM: Day's "mesas" on the T2T ape alignment
Day's post of 2026-10-10 (see milestone 11) said substitution density across six T2T ape genomes is "massively overdispersed", clusters into "mesas" with a human-lineage excess, and that selection and drift can no longer be viable (sic). The audit ran his named data (the T2T Primate Consortium 8-way Progressive Cactus alignment, hs1-referenced MAF, 5,366,631 blocks) through a frozen, pre-registered pipeline (`d723064`) and counted substitutions by parsimony on four lineages: human (H), chimp (C), bonobo (B) and gorilla (G). Day's code, window size and statistic are unreleased, so the mesa rule and windows are the audit's. All results are scoped to hg38- and orangutan-alignable sequence (about 86% of 1-kb bins).

**What replicated, in Day's favour**
- **Overdispersion above 80 times is reachable.** At 1 Mb the dispersion index φ is 136 for human, 125 for chimp, 93 for gorilla and 826 for unpolarised human-chimp differences. The magnitude depends on the window: φ grows roughly linearly with W (3.3 at 1 kb to 136 at 1 Mb), so the same data give 3 times or 800 times.
- **Clustering is real.** 32 to 53% of human-mesa windows lie inside chimp mesas, against a 0.56 to 1.0% background. Mesas exceeding both 191 and 840 substitutions exist (F0 100 kb: 32 human mesas above 840).
- **His invitation to replicate was workable** with public data (one 3.4 GB file, about 70 minutes on one core).

**What the discriminating tests found, in the critics' favour**
- **The pattern is shared.** Chimp, bonobo and gorilla show it too (32 human, 29 chimp, 31 bonobo and 19 gorilla mesas above 840). Against a null that shares regional rate variation across lineages the dispersion shrinks to about 2.4 to 2.7 (F2 100 kb), and the null reproduces 64 to 69% of human mesas (P3, P4, P5 all critics' hits; P4 specific-mesa ratio 0 of 0 at the registered cell).
- **Human mesas hold 1.25 to 2.5% of human-chimp single-nucleotide differences**, not a "dominant" share (P7; FM8b contradicted for SNVs on alignable sequence). Structural, indel and segmental-duplication divergence are not measured.
- **Mirror test (post hoc, pre-registered `737648e`).** Re-running the frozen pipeline on the chimp-referenced MAF: the autosomal human-heavy excess seen in unmasked sequence follows the reference. On the chimp reference the chimp lineage is heavier (R 0.25 at 100 kb). Critic hit (M1). It vanishes once paralogous rows are removed.

**What stays with Day, and what is indeterminate**
- **chrX hotspot (M3, a Day-side hit).** In F1 at 100 kb the human residual on chrX crosses the 3-fold cut the audit pre-registered as Day's prediction (3.76; 3.39 on the chimp reference). It is not a registered cell (P3 was registered on autosomes). Fix pass 2 (`e201384`, post hoc) shows it is one orthologous window (CHM13 chrX 57.3 Mb = chimp chrX 58.1 Mb) in the centromeric transition region; without it R is 1.16 on hs1 and 1.11 on the chimp reference. Its cause is unknown, and it is not a mesa.
- **"Sharp boundaries" is indeterminate.** Calibrated against a perfect step, the observed edge sharpness at 10 kb is 0.88 to 0.92 of a perfect step: the registered Day bound is met in one of two cells, the critic bound in neither. The estimator cannot separate a step from a 10-kb ramp. An earlier "soft at 100 kb" wording was withdrawn as a resolution artefact (review D-1).
- **A residual of 2.3 to 2.7 in every lineage (gorilla 4.4) is unattributed.** The shared-rate null is not a mechanistic neutral model; Day-side, it does not show that drift with variable μ produces the mesas, and critic-side, the residual is an upper bound under a better-specified null.
- **Process note.** The first scoring of the mirror test was challenged in the combined re-review (2 MAJOR: edge-sharpness calibration, FM10 wording); both were answered. The audit's own P1 prediction for 1 Mb (200 to 4,000) missed.

**Verdicts (proposed in the write-up, integrated in `455f22b`)**
- FM3 (">80 times"): holds (weak sense) / unverifiable / supported (as a description).
- FM4 (clustering, "sharp boundaries"): clustering supported and shared; sharp boundaries pending.
- FM5 (one mesa exceeds MITTENS and Haldane): holds (literal) / unverifiable / supported, non-discriminating (equally true of chimp).
- FM7 (lineage-specific mesas): contested, leaning critic.
- FM8b ("dominant source"): contradicted for SNVs on alignable sequence.
- FM10 ("neither selection nor drift viable"): external **contested, leaning critic**; internal **pending** (see below).
- ROOT-FM: pending / pending / contested.

**FM10 internal.** The step from "mesas exist" to "neither selection nor drift is viable" needs the premise "drift implies a uniform rate". A grep of Day's corpus for it (rule N) did not trigger N2b (Day's own material contradicting the premise); whether the conclusion simply exceeds its premises (N2d) is unresolved, so internal stays pending.

## Verdict changes
| Claim | Before | After |
|---|---|---|
| ROOT-FM (Fourth Mechanism) | pending / pending / pending | pending / pending / **contested** (leaning critic) |
| FM3 (">80 times") | n/a | **holds** (weak) / unverifiable / **supported** |
| FM4 (clustering) | n/a | clustering **supported**; "sharp boundaries" pending |
| FM5 (mesa vs MITTENS/Haldane) | n/a | **holds** / unverifiable / supported (non-discriminating) |
| FM7 (lineage-specific mesas) | n/a | external **contested** |
| FM8b ("dominant source") | n/a | external **contradicted** (SNVs, alignable) |
| FM10 (neither viable) | n/a | internal pending; external **contested** |
| B3m ("median 25") | pending / pending / pending | n/a / **accurate** / **contested** |
| H, H5, H8 (cost of selection) | contested; conditional on K to 16,000 | unchanged; conditional on K to 64,000 and on horizon |
| B3d (k = 32.3μ) | holds / misread / contradicted | unchanged |

Totals after integration (225 claims): internal 115 hold, 18 non-sequitur, 2 arithmetic error, 62 pending; fidelity 41 accurate, 34 partial, 10 misread, 54 unverifiable, 22 pending; external 32 supported, 106 contested, 13 contradicted, 6 untestable, 56 pending. The argument map now holds 401 typed objections and 222 dated versions.

## Who this helps
| Result | Helps Day | Helps the critics |
|---|---|---|
| H8 kscale64 | The upper bound holds at every K; "slower than 1/300" is not refuted at the 10,000-generation horizon (bracket straddles 300) | No K trend; the effect is the horizon, so the finite-size explanation is not supported; R = 2 is 5.7 times faster than 1/300 |
| B3m | The cited 25 reproduces exactly from Bergeron 2023 (fidelity accurate) | Terminal-edge rates; lineage-average k is about 2 times μ; the gap is unexplained |
| FM description | Overdispersion above 80 times, clustering, and mesas above 840 all replicate; data were public and testable | The same holds for chimp, bonobo and gorilla |
| FM discriminators | chrX F1 hotspot (3.76), one window of unknown cause; human mesas outnumber chimp mesas in all four cells (ratio 1.06 to 1.32); unmasked human residual is highest | Shared-rate null reproduces 64 to 69%; 1.25 to 2.5% of divergence; mirror test: excess follows the reference |
| FM sharp boundaries | Edges at least 0.88 of a perfect step at 10 kb | Not shown sharper than chimp edges; indeterminate |

Reading across the table: Day's descriptive statements replicate, and every pre-registered test that separates a human-lineage mechanism from a shared one fell on the critics' side except one unregistered window. What is left for Day's side is the unattributed residual and the chrX window; what is left for the critics' side is a null that is borrowed, not mechanistic.

## What stays uncertain
- **FM10 internal** is pending on rule N2d (does the conclusion exceed its premises?).
- **The chrX window's cause** (57.3 Mb, centromeric transition region): real human-lineage change, annotation or repeats the filters miss.
- **The residual of 2.3 to 2.7** after the shared-rate null, unattributed in every lineage.
- **Day's own mesa rule and window** are unreleased; the audit's rule is its own.
- **Structural and segmental-duplication divergence** are not measured, so FM8b is silent on total divergence.
- **B3 Q157** (the Hard Limits peroration RH tag, claim B) awaits the owner.
- **The 2-versus-25 gap** in B3m, and which species failed the tree match.
- **"Slower than 1/300"** at human K and long horizons.
- **XT's unexplained deficit** is unchanged.

## Next
- A U-scaling rerun or SLiM for XT.
- Review of the 12 new mapping claims; the RH pass; E leftovers.
- Stage R5 begins when the load-bearing claims without a reviewed check are resolved.

```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
