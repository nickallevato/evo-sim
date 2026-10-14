# Fresh-reviewer check of the lead's rulings on B internal (D-24 safeguard)

Date 2026-10-14. Reviewer: fresh reviewer instance (Paperclip EVO-73), skill `review-correctness`. Labels: BLOCKER / MAJOR / MINOR / NOTE. **This review sets no verdict.** It says whether each ruling survives and, where one does not, what the field takes instead. The lead then rules again (D-24).

**Independence.** I wrote none of the following: R4-B2, R4-RHclose, the O5 revert, the three O5 reviews of B, the lead's rulings or the fix pass. The task requires me to read the rulings and the three reviews, so I read them in full. I also read the fix-pass write-up `results/R4-B-internal.md` (54adad7), because it applies the rulings and lists points for this check (P1-P3).

**Read.** Brief `research/checks/briefs/O5-reviews-reviewer.md` Part 1, B-R1 to B-R10 (l.72-191, 35b196a). `REVIEW-R4-B-internal-correctness-2.md`, `-steelman-day.md`, `-steelman-critic.md`. `results/R4-B-internal.md`. Claim file `claims/B-neutral-theory-cannot-rescue.md`. `R4-X1-verdict-rule.md` RH3, RH6, RD (l.191-202). `DECISIONS.md` D-15, D-24, O-6.

**Source text.** `sources/raw/b-steelday-2026-10-13/hl.txt` (gitignored), sha256 `3182a5b6…dbfe2`, the hash of the audit's local text. So "HL l.N" here uses the same numbering as the claim file and the fix pass. I read HL l.15-40, l.95-135, l.200-232 and l.240-467 directly. I did not rely on any review's quotation.

**Recomputation** (trivial local check, stdlib, under a second, post hoc, not committed). Kimura series F(x), x = G/Nₑ, Nₑ = 4·1e5/7, g = 25 y. 6.5 My: x 4.55, F 0.69703. 6.3 My: x 4.41, F 0.67594. 2 My: x 1.40, F 0.02547. These match all three reviews. **New in this file:** F(4.00) = 0.60634, which is HL's own criterion boundary 4Nₑ = G. HL's ceiling X = (Vₖ+2)G/16 at Vₖ 5 is 113,750 at 6.5 My (HL l.250: "about one hundred fourteen thousand"), 110,250 at 6.3 My and 35,000 at 2 My.

## Summary for the lead

