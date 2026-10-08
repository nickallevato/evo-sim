---
id: B7a
title: "Kimura 1962: U = 1/2N for a neutral gene; approximately 2s for an advantageous one"
side: literature
branch: B
parent: B7
edges: [{type: supports, target: B7}, {type: attacks, target: B3a}]
load_bearing: false  # primary-literature anchor for B7 and for F4 (2s)
sourcing: firsthand
status: reviewed
verdicts:
  internal: n/a
  fidelity: partial
  external: n/a
---

## Statement (verbatim)
> The probability of fixation of an individual mutant gene is obtained from (8) by putting p = 1/(2N).

Source: [Kimura 1962, On the probability of fixation of mutant genes in a population, Genetics 47:713-719 (user-downloaded PDF, sha256 24baddd6...f85e1)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1210364/), 1962-06, p.715, Eq. 10

> if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene.

Source: [Kimura 1962, On the probability of fixation of mutant genes in a population, Genetics 47:713-719 (user-downloaded PDF, sha256 24baddd6...f85e1)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1210364/), 1962-06, p.716. OCR text layer of a scanned PDF: mathematical symbols and some spacing are repaired in this quote (fragments checked verbatim against the raw extraction; full sentence as in quotes-literature.md)

> where N is the number of reproducing individuals in the population.

Source: [Kimura 1962, On the probability of fixation of mutant genes in a population, Genetics 47:713-719 (user-downloaded PDF, sha256 24baddd6...f85e1)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1210364/), 1962-06, p.714, Eq. 6

> the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient

Source: [Kimura 1962, On the probability of fixation of mutant genes in a population, Genetics 47:713-719 (user-downloaded PDF, sha256 24baddd6...f85e1)](https://pmc.ncbi.nlm.nih.gov/articles/PMC1210364/), 1962-06, p.716 (HALDANE 1927)

## Formal statement
Kimura 1962, genic selection: u(p) = (1 − e^{−4Nsp})/(1 − e^{−4Ns}) (Eq. 8); at p = 1/(2N): U = (1 − e^{−2s})/(1 − e^{−4Ns}) (Eq. 10); for small |s|: U = 2s/(1 − e^{−4Ns}) (Eq. 11); U → 1/2N as s → 0; U ≈ 2s for large positive Ns (equations reconstructed from the OCR text layer, which shows only fragments).
**Fidelity note (new, from reading the paper):** the 1962 model has a single N, the number of reproducing individuals, which enters both the variance V = x(1−x)/(2N) (Eq. 7) and the starting frequency p = 1/(2N). The paper therefore does not itself distinguish census from variance-effective size; its introduction recalls that Kimura (1957) expressed U in terms of the initial frequency p, the selection coefficients and the effective population number. The fidelity ledger's gloss that N is the census number is therefore stronger than the paper. The critics' reading (B7) rests on P_fix = initial frequency (a martingale property, independent of this paper) and on Day's own 1/(2N) statements (B7); this paper supports 1/2N rather than 1/2Nₑ only in the sense that the formula is written with the starting-frequency N and the model has no separate Nₑ.

## Assumptions
- Stated: Random mating, genic selection, diffusion approximation; N reproducing individuals.
- Implicit: N = variance size = counting size (ideal population).

## Responses
- Against: Day: Kimura 1962 is cited by Day for ≈ 2s (accurate, ledger) and for "1/(2Nₑ)" (misread, ledger).
- In support: Ledger: verified-accurate for ≈2s; verified-misread for 1/(2Nₑ).
- Weaknesses in the responses: The ledger's census gloss; see the fidelity note.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Kimura 1962 | see Statement | accurate for 1/2N and ≈2s; partial for the census/Nₑ distinction |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: U = 1/2N (neutral).
- Under the opposing model: U = 1/2Nₑ (Day, pre-retraction).
- Result that would change a verdict: n/a (primary text).

## Check
Script: none. Quotes are from the user-downloaded PDF via pdftotext (spacing in the extraction is corrupted, e.g. "byputtingp"; quotes are spacing-normalised).

## Simulator variables implied
- —
