# Quotes: primary literature (R1 pass 2)

Each quote is verbatim (<=60 words), machine-checked against the extracted text of the local copy (Unicode-normalised: ligatures, dashes, apostrophes and superscript-lost exponents may differ from print). Locator = section/page of the paper. **Role codes:** S = bears in favour of the use Day makes (per PLAN pass-1); C = bears against it; N = context; K = bears against a critic's use; KS = supports a critic's use. "Params" = `parameters.yaml` key (or `new:` proposed). Verdicts are "matches / does not match the cited use" only; no wider adjudication. Day's uses are taken from PLAN.md pass-1 and were not re-verified against his texts in this slice.

## Kimura1968

> "Calculating the rate of evolution in terms of nucleotide substitutions seems to give a value so high that many of the mutations involved must be neutral ones."
> - locator: Abstract (Nature landing page; full text paywalled); role: N; params: B

## Chalub2022
- **Cited use (PLAN pass-1):** Day cites it for the claim that k = mu is steady-state only / neutral fixation takes time (B1, "empty pipeline"). Also sought "Chalub 2012".
- **Fidelity (this pass):** Math is not disputed. Paper is a two-allele PDE solution with no mutation or selection, so it does not address substitution rates; it does give a finite-time fixation probability for a stated initial condition. Use as support for "finite-time behaviour differs from the asymptote" is compatible with the paper; use as evidence about k vs mu is not.

> "we consider a population of two types evolving without mutation or selection, the so-called neutral evolution"
> - locator: Abstract; role: C (as support for k != mu with mutation); params: B1

> "Its solution is required to satisfy not only the equation but a series of conservation laws formulated as integral constraints."
> - locator: Abstract; role: N; params: B1

> "Finally, the time-dependent fixation probability is given by"
> - locator: Section 3 (end); role: S/N (finite-time fixation probability for a given initial state); params: B1

> "However, the classical solution decay in the limit t → ∞, and therefore cannot be the correct solution from the modeling point of view."
> - locator: Section 2 (discussion of classical solution); role: N (guard against misreading); params: B1; note: statement is about the PDE solution/measure formulation, not about biological substitution rates

## Zeng2021
- **Cited use (PLAN pass-1):** Day uses s ~ 0.001 as a beneficial-selection coefficient for fixation-time arithmetic (PLAN: t = (2/s) ln(2Ne)).
- **Fidelity (this pass):** Does not match: the quoted value is a predicted mean selection coefficient against trait-affecting variants under negative selection (abstract). Positive selection appears only as a simulation sensitivity scenario.

> "about 1% of human genome sequence are mutational targets with a mean selection coefficient of ~0.001"
> - locator: Abstract; role: C; params: selection.s_zeng_2021

> "We detect widespread signatures of negative selection in the genetic architecture across 155 complex traits with a predicted mean selection coefficient of ~0.001"
> - locator: Results, "Evolutionary inference" / Introduction summary; role: C; params: selection.s_zeng_2021

> "which was significantly higher than that of 0.0005 for physical measures (median P value = 0.015 among the four groups of estimation methods and pleiotropic models)"
> - locator: Results, Fig. 5 discussion; role: N; params: selection.s_zeng_2021; note: preceding clause (symbol lost in text extraction): common diseases had a mean predicted s of 0.0010

> "Since we only detected signatures of negative selection in real traits, our evolutionary simulations focused on the models of negative selection."
> - locator: Results, Discussion of simulations; role: N (nuance: positive selection was only a sensitivity scenario); params: selection.s_zeng_2021

## Bergeron2023
- **Cited use (PLAN pass-1):** Day cites 40-fold variation in mutation rates.
- **Fidelity (this pass):** Matches (Fig. 1 legend and Results).

> "The average pedigree-based mutation rates per generation for each species, which are represented by the squares, show 40-fold variation among species."
> - locator: Results, Fig. 1 legend; role: S (Day cites ~40x variation); params: mutation.mu_per_site_per_gen

> "On average, mutation rates per generation are higher in reptiles (average of all species 1.17 × 10-8, 95% CI of the mean = 5.34 × 10-9 to 1.80 × 10-8)"
> - locator: Results, first paragraph on rates; role: N; params: mutation.mu_per_site_per_gen; note: mammal mean 7.97e-9 is in the same sentence; the human-specific value is in Supplementary Table 8, not the main text

