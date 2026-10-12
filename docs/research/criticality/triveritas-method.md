# The Triveritas: what it is, and whether it can be used to critique this audit

*Criticality layer, component ii, part 1 of 2 (research and assessment). Part 2, the application, is [`triveritas-audit-2026-10-12.md`](triveritas-audit-2026-10-12.md). Written 2026-10-12.*

**Who wrote this, read first.** A Claude Opus instance launched from inside the project's own session, with the project's `AGENTS.md` loaded. That is the same AI model family that did the audited work, wrote the method audit ([`METHOD-AUDIT-2026-10-12.md`](METHOD-AUDIT-2026-10-12.md)), and is listed as co-author ("Claude Athos") on the Triveritas papers themselves. It is not an independent party. Day's own protocol for scoring a piece of work with the Triveritas says the authors do not score their own work (Q224), and the one third-party applier found excluded the model that composed the study (Q256). Both rules are broken here and cannot be mended by this author. Treat every placement below as a self-assessment.

**Sources.** Everything stated about the Triveritas comes from text fetched on 2026-10-12 into `sources/raw/refresh-2026-10-12d/` (harvest log: [`sources/harvest-log-day.md`](../sources/harvest-log-day.md), last section). Quotes are in [`sources/quotes-day.md`](../sources/quotes-day.md), Q195 to Q271, each cut by script from the saved text and checked as a substring of it. A quoted phrase below followed by a Q-id is verbatim from that entry. Nothing here comes from memory.

---

## Summary

- **What it is.** An epistemic criterion published by Vox Day (with "Claude Athos") in February and March 2026 as the working tool of a philosophy he calls Veriphysics. "The Triveritas holds that a claim merits warranted assent if and only if it satisfies three jointly necessary conditions: logical validity (L), mathematical coherence (M), and empirical anchoring (E)." (Q203)
- **It is a critique system**, as the owner supposed. Day uses it to pass or fail theories, papers and other people's arguments, first as three pass/fail tests and from 2026-03-09 with 0 to 100 scores against published anchor scales.
- **Is it applicable to this audit?** Yes, with stated readings. Day says it is "scoped to claims about reality" (Q213), that "anyone competent in mathematics" may check the numbers (Q198), and that it is "merely an analytical tool" separable from his metaphysics (Q265). He applied it to one of his own papers (Q224) and a third party applied it to analytical essays (Q255). The narrowest scope statement, "claims about the physical world that involve quantities, predictions, and empirical observations" (Q246), covers only part of an audit's method.
- **Is it well-defined?** Partly. The conjunction and the three names are stable. The definitions of L, M and E each exist in three versions, there are three different pass marks (50, 60, 90), two aggregation rules, and Day's four applications to evolution give three different results for L. An application is reproducible only if it reports each reading, which part 2 does.
- **What it adds to the method audit.** A test of whether the audit's rule set has one principle or is a set of case-by-case fixes; a test of whether the audit has ever made a prediction about itself that an outsider could refute; and a rule against letting strength on two legs excuse weakness on the third.
- **What it does not cover.** Fidelity to sources, fairness to named people, right of reply, conflicts of interest, presentation, and the mechanics of pre-registration. The method audit covers those.

---

## 1. What the Triveritas is, in Day's words

### 1.1 The criterion

First statement found, blog serial of *Veriphysics: The Treatise*, part 023, 2026-02-25: "A claim merits assent and may be accepted as probably true when and only when it satisfies three conditions: logical validity, mathematical coherence, and empirical anchoring. Each condition is necessary; none is sufficient; the conjunction of all three elements is required." (Q195)

Formal statement, Zenodo 18724454, 2026-02-21: Q203 above. The criterion is the intersection of three sets of claims; a claim outside any one of them does not merit assent. Day's own short form: "I do not care how strong you are on two dimensions." (Q219, rhetoric; the dialectical core is that the test is conjunctive and nothing compensates).

What it claims to deliver: "It does not promise certainty; it offers warranted assent." (Q201) and "It does not demonstrate that the Triveritas is sufficient for truth." (Q210). Day also calls it a "heuristic" (Q253).

### 1.2 The three criteria, and their versions

Each criterion is defined more than once, and the definitions are not equivalent. The labels a, b, c are mine and are used in part 2.

