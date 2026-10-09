# Milestone 10: Auditing the audit: one rule for both sides
*2026-10-09 · stage: R4 (in progress)*

This milestone covers four pieces of work:
- **X1:** an arithmetic audit of every number the critics and allies use, and one written verdict rule applied to Day and the critics alike;
- **GAP-07c:** how many of the human–chimp differences are still variable within humans;
- **the mapping round:** every critic and ally argument now has a place in the argument map;
- **the Holocene Nₑ retrieval:** what the published literature says about Europe's population size over the last 10,000 years.

## X1: was the audit itself fair?

**How the question came up.** The first draft of the R5 synthesis counted verdicts by side. 22 of Day's 112 claims carried an "arithmetic error" or "doesn't follow" verdict. 0 of the critics' 51 did. Only one check had ever targeted a critic claim. The plan always had an "arithmetic audit of both sides" step, and it had never been run for the critics.

**What X1 did.**
1. Recomputed all 45 numeric critic and ally claims from their own stated inputs. The predictions were committed first.
2. Three reviews followed (correctness, Day-side, critic-side). They agreed on one thing from opposite directions: there was no stated rule. The Day-side review found critic slips excused that Day had been penalised for. The critic-side review found critic slips penalised more harshly than Day's.
3. So X1 wrote [one rule](../research/checks/results/R4-X1-verdict-rule.md) and re-scored every numeric claim on both sides under it, Day's included.
4. A fresh agent then applied the rule **blind** to Day's error claims and every critic candidate, and compared its calls with the re-score. It agreed on 90% of Day calls and on every critic error / no-error call. It also found clauses that bit one side harder.
5. The rule was revised (rev 2) and everything was re-scored again.

**The rule, in short.**
- **One slip test.** A mistyped number (Day's typical slip) and a left-out term (the critics' typical slip) are judged the same way. Each is an error only if fixing it moves the author's own stated conclusion, on the author's own basis, by more than 25%, or flips it. Smaller slips go to a ledger.
- **What gets scored.** The quoted claim and its derivation. Slips in blog comments, replies and video asides go to the ledger, on every side.
- **"Doesn't follow"** means the conclusion fails against the author's own numbers or text. A disputed premise is a question of realism, not logic.
- **Uncited inputs** are "unverifiable" on both sides.
- **Charity.** The most charitable reading of an ambiguous number is tried, and recorded, for every claim.
- **No loophole for steep functions.** A ±25% allowance on an input cannot rescue a probability that swings by orders of magnitude.

**The result.**

| Error verdicts under one rule | Day | Critics | Fisher p |
|---|---|---|---|
| claims with a number in the author's quoted words (primary) | 13 of 81 | 1 of 20 | 0.29 |
| claims with a number in the formal statement | 16 of 82 | 1 of 31 | 0.038 |
| all claims | 18 of 114 | 1 of 51 | 0.008 |

Per 10,000 quoted words: Day 22.7, critics 10.0. If the three close calls on the critic side had gone the other way, the gap disappears (16 of 82 against 4 of 31, p = 0.58).

**Reading.** Day's error rate is higher on every measure, and his errors hold up under any reasonable reading: most contradict his own table, equation or paragraph. What the counts cannot show is that the critics make fewer errors per argument. Their claims are mostly one-line identities from a single comment or video, so they have had less room to err. Day has written far more, and a rule about "contradicted by your own text" exposes whoever wrote more. So neither "Day's argument is worse" nor "the audit is biased" follows from these numbers.

**What changed, on each side.**
- **For Day.** Three earlier error verdicts were withdrawn:
  - **His 205M total.** Read charitably (187 Mb per lineage), 35M + 2 × 187M = 409M, within 0.24% of his 410M. The unit problem (base pairs vs events) is separate and stands.
  - **The Bernoulli-barrier 14.7.** It is a label slip, and his conclusion of 107 survives at 106.5.
  - **One claim (F)** had been counted twice for a step that belongs to another claim (F1a).
  - **Two 12% rounding slips** moved to the ledger.
