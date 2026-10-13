# Argument-structure pass, 2026-10-12: warrants, qualifiers, critical questions, fair discussion

*Criticality layer, component v. Applier: one Claude instance (Opus 5.5) in the project's own session, the same model family that extracted the claims, wrote and ran the checks, reviewed them and wrote the verdicts examined here. Single rater. Not blind: the applier read the criticality README (with the MA, TV, AR and ST findings), the methods page, the verdict rule and the R5 draft's verdict table before starting. Day's papers credit a co-author from the same model family, and the model's training corpus is overwhelmingly mainstream on evolution (methods page, "Who did it"). A reader should treat every code below as one same-family rater's judgement and not as an outside review (finding AS-13).*

**The question.** Earlier passes asked who reviewed (MA-01), whether predictions were fixed first (MA-04), what an external verdict rests on (MA-05), whether the review meets systematic-review standards (AR) and whether a check could have failed (ST). This pass asks about the *shape of the arguments*: for each load-bearing node, what is claimed, on what grounds, by what licence the grounds are taken to support the claim (the warrant), how strongly the claim is worded against how strongly the grounds support it (the qualifier), and what conditions would defeat it (the rebuttal). It asks this of three parties on the same nodes: Day, his critics, and the audit itself, whose verdict is treated as one more argument.

**Order of work (stated so the reader can discount it).** 1. The framework texts were fetched, hashed and quoted (section 1; 95 quotes, machine-checked). 2. One claim file (`A-mittens-formula.md`) was read to learn the file layout; no other claim file had been opened by this instance. 3. This rubric (sections 1 and 2) was written and committed. 4. The rubric was applied (sections 3 onward, a later commit). The rubric was written by an instance that already knew the earlier passes' findings, so it is not blind to where the audit's weak points were said to be.

**What this pass does not do.** It changes no verdict, rule, claim file, check script or argument-map entry. It runs no check. It does not re-read the check write-ups: the audit's argument at each node is taken from the claim file (Statement, verdict fields with their comments, the R4 paragraphs, Responses) and the R5 draft. Where a write-up answers a critical question and the claim file does not carry the answer, this pass will code the question lower than a full reading would; that is itself part of what is being measured (is the licence visible where the verdict is stated?), and it is a limit.

---

## Executive summary

**Scope.** The 33 load-bearing nodes: 15 laid out in full (section 3), 18 in a compact table (section 4). 83 argument layouts: 27 for Day's side, 16 for the critics, 40 for the audit's own verdicts. Every code is one same-family rater's judgement (AS-13). The counts are not error rates and are not comparable across parties (2.6).

| | Day side | Critics | The audit |
|---|---|---|---|
| Layouts | 27 | 16 | 40 |
| Hidden warrants (stated elsewhere + stated nowhere) | 18 (2 + 16) | 4 (0 + 4) | 11 (10 + 1) |
| Qualifier mismatches (word only + full) | 20 (8 + 12) | 1 (1 + 0) | 10 (8 + 2) |
| Unanswered critical questions / scored | 42 / 90 | 16 / 36 | 33 / 150 |
| Rebuttal conditions unrecorded | 9 | 12 | 4 |

**What is sound in the audit's own arguments.**
1. Three quarters of its verdict arguments are well formed: 30 of 40 have no gap between word and grounds, 29 state their licence where the verdict is stated, and 32 record at the node what would defeat them.
2. Its recomputations are defended: the questions put to a recomputation are answered with evidence 31 times in 40.
3. Its `contested` verdicts on A, B4a, B5, F2, H and H8 carry every clause with its regime; H8's is the best-warranted comment read, and B4a prints an anchor test the standard model partly fails.
4. It did not argue from Day's unpublished method to a defect (FM10), did not treat an unretrieved source as false (C2, F3a), and moved one verdict in Day's favour to avoid scoring a step twice (F).
5. It reads the parties carefully: verbatim quotes, every plausible reading tabled. Under the pragma-dialectical rules that is its strongest mark.

**What is not.**
1. **Seven of the eight decided `supported` or `contradicted` external verdicts on these nodes are worded above what their grounds license** (A2e, B1c, B3, B3a, B3g, B6, B7). The ground is a model result, an identity inside a class of models, a model-based published estimate or the author's own withdrawal; the word is the one used for a data result (AS-01).
2. **29 of 74 decided verdict fields carry no argument at the field**, and in 11 of 40 layouts the licence is stated only in a standing document or nowhere (AS-02).
3. **An author's concession is used as evidence about the world** in five external comments (AS-03).
4. **Two load-bearing verdicts are decided on readings the audit made** and has not shown to be the author's: A2e external and B internal (AS-04). **Two internal `non-sequitur` verdicts lean on an input the audit supplied**: A2e and F1a (AS-05).
5. **The audit is an arguer, not only a rater**: 146 of the 437 attacks in its argument map are its own checks' (100 on Day's nodes, 33 on critics'), none rated `not_upheld` by it, and on six nodes the case against Day is one only the audit has made (AS-06).
6. **No critical discussion has taken place** between the audit and anyone it audits, so the rules on freedom to doubt, burden of proof and closure are untested for it (AS-07).

**The same lens on the parties.** Day: 16 of 27 arguments rest on a licence he states nowhere, 20 are worded above their grounds (12 with no limit stated in the same source), and the question he most often leaves open is whether a sign has another account (7 times). He also has the best record of the three of withdrawing specific points (four on these nodes), and two of his statements are fully qualified by himself (the sigillation hypothesis; the fixation-count paper). Critics: one mismatch in 16, but 12 of 16 arguments name no condition under which they would fail, 10 of their 16 unanswered questions are about carrying a textbook result to the actual lineage, and on 9 of the 33 nodes no critic argument is recorded at all.

**The five licences the audit most needs to state** (section 8.3): own basis (all 27 internal verdicts); model to world (6 of the 8 decided external `supported` or `contradicted`); concession as evidence (5 comments); literature as benchmark (A2e and B1c external, and the conditions of four more); default and burden (what all 20 `contested` fields leave standing).

**Proposals** (section 9; none applied): a `warrant:` and a `rebuttal conditions:` line per decided field; seven standing warrants stated once; wording of verdict comments by kind of ground; a closure rule for replies.

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

## 3. Full layouts (15 nodes)

**How to read a layout.** C claim, G grounds, W warrant (written out by this pass; the code says whether the party stated it), B backing, Q qualifier (asserted against licensed), R rebuttal. The line "Codes" carries the rubric codes of 2.2 to 2.4 and is what section 8 counts. Verdicts are I / F / E (internal, fidelity, external) as they stand in the claim file's front matter on 2026-10-12. Quotes are copied from the claim files' Statement sections, where their sources and locators are given. Where two nodes carry the same argument or the same verdict comment, it is laid out once and the other node says "as at X"; nothing is counted twice.

**Clarifications made while applying the rubric (after it was committed; none changes a definition in section 2).** (1) Notation in the code lines: a `c` after the warrant code means contested; `(RH?)` marks a mismatch on a sentence whose rhetoric tag the claim file records as unclear; `+RH` marks a further over-strength sentence tagged rhetoric at the same node; `A-` is the rubric's `A−`; tags such as `U-int`, `U-ext`, `U-fid` name the verdict field, and `U-agg`, `U-cat` an argument the audit makes at a node where its verdict is `pending`. (2) A critical question is scored against the claim as asserted: an argument that states its own limit and claims no more gets `A+` on the question the limit answers. (3) Where a question's parts have different answers, the code less favourable to the argument is recorded and the split is said in the text. (4) The critics are treated as one side: a limit stated by one critic on the node counts as stated by the side (`QMw`, `R1`), which is lenient to them; Day's limits count only from the same source, as the rubric says. (5) In the compact table the audit gets one layout per node, for its most consequential decided field.

### 3.1 ROOT (Day). I pending / F n/a / E pending

**D.** C: no evolutionary mechanism can produce the observed human-chimpanzee divergence in the time available. G: the shortfall 205M / (252,000 / 1,322) ≈ 1,075,000 (reconciles, claim file "Check"); "Each alternative, when subjected to quantitative analysis, fails to close gaps of 3-5 orders of magnitude." W (unstated): a mechanism that nobody has shown to be sufficient is thereby excluded, so *not shown sufficient* licenses *impossible*; with it, the stated premise that the LTEE rate bounds every mechanism in every organism (laid out at A2e). B: the LTEE papers, Yoo 2025. Q asserted: "mathematical impossibility of evolution by natural selection, selective sweeps, neutral sweeps, genetic drift, ILS, biased gene conversion, and every other imagined mechanism" (level 5). Licensed: level 3, conditional on the ceiling premise and on the count being a count of fixations. The RH tag of this sentence is recorded as UNCLEAR in the claim file and it is scored as dialectic under rule C; on the rhetoric reading the mismatch would move to the `(RH)` column. R: none in the quoted sources; elsewhere he excepts "three minor ones" (ROOT-M). Schemes: IG, GE, AN. The LTEE as a typical case (GE2) is asserted; that special circumstances limit the generalisation (GE3) is answered against the argument by Day's own remark that the LTEE is asexual (ROOT-M, Responses); what would count as showing sufficiency (IG3) is not stated.
**Codes D:** W2c · QMf(RH?) · R1 · GE2=S GE3=A- AN3=S IG3=U

**K.** "No critic in the corpus addresses ROOT as a whole" (claim file, Responses; a statement about the corpus). The nearest is Hancock's track-record argument (node ROOT-PG, not load-bearing): "any new idea must run the gauntlet and be able to survive the theoretical edifice of population genetics". C: Day's demonstration fails, and the standard account stands until a challenger survives its record. G: the attacks on branches A, B and F; the field's predictive record. W (unstated): the record of a theory at one scale is a precedent for its adequacy at the scale in dispute, and the challenger carries the whole burden. Q asserted: "The blunt fact of the matter is Vox Day's math can't do any of this." (RH-15, reading-dependent in the claim file). For the negative claim (that the demonstration fails) the licence is adequate once any necessary branch fails, so no mismatch is coded. R: none stated. Schemes: PC, EX, IG. Whether the precedent's cases differ from this one in a relevant way (PC1: the record is microevolutionary, as the claim file notes) is not answered by the critic.
**Codes K:** W2c · QM0 · R2 · PC1=U EX5=S EX6=S IG2=S

**U.** No verdict is asserted (`pending`). The audit still makes one argument here, in the `load_bearing` comment: "it fails if its universal quantifier fails for any mechanism". C: ROOT stands or falls on the conjunction over mechanisms. W: a universal impossibility claim is defeated by one admissible mechanism, and the standard model is the default against which admissibility is judged (stated on the methods page as a stance, not at the node). Q: no conclusion drawn; matched. R: what would make the audit conclude that ROOT *stands* is nowhere recorded (no aggregation rule; MA-11). Scheme: IG. Who has the burden (IG2) is asserted as a stance; how strong the proof must be (IG3) is unanswered.
**Codes U-agg:** W1c · QM0 · R2 · IG2=S IG3=U

### 3.2 ROOT-M (Day). I pending / F n/a / E pending