## Keightley2012

> "Direct estimates from genome sequencing of relatives suggest that μ is about 1.1 × 10(-8), which is about twofold lower than estimates based on the human-chimp divergence. This implies that an average of ~70 new mutations arise in the human diploid genome per generation."
> - locator: Abstract (Europe PMC); role: S (mu value); params: mutation.mu_per_site_per_gen; mutation.new_mutations_per_genome

## Kong2012

> "with an average father's age of 29.7, the average de novo mutation rate is 1.20×10-8 per nucleotide per generation"
> - locator: Abstract; role: S; params: mutation.mu_per_site_per_gen

> "The effect is an increase of about 2 mutations per year."
> - locator: Abstract; role: N; params: mutation.new_mutations_per_genome

## BallouxLehmann2012
- **Cited use (PLAN pass-1):** Day cites for k < mu / N-dependence of neutral substitution rate; "k = 0.743 mu" is Day's own figure.
- **Fidelity (this pass):** Partly matches: the paper shows N- and demography-dependence for neutral k only when generations overlap AND population size fluctuates; k = mu stays exact for non-overlapping generations. No 0.743 or 32.3 in the text.

> "One of the central results of the Neutral Theory of evolution (Kimura and Ohta 1971; Kimura 1983) states that the rate k of allele substitution (rate of evolution) at neutral loci is unaffected by fluctuations in population size and is simply equal to the mutation rate."
> - locator: Introduction; role: K (supports k=mu as the standard result); params: new: neutral k=mu

> "we show that the substitution rate at neutral genes does depend on population size fluctuations in the presence of overlapping generations"
> - locator: Abstract; role: S (partial: N-dependence exists under overlapping generations + fluctuating size); params: B3

> "introducing overlapping generations reduces the substitution rate as fewer age class one individuals are produced per generation and therefore mutants."
> - locator: Results, overlapping generations; role: N; params: B3; note: paper gives k = mu(1 - s) for constant survival s; no 0.743 or 32.3 appears anywhere in the text

> "population size fluctuations do not affect substitution rates at neutral loci in a population with discrete nonoverlapping generations"
> - locator: Results, "Overlapping generations without fluctuating demography"; role: K; params: B3

## CSAC2005
- **Cited use (PLAN pass-1):** Day uses ~35M SNV + ~5M indels as required fixations (A3).
- **Fidelity (this pass):** Partly matches: the counts are in the abstract, but the same paper says they are differences between one human and one chimp copy, include polymorphic sites, and that fixed divergence is <=1.06% vs 1.23% total.

> "constituting approximately thirty-five million single-nucleotide changes, five million insertion/deletion events, and various chromosomal rearrangements"
> - locator: Abstract; role: S/N; params: divergence.snv_differences_total; divergence.indel_events_total

> "The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species."
> - locator: Main text, "Nucleotide divergence" / Genome-wide rates; role: C (if 3.5e7 is used as required fixations); params: divergence.snv_differences_total

> "we estimate that polymorphism accounts for 14-22% of the observed divergence rate"
> - locator: Main text, "Nucleotide divergence" / Genome-wide rates; role: C/N; params: new: divergence.fixed_fraction_of_observed (0.78-0.86)

> "Single-nucleotide substitutions occur at a mean rate of 1.23% between copies of the human and chimpanzee genome, with 1.06% or less corresponding to fixed divergence between the species."
> - locator: Main text, Introduction findings; role: N; params: new: divergence.rate_observed=0.0123; fixed<=0.0106

> "Of course, the number of indel events is far fewer than the number of substitution events (,5 million compared with ,35 million, respectively)."
> - locator: Main text, "Insertions and deletions"; role: N; params: divergence.indel_events_total; note: extraction renders "~" as ","

> "t 1 is constant across loci (,6-7 million years38), t 2 is a random variable that fluctuates across loci (with a mean that depends on population size and here may be on the order of 1-2 million years39)"
> - locator: Main text, "Genome-wide rates"; role: N; params: divergence.t_div_years; note: t1 = time since speciation; t2 = ancestral coalescence time (ILS term)

## Yoo2025
- **Cited use (PLAN pass-1):** Day uses 410 Mb (-> 205M per lineage) from Yoo 2025 and cites inversion counts.
- **Fidelity (this pass):** Not matched: neither 410 Mb nor 187 Mb found. SDR average is 327 Mb per lineage; inversion count 1,140 is across the six-ape set vs human reference; divergence measures differ by method (see derived table).

