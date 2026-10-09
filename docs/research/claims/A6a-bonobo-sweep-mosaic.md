---
id: A6a
title: "Bonobos: if 326,000 loci fixed by selection in 930,000 years, the genome would be a mosaic of overlapping sweep signatures; it is not"
side: day
branch: A
parent: A6  # earlier dated version (2026-01-31) of the sweep-signature argument that A6 (2026-02-02) restates for humans; same all-fixations model (branch A)
edges: [{type: supports, target: A6}]
load_bearing: false  # a subspecies-level application; ROOT does not depend on it
sourcing: firsthand
status: checked
verdicts:
  internal: holds   # R4 GAP-02: the detection window (~20,000 generations at Day's N_e ~ 20,000) covers 43-50% of the 46,500 nominal / 40,000 effective generations, so 326,000 selective sweeps would leave ~1.4-1.6 x 10^5 detectable at power 1 (still 1.6 x 10^4 with a window 10x smaller)
  fidelity: n/a   # no source is cited for the absence of the mosaic
  external: supported   # as against 326,000 *selective* fixations: Yoo 2025 SweepFinder2 finds 30 bonobo candidates; consistent with the neutral reading; the logical work is also done by Day's own 'First' argument (G_f already selection-driven)
---

## Statement (verbatim)
> Third, selection leaves signatures—selective sweeps reduce diversity around the selected site, create characteristic haplotype patterns, and skew the site frequency spectrum. If 326,000 loci fixed by selection in bonobos over 930,000 years, the entire genome should be a mosaic of overlapping sweep signatures.

Source: [The Pan Paradox: MITTENS Applied to Chimpanzee Subspecies Divergence](https://zenodo.org/records/18441321), Z18441321, 2026-01-31, §3.1 ("Third"), raw `sources/raw/day/zenodo-18441321.txt` l.119.

> The observed patterns do not support this. Chimpanzee genomes show typical neutral diversity patterns, not the reduced diversity expected from hundreds of thousands of recent sweeps.

Source: same, l.119.

## Formal statement
Required fixations (bonobo lineage) = 326,000 (10% of 3,263,686 private alleles, l.71); generations = 930,000 / 20 = 46,500 nominal, 40,000 effective with d = 0.86 (l.69). Prediction: if those fixations were selective sweeps, sweep signatures would cover the genome.

`derived:` (R4 GAP-02) detection window W ≈ 0.25 × 4N_e = 20,000 generations at Day's N_e ≈ 20,000 (§3.2, l.123; same N_e scaling as Hernandez 2011's 10,000 at N_e = 10⁴, which is not separately sourced); expected detectable at power 1 = 326,000 × 20,000 / 46,500 ≈ 1.4 × 10⁵ (1.6 × 10⁵ at 40,000 effective generations).

## Assumptions
- Stated: the 326,000 are fixations "by selection"; signatures are diversity reduction, haplotype patterns and SFS skew.
- Implicit: the 10% of private alleles taken as fixed differences are real fixed differences; the alternative (most fixed neutrally) is answered separately in §3.2 (neutral fixation takes 4N_e).

## Responses
- Against: none located.
- In support: Yoo et al. 2025 SI Note VII: SweepFinder2 detected 30 sweep regions in bonobos (power-limited: q-value regions, n = 13).
- Weaknesses in the responses: not engaged. Note: no critic asserts that 326,000 bonobo fixations were selective; the passage refutes a position the critics do not hold, and is consistent with their neutral reading.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| (none cited for the signature claim) | – | n/a |

## Pre-registered prediction
R4 GAP-02 (`research/checks/gap02_sweep_window.py`, committed b812741). P5: the window does not rescue 326,000 selective sweeps (E ≥ 10⁵ at power 1 vs Yoo's 30). Arithmetic consequence of the model, not a test.

## Check
R4 GAP-02 (research/checks/results/R4-GAPS-04-07-02.md): window 43% (nominal) to 50% (effective generations) of the span; E ≈ 1.4–1.6 × 10⁵ at power 1, still 1.6 × 10⁴ with a 10× smaller window, against 30 SweepFinder2 candidates in bonobos (Yoo 2025). The margin exceeds any plausible power or window error. Review: `research/checks/REVIEW.md` (review #6, 2026-10-08).

## Simulator variables implied
Sweep count, detection window vs split time, detection power, N_e of Pan.
