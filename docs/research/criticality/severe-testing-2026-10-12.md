# Severe-testing pass, 2026-10-12: could each check have found the flaw?

*Criticality layer, component iv. Applier: one Claude instance (Opus 5.5) in the project's own session, the same model family that wrote, ran, reviewed and integrated the checks graded here. Single rater. Not blind: the applier read the method audit, the Triveritas pass, the AMSTAR 2 and ROBIS pass and the pre-registration table before starting, and read the checks before writing the rubric (see "Order of work"). By the standing procedure this is a same-model pass and counts as nothing more (finding ST-13). No verdict, rule, claim file, check script or pre-registration label is changed by this file.*

**The question.** The earlier passes asked whether predictions were written down first (MA-04), who reviewed them (MA-01), and what an external verdict rests on (MA-05). This pass asks a different thing of each check: *if the inference the audit drew from it were wrong, would this check have shown that?* A prediction can be registered, pushed, timestamped and confirmed, and still have been certain to come out as it did. A recount with no registration at all can be a hard test.

**Order of work (stated so the reader can discount it).** 1. The framework texts were fetched and quoted (section 1). 2. The docstrings of all 57 run checks at their registration commits, the one-paragraph results and the failed-prediction rows of the write-ups were read. 3. The rubric (section 3) was written and committed. 4. The rubric was applied (sections 4 to 12, a later commit; the rubric commit is `63227e3`). Step 2 came before step 3. In the project's own labels the rubric is therefore `criterion-only`: fixed before scoring, written with the material in view. The grade of each check is computed from six coded answers by the rule in section 3.4, so a reader who disagrees with a code can recompute the grade.

## Executive summary

**Grades of the 57 run checks** (section 4; the rule is in 3.4):

| | SEVERE | PARTIAL | WEAK | BENT (no test) | Total |
|---|---|---|---|---|---|
| All run checks | 13 | 29 | 7 | 8 | 57 |
| Checks that target a load-bearing node | 7 | 22 | 4 | 4 | 37 |
| `blind` in `PREREG-STATUS.md` | 2 | 7 | 0 | 1 | 10 |
| Not `blind` | 11 | 22 | 7 | 7 | 47 |

