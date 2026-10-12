---
id: B9
title: "Day: if drift could change the genome, the 3x excess of harmful mutations would have made humans 'infertile and gone extinct within centuries'"
side: day
branch: B
parent: B
edges: [{type: supports, target: B}, {type: depends-on, target: H10}]
load_bearing: false  # comment-level argument; not in the papers
sourcing: firsthand
status: extracted
verdicts:
  internal: non-sequitur   # OWNER DECISION PENDING (R4 B9, 2026-10-11): (a) holds, conditional on reading A (mutation load), with N2a under reading B recorded (auditor recommends) or (b) keep non-sequitur, reading A a ledger rescue. Until decided: non-sequitur. N2a in the same comment: 'within centuries' conflicts with his '~one million years apiece' per neutral fixation. (R4 X1 rule rev 2: the earlier Q105 basis is dropped, since premise 1 makes harmful mutations effectively neutral)
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: contradicted   # R4 B9, scoped: premises 1 and 2 as worded are false (premise 2 also against R4-L1 dN/dS ~0.21-0.27); the conditional's arithmetic is supported on reading A (Lynch 2016). The fixation of slightly deleterious mutations (|N_e s| ~ 1) is the open GAP-05 question
---

## Statement (verbatim)
> "So if genetic drift were capable of producing actual changes to the genome, the human species would have been rendered infertile and gone extinct within centuries."

Source: [Vox Day, comment on McCarthy, "Why Probability Zero is Wrong About Evolution"](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337302874), 2026-09-15, comment id 337302874, last paragraph (Q104). Premises in the same comment: "1. For neutral substitution to work to fixation at its maximum speed, natural selection cannot be operating." "2. There are 3x more harmful substitutions than neutral substitutions."


RH tag: **dialectic** (owner rule, 2026-10-11: graded by whether the literal claim is remotely close when mathed out under the most charitable reading; R4 B9). Replaces the 2026-10-10 UNCLEAR note (reading A literal reductio vs reading B hyperbole).

## Formal statement
Premise A: drift fixes neutral mutations only if selection is not operating. Premise B: harmful mutations outnumber neutral 3:1. Conclusion: drift would fix harmful mutations, causing extinction within centuries. Standard theory: fixation probability of a new mutation with selection coefficient s < 0 is u(s) = (1 - e^(-2s)) / (1 - e^(-4N_e s)) (Kimura 1962, N = N_e, initial frequency 1/(2N)), which for s < 0 and N_e|s| >> 1 is about 2|s| e^(-4N_e|s|), far below 1/(2N). `derived:` (python3 -I) N_e = 1e4, s = -0.001: 4N_e s = -40, u = 8.5e-21 against 1/(2N) = 5e-5. Only the nearly neutral class (|N_e s| < ~1) fixes at near-neutral rates (Ohta).

## Assumptions
- Stated: the two premises above; "1/2Nₑ is the fixation probability for a neutral mutation" (Q105).
- Implicit: premise A treats "selection operating" as all-or-nothing across mutation classes, so that drift on neutral sites implies no selection against harmful ones.

## Responses
- Against: none located directly; McCarthy's reply in the thread addresses the Darwillion part of the same comment.
- In support (for Day): the nearly neutral class does accumulate by drift at small N_e; GAP-05 (how many slightly harmful fixations a drift account implies) is unaddressed by both sides.
- Weaknesses in the responses: no critic has quantified the slightly deleterious class against the observed divergence.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | u(s) for selected alleles | B7a |

## Pre-registered prediction
R4 B9 (e95f0d3, `research/checks/b9_relaxed_load.py`): central range of years to half or a tenth of fitness under relaxed selection (Lynch's 0.5%, 1%, 5% per generation) touches 100-999 y => dialectic; Day's premise 2 rows within 10-999 y; literal fixation reading >= 1,000x "centuries". All held (exploratory numbers known in advance; not blind). The GAP-05 computation (expected harmful fixations over 252,000 generations for a DFE with a nearly neutral share, N_e = 1e4) is still not run.

## Check
None. Internal verdict from Day's own premises in the same comment. From the 2026-10-09 corpus refresh (D-5b).

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is non-sequitur / unverifiable. N2a in the same comment: 'extinct within centuries' vs 'about one million years apiece' per neutral fixation. The Q105 basis is dropped (premise 1 makes harmful mutations effectively neutral). F: '3x excess harmful mutations' uncited Charitable reading tried: attempted: no ambiguous referent.

## Simulator variables implied
Deleterious DFE including the nearly neutral class; N_e.

R4 B9 (research/checks/results/R4-B9.md; combined review #61, 2026-10-11; fix pass e51ab10, post hoc c20c210): under the owner's RH rule Q104 is `dialectic`. Reading A (selection fully relaxed, new deleterious mutations accumulate, Lynch 2016): fitness halves in 338 / 1,724 / 3,457 y and falls to a tenth in 1,122 / 5,728 / 11,484 y at d = 5% / 1% / 0.5% per generation (W = 0.01: 2,245-22,968 y); Day's premise 2 (3:1, s assumed 0.1-1%) gives 12-970 y. So "within centuries" is right on Lynch's upper value and Day's premise 2 and is millennia on Lynch's central and mouse values; the tag survives a 3x band. Reading B (harmful substitutions fix like neutral ones, 4Ne generations) gives 1.0-1.6 million y, 1,000-1,600x "centuries". **Internal: owner decision pending** between (a) `holds`, conditional on reading A, with the N2a non-sequitur under reading B (Day's own "~one million years apiece" in the same comment) recorded (the auditor recommends this), and (b) keep `non-sequitur` with reading A recorded in `ledgers/slips.md` as a possible rescue; stays `non-sequitur` until decided. **External `contradicted`, scoped:** premise 1 is false under standard theory (selection and drift act concurrently; k = mu at neutral loci) and premise 2 as worded ("harmful *substitutions*") is false against R4-L1's dN/dS ~0.21-0.27; the conditional's arithmetic is supported on reading A. Fidelity unverifiable (premise 2 uncited). Credit to Day: the underlying worry, deterioration under relaxed selection, is mainstream (Lynch 2016), and GAP-05 (slightly deleterious fixations, |N_e s| ~ 1) stays open as his best point. Caveat: relative fitness W is not fertility; the model is multiplicative, and Lynch's 1% and 5% are recurrent loads, not measured relaxed-selection rates.
