# Fresh-reviewer check of the lead's ruling on L5 / claim C external (D-24 safeguard)

Date 2026-10-14. Reviewer: a fresh reviewer instance (Paperclip EVO-75), using the skill `review-correctness`. Labels: BLOCKER / MAJOR / MINOR / NOTE. **This review sets no verdict and does not answer the owner question of L-R6.** It says whether each ruling survives and, where one does not survive on its stated ground, what ground it has instead. The lead then rules again (D-24).

**Independence.** I wrote none of the following: `R4-L5.md`, its two fix passes, the combined review, the two steelman reviews, the lead's ruling, or the L5 registration. The task requires me to read the ruling and the reviews it rules on, so I read all of them in full. I also read fix pass 2 (b4b7772), because it applies the ruling and lists two departures from it for the lead.

**Read.**
- Brief `research/checks/briefs/L5-reviews-reviewer.md`, addendum L-R1 to L-R10 (l.54-169, 35b196a).
- `results/REVIEW-R4-L5-steelman-day.md` (S1-S10), `results/REVIEW-R4-L5-steelman-critic.md` (K-1 to K-11).
- `results/R4-L5.md` at b4b7772: section 7 (l.237-268), section 8 (l.270-328), section 9 (l.330-357), Review resolution 2 (l.503-544). Section 8-9 as at 0b0431c (`git show 35b196a^:…`, l.250-312), for the text L-R1 quotes.
- `results/R4-L1b-L5-prerun-notes.md`, all of it.
- `l5_adna_power.py` docstring at the registration commit 0e6da82 (l.1-135; bands and moves l.115-127).
- `raw/l5_analysis.txt` (md5 `5e535e9f…7416aa`, matches the hash the critic review cites): neutral rows, mainstream rows x1 to x100, per-cell rows at s = 0.01 and 0.02, gy-25 medians.
- Claim C (front matter, Statement, Formal statement l.39-58, R4 L5 paragraph l.89-101) and the external field before L5 (`git show cb5ed16^:`). Claim C1a (front matter, Statement, Formal statement, l.44-46). Claim C5a front matter. Claim A2e front matter.
- `R4-X1-verdict-rule.md` l.84-86 and rule RD l.196-202. `DECISIONS.md` D-12, D-15, D-23, D-24, O-25, O-26.
- `quotes-day.md` Q26, Q27, Q44. `severe-testing-2026-10-12.md` L5 row (l.359), ST-05, ST-09. `R5-draft.md` 1.3.

**Recomputation** (trivial local checks: one process, stdlib, post hoc, not committed). Every per-cell value below was read from `raw/l5_analysis.txt`.

| Quantity | Value |
|---|---|
| Zero statistics, s <= 0.01, max over 25-y cells | 5.76e-27 (standing, Gazave) |
| Zero statistics, s <= 0.01, max over all cells incl. 20 y | 5.88e-16 (standing, const, 20 y) |
| Zero statistics, s = 0.02 | <= 9.64e-07 at 25 y; 0.0435 at 20 y |
| Neutral model (i), Z50 / Z10 / B10 | 0 in every demography, both designs |
| Mainstream (ii) x1, max at 25 y / x100 at 20 y | 4.66e-31 / 4.75e-18 |
| M10 v62, standing const 25 y, s = 0.02: E 25.2 | P(X <= 1) = 2.98e-10 |
| M10 v62, hard const 25 y, s = 0.02: E 1.05 | P(X <= 1) = 0.717 (no bite) |
| M10 v62, standing const 20 y, s = 0.01: E 10.3 | P(X <= 1) = 3.8e-4 |
| M10 v62, hard const 20 y, s = 0.01 / 0.02: E 0.993 / 16.1 | 0.738 / 1.74e-6 |
| Q44 fixation time (2/0.001) ln 20,000 | 19,807 generations |
| B10 deterministic threshold 2 ln 81 / 280 | 0.0314 |
| Mainstream strong class remapped (28% of F_ii = 4.489, i.e. 1.257 per window) x model (iii) per-completion yield at s = 0.05 (hard 519.8 / standing 285.8 per 15,556) | x1: 0.042 / 0.023; x100: 4.2 / 2.3 |
| Same at s = 0.1 (hard 3,924 / standing 1,237 per 15,556) | x1: 0.32 / 0.10; x100: 31.7 / 10.0 |

