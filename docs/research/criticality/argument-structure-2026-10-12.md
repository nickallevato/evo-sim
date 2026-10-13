# Argument-structure pass, 2026-10-12: warrants, qualifiers, critical questions, fair discussion

*Criticality layer, component v. Applier: one Claude instance (Opus 5.5) in the project's own session, the same model family that extracted the claims, wrote and ran the checks, reviewed them and wrote the verdicts examined here. Single rater. Not blind: the applier read the criticality README (with the MA, TV, AR and ST findings), the methods page, the verdict rule and the R5 draft's verdict table before starting. Day's papers credit a co-author from the same model family, and the model's training corpus is overwhelmingly mainstream on evolution (methods page, "Who did it"). A reader should treat every code below as one same-family rater's judgement and not as an outside review (finding AS-13).*

**The question.** Earlier passes asked who reviewed (MA-01), whether predictions were fixed first (MA-04), what an external verdict rests on (MA-05), whether the review meets systematic-review standards (AR) and whether a check could have failed (ST). This pass asks about the *shape of the arguments*: for each load-bearing node, what is claimed, on what grounds, by what licence the grounds are taken to support the claim (the warrant), how strongly the claim is worded against how strongly the grounds support it (the qualifier), and what conditions would defeat it (the rebuttal). It asks this of three parties on the same nodes: Day, his critics, and the audit itself, whose verdict is treated as one more argument.

**Order of work (stated so the reader can discount it).** 1. The framework texts were fetched, hashed and quoted (section 1; 95 quotes, machine-checked). 2. One claim file (`A-mittens-formula.md`) was read to learn the file layout; no other claim file had been opened by this instance. 3. This rubric (sections 1 and 2) was written and committed. 4. The rubric was applied (sections 3 onward, a later commit). The rubric was written by an instance that already knew the earlier passes' findings, so it is not blind to where the audit's weak points were said to be.

**What this pass does not do.** It changes no verdict, rule, claim file, check script or argument-map entry. It runs no check. It does not re-read the check write-ups: the audit's argument at each node is taken from the claim file (Statement, verdict fields with their comments, the R4 paragraphs, Responses) and the R5 draft. Where a write-up answers a critical question and the claim file does not carry the answer, this pass will code the question lower than a full reading would; that is itself part of what is being measured (is the licence visible where the verdict is stated?), and it is a limit.

---

## 1. The frameworks, from the fetched texts

Sources and hashes: [`../sources/bib-literature.md`](../sources/bib-literature.md), section "Criticality pass v". Quotes: [`../sources/quotes-literature.md`](../sources/quotes-literature.md), ids AT-01 to AT-95. **Not obtained:** Toulmin 1958, Walton, Reed and Macagno 2008, and van Eemeren and Grootendorst 1992 and 2004. Each is used only through the open texts named beside each quote, and where the only open text is tertiary (Wikipedia) or derived (templates, a formalisation) that is said.

### 1.1 Toulmin's layout

| Part | Statement used | Source |
|---|---|---|
| Claim | "A conclusion whose merit must be established." | AT-05 (tertiary) |
| Grounds (data) | "A fact one appeals to as a foundation for the claim." | AT-06 (tertiary) |
| Warrant | "A statement authorizing movement from the ground to the claim." | AT-07 (tertiary) |
| Backing | "Credentials designed to certify the statement expressed in the warrant; backing must be introduced when the warrant itself is not convincing enough to the readers or the listeners." | AT-08 (tertiary) |
| Qualifier | "Words or phrases expressing the speaker's degree of force or certainty concerning the claim." | AT-10 (tertiary) |
| Rebuttal | "Statements recognizing the restrictions which may legitimately be applied to the claim." | AT-09 (tertiary) |

From a text by an argumentation theorist (van Eemeren and Verheij 2017): "The validity of argumentation is in his view primarily determined by the degree to which the (usually implicit) warrant that connects the data advanced in the argumentation with the claim at issue is acceptable—or, if challenged, can be made acceptable by a backing." (AT-01), and "What kind of backing may be required in a particular case depends on the field to which the standpoint at issue belongs." (AT-02). Two points follow for this pass. Warrants are *usually implicit*, so finding an unstated warrant is normal and not a fault in itself; the fault, where there is one, is a warrant that would be contested if stated. And backing is field-dependent, which matters here because the two sides do not agree on which field's backing counts (population genetics as practised, or arithmetic on stated premises).

