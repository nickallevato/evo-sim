---
id: C2
title: "Bio-Cycle model: a generation-overlap factor d = 0.45, fitted to three aDNA loci, halves the effective generations available to selection (g_eff = d x g_nominal)"
side: day
branch: C
parent: C
edges: [{type: supports, target: C}, {type: supports, target: A4}, {type: depends-on, target: C2a}, {type: depends-on, target: C2c}]  # C2 -> C2c was typed attacks; C2c (the ratio cross-validation) supports C2 (fixed 2026-10-08)
load_bearing: true  # d = 0.45 multiplies the available generations in MITTENS 2025 (146,250 = 325,000 x 0.45), in Haldane+d (487) and in the aDNA prediction (158 of 350). MITTENS 3.0 (Z23003785) drops d, so ROOT survives without it, but the 2025 headline figures (91 fixations, 219,780-fold) do not.
sourcing: firsthand
status: reviewed
verdicts:
  internal: "non-sequitur"   # d fit not identifiable apart from s (C2d); 'd = 1 for discrete generations' fails on own formula; d*s exact for hazard-scale s (V1)
  fidelity: "unverifiable"   # Coale-Demeny tables not retrieved; Table 1 not reproduced with a Siler stand-in
  external: "contested"   # which s scale the cited papers use is unretrieved; published s are per-generation slopes (d = 1)
---

## Statement (verbatim)
> "We introduce the Bio-Cycle Fixation Model, which incorporates a generation overlap correction factor (d) into standard allele frequency dynamics."