| | Version a: Treatise serial, 2026-02-25 | Version b: Mathematical Proof, 2026-02-21 | Version c: scales and later papers, 2026-03 |
|---|---|---|---|
| **L** | "the argument for the claim must be formally sound. The conclusions must follow from the premises; the inferences must be valid; the reasoning must be free from fallacy." (Q196) | "its conclusion follows deductively from its premises and its inferential structure is explanatorily coherent" (Q204): validity plus non-ad-hoc premises and "logical unity" | "Explanatory coherence, non-ad-hoc premises, principled relationship between premises and conclusions, logical unity." (Q231). Deduction is no longer named. An AI rater's working version: "deductive coherence + non-circularity" (Q247, relay) |
| **M** | "the claim must survive quantitative analysis where quantification is possible" (Q197): the numbers work | "its quantitative structure is internally consistent: the operations it performs are well-defined, its parameters are finite and computable in principle, and its mathematical predictions do not contradict its own axioms" (Q205): consistency on the claim's own model | "whether the theory possesses a mathematical architecture that generates quantitative predictions from its own structure" (Q230); statistics on data "belong to" E. Rater's version: "formal consistency + no free parameters" (Q247, relay) |
| **E** | "must be confirmed or at least not refuted by what we observe" (Q199) | "it makes at least one prediction that has been tested against observation and not refuted", on data other than "data already used to construct the claim" (Q206) | "observations the claimant does not control" (Q212); and a count: "how many predictions has the theory made, how many have been tested, how many confirmed" (Q237) |

Two decision rules attach to E and can disagree: a tally, "above 50, the confirmed predictions outweigh the failures" (Q238), and a veto, "one counterexample is sufficient to negate E" (Q242).

A corollary Day draws from E, used heavily in part 2: "Any system of claims that cannot, even in principle, be constrained by something external to its own stipulations is epistemically inert." (Q211)

### 1.3 How it is applied and scored

| Step | Day's rule | Quote |
|---|---|---|
| Binary first | Each dimension is passed or failed; the numbers come second. "The numerical scores are a refinement. The binary determinations are the foundation." | Q227 |
| 0 to 100 per dimension | "based on informed assessment" | Q229 |
| Anchor scales | About twenty named historical theories per dimension, published 2026-03-16 to 03-20. Day on what the numbers mean: "It's all relative. The actual numbers are irrelevant." | Q231 to Q240; Q241 |
| Composite | The arithmetic mean of the three scores in every worked case, e.g. (35, 5, 10) gives "Composite ~ 17" | Q221 |
| Veto | A failed dimension overrides the mean: "Effective composite for warranted assent: 0" | Q223 |
| Pass mark | "the 60-point threshold that separates passing from failing theories" (applied to what, composite or each dimension, is not said); 50 on the M and E scales; an AI rater speaks of "the ≥90 threshold" | Q226; Q235, Q238; Q266 (relay) |
| Decision rule in pseudocode | "warranted = (L > threshold) and (M > threshold) and (E > threshold)", with `threshold` never given a value | Q228 |
| Sensitivity | Vary each score by plus or minus 20% of itself and see whether the verdict moves | Q226, Q268 |
| Who scores | For his own paper: "two independent AI reviewers (Grok and Gemini)"; "The authors did not score their own work." | Q224 |
| Procedure as an AI rater ran it | "accept internal arguments at face value, test L ..., M ..., E ..., compute composite, run ±20% sensitivity, and declare Confirmed/Rejected." | Q247 (relay) |

Day states that there is no algorithm: "a criterion of warranted assent, not a decision procedure" (Q209), and that "Assigning a claim to a specific failure mode requires judgment" (Q218).

### 1.4 What he applies it to

- **Scientific theories**, historical and current: twelve cases in the Empirical Proof, four in the History of Science paper, scored theories in the Demarcation paper (general relativity, quantum mechanics, the Modern Synthesis, string theory, intelligent design, phrenology).
- **Evolution**, four times (table in 1.6).
- **His own papers**, scored by AI raters at his request (Q224, Q267).
- **A theological epistemology** and a doctrine (Q244), six days after writing that the tool is for "claims concerning the physical world" and "is not a theological filter" (Q245).
- **A critic's argument**: keruru's martingale argument for k = μ, where Day says the fault is mathematics not anchored in "material reality" (Q251).
- **As a working heuristic on evolution data**, 2026-10-09: "it is only when the logic, the math, and the empirical evidence all triangulate an answer can one be reasonably confident" (Q248).

