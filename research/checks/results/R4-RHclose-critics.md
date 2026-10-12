# R4 RHclose-critics: the owner's RH rule applied to critic and ally statements (RH5 symmetric pass)

**Status: pre-registered (8aef421), run once, written up. Low-stakes tier: awaiting one combined review. Not integrated: no claim file, quote tag, ledger, QUEUE, RESULTS or argmap edits.** All tags below are **proposed and per reading**; the owner chooses the reading. Answers review finding RH5 of `REVIEW-R4-RHclose-combined.md`: the "remotely close" test had been applied only to Day statements (B9, C7, Q157/Q158).

## Files
- Script `research/checks/rhclose_critics.py` (pre-registered at **8aef421**; readings, criteria, predictions and verdict mapping are in its docstring; not edited after the run). Stdlib plus pyyaml, local, seconds.
- Raw output `research/checks/results/raw/rhclose_critics.out`. All seven quote checks and the continuation checks print OK (0 misses). Source hashes are in the output (transcript 96109519..., Myers 10-02 post 456fdcd9..., MITTENS 3.0 0287f54b..., Z18470617 6d115681..., hierarchy.yaml 45368513...).

## Disclosure (read first)
- **Not blind.** Before writing the script I had read the Hancock transcript passage, Myers's posts, the ROOT-PG/G2e/G2g/B5 claim files, the MITTENS 3.0 reference list, and had grepped Day's texts for most of Hancock's system names. What was pre-registered is the readings, bands, edges and mapping, not blind outcomes.
- **Three predictions missed, reported as missed:** (1) H2 count: predicted 3 of 10 classes, found **4** (the regex included "warfarin" but my earlier grep had not; Day's Z18470617 s3.4 applies MITTENS to warfarin-resistant rats). The prediction had put H2 *on* the edge (3 <= 3); the miss moves it one step over, to **rhetoric**. (2) Load-bearing Day nodes: predicted 21, hierarchy.yaml has **24**. (3) Word share of the maths paragraphs: the regex also caught paragraph 3 (12.4%, not the roughly 8% for paras 4-5 alone). None changes a tag.
- Bands: the author's 3x/one-third rules, fixed in advance (docstring "BAND RULE"). For count claims of the form "none", "remotely close" was set at <= floor(N/3). That is a judgement, and H2 shows it matters.

## The rule and the operational definition for evaluative claims
- **Owner rule (2026-10-11):** `dialectic` if the literal claim is "remotely close" when mathed out under the most charitable reading (rule C); otherwise `rhetoric`.
- **Evaluative words** ("stupid", "mystifying", "blunt fact") are not checkable and are not scored. For a statement like "debunked", the "math" was defined operationally as: **do the audit's own verdicts (hierarchy.yaml, claim files) support the literal content?** ADVERSE(node) = internal `non-sequitur`/`arithmetic-error`, or external `contradicted`, or fidelity `misread`. Share = engaged-and-adverse nodes over the units named by the reading; literal = 100%; remotely close = share >= 1/3.
- **In-scope vs extended readings.** In-scope = a reading of the words about the object the speaker names. Extended = substitutes a different object or widens the claim. The headline tag is "dialectic iff any in-scope reading passes" (most charitable); extended readings are reported with their own tags and **cannot set the headline** (answers the B9/RHclose lesson to report every reading, and the RHclose MAJOR-2 complaint about unlisted readings).

## Per-quote, per-reading table
| Quote | Reading | Test and result | Tag |
|---|---|---|---|
| **RH-15 Hancock/host, GG-34**, t=00:26:41: "The blunt fact of the matter is Vox Day's math can't do any of this." | **H1 (in-scope).** "Day's math" = the printed F_max = (t_div x d)/(g_len x G_f); "this" = allele-frequency / selection prediction | Variables needed {s, N_e, p0, mu} vs F_max {t_div, d, g_len, G_f}: overlap **0 of 4** (edge <= 1). Matches claim G2h | **dialectic** (literally true) |
| | **H2 (in-scope).** "Day's math" = any MITTENS-type computation Day has authored; "any of this" = her 10 named classes | **4 of 10** classes have a Day computation (edge <= 3): Drosophila (Z18452504: "fails by 127-fold"), peppered moth (Z18470617 s3.3), stickleback (Z18452504, Z18470617 s3.2), warfarin-resistant rats (Z18470617 s3.4). None for blowflies, crickets, mosquitoes, scrub jays, Darwin's finches (1 hit, no computation), snails (analogy only). Hand check agrees with the automatic count (all four are real applications). Margin: one over the edge; with N = 8 the edge would be 2 and it would still be rhetoric, with N = 12 it would be 4 and flip to dialectic | **rhetoric** |
| | **H3 (extended).** "can't do any of this" = cannot make any testable quantitative prediction | Day-side tested predictions exist (claim C and C7: about zero completions from below 50%; the ROOT-PG file itself says so) | rhetoric (cannot set headline) |
| | **Headline** | dialectic via H1; rhetoric via H2 and H3 | **dialectic, reading-dependent** |
| **RH-20 Myers, PZ-04** (2026-10-03, para 1): "I debunked Vox Day's stupid evolution 'disproof' in one fairly short written post." (post = 2026-10-02 "Vox Day's amazing ego...") | **M1 (in-scope).** "the disproof" = Day's whole argument | Engaged nodes {G2g, A, G1}; load-bearing Day nodes: 24; engaged and adverse: **0/24**. ROOT itself is pending/pending. Adverse load-bearing nodes are A2e, B3, B3a, C2, F1a, F3a, none engaged by the post | **rhetoric** |
| | **M2 (in-scope).** "the disproof" = the MITTENS 3.0 method the post itself names (252,000 gen, 205M, 1,075,000-fold; divide by one fixation's time) | Units {A, G1}: A `holds`, G1 `holds`: **0/2**. MITTENS 3.0 s8.1 states G_f already includes parallel fixation ("The 45.4 fixations ... were not fixed one at a time"), so the post's "sequential" description of the method is contradicted by the paper it criticises; G2e fidelity `partial` | **rhetoric** |
| | **M3 (extended: different object).** "the disproof" = the Appendix A chain in Day's 2026-10-01 blog ("fixation must be sequential", 180 vs 205M) | Unit {G2g}: `non-sequitur`, **1/1**. The post does not quote Appendix A (checked: no "Appendix A" in it). Day's own blog para 25 concedes the wording | dialectic (cannot set headline) |
| | **Headline** | rhetoric on both in-scope readings | **rhetoric** (dialectic only on M3) |
| | Descriptive | maths paragraphs are about 12% of the post's 1,686 words; "fairly short" is relative and is not scored | n/a |
| **PZ-03 Myers** (10-02 post, para 23): "7 of those citations are to the LTEE ... and 2 are to ape genome sequencing papers" (of 11) | **CX.** Count the MITTENS 3.0 reference list | **11 entries; 7 LTEE-related; 2 ape-genome.** Exact match to Myers's three numbers. Rule: LTEE-related = Lenski / long-term / E. coli / generation experiment. Strict LTEE-population papers (excluding Gerrish & Lenski 1998, an asexual-theory paper with Lenski as author) = 6, still within the band. The remaining 2 entries are Day's own | **dialectic** (and the count is right). "contradict his conclusions" is evaluative, unscored |
| **RH-18 Mansfield, MF-01**: "Genetic drift happens in every population and his claim otherwise is mystifying. Population size only affects which alleles are effectively neutral." | **F1 (in-scope).** "drift happens in every population" | Drift variance 0.25/(2N) > 0 for N = 1e3 ... 8e9; SD of drift over 280 gen at p = 0.5 is 0.18 (N 1e3), 0.059 (1e4), 0.0059 (1e6), 6.6e-5 (8e9). Neutral P_fix = 1/(2N) > 0 and substitution rate = mu at every N (so Day's Q93 "will not fixate at all" is false as stated) | **dialectic** (existence claim, exact) |
| | **F2 (in-scope).** "N only affects which alleles are effectively neutral" read as scaling | Kimura P_fix: 2N*P_fix at fixed S = 2Ns across N 1e4 ... 1e8, relative spread 5e-6 (S 0.1), 5e-5 (S 1), 5e-4 (S 10); edge 1e-3 | **dialectic** |
| | **F3 (in-scope, strictest).** literal "only": no other effect of N | Drift variance per generation and neutral fixation time both scale with N: **x100** between N 1e4 and 1e6 (edge 3x). Mansfield's own MF-02 uses 2N new mutations per generation, so N also sets supply | **rhetoric** |
| | "mystifying" | report of the speaker's state; no literal claim | rhetoric (device only; as the B5 claim file already tags) |
| | **Headline** (factual clauses) | dialectic via F1, F2 | **dialectic** (rhetoric on strict "only") |

## Proposed tags (summary)
- **RH-15 Hancock:** reading-dependent. Dialectic if "Day's math" is the printed formula (H1); **rhetoric if it is the math Day has actually applied (H2)**, which has been applied to 4 of her 10 classes. Under the registered headline rule (any in-scope reading passes) the headline is dialectic, but that rule favours the critic here and the owner should say whether it should.
- **RH-20 Myers:** **rhetoric** on both in-scope readings; dialectic only if "the disproof" is read as Day's Appendix A serial chain, which Myers's post does not quote. PZ-03 (the citation count) is dialectic and correct.
- **RH-18 Mansfield:** the factual clauses are **dialectic** (confirms the existing B5 claim-file tag); "mystifying" is rhetoric; the strict "only" overstates by about 100x on drift rate.
- **Not checkable, no reading run** (docstring gives the reason for each): RH-2 (relayed insult, rule U), RH-13 (superlative over an unbounded set), RH-14 (verdict word; content is D13), RH-16 (idiom, names no input), RH-17 (incredulity; content is GG-41/D2k, already dialectic and `supported`), RH-19 (motive self-report; content is GG-30/B5j, dialectic).

## Verdict effects (proposed; for integration after review)
| Statement | If dialectic | If rhetoric | Who the tag benefits |
|---|---|---|---|
| RH-15 Hancock (ROOT-PG, currently rhetoric by device, unscored) | Sentence scored. On H1: internal `holds`, external `supported` for the formula alone. If scored on H2: external `contested`/partly `contradicted` for the broad sentence (4 of 10 classes). ROOT-PG's own verdicts (holds / contested) do not change | No change (unscored) | **Critic on H2:** rhetoric releases her from a literal contradiction by Day's own texts. **Critic on H1:** dialectic credits her with a true statement |
| RH-20 Myers (no claim node; G2) | Only via M3: `supported`, scoped to the Appendix A chain. ROOT unchanged | No change; core stays G2e (`holds` against Appendix A only, fidelity `partial`) and A/G1 (`holds`) | **Critic:** rhetoric releases "debunked" from a 0/24 audit record |
| PZ-03 Myers | Count verified `supported`; no verdict change (claim G2e note "not independently checked" can be closed) | n/a | Critic (credit) |
| RH-18 Mansfield (B5) | B5 unchanged (holds / accurate / contested) | unchanged | none; existing tags confirmed |

- **Asymmetry, quantified and flagged.** Critic-side rhetoric statements were already "Not scored" by default, whereas Day's were scored until tagged rhetoric. So applying the rule to critics adds **no new negative** to a critic unless a statement is tagged dialectic and found false. Here, if the owner wants the scored-and-false outcome, only H2 (broad reading of Hancock) and M1 (Myers, "debunked" = ROOT falls) would produce one, and both are tagged rhetoric, so neither is scored. The release works the same direction as for Day's C7 and B (rhetoric removes the negative), so the rule is symmetric in effect; it is not symmetric in default.
- Net: no verdict changes anywhere if the owner accepts the headline tags except that PZ-03 is closed as verified.

## Who this helps
- **Day side.**
  - Hancock's sentence is false on the broad reading. Day applied MITTENS, with measured selection coefficients, to peppered moths (s = 0.20, N_e 50,000, G_f 115, "0.66 achievable fixations", "It predicts trajectories"), sticklebacks, warfarin rats, beach mice and Drosophila. Z18470617 (concluding passage, l.139) says "All four passed".
  - Myers's post misdescribes the method as sequential when MITTENS 3.0 s8.1 puts parallel fixation inside G_f. His "debunked" is 0/24 on the audit's load-bearing Day nodes, and the post's maths is about 12% of its text.
  - Mansfield's "only" is an overstatement by two orders of magnitude on drift rate. His "happens in every population" is an existence claim and says nothing about size (hand arithmetic, not in the script: F_drift over 280 generations is about 140/N, so at N >= 1.4e6 it falls inside the 1e-4 "not at all" band the Day-side check C7 used. The existence reading is more generous to Mansfield than the practical band was to Day).
- **Critic side.**
  - H1 is exactly true: F_max has no s, N_e, p0 or mu term, which is the content behind "can't do any of this".
  - The Day computations in H2 are plug-in retrodictions with chosen s and N_e (and G_f = (2/s) ln(2N_e) is the textbook sweep-time approximation): the logistic gives p(80 gen) = 0.989 and 72 generations to 95% from the same inputs, which is the standard model's output. They are not out-of-sample predictions of the kind in her paper list.
  - Myers's serial-reading point is right about Day's own Appendix A text (G2g `non-sequitur`; Day concedes the wording at para 25). His citation count (11 / 7 / 2) is exact.
  - Mansfield's two factual clauses both check: drift is positive at every N, and N enters fixation probability through 2Ns (spread <= 5e-4). Day's Q93 "will not fixate at all" is false at every N (P_fix = 1/2N; rate = mu).
- **Both.** Each tag turns on one choice: Hancock on what "Day's math" is (formula vs applied); Myers on what "the disproof" is (MITTENS 3.0 vs Appendix A); Mansfield on whether "only" is read as scaling or as literally exclusive. The tags do not depend on tone.

## Caveats
- The 3x band and the one-third count rule are the author's judgement. H2 is within one class of the edge; the owner could reasonably move it.
- H2's "Day computation" is a text window rule plus hand check; whether Day's retrodictions count as "predictions" is the critic's best objection and is not scored by the rule.
- M1/M2 count the audit's own verdicts, which are a record of what was checked, not of what is true. Unchecked nodes are not adverse. An absence of adverse verdicts for critic-engaged nodes is not proof the critic is wrong; ROOT is pending.
- Single run, no replication needed (deterministic arithmetic and text parsing). Same-agent-family author and, unless the review is independent, reviewer.
- Quote glyphs: the Myers quotes match with their curly quotes as stored in `quotes-critics.md`; no MISS.

## For the owner
1. **RH-15 Hancock: which object is "Day's math"?** The formula (dialectic, true) or what Day has applied (rhetoric; 4 of 10 classes covered)? Should the headline be "any in-scope reading passes" (dialectic) or the stricter "applied math" (rhetoric)?
2. **RH-20 Myers: is "the disproof" MITTENS 3.0 (rhetoric) or the Appendix A chain (dialectic, narrow)?** The post names the former.
3. **The H2 edge** (count <= N/3). Is a count of 4 of 10 "remotely close" to none?
4. **RH-18:** confirm that "Population size only..." is read as the scaling statement (dialectic) and "mystifying" stays rhetoric.
5. Whether to close the "not independently checked" note on PZ-03 with the exact count at integration.
