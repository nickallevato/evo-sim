# Zach Hancock (@talkpopgen)

- **Side:** critic
- **Role:** Guest population geneticist on the Gutsick Gibbon video; derives the neutral substitution rate on camera and compares to observed divergence.
- **Stated credentials (as self-described or as introduced; unverified here):** Says he has a PhD in ecology and evolutionary biology, did a postdoc in statistical population genetics, and is an assistant professor at Augusta University (GG-14, GG-15).
- **Sources (see `sources/bib-critics.md`):** GG-1, TH-1

## Arguments mapped to branches
(Branch IDs from `hierarchy.yaml`. Quote IDs are in `sources/quotes-critics.md`.)

| Branch | Argument | Quote refs |
|---|---|---|
| G1 | F_max = t/(g Gf) encodes sequential fixation; implied polymorphism pattern (no standing variation) is contradicted by site-frequency spectra | GG-01, GG-13 |
| A | Factor-of-two error: both lineages fix | GG-02 |
| B5 | k = mu from Taylor expansion of the Kimura fixation formula; 2N mu x 1/(2N) | GG-03 |
| B5 | 76.8 per generation x 2 x 252,000 -> ~38M vs ~35-40M observed SNVs | GG-04, GG-09 |
| A5 | Bacterial neutral rate: 4e-5 per gen -> ~22,000 gens per fixation; humans fix many per generation | GG-07, GG-08 |
| A3x | 205M requires ~407 mutations/gen (~5x his estimate); "within biological reality" if structural variants count | GG-11, GG-12 |

## Weaknesses noted (own math / inputs / reading of Day)
- First pass used a diploid genome (6.4e9) giving 76.8; he corrected to haploid on screen (GG-05) but kept 76 by citing a de novo count of 98-206 per generation that includes structural variants (GG-06). Using haploid SNVs only: 38.4 x 2 x 252,000 = 19.4M, about 1.8x short of ~35M observed (derived; matches the KITTENS and Reddit critiques). The "38M matches 35-40M" agreement therefore partly rests on that factor of two.
- Bacterial mu ~1e-11 per site is lower than the 8.9e-11 per bp measured in the LTEE ancestor (Wielgoss 2011, quoted by McCarthy). With 8.9e-11 the neutral expectation is ~1 per 2,400 gens instead of ~22,000, which is within 2x of the LTEE rate of 1 per 1,322-1,600. The conclusion that humans out-fix E. coli per generation survives, but the comparison "LTEE rate >> neutral" changes character.
- All genome sites are treated as neutral (k = mu x L), an upper bound; no constraint fraction is applied.
- Self-described "back of the napkin" calculation (GG-16), no confidence interval. Auto-captions garble some figures (e.g. "Perky at all 2025").
- Does not address Haldane's cost (branch H) for the adaptive part; the null-model argument shows the neutral share only.
- The 205M step relies on the same SNV-rate model for structural variants while saying structural rates are hard to estimate (internal tension).

## Strongest technical point
The derivation that the neutral substitution rate is mu and that parallel fixation makes F_max misread the required quantity (GG-01, GG-03) is correct textbook theory and checks numerically; the open quantity is the factor ~2 from haploid bookkeeping.

## Unknown / not checked
Whether the whiteboard contained corrections not spoken aloud.
