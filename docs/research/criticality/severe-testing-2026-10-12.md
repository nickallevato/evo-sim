# Severe-testing pass, 2026-10-12: could each check have found the flaw?

*Criticality layer, component iv. Applier: one Claude instance (Opus 5.5) in the project's own session, the same model family that wrote, ran, reviewed and integrated the checks graded here. Single rater. Not blind: the applier read the method audit, the Triveritas pass, the AMSTAR 2 and ROBIS pass and the pre-registration table before starting, and read the checks before writing the rubric (see "Order of work"). By the standing procedure this is a same-model pass and counts as nothing more (finding ST-13). No verdict, rule, claim file, check script or pre-registration label is changed by this file.*

**The question.** The earlier passes asked whether predictions were written down first (MA-04), who reviewed them (MA-01), and what an external verdict rests on (MA-05). This pass asks a different thing of each check: *if the inference the audit drew from it were wrong, would this check have shown that?* A prediction can be registered, pushed, timestamped and confirmed, and still have been certain to come out as it did. A recount with no registration at all can be a hard test.

**Order of work (stated so the reader can discount it).** 1. The framework texts were fetched and quoted (section 1). 2. The docstrings of all 57 run checks at their registration commits, the one-paragraph results and the failed-prediction rows of the write-ups were read. 3. The rubric (section 3) was written and committed. 4. The rubric was applied (sections 4 on, a later commit). Step 2 came before step 3. In the project's own labels the rubric is therefore `criterion-only`: fixed before scoring, written with the material in view. The grade of each check is computed from six coded answers by the rule in section 3.4, so a reader who disagrees with a code can recompute the grade.

## 1. The framework, from the fetched texts

Sources (all open or author-posted; hashes in [`../sources/bib-literature.md`](../sources/bib-literature.md), section "Criticality pass iv"; fetch log in [`../sources/harvest-log-literature.md`](../sources/harvest-log-literature.md); 27 quotes machine-checked, ids `SV-…`, in [`../sources/quotes-literature.md`](../sources/quotes-literature.md)): Mayo & Spanos 2006 and Mayo & Spanos 2011 (author-posted copies), Mayo & Cox 2006 (arXiv), Mayo & Hand 2022 (open access), and two posts on Mayo's own blog that give notes and an excerpt from Mayo 2018. **The book itself (Mayo 2018, *Statistical Inference as Severe Testing*) was not obtained**; "BENT" and the weak/strong wording are quoted from the author's posts of it, not from the book.

**The definition** (Mayo & Spanos 2006, p.329, SV-MS1):

> "A statistical hypothesis H passes a severe test T with data x0 if, (S-1) x0 agrees with H, and (S-2) with very high probability, test T would have produced a result that accords less well with H than x0 does, if H were false."