> "We catalogued all structurally divergent regions (SDRs) among the ape genomes and found an average of 327 Mb of sequence (10%) per ape lineage"
> - locator: Main text, Divergence and selection; role: S/N (supports "more divergence than previously estimated"); params: new: divergence.sdr_mb_per_lineage

> "12.5-27.3% of an ape genome failed to align or was inconsistent with a simple one-to-one alignment"
> - locator: Main text, Divergence and selection; role: N; params: new: divergence.unaligned_fraction

> "Gap divergence showed a 5-fold to 15-fold difference in the number of affected megabases when compared to single-nucleotide variants"
> - locator: Main text, Divergence and selection; role: C (bp vs events); params: A3 bp-vs-events

> "we curated 1,140 interspecific inversions, of which 522 are newly discovered"
> - locator: Main text, Structural variation; role: N; params: A3 inversions (event count)

> "Our analyses dated the human-chimpanzee split between 5.5 and 6.3 million years ago (Ma; minimum to maximum estimate of divergence)"
> - locator: Main text, Divergence and selection; role: S/N (matches 6.3 My upper bound); params: divergence.t_div_years

> "we estimated that the human-chimpanzee-bonobo ancestral population size (average Ne = 198,000) is larger than that of the human-chimpanzee-gorilla ancestor (Ne = 132,000)"
> - locator: Main text, Divergence and selection; role: N; params: population.Ne_ancestral_hc

> "Autosome SNV divergence between human and nonhuman primates (NHPs) was lowest for human-chimpanzee and human-bonobo (0.15-0.16%)"
> - locator: Supplementary Information (MOESM1), Note III, "SNP vs. gap divergence"; role: N (internal inconsistency with Table III.14); params: new: divergence.snv_divergence_hc; note: Supplementary Table III.14 (MOESM4, sheet "14") gives mean autosome SNV divergence 0.0146 (1.46%) for chimp-vs-human haplotypes, 0.0016 for human-vs-human; text value looks like a decimal-place slip but this has not been confirmed with authors

> "SNV divergence is defined as the fraction of positions in the target haplotype where the two haplotypes are in different nucleotide states."
> - locator: Supplementary Information (MOESM1), Note III; role: N; params: definition

## Langergraber2012
- **Cited use (PLAN pass-1):** Day uses 6.3-9 My and g_len 20-32.5 y.
- **Fidelity (this pass):** Paper states at least 7-8 My for human-chimp and that its method is independent of fossil calibration; chimp generation ~24-25 y.

> "We date the human-chimpanzee split to at least 7-8 million years and the population split between Neanderthals and modern humans to 400,000-800,000 y ago."
> - locator: Abstract; role: C (Day: 6-7 My) / S for any later-split reading; params: divergence.t_div_years

> "This suggests that molecular divergence dates may not be in conflict with the attribution of 6- to 7-million-y-old fossils to the human lineage"
> - locator: Abstract; role: N; params: divergence.t_div_years

> "The average generation time for the former communities was 24.9, whereas it was 24.3 for the latter."
> - locator: Results (chimpanzee generation time); role: N; params: generation_time_years; note: chimpanzee communities with vs without high infection-induced mortality

## Scally2012

> "In 30% of the genome, gorilla is closer to human or chimpanzee than the latter are to each other; this is rarer around coding genes, indicating pervasive selection throughout great ape evolution"
> - locator: Abstract; role: N; params: population.Ne_ancestral_hc (ILS)

> "We propose a synthesis of genetic and fossil evidence consistent with placing the human-chimpanzee and human-chimpanzee-gorilla speciation events at approximately 6 and 10 million years ago (Mya)."
> - locator: Abstract; role: N; params: divergence.t_div_years

> "This variation reflects local differences in the ancestral effective population size Ne during the period between the gorilla and chimpanzee speciation events, most likely due to natural selection reducing Ne and making ILS less likely."
> - locator: Results, ILS and selection; role: N; params: population.Ne_ancestral_hc

## PradoMartinez2013

> "Inferred effective population sizes have varied radically over time in different lineages and this appears to have a profound effect on the genetic diversity at, or close to, genes in almost all species."
> - locator: Abstract (Europe PMC); role: N; params: population.Ne_ancestral_hc; note: abstract only; numbers are in the paper body/SI (not retrievable here)

