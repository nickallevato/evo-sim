# Certainty-of-evidence pass, 2026-10-12: how sure can each external verdict be?

*Criticality layer, component vi. Applier: one Claude instance (Opus 5.5) in the project's own session, the same model family that extracted the claims, wrote and ran the checks, reviewed them and wrote the verdicts rated here. Single rater. Not blind: the applier read the criticality README (with the MA, TV, AR, ST and AS findings), the proposals file, the methods page, the verdict rule, and the tables of the severe-testing and argument-structure passes before writing the adaptation. Day's papers credit a co-author from the same model family, and the model's training corpus is overwhelmingly mainstream on evolution (methods page, "Who did it"). Every rating below is one same-family rater's judgement and not an outside review (finding GR-13).*

**The question.** The external verdict vocabulary is `supported | contested | contradicted | untestable | pending`. `contested` holds 114 of the 172 decided external verdicts, and four earlier passes call it a dumping ground (MA-08, TV-06, ST-12, AS-11). Proposal (c) would split it four ways. This pass tests a different instrument: keep the verdict word and add a rating of *how certain the evidence makes it*, by the GRADE approach used for systematic reviews in medicine (high, moderate, low, very low; five reasons to rate down, three to rate up). It asks which instrument tells a reader more, and it applies the rating to every decided external verdict on a load-bearing node and to a seeded sample of 30 others.

**Order of work (stated so the reader can discount it).** 1. The GRADE texts were fetched, hashed and quoted (section 1; 67 quotes, machine-checked). 2. The applier ran the read-only frame count and the seeded draw (`research/tools/grade_certainty.py sample`) and opened one claim file (`A2e-ltee-as-ceiling.md`) to learn the layout. No claim file of the sample had been read by this instance. Verdict comments of many load-bearing nodes had been seen through the earlier passes' tables. 3. Sections 1 to 3 (framework, adaptation, scope) were written and committed. 4. The ratings (section 4 onward) were made in a later commit. The adaptation was written by an instance that already knew where the earlier passes said the weak points were, so it is not blind to them.