| Ruling | Survives? | Why, in one line |
|---|---|---|
| **B-R4** (S cannot govern Q157's field) | **No** | Its ground is false on HL's text. A current-size reading of Q157 that **keeps** "inside the same lineage duration" is HL's own use of that term (l.97-98, l.126-135, l.247-253), and it is supported by Q157's own paragraph (l.456-461), not by Q158 (BLOCKER-1). |
| **B-R5** (C governs; field `non-sequitur`) | **No, as a governing ruling.** Its value under C survives, on a corrected basis. | Because B-R4 falls, a reading of Q157 exists under which the clause is true **and** the inference follows. That is B-R9's first overturn condition. Separately, C's "clause literally true in every window" is false at 6.5 and 6.3 My under HL's own fill criterion (MAJOR-2). |
| **B-R2** (adopt Q157; refuse Q158) | **Yes** | The adoption is sound and the refusal is sound. But the refusal of Q158 does not do the work B-R4 asks of it (MINOR-4). |

**What the field takes instead, on the record as it stands:** `holds`, reading-dependent. It is set on Q157 under reading S_L (BLOCKER-1): at the census the field reports, the neutral pipe cannot fill within the lineage duration. That is HL's census ceiling X at G = lineage duration, which is B2's content. The value is **scoped and never displayed bare**. Recorded beside it, not governing: C (lineage-actual, completion sense) `non-sequitur`; 2 My `non-sequitur`; F `n/a` (B-R6); D, 1e5 and Yoo "N2b not shown". B stays reading-dependent in value, so the count change in B-R8 does not arise.

The lead can keep `non-sequitur` only by ruling S_L **implausible** as a reading of Q157, on a textual ground that answers HL l.247-256 and l.456-461. Showing that S_L is less natural than C is not enough, because RD (l.198) takes the most defensible plausible reading, not the most natural one. The strongest ground available is set out in BLOCKER-1 (iv). In my judgement it makes the lineage-actual reading plausible, but it does not make S_L implausible.

## Findings

### BLOCKER-1: B-R4's ground is false. A current-size reading of Q157's own words keeps the defined term, and under D-15 it governs.
*Attaches to:* brief l.126-140 (B-R4); `results/R4-B-internal.md` l.39 (row S, "a reading of **Q158's** framing"), l.76 (P2), l.103.

**(i) What B-R4 says.** It says S "drops Q157's own defined term 'inside the same lineage duration'", so S "is a reading of a different statement". The ruling answers the Day-side steelman's version of S ("near end", Q158). It also relies on that reviewer's cost item 3, which is a reviewer's concession, not HL text. It does not answer the version that the correctness review had already put (BLOCKER-1, l.38): "Under S, Q157 also reads coherently: at current census the pipe cannot fill within the lineage duration, which is B2's X ceiling with T = 6.5 My." Call that version **S_L**.

**(ii) HL defines and uses "lineage duration" as G, against the census.**
- l.97-98: the criterion is "4 Nₑ < G, where G is the number of generations the lineage has been available".
- l.130-135: X contains "the lineage duration in generations G … Above the census X, a population is too large for a neutral allele to cross it by drift in the time its lineage has existed."
- Abstract, l.15-17: "within the generations its lineage will ever have … for humans at current size".
- l.247-253 is the only place the term is introduced and applied. "Use the lineage duration … roughly six and a half million years … The human ceiling rises … to about one hundred fourteen thousand. And then note that we are still eight billion strong … seventy-two thousand times over the enlarged ceiling. The objection is valid, the correction triples the ceiling, and the conclusion is not changed."
- l.222: "a hundred thousand as a lineage".

In HL's own usage, then, "lineage duration" is the window in which **a census** must fill its pipe. S_L keeps the term in exactly that sense. It does not drop it.

**(iii) Q157's own paragraph names S_L's inputs.** Q157 runs on without a break into l.456-461: "It takes Kimura's own fixation time, Wright's own effective size, and the field's own census, generation, and reproductive-variance figures, and it asks … how long is the pipe." These are the inputs of X = (Vₖ+2)G/16 (l.126-135) and of the census compared with it. The context is Q157's own paragraph, so B-R2's bar on setting a verdict from Q158's wording is not engaged.

**(iv) Under S_L the clause is true and the inference follows on HL's text.**
- *Clause.* At the census scale Nₑ/G is about 1.8e4 to 2.8e4 (variance or census Nₑ, Table 3 l.318, G = 2.6e5; post hoc), so F ≈ exp(−π²·Nₑ/G) ≈ 0, and "never fills" is literal.
- *Inference.* "The neutral substitutions cannot be finished … the neutral channel closes" is HL's own sentence about the census at l.353-354: "the neutral substitutions these species exhibit today are not being seeded at their current size at all. The channel is not slow, it is empty." The fix pass cites this same line (C2, l.53) as HL's sense of "closed". HL's closure vocabulary ("empty", "not slow", "orders of magnitude") is in fact used only of the census regime. HL never calls the lineage pipe empty: it calls it "partly-loaded" or "partly-filled".
- *No exclusion.* HL's partial-load concessions (l.355-360, l.417-419, l.439-441) concern "the smaller populations they descend from" and do not exclude S_L.

So S_L meets B-R9's first overturn condition: "a plausible reading of Q157's own words under which the clause is true **and** the inference follows". RD l.198 then picks S_L over C, because under C the inference fails. S_L is narrower than the lineage-actual claim, not wider, and its object (the pipe at the census over G) is HL's own. So RD l.202 ("a different object, or a wider claim") does not bar it.

**(v) The best case for B-R4, which the ruling does not make.** It is not the defined term. It is the two-channel frame:
- l.444: "the two channels by which a genome is supposed to change";
- the parallel "The adaptive substitutions cannot be paid for; the neutral substitutions cannot be finished";
- l.388-389: species-wide fixation "is … what the human–chimpanzee differences must account for in their entirety".

On this ground, "the neutral substitutions" are the lineage's actual divergence, and S_L narrows them to substitutions seeded at the census. That makes the lineage-actual reading (C) **plausible**. It does not make S_L implausible, for two reasons:
1. HL's own answer to the lineage objection (l.247-256) is the S_L computation, and HL presents it as settling the lineage question ("the conclusion is not changed").
2. HL's closure words fit S_L and not C (iv).

RD records both readings. The field takes the more defensible one.

**(vi) What S_L's `holds` does not say.** It is a counterfactual about the census: humans have been at that size for about 400 generations (l.330). It says nothing on whether drift produced the observed lineage divergence. That is the Day-side cost item 3 and B-R4's own "does not say", and it is why the value must be displayed with its scope. The lineage-level claim in B's title is asserted by no governing reading. RH3's wording applies: "no dialectical support offered".

*Fix.* Withdraw B-R4's stated ground. Add S_L to the Readings table as a reading of **Q157**: tag dialectic; F ≈ 0; derivation HL l.97-98, l.126-135, l.247-253, l.353-354, l.456-461; verdict `holds`, scoped to the census ceiling at G = lineage duration (B2). Either let S_L govern under D-15, or rule it implausible on a ground that answers (ii) to (iv). Keep the existing row S (Q158, "near end") as context.

### MAJOR-2: B-R5's basis, "the clause is literally true in every window", is false at 6.5 and 6.3 My under HL's own fill criterion
*Attaches to:* brief l.144-147; `results/R4-B-internal.md` l.32 (row C), l.49 (C0, threshold "between 0.70 and 0.999"), l.51 (C1), l.83 ("literally true on HL's inputs in every window").

HL's operational test for filling is 4Nₑ < G (l.97-98), and its ceiling statement says populations below X fill:
- l.135: "Below X, fixation can …";
- l.437-438: "the only census population that fills the pipe in time is one too small to sustain a viable species";
- l.362-363: "when a lineage sits near its own X … the pipe substantially fills, and Kimura's rate is approached".

At HL's lineage inputs the hominid census 1e5 is **below** HL's own X (113,750 at 6.5 My; 110,250 at 6.3 My), and x = 4.55 > 4 (F 0.697 against F 0.606 at the criterion boundary). By HL's criterion, that pipe fills.

The completion sense read asymptotically (F < 1) would make "never fills" true of every population of any size. l.437-438 contradicts that, so it is not HL's sense. The fix pass's threshold of 0.70 to 0.999 is post hoc and has no anchor in HL. The clause is true under C only at 2 My, Yoo and Takahata 1e5 (x < 4), which are the non-governing rows.

*Effect on the value.* Under C the value is still `non-sequitur`, on a stronger basis: N2b now applies to the clause itself, which HL's own criterion and ceiling contradict, as well as to the inference. B-R5's value under C survives. Its stated basis ("the clause is true; the field turns on the inference") does not, and the Day-side credit "literally true on HL's inputs in every window" (fix pass l.83) must be withdrawn for the 6.5 and 6.3 My windows.

*Fix.* Restate row C and C0/C1 on HL's criterion: at 6.5 and 6.3 My, "never fills" is contradicted by l.97-98, l.250 and l.437-438; at 2 My it is true. Correct "Who this helps".

### MINOR-3: B-R5's hominid-specific "partly-loaded" evidence is HL's 2 My linear-bound passage, which HL itself disowns
*Attaches to:* brief l.150-152; `results/R4-B-internal.md` l.57.

l.363-366 ("thirty-five percent — a partly-loaded pipe") is the linear bound over "the full two million years". HL calls that bound "an overstatement, and a vast one" (l.302). HL's own exact law gives F 0.025 there. B-R3 also sets 2 My aside as a window HL gave up. Used as an exclusion of P\* at 6.5 My, the passage is at best an a fortiori argument. The 6.5 My exclusion stands without it, on k(T) = μF(T) (l.287-291; 0.697) and l.362-363.

*Fix.* Cite l.287-291, l.362-363, l.419 and l.439-441 as the basis, and l.363-366 only as an a fortiori point with HL's l.302 noted.

### MINOR-4: B-R2 survives, but it does not do the work B-R4 asks of it
*Attaches to:* brief l.97-106, l.133.

- **Adopting Q157 is sound.** It is the only quote asserting B's own claim, all three reviews asked for it, and R4-B2 l.24 had already required it.
- **Refusing Q158 is sound.** Q158 ("for every large animal it had ever dated, the pipe was nearly empty") asserts B2's near-end content, not B's. Under the B-R7 aggregation rule, adopting it would not change which quote sets the field, so the refusal is neutral in effect.
- **But the refusal does not carry B-R4.** B-R4 reasons "S belongs to Q158, and Q158 is not adopted, so S cannot govern". S_L rests on HL's definitions and on Q157's own paragraph (BLOCKER-1 ii-iii), so refusing Q158 leaves it untouched.

*Fix.* None to B-R2 itself. Drop "with B-R2 …" (l.133) as a ground in any restated B-R4.

### NOTE-5: P1's C′ is not the strongest overturn
The fix pass (P1, l.75) offers C′ (completion sense, weak inference) as the point to attack. Under MAJOR-2 the C′ clause is also false at 6.5 My on HL's criterion, so C′ is weaker than the fix pass thinks. The overturn that meets B-R9 is S_L (BLOCKER-1), not C′.

### NOTE-6: the B-R7 aggregation rule is a rule, not a fix
"An internal field takes the governing reading of the Statement quote that asserts the node's own claim" (brief l.170-172; fix pass l.13) is new text that the verdict rule does not contain (correctness NOTE-12). It is not one of the three rulings this check covers. Under O-6 as accepted (DECISIONS l.86), any rule change needs a written proposal, a 24-hour cooling-off and a re-score of the load-bearing verdicts it moves. It moves nothing here (every reading in play is of Q157), but the lead should say whether O-6 applies.

### NOTE-7: B-R8 does not arise if BLOCKER-1 is accepted
With S_L governing, B's derived readings are {`holds` (S_L), `non-sequitur` (C, 2 My), `n/a` (F)}. B therefore stays reading-dependent in value, and the count change B-R8 flags is not triggered.

## Who this helps
- **Day side.** The field's governing reading becomes the one HL itself uses for its defined term, and under it Q157 is true and follows (`holds`, scoped). This is the Day-side steelman's F2 outcome, reached here by a reading that keeps "lineage duration" rather than by "near end".
- **Critic side.** The lineage-level claim is asserted by no governing reading. Under the lineage-actual reading (C) the non-sequitur is **stronger** than B-R5 says: HL's own criterion contradicts "never fills" at 6.5 My (MAJOR-2). The `holds` is a statement about a census the lineage occupied for about 400 generations (l.330), and it must never be shown bare.
- **The audit.** A lead ruling was built on a reviewer's concession instead of the source's definitions. The record had already stated the version of S that the ruling needed to answer (correctness BLOCKER-1, l.38), and the ruling did not answer it.

## Counts and wrong numbers
**1 BLOCKER, 1 MAJOR, 2 MINOR, 3 NOTE.**

Wrong numbers: none. One wrong claim: "the clause is literally true on HL's inputs in every window" (fix pass l.32, l.49, l.51, l.83; brief l.145-146). It is true at 2 My, Yoo and Takahata 1e5, and **false at 6.5 and 6.3 My** under HL's criterion 4Nₑ < G (x 4.55 and 4.41 > 4; census 1e5 < X 113,750 and 110,250).
