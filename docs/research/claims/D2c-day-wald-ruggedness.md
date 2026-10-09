---
id: D2c
title: "Wald: one is 'hard put to find' a hemoglobin amino-acid change that does not markedly change properties; this supports a rugged landscape"
side: day
branch: D
parent: D2
edges: [{type: supports, target: D},{type: attacks, target: D1}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: pending      # the inference from hemoglobin variants to landscape ruggedness is not worked out
  fidelity: accurate      # Day's quotation matches Wald p.19 (two sentences combined)
  external: contested   # ascertainment bias and counter-examples (Lewontin, Wistar pp.76-79); modern DMS not in corpus; R4 D1: hemoglobin not tested; modern DMS gives 53% of singles below 80% of the WT-like level but 71% keeping at least half, compatible with Wald's 'markedly change the properties' and with retained function
---

## Statement (verbatim)
> "Wald stated that he was “hard put to find a single instance” where a single amino acid change in hemoglobin did not “change markedly the properties.”"

> "This is relevant to Eden’s argument about the ruggedness of the fitness landscape—if nearly every single-residue change has significant functional consequences, then the space is rugged, not smooth, and local search is unreliable."

Source: [The Best They've Got I](https://voxday.net/2026/10/05/the-best-theyve-got-i/), 2026-10-05, voxday.net, paras 22 and the following paragraph.

Primary text (Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (OCR garbles noted in place)):

> "One is hard put to find a single instance in which a change in one amino acid in sequence does not change markedly the properties. The restrictions are enormous."
— George Wald, p.19 (in discussion of Eden's paper; the surrounding passage says 'I want to add a further note which has a large bearing, I think, on Eden's discussion').

## Formal statement
Observation O: among known hemoglobin variants, a single amino-acid substitution that leaves function largely unchanged is rare (Wald's sample). Day's inference: O => the landscape is rugged (most single steps off a functional protein are not functional), so local search is unreliable. In parameter form: p_neutral-or-better(single substitution) is small. Wald's statement carries no number.

## Assumptions
- Stated: hemoglobin changes 'change markedly the properties'.
- Implicit: (i) the hemoglobin variants Wald considers are an unbiased sample of single substitutions (they are the ones that appear in clinical practice, i.e. detected because they have effects); (ii) 'change markedly the properties' = loss of function rather than modified function; (iii) hemoglobin is typical.

## Responses
- Against: ascertainment (clinically detected variants over-represent functional effects); Wald himself says (p.16) he does not know of any hemoglobin with a long run of shifts, i.e. he is supporting the point that long substitution runs are not seen, not that single steps are lethal; Lewontin (p.76) offers enzymes with changed but retained function; Mayr (p.16): 'Because it doesn't survive' (reply on long runs).
- In support: Wald's point is made by a biologist at the symposium, on factual grounds.
- Weaknesses: both directions rest on anecdote at Wistar. The quantitative modern evidence (DMS: fraction of single mutants tolerated, typically a substantial share for most positions) is not in the corpus and Day cites none (D2h); the claim 'single-residue changes to most proteins tend to reduce or destroy function' is, as written, a statement about proteins in general.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.19 (Wald) | 'One is hard put to find such an instance ... a single instance in which a change in one amino acid in sequence does not change markedly the properties.' | accurate quotation |
| Wistar p.16 (Wald) | 'I don't know of any instance in which one has yet discovered a hemoglobin with a long run of shifts.' | context: long runs |

## Pre-registered prediction
Written before any check. Under Day's inference: in a DMS dataset, the median fraction of tolerated single substitutions per position is low (< ~20%) for most globular proteins. Under the opposing inference: it is high (> ~40%) with most positions tolerating many substitutions, and most deleterious effects are mild. Result that would change a verdict: harvested DMS distributions (e.g. median tolerated fraction) from the literature.

## Check
R4 D1 (research/checks/results/R4-D1-spike.md, review #11, 2026-10-09): hemoglobin itself is not tested. Across 114 DMS sets, 53% of single substitutions fall below 80% of the WT-like level but 71% keep at least half.

No script (data not in corpus). Action: harvest DMS datasets (e.g. ProteinGym-style summaries).

## Simulator variables implied
Distribution of single-substitution fitness effects; fraction tolerated per position; epistasis between substitutions.