*From memory, marked as such:* Toulmin's own example (Harry was born in Bermuda, so presumably he is a British subject) and his point that a qualifier and its rebuttal go together ("presumably ... unless") are recalled from the 1958 book and were not checked against it.

### 1.2 Walton's argumentation schemes and critical questions

"The most common approach to argument schemes combines a pattern of argument with a set of “critical questions” with which it is associated." (AT-13). "Schemes do not identify fallacies but rather argument kinds that are sometimes used fairly, and, other times, fallaciously. With each kind of scheme is associated a set of critical questions which guide us in deciding whether a given use of an argument is correct, weak or fallacious." (AT-18). "every scheme has a corresponding set of critical questions, representing its defeasibility conditions and the possible weak points that the interlocutor can use to question the argument and evaluate its strength." (AT-38).

What an unanswered question means: "If one of the questions cannot be answered clearly this is an indication that the argument is weak, and answering No to either of the two questions cancels the presumption for the conclusion" (AT-19); "If a respondent asks any one of the six appropriate critical questions, a burden of proof is shifted back onto the proponent of the argument to provide a satisfactory answer to the question. If she fails to give such an answer, the appeal to expert opinion loses its previous weight of support." (AT-37). So an unanswered critical question does not make a conclusion false. It removes the presumption until answered.

A caution taken from a critic of scheme lists: "in order to justify different argument schemes there must minimally be some consequential difference to either the basic inference or the critical questions." (AT-95). Counts "by scheme" below depend on how arguments are sorted into schemes, and neighbouring schemes (expert opinion and position to know; sign and abduction; cause to effect and consequences) share questions.

### 1.3 The pragma-dialectical rules

The theory treats argument "as part of a discourse aimed at resolving a difference of opinion on the merits by methodically testing the acceptability of the standpoints at issue." (AT-03). "A set of ten rules has been proposed as constitutive of the critical-discussion ideal" (AT-20); "Any move that is an infringement of any of these rules, whichever party performs it and at whatever stage in the discussion, is a possible threat to the resolution of a difference of opinion on the merits and must therefore—and in this particular sense—be regarded as fallacious." (AT-93). They are "not just rules of logic or epistemology, but rules of conduct for rational discussants" (AT-24).

