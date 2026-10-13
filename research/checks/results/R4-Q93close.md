# R4 Q93close: the "remotely close" test (RH6, RD) applied to Day's Q93, "over 10,000 ... will not fixate at all"

**Status: pre-registered (0ee6292), run once, written up. Not reviewed (one combined review to follow: `REVIEW-R4-Q93close-combined.md`). Not integrated: no claim file, quote tag, ledger, QUEUE, REVIEW.md or argmap edits. The tag and verdict comments below are proposals.** Low-stakes tier (ROADMAP A6; QUEUE item 15 follow-up). **Result: reading-dependent.** 6 of 25 registered readings are true or within the 3x band, 19 are outside it.

## Files
- Script `research/checks/q93_closeness.py`, pre-registered at **0ee6292**, run locally once after that commit (stdlib, 0.2 s), not edited since. It imports `F`, `f_drift` and `verify` from `rhclose.py` (R4-RHclose).
- Raw output `research/checks/results/raw/q93_closeness.out` and `.json`.
- Sources, all verified by the script as substrings (0 misses):
  - Day comment 337074301 (2026-09-14T18:11Z, not edited), parent McCarthy comment 337048907 and Q96 comment 335823489: `sources/raw/refresh-2026-10-09/mccarthy-comments-why/comments.json`, sha256 cba6b15b...da92bc.
  - Hard Limits (Z22129121, 2026-08-27): `sources/raw/day/zenodo-22129121.txt`, sha256 3182a5b6...9dfe2.

## Disclosure (read first)
Not blind. Known before registration: the hand arithmetic in `R4-RHclose-critics.md` (F_drift about 140/N, crossing 1e-4 near N = 1.4e6), the R4-B2 fill values, claim B2b's ceiling table (35,000 and 113,750 against "about ten thousand"), and C7 reading R3. What was registered is the readings, the criteria, the selection rule and the mapping. Not computed before the run: the roots x_a, x_b and every cutoff that depends on them.

## Target
**Q93** (Vox Day, McCarthy Substack, comment 337074301, 2026-09-14): "In any population over 10,000, neutral substitution will not fixate at all."

The sentence names no window and does not say whether 10,000 is a census or an effective size. What the same comment puts on the table:
- Before: "With the standard human effective population size, Nₑ = 10,000:" and "t̄ = 4 × 10,000 = 40,000 generations. At 25 years per generation, that's 1,000,000 years per neutral fixation."
- Directly before: "Now, it's actually a lot worse for the neutral substitution case than that, because there is a hard limit to genetic drift even being able to affect a population."
- Directly after: "And we have actually found empirical evidence for this mathematical barrier in the ancient DNA database."
- Parent comment (McCarthy): "over the course of 9 million years", "in a population of 10,000 humans".
- Same thread, a day earlier (Q96): "over the last 7000 years".
- The "hard limit" is Hard Limits, published 18 days earlier. Its l.52-54 is nearly the same sentence, and it does name a window: "A population of 10,000 is roughly where drift permanently stops for an animal like us, the size of the population below which a neutral allele can still cross the whole population by chance in all the generations its lineage will ever have, and above which it cannot." Its criterion is "4Nₑ < G, where G is the number of generations of the lineage concerned", with the census frame "Nₑ = (4N − 2) / (Vₖ + 2)".