**D.** C: every named mechanism is excluded: "So is any and every evolutionary mechanism, with the exception of three minor ones." G: the LTEE as one experiment in which several mechanisms run together; nine rows of the catalogue computed or bounded, three partial, five asserted and not computed (R5 draft). W (unstated): a mechanism with no computed bound of its own is covered by the aggregate LTEE bound or by the burden on whoever proposes it (the claim file: "Both are positions on who must compute, not computations"). Q asserted: "any and every" (level 5), with the exception stated in the same sentence. Licensed: level 3 for the computed rows, none for the five asserted rows. R: stated (three exceptions; relictation accepted). Scheme: IG. Day's premise that no calculations "were ever attempted or provided" is answered against him by the claim files (KITTENS, Hancock, Mansfield and Nesslig20 give numbers), with the split that no critic calculation of ILS is in the corpus.
**Codes D:** W2c · QMw · R0 · IG0=S IG1=A- IG2=S IG3=U

**K.** "no critic engages the table as such". The critics' route through the table is its neutral rows; that argument is laid out at B and is not counted here.

**U.** No verdict (`pending`). The audit's own claim is the catalogue: five rows "asserted but not computed". C: the corpus holds no quantitative exclusion for those rows. G: keyword search over harvested text. W: a universal claim needs a computed exclusion per mechanism (stated in the `load_bearing` comment). Q: worded as a statement about the corpus; matched. R: recorded ("paywalled books may contain computations for the five 'asserted' rows"). Scheme: IG, used by the audit itself. Would a computation be known to the audit if it existed (IG0)? The file answers against its own inference: the book is unread.
**Codes U-cat:** W0c · QM0 · R0 · IG0=A- IG1=A+ IG2=S IG3=U

### 3.3 ROOT-FM (Day). I pending / F pending / E contested ("leaning critic")

**D.** C: substitution density is overdispersed and clusters into "mesas"; "I propose the term sigillation for the hypothesis that some of these mesa regions represent deliberate genomic modification". G: the T2T ape alignment (named, public); no statistic, window or code published as of the 2026-10-10 refresh. W (unstated): a contiguous block of excess substitutions is a sign of a discrete event and not of a locally high rate shared across lineages. Q asserted for sigillation: "Sigillation is no more proof of IGM than relictation is. But it may be initial evidence of IGM." (level 1 to 2). Licensed: level 1 to 2. Matched; this is among the best-qualified Day statements on the 33 nodes. (The level-5 sentence of the same post is node FM10.) R: stated. Schemes: SG, AB. Whether the sign has other, more reliable accounts (SG2) and how the hypothesis compares with alternatives (AB2, AB3) are not addressed in the post; that it is better to keep inquiring than to conclude (AB4) is answered by Day himself.
**Codes D:** W2c · QM0 · R0 · SG1=U SG2=U AB1=S AB2=U AB3=U AB4=A+ GE1=S

**K.** None recorded. No critic had replied when the node was written; the six-point critic case in the claim file is "the audit's steelman of the critics; marked inference". Nothing is counted for K. The audit's authorship of the opposing case is taken up in section 7 and finding AS-06.

**U (external `contested`, leaning critic).** C: the pattern Day describes exists and does not discriminate between his hypothesis and a shared-rate account. G: the audit's own processing of the alignment: 32 to 53% of human-mesa windows lie inside chimp mesas against a 0.56 to 1.0% background; a shared-rate null reproduces 64 to 69% of human mesas; the four registered discriminating cells fall on the critics' side; one chrX window remains on Day's. W: (i) an engineering event confined to one lineage would not be shared across lineages (stated, as the critic steelman's point 3); (ii) the audit's windows and statistic stand in for Day's unpublished ones (stated: "No code, mesa coordinates, window size or dispersion statistic released by Day"); (iii) the shared-rate null is a fair neutral model (contested; the Day-side objection is recorded: it "borrows other lineages' variation and is not a mechanistic neutral model"). Q: `contested`, "leaning critic", with the remaining Day-side cell named. Matched. R: recorded. Schemes: SG and AB turned round, RC, MW. The inputs are not the author's (RC1 answered against: his method is unpublished, and the verdict is limited accordingly); whether the null presupposes the critics' answer (MW5) is raised in the file and not answered. Non-release is listed beside the grounds and is not used as one: internal stays `pending` "until Day releases his method/window/statistic".
**Codes U-ext:** W0c · QM0 · R0 · SG2=A+ AB2=A+ RC1=A- RC3=A+ MW5=U

### 3.4 FM10 (Day). I pending / F n/a / E contested ("leaning critic")

**D.** C: "What we do know is that neither natural selection nor neutral diffusive drift can still be considered viable candidates." (the claim file notes that in context it means "can no longer be considered viable"). G: the mesa pattern. W (unstated, and not found in Day's corpus by the claim file's own search): neutral drift implies a uniform rate per window, and a pattern that selection and drift can both contain excludes both. Q asserted: "What we do know is" (level 5; tagged dialectic). Licensed: level 1 to 2. R: none. Schemes: AB by elimination, SG.
**Codes D:** W2c · QMf · R2 · AB2=U AB3=U SG2=U GE1=S

**K.** None recorded (as at ROOT-FM).

**U.** External: as at ROOT-FM (same comment, same check); not counted again. Internal stays `pending`: the audit found no stated premise to test and declined to call it `non-sequitur` (N2d) on its own reconstruction. The same treatment is given to a critic's unretrieved method (C5 in the rule's table, `pending`).

### 3.5 A (Day). I holds / F n/a / E contested

**D.** C: "F_max = maximum achievable fixations", with a shortfall of 10^5 to 10^6. G: G_f from the LTEE, divergence time, generation length; the arithmetic. W: G_f is constant in time and carries over to any organism as an upper bound (stated in another text, the 3.0 paper's "ceiling"); fixations scale linearly with generations (unstated). Q asserted: "maximum achievable" (level 5). Licensed: level 3 (an asexual system, one regime). R: none. Schemes: AN, GE, CE.
**Codes D:** W1c · QMf · R2 · AN1=S AN3=S AN4=U GE2=S CE2=U

**K.** The scaling objection; as at A2e, not counted here.

**U (internal `holds`).** C: the arithmetic reconciles for the 2025 and 3.0 versions. G: the recomputation table in the claim file (scratch script, "not committed"). W: internal means arithmetic on the author's stated inputs (stated). Q: scoped in the comment to "(2025, 3.0)"; the 2019 table, which does not reconcile, is outside the quoted Statement. Matched. Scheme: RC.
**Codes U-int:** W0 · QM0 · R0 · RC1=A+ RC2=A+ RC3=S

**U (external `contested`).** C: whether G_f bounds a recombining genome is unsettled; "which model holds is branch B". G: the F2 simulation (free recombination to 272 active loci; the 1.5 to 172x factor is labelled "EXTRAPOLATION"); Weissman and Barton 2012, not reprocessed. W: the multi-locus model and W&B's asymptote represent hominid adaptive substitution (stated with its regime), and W&B 2012 is a sound benchmark (not stated at the node). Q: `contested`, with flip conditions (adaptive share 13 to 27%). Matched. R: recorded. Schemes: MW, EX.
**Codes U-ext:** W0c · QM0 · R0 · MW1=A+ MW2=S MW3=A+ MW5=A+ EX5=U EX6=S

### 3.6 A2e (Day). I non-sequitur / F pending / E contradicted (SCOPED)

**D.** C: "Whatever number the LTEE produces, it is the empirical ceiling on what evolution can accomplish when every tool in its kit is deployed simultaneously under ideal conditions." G: the LTEE's conditions (large populations, short generations, strong selection). W (unstated): conditions that are more favourable in the respects Day lists make the per-generation fixation rate higher than in any other organism, whatever the differences in recombination and in mutations per genome. Q asserted: "It is an unattainable ceiling, the absolute best-case scenario, the performance of a Formula One car used to benchmark a horse-drawn cart." (level 5; tagged dialectic). Licensed: level 2 (an analogy from one system). R: none. Schemes: AN, GE. The differences that would undermine the analogy (AN3: recombination; 38.4 new mutations per haploid human genome against 4.1e-4 per LTEE genome, both Day's own figures) are not addressed.
**Codes D:** W2c · QMf · R2 · AN1=S AN3=U AN4=U GE2=S GE3=U

**K.** C: the LTEE rate is no ceiling for humans; after scaling by mutation supply the gap closes (KITTENS) or is about 2x (Hössjer, an ally). G: genome size and mutation rate ratios; the LTEE is "largely nonrecombining". W: adaptive fixations scale with mutation supply (stated, and flagged by its authors as an illustration, RE-09). Q: offered as illustration; matched. R: stated. Schemes: AN (attacking through AN3), CE. Interfering factors (CE2: linkage, cost) are not computed by any critic.
**Codes K:** W0c · QM0 · R0 · AN3=A+ CE1=S CE2=U

**U (internal `non-sequitur`).** The verdict field carries no comment and names no clause of rule N. From the Check section: the conclusion is drawn "from the paper's own tables" and is "strengthened by the supply point (humans 19-57x LTEE population supply per generation)". C: the ceiling does not follow from Day's premises. W: a general ceiling drawn from one asexual system is "stronger than the premises support" (N2d, in the verdict rule, not at the node); and supply bears on the rate, which is the critics' premise and not Day's ("Day applies no supply scaling"). Q: categorical; licensed as a judgement that the generalisation outruns its premises. R: no condition recorded under which the internal verdict would be withdrawn. Scheme: RC. Whether the inputs are only the author's (RC1) is asserted, not shown, because the supply point enters.
**Codes U-int:** W1 · QM0 · R2 · RC1=S RC3=A+ RC5=A+

**U (external `contradicted`, SCOPED).** C: "contradicted for rate_human <= 1/G_f read as a per-generation count of adaptive fixations of any effect size, coding-only, on model-inferred alpha". G: Uricchio, Petrov and Enard 2019, lower 95% HPD alpha 0.096, giving 798 against the flip of 191 on the audit's most Day-charitable denominator; Boyko's lower limit 599. W: (i) a published, model-inferred alpha measures the number of adaptive coding substitutions on the human lineage (stated as a condition; the Day-side point "the figure is a model inference" is kept in the file); (ii) the ceiling is to be read as a count of adaptive fixations, "because A2e's formal statement is a count, so the reading is fixed". The formal statement is the audit's text, and Day's stated basis is "total throughput — every fixation, regardless of mechanism", on which the file says "NOT yet `contradicted`: that waits on A5c"; (iii) the flip of 191 and a 25% haircut mark materiality. B: two published estimates and one baseline. Q: `contradicted` (level 5) with the scope and conditions in the comment. Word above licence, comment at licence. R: recorded ("A2e survives if ~36% or more of the compounded residual is artefact"; strong-effect reading `contested`). Schemes: EX, MW, TR. The estimate rests on a contrast that assumes the standard neutral model for the reference class of sites, which is the framework in dispute (MW5), and that is not answered at the node; whether Day would accept the reading scored (TR3) is unanswered; the rule that fixed the reading was changed on the day it was applied (TR4, answered against, and disclosed on the methods page).
**Codes U-ext:** W0c · QMw · R0 · EX1=A+ EX2=A+ EX3=A+ EX5=A+ EX6=S MW2=U MW5=U MW6=U TR2=A+ TR3=U TR4=A-

