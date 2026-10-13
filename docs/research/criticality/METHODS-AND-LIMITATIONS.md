# Methods and limitations

*State at 2026-10-12, commit `408ba53`. This page says how the audit was done and what that method can and cannot support. It follows the text proposed in [`METHOD-AUDIT-2026-10-12.md`](METHOD-AUDIT-2026-10-12.md); each limitation carries the id of the finding it answers (MA-01 to MA-20). Counts come from `research/tools/method_audit_stats.py` and [`research/checks/PREREG-STATUS.md`](../../../research/checks/PREREG-STATUS.md) unless a source is named. Changes proposed in answer to these limits, none yet adopted, are in [`METHOD-AUDIT-proposals.md`](METHOD-AUDIT-proposals.md); decisions waiting on the owner are in [`DECISIONS.md`](../DECISIONS.md).*

## What this is

An examination of the mathematical arguments in Vox Day's Zenodo papers and blog posts on evolution, and of the published replies to them. It is not yet an audit of the book *Probability Zero*: the book has not been read (see "Sources not read"). The corpus has no freeze date; material Day has published up to 2026-10-12 has been added as it appeared (MA-09, MA-11).

## Who did it

- **One AI model family and one person.** An AI system (Anthropic's Claude models) directs subagents of the same model family. They harvested the sources, extracted the claims, wrote and ran the checks, reviewed them, resolved the reviews, wrote the rules and counted the results. One human owner directs the work and makes the rule decisions. His decisions were given in chat and are reconstructed, not quoted, in `DECISIONS.md` (MA-01, MA-03, MA-10).
- **Reviews are same-model.** Every correctness review, every "steelman for Day", every "steelman for the critics" and every re-review is an instance of the same model family with a different brief. Reviews #1 to #13 were done by a smaller model of that family on the larger model's work. Three reviews of this kind are three prompts to one reviewer: they share training data, priors and characteristic mistakes, so their agreement is weaker evidence than three independent reviews would be (MA-01).
- **Reviews are not blind.** Reviewers read the finished write-up with its proposed verdicts, and the project instructions. The one review designed to be blind reported that it was not (`REVIEW-R4-X1-rule-audit.md` §0) (MA-01).
- **Reviews are author-adjudicated.** The author of a check writes the "Review resolution" and may decline a finding. No reviewer signs off. The method audit counted 91 review files and one BLOCKER in the 65 logged reviews, an import bug. No review has blocked a check on substance. Without a measured catch rate, that record does not show that the checks are right (MA-01).
- **No human specialist.** No population geneticist has checked the simulations or the derivations (MA-01).
- **The same model family is in the audited material.** Day's papers credit an AI co-author from this family ("Claude Athos"), and at least one critic source is AI-assisted. The model's training corpus is overwhelmingly mainstream on evolution, and the project's own notes record that its first-pass summaries leaned that way (`PLAN.md` l.273) (MA-01).
- **This page and the method audit share the limit.** Both were written by the same model family inside the project.

## Stance

Standard population genetics is treated as the default model. The audit asks whether Day's arguments defeat it and whether his critics' replies are themselves correct. It does not test standard theory against a rival of equal standing. That places the burden of proof on the challenger; it is a stance and not a neutral starting point (MA-05).

The claim tree is rooted at Day's claim, with critics' statements entered as attacks on it. "Load-bearing" is defined relative to that root. Equal scrutiny therefore does not mean equal depth: 24 Day nodes are load-bearing against 5 critic nodes, and load-bearing status is what buys three reviews. No mirror tree rooted at the critics' positive thesis has been built (MA-13).

## Verdicts and what they rest on

Each claim gets three verdicts: whether it follows from its author's own premises (internal), whether its citations say what is claimed (fidelity), and whether its premises fit the world (external).

**External verdicts rest on four different bases.** The project plan says simulations settle the first two columns and "only data settles" the third. In practice 52 claim files carry a decided `supported` or `contradicted` external verdict, and a coded reading of each verdict comment (one coder, primary basis; table in `METHOD-AUDIT-proposals.md` §b) gives:

| Basis of the external verdict | Files | Day | Critic | Literature |
|---|---|---|---|---|
| Data the audit processed itself (alignments, ancient-DNA genotypes) | 16 | 11 | 2 | 3 |
| Published results or texts, not reprocessed | 10 | 3 | 3 | 4 |
| Forward or exact-chain simulation | 10 | 2 | 6 | 2 |
| Standard theory (an identity or analytical result) | 16 | 10 | 6 | 0 |

Half of them (26 of 52) rest on simulation or standard theory with no observation: 12 of the 17 decided critic verdicts and 12 of the 26 decided Day verdicts. Of the 16 `contradicted` verdicts on Day claims, 7 rest on data, 1 on published results and 8 on the model. A Wright-Fisher simulation that returns k = μ confirms the program and shows what follows from Wright-Fisher premises. It is strong evidence on the internal question and no evidence that real hominid populations satisfy those premises. Read those 26 as "consistent (or inconsistent) with the standard model", not as statements about real genomes (MA-05).

**Some verdicts are conditional on a run not yet made.** DN1 to DN3 are `contradicted` on hg38/panTro5 with knownCanonical genes; Day's stated pipeline is T2T with GENCODE v46, and the like-for-like rerun (L1b) is registered and not run. Their verdict comments now say so (MA-12). Several simulation results hold only in the regimes tested, and some deciding parameters (hardness of selection, the human beneficial DFE) have no published source (MA-16).

## What the tallies can and cannot mean

- **`holds` includes claims nobody checked.** 131 internal verdicts read `holds`. 58 of them sit on claim files whose status is still `extracted`. By what those 58 files themselves record: 22 cite a check write-up, 12 cite only the one combined review of the "mapping" claims, 18 record only an inline calculation or a reading of the text that no second agent reviewed, and 6 record nothing. The vocabulary has no value for "not examined, no defect noticed", so the default is `holds`. `holds` also covers arithmetic that is correct on a premise the author later withdrew. "131 hold" is not 131 validations (MA-07).
- **`contested` is two-thirds of the external column.** 114 of 172 decided external verdicts. The word covers at least five situations: disputed in the literature, true only in the tested regime, conditional on an unsourced parameter, leaning one way but short of decisive, and not examined. In a seeded sample of 20, 6 had no recorded basis at all. The share says little about how open the questions are, and it must not be read as "most of Day's case is still in play" or as "the field is evenly split" (MA-08).
- **Day-versus-critic rates are not comparable.** The claim files give 19 error verdicts among 85 decided internal verdicts for Day and 1 among 51 for critics. Four things widen that gap regardless of anyone's competence: Day wrote far more; sharp numerical claims are exposed to the materiality rule while vague ones "hold" by construction; Day's nodes were checked or reviewed at 57% against 39% for critics; and critics' defects tend to be routed to the external column or the slip ledger. The project's own re-score found the gap "not robust". Claim nodes are also not independent units (they are nested in authors, documents and derivation chains, at a granularity the auditor chose), so the Fisher p-values printed in `HANDOFF.md` do not mean what a p-value usually means. This project does not claim an error rate for either side. The individual error verdicts stand or fall one by one on their own evidence (MA-06).
- **Reading-dependent verdicts enter the tallies as one value.** Where a verdict depends on how a quote is read, every reading is recorded in the claim file, and the single value in the verdict field is chosen by a selection rule. That rule was redefined on 2026-10-11 (see "Rules"). The readings table is the finding; the single value is a convention (MA-03).
- **Presentation.** The README scorecard pairs twelve points for Day with twelve for his critics. The rows are not of equal weight, and equal row counts should not be read as an even contest (MA-17).
- **Category leaks.** Nodes raised by the audit itself are coded `side: literature`, and "upheld" on an objection is the audit's own judgement, often about an objection the audit made (MA-15).
- **Small bookkeeping disagreements.** The method audit's parse of the claim files differed from the `HANDOFF.md` totals by one in five cells. One internal verdict (`A4`) carries a value outside the vocabulary ("holds for hazard-scale s") and is counted as `holds` (MA-20).

## Pre-registration: what it did and did not guarantee

The project rule is that each check script is committed with its predictions before the main run. A commitment is worth what separates it from the result. Three kinds must be kept apart (MA-04):

- **Blind:** the prediction was fixed, and pushed to the public remote, before any result existed.
- **Criterion-only:** the numbers were already known; only the scoring criterion was fixed in advance. The prediction scores are not tests.
- **Reproduction:** a known result is re-derived; no prediction is at stake.

`PREREG-STATUS.md` classifies every registered check from the commit history. Of 61 rows:

| Label | Rows | Meaning |
|---|---|---|
| blind | 10 | Registration pushed before the first commit containing a result; no disclosed foreknowledge. These include the long runs: H3, D15, H8, A2e, FM, the HF main sweep. |
| criterion-only | 6 | The script or write-up itself says the numbers were known (B9, RHclose, RHclose-critics, GAP05, L7, the Uricchio addendum). |
| reproduction | 3 | P1, XT, B3g. |
| single-commit | 18 | Script and results entered git in one commit (rounds 1 and 2, E, G1). Order not verifiable from history. |
| unknown | 20 | Separate commits, registration first, no push recorded in between, no disclosure either way. Fourteen of these have a gap under ten minutes; five are load-bearing (B3 family 36 s, B2/B 61 s, A2e-alpha 94 s, L1 333 s, the fast part of HF 632 s). |
| registered, not run | 4 | L1b, L5, L1c, FMnull. |

What this shows and does not show:

1. For the 10 blind rows the commit history supports "the prediction preceded the result". Missed predictions in those runs were reported.
2. For the 38 single-commit and unknown rows the history cannot show the order. That is 62% of the rows, including the core checks of branches B, F and H from the first two rounds.
3. **Commit order alone does not show that results preceded registration either.** A short gap is what an agent produces when it writes the docstring, runs a sub-minute script, writes up and commits in two steps. The stronger charge, that results were written before the predictions, is not established for any check.
4. Push times come from the owner's local reflog. No third-party timestamp exists for any registration.
5. Registered outcome bands do not always cover every outcome. A pre-run review of L1c found unregistered outcome regions that "would be interpreted after the data are seen".
6. Post hoc analyses are labelled as such in their own commits, including "exploratory, NOT pre-registered". That discipline has been consistent.

A reader should count 10 checks as pre-registered tests, not 57.

## Sources not read

- ***Probability Zero*, the book, has not been bought or read.** 20 claim files rest on it at second hand (Day 7, critics 8, allies 4, literature 1). Appendix A's "fixation must be sequential" is known only through Day's later quotation; two Day claims exist only through slides read aloud in a critic's video (MA-09).
- **Paywalled and paid material:** McCarthy's paid posts, Rosenhouse chapter 6, and the paywalled papers listed in `sources/refresh-2026-10-11b-lit.md`. The project rule forbids paywall bypass (MA-09).
- **Platforms that could not be read:** X, Gab, Telegram and SocialGalactic. One critic video is used through automatic captions (`sources/HOWTO-refresh.md`) (MA-09).
- **Selection and extraction.** Quotes are machine-checked against hashed raw text, which shows the words exist; it does not show the passage is representative. The second harvest pass and the first 193 claims were committed within an hour and a half on 2026-10-07, and no sampling audit of extraction accuracy has been run. `parameters.yaml` has 30 entries `verified: false` against 25 `true` (MA-09).
- Full texts are not in the repository (copyright). There is no one-command way for an outsider to refetch the sources and verify the quotes (MA-19).

## No right of reply so far

None of the authors on either side has been contacted. Verdicts on named living people are published in a public repository as they are made, without notice and without a reply. Project rule 6 forbids contact without the owner's approval; lifting it for this purpose is an open decision (`DECISIONS.md`, O-2). No outside reader from either camp has seen the rules or the load-bearing list (MA-10).

## Rules were added and changed mid-audit

- Revision 1 of the verdict rule was written after the first verdicts were known; the rule file says so. The 25% materiality line sits in a gap between the observed slips. It is a convention, checked for sensitivity (MA-14).
- Rule RH (rhetoric is tagged and not fact-checked) was added on 2026-10-09, after the X1 reviews. Rules RD (reading-dependent verdicts) and RH6 (the "remotely close" test) were added on 2026-10-11, the day they were applied to five checks.
- On 2026-10-11 at 21:24, four minutes after those checks were integrated, "most charitable reading" was redefined (commit `3f881b0`). The redefinition moved the internal verdict of node B, which is load-bearing, from `holds` to `non-sequitur`, with no review file. The same evening A2e, also load-bearing, moved from `contested` to `contradicted` (scoped) on a post hoc addendum with one combined review. Both moves are adverse to Day, and both happened outside the three-review tier that the project's own rule requires for such nodes. The same evening B9 moved in Day's favour, and every alternative reading is preserved in the claim files (MA-03).
- Under RH6 as written, a statement that is far from true can be tagged rhetoric and go unscored, while one that is nearly true is scored. The rule has protected statements on both sides (Day's "nearly empty" on one reading; a critic's "I debunked"). A revision is proposed and not adopted (MA-02).
- The rhetoric/dialectic distinction is Day's own framework, adopted by owner directive. The ledger also drafts counter-rhetoric, which is persuasion and not audit (MA-02).
- Review depth is set by a token budget, and the tier of a check is chosen by the agent that writes it. One check's tier was lowered after registration (L5) (MA-18).
- The verdict rule is not frozen. A freeze and a cooling-off rule are open decisions (`DECISIONS.md`, O-6).

## No aggregation rule and no stopping rule yet

No rule yet says how node verdicts combine into a statement about Day's root claim; `HANDOFF.md` lists that as "not yet decided". With 33 load-bearing nodes, three verdict columns and a majority of `contested`, many top-level sentences could be written after the fact. The exit criteria of the research phase are coverage criteria, the corpus has no freeze date, and since 2026-10-10 the work queue has followed Day's new posts. A draft aggregation rule and stopping rule are in the proposals file; neither is registered. Until one is, **this audit states no conclusion about the root claim** (MA-11).

## Known error

The audit has corrected errors of its own (a 41x error in one tail calculation; three findings against Day withdrawn). It has no estimate of how many remain. A seeded-error test of the review process and a blind re-derivation of ten load-bearing nodes are specified in the proposals file and have not been run (MA-01, MA-19).

## Interests

No conflict-of-interest statement, priors statement or licence exists yet. They are the owner's to write (`DECISIONS.md`, O-9). The project icon combines a double helix with a Christian cross; that was the owner's choice (MA-19).

## What the method does support

Stated so that the limits above are not read as "nothing here counts":

- Quotes are verbatim and machine-checked against hashed raw text; misses are printed.
- The checks are executable, seeded and re-runnable. The largest reproduced 696 jobs on two hosts with no mismatch, and core results were replicated in a second simulation tool. The replication was not clean: the second tool's substitution counts came out 0.7% to 36% low in step with the mutation rate per gamete, seven table items missed their registered tolerance (`RESULTS.md` names four results as not replicated), the cause has not been localised and the follow-up run has not been made (`R4-XT.md`; severe-testing pass, ST-06).
- Internal validity is scored on each author's own basis, separately from fidelity and realism, so the audit cannot simply assert the consensus.
- The long runs and one prediction note were registered and pushed before their results; missed predictions were reported.
- Limits were disclosed before this page existed (`HANDOFF.md`, "Things a reader should weigh").

Check by check, the write-ups are a usable provisional record. The tallies across claims are not a result.