The last two rows are an illustration of MINOR-8, not a run: they scale model (iii)'s median yield per completion linearly and assume independence.

## Summary for the lead

| Ruling | Survives? | Ground |
|---|---|---|
| **L-R2** (R-c cannot set the field) | **In its conclusion, conditionally; not on its stated ground** | RD's extended-reading bullet does not cover R-d (S5, accepted in L-R7). The operative ground is the plausibility criterion of L-R7 / fix pass 2, and that criterion turns on exactly the registered owner question. A "no" keeps L-R2; a "yes" removes its premise (MAJOR-1) |
| **L-R4** (scoped `contradicted`) | **The value, yes, if L-R2 or L-R5 holds; the wording, not yet** | The scope wording says more than the run in three places (Z50/Z10 carry no inference in their source; the clock qualifier; the field word on a claim titled by the observation) and less in one (20 y). MAJOR-3, MINOR-4 to MINOR-9, MINOR-11 |
| **L-R1** (the weak-test caveat was never a ground) | **Yes** | The severity limit bears on what the run added, not on the scoped content, which rests on registered arithmetic; the criticality layer itself rates L5 "SEVERE in design for 'no power at s ≤ 0.01'". One misattributed quote (MINOR-10) and one overstatement (NOTE-13) |
| **L-R5** (SCOPED, not reading-dependent) | **Its conclusion probably; its stated ground, no** | C's formal statement fixes the comparator's object, not its s, which is the dimension in dispute. A2e's formal statement named its disputed dimension ("of any effect size"); C's does not. The count stays flat only because every admissible reading gives `contradicted`, which again depends on L-R2 and the owner's answer (MAJOR-2) |

Net: `contradicted` (scoped) is reachable, but on a different chain from the one the ruling gives. The chain is: R-d fails the plausibility criterion, which makes R-c's only admissible disjuncts R-a / R-b, which makes every admissible reading `contradicted`. Its weak link is the owner's answer to the registered question, not R-c. The lead should re-ground L-R2 and L-R5 and restate what each owner answer does before the question is put.

## L-R2: may R-c set the field?

I attacked it in four ways.

1. **Is R-d barred as "extended"?** RD l.202 defines extended readings as "a different object, or a wider claim". The day-side reviewer showed that R-d is neither: it fixes the same unstated parameter as R-a and R-b (S5). The lead accepted S5 in L-R7, and fix pass 2 says the operative ground is now that R-d "fails this criterion" (R4-L5 l.343), not that it is extended. So L-R2's sentence "R-d (… which the same table marks extended and which RD bars from setting the field)" cites a bar that the ruling's own L-R7 removes. There is a symmetry point too. After L-R3, R-e is the literal object (a substitution total) and R-c "adds a mechanism" (R4-L5 l.341). But R-a, R-b and R-d also add the sweep mechanism. If adding a mechanism makes a reading "a different object", all four are extended and only R-e can set the field. If it does not, none of them is. RD has no ground that keeps R-a and R-b in and R-d out. Only the plausibility criterion separates them.
2. **Does the criterion separate them?** Yes. "An s given by Day, or by the mainstream model the comparator stands for" (l.343): R-a (Q44, verbatim) and R-b (Day's 0.01, still to be filed; Uricchio's classes under an ASSUMED mapping) qualify, and R-d does not. On the record as it stands, the disjunction argument then goes through: R-c's admissible disjuncts are R-a and R-b, both `contradicted`. The critic side's K-6 adds that the repo holds no evidence for s ≥ s\* and four items against it.
3. **But the criterion is the registered owner question.** The registration's MIDDLE clause asks for an "owner decision whether Day's model implies s >= s\* (his own beneficial s input is 1e-3)" (docstring l.124-125). "Given by Day" in the criterion and "Day's model implies" in the question are the same test. An owner "yes" makes R-d plausible under the criterion. R-c then has two admissible disjuncts with opposite verdicts, and L-R2's "a disjunction cannot carry a verdict that none of its admissible disjuncts carries" no longer applies. So L-R6's "Under L-R2 it no longer sets the field" is wrong (MAJOR-1).
4. **Is R-c exactly R-a/R-b ∪ R-d?** No. R-b is s ≤ 1e-2 and R-d is s ≥ s\*, which leaves s = 0.02 at both clocks, and 0.03 to 0.05 in hard mode at 25 y, in neither. On the zero statistics that gap behaves like R-b (≤ 9.6e-7 at 25 y at s = 0.02), and no source gives the 15,556 an s in it. So the gap strengthens L-R2's conclusion. It still makes "the undecided disjunction of R-a/R-b and R-d" imprecise (NOTE-14).

