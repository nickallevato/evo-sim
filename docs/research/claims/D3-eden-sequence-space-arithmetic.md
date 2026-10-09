---
id: D3
title: "Eden: there are about 20^250 = 10^325 polypeptide chains of length 250 versus about 10^52 protein molecules that could ever have existed"
side: literature
branch: D
parent: D
edges: [{type: supports, target: D},{type: depends-on, target: D3a}]
load_bearing: false  # D is not required for ROOT
sourcing: firsthand
status: extracted
verdicts:
  internal: holds      # 20^250 = 10^325.26 reproduces; the 10^52 figure does not reproduce from the printed inputs (see D3a) but the comparison is insensitive to it
  fidelity: accurate      # Day's transcription of the two numbers matches p.7; Day's "functional proteins" wording is looser than Eden's "protein molecules" (D3a)
  external: contested   # whether the size comparison bears on evolutionary search depends on landscape structure (D3b); R4 D1: the arithmetic is unaffected; whether the size comparison bears on search depends on landscape structure, measured locally by D1
---

## Statement (verbatim)
> "We may think of words which are 250 letters long, constructed from an alphabet of 20 different letters. There are about 20250 such words or about 10 325 •"

> "The number of protein molecules that ever existed is by this computation about 10 52 •"

> "Clearly the number of species of protein molecules is much smaller than this, say 1040, but it would be immaterial to our purposes to try to make such a reduction."

Source: Eden, 'Inadequacies of Neo-Darwinian Evolution as a Scientific Theory', in Moorhead & Kaplan (eds), *Mathematical Challenges to the Neo-Darwinian Interpretation of Evolution*, Wistar Institute Monograph No. 5 (1967; symposium 25-26 Apr 1966), local copy = 1985 Liss reprint scan, OCR text; page = printed folio (page numbers from the PDF text layer headers; OCR garbles noted in place), p.7. OCR renders 20^250 as '20250', 10^325 as '10 325 •', 10^52 as '10 52 •', 10^40 as '1040'. For comparison, Eden's pre-circulated working paper (same volume, p.110) states:

> "Now the space of all polypeptide sequences of length 250 or less contains about 10 350 members. Over the last billion years a very liberal estimate of the number of genetic couplings is about 1037 • In fact the number of protein molecules of such size that ever existed on earth can be estimated to be less than 10 55 •"
— Eden, Preliminary Working Paper, p.110 ('10 350', '1037', '10 55' = 10^350, 10^37, 10^55).

## Formal statement
S = A^L with A = 20, L = 250: log10 S = 250*log10(20) = 325.257, i.e. S = 1.81e325 (recomputed; Eden: 'about 10^325'). N_ever = 10^52 (p.7; talk) or <10^55 (p.110; working paper). N_ever/S = 10^-273 (talk) or 10^-270 (working paper). The working paper's '10^350' for 'length 250 or less' is not reproduced: sum over lengths <=250 is 20^250*(1+1/20+...) = 1.05*20^250 = 10^325.3. Wright's discussion (p.117) quotes the working paper's 10^350 (D6).

## Assumptions
- Stated (Eden): the biosphere inputs; the upper bound is deliberately high; the real number of species of proteins is 'much smaller, say 10^40'.
- Implicit: 250 residues is typical of a protein; 20 equiprobable letters; sequences of other lengths ignored; counting molecules, not distinct sequences, as the exploration budget.

## Responses
- Against: none on the arithmetic of 20^250. On 10^52: reproduction with Eden's own stated inputs gives 10^55 (D3a). Eden himself calls the reduction to 10^40 'immaterial'.
- In support: Day (D), Rebekah Davis (D14) cite Eden.
- Weaknesses: the number is not a probability; Eden uses it to pose a dichotomy (D3b), not a bound. Because Eden's two figures (10^325 and 10^52) differ by 273 orders of magnitude, the conclusion is not sensitive to any single input error of a few orders.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Wistar p.7 | 'about 20^250 ... about 10^325'; 'about 10^52' | primary |
| Wistar p.110 | 10^350; <10^55 | primary (working paper) |

## Pre-registered prediction
Written before the arithmetic. Prediction under the claimant (Eden/Day): 20^250 = 10^325 +- 0.5; 10^52 reproducible from the printed inputs within ~1 order. Under the opposing model (critics): arithmetic correct but the number is irrelevant. Result that would change the arithmetic verdict: log10(20^250) outside [324.7, 325.8].

## Check
S1 (done): `python3 -I -c "import math;print(250*math.log10(20))"` -> 325.257 (reconciles). 10^52 reconstruction: see D3a (does not reconcile with p.7 inputs: 10^55.0).

## Simulator variables implied
Alphabet size A=20; length L=250; N_ever (exploration budget); distinct-sequence vs molecule-count budget.