Stated targets in the book blurb: "the cogito, Darwinian evolution, classical economics, and social contract theory" (Q252, rhetoric).

### 1.5 Dates and versions

| Date | Event | Source |
|---|---|---|
| 2026-02-08 | Earliest blog use found: "Applied Triveritas", in a passage by "Athos" quoted by Day; no definition | Q250 |
| 2026-02-18 | *Veriphysics: The Treatise* announced (ebook; not read by this pass) | Q252 |
| 2026-02-21 | Mathematical, Logical and Empirical Proofs on Zenodo (version b definitions) | Q203 to Q219 |
| 2026-02-22 | Agrippan Trilemma paper (modified 2026-03-08) | bib `Z18727817` |
| 2026-02-25 to 03-01 | Treatise serial parts 023 to 025 on the blog (version a definitions; evolution "fails all three") | Q195 to Q202 |
| 2026-03-02 | Dedicated Substack opens | harvest log |
| 2026-03-09 | Demarcation paper: first 0 to 100 scores, composite, 60 mark, sensitivity (modified 2026-03-15) | Q220 to Q228 |
| 2026-03-14 | History of Science paper (M version c) | Q229, Q230 |
| 2026-03-16 to 03-20 | L, M, E anchor scales; L scale revised 03-19 | Q231 to Q240 |
| 2026-03-23 | Scoring of a non-scientific target | Q244 |
| 2026-08-26, 2026-10-09 | Used in the evolution dispute | Q251, Q248 |

In summary (my paraphrase, not a quotation): the definitions moved from *valid argument, numbers work, not refuted* to *explanatory unity, own mathematical architecture, tested novel prediction* inside four weeks. No changelog exists; the Zenodo papers were not revised to match the scales.

### 1.6 Worked examples

**Evolution, by the same author, four times:**

| Date | Where | L | M | E | Quote |
|---|---|---|---|---|---|
| 2026-02-21 | Mathematical Proof 2.2; Empirical Proof case 5 | satisfied | failed | satisfied | Q207, Q216, Q217 |
| 2026-02-27 (serial; book 02-18) | Treatise 024 | fails ("The logic is unsound") | fails | fails | Q200 |
| 2026-03-09 | Demarcation 3.4 and 6.2 | ~ 60 | ~ 5 | ~ 70; composite ~ 45 | Q222 |
| 2026-03-16 | L scale | ~ 40 | not restated | not restated | Q233 |

L is pass, fail, 60 and 40. The stated sensitivity band for L ~ 60 is "48 to 72" (Q268); 40 lies outside it. Only M's failure is constant, and M is not assessed afresh: "The Triveritas does not require new analysis to reach this conclusion; it applies the existing analysis" (Q222). The M score for evolution is therefore the MITTENS conclusion restated on a scale, and is exactly as sound as branches A, B, G and H of this audit find it (it names "d ≈ 0.45" and the "Bernoulli Barrier", Q270).

**Other examples.** Intelligent design: "Composite ~ 17. Verdict: not science." (Q221), lower than evolution, which is a point for Day's even-handedness with his own tool. String theory: mean 57, effective 0 (Q223). His own Demarcation paper: 92 from two AI raters (Q224, Q225). Reformed presuppositional epistemology: (45, 15, 15), composite 25, with M scored low because the system "simply does not show up" on that dimension (Q244).

### 1.7 Secondary sources (not Day), kept apart

- **Third-party applier.** C. Kererū (keruru, a critic of Day on k = μ elsewhere in this repository) ran a "Triveritas Stress Test" on ten policy essays with one human and six AI raters, using his own pass/fail questions per leg (Q255). Findings relevant here: the two AI raters on L failed every essay, including three the human passed (Q257); the author notes this may reflect "the model’s ability to generate plausible-sounding opposition to virtually anything" (Q258); Claude was excluded from scoring because it composed the study (Q256).
- **Allies extending it.** Van Allen adds a fourth criterion and renames M "Structural Coherence" for theology (Q259). Howland adds a utility axis because utility otherwise "leaks into the truth evaluation" (Q260).
- **Critics.** Thin. No critic already tracked here (Hancock, Myers, McCarthy, Camestros, Mansfield) was found discussing the Triveritas. One theological critique exists only as reproduced by Day after its author deleted it (Q261, relay). Reader comments supply three sceptical points: that the evolution score "needs independent mathematical support or explicit flagging as contested" (Q262, a reader relaying an AI review); that the plum pudding model was refuted by observation, not mathematics (Q263); and that interpretation of evidence is the weak point of E (Q264).