### 3.7 A3 (Day). I holds / F partial / E contested

**D.** C: "it requires a minimum of 15,000,000 mutations to become fixed in the human population"; "~20 million fixations required on human lineage". G: CSAC 2005 (35M substitutions, 5M indel events). W (unstated): every difference between two reference genomes is a fixation that had to be produced on one lineage after the split. Q asserted: "a minimum of" and "~". Licensed: the audit's counts (17.2 to 17.9M fixed events per lineage) sit above 15M and near 20M, so no mismatch is coded. R: none. Schemes: SG, EX.
**Codes D:** W2c · QM0 · R2 · SG1=S SG2=U EX3=S

**K.** C: the count includes polymorphism: "The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species." (Mansfield, quoted at B6). G: none numeric. W: stated. Q: "some"; matched. R: none.
**Codes K:** W0 · QM0 · R2 · SG2=S

**U (internal `holds`).** Arithmetic 35 + 5 = 40, halved. "Arithmetic audit (python3 -I, scratch). Review: pending."
**Codes U-int:** W0 · QM0 · R0 · RC1=A+ RC3=S

**U (fidelity `partial`).** C: CSAC is read with a flagged omission. G: CSAC's text in hand. W: the two-lineage reading of "five million insertion/deletion events" is right; the alternative reading was tested and gives an implausible indel-to-SNV ratio. Scheme: TR.
**Codes U-fid:** W0 · QM0 · R0 · TR1=A+ TR2=A+

**U (external `contested`).** C: the 20M magnitude is corroborated; the polymorphism share on the chimpanzee side and the T2T question are open. G: data the audit processed (21.05M events per lineage on hg38 against panTro6; 17.2 to 17.9M fixed; 24.14M on T2T). W: stated. Q: `contested`. This is a mismatch in the other direction, not counted by the rubric: three data counts corroborate Day's magnitude and the verdict word does not say so (see AS-11). R: recorded.
**Codes U-ext:** W0 · QM0 · R0 · RC1=A+ RC3=A+ SG1=A+ GE3=A+

### 3.8 B (Day). I non-sequitur (reading-dependent) / F partial / E contested

**D.** C: neutral theory cannot supply the fixations: "The adaptive substitutions cannot be paid for; the neutral substitutions cannot be finished, because the pipe that would finish them never fills." G: the Hard Limits derivation k(T) = μ F(T). W (unstated): the lineage's pipe starts empty, or nearly, at the split, so a deficit at current size is a deficit for the lineage. Q asserted: "never fills" (level 5); and, tagged rhetoric (RH-10): "There is absolutely nothing Dennis McCarthy or anyone else can do at this point to salvage either natural selection or neutral theory". Licensed: level 3, at current size, which the same paper's abstract states ("residual drainage from the smaller populations they descend from"). R: stated elsewhere in the paper. Schemes: CE, MW.
**Codes D:** W2c · QMw+RH · R1 · MW2=S MW3=U MW6=U MW7=A- CE2=A-

**K.** C: "what you're left with is a neutral substitution rate that's equal to the mutation rate" (Hancock); "The ‘pipeline’ would have been full from the X generations preceding that point in time." (Mansfield). G: 2Nμ × 1/(2N). W: the lineage is at, or near enough to, the steady state the identity assumes. One critic states the condition ("It needs the elapsed time to be long compared with the fixation time."); none gives a sourced ancestral demography ("Mansfield offers no sourced demography"). Q asserted: "equal to" (level 4 to 5). Licensed: level 3. The limit is stated on the critics' side. R: stated by one critic. Scheme: MW. Whether the result survives a reproduction law with covariance (MW4) and whether N_e near 10^4 presupposes the model in dispute (MW5; Day calls it circular, B3h) are not answered by the critics.
**Codes K:** W0c · QMw · R1 · MW2=S MW3=U MW4=U MW5=U MW6=S

**U (internal `non-sequitur`, reading-dependent).** C: on the reading under which the quoted sentence is most defensible, the sentence needs an empty pipe that the paper's own text excludes (N2b). G: five readings of "nearly empty" with a registered edge at fill 0.30: 0.697 over 6.5 My (rhetoric, so `holds`, scoped to B2), and 0.256, 0.281, the current-size reading and 0.025 over 2 My (dialectic, so `non-sequitur`). W: (i) the "remotely close" test decides whether the sentence is dialectic; (ii) the field takes "the reading under which the QUOTED STATEMENT is most defensible ... not the reading best for Day"; (iii) N2b. All three are stated at the node. All three are contested inside the project (MA-02, MA-03, TV-08). Q: `non-sequitur` with "reading-dependent" and the table beside it. Word above licence, comment at licence. R: recorded (the other reading and its verdict). Schemes: TR, RC. Would Day accept either reading as what he meant (TR3)? Not answered, and it cannot be without asking him. The selection rule was redefined four minutes after the checks were integrated (TR4, answered against; methods page). The move of this field had "no review file" (RC3 unanswered).
**Codes U-int:** W0c · QMw · R0 · TR1=A+ TR2=A+ TR3=U TR4=A- TR5=A+ RC3=U RC4=A+

**U (fidelity `partial`; external `contested`).** No comment at either field; external "stays with B1c and B4a". No argument is stated at the node, so none is laid out (section 5.1).

### 3.9 B2 (Day). I holds / F unverifiable / E contested

**D.** C: "The domain of k = μ is confined to demographic conditions that no non-endangered species is capable of meeting." G: X = (V_k + 2)·G/16; a Wright-Fisher demonstration. W: stated (the claim concerns fixations produced at current size). Q asserted: "a hard ceiling", "no non-endangered species" (level 5). Licensed: level 3, inside his model with an unsourced V_k; the abstract states the current-size limit, and its "about ten thousand" is not what the paper's table gives. R: three objections pre-empted in the text. Scheme: MW (his own model to real species).
**Codes D:** W0 · QMw · R0 · MW1=A+ MW2=S MW3=S MW4=S MW6=U MW7=A+

**K.** "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral." (Mansfield). The comment predates the paper and "is aimed at a different statement" (claim file). C: drift operates at every N. G: none. W (unstated): the textbook account. Q: matched on the existence reading (RH-18 is reading-dependent). R: none. Scheme: EX.
**Codes K:** W2 · QM0 · R2 · EX3=S EX6=U

**U (internal `holds`).** C: on the paper's own text the claim holds; "rule C not needed". G: the abstract's confinement to current size (quoted); the exact chain reproduces Day's demonstration; one sub-prediction of the audit failed and is reported; a slip of "two orders" against about eleven is ledgered as immaterial. W: scope S1, the current-size reading, and the 25% materiality line. Scheme: RC, TR.
**Codes U-int:** W0 · QM0 · R1 · RC1=A+ RC2=A+ RC3=A+ RC4=S TR3=A+

**U (fidelity `unverifiable`; external `contested`).** Fidelity is rule F applied (uncited inputs are not thereby false): no mismatch. External has no comment and no argument at the node.

### 3.10 B3 (Day). I pending / F partial / E contradicted

**D.** C: k is not μ: "In mammals, census populations exceed diversity-derived N_{e} by 19- to 46-fold."; "it yields k = 0.743μ, confirming Balloux and Lehmann’s finding"; "gives k = 32.3μ, not k = μ." G: census against N_e; four generations of census data; a pedigree mutation rate against a required substitution rate. W: for the first leg, stated and later withdrawn by Day (B3g); for 32.3 (unstated): a required rate computed from the difference count and the assumed time is a measurement of k. Q asserted: "confirming", "not k = μ" (level 5). Licensed: level 2 at most for 0.743 and 32.3. R: the N/N_e leg withdrawn by its author within a day of the objection. Schemes: EX, SG.
**Codes D:** W2c · QMf · R1 · EX3=A- EX5=U SG2=U GE2=U

**K.** C: the fixation probability is 1/(2N) in the census N: "The fixation probability of a single new mutant in both chains: exactly 1/(2N_census), to fifteen decimal places." (keruru). G: exact Markov chains; "code not retrieved". W (unstated): parents are drawn exchangeably. Day's objection is on record: "his sweepstakes parent is drawn uniformly at random — setting the one parameter in dispute, the covariance between who breeds and what they carry, to zero by fiat." Q: exact inside the chains; matched for that claim. R: none ("the critics have not tested a non-exchangeable reproduction law").
**Codes K:** W2c · QM0 · R2 · MW1=S MW2=U MW4=U MW5=U

**U (external `contradicted`).** C: the listed k/μ values do not fit the world. G: (a) Day's withdrawal of the N/N_e leg; (b) simulation: the Balloux and Lehmann effect is reproduced and is −2% to +38% at human-like parameters, and the mechanism behind 0.743 "is falsified by simulation"; (c) 32.3 is "contradicted per-site" after an ancestral term. W: (a) an author's withdrawal settles the external status of what he withdrew; (b) a simulation with exchangeable offspring represents fixation in real populations. Neither is stated at the node; (b) is the standing warrant the methods page states globally ("consistent (or inconsistent) with the standard model"), and it is the premise Day disputes. Q: `contradicted` and "falsified", with no in-model wording at the node. R: the condition under which the verdict would fail (a reproduction law outside the exchangeable class) is recorded at B7, not here.
**Codes U-ext:** W1c · QMf · R2 · MW1=A+ MW2=U MW3=S MW4=U MW5=U MW6=U MW7=A-

### 3.11 C2 (Day). I non-sequitur / F unverifiable / E contested

**D.** C: "All three loci independently converge on d ≈ 0.45, consistent with Neolithic/Bronze Age demographic structure." G: fitted d of 0.49, 0.49 and 0.38 at three loci (the loci named differ between two of his papers). W (unstated): d is identified separately from the selection coefficient. Q asserted: "independently converge" (level 4 to 5). Licensed: level 2. His first version states the sensitivity ("When selection coefficients are reduced by 25%, the mean optimal d increases to 0.56"). R: stated there. Schemes: GE, CC, AB.
**Codes D:** W2c · QMw · R1 · GE1=S GE2=U GE3=U CC3=A- AB2=U

