---
id: B7b
title: "Kimura & Ohta 1969: neutral fixation takes about 4Ne generations; the fraction 1/2N fix"
side: literature
branch: B
parent: B7
edges: [{type: supports, target: B7}, {type: supports, target: B1a}]
load_bearing: false  # source of the 4Nₑ transit time used throughout B1/B2; also of the 1/2N fraction
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a
  fidelity: accurate
  external: n/a
---

## Statement (verbatim)
> a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne.

Source: [Kimura & Ohta 1969, The average number of generations until fixation of a mutant gene in a finite population, Genetics 61:763-771 (user-downloaded PDF, sha256 80694ab2...299fc5)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1212239/), 1969-03, Summary, p.770 (also Eq. 15, p.766). OCR text layer of a scanned PDF: mathematical symbols and some spacing are repaired in this quote (fragments checked verbatim against the raw extraction; full sentence as in quotes-literature.md)

> the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation) taking a very large number of generations.

Source: [Kimura & Ohta 1969, The average number of generations until fixation of a mutant gene in a finite population, Genetics 61:763-771 (user-downloaded PDF, sha256 80694ab2...299fc5)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1212239/), 1969-03, p.769. OCR text layer of a scanned PDF: mathematical symbols and some spacing are repaired in this quote (fragments checked verbatim against the raw extraction; full sentence as in quotes-literature.md)

> Since the ratio Ne/N is around 0.8 in man (CROW 1954), a single mutant gene which appeared in a human population will be lost from the population on the average in about 1.6 log_e 2N generations.

Source: [Kimura & Ohta 1969, The average number of generations until fixation of a mutant gene in a finite population, Genetics 61:763-771 (user-downloaded PDF, sha256 80694ab2...299fc5)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1212239/), 1969-03, p.769. OCR text layer of a scanned PDF: mathematical symbols and some spacing are repaired in this quote (fragments checked verbatim against the raw extraction; full sentence as in quotes-literature.md)

## Formal statement
t̄(0) = 4Nₑ (Eq. 15), conditional on fixation, for the variance effective number Nₑ; first moment only. The paper keeps N and Nₑ distinct (for man it takes Nₑ/N ≈ 0.8), uses Nₑ for the time and N for the fraction that fix (1/2N). Not in this paper (ledger): SD ≈ 2.15Nₑ (our B0.2 simulation: ≈2.1N); any statement about recombination (the word occurs 0 times).

## Assumptions
- Stated: Single locus, variance effective size.
- Implicit: Single locus; no linkage.

## Responses
- Against: Day cites it also for the statement that fixation time does not depend on recombination (misattribution; the word does not occur in the paper, ledger).
- In support: RESULTS B0.2: conditional mean t_fix/N = 3.908 (N=50), 4.006 (N=200) vs diffusion 3.980/3.995.
- Weaknesses in the responses: n/a

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura & Ohta 1969 | see Statement | accurate for 4Nₑ; accurate (critics) for 1/2N fraction; not found: SD; misattribution: recombination |

## Pre-registered prediction
Written **before** the check runs.
- Under the claimant's model: t̄ = 4Nₑ for neutral alleles that fix.
- Under the opposing model: n/a
- Result that would change a verdict: n/a

## Check
Script: `research/checks/baseline_textbook.py` B0.2 · Result: conditional mean t_fix/N 3.908 (N=50), 4.006 (N=200); SD ≈ 2.105–2.108 N. Review #2 corrected the target to the diffusion value at p = 1/(2N). Review: `research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`

## Simulator variables implied
- Nₑ
- 4Nₑ transit display