---

## 2. Assessment of the system itself

The Triveritas is one of Day's own methods. It gets the same scrutiny as his other claims and the same charity. No claim node or verdict is created or changed here; the points below are proposals for nodes, with both sides' readings.

### 2.1 Is it defined well enough to apply reproducibly?

**Stable:** the three names, the conjunction, the non-compensation rule, binary-before-numeric, the exclusion of construction data from E, the statement that it is necessary and not sufficient.

**Not stable:**

| # | Gap | Evidence | Effect on an application |
|---|---|---|---|
| W1 | Each criterion has three definitions | Table 1.2 | A target can pass L-a and fail L-b (a valid argument from ad hoc premises); pass M-b and fail M-c (consistent numbers, no generating model) |
| W2 | Pass mark is 50, 60 or 90, per dimension or on the composite | Q226, Q228, Q235, Q238, Q266 | A profile such as (60, 55, 70) passes or fails by choice of mark |
| W3 | Composite is a mean of scores the author calls ordinal ("It's all relative") | Q221, Q241 | The composite has no defined meaning; only the per-dimension pass/fail does |
| W4 | No rule for a target without quantitative content: "where quantification is possible" against a score of 15 for not showing up | Q197, Q244, Q246 | Qualitative arguments either escape M or fail it, by choice |
| W5 | Scope moves: "claims about reality", "claims concerning the physical world", then theology | Q213, Q245, Q244 | Whether a method, a verdict or a blog remark is a proper target is undetermined |
| W6 | Rater dependence | Q257 (0 of 3 agreement on L between a human and two models); Day's L for evolution: pass, fail, 60, 40 | Two honest appliers can differ by a pass/fail on L |
| W7 | The sensitivity band is a percentage of the score | Q268: M varies "from 4 to 6" | The lowest and most decisive score is the one least tested |
| W8 | Classification between dimensions is a judgement | Q218; Q263 (plum pudding); Q230 (statistics are E, not M) | The same defect can be booked to different legs |

Day concedes W6 and W8 in his own limitations sections (Q218, Q209) and says the scales are "merely a first draft" (in the paragraph after Q232). That is to his credit and it is also the answer to the question: by its author's account it is a criterion plus informed judgement, not a procedure.

**Reading-dependent result (rule RD spirit).** Reading 1, the Triveritas as the three-part pass/fail test of Q203 to Q206 with reasons given per leg: well enough defined to apply, if each definitional version is reported. Reading 2, the Triveritas as a 0 to 100 measuring instrument with a pass mark: not reproducible on the evidence fetched. Part 2 uses reading 1 and shows anchor placements only as bands.

### 2.2 Relation to standard epistemology

*This subsection is the applier's characterisation from general background, not from fetched text, and should be read as such.*

- **L** in version a is deductive validity (Day writes "formally sound", Q196, but describes validity: the premises are not required to be true). In versions b and c it becomes explanatory unification and absence of ad hoc adjustment, which is a coherence virtue in the family of consilience and of the standard objections to ad hoc auxiliary hypotheses.
- **M** is internal consistency of the quantitative part (b) or possession of a predictive formal model (c). Both are again coherence-type tests. M and L are not independent in the ordinary sense, as one of Day's readers asks ("Aren’t L and M basically the same thing", the question that opens the Q&A 3 post); Day's answer is that they have different characteristic failures (Q243).
- **E** in version b is corroboration by a tested prediction on data not used to build the claim, close to the requirement of novel or use-novel prediction, and to out-of-sample testing. Version c's "observations the claimant does not control" (Q212) is an independence requirement on evidence.
- **The conjunction** is triangulation: accept only where independent lines agree. Day uses that word (Q248).
- Against the classical triad of truth theories: L and M are coherence tests, E is a correspondence test, and there is no pragmatic leg. Day notes that the Mohist "three tests" had practical applicability as the third (in the Q&A 3 post), and both allies who extend the scheme add exactly that leg (Q259, Q260).
- Against this audit's three columns: `internal` is L and M on the author's own basis; `external` is E (and M with real parameters); **`fidelity` has no counterpart**. The Triveritas has no test for whether a cited source says what is claimed.