## Nunney2003
- **Cited use (PLAN pass-1):** Day cites Haldane 1957 (300 gens) and the cost-of-selection bound (H).
- **Fidelity (this pass):** Nunney reports Haldane's ~1 per 300 generations accurately and confirms hard selection can impose a cost, but finds the cost "substantially less" than Haldane's for M > 1/2 and notes soft selection eliminates it.

> "Based on mutation-selection balance and 10% selective mortality, he suggested that the limit to adaptive evolution was about one allelic substitution per 300 generations."
> - locator: Abstract; role: S (Haldane figure reported correctly); params: haldane.gens_per_substitution

> "For M > 1/2, the cost of natural selection is substantially less than Haldane's estimate; however, when M < 1/2, the cost (and particularly the fixed cost) increases in an accelerating fashion as M is lowered."
> - locator: Abstract; role: C/KS (cost smaller than Haldane under his simulations); params: haldane.gens_per_substitution

> "If correct, this result has far-reaching consequences, both for the interpretation of molecular data (Kimura 1968) and for expectations regarding the survival of populations exposed to long-term environmental change."
> - locator: Introduction; role: S; params: H

> "As a result, soft selection inevitably reduces or eliminates the cost of substitution. However, given directional environmental change, it is likely that hard selection will dominate the adaptive process"
> - locator: Introduction; role: C/KS; params: H (hard vs soft)

## Tenaillon2016
- **Cited use (PLAN pass-1):** Day uses LTEE for G_f, hypermutator hazard (A2, E).
- **Fidelity (this pass):** Hypermutator share (96.5% of point mutations in six populations) matches; neutral mutations accumulating at constant rate also appears and is the basis for critic arguments about k = mu in asexuals.

> "The populations that retained the ancestral mutation rate support a model where most fixed mutations are beneficial, the fraction of beneficial mutations declines as fitness rises, and neutral mutations accumulate at a constant rate."
> - locator: Abstract; role: N (supports neutral clock-like accumulation in non-mutators); params: ltee; k=mu

> "six populations (Ara-1, Ara-2, Ara-3, Ara-4, Ara+3 and Ara+6) had 96.5% of the point mutations, having evolved hypermutable phenotypes"
> - locator: Results, "Genome evolution"; role: S/N (hypermutators); params: ltee.hypermutators

> "Nonsynonymous mutations accumulated ~17.1 times faster than synonymous ones during the first 500 generations and ~3.4 times faster over 50,000 generations."
> - locator: Results, "Dynamics of genome evolution"; role: N; params: ltee

> "Some others-including Ara-4, which became hypermutable, and Ara+2, which did not-are more linear in structure, without deep branches among the sequenced clones."
> - locator: Results, population phylogenies; role: N; params: ltee

## Good2017
- **Cited use (PLAN pass-1):** Day uses the dynamics for G_f, ">=95% rule", fixation counts.
- **Fidelity (this pass):** ">=95%" is not in the main text; Good et al. report clade structure, deficit of population-wide fixations, and rejection of periodic-selection (sweep-by-sweep) models.

> "molecular evolution continues to be characterized by signatures of rapid adaptation, with multiple beneficial variants simultaneously competing for dominance in each population"
> - locator: Abstract; role: S/N; params: ltee; G2

> "We find that the trajectories in Fig. 1 are inconsistent with a "periodic selection" model in which individual driver mutations fix in a sequence of discrete selective sweeps."
> - locator: Results; role: C/N for sweep-by-sweep models (G_f as serial sweeps); params: ltee.gens_per_fixation

> "The number of fixed mutations closely tracks Mp(t) in some populations (e.g. Ara+2 and Ara+4), but there is a marked deficit of fixations in others (e.g. Ara-6)."
> - locator: Results; role: N; params: ltee.whole_pop_fixations_lineage_aware

> "This striking separation of timescales between inter- and intra-clade fixations cannot be explained by clonal interference"
> - locator: Results; role: N; params: ltee

## Barrick2009

> "Although adaptation decelerated sharply, genomic evolution was nearly constant for 20,000 generations."
> - locator: Abstract (Europe PMC; full text paywalled); role: S/N; params: ltee