**Ruling on L-R2: survives in its conclusion, provided the owner's answer to the registered question is not "yes". Not on its stated ground.**

## L-R4: does the scoped wording say exactly what the run shows?

The value follows if L-R2 or L-R5 holds. Every number in L-R4's text checks against the raw (table above). The wording problems are below, sorted by whom each one helps:
- *More than the run shows, against Day:* the field word on a claim whose title is the observation (MAJOR-3). The inference attributed to Z50/Z10, whose source makes none (MINOR-4). The R-e mainstream bracket at ×100, which rests on an ASSUMED mapping (MINOR-8).
- *Less than the run shows, against the critics:* the clock qualifier, which suggests the scope is clock-limited when the zero result holds at 20 y too (MINOR-5).
- *Inconsistent with L-R5's own logic, toward Day:* the M10 bite is given in standing mode, which the formal statement's "new-mutation" object excludes (MINOR-6).
- *Factual:* "his only stated s" (MINOR-7). R-d's RD category (MINOR-9). The field's earlier grounds are dropped (MINOR-11).

The phrase "the comparator as derived (… the formal statement)" also sits inside "fails for s ≤ 1e-2 … including", as if R-e were one of the s values. R-e is a reading, not an s. Its verdict rests on the Modern Synthesis's own expectation (0 neutral; ≤ 4.66e-31 mainstream), not on model (iii) at low s. It should be its own clause (MINOR-8 fix).

## L-R1: was the weak-test caveat ever a ground for withholding?

It survives. Item 5 of the pre-run note registered "That move stays a proposal for the three reviews; the write-up reports the severity limit beside it" (l.29). That sentence asks for the limit to be reported, not for the move to be withheld. The limit concerns what the run added: P2 and P3 fixed the CRITIC outcome before the run. It does not touch the scoped content, which rests on the registered arithmetic (2 ln 81 / 280 = 0.031 for B10; about 1,000 generations at s ≤ 0.01 against 280) and the trajectory bound. The criticality layer agrees: the severe-testing row for L5 (l.359) rates it "SEVERE in design for 'no power at s ≤ 0.01'". The one precedent for withholding after a weak probe (ST row 52, L7) is different, because there the probe showed the reconstruction itself was weak. Here the probe is weak only because the answer was already proved. Two defects, neither of which changes the ruling: MINOR-10 and NOTE-13.

## L-R5: SCOPED against RD's own text

RD l.198: "A claim whose formal statement fixes the reading (A2e, a count) is `SCOPED`, not reading-dependent; other scopes are recorded as contested." The ruling satisfies the letter of the parenthetical, since C's comparator is "a count". It does not satisfy the operative condition, that the formal statement "fixes the reading" in dispute. MAJOR-2 has the detail.

## Findings

### MAJOR-1: L-R2 rests in practice on the plausibility criterion, which is the registered owner question. L-R6 therefore misstates what the owner's answer does.