### 2.3 What it measures that the method audit did not, and the reverse

| The Triveritas asks, the method audit did not | The method audit asked, the Triveritas does not |
|---|---|
| Does the rule set follow from one principle, or is it a set of independent accommodations (L-b)? The method audit examined RH6, RD and the 25% line one at a time (MA-02, MA-03, MA-14) and never the rule as a whole | Fidelity to sources; the unread book as a sourcing fault (MA-09 is covered by E only indirectly) |
| Does the audit's own quantitative scheme hang together and derive its thresholds, or carry free parameters (M-b, M-c)? | Right of reply, fairness to named living people, governance by one owner (MA-10) |
| Has the audit made any prediction about itself that someone outside could test and refute (E-b, E-c)? | Conflicts of interest, priors, licence, threat model (MA-19) |
| Non-compensation: a named weakest leg, not a list of strengths set beside a list of weaknesses | Presentation symmetry (MA-17); budget-driven depth (MA-18); stale documents (MA-20, except as contradictions) |
| Presence or absence of mathematics as a property of each claim, both sides | Mechanics of pre-registration: commit gaps, push times, label classes (MA-04) |

### 2.4 Strengths (recorded with the same prominence as the weaknesses)

1. **It is conjunctive and refuses trade-offs.** A critique that cannot be answered by pointing at one's strong side is a real discipline.
2. **E excludes accommodation.** "not merely consistency with data already used to construct the claim" (Q206) is the principle behind out-of-sample testing and behind this project's pre-registration rule.
3. **The anti-self-sealing corollary** (Q211, Q212) is a sharp, usable test of any self-assessing system, this audit included.
4. **It states its limits.** Necessity without sufficiency (Q210), no decision procedure (Q209), judgement in classification (Q218), independence assumed in the elementary case (Q208), "this is, of course, backtesting" (Q254). Few of Day's evolution papers carry sections like these.
5. **It is diagnostic.** It names which leg is weak, which tells the audited party what to fix.
6. **It was applied against a position friendly to Day's side** (intelligent design, Q221) and returned a lower score than for evolution.
7. **It is open to anyone.** "anyone competent in mathematics" (Q198) removes the objection that an outside party has no standing to apply it.
8. **Its author invited attack**: a reader's harder cases were taken up within a day (History of Science paper; the exchange is in the "Grok Pronounces the Verdict" comments).

### 2.5 Failure modes

1. **Definition drift (W1).** A system whose L test changed from validity to unity in four weeks lets its user pick the version that gives the wanted answer. Day-side reading: the versions refine one idea. Critic-side reading: the refinement tracked the targets.
2. **The M verdict on evolution has two incompatible grounds.** Ground 1: the theory's quantities exceed what its own model allows (the Q205 definition; the Empirical Proof's "five orders of magnitude", Q217). Ground 2: the theory "possesses no internal mathematical architecture" (Q268) because population genetics is "not part of the modern synthesis" (Q269). If population genetics is outside the theory, there is no "own model" for ground 1 to contradict; if it is inside, ground 2 is false. Candidate non-sequitur under this audit's rule N, on Day's own texts; not scored. Day-side reading: the 1940s verbal synthesis and its later mathematics really are distinct, and the theory fails either way. Not resolved here.
3. **Self-validation.** The Triveritas is said to pass its own E test on twelve historical cases chosen by its authors, one of which (evolution) is confirmed by the authors' own companion papers (Q217) while the case-selection rule says outcomes "are not in dispute" (Q215). By Q206 and Q212 that case is not independent evidence. Prediction 1 is also hard to refute as worded: a failed claim must turn out "false or unwarranted" (Q214), and "unwarranted" is what failing the test means.
4. **Friendly raters.** Eight of the authors' papers scored by AI systems at the authors' request: "Every paper scores 90–94" (Q267, relay). The rater accepted "internal arguments at face value" (Q247). Agreement of two language models is offered as evidence of objectivity (Q225). This is the same defect the method audit finds in this project's reviews (MA-01), and the remedy is the same: a measured catch rate, and raters who do not share the author's sources.
5. **Scores without a scale (W2, W3, W7).** Means of ordinal placements, three pass marks, and a sensitivity band that shrinks to one point where the verdict is decided.
6. **Built-in preferences.** M-c favours theories with a compact generating equation and marks down historical and statistical sciences; E-b favours prospective prediction over retrodiction. These are defensible values and they are also the terrain on which Day's own argument is strongest and his critics' replies (often qualitative) weakest. See 2.6.
7. **Independence of the three legs is argued from the same twelve cases** that are then used as the empirical proof (Axiom 5 is said to be warranted by "each historical example" in the Mathematical Proof, section 1.2).
8. **Scope creep (W5)** lets the tool be withdrawn where it is unwelcome (the Trinity, per the same post as Q246) and deployed where it is useful (Q244).

