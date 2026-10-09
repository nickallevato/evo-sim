# Milestone 7: Founders, the Bernoulli barrier, and a map of the argument
*2026-10-08 · stage: R4 (in progress)*

This milestone covers four pieces of work:
- **two R4 checks:** E (LTEE founders and relictation) and G1 (what 0.02^(2×10⁷) actually prices);
- **an argument map:** the debate written out the way a philosopher would lay it out;
- **a gap hunt:** things neither side, nor this audit, had addressed;
- **corrections to the audit's own files**, found while building the map.

Each check went through the usual three reviews: correctness, a Day-side steelman and a critic-side steelman. All numbers below are final, after review.

## E: founder events and relictation
**The founder hazard (E, E3).** Day estimates that about 2.3% of founder events produce a hypermutator homozygote, a risk he says punctuated equilibrium ignores.
- **For Day:** the size holds. Exact models give 2.0–2.75% per event.
- **Against Day:** the route to the number is wrong, and two errors partly cancel:
  - one carrier is enough, not "two or more";
  - the 0.39 conditional comes from sampling with replacement.
- **E3's simulation** reproduces 2.33% only under a mean-field reading of the selection step. The literal reading gives 2.75%. That is outside the band the audit pre-registered, so its own falsifier fired. That result is recorded as is.
- **The consequence is untested.** Day himself defers it to "formal demographic modeling". The stronger wording in E3 ("independently sufficient", "minefields") is marked as overreach. Population-level fitness dips are rarer than per-event hazards suggest, by an amount that depends on N and on the threshold chosen.

**Relictation (E4).** Day's exact-chain tables reproduce exactly. It is the known multiple-merger ("sweepstakes") result: when one family can replace a large share of the population, the mean fixation time moves away from 4Nₑ.
- **What it doesn't change:** the fixation probability 1/(2N) and the substitution rate k. Day's paper says so itself, which is the critics' position on k.
- **Credit:** keruru worked the same chain to the same end on 2026-08-26. The audit's claim file had said "no response located" and now credits the post.

## G1: what the "Bernoulli barrier" prices
- **The product.** p^n = 0.02^(2×10⁷) is the probability of one pre-specified list of outcomes. Its value doesn't depend on timing, so it cannot "force sequential fixation". That inference is marked a non-sequitur.
- **Specific vs any.** Suppose each needed change can be met by several interchangeable alternatives. Then the probability of getting *some* full set jumps from about 0 to about 1 once there are 12–17 successful arisings per needed change. Day's dilemma ("either the specific fixations matter, or they're neutral noise") leaves out this middle case. Its "neutral isn't functional" half is valid.
- **The open number.** Whether real biology sits above or below 12–17 is a sequence-space question. Branch D, the next check, has to supply it.
- **The 230-sweep cap.** It does not appear under multiplicative fitness (soft selection, free recombination, N = 1000). 230 equals 157,000 × transit time / total time, so the "match" to the requirement is circular if the cap was fitted.
- **For Day:**
  - with linkage or clonal reproduction, joint success really is less than the product of the parts, which is the direction Day stated;
  - the audit's own earlier objection to the 14.7× figure ("mixed scales") was wrong and is withdrawn. 14.7 is recoverable as an additive or a log ratio, though "(1.01)^1474 ≈ 14.7×" is still false as written.

## The argument map
[`docs/arguments/`](arguments/README.md) is new. It contains:
- **Standard forms.** The root argument and 115 others as numbered premises, an inference type, and a conclusion.
- **Typed objections.** All 238 attacks, each typed as undermining (hits a premise), undercutting (grants the premises, hits the step) or rebutting (argues the opposite), with the audit's verdict on whether it lands.
- **Survival computation.** It computes which arguments survive their objections (grounded semantics) three ways: as argued, and under strict and lenient readings of the audit's verdicts. The framework has no notion of support, so the results come with that caveat and a "rejected supports" column. ROOT draws few direct objections; most land on the claims it rests on.
- **A genealogy.** 178 dated versions of arguments on both sides, from Wistar 1966 to this week, drawn as a family tree with the 13 turning points numbered.

What the genealogy shows:
- **Parallel vs serial is old.** The dispute goes back to Mayr's question to Ulam in 1966.
- **Fixation probability goes back and forth on Day's side.** Day moved from 1/(2Nₑ), to a concession, to "holds exactly regardless of offspring distribution". keruru adopted and retracted the same formula in step.
- **Both sides make unit errors.** Day counts bases as events. Two critics' "matches" double-count ancestral variation.
- **The split date doesn't move in one direction.** It goes from 9 My to 68 kya and back to 6.3 My, with no text reconciling the values.

## What everyone missed
[`gaps.md`](research/ledgers/gaps.md) lists seven gaps. Every "nobody addressed this" is backed by search terms and hit counts that can be re-run, and each entry was fact-checked. By main beneficiary: two-sided 3, critics 3, Day 1. The most important:
- **GAP-01, the adaptive fraction:** how many of the differences needed selection at all.
  - The paper both sides cite has a test pointing to little positive selection.
  - That cuts Day's 17.5M by 20× to about 6,000×.
  - Even so, the adaptive count still exceeds Haldane's rate by 1.5–7× on coding sites alone, more if any non-coding share was adaptive.
  - It helps both sides, and it now bounds check H.

[`prior-art.md`](research/sources/prior-art.md) lists the older literature that neither side cites, including the 1970s resolutions of Haldane's dilemma, Durrett & Schmidt's waiting-time results, Nunney's cost simulations and Weissman & Barton's finite-map limit.

## Corrections to the audit's own files
Building the map meant checking every link in the claim tree, and that found errors in the audit itself:
- **Links:** 17 objection links were mis-typed or aimed at the wrong claim. They were retyped, retargeted or removed, each with a comment.
- **Hössjer's "2.2×" gap** does not appear in his text. His equations give 1.94× ("a factor of 2") and 2.63×. The 2.2 is just 1/d (1/0.45), which the audit had wrongly attributed to him. Corrected in five files.
- **A missing post:** "Where the Errors Hide" (2026-09-21), a Day post the version ledger had missed, was added. Its covariance objection already appears in the 08-27 concession, so that concession was qualified from the start.
- **keruru's side** is now dated: ally before the 2026-08-26 retraction, critic from that post on.
- **A new claim** for Hössjer's prediction that the waiting time "far exceeds" 9 million years (D15).

## Process change
The E and G1 scripts had no commit before their main runs, so their pre-registered predictions can't be proven from git. From now on each check script is committed with its predictions before the main run.

## Where things stand
```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
| Next | What it settles |
|---|---|
| H at human scale | The one place the overall verdict could still go either way, now bounded by GAP-01 and cross-checked against Nei and Felsenstein |
| GAP-04, GAP-07, GAP-02 | Quick fits and arithmetic: the finite-map cap, indel/SV event counts, how far back sweep scans can see |
| D | The number G1 left open: interchangeable routes per needed change |
| C1b | Day's ancient-DNA "21" with realistic call depth |
