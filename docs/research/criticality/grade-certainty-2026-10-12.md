# Certainty-of-evidence pass, 2026-10-12: how sure can each external verdict be?

*Criticality layer, component vi. Applier: one Claude instance (Opus 5.5) in the project's own session, the same model family that extracted the claims, wrote and ran the checks, reviewed them and wrote the verdicts rated here. Single rater. Not blind: the applier read the criticality README (with the MA, TV, AR, ST and AS findings), the proposals file, the methods page, the verdict rule, and the tables of the severe-testing and argument-structure passes before writing the adaptation. Day's papers credit a co-author from the same model family, and the model's training corpus is overwhelmingly mainstream on evolution (methods page, "Who did it"). Every rating below is one same-family rater's judgement and not an outside review (finding GR-13).*

**The question.** The external verdict vocabulary is `supported | contested | contradicted | untestable | pending`. `contested` holds 114 of the 172 decided external verdicts, and four earlier passes call it a dumping ground (MA-08, TV-06, ST-12, AS-11). Proposal (c) would split it four ways. This pass tests a different instrument: keep the verdict word and add a rating of *how certain the evidence makes it*, by the GRADE approach used for systematic reviews in medicine (high, moderate, low, very low; five reasons to rate down, three to rate up). It asks which instrument tells a reader more, and it applies the rating to every decided external verdict on a load-bearing node and to a seeded sample of 30 others.

**Order of work (stated so the reader can discount it).** 1. The GRADE texts were fetched, hashed and quoted (section 1; 67 quotes, machine-checked). 2. The applier ran the read-only frame count and the seeded draw (`research/tools/grade_certainty.py sample`) and opened one claim file (`A2e-ltee-as-ceiling.md`) to learn the layout. No claim file of the sample had been read by this instance. Verdict comments of many load-bearing nodes had been seen through the earlier passes' tables. 3. Sections 1 to 3 (framework, adaptation, scope) were written and committed. 4. The ratings (section 4 onward) were made in a later commit. The adaptation was written by an instance that already knew where the earlier passes said the weak points were, so it is not blind to them.