Source: [The Bio-Cycle Fixation Model](https://zenodo.org/records/18203514), Z18203514 (v2 of concept 18202767), 2026-01-09, Abstract.

> "The effective number of generations is: g_{eff} = g_{nominal} × d"

Source: Z18203514, §2.1.

> "All three loci independently converge on d ≈ 0.45, consistent with Neolithic/Bronze Age demographic structure."

Source: Z18203514, Abstract.

> "Under base-case parameters, the three loci yield optimal d values of 0.49 (Lactase), 0.49 (SLC45A2), and 0.38 (TYR), with a mean of 0.45. When selection coefficients are reduced by 25%, the mean optimal d increases to 0.56 (range 0.51–0.59); when increased by 25%, the mean decreases to 0.36 (range 0.31–0.39)."

Source: [Bio-Cycle v1](https://zenodo.org/records/18202768), Z18202768, 2025-12-25 (superseded by v2), Results (sensitivity paragraph, line 43 of the docx text extraction).

> "The persistence allele was virtually absent in early Neolithic Europeans 6,000 years ago (less than 1 percent frequency). Today, about 75 percent of Northern Europeans carry it."

Source: Day, [Fixing Kimura](https://voxday.net/2025/12/20/fixing-kimura/), B2025-12-20-fixing-kimura, posted 2025-12-20 (the lactase example, "Test 2"; the blog's version of the Table 1 numbers is in the version-drift note below).

> "Three independent loci (LCT, SLC24A5, HERC2) yielded d = 0.45 ± 0.08^2."

Source: Z18165980 (MITTENS, 2025-12-28), Methods, ¶69 (quote Q10). The loci differ from Z18166234's "(LCT, SLC45A2, TYR)" (Q22).

## Formal statement
Per nominal generation, discrete selection recursion: p' = p + s p(1-p)/(1 + sp). The Bio-Cycle prediction after G nominal generations is p_G(d) = p after round(d x G) iterations. Inputs: parameters.yaml `selection.turnover_d` = 0.45. Table 1 inputs (Z18203514 §2.2-§3.1): LCT s = 0.05, p0 < 1% (we use 0.01), 6,000 BP; SLC45A2 s = 0.05, p0 = 0.43, 4,000 BP; TYR s = 0.03, p0 = 0.25, 5,000 BP; generation length not stated in the paper; 25 y/gen reproduces the table exactly.

derived (R2 recompute, python3 stdlib, 2026-10-07; no script committed):
- Reproduction of Table 1 (T = 25 y, G = 240 / 160 / 200): Kimura 99.92% / 99.95% / 99.19% (paper 99.9 / 99.9 / 99.3); Bio-Cycle 66.2% / 96.2% / 82.7% (paper 66.2 / 96.2 / 82.7). Holds.
- Error reduction from the paper's own numbers: LCT (24.9-8.8)/24.9 = 64.7%; SLC45A2 (2.9-0.8)/2.9 = 72.4%; TYR (23.3-6.7)/23.3 = 71.2%; mean 69.4%. The paper's "69%" holds.
- Required d at the paper's s (continuous solve): LCT 0.486, SLC45A2 0.481, TYR 0.381; mean 0.449. These match Z18202768 (0.49, 0.49, 0.38) and the blog, and do not match Z18203514 Table 4 (0.46, 0.43, 0.46). TYR 0.381 vs 0.46 is outside any rounding.
- Required s under d = 1 (Table 2 "Kimura req."): 0.0240, 0.0238, 0.0113 (paper 0.024, 0.024, 0.011; holds).
- Required s at d = 0.45: 0.054, 0.054, 0.025 versus paper 0.048, 0.050, 0.023 (paper values are about 10% lower).
- d and s enter only as the product s x d in the weak-selection regime (logit gain per generation = ln(1+s) per effective generation). Day's own sensitivity (+/-25% on s moves mean d to 0.36 / 0.56, i.e. 0.45/1.25 = 0.36 and 0.45/0.75 = 0.60) is that identity. Observed trajectories identify s x d, not d.

Version drift across Day's own texts (no verdict): blog "Fixing Kimura" 2025-12-20 gives 67.4 / 95.2 / 83.3% and reductions 69 / 38 / 69% with matching d of 0.48, 0.52, 0.38; Z18202768 (2025-12-25) gives optimal d 0.49, 0.49, 0.38, "initial prediction of d ≈ 0.40" and says d "was developed empirically before this theoretical grounding" (Z18166234); Z18203514 (2026-01-09) gives 66.2 / 96.2 / 82.7%, 65/72/71% and Table 4 d of 0.46, 0.43, 0.46; MITTENS Z18165980 names HERC2 where Bio-Cycle names TYR.

## Assumptions
- Stated: d in (0,1], "the fraction of the breeding population replaced in each nominal generation cycle"; weak selection; additive haploid-like recursion.
- Implicit: published s values (Burger 2007, Itan 2009, Mathieson 2015, Wilde 2014, Beleza 2013) were estimated under discrete-generation models and so already absorb overlap (Day concedes this in Discussion: researchers "appear to have been implicitly compensating"); selection began at the stated start date (LCT rise from 6,000 BP); the alleles are additive (lactase persistence is usually modelled dominant); no admixture (Mathieson 2015 attributes the SLC24A5 rise "mostly" to migration); fitting d to three loci with s drawn from a 0.04-0.10 literature range is not independent of s.

## Responses
- Against: Camestros CA-12 (d "would clearly have changed during human evolution"), and Nesslig20 who found d unexplained (PS post 1). The repo's own recompute above (d and s are degenerate).
- In support: Hössjer (HO-pdf) uses d = 0.45 as a "turnover rate" without testing it; Camestros CA-02 concedes the MITTENS arithmetic once d is granted.
- Weaknesses in the responses: CA-03's complaint that d is undefined is answered by Z18166234 (C2a); Hössjer's use is uncritical (he applies d to the neutral rate too, a step Day's 3.0 paper no longer makes).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Mathieson 2015 (LCT) | "The strongest signal of selection is at the SNP (rs4988235) responsible for lactase persistence in Europe" (no s value in main text) | s values unverified (fidelity ledger) |
| Mathieson 2015 (SLC24A5) | "its rapid increase in frequency to around 0.9 in Early Neolithic Europe was mostly due to migration" | misfit for use as a selection example in Z18165980 (loci list); partial |
| Kimura 1962 | discrete-generation base model (Day cites it in the Bio-Cycle reference list for the base model) | accurate as a base model; Kimura does not address overlap |
| Hill 1972 / Felsenstein 1971 | standard overlapping-generation Ne (drift) | not retrieved; used in C2a |
| Charlesworth 1994 | age-structured selection (cited, not quoted) | unverified |

## Pre-registered prediction
Written before any check runs.
- Under the claimant's model: allele-frequency change per nominal generation in an age-structured population is d x s p(1-p) with d near 0.45 (0.53 from life tables for the Neolithic) for a human-like life table; the d fitted to unrelated loci agrees within 0.1; d is a property of the demography and not of s.
- Under the opposing model (standard age-structured theory, Charlesworth/Hill-Felsenstein): the per-generation change of an allele frequency under selection is governed by the intrinsic fitness difference and the generation time, and when s is defined as the per-generation fitness difference (mean-generation-time scale) no further factor d<1 is needed; published aDNA estimates of s already carry whatever overlap correction applies. d = 0.45 cannot then be estimated separately from s. (Expectation stated from the literature Day cites; the Charlesworth 1994 text itself has not been retrieved, so this is a pre-registered hypothesis, not a sourced quote.)
- Result that would change a verdict: a life-table-explicit age-structured simulation (see C2a) in which the rate of frequency change per mean generation time T for a viability or fecundity effect s is (a) d x s p q with d < 1 (supports C2), or (b) equals s p q to within a few percent (supports the opposing model). Also: a joint fit of d across loci with s free per locus that can distinguish d from s (the trajectories alone cannot).

## Check
R4 C2 (research/checks/results/R4-H-C2.md): d*s is exact for hazard-scale s (V1, within 1.5%; Day-side point), and the factor is 1 for per-generation s (V3/V4/V5 ratios 1.000). Day's own formula gives d = -ln L for a semelparous annual (d = 1 only at L = 1/e), so "d = 1 for discrete generations" and "0 to 1" fail on his own terms. d is not identifiable apart from s, onset time, T and dominance (C2d). Table 1 d values not reproduced (Siler stand-in 0.79/0.93 vs 0.53 at e0 = 32): an open fidelity gap because the Coale-Demeny tables were not retrieved. Review: `research/checks/REVIEW.md` (review #4, 2026-10-08)
Earlier note: Script: none yet (spec: `research/checks/c2_overlap_vs_standard.py`, planned). Spec: an age-structured Wright-Fisher with explicit l(x), b(x), selection on viability (s on survival at each age) and separately on fecundity; measure Delta-p per T years where T = mean age of parents; compare with (i) d x s p q using Day's d formula (Z18166234 eq. 3.3) from the same l(x), b(x); (ii) s p q (standard). Include a Coale-Demeny-like life table with e0 = 32 and T = 27.7 (Z18166234 Table 1), and a discrete-generation control that must return d = 1. · Result: not run · Review: pending

## Simulator variables implied
d (or the life table l(x), b(x) that generates it), s per locus, generation length T, p0, number of nominal generations, dominance h, selection start time.