*Evidence.* L-R2 (brief l.76-82) bars R-d through RD's extended-reading bullet. L-R7 (l.138) accepts S5, whose point is that R-d is not extended in RD's terms. Fix pass 2 (R4-L5 l.343) accordingly makes the criterion "an s given by Day, or by the mainstream model" the operative ground. The registered MIDDLE question (docstring l.124-125) asks whether Day's model implies s ≥ s\*, which is that same criterion applied to R-d. L-R6 (l.128-129) tells the owner: "Under L-R2 it no longer sets the field, but an owner who holds that R-c governs would keep C external at `contested`." The R4-L5 text repeats this (l.287). Neither answer to the registered question is "R-c governs":
- **"No":** R-d stays outside the criterion. L-R2 holds, and the field takes `contradicted` (scoped) by both routes, L-R2 and L-R5.
- **"Yes":** R-d becomes plausible, and L-R2's premise falls. If L-R5 stands, the field still takes R-e (`contradicted`, scoped) and R-d is recorded as another scope. If L-R5 falls (MAJOR-2), rule RD's charity clause applies to a set of plausible readings that now includes R-d. The field is then open between `contested` and `supported` (scoped, s ≥ s\*), for the lead to rule. It is not fixed at `contested`.

There is a second point. The registration attached the owner question to **band MIDDLE**. The band was CRITIC, whose registered move carries no owner question (docstring l.120-122). Putting the question to the owner is a reasonable precaution, because fix pass 1 and the 2026-10-13 integration answered it themselves. But it is a precaution beyond the registration, not a step the registration requires, and the record should say so.

*Fix.* (a) Re-ground L-R2: R-d is excluded because it fails the L-R7 plausibility criterion, not because RD's extended bullet covers it. Say whether R-a, R-b and R-d are all "a different object" after L-R3 (point 1 of the L-R2 section). (b) Restate L-R6's consequence sentence as the two branches above, so the owner knows what each answer does. Also say that the question is asked as a precaution, since band CRITIC registered none. (c) L-R10's list of what would overturn L-R4 should read "an owner answer that Day's model implies s ≥ s\* (L-R6), together with a finding that the formal statement does not fix the reading (MAJOR-2)", in place of "an owner ruling that R-c governs".

### MAJOR-2: C's formal statement fixes the comparator's object, not its s, so L-R5's stated ground does not carry the SCOPED label as A2e's did.

*Evidence.*
- **What is in dispute.** Section 9's title is "readings of what selection strength Day's argument implies". C's formal statement (l.56) says "This is a genome-wide, new-mutation substitution count" and nothing about s or mechanism. R-a, R-b and R-d in hard mode are all readings of that same object, new-mutation substitutions by selection, at different s. The formal statement does not choose among them. R-e's "no mechanism" is the statement's silence, not its content.
- **A2e is not like for like.** A2e's formal statement named the disputed dimension: "rate_human <= 1/G_f read as a per-generation count of adaptive fixations **of any effect size**" (A2e l.14). That is why the strong-only reading became "another scope". C's has no "of any s".
- **The strongest case for L-R5,** stated so the lead can adopt it: a count of all substitutions, with no filter, is a count of substitutions of whatever s, in the proportions the Modern Synthesis gives them. That is the analogue of "any effect size", and it makes Q276's "the Modern Synthesis expectation" the theory's own expectation (R-e). This is a defensible implication. It is still an implication, not a fix by the text, and the ruling should say that.
- **The ruling uses the formal statement selectively.** "New-mutation" excludes standing-variant sweeps, yet L-R4's M10 sentence gives the bite in standing mode only (MINOR-6). The formal statement's clock is "350 generations at 20 y/gen (blog)" (l.40), yet L-R4 scopes to 25 y (MINOR-5).
- **The formal statement was not written for Q276.** It was written on 2026-10-07 for the observable and the comparator. Q276, the inference the scoped verdict scores, is not in claim C's Statement even now (l.17-35; it appears only in the R4 paragraph, l.89). Rule S scores "only verbatim Statement quotes and their derivation".

*Consequence.* "Not reading-dependent" can still be right, but on another ground. If every admissible reading gives `contradicted` (R-a, R-b, R-e; R-c excluded under L-R2), the verdict does not depend on the reading. That ground is conditional on MAJOR-1's "no". Under L-R5 as stated, the owner's answer cannot move the field. Under this ground it can. That changes what L-R6 is asking.

