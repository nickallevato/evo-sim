# Review of R4-B2: critic-side steelman

Reviewer role: argue for the critics (Mansfield, McCarthy, B2a's latency reply, B1c) as strongly as honesty allows, then judge fairness. Date: 2026-10-10. Targets: `results/R4-B2.md`, `research/checks/b2_hard_limits_internal.py` (3d07343, unchanged), `results/raw/b2_hard_limits.out`, the HL text `sources/raw/day/zenodo-22129121.txt` (read by line range, as data), claim files B, B2, B1c, B1d and B6, `R4-X1-verdict-rule.md`, and `quotes-day.md` Q29-Q34. The diffusion values not in R4 come from the scratch series described in `REVIEW-R4-B2-correctness.md`. No repo run.

## Verdict in brief
The check is careful and pre-registered, and on B2 it reaches the right result. On the critic side it errs in two places. First, it promotes P6 ("best-case fill 3%") to a Day-side headline, although that figure rests on two premises Day himself gives up: a 2 My window, and an empty pipe at the start. Second, it hangs the rule-N finding on a paraphrase, when HL contains a verbatim sentence that carries B and can be scored against HL's own drainage text. It also understates how much of HL agrees with the critics. HL itself concedes the steady-state flux, the drainage, and a partial ancestral load.

## The strongest honest critic-side case
1. **On its own words, HL concedes the critics' main point.** "At steady state the total flux out is μ per site regardless of how long any individual site took to traverse" (l.267-268). The observed substitutions are "residual drainage from the smaller populations they descend from" (abstract l.22-24). The clock rate "was loaded, at least partially" in the past (l.440). That is the critics' position (Mansfield "drift happens in every population"; B6 "ancestral pipe full"), stated by Day.
2. **On HL's own accepted window, the H8 input fills.** HL accepts the lineage window ("The objection is valid", l.252; Table 1 l.157, 6.5 My). At census 1e5 with V_k = 5, T/N_e = 4.55: F = 0.70, and the time average from an empty start is 0.26. At the lineage ceiling X that H8's census sits on, T = 4N_e and F = 0.61. l.361-363 says the same thing in words: near X "the pipe substantially fills". The "nearly empty" 3% exists only on the 2 My species window.
3. **Day later concedes a full pipe at exactly that input.** B1d (blog 2026-10-01 ¶36): "At the time of the CHLCA split, we can assume that it was full and 228,000 generations long, so fixations can be reached around now." 228,000 = 4N_e at census 1e5 and V_k = 5. B1c already scored the empty-start premise `contradicted`.
4. **The law Day used to close the argument understates the exact tail where it matters.** It is 33x low at H8, and 48x low (diffusion) at T = N_e. HL's "order-one constant ... two orders of magnitude" is a growing power-law prefactor, not a constant. That is immaterial to the human exponent, but it is a slip on a stated quantitative claim.

## What does not survive scrutiny (Day's side of this steelman)
- At current size the exponent is right and overwhelming (7.8e7 decimal orders). No critic needs current-size seeding, and none should dispute B2 read as a current-size claim. B2a's "latency, not throughput" reply answers a throughput claim that HL explicitly disowns (l.262-270), so as a reply to HL it lands on nothing.
- The field's 1e4 is a coalescent figure that HL rejects (l.101-118). The critics cannot cite it as HL's own input. The critic rows at 1e4 and 2.5e4 are external (B1c, B4a), not internal.
- The delivered count from an empty start is lower than the F(T) figures in R4: 51% at N_e = 1e4 over 2 My, not 95%. The critics' "95-100% full" is the end-of-window flux. Without pre-window fill, the critic case at 2 My is about half, not full.

## Findings

### F1 (MAJOR). "P6 failed in Day's favour (best-case fill 3%)" rests on two premises Day abandons
Locator: R4 P6 row, "Who this helps", Day side ("at his best-case ancestral input the exact fill is 3%"), and the Rule N table, first row. The commit message and QUEUE carry the same wording.

Problem.
- The 2 My window contradicts HL's own accepted lineage window (l.244-253, Table 1).
- The empty start contradicts Day's later full-at-split statement at the identical census (B1d ¶36) and B1c's verdict.

On HL's lineage window the same input gives F = 0.70. With B1d's full start, it gives about 1. The P6 result legitimately shows one thing: HL's linear bound overstates the 2 My, empty-start fill. That is a statement about HL's arithmetic label ("generous"), not about the ancestral pipe.

Fix. In the P6 row, the headline and "Who this helps", say: "HL's 35% linear bound is generous; the exact empty-start fill at H8's census over 2 My is 0.029 (time average 0.003). On HL's lineage window (6.5 My) the same census gives 0.70 (0.26), and Day's later reply (B1d) grants a full pipe at the split." Add the 6.5 My row to the table. Steelman-day D5 agrees on the substance.

### F2 (MAJOR). Rule N should be retargeted to a verbatim HL sentence, not dropped
Locator: R4 Rule N section. The correctness review (finding 1) and steelman-day (D1) both find the current target invalid.

Problem. HL l.453-457 reads: "And now the neutral channel closes on the same window for an entirely independent reason. The adaptive substitutions cannot be paid for; the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the priced channel and the free channel shut inside the same lineage duration."

The case for tagging it `dialectic` under RH1:
- It carries the paper's conclusion. It is the step that joins HL to Haldane, and so to ROOT.
- It makes a checkable claim: no fill "inside the same lineage duration".
- It is not hyperbole. Its numbers are those of the body.

Rule C on the referent was tried. "Never fills" read as "at current size" does not fit "inside the same lineage duration", which names the whole lineage window, and HL Table 1 sets that window at 6.5 My.

On that reading the sentence needs a premise that HL's own text excludes:
- abstract l.22-24, drainage from smaller populations;
- H7, "short enough to fill";
- l.361-363, "substantially fills" near X;
- l.440, "loaded, at least partially".

That is N2b within one source. B's Statement should quote it under S1.

Fix. Add l.453-457 to B's Statement with its RH1 tag. Score it under N2b with the rule-C reading recorded. If the tag is `dialectic`, propose B internal `non-sequitur` (HL basis). If integration accepts steelman-day's `rhetoric` tag, the verdict is `holds`, and the RH2 entries go to the ledger. Either way the decision must be on the record.

### F3 (MINOR). The prefactor credit to critics is stated as a constant; it is a growing power law
Locator: P3 row ("It is a prefactor, as HL says").

Problem. "As HL says" concedes HL's description. HL says "an order-one detail that could be wrong by two orders of magnitude" (l.303-304). The diffusion ratios (48 at T = N_e, 18 at 2N_e) imply growth of about (N_e/T)^1.5. That is about 11 decimal orders at H5's N_e/T, not 2. It is immaterial to 7.8e7 (R1), so it is a ledger slip, but "as HL says" is not accurate.

Fix. Replace "as HL says" with "a power-law prefactor; HL's 'two orders' is a slip (ledger, R1-immaterial)". Quote the diffusion values so that discreteness at T = N_e/4 is not counted (correctness finding 6).

### F4 (MINOR). The critics' rescue figure should be the delivered count, plus pre-window fill, not F(T) alone
Locator: "Who this helps", critic side ("95-100% full").

Fix. Report flux and time average together (0.95 / 0.51 at 1e4, 2 My; 1.00 / 0.85 at 1e4, 6.5 My). State that pre-window fill raises both: B1c gives an excess under every tested history, and B1d concedes a full pipe. That keeps the critic case accurate rather than inflated.

### F5 (MINOR). H10 against HL's own ancestral picture is pre-registered and omitted
Locator: script docstring P7 ("H9 with H10 is also scored ... recorded"); the write-up has no H10 line.

Problem. H10 (l.206-207) reads: "There is no census at which a large vertebrate is simultaneously large enough to be a viable species and small enough to fix a neutral allele by drift." HL's own drainage thesis needs hominid ancestors that were viable and small enough to load the pipe. H8 places them in "the near-ceiling regime", and Table 1 puts the lineage ceiling at 114,000 against H8's census of about 1e5. Under rule C (H10 is said of the elephant's 2 My species window, and of "non-endangered" species) it can stand. The tension should still be recorded, as pre-registered. H10's sequel, "The window is not narrow. It is empty", is correctly tagged rhetoric.

Fix. Add the H10 line: dialectic, rule-C reading recorded, no verdict change, ledger.

### F6 (MINOR). Mansfield credit needs its scope note
Locator: "Who this helps", critic side ("Mansfield's 'drift happens in every population' is consistent with HL's own k(T) = μF(T) at small N").

Problem. The B2 claim file records that the comment predates HL and replies to a different Day sentence (UgyhNduYke46IStQ5pd4AaABAg). Consistency with HL is fair to note, but as written it reads as a rebuttal of HL.

Fix. Add "(predates HL; aimed at a different statement)".

### F7 (MINOR). Record B2a's reply as answered by HL itself, and credit it
Locator: "Who this helps", Day side ("B2a's 'latency, not throughput' reply answers a claim HL does not make").

Problem. That is true of HL. But B2a was written against the abstract's "chance of fixing within the generations its lineage will ever have" (Q30), which reads as a throughput claim unless the body is read. HL's own concession (l.262-270) is the evidence that the critics' reply was correct on the mechanics.

Fix. Add one sentence: "HL concedes the throughput point; the critics' reply was right on the mechanics, and HL relocates the dispute to fill state."

## View of the verdicts
- B2 internal `holds` (current size, abstract l.22-24): agreed. Critics should accept it.
- P6: credit Day for the "generous" label only. The 3% is not a defensible description of the ancestral pipe on Day's own accepted window or his later concession.
- B internal: rescore on l.453-457. The critic view is `non-sequitur` (N2b, within HL). It is a genuine dispute with steelman-day's `rhetoric` tag, and integration should decide it explicitly. The external question (ancestral fill, counts) stays with B1c and B4a, where the critics' case is already stronger.