> "Such clock-like regularity is usually viewed as the signature of neutral evolution, but several lines of evidence indicate that almost all of these mutations were beneficial."
> - locator: Abstract (Europe PMC; full text paywalled); role: S/N; params: E

## Mathieson2015
- **Cited use (PLAN pass-1):** Day uses it for aDNA selection signals / s values and the 1240k panel (C).
- **Fidelity (this pass):** No s values in the main text. Panel is built from known present-day polymorphic sites (array SNPs).

> "The targeted sites include nearly all SNPs on the Affymetrix Human Origins and Illumina 610-Quad arrays, 49,711 SNPs on chromosome X and 32,681 on chromosome Y, and 47,384 SNPs with evidence of functional importance."
> - locator: Main text, first results paragraph; role: S (panel is ascertained on known polymorphic sites); params: C (1240k panel)

> "We performed in-solution enrichment for a targeted set of 1,237,207 SNPs using previously reported protocols"
> - locator: Methods, "Ancient DNA analysis"; role: N; params: C (1240k panel)

> "The targeted SNP set merges 394,577 SNPs first reported in Ref. 7 (390k capture), and 842,630 SNPs first reported in ref.44 (840k capture)."
> - locator: Methods, "Ancient DNA analysis"; role: N; params: C (1240k panel)

> "The strongest signal of selection is at the SNP (rs4988235) responsible for lactase persistence in Europe"
> - locator: Results, "Evidence of selection"; role: N; params: selection (LCT); no s value given in main text

> "the derived allele of SLC24A5 that is the other major determinant of light skin pigmentation in modern Europe appears fixed in the Anatolian Neolithic, suggesting that its rapid increase in frequency to around 0.9 in Early Neolithic Europe was mostly due to migration"
> - locator: Results, pigmentation; role: K/N (SLC24A5: authors attribute rise mostly to migration); params: selection (SLC24A5); no s value given

> "Estimated power for different selection coefficients for a SNP that is selected in all populations for either 50, 100 or 200 generations."
> - locator: Extended Data Fig. 6 legend; role: N; params: selection

## Fu2015

> "we used three sets of oligonucleotide probes that cover about two million sites that are single nucleotide polymorphisms (SNPs) in present-day humans"
> - locator: Results (Oase 1 capture); role: S (probes cover sites polymorphic in present-day humans); params: C (ascertainment)

## Haak2015

> "We generated genome-wide data from 69 Europeans who lived between 8,000-3,000 years ago by enriching ancient DNA libraries for a target set of almost 400,000 polymorphisms."
> - locator: Abstract (Europe PMC); role: N; params: C (ascertainment)

## Mallick2024

> "We process these bams to produce genotypes at a set of about 1.23 million SNPs that have been assayed for nearly all published individuals with ancient DNA data."
> - locator: Main text, "Data processing"; role: S/N; params: C

## Wistar1967
- **Cited use (PLAN pass-1):** Day cites Eden 10^325 vs 10^52, Ulam, Schutzenberger (D).
- **Fidelity (this pass):** Eden's numbers match the text. Ulam and Wright in the same volume reject the random-construction framing; Schutzenberger argues a "gap", not a probability calculation.

> "We may think of words which are 250 letters long, constructed from an alphabet of 20 different letters. There are about 20250 such words or about 10 325 •"
> - locator: Eden, "Inadequacies of Neo-Darwinian Evolution as a Scientific Theory", p. 7; role: S (source of the 10^325 vs 10^52 comparison); params: D; note: OCR renders 20^250 as "20250" and 10^325 as "10 325"

> "The number of protein molecules that ever existed is by this computation about 10 52 •"
> - locator: Eden, p. 7; role: S; params: D

> "Clearly the number of species of protein molecules is much smaller than this, say 1040, but it would be immaterial to our purposes to try to make such a reduction."
> - locator: Eden, p. 7; role: C (Eden himself says the lower number "would be immaterial"; also pitches 10^52 against ALL sequences, not fraction functional); params: D

> "But, I believe that the comments of Professor Eden, in the first five minutes of his talk at least, refer to a random construction of such molecules and even those of us who are in the majority here, the non-mathematicians, realize that this is not the problem at all."
> - locator: Ulam, p. 21-22; role: K/C (Ulam himself rejects random construction as "the problem"); params: D