The ten rules as listed in the one open text found that lists them all (Wikipedia, citing van Eemeren, Grootendorst and Snoeck Henkemans 2002; tertiary; rules 1 and 10 agree with the wording quoted from the theory's authors in AT-88, AT-89 and AT-92):

| # | Name | Wording used | Quote |
|---|---|---|---|
| 1 | Freedom | "Parties must not prevent each other from advancing standpoints or from casting doubt on standpoints." | AT-77 |
| 2 | Burden of proof | "A party that advances a standpoint is obliged to defend it if asked by the other party to do so." | AT-78 |
| 3 | Standpoint | "A party's attack on a standpoint must relate to the standpoint that has indeed been advanced by the other party." | AT-79 |
| 4 | Relevance | "A party may defend a standpoint only by advancing argumentation relating to that standpoint." | AT-80 |
| 5 | Unexpressed premise | "A party may not deny premise that he or she has left implicit or falsely present something as a premise that has been left unexpressed by the other party." | AT-81 |
| 6 | Starting point | "A party may not falsely present a premise as an accepted starting point nor deny a premise representing an accepted starting point." | AT-82 |
| 7 | Validity | "A party may only use arguments in its argumentation that are logically valid or capable of being made logically valid by making explicit one or more unexpressed premises." | AT-84 |
| 8 | Argument scheme | "A party may not regard a standpoint as conclusively defended if the defense does not take place by means of an appropriate argumentation scheme that is correctly applied." | AT-83 |
| 9 | Closure | "A failed defense of a standpoint must result in the party that put forward the standpoint retracting it and a conclusive defense of the standpoint must result in the other party retracting its doubt about the standpoint." | AT-85 |
| 10 | Usage | "A party must not use formulations that are insufficiently clear or confusingly ambiguous and a party must interpret the other party's formulations as carefully and accurately as possible." | AT-86 |

The source lists the argument-scheme rule seventh and the validity rule eighth. The order above (validity, then scheme) is the order of the task brief and, *from memory*, of the 2004 book; nothing below depends on the numbers of those two rules.

### 1.4 Fallacy definitions used in section 6

- Argument from ignorance: "the inability of an opponent to produce a better argument is not sufficient reason to think the proponent’s argument must be accepted. Modern versions of this kind of argument take it as a fallacy to infer a proposition to be true because there is no evidence against it" (AT-25). As a scheme it is not always a fallacy; its questions are in 2.3.
- Appeal to authority under dispute: "when there is controversy, and authorities are divided, it is an error to base one’s view on the authority of just some of them." (AT-26). Popular opinion: AT-27.
- Straw man: "straw man fallacies happen when someone in the course of argumentation inaccurately and unfavourable distorts a ground-level argument in an attempt to refute it or discredit its source." (AT-28). The "iron man" (rebuilding an argument into something stronger than its author offered and then judging that) is *from memory* of the informal-logic literature and is not in the fetched texts; here it is treated as the same breach of rule 3 in the other direction.
- False balance: "there are conflicting arguments each drawing on prima facie evidence. This can lead to the meta-argument that the truth lies somewhere in the middle between the opposed ground-level conclusions. This is considered a fallacy because purported contrary evidence noticed at the meta-level is insufficient reason to abandon both the ground-level conclusions in favour of a compromise." (AT-29).
- Burden of proof: "evading the burden of proof which breaks the rule that you must defend your standpoint if asked to do so" (AT-22). Equivocation and misuse of a scheme: AT-23.
- Ad hominem as a scheme with a legitimate use: "The basic question that must be asked is whether there is a good reason why the arguer’s views should not be taken seriously" (AT-17). The genetic fallacy (judging a claim by its origin) is *from memory*; it is treated here under the ad hominem questions.

---

## 2. Rubric (written before any node was laid out)

### 2.1 Unit, parties, nodes

- **Unit:** one party's argument at one node. Three parties per node: **D** (Day's side: Day, or an ally where the node is an ally's), **K** (the critics' side: the strongest counter-argument, or the critic's own argument where the node is a critic's), **U** (the audit: its verdict fields on that node, taken as claims).
- Where the node's author is a critic, an ally or the audit, layout (a) is still the Day-side position on that node and layout (b) the critic-side position, so the columns mean the same thing everywhere. Where a side has no recorded argument at a node, the cell says "none recorded" and nothing is counted.
- "Strongest" counter-argument: the one the claim file's Responses section or verdict comment treats as doing the most damage; if several, the one a check was built on. This is a choice by the applier and is named at each node.
- **Nodes:** the 33 that `hierarchy.yaml` marks `load_bearing: true`. Time and tokens force the split the task brief allows. **Full layouts (15):** ROOT, ROOT-M, ROOT-FM, A, A2e, A3, B, B2, B3, C2, F1, F1a, H, H8, FM10. **Compact table (18):** B1, B1c, B2b, B3a, B3g, B4a, B5, B6, B7, C2a, E5, E6, F, F2, F3a, H1, H2, H5. Compact rows carry the same codes with one line of reasons; they count in the aggregates and are flagged as compact.

### 2.2 Toulmin fields and their codes

Each layout has six fields: claim (C), grounds (G), warrant (W), backing (B), qualifier (Q), rebuttal (R).