*Fix.* Either (a) restate L-R5 as the implication above, with the A2e disanalogy said openly, and apply "new-mutation" and "20 y" consistently in the comment; or (b) ground "not reading-dependent" on the agreement of all admissible readings and say that this ground is conditional on L-R6. Before integration, Q275 and Q276 go into claim C's Statement (rule S; fix pass 2 lists this at l.294 as "check that", but the file does not carry them).

### MAJOR-3: The field word `contradicted` on a claim whose title is the observation says more than the run shows to every reader who does not open the comment.

*Evidence.* Claim C's title is "European aDNA shows ~zero fixations from intermediate frequency across ~1.1-1.2M SNPs in ~7,000 years". L5 reproduces that observation in every model, and L-R4's own text says "The observation stands". The scope lives in a YAML comment. `lint_research.py` and the board patches read the field word and nothing in the comment: a grep of `research/checks/lint_research.py` for "scoped" returns nothing, and only two old board patches (`upd14.py`, `upd17.py`) mention "scoped", in prose. A tally, a hierarchy render or a board row will read "C external: contradicted" next to an observation the audit itself reproduces. This is the defect EVO-74 found as MAJOR-2 on A2e, and the same treatment applies. The flip is registered (docstring l.120-122), so the value is licensed; the presentation is not.

