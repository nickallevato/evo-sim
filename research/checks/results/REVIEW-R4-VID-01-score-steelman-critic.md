# Review 3 (steelman, critics' side): R4 VID-01-score

Reviewer: `reviewer` (Opus), fresh instance. Did not author the work, wrote neither of the other two
reviews. Task EVO-76, review 3 of 3. Brief: `research/checks/briefs/VID-01-score-reviews-reviewer.md`
(`d7d2f7d`); the lead directed me to read the two landed reviews and to answer two of their findings
point by point, so the skill's "do not read the other steelman" default is overridden for this file.
Under review: `research/checks/results/R4-VID-01-score.md` (registration `e857d1f`, post hoc
`31d7f0d`) and `A4d`, `A5h`, `Ge`. Lead rulings R-1..R-7 binding and not reopened. The review tier
is not re-litigated.

**Counts: 0 BLOCKER, 5 MAJOR, 5 MINOR, 6 NOTE.**
**Findings that would move a verdict field: none.** A4d `internal: holds`, A5h
`internal: arithmetic-error` / `external: pending` and Ge `internal: holds` are all right, and the
critics' side does not need any of them to move. What my findings change is the *grade of a critic
statement* (MAJOR-1, MAJOR-2), the *headline* a claim file and the write-up may carry (MAJOR-3), and
the *stated ground* for two no-moves (MAJOR-4, MAJOR-5).

This is the strongest honest case for the critics, not a counterweight. Three findings run against
my own side and are labelled as such (MINOR-4, MINOR-5, NOTE-1).

**On the brief's question — is a third audit error against the critics standing in this pass?**
Yes, in a weaker form than the first two: MAJOR-3. It is a headline overstatement, not a suppressed
fact — A4d's Weaknesses line and the write-up's "For the critics" section both record the
underlying fact correctly. It is not of the same order as MAJOR-1 at EVO-57 (an evaluative sentence
written without reading the answer) or NOTE-5's invented inconsistency. I reached it from the C2
claim file and §8.6, not from the pattern; and I record at MINOR-4 and MINOR-5 two places where the
pass was *not* unfair to the critics and one place where it was too generous to them.

---

## What I recomputed (nothing relayed)

Both fetch directories read, nothing executed, nothing from `sources/raw/` committed. `main.txt`
§1 (lines 45–60), §8.6 (640–665) and the `27,600` / `recombination` / `effective generation` hits
read verbatim; `R4-G1.md` lines 155–180, 213, 252, 312, 318; `R4-X1-verdict-rule.md` §RD, §RH3,
§RH5, lines 84–86; `METHODS-AND-LIMITATIONS.md` line 45; `C2-bio-cycle-d.md` lines 3, 8;
`A5e-human-derived-rate-27600.md` lines 18, 25–26, 55; `A4d` lines 12, 20, 34, 61–82; `Ge` lines
12–14, 24; `quotes-critics.md` lines 802–935 (GGR-11..GGR-46 notes); transcript lines 332–340 and
386–393. Arithmetic in `research/.venv/bin/python -I`: 252,000/27,600 = **9.1304**;
113,400/27,600 = **4.1087**; 8 × 27,600 = **220,800**; 252,000 × 0.45 = 113,400;
450,000 × 0.45 = 202,500; e^−384 = 1.7018e−167.

---

## MAJOR

### MAJOR-1 — reading (c) is worth at least "partly accurate", and the Bio-Cycle correction *is* d by the audit's own definition
The Day-side steelman (its MAJOR-1) asks for (c) to be regraded "**contradicted** as to the quoted
statement; one adjacent point survives". It should not be. The audit's own `C2-bio-cycle-d.md`
title (line 3) defines the thing:

> "Bio-Cycle model: a generation-overlap factor **d = 0.45**, fitted to three aDNA loci, halves the
> effective generations available to selection (**g_eff = d x g_nominal**)"

MITTENS 3.0 §8.6 (main:652–654), verbatim:

> "The human-derived fixation rate, calculated independently from human parameters alone using
> Kimura's fixation time formula and **the Bio-Cycle correction for overlapping generations**,
> yields approximately one fixation per **27,600 effective generations** (Day and Athos 2025,
> Appendix D). Applied to 252,000 generations provides 8 achievable fixations…"