### 2.6 Is it fair to judge the audit by the audited party's own standard?

**For.**
- It answers "you judged me by your rules" directly. The verdict rule in this repository was written by the auditor (rule X1) and one of its categories, dialectic and rhetoric, was itself borrowed from Day; the Triveritas is his stated criterion of warranted assent, so a result under it cannot be dismissed by him as foreign.
- Day's texts license it: universal scope (Q213), any competent applier (Q198), separable from his metaphysics (Q265), and a precedent of applying it to a paper (Q224).
- It is a second lens with different blind spots from the method audit, and where the two agree the finding is harder to wave away from either side.

**Against, or with care.**
- **The applier chooses the readings.** With three versions per leg, the auditor's model is still the judge. Reporting every reading reduces this; it does not remove it. Day could fairly say the audit has not been judged by his standard until a rater he would accept has done it.
- **It imports his tilt.** Failure mode 6. Critics never agreed to be scored on whether their blog replies contain a generating equation. Applying M to Myers or Hancock holds them to a standard chosen by their opponent. A critic-side reader may say the audit has now adopted Day's rhetoric category and his epistemology.
- **It can flatter the audit.** A method that is strong on re-computation will look good on M-a. Passing the audited party's test is not evidence of being right, by the test's own terms (Q210).
- **It is not endorsement.** Using the Triveritas as a lens says nothing about Veriphysics, about the claims Day derives with it, or about its proofs, none of which is audited here.

**Position taken.** Apply it as a parallel lens, to all three parties with the same readings, report every reading, move no verdict on its account, and say plainly that a valid application needs raters from outside this model family (owner decision, part 2).

### 2.7 Protocol fixed for part 2

Fixed before the application was written up, but **not blind**: the applier had already read the method audit, the claim files and Day's texts. Label: criterion-only.

1. Pass/fail per leg first (Q227); conjunctive (Q203, Q228).
2. Each leg is assessed under each version, L-a, L-b; M-a, M-b, M-c; E-a, E-b, E-c, as defined in table 1.2 (L-c is merged into L-b).
3. A target with no quantitative content is reported under two readings: N1 "not applicable" (Q197, Q246) and N2 "fails M" (Q244).
4. Anchor placement is given as a band between named anchors, never as a point. No composite is used to decide anything; where Day's mean is shown it is marked indicative.
5. Pass marks 50 and 60 are both reported where they differ.
6. Targets: (a) the method as a whole, treated as Day treated his own paper; (b) a verdict, treated as the claim "statement X has status V"; (c) the underlying Day and critic claims.
7. For a verdict: L asks whether it follows from the stated rule and the quoted text, and whether that rule is principled; M asks whether its numbers are consistent and derived or carry free parameters; E asks whether it rests on, or has been tested against, anything the audit does not control.

---

## 3. What was not examined

- *Veriphysics: The Treatise* itself (paid ebook, not bought). Definitions are taken from the blog serial of part three and from the Zenodo papers. Anything that exists only in the book is missing.
- The correctness of the three "proofs", of the Agrippan Trilemma argument, and of the historical classifications. Read, not checked.
- The Philosophical Proof, Amphiboly, Non-Arbitrary Termination and Hard Problem papers beyond abstract and grep.
- Most comment threads; SocialGalactic; anything behind a login.
- Whether historians of biology place Fisher, Haldane and Wright inside the Modern Synthesis (Q269): no source was fetched; the point is left as two readings.
- Section 2.2 rests on general background, not on fetched sources.
