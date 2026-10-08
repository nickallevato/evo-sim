---
id: D3a
title: "The 10^52 is a count of protein molecules that could ever have existed, not of functional proteins; Day restates Eden's inputs differently"
side: literature
branch: D
parent: D3
edges: [{type: depends-on, target: D3},{type: attacks, target: D}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # the order of the count does not matter to the 273-order comparison
  fidelity: partial      # Eden: "protein molecules ... ever existed"; Day (Best I): "functional proteins that have ever existed"; Day ch.6 restates the inputs (cell density 10^18 per cm^3, concentration 10^-4) differently from Eden (30%, density 1)
  external: contested      # 
---

## Statement (verbatim)
> "Assume a biosphere of cells 1 cm. thick over the surface of the earth, a protein concentration in these cells of 30%, a density of 1, an age for life on earth of 10 billion years and an average lifetime of a protein molecule of 1 second. Of course all these quantities except density err very heavily toward the high side."

Source: Eden, 'Inadequacies of Neo-Darwinian Evolution as a Scientific Theory', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.7.

> "Yet this relatively small set of 1052 proteins contains within it all the useful proteins which have existed to date."

Source: same, p.7 (the sentence that licenses reading the 10^52 as covering 'all the useful proteins which have existed').

> "Assume a biosphere one centimeter thick covering the entire Earth, filled with cells at a density of a billion billion per cubic centimeter, each containing proteins at a concentration of one ten-thousandth, with each protein molecule lasting an average of one second, over a total span of ten billion years. This yields approximately one followed by fifty-two zeros—ten thousand trillion trillion trillion trillion—protein molecules that could ever have existed."

Source: [Vox Day Interview on Evolutionary Theory](https://billdembski.substack.com/p/vox-day-interview-on-evolutionary) (Dembski Substack), 2026-09-28, appended chapter 'From Probability Zero (2nd ed.) on 1966 Wistar Symposium, Chapter 6: The 1966 Meeting of the Minds' (primary Day text, posted with Day's permission). Day's Best They've Got I (2026-10-05) says: 'the number of functional proteins that have ever existed is ~10^52' (see D).

## Formal statement
Count: N_ever = (protein mass of biosphere / molecular mass) * (age / lifetime). Biosphere volume V = 4*pi*R^2 * 1 cm = 5.10e18 cm^3 (R = 6.371e8 cm); protein mass m = V * density(1 g/cm^3) * c; molecules alive = m*N_A/M; ever = alive * (1e10 yr = 3.156e17 s) / (1 s). With M = 27.5 kDa (250 residues x 110 Da):
- Eden p.7 inputs (c = 0.30): m = 1.53e18 g; alive 3.35e37; ever **1.06e55** (log10 55.02). Matches Eden's working paper ('less than 10^55', p.110) and is 3 orders above the 10^52 he prints in the talk.
- Day ch.6 inputs read as a 1e-4 mass fraction of the biosphere volume (cell density then irrelevant): m = 5.10e14 g; alive 1.12e34; ever **3.5e51** (log10 51.55), i.e. 'approximately 10^52'. As printed (cells at 10^18 per cm^3 each with proteins at 10^-4) the inputs are not self-consistent: a cell of volume 10^-18 cm^3 is ~10 nm across, below virus size.
So neither source's printed inputs reproduce Eden's 10^52 with a 27.5 kDa protein except Day's version, read charitably.

## Assumptions
- Stated (Eden): upper bound; inputs err 'very heavily toward the high side'.
- Implicit: all proteins on Earth are 250-residue; one-second turnover.

## Responses
- Against: the distinction between molecules and distinct functional sequences: many molecules are copies of the same sequence, so distinct sequences ever realised is far below 10^52 (Eden's own 'say 10^40').
- In support: Eden, p.7, says the 10^52 set 'contains within it all the useful proteins which have existed to date', so Day's paraphrase is a licensed shorthand if 'functional proteins' means 'contained in'.
- Weaknesses: for D's argument the relevant budget is distinct sequences tested by lineages; neither the molecule count nor 10^40 is that quantity.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.7 | quoted above | accurate |
| Wistar p.110 | working paper: less than 10^55 | accurate; matches the reconstruction |

## Pre-registered prediction
Written before the reconstruction. Prediction under Eden: 10^52 +- 1. Under a re-computation with Eden's printed inputs: 10^55. (The prediction under Eden failed; recorded as a fidelity finding, not a refutation of the comparison.)

## Check
Script (arithmetic, not committed): area = 4*pi*(6.371e8)^2; mol = area*1*c/(27500/6.022e23); ever = mol*3.156e17. Results above. Recomputed twice (c=0.3 and c=1e-4).

## Simulator variables implied
N_ever (budget) as a parameter with distinct-sequence variant; generation/turnover time.