- **Against Day.** His MITTENS 3.0 §6.4 "38,400 mutations" should be 3,840. A Reddit commenter caught it on 2026-09-28. It had never been recorded against Day, and now has its own claim (A5h), scored an arithmetic error.
- **Against the critics.** Hancock's "38 million matches" doesn't follow on his own event-count basis: adding the ancestral variation he leaves out makes his prediction 46% too high.
- **For the critics.** keruru's tail probabilities, first flagged as 10 orders of magnitude off, reproduce exactly at his own measured population size (about 8,100). His method isn't recorded, so the claim is "pending", not an error.
- **The audit's own error.** The audit's figure for that probability (1.2×10⁻⁴⁶) was 41× too low. It is corrected in three files, with dated notes.
- **A misattribution.** The "gap under a factor of two" argument belongs to a different Reddit commenter (justatest90) than the one the audit had credited.

## GAP-07c: how much of the 205M gap is still-variable sites?
The direct genome count (GAP-07b) found about 21 million mutation events per lineage, against Day's 205 million base pairs. Some of those events are still variable within humans, so they are not fixed. Measured with 1000 Genomes:
- **Single-letter differences.** 15.6% of human-lineage differences are still polymorphic, at the low end of the 2005 consortium's 14–22% estimate.
- **Larger changes.** Insertions/deletions are 7–9% polymorphic, and structural variants about 7%.
- **The chimp side** could not be measured, so it is assumed.
- **For Day.** 84% of the differences are fixed. Large variants are mostly fixed, which is consistent with his "post-divergence" point. His single-letter-only 17.5M sits within 2% of all fixed events.
- **For the critics.** That near-match is two offsetting errors: like for like, 17.5M is 10% above the fixed single-letter count. On fixed events, 205M is **10.6–12.6×** too high as a count, or about **8–13×** with GAP-07b's assumptions. Polymorphism is a 10–20% correction. The roughly 10× unit mismatch stands.

## Every critic and ally argument now mapped
- **What "mapped" means.** The audit ratified a definition: an argument is mapped if it sits in the claim tree and either has an objection attached or carries an explicit "no attack warranted" note.
- **What was added.**
  - 27 objections.
  - 12 new claims from Hancock and Gutsick Gibbon's video. 10 are critic arguments, such as "selection is a covariance" and "the cost of selection applies only to hard selection". 2 are the Day-side statements they answer.
  - 32 caption quotes, each checked against the transcript.
- **No attack warranted.** Three arguments genuinely attack nothing and say so: Samson and Camestros on an accounting identity both sides accept, and a Dembski position statement.
- **Three possible Hancock slips** are recorded as untested objections, not verdicts. The most notable: his "factor of two error" charge against Day's fixation-time formula looks contradicted by Kimura & Ohta 1969.
- **Agreement across sides.** McCarthy, Hössjer and keruru each agree with Day that divergence dates depend on the assumed neutral rate. That is recorded as support.
- **Exit criterion 2** of the research phase is therefore met. The 12 new claims still await review.

## Holocene Nₑ: the literature doesn't decide it
C1c showed that whether Day's ancient-DNA "21" is a real deficit depends on Europe's effective population size over the last 7,000 years. The audit retrieved the published estimates: 37 open-access papers and 63 verified quotes.
- **No study supports a constant ~10,000 to the present.** Every method that can see recent times finds growth of 100× or more.
- **For most of the window, fitted values sit around 1,500–12,000.**
- **The models disagree on when the growth happened.** Most put it in the last 1,000–3,500 years. One large study (Nelson 2012) puts it much earlier.
- **Under the flatter models,** neutral evolution predicts roughly 40–190× more events than 21, which favours Day's deficit reading. **Under the earlier-growth model** it predicts about 32–35, so 21 needs no explanation.
- **The window that matters (3,000–7,000 years ago) is the least constrained by any method.** The next check, C1e, runs the model on each published trajectory.

## In progress
- **XT:** core results re-run in a second simulator (fwdpy11), as the plan requires.
- **D15:** Hössjer's claim that coordinated regulatory changes take far more than 9 million years.
- **Queued:**
  - C1e;
  - Mansfield's mutation-supply argument;
  - latency vs throughput (the in-transit count is assumed, not measured);
  - Hancock's standing-variation prediction;
  - reviews of the 12 new mapping claims.

## Where things stand
```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
- **Argument map:** 335 typed objections, 203 dated versions, 217 claims, 31 load-bearing.
- **Surviving their objections:** 129 as argued; 195 under a strict reading of the audit's verdicts; 144 under a lenient one.
- **Checks reviewed:** 29.