**What this pass does not do.** It changes no verdict, rule, claim file, check script or argument-map entry, and runs no check. It rates the **external** column only. The **internal** column (does the conclusion follow from the author's own premises) and the **fidelity** column (do the citations say what is claimed) are not rated at all: GRADE grades confidence in an estimate drawn from a body of evidence, and neither the validity of an argument nor the accuracy of a citation is such an estimate (section 2.9). It does not re-read the check write-ups in full: each row is rated from the claim file's front matter and R4 paragraphs, the check's paragraph in `research/checks/RESULTS.md`, `research/checks/PREREG-STATUS.md`, and the grade table of the severe-testing pass.

---

## Executive summary

**What was done.** GRADE's four certainty levels, five reasons to rate down and three to rate up were taken from the handbook and six working-group papers (67 quotes, machine-checked), adapted in writing to the unit "one external verdict", and committed (`86cdf64`) before any rating. They were then applied to all 28 decided external verdicts on load-bearing nodes and to a seeded, stratified sample of 30 of the other 144 (seed 2026101206), which contains the 20 claims of proposal (c)'s trial. Every rating is recomputable from a code line by `research/tools/grade_certainty.py`. The internal and fidelity columns were not rated.

**The adaptation in one paragraph.** A verdict is rated for how far the recorded evidence carries it as a statement about the world, after a direction is assigned (for the claim, against it, or none). Evidence that observes the thing claimed starts high; evidence that reaches it through a model starts low (mapping M0). Because GRADE gives no starting level for a model, two alternatives are computed from the same codes: a Day-side mapping (only data the audit processed starts high) and a critic-side mapping (everything starts high; the audit's own unreproduced work is rated down).

**What it found.**

| | high | moderate | low | very low | no evidence recorded | not rateable |
|---|---|---|---|---|---|---|
| All 58 rated rows (M0) | 3 | 7 | 3 | 32 | 11 | 2 |
| Load-bearing (28) | 2 | 2 | 1 | 22 | 1 | 0 |
| Sample (30) | 1 | 5 | 2 | 10 | 10 | 2 |

- **Over-stated verdicts.** 11 of the 17 `supported` or `contradicted` verdicts rated are low or very low; 8 of them under all three mappings: A2e, B1c, B3, B6 (load-bearing) and F1b, DN1, DN2, B5c. Nine of the eleven sit on the critics' side of the ledger.
- **Under-stated verdicts.** Two `contested` verdicts carry a clear direction at moderate or high certainty: A3 (load-bearing; Day's required-fixations count is corroborated by three data counts, high under every mapping) and D9 (against Day, moderate).
- **What `contested` holds** (39 rated): 5 with a lean (2 moderate or high, 3 low or very low), 23 conditional or mixed, 11 with no evidence recorded. Estimated for all 114: about 45 with nothing recorded, about 19 with a lean, about 50 conditional or mixed.
- **The instrument saturates.** 32 of 45 rated rows are at the floor. A conditional worked out inside a model is very low as a statement about the world however good the work, so the rating cannot tell a well-mapped conditional from a poor one without an added column (FR).
- **The stance decides a third of the rows.** The Day-side and critic-side mappings differ by two or more levels on 15 of 45 rows, all resting on theory, simulation or the literature. They agree on the over-stated and under-stated lists above.
- **Against the four-way split,** on the 20 shared claims: same sorting on 14, in part on 5, different on 1. The split is the better instrument inside `contested`; the certainty rating is the only one of the two that touches `supported` and `contradicted` and that grades a lean.
- **Symmetry.** By the same rules, each party has one headline number that is high as a description (Day's required count; keruru's temporal N_e) and none better than moderate as evidence for its conclusion. Day's dN/dS of 0.80 is very low as a description under every mapping.

**Recommendation (proposal k, not applied):** adopt both. `external_certainty` and `external_direction` beside every decided external verdict, the four-way split as a companion field for rows with no direction, rows with no evidence to `pending`, and the mapping always stated. No verdict value moves.

**Credited as sound.** The data counts behind A3, DN5 and keruru's N_e; verdict comments that already state their own conditions (A, F2, H8, D15), which is why a direction and a "what would raise it" could be read off them; three places where the claim file itself states the limit that sets the rating (FM10: "a premise, not a verdict on FM10"; B4a prints its own failed anchor; H2 labels its reconstruction exploratory).

**Limits.** One rater of the audited model family, not blind (GR-13). Four rules were settled while rating (GR-07). GRADE was built for effect estimates in medicine; its handbook says it does not ensure reproducible judgements; a second rater would differ by a level on many rows.

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

**Rated proposition.** By GC-41, certainty is confidence that the truth lies on one side of a stated threshold. An external verdict is a statement of that kind: the claim, as its author worded it in the verbatim Statement, is true of the world (`supported`) or is not (`contradicted`). The rating answers: *how confident does the recorded body of evidence make us that the truth lies on the side the verdict names?* The "threshold" is the claim's own truth condition, or the flip value where the claim file states one (for example, more than 191 adaptive substitutions).

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
| `F` formal or documentary | The verdict asserts what a model or definition implies, or what a published record contains (for example "cost bounds selected substitutions only", or that a quantitative literature exists after 1966) |

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

## 4. Summary of findings

58 rows: the 28 decided external verdicts on load-bearing nodes, then the sample of 30. Verdict values are as the claim files give them on 2026-10-12; none is changed.

**How to read a row.** *Basis, kind, start*: the codes of 2.3 and the M0 starting level of 2.4, with the severe-testing grade of the check that decided the field. Each domain cell gives the level and the reason. *Certainty*: **M0** is the pass's mapping; M-D and M-C are the Day-side and critic-side alternatives computed from the same codes (2.7); FR is explained in note N4. *Code*: the line that `research/tools/grade_certainty.py count` recomputes from; it reports 0 mismatches. The line carries `sp` and `rd` separately (the `oi` of 2.7 is the larger of the two) and, besides the codes of 2.7, the row's id, party, load-bearing flag, verdict and the severity grade `st` of the deciding check.

**File references.** CF = the external-verdict comment in the claim file's front matter (`docs/research/claims/<id>-*.md`); R4 = that file's R4 paragraphs; CK = its Check section; ST#n = row n of the table in section 4 of [`severe-testing-2026-10-12.md`](severe-testing-2026-10-12.md), ST§6 and ST 7.x its sections; AS = the layout of the node in [`argument-structure-2026-10-12.md`](argument-structure-2026-10-12.md); labels in code font (`blind`, `unknown`, `single-commit`, `criterion-only`) are from `research/checks/PREREG-STATUS.md`. Text in double quotes is verbatim from those files (machine-checked as substrings).

**Application notes (written while rating, so post hoc relative to the adaptation committed in `86cdf64`).** The committed rules left four things open. Each was settled once, as follows, and applied to every row; a reader may prefer the other choice, and the sensitivity of the result to each is given in 5.7.

- **N1. Starting low and the `mw` tag.** Read literally, section 2.5 puts `mw` 1 on nearly every model-based world row, on top of a low start that is already there because a model stands between the evidence and the world. That is close to the double counting GC-59 warns against. Reading used: the low start says a model is in the way; `mw` 1 is added where no observation recorded at the node anchors the model's result (true of every model-based world row except B4a, which *is* a comparison with the observed divergence); `mw` 2 where that fit is the point in dispute. The table "M0 without the `mw` tag" in 5.7 shows what the other reading gives: four rows move.
- **N2. One fact, one domain.** Where one fact triggers a rule in two domains, it is counted once: a statistic the audit defined, or a scope it chose, under indirectness (`rd`), not also under risk of bias; a post hoc criterion under risk of bias, not also under selection; an unrun check that is the cure for an indirectness gap (L1b for DN1, FMnull for FM10) under indirectness, not also under selection. Each such case is marked in the row.
- **N3. Conditional rows.** On a `cond` row the unsourced parameter or unread source that *is* the stated condition is counted neither under imprecision (as 2.5 says) nor under selection (which 2.5 did not say). Selection counts on a `cond` row only where an unrun check could move the condition itself.
- **N4. Column FR ("formal reading").** Under M0 a conditional derived inside a model is rated as a statement about the world, and almost all of them land on the floor (5.5). To show what is lost, a fourth value is computed for every row whose basis is `S`, `T` or `Lm`: the certainty of the statement *"this is what the stated model or published estimate implies"*, FR = high minus (`rob` + `inc` + `rd` + `imp`), leaving out everything that concerns the fit to the world (`mw`, `sp`, selection). It is not a rating of the external verdict. It separates a well-established in-model result from a shaky one.
- **N5. `mixed`** is used once (ROOT-FM), where a description and an inference drawn from it part ways.

### 4.1 Load-bearing nodes (28)

| Claim | Party | Quote | Verdict | Basis, kind, start | Risk of bias | Inconsistency | Indirectness | Imprecision | Selection | Upgrade factors | Direction | Certainty | What would raise it one level | Code |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** | day | Q06 | `contested` | simulation, W, low; deciding check graded WEAK | serious: F2 / A-sim PARTIAL, `single-commit`; the flip (adaptive share 13-27%) comes from GAP-04, WEAK, scored on cells already published; Weissman and Barton 2012 not reprocessed (ST#16, ST#19) | not serious: two engines and the W&B formula agree within 6 to 10% (AS 3.5) | very serious: `mw` 1: multi-locus model and W&B asymptote not anchored on the lineage. `sp` 1: soft selection, 272 active loci; human scale reached by a factor labelled "EXTRAPOLATION" (CF) | serious: the flip is a range wider than twofold (13 to 27%) and moves with hard or soft selection, unsourced (CF) | suspected: "hard selection with linkage untested; tight linkage supports Day" (CF of F2): a named unrun check that bears on where the flip lies | none | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR low | Run the hard-selection-with-linkage cell at a human-length map (roadmap A21), which removes the selection downgrade | `id=A;party=day;lb=1;v=contested;b=S;k=W;st=WEAK;rob=1;inc=0;mw=1;sp=1;rd=0;imp=1;sel=1;ur=0;upf=0;dir=cond` |
| **A2e** | day | Q131 | `contradicted` | literature (model estimate), W, low; deciding check graded WEAK | very serious: decided by the A2e-alpha addendum: WEAK, `criterion-only`, "POST HOC LABEL"; trigger written by the scorer with the value known; verdict moved that evening outside the three-review tier (ST#55, MA-03) | serious: scopes named in the comment give different verdicts: strong-effect-only lower HPD 0.0 and the total-throughput basis "NOT yet `contradicted`" (CF); Gayà-Vidal's 0.2% reclassified as a null (ST#47) | very serious: `mw` 1: alpha is a model-inferred estimate, not reprocessed. `rd` 1: the count reading is fixed by the audit's formal statement; Day's stated basis is total throughput (AS 3.6, AS-04) | not serious: lower 95% HPD maps to 798 against a flip of 191 (CF) | suspected: published alpha estimates gathered with no search strategy on a point where they differ (AR-05). The post hoc choice is counted once, under risk of bias | 2 present: margin 4.2x from the interval bound (+1); built on the most Day-charitable denominator with a 25% haircut (+1). Not applied: four domains downgraded | against-claim | M0 **very-low** · M-D very-low · M-C very-low · FR very-low | The audit's own estimate from public polymorphism with planted-alpha controls (L3, roadmap A12): changes the basis to data and removes the risk-of-bias downgrade | `id=A2e;party=day;lb=1;v=contradicted;b=Lm;k=W;st=WEAK;rob=2;inc=1;mw=1;sp=0;rd=1;imp=0;sel=1;ur=0;upf=2;dir=against` |
| **A3** | day | Q05 | `contested` | data, W, high; deciding check graded SEVERE | not serious: GAP-07b, GAP-07c, GAP-07t all SEVERE; real alignments, thresholds for each side named (ST#21, ST#26, ST#46) | not serious: 21.05 M raw, 17.2-17.9 M fixed, 24.1 M on T2T per lineage: within 25% of 20 M and above the 2019 minimum of 15 M (CF) | not serious: the counted quantity is the claimed one; chimp-side polymorphism assumed, human side measured (CF) | not serious: no count leaves the 25% band around 20 M | undetected: indel and structural-variant polymorphism share open (CF); does not reach the magnitude | none | for-claim | M0 **high** · M-D high · M-C high · FR - | Already high. The verdict word, not the evidence, is what lags (AS-11) | `id=A3;party=day;lb=1;v=contested;b=D;k=W;st=SEVERE;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **B** | day | B2026-02-04 ¶60 (no Q id; Q157, Q158 carry the tag) | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: no comment at the field; by pointer to B4a (PARTIAL, `single-commit`) and B1c (AS 3.8; ST#9) | serious: B4a's model overshoots the observed 1.23% by about 25% at the sourced ancestral N_e; fwdpy11 did not reproduce the B1 counts (21% low, unlocalised) (CF of B4a; ST#3, ST-06) | very serious: `mw` 1: neutral model with ancestral diversity; the anchor test partly fails. `rd` 1: the title is the audit's paraphrase, "not scored (S1)" (R4) | serious: "(mu, T, Ne_anc) underdetermined" (CF of B4a): the flip depends on three inputs | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR very-low | State the external argument at the node (AS-02) and source the ancestral N_e, mu and T used; that removes the wording downgrade | `id=B;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=1;mw=1;sp=0;rd=1;imp=1;sel=0;ur=0;upf=0;dir=cond` |
| **B1** | day | Q34 | `contested` | theory, W, low; deciding check graded PARTIAL | not serious: the transient formula is proved symbolically (P1, `reproduction`) and estimated independently (ST#3, ST#27) | not serious: the sign of the deficit is not in dispute between tools | serious: `mw` 1: "deficit exists only for new-mutation accounting from an empty start" (CF) is a statement inside neutral Wright-Fisher | not serious: exact | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C high · FR high | An observation that bears on the start state (the ancestral-polymorphism count of roadmap A20) anchors the model and removes the `mw` downgrade | `id=B1;party=day;lb=1;v=contested;b=T;k=W;st=PARTIAL;rob=0;inc=0;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **B1c** | literature | Day blog 2026-10-01 ¶22 | `contradicted` | literature (model estimate), W, low; deciding check graded BENT | serious: the run is BENT and "not an independent empirical result"; what carries the verdict is one published ancestral-N_e series, not appraised (ST#8, ST§6) | serious: the comment leans on Day's withdrawal, and he reversed himself on the pipe twice (AS 5.5) | serious: `mw` 1: ancestral N_e is a coalescent-model inference; no site-pattern count was made | not serious: excess 1.9 to 4.0x across the step histories, all on one side (CF) | undetected | none: lower bound 1.9x, under the factor 2 | against-claim | M0 **very-low** · M-D very-low · M-C low · FR low | Count discordant site patterns with an outgroup on the alignments already held (roadmap A20): basis becomes data | `id=B1c;party=literature;lb=1;v=contradicted;b=Lm;k=W;st=BENT;rob=1;inc=1;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **B2** | day | Q29 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. No comment at the field and no argument at the node (AS 3.9); the Check and R4 text concern the internal verdict only | Record what bears on "the domain of k = mu is empty for large vertebrates": sourced V_k and census histories (B2b), or move the field to `pending` | `id=B2;party=day;lb=1;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **B2b** | day | Q32 | `contested` | theory, W, low; deciding check graded PARTIAL | serious: B2b PARTIAL, `unknown`; the audit's first script was wrong and review caught it (ST#34) | not serious: simulated N_e within 2.2% of Wright's formula at four V_k (R4) | serious: `mw` 1: iid offspring variance; "Inputs (human V_k, G window) not tested" (R4) | not serious: the flip is stated: N_e/N = 1e-3 needs V_k about 4,000 (R4) | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C moderate · FR moderate | A sourced human V_k settles which side of the stated value the lineage is on | `id=B2b;party=day;lb=1;v=contested;b=T;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **B3** | day | Z18429937 ¶6 (abstract) | `contradicted` | theory, W, low; deciding check graded PARTIAL | serious: B3b / B3c PARTIAL, `single-commit`; B3 family PARTIAL, `unknown`, grid of inputs the audit's own with no base-rate control (ST#10, ST#39, ST-11) | serious: fwdpy11 missed two rows of B3b; the comment mixes a withdrawn leg, a simulated leg and a per-site leg, with "median 25" pending (CF; ST#10) | very serious: `mw` 2: exchangeable offspring as a description of real populations is the premise Day disputes (AS 3.10). `rd` 1: one verdict word over five different values | not serious: simulated effect -2% to +38% at human-like values against the 26% drop that 0.743 needs | undetected | none | against-claim | M0 **very-low** · M-D very-low · M-C very-low · FR very-low | Give each k/mu value its own external field; the per-site 32.3 leg rests on measured event counts and would rate higher alone | `id=B3;party=day;lb=1;v=contradicted;b=T;k=W;st=PARTIAL;rob=1;inc=1;mw=2;sp=0;rd=1;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **B3a** | day | Z18525547 eq. 1 | `contradicted` | theory, W, low; deciding check graded PARTIAL | not serious: P_fix = 1/(2N) proved for exchangeable models (P1) and reproduced in a second engine (ST#4, ST#35) | serious: the verdict leans on Day's concession, and his later text is "in tension with the concession" (AS 5.5) | serious: `mw` 1: an identity of a class of models; the non-exchangeable case is untested (AS, B7 row) | not serious: Day's 1/(2N_e) is 1.5 to 7x from the simulated value | undetected | none: lower bound 1.5x, under the factor 2 | against-claim | M0 **very-low** · M-D very-low · M-C moderate · FR moderate | A reproduction law with covariance between breeding success and genotype at sourced human values, giving P_fix within 25% of 1/(2N) (the rebuttal condition AS 9.1 drafts) | `id=B3a;party=day;lb=1;v=contradicted;b=T;k=W;st=PARTIAL;rob=0;inc=1;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **B3g** | day | Day blog 2026-08-27 ¶2 | `supported` | theory, F, high; deciding check graded PARTIAL | not serious: the statement is about the derivation; eleven quotes machine-checked and the identity proved (ST#41, ST#27) | serious: two unsettled readings recorded: the concession, and Day's later "false for any real population" (AS compact table) | not serious: formal claim: what Kimura's derivation needs | not serious: exact | undetected | none | for-claim | M0 **moderate** · M-D very-low · M-C moderate · FR moderate | Day's own answer on which of the two statements stands (right of reply, O-2) | `id=B3g;party=day;lb=1;v=supported;b=T;k=F;st=PARTIAL;rob=0;inc=1;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **B4a** | literature | CSAC 2005, "Genome-wide rates" | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: B4a PARTIAL, `single-commit`; the fit has a free ancestral N_e (ST#9) | serious: "overshoots 1.23% by ~25% at HCB node; half at Ne 1e4" (CF): the anchor test partly fails | not serious: this row is the comparison with the observed divergence | serious: "(mu, T, Ne_anc) underdetermined; Yoo mu unrecorded" (CF) | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR very-low | Record Yoo's mu and fix T and N_e,anc from sources before the comparison (a registered re-run), which removes the imprecision downgrade | `id=B4a;party=literature;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=1;mw=0;sp=0;rd=0;imp=1;sel=0;ur=0;upf=0;dir=cond` |
| **B5** | critic | GG-03 | `contested` | theory, W, low; deciding check graded PARTIAL | not serious: identity proved (P1); engine baseline reproduces k = U (ST#1, ST#27) | serious: the independent engine returned k/U counts 0.7 to 36% low, unlocalised, follow-up not run (ST#35, ST-06) | serious: `mw` 1: "exact at steady state"; "The critics' stated totals assume stationarity" (CF; AS compact table) | not serious: exact | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C moderate · FR moderate | Localise the fwdpy11 discrepancy (roadmap, ST-06 follow-up): removes the inconsistency downgrade | `id=B5;party=critic;lb=1;v=contested;b=T;k=W;st=PARTIAL;rob=0;inc=1;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **B6** | critic | MF-05 | `supported` | simulation, W, low; deciding check graded BENT | very serious: "full pipe gives k = mu ... (forward sim)": a simulation started full returns the full-start result; BENT for the world claim (ST§6; AS compact table) | serious: B4a's anchor overshoots by about 25%; fwdpy11 did not reproduce the B1 counts; Day's concession on the pipe reversed twice (CF of B4a; ST#3; AS 5.5) | serious: `mw` 1: Mansfield states the full pipe as an assumption with no ancestral N_e; the only anchor is CSAC's polymorphic share through B4a | not serious: the claim is qualitative | undetected | none | for-claim | M0 **very-low** · M-D very-low · M-C very-low · FR very-low | The ancestral-polymorphism count on held alignments (roadmap A20), with Scally 2012 as the published number to reproduce: basis becomes data | `id=B6;party=critic;lb=1;v=supported;b=S;k=W;st=BENT;rob=2;inc=1;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **B7** | critic | Z22129121 §The Third (quoting Maruyama) | `supported` | theory, W, low; deciding check graded PARTIAL | not serious: proved (P1) and reproduced in two engines (ST#4, ST#35) | not serious: no discordant result on 1/(2N) | serious: `mw` 1: no comment at the field; "Provisional (pending B3b)"; non-exchangeable case noted as untested (AS compact table) | not serious: exact | undetected | none | for-claim | M0 **very-low** · M-D very-low · M-C high · FR high | As for B3a. Read as a statement about the model it is already high (column FR) | `id=B7;party=critic;lb=1;v=supported;b=T;k=W;st=PARTIAL;rob=0;inc=0;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **C2** | day | Z18203514 abstract | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: C2 PARTIAL, `single-commit`; Day's Table 1 not reproduced with the stand-in life tables (ST#15) | not serious: the rule went both ways as registered: d·s exact for hazard-scale s, factor 1 for per-generation s | very serious: `mw` 1: age-structured simulation, not anchored. `sp` 1: stand-in life tables, not Day's | not serious: the condition is binary (which s scale) | undetected: the unretrieved s scale of the cited aDNA papers is the stated condition itself, so it is not counted again | none | none: conditional | M0 **very-low** · M-D very-low · M-C low · FR moderate | Retrieve which s scale the cited aDNA papers use (CF): that resolves the condition and gives the row a direction | `id=C2;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=1;rd=0;imp=0;sel=0;ur=1;upf=0;dir=cond` |
| **C2a** | day | Q20 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: C2 PARTIAL, `single-commit`; Day's Table 1 not reproduced with the stand-in life tables (ST#15) | not serious: the rule went both ways as registered: d·s exact for hazard-scale s, factor 1 for per-generation s | very serious: `mw` 1: age-structured simulation, not anchored. `sp` 1: stand-in life tables, not Day's | not serious: the condition is binary (which s scale) | undetected: the unretrieved s scale of the cited aDNA papers is the stated condition itself, so it is not counted again | none | none: conditional | M0 **very-low** · M-D very-low · M-C low · FR moderate | Retrieve which s scale the cited aDNA papers use (CF): that resolves the condition and gives the row a direction | `id=C2a;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=1;rd=0;imp=0;sel=0;ur=1;upf=0;dir=cond` |
| **F** | day | Day blog 2026-10-01 ¶6 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: no comment at the field; from the Check: F2 / A-sim PARTIAL, `single-commit` (CK; ST#16) | not serious: numpy and fwdpy11 agree on the interference runs | very serious: `mw` 1: "interference bounds it only with linkage" is a model result. `sp` 1: soft selection, N = 1000, 272 loci (CK) | not serious | suspected: hard selection with linkage untested (CF of F2) | none | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR moderate | As for F2: the hard-selection-with-linkage run at a human-length map | `id=F;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=1;rd=0;imp=0;sel=1;ur=0;upf=0;dir=cond` |
| **F1** | critic | MF-04 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: no comment at the field; F1 PARTIAL, `single-commit` (ST#6) | not serious: rate 0.3972 ± 0.0018 against 0.3960 (CK) | very serious: `mw` 2: loci independent by construction, which is what Day's capacity argument disputes. `sp` 1: "unrealistic regime"; "feasibility is untested (F2)" (CK) | not serious | suspected: as for F2 | none | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR moderate | As for F2. Read as logic (a counterexample to a bound) it stands (column FR) | `id=F1;party=critic;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=2;sp=1;rd=0;imp=0;sel=1;ur=0;upf=0;dir=cond` |
| **F2** | day | Q25 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: F2 / A-sim PARTIAL, `single-commit`; GAP-04 WEAK (ST#16, ST#19) | not serious: two engines and W&B agree within 6 to 10% (AS compact table) | very serious: `mw` 1: not anchored on the lineage. `sp` 1: soft selection, active loci to 272; "hard selection with linkage untested" (CF) | serious: the binding share is a range, 13 to 27% (CF) | suspected: "tight linkage supports Day" (CF): the untested cell could move the condition | 1 present: monotone trend of the interference ratio with map length, clonal 0.09 to free 0.975 (CK of F). Not applied: downgraded | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR low | The hard-selection-with-linkage run at a human-length map (roadmap A21) | `id=F2;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=1;rd=0;imp=1;sel=1;ur=0;upf=1;dir=cond` |
| **F3a** | day | Day blog 2026-10-01 ¶15 | `contested` | theory, W, low; deciding check graded SEVERE | not serious: the latency formula was tested against the exact integral and a second engine (B0.4, SEVERE; ST#2) | not serious | serious: `mw` 1: single-locus diffusion; "no sourced human beneficial mean s is in the repo" (CF) | not serious: flip stated: latency moves more than 25% for s outside 0.0008 to 0.00133 (CF) | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C high · FR high | A sourced human mean beneficial s resolves the condition | `id=F3a;party=day;lb=1;v=contested;b=T;k=W;st=SEVERE;rob=0;inc=0;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **FM10** | day | Q171 | `contested` | data, W, high; deciding check graded PARTIAL | not serious: FM PARTIAL, `blind`, real T2T alignment, numeric thresholds for each side (ST#44). The audit-defined statistic is counted once, under indirectness | not serious: one Day-side cell, traced to one orthologous centromeric-transition window (CF) | very serious: `rd` 2: the data address a premise (a human-specific mesa signal), "not a verdict on FM10" (CF); FM10 says neither selection nor drift is viable. The statistic is the audit's; Day's is undefined | not serious: "every pre-registered discriminating cell (P3, P4, P5, P7) falls on the critics' side" (CF) | undetected: FMnull, registered and not run, is the cure for the wording gap and is not counted twice | none | against-claim | M0 **low** · M-D low · M-C very-low · FR - | FMnull's reproduction gate (roadmap A4): shows whether the audit's statistic is Day's | `id=FM10;party=day;lb=1;v=contested;b=D;k=W;st=PARTIAL;rob=0;inc=0;mw=0;sp=0;rd=2;imp=0;sel=0;ur=1;upf=0;dir=against` |
| **H** | day | Q47 | `contested` | simulation, W, low; deciding check graded PARTIAL | not serious: H8 / H5 PARTIAL, `blind`, numeric criteria for both sides, misses printed (ST#37). The audit's mapping s_max·d = ln R is counted under `mw` | serious: registered predictions at K = 64,000: K1' missed, K2' indeterminate with a bracket of 294 to 368 that straddles 300 (CF) | very serious: `mw` 1: no observation of the lineage is reproduced; "no sourced net hominid R" (AS 3.15). `sp` 1: K to 64,000; hard and soft selection as model switches | serious: the flip moves with K and the survival horizon and no K trend was found (CF) | undetected | none: budget rises with ln R, but that is the regulation rule, not a finding (ST#37) | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR low | A sourced net reproductive excess R and hard-selection share for hominids would place the lineage on the map | `id=H;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=0;inc=1;mw=1;sp=1;rd=0;imp=1;sel=0;ur=1;upf=0;dir=cond` |
| **H5** | ally | Hössjer PDF 2026-09-14 | `contested` | simulation, W, low; deciding check graded PARTIAL | not serious: H8 / H5 PARTIAL, `blind`, numeric criteria for both sides, misses printed (ST#37). The audit's mapping s_max·d = ln R is counted under `mw` | serious: registered predictions at K = 64,000: K1' missed, K2' indeterminate with a bracket of 294 to 368 that straddles 300 (CF) | very serious: `mw` 1: no observation of the lineage is reproduced; "no sourced net hominid R" (AS 3.15). `sp` 1: K to 64,000; hard and soft selection as model switches | serious: the flip moves with K and the survival horizon and no K trend was found (CF) | undetected | none: budget rises with ln R, but that is the regulation rule, not a finding (ST#37) | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR low | A sourced net reproductive excess R and hard-selection share for hominids would place the lineage on the map | `id=H5;party=ally;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=0;inc=1;mw=1;sp=1;rd=0;imp=1;sel=0;ur=1;upf=0;dir=cond` |
| **H8** | day | Z19984826 §3.3 | `contested` | simulation, W, low; deciding check graded PARTIAL | not serious: H8 / H5 PARTIAL, `blind`, numeric criteria for both sides, misses printed (ST#37). The audit's mapping s_max·d = ln R is counted under `mw` | serious: registered predictions at K = 64,000: K1' missed, K2' indeterminate with a bracket of 294 to 368 that straddles 300 (CF) | very serious: `mw` 1: no observation of the lineage is reproduced; "no sourced net hominid R" (AS 3.15). `sp` 1: K to 64,000; hard and soft selection as model switches | serious: the flip moves with K and the survival horizon and no K trend was found (CF) | undetected | none: budget rises with ln R, but that is the regulation rule, not a finding (ST#37) | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR low | A sourced net reproductive excess R and hard-selection share for hominids would place the lineage on the map | `id=H8;party=day;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=0;inc=1;mw=1;sp=1;rd=0;imp=1;sel=0;ur=1;upf=0;dir=cond` |
| **H1** | day | Q65 | `supported` | theory, F, high; deciding check graded SEVERE | not serious: true by the definition of the cost; neutral k = U reproduced in the engine baseline (ST#1; AS 5.2) | not serious | not serious: formal claim: what Term 3 bounds | not serious: exact | undetected | none | for-claim | M0 **high** · M-D very-low · M-C high · FR high | Already high as a formal statement. It is in the external column by a category leak (MA-15) | `id=H1;party=day;lb=1;v=supported;b=T;k=F;st=SEVERE;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **H2** | literature | Nunney 2003, abstract | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: "EXPLORATORY reconstruction ... adjusted twice after seeing results" (AS compact table) | serious: M-dependence reproduced; "absolute T and soft-selection elimination not reproduced" (CF) | serious: `mw` 1: the audit's reconstruction of Nunney's model; "human M unsourced" (CF) | not serious: the condition is M | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C low · FR low | A reconstruction registered before it is run, compared with Nunney's printed tables | `id=H2;party=literature;lb=1;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=1;mw=1;sp=0;rd=0;imp=0;sel=0;ur=1;upf=0;dir=cond` |
| **ROOT-FM** | day | Q164 | `contested` | data, W, high; deciding check graded PARTIAL | not serious: FM PARTIAL, `blind`, real T2T alignment (ST#44) | not serious: description and inference are sorted by a stated distinction: overdispersion is real in every ape lineage; a human-specific excess is not found (CF; ST 7.1) | serious: `rd` 1: the dispersion statistic and window are the audit's; "No code, mesa coordinates, window size or dispersion statistic released by Day" (CF) | not serious | undetected: FMnull counted once, under indirectness | none | none: mixed | M0 **moderate** · M-D moderate · M-C low · FR - | FMnull's reproduction gate (roadmap A4) | `id=ROOT-FM;party=day;lb=1;v=contested;b=D;k=W;st=PARTIAL;rob=0;inc=0;mw=0;sp=0;rd=1;imp=0;sel=0;ur=1;upf=0;dir=mixed` |

### 4.2 Sample (30)

| Claim | Party | Quote | Verdict | Basis, kind, start | Risk of bias | Inconsistency | Indirectness | Imprecision | Selection | Upgrade factors | Direction | Certainty | What would raise it one level | Code |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **A2** | day | Q13 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: A-sim PARTIAL, `single-commit` (ST#16) | serious: G_f moves about threefold with the counting rule (1,322 against 1,587 strict; ST#32) | very serious: `mw` 1: clonal fixed-s model fitted to the number it is asked to support. `rd` 1: the evidence is for an order of magnitude; the claim is 1,322 | very serious: "U_b spans 3 orders of magnitude"; N_e 3.3e7 is an "unsourced assumption" (R4) | undetected | none | for-claim | M0 **very-low** · M-D very-low · M-C very-low · FR very-low | Cite the recount of the LTEE papers' own tables (E5 / E6, L6) at this node: basis becomes data | `id=A2;party=day;lb=0;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=1;mw=1;sp=0;rd=1;imp=2;sel=0;ur=1;upf=0;dir=for` |
| **A3z** | day | Q179 | `contested` | data, W, high; deciding check graded WEAK | serious: the events leg is GAP-07t (SEVERE); the base-pair leg is L7 (WEAK, `criterion-only`): the route to 410 M is unconfirmed (ST#46, ST#52) | not serious: the two readings are sorted by unit: 410 M is close as base pairs (404 M from Yoo's SI) and 8.5x too high as events (CF) | not serious | not serious: 8.5x between the units | undetected | none | none: conditional | M0 **moderate** · M-D moderate · M-C moderate · FR - | Day's statement of which unit "differences" means (O-2); on the events reading the row is `against` on SEVERE data | `id=A3z;party=day;lb=0;v=contested;b=D;k=W;st=WEAK;rob=1;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **A4** | day | Q20 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: C2 PARTIAL, `single-commit` (ST#15) | not serious: d·s exact for hazard-scale s (within 1.5%): "a point for Day" (R4) | very serious: `mw` 1, `sp` 1: as C2 | not serious | undetected: the unretrieved s scale is the condition | none | none: conditional | M0 **very-low** · M-D very-low · M-C low · FR moderate | As for C2 | `id=A4;party=day;lb=0;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=1;rd=0;imp=0;sel=0;ur=1;upf=0;dir=cond` |
| **A4f** | critic | GG-21 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; Check: "None beyond R4 C2." (a pointer, no stated result) | State what R4 C2 shows for each of Hancock's three clauses, or `pending` | `id=A4f;party=critic;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **A4g** | day | Z18166234 (STC paper) | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; Check: "None." The only argument recorded sits under the internal field (proposal c) | A statement of which published fixation models assume non-overlap, with sources; or `pending` | `id=A4g;party=day;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **B2c** | day | Z22129121 §The Second | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; Check is arithmetic on Day's own inputs (internal) | Sourced N_e and G for the stated window; or `pending` | `id=B2c;party=day;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **B4d** | day | Z22903977 §5 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; "Script: none." | How the cited split dates were obtained (fossil, pedigree rate, or k = mu), from the dating papers; or `pending` | `id=B4d;party=day;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **B4e** | critic | MC-12 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; "Script: none." | As for B4d: the two nodes are one question | `id=B4e;party=critic;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **D13** | ally | Dembski 2022-08-26 §3 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Comment is a bare `#`; Check: "None." An evaluative claim | `untestable` with a reason code, or `pending` | `id=D13;party=ally;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **D15** | ally | HO-12 | `contested` | simulation, W, low; deciding check graded SEVERE | not serious: D15 SEVERE, `blind`: sweep against an analytic chain (ST#36) | not serious: p9 = 0 in all 96 in-scope cells | serious: `mw` 1: "those premises are unsourced on both sides"; "A sensitivity of this audit's grid, not a sourced rebuttal" (CF) | not serious: flip conditions stated: beneficial intermediates, kmult >= 10, a non-specific set of about 1,000 genes or more (CF) | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C high · FR high | Sourced values for target specificity and the fitness of intermediates place the lineage on the map | `id=D15;party=ally;lb=0;v=contested;b=S;k=W;st=SEVERE;rob=0;inc=0;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **D3** | literature | Eden 1967, in Moorhead and Kaplan | `contested` | data, W, high; deciding check graded PARTIAL | not serious: D1 PARTIAL, `blind`; both sides' outcomes reachable (ST#24) | serious: eight sub-predictions failed; alternatives per change "turn on the definition of equivalence" (ST#24) | serious: `sp` 1: RNA folding and one protein domain stand in for protein space. `rd` 1: Eden's count is exact; the verdict is on its bearing on search | not serious | undetected | none | none: conditional | M0 **low** · M-D low · M-C very-low · FR - | The queued multi-mutant decay follow-up (roadmap A9) on more than one protein | `id=D3;party=literature;lb=0;v=contested;b=D;k=W;st=PARTIAL;rob=0;inc=1;mw=0;sp=1;rd=1;imp=0;sel=0;ur=1;upf=0;dir=cond` |
| **D4** | literature | Ulam 1967, same volume | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: "serial assumption not tested"; the shared-pool table is exploratory (CF; R4) | not serious | very serious: `mw` 1: one-gene shared-pool model. `sp` 1: proxies as D3 | serious: P(success) runs from 0.999 to 4e-20 across k and s, with s unsourced (R4) | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C very-low · FR low | A sourced range for s and for the number of needed changes | `id=D4;party=literature;lb=0;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=1;rd=0;imp=1;sel=0;ur=1;upf=0;dir=cond` |
| **D9** | day | Day blog 2026-09-12 ¶9-12 | `contested` | simulation, F, high; deciding check graded SEVERE | serious: conditional fixation time rests on B0.4 (SEVERE); the parallel-loci figure is an "Exploratory scratch run ... not committed" (CK; ST#2) | not serious | not serious: formal claim: a stipulated population of weasels with stated N and s | not serious: 8,500 against 20,000 generations per letter; about 13,000 against 540,000 for the phrase (CF) | undetected | none | against-claim | M0 **moderate** · M-D very-low · M-C moderate · FR moderate | Commit the parallel-loci run as a registered check | `id=D9;party=day;lb=0;v=contested;b=S;k=F;st=SEVERE;rob=1;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **G2g** | day | Day blog 2026-10-01 ¶24 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; the R4 G1 text is about the logic of p^n (internal) | The book's Appendix A at first hand (O-1), then an external statement; or `pending` | `id=G2g;party=day;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **Ga** | day | Q11 | `contested` | simulation, W, low; deciding check graded PARTIAL | serious: G1 PARTIAL, `single-commit` (ST#18) | not serious: independence holds with free recombination and fails with linkage, in Day's stated direction (R4): sorted by regime | very serious: `mw` 1: multiplicative-fitness model. `rd` 1: the lean ("prices pre-specified arisings, not the event required") is a reading of which event the number prices | not serious | undetected | none | against-claim | M0 **very-low** · M-D very-low · M-C low · FR low | Tie the specific-versus-any reading to Day's own sentences (right of reply), which removes the wording downgrade | `id=Ga;party=day;lb=0;v=contested;b=S;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=0;rd=1;imp=0;sel=0;ur=1;upf=0;dir=against` |
| **ROOT-K** | ally | KE-01 | `contested` | theory, W, low; deciding check graded none | serious: inline arithmetic, no registered check, no review; status `extracted` (CK) | not serious | serious: `mw` 1: "only reaches the claim if the bacterial rate is a fixed ceiling" (CF), which is A2e | not serious | undetected | none | none: conditional | M0 **very-low** · M-D very-low · M-C moderate · FR moderate | Follows A2e | `id=ROOT-K;party=ally;lb=0;v=contested;b=T;k=W;st=none;rob=1;inc=0;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=cond` |
| **ROOT-PG** | critic | GG-32 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; the R4 text concerns an RH tag. A track-record argument | A stated standard for surviving the record; or `untestable` with a reason code | `id=ROOT-PG;party=critic;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **F1b** | critic | MC-08 | `supported` | simulation, W, low; deciding check graded BENT | very serious: F1b BENT: Little's law on the same sample is an identity; independence is assumed (ST#29) | not serious | very serious: `mw` 2: no interference by construction, the point in dispute. `sp` 1: "beneficial s = 0.01 only"; "feasibility at human scale untouched" (CF) | not serious | undetected | none | for-claim | M0 **very-low** · M-D very-low · M-C very-low · FR low | Cite the measured share of sites still polymorphic (GAP-07c, 15.6%): many variants in transit at once is an observation the audit already made | `id=F1b;party=critic;lb=0;v=supported;b=S;k=W;st=BENT;rob=2;inc=0;mw=2;sp=1;rd=0;imp=0;sel=0;ur=1;upf=0;dir=for` |
| **H6** | critic | Nesslig20 2026-10-05, post 1 | `supported` | theory, F, high; deciding check graded SEVERE | not serious: by the definition of the cost; engine baseline z = +0.13 / -0.64 (R4) | not serious | not serious: formal claim: what the cost applies to | not serious: exact | undetected | none | for-claim | M0 **high** · M-D very-low · M-C high · FR high | Already high as a formal statement | `id=H6;party=critic;lb=0;v=supported;b=T;k=F;st=SEVERE;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **A1** | day | Q18 | `supported` | literature (model estimate), W, low; deciding check graded BENT | not serious: three independent published sources (Yoo, Langergraber, Scally: A1a); GAP-06 is arithmetic on them (ST#45) | serious: published split dates run from 5.5-6.3 My to "at least 7-8 My" (A1a): at 25 y that is 220,000 to 320,000, across the 25% edge | serious: `mw` 1: split dates are clock-model estimates; how each was calibrated is not recorded | not serious | undetected: the spread is counted once, under inconsistency | none | for-claim | M0 **very-low** · M-D very-low · M-C moderate · FR moderate | Record the calibration behind each published date (the question B4d and B4e raise) | `id=A1;party=day;lb=0;v=supported;b=Lm;k=W;st=BENT;rob=0;inc=1;mw=1;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **A6a** | day | Z18441321 §3.1 | `supported` | literature (measurement), W, high; deciding check graded WEAK | serious: one published scan (Yoo 2025, SweepFinder2), not appraised or reproduced; GAP-02 is "Arithmetic consequence of the model, not a test" (R4; ST#19) | not serious | not serious: the comment scopes it as Day's own conditional does | not serious: expected 1.6e4 even with a tenfold smaller window, against 30 candidates (R4) | undetected | none | for-claim | M0 **moderate** · M-D very-low · M-C moderate · FR - | A second published sweep scan in bonobos, or the power of the scan from its own paper | `id=A6a;party=day;lb=0;v=supported;b=L;k=W;st=WEAK;rob=1;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **DN5** | literature | Q173 note (Day's relay of CSAC 2005) | `supported` | data, W, high; deciding check graded PARTIAL | not serious: L1 on real alignments reproduces the published value; graded SEVERE for this number (ST 7.2) | not serious: 0.207 and 0.200 against 0.23 | serious: `sp` 1: "in kind": Ensembl one2one genes on hg38, not CSAC's gene set. `rd` 1: `sourcing: secondhand`; CSAC 2005 not yet fetched for fidelity (CF) | not serious | undetected | none | for-claim | M0 **moderate** · M-D moderate · M-C moderate · FR - | Fetch CSAC 2005 and an independent ML estimate (CF), which removes the secondhand tag | `id=DN5;party=literature;lb=0;v=supported;b=D;k=W;st=PARTIAL;rob=0;inc=0;mw=0;sp=1;rd=1;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **A1b** | literature | Langergraber 2012, Results | `supported` | literature (measurement), W, high; deciding check graded none | serious: one published field study, not appraised; "No script."; status `extracted` (CK) | not serious | not serious | not serious: 24.3 and 24.9 y | undetected | none | for-claim | M0 **moderate** · M-D very-low · M-C moderate · FR - | A second source for chimpanzee generation time | `id=A1b;party=literature;lb=0;v=supported;b=L;k=W;st=none;rob=1;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=for` |
| **DN1** | day | Q172 | `contradicted` | data, W, high; deciding check graded PARTIAL | serious: L1 PARTIAL, `unknown` (333 s between registration and result) (ST#50, methods page) | not serious: every filter combination 0.23 to 0.28 (R4) | serious: `sp` 1: hg38 / panTro5, not Day's T2T and GENCODE v46; "conditional on L1b" (CF, MA-12) | not serious: 0.27 against 0.80 | undetected: the unrun L1b is the cure for `sp` and is counted once | none | against-claim | M0 **low** · M-D low · M-C low · FR - | Run L1b (roadmap A2) | `id=DN1;party=day;lb=0;v=contradicted;b=D;k=W;st=PARTIAL;rob=1;inc=0;mw=0;sp=1;rd=0;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **DN2** | day | Q175 | `contradicted` | data, W, high; deciding check graded PARTIAL | serious: as DN1 | serious: two readings named in the comment: contradicted "as a statement about human-chimp coding sequence", and "As a report of his pipeline it is plausible" (CF) | serious: `sp` 1: as DN1. `rd` 1: the verdict takes the first reading | not serious | undetected | none | against-claim | M0 **very-low** · M-D very-low · M-C very-low · FR - | Run L1b; ask which statement Day meant (O-2) | `id=DN2;party=day;lb=0;v=contradicted;b=D;k=W;st=PARTIAL;rob=1;inc=1;mw=0;sp=1;rd=1;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **B5c** | critic | GG-04 | `contradicted` | theory, W, low; deciding check graded PARTIAL | serious: B4a PARTIAL, `single-commit`; X1 PARTIAL, `unknown`, materiality rule fixed after the slips were known (ST#9, ST#25) | not serious | very serious: `mw` 1: the split (19 M post-split, 15 M ancestral) is B4a's model. `rd` 1: contradicted "as an SNV match"; "event-basis reading untested" (CF) | not serious: a factor of two | undetected | none | against-claim | M0 **very-low** · M-D very-low · M-C low · FR low | Score the event-basis reading | `id=B5c;party=critic;lb=0;v=contradicted;b=T;k=W;st=PARTIAL;rob=1;inc=0;mw=1;sp=0;rd=1;imp=0;sel=0;ur=0;upf=0;dir=against` |
| **D7b** | day | Day blog 2024-04-25 ¶6-8 | `untestable` | none recorded | – | – | – | – | – | – | n/a | **NR (not rateable)**. "a biological quantity nobody in the corpus measures" (CF): unmeasured in the corpus, which is not the same as untestable | A reason code on `untestable` (not measured, or not measurable) | `id=D7b;party=day;lb=0;v=untestable;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=na` |
| **ROOT-COV** | critic | GG-35 | `untestable` | none recorded | – | – | – | – | – | – | n/a | **NR (not rateable)**. Empty comment; a conceptual claim about what selection is | A reason code on `untestable` | `id=ROOT-COV;party=critic;lb=0;v=untestable;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=na` |
| **B5f** | critic | RE-06 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; the R4 X1 text is internal and fidelity. B5b and GAP-06 bear on it and are not cited here | Cite B5b (supply 0.5 to 0.66x of the requirement at 252,000 generations) at the node | `id=B5f;party=critic;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |
| **G2f** | critic | BO-02 | `contested` | none recorded | – | – | – | – | – | – | none: no evidence | **NE (not rated)**. Empty comment; R4 G1 is about the logic | An external statement, or `pending` | `id=G2f;party=critic;lb=0;v=contested;b=N;k=W;st=none;rob=0;inc=0;mw=0;sp=0;rd=0;imp=0;sel=0;ur=0;upf=0;dir=ne` |

---

## 5. Aggregates

All counts are printed by `research/tools/grade_certainty.py count` from the code column. One rater. The 28 load-bearing rows are a census; the 30 sample rows over-represent `supported`, `contradicted` and `untestable` by design (3.2), so the "All" lines are counts of what was rated and **not** estimates for the 172. Estimates for the whole column are given only in 5.5 and 5.6, with their basis. No distribution here should be averaged into one grade (2.9, point 4).

### 5.1 By verdict value (M0)

| | high | moderate | low | very low | NE | NR | Total |
|---|---|---|---|---|---|---|---|
| `supported` | 2 | 4 | 0 | 4 | 0 | 0 | 10 |
| `contradicted` | 0 | 0 | 1 | 6 | 0 | 0 | 7 |
| `contested` | 1 | 3 | 2 | 22 | 11 | 0 | 39 |
| `untestable` | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| **All rated rows** | 3 | 7 | 3 | 32 | 11 | 2 | 58 |

45 rows carry a level; 11 have no recorded evidence (NE); 2 are `untestable` and outside the instrument (NR). **32 of the 45 are at the floor.** The three at high are A3 (Day's required count, on data), H1 and H6 (the scope of Haldane's cost, true by definition). No `contradicted` verdict rated here is above low.

### 5.2 By load-bearing status (M0)

| | high | moderate | low | very low | NE | NR | Total |
|---|---|---|---|---|---|---|---|
| Load-bearing, `supported` | 1 | 1 | 0 | 2 | 0 | 0 | 4 |
| Load-bearing, `contradicted` | 0 | 0 | 0 | 4 | 0 | 0 | 4 |
| Load-bearing, `contested` | 1 | 1 | 1 | 16 | 1 | 0 | 20 |
| **Load-bearing, all** | **2** | **2** | **1** | **22** | **1** | **0** | **28** |
| Sample, `supported` | 1 | 3 | 0 | 2 | 0 | 0 | 6 |
| Sample, `contradicted` | 0 | 0 | 1 | 2 | 0 | 0 | 3 |
| Sample, `contested` | 0 | 2 | 1 | 6 | 10 | 0 | 19 |
| Sample, `untestable` | 0 | 0 | 0 | 0 | 0 | 2 | 2 |
| **Sample, all** | **1** | **5** | **2** | **10** | **10** | **2** | **30** |

The load-bearing nodes are better documented (1 NE of 28 against 10 of 30) and no better evidenced as statements about the world: 22 of their 27 rated rows are at the floor, against 10 of 18 in the sample. They are where the audit ran simulations, and under M0 a simulation that is not anchored on an observation of the lineage cannot rise above very low.

### 5.3 By party (M0, with the two alternatives)

| Party of the claim | high | moderate | low | very low | NE | NR | Total |
|---|---|---|---|---|---|---|---|
| Day, M0 | 2 | 5 | 2 | 19 | 5 | 1 | 34 |
| Day, M-D | 1 | 2 | 2 | 23 | 5 | 1 | 34 |
| Day, M-C | 4 | 7 | 6 | 11 | 5 | 1 | 34 |
| Allies, M0 | 0 | 0 | 0 | 3 | 1 | 0 | 4 |
| Allies, M-D | 0 | 0 | 0 | 3 | 1 | 0 | 4 |
| Allies, M-C | 1 | 1 | 0 | 1 | 1 | 0 | 4 |
| Critics, M0 | 1 | 0 | 0 | 6 | 5 | 1 | 13 |
| Critics, M-D | 0 | 0 | 0 | 7 | 5 | 1 | 13 |
| Critics, M-C | 2 | 1 | 1 | 3 | 5 | 1 | 13 |
| Literature and audit-raised, M0 | 0 | 2 | 1 | 4 | 0 | 0 | 7 |
| Literature and audit-raised, M-D | 0 | 1 | 1 | 5 | 0 | 0 | 7 |
| Literature and audit-raised, M-C | 0 | 2 | 2 | 3 | 0 | 0 | 7 |

This is the certainty of the audit's verdict *on* a party's claim. It is not a rating of the party, and the rows are not comparable across parties: Day authored 34 of the 58, and a verdict against a claim and a verdict for it are pooled. What it does show: the critics' claims have the highest share of rows with no recorded evidence (5 of 13, against 5 of 34 for Day), which repeats AR-11 and ST-04 from another side, and every critic row but one is at the floor or unrated under M0.

### 5.4 By evidence basis (M0)

| Basis, kind | high | moderate | low | very low | Total rated |
|---|---|---|---|---|---|
| `D` data | 1 | 3 | 3 | 1 | 8 |
| `L` literature, measurement | 0 | 2 | 0 | 0 | 2 |
| `Lm` literature, model estimate | 0 | 0 | 0 | 3 | 3 |
| `S` simulation, kind `W` | 0 | 0 | 0 | 19 | 19 |
| `S` simulation, kind `F` | 0 | 1 | 0 | 0 | 1 |
| `T` theory, kind `W` | 0 | 0 | 0 | 9 | 9 |
| `T` theory, kind `F` | 2 | 1 | 0 | 0 | 3 |

Under M0 the level is very nearly a function of the basis: every one of the 31 model-based world rows (`Lm`, `S`, `T`) is very low, and 9 of the 10 observation-based rows are above it (the exception is DN2, a data verdict taken on one of two recorded readings). Four rows are of kind `F`: B3g, H1, H6 and D9. They rate moderate or high because they assert what a model or a definition implies, and by the audit's own definition of the external column they do not belong in it (MA-15).

### 5.5 What `contested` hides (39 rows)

| Class | Rows | Ids |
|---|---|---|
| **Lean one way, moderate or high** (under-stated) | 2 | A3 (for Day's count, high); D9 (against, moderate) |
| **Lean one way, low or very low** | 3 | FM10 (against, low); A2 (for, very low); Ga (against, very low) |
| **Open as described, moderate or high** | 2 | ROOT-FM (mixed, moderate); A3z (conditional on the unit, moderate) |
| **Open as described, low or very low** | 21 | A, B, B1, B2b, B4a, B5, C2, C2a, F, F1, F2, F3a, H, H2, H5, H8 (load-bearing); A4, D15, D3, D4, ROOT-K (sample) |
| **No evidence recorded** | 11 | B2 (load-bearing); A4f, A4g, B2c, B4d, B4e, D13, G2g, ROOT-PG, B5f, G2f (sample) |

Directions: 22 conditional, 1 mixed, 3 against the claim, 2 for it, 11 with nothing recorded.

**The 21 "open, low or very low" rows are where the instrument stops discriminating.** All but D3 are model-based, and under M0 a conditional worked out inside a model is very low as a statement about the world whatever the quality of the work. Column FR, the certainty of the in-model statement alone (note N4), spreads the same rows out:

| FR | Open rows | Ids |
|---|---|---|
| high | 3 | B1, F3a, D15 |
| moderate | 8 | B2b, B5, C2, C2a, F, F1, A4, ROOT-K |
| low | 7 | A, F2, H, H2, H5, H8, D4 |
| very low | 2 | B, B4a |
| not applicable (data-based) | 3 | D3, ROOT-FM, A3z |

So the answer to "how many `contested` are really a low-certainty lean, a moderate-certainty genuine conditional, or nothing either way" depends on what a conditional is taken to be about. As statements about the world: 5 lean (2 of them moderate or high), 23 open (2 of them moderate), 11 nothing. As statements of what the models imply: 11 of the 20 model-based open rows are moderate or high, which is what a reader would mean by "genuinely conditional, and known to be".

**Estimate for all 114 `contested`.** The 20 load-bearing rows are a census. The 17 forced sample rows are the non-load-bearing part of a simple random sample of the 114, so they stand for the other 94 (the two extra critic rows, both NE, are left out of the estimate).

| Class | Load-bearing (20, census) | Other (17 of 94 sampled) | Estimate for 114 |
|---|---|---|---|
| No evidence recorded | 1 | 8 of 17 | about 45 (39%) |
| Lean one way | 2 | 3 of 17 | about 19 (16%) |
| Open (conditional or mixed) | 17 | 6 of 17 | about 50 (44%) |

With 17 rows the middle column carries about ±24 points, so the estimates are rough. They agree with proposal (c)'s trial (6 of 20 with no basis, 13 of 20 `undetermined`) in the main point: **the largest single use of `contested` outside the load-bearing nodes is "nothing recorded"**.

### 5.6 Over-stated and under-stated verdicts

**Over-stated:** a `supported` or `contradicted` verdict whose evidence rates low or very low.

| Mapping | Over-stated among the 17 rated | Ids |
|---|---|---|
| M0 | 11 | A2e, B1c, B3, B3a, B6, B7 (load-bearing); F1b, A1, DN1, DN2, B5c (sample) |
| M-D | 16 | all but DN5 |
| M-C | 8 | A2e, B1c, B3, B6; F1b, DN1, DN2, B5c |
| **All three mappings** | **8** | **A2e, B1c, B3, B6** (load-bearing); **F1b, DN1, DN2, B5c** (sample) |

On the load-bearing nodes, 6 of the 8 decided `supported` or `contradicted` verdicts are over-stated under M0 and 4 under every mapping. The two that hold are B3g (moderate) and H1 (high), both of kind `F`. Three of the four robust ones are very low under all three mappings: **A2e** (`contradicted` against Day), **B3** (`contradicted` against Day) and **B6** (`supported` for a critic); B1c is low at best.

Whom the over-statement favours: of the 11 under M0, nine are verdicts on the critics' side of the ledger (`contradicted` on A2e, B1c, B3, B3a, DN1, DN2; `supported` on B6, B7, F1b) and two are on Day's (`supported` on A1, his own premise; `contradicted` on B5c, a critic's number). This is the direction ST-04 found (22 to 1). It says where the wording runs ahead of the evidence. It is not evidence that any of the eleven is wrong: DN1 is low only because the like-for-like rerun is not made, and B7 and B3a are high or moderate if read as statements about the model.

**Estimate for all 52 `supported` or `contradicted`.** Load-bearing: 6 of 8 (census). Others: 2 of 6 sampled `supported` and 3 of 3 sampled `contradicted`, which scaled to the 30 and 14 in the frame gives about 10 and 14. Together about 30 of 52 under M0. The sample is 9 rows, so this is an order of magnitude; it sits beside proposal (b)'s coded count of 26 of 52 resting on a model.

**Under-stated:** a `contested` verdict with a direction and moderate or high certainty.

| Row | Direction | M0 / M-D / M-C | Note |
|---|---|---|---|
| **A3** (load-bearing) | for the claim | high / high / high | Three SEVERE data counts put events per lineage within 25% of Day's 20 M. The verdict word does not say so (AS-11 found the same) |
| **D9** | against the claim | moderate / very low / moderate | A formal claim about a stipulated population; the conditional fixation time is 8,500 generations against the 20,000 stated |

Two further rows would resolve to a direction on one reading: A3z is `against` on SEVERE data if "differences" means events, and ROOT-FM is `for` as a description and `against` as an inference. FM10 leans against at low.

### 5.7 How much the mapping matters, and the sensitivity of the notes

| | Count |
|---|---|
| Rated rows with the same level under M0, M-D and M-C | 20 of 45 |
| Rows where M-D and M-C are two or more levels apart | 15 of 45: B1, B2b, B3a, B3g, B5, B7, F3a, H1 (load-bearing); A1, A1b, A6a, D15, D9, H6, ROOT-K (sample) |
| Rows where M-C is *lower* than M0 | 3: FM10, ROOT-FM, D3 (the audit's own data analyses, unreproduced) |
| Rows at moderate or high: M-D / M0 / M-C | 4 / 10 / 18 |
| Upgrade factors present / applied under M0 / applied under the lenient rule | 2 (A2e, F2) / 0 / 0 |
| Rows that move if `mw` is not counted (note N1) | 4, each from very low to low: B1, B7, F3a, D15 |

Three things follow.

1. **For a third of the rated rows the certainty is decided by the starting level, which is a stance and not a finding.** The fifteen rows two or more levels apart all rest on theory, on a simulation, on the published literature or on a formal claim; none rests on data the audit processed. A reader who takes standard population genetics as background reads them as moderate or high; a reader who requires an observation the claimant does not control reads them as very low. GC-60's expectation that either starting point leads to "the same" final rating does not hold here, because what separates the starting points is the thing in dispute.
2. **The mappings agree where it matters most for the tallies.** The eight verdicts that are over-stated under every mapping, and the one that is under-stated under every mapping (A3), do not depend on whose starting point is taken.
3. **The critic-side mapping is not uniformly kinder to the critics' side.** It rates the audit's own unreproduced data work lower than M0 does, and with it the lean against Day at FM10.

The upgrade factors did nothing: they are present on two rows and barred on both by GRADE's own condition that nothing else be downgraded (GC-24). A2e's "4.2x the flip" is a real margin; it cannot be credited while the estimate behind it is model-inferred, relayed, scoped by the audit and chosen post hoc.

### 5.8 Which domains did the work (45 rated rows)

| Domain | Rows downgraded |
|---|---|
| Indirectness, model to world (`mw`) | 30 |
| Risk of bias | 27 |
| Inconsistency | 17 |
| Indirectness, regime or data set (`sp`) | 16 |
| Indirectness, wording (`rd`) | 11 |
| Imprecision | 9 |
| Selection of evidence | 5 |

Flag `ur` (an audit data or simulation result not reproduced by a second tool, release or published number) is set on 14 rows. Selection of evidence was the hardest domain to judge and the least used: the project keeps no per-claim list of checks considered and not run, so "undetected" mostly means "nothing was written down" (GR-11).

### 5.9 The expectations of 3.4

(1) Partly met. Six of the eight load-bearing `supported` or `contradicted` verdicts are low or very low under M0, not seven: B3g is a formal claim and rates moderate. The second half was wrong: under M-C four of the eight are still low or very low (A2e, B1c, B3, B6), because their weakness is in how the ground was chosen or built, not in the starting level. (2) Under-estimated: 10 of 19 sampled `contested` rows are NE, and 8 of the 20 in proposal (c)'s own sample, against the 6 it coded. All five directional rows are on Day claims; three lean against and two for. (3) Met for theory rows; wrong in one respect for data rows, where M-C is lower on three. (4) Met: no upgrade applied.

---

## 6. Comparison with the other instruments

### 6.1 The four-way split of proposal (c), on the same 20 claims

| Id | Four-way trial value | This pass: direction; M0; FR | Agreement |
|---|---|---|---|
| A | `conditional:adaptive share` | conditional; very low; low | same kind |
| D15 | `conditional:intermediates, target specificity` | conditional; very low; high | same kind |
| D3 | `conditional:landscape structure` | conditional; low; n/a | same kind |
| H | `conditional:K, survival horizon` | conditional; very low; low | same kind |
| ROOT-K | `conditional:bacterial rate as ceiling` | conditional; very low; moderate | same kind |
| F2 | `regime-limited` | conditional, with `sp` 1 | in part: the regime is recorded as indirectness; "tight linkage supports Day" makes it a condition |
| D4 | `disputed-in-literature` | conditional on the serial assumption; very low; low | in part |
| A2 | `undetermined` (`source-missing`) | for (order of magnitude); very low | **differs**: GRADE reads a weak lean where the split saw none |
| A4 | `undetermined` (`source-missing`) | conditional on the s scale; very low; moderate | in part: the same missing source, named as the condition |
| A3z | `undetermined` (`other`), lean contradicted | conditional on the unit; moderate | in part: against on one of two readings |
| D9 | `undetermined` (`other`), lean contradicted | against; moderate | same direction |
| Ga | `undetermined` (`other`), lean contradicted | against; very low | same direction |
| A4g | `undetermined` (`other`) | NE | in part: the only argument is under the internal field |
| ROOT-PG | `undetermined` (`evaluative`) | NE | same |
| A4f, B2c, B4d, B4e, D13, G2g | `undetermined` (`no-basis-recorded`) | NE | same (6) |

**Agreement: same 14, in part 5, differs 1.** The two instruments, applied by two instances of one model family to the same short comments, sort the 20 claims almost identically. That is weak evidence for either (MA-01) and good evidence that they are measuring the same property of the claim files.

What each adds that the other lacks:

| | Four-way split | Certainty and direction |
|---|---|---|
| Names the deciding parameter or regime | yes (5 of 20 with a parameter; 1 regime) | only in the reason text |
| Says how well the conditional is established | no | only through FR (D15 high against A low); M0 puts both at very low |
| Grades a lean | no (`lean` is a free note kept out of every tally) | yes: D9 moderate against Ga very low |
| Separates "nothing recorded" | yes (`no-basis-recorded`) | yes (NE) |
| Says anything about `supported` and `contradicted` | no | yes: 11 of 17 over-stated under M0, 8 under every mapping |
| Says what would settle it | as a companion on `lean` | for every row |
| Needs a stance to apply | no | yes (the starting level) |
| Verdict values changed | all 114 | none |

Neither is the better instrument for the whole column. The split is better **inside** `contested`: it names what the question turns on and needs no starting-level stance. The certainty rating is better **at its edges**: it is the only one of the two that touches the 52 verdicts a reader takes as decided, and the only one that says how strong a lean is.

### 6.2 The Triveritas conjunction

Three of the seven verdicts the Triveritas pass examined are rated here.

| Verdict | Triveritas pass | This pass | Agreement |
|---|---|---|---|
| A2e external `contradicted` | stands on L and M; E-b fails (model-inferred, comparison not registered first) | very low under every mapping | agrees |
| H8 external `contested` | "an honest conditional that one word hides"; simulation only, E-c fails | conditional; very low under M0; FR low | agrees |
| B5c external `contradicted` | "robust to the audit's own free parameter" | very low (M0, M-D), low (M-C) | in part: GRADE takes a level off for the model that splits the count and one for the scope ("as an SNV match") |

On the whole column the nearest analogue to Day's rule (a claim needs anchoring in observations the claimant does not control) is mapping M-D. Under it 4 of the 45 rated rows are moderate or high (A3, ROOT-FM, A3z, DN5), all four on data the audit processed; the Triveritas pass found 1 of its 7 standing on all three legs. The two instruments agree on the order of magnitude and on which rows.

### 6.3 Severity grades

| Grade of the deciding check | high | moderate | low | very low | Rated |
|---|---|---|---|---|---|
| SEVERE | 3 | 1 | 0 | 2 | 6 |
| PARTIAL | 0 | 3 | 3 | 23 | 29 |
| WEAK | 0 | 2 | 0 | 2 | 4 |
| BENT | 0 | 0 | 0 | 4 | 4 |
| no check | 0 | 1 | 0 | 1 | 2 |

The two are not independent: the severity grade is an input to risk of bias (2.5). With that said: every row at high rests on a SEVERE check; every row decided by a BENT check is very low; and two SEVERE checks sit under very-low rows (F3a, D15). Severity is necessary for certainty here and not sufficient. A check can be a severe test of what a model implies and still leave the verdict about the world where it started; that is the difference between M0 and FR in one line, and it sharpens ST-02 rather than adding to it.

---

## 7. Symmetry: the parties' own headline numbers, by the same rules

Each number is rated twice: (a) as a description, (b) as evidence for the conclusion its author draws from it. Same starting levels, same domains, same arithmetic; rated briefly, from the severe-testing pass's section 7, the claim files already read and the quotes cited there. These are not rows of the summary table and no claim file was opened for them alone.

| Assertion | (a) As a description: M0 / M-D / M-C | (b) As evidence for the author's conclusion: M0 / M-D / M-C | Deciding judgement |
|---|---|---|---|
| **Day: required fixations**, 17.5 to 20 M per lineage (Q16, Q05) | high / high / high | low / low / low | (a) is row A3. (b) That selection cannot account for the divergence: indirectness very serious, because the same count is what the account he is arguing against expects (most differences neutral and fixed in parallel; ST 7.1) |
| **Day: the aDNA zero** ("zero alleles moved from below 50% starting frequency to regional fixation", Q53) | low / low / low | very low / very low / very low | (a) data, but his two reports use different thresholds with 1 and 3 completions set aside, and the audit could not reproduce his table on the AADR genotypes by any reading (C1d): inconsistency and wording, one level each. (b) That substitution has stopped: no power against neutral substitution, power against selection not yet computed (L5): indirectness very serious |
| **Day: dN/dS = 0.80** (Q172) | very low / very low / very low | very low / very low / very low | His own unreleased pipeline, no run on sequences of known dN/dS (risk of bias very serious); the audit's 0.21 to 0.27 and the published 0.23 are on the other side (inconsistency very serious). His proposed test (Q176) is credited as sound in design |
| **Day: the mesa index**, "more than 80 times more variable than a uniform-rate process predicts" (Q164) | moderate / moderate / low | very low / very low / very low | (a) reproduced by the audit at 1 Mb in every ape lineage; the statistic is undefined in his post, so one level for wording; M-C takes one more for an unreproduced audit pipeline. (b) That a fourth mechanism is at work: the uniform null fails under every account and the excess is not human-specific |
| **Critics: about 20 to 40 M neutral substitutions expected** (McCarthy MC-04; Hancock GG-04; r/DebateEvolution RE-06 gives 9.7 M) | very low / very low / low | very low / very low / very low | Theory with no observation; the critics' own figures differ by a factor of four and two carry arithmetic slips (X1); with sourced inputs the supply is 0.5 to 0.66x of the requirement at 252,000 generations (B5b). (b) needs the ancestral term and the divergence time, both adjustable (B4a) |
| **Critics: dN/dS ≈ 0.23** (as relayed; DN5) | moderate / moderate / moderate | low / low / low | (a) is row DN5: reproduced at 0.21 on real alignments. (b) That Day's 0.80 is therefore an artefact: not his assemblies or annotation until L1b reports (row DN1) |
| **Critics: k = μ holds in practice** (GG-03 and the textbook reply) | very low / very low / moderate | very low / very low / low | (a) is row B5: an identity, exact at steady state, with the second engine's counts unexplained; FR moderate. (b) That the shortfall therefore dissolves: agreement with the observed divergence is taken up by a free ancestral N_e and divergence time |
| **Critics: keruru's temporal N_e** (C5b) | high / high / high | moderate / moderate / moderate | (a) reproduced by the audit within 4% on two data releases (C1d, SEVERE). (b) That the movement is drift alone: admixture is not separated and his sampling correction is off by 7 to 19% |

What the table shows. Each side has one number that is high as a description and that the audit could recount on public data (Day's required count; keruru's N_e), and one that is moderate (the mesa index; 0.23). Neither side has a headline number that is better than moderate *as evidence for its conclusion*, and most are very low: the step from the number to the conclusion is where both lose their levels, Day through indirectness (a count or a zero that the rival account also predicts) and the critics through model dependence (an identity or a supply count with no observation of the lineage in it). The mapping moves the critics' theory-based assertions (very low to moderate under M-C) and does not move Day's data-based ones; which side that favours depends on the stance, as in 5.7. Day's 0.80 is the one headline number that is very low as a description under every mapping.

---

## 8. Recommendation (proposal k; not applied)

**Adopt both instruments, each where it works, and neither as a new verdict value.**

1. **Certainty and direction as fields beside the verdict**, for every decided external verdict, required first for `supported` and `contradicted`.
2. **The four-way split as a companion field** for rows whose direction is `none`, not as four new verdict values. The word `contested` stays; what it turns on is recorded.
3. **Rows with no recorded evidence** leave the decided column (`pending`), as proposals (a) and (c) already suggest for their own columns.
4. **The starting-level mapping is declared, not hidden.** The stored value is M0; lint prints M-D and M-C beside it. No public page reports a certainty without saying which mapping.

This replaces the "relabel" strength of proposal (b) (`model-consistent`, `model-inconsistent`): the basis is recorded and the certainty says what it is worth, with no change to the verdict vocabulary. It does not replace proposal (b)'s field, which it absorbs, or proposal (g)'s `severity`, which it uses as an input.

### 8.1 Field spec

```yaml
verdicts:
  external: contradicted
external_certainty: very-low        # high | moderate | low | very-low | not-rated
external_direction: against-claim   # for-claim | against-claim | none
external_open: null                 # required when direction is none:
                                    #   conditional:<parameter> | regime-limited | mixed | disputed-in-literature | no-evidence
external_grade: "b=Lm;k=W;st=WEAK;rob=2;inc=1;mw=1;sp=0;rd=1;imp=0;sel=1;ur=0;upf=2"
                                    # the code line of section 2.7; basis `b` supersedes proposal (b)'s external_basis
external_raise: "The audit's own alpha estimate with planted-alpha controls (L3)"
external_rated: {date: 2026-10-12, rater: "claude-opus-5-5, single, not blind", mapping: M0, rubric: "grade-certainty-2026-10-12 sections 2 and 4 notes"}
```

**Where the domains are recorded.** The code line lives in the claim file's front matter, one line, so the rating travels with the verdict and is diffable. The one-line reason for each domain lives in a generated table, `research/checks/CERTAINTY.md`, written by `research/tools/grade_certainty.py` from a reasons file kept beside the tool; the summary-of-findings table of this pass is its first 58 rows. Nothing is stored twice by hand.

### 8.2 Lint rules

| Rule | Check | Fails or warns |
|---|---|---|
| L-GC1 | `external` in {`supported`, `contradicted`} has `external_certainty`, `external_direction`, `external_grade`; direction is `for-claim` for `supported` and `against-claim` for `contradicted` | fails |
| L-GC2 | `external_certainty` equals the value recomputed from `external_grade` under M0 | fails |
| L-GC3 | `external_direction: none` has `external_open`; `external_open: no-evidence` only with `external: pending` | fails |
| L-GC4 | `supported` or `contradicted` with certainty `low` or `very-low` | warns, and the row is listed as "worded above its evidence" in the generated table and on the board |
| L-GC5 | `contested` with a direction and certainty `moderate` or `high` | warns: "under-stated" |
| L-GC6 | `load_bearing: true` with a decided external verdict and no `external_raise` | fails |

L-GC4 and L-GC5 warn and do not fail, because changing the verdict word is a rule-freeze matter and not lint's to force.

### 8.3 Expected movement in public tallies

No verdict value moves on adoption. What a reader would see beside the tallies:

| Tally now | With the fields (M0; estimates as in 5.5 and 5.6) |
|---|---|
| 34 `supported`, 18 `contradicted` | about 30 of the 52 marked low or very low, of which 6 of the 8 on load-bearing nodes; of the 11 found here, 8 are robust to the mapping |
| 16 `contradicted` on Day claims | all five rated here are low or very low (A2e, B3, B3a, DN1, DN2), four of them under every mapping |
| 16 `supported` on critic claims | three of the four rated here very low (B6, B7, F1b), two of them under every mapping; H6 high |
| 114 `contested` | about 45 `no-evidence` (to `pending`: decided external verdicts fall from 172 to about 127 and the `contested` share from 66% to about 54%); about 19 with a direction, a handful of them moderate or high; about 50 conditional or mixed, each with its parameter named |
| "no load-bearing external verdict rests on data the audit processed" (proposal b) | still true of the eight `supported` or `contradicted`; A3 (`contested`) is on data at high certainty and leans to Day |

### 8.4 Which side each change helps

- **Day's side:** the count most often quoted against him loses weight. Every `contradicted` verdict on a Day claim rated here is low or very low under M0, and his required-fixations count is shown as corroborated at high certainty. Mapping M-D is printed beside M0.
- **The critics' side:** verdicts for them that rest on a simulation built to agree (B6, F1b) are marked as such, which protects the ones that do not (H6; B7 and B3a as statements about the model). Leans against Day that `contested` now hides become visible with a level (D9, FM10, Ga), and Day's `supported` verdicts are graded by the same rule (A1 very low under M0). Mapping M-C is printed beside M0.
- **Neither:** the 45 or so rows with nothing recorded, and the 30 or so model-based conditionals that sit at the floor as statements about the world.
- **A risk for both:** a certainty column invites a new tally ("Day has N high, the critics M"). The rows are not comparable across parties (5.3), and GRADE itself gives no overall grade (GC-29). The lint and the board should print the list, not a score.

### 8.5 Cost

| Item | Size | Estimate |
|---|---|---|
| Rate the remaining 114 decided external verdicts, one rater | 35 `supported` or `contradicted`, about 75 `contested` of which roughly half will be NE at a glance, 4 `untestable` | about two agent sessions the size of this one (tokens L); no compute |
| Fold the four application notes into the rubric before any further rating (GR-07) | sections 2.4 to 2.7 | tokens S |
| Lint rules and the generated table | six rules, one generator | tokens S to M |
| A second rater who is not of this model family, on the 58 rows first | code sheet without the codes; agreement reported as exact and within-one-level, and weighted kappa | owner decision (proposed O-23); the 58-row packet is tokens S to prepare |
| Upkeep | one row re-rated when a check lands | marginal |

---

## 9. Concordance with the earlier passes

| Earlier finding | This pass | Note |
|---|---|---|
| MA-01, TV-01, TV-11, AR-13, ST-13, AS-13 (one model family; not blind) | agrees | GR-13. GRADE adds that its own authors do not expect reproducible ratings (GC-10) |
| MA-03 (rules changed the day they decided verdicts) | agrees for A2e external | very serious risk of bias; very low under every mapping. B internal is out of scope |
| MA-04 (pre-registration) | in part | the label feeds risk of bias, and moves few rows: indirectness decides more (5.8). Agrees with ST-01 |
| MA-05, TV-04, ST-02 (external verdicts decided by the disputed theory) | agrees | GR-01, GR-02. Refines: the size of the problem depends on the starting-level mapping, which is the stance MA-05 names |
| MA-05, remedy "relabel" (`model-consistent`) | **disagrees in part** | a certainty field does the same work with no new verdict values |
| MA-07 (`holds` as default) | not covered | internal column not rated |
| MA-08, ST-12, AS-11 (`contested` holds different things) | agrees | GR-03, GR-04. Adds direction and level |
| MA-08, remedy (proposal c alone) | **disagrees in part** | the split says nothing about the 52 decided verdicts and cannot grade a lean (6.1); recommends both |
| MA-09 (sources not read) | in part | enters as `rd` on second-hand claims and as selection; the selection domain could rarely be judged (GR-11) |
| MA-11, AR-12 (no aggregation rule; no confidence grading in the draft) | agrees, and limits its own use | GRADE supplies per-verdict confidence and expressly no overall grade (GC-29) |
| MA-12 (verdicts ahead of the like-for-like test) | agrees | DN1 low, DN2 very low under every mapping until L1b |
| MA-15 (category leaks) | agrees | four formal claims sit in the external column (GR-06) |
| MA-16 (from "the simulation shows" to hominids) | agrees | `mw` on 30 rows, `sp` on 16 |
| TV-06 (three columns allow a trade-off) | not covered | one column rated |
| TV-10 (no as-of date) | agrees | `external_rated` carries a date |
| AR-11 (no rule for which claims get a check) | agrees in part | 5 of 13 critic rows NE against 5 of 34 Day rows; selection domain |
| ST-03 (four live load-bearing verdicts on WEAK or BENT probes) | agrees on the two in scope | A2e and B6 are very low under every mapping. B internal and F1a internal are not rated |
| ST-04 (the untested risk points one way) | agrees | 9 of the 11 over-stated verdicts are on the critics' side of the ledger |
| ST-06 (the second engine's discordant counts) | agrees | counted as inconsistency at B5, B and B6 |
| ST reading "SEVERE means well probed" | **refines** | two SEVERE checks sit under very-low rows (6.3) |
| AS-01 (seven of eight worded above their grounds) | agrees on six, **disagrees on B3g** | B3g is a claim about a derivation and rates moderate; H1 is sound in both passes |
| AS-02 (no argument at the field) | agrees | B2 external is NE; B, F, F1 were rated by pointer |
| AS-03 (concession used as a ground) | agrees | a concession is not a body of evidence (GC-12, GC-13); counted as inconsistency where the author later re-asserts |
| AS-04 (A2e decided on the audit's reading) | agrees | `rd` at A2e |
| AS-08 (model presupposes what is disputed) | agrees | `mw` 2 at B3, F1, F1b |
| Triveritas pass on B5c ("robust") | **disagrees in part** | very low to low here (6.2) |

**Counts over the 26 rows:** agrees 16, agrees in part 3, disagrees in part 4 (two remedies, AS-01 on B3g, the Triveritas reading of B5c), refines 1, not covered 2 (MA-07 and TV-06; fidelity and fairness to named people are also outside the instrument). No earlier finding is closed or contradicted by this pass.

**What this lens sees that the earlier ones did not:** a level for each verdict, with the reasons separated; a direction for `contested`; which over-statements survive a change of stance; what one action would raise each row; that the evidence for some low rows is already in the repository and not cited at the node. **What it cannot see:** the validity of an argument; whether a quote was read correctly; a claim that has no verdict; whether the rater is right.

---

## 10. Findings

Severity scale as in the earlier passes. "Who" is who would act.

| ID | Severity | Finding | Evidence | Remedy | Who |
|---|---|---|---|---|---|
| GR-01 | MAJOR | **Six of the eight decided `supported` or `contradicted` external verdicts on load-bearing nodes are low or very low in certainty (A2e, B1c, B3, B3a, B6, B7); four under every starting-level mapping (A2e, B1c, B3, B6).** In the sample, 5 of 9, four of them under every mapping (F1b, DN1, DN2, B5c). Nine of the eleven favour the critics' side | 5.6; rows | Record certainty and direction (proposal k). For each row, its "raise" action: L3 for A2e, the ancestral-polymorphism count for B6 and B1c, a field per value for B3, L1b for DN1 and DN2 | agent; owner for the rule-freeze if a word changes |
| GR-02 | MAJOR | **For a third of the rated rows the certainty is set by the starting level, and the starting level is the stance.** M-D and M-C differ by two or more levels on 15 of 45 rows; 20 of 45 are the same under all three. GRADE gives no starting level for a model (GC-45), so the instrument cannot be applied to this column without taking a side or printing three | 5.7 | Never report a certainty without its mapping; store M0, print M-D and M-C | agent, owner (proposed O-22) |
| GR-03 | MAJOR | **`contested` is the external column's default.** 11 of 39 rated `contested` rows have no recorded evidence: 10 of 19 in the sample, 8 of the 20 in proposal (c)'s own sample, an estimated 45 of 114. One is load-bearing: B2 external has no argument at the node | 5.5; NE rows | Move NE rows to `pending` (rule-freeze), or record the evidence; B2 first | agent; owner |
| GR-04 | MINOR | **Two `contested` verdicts are under-stated:** A3 (load-bearing; high, for Day's count, under every mapping) and D9 (moderate, against). Two more resolve to a direction on one reading (A3z, ROOT-FM) | 5.6 | `external_direction`; lint L-GC5 | agent |
| GR-05 | MAJOR | **The adapted instrument saturates.** 32 of 45 rated rows are at the floor, and 21 of the 23 open `contested` rows are low or very low, because GRADE has no construct for a conditional and a model-derived conditional is rated as a statement about the world. It tells D9 from Ga and cannot tell D15 from A without the added FR column | 5.1, 5.5, 2.9 point 2 | Use the four-way split, as a companion field, inside `contested`; keep FR or drop conditionals from the rating | agent |
| GR-06 | MINOR | **Four of the 45 rated verdicts are formal claims in the external column** (B3g, H1, H6, D9), and they supply 2 of the 3 highs. Several more are high only if read that way (B7, B1, F3a, D15 by FR) | 5.4 | A `kind` code on the row; decide whether formal claims take an external verdict at all (with MA-15) | agent, owner |
| GR-07 | MAJOR for the standing of the ratings | **The rubric committed before rating was incomplete, and four rules were settled while rating** (notes N1 to N4). FM10 and DN1 each move between very low and low depending on note N2. This is the pattern MA-03 and TV-02 describe, in this pass | section 4 notes; `86cdf64` | Fold the notes into a revision 2 of the adaptation and re-rate under it before any further row is rated; report what moved | agent |
| GR-08 | MINOR | **Severity is necessary for certainty and not sufficient.** All three highs rest on SEVERE checks; all four BENT-decided rows are very low; two SEVERE checks sit under very-low rows | 6.3 | In any public use of the severity grades, say what inference the grade is for | agent |
| GR-09 | MINOR | **`untestable` is used for "not measured in the corpus"** (D7b) as well as for conceptual claims (ROOT-COV). GRADE cannot rate either; six verdicts carry the word | rows D7b, ROOT-COV | A reason code: `not-measured`, `not-measurable`, `evaluative` | agent |
| GR-10 | MINOR | **Evidence already in the repository is not cited at the node, and the verdict rates lower for it:** A2 (the LTEE table recounts of E5 / E6 and L6), F1b (the measured polymorphic share, GAP-07c), B5f (B5b), B6 (the published ancestral-polymorphism figure quoted in the FMnull registration) | rows | Cite it; no new work. Claim-file comment edits need the owner's go-ahead (C22) | agent |
| GR-11 | MINOR | **Selection of evidence could rarely be judged.** It downgrades 5 rows and is "undetected" on the rest mostly because no per-claim list of checks considered and not run exists | 5.8; AR-11 | A "not run, and why" line per load-bearing claim | agent |
| GR-12 | MINOR | **By the same rules, neither party's headline number is better than moderate as evidence for its conclusion,** and each has one that is high as a description. Day's 0.80 is very low as a description under every mapping. The mapping moves the critics' theory-based numbers and not Day's data-based ones | section 7 | Use this table, with its mappings, wherever the parties' numbers are set side by side | agent |
| GR-13 | CRITICAL for the standing of the document | **One rater, of the model family that produced the verdicts, not blind, applying an instrument whose own handbook says it does not ensure reproducible judgements (GC-10).** No second rater, no agreement statistic. A one-level difference on many rows is to be expected from any second rater | preface; GC-10 | A second rater not of this family on the 58 rows, codes hidden. Registered expectation: the same level on at least half the rated rows, within one level on at least 80%, and at least 6 of the 8 verdicts found over-stated under every mapping found over-stated again | owner, outside (proposed O-23) |

**Counts (13 findings).** CRITICAL for the document's standing 1; MAJOR 5 (GR-01, GR-02, GR-03, GR-05, GR-07); MINOR 7. None is closed.

---

## 11. Remediation, split three ways

**No-decision fixes** (change no rule, vocabulary or verdict). None was applied by this pass: it edits no claim file. Ready to do on a go-ahead for claim-file comments: cite the evidence already held (GR-10); add the "not run, and why" line (GR-11).

**Proposals** (specified, held back).
- **Proposal k:** the fields and lint of section 8 (GR-01, GR-04, GR-05). Moves no verdict value. Printing M-D and M-C beside M0 is part of it (GR-02).
- NE rows to `pending` (GR-03): about 45 verdict values, a rule-freeze matter; the 11 found here are named in 5.5.
- A reason code on `untestable` (GR-09).
- A field per k/μ value at B3 (from GR-01).
- Revision 2 of the adaptation, then re-rating (GR-07), before the remaining 114 rows are rated.

**Owner decisions** (proposed; not yet in `DECISIONS.md`).
- **O-22:** adopt certainty and direction beside the external verdict, or treat this pass as a one-off; if adopted, which mapping is the stored one and whether all three are always printed; decide together with proposals (b) and (c), which it partly absorbs.
- **O-23:** a second rater for the 58 rows who is not of this model family (with O-3, O-4 and the second raters asked for by ST-13 and AS-13).

Whom each helps is in 8.4.

---

## 12. What was not examined

The internal and fidelity columns, by design. The 114 decided external verdicts outside the 58. The check write-ups in full: a limit stated in a write-up and not carried to the claim file or to `RESULTS.md` will have been missed, which lowers a row. The claim files' Responses sections. The GRADE Book and the single-domain papers of the J Clin Epidemiol series, which may define the domains more exactly than the 2013 handbook does. Whether the 25% materiality line is the right "threshold" in the sense of GC-41. Any rating of the parties' numbers beyond the eight in section 7. No check was run, no source outside the GRADE texts was fetched, and nobody was contacted.