So the single human-derived throughput number in MITTENS 3.0 is, by the paper's own words, computed
*with the d correction* and expressed in *d-corrected units* ("effective generations" — the
vocabulary C2 defines, and the only occurrence of that phrase in body or addendum). GGR-13's core
assertion — "he's still using the de coefficient in mittens" — is **accurate of that step**, not
adjacent to it. And §8.6 is not a footnote: the paper calls the objection it answers there "the most
persistent objection to MITTENS".

What (c) does **not** rescue is GGR-14's elaboration: `450,000`, `225,000`, `202,500` and `0.45` are
0 hits, `252,000` appears 10 times uncut, and "for all his math" is false. That split — core
assertion accurate, elaboration false — is exactly what "partly accurate" names. The write-up has
it right and the Day-side regrade would lose a true proposition.

**Which reading governs.** `R4-X1-verdict-rule.md` §RD, last bullet: "Extended readings (**a
different object**, or a wider claim) are reported with their own verdicts but **cannot set the
verdict field or the headline tag**." Reading (a) is a different object — the pre-3.0 /
*Probability Zero* corpus, not the paper the exchange is about. Readings (b) and (c) are the same
object at two scopes (3.0's own body; 3.0 including what it incorporates by citation), and (c) is
the scope under which the quoted statement is most defensible. Among in-scope readings **(c)
governs**, which is where the correctness review's MAJOR-3 also lands. The Day-side steelman's
NOTE-3 ("Day does not need (a)") is right only if its MAJOR-1 regrade succeeds; MAJOR-2 below is why
it does not.

**Fix:** keep (c) at **partly accurate**; add the C2 identity (`g_eff = d × g_nominal`) and the
"effective generations" locator to the Readings table so the grade is self-evidencing; state in the
write-up and in A4d that (c) governs among in-scope readings under RD's extended-reading bullet,
with (a) recorded beside it.

### MAJOR-2 — the "printed 8" argument is invalid and cannot carry a downgrade of (c)
The Day-side steelman's MAJOR-1 rests on a new computation: "113,400 / 27,600 = 4.1, against the
printed 8 … **The printed number is inconsistent with any application of d = 0.45** to the
generation count." The premise is true and the inference does not follow, because the printed 8 is
inconsistent with the **no-d** reading too. Recomputed: 252,000/27,600 = **9.13**, not 8. The
audit already knows this — `A5e-human-derived-rate-27600.md` line 26:

> "252,000/27,600 = 9.13, not 8 (8 x 27,600 = 220,800 …). **A 12% discrepancy in the paper's own
> sentence**; immaterial to the 205M shortfall, but **the figure does not reconcile**."

A number that reconciles with neither candidate cannot discriminate between them. Using it to
conclude that d is absent from the step, while the same sentence names the Bio-Cycle correction and
its units, is reasoning from an unreconciled figure to a conclusion it cannot support.

**This is the live D-24 conflict** the lead flagged. My position: the Day-side MAJOR-1's four-row
table is otherwise sound and should be adopted for GGR-14's elaboration; its §8.6 "Applied to
252,000 generations" observation is a fair point about the *generation count*; but the regrade of
(c) to "contradicted" must be declined, and the "inconsistent with any application of d" sentence
must not enter the write-up or any claim file in that form.

**Fix:** decline the regrade. If the §8.6 arithmetic is cited at all, cite it as A5e does — 8
reconciles with neither 9.13 nor 4.11, so the step is unreconciled in Day's own text and settles
nothing either way.

### MAJOR-3 — "MITTENS 3.0 is clean of the d coefficient" is a concept claim resting on a token search
Write-up, "Who this helps / For Day", first bullet, and the "Who this helps, at Q1" line: "MITTENS
3.0 is **clean of the d coefficient** by an exhaustive token search over a hash-verified text"; A4d's
verdict comment (line 12) carries the same shape ("**Exhaustive** token search … 0 standalone `d`").
A token search is exhaustive over tokens. The concept is present: §8.6 imports a rate built on the
d correction and expressed in d-corrected units, by citation to a document outside the corpus. The
precise, fully supported claim — and the one A4d's Formal statement actually needs — is: **3.0's own
generation count is 252,000, uncut, and no d multiplies it anywhere in body or addendum.**

The same overstatement sits upstream in `C2-bio-cycle-d.md` line 8: "MITTENS 3.0 (Z23003785) **drops
d**, so ROOT survives without it". After this pass that comment should read "drops d from the
generation count; §8.6 still imports a Bio-Cycle-corrected rate by citation". C2 is marked
`load_bearing: true`, so this is worth getting right even though no field moves.

**This is the third standing audit statement that runs against the critics from this source**, and I
state its weight honestly: it is a headline overstatement, not a suppressed fact. A4d line 34 already
records "the correction is still invoked in 3.0 elsewhere", and the write-up's "For the critics"
section says reading (c) is partly right. The fact was never hidden; the summary that readers and
counts will carry overstates it.

**Fix:** narrow the "For Day" bullet and A4d's verdict comment to the generation-count claim; flag
the C2 line-8 wording for the integration task (outside this pass's file list).

### MAJOR-4 — Q3's stated ground for "nothing moves" is wrong: GGR-43/44 is not a weaker form of G5
The write-up: "**A critic-side node whose content is strictly weaker than an existing critic-side
node moves no verdict**", on the ground that "G5 states the defect with the algebra; GGR-43/44 name
a model without it." The two are about **different quantities**.

- **G5** (Matev) is about the variance of the **beneficial allele count**: "the variance of the
  beneficial allele count of an individual just increases as n increases" — Var(K) = n/4.
- **GGR-43** (t=02:13:47, verbatim from the transcript) is about the variance **in fitness**: "I'll
  give the pop gen answer to go back to Bernoli's law **if you want to know how it is that variance
  and fitness can be maintained** even if you have very … low fitness impacts of each individual
  mutation", then names the infinitesimal model as "the fundamental model of quantitative genetics".

The write-up itself identifies variance in fitness as the quantity the inference misuses:
"**Fisher's theorem relates the response to additive genetic variance in log fitness, not to the CV
of a count.**" By the write-up's own statement of the defect, the panellist names the correct
quantity and the correct standard model of the regime. The harvest note at `quotes-critics.md`
GGR-43 says the same thing more strongly than the scoring does: "it **addresses GGR-19's premise
directly**: how variance in fitness survives when each mutation has a small effect."

The grade **on point** is right and I do not ask for *meets* (see MINOR-4). The conclusion — nothing
moves — is also right, for the independent reason that G `external` is already `contested`. What is
wrong is the ground, and it is the ground that the Open item 2 proposal (a critic-side node for the
infinitesimal-model answer) will be judged on at integration.

**Fix:** replace "strictly weaker than an existing critic-side node" with: GGR-43/44 attacks the
same substitution from the fitness-variance side, where G5 attacks it from the allele-count side;
it adds no derivation, so no field moves, but it is an independent angle and the Open-2 node
proposal stands on its own content rather than as a weaker G5.

### MAJOR-5 — Q2's criterion is narrower than the audit's own operative use of `contested`, and the write-up says the opposite
The write-up, "Things that looked wrong": "I chose the narrower reading because **it is the one the
vocabulary supports**, and I registered it before looking." The audit's own methods file says the
reverse. `criticality/METHODS-AND-LIMITATIONS.md` line 45 (MA-08):

> "**`contested` is two-thirds of the external column.** 114 of 172 decided external verdicts. The
> word covers at least five situations: disputed in the literature, **true only in the tested
> regime**, conditional on an unsourced parameter, leaning one way but short of decisive, and **not
> examined**. In a seeded sample of 20, **6 had no recorded basis at all**."

`R4-X1-verdict-rule.md` line 86 shows the same looseness in the other direction: a node merely
*depending on* a contested-standard value "carries the flag in its external column ('contested')".
Nothing in the rule file conditions `external: contested` on an objection weakening the conclusion's
direction. A5h's "functionally dead" is true only in the tested regime — Day's multiplicative model
with his chosen s — which is one of MA-08's five listed situations verbatim; and the audit elsewhere
awards `contested` for "not examined", which is strictly less than what A5h now has on the record.

**I do not ask for the field to move.** The criterion was registered before the evidence was read
(`e857d1f`, byte-identical per the correctness review's diff check), the substance of the write-up's
band 2b is right — on the critics' own e^−U the direction strengthens, and e^−384 removes the
s = 0.001 escape — and changing the criterion now would be a post hoc widening of exactly the kind
hard rule 5 exists to prevent. `pending` stands. What must go is the claim that the narrow reading
is what the vocabulary supports, because the audit's own appraisal says `contested` is applied far
more loosely than this, and applying the strict form to the one objection sourced from the critics
is an asymmetry the audit should name rather than assert away.

**Fix:** strike "it is the one the vocabulary supports"; replace with a sentence recording that the
registered criterion is **stricter than the audit's operative usage (MA-08)**, that `pending` stands
because the criterion was pre-registered, and route the asymmetry to the criticality layer as a
named finding for the next pass.

## MINOR

### MINOR-1 — 0.84 / 0.65 are cited without their post-hoc label, and the only pre-registered linkage test failed
Q3 and the "For the critics" list: "joint < product when **linked** (0.84 / 0.65) or **clonal** (0)
— Day's stated direction", with no label. `R4-G1.md` line 165–166 marks both rows **post-hoc**, and
line 172 records: "**Pre-registered prediction failed at 1 M.** I predicted a pair ratio of 0.5–0.95
and got 1.015 ± 0.022 … **It did not show that interference is absent.**" Under hard rule 5 the
label is owed. Here it cuts for the critics, not against them: the *only* pre-registered test of
Day's sub-multiplicative direction at linkage returned independence, and the sub-multiplicative
numbers come from maps chosen after that failure.

This also disposes of the Day-side steelman's MAJOR-2 point 1, which argues that the human-relevant
density (R4-G1 line 174: "about 4,500 loci/M, between the two tight maps") is "where Day's direction
holds". No run was done at 4,500 loci/M. That is an interpolation between two post hoc rows, offered
against a pre-registered row that failed. The honest statement of R4-G1 on this premise is: free
recombination gives independence (measured, pre-registered); tighter-than-pre-registered maps give
0.84 / 0.65 (post hoc); the human density was not run. The write-up's sentence and the Day-side
steelman's correction are **both** owed the label.

**Fix:** "(post hoc rows; the pre-registered 1 M row returned 1.015 ± 0.022 against a predicted
0.5–0.95, and no run was done at the human-relevant 4,500 loci/M)".

### MINOR-2 — Ge: the §1 clause is not scored under RH3, and it should be
I tested the opposite reading the brief asked me to test, and it **fails**: rule C does decide Ge
`internal: holds`. Day's statement is about what he put in the paper, the argument is genuinely
absent (no p^n, no derivation, no number; `Averaging` / `law of large numbers` 0), and one clause in
a paragraph about "the characteristic rhetorical structure" of the polythesis is not a retention of
the argument. `holds` is right and I do not contest it.

But the write-up disposes of the clause as "one undefined **rhetorical** clause", and the clause is
not purely rhetorical in the RH sense. Verbatim (main:55–56): "**When the Bernoulli Barrier
demonstrates that parallel fixation is probabilistically self-defeating**, the defender invokes
neutral drift." That is an indicative assertion that the Barrier demonstrates something, used as a
premise in §1's case that the polythesis is ad hoc, with no support anywhere in the paper.
`R4-X1-verdict-rule.md` **RH3** has the label for exactly this: "A node whose only support is
rhetoric is marked '**no dialectical support offered**'. It is not marked an error." The accurate
record is: the argument is omitted (Day's statement true), **and** its conclusion is asserted in §1
without dialectical support in 3.0.

**Fix:** add one sentence to Ge's R4 paragraph recording the §1 clause under RH3 as "no dialectical
support offered", explicitly not as an error and not as a reason to disturb `holds`.

### MINOR-3 — the "load occurs 0 times" rebuttal is given first place and is a fact-check of the wrong object
Q2's "cost to the critics" row leads with: GGR-33's premise "is an attribution the text does not
carry (0 occurrences of 'load')". GGR-33 says "This is supposed to be a genetic load that he's
**calculating**" — a statement about the quantity, not about Day's vocabulary. §6.4 computes a
carrier's fitness from its own deleterious-mutation count under multiplicative fitness, which is the
quantity classical load theory handles; the absence of the word is not an answer. `RH5` makes the
symmetric charge explicit: "A critic who literal-fact-checks Day's rhetoric and presents it as a
refutation gets an N entry for overreach. **So does Day, when he does the same**" — and so does the
audit. The real cost to the critics is the second one (adopting e^−U strengthens the direction and
removes the s = 0.001 escape), which is sound and which I do not dispute.

**Fix:** demote the word-count to second place and restate it as what it does establish — that "*the*
genetic load calculation" is not what §6.4 calls itself — not as an answer to the conceptual
attribution. (The Day-side steelman reaches the same place from its own side at its MINOR-1.)

### MINOR-4 — band 3b's criterion is **not** set too high (finding against my own side)
The brief asks whether "meets" was pitched at a height no spoken reply could clear. I tested it and
the answer is no. The registered criterion reads: "**meets** (addresses the inference and shows
where it fails, **with or without numbers**)". One spoken sentence clears it — "the CV going to zero
doesn't mean the variance goes to zero; the variance of the count rises with n, and Fisher's theorem
is about variance, not the CV" — no derivation, no numbers, no blackboard. The criterion is
clearable in conversation and was applied as written. I do not ask for it to be changed, and I note
that changing it now would be post hoc, as the write-up says.

Two things the write-up should nonetheless tighten, both in the critics' favour and neither
requiring a new band: (i) GGR-43/44 sits at the **top** of *on point*, not the bottom — it names the
quantity and the regime, which is the whole of what *on point* requires; (ii) the prose "**a weaker,
model-naming restatement**" and "name a model without it" understate the panellist's own framing and
the harvest note's own reading of it (MAJOR-4).

### MINOR-5 — band 3d was never considered, and there is at least one candidate (also against my own side)
The registration carries band **3d**, "an answer is wrong as stated → critic-side ledger row". The
Q3 results section grades 3a/3b/3c and never says whether 3d was reached. At t=01:55:19, replying
to the relayed GGR-19 formulation, a panellist says: "**that sounds like vaguely related to
Haldane's dilemma, but that's not a thing anymore. That's not like actually an issue.**" That is a
dismissal with no argument attached, offered against the clearest statement of the barrier in the
critic corpus, and it is a candidate for 3d or for an RH row (the surrounding "that's preposterous"
/ "that's just stupid" at t=01:57:03 are already noted at `quotes-critics.md` GGR-19). A pass that
claims its bands were applied should say that 3d was checked and what it found.

**Fix:** one line in Q3 recording that 3d was considered, with the t=01:55:19 line named either as a
3d candidate or as rhetoric under RH1/RH5 (the operator brief's standing instruction that rule RH
applies to the critic side exactly as to Day), and the choice reasoned.

## NOTE

- **NOTE-1 — the correctness review's MINOR-5 is wrong and the Day-side steelman's MAJOR-4 is right;
  decline the substitution.** I recomputed from `R4-G1.md` lines 161–166 without reading either
  review's reasoning first. The column order is `Recombination | Reps | P_fix ÷ Kimura |
  Dispersion of K | P(specified pair)/p² | P(triple)/p³`; the **free** row is
  `4000 | 1.019 | 1.029 | 1.029 ± 0.022 | 1.04 ± 0.08` and the **linked 1 M** row is
  `… | 1.015 | 1.015 ± 0.022 | …`. So the free-recombination pair ratio is **1.029 ± 0.022**, the
  write-up's "1.03 ± 0.02" is correct as cited (and matches R4-G1's own Ga summary row, line 318),
  and 1.015 ± 0.022 belongs to the linked row. Writing 1.015 into the write-up would substitute a
  *linked* result for a *free* one in a sentence about free recombination. The correction happens to
  favour the critics marginally (1.029 is further above independence than 1.015), and I record it
  because the lead must rule, not because of which way it runs.
- **NOTE-2 — I agree with the correctness review's MAJOR-1 and MAJOR-2, and from this side they
  matter more than it says.** The t=01:49:52 line is inside GGR-11's turn, whose speaker the audit
  itself de-attributed on 2026-10-13 (`quotes-critics.md` line 806), and in the transcript it is a
  claim **about 3.0** ("In mittens 3.0, he completely retracts all of his arguments … He kind of
  throws the D coefficient off to the side"), to which GGR-13 is the solicited **reply in
  disagreement** ("Does that sound right to you, especially Grayson?" → "Yeah, I I think that he's
  Yeah, this he's still using the de coefficient in mittens"). Presenting a line the panel's own
  interlocutor was contradicting as Day-side corroboration for reading (a) inverts the exchange. The
  Day-side steelman's NOTE-2 asks to re-label rather than delete, and on A4d's **fact** (3.0 drops d
  from the generation count) it is right that the line is hostile-source corroboration and belongs in
  A4d's Responses. Both can be done: record it as corroboration of the fact, and strike it as
  corroboration of reading (a).
- **NOTE-3 — the SCOPED ruling and the extended-reading bullet are compatible.** I agree with the
  correctness review's NOTE-1 that A4d is `SCOPED` (its Formal statement fixes the reading; no
  `reading-dependent:` comment, no count), and separately with its MAJOR-3 that the *headline about
  GGR-13/14* is still governed by RD's extended-reading bullet. The first is about A4d's own field;
  the second is about which reading of someone else's quote may set a headline. A ruling on one does
  not settle the other.
- **NOTE-4 — credits to the critics that this pass gives properly, and that I confirm.**
  GGR-31/GGR-32 reaching 3,840 independently (the audit's exact value, by a panel with no reference
  to this audit) is recorded first in the "For the critics" list, where it belongs. GGR-20's
  "mentioned once in that paper and not defined" is literally exact, verified: `Bernoulli` occurs
  once, main:55, undefined. NOTE-5's "panel inconsistency" is correctly dissolved and correctly
  booked to the audit rather than netted against either side. GGR-34's standard-theory point is
  recorded as right, in the same table as its cost. Hard rule 1 is satisfied on these.
- **NOTE-5 — a credit candidate the pass could not reach, flagged for the harvest.** The Day-side
  steelman's MINOR-5 names t=01:39:30 (the AI review's "the adaptive fraction is the legitimate open
  empirical question"). I agree it should be harvested, and agree with its framing condition: the
  same passage says the argument "collapses into a much weaker claim" and supports "more research,
  not the conclusion that natural selection is mathematically impossible". Harvested whole or not at
  all. Not this pass's file.
- **NOTE-6 — recomputed with no finding.** G0 hashes (`22bb4ef8…`, `d55e8a03…`) as pinned;
  `252,000` 10× and never multiplied; `450,000` / `225,000` / `202,500` / `0.45` 0; `Bernoulli`
  exactly 1 (main:55); `Averaging` / `law of large numbers` 0; `effective generations` 1 (main:653);
  `recombination` at main:72, 128–129, 423, 454–455; §2's "No recombination overhead" bullet
  verbatim at main:128–131; GGR-19, GGR-20, GGR-41..GGR-44 and GGR-27..GGR-29 exact at their `t=`
  chunks, and GGR-43/GGR-44 and GGR-27..GGR-29 confirmed to be one unbroken turn (transcript lines
  386–392, no `>>` between 02:13:47 and 02:15:49). Hard rules observed: nothing executed, nothing
  from `sources/raw/` committed, no workhorse use, no outward action.

---

## Summary for the lead

The critics' side comes out of this pass **slightly better than the write-up states and
substantially better than the Day-side steelman would leave it**, and it needs no verdict field to
move. The two conflicts the lead flagged resolve as follows. **Q1 reading (c):** do not regrade to
"contradicted" — the Bio-Cycle correction is d by the audit's own C2 definition, §8.6 imports it by
citation in d-corrected units, and the "printed 8" evidence offered for the downgrade is an
unreconciled figure (8 vs 9.13 vs 4.11) that discriminates nothing (MAJOR-1, MAJOR-2). **Q3's
1.03 ± 0.02:** the Day-side steelman is right against the correctness review and I confirm it from
the table (NOTE-1) — but its human-density argument built on 0.84 / 0.65 relies on unlabelled post
hoc rows and an unrun density, against a pre-registered row that failed (MINOR-1). **Band 3b's
height:** not too high; the criterion is clearable in one spoken sentence and was applied as written
(MINOR-4) — but the stated *ground* for the Q3 no-move is wrong, because GGR-43/44 names variance in
fitness, which the write-up itself identifies as the quantity Fisher's theorem uses (MAJOR-4).
**Ge:** the opposite reading fails, rule C does decide it, `holds` is right; the §1 clause should be
booked under RH3 as "no dialectical support offered" (MINOR-2). **Q2:** `pending` stands because the
criterion was pre-registered, but the write-up may not claim that criterion is what the vocabulary
supports — MA-08 says the audit's `contested` is far looser (MAJOR-5). The third error against the
critics is MAJOR-3, and it is a headline overstatement, not a suppressed fact.