> "It appears, naIvely at least, that no matter how large the probability of a single mutation is, should it be even as great as one-half, you would get this probability raised to a millionth power, which is so very close to zero that the chances of such a chain seem to be practically nonexistent."
> - locator: Ulam, p. 21; role: S (Ulam found the unselected chain-probability argument troubling); params: D

> "I intend to restrict my argument to show the existence of a serious gap in the current theory of evolution."
> - locator: Schützenberger, p. 73; role: S; params: D

> "From their talks it is clear that even on the most schematic models the number of cycles involved is truly enormous."
> - locator: Schützenberger, p. 73; role: S/N (the "10^1000" cycle scale is quoted from other speakers; not his own computation); params: D

> "On the principle of the children's game of twenty questions in which it is possible to arrive at the correct one of about a million objects by a succession of 20 yes-orono answers, it would require less than 1250 questions to arrive at a specified one of these proteins."
> - locator: Wright, "Comments on the Preliminary Working Papers of Eden and Waddington", p. 118; role: C/K (direct rebuttal to Eden); params: D; note: OCR garble "yes-orono" = "yes-or-no"; Wright writes 10^350 where Eden wrote 10^325

> "In a population as large as the human species, 3 x 10 9 , a mutation rate of 10 5 at each locus implies that all single step mutations from the common alleles will recur in every generation."
> - locator: Wright, p. 119-120; role: N (Wright on mutation supply); params: D; mutation; note: OCR renders 10^-5 as "10 5"

## Axe2004
- **Cited use (PLAN pass-1):** Day cites 1e-77 functional fraction (D).
- **Fidelity (this pass):** Matches the abstract; scope is one domain-sized beta-lactamase fold extrapolated.

> "this implies the overall prevalence of sequences performing a specific function by any domain-sized fold may be as low as 1 in 10(77)"
> - locator: Abstract (Europe PMC; full text paywalled); role: S (source of 1 in 10^77); params: D (new: sequence_space.functional_fraction)

> "the difficulty of specifying a working beta-lactamase domain is assessed here"
> - locator: Abstract; role: N (scope: one beta-lactamase domain, extrapolated); params: D

## Taylor2001

> "Two-stage in vivo selection yielded catalytically active variants possessing biophysical and kinetic properties typical of the natural enzyme even though approximately 80% of the protein originates from the simplified modules and >90% of the protein consists of only eight different amino acids."
> - locator: Abstract (Europe PMC; full text not retrievable); role: K (functional variants tolerate heavy simplification of the sequence); params: D

## KeefeSzostak2001

> "Starting from a library of 6 x 1012 proteins each containing 80 contiguous random amino acids, we selected functional proteins by enriching for those that bind to ATP."
> - locator: Abstract (PubMed); role: K/N (functional proteins found in a 6e12 random library; frequency stated only qualitatively in the abstract); params: D

## Works with no quotable raw text obtained

- **Kimura 1962 (Genetics 47:713)**, **Kimura & Ohta 1969 (Genetics 61:763)**: free on PMC but automated download is blocked by a bot challenge; no abstract exists in PubMed/Europe PMC. No quotes recorded. The fidelity ledger's "accurate" verdicts for both rest on the pass-1 summarizer and are **unverified**.
- **Kimura 1983 p.44 ("2Nv new, distinct mutants")**: not located (Google Books API quota exhausted; no snippet). Unverified. Secondary lecture slides confirm only that k = (2N)(mu)(1/(2N)) = mu is the textbook derivation; those are not quotes from the book.
- **Haldane 1957**: not retrieved. The "about one allelic substitution per 300 generations" figure is confirmed only as reported in Nunney 2003 (quoted above).
- **Crow & Kimura 1970, ReMine 2005, Maruyama 1970/1974, Cannings 1974, Frankham 1995**: record only (paywalled or not retrievable).

## Derived numbers from Yoo 2025 supplementary tables (MOESM4.xlsx)

These are computed by the harvest agent from the xlsx rows (Python/openpyxl, no manual edits) and are NOT quotes. Method and file hash are in `bib-literature.md`; label any use `derived:`.