## Readings, quantity and criterion (pre-registered)
A reading is a window, a meaning of "10,000" and a meaning of "will not fixate at all".
- **Windows** (generations, 25 y): W1 none (steady state); W2 280 (the aDNA 7,000 y); W3 40,000 (the comment's 4N_e figure as a fixed window); W3s 4N_e scaling with N; W4 80,000 (HL species window, 2 My); W5 260,000 (HL lineage, 6.5 My); W6 360,000 (McCarthy's 9 My).
- **"10,000" as:** `Ne` (the comment's own "Nₑ = 10,000"); `wright` (census, N_e = (4N - 2)/7, the Hard Limits frame, so N_e = 5,714 at N = 10,000).
- **"Will not fixate at all" as:**
  - Ca: exact fill F(T/N_e) <= 1e-4. F is the Kimura diffusion probability that a new neutral mutation destined to fix has fixed by T, which is also Day's own flux k(T)/mu. The 1e-4 band is the one R4-RHclose fixed for "at all" in Q96.
  - Cb: F <= 0.10 (the "never fills" band of R4-RHclose Part 2).
  - Cc: Day's own criterion in Hard Limits, "will not" iff 4N_e > T.
  - Cd: the C7 standard named in the queue entry, F_drift <= 1e-4 (W2 only).
- **N\*** is the true cutoff under a reading: the population size above which the criterion holds for every larger population.
- **3x band on the literal value 10,000** (RH6): TRUE if N\* <= 10,000; CLOSE if N\* <= 30,000; OFF-10x if N\* <= 100,000; OFF beyond. Tag per reading: `dialectic` if TRUE or CLOSE, else `rhetoric`.
- **Cutoff column** (reported, not used for the tag): LOCATED if N\* is within 3x of 10,000 either way; SLACK if N\* is more than 3x below it (true, but equally true of far smaller populations); HIGH if more than 3x above.
- **Selection rule for the verdict-field reading** (RD): best status first; ties by textual anchor (W5, W4, W2, W3, W6, W3s, W1), then N meaning, then Cc, Ca, Cb, Cd.

## Readings table (25 used rows, from the raw output)
Roots: F = 1e-4 at x_a = 0.730; F = 0.10 at x_b = 1.870.

| Window | "10,000" as | Criterion | Value at N = 10,000 (vs band) | True cutoff N\* | N\*/10,000 | Status | Cutoff | Tag |
|---|---|---|---|---|---|---|---|---|
| W1 steady state | Ne | flux k/mu | 1 at every N | none | inf | OFF | HIGH | rhetoric |
| **W2 280 gen** | Ne | **Cc (selected)** | window = 0.007 mean fixation times | **70** | 0.007 | **TRUE** | SLACK | dialectic |
| W2 | Ne | Ca | F < 1e-12 | 384 | 0.038 | TRUE | SLACK | dialectic |
| W2 | Ne | Cb | F < 1e-12 | 150 | 0.015 | TRUE | SLACK | dialectic |
| W2 | wright | Ca | F < 1e-12 | 672 | 0.067 | TRUE | SLACK | dialectic |
| W2 | Ne | Cd (C7 standard) | F_drift 0.0139 (139x) | 1,399,930 | 140 | OFF | HIGH | rhetoric |
| W2 | wright | Cd | F_drift 0.0242 (242x) | 2,449,878 | 245 | OFF | HIGH | rhetoric |
| W3 40,000 gen | Ne | Cb | F 0.606 (6.1x) | 21,386 | 2.1 | CLOSE | LOCATED | dialectic |
| W3 | Ne | Ca | F 0.606 | 54,815 | 5.5 | OFF-10x | HIGH | rhetoric |
| W3s 4N_e(N) | Ne | Ca | F 0.606 at every N | none | inf | OFF | HIGH | rhetoric |
| W4 80,000 gen | wright | Cc (HL's own frame) | window = 3.5 mean fixation times | 35,000 | 3.5 | OFF-10x | HIGH | rhetoric |
| W4 | wright | Ca / Cb | F 0.997 | 191,854 / 74,852 | 19 / 7.5 | OFF / OFF-10x | HIGH | rhetoric |
| W4 | Ne | Cc | window = 2 mean fixation times | 20,000 | 2.0 | CLOSE | LOCATED | dialectic |
| W4 | Ne | Ca / Cb | F 0.945 | 109,630 / 42,772 | 11 / 4.3 | OFF / OFF-10x | HIGH | rhetoric |
| W5 260,000 gen | wright | Cc (HL's own frame) | window = 11.4 mean fixation times | 113,750 | 11.4 | OFF | HIGH | rhetoric |
| W5 | wright | Ca / Cb | F 1.000 | 623,524 / 243,268 | 62 / 24 | OFF | HIGH | rhetoric |
| W5 | Ne | Cc | window = 6.5 mean fixation times | 65,000 | 6.5 | OFF-10x | HIGH | rhetoric |
| W5 | Ne | Ca / Cb | F 1.000 | 356,299 / 139,010 | 36 / 14 | OFF | HIGH | rhetoric |
| W6 360,000 gen | Ne | Cc | window = 9 mean fixation times | 90,000 | 9.0 | OFF-10x | HIGH | rhetoric |
| W6 | Ne | Ca / Cb | F 1.000 | 493,337 / 192,475 | 49 / 19 | OFF | HIGH | rhetoric |

Counts: TRUE 4, CLOSE 2, OFF-10x 6, OFF 13.

Reported, not used:
- **W3 with Cc is an identity.** N\* = 40,000/4 = 10,000 exactly, because the window was defined as 4 x 10,000. It is circular and shows nothing about closeness.
- **Per-mutation reading** (a given new mutation, unbounded time): P_fix = 1/(2N) = 5e-5 at N = 10,000. It is scale-free, so it has no cutoff; a 1e-4 band would put one at 5,000, which is an artefact of the band. Day's own arithmetic in the thread uses 1/20,000, which is not zero.
- Absolute probability that a given new mutation has fixed within the window at N_e = 10,000: W2 < 1e-12; W3 3.0e-5; W4 4.7e-5; W5 and W6 5.0e-5.
- N_e/N = 0.1 (Frankham 1995, unverified in `parameters.yaml`): the C7-standard cutoff rises to a census of 1.4e7, and the HL-lineage cutoff to 650,000. A realistic census-to-effective ratio moves every long-window row further from 10,000.
- 20 y per generation (350 generations), C7 standard: cutoff 1.75e6.

## Which reading is most defensible (RD: all recorded, none picked for the speaker)
- **Selected by the registered rule: W2 / Ne / Cc.** Within the 7,000-year ancient-DNA window, no new neutral mutation completes fixation in any population over 10,000. This is true, and the sentence after Q93 points at exactly that evidence.
- **It is true with a great deal of slack.** The same statement is true of any population over about 70 to 700. The "over 10,000" does no work on this reading. This is the C7-R3 situation: true as a count, and also what neutral drift predicts.
- **The reading closest to Day's own text does not pass.** Hard Limits l.52-54 gives the window ("all the generations its lineage will ever have") and the frame (census, Wright N_e). On Hard Limits' own criterion and its own two human windows the cutoff is 35,000 (3.5x, just outside the band, inside 10x) or 113,750 (11.4x). This restates B2b's existing discrepancy (i). At a census of exactly 10,000 the window is 3.5 to 11.4 mean fixation times and the exact fill is 0.997 to 1.000.
- **Two readings locate the cutoff near 10,000:** the 2 My window with 10,000 read as N_e (cutoff 20,000), and the comment's own 1 My figure as a fixed window with the loose band (cutoff 21,386). Neither is Day's stated frame: Hard Limits uses census with Wright's formula, and 40,000 generations is offered as a fixation time, not a window.
- **No window at all** (steady state): the flux is mu at every N, so there is no cutoff. On the C7 standard the cutoff is 1.4e6 (140x), as the queue entry expected.

## Scoring of pre-registered predictions (not blind)
| ID | Prediction | Result | Score |
|---|---|---|---|
| P1 | x_a in [0.60, 0.95]; x_b in [1.80, 2.00] | 0.730; 1.870 | Holds |
| P2 | C7 standard: 0.0139 at N = 10,000; N\* 1.40e6 (wright 2.45e6); OFF | 0.0139; 1,399,930; 2,449,878 | Holds |
| P3 | W2 fixation rows: F < 1e-12, N\* < 1,000, TRUE and SLACK | N\* 70 to 672 | Holds |
| P4 | HL frame: N\* 35,000 (OFF-10x) and 113,750 (OFF); F >= 0.80 and >= 0.999 at census 10,000 | 35,000; 113,750; 0.997; 1.000 | Holds |
| P5 | W4 Ne Cc 20,000 CLOSE; W5, W6 Ne Cc OFF-10x; all W4-W6 Ca rows >= 80,000 | as predicted (smallest 109,630) | Holds |
| P6 | W3: F(4) = 0.63 ± 0.01; Cb N\* in [20,000, 22,300] CLOSE; Ca in [42,000, 67,000] OFF-10x | **F(4) = 0.606**; 21,386 CLOSE; 54,815 OFF-10x | **Miss** (the value; both statuses as predicted) |
| P7 | W1 and W3s: no cutoff, OFF | OFF | Holds |
| P8 | Selection W2 / Ne / Cc, TRUE, SLACK; outcome (a) reading-dependent | as predicted | Holds |
| Day side | Most defensible reading is remotely close | TRUE on the selected reading (as a count, with slack) | Holds on that reading |
| Critic side | Every reading is outside the band just above 10,000 | 6 of 25 are TRUE or CLOSE | Fails as a universal; holds on 19 rows, including W1, the C7 standard and HL's own frame |

**P6 miss.** The audit's 0.63 was a misremembered value (F(4.06) = 0.62 from R4-RHclose). F(4) is 0.606. The docstring's "F = 0.63 at every N" for W3s carries the same wrong figure. No status depends on it. Self-tests pass: F(1.40) = 0.0255 and F(4.55) = 0.697 as in R4-B2; the exact Wright-Fisher chain (2N = 100) is within 0.015 of the diffusion F at x = 2, 4, 8.

## Proposed tag and verdict comments (pre-registered mapping, outcome (a); proposals only)
- **Q93 RH tag: `reading-dependent` (RD); value `dialectic` on the selected reading** (W2 fixation count: true, cutoff slack). Rhetoric on W1, on the C7 standard, on HL's own census frame over both HL windows, and on McCarthy's 9 My.
- **No claim verdict moves.** Q93 is in no claim's Statement block, so under rule S it scores nothing directly.
- **B2b:** add a Q93 Readings table under the existing discrepancy (i). Verdicts unchanged (holds / unverifiable / contested).
- **The step from the true reading to a "hard limit" or "mathematical barrier" at 10,000** is the non-sequitur already scored at claim C (X1 row C). Zero completed fixations in 280 generations is the neutral expectation at every N above a few hundred. Nothing new is scored.
- **B5:** its note "queued as a Day-side closeness re-test" can be closed by reference to this check. The withdrawn "false at every N" stays withdrawn: it is right on W1 only.
- **Ledger proposal** (`ledgers/slips.md`, for the rhetoric readings). Device: universal plus absolute ("any", "not at all") with a round cutoff. Audience: a critic's comment thread. Function: turns a slow rate into a wall. Core: B2 and B2b. Better rhetoric: "Hard Limits' own table puts the human ceiling at 35,000 to 114,000, not 10,000, and at 10,000 its own flux formula gives a full pipe. The one window where nothing fixes above 10,000 is the 7,000-year one, where nothing fixes above 700 either."

## Who this helps
- **Day side.**
  - The statement is literally true on the window his next sentence invokes. The earlier critic-side line "false at every N" was wrong to drop the window, and its withdrawal stands.
  - Two further readings put the cutoff within about 2x of 10,000.
  - On his own criterion with the 2 My window the miss is 3.5x, just outside the band and inside the 10x sensitivity.
  - His point against McCarthy's reply, that the time component matters, is real: within 1 My at N_e = 10,000 the exact fill is 0.61, not 1.
- **Critic side.**
  - At steady state the neutral substitution rate is mu at every population size. There is no cutoff.
  - On Hard Limits' own frame a population just over 10,000 fixes neutral mutations freely (fill 0.997 to 1.000), and the paper's own ceilings are 3.5 to 11.4 times higher.
  - Over McCarthy's 9 My, the window actually in dispute in that exchange, the cutoff is 90,000 to 490,000.
  - On the C7 drift standard the cutoff is 1.4 million.
  - Where the statement is true, the number 10,000 does no work, and the evidence cited for a "barrier" is what neutral theory predicts.
- **Both.** The tag turns on the window, which the sentence omits. 19 of 25 registered readings are outside the 3x band and 4 are true. No verdict moves either way.

## Caveats
- Diffusion limit, constant size, neutral, pipe empty at the window start. Pre-window fill only raises F.
- The bands 1e-4 and 0.10 are judgements inherited from R4-RHclose. The 3x band is applied to the cutoff (the only number in the sentence), not to the value at the boundary as in C7; the value-versus-band ratio is given in the table for comparison.
- A row count is not a vote: the 25 rows are not equally plausible, and W4 to W6 contribute 15 of them.
- RH tags classify statements; they do not make them true.

## Open
1. **Does SLACK count as close?** The registered rule tags a true-with-slack universal `dialectic`. A reviewer may hold that a claimed threshold which is off by 15 to 140x on the low side is not "remotely close" as a threshold claim. On a two-sided 3x test only the two LOCATED rows pass.
2. **Is W2 a fair window for Q93?** The 7,000 years is in Q96 and in the aDNA papers, not in this comment; the comment says only "the ancient DNA database".
3. **Anchor order.** The tie-break put HL first, but no HL row reached TRUE, so status decided. If textual closeness came before status, the selected reading would be HL's own frame (OFF-10x at 2 My, OFF at 6.5 My) and the value would be `rhetoric`. The owner's RD rule as written (most defensible) gives the W2 row.
4. **Where the Readings table lives** (B2b proposed; B2 or C7 are alternatives), and whether Q93 should get a tag line in `quotes-day.md`.
5. The docstring's wrong F(4) figure (0.63) stays as registered; correct it only in a commit labelled post hoc if the review asks.