*Fix (lead's choice).* (a) A front-matter field that tallies and renders do read (for example `external_scope:`), shown wherever the word is shown. (b) A title or headline amendment that separates the observation from the inference (for example "… ; inference to a refuted required rate: see external"). (c) At the least, the board and count rows print "contradicted (scoped: inference, s ≤ 1e-2)" for C. Without one of these, the integrated field states more than L-R4's scope.

### MINOR-4: The scope attributes the blog's inference to Z50 and Z10, whose source makes no inference.

*Evidence.* Fix pass 2's comment says "the inference from the zero-reported statistics (Z50, Z10, B10)"; L-R4 has "the zero-reported statistics". Q276 is in the blog of 2026-01-14, whose zero statistic is B10 (Q55). Z50 and Z10 are the paper's (Q53), and R4-L5 l.338 says "The paper (Z23046531) carries the observation only." *Fix.* "The inference from the blog's zero (B10, beside Q276) … fails …; the paper's zero statistics (Z50, Z10), reported without that inference, give the same result." This helps Day: it scores only the statement he made.

### MINOR-5: "At Day's current 25-year generation" narrows the scope below what the run shows, and it is not the clock of the derivation scored.

*Evidence.* At s ≤ 0.01 the zero statistics are at most 5.88e-16 at 20 y (standing, const), so the scoped result holds at both clocks. The formal statement and the blog derive the window at 20 y/gen (claim C l.40; "350 nominal generations"). Naming one clock invites a reader to infer that the result is clock-dependent. Fix pass 2 says this itself (l.306), but the comment does not. *Fix.* "fails for s ≤ 1e-2 at 25 y (Day's current value) and at 20 y (the post's own 350 generations)". This helps the critics, and it is what the run shows.

### MINOR-6: The M10 sentence leads with standing mode, which the formal statement's "new-mutation" object excludes.

*Evidence.* At 25 y, s = 0.02, M10 v62 bites in standing const (E 25.2, P 3e-10) but not in hard const (E 1.05, P 0.717). Under the object L-R5 relies on, the hard-mode crossovers are 0.03 at 25 y and 0.02 at 20 y (16.1, P 1.7e-6). Fix pass 2's change 2 adds the hard values in brackets. *Fix.* Give both modes with equal weight, and say which one is the formal statement's object. This cuts toward the critics: the Day-favourable bite at 0.02 is in the mode the formal statement leaves out.

### MINOR-7: "His only stated s for a fixation (1e-3, Q44)" is wrong under L-R7, and the corrected text uses a number not yet checked against its source.

*Evidence.* L-R7 accepts S6: Z18167588 s7.8 uses s = 0.01 in "t_transit ≈ (2/s) × ln(9) ≈ 440 generations" (Q26 note), and Q27 builds "Maximum fixations ≈ (300,000 / 440) × 230" on it. That is a fixation pipeline, so "only" is wrong. Fix pass 2's change 1 names both values, but the 0.01 is from the audit's own note. Its verbatim quote is not filed, and the raw Z18167588 text is not on the workstation (`sources/raw/` holds no Z18167588 directory; fix pass 2 l.337). Hard rule 2 bars recording it in a field comment until it is checked. *Fix.* Accept change 1 on condition that the s7.8 sentence is filed verbatim with its locator and checked against the raw text before integration. Until then the comment says "1e-3 (Q44)", without "only".

### MINOR-8: The R-e ground's robustness bracket ("4.75e-18 at 100 times its rate") depends on an ASSUMED mapping.

*Evidence.* Model (ii) maps Uricchio's strong class to s = 1e-2 ("ASSUMED mapping; the paper's class boundaries are not in the repo", docstring l.77-78). With that mapping every mainstream cell is about 1e-18 or below, up to ×100. If the strong class sits at s = 0.05 or 0.1 instead, the run's own per-completion yields give 0.023 to 0.32 at ×1, which is still below 1, but 2.3 to 32 at ×100 (table above; post hoc illustration). The central conclusion, that the Modern Synthesis's own expectation is about 0 and equal to the observation, survives. The ×100 bracket does not survive as a robustness claim. *Fix.* R-e's clause cites the central value, names the mapping, and drops ×100 as evidence of robustness, or labels it "under the ASSUMED 1e-2 mapping". Write R-e as its own clause, not as an item inside "fails for s ≤ 1e-2 … including".

### MINOR-9: R-d's RD category is not applied consistently.

*Evidence.* Under SCOPED, RD records "other scopes … as contested", and fix pass 2 relies on that clause to refuse K-6's request for R-c (l.525). L-R4 records R-d as "supported, extended", which is RD's other clause (l.202, extended readings keep their own verdicts). After S5, R-d is not extended in RD's terms (MAJOR-1). It is a reading that fails the plausibility criterion. *Fix.* Pick one category for R-d and apply it: "another scope, contested" (the SCOPED clause), or "implausible reading, recorded with its own verdict `supported`, cannot set the field" (the criterion). Then use the same logic for R-c.

### MINOR-10: L-R1 attributes a sentence to the pre-run note that the note does not contain.

*Evidence.* L-R1 (l.69-70): "the same item says the caveat 'does not weaken the low-s result itself'". Item 5 of the pre-run note (l.29) has no such sentence. It is in `R4-L5.md` section 8, reason 1, at 0b0431c ("It does not weaken the low-s result itself, which is checkable arithmetic"). The critic review places it correctly ("The same item then says", meaning the write-up's item). *Fix.* Re-point the quote to R4-L5 §8 reason 1 (0b0431c). The ruling stands either way: one sentence comes from the registration, the other from the write-up, and together they still show that the write-up's own text did not support withholding.

### MINOR-11: L-R4's comment drops the field's earlier grounds, including the Ne contested-standard flag.

*Evidence.* Before L5 the external field was `contested` on other grounds: "observed 1 and 3 mildly above neutral at Ne 1e4, equal at Ne ~7k; admixture not modelled; … C1d reproduces the completions in kind" (`git show cb5ed16^:` l.14). The current field carries these under "Other notes". The comment proposed in L-R4 and fix pass 2 (l.302) does not. Rule l.86 also makes human Ne about 1e4 a contested standard, and "any node whose conclusion depends on it carries the flag in its external column". R-e's neutral leg (model (i) = 0) uses demographies anchored at Ne 1e4. Day contests that value in C5a ("a drift-variance Nₑ near 2"), and C5a's external field is still `pending`. R-a's and R-b's arithmetic leg (sweep time about 2 ln(odds)/s) does not depend on Ne. *Fix.* Carry the "Other notes" forward. State that the scoped result rests on the Ne-independent R-a/R-b arithmetic and on R-e's neutral leg, and that the second is supported independently of θ by C1d's measured between-bin F (0.002-0.014, C5a l.14). The lead should say whether the l.86 flag applies to R-e's leg. The rule does not say whether "the flag" means the word `contested` or a note, and I found no claim file that applies it.

### MINOR-12: L-R8 and L-R5 apply opposite principles to C1a and C.

*Evidence.* L-R5 lets C's formal statement fix the reading. L-R8 makes C1a's reading (i), "not obscure" read absolutely, the governing one because "it is the clause that answers the critics". C1a's formal statement is comparative: "an ascertainment effect increases the expected number of observed completions" (C1a l.25). Its pre-registered prediction and reversal condition also name the comparator: "higher than for a random site sample" and "exceed the unascertained rate" (l.44, l.46). Applied to C1a, L-R5's logic gives (iv) (not computed) or (ii) (supported), not (i). Fix pass 2 raises this for the fresh reviewer (l.326). The field does not change either way: band CRITIC registered C1a to stay `contested`. *Fix.* The lead says which principle governs both claims. If it is the formal statement, C1a's governing reading is the comparative one, (iv), with (i) and (ii) recorded as supported.

### NOTE-13: L-R1's "the kind of move this audit exists to catch when Day does it" overstates.

Fix pass 1 withheld a move toward the audit's own expected band, CRITIC, so the narrowing ran against the audit's prediction, not for it. And at that time the note's own precondition ("for the three reviews") was unmet: D-16 had cut the tier to one review. Not applying the flip then was consistent with the note, even though the reason given was the wrong one. L-R1's conclusion is unaffected.

### NOTE-14: R-c is not exactly R-a/R-b ∪ R-d.

The gap between them is s = 0.02 at both clocks, and 0.03 to 0.05 in hard mode at 25 y. On the zero statistics it behaves like R-b, and no source gives an s inside it. This strengthens L-R2's conclusion, but L-R2's wording should say "s < s\*" rather than "R-a/R-b".

### NOTE-15: The internal `non-sequitur` and R-e's external `contradicted` share the neutral leg.

They are logically distinct: the inference does not follow, and the comparative claim is false. In a tally they will look like two independent marks against Day. The comment should name the legs that are independent of the internal ground: model (iii) at low s (R-a, R-b) and the literature-based model (ii).

### NOTE-16: Standing.

The issue calls C external "load-bearing". Claim C is `load_bearing: false`. The three-review tier applies through both clauses of D-23: the registered flip, and the R5-draft 1.3 feeder row "C / C6 / C1c". No consequence.

## Counts and wrong numbers

BLOCKER 0; MAJOR 3 (MAJOR-1 to MAJOR-3); MINOR 9 (MINOR-4 to MINOR-12); NOTE 4 (NOTE-13 to NOTE-16).

Wrong or misattributed (old -> right):
- L-R4: "his only stated s for a fixation (1e-3, Q44)" -> "1e-3 (Q44)", with 1e-2 (Z18167588 s7.8) added once its quote is filed and checked.
- L-R1: "the same item says … 'does not weaken the low-s result itself'" -> the sentence is in R4-L5 §8 reason 1 (0b0431c), not the pre-run note.
- L-R6 / R4-L5 l.287: "an owner who holds that R-c governs would keep C external at `contested`" -> "no": `contradicted` (scoped); "yes": `contradicted` if L-R5 stands, otherwise open between `contested` and `supported` (scoped).
- L-R2: "R-d … which the same table marks extended and which RD bars from setting the field" -> R-d fails the L-R7 plausibility criterion; RD's extended bullet does not cover it (S5).
- R-e row / comment: "4.75e-18 at 100 times its rate" as robustness -> valid only under the ASSUMED strong-class mapping to 1e-2; 2.3 to 32 at ×100 if the class sits at 0.05 to 0.1 (post hoc illustration).

Every other number in L-R1 to L-R10 recomputes from `raw/l5_analysis.txt` or from the quotes as cited.