**What is sound.**
1. The recounts and the data checks are hard tests. All 13 SEVERE checks are of two kinds: a derivation or tool set against an independent calculation (7), or a reading of public data or a published table (6). In two of the data checks (B3m, L6) the result went for Day against the audit's own registered expectation.
2. The audit's predictions do fail and the failures are reported: at least 98 failed or missed predictions of its own in 31 of the 57 checks (section 5.4).
3. Weak probes have been followed by stronger ones without prompting: C1 (wrong statistic) by C1b, C1c and C1d on the real genotypes; H2-hard (Haldane's regime untested) by H8, which confirmed Day's 1/300 there; L7's base-rate control undid the audit's own registered test.
4. Two of the four queued checks are designed the way severity asks: L5 computes the power of Day's own aDNA test, and L1c's amendment adds planted effects and negative controls.

**What is not.**
1. **Registration does not mark the tests.** Of the 10 `blind` checks 2 are SEVERE and 1 could not have failed; 11 of the 13 SEVERE checks are not `blind` (ST-01).
2. **No check that addresses the world by simulation alone is SEVERE** (0 of 15). Thirteen decided verdict fields rest only on WEAK or BENT probes; four of them are live and load-bearing (B internal, A2e external, F1a internal, B6 external) and all four lean to the critics' side (ST-02, ST-03).
3. **Eight checks registered an outcome that could not occur**, or predictions that were the registered arithmetic; three are reported as "All predictions met" (ST-05).
4. **The untested risk points one way**: of 44 checks below SEVERE the weakness favours the critics' side in 22 and Day's in 1; no check aimed at a critic's claim alone is SEVERE (ST-04).
5. **The one independent-engine probe disagreed and the disagreement was set aside**, unlocalised, with the follow-up not run (ST-06).
6. Queued checks: L1b's bands leave a Day-favourable region unclassified (ST-08); L5's own predictions contradict its band rule (ST-09); FMnull is a severe test of one outcome and a weak test of the other (ST-10).

**The same question put to the parties** (section 7). Day's MITTENS calculation and his mesa statistic could not have come out against him and are no test of the theory they are aimed at; his aDNA zero is no test against neutral theory, and its power against selection is what L5 will compute; his dN/dS result is weakly probed as presented, and the test he has promised (Q176) is a good one. Most of the critics' replies are derivations from the standard model, sound or not as arithmetic and no test of that model; the exception with data in it is keruru's temporal N_e, which the audit reproduced.

**Standing.** One rater, same model family, not blind; the rubric was written after the checks were read. Findings ST-01 to ST-13 (1 CRITICAL for the document's standing, 6 MAJOR, 6 MINOR); none closed. Nothing in the audit is changed by this file except two pointers and one caveat listed in section 11.

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

## 3. Rubric (fixed in commit `63227e3`, before any grade was written)

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

## 4. Every check, graded

57 run checks, in the order of `PREREG-STATUS.md`. None was sampled or skipped. For each, the docstring was read at its registration commit (`git show <reg>:research/checks/<script>`: the prediction block in full, the rest by section), with its paragraph in `RESULTS.md` and the scoring rows of its write-up. Whole write-ups were not read. **LB** = a registered target is one of the 33 load-bearing nodes ("tier 3" = the check also had the three-review tier). **About** = whose claim the primary inference concerns. **Type** and **C1-C6** are defined in section 3; the grade is computed from the six codes by the rule in 3.4. Verdict values in the inference column are as the write-ups and claim files give them; none is changed here.

| # | Check | LB | Label | About | Type | Primary inference | Alternative under which it is wrong | C1-C6 | Grade | Reason | Weakness favours | Audit predictions failed, and effect |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | B0 | no | single-commit | audit | D | The engine reproduces five textbook results within 3 SE (tool validation) | A coding error biases fixation probability or time | `YYYPYY` | **SEVERE** | Known-answer test against exact theory; a bias of the size that matters would fail it | – | 0. None (all pass). Order not verifiable |
| 2 | B0.4 | yes | single-commit | Day | D | Day's (2/s)ln(2N) overstates the conditional fixation time about 2x; the diffusion integral is right (F, F3a: latency) | Day's formula is the accurate one | `YYYPPY` | **SEVERE** | Simulation against two candidate formulas and the exact integral; replicated in fwdpy11 (XT) | – | 0. None |
| 3 | B1 | yes | single-commit | both | D | Day's empty-start formula is exact (B1 internal `holds`); from an equilibrium start the count is U·T | The formula or the stationarity result is mis-derived | `PYYPPP` | **PARTIAL** | Independent F_X estimate; later proved symbolically (P1). B6's external `supported` cites the forward simulation, which assumes the equilibrium start it is cited for | critics | 0. None. fwdpy11 did not reproduce these counts (XT: 21% low, cause not localised) |
| 4 | B3 (N vs Ne) | yes | single-commit | both | D | In exchangeable models P_fix = 1/M whatever N_e is; fixation time scales with N_e (Day right on time, wrong on probability) | P_fix depends on N_e | `YYYPYP` | **PARTIAL** | Day's 1/(2N_e) predicted values 1.5x to 7x away, so the run discriminated; replicated in XT and proved in P1. B3a external `contradicted` and B7 external `supported` are world verdicts resting on this identity (Day conceded the point on 2026-08-27, B3g) | critics (moot after the concession) | 0. None |
| 5 | B2a | yes | single-commit | Day | D | Day's exponent −π² is the correct leading-order asymptotic (B2 internal `holds`) | The exponent is wrong | `YYYPPY` | **SEVERE** | Exact Markov chain, no sampling; review #3 corrected the limit order; fwdpy11 agrees at G/N 1 to 4 | – | 0. None |
| 6 | F1 | yes | single-commit | critic | D | As logic, elapsed time divided by fixation latency is not a throughput bound (F1 internal `holds`) | Latency does bound throughput in every model | `PYYPPP` | **PARTIAL** | A counterexample model suffices for the logical point and the rate matches Kimura's; loci are independent by construction, so nothing is learned about feasibility, and review #3 flagged that the serial reading must be tied to a quote | critics | 0. None |
| 7 | B1b | yes | single-commit | Day | D | Size changes from an equilibrium start give a transient excess (contraction) or deficit (expansion); Day's mechanism is real for expansions only | A persistent deficit, or a deficit under contraction | `YPPPPP` | **PARTIAL** | The cumulative effect is a telescoping identity (U·4ΔN), so the registered verdict-changing outcome cannot occur inside neutral Wright-Fisher; the run checks the derivation. fwdpy11: contraction met, expansion 4.7% off | neither | 0. None of the audit's; the Day-side band failed for contraction |
| 8 | B1c | yes | single-commit | Day | W | With sourced N_e histories every lineage shows an excess: the empty-start premise is `contradicted` (B1c external) | The ancestral population was not at equilibrium, or the histories are wrong | `YNYPPN` | **BENT** | The excess was computed analytically before the run from inputs already in hand; the write-up calls it "not an independent empirical result". The evidence is the sourced N_e values, which the run does not test | critics (moot: Day withdrew the premise, B1d) | 0. None |
| 9 | B4a | yes | single-commit | both | D | E[d] = 2μT + θ_anc holds in forward simulation and in msprime (B4a internal `holds`; external fit `contested`) | The formula is mis-derived | `YYYPPP` | **PARTIAL** | Two independent tools agree to 0.3%. The Day-favourable outcome cannot occur in a model that contains ancestral diversity; the fit to 1.23% has a free N_e,anc. B6 external `supported` cites it | critics | 0. None |
| 10 | B3b / B3c | yes | single-commit | Day | D | Overlap with fluctuating N does move k (credit to Day), by too little for 0.743 at human-like values; 0.743 is a window artefact (B3c) | The effect is large at human parameters | `YPPPPP` | **PARTIAL** | Balloux & Lehmann eq. 3 reproduced in 9 scenarios, and the model did show departures both ways; human-scale size rests on a haploid, uniform-survival model with the per-generation normalisation open (0.81 to 1.11). fwdpy11 missed two rows | critics | 0. None of the audit's |
| 11 | C1 | no | single-commit | both | W | The two-period aDNA test does not discriminate; panel ascertainment (C1) `supported` | Ascertainment does not hide completions, or the statistic behaves otherwise | `YPYPPN` | **WEAK** | Scaling validated three ways, but the statistic simulated was not the one in Day's binned paper; the follow-up's own docstring calls the verdict "unsupported until that statistic is simulated" | critics (superseded by C1b to C1d) | 0. None recorded |
| 12 | C1b | no | single-commit | Day | W | Day's binned 21 is not reproducible from the published procedure in this model; cannot adjudicate | Neutral drift gives about 21 for his statistic | `YYPPPP` | **PARTIAL** | A falsifier (S21 below 100 with 21 inside the central 95%) was named and reachable; the model lacked real call depth and missed Day's own bin profile | neither | 1. P2 magnitude wrong (thousands, not about 500): led to C1c with real call depth |
| 13 | H | yes | single-commit | both | D | Haldane arithmetic holds and D = 30 is an input (H internal `holds`); H5 cost step `non-sequitur`; H1 scope | The arithmetic is wrong, or Nunney's M-dependence is absent | `YPPPPP` | **PARTIAL** | Recount is sound; the individual-based part is the audit's reconstruction of Nunney, with extras written after a smoke run; the non-sequitur is a reading | neither | 0. None found by keyword |
| 14 | H2-hard | yes | single-commit | Day | W | 10% is not a general bound; the cap is ln R / D; 1/300 "not supported in the tested range, not falsified" | The sustainable rate is about 1/300 whatever R is | `YPPNPP` | **WEAK** | The ceiling-fecundity rule makes persistence a function of ln R by construction; Haldane's own regime (R about 1.1) was not in the grid; the docstring was edited after the validation run (disclosed) | critics | 1. R = 10 prediction missed; n_crit conflict noted |
| 15 | C2 | yes | single-commit | Day | D | d is a unit conversion between hazard-scale and per-generation s: C2a `holds` for hazard-scale s, C2 `non-sequitur` as a fitted correction | d is a real slowing of selection | `YYPPYP` | **PARTIAL** | The decision rule could go either way and went both, by definition of s; Day's Table 1 is not reproduced with the stand-in life tables, and which s scale the cited aDNA papers used was not retrieved | critics | 0. None |
| 16 | F2 / A-sim | yes | single-commit | Day | W | Day's cap (about 230 concurrent sweeps) is not reproduced in the tested regime; external `contested` | A cap binds at human-like parameters | `YPYPPP` | **PARTIAL** | Clonal and short-map runs show the engine can register interference (R_int down to 0.09), and fwdpy11 agrees; selection is soft and active loci stop at 272, so the regime the claim is about is untested | critics | 0. None found by keyword |
| 17 | E | no | single-commit | Day | D | Day's founder-hazard tables reproduce only under a mean-field (HWE) formulation; the headline 2.33% holds approximately | His tables follow from the literal model | `YYYPPY` | **SEVERE** | An exact chain was run under two formulations and Day's own Table 4 picks between them (3.62 against 3.94) | – | 5. P2, P3 numeric, P5, P6, P8 failed in part: the stated reason ("drift") was withdrawn and the formulation identified |
| 18 | G1 | no | single-commit | both | D | The p^n arithmetic holds but prices a specific outcome; "forces sequential" is a `non-sequitur`; no cap near 230 under multiplicative fitness | The arithmetic is wrong, or the cap is real | `YPPPPP` | **PARTIAL** | Recounts are sound (and found 1.01^1474 is not 14.7); the cap result is set by the fitness model chosen, and both models are shown; specific-versus-any is a reading | critics | 2. Pair ratio at 1 M and P6 (multiplicative Δp) failed: post hoc rerun |
| 19 | GAP-04/07/02 | yes | unknown | both | D | Weissman-Barton's finite-map formula describes the F2 grid; at human scale Day's all-fixations rate exceeds R/2; verdict cells unchanged | The formula fails on the grid | `YPPNPP` | **WEAK** | The 20 grid cells were already published when the formula was scored against them, and the write-up says of one registered falsifier that it "could not fail" | neither | 1. P1 failed strictly (0.046 against 0.03) |
| 20 | H3 | yes | blind | both | W | At human-like excess R of 2 to 3 the required adaptive substitutions are payable; D = 2 ln 2N; every verdict cell unchanged, conditions added | The rate is capped near 1/300 at human R | `YPPYPP` | **PARTIAL** | Blind, with falsifiers for both sides; D and the fluctuation factor were measured, not assumed, and went partly Day's way; the scaling of the budget with ln R is built into the regulation rule | critics | 4. S3 (marginal), S5, S6, S7 at 2Ns = 100: K = 4,000 reruns showed one failure was an artefact |
| 21 | GAP-07b | yes | unknown | both | W | About 21 M divergence events per lineage on hg38/panTro6; 205 M and 410 M are base pairs, not events (A3x `supported`; A3 magnitude corroborated) | Events per lineage are of order 100 M | `YYYPPY` | **SEVERE** | Real alignment, outcome unknown beforehand, a Day-favouring threshold named, and later repeated on different assemblies and aligner (GAP-07t, +14.7%) | – | 9. Nine band misses (SNV 37.8 M above the band, toward Day's 40 M; gap bp; masking): filters added post hoc, conclusion unchanged |
| 22 | C1c | no | unknown | Day | W | No model cell reproduces Day's table; 21 is bracketed by Holocene N_e; cannot adjudicate on the full table | Neutral drift with replacement gives his table | `YYPPPP` | **PARTIAL** | A strict validity gate was named and it fired once an error rate was added; several of the audit's own statements were withdrawn. Still a model of the data, not the data | neither | 5. P2 part, P3, P4, P6, P7: four statements withdrawn |
| 23 | C1d | no | unknown | both | W | On the real AADR genotypes Day's count is not reproduced by any reading of the published method, and allele frequencies moved (C6, C7 external `contradicted`; keruru's N_e reproduced, C5b `supported`) | The published procedure gives his numbers; frequencies did not move | `YYYPPY` | **SEVERE** | Real data in two releases; an independent critic's number reproduced within 4%; a grid of readings tried; attribution to drift left open in the write-up | – | 6. P1 part, P3, P6, P12 part, P14, P16 part: the "damage" explanation was dropped |
| 24 | D1 | no | blind | both | W | Neutral neighbours exist (D1d existence part `supported`); alternatives per change sit between Day's and the critics' models and turn on the definition of equivalence | Functional sequences are isolated (Day), or richly connected (critics) | `YYPPPP` | **PARTIAL** | Both sides' outcomes were reachable and strict identity came out Day's way; RNA folding and one protein domain are proxies; bands were literature-informed ("not blind") | neither | 8. Eight sub-predictions failed; the pooled-count premise was withdrawn |
| 25 | X1 | yes | unknown | critic | D | Critic and ally arithmetic reproduces from their own inputs with listed exceptions (McCarthy 35 M, Hancock 76.8 per generation); one rule for both sides | More critic numbers fail | `PYPNPP` | **PARTIAL** | Row-by-row recounts can fail and did, including the repo's own figure (41x); most rows were predicted from arithmetic already in claim files, and the materiality rule that sorts error from slip was fixed after the slips were known | neither (direction not established) | 2. Band and row misses reported; the audit's own 1.2e-46 corrected to 5.1e-45 |
| 26 | GAP-07c | yes | blind | both | W | 15.6% of human-derived divergent sites are still polymorphic; about 17.9 M fixed events per lineage | The polymorphic share is 8% or less (favours Day) or the count is otherwise far off | `YYYYPY` | **SEVERE** | Blind, real 1000 Genomes data, thresholds for each side named, site list reproduced exactly, cross-checked on a second call set. Chimp side assumed and said so | – | 1. Q5 missed; one mis-registered point (no effect) |
| 27 | P1 | yes | reproduction | both | D | Seventeen identity groups hold as mathematics; 30 of 33 Day arithmetic rows reproduce (no verdict changed) | An identity or a row is wrong | `PYYPYP` | **PARTIAL** | A symbolic proof or exact rational chain would not pass a false identity. The write-up calls part of it "a machine re-confirmation, not new evidence"; several target nodes carry world verdicts that rest on these identities | critics (moot where Day conceded) | 0. None |
| 28 | B5b | no | unknown | critic | D | Mansfield's 2% is right as an identity and wrong as a magnitude; with a sourced neutral fraction the supply covers 20 M over 450,000 generations and 0.66x of 17.5 M over 252,000 (no verdict change) | The supply arithmetic is wrong | `PN––PY` | **BENT** | The registered predictions are the same arithmetic done by hand, so "all predictions met" could not be otherwise; what could change the conclusion is the sourced fraction, which the run does not test | neither | 0. None (could not fail) |
| 29 | F1b | yes | unknown | critic | W | In-transit count measured equals rate times latency; F1b external `supported` (independent loci) | Overlap is limited | `YNPPPP` | **BENT** | Review #16: Little's law on the same sample is an identity; independence is assumed, so the verdict-changing outcome was unreachable | critics | 0. None (could not fail) |
| 30 | C1e | no | blind | both | W | Under three of four published Holocene N_e trajectories 21 is a 34x to 161x deficit; only one trajectory comes near (no verdict change) | All trajectories give about 21, or none does | `YYPYPP` | **PARTIAL** | Blind, verdict-changing results named both ways and one of them nearly reached; shares C1c's model, with no error term; first run had a generation-time mismatch found in review | neither | 3. P5 sensitivity clauses and P7 missed; post hoc rerun met all |
| 31 | G2c / B6c | no | blind | critic | W | Unlinked neutral diversity stays near θ under parallel sweeps; G2c and B6c external `supported` (as a conditional) | Parallel sweeps at these rates erase diversity | `YNPYPP` | **BENT** | The registered derivation (P3, P4) already showed the falsifier needs about a million concurrent sweeps; linkage, the mechanism that could reduce diversity, is excluded by design ("the most favourable case for the critics") | critics | 2. Concurrency missed twice (realised rate 1.55x intended, unexplained): verdict withdrawn, then restored after a longer run |
| 32 | E5 / E6 | yes | unknown | both | D | LTEE fixation counts reproduce from Day's tables under each rule; G_f moves 3x with the rule; strict gives 1,587 (no verdict change) | The table sums are wrong | `PYP–PY` | **PARTIAL** | A recount of the papers' own tables ("arithmetic, not a blind test"); the underlying calls are not held and the −906 formula was skipped | Day (E6 `holds` on his own tables) | 0. None |
| 33 | F1a | yes | unknown | Day | D | Dividing by the latency gives the right count only at the serial supply boundary (F1a `non-sequitur` unchanged) | Day's six or seven already contains parallelism | `PNYPPY` | **BENT** | Both sides' registered models predict the same counts, and the docstring says no outcome here could change the verdict. The `non-sequitur` rests on a reading of Day's text | critics | 0. None (could not fail) |
| 34 | B2b | yes | unknown | Day | D | Wright's N_e = (4N−2)/(V_k+2) is confirmed and X follows by algebra (B2b `holds`); "about ten thousand" needs V_k near 4,000 | The formula or the algebra is wrong | `YYPPPP` | **PARTIAL** | A known-answer simulation that the audit's own first script got wrong and review caught; the critic-side point rests on which V_k is realistic, not tested | neither | 0. None (an N_e/N slip in the script, fixed post hoc) |
| 35 | XT | yes | reproduction | audit | D | fwdpy11 reproduces the qualitative core (1/2N, time scales with N_e, B1c excess, beneficial fixation time) and does not reproduce four count-type results | The numpy results are a bug of one implementation | `YYYYYY` | **SEVERE** | An engine sharing no code, with z-within-3 criteria: a probe that could and did return discordant results. See ST-06 on what was done with them | – | 7. Seven table items missed their tolerance (k/U counts 0.7% to 36% low, tracking U); `RESULTS.md` names four results as not replicated. No follow-up run, no verdict change |
| 36 | D15 | no (tier 3) | blind | ally | D | Hössjer's "far exceeds 9 My" holds inside his stated premises (96 cells, p9 = 0) and flips outside them | His waiting times are wrong inside his own premises | `YYYYPY` | **SEVERE** | Blind sweep against an analytic chain; engine validation partly failed (27% to 30%), but the in-scope margin is orders of magnitude, so C3 is raised to Y on the result | – | 5. P2, P4, P6, P7 in part and P8 (validation): cells stay conservative |
| 37 | H8 / H5 | yes (tier 3) | blind | both | W | Haldane's 1/300 is confirmed at R = 1.111 (a Day-side point); the budget grows with ln R; soft selection removes the cap in-model; verdicts unchanged | 1/300 holds at every R (Day), or fails in Haldane's own regime (critics) | `YPYYPP` | **PARTIAL** | Blind, numeric criteria for both sides, each partly realised; scaling with ln R is the regulation rule, the soft-selection result is conditional on purely relative fitness, and "slower than 1/300" depends on K and horizon | neither | 4. P2, P4 ratio, and post hoc K1, K3; critics' PC2 partly missed: finite-size explanation dropped |
| 38 | A2e | yes (tier 3) | blind | Day | W | The LTEE-as-ceiling answer flips on supply scaling κ (3.9 to 13,050), which the check cannot set; external stays `contested` | F ≤ 1 at Day's own supply figures | `YPPYPP` | **PARTIAL** | Blind sensitivity map with both outcomes realised across κ; at high κ the model's answer is nearly fixed by linear supply; no direction inferred | neither | 6. 6 of 19 rows missed (ranking, ranges) |
| 39 | B3 family | yes (tier 3) | unknown | Day | R | 32.3 reconstructs only from base-pair totals; with measured events k/μ is 2 to 3.4 (B3d fidelity `misread`, external `contradicted` per site) | Day reached 32.3 by another route | `YPPPPP` | **PARTIAL** | The grid of inputs is the audit's and has no random-target control of the kind that overturned L7's registered test; the per-site part rests on measured event counts | critics | 1. P6 withdrawn on a wrong premise (Day did cite Bergeron): a finding against Day was dropped |
| 40 | B2 / B | yes (tier 3) | unknown | Day | D | Hard Limits' definition, demonstration, exponent arithmetic and algebra hold (B2 internal `holds`); the asymptotic law understates the exact F by a power-law prefactor | The demonstration or arithmetic does not reproduce | `YYYPPY` | **SEVERE** | Exact chain against Day's own simulated numbers (396.5 against 391; his six inside the expected range) | – | 2. P6 and the numeric part of P7 failed, one each way |
| 41 | B3g | yes | reproduction | Day | R | The 2026-08-27 concession removes the N/N_e family and not 0.743 or 32.3 (verdicts unchanged) | The concession reaches further, or less far | `YYY–PP` | **PARTIAL** | Eleven quotes machine-checked and the withdrawn ratios recomputed; which values the concession reaches is, in the write-up's words, "a classification from stated bases, not a derivation" | neither | 0. None (one docstring figure corrected) |
| 42 | F3a | yes | unknown | Day | R | Day's latency arithmetic is exact (internal `holds`); Zeng's 0.001 is a mean absolute s under negative selection (fidelity `misread`) | Zeng reports a beneficial mean somewhere | `YYPPPY` | **PARTIAL** | Every sentence with a numeric s in the fetched paper was listed; the text check itself failed once on a PDF artefact | neither | 1. P1 failed on extraction: post hoc fix, no prediction changed |
| 43 | B3m | no | unknown | Day | R | Day's "median 25 across 55 vertebrates" reproduces from Bergeron's table (fidelity `accurate`); what it means is `contested` | No matched basis gives about 25 over 55 species | `YYYPYY` | **SEVERE** | Published table, three-way scoring rule fixed first, and the result went against the audit's own expectation and against the critic steelman | – | 1. A4 missed (Day-favourable); the critic-side band missed: fidelity scored for Day |
| 44 | FM | yes (tier 3) | blind | Day | W | Against a shared-rate null the human mesas are not human-specific and hold 1.25% to 2.5% of differences (FM8b `contradicted`); overdispersion is real as description (FM3) | A human-specific excess survives the shared-rate null | `YYYYPP` | **PARTIAL** | Blind, real T2T alignment, numeric thresholds for each side, a mirror test that exposed a reference artefact. The statistic is the audit's: Day's is undefined in the post, and whether the two agree waits on FMnull's reproduction gate | critics | 2. Audit missed at 1 Mb and on P7; Day-side P3, P4, P5, P7 missed |
| 45 | GAP-06 | no | unknown | Day | D | Yoo 2025's μ and generation times move none of Day's numbers by 25% (no verdict change) | Some number moves by more | `PN––PY` | **BENT** | Arithmetic on fetched inputs with the results in the registered predictions to three figures | neither | 0. None (could not fail) |
| 46 | GAP-07t | yes | unknown | both | W | On the T2T alignment 24.1 M events per lineage (+14.7%); 205 M bp is 8.5x events | T2T moves the count by more than 25% toward 205 M | `YYYPYY` | **SEVERE** | Second assemblies and a second alignment method, bands for both sides, Day's two registered conditions met at the low end; SNV totals had been seen (disclosed) | – | 3. Three marginal misses |
| 47 | A2e-alpha | yes (tier 3) | unknown | Day | W | Bias-corrected published α values put human adaptive coding substitutions above the 191 threshold; external `contested`, leaning contradicted | The human count is below 191 | `YPPNPP` | **WEAK** | A relay of model-based published estimates the audit did not reprocess; their values were in the registration, so the side of the threshold was known; it was review, not the run, that reclassified the one Day-side value as a null | critics | 3. Q1 part, Q2 part, Q3 failed: Gayà-Vidal's 0.2% reclassified |
| 48 | HF-d | yes (tier 3) | unknown | both | W | Mutational decline over 252,000 generations exceeds ln 3 only at the upper deleterious rate | The decline is large at central values | `YPPPPP` | **PARTIAL** | Seven-point validation with one failure; the result is set by an unsourced rate (later sourced in GAP05) | neither | 2. PD3 and one validation point |
| 49 | HF main | yes (tier 3) | blind | both | W | Soft selection and truncation lift the limit far above Term 3; a 10% hard component leaves most of the soft advantage at R = 2 (Day's DA1 fails there; at 30% it holds only on a floor tie); synergy lowers the limit (critics' CB2 fails) | Soft selection does not raise the limit (Day), or any softness keeps it (critics) | `YYPYPP` | **PARTIAL** | Blind, both sides' numeric predictions, failures on both; validated against H8 at h = 1; a post hoc run is still in progress and one cell carries a pipeline caveat | neither | 2. PA1, PA5 in part; both sides' bands failed in places |
| 50 | L1 | no (tier 3) | unknown | Day | W | On hg38/panTro5 no gene set, estimator or filter gives 0.80; pooled dN/dS is 0.21 to 0.27 (DN1 to DN3 `contradicted`, conditional on L1b) | Day's 0.80 is a property of the data | `YYYPYP` | **PARTIAL** | Real alignments, the published 0.23 reproduced on the one-to-one set, 32 filter stacks; not Day's stated assembly or annotation | critics | 4. Three marginal misses and one post hoc miss; the frame-error attribution was withdrawn |
| 51 | L6 | no | unknown | Day | W | Day's "ten of twelve" reproduces exactly from Good 2017's trajectories (E10 internal `holds`); the fixed calls cannot decline by construction | His count does not reproduce | `YYYPYY` | **SEVERE** | Public data not opened before registration; 28 of 29 cells match. The write-up itself identifies the critic-side check (fixed calls never fall) as true by definition | – | 1. "At least 30% real losses" missed (4.6%): wording of E10 changed |
| 52 | L7 | no | criterion-only | Day | R | 410 M can be reached from Yoo's SI (404 M) but the route is unconfirmed; A3x1 "not-found" was too strong | There is a unique route to 410 M | `YPNNPY` | **WEAK** | The audit's own base-rate control showed that matches near 410 M are common, so the reconstruction is weak; the inference was withheld, which is the right response | neither | 1. The registered random-target test was withdrawn (its pool contained the readings) |
| 53 | B9 | no | criterion-only | Day | R | Q104 is `dialectic`; internal `holds` on reading A; external `contradicted` on premise 1 | The statement is far from true on every reading | `YN–NYP` | **BENT** | The docstring: "The numbers below are known in advance". The band was 10x at registration and became 3x after review. The tag was known before the criterion was written | both ways (internal for Day, external for critics) | 0. None (could not fail) |
| 54 | RHclose | yes | criterion-only | Day | R | C7 and the Hard Limits peroration tagged by reading; B internal moves to `non-sequitur` | Another reading or edge gives another tag | `YN–NYP` | **BENT** | Numbers "ALREADY KNOWN from R4-B2"; the edges are the author's, set with them in view; the verdict field then followed a selection rule redefined the same evening (MA-03) | critics | 0. One glyph mismatch only |
| 55 | A2e-alpha addendum | yes | criterion-only | Day | W | Uricchio 2019 in full: lower HPD 0.096 maps to about 800, 4.2x the threshold; A2e external `contradicted` (scoped to any effect size, per generation) | The interval reaches below the threshold | `YPPNPP` | **WEAK** | A relay of one model-based estimate; the trigger for the move was written by the scorer with the abstract's point value known ("POST HOC LABEL"); the strong-only interval does reach zero and is reported | critics | 0. None |
| 56 | RHclose-critics | no | criterion-only | critic | R | Hancock, Myers and Mansfield statements tagged by reading (no node verdict change) | Another count or reading gives another tag | `YP–NYY` | **WEAK** | "NOT BLIND", with one edge sitting exactly on the prior count; even so a recount surprised (4 classes, not 3) and flipped a tag on one reading | neither | 3. Three predictions missed; one tag reading changed |
| 57 | GAP05 | no | criterion-only | both | W | A sourced DFE gives 15,000 to 21,000 slightly deleterious coding fixations per lineage and a log-fitness decline of 0.29 to 0.43 (0.8 to 1.1 on a post hoc base) | The count or the cost is far larger (Day) or negligible (critics) | `YPYPPP` | **PARTIAL** | The DFE predicts dN/dS of 0.21 to 0.25 with no fitted parameter, matching the audit's measured value, a check that could have failed; the decline depends on the base and flips post hoc; noncoding unsourced | neither | 0. None of the audit's; Day-side DB2, DB3 missed on the registered base |

**Three things the table shows before any counting.**

1. *Reachability (C2) is where grades are lost, not registration.* C1 is never N: every check named something that would count against it. C2 is N in 8 checks and P in 18. In 6 of the 8 the project's own text says so: the write-up or review calls the result an identity (F1b, B1c), the docstring says no outcome could change the verdict (F1a), the registration derives in advance that the falsifier cannot fire (G2c), or the docstring says the numbers were known (B9, RHclose).
2. *The programme does respond to weak probes.* C1 was found to have simulated the wrong statistic and was followed by C1b, C1c and then C1d on the real genotypes; H2-hard left Haldane's own regime untested and H8 went there and confirmed Day's number; L7's base-rate control undid the audit's own registered test and the inference was withheld.
3. *A severe probe returned a discordant result that is still open.* XT is the one independent engine. Its count-type rows came out 0.7% to 36% low, the deficit tracking the per-gamete mutation rate; the write-up attributes this to the harness or engine as a hypothesis "not tested here", the follow-up is "not run", and no verdict changed (ST-06).

## 5. Aggregates

### 5.1 Counts by grade

| By target | SEVERE | PARTIAL | WEAK | BENT | Total |
|---|---|---|---|---|---|
| load-bearing node targeted | 7 | 22 | 4 | 4 | 37 |
| no load-bearing node | 6 | 7 | 3 | 4 | 20 |
| **All** | **13** | **29** | **7** | **8** | **57** |

| By review tier | SEVERE | PARTIAL | WEAK | BENT | Total |
|---|---|---|---|---|---|
| three-review tier | 2 | 7 | 1 | 0 | 10 |
| one-review tier | 4 | 7 | 3 | 7 | 21 |
| before tiering | 7 | 15 | 3 | 1 | 26 |
| **All** | **13** | **29** | **7** | **8** | **57** |

| Verdict concerns | SEVERE | PARTIAL | WEAK | BENT | Total |
|---|---|---|---|---|---|
| Day | 6 | 13 | 4 | 5 | 28 |
| critic | 0 | 2 | 1 | 3 | 6 |
| ally | 1 | 0 | 0 | 0 | 1 |
| both | 4 | 14 | 2 | 0 | 20 |
| audit | 2 | 0 | 0 | 0 | 2 |
| **All** | **13** | **29** | **7** | **8** | **57** |

| Inference type | SEVERE | PARTIAL | WEAK | BENT | Total |
|---|---|---|---|---|---|
| D | 7 | 13 | 1 | 3 | 24 |
| W | 5 | 13 | 4 | 3 | 25 |
| R | 1 | 3 | 2 | 2 | 8 |
| **All** | **13** | **29** | **7** | **8** | **57** |

Of the 37 checks that target a load-bearing node: SEVERE 7 (B0.4, B2a, GAP-07b, GAP-07c, XT, B2/B, GAP-07t), PARTIAL 22, WEAK 4 (H2-hard, GAP-04/07/02, A2e-alpha and its addendum), BENT 4 (B1c, F1b, F1a, RHclose).

**What the 13 SEVERE checks have in common.** Seven are derivation or tool probes (B0, B0.4, B2a, E, XT, D15, B2/B): an exact chain, a second engine or a recount set against a simulation or against the author's own numbers. Six read public data or a published table (GAP-07b, C1d, GAP-07c, GAP-07t, L6, B3m). Fifteen checks address a world claim by simulation or model calculation alone (B1c, C1, C1b, H2-hard, F2, H3, C1c, F1b, C1e, G2c, H8, A2e, HF-d, HF main, GAP05); **none of the fifteen is SEVERE** (PARTIAL 10, WEAK 2, BENT 3). The other five world-type checks below SEVERE read data without settling the inference (FM, L1: scope; D1: proxies) or relay published estimates (A2e-alpha and its addendum). A simulation can test a derivation severely. It cannot test whether the world is like the simulation.

**By whose claim.** Six checks concern a critic's claim alone (F1, X1, B5b, F1b, G2c, RHclose-critics): SEVERE 0, PARTIAL 2, WEAK 1, BENT 3. Twenty-eight concern Day's alone: SEVERE 6, PARTIAL 13, WEAK 4, BENT 5. The critics' claims have fewer checks (AR-11) and the ones they have are the weakest probes in the table. The one severe result on a critic's own measurement is inside C1d (keruru's temporal N_e, reproduced within 4%).

### 5.2 Severity against the pre-registration label

| PREREG-STATUS label | SEVERE | PARTIAL | WEAK | BENT | Total |
|---|---|---|---|---|---|
| blind | 2 | 7 | 0 | 1 | 10 |
| criterion-only | 0 | 1 | 3 | 2 | 6 |
| reproduction | 1 | 2 | 0 | 0 | 3 |
| single-commit | 4 | 11 | 2 | 1 | 18 |
| unknown | 6 | 8 | 2 | 4 | 20 |
| **All** | **13** | **29** | **7** | **8** | **57** |

**Headline.** The two properties are close to unrelated here. Of the 10 `blind` checks, 2 are SEVERE (GAP-07c, D15), 7 PARTIAL and 1 BENT. Of the 13 SEVERE checks, 11 are not `blind`: 6 `unknown`, 4 `single-commit`, 1 `reproduction`.

*Pre-registered and not severe (the first interesting cell).* **G2c / B6c**: blind, pushed, and BENT, because its registered falsifier needed about a million concurrent sweeps by the registration's own arithmetic and the one mechanism that could have fired it (linkage) was excluded by design. It moved two external verdicts to `supported`. The seven blind PARTIAL checks (H3, D1, C1e, H8/H5, A2e, FM, HF main) are held back by scope (a model for a world claim, or an operationalisation of an undefined statistic), not by anything registration could cure.

*Severe and not verifiably pre-registered (the second).* **GAP-07b, C1d, GAP-07t, L6, B3m, B2/B** (`unknown`) and **B0, B0.4, B2a, E** (`single-commit`). The data checks are severe because the outcome was out of the audit's hands and a discordant result was reachable: in B3m and L6 it arrived, in Day's favour, against the audit's own registered expectation. The recounts are severe because an arithmetic error cannot hide from a recount whether or not anyone wrote a prediction first.

*Neither.* The six `criterion-only` rows are WEAK or BENT except GAP05, as their label already warns. Four `unknown` rows are BENT (B5b, F1b, F1a, GAP-06): each registered "predictions" that were the same arithmetic done in advance, or that both sides shared.

So the methods page's advice, "A reader should count 10 checks as pre-registered tests, not 57", is right about registration and is not a count of tests. By this pass the count of checks that could have embarrassed the inference drawn from them is 13, and only 2 of those are among the 10 (ST-01).

### 5.3 Where the weakness points

Of the 44 checks graded below SEVERE, the unprobed error, if it exists, would favour the critics' side in 22, Day's in 1 (E5/E6, where his counts hold on his own tables and the underlying calls are not held), both ways in 1 (B9), and neither in 20. Among the 30 such checks that target a load-bearing node: critics 18, neither 11, Day 1. This is the stance of the audit seen from another side (standard theory is the default model, MA-05): where the audit has only derived what the standard model implies, the verdict that results sits on the critics' side of the ledger. It is where the risk lies. It is not a finding that any of the 22 is wrong.

### 5.4 Did the audit's own predictions ever fail?

Yes, often. By the keyword count of 3.6, **at least 98 registered predictions or sub-predictions of the audit's own were scored failed, missed or partly missed, in 31 of the 57 checks**. The write-ups report them in the open, usually in a table. That is what a tested programme looks like, and it confirms what the method audit credited.

Three qualifications.

| Group | Checks | With a failure | Failures |
|---|---|---|---|
| blind | 10 | 10 | 37 |
| unknown | 20 | 14 | 41 |
| single-commit (rounds 1 and 2, E, G1) | 18 | 4 | 9 |
| criterion-only | 6 | 2 | 4 |
| reproduction | 3 | 1 | 7 |
| BENT, any label | 8 | 1 | 2 |

1. *Every blind check missed something; four of eighteen single-commit checks did.* The early rounds either made safer predictions or wrote them with the results in view. The history cannot say which (MA-04), and the difference in miss rate is the only evidence either way.
2. *The BENT checks could not miss and did not* (the two G2c misses are side quantities, not the falsifier). "All predictions met" appears in `RESULTS.md` for B5b, F1a and F1b, where it could not have been otherwise.
3. *Most misses are of magnitude; few are of direction.* Failures that changed a verdict, a tag or a published statement, as far as this pass found: B3 family P6 (a finding against Day withdrawn) and B3m (fidelity `accurate`, for Day); A2e-alpha Q3 (Gayà-Vidal's value reclassified, for the critics); L6 (E10 wording, for Day); L7 (the audit's own registered test withdrawn); RHclose-critics (one tag reading); G2c (a verdict withdrawn and restored); C1b and C1c (statements withdrawn, follow-up checks built); L1 (the frame-error attribution withdrawn). HF main and H8 produced failures of the critic-side bands (CA2, CB2, PC2) and a confirmation of Day's 1/300 in Haldane's regime. No failed prediction has yet changed a load-bearing verdict value in Day's favour: B3d and E10, which did move his way, are not load-bearing nodes, and on A3, which is, the audit's SNV band missed on Day's side (37.8 M against 27 to 35 M) and his magnitude was recorded as corroborated with the verdict value unchanged.

## 6. Verdicts that rest only on WEAK or BENT probes

Scope of this list: the decided verdict fields (`holds`, `non-sequitur`, `supported`, `contradicted`) of the target nodes of every check graded WEAK or BENT, or coded C6 below Y, read from the claim files on 2026-10-12. The other claim files were not opened, so the list is a lower bound; the method audit's coding (26 of 52 decided external verdicts rest on a simulation or an identity) says how much larger the population is. "Deciding step" = the check whose result put the present value in the field.

| Node (side; load-bearing?) | Verdict field | Probes behind it | Grade of the deciding step | Favours | What a severe probe would look like (design only) |
|---|---|---|---|---|---|
| **B** (Day; LB) | internal `non-sequitur` | B2/B (SEVERE, for the definition, numbers and Hard Limits' own text); RHclose (BENT) chose the reading the field takes, under a rule redefined that evening (MA-03) | BENT | critics | A reading probe, not a computation. Give the passage (Hard Limits l.265-300 and 430-470 with Q157, Q158) to readers who have not seen the audit's readings, ideally the non-Claude seat and one human (proposal f2, O-3, O-4). Each states what "the pipe" refers to and whether the lineage-level closure follows. Register beforehand: the field reads `non-sequitur` only if at least a stated share reach it unprompted. Add Day's own answer on which window he meant (right of reply, O-2). Positive control: include two passages whose reading is not in dispute, one valid and one not, to show the readers can tell |
| **A2e** (Day; LB) | external `contradicted` (scoped: any effect size, per generation) | A2e (PARTIAL, no direction inferred); A2e-alpha (WEAK); addendum (WEAK) | WEAK | critics | The audit's own estimate, queued as L3 (roadmap A12). Human-lineage adaptive substitutions from public polymorphism (1000 Genomes) and the codon alignments already built for L1/L1b, polarised as in GAP-07c, by two estimators (asymptotic MK and a DFE-based α). Before the real run: simulate coding sequence under human demography with planted α = 0 and α = 0.1 and show both estimators recover each (known-answer and negative control). Bands registered on the count: below 191 (Day), above 3 x 191 (critics), between (`contested`). Until it runs, the field rests on two relayed model estimates |
| **F1a** (Day; LB) | internal `non-sequitur` | F1a (BENT: both sides predict the same counts); the verdict is a reading of three quoted passages | BENT | critics | Machine-search the corpus for every use of the 19,800 figure and the "six" or "seven" fixations; classify each use as a spacing between fixations or as a latency, by two readers blind to the audit's verdict, on a rule registered first; score `non-sequitur` only if a spacing use carries a stated conclusion (R1). Ask Day (O-2) |
| **B6** (critic; LB) | external `supported` ("full pipe gives k = mu and d = 2muT + theta_anc (forward sim)") | B1, B4a (PARTIAL: derivations that assume the equilibrium start); B1c (BENT) | BENT for the world claim | critics | Test the ancestral polymorphism itself on data the audit holds. From the hg38, panTro6, gorGor6 alignments of GAP-07b, add an outgroup and count discordant site patterns (human and gorilla sharing a derived base against chimp; chimp and gorilla against human). An empty ancestral pipe predicts only the recurrent-mutation rate of such sites; an ancestral N_e near 1e5 predicts several percent of each. Register the two bands; run msprime with and without ancestral diversity through the same counting code as positive and negative controls. The literature value is already quoted (Scally 2012, in the FMnull registration) and would be the published number to reproduce |
| **B7** (critic; LB) and **B3a** (Day; LB) | external `supported`; external `contradicted` | B3 (N vs Ne), P1 (PARTIAL): an identity of exchangeable models | no test of the world | critics | Moot between the parties: Day withdrew 1/(2N_e) on 2026-08-27 (B3g). No probe is proposed. The basis should read "identity; conceded by Day", which proposal (b) `external_basis` would record |
| **B1c** (audit-raised; LB) | external `contradicted` | B1c (BENT) | BENT | critics | Moot: Day withdrew the empty-start premise (B1d). The live question is B6's, above |
| **H1** (Day; LB) | external `supported` ("neutral k = U (B0.5)") | B0 baseline: an identity | no test of the world | neither | Moot: it is Day's own scoping of his retraction and the critics agree |
| **F1b** (critic) | external `supported` (independent loci) | F1b (BENT) | BENT | critics | Measure overlap where it could fail: a human-length map, hard selection at the R of H8, supply at the rates Day states. HF and H3 hold most of the machinery. Positive control: shorten the map until interference appears |
| **G2c**, **B6c** (critic) | external `supported` (as a conditional) | G2c (BENT) | BENT | critics | Put the neutral sites on the same map as the sweeps. Positive control: a short map where hitchhiking must cut diversity, to show the engine registers it. Then compare the predicted depth and width of diversity troughs at Day's sweep rate with a published human diversity map: that is contact with data |
| **C1** (audit-raised) | external `supported` (ascertainment) | C1 (WEAK); C1c informs the panel density | WEAK | critics | Already registered: L5 (section 7.3) |
| **B9** (Day) | internal `holds` (reading A) | B9 (BENT) | BENT | Day | A reading probe as for B. The external field does not belong in this list: it rests on premise 1 by standard theory (an identity) and on the L1 dN/dS measurement |

**Count.** Thirteen verdict fields on thirteen nodes. Eight are on load-bearing nodes; four of those are moot because the party has conceded or agrees (B7, B3a, B1c, H1). The four that are live and load-bearing are **B internal, A2e external, F1a internal (all against Day) and B6 external (for a critic)**. All four lean the same way.

## 7. The same question put to the audited parties and to the queued checks

The rubric is the same. These are not checks the audit ran, so C4 is read as "was the criterion chosen after seeing the result, as far as the text shows". Quotes are from [`../sources/quotes-day.md`](../sources/quotes-day.md) by id. Grades are of each party's test *as presented in the texts held*; they say nothing about whether its conclusion is true.

### 7.1 Day's own tests

| Test, as he presents it | Inference he draws | Could it have come out against him? | Grade |
|---|---|---|---|
| **MITTENS bound.** "Restricting to the approximately 35 million SNVs and apportioning symmetrically: 17.5 million required fixations on the human lineage." (Q16, Z23003785 p.12, 2026-09-28); "At 1,322 gen/fix (non-mutator): 191 achievable. Shortfall: 91,600×." (Q17, p.13) | Selection cannot account for the divergence | No. Achievable = generations x d / G_f with G_f taken from the LTEE; required = the differences. Any two species that differ at millions of sites show a shortfall, and they would under the standard account too, in which most differences are neutral and fix in parallel. The calculation returns the same answer whether or not the theory it is aimed at is true. Day does report a cross-check of the rate input ("cross- validated at 893 generations per fixation by clone-pair analysis", Q13, p.1), which calibrates G_f and not the premise that it is a ceiling for all fixations | **BENT** as a test of the theory; sound as a deduction from its premises (A internal `holds`). What would make it a test: apply it to a divergence whose time and count both sides accept and show it does not forbid what was observed. This pass did not search the corpus for such an application |
| **aDNA "zero fixations".** "Across 1.14 million autosomal loci and 7,000 years of European prehistory, zero alleles moved from below 50% starting frequency to regional fixation, and zero moved from below 10% to fixation, in either run." (Q53, Z23046531 p.6, 2026-09-29); "The observed fixation count was zero." (Q55, blog 2026-01-14) | The clock has stopped; the required rate is not being met | A non-zero count was possible. Against neutral substitution the test is empty: the probability of a fixation from 50% in 280 generations is about 1e-17 (R4-RHclose; claim C7), and claim C is scored internal `non-sequitur` because "neutral also predicts ~0". Against a selection-driven rate its capability is its power, which Day does not report and which L5 is registered to compute. The thresholds differ between his two reports (below 10% to above 90% in the blog; below 50% to fixation in the paper, with 1 and 3 completions from the 50-90% range set aside; `quotes-day.md` discrepancy table, row 6) | **BENT** against neutral theory; **ungraded** against the selective rate until L5 reports |
| **dN/dS of 0.80.** "No combination of quality filters moves the number below 0.65." (Q175, blog, added 2026-10-11); "If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome." (Q176) | The published 0.23 is a gene-selection artefact | Filter robustness is not capability: an extraction or frame error is also filter-robust (one of L1's deliberately broken extractions, W2, read 0.76 and the write-up calls it "filter-robust"). No run of the pipeline on sequences of known dN/dS is reported, and the pipeline is unreleased. Q176 is different: it is a test Day has named in advance that can fail, and the audit credits it as "a valid, discriminating test". As quoted it names only the outcome that favours him | **WEAK** as presented; the Q176 test, once run on a released pipeline with the other outcomes named, would be **SEVERE** in design |
| **Mesas.** "The substitution density across the genome is massively overdispersed, more than 80 times more variable than a uniform-rate process predicts." (Q164, blog 2026-10-10) | A fourth mechanism beyond selection and drift | No. The null is a uniform rate. Mutation rate varies along the genome under every account in play, so the uniform null is rejected whether or not a fourth mechanism exists; FM found the index above 80 at 1 Mb for every ape lineage and none of the mesas under the uniform null. The discriminating statistic (is the excess specific to the human lineage?) is not reported in the post | **BENT** for the fourth-mechanism inference; **SEVERE** for the description (FM3 `supported` as description) |

Two things on the other side of the ledger. Day's counts that the audit could recount on public data reproduced (L6 "ten of twelve"; B3m "median 25 across 55"; the Hard Limits demonstration in B2/B). And on 2026-08-27 he withdrew the 1/(2N_e) leg after critics pressed it (B3g): one of his claims met a test from outside and he changed it.

### 7.2 The critics' rebuttal tests

| Test | Inference drawn | Could it have come out against the critic? | Grade |
|---|---|---|---|
| **keruru's temporal N_e** (C5b): allele-frequency variance between dated AADR bins | Drift is happening at an N_e near 1e4 | Yes. A census-scale N_e was a possible result of the same calculation. The audit reproduced his values within 4% on two data releases (C1d). His sampling correction is off by 7% to 19% (slip ledger), the estimate is a lower bound, and admixture is not separated from drift | **SEVERE** for "frequencies moved at this rate"; **PARTIAL** for "by drift alone" |
| **keruru's "zero is the expectation"** (C5): exact fixation probabilities over the window | Day's zero does not discriminate | It is a power calculation on Day's test: a derivation, checked by exact recursion in X1 | Sound as a derivation; it is itself a severity objection to Day's test, not a test of neutral theory |
| **McCarthy's supply count** (B5a): mutations per generation x generations x fixation probability, about 20 M | Neutral supply covers the divergence | In principle: pedigree rate x time could have been far from the counted differences. As run it had mixed generation times and one arithmetic slip (X1). With sourced inputs at Day's 252,000 generations the supply is 0.5x to 0.66x of the requirement (B5b) and the counted divergence is 2.2x to 2.6x the k = μ route (GAP-06); the gap is absorbed by the ancestral term and the divergence time, both adjustable (B4a's fit has a free N_e,anc) | **PARTIAL**: a consistency check that can fail, with free parameters taking up the slack |
| **Mansfield's pipelining argument** (F1, B5b) | Latency does not cap throughput | As a counterexample to a logical bound it is conclusive; it shows nothing about feasibility, and his 2% illustration is wrong in magnitude by 44x to 69x (B5b) | **PARTIAL** |
| **Hancock's and Myers's "serial" objection** (G2 family; RH-15, RH-20) | Day's mathematics assumes one fixation at a time | A reading of Appendix A, which the audit could not read at first hand (MA-09). Myers's "I debunked" is tagged rhetoric on one reading and is not a test; RHclose-critics found that the post does not engage MITTENS 3.0's parallel counting | **No test** where offered as a refutation of MITTENS 3.0 |
| **The published 0.23** (DN5), cited against Day's 0.80 | The textbook value is right | The critics relay it; the audit reproduced 0.21 on the one-to-one genes (L1). A relay tests nothing; the reproduction does | **SEVERE** for the number on hg38 once reproduced; what Day's 0.80 is waits on L1b and L1c |
| **Soft selection lifts Haldane's limit** (H2; Nunney, Wallace) | 1/300 is not a ceiling | In HF the critic-side bands failed in two places (partial softness at R = 1.111; synergy lowers the limit) and Day's band failed at a 10% hard component: the model test could go against either side and did | **PARTIAL** (model only) |

Most of what the critics offer is the standard model's own prediction, set beside Day's number. That is the right reply to a claim that the standard model cannot produce the observation, and it is a derivation: by this rubric it is sound or unsound as arithmetic and is no test of the standard model against the world. The exception with data in it is keruru's.

### 7.3 The four registered, not-yet-run checks, as amended

Read at `HEAD`. L1b and L5 have no amendment after registration; L1c has one pre-run amendment (`0e0e840`), FMnull two (`cc5e6dd`, `408ba53`). Grades are of the design and assume the validations pass.

| Check | Inference it can support | Severe? | What remains |
|---|---|---|---|
| **L1b** (T2T rerun of the dN/dS check) | Under band CRITIC: on Day's stated assemblies, with a correct frame, pooled dN/dS is in the textbook range (DN1 to DN3 stay `contradicted`, no longer conditional). Under DAY: the 0.80 is a property of the data | **SEVERE in design for the data statement**: real data, both outcomes reachable (L1's broken-extraction arm read 0.76, so the pipeline can read high), the published 0.23 as a number to reproduce, 32 filter stacks. **PARTIAL for "Day's 0.80 is an extraction artefact"** until his pipeline is released: the annotation (GENCODE v35 CAT) and alignment (Cactus) are the audit's choices | **The bands are not exhaustive** (ST-08): ALL ≥ 0.65 with SYN ≥ 0.65 and a single-difference share below 66% falls in no band, and it is a Day-favourable region; ALL < 0.40 with SYN ≥ 0.65 falls in none either. L1 on hg38 already makes CRITIC the expected band, so a CRITIC result is not a surprise; its weight comes from the assemblies being Day's |
| **L5** (aDNA power analysis) | Under CRITIC: Day's zero has no power against selection at s ≤ 0.01, which includes his own s = 0.001 (C external → `contradicted`, scoped). Under DAY: the zero does exclude the required rate | It is the severity calculation for Day's own test, and a model is the right instrument for it: if the test has no power inside the very model it is aimed at, the inference from zero fails whatever the world is like. Validations V1 to V3 are known-answer tests; the strong-sweep cells (s ≥ 0.05, predicted median ≥ 10 events) are the positive control that the pipeline can see a sweep. **SEVERE in design for "no power at s ≤ 0.01"; PARTIAL for the crossover s\*** (no admixture, error or background selection) | Two points (ST-09). The registered predictions are inconsistent with the band rule: P2 and P3 together satisfy the CRITIC condition as coded (script l.796-812), while P7 predicts MIDDLE. And the DAY band's clauses at s = 0.003 and 0.01 cannot be met by the registration's own arithmetic (P3: such a sweep needs about 1,000 generations), so "not DAY" will carry no information; the informative contrast is CRITIC against MIDDLE. The review tier was cut from three to one after registration (MA-18) |
| **L1c** (alignment method against dN/dS) | Under CRITIC with no mechanism: protein-guided alignment does not lower dN/dS at this divergence (DN6 → `contradicted`). Under DAY: it does, by the amount claimed | The amendment added what severity asks for: a `transfer` mode with planted dN/dS (0.23 to 1.0) and planted misalignment pushed through every arm, two pure-noise worlds as negative controls, and bands closed as a decision tree. **PARTIAL, near SEVERE** | The "realistic" protein-guided arms are the audit's own implementations (an in-script aligner; a Gblocks rule "Implemented from the documentation; not validated against the binary."). If the bias lives in a real tool's behaviour and not in the stand-in, the probe misses it. One arm run through a third-party aligner, or the stand-in validated against one on a sample, would close this. The synthetic rates are assumed design values. Not blind in the sense that matters least: L1 already points to CRITIC |
| **FMnull** (neutral-null calibration of "more than 80 times") | Under DAY (index above 3 x the neutral upper bound): the overdispersion exceeds known neutral heterogeneity. Under CRITIC: 80 is unremarkable at his window | **Asymmetric** (ST-10). A DAY class is hard to reach by accident and would be a severe result. A CRITIC class is cheap where the band is wide: at 100 kb the registered band runs from about 5.7 to about 133, most edges are marked UNSOURCED, and "inside" is then the expected outcome under many worlds. Amendments A4 (the critic needs the same 3x clearance), A5 (alignment term labelled), A7 (the real-data arm must reproduce Day's number before any class moves a verdict) and P8 (a planted block mechanism, with the admission that a small one is not detectable) reduce this and do not remove it. **SEVERE for a DAY result; WEAK to PARTIAL for a CRITIC result** under the registered brackets | P4 and P5 use results already known ("informed, not predictive"). The discriminating statistics are the empirical ones (lineage specificity S2, tree-incongruent sharing S4), which need no bracket: the write-up should lead with them |

## 8. Concordance with the earlier passes

| Earlier finding | This pass | Note |
|---|---|---|
| MA-01, TV-01 (one reviewer in three prompts; self-sealing) | **agrees**, with one addition | Same limit applies here (ST-13). Addition: the reviews are not without capability. In at least seven checks a review, not the run, produced the discordant result (C1's wrong statistic; B2a's limit order; F1b "an identity"; B2b's script slip; C1e's generation time; A2e-alpha's reclassified value; B3 family's withdrawn premise). The catch rate is still unmeasured (proposal f) |
| MA-03 (rules remade on the day they decided verdicts) | **agrees** | ST-03 reaches B and A2e from the probe side: the deciding steps are BENT and WEAK whatever the rule history |
| MA-04 (pre-registration unverifiable or empty for many checks) | **agrees in part; disagrees with the remedy's emphasis** | The labels are right as descriptions. Pushed timestamps would raise the `blind` count without making one more check able to fail. And "count 10 checks as pre-registered tests" undercounts the probes that could have embarrassed the audit (13) while including one that could not (ST-01) |
| MA-04 (bands not exhaustive, L1c) | **agrees; new instance** | L1c's were closed by amendment; L1b's are not (ST-08) |
| MA-05, TV-04 (external verdicts decided by the disputed theory) | **agrees** | ST-02 gives the same result from the checks upward: no simulation-only check is SEVERE for a world claim |
| MA-06, AR-11 (coverage differs by side) | **agrees in part** | The critic-only checks are the weakest in the table (0 SEVERE of 6, 3 BENT); the cause is that their claims are mostly derivations, not that they were treated more gently (ST-04) |
| MA-07 (`holds` is the default) | **agrees in part** | True of the unexamined files. But an internal `holds` that rests on a recount (B2/B, E, the Day rows of P1) is among the best-probed verdicts in the audit. Proposal (a) should keep those apart from the default ones |
| MA-12 (verdicts ahead of the like-for-like test) | **agrees** | L1 is PARTIAL on scope for exactly this reason |
| MA-14, TV-05 (thresholds are free parameters) | **agrees** | B9's band moved from 10x to 3x after review, with the numbers known |
| MA-16 (from the simulation to hominids) | **agrees** | C6 is below Y in 37 of 57 checks |
| MA-02, TV-08 (RH6) | **agrees in part** | The three RH checks are BENT, BENT and WEAK as probes; this pass says nothing about whether the RH rule is a good rule |
| TV-03 (the audit has made no prediction about itself that could fail) | **not covered; adjacent** | This pass counts failed predictions about the subject matter (98 at least). It makes one prediction about the audit that can fail: a second rater applying section 3 will move fewer than a third of the grades by more than one step (ST-13) |
| AR-01, AR-02 (plan not registered; no deviations log) | **not covered** | Severity is assessed check by check; it does not see the plan |
| AR-13, TV-11 (the pass is itself same-model, single rater) | **agrees** | ST-13 |
| **New in this pass** | | The cross-tabulation of severity against registration (ST-01); the direction count (ST-04); unreachable falsifiers as a class (ST-05); the open XT discordance (ST-06); the miss rate by registration group (ST-07); L5's inconsistent predictions (ST-09); FMnull's asymmetry by class (ST-10); reconstructions without a base rate (ST-11); severity objections with no place in the vocabulary (ST-12) |

**Tally over the 13 ST findings:** agrees with an MA, TV or AR finding 3 (ST-02, ST-03, ST-13); agrees in part 4 (ST-01, ST-04, ST-07, ST-08); new 6 (ST-05, ST-06, ST-09, ST-10, ST-11, ST-12). One partial disagreement (with MA-04's remedy and the methods page's "count 10", under ST-01), and it cuts both ways: it removes a blind check from the list of tests and adds eleven unregistered ones. No earlier finding is closed or contradicted.

What severity sees that the earlier lenses did not: whether a registered falsifier could fire; what was done with a discordant result; which way the untested risk points. What it cannot see: sources not read, selection of claims, fairness to named people, the rule history, anything about a claim that never had a check.

## 9. Findings

Severity labels as in the standing procedure. "Who it helps" says which side gains if the finding is acted on.

### ST-01. Registration status does not track severity
- **Severity:** MAJOR. **Category:** pre-registration, presentation.
- **Evidence.** Section 5.2: of 10 `blind` checks 2 are SEVERE and 1 is BENT; of 13 SEVERE checks 11 are not `blind`. `METHODS-AND-LIMITATIONS.md` l.80: "A reader should count 10 checks as pre-registered tests, not 57".
- **Why it matters.** The public pages use registration as the mark of a real test. A reader who follows that advice trusts G2c/B6c (blind, could not fail) over C1d, GAP-07b, L6 and B3m (not verifiably registered; the outcome was out of the audit's hands, and twice went against it).
- **Remedy.** Report a severity grade for the named inference beside the registration label (proposal g, section 10). Reword the methods-page sentence to say what the 10 are (registered before the result) and what they are not (the set of checks that could have failed). Agent; the rewording touches no verdict.
- **Who it helps.** Both. Day gains where blind model runs are currently read as tests against him; the critics gain where unregistered data checks that went their way are currently discounted.

### ST-02. No simulation-only check is severe for a claim about the world
- **Severity:** MAJOR. **Category:** epistemology.
- **Evidence.** Section 5.1: the 13 SEVERE checks are 7 derivation or tool probes and 6 that read public data or a published table; 0 of 15 simulation-only or model-only world checks is SEVERE. Section 6: thirteen verdict fields rest only on WEAK or BENT probes.
- **Why it matters.** It is MA-05 and TV-04 again, reached from the checks instead of from the verdict comments, with the list of fields attached.
- **Remedy.** Proposal (b) `external_basis` already covers the label. Add the probes of section 6. Agent, then owner for the outside readers.
- **Who it helps.** Day mostly (11 of the 13 fields favour the critics' side as they stand); the critics where a data probe would turn a model verdict into a measured one.

### ST-03. Four live load-bearing verdicts rest for their deciding step on WEAK or BENT probes, and all four lean one way
- **Severity:** MAJOR. **Category:** verdicts.
- **Evidence.** Section 6: B internal `non-sequitur` (RHclose, BENT: numbers "ALREADY KNOWN from R4-B2"); A2e external `contradicted`, scoped (addendum, WEAK: "POST HOC LABEL", trigger written by the scorer); F1a internal `non-sequitur` (F1a, BENT: both sides' registered models predict the same counts); B6 external `supported` (derivations that assume the equilibrium start). Three are against Day and one is for a critic.
- **Why it matters.** Two of the four are the moves MA-03 flagged for their process. Whatever is decided about the process, the probes behind them could not have come out otherwise.
- **Remedy.** The four designs in section 6. Until one has run, a decision for the owner (proposed O-17): leave the fields with a "weak probe" note, or return them to `pending` / `contested`. This pass changes neither.
- **Who it helps.** Day.

### ST-04. The untested risk points one way, and the critics' own claims get the weakest probes
- **Severity:** MAJOR. **Category:** fairness, coverage.
- **Evidence.** Section 5.3: of 44 checks below SEVERE the weakness favours the critics' side in 22, Day in 1, both in 1, neither in 20 (load-bearing: 18, 1, 0, 11). Section 5.1: critic-only checks SEVERE 0 of 6.
- **Why it matters.** "Both sides get equal scrutiny" is hard rule 1. Scrutiny of the same severity is a stronger requirement and it is not met: Day's numbers are recounted and his data claims re-measured (which is where his credits come from), while the critics' replies are mostly confirmed as derivations from the model they defend.
- **Remedy.** Order the queue by this list: data probes for B6 and G2c first (section 6). For each branch, one check designed so that the standard model's prediction can fail against data (GAP05's dN/dS cross-check is the pattern). Mirror tree, MA-13.
- **Who it helps.** Day in the short run; the critics if their model passes harder tests than it has been set.

### ST-05. Falsifiers that could not fire, and "all predictions met" where nothing could fail
- **Severity:** MAJOR. **Category:** check design, presentation.
- **Evidence.** Eight checks are BENT (C2 = N). G2c: registered falsifier "Hn ratio < 0.10", registered derivation that it needs about a million concurrent sweeps. F1a docstring: the non-sequitur verdict "is unchanged by any outcome here unless" Day's figure is shown to include a width factor. F1b: review #16, "Little's law on the same sample is an identity". GAP-04/07/02 write-up l.499: "The falsifier (E > 1,000) could not fail". B5b and GAP-06: predictions to three figures that are the registered arithmetic. `RESULTS.md` records "All predictions met" for B5b, F1a and F1b.
- **Why it matters.** A named falsifier reads as exposure to risk. Mayo & Hand's requirement is of "outcomes that will not be allowed to count in favor of H" (SV-MH3); an outcome that cannot occur does not qualify.
- **Remedy.** Proposal (h): each registered falsifier carries a reachability line (a parameter setting or planted effect under which it fires) and the registration includes that run as a positive control. Runs whose predictions are the same arithmetic are labelled derivations and get no prediction score. Agent.
- **Who it helps.** Both; it removes confirmations of both sides' claims that were never at risk.

### ST-06. The one independent-engine probe returned discordant results that were set aside unlocalised
- **Severity:** MAJOR. **Category:** tool validation.
- **Evidence.** `R4-XT.md`: every k/U-type count is low in fwdpy11, by 0.7% (U = 0.0125) to 21% (U = 0.5) and 36% (U = 1.0); the pattern is called "a hypothesis about a harness or engine effect at large U", "not tested here"; "Follow-up (not run)". `RESULTS.md`: "Not replicated and not localised", "No verdict change." Roadmap A15 lists the follow-up as "Specify or drop (owner call)". `METHODS-AND-LIMITATIONS.md` l.121 says "core results were replicated in a second simulation tool" with no exception.
- **Why it matters.** XT is graded SEVERE because it could disagree, and it did. An anomaly explained by an auxiliary hypothesis that nobody tested is the pattern the severity account is written against. The identities themselves are proved symbolically (P1), so k = μ as mathematics is not in doubt; what is open is whether either engine is right at high mutation input, and several checks run there.
- **Remedy.** Run the U-scaling test the write-up already specifies (B1 equilibrium and the cohort rows at four values of U, same seeds), registered with both outcomes named: deficit vanishing as U falls (harness) or not (something else). Small compute. Until then the methods-page sentence carries the exception (done in this commit). Agent. Not a "drop".
- **Who it helps.** Neither side in particular; the write-up shows the deficit does not take the form Day's formula predicts.

### ST-07. The failure record is real and uneven
- **Severity:** MINOR. **Category:** pre-registration.
- **Evidence.** Section 5.4: at least 98 failed or missed audit predictions in 31 checks. Blind: 10 of 10 checks with a miss. Single-commit: 4 of 18. BENT: 1 of 8, on side quantities. No failed prediction has changed a load-bearing verdict value in Day's favour (on A3 his magnitude was corroborated when the audit's own band missed on his side).
- **Why it matters.** The first number answers "a programme whose predictions never fail is not being tested": this one's do. The second is the only evidence the history offers on the early rounds, and it is what safer or later-written predictions would look like.
- **Remedy.** Print the miss count beside each check in `RESULTS.md`; generate it by script from the scoring tables so it is a census, not a keyword count. Agent.
- **Who it helps.** Both.

### ST-08. L1b's registered bands leave two outcome regions unclassified
- **Severity:** MINOR (raise to MAJOR if it runs unamended and lands there). **Category:** pre-registration.
- **Evidence.** `l1b_t2t_dnds.py` docstring, "Bands": DAY needs ALL ≥ 0.65, SYN ≥ 0.65 and share ≥ 66%; LOCATED needs SYN < 0.40; MIDDLE needs SYN or ALL in [0.40, 0.65); CRITIC needs both below 0.40. (ALL ≥ 0.65, SYN ≥ 0.65, share < 66%) and (ALL < 0.40, SYN ≥ 0.65) match none. No amendment commit exists for L1b.
- **Remedy.** Before launch, a pre-run note or amendment commit that assigns both regions (the first is Day's number reproduced with a different signature; it should not be left to be read after the data). The script need not change if the note fixes the reading. Agent; pointer added to `QUEUE.md`.
- **Who it helps.** Day (the larger hole is on his side).

### ST-09. L5's registered predictions contradict its band rule, and half of its DAY band cannot be reached
- **Severity:** MINOR. **Category:** pre-registration.
- **Evidence.** `l5_adna_power.py` l.796-812: `band = "DAY" if day else ("CRITIC" if (crit_iii and crit_ii) else "MIDDLE")`, with `crit_iii` = E ≤ 1 for s ≤ 0.01 in every cell and `crit_ii` = mainstream E ≤ 0.1. P3 predicts E < 1 for s ≤ 0.01 in every cell and P2 predicts mainstream E < 0.01: together CRITIC. P7 predicts MIDDLE. And P3's own reasoning (about 1,000 generations for such a sweep against a 280-generation window) makes the DAY condition at s = 0.003 and 0.01 unreachable.
- **Remedy.** Record before launch which of P2, P3 or P7 the audit expects to fail, and that the informative contrast is CRITIC against MIDDLE. Report the s ≥ 0.05 cells as the positive control. No script change. Agent; pointer added to `QUEUE.md`.
- **Who it helps.** Both: a CRITIC result moves C external against Day, and the reader should know the audit's own registration could not say whether it expected that.

### ST-10. FMnull is a severe test of one outcome and a weak test of the other
- **Severity:** MINOR. **Category:** check design.
- **Evidence.** Section 7.3. Registered band at 100 kb about 5.7 to about 133; "ALL brackets UNSOURCED unless noted".
- **Remedy.** In the write-up, lead with the empirical lineage-specificity and tree-incongruence statistics; give every CRITIC class with the width of its band and the share of that width that is sourced; treat a CRITIC class on a band wider than a stated ratio as "not discriminating". Agent, at write-up.
- **Who it helps.** Day.

### ST-11. Reconstructions of unstated methods lack a base-rate control, with one exception
- **Severity:** MINOR. **Category:** check design.
- **Evidence.** L7's random-target control showed that matches near 410 M are common and undid the audit's registered test. B3 family's "32.3 reconstructs only from base-pair totals" (8 of 480 grid cells) has no such control.
- **Remedy.** Apply L7's control to the B3 grid: how often does a random target in the plausible range get a hit within 2% from this grid, and how often only from base-pair counts. Registered, trivial compute. Agent.
- **Who it helps.** Day if hits are common; the critics if 32.3 stands out.

### ST-12. The audit's strongest objections to Day are severity objections, and the vocabulary has no place for them
- **Severity:** MINOR. **Category:** vocabulary.
- **Evidence.** Claim C internal `non-sequitur` because "neutral also predicts ~0"; FM's finding that the uniform rate is the wrong null; C1's "the test does not discriminate". Each says that Day's test would have come out the same either way. They are filed as `non-sequitur` or `contested`. The same holds in reverse for the critic-side fields of section 6. Section 7 is the first place either party's own tests are graded for capability.
- **Remedy.** Under proposal (g), a `test_severity` note on claims that are themselves tests (whose test, against what, could it have failed). No new verdict value.
- **Who it helps.** Both: it states the objection in a form the other side can answer by showing a control.

### ST-13. This pass is one rater of the same model family, not blind, and its rubric was written after the checks were read
- **Severity:** CRITICAL for the standing of the document. **Category:** independence.
- **Evidence.** The first paragraph and "Order of work". The 57 x 6 codes are one reader's judgement from docstrings and summaries; the code of the checks was not read (one exception: L5's band rule). Several grades sit one code away from the next grade (D15 is SEVERE on a margin argument; FM is PARTIAL on C6 alone; A2e-alpha is WEAK on C4 alone).
- **Remedy.** A second rater applies section 3 to the same 57 rows without seeing the codes; agreement is reported per question. Same-model unless O-3 or O-4 provides an outside seat. Registered prediction of this pass, which can fail: fewer than a third of the grades move by more than one step, and the two headline cells of 5.2 (blind and not severe; severe and not blind) both stay non-empty.
- **Who it helps.** Whoever the second rater's changes favour.

**Counts (13 findings).** CRITICAL for the document's standing 1 (ST-13); MAJOR 6 (ST-01 to ST-06); MINOR 6 (ST-07 to ST-12). None is closed.

## 10. A `severity` field (proposal g; not applied)

A block in the check's metadata, one entry per inference, and a one-line pointer in the claim file. Nothing below exists in any file yet.

```yaml
# in results/R4-<ID>.md front matter, or a generated research/checks/SEVERITY.md
severity:
  - inference: "G2c external supported (as a conditional)"
    type: W                 # D derivation/tool | W world | R reading/tag
    alternative: "parallel sweeps at these rates erase neutral diversity"
    capability: {named: Y, reachable: N, calibrated: P, independent: Y, exhaustive: P, scope: P}
    grade: BENT             # SEVERE | PARTIAL | WEAK | BENT, by the rule in severe-testing-2026-10-12.md 3.4
    favours: critics        # critics | day | both | neither
    reachability: "none registered"   # the setting or planted effect under which the falsifier fires
    rater: "same-model, single, 2026-10-12"

# in the claim file, beside each decided verdict
verdicts:
  external: supported       # unchanged
severity:
  external: {best_probe: BENT, probes: [chk:G2c], rater: "same-model, 2026-10-12"}
```

- **What moves.** No verdict and no count in the existing tallies. A new column: by this pass's grades, 13 verdict fields would show WEAK or BENT as their best probe (section 6), a lower bound.
- **Lint.** `grade` must equal the value the rule gives for `capability`; a decided external verdict with no `severity` entry is a warning, not an error.
- **Which side it helps.** Day where model verdicts against him would carry a visible grade; the critics where their data-backed points (A3x, C5b) would show SEVERE.
- **Risk.** A single same-model rater's codes would acquire the look of a measurement. The `rater` field is there for that reason, and the field should not be filled from this pass alone (ST-13).

Proposal (h), for the pre-registration template: every falsifier has a `reachability:` line and a positive-control run; a run whose predictions are the registered arithmetic is filed as a derivation.

## 11. Remediation, split three ways

**No-decision fixes (done with this pass; no rule, vocabulary or verdict touched).** The exception for the unreplicated rows added to the replication sentence of `METHODS-AND-LIMITATIONS.md` (ST-06). Pointers to ST-08 and ST-09 added under L1b and L5 in `QUEUE.md`, so that whoever launches them sees the two points first. Component row, findings table and concordance in the criticality `README.md`; rows in `ROADMAP.md`.

**Proposals (specified here, held back).** (g) the `severity` field; (h) the reachability line and the derivation label; the second-rater pass (ST-13); the miss census by script (ST-07). Checks to specify and pre-register: the XT U-scaling run (ST-06), the discordant-site probe for B6, the linked-site probe for G2c and B6c, the base-rate control for B3 family (ST-11); L3 with planted-α controls is already in the queue and is the probe for A2e (ST-03).

**Owner decisions (proposed; not entered in `DECISIONS.md` by this pass).**
- **O-16.** Keep severity as a standing lens of the criticality layer and adopt the `severity` field, or treat the pass as a one-off.
- **O-17.** For B internal, A2e external, F1a internal and B6 external: leave the present values with a "weak probe" note, or return them to `pending` / `contested` until a severe probe has run. Related to O-5.

## 12. What was not examined

- The code of the 57 scripts, beyond docstrings (and L5's band rule). A grade of "reachable" is the design's claim, not a verified property of the program.
- Whole write-ups, review files and claim files other than the twenty-two whose verdict fields were read for sections 6 and 7.
- Post hoc scripts and the twelve mapping claims, which `PREREG-STATUS.md` does not list.
- Claims that never had a check: 233 claim files against 57 checks. Severity has nothing to say about a verdict with no probe at all except that it has none.
- Mayo 2018, Mayo 1996, Popper 1959 and every Bayesian primary text (section 1 and 2 mark what is from memory).
- Day's corpus for a known-answer application of MITTENS or a control run of his dN/dS pipeline; section 7.1 says "not reported in the quotes held", not "does not exist".