| item | value | how |
|---|---|---|
| Table III.14 mean autosome SNV divergence, chimp (mPanTro3#1/2) vs human (hg002#M/P) | 0.0146 (1.46%) | sheet "14", column "Mean SNV Div. Autosomes (A)" |
| same, bonobo vs human | 0.0146 | same sheet |
| same, human hap vs human hap (hg002#M vs #P) | 0.0016 | same sheet |
| Table III.14 mean autosome gap divergence, chimp vs human | 0.1247 (12.5%) | same sheet, "Mean Gap Div." |
| Table V.24 SDR total, human-specific (HSA) h1 / h2 | 147.8 Mb / 183.6 Mb | sum of `SDR_Size` by Lineage and Haplotype, sheet "24" |
| Table V.24 SDR total, chimp-specific (PTR) h1 / h2 | 288.9 Mb / 308.2 Mb | same |
| Table V.24 euchromatic SDR only, HSA h1 / h2 | 40.8 Mb / 81.6 Mb | rows with `SDR_Euchromatin` = TRUE |
| Table V.24 euchromatic SDR only, PTR h1 / h2 | 13.2 Mb / 20.1 Mb | same |
| Table XII.67 inversion rows (SYRI+PAV calls vs T2T-CHM13), all six apes | 1,175 rows | sheet "67"; main text says 1,140 curated inversions (>10 kb); chimp assembly contributes 171 rows (96 hom, 75 het) |
| search for 187 Mb or 410 Mb as any single or pairwise sum of the SDR totals above | no match (closest: HSA h2 + PAB h1 = 412.1) | brute force over lineage/haplotype totals; coincidence, not evidence |

**Observation, not a verdict:** the SI text of Note III says autosome SNV divergence for human-chimpanzee and human-bonobo "(0.15-0.16%)", whereas Table III.14 gives 0.0146, i.e. 1.46%, for the same pairs (0.0016 for within-human). The two differ by a factor of ~10; the table value is the one consistent with CSAC 2005's 1.23% total divergence order of magnitude. Not confirmed with the authors.

## Candidate values for `parameters.yaml` (from verified quotes only; nothing edited in that file)

| key | value | source quote above |
|---|---|---|
| divergence.t_div_years (new entry) yoo_2025 | 5.5e6-6.3e6 | Yoo 2025 main text |
| divergence.t_div_years langergraber_2012 | ">=7e6-8e6" (confirms existing entry) | Langergraber abstract |
| divergence.snv_differences_total chimp_consortium_2005 | 3.5e7 (confirms; add note: one copy each, includes polymorphic) | CSAC abstract + Genome-wide rates |
| divergence.indel_events_total | 5.0e6 (confirms) | CSAC abstract |
| new divergence.fixed_fraction_of_observed | 0.78-0.86 (polymorphism 14-22%) | CSAC Genome-wide rates |
| mutation.mu_per_site_per_gen pedigree_human | 1.1e-8 (Keightley), 1.20e-8 (Kong) | abstracts |
| population.Ne_ancestral_hc | 1.32e5 (HCG ancestor), 1.98e5 (HCB ancestor) per Yoo 2025; current entry [5e4,1e5] has no verified source | Yoo 2025 main text |
| selection.s_zeng_2021 | confirmed: 0.001, sign negative | Zeng abstract |
| haldane.gens_per_substitution | 300 (as reported by Nunney 2003; Haldane original unread) | Nunney abstract |
| population.Ne_over_N Frankham1995 | 0.1 (unverified here; abstract not retrieved verbatim) | - |

## Manual downloads (2026-10-07; text via pdftotext of user-downloaded PMC PDFs; OCR artefacts normalised only in spacing)
### Kimura1962 (sha256 24baddd6…f85e1)
> "The probability of fixation of an individual mutant gene is obtained from (8) by putting p = 1/(2N)."
> - locator: p.715–716, eq. 10; role: critics (B7)
> "the probability of ultimate survival of an advantageous mutant gene is approximately twice the selection coefficient (HALDANE 1927). On the other hand, if we let s → 0 in (10), we obtain U = 1/2N, the result known for a neutral gene."
> - locator: p.716; role: Day (≈2s) and critics (1/2N)
### KimuraOhta1969 (sha256 80694ab2…299fc5)
> "a single mutant gene, if it is selectively neutral, takes about 4Ne generations until fixation in a population of effective size Ne."
> - locator: Summary, p.770; role: Day (B2/F)
> "the remaining minority (fraction 1/2N) spread over the entire population (i.e. reach fixation) taking a very large number of generations."
> - locator: p.769; role: critics (B7)
> Note: "recombination" occurs 0 times; no SD/2.15 figure present (first moment only).
