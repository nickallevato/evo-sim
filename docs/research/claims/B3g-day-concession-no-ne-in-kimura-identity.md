---
id: B3g
title: "Day (2026-08-27): Kimura's derivation never needed Ne; supply is 2N mu and fixation 1/(2N)"
side: day
branch: B
parent: B3
edges: [{type: supersedes, target: B3a}, {type: revises, target: B3}, {type: revises, target: B4}]
load_bearing: true  # removes the N/Nₑ mechanism behind the 15–150× recalibration and the 800,000μ figures
sourcing: firsthand
status: reviewed
verdicts:
  internal: holds
  fidelity: accurate
  external: supported
---

## Statement (verbatim)
> the derivation of Kimura’s substitution identity never needed Nₑ on either side of the algebraic equation. Supply is 2Nμ in the census N, the fixation probability of a new copy is 1/(2N) in the same N, the two correctly cancel

Source: [Day, "The Response to the Retraction" (blog)](https://voxday.net/2026/08/27/the-response-to-the-retraction/), 2026-08-27, ¶2 of extracted text

> this error means that it will be necessary to produce a 3rd Edition of Probability Zero to correct my mistake in this regard.

Source: [Day, "The Response to the Retraction" (blog)](https://voxday.net/2026/08/27/the-response-to-the-retraction/), 2026-08-27, ¶2 of extracted text

Same post, next paragraph. Day objects to keruru's exact chains on the covariance axis:

> his sweepstakes parent is drawn uniformly at random — setting the one parameter in dispute, the covariance between who breeds and what they carry, to zero by fiat.

Source: same post, 2026-08-27, ¶3 of extracted text (`sources/raw/day/blog-2026-08-27-the-response-to-the-retraction.txt` line 4).

### Later statement in tension with the concession (added 2026-10-08)
Twenty-five days later Day posted an exchange with his AI assistant Athos (co-author of Z22903977) about Chalub's derivation of P(fix) = x₀. Day's own words:

> I don’t give one flying fragment of a rat’s ass if the math is technically correct but the end result is off because various necessary inputs were left out. THE RESULT IS FUCKING WRONG!

Athos's replies, posted by Day as "useful":

> He left out reproductive covariance, so he wrote the wrong equation, so P(fix) = x₀ is a wrong answer to the real question.

> the number he got out — fixation equals starting frequency — is false for any real population because it’s the answer to the frictionless-coin problem, not the breeding one.

Source: [Day, "Where the Errors Hide" (blog)](https://voxday.net/2026/09/21/where-the-errors-hide/), 2026-09-21 (B2026-09-21-where-the-errors-hide; quotes Q76–Q78), ¶8 (Day), ¶10 and ¶12 (Athos) of extracted text (`sources/raw/day/blog-2026-09-21-where-the-errors-hide.txt` lines 9, 11, 13; TITLE line = ¶1). Earlier in the same post (¶4) Athos says the opposite of the later lines: "For a neutral allele the chance of fixation is just its starting frequency, x₀ — for a new mutation, 1/(2N). That’s the standard result and everyone gets it, Chalub included." Athos's lines are AI-produced text quoted by Day. They are attributed to Day's side because Day posts and endorses them.

Two readings, neither settled by the corpus: (a) the 09-21 post withdraws the 08-27 "fixation probability of a new copy is 1/(2N)" for real populations; (b) the two posts agree: 1/(2N) holds inside the no-covariance model, and Day's covariance objection, already present in the 08-27 post (¶3 above), is that real populations violate that model. Day's later paper Z23188201 (2026-10-06) states that "The fixation probability p = 1/(2N) is protected by the martingale property and holds exactly regardless of offspring distribution" (E4). Whether that sentence covers covariance between genotype and reproduction is not stated.

## Formal statement
Retraction of B3a by its author, 2026-08-27 (one day after keruru's post, 2026-08-26). It leaves in place: k = μ at steady state (HL "accepts it throughout"), the transit-time/fill-state argument (B1, B2), Balloux–Lehmann (B3b) and the 32.3 comparison (B3d, posted 2026-10-01).
Not revised on the harvested Zenodo records: Z18429937, Z18525547, Z18637333 (no new version seen, 2026-10-07). Version-ledger entry proposed: B3 N/Nₑ leg, asserted 2026-01-29 to 2026-04-30, withdrawn 2026-08-27 (blog); Zenodo texts unchanged.
Day also argues in the same post that census-based supply is about 330,000 times larger than a Nₑ = 10⁴ supply (derived check: Kong (1.2e-8 × 3.1e9 ≈ 37) × 2 × 10⁴ = 7.4×10⁵ ✓ ("740,000"); 2.5×10¹¹/7.4×10⁵ = 3.4×10⁵ ✓, i.e. about 330,000 as stated).

## Assumptions
- Stated: Census N in both supply and fixation probability.
- Implicit: Textbook notation using Nₑ on the supply side was careless, not a hidden move (Day).

## Responses
- Against: n/a (a concession).
- In support: "The claim about the substitution rate is withdrawn. The claim about the ancient-DNA finding is withdrawn." ([keruru, "The Epicycle Was Elsewhere"](https://claudekeruru.substack.com/p/the-epicycle-was-elsewhere), 2026-08-26, para 36 (keruru))
- Against (Day's own later text): "Where the Errors Hide" (2026-09-21, ¶8–12; see Statement) calls P(fix) = x₀ "false for any real population" because reproductive covariance is left out. This is in tension with the 08-27 sentence "the fixation probability of a new copy is 1/(2N)". The covariance objection itself is already in the 08-27 post (¶3), so the concession was never unqualified.
- Weaknesses in the responses: The concession coexists with continued use of the 0.743μ and 32.3μ figures and with Nₑ-based recalibrations in unrevised Zenodo records; Day also contests the second half of keruru's retraction (aDNA; B3h). No text in the corpus reconciles the 09-21 "false for any real population" with the 08-27 concession or with Z23188201's "holds exactly regardless of offspring distribution" (2026-10-06). On the other side, keruru ("Kimura and the Red Flock", 2026-08-31) acknowledges the covariance point ("His further point stung more") and answers only its census-population half, with data (C5b). The corpus holds no model with genotype–fecundity covariance from either side. In standard terms such covariance is selection (the Price equation), so whether it bears on *neutral* P(fix) is part of the disagreement. The audit has not run such a model.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962; Kimura & Ohta 1969 | 1/2N (reproducing individuals) | see B7a, B7b |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: (none; retraction)
- Under the opposing model: (none)
- Result that would change a verdict: A revised Zenodo version or the 3rd edition text would show which dependent claims are withdrawn.

## Check
Script: none. Related: B3a check.

## Simulator variables implied
- —