**Weak (negative) form** (Mayo & Spanos 2011, SV-ES1; Mayo's notes from the 2018 book, SV-B1a, SV-B1b):

> "Severity Principle (weak). Data x0 (produced by process G) do not provide good evidence for hypothesis H if x0 results from a test procedure with a very low probability or capacity of having uncovered the falsity of H, even if H is incorrect."

> "If data x agree with a claim C but the method used is practically guaranteed to find such agreement, and had little or no capability of finding flaws with C even if they exist, then we have bad evidence, no test (BENT)."

**Strong (positive) form** (SV-ES2; SV-B3):

> "Severity Principle (full). Data x0 (produced by process G) provides good evidence for hypothesis H (just) to the extent that test T severely passes H with x0"

> "Severity (strong): We have evidence for a claim C just to the extent it survives a stringent scrutiny. If C passes a test that was highly capable of finding flaws or discrepancies from C, and yet none or few are found, then the passing result, x, is evidence for C."

**Four features the rubric takes from the texts.**

| Feature | Quote | Use here |
|---|---|---|
| Severity is of a test, an outcome and a claim together | "The severity function has three arguments: a test, an outcome or result, and an inference or a claim." (SV-MS2); "It requires being very specific about which inference is thereby warranted" (SV-ES5) | One check can be severe for one inference and no test of another. Each check is graded for a named inference |
| It is assessed after the data | "the severity evaluation must be sensitive to the particular outcome x0; it must be a post-data assessment." (SV-MS3) | The size of the margin in the result counts, not only the design |
| The burden is on the claimant | "The onus is on the person claiming to have evidence for H to show that they are not guilty of at least so egregious a lack of severity." (SV-ES3) | A check with no shown capability is graded down, not given the benefit of the doubt |
| Capability is shown on known cases | "were George to have gained δ pounds or more (i.e., were H false), then this method would almost certainly have detected this." (SV-ES4, the scales that register a known added weight) | Baselines, known-answer tests, planted effects and negative controls are what "calibrated" means below |

Two more points of design: "for a given test of H it is essential to specify in advance at least some outcomes that will not be allowed to count in favor of H." (SV-MH3), and "a probative test will generally involve combining several subsidiary tests, deliberately designed to unearth different flaws." (SV-MH2).

**No numbers are computed.** In the papers severity is a probability, SEV(T, x0, H), worked out inside a statistical model. Almost none of the checks here is a statistical test with a sampling distribution, so this pass uses the informal sense that the same authors allow ("we will also suggest how the idea may be generalized to inferring the presence of 'an error' or flaw, very generally conceived.", SV-MS5). The four grades are ordinal judgements. They are not severity values.

## 2. How severity differs from three neighbours

Day, his critics and this audit each lean on a different standard, so the differences matter.

**Pre-registration.** Pre-registration fixes the criterion before the outcome is known. It guards against one way of losing severity: choosing the test after seeing the data ("impressive-looking results are easy to achieve if one can ignore unwelcome results, alter what is being tested post-data, or exploit a variety of sources of researcher flexibility", SV-MH4; the marksman who "paints a bull's-eye in spots where the bullet holes are clustered", SV-B6). It does not ask whether the fixed criterion could have failed. A registered prediction that both sides' models share, or that follows from the model's own assumptions, is registered and is no test. In the other direction, the texts do not make foreknowledge a defect in itself: what matters is "whether the probativeness is altered with respect to the particular error of interest" (SV-MS4). Recounting an author's sum is not blind and can still catch the error. *From memory, not fetched:* Mayo 2018 and Lakens 2019 both argue that the value of pre-registration is that it lets a reader judge severity; neither text was read for this pass.

**Popper's falsifiability.** Falsifiability is a property of a hypothesis: some observation would contradict it. Severity is a property of a test, a result and a claim: this procedure would probably have produced that contradiction. A falsifiable claim can be given a test that could not have failed. The fetched text says the account "goes beyond falsificationism, of both the Popperian and Fisherian varieties, most notably in its consideration of what positive inferences are licensed when data do not falsify but rather accord with a hypothesis or claim." (SV-ES6). *From memory:* Popper also used the word "severe" for tests and asked for risky predictions, without giving a measure of it. Popper 1959 was not fetched.

**Bayesian confirmation (and likelihood accounts).** These ask how probable, or how much more probable, a claim is given the data. Severity asks how well probed it is. "There's a difference between finding H poorly tested by data x, and finding x renders H improbable" (SV-B2); "It is not probabilism or performance we seek to quantify, but probativeness." (SV-B5). Mayo's own gloss in a comment reply: "With probabilism, one has evidence for a claim to the extent that it's probable in some sense, or gets a probability boost, or is comparatively more likely than some other claim." (SV-B7), and "To block BENT cases requires considering error probabilities of methods and these go beyond likelihoods." (SV-B8). *From memory, and only one side of a live dispute:* a Bayesian answers that a result certain under every hypothesis has a likelihood ratio of one and confirms nothing, so the two accounts often agree on which probes are worthless; they differ on stopping rules, selection effects and whether a prior belongs in the appraisal. This pass does not adjudicate that dispute. It applies one account as a lens, as the Triveritas pass applied Day's.

**Long-run reliability** is not the same thing either: "The reliability of the rule used to infer H is at most a necessary and not a sufficient condition to warrant inferring H." (SV-ES7). A review process that rarely errs on average does not show that this check could have caught this error.

**Who might prefer which.** Day's Triveritas asks for empirical anchoring and for predictions that could fail (Q203, Q212, in the Triveritas pass). That is close to Popper. The critics mostly argue that Day's results are what the standard model predicts anyway, which is a severity objection to Day's tests. The audit's own rule has been pre-registration. Section 6 applies the severity question to all three.

## 3. Rubric (fixed in this commit, before any grade is written)

**Unit.** One row of [`research/checks/PREREG-STATUS.md`](../../../research/checks/PREREG-STATUS.md): 57 run, 4 registered and not run.

### 3.1 The inference graded

For each check, the **primary inference** is the one its own write-up draws in its verdict line or its paragraph in `RESULTS.md`: a verdict value for a party, or, where no verdict moved, the stated finding. It is typed:

| Type | What is inferred | The alternative under which it is wrong | What a capable probe looks like |
|---|---|---|---|
| **D** derivation or tool | "X follows in model M", "the engine reproduces theory", "the author's number follows from the author's own inputs" (internal verdicts) | An error of algebra, code or arithmetic | An independent recomputation: exact chain against simulation, a second engine, a symbolic proof, a recount |
| **W** world | An external `supported` or `contradicted`, or a description of data | The world differs from the model, or the data say otherwise | Contact with data or with a published measurement the audit did not produce; a discordant outcome that was possible |
| **R** reading or tag | Fidelity, an RH tag, a `non-sequitur` that turns on how a text is read, a reconstruction of an unstated method | Another defensible reading, statistic or route exists | Readings enumerated before scoring; machine-checked text; a base-rate or negative control for "this is the only route" |

A check that verifies a derivation is graded as type D even when a claim file later uses it for a world verdict. That wider use is caught by question C6 and listed verdict by verdict in section 5.

### 3.2 Six capability questions

Each is answered **Y**, **P** (in part) or **N**; **–** means the question does not apply.

| | Question | N when |
|---|---|---|
| **C1** Named | Was an outcome that would count against the inference named in advance (a falsifier, the other side's band, a fail criterion)? | Only "predict: confirmed" is registered |
| **C2** Reachable | Under the alternative, could this design have produced that outcome? | The result follows from an identity or from the model's own assumptions; both sides' models predict the same number; the registered arithmetic already shows the falsifier cannot fire; the tag or number was known and the criterion left no reading that could change it |
| **C3** Calibrated | Is there evidence the instrument detects what it should: a baseline or known-answer test, a planted effect, a negative control, a second tool, host or data release, an independently published number reproduced? | No such step, or the step failed and was not resolved |
| **C4** Independent | Were the criterion and bands fixed before the scored numbers were known, and left alone afterwards? Uses the `PREREG-STATUS` label and the disclosures. P = order not verifiable, or informed. | The docstring says the numbers were known and a band edge, threshold or reading was chosen with them in view; or the criterion was edited after output |
| **C5** Exhaustive | Does every possible outcome fall in a registered class? | Outcome regions are left to be read after the data |
| **C6** Scope | Is the inference recorded (in the write-up and in the claim files of the check's target nodes) no wider than what was probed? P = a claim-file world verdict cites it with scoping words ("in the exchangeable class", "independent loci", "as a conditional"), or the regime or pipeline probed is not the one the claim is about. | A world verdict rests on it with no data and no scoping, or the statistic probed is not the one at issue |

C4 counts against a grade only where the criterion had freedom the outcome could exploit. A recount of a sum has none; it is coded –.

### 3.3 Grades

| Grade | Meaning |
|---|---|
| **SEVERE** | If the inference were wrong, this check would very probably have shown it. |
| **PARTIAL** | It could have found some of the ways the inference could be wrong, or it is severe for a narrower inference than the one recorded. |
| **WEAK** | A discordant result was possible in principle and unlikely under the alternative, or the inference is of a different kind from what was probed. |
| **BENT** | Bad evidence, no test: the result was fixed by construction. This is a statement about the probe. It does not say the inference is false, and a correct derivation can be BENT as a *test*. |

### 3.4 Decision rule (applied in this order)

1. **BENT** if C2 = N.
2. Otherwise **WEAK** if C6 = N, or if C2 = P and (C3 = N or C4 = N).
3. Otherwise **SEVERE** if C2 = Y and C3 = Y and C6 = Y, and none of C1, C4, C5 is N.
4. Otherwise **PARTIAL**.

The margin in the result may raise C3 from P to Y when the instrument's known error is far smaller than the distance between the result and the threshold (section 1, "assessed after the data"); each such case is marked in the table.

### 3.5 Direction

For every grade below SEVERE: **whom the weakness favours**. "Favours critics" means that if the unprobed error exists, the recorded verdict is kinder to the critics' side (or harder on Day) than a severe test would have left it; "favours Day" the reverse; "neither" where no verdict direction hangs on it. It is a statement of where the risk lies. It is not evidence that the error exists.

### 3.6 Failed predictions

For each check: whether any registered prediction of the audit's own was scored failed, missed or partly missed, and whether a failure changed a verdict, a tag or a published statement. Source: the scoring rows of the write-ups, found by keyword search (`fail`, `miss`, `falsified`, `wrong`, `refuted`, `not met`), and `RESULTS.md`. It is a lower bound. Sub-predictions are counted separately. Side-attributed predictions (the bands the audit wrote for Day or for the critics) are noted and not counted as the audit's own.

### 3.7 Load-bearing

A check is counted **load-bearing** here if one of its registered target claims is among the 33 nodes `hierarchy.yaml` marks `load_bearing: true` (A, A2e, A3, B, B1, B1c, B2, B2b, B3, B3a, B3g, B4a, B5, B6, B7, C2, C2a, E5, E6, F, F1, F1a, F2, F3a, FM10, H, H1, H2, H5, H8, ROOT, ROOT-FM, ROOT-M). This differs from the review-tier column of `PREREG-STATUS.md`, which says how many reviews a check received; both are reported.

### 3.8 What this rubric cannot see

It grades the probe, not the truth of the inference. It reads docstrings and result summaries, not the code, so a bug that makes a "reachable" outcome unreachable is invisible to it. It takes each check's own account of its validation at face value. It says nothing about fidelity to sources beyond the probes that tested it, nothing about fairness to named people, and nothing about which claims were never given a check at all (AR-11).

*Sections 4 to 10 (the per-check table, aggregates, verdicts resting on weak probes, the same question put to Day's and the critics' own tests and to the four queued checks, concordance, findings ST-01 on, remediation) follow in the next commit.*