**What this pass does not do.** It changes no verdict, rule, claim file, check script or argument-map entry, and runs no check. It rates the **external** column only. The **internal** column (does the conclusion follow from the author's own premises) and the **fidelity** column (do the citations say what is claimed) are not rated at all: GRADE grades confidence in an estimate drawn from a body of evidence, and neither the validity of an argument nor the accuracy of a citation is such an estimate (section 2.9). It does not re-read the check write-ups in full: each row is rated from the claim file's front matter and R4 paragraphs, the check's paragraph in `research/checks/RESULTS.md`, `research/checks/PREREG-STATUS.md`, and the grade table of the severe-testing pass.

---

## 1. GRADE, from the fetched texts

Sources: the GRADE Handbook (Schünemann, Brożek, Guyatt and Oxman, eds., updated October 2013), the first two papers of the 2008 BMJ series (Guyatt et al.), the working group's 2017 paper on the construct of certainty (Hultcrantz et al.), its guidance on modelled evidence (Brozek et al. 2021), on non-randomised studies (Schünemann et al. 2019) and on evidence without a pooled estimate (Murad et al. 2017). Bibliography rows and hashes: [`../sources/bib-literature.md`](../sources/bib-literature.md), section "Criticality pass vi"; fetch log: [`../sources/harvest-log-literature.md`](../sources/harvest-log-literature.md); quotes GC-01 to GC-67: [`../sources/quotes-literature.md`](../sources/quotes-literature.md). **Not obtained:** the new GRADE Book, which the handbook's own disclaimers say has updated its sections 1, 2, 3, 5 and 8 (the site returns a script-rendered shell); Balshem et al. 2011 and the single-domain papers of the J Clin Epidemiol series. Three statements in this file are **from memory** and marked so where they occur.

**What is rated.** For the authors of a review, "The quality of evidence reflects the extent to which we are confident that an estimate of the effect is correct." (GC-01). The unit is a body of evidence for one outcome, not a study: "The quality of evidence is rated for each outcome across studies (i.e. for a body of evidence). This does not mean rating each study as a single unit." (GC-02). The handbook and the 2008 papers say "quality"; the working group later preferred "certainty" and restated the construct: "Certainty of evidence is best considered as the certainty that a true effect lies on one side of a specified threshold, or within a chosen range." (GC-41); "we are not assessing our confidence in point estimates of effects, but rather our confidence in where effects lie relative to particular thresholds" (GC-42).

**The four levels** (handbook, Table 5.1):

| Level | Definition |
|---|---|
| High | "We are very confident that the true effect lies close to that of the estimate of the effect." (GC-03) |
| Moderate | "We are moderately confident in the effect estimate: The true effect is likely to be close to the estimate of the effect, but there is a possibility that it is substantially different" (GC-04) |
| Low | "Our confidence in the effect estimate is limited: The true effect may be substantially different from the estimate of the effect." (GC-05) |
| Very low | "We have very little confidence in the effect estimate: The true effect is likely to be substantially different from the estimate of effect" (GC-06) |

The 2008 wording defines the same levels by what further research would do: "Further research is very unlikely to change our confidence in the estimate of effect" (high, GC-30) down to "Any estimate of effect is very uncertain" (very low, GC-33).

**Structure.** "The GRADE approach to rating the quality of evidence begins with the study design (trials or observational studies) and then addresses five reasons to possibly rate down the quality of evidence and three to possibly rate up the quality." (GC-08). Randomised trials start high; "observational studies without special strengths or important limitations provide low quality evidence" (GC-11), because of "the magnitude of the potential for residual confounding, and the limited protection against bias provided by adjusted analysis" (from GC-57). "Expert opinion is not a category of quality of evidence." (GC-12); "It is important to describe what type of evidence (whether published or unpublished) is being used as the basis for interpretation." (GC-13). The starting level is not one fixed rule: it differs by kind of question (GC-64), and where a full risk-of-bias tool is applied to non-randomised studies "the initial GRADE certainty in the evidence from a body of studies using an NRS design would be high" (GC-58), with the warning that a rater must not "double count the risk of confounding and selection bias" (GC-59) and the expectation that under either starting point "the final certainty rating should be the same." (GC-60).

**Five reasons to rate down** (each by one or two levels):

| Domain | Definition in the texts |
|---|---|
| Risk of bias | "Our confidence in an estimate of effect decreases if studies suffer from major limitations that are likely to result in a biased assessment of the intervention" (GC-14). Whether a limitation counts depends on how exposed the outcome is to judgement: "it is possible that stroke - much more vulnerable to biased judgments - will be rated down for risk of bias, whereas all-cause mortality will not." (GC-67) |
| Inconsistency | "Inconsistency refers to an unexplained heterogeneity of results." (GC-15). "Investigators should explore explanations for heterogeneity, and if they cannot identify a plausible explanation, the quality of evidence should be downgraded." (GC-16). Without a pooled estimate: "Judge inconsistency by evaluating the consistency of the direction and primarily the difference in the magnitude of effects across studies" (GC-62) |
| Indirectness | "Direct evidence consists of research that directly compares the interventions which we are interested in, delivered to the populations in which we are interested, and measures the outcomes important to patients." (GC-17). Reviewers "should consider the extent to which they are uncertain about the applicability of the evidence to their relevant question and downgrade the quality rating by one or even two levels." (GC-18) |
| Imprecision | "In general, results are imprecise when studies include relatively few patients and few events and thus have a wide confidence interval (CI) around the estimate of the effect." (GC-19) |
| Publication bias | "Publication bias is a systematic under-estimation or an over-estimation of the underlying beneficial or harmful effect due to the selective publication of studies." (GC-20). It is a property of the set of studies: confidence "can be reduced when publication bias is suspected, even when the included studies themselves have a low risk of bias." (GC-21) |

**Three reasons to rate up**, considered only afterwards: "Consideration of factors reducing quality of evidence must precede consideration of reasons for rating it up." (GC-22); "The decision to rate up should only rarely be made if serious limitations are present in any of these areas." (GC-23).

| Factor | Definition in the texts |
|---|---|
| Large effect | "When body of evidence from observational studies not downgraded for any of the 5 factors yield large or very large estimates of the magnitude of an intervention effect, then we may be more confident about the results." (GC-24). Thresholds: a relative risk above 2 "may increase 1 level", above 5 "may increase 2 levels", in both cases "based on direct evidence" (GC-65, GC-66); and by the interval, not the point value (GC-25) |
| Dose-response | "The presence of a dose-response gradient may increase our confidence in the findings of observational studies and thereby increase the quality of evidence." (GC-26) |
| Opposing bias | "On occasion, all plausible residual confounding from observational studies may be working to reduce the demonstrated effect or increase the effect, if no effect was observed." (GC-27) |

**Modelled evidence.** The working group's 2021 paper holds that the same domains "also apply when assessing the certainty of evidence from models" (GC-44) and stops there: "further work is needed to identify examples and develop specific criteria to be assessed" (GC-45); "Specific methods for operationalizing this integration remain to be developed." (GC-56). It gives no starting level for a model. What it does fix: "The risk of bias of model outputs (i.e., model outputs being systematically overestimated or underestimated) is determined by the credibility of a model itself and the certainty of evidence for each of model inputs." (GC-46); directness is "the extent to which model outputs directly represent the phenomenon being modeled" (GC-48), and "When there are concerns about the directness of the model or there is limited understanding of the system being modeled making it difficult to assess directness, then one may have lower confidence in model outputs." (GC-49); imprecision is read from sensitivity analysis and "the robustness of model's qualitative conclusions" (GC-50); inconsistency is "unexplained differences across model outputs" (GC-55); publication bias is "the likelihood that relevant models have been constructed but were not published" and "may not be relevant" for a single model built for the purpose (GC-51, GC-52); whether a large effect counts "may depend on the modeling discipline" (GC-53); and the opposing-bias upgrade is "a conservative model not incorporating input data parameter in favor of an intervention but still finding favorable outputs" (GC-54).

**Limits the texts state themselves.** "Quality of evidence is a continuum; any discrete categorisation involves some degree of arbitrariness." (GC-07). "Therefore, GRADE is not a quantitative system for grading the quality of evidence." (GC-09). "We caution against a mechanistic approach toward the application of the criteria for rating the quality of the evidence up or down." (GC-28). "Indeed, the great merit of GRADE is not that it ensures reproducible judgments but that it requires explicit judgment that is made transparent to users." (GC-10). "Authors of systematic reviews do not grade the overall quality of evidence across outcomes." (GC-29). The guidance for evidence without a pooled estimate covers "quantitative estimates of effect not amenable to meta-analysis" and excludes reviews of conceptual questions (GC-63).

*From memory, not from the fetched texts:* (m1) GRADE's guidance for questions of prognosis starts a body of cohort studies at high, which is what GC-64 alludes to; (m2) a separate instrument, GRADE-CERQual, exists for qualitative evidence and was not looked at; (m3) the GRADE Book may word the definitions differently from the 2013 handbook.

---

## 2. The adaptation (written and committed before any rating)

GRADE rates certainty in an effect estimate for an outcome. Nothing in this audit is an effect estimate in that sense. The adaptation below is this pass's own construction; each choice names the GRADE text it leans on and says where it departs.

### 2.1 Unit and rated proposition

**Unit:** one decided external verdict field on one claim file (`supported`, `contradicted`, `contested`, `untestable`).

**Rated proposition.** By GC-41, certainty is confidence that the truth lies on one side of a stated threshold. An external verdict is a statement of that kind: the claim, as its author worded it in the verbatim Statement, is true of the world (`supported`) or is not (`contradicted`). The rating answers: *how confident does the recorded body of evidence make us that the truth lies on the side the verdict names?* The "threshold" is the claim's own truth condition, or the flip value where the claim file states one (for example "above 191 adaptive substitutions").

The proposition is the claim **as the author stated it**. Where the verdict comment narrows it ("SCOPED", "per site", "in the exchangeable class", "as a conditional"), the gap between the narrowed statement and the author's statement is counted under indirectness (2.5), because a reader of a tally sees the bare word.

**What a rating is not.** It is not the probability that the verdict is right, not a grade of how well the check was done, and not a verdict. `contradicted` at very low certainty means "the evidence recorded does not yet show this", not "the claim is true".

### 2.2 Direction (needed because `contested` names no side)

`contested` states no side, so "certainty that the verdict is correct" has no meaning for it until one asks what the evidence says. Each row therefore gets a **direction** first, then a certainty for the statement the direction makes.

| Direction code | Meaning | What the certainty then rates |
|---|---|---|
| `for` | The recorded evidence points to the claim being true of the world | that the truth lies on that side |
| `against` | It points to the claim being false of the world | that the truth lies on that side |
| `cond` | The answer turns on a named parameter or regime; the claim file says which side of a stated value goes which way | the conditional statement itself (the flip and its location), not either side |
| `mixed` | Results point both ways with no named condition that sorts them | the statement that the evidence is mixed |
| `ne` | No evidence is recorded for the external verdict (empty comment and nothing in the Check or R4 text that bears on the world) | nothing: **not rated (NE)** |
| `na` | The verdict is `untestable` | nothing: **not rateable (NR)**; the verdict asserts that no test exists, which is not a side of a threshold |

`supported` is `for` and `contradicted` is `against` by definition. For a `contested` row the rule, fixed here: code `for` or `against` only if (i) the claim file's external comment or R4 text states a lean, or records a result on one side of a stated flip, for the claim as its author stated it, in at least the regime tested, and (ii) no recorded result points the other way inside a regime the claim covers. Otherwise `cond` if a deciding parameter or regime is named, `mixed` if not, `ne` if nothing is recorded.

A high certainty on a `cond` row means "we are confident the question is open in the way described". It does not favour either party.

### 2.3 Evidence basis and kind of question

Each row is coded with the **basis** of the evidence that carries the verdict, using proposal (b)'s four values plus two it lacked, and with the **kind of question** the verdict answers.

| Basis code | Meaning |
|---|---|
| `D` data | An observation the audit processed itself in a registered check (an alignment, genotypes, a published data table recounted) |
| `L` literature, measurement or record | A published measurement, count or documentary fact, cited and not reprocessed |
| `Lm` literature, model-based estimate | A published value that was itself inferred through a population-genetic model (an adaptive fraction, an ancestral N_e, a fitted distribution of fitness effects) |
| `S` simulation | A forward or exact-chain simulation under a stated model, or a calculation that applies a model to inputs |
| `T` theory | An identity or analytical result of standard population genetics, stated or proved, with no observation |
| `C` concession only | The author's own withdrawal or agreement, with no other ground recorded |
| `N` none | Nothing recorded |

One primary basis per row; a second is named in the reason. Where the basis is mixed, the primary one is the one without which the verdict value would not stand.

| Kind | Meaning |
|---|---|
| `W` world | The verdict asserts something about real genomes, populations or history |
| `F` formal or documentary | The verdict asserts what a model or definition implies, or what a published record contains ("the cost bounds selected substitutions only"; "a quantitative literature exists after 1966") |

The kind is read from the claim's verbatim Statement and formal statement, not from the evidence used. The external column is defined as "whether its premises fit the world", so `F` rows are, strictly, in the wrong column (MA-15); they are rated as they stand and counted.

### 2.4 Starting level: the mapping used, and the two alternatives

**Principle of the mapping used (M0).** GRADE starts randomised trials high because the design removes the main systematic alternative explanation, and starts observational studies low because it does not (GC-11, GC-57). The main systematic alternative explanation for an external verdict in this audit is not confounding. It is **dependence on the model in dispute**: evidence produced by assuming standard population genetics cannot show that the world is as that model says (MA-05, TV-04, ST-02, AS-08). So:

> **Start high** where the evidence observes the thing the verdict is about. **Start low** where it reaches that thing through a model whose fit to the lineage is not itself observed.

| Basis | Kind `W` | Kind `F` | Why |
|---|---|---|---|
| `D` data | high | high | A recount of public data observes the quantity. What can still go wrong (assembly, alignment, annotation, filters, the audit's choice of statistic) is execution, rated under risk of bias, as GC-58 does for non-randomised studies with a full bias appraisal |
| `L` literature, measurement or record | high | high | Same design as `D`. That the audit did not reprocess or appraise the source is rated under risk of bias, not in the start, so that it is counted once (GC-59) |
| `Lm` literature, model-based estimate | low | high | For a world claim the estimate carries the model's assumptions with it: the analogue of residual confounding. For a claim about what the literature reports, it is the record itself |
| `S` simulation | low | high | For a world claim a simulation shows what follows from its assumptions (GC-46, GC-48). For a formal claim it is an experiment on the object the claim is about |
| `T` theory | low | high | For a world claim an identity with no observation is the field's considered opinion, and "Expert opinion is not a category of quality of evidence" (GC-12); it is rated as modelled evidence, not as nothing. For a formal claim a proof observes the thing claimed |
| `C` concession only | not rated (NE) | not rated (NE) | An author's withdrawal is an opinion about the evidence (GC-13: say what it rests on). Where nothing else is recorded there is no body of evidence to rate (AS-03) |
| `N` none | not rated (NE) | not rated (NE) | No body of evidence |

M0 uses GRADE's two starting levels only. It departs from the handbook in one respect: the handbook starts by study design alone, and M0 starts by design and kind of question together, which GC-64 shows GRADE itself does across question types.

**What a Day-side reader would argue (mapping M-D).** Only observations "the claimant does not control" anchor a claim (Day's Triveritas E-leg, Q212). Published values in this field are produced by the party whose theory they support, usually with that theory's tools. An identity or a simulation of the standard model is mathematics without anchoring, and the external column is about the world, so no row is `F`.

| Basis | M-D start (all rows treated as `W`) |
|---|---|
| `D` | high |
| `L` | low |
| `Lm`, `S`, `T` | very low |

Under M-D the model-to-world part of indirectness (2.5, tag `mw`) is already in the start and is not taken off a second time (GC-59).

**What a critic-side reader would argue (mapping M-C).** Standard population genetics is the most tested body of results in the field; a theorem that holds over a wide class of models, and decades of published measurements, are not an "observational study" to be started low. The weak evidence here is the audit's own: pipelines and simulations written by an AI system in days, unreviewed by a specialist. Start everything high (the GC-58 route) and rate down what is actually wrong.

| Basis | M-C start (both kinds) |
|---|---|
| `D`, `L`, `Lm`, `S`, `T` | high |

Under M-C the `mw` part of indirectness is not counted (the model's fit to the lineage is taken as background), and risk of bias is at least "serious" for any `D` or `S` row whose deciding result has not been reproduced by a second tool, data release, host-independent method or published number (flag `ur`).

**Use.** Every row is rated under M0 with the five domains written out. The M-D and M-C certainties are then *computed* from the same codes by the rules above (2.7), so a reader can see exactly where the mappings part. Where the three agree, the rating does not depend on whose starting point one takes.

### 2.5 The five reasons to rate down, adapted

Each is judged **not serious** (0), **serious** (−1) or **very serious** (−2), with a one-line reason and a file reference. The decision rules:

**Risk of bias** (GC-14, GC-46, GC-67): could the way the deciding evidence was produced have pushed the result toward the recorded verdict?

| Level | When |
|---|---|
| not serious | The deciding evidence is a check graded SEVERE by the severe-testing pass; or graded PARTIAL with label `blind` or `reproduction` and not hinging on an operationalisation, reading or band of the audit's own choosing; or published measurements from two or more independent sources, or one source that the audit reproduced; or, for an `F` row, a proof or exact computation |
| serious | A PARTIAL check labelled `unknown`, `single-commit` or `criterion-only`; any WEAK check; a verdict that hinges on a statistic, reading or operationalisation chosen by the audit (this is where non-blind same-model review counts, by the reasoning of GC-67: it bears on judgements, not on recounts); a single published source neither appraised nor reproduced; an inline calculation or reading with no registered check and no review |
| very serious | A BENT check as the only ground for a `W` verdict; a criterion, band or reading fixed with the numbers known where the verdict value then moved (MA-03); a model whose validation failed and was not resolved |

Same-model, non-blind review applies to every row (MA-01). It is counted only where a judgement decides the verdict. A reader who weights MA-01 more heavily should read every rating in this file as an upper bound.

**Inconsistency** (GC-15, GC-16, GC-55, GC-62): unexplained disagreement about the direction of the deciding result.

| Level | When |
|---|---|
| not serious | No recorded disagreement in direction; or disagreement fully sorted by a named regime or parameter (the row is then `cond`, and GC-16 says explained heterogeneity does not count) |
| serious | The verdict differs between plausible readings recorded under rule RD or between scopes named in the comment; two checks or two tools differ on the deciding quantity by more than the 25% materiality margin with no explanation (this includes a simulated *count* that the second engine, fwdpy11, did not reproduce: ST-06); published sources fall on both sides of the flip; a registered prediction of the audit's about the deciding quantity failed in direction |
| very serious | Results of equal standing on opposite sides of the flip with no explanation; or the author's later text re-asserts what the ground says he withdrew |

**Indirectness** (GC-17, GC-18, GC-48, GC-49): the gap between what the evidence is about and what the claim is about. Three tags, each 0, 1 or 2; the domain total is capped at two levels, as in GRADE.

| Tag | Gap | serious (1) | very serious (2) |
|---|---|---|---|
| `mw` | model to world | The evidence is a model result and the model's fit to the lineage, in the respect the verdict needs, is not itself evidenced | That fit is the very point the other party disputes (the argument-structure pass's question MW5) |
| `sp` | species, parameters, regime, data set | The regime, organism, assembly or parameter range tested is not the one the claim is about, but adjoins or brackets it | The claimed regime lies wholly outside what was tested |
| `rd` | wording | The verdict is on a narrowed, scoped, paraphrased or charitably chosen version of the author's statement, on a claim known only at second hand, or on a statistic the audit defined in place of one the author left undefined | The verdict's proposition is one the author did not make |

For `F` rows `mw` is 0 by definition.

**Imprecision** (GC-19, GC-50): does the uncertainty in the deciding quantity reach across the flip?

| Level | When |
|---|---|
| not serious | The stated bracket of every deciding input stays on one side of the flip; or the result is exact |
| serious | A deciding input is unsourced, or its sourced bracket crosses the flip; or the result rests on a handful of replicates or cells whose spread crosses the flip |
| very serious | The answer changes side across the plausible range of an unsourced input by an order of magnitude or more, with no anchoring value |

On a `cond` row the unsourced deciding parameter *is* the stated condition and is not counted against it; imprecision then concerns the flip value (serious if the flip is itself a range wider than twofold or depends on a second unsourced input).

**Selection of evidence** (the analogue of publication bias; GC-20, GC-21, GC-51): is the evidence behind this verdict a selected part of what exists or could have been produced? GC-52 says publication bias "may not be relevant" for a single model built for the purpose. This pass departs from that, on purpose: the audit chose which claims got a check with no written rule (AR-11), its literature arm has no search strategy (AR-05), and some sources bearing on particular verdicts are unread (MA-09).

| Level | When |
|---|---|
| undetected (0) | No named unrun check, unread source or set-aside result bears on this verdict's direction |
| suspected (−1) | A named unrun check, unreleased pipeline or unread source bears on this verdict and could plausibly reverse it (for example a registered like-for-like rerun not yet made; the claim is known only through a critic's video; the book); or the ground is literature gathered without a search on a point where published estimates are known to differ |
| strongly suspected (−2) | The deciding sources were picked, or the deciding criterion written, with their values known, and a contrary source was set aside or reclassified |

### 2.6 The three reasons to rate up, adapted

GRADE's own restrictions are kept: upgrades apply only to a body of evidence that started low and was "not downgraded for any of the 5 factors" (GC-24), and large-effect upgrades need direct evidence (GC-65).

| Factor | Analogue here | Size |
|---|---|---|
| Large effect | **Margin to the flip.** The bound of the stated interval nearest the flip (not the point value, GC-25) lies at least 2 times past the flip: +1; at least 5 times: +2. The factors 2 and 5 are the handbook's relative-risk thresholds (GC-65, GC-66) carried over to the ratio of the result to the flip value; that carry-over is this pass's construction | +1 or +2 |
| Dose-response | **Monotone trend.** The result moves monotonically across at least three ordered levels of the parameter the claim is about (K, R, N, map length, supply), in the direction the verdict's reasoning predicts | +1 |
| Opposing bias | **Conservative design.** The check was built on the assumption most favourable to the party the verdict goes against, and the verdict still went against that party (GC-54). A design favourable to the party the verdict *helps* is the reverse and counts under risk of bias | +1 |

Each row records which factors are **present** (`upf`, the number of levels they would add, at most 2). They are **applied** only if the row started low under the mapping in question and has no downgrade in any domain under that mapping. Because the applied rule is strict, a sensitivity line in the aggregates reports how many rows would move under a lenient rule (factor present, start low, risk of bias not serious, no domain very serious).

### 2.7 Arithmetic, stated so it can be recomputed

Levels: very low = 0, low = 1, moderate = 2, high = 3. Code line per row: `b` (basis), `k` (kind), `rob`, `inc`, `mw`, `oi` (other indirectness: the larger of `sp` and `rd`, capped at 2), `imp`, `sel`, `ur` (1 if a `D` or `S` result is unreproduced), `upf`, `dir`.

| Mapping | Start | Down | Up |
|---|---|---|---|
| M0 | by the table in 2.4 | `rob + inc + min(2, mw + oi) + imp + sel` | `upf` if start is low and Down = 0, else 0 |
| M-D | `D` 3; `L` 1; `Lm`, `S`, `T` 0 | `rob + inc + min(2, oi) + imp + sel` | `upf` if start ≤ 1 and Down = 0, else 0 |
| M-C | 3 | `max(rob, ur) + inc + min(2, oi) + imp + sel` | none (nothing starts low) |

Final = start − Down + Up, held within 0 to 3. `dir` in {`ne`, `na`} or `b` in {`C`, `N`}: no number; the row reads NE or NR. `research/tools/grade_certainty.py count` recomputes every printed value from the code column and fails if one differs.

GRADE warns against exactly this kind of sum (GC-09, GC-28). The sum is used here for one reason: with a single same-model rater, a rule that can be recomputed is worth more than a judgement that cannot be checked. Each code is still a judgement.

### 2.8 "What would raise it one level"

Each rated row names the single cheapest change that would remove one downgrade: a check to run, a source to read, a scope to write into the verdict value, a parameter to source. For NE rows it names what evidence would make the row rateable.

### 2.9 What GRADE cannot do here, and how to read the result

1. **It does not adjudicate arguments.** Whether a conclusion follows from premises (the internal column), whether an author was read correctly (fidelity), whether a step is a non-sequitur: none of these is an estimate from a body of evidence. The argument-structure pass is the instrument for those. This pass leaves the internal and fidelity columns unrated.
2. **It has no place for "the question is conditional".** GRADE assumes one estimate whose distance from a threshold is uncertain. Many `contested` verdicts are a different object: a known dependence on an unknown parameter. The `cond` direction is this pass's patch; a high rating on such a row is confidence in the map of the dependence, not in either side.
3. **It has no starting level for a model**, by its own account (GC-45, GC-56). The starting levels in 2.4 are the place where the three mappings differ, and the place a reader should look first.
4. **It gives no overall grade.** "Authors of systematic reviews do not grade the overall quality of evidence across outcomes." (GC-29). No certainty is assigned to ROOT, to a branch or to a party, and the distributions in section 5 are not to be averaged into one.
5. **It is not reproducible by design** (GC-10). Two raters will differ by a level on many rows. One same-model rater produced these.
6. **Its unit is the verdict, not the claim.** A claim may be true and its verdict poorly evidenced, or the reverse.
7. **Do read it as:** for each verdict, how far the recorded evidence carries the word in the field, in which direction, and what would carry it further. **Do not read it as:** a score for Day or for his critics; a count of who is ahead; a statement that low-certainty verdicts are wrong; or an independent appraisal.

---

## 3. Scope, sample and table format

### 3.1 Load-bearing set: all 28

All decided external verdicts on the 33 nodes that `hierarchy.yaml` marks `load_bearing: true`. Five of the 33 have external `pending` (ROOT, ROOT-M, E5, E6, F1a) and are not rated. The 28: A, A2e, A3, B, B1, B1c, B2, B2b, B3, B3a, B3g, B4a, B5, B6, B7, C2, C2a, F, F1, F2, F3a, FM10, H, H1, H2, H5, H8, ROOT-FM (20 `contested`, 4 `contradicted`, 4 `supported`).

### 3.2 Sample of 30 from the other 144

Frame: the 144 decided external verdicts on claim files that are not load-bearing.

| Verdict | day | critic | ally | literature | Total |
|---|---|---|---|---|---|
| `contested` | 50 | 24 | 9 | 11 | 94 |
| `supported` | 8 | 14 | 0 | 8 | 30 |
| `contradicted` | 13 | 1 | 0 | 0 | 14 |
| `untestable` | 1 | 2 | 2 | 1 | 6 |

**Forced inclusions (17).** Proposal (c)'s trial sample of 20 `contested` ids (`random.Random(20261012).sample(sorted(ids), 20)`, `research/tools/method_audit_stats.py`) is reused so that the two instruments can be compared on the same claims. Three of the 20 are load-bearing (A, F2, H) and are rated in 3.1. The other 17 enter the sample: A2, A3z, A4, A4f, A4g, B2c, B4d, B4e, D13, D15, D3, D4, D9, G2g, Ga, ROOT-K, ROOT-PG.

**Stratified draw (13).** The 17 are all `contested` (day 9, critic 3, ally 3, literature 2). The remaining 13 places were allocated before the draw to bring the sample near the frame's shares by verdict value (proportional would be 19.6, 6.3, 2.9, 1.3 of 30) and to put each party in each decided value where the frame allows: `supported` 6 (critic 2, day 2, literature 2); `contradicted` 3 (day 2, critic 1, the only one); `untestable` 2 (day 1, the only one; critic 1); `contested` 2 (critic 2, the party most under-represented among the 17). Draw: one `random.Random(2026101206)`, strata in that order, `rng.sample(sorted(pool), n)` (`research/tools/grade_certainty.py sample`).

Drawn: F1b, H6 (`supported`, critic); A1, A6a (`supported`, day); DN5, A1b (`supported`, literature); DN1, DN2 (`contradicted`, day); B5c (`contradicted`, critic); D7b (`untestable`, day); ROOT-COV (`untestable`, critic); B5f, G2f (`contested`, critic).

Sample of 30: `contested` 19, `supported` 6, `contradicted` 3, `untestable` 2; day 14, critic 9, ally 3, literature 4. It over-samples `supported`, `contradicted` and `untestable` on purpose and is **not** a proportional sample of the 144; section 5 says where a scaled figure is given and with what weights. With 30 rows a share carries roughly ±18 points.

Total rated: 58 of the 172 decided external verdicts.

### 3.3 Columns of the summary-of-findings table

Claim id; party; quote id (the id of the verbatim Statement quote where the claim file gives one, else the source key and locator); verdict; basis and kind; starting level (M0); the five domains, each with level, reason and file reference; upgrade factors present; direction; certainty under M0, M-D and M-C; what would raise it one level; and the code line of 2.7.

### 3.4 Expectations written down before the ratings (not blind)

From the earlier passes, not from the claim files of the sample: (1) most of the eight `supported` or `contradicted` verdicts on load-bearing nodes will rate low or very low under M0 and high or moderate under M-C, since seven rest on a model or an identity (AS-01); (2) in the sample, about a third of `contested` rows will be NE (proposal c found 6 of 20 with no recorded basis) and the directional ones will mostly be `against` on Day claims; (3) the three mappings will agree on data-based rows and part widely on theory rows; (4) under the strict rule almost no upgrade will be applied, because few rows have no downgrade. If the ratings show something else, section 5 says so.

---

*Sections 4 onward (summary of findings, aggregates, symmetry, recommendation, concordance, findings GR-01 onward) are added in a later commit.*