**Warrant code.** The warrant is written out by the applier whether or not the party stated it.
- `W0` stated where the argument is made (in the quoted statement or its recorded context for D and K; in the verdict comment or the claim file's R4 paragraph for U).
- `W1` stated by the party elsewhere (another node's quote for D and K; the verdict rule, the methods page or a write-up, as far as the claim file points to it, for U), but not where the argument is made.
- `W2` not found stated by the party anywhere in the material read.
- A **hidden warrant** is `W1` or `W2`; the two are counted separately. A claim file's "Assumptions → Implicit" line is the audit's reconstruction of D's or K's warrant; it does not make the warrant stated by D or K, and for U it counts only if it is the warrant of the *verdict* and not of the audited argument.
- Each warrant is also marked `contested` if the other side is on record (in the claim files read) as denying it, since an implicit warrant nobody disputes is ordinary.

**Qualifier code.** Strength scale, weakest to strongest: (1) possible; (2) plausible, presumably; (3) holds in a stated regime or on a stated condition; (4) generally, typically; (5) necessarily, always, impossible, zero, certain.
- *Asserted* strength: for D and K, the modal words of the quoted statement (quoted in the layout). For U, the verdict word is categorical by vocabulary (`holds`, `non-sequitur`, `arithmetic-error`, `contradicted`, `supported` are read as level 5 on the question they answer; `contested`, `pending`, `unverifiable` assert no conclusion), and the verdict comment may lower it.
- *Licensed* strength: the strongest level the stated grounds and the warrant support once the critical questions are scored, in the applier's judgement, with the reason given.
- `QM0` asserted ≤ licensed. `QMw` (word only): for U, the verdict word exceeds the licence but the comment at the node carries the limiting condition; for D and K, the quoted sentence exceeds the licence but the same source states the limit. `QMf` (full): asserted > licensed and no limiting statement at the node (U) or in the quoted source (D, K). Mismatches are `QMw` + `QMf`, counted separately.
- Under rule RH a statement tagged `rhetoric` is not literal-fact-checked. Its qualifier is still recorded here, marked `(RH)`, and counted in a separate column, because the question "what strength is asserted" is prior to the question "is it rhetoric".

**Rebuttal code** (conditions under which the claim fails).
- `R0` stated by the party where the argument is made. `R1` stated elsewhere by the party. `R2` not stated. For U the question is the task's: are the conditions under which the verdict would fail recorded in the claim file?

### 2.3 Schemes in scope and their critical questions

Each argument is assigned its main scheme and, where a second scheme carries a separate step, that too. Questions are numbered here for scoring; the wording is from the cited quotes, shortened.

| Code | Scheme | Critical questions | Source of the questions |
|---|---|---|---|
| EX | Argument from expert opinion (incl. appeal to a literature or a consensus of specialists) | EX1 how credible is the source as an expert; EX2 expert in this field; EX3 what did the source assert that implies the claim; EX4 personally reliable; EX5 consistent with what other experts assert; EX6 based on evidence | AT-32, AT-33 (primary); AT-14, AT-15 |
| PK | Argument from position to know | PK1 is the source in a position to know; PK2 honest, reliable; PK3 did the source assert it | AT-62, AT-63 (tertiary); AT-47 to AT-49 (derived) |
| AN | Argument from analogy | AN1 are the cases similar in the respect cited; AN2 is the claim true in the source case; AN3 are there differences that undermine the similarity; AN4 is there another similar case where the claim is false | AT-54 to AT-56, AT-72, AT-75 (derived) |
| SG | Argument from sign | SG1 is the relation between sign and thing signified established; SG2 are there other events that would more reliably account for the sign | AT-34 (primary, example); AT-43, AT-44 (derived) |
| CE | Argument from cause to effect | CE1 how strong is the causal generalisation; CE2 are there interfering factors in this case | AT-39 (primary, scheme); AT-50, AT-51 (derived) |
| CC | Argument from correlation to cause | CC1 is there a correlation; CC2 is there a theory explaining how one causes the other; CC3 does some third factor cause both. *From memory, not in the fetched texts:* CC4 could the causation run the other way; CC5 is the correlation more than coincidence (enough instances) | AT-69 to AT-71 (derived); AT-30 |
| GE | Argument from example / generalisation | GE1 is the example as described; GE2 is it a typical case, how widely does the generalisation apply; GE3 are there special circumstances that undermine generalising from it | AT-45, AT-46 (derived) |
| IG | Argument from ignorance (lack of evidence) | IG0 premise: if it were true, would it be known (found, published, recorded); IG1 how far has the search for evidence progressed; IG2 which side has the burden of proof; IG3 how strong must the proof be | AT-64 to AT-68 (tertiary); AT-74 (derived); AT-25 |
| PR | Practical reasoning | PR1 conflicting goals; PR2 alternative actions; PR3 which is most efficient; PR4 is the action practically possible; PR5 side effects | AT-40 (primary) |
| CN | Argument from consequences | CN1 will the consequences occur, how likely, on what evidence; CN2 what other consequences should be weighed | AT-41 (primary, scheme); AT-52, AT-53 (derived) |
| AH | Ad hominem (generic, circumstantial, bias) | AH1 how does the allegation bear on the person's reliability; AH2 is the person's reliability relevant to the point at issue; AH3 (bias) what is the evidence of bias, and could the person have weighed the evidence anyway | AT-17 (secondary); AT-59 to AT-61 (derived) |
| PO | Argument from popular opinion / consensus | PO1 what is the evidence that it is generally accepted; PO2 even if accepted, are there good reasons to doubt it | AT-57, AT-58 (derived); AT-26, AT-27 |
| PC | Argument from precedent (incl. "this is how the field / the author has always done it") | PC1 are there relevant differences between the precedent and this case; PC2 is the rule drawn from the precedent applicable here | AT-72, AT-73 (derived) |
| AB | Abductive argument (inference to the best explanation) | AB1 how satisfactory is the explanation by itself; AB2 how much better than the alternatives on the table; AB3 how thorough was the search for alternatives; AB4 would it be better to continue than to conclude now | AT-35, AT-36 (primary); AT-76 |

**Three schemes that are the audit's construction, not Walton's.** Walton's list has no entry for an inference from a model or simulation to the world, for a recomputation on an author's own basis, or for fixing the reading of a quoted sentence. These three steps carry most of the audit's own verdicts, so they are defined here with their own questions. They have no standing in the literature cited; they are this pass's working definitions and are marked `(constructed)` wherever used. The same schemes are applied to Day and to the critics where they argue the same way (Day's use of the LTEE and of his own simulations; critics' appeals to Wright-Fisher results).

| Code | Scheme (constructed) | Form | Critical questions |
|---|---|---|---|
| MW | Argument from a model or simulation to the world | P1: in model M, under assumptions a1..an and inside parameter region P, result r holds (shown by derivation or run). P2: the program or derivation computes M. P3: the target system T satisfies a1..an, and has its parameters inside P, in every respect r depends on. C: presumably r holds of T. | MW1 implementation: is there evidence the code computes the model (known-answer baseline, second engine, review that could have caught an error); MW2 assumptions: are the assumptions r depends on listed, and is each shown to hold of T by evidence that does not itself assume the conclusion; MW3 coverage: are T's parameter values inside the region run, or is the result extrapolated; MW4 robustness: does r survive changing the assumptions that are in dispute; MW5 non-circularity: is M (or a parameter in it) the very thing the other party disputes, so that P3 presupposes the answer; MW6 anchor: does M reproduce some observation of T that it was not fitted to; MW7 scope: is the conclusion worded with its regime, or generalised beyond it |
| RC | Argument from recomputation on the author's own basis | P1: the author states inputs i and method m and prints result x. P2: recomputing m on i gives y. P3: reading ρ of the author's referents is the right one. C: the author's result does (y ≈ x) or does not (y ≠ x) follow from the author's own premises. | RC1 are i and m the author's stated ones, with locators, and nothing supplied by the auditor; RC2 were alternative readings of ambiguous referents tried, and is the one used one the author would accept; RC3 was the recomputation checked by something that could have caught an error in it (independent derivation, a reviewer who recomputed); RC4 is the size of the mismatch judged by a threshold fixed before the case and justified; RC5 does the verdict concern the conclusion the author actually drew from the number |
| TR | Argument from the reading of a text | P1: the author wrote sentence s. P2: s is best read as ρ (and as dialectic or as rhetoric). C: the author is committed to ρ; the verdict on ρ is the verdict on the author's claim. | TR1 is s quoted verbatim with context and date; TR2 are the other plausible readings listed with their verdicts; TR3 would the author accept ρ as what was meant (later statements, usage elsewhere); TR4 is the choice among readings made by a rule fixed before the case; TR5 is the same sentence read the same way wherever it is used (no equivocation across nodes) |

### 2.4 Scoring an answer to a critical question

| Code | Meaning | Counted as |
|---|---|---|
| `A+` | Answered with evidence, in the argument's favour: the party (or, for U, the claim file) points to a datum, a derivation, a run, a quoted text or a cited source that can be checked | answered |
| `A−` | Answered with evidence, against the argument: the material read shows the question defeats the step (the presumption is cancelled, AT-19) | answered against |
| `S` | Asserted: an answer is given with no evidence that can be checked | asserted |
| `U` | Unanswered: the question applies and no answer was found in the material read for that party | **unanswered** |
| `—` | Not applicable to this argument | not counted |

Rules of application.
1. **Whose answer.** For D and K the answer must be theirs, as the claim files record it (their quotes, the Responses sections). An answer the audit supplied for them does not count for them; it is credited to U. For U the answer must be in the claim file or in a standing project document the claim file's comment names.
2. **Equal rigour.** The same question is asked of each party that uses the same scheme at the node. Where the audit uses a party's own argument as its ground (for example, upholds a critic's objection), the audit inherits that argument's unanswered questions unless it answers them itself.
3. **One code per question per party per node.** Where a question has parts with different answers, the weaker code is recorded and the split is noted.
4. **No verdict follows from a code.** An unanswered question is a place where the argument has not been defended, not a finding that it is wrong.
5. **The audit's verdict columns are separate arguments.** Internal, fidelity and external verdicts are laid out separately when their warrants differ; a verdict of `pending` or `n/a` asserts nothing and gets no layout. `contested` is laid out as the claim "this is not settled either way" where the comment gives grounds.

### 2.5 Fallacy audit and the ten rules

Section 6 asks seven questions of the audit and the matching question of Day and the critics: (i) argument from ignorance; (ii) appeal to consensus or authority as ground truth; (iii) straw man or over-charitable rebuilding; (iv) shifting the burden of proof; (v) equivocation across readings; (vi) genetic or ad hominem leakage (does who said it change the score); (vii) false balance. Each is coded `observed` (an instance with a file path), `risk` (the structure allows it and no instance was confirmed in the material read), or `not found`.

Section 7 scores each party against each of the ten rules: `kept` (evidence of compliance), `breached` (an instance with a locator), `at risk`, or `cannot be assessed`. One fact governs rules 1, 2 and 9: **no discussion has taken place between the audit and the audited parties.** None has been contacted (methods page, "No right of reply so far"). A critical discussion needs two parties who can advance doubt and be answered; where a rule presupposes that exchange, the audit's standing under it is coded for what it has done unilaterally and marked as untested.

### 2.6 Counting

- Per party: number of layouts; hidden warrants (`W1`, `W2`, and how many are `contested`); qualifier mismatches (`QMw`, `QMf`, and `(RH)` separately); unanswered critical questions (`U`) by scheme, with `S` and `A−` reported beside them; rebuttal conditions unrecorded (`R2`).
- Counts are of codes in this file, by one rater. They are not rates of error and must not be compared across parties as if the parties had been sampled alike: Day authored most load-bearing nodes, a critic's "strongest counter-argument" is often one sentence, and the audit has three verdict columns per node. The per-layout averages are given only so that the raw counts are not misread.
- "Most load-bearing hidden warrants" are ranked by the number of decided verdict fields on the 33 nodes that would have to be re-argued if the warrant were rejected, with the fields listed.

### 2.7 Expectations written down before the layouts (not blind)

The applier expects, from the earlier passes and not from the claim files: (1) the audit's hidden warrants will cluster in external verdicts that go from a simulation to hominid history (scheme MW, questions MW2 and MW5); (2) Day's qualifier mismatches will cluster at ROOT and wherever "impossible" or "zero" is asserted on grounds that support "not shown"; (3) the critics' unanswered questions will cluster on appeals to the standard model as settled (EX5, PO2) and on analogies from textbook identities to the actual lineage (MW3). If the layouts show something else, section 8 says so.

---

*Sections 3 onward (node layouts, compact table, fallacy and fair-discussion audit, aggregates, proposals, concordance, findings AS-01 onward) are added in a later commit, after this rubric.*
