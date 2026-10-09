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
  internal: non-sequitur   # N2a in the same comment: 'within centuries' conflicts with his '~one million years apiece' per neutral fixation. (R4 X1 rule rev 2: the earlier Q105 basis is dropped, since premise 1 makes harmful mutations effectively neutral)
  fidelity: unverifiable   # R4 X1 rule rev 2 (was n/a): rule F (uncited/unretrievable input) or S/U; see R4-X1-rescore.md
  external: pending   # the fixation of slightly deleterious mutations (|N_e s| ~ 1) is the open GAP-05 question
---

## Statement (verbatim)
> "So if genetic drift were capable of producing actual changes to the genome, the human species would have been rendered infertile and gone extinct within centuries."

Source: [Vox Day, comment on McCarthy, "Why Probability Zero is Wrong About Evolution"](https://dennismccarthy.substack.com/p/why-probability-zero-is-wrong-about-0d1/comment/337302874), 2026-09-15, comment id 337302874, last paragraph (Q104). Premises in the same comment: "1. For neutral substitution to work to fixation at its maximum speed, natural selection cannot be operating." "2. There are 3x more harmful substitutions than neutral substitutions."

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
Not run. A check would compute expected harmful fixations over 252,000 generations for a DFE with a nearly neutral share, at N_e = 1e4 (GAP-05).

## Check
None. Internal verdict from Day's own premises in the same comment. From the 2026-10-09 corpus refresh (D-5b).

R4 X1 (research/checks/results/R4-X1-rescore.md; rule research/checks/results/R4-X1-verdict-rule.md rev 2; review #12, 2026-10-09): under the single both-sides rule this node is non-sequitur / unverifiable. N2a in the same comment: 'extinct within centuries' vs 'about one million years apiece' per neutral fixation. The Q105 basis is dropped (premise 1 makes harmful mutations effectively neutral). F: '3x excess harmful mutations' uncited Charitable reading tried: attempted: no ambiguous referent.

## Simulator variables implied
Deleterious DFE including the nearly neutral class; N_e.