**K.** C: d "would clearly have changed during human evolution" (Camestros); "Will does not explain what it actually means" (Nesslig20). G: none. W: stated. Q: matched (Day's own table has d falling from 0.53 to 0.015). R: none. Schemes: GE, IG. The complaint that d is undefined is answered against the critics by a paper they had not engaged ("critics did not engage the integral").
**Codes K:** W0 · QM0 · R2 · GE3=S IG1=A-

**U (internal `non-sequitur`, N2d).** C: "independently converge" is stronger than the premises support. G: Day's own sensitivity paragraph (from version 1 of the paper; the scored abstract is version 2). W: stated. R: implied by the external comment (the scale of s).
**Codes U-int:** W0 · QM0 · R1 · RC1=A+ RC3=A+ RC5=A+

**U (external `contested`).** C: unsettled; "published s are per-generation slopes (d = 1)". G: an age-structured simulation (d·s exact for hazard-scale s, "Day-side point"; factor 1 for per-generation s). W: the simulation captures the relevant demography (methods page); published coefficients are per-generation (asserted while "which s scale the cited papers use is unretrieved").
**Codes U-ext:** W1c · QM0 · R0 · MW1=A+ MW2=S MW3=S EX3=S

### 3.12 F1 (critic). I holds / F n/a / E contested

**D.** As at F1a.

**K.** C: "The time it takes for one allele to get fixed is not important, it is the time BETWEEN successive fixations that is important." G: a pipeline analogy (trucks from New York to Los Angeles). W (unstated): fixations at different loci proceed independently, with no cap from linkage or cost. Q: as a point of logic, matched. R: none. Scheme: AN. The differences that would undermine the analogy (AN3: trucks do not interfere with each other or share a mortality budget) are not addressed.
**Codes K:** W2c · QM0 · R2 · AN1=S AN3=U AN4=U

**U (internal `holds`; external `contested`).** C: dividing elapsed time by a latency is not a bound on throughput; whether pipelining is feasible is open. G: a simulation with independent loci (in-transit count 333.3 against theory 335.5). W: a queueing identity (stated). Q: "pipelining is shown possible, not feasible"; matched. R: recorded (the parameters "avoid selective load by construction").
**Codes U-int:** W0 · QM0 · R0 · MW1=A+ MW2=A+ MW7=A+
**Codes U-ext:** W0 · QM0 · R0 · MW3=A+

### 3.13 F1a (Day). I non-sequitur / F n/a / E pending

**D.** C: "The MITTENS calculation does not assume sequential fixation."; "dividing total generations by per-fixation time to get maximum achievable fixations is not an assumption of sequential processing. It is also a throughput calculation". G: the LTEE count is an aggregate; (2/s) ln(2N_e) = 19,800. W: a time per fixation can stand for the spacing between fixations (stated, and it is the point in dispute). Q asserted: "does not assume"; "So using the 1,600 generations rate was extremely generous" (level 5). Licensed: the first half (an aggregate count contains parallelism) is supported; the second is not. R: none. Schemes: CE, EX. The input s = 0.001 misreads its source (F3a, fidelity `misread`).
**Codes D:** W0c · QMf · R2 · CE1=U EX3=A-

**K.** C: the calculation is serial. G: a slide and a pasted quotation. W: dividing a time by a per-fixation figure is a sequential assumption. Scheme: TR. Day disowns the reading for the LTEE figure and confirms it for the 19,800 figure, so the attribution is half right; the critics do not separate the two.
**Codes K:** W0c · QM0 · R2 · TR1=S TR2=U TR3=A-

**U (internal `non-sequitur`).** The field has no comment and names no clause. C: dividing by a latency as if it were a spacing does not follow. G: a simulation at Day's 4Ns = 40: 7.1, 71.9 and 702 fixations at 1x, 10x and 100x the serial supply. W: a model with independent loci and a supply set by the audit shows what follows from Day's premises. But the supply levels are the audit's, and on Day's own premises (width capped by cost or interference) the count could sit at the boundary: "the serial reading (7) is right only at the boundary supply"; "interference and human supply untested". Q: categorical word, limit in the Check paragraph. R: recorded there. Schemes: RC, MW.
**Codes U-int:** W1c · QMw · R0 · RC1=A- RC3=A+ MW3=A+ MW5=U MW7=A+

### 3.14 H (Day). I holds / F partial / E contested

**D.** C: "Haldane calculated that mammals could fix no more than approximately one beneficial substitution per 300 generations"; "Achievable fixations (Haldane + d) = 146,250 / 300 = 487 fixations". G: Haldane 1957; the arithmetic. W (unstated): Haldane's parameters (10% selective mortality, hard selection) hold for the hominid lineage over the whole window. Q asserted: "no more than" (level 5 as applied to the lineage). Licensed: level 3, in Haldane's regime, where the audit's runs reproduce it. The same paper has a scope reply and still compares 487 with 20M. R: narrowed by Day's own later retraction (H1). Schemes: EX, MW. What other specialists say (EX5: Nunney 2003) is answered by assertion ("mechanisms for redistributing a fixed reproductive budget"), without engaging the source.
**Codes D:** W2c · QMw · R1 · EX1=A+ EX3=A+ EX5=S MW2=S MW3=U MW4=S MW6=U

**K.** C: the limit bounds selected substitutions only (Nesslig20: it "does not apply to drift"). G: neutral theory. W: most differences are neutral; Day concedes this premise in H1 ("the great majority"). Q: matched. R: none. No critic computes whether the adaptive share is payable, and "no critic in the corpus engaged Nunney 2003".
**Codes K:** W0 · QM0 · R2 · EX5=A+ MW3=U

**U (internal `holds`).** Arithmetic 300, 487, 41,068.
**Codes U-int:** W0 · QM0 · R0 · RC1=A+ RC3=A+

**U (fidelity `partial`).** The 300 figure is judged accurate through Nunney's report; "primary Haldane 1957 not retrieved". Stated at the field.
**Codes U-fid:** W0 · QM0 · R0 · EX3=S

**U (external `contested`).** As at H8.

### 3.15 H8 (Day). I holds / F pending / E contested

**D.** C: "ksel = smax · d / [2L · ln(2Nₑ)] ... ≈ 8.3 × 10⁻¹²"; "The defense is partially correct and entirely fails to deliver k = μ." G: "the differential available to any individual is bounded by what the organism can physically achieve." W: the selection coefficients of concurrent sweeps sum to no more than s_max of about 1 (stated; contested through soft selection). Q asserted: "None of them raises smax above order unity"; "entirely fails" (level 5). Licensed: level 3 (under hard selection through the death budget). R: Day's retraction of the use of this term as a bound on total k ("a category error", H1), in a later source. Schemes: CE, MW.
**Codes D:** W0c · QMf · R1 · CE1=S CE2=S MW2=S MW6=U EX5=U

**K.** None recorded: "no critic engaged the formula or the s_max ≈ 1 argument". The counter-argument at this node (Nunney 2003, Keightley 2012) is literature applied by the audit.

**U (internal `holds`).** Arithmetic.
**Codes U-int:** W0 · QM0 · R0 · RC1=A+ RC3=A+

**U (external `contested`; the same comment stands at H and H5).** C: the 1/300 figure is reproduced in Haldane's regime; "slower than 1/300" is conditional on K and on the survival horizon; the budget's size is ln R; the premise that s_max bounds the sum "is contradicted in-model under soft selection (purely relative fitness assumed) and holds under hard selection only through the death budget". G: 726 jobs and two scale-up stages to K = 64,000, with the audit's missed predictions printed. W: the treadmill model and the mapping s_max·d = ln R (stated as "the audit mapping"). Q: `contested`, every clause with its regime. Matched. R: recorded (no K trend; horizon; "no sourced net hominid R"). Scheme: MW. The one question left open is the anchor (MW6): no observation of the lineage is reproduced. This is the best-warranted verdict comment of the fifteen.
**Codes U-ext:** W0c · QM0 · R0 · MW1=A+ MW2=A+ MW3=A+ MW4=A+ MW5=A+ MW6=U MW7=A+

---

## 4. Compact table (18 nodes)

One layout per party per node: the party's main argument, and for the audit its most consequential decided verdict (named). Coded from the claim file's front matter, Statement and Responses sections and the opening of each Check paragraph (the first 430 characters), so a limit stated later in a Check paragraph may have been missed. "—" = none recorded; "as at X" = the same argument, counted at X.

| Node (side; I / F / E) | Day side | Critic side | Audit |
|---|---|---|---|
| B1 (Day; holds / n/a / contested) | Finite-time count differs from the steady-state rate; "At generation zero, the subsitution pipeline is empty." Well qualified ("It is a rate, not a count"); the empty start is the contested premise, and his later "The pipeline was full" is unreconciled. D: W0c · QM0 · R1 · MW2=A- MW3=U MW6=U | Mansfield: "would have been full"; no number. K: W0c · QM0 · R1 · MW2=S MW3=U | E `contested`, whose comment says "contradicted for the human-chimp observable (B4a)" while B4a itself is `contested`: the comment is stronger than the node it cites. U-ext: W0 · QMf · R0 · MW1=A+ MW2=S MW5=U MW6=S |
| B1c (audit question; holds / n/a / contradicted) | "It’s functionally nonexistent and empirically confirmed to be empty." then "The pipeline was full, but it was much shorter." Ground: ancient-DNA stasis read as a sign of an empty pipe. D: W2c · QMf · R1 · SG1=U SG2=U | Mansfield: Day's reply was "basically an assumption". K: W0 · QM0 · R2 · MW3=U | E `contradicted`: step histories from Yoo's ancestral N_e give an excess of 1.9 to 4.0x; the Check says this is "not an independent empirical finding". Word above licence, limit in the Check. U-ext: W0c · QMw · R0 · MW2=S MW5=A+ MW6=A+ EX5=U |
| B2b (Day; holds / unverifiable / contested) | X = (V_k + 2)G/16; "about ten thousand" against his own table. D: W0 · QMw · R0 · MW2=S MW6=U | — (Mansfield's comment addresses an earlier sentence) | I `holds`: the algebra matches a simulated N_e within 2.2%; "Inputs (human V_k, G window) not tested". U-int: W1 · QM0 · R0 · RC1=A+ RC3=A+ MW1=A+ |
| B3a (Day; holds / misread / contradicted) | k = 2Nμ × 1/(2N_e): "This cancellation is invalid." Withdrawn by Day (B3g). D: W0c · QMf · R1 · EX3=A- MW2=A- | as at B3 | E `contradicted` (no comment at the field): simulated P_fix = 1/(2N); the review notes it "is a theorem in this class ... so the run verifies the code; the verdict is provisional". U-ext: W1c · QMw · R1 · MW1=A+ MW2=U MW4=U MW5=U MW6=U |
| B3g (Day's concession; holds / accurate / supported) | "the two correctly cancel"; the covariance objection kept in the same post. D: W0 · QM0 · R0 · MW2=S | keruru's own retraction ("The claim about the substitution rate is withdrawn."). K: W0 · QM0 · R0 · | E `supported`: an identity and a concession, with the later tension ("false for any real population") recorded as two unsettled readings. U-ext: W2c · QMw · R0 · TR2=A+ MW2=U MW5=U |
| B4a (audit check; holds / accurate / contested) | — | — | E `contested`: the model with the sourced ancestral N_e overshoots the observed 1.23% by about 25%; "(mu, T, Ne_anc) underdetermined". The anchor test partly fails and is printed. U-ext: W0 · QM0 · R0 · MW1=A+ MW2=S MW5=A+ MW6=A- |
| B5 (critic; holds / accurate / contested) | as at B1 and B2 | as at B | E `contested`: "exact at steady state"; "The critics' stated totals assume stationarity." U-ext: W0 · QM0 · R0 · MW1=A+ MW2=A+ MW7=A+ |
| B6 (critic; holds / n/a / supported) | as at B1c | Mansfield: "The ‘pipeline’ would have been full"; stated as an assumption, no ancestral N_e. K: W0c · QM0 · R2 · MW2=S MW3=U | E `supported`: "full pipe gives k = mu ... (forward sim)" and Day's later concession. A simulation started full returns the full-start result; the anchor is CSAC's polymorphic share (B4a). U-ext: W1c · QMw · R1 · MW2=U MW5=U MW6=A+ |
| B7 (critic; holds / accurate / supported) | as at B3a | as at B3 | E `supported` (no comment at the field): simulation, Kimura, and Day's own paper; "Provisional (pending B3b)"; the untested non-exchangeable case is noted at the node. U-ext: W1c · QMw · R0 · MW1=A+ MW2=U MW4=U MW5=U EX5=S |
| C2a (Day; holds / unverifiable / contested) | d from life tables; "d ≈ 0.50 ± 0.10 represents a reasonable range". Hidden: published s are on the hazard scale. D: W2c · QM0 · R0 · MW2=U EX3=S | as at C2 | E `contested`: "a unit conversion, not a separate correction"; the scale of published s unretrieved. U-ext: W0 · QM0 · R0 · RC3=A+ EX3=U |
| E5 (critic; holds / accurate / pending) | The 3.0 paper reads the negative count as a biological result (claim file summary; the sentence was not read by this pass); corrected in Day's later paper. D: W2c · QMw · R1 · SG2=U | "A count of fixed mutations cannot be negative". K: W0 · QM0 · R2 · SG2=S RC1=S | I `holds`: recount from the papers' tables; the formula behind −906 "was not recomputed". U-int: W0 · QM0 · R0 · RC1=S RC2=A+ RC3=A+ |
| E6 (Day; holds / unverifiable / pending) | Day's self-correction: 5,496 strict against 8,679 naive; counts "are not well-defined quantities in this system ... (a 2–3× range)". Limits stated by the author. D: W0 · QM0 · R0 · GE1=A+ | — | I `holds`: Table 1 sums reproduce; state calls "not re-derived". U-int: W1 · QM0 · R0 · RC1=A+ RC3=A+ |
| F (Day; holds / partial / contested) | "k = μ gives the output rate once the process is running. t̄ = 4Nₑ gives the startup cost before any output appears." The startup applies only from an empty pipe. D: W1c · QM0 · R2 · MW2=U | as at F1 | I `holds`, moved from `non-sequitur` by scope S1 so that one step is not scored on two nodes (a rule decision in Day's favour). U-int: W0 · QM0 · R0 · TR2=A+ TR5=A+ RC3=A+ |
| F2 (Day; holds / n/a / contested) | "a hard limit on pipeline capacity of approximately 230 simultaneous sweeps". Hidden: interference in an asexual system carries over to a recombining genome. D: W2c · QMf · R2 · AN3=U GE3=U EX3=S | as at F1 | E `contested`: two engines and W&B agree within 6 to 10%; the extrapolation is labelled; "hard selection with linkage untested; tight linkage supports Day". U-ext: W0 · QM0 · R0 · MW1=A+ MW2=S MW3=A+ MW4=A+ MW6=U EX5=U |
| F3a (Day; holds / misread / contested) | "at s = 0.001 (the empirical mean for beneficial mutations in humans from Zeng et al. 2021)"; the source's figure is for negative selection. D: W0c · QMf · R2 · EX3=A- EX6=U | — (the objection is the audit's fidelity ledger) | F `misread` from the raw text; E `contested` because "no sourced human beneficial mean s is in the repo": unverifiable is not treated as false. U-fid: W0 · QM0 · R0 · TR1=A+ TR2=A+ RC3=A+ IG1=A+ |
| H1 (Day's retraction; holds / partial / supported) | "my error was in interpreting its output as a constraint on total k"; but also "The textbook k = μ identity is still falsified". D: W2c · QMf · R0 · SG2=U EX3=S | Nesslig20: the limit "does not apply to drift". K: W0 · QM0 · R2 · | E `supported`: the cost bounds selected substitutions only, which holds by the definition of the cost; no condition of failure recorded. U-ext: W0 · QM0 · R2 · EX5=A+ |
| H2 (literature, Nunney 2003; n/a / accurate / contested) | as at H8 | — (no critic engaged the paper) | E `contested`: the dependence on M reproduced; absolute values and the elimination by soft selection not reproduced by an "EXPLORATORY reconstruction ... adjusted twice after seeing results"; "Human M is unsourced". U-ext: W0 · QM0 · R0 · MW1=A- MW3=U EX6=S |
| H5 (ally, Hössjer; non-sequitur / pending / contested) | "Vox Day convincingly argues ..."; "perhaps more in line with equation (3)"; "I agree with this conclusion". The cost step is asserted. D: W2 · QMw · R2 · EX6=U CE1=S | — ("no critic engaged Hössjer's cost step") | I `non-sequitur`: 15,800 "is a rate scaling, not a cost computation"; his conditional is "mechanically confirmed" and recorded as payable at R of 2 to 3. U-int: W0 · QM0 · R0 · RC1=A+ RC3=A+ RC5=S |

---

## 5. What the layouts show across nodes

### 5.1 Verdict fields with no stated argument at the field

The 33 load-bearing claim files carry 74 decided verdict fields (27 internal, 19 fidelity, 28 external; `pending` and `n/a` excluded). **29 of the 74 have no comment at the field** (counted by script from the front matter): A2e internal; B fidelity and external; B1 internal; B2 external; B2b all three; B3 fidelity; B3a all three; B3g internal and fidelity; B5 internal and fidelity; B6 internal; B7 all three; E5 fidelity; E6 internal and fidelity; F fidelity and external; F1 internal and external; F1a internal; H2 fidelity. For most of them the grounds can be found in the file's Check section. Two of the five internal `non-sequitur` verdicts on these nodes (A2e, F1a) name no clause of rule N at the field, and two of the external `contradicted` or `supported` verdicts that rest on a simulation (B3a, B7) have no comment at all.

### 5.2 Where the audit's wording outruns its grounds

Ten of the 40 audit layouts carry a qualifier mismatch: two full (B3 external; the comment on B1 external) and eight in the word only (A2e external; B internal; F1a internal; B1c, B3a, B3g, B6, B7 external). **Seven of the eight decided `supported` or `contradicted` external fields on the 33 nodes are among them** (A2e, B1c, B3, B3a `contradicted`; B3g, B6, B7 `supported`); the eighth, H1, is true by the definition of the cost. In each of the seven the ground is a model result, an identity that holds inside a class of models, a published model-based estimate, or the author's own withdrawal, and the verdict word is the same one used where the audit processed data. The methods page already tells the reader to take such verdicts as "consistent (or inconsistent) with the standard model"; the node does not.

The reverse case exists once in what was read: A3 external is `contested` although three data counts made by the audit corroborate Day's magnitude.

### 5.3 Where the audit's argument is well formed

Thirty of 40 audit layouts have no mismatch, 29 state their warrant where the verdict is stated, and 32 record at the node the conditions under which the verdict would fail. The `contested` external verdicts on A, B4a, B5, F2, H and H8 carry every clause with its regime, print the audit's own missed predictions (H8) or a failed anchor (B4a: the model with the sourced ancestral N_e overshoots the observed divergence by about 25%), and state which side each open parameter favours. The recomputation questions are answered with evidence in 31 of 40 instances (asserted 6, against 2, unanswered 1). The audit declined to infer from Day's unpublished method to a defect (FM10 internal `pending`), declined to treat an unretrieved source as false (C2 and F3a fidelity and external), and moved one verdict in Day's favour so that a step is not scored on two nodes (F).

### 5.4 Opposing cases written by the audit

On 9 of the 33 nodes no critic argument is recorded (ROOT-FM, FM10, H8, B2b, B4a, E6, F3a, H2, H5). On six of them the case against the Day-side claim is supplied by the audit: a steelman written before any critic had replied (ROOT-FM, FM10), literature that "no critic in the corpus engaged" (H8, H2, H5: Nunney 2003, Keightley 2012) and the audit's own fidelity ledger (F3a). In the argument map 146 of 437 defeaters are attacks made by the audit's checks (prefix `chk:`): 100 on Day's nodes, 33 on critics', 6 on allies', 2 on literature nodes, 4 on its own checks and 1 on an unmapped statement; their `audit_status`, set by the audit, is upheld or partly upheld for all but 2, which are untested, and for none is it `not_upheld`. A further 88 are reviews attacking the audit's own checks (prefix `rev:`). The audit is, by count, the most active arguer in its own map.

### 5.5 The author's withdrawal used as a ground

Five external comments cite the author's own concession beside or in place of evidence: B3 ("N/N_e leg withdrawn by its author"), B3a (through B3g), B1c ("empty-start premise (withdrawn by Day, B1d)"), B6 ("Day's later concession") and B3g itself (`supported`). A concession closes a point between two parties (rule 9). It is an argument from the author's commitment, and it shows what the author now holds; it does not show how the world is, which is what the external column is defined to record. The claim files themselves record that Day's later text is "in tension with the concession" (B3g) and that he reversed himself on the pipe twice (B1c).

---

## 6. Fallacy audit, three parties

Codes: **observed** (an instance with a path), **risk** (the structure allows it; no instance confirmed in what was read), **not found**. Rhetoric tagged as such under rule RH is listed, because the question here is what was said and not whether it is scored.

| | The audit | Day | The critics |
|---|---|---|---|
| (i) Argument from ignorance | **Observed, structural:** `holds` is assigned where no defect was noticed (methods page: 58 of 131 on files still `extracted`), which is the form "true because there is no evidence against it" (AT-25); agrees with MA-07. **Observed, corrected:** B3's Check first says 32.3 "has no derivation" and a later paragraph finds it ("Day's arithmetic on a base-pair numerator"). **Risk, disclosed:** "No critic in the corpus addresses ROOT as a whole" and the five "asserted" rows of ROOT-M, each with the caveat that the book is unread. **Not found** where it was most expected: Day's unpublished mesa method is listed beside the grounds of ROOT-FM and is not used as one; unretrieved sources give `unverifiable`, not `misread` | **Observed:** ROOT and ROOT-M ("No calculations of their effects, individual or cumulative, were ever attempted or provided", so the mechanisms cannot suffice); the stated burden "they gesture at alternative mechanisms without demonstrating"; FM10 (a pattern not yet explained by two mechanisms excludes both) | **Observed:** "Will does not explain what it actually means" used to dismiss d, which a paper they had not engaged defines; "Vox Day's math can't do any of this" (no predictions, so wrong), where the claim file records that Day does make a testable prediction |
| (ii) Consensus or authority as ground truth | **Observed, structural, disclosed on the methods page and not at the nodes:** standard population genetics is "the default model"; rule F exempts "standard values" from citation and flags N_e of about 10^4 as contested; 6 of the 8 decided `supported` or `contradicted` external fields on these nodes rest on the standard model or an identity inside it, and a seventh on a published estimate inferred with it. The audit's most often unanswered question is whether the model or estimate presupposes what Day disputes (MW5, 9 times) | **Observed:** endorsements offered as support (Tipler's "most rigorous mathematical challenge", tagged rhetoric; Hössjer's "convincingly argues"); a chatbot's concession used as confirmation (B3a: "LLM concedes both propositions"); Haldane's figure used as a bound without his regime | **Observed:** "the theoretical edifice of population genetics" as the test a challenger must survive; credentials of Day's endorsers (ROOT-EP); one-line appeals to the textbook with no evidence (Mansfield at B2) |
| (iii) Straw man, or rebuilding into something the speaker would not accept | **Observed:** A2e external is decided on a reading "fixed" by the formal statement the audit wrote, while the reading Day states (total throughput) is left undecided; B internal is decided on the reading under which the sentence is "most defensible", which makes it scoreable and then wrong, and nobody has asked the author which he meant. **Risk:** reconstructions of unpublished methods (mesas; the B3 family; ST-11). **Kept:** verbatim quotation; the serial reading was tied to a quote before it was scored (F1a); F is no longer scored for F1a's step | **Observed:** the critics' reply described as not "a quantitative rebuttal", "contradicted by at least KITTENS, Hancock, Mansfield and Nesslig20, who give numbers" (ROOT file); Mansfield paraphrased as "it gets reset somehow" (B6 file) | **Observed:** the serial reading of F_max, which Day disowns for the LTEE figure (half right: he confirms it for 19,800); Camestros reviewed the first edition and says the "core argument hasn't changed", against the version drift (A file) |
| (iv) Shifting the burden of proof | **Observed, structural, disclosed:** "That places the burden of proof on the challenger; it is a stance" (methods page). The `load_bearing` comments say what makes ROOT fail and nothing says what would make it stand; the draft synthesis rule has statements for Day's branches only (AR-12). An inconclusive check leaves `contested`, and the default model is what stands behind `contested` | **Observed:** a universal impossibility claim defended by assigning the computation to whoever proposes a mechanism (ROOT-M: "positions on who must compute") | **Observed:** "any new idea must run the gauntlet"; "would have been full" offered as an assumption with no ancestral N_e, leaving Day to disprove it |
| (v) Equivocation across readings | **Observed:** one word, `contradicted`, for a data result and for a result inside a model (5.2; MA-05); `contested` in five senses (MA-08); `holds` for checked and for unexamined (MA-07); "most charitable" defined two ways before and after 2026-10-11 with stale comments left (MA-03); "ceiling" at A2e scored as a count of adaptive fixations under a node whose title is the general ceiling claim, so a tally reads *A2e contradicted*. **Kept:** the same sentence is read the same way across B, B2 and C (TR5) | **Observed:** N against N_e (conceded 2026-08-27); "lineage" as 2 My and as 6.5 My inside one paper; a time per fixation used as a spacing; "fixation" at 95% and by a strict rule (self-corrected, E6); 40M "single-nucleotide variants" that include 5M indel events; "impossibility" as a demonstration and, of one equation, as "a rhetorical device" | **Observed:** N = N_e in McCarthy's 50,000 × 9 million; "38M matches" on different bases (one scored `non-sequitur`, B5c); "Genetic drift happens in every population" (existence against sufficiency; RH-18 reading-dependent); per lineage against both lineages (A3d) |
| (vi) Genetic or ad hominem leakage: does who said it change the score? | **Risk; no scored instance found.** None of the 74 decided fields cites the author's identity as a ground, and a rule exists that credentials are not a rebuttal (ROOT-EP comment). But claim files carry markers about persons in "Weaknesses" sections ("keruru is an LLM-assisted blog author"; "KITTENS is AI-assisted and cites literature from memory"; "LLM-assisted; advocacy"), one of which weighs evidence by source ("stronger evidence than keruru alone"), and no rule says when a source's nature may bear on weight (AH2). Exposure differs by author by construction (rule N2b says so). The applier shares a model family with Day's co-author and with at least one critic source, so any leakage could run either way and is unmeasured | **Observed, in rhetoric:** post titles "Math Teacher Can't Math" and "The Education of a Population Geneticist"; "This objection misunderstands Haldane's argument." (RH-3) | **Observed:** "you're really just a crank" (relayed, RH-2); "AI-Generated Books" in a video title; "you probably should Google him and see that he's an ID proponent" (tagged dialectic as a disclosure bearing on an endorsement, which is the legitimate use, AT-17) |
| (vii) False balance | **Risk; observed in presentation.** Each check has a Day-side and a critic-side credit paragraph and the README pairs twelve points with twelve (MA-17). 20 of the 28 decided external fields on these nodes are `contested`. Conflicting prima facie evidence is not by itself a reason for a middle verdict (AT-29); where the audit's own data corroborate one side the word should say so (A3). The opposite risk is also recorded: the default-model stance, and ST-04's count that untested risk points to the critics' side 22 to 1 | **Not found.** The matching fault is a false dilemma: two mechanisms excluded, so a third (FM10) | **Observed, by a third party:** "McCarthy vs Vox was just two cranks battling each other" (relayed, RH-2) |

---

## 7. The ten rules of a critical discussion

**The governing fact.** The rules describe an exchange in which one party advances a standpoint, another doubts it, and both can answer. No such exchange has happened between the audit and anyone it audits: "None of the authors on either side has been contacted" (methods page). Day and his critics have had one with each other, in public, and the audit observes it. So the audit's row is scored for what it has done alone, and rules 1, 2 and 9 are marked untested where they need a second party. The audit is not a judge in this model. The model has no judge; "the participants themselves are to decide which party was successful" (AT-21). By the counts of 5.4 the audit is a third discussant with standpoints of its own.

| Rule | The audit | Day | The critics |
|---|---|---|---|
| 1 Freedom | **Untested.** Both sides are quoted verbatim and steelmanned. The audited parties have had no means to advance doubt where the verdicts are published; verdicts on named people are public without notice. Tagging a sentence `rhetoric` takes it out of scoring, in both directions | **Breached in rhetoric, kept in substance.** Personal attack counts against this rule (AT-88's context); the titles in 6(vi). "There is absolutely nothing ... anyone else can do at this point" declares the matter closed. He also quotes his critics at length and invites replication ("there is no need to take my word") | **Breached in rhetoric, kept in substance.** "crank", "AI-Generated", credentials. A 3.5-hour reply engages the argument |
| 2 Burden of proof | **Kept in form, untested.** Grounds are published and the checks re-run; nobody has asked. 29 of 74 decided fields carry no argument at the field (5.1). The burden for the default model is assigned by stance | **Breached for the universal claim** (five catalogue rows asserted, the computation assigned to others); **kept** for the computed rows and in publishing derivations | **Breached in places:** one-line assertions with no number (B2, B6); Nunney 2003, Hössjer's cost step and the fill-state question left unengaged. **Kept** by KITTENS, Hancock, Nesslig20, keruru, who compute |
| 3 Standpoint | **At risk; two instances** (A2e external and B internal are decided on readings the author has not been shown to hold; AS-04). **Kept** by verbatim quotation, scope rule S1, and tying the serial reading to a quote | **At risk; one instance recorded** (critics' reply called non-quantitative) | **Breached in part** (the serial reading; a first-edition review applied to later texts) |
| 4 Relevance | **Kept, with one exception by design:** the ledger drafts counter-rhetoric (RH2), which is persuasion and not argument; it is unposted | **Mixed by design:** he distinguishes rhetoric from dialectic and uses both | **Mixed:** credentials offered against arithmetic (ROOT-EP) |
| 5 Unexpressed premise | **At risk.** The claim files attribute "Implicit" premises to authors; internal verdicts under N2b and N2d turn on them. One good practice: before scoring FM10 the audit searched Day's corpus for the premise it would have attributed and, not finding it, left the verdict `pending`. No party has been asked whether a reconstructed premise is theirs. The audit's own unexpressed premises: 11 of 40 layouts | **At risk:** denies a sequential assumption while a figure he uses is a time per fixation (F1a); FM10's premise is nowhere stated | **At risk:** attribute the sequential assumption to Day without separating his two figures |
| 6 Starting point | **At risk; breach-like at bare fields.** The standard model is presented as a stance on the methods page, which is honest; at B3a and B7 a result inside the model stands as `contradicted` and `supported` with no such note | **At risk:** uses "N_e = 10,000 (standard effective population constant)" as a starting point (F1a quote) and elsewhere calls it circular (B3h) | **At risk:** N_e near 10^4 and stationarity are presented as common ground, which Day disputes |
| 7 Validity | **Kept by abstaining.** No inference to the root claim is drawn, because no rule for one exists (MA-11, TV-05). Node verdicts can be made valid by adding the premises of section 8.3, which is the point of this pass | **Breached at four of his load-bearing nodes** as the audit scores them (A2e, B, C2, F1a `non-sequitur`), subject to AS-04 and AS-05 | **Kept on the 33 nodes** (all critic nodes `holds`); one `non-sequitur` elsewhere (B5c) |
| 8 Argument scheme | **At risk:** a categorical word on a presumptive scheme in 10 of 40 layouts (5.2) | **Breached:** analogy, sign and generalisation treated as conclusive ("mathematical impossibility", "What we do know is"); 20 of 27 layouts over-qualified | **At risk:** the pipeline analogy and the steady-state identity carried to the lineage with the conditions unargued; 1 of 16 over-qualified |
| 9 Closure | **Kept alone, untested with others.** The audit has withdrawn findings against Day (methods page: three), corrected a 41x error of its own, and moved F back. Whether a defence has failed is decided by the check's author (MA-01); no outside doubt has been received, so no retraction has been owed | **Kept on specifics, the best record of the three on these nodes:** the N/N_e leg (B3g, "necessary to produce a 3rd Edition"), Term 3 (H1, "a category error"), the fixation counts (E6), the pipe (B1c). **Not kept upward:** the unrevised Zenodo copies still carry withdrawn values; the root claim was not narrowed after its branches were | **Kept where seen:** keruru's retraction; Hancock's same-video correction; Camestros's "the arithmetic itself isn’t wrong". Otherwise unknown |
| 10 Usage | **First half breached, second half kept.** The verdict vocabulary is "confusingly ambiguous" in three of its words (6(v)). The other party's formulations are interpreted "as carefully and accurately as possible": verbatim, hashed, with every plausible reading tabled. This is the audit's strongest rule | **Breached in places:** "impossibility"; "lineage"; a sentence in FM10 that literally says the opposite of what it means | **Breached in places:** N for N_e; "debunk" |

**Headline.** By these rules nothing has yet been resolved between the audit and the parties, because nothing has been put to them. The audit is strongest where it works alone (careful interpretation, rule 10's second half; self-correction, rule 9) and weakest where the rules need the other party or need its own words to be unambiguous (rules 1, 2, 3, 6 and 10's first half). Day's best rule is closure on specific points and his worst are the burden for the universal claim and the strength of his wording. The critics' best is validity on short identities and their worst are undefended one-liners and the serial reading.

---

## 8. Aggregates

Counted by script from the "Codes" lines of sections 3 and 4 (83 layouts: 46 in full, 37 compact). One rater. **These are not error rates and are not comparable across parties** (2.6): Day authored 24 of the 33 nodes and wrote at length; a critic layout is often one sentence; the audit has up to three fields per node and wrote its comments knowing they would be reviewed.

### 8.1 Per party

| | Day side | Critics | The audit |
|---|---|---|---|
| Layouts | 27 | 16 | 40 |
| Nodes without a layout of their own | 1 none recorded (B4a); 5 as at another node | 9 none recorded; 8 as at another node | 1 as at another node (FM10) |
| Warrant stated where argued (`W0`) | 9 | 12 | 29 |
| **Hidden warrants** (`W1` + `W2`) | **18** (2 + 16) | **4** (0 + 4) | **11** (10 + 1) |
| of which contested by another party | 17 | 3 | 8 |
| **Qualifier mismatches** (`QMw` + `QMf`) | **20** (8 + 12) | **1** (1 + 0) | **10** (8 + 2) |
| rhetoric column (not scored by rule RH) | 1 further sentence tagged rhetoric (B); 1 of the 12 has an unclear tag (ROOT) | 0 | 0 |
| Rebuttal conditions unrecorded (`R2`) | 9 | 12 | 4 |
| Critical questions scored | 90 | 36 | 150 |
| answered with evidence, for (`A+`) | 6 | 2 | 86 |
| answered with evidence, against (`A−`) | 11 | 2 | 8 |
| asserted (`S`) | 31 | 16 | 23 |
| **unanswered** (`U`) | **42** | **16** | **33** |
| unanswered per layout | 1.6 | 1.0 | 0.8 |

### 8.2 Unanswered critical questions by scheme (unanswered / scored)

| Scheme | Day side | Critics | The audit |
|---|---|---|---|
| MW model to world (constructed) | 11 / 25 (MW6 anchor 6, MW3 coverage 3, MW2 assumptions 2) | 10 / 15 (MW3 coverage 5, MW4 robustness 2, MW5 non-circularity 2, MW2 1) | 24 / 68 (MW5 non-circularity 9, MW2 assumptions 6, MW6 anchor 5, MW4 robustness 3, MW3 1) |
| SG sign | 9 / 10 (SG2 other accounts 7) | 0 / 2 | 0 / 2 |
| AB abduction | 5 / 7 | — | 0 / 1 |
| GE example, generalisation | 5 / 13 | 0 / 1 | 0 / 1 |
| AN analogy | 4 / 8 | 2 / 4 | — |
| EX expert opinion, literature | 4 / 15 | 1 / 5 | 4 / 15 (EX5 other experts 3) |
| CE cause to effect | 2 / 6 | 1 / 2 | — |
| IG ignorance | 2 / 5 | 0 / 2 | 2 / 7 (IG3 standard of proof 2) |
| TR reading of a text (constructed) | — | 1 / 3 | 2 / 16 (TR3 would the author accept it, 2) |
| RC recomputation (constructed) | — | 0 / 1 | 1 / 40 |
| PC precedent | — | 1 / 1 | — |
| CC correlation to cause | 0 / 1 | — | — |

Schemes in scope that no layout used as a main scheme: PK (position to know), PR (practical reasoning), CN (consequences), PO (popular opinion), AH (ad hominem). The last two occur in the corpus on nodes that are not load-bearing (ROOT-T, ROOT-EP, ROOT-PG) and in the rhetoric ledger; they are treated in section 6.

### 8.3 The most load-bearing hidden warrants

Ranked by the decided verdict fields on the 33 nodes that would have to be argued again if the warrant were rejected.

**The audit.**

| # | Warrant, as the audit would have to state it | Where it is stated now | Verdicts it carries |
|---|---|---|---|
| 1 | **Own basis.** A recomputation on the inputs, model and reading the audit selects is the author's own argument, so its result is a verdict on the author's reasoning | Verdict rule, section 0; often not at the field | All 27 decided internal fields (22 `holds`, 5 `non-sequitur`). It does contestable work where an input of the audit's enters: A2e internal and F1a internal (supply levels the author does not use), C2 internal (a paragraph from an earlier version), B internal (through the reading) |
| 2 | **Model to world.** The exchangeable Wright-Fisher model and the identities that hold inside it describe the hominid lineage in the respect at issue | Methods page, once; not at B3, B3a, B6, B7 | 6 of the 8 decided `supported` or `contradicted` external fields: B1c, B3, B3a `contradicted`; B3g, B6, B7 `supported`; the comment on B1. As a stated condition, the `contested` verdicts on A, B4a, B5, C2, F1, F2, H, H5, H8 |
| 3 | **Concession.** What an author withdraws is thereby contradicted, and what he concedes is thereby supported | Nowhere | B3g external `supported`; co-carries B3, B3a, B1c `contradicted` and B6 `supported` |
| 4 | **Literature as benchmark.** A published mainstream estimate or theory is the correct value until shown otherwise, including where it was inferred with the model in dispute | Nowhere as a rule; rule F exempts "standard values"; conditions stated at some nodes | A2e external `contradicted` (Uricchio 2019, Boyko 2008); B1c external `contradicted` (Yoo's ancestral N_e); the conditions of A and F2 external (Weissman and Barton 2012), H2 (Nunney 2003), B4a; A3 and F3a fidelity (texts in hand, the strongest use) |
| 5 | **Default and burden.** The standard model stands unless defeated; a universal claim fails if one mechanism is admissible; an inconclusive check leaves `contested` | Methods page ("a stance"); `load_bearing` comments | What all 20 `contested` external fields leave standing; the `pending` on ROOT and ROOT-M; which nodes are load-bearing at all |

Two further warrants are stated where they are used and are contested inside the project, so they are not hidden, but verdicts turn on them: **reading selection** (the reading picked by rules C, RD and RH6, or fixed by the audit's formal statement, is what the author answers for: B internal, A2e external, B2 internal, F internal, and the `dialectic` tags at ROOT, ROOT-M and FM10 that decide whether "impossibility" is scored at all) and **materiality** (25% divides slip from error: B2 internal, H8's "within R1", A3's "R1 not triggered", E6).

**Day.**

| # | Hidden warrant | Nodes it carries |
|---|---|---|
| 1 | A mechanism not shown to be sufficient is excluded; the computation is owed by whoever proposes it | ROOT, ROOT-M, FM10 |
| 2 | The LTEE's aggregate rate carries over to every organism as an upper bound, linearly in generations, whatever the differences in recombination and mutation supply | A, A2e, F2, and through them ROOT |
| 3 | Every difference between two reference genomes is a fixation that had to be produced on one lineage after the split, from an empty start | A3, B1c, B, F, and the shortfall in ROOT |
| 4 | Haldane's parameter values, hard selection and s_max of about 1 hold for the hominid lineage over the whole window | H, H8, H5 (ally) |
| 5 | A quantity read off a fit or a discrepancy measures what it is named for: fitted d apart from s (C2, C2a); a pedigree-to-phylogeny ratio as k/μ (B3, H1); a negative corrected count as biology (E5); a contiguous excess as a discrete event (ROOT-FM, FM10) | C2, C2a, B3, H1, E5, ROOT-FM, FM10 |

**The critics.**

| # | Hidden warrant | Nodes it carries |
|---|---|---|
| 1 | The standard model (exchangeable reproduction, steady state) describes the lineage, so its identities are facts about it | B, B5, B7, B3 (keruru's chains), ROOT-M |
| 2 | Fixations at different loci proceed independently; nothing caps the width of the pipeline | F1, F, F2, and the scaling reply at A and A2e |
| 3 | The ancestral state is what standard inference says it was (a full pipe; N_e near 10^4) without a sourced demography | B6, B1, B1c |
| 4 | A theory's record at one scale, and the standing of the field, settle the burden; refuting the challenger's steps is enough | ROOT (ROOT-PG), B2 (the textbook one-liner) |
| 5 | A reading of the opponent can be taken from a slide or a paste (the serial reading) | F1a, F |

Warrant 1 of the critics and warrant 2 of the audit are the same proposition. Where the audit upholds a critic on a simulation, it has adopted the critic's hidden warrant and added no independent support for it; the audit's nine unanswered MW5 questions are that point counted.

### 8.4 The expectations of 2.7

(1) Met: 6 of the audit's 11 hidden warrants are in external fields that go from a model to the lineage, and MW5 and MW2 are 15 of its 33 unanswered questions. (2) Partly wrong: Day's 12 full mismatches are not concentrated at ROOT. They are spread over every branch (ROOT, FM10, A, A2e, B3, B3a, B1c, F1a, F2, F3a, H8, H1), wherever a categorical word sits on an analogy, a sign or a fit. (3) Half wrong: the critics' unanswered questions do cluster on model-to-world (10 of 16, coverage first), but explicit appeals to consensus are rare on these nodes (one EX question unanswered); the appeal is carried silently by their first hidden warrant.

---

## 9. Proposals (not applied; no claim file, rule or verdict is changed by this pass)

### 9.1 Two lines per decided verdict on load-bearing claim files

A `warrant:` line and a `rebuttal conditions:` line beside each decided field, checked by lint for presence only. Sketch for B3a (wording to be reviewed; this is not a proposed verdict):

```yaml
verdicts:
  external: contradicted
warrant:
  external: "SW-2 (model to world): P_fix = 1/(2N) is a theorem for exchangeable reproduction; simulated across N_e/N. SW-3 not used: the author's withdrawal is recorded, not counted as evidence."
rebuttal_conditions:
  external: "Fails if a reproduction law with covariance between breeding success and genotype, at parameters sourced for humans, gives a fixation probability more than 25% from 1/(2N). Not run."
```

The 29 bare fields and the 11 layouts with a warrant stated only elsewhere would each get a line; no count moves. Cost: small per file. Both sides gain: Day's side sees what would reverse a verdict against him; the critics' side sees that verdicts for them rest on stated premises and not on the auditor's agreement.

### 9.2 Standing warrants, stated once and in public

A short section in the verdict rule's successor or on the methods page, each with what would make the audit drop it:

- **SW-1 Own basis.** Internal verdicts use only inputs, models and readings stated by the author; anything the audit supplies is listed in the comment, and a verdict that needs a supplied input is external.
- **SW-2 Model to world.** A result in a model says what follows from the model's assumptions. It bears on the lineage only as far as each assumption the result depends on has been shown to hold of the lineage by evidence that does not assume the result. Where the model is the thing in dispute the verdict says "in the model" in its words.
- **SW-3 Concession.** A withdrawal is recorded as a fact about the author's position, dated. It decides no external verdict.
- **SW-4 Literature as benchmark.** A published estimate is used as published, with its inference method named; where that method assumes what a party disputes, the dependence is stated beside the number.
- **SW-5 Default and burden.** The standard model is the default by stance, not by finding. `contested` does not mean the default stands. A statement of what would make the root claim stand is owed before R5 (MA-11).
- **SW-6 Reading.** The reading scored is the one the author states; where the author is ambiguous every reading is reported and the field stays reading-dependent until the author has been asked or the readings agree.
- **SW-7 Materiality.** 25% is a convention with its sensitivity printed (as now), and it is applied to the audit's own reproductions under the same name.

### 9.3 Wording of verdict comments by kind of ground

| Ground | Wording the comment should carry | Wording to avoid at that node |
|---|---|---|
| Data the audit processed | "contradicted by [dataset, build, filter]" | (none; say which data) |
| Published result, not reprocessed | "as published in [source]; method: [model-based / direct count]" | "measured" |
| Simulation or exact chain | "in [model], for [regime]; not shown for the lineage" | "falsified", bare `contradicted` or `supported` |
| Identity inside a class of models | "holds for [class]; untested outside it" | "exactly", without the class |
| Author's withdrawal | "withdrawn by the author on [date]; external status undecided by that" | "contradicted (withdrawn)" |
| A chosen reading | "on reading [ρ]; on reading [σ]: [verdict]" in the first clause | the verdict word first and the reading later |
| Recount of the author's table | "recomputed from [locator]: [value] against printed [value]" | `holds` with no recount named |
| Nothing found | "searched [where]; not searched [where]" | "no derivation", "no critic" |

### 9.4 A closure rule for replies

If the right of reply is exercised (O-2), a reply is logged as a doubt against named fields; each doubt is answered in writing or the field is withdrawn, by someone other than the check's author, within a period fixed in advance; the `rebuttal conditions:` lines say beforehand what would count. This is rule 9 made operational, and it is the one remedy here that needs the other parties.

---

## 10. Concordance with the earlier passes

| AS finding | MA | TV | AR | ST | Relation |
|---|---|---|---|---|---|
| AS-01 wording above licence in 7 of 8 decided external fields | MA-05, MA-16 | TV-04 | — | ST-02, ST-03 | **agrees**; the field list and the wording fix are new. **In part disagrees** with the breadth of MA-05's remedy: the model-based `contested` verdicts (A, B4a, B5, F2, H, H8) are worded within their grounds and need no re-coding |
| AS-02 bare fields; warrants not at the node | MA-07 (part) | — | AR-04 (no field linking a claim to its source) | — | **new**; agrees in part |
| AS-03 concession used as external evidence | — | — | — | — | **new** |
| AS-04 the audit scores readings of its own making | MA-02, MA-03 | TV-02, TV-08 | — | ST-03 | **agrees**; the audit's formal statement fixing the reading, as the mechanism at A2e, is new |
| AS-05 the audit's inputs inside internal verdicts | — | — | — | ST-03 (F1a) | **agrees in part**; A2e internal and the unnamed clauses are new |
| AS-06 the audit as discussant | MA-15, MA-13 | TV-01 | AR-12 | ST-04 | **agrees**; the counts and the six audit-authored opposing cases are new |
| AS-07 no critical discussion; rules 1, 2, 9 untested | MA-10, MA-01 | TV-01, TV-03 | AR-13 (part) | — | **agrees**; the closure rule is new |
| AS-08 non-circularity unanswered | MA-05 | TV-04 | — | ST-02 | **agrees**; the per-question count is new |
| AS-09 arguments from ignorance without a stated search | MA-07, MA-09 | — | AR-05, AR-06 | — | **agrees in part** |
| AS-10 markers about persons without a rule | — | — | AR-10 | — | **new**; touches AR-10 |
| AS-11 under-statement and balance pressure | MA-08, MA-17 | TV-06 | — | ST-04 | **agrees in part**; A3 is a new instance in Day's favour |
| AS-12 no place for a party's over-statement or unanswered question | MA-15 | TV-07 | — | ST-12 | **agrees in part** |
| AS-13 this pass's own standing | MA-01 | TV-11 | AR-13 | ST-13 | **agrees** (independence) |

**Counts over the 13 AS findings:** agrees 6 (AS-01, AS-04, AS-06, AS-07, AS-08, AS-13); agrees in part 4 (AS-05, AS-09, AS-11, AS-12); new 3 (AS-02, AS-03, AS-10). One partial disagreement (inside AS-01, with the breadth of MA-05's remedy). Two refinements: against reading MA-07 as "`holds` means unexamined", the recomputation questions on these 33 nodes are answered with evidence 31 times in 40 (the same refinement ST made); against reading MA-05 and ST-02 as *simulation verdicts over-claim*, the over-claim is in the word chosen at seven fields and not in the simulations' own write-ups.

**What this lens sees that the earlier ones did not:** the unstated licence under each verdict, by name; the gap between a verdict's word and its comment; the author's concession doing the work of evidence; the audit's role as an arguer; the same questions put to all three parties in one table. **What it cannot see:** whether a simulation is right, whether a source was read, whether the search was complete, who the rater is. No MA, TV, AR or ST finding is closed or contradicted by this pass.

---

## 11. Findings

Severity as in the standing procedure. "Who" is who can act. Evidence paths are relative to the repository root.

| ID | Severity | Finding | Evidence | Remedy | Who |
|---|---|---|---|---|---|
| AS-01 | MAJOR | Seven of the eight decided `supported` or `contradicted` external verdicts on load-bearing nodes are worded more strongly than their grounds license; with B and F1a internal and the comment on B1, 10 of 40 audit layouts | Section 5.2; `docs/research/claims/` files A2e, B1c, B3, B3a, B3g, B6, B7 (front matter), B1 (comment citing B4a) | 9.3 wording, applied to the comments (no value changes); SW-2, SW-3 | agent; rule-freeze if any word changes |
| AS-02 | MAJOR | 29 of 74 decided fields carry no argument at the field; in 11 of 40 layouts the warrant is stated only in a standing document (10) or nowhere (1), and 8 of those are contested | Section 5.1; script count over the 33 front matters | 9.1 `warrant:` line; lint for presence | agent (proposal) |
| AS-03 | MAJOR | An author's withdrawal or concession is used as a ground in five external comments. A concession closes a point between parties; it is not evidence about the world, and the claim files record that Day's later text reopens one of them | Section 5.5; claim files B3, B3a, B1c, B6, B3g | SW-3; record withdrawals as a dated note beside the verdict; decide the external field on evidence or leave it `contested` | agent, then owner (values could move at B3g) |
| AS-04 | MAJOR | Two load-bearing verdicts are decided on readings made by the audit and not shown to be the author's: A2e external (the reading "fixed" by the audit's formal statement, while Day's stated basis is undecided) and B internal (the "most defensible" reading). Whether the author would accept the reading is unanswered in both | Sections 3.6, 3.8; `A2e-ltee-as-ceiling.md`, `B-neutral-theory-cannot-rescue.md` | SW-6; put the two readings to Day in the right-of-reply packet as specific questions; until then mark both fields reading-dependent in the tallies | owner (O-2, O-5), agent |
| AS-05 | MAJOR | Two internal `non-sequitur` verdicts depend on an input the audit supplied (A2e: supply scaling; F1a: supply levels) and name no clause of rule N at the field; a third (C2) cites a paragraph from an earlier version of the paper | Sections 3.6, 3.11, 3.13 | SW-1; add "inputs supplied by the audit: none / list" to internal comments; name the clause | agent (comment text); owner if a value moves |
| AS-06 | MAJOR | The audit argues as well as rates: 146 of 437 defeaters are its own checks' attacks (100 on Day's nodes, 33 on critics'), none rated `not_upheld` by it; on 6 of the 9 nodes with no critic argument the case against Day is the audit's own or literature only the audit applied | Section 5.4; `docs/research/argmap/defeaters.yaml` (script count) | Mark audit-authored opposing cases at the node; adopt `side: audit` (MA-15); in any synthesis count them as the audit's standpoints, owed a defence | agent (proposal) |
| AS-07 | MAJOR | No critical discussion has occurred between the audit and the parties, so the freedom, burden and closure rules are untested for it; whether a defence has failed is decided by the check's author | Section 7; methods page, "No right of reply so far" | 9.4 closure rule, with the right of reply | owner (O-2), outside |
| AS-08 | MINOR (the substance is MA-05's) | The audit's most often unanswered question is whether the model or the published estimate presupposes what the other party disputes (9 of its 33 unanswered questions), then whether the assumptions hold of the lineage (6) and whether any observation of the lineage is reproduced (5) | Section 8.2 | A one-line answer to MW5 in each `warrant:` line; B4a's printed anchor test as the pattern | agent |
| AS-09 | MINOR | The audit argues from absence without saying how far the search went: "no derivation" for 32.3 (later found), "No critic in the corpus addresses ROOT", five "asserted" catalogue rows; `holds` by default is the same form | Section 6(i); `B3-k-neq-mu-values-umbrella.md` Check; `ROOT-*.md` | 9.3 last row: "searched / not searched" | agent |
| AS-10 | MINOR | Claim files carry markers about persons ("LLM-assisted", "AI-assisted", "advocacy") and one weighting by source; no decided field among the 74 uses them, and no rule says when a source's nature may bear on weight | Section 6(vi); claim files A, B3, E5 | One sentence for the rule's successor: provenance notes never enter a verdict comment; a source's reliability is relevant only where the ground is its testimony | agent (proposal) |
| AS-11 | MINOR | `contested` is used where the audit's own data corroborate one side (A3 external), and 20 of 28 decided external fields on these nodes are `contested`; paired credits per check add pressure toward a middle verdict | Sections 3.7, 6(vii) | With proposal (c) of the method audit: a sub-label that says which way the evidence run so far points | agent (proposal) |
| AS-12 | MINOR | The vocabulary records a party's over-statement only as N2d and has no place for an unanswered critical question, so Day's 20 over-qualified layouts and the critics' 12 arguments with no stated rebuttal condition are invisible in the tallies | Section 8.1 | A `qualifier:` note per Statement quote (asserted level, licensed level, source of the limit), outside the verdict fields; with ST-12's proposal | agent (proposal) |
| AS-13 | CRITICAL for the standing of the document | One rater of the same model family, not blind, who knew the earlier findings; codes are judgements, several one step from the next; the sorting into schemes is the rater's; three schemes are the pass's own construction; the frameworks' primary books were not obtained and part of the rubric rests on tertiary or derived texts; the check write-ups were not re-read | This file, preface, 1, 2.3 | A second rater applies sections 2.2 to 2.4 to the same 33 nodes without seeing the codes; registered expectation: the audit's hidden-warrant and mismatch counts each move by less than a third | owner, outside |

**Counts (13 findings).** By severity: CRITICAL for the document's standing 1, MAJOR 7, MINOR 5. None is closed.

---

## 12. Remediation, three ways, and whom each finding helps

**No-decision fixes (change no rule, vocabulary or verdict value).** None was applied in this pass, by instruction: claim files are not to be touched. Ready to apply on the owner's word: comment wording per 9.3 on the seven fields of AS-01 (words added, values unchanged); "searched / not searched" notes (AS-09); marking audit-authored opposing cases (AS-06).

**Proposals (held back).** The `warrant:` and `rebuttal conditions:` lines (9.1; AS-02, AS-08); standing warrants SW-1 to SW-7 (9.2; AS-01, AS-03, AS-04, AS-05); the provenance sentence (AS-10); the direction sub-label (AS-11); the `qualifier:` note (AS-12). SW-3 and SW-6 could move values (B3g external; A2e external and B internal toward reading-dependent or `contested`) and so fall under the rule-freeze procedure.

**Owner decisions (proposed; not yet in `DECISIONS.md`).** O-18: adopt the standing warrants and the two lines, or treat this pass as a one-off. O-19: whether a concession may decide an external field (AS-03). O-20: add the two reading questions (A2e, B) and the closure rule (9.4) to the right-of-reply packet. O-21: a second rater for this pass (AS-13).

**Whom each finding helps.** AS-01, AS-03, AS-04, AS-05 and AS-08 help Day's side on the face of it: each weakens a verdict against him or for a critic. They help the critics' side in a second way: a verdict for them that says what it rests on is harder to dismiss as the auditor's agreement. AS-11 and AS-12 help the critics' side: A3 aside, they make Day's over-statements and the audit's hedged words visible. AS-06 and AS-07 help neither and cost the audit its claim to be only a rater. AS-02, AS-09 and AS-10 are housekeeping with no direction. In this pass, as in ST-04, the audit's untested or over-worded verdicts lean one way (toward the critics) and the parties' unanswered questions lean the other (Day 42, critics 16, on unequal exposure); neither count is a rate.
