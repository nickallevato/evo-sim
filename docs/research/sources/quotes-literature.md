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


# Holocene Ne retrieval (2026-10-09)

Retrieved for the C1c Holocene-Ne gap; synthesis in `holocene-ne.md`. Every quote below was machine-checked as a substring of the saved text (Unicode-normalised; table rows use ' | ' as the column separator; superscript-lost exponents may differ from print). Full texts are in `sources/raw/holocene-ne-2026-10-09/` (gitignored). **Role codes here:** DAY = bears for the flat or low-Ne (about 1e4 or below) reading of the Holocene; CRIT = bears for the growth reading; N = context or method caveat. These codes are my own for this section; they are not the S/C/K codes of the pass-2 quotes above. "Params" = `new:population.Ne_holocene_europe` (proposed; `parameters.yaml` not edited).

### Allentoft2024 (sha256 0ad1b076…89ca42)
> "This pattern is consistent with a scenario of increasing effective population sizes during this period"
> - locator: Results, Sociocultural insights (IBD sharing over time); role: CRIT; params: new:population.Ne_holocene_europe
### Ariano2022 (sha256 64095a60…92b304)
> "the Late Neolithic Maltese sample giving a 30-generation average of only 382 individuals"
> - locator: Results and discussion (IBDNe); role: N; params: new:population.Ne_holocene_europe; note: island isolate, not pan-European
### Batini2017 (sha256 4e8d1b06…4bd5e7)
> "All other populations show a signature of Paleolithic expansion, between 13 and 20 KYA."
> - locator: Results (Bayesian Skyline Plots); role: N; params: new:population.Ne_holocene_europe; note: mtDNA (maternal), female effective size; not autosomal
### Browning2015 (sha256 b11fefd3…d803e0)
> "We estimate the effective population size of European-ancestry individuals in the UK four generations ago to be eight million and the effective population size of Finland four generations ago to be 0.7 million."
> - locator: Abstract; role: N; params: new:population.Ne_holocene_europe
> "inferred segments of IBD contain information about effective population size from around 4 generations to around 50 generations ago for SNP array data and to over 200 generations ago for sequence data."
> - locator: Abstract; role: N; params: new:population.Ne_holocene_europe; note: window of the method
> "The estimated effective size for the g = 0 generation (for individuals born in or around 1958) is 27 million (95% confidence interval = 21–34 million). Because of extrapolation in a population with slowing growth rates, this estimate might be too high."
> - locator: Results, Effective Population Size of the UK (WTCCC2); role: CRIT; params: new:population.Ne_holocene_europe
> "the effective size was greater than 4 million more than 3,900 years (130 generations) ago, dropped to 75,000 by 2,250 years (75 generations) ago, increased to over 4 million 1,380 years (46 generations) ago"
> - locator: Results, UK (comparison with Ralph and Coop's estimates); role: N; params: new:population.Ne_holocene_europe; note: the authors' conversion of Ralph & Coop's curve; they call it 'significantly more oscillatory than our estimates'
> "a recent analysis of the site frequency spectrum (SFS) from sequence data on over 10,000 European-American individuals gave a current estimated effective population size of 1.1 million"
> - locator: Introduction; role: N; params: new:population.Ne_holocene_europe
> "In human populations that we examined, the estimates of effective size were approximately one-third of the census size."
> - locator: Abstract; role: N; params: new:population.Ne_holocene_europe
### Browning2018 (sha256 c471df5e…5f8512)
> "With the development of agriculture, human populations have grown super-exponentially during the past few thousand years"
> - locator: Introduction; role: N; params: new:population.Ne_holocene_europe; note: context sentence by IBDNe authors
### Cai2023 (sha256 c9cf06db…e35a7a)
> "The effective population size had a high rate of growth in the most recent 20 generations and reached a current population size of 169 million (95% confidence interval = 139–221 million)."
> - locator: Results, UK Biobank data; role: N; params: new:population.Ne_holocene_europe; note: exceeds census: see next quote
> "went through a period of moderate growth between 50 and 100 generations ago. Between 20 and 50 generations ago, the effective population size was fairly constant."
> - locator: Results, UK Biobank data; role: N; params: new:population.Ne_holocene_europe
> "IBDNe estimates the most recent generations by extrapolating the growth rate of earlier generations and does not account for a possible recent decrease in the population growth rate; hence, the Ne for generation 0 may be overestimated"
> - locator: Results, UK Biobank data; role: N; params: new:population.Ne_holocene_europe
### Childebayeva2022 (sha256 a318b392…236208)
> "we estimated the effective population size to have been ∼5,000 individuals (3,688–6,778 95% CI) for all LBK sites from Germany"
> - locator: Results and Discussion (LBK population structure); role: DAY; params: new:population.Ne_holocene_europe; note: early Neolithic Germany, ROH maximum likelihood
### Coventry2010 (sha256 bd733c50…811997)
> "giving a mean posterior growth rate of 1.094 (that is, an increase of 9.4%) per generation"
> - locator: Results; role: CRIT; params: new:population.Ne_holocene_europe
### Davy2023 (sha256 ee43caa6…aa90cd)
> "an Ne of 10,000, which we take to be a fair assumption of Mid- to Late Neolithic effective population size"
> - locator: STAR Methods (ancestry HMM); role: N; params: new:population.Ne_holocene_europe; note: an assumption, not an estimate
### Fournier2023 (sha256 9506884e…8aefed)
> "an accurate method for inferring effective population size variation during the past ~2000 years in both modern and ancient DNA data"
> - locator: Abstract; role: N; params: new:population.Ne_holocene_europe; note: window of the method
> "IBD-based inference consistently resulted in larger inferred effective population sizes compared to LD-based inference."
> - locator: Results, 1000 Genomes; role: N; params: new:population.Ne_holocene_europe; note: method dependence
> "The recent effective population size inferred for individuals in the South of England was compatible with population size estimates obtained for modern UK Biobank individuals"
> - locator: Results, aDNA (Arras / South England); role: N; params: new:population.Ne_holocene_europe
> "both trajectories show a significant expansion during the iron age (−500 to 800 CE)"
> - locator: Results, aDNA (Vikings); role: CRIT; params: new:population.Ne_holocene_europe
### Fu2013 (sha256 2e65091a…cfe454)
> "accelerated population growth began 5,115 years ago with a per generation growth rate of 1.95% and 1.66% for EAs and AAs, respectively"
> - locator: Results; role: CRIT; params: new:population.Ne_holocene_europe; note: taken from Tennessen et al. 2012
### GaoKeinan2016 (sha256 9d8f07aa…7fd522)
> "They estimated population size for each generation during the last 50 generations (~1250 years) and showed that the UK population had grown from ~0.1 million to 27 (21–34) million individuals during this time."
> - locator: Review text, section on other inference methods; role: CRIT; params: new:population.Ne_holocene_europe; note: review of Browning & Browning 2015; secondary
> "(1) | Nelson et al. (2012) [9] | 14,002 | 202 Genes | 9.3 | 1.7 (1.2, 2.3)"
> - locator: Table 2 (review table of European recent-growth estimates); role: N; params: new:population.Ne_holocene_europe; note: columns: ancient model, study, sample size, variants, growth start (kya), growth rate (%/generation); secondary source for the 9.3 kya start
> "(2)c | Chen et al. (2015) [19] | 4,298 | Whole Exome | 7.3 (6.95, 7.55) | 1.49 (1.11, 1.87)"
> - locator: Table 2; role: N; params: new:population.Ne_holocene_europe; note: Chen et al. 2015 not retrieved here; secondhand via this review
> "(2) | Gazave et al. (2014) [12] | 500 | Neutral variants (216 kb) | 3.5 | 3.4"
> - locator: Table 2; role: N; params: new:population.Ne_holocene_europe
> "(2) | Gao and Keinan (2016) [22] | 4,300 | Whole Exome | Exponential | 4.95 (4.88, 5.05) | 2.2 (2.15, 2.26)"
> - locator: Table 2; role: N; params: new:population.Ne_holocene_europe
### Gazave2014 (sha256 bebd6e0f…d2fbe3)
> "It estimates the ancestral Ne before the growth to be 5,633 (CI of 4,400–7,100), markedly lower than the fixed value of 10,000 in model I (Table 1). It estimates growth starting 141 (117–165) generations ago"
> - locator: Results, model II; role: DAY; params: new:population.Ne_holocene_europe
> "with a less rapid growth rate of 3.4% (2.4–5.1%) per generation, which culminates in an extant Ne of 0.65 (0.3–2.87) million individuals"
> - locator: Results, model II; role: CRIT; params: new:population.Ne_holocene_europe
> "They all estimate the second, more recent epoch of growth to be practically identical to the one estimated in model II and the earlier epoch of growth to be equivalent to an epoch of constant population size"
> - locator: Results (two-epoch models); role: DAY; params: new:population.Ne_holocene_europe
> "another potential explanation is that effective population size increases extremely slowly with the census population size, at least initially."
> - locator: Discussion; role: DAY; params: new:population.Ne_holocene_europe
> "estimated to have started ∼3,500 y ago (assuming 25 y per generation)"
> - locator: Results; role: N; params: new:population.Ne_holocene_europe
### Gravel2011 (sha256 a2217c8a…31261c)
> "NEUO | 1,000 | 500–1,900 | 1,032 | 677–1,290"
> - locator: Table 2 (Low-coverage + exons); role: N; params: new:population.Ne_holocene_europe; note: row: NEUO (European size at the start of growth), columns NIEHS / low-cov+exons / exons
> "rEU (%) | 0.40 | 0.15–0.66 | 0.38 | 0.28–0.59"
> - locator: Table 2 (Low-coverage + exons); role: N; params: new:population.Ne_holocene_europe
> "TEU − AS (kya) | 21.2 | 17.2–26.5 | 23 | 21–27"
> - locator: Table 2 (Low-coverage + exons); role: N; params: new:population.Ne_holocene_europe
> "the current population sizes inferred from our model (15,500, 35,900, and 49,000 for YRI, CEU, and CHB, respectively) are still significantly lower than census sizes"
> - locator: Discussion; role: DAY; params: new:population.Ne_holocene_europe; note: present-day CEU 35,900
> "using a 25 y generation time"
> - locator: Results; role: N; params: new:population.Ne_holocene_europe
### HarrisNielsen2013 (sha256 3899591c…15e422)
> "The out-of-Africa bottleneck period, where the European effective population size is only 1,530, lasts until 5.9 kya."
> - locator: Results (inferred history of Europeans and Yorubans); role: DAY; params: new:population.Ne_holocene_europe; note: IBS-tract method, 1000 Genomes CEU trio parents; instantaneous-step model; Table 2 symbols lost in extraction
### Huang2025 (sha256 ed18f3ac…d47f08)
> "we inferred a ∼3-fold population expansion in a ∼1,000 year period starting ∼5,500 BP"
> - locator: Results, Corded Ware; role: CRIT; params: new:population.Ne_holocene_europe
> "the estimated Ne beyond 50 generations likely does not reflect the true Ne but is the result of regularization."
> - locator: Results, Corded Ware; role: N; params: new:population.Ne_holocene_europe; note: window limit
> "the inferred effective population size of the British Isles is an order of magnitude larger than that of Corded Ware"
> - locator: Discussion; role: CRIT; params: new:population.Ne_holocene_europe
### KGP2015 (sha256 4c635f9f…af836b)
> "European, Asian and American populations shared strong and sustained bottlenecks, all with Ne < 1,500, between 15,000 to 20,000 years ago."
> - locator: Results (population history, PSMC); role: N; params: new:population.Ne_holocene_europe; note: PSMC; ends before the Holocene
> "These bottlenecks were followed by extremely rapid inferred population growth in non-African populations, with notable exceptions including the PEL, MXL and FIN."
> - locator: Results (population history, PSMC); role: CRIT; params: new:population.Ne_holocene_europe; note: no numeric Ne in the text for the Holocene
### Keinan2012 (sha256 2222f5a7…79a386)
> "Coventry et al. (18) | 10,422 | 1400 (900–2800) | 7700# | 9.4 (4.5–14.5)"
> - locator: Table 1 (review of European growth estimates); role: N; params: new:population.Ne_holocene_europe; note: columns: sample size, growth start (years ago), initial Ne, growth per generation (%)
> "The present effective population size of Europeans as estimated by the model is 1.1 million (95% CI, 0.3 to 1.9 million) (18), compared to the present effective population size of only a few tens of thousands estimated by previous models that incorporated recent exponential growth"
> - locator: Main text; role: CRIT; params: new:population.Ne_holocene_europe; note: Coventry 2010 vs earlier
> "Time of growth was assumed in these studies to coincide with the split of the ancestors of Europeans and East Asians, hence the split and growth were estimated as a single parameter."
> - locator: Table 1 footnote; role: N; params: new:population.Ne_holocene_europe; note: caveat on Gravel/Gutenkunst timing
### MathiesonTerhorst2022 (sha256 8412ea26…93dcb8)
> "an effective population size of N = 104"
> - locator: Results (selection scan); role: N; params: new:population.Ne_holocene_europe; note: exponent lost in text extraction (N = 10^4); an input assumed for the scan, not an estimate
### Nelson2012 (sha256 aaffb6eb…918840)
> "we obtained a maximum-likelihood estimate for a recent growth rate of 1.7% (95% confidence interval [CI]=1.2%–2.3%), and a recent European effective population size of 4.0 million (95% CI=2.5–5.0 million; Fig. 1C)"
> - locator: Results; role: CRIT; params: new:population.Ne_holocene_europe
> "These patterns are at odds with notions that human genetic diversity can be summarized by use of an effective population size (Ne) of 10,000 individuals"
> - locator: Results; role: CRIT; params: new:population.Ne_holocene_europe
> "An Ne of 10,000 individuals is predictive of the average pairwise differences between human sequences"
> - locator: Results; role: DAY; params: new:population.Ne_holocene_europe; note: the same paragraph concedes what 1e4 does fit
### Ringbauer2021 (sha256 d60136ce…0fafa1)
> "Assuming that individual mobility is comparable between groups, sROH[4,8] proxies for local population size"
> - locator: Results, Human background relatedness decreased over time; role: N; params: new:population.Ne_holocene_europe
> "median sROH[4,8] values drop from 13 to 66 cM per foraging group to 0–9 cM per early farming group"
> - locator: Results, Human background relatedness decreased over time; role: CRIT; params: new:population.Ne_holocene_europe; note: short-ROH fall = rising local mating pool; no Ne value
### Schaffner2005 (sha256 77f20fbb…2e575a)
> "Ne (post-agriculture) | 100,000"
> - locator: Table 1 (fixed parameters); role: N; params: new:population.Ne_holocene_europe; note: fixed, not fitted
> "T (European agriculture) (gens) | 350"
> - locator: Table 1 (fixed parameters); role: N; params: new:population.Ne_holocene_europe; note: fixed, not fitted
> "Late expansion to a large size, roughly coincident with the advent of agriculture, was included for the sampled populations in all calibrated models, but had little effect on results"
> - locator: Methods; role: N; params: new:population.Ne_holocene_europe
> "The resulting parameters, however, represent a mechanism for producing realistic-looking data, not an inference about the actual history of human populations"
> - locator: Results; role: N; params: new:population.Ne_holocene_europe
### Schiffels2014 (sha256 f0201d22…c20ae8)
> "In Europe, Northern European ancestors (CEU) experience a relatively constant effective population size between 2kya and 10kya, only increasing rapidly since 2kya"
> - locator: Results (Figure 3b); role: DAY; params: new:population.Ne_holocene_europe
> "Between 30kya and 10kya we see similar expansions in population size for the CEU, TSI, GIH, and CHB populations."
> - locator: Results (Figure 3a); role: N; params: new:population.Ne_holocene_europe
### Speidel2021 (sha256 74be2d01…83088f)
> "At shorter distances we observe a clear trend for smaller coalescence rates (larger effective population sizes) toward the present, suggesting strongly increasing local population sizes."
> - locator: Results, Effective Population Sizes Increased from Mesolithic Europe to the Present; role: CRIT; params: new:population.Ne_holocene_europe; note: Relate on aDNA + SGDP; figure-only values
### Tenesa2007 (sha256 ec5ea2de…2eb61c)
> "Effective population size has increased dramatically in the last ∼1000 generations (20,000 yr), from a fairly constant ancestral size of ∼2500 (CEU)"
> - locator: Figure 3 legend; role: DAY; params: new:population.Ne_holocene_europe; note: LD-based, HapMap CEU; ancestral size refers to the bottleneck period before 20 kya
### Tennessen2012 (sha256 9308e185…2e5f13)
> "followed by explosive growth of 1.95% (SD ±0.03%) over the past 5115 years."
> - locator: Results (demographic model); role: CRIT; params: new:population.Ne_holocene_europe
> "The final population sizes in this model are lower than current census sizes"
> - locator: Results (demographic model); role: N; params: new:population.Ne_holocene_europe
### Terhorst2017 (sha256 8616f2d8…2761c8)
> "The European populations (Supplementary Figure 4) experience a similar bottleneck as Asians ending around 50 kya, followed by a period of rapid growth starting 10–15 kya."
> - locator: Results (Figure 5); role: CRIT; params: new:population.Ne_holocene_europe; note: figure-only values
> "A generation time of 29 years was used to convert the coalescent scaling to calendar time."
> - locator: Results (Figure 5 caption); role: N; params: new:population.Ne_holocene_europe

# Refresh 2026-10-09b quotes (foundational and tool literature)
Each quote machine-checked as a substring (whitespace and quote-mark normalised) of the local text. Abstract-only items are quoted from the abstract only. Superscripts are lost in the extracted text where noted.

### DurrettSchmidt2007 (sha256 f18748cc…db9466)
> "given a 1000 nucleotide region in our genome, how long does it take for a specified six to nine letter word to appear in that region in some individual?"
> - locator: abstract/introduction (arXiv:math/0702883v1, p.1); role: BOTH; params: D15 inputs; note: the probability question the paper answers
> "for words of length 6, the average waiting time is 100,000 years"
> - locator: abstract (p.1); role: CRIT; note: their own model; Stone and Wray had computed 5,950 years
> "If we model this by saying that a 7 out of 8 letter match is good enough, the mean reduces to about 60,000 years."
> - locator: abstract (p.1); role: CRIT; note: relaxing perfect-match requirements changes the answer by orders of magnitude (the same sentence block gives 650 million years for length 8 without a 7/8 match)
### DurrettSchmidt2008 (sha256 e699e598…07d6f1)
> "for humans with a much smaller effective population size, this type of change would take >100 million years"
> - locator: abstract; role: DAY; note: critics' own paper gives a waiting time longer than the time since the human-chimp split for this specific two-step regulatory change
> "we use these results to expose flaws in some of Michael Behe's arguments concerning mathematical limits to Darwinian evolution"
> - locator: abstract; role: CRIT
### BeheSnoke2004 (sha256 89ac5071…b7d854)
> "We conclude that, in general, to be fixed in 10 8 generations, the production of novel protein features that require the participation of two or more amino acid residues simply by multiple point mutations in duplicated genes would entail population sizes of no less than 10 9 ."
> - locator: abstract; role: DAY; note: superscripts lost in extraction (10^8 generations, 10^9 individuals)
### Lynch2010 (sha256 b4d2ff1d…095b58)
> "The issue explored here is the procurement of novel traits that specifically require multiple mutations to achieve a fitness advantage."
> - locator: abstract; role: BOTH; note: states the scope; the abstract has no numbers
### HermissonPennings2005 (sha256 31cebc85…fee027)
> "find a large increase in the fixation probability for weak substitutions, if alleles originate from the standing genetic variation"
> - locator: abstract; role: CRIT; params: G2c, A6
> "Adaptations from the standing genetic variation are favored if either the selective advantage is weak or the selection coefficient and the mutation rate are both high."
> - locator: abstract; role: BOTH; note: the conditions are parameter-dependent, so Hancock's prediction needs a stated s and mutation rate to be tested
### MesserPetrov2013 (sha256 123323fb…74ae3b)
> "We argue that soft sweeps might be the dominant mode of adaptation in many species."
> - locator: abstract; role: CRIT; note: "might be", "many species" (not a human-specific claim)
> "Hard sweeps are expected when adaptive alleles are not present in the population at the onset of selective pressure and when the waiting time for adaptive mutations is long."
> - locator: main text, section on when sweeps are hard or soft; role: DAY; note: conditions favouring Day's picture of waiting for new mutations
### DesaiFisher2007 (sha256 ad91a673…54ea4e)
> "sets the rate at which the population accumulates beneficial mutations, which thus also grows only logarithmically with population size and mutation rate"
> - locator: abstract; role: BOTH; note: asexual populations only; bears on LTEE as a ceiling (A2e) and on mutator results (E7)
### Lesecque2012 (sha256 ed1f8991…fe0bca)
> "at least 88% of individuals should fail to reproduce and that each female would need to have more than 16 offspring to maintain population size"
> - locator: abstract; role: BOTH; note: the "paradox" under an absolute-fitness load
> "a species could tolerate 10’s or even 100’s of new deleterious mutations per genome each generation"
> - locator: abstract; role: CRIT; params: H, H10; note: under relative-fitness (competition) selection
### Lynch2016 (sha256 c6b66c57…106c8b)
> "The long-term consequence of such effects is an expected genetic deterioration in the baseline human condition, potentially measurable on the timescale of a few generations in westernized societies"
> - locator: abstract; role: DAY; params: H10; note: mainstream author predicts deterioration under relaxed selection; the abstract gives no size, and "relaxed selection against mildly deleterious mutations" is not drift fixing harmful alleles at 3x the neutral rate
> "the rate is not exceptional once the effective genome size and effective population size are taken into consideration"
> - locator: abstract; role: CRIT; note: on the human germline mutation rate
### Moorjani2016 (sha256 b70133ca…fdb435)
> "We find that there is substantial variation in the molecular clock between apes and monkeys and that rates even differ within hominines."
> - locator: Significance statement; role: BOTH; params: B4, A1
### Haller2023 (sha256 bbf4f3d6…9f5330)
> "The SLiM software framework for genetically explicit forward simulation has been widely used in population genetics."
> - locator: abstract; role: N
### Baumdicker2022 (sha256 0cb4064c…523866)
> "Stochastic simulation is a key tool in population genetics, since the models involved are often analytically intractable and simulation is usually the only way of obtaining ground-truth data to evaluate inferences."
> - locator: abstract; role: N
### GitHub API descriptions (fetched 2026-10-09; sha256 in bib / below)
> "Forward-time simulation in Python using fwdpp"
> - locator: molpopgen/fwdpy11 `description` (sha256 d8e355ba…210b8); role: N
> "SLiM is a genetically explicit forward simulation software package for population genetics and evolutionary biology."
> - locator: MesserLab/SLiM `description` (sha256 667c00a6…555560); role: N
> "Simulate ARGs and genomic sequence data using population genetic models"
> - locator: tskit-dev/msprime `description` (sha256 b821b198…bb0ce); role: N

## Refresh 2026-10-11b-lit quotes

Verbatim (whitespace-normalised substrings of the saved text, machine-checked 2026-10-11). Math glyph spacing follows the XML/PDF extraction ("10 −4"). Sha256 are of the saved files (see `bib-literature.md`, section "Refresh 2026-10-11b-lit").

### Kim2017 (sha256 9a1a87c4b167d4c4f7f3cf78db6c3e39f8c8cba2808c19bc8d676b0ec2e00a8b)
> "We infer significantly fewer (0.38–0.84 fold) strongly deleterious mutations with selection coefficient | s | > 0.01 and more (1.24–1.43 fold) weakly deleterious mutations with selection coefficient | s | < 0.001 compared to previous estimates."
> - locator: Abstract; role: N; params: DFE shares (GAP-05, B9)
> "These studies have found ∼57–61% of new nonsynonymous mutations to be moderately to strongly deleterious (| s | ≥ 10 −3 ), about 15–16% to be weakly deleterious (10 −4 ≤ | s | < 10 −3 ), and the remainder (24–28%) to be nearly neutral"
> - locator: Introduction (describing Eyre-Walker 2006 and Boyko 2008); role: N
> "Our results suggest that nearly neutral forces play a larger role in human evolution than previously thought."
> - locator: Abstract; role: N
> "0 ≤ | s | < 10 −5 10 −5 ≤ | s | < 10 −4 10 −4 ≤ | s | < 10 −3 10 −3 ≤ | s | < 10 −2 10 −2 ≤ | s |"
> - locator: Table 3 column headers; role: N
> "Boyko et al. (2008) (AA a ) 1.8 × 10 −8 , 2.5 b Gamma 0.183 0.096 0.147 0.219 0.355"
> - locator: Table 3, Boyko row; role: N
> "1000 Genomes 1.8 × 10 −8 , 2.5 b Gamma 0.217 (0.212–0.223) 0.112 (0.111–0.113) 0.169 (0.165–0.172) 0.243 (0.235–0.249) 0.259 (0.252–0.266)"
> - locator: Table 3, 1000 Genomes gamma row; role: N
> "A population size of 10,000 diploids is used to rescale"
> - locator: Figure 1 legend; role: N; note: s, not Ns
> "estimates of the proportion of nearly neutral and neutral mutations (| s | < 10 −4 ) are less accurate"
> - locator: Results, simulations (Fig. 2A); role: C

### Boyko2008 (sha256 2312fe12f5140f09bdb0e81dc15ed3134e77edc1cd95dccf05f611d1c5d57fb4)
> "we predict 27–29% of amino acid changing (nonsynonymous) mutations are neutral or nearly neutral (| s |<0.01%), 30–42% are moderately deleterious"
> - locator: Abstract; role: N
> "Our results are consistent with 10–20% of amino acid differences between humans and chimpanzees having been fixed by positive selection"
> - locator: Abstract; role: N; params: alpha (RG-03)

### Boyko2008 and Kim2017: s convention and rescaling (added 2026-10-11, R4-GAP05 fix pass; same saved files, thin spaces normalised to plain spaces, machine-checked)
> "We assume s and 2s are the selective disadvantage of heterozygotes and homozygous mutants and infer the DFE based on the scaled selection parameter, γ = 2Nes."
> - locator: Boyko 2008, Materials and Methods (Boyko2008 sha256 as above); role: N; params: s convention (GAP-05)
> "our results should be interpreted as the distribution of heterozygote fitnesses over all genetic backgrounds"
> - locator: Boyko 2008, Discussion/Methods (saved text); role: N
> "The DFEs inferred using the approach described above were for the population-scaled selection coefficient, scaled by twice the ancestral population size (γ = 2NAs)."
> - locator: Kim 2017, Materials and Methods, "Estimating s from 2Ns"; role: N
> "We computed NA from the value of θS inferred from synonymous sites (Table S1 in File S1) using the equation θS = 4NAμLS."
> - locator: Kim 2017, same subsection; role: N
> "We assumed the mutation rate to be μ = 1.5 × 10−8 to reflect estimates of the mutation rate in the human exome (Ségurel et al. 2014)."
> - locator: Kim 2017, same subsection; role: N
> "For comparison to results from Boyko et al. (2008), we assumed the mutation rate to be μ = 1.8 × 10−8. For the reanalysis of the Boyko et al. (2008) data set, we assumed the same ancestral population size, N = 7778 diploids, instead of computing it."
> - locator: Kim 2017, same subsection; role: N
> "like the method of Boyko et al. (2008), our method assumes additive selective effects and should be interpreted as averaging of selection over all heterozygotes and genetic backgrounds."
> - locator: Kim 2017, Discussion; role: N
> "A population size of 10,000 diploids is used to rescale the distribution of 2Ns to s for Eyre-Walker et al. (2006). For Boyko et al. (2008) and Li et al. (2010), we rescale the DFE from 2Ns to s using population sizes of 25,636 and 52,097 diploids, respectively"
> - locator: Kim 2017, Figure 1 legend (applies to the figure's comparison curves, not to Table 3); role: N

### EyreWalker2006 (sha256 78fc986d4f20eb6052a3e6323e9c0c15fa361ff04929f188c2d80d74fbf4c36f)
> "a gamma distribution with a shape parameter of 0.23 provides a good fit to the data and we estimate that >50% of mutations are likely to have mild effects, such that they reduce fitness by between one one-thousandth and one-tenth"
> - locator: Abstract (abstract only); role: N
> "We also infer that <15% of new mutations are likely to have strongly deleterious effects."
> - locator: Abstract; role: N
> "the average strength of selection acting against a nonsynonymous polymorphism is ∼9 × 10 −5"
> - locator: Abstract; role: N

### KeightleyEyreWalker2007 (sha256 592538eff7271106770b5493765b19612d505d9c7aa8a960fe840b79af9cae94)
> "the mean estimate for the distribution shape parameter is approximately 0.2 for human populations, which implies that the DFE is strongly leptokurtic"
> - locator: Abstract (abstract only); role: N

### Huber2017 (sha256 6fabb2a07d0ac7caa975d212ad81a0e0e1f6304f2b94752a55847e5c81301ae5)
> "we find that humans have a higher proportion of strongly deleterious mutations than Drosophila melanogaster"
> - locator: Abstract (abstract only); role: N

### Rands2014 (sha256 3fd9dde1c35d4f3f865fcf25df5076299e802f73cc45eaf74e3c3a82c3f0a9cb)
> "we estimate that 8.2% (7.1–9.2%) of the human genome is presently subject to negative selection and thus is likely to be functional, while only 2.2% has maintained constraint in both human and mouse since these species diverged"
> - locator: Abstract; role: N; params: constrained fraction (HF)

### Zoonomia2023 (search JSON sha256 d0adb23d306e987cb93fefd62804b2dddc03751c3d212d2db293ecef8ce6e515)
> "At least 332 million bases (~10.7%) in the human genome are unusually conserved across species (evolutionarily constrained) relative to neutrally evolving repeats"
> - locator: Abstract (Science structured abstract via Europe PMC; abstract only); role: N
> "Of 101 million significantly constrained single bases, 80% are outside protein-coding exons"
> - locator: same; role: N

### Uricchio2019 (sha256 3e7c44cb27fb68ffbe07b4ba2884dc31c448145c93d365142643e22c5b865977)
> "estimate α = 0.135 in human protein-coding sequences, 72% of which is contributed by weakly-adaptive variants"
> - locator: Abstract; role: N; params: alpha (RG-03)
> "95% highest posterior density. α: total adaptation rate;"
> - locator: table caption, inferred adaptation rates; role: N
> "0.135 (0.096,0.17) 0.097 (0.0,0.21) 0.041 (0.0,0.13) VIPs 6249 10309 0.224 (0.17,0.28)"
> - locator: same table (total, weak, strong; then VIPs row); role: N; note: first row label reads "Whole-egoism" in the saved copy
> "original aMK approach ( α ^ = 0.076"
> - locator: Results; role: N

### CSAC2005 (held copies; txt sha256 0b5abab3be36578ac4c7e994a94c051ba1f39e491cb8615d3be39b2abf908e5a)
> "The K A/K S ratio for the human–chimpanzee lineage (q hominid) is 0.23."
> - locator: main text, gene-evolution section, journal p. 76-77; role: N; params: dN/dS (Day 0.80 vs 0.23)
> "Similarly, K A/K I was also estimated as 0.23."
> - locator: same paragraph; role: N
> "the results imply that 77% of amino acid alterations in hominid genes are sufficiently deleterious as to be eliminated by natural selection"
> - locator: same paragraph; role: N
> "We began by identifying a set of 13,454 pairs of human and chimpanzee genes with unambiguous 1:1 orthology"
> - locator: same section; role: N; params: gene list (Q176)
> "A total of 585 of the 13,454 human–chimpanzee orthologues (4.4%) have observed K A/K I . 1"
> - locator: same section; role: N
> "Nucleotide divergence rates were estimated using baseml with the REV model."
> - locator: Methods, rates of divergence; role: N
> "A total of 19,277 human RefSeq transcripts157, representing 16,045 distinct genes, were indirectly aligned to the chimpanzee sequence via the genome alignment."
> - locator: Methods, Gene annotation (CSAC2005.txt ~l.1996; added 2026-10-12, machine-checked against the held txt, whitespace normalised); role: N; params: Q180 (alignment method behind the 13,454 list: the genome alignment, not a protein-guided realignment)
> "After removing low-quality sequences and likely alignment artefacts, an initial catalogue containing 13,454 distinct 1:1 human–chimpanzee orthologues was created for the analyses described here."
> - locator: Methods, Gene annotation (~l.1997-1999); role: N; params: Q176, Q185
> "A subset of 7,043 of these genes with unambiguous mouse and rat orthologues were realigned using Clustal W158 for the lineage-specific analyses."
> - locator: Methods, Gene annotation (~l.2000-2002); role: N; params: Q180 (Clustal W only for a 7,043-gene subset, lineage-specific analyses)
> "K A and K S were estimated jointly for each orthologue using codeml with the F3x4 codon frequency model and no additional constraints"
> - locator: Methods, Rates of divergence (~l.2006-2008); role: N
> "with N S/N A, the ratio of synonymous to non-synonymous sites, estimated as 0.36 from the orthologue alignments."
> - locator: Methods, Rates of divergence (~l.2009-2011); role: N; note: stated for the divergent-vs-polymorphic comparison (K A/K S = (DA/N A)/(DS/N S)); inverse N A/N S = 2.78
> "Unless otherwise specified, K A/K S for a set of genes was calculated by summing the number of substitutions and the number of sites to obtain K A and K S for the concatenated set before taking"
> - locator: Methods, Rates of divergence (~l.2011-2013; sentence continues on the next page); role: N; params: pooled estimator (no mean-of-ratios mismatch unless the hominid 0.23 was "otherwise specified", which the main text does not say)
> "with unambiguous 1:1 orthology for which it was possible to generate high-quality sequence alignments covering virtually the entire coding region"
> - locator: main text, gene-evolution section (~l.702-704; added 2026-10-12, machine-checked); role: N; params: Q180, Q185 (the 13,454 set was selected on alignment quality and coverage: a point for Day's gene-set/alignment concern, and a point against reading the 0.23 as a protein-guided gap-out)
> "than the value of 0.23 obtained with all human–chimpanzee orthologues"
> - locator: main text (~l.891); role: N; note: the 0.23 is stated as the all-orthologue (13,454) value

### Nielsen2005 (sha256 a091301eb921b2df4616b1044bf5e40003477e9462be035c6cb2a3cdeae69ebb)
> "The average numbers of nonsynonymous and synonymous mutations per nucleotide site are 0.002578 and 0.003281, respectively."
> - locator: Results; role: N; note: per nucleotide site, not per nonsynonymous/synonymous site; ratio 0.786 is NOT dN/dS
> "We here compare 13,731 annotated genes from humans to their chimpanzee orthologs"
> - locator: Synopsis; role: N
> "Seven hundred thirty-three of the 8,079 genes evolved with d N / d S greater than one, but only 35 had p -values less than 0.05"
> - locator: Results; role: N

### Bakewell2007 (sha256 e388f6fc89f2d347e22c34cd8a67b9e3603a948c048a1a977f630b6ffc4d0e92)
> "Here, we test this hypothesis by analyzing nearly 14,000 genes of humans and chimps."
> - locator: Abstract (abstract only); role: N
> "despite a generally higher nonsynonymous substitution rate in humans"
> - locator: Abstract; role: N

### Good2017-SI (sha256 bb23faa5e97dd59cc6e3176d5720ee9c662ade6123ed6935f135d9cb762be9ba)
> "From this polymorphic state, the mutation can transition to either a fixed state F, where all reference reads are sequencing errors, or an extinct state E that is similar to the ancestral state above. In rare cases, mutations are allowed to transition from E back to A, after which it can be reborn as a recurrent mutation event."
> - locator: SI section 5.2 "Simplest hidden Markov model", p. 15; role: N; params: L6 (F has no listed exit)
> "Pr[A → P] ≈ 10−2 , Pr[P → F] ≈ Pr[P → E] ≈ 0.5 , Pr[E → P] ≈ 10−6 , (31)"
> - locator: SI Eq. (31); role: N
> "we turned to an ad hoc Markov model that contains some of the minimal features of a true mutation trajectory"
> - locator: SI section 5.2; role: C
> "though the results are relatively insensitive to the precise values"
> - locator: SI after Eq. (31); role: C

### Byars2010 (sha256 3c6fae3d376fd3d26889f440871437d60c2bc59ca85aae5ca8c93a3cc0198a77)
> "we measured the strength of selection, estimated genetic variation and covariation, and predicted the response to selection for women in the Framingham Heart Study"
> - locator: Abstract (abstract only); role: N; params: L2 h
> "We found that natural selection is acting to cause slow, gradual evolutionary change."
> - locator: Abstract; role: N

### Stearns2010 (Nat Rev Genet; sha256 077101180e25164da96b10c4a5a2fe763b05b0c9ec20e0c5e6e4b47da442f132)
> "Are humans currently evolving? This question can be answered using data on lifetime reproductive success, multiple traits and genetic variation and covariation in those traits."
> - locator: Abstract (PubMed; abstract only); role: N; params: L2 h

## Refresh 2026-10-12c-lit quotes (variance components for FMnull, `research/checks/fm_mesa_null.py`)
Full text via Europe PMC `fullTextXML` (PLoS OA) converted to plain text; every quote machine-checked as a whitespace-normalised substring. Ids `FML-<paper>-<n>`. Abstract-only items are marked. Numbers not in the text (figures, tables) are not recorded.

### Smith2018 (sha256 c9d859311826828aa3457e037f60ea6abb2710228636b3301e5537899bfc4939)
> "at the 1MB scale we infer that ~90% of regions have a mutation rate within 50% of the mean"
> - id: FML-S1; locator: Abstract; role: N; note: 1 Mb; human germline DNM (130,000 DNMs, 3 trio datasets); mutation, not divergence
> "The CV of the gamma distribution fitted to the density of DNMs is 0.18, 0.27 and 0.15 for the Francioli, Wong and Jonsson datasets respectively (Fig 2)."
> - id: FML-S2; locator: Results, Distribution of rates; role: N; note: 1 Mb; human DNM; CV = excess over sampling error
> "A gamma distribution with a coefficient of variation of 0.18 is one in which 90% of regions have a mutation rate within 30% of the mean"
> - id: FML-S3; locator: Results, Distribution of rates; role: N; note: internal tension with the Abstract's 'within 50%' (CV 0.18 gives ~+/-30%); both recorded
> "we divided the genome into non-overlapping windows of 10KB, 100KB, 1MB and 10MB and fit a gamma distribution to the number of mutations per region"
> - id: FML-S4; locator: Results, Distribution of rates; role: N; note: scales 10 kb-10 Mb
> "The slope for each dataset is shallower than this (Francioli b = -0.25; Wong b = -0.10; Jonsson b = -0.16)."
> - id: FML-S5; locator: Results, Fig 4 text; role: N; note: log-log slope of CV on window size; -0.5 would mean all variation is finer-scale. 100-kb CV is NOT given in text (Fig 4/S1 Table only); 100-kb CV from these slopes is derived, not quoted
> "We find that genomic features explain less than 40% of the explainable variance in the rate of DNM."
> - id: FML-S6; locator: Abstract; role: N; note: covariates (replication time, recombination, GC etc.) vs DNM density; the Discussion says 'less than 50%'
> "Furthermore, the largest amounts of variation are at the smallest scales (Fig 4) where we have the lowest density of DNMs."
> - id: FML-S7; locator: Discussion; role: N; note: fine scale carries the most variance but is least measured
> "the correlation between divergence and rate of DNM is only about half as strong as it could and this correlation gets worse as more divergent species are considered"
> - id: FML-S8; locator: Discussion; role: N; note: divergence vs DNM density; biased gene conversion proposed as the cause

### McVicker2009 (sha256 9bee2be2a1ef463dbfbf26bba15456b8a8e33aac1fd9bfff6fe3bf7073b3fcdf)
> "a surprisingly large genome average diversity reduction due to selection of 19–26% on the autosomes and 12–40% on the X chromosome"
> - id: FML-M1; locator: Abstract; role: N; note: diversity (Ne) reduction by background selection, genome average
> "The mean autosomal B value predicted by our model is 0.74–0.81 (bootstrap 90% CI)"
> - id: FML-M2; locator: Discussion; role: N; note: B = fraction of neutral diversity retained
> "Long term selection, rather than complex speciation scenarios, explains the large intragenomic variation in human/chimpanzee divergence."
> - id: FML-M3; locator: Abstract; role: N; note: H/C divergence variation; paper's own claim
> "Human diversity and human/chimpanzee (H/C) divergence are indeed both substantially reduced near conserved segments"
> - id: FML-M4; locator: Results; role: N; note: 10% nearest vs 50% farthest neutral sites; magnitudes in Fig 3 only (not in text)
> "In comparison to B, factors previously proposed to influence local mutation rates such as recombination rate and GC content [17] are only weakly correlated with diversity and H/C divergence"
> - id: FML-M5; locator: Discussion; role: N; note: 1 Mb windows; Spearman r^2 (Fig 7C)
> "Pairwise correlations (Spearman's rank squared) with regional human/chimpanzee (H/C) divergence and human diversity in non-overlapping 1 Mb windows across all autosomes."
> - id: FML-M6; locator: Figure 7 legend; role: N; note: 1 Mb; values in figure only
> "Non-overlapping autosomal windows of sizes between 212 and 222 bp were used for calculations."
> - id: FML-M7; locator: Figure S6 legend (Supporting Information); role: N; note: extraction lost superscripts: 2^12-2^22 bp (4 kb-4 Mb)

### Phung2016 (sha256 35e3b9413f9139d549c317f894d6003401727ebceb197d7d3dd98985c03ac1d1)
> "background selection in the ancestral population can still explain a large proportion of the variance in divergence across the genome"
> - id: FML-P1; locator: Abstract; role: N; note: paper's claim; simulation, human-chimp and deeper pairs
> "Here we use the value of Spearman's ρ estimated from the data after filtering out sites that could be affected by biased gene conversion (ρ = 0.108)."
> - id: FML-P2; locator: Results (recombination vs human-chimp divergence); role: N; note: 100 kb windows; human-chimp
> "When considering a model without background selection (i.e. B = 1 for all windows), the average value of Spearman's ρ between human-chimp divergence and recombination rate was 0.042"
> - id: FML-P3; locator: Results; role: N; note: simulated, no BGS; with McVicker B the paper reports rho 0.107
> "Each point represents the mean divergence and functional content (A and B) or recombination rate (C and D) in 1% of the 100kb windows binned by functional content or recombination rate."
> - id: FML-P4; locator: Figure legend; role: N; note: window = 100 kb
> "the main driver of these correlations is not the average amount of ancestral polymorphism, but rather the contribution to the variance in divergence due to the variance in ancestral polymorphism."
> - id: FML-P5; locator: Results (S4 Fig discussion); role: N; note: ancestral-polymorphism variance, not mean, drives the BGS-divergence correlation

### DuretArndt2008 (sha256 9576c4f34078f8e66b59dee065414862ea9c7630f84d4ec704cbd3762ea8db6c)
> "the GC-content toward which sequences are evolving is strongly negatively correlated to the distance to telomeres and positively correlated to the rate of crossovers (R2 = 47%)"
> - id: FML-D1; locator: Abstract; role: N; note: GC* (stationary GC) in primate non-coding DNA, 1 Mb; human
> "we found at the 1 Mb scale a strong correlation between GC* and the sex-averaged rate of crossover on autosomes, both with the HAPMAP data (Pearson correlation R2 = 0.36, Figure 1b) and with the deCODE data (R2 = 0.31)."
> - id: FML-D2; locator: Results; role: N; note: 1 Mb; R^2 of GC*, not of substitution density
> "the crossover rate explains 36% of the variance in GC*, compared to only 15% of the variance in GC"
> - id: FML-D3; locator: Results; role: N; note: 1 Mb; human
> "Thus, for an average recombination hotspot (i.e. 4Ns = 5.2), the impact of BGC on the local substitution rate is relatively modest."
> - id: FML-D4; locator: Results, BGC Model; role: N; note: model prediction
> "The rate of substitution in that hotspot is predicted to be about 11.1%, i.e. about 20 times higher than in the rest of the genome."
> - id: FML-D5; locator: Results, BGC Model; role: N; note: hotspot of ~450 cM/Mb; model prediction; hotspot extent small
> "recombination hotspots can create strong substitution hotspots"
> - id: FML-D6; locator: Abstract; role: N; note: gBGC substitution excess is localized to hotspots

### Hobolth2007 (sha256 a2a5520884c479cf77fbd224f933c2f5228ce20b1494f38a4ed6d84669144c3f)
> "We find a very recent speciation time of human–chimp (4.1 ± 0.4 million years), and fairly large ancestral effective population sizes (65,000 ± 30,000 for the human–chimp ancestor and 45,000 ± 10,000 for the human–chimp–gorilla ancestor)."
> - id: FML-H1; locator: Abstract; role: N; note: coal-HMM; 1.9 Mb of four autosomal HCGO alignments; assumes orangutan 18 My, generation 25 y
> "Furthermore, around 50% of the human genome coalesces with chimpanzee after speciation with gorilla."
> - id: FML-H2; locator: Abstract; role: N; note: i.e. coalescence in the HCG ancestor
> "We apply the HMM to four autosomal contiguous human–chimp–gorilla–orangutan alignments comprising a total of 1.9 million base pairs."
> - id: FML-H3; locator: Abstract; role: N; note: data size
> "shows that 78% ± 5% of the alignment supports state HC1"
> - id: FML-H4; locator: Results (X chromosome); role: N; note: X chromosome; ~250 kb; state HC1 = human-chimp sister topology
> "The average number of base pairs in state HC1 correlates well with the average recombination rate of the target estimated from pedigree data"
> - id: FML-H5; locator: Results (Table 2); role: N; note: tract-length scale: numbers in Table 2, not in extracted text

### MasseyKoren2022 (sha256 6c6e6c61bb0feea0dbbe5bdf4cd510095878c22c95aa11c4beb2470f14e5db15)
> "Sequence data analyzed in this study are available from the Sequence Read Archive (SRA) under accession number PRJNA419407. The reference assembly T2T-CHM13 v1.1 was downloaded from GitHub (https://github.com/marbl/CHM13). Chain files for liftOver (grch38.t2t-chm13-v1.1.over.chain; t2t-chm13-v1.1.grch38.over.chain) were obtained from the UCSC Genome Browser (https://t2t.gi.ucsc.edu/chm13/dev/t2t-chm13-v1.1/downloads/)."
> - id: FML-R1; locator: Data availability; role: N; note: T2T replication-timing profiles (5 cell lines); processed profile location NOT stated in the open text

### HodgkinsonEyreWalker2011 (sha256 676d1d7066e2b4b948296bcedb8256d87934a5fb1e483d36892ec743a72d768b)
> "The mutation rate varies over many different scales, from adjacent sites to whole chromosomes, with the strongest variation seen at the smallest scales."
> - id: FML-HE1; locator: Abstract (Europe PMC record; paywalled, abstract only); role: N; note: no numbers in abstract

### HwangGreen2004 (sha256 5c4e781eab4f8e95d241c55888f1560215cc221eafd38e28fb8d22dd881426d1)
> "In contrast to other substitution types, CpG transition substitutions have accumulated in a relatively clock-like fashion."
> - id: FML-HG1; locator: Abstract (Europe PMC record; PNAS page behind bot challenge, abstract only); role: N; note: 19 mammals, 1.7 Mb region
> "characterize phylogenetic variation in context-dependent substitution patterns in a 1.7-megabase genomic region in 19 mammalian species"
> - id: FML-HG2; locator: Abstract; role: N; note: 

## Criticality pass iii quotes (AMSTAR 2 and ROBIS), 2026-10-12

Purpose: the wording of every AMSTAR 2 item and every ROBIS signalling question applied in [`../criticality/amstar2-robis-2026-10-12.md`](../criticality/amstar2-robis-2026-10-12.md), with the rating rules that pass relies on. These are appraisal instruments, not sources for any claim file; role codes S/C/N/K do not apply and the role field says what part of the instrument the line is. Fetched 2026-10-12 about 23:14 UTC into `sources/raw/crit3-amstar-robis-2026-10-12/` (gitignored), one directory per file. All 77 quotes were machine-checked as exact substrings of the extracted text after whitespace and curly-quote normalisation (curly quotation marks in the originals are printed straight here); checklist and tool items that wrap over several lines in the PDF are joined with single spaces. No item wording is from memory. Each sha256 is of the raw downloaded file (PDF or Europe PMC XML); the XML was matched after tags were stripped.

### Shea2017 (sha256 a38ebd064d97d1e2253033b264f5b5d90d2bab92efcb9d816e15ea32203272e1)
> "Protocol registered before commencement of the review (item 2)"
> - id: AM-B1a; locator: Box 1; role: critical domain; note: 
> "Adequacy of the literature search (item 4)"
> - id: AM-B1b; locator: Box 1; role: critical domain; note: 
> "Justification for excluding individual studies (item 7)"
> - id: AM-B1c; locator: Box 1; role: critical domain; note: 
> "Risk of bias from individual studies being included in the review (item 9)"
> - id: AM-B1d; locator: Box 1; role: critical domain; note: 
> "Appropriateness of meta-analytical methods (item 11)"
> - id: AM-B1e; locator: Box 1; role: critical domain; note: 
> "Consideration of risk of bias when interpreting the results of the review (item 13)"
> - id: AM-B1f; locator: Box 1; role: critical domain; note: 
> "Assessment of presence and likely impact of publication bias (item 15)"
> - id: AM-B1g; locator: Box 1; role: critical domain; note: 
> "We emphasise that our listing is a suggestion and appraisers may add or substitute other critical domains."
> - id: AM-B1h; locator: section 'Identification of critical domains'; role: caveat; note: 
> "No or one non-critical weakness"
> - id: AM-B2a; locator: Box 2 (High); role: rating; note: 
> "the systematic review provides an accurate and comprehensive summary of the results of the available studies that address the question of interest"
> - id: AM-B2h; locator: Box 2 (High); role: rating; note: what the overall rating is a rating of
> "More than one non-critical weakness"
> - id: AM-B2b; locator: Box 2 (Moderate); role: rating; note: 
> "One critical flaw with or without non-critical weaknesses"
> - id: AM-B2c; locator: Box 2 (Low); role: rating; note: 
> "More than one critical flaw with or without non-critical weaknesses"
> - id: AM-B2d; locator: Box 2 (Critically low); role: rating; note: 
> "Multiple non-critical weaknesses may diminish confidence in the review and it may be appropriate to move the overall appraisal down from moderate to low confidence"
> - id: AM-B2e; locator: Box 2 footnote; role: rating; note: 
> "We strongly recommend that individual item ratings are not combined to create an overall score."
> - id: AM-B2f; locator: section 'Applying AMSTAR 2 to systematic reviews'; role: rating; note: 
> "If no information is provided to rate an item, the review authors should not be given the benefit of doubt and the item should be rated as a "No.""
> - id: AM-B2g; locator: section on response options; role: rating; note: 

### AMSTAR2-checklist (sha256 318ba4139ff590e8aacc84c7be4dc84ddaa3fcd52522e10f7508c52ead2d1f05)
> "AMSTAR 2: a critical appraisal tool for systematic reviews that include randomised or non- randomised studies of healthcare interventions, or both"
> - id: AM-00; locator: title line, p.1; role: scope; note: the instrument's own statement of what it is for; "non- randomised" is a line-wrap artefact of the PDF text (the title prints "non-randomised")
> "Did the research questions and inclusion criteria for the review include the components of PICO?"
> - id: AM-01; locator: item 1, p.1; role: item; note: 
> "Did the report of the review contain an explicit statement that the review methods were established prior to the conduct of the review and did the report justify any significant deviations from the protocol?"
> - id: AM-02; locator: item 2, p.1; role: item (critical); note: 
> "Did the review authors explain their selection of the study designs for inclusion in the review?"
> - id: AM-03; locator: item 3, p.1; role: item; note: 
> "Did the review authors use a comprehensive literature search strategy?"
> - id: AM-04; locator: item 4, p.1; role: item (critical); note: 
> "Did the review authors perform study selection in duplicate?"
> - id: AM-05; locator: item 5, p.1; role: item; note: 
> "Did the review authors perform data extraction in duplicate?"
> - id: AM-06; locator: item 6, p.2; role: item; note: 
> "Did the review authors provide a list of excluded studies and justify the exclusions?"
> - id: AM-07; locator: item 7, p.2; role: item (critical); note: 
> "Did the review authors describe the included studies in adequate detail?"
> - id: AM-08; locator: item 8, p.2; role: item; note: 
> "Did the review authors use a satisfactory technique for assessing the risk of bias (RoB) in individual studies that were included in the review?"
> - id: AM-09; locator: item 9, p.2; role: item (critical); note: 
> "Did the review authors report on the sources of funding for the studies included in the review?"
> - id: AM-10; locator: item 10, p.2; role: item; note: 
> "Reporting that the reviewers looked for this information but it was not reported by study authors also qualifies"
> - id: AM-10n; locator: item 10, p.2; role: criterion; note: 
> "If meta-analysis was performed did the review authors use appropriate methods for statistical combination of results?"
> - id: AM-11; locator: item 11, p.3; role: item (critical); note: 
> "If meta-analysis was performed, did the review authors assess the potential impact of RoB in individual studies on the results of the meta-analysis or other evidence synthesis?"
> - id: AM-12; locator: item 12, p.3; role: item; note: 
> "Did the review authors account for RoB in individual studies when interpreting/ discussing the results of the review?"
> - id: AM-13; locator: item 13, p.3; role: item (critical); note: 
> "Did the review authors provide a satisfactory explanation for, and discussion of, any heterogeneity observed in the results of the review?"
> - id: AM-14; locator: item 14, p.3; role: item; note: 
> "If they performed quantitative synthesis did the review authors carry out an adequate investigation of publication bias (small study bias) and discuss its likely impact on the results of the review?"
> - id: AM-15; locator: item 15, p.3; role: item (critical); note: 
> "Did the review authors report any potential sources of conflict of interest, including any funding they received for conducting the review?"
> - id: AM-16; locator: item 16, p.4; role: item; note: 
> "at least two reviewers independently agreed on selection of eligible studies and achieved consensus on which studies to include"
> - id: AM-05c; locator: item 5, p.1; role: criterion; note: 
> "provided a list of all potentially relevant studies that were read in full-text form but excluded from the review"
> - id: AM-07c; locator: item 7, p.2; role: criterion; note: 

### AMSTAR2-guidance (sha256 d08d0bb466a5f8b38a00153b7b2c68e62aa96e9857bfc303d4b17cb26680f6f5)
> "Authors should demonstrate that they worked with a written protocol with independent verification."
> - id: AM-G2a; locator: Item 2, p.1; role: guidance; note: 
> "At a minimum this should be stated in the report (scores 'Partial Yes')."
> - id: AM-G2b; locator: Item 2, p.1; role: guidance; note: 
> "Obvious unexplained discrepancies should result in downgrading of the rating."
> - id: AM-G2c; locator: Item 2, p.2; role: guidance; note: 
> "There should have been at least two independent assessors for study selection."
> - id: AM-G5; locator: Item 5, p.3; role: guidance; note: 
> "In the event that one individual carried out data extraction a second reviewer should have checked agreement on a sample of studies and they should have achieved a kappa score of 0.80 or greater."
> - id: AM-G6; locator: Item 6, p.3; role: guidance; note: 

### Whiting2016 (sha256 18be2acca11a7fe431a04b76c557ee700808c3b9e4d735ae1c0cc4013b98c1b9)
> "The tool is completed in three phases: (1) assess relevance (optional), (2) identify concerns with the review process, and (3) judge risk of bias."
> - id: RB-W1; locator: Abstract (Results); role: structure; note: 
> "ROBIS is the first rigorously developed tool designed specifically to assess the risk of bias in systematic reviews."
> - id: RB-W2; locator: Abstract (Conclusion); role: scope; note: 

### ROBIS-tool (sha256 6052c8cdf1bafbeacd6e7451da03069d0509775e00ba087dbd69b6b4c0bf65a0)
> "ROBIS is designed to assess the risk of bias in reviews with questions relating to interventions, aetiology, diagnosis and prognosis."
> - id: RB-00; locator: Phase 1, p.1; role: scope; note: 
> "Did the review adhere to pre-defined objectives and eligibility criteria?"
> - id: RB-1.1; locator: Domain 1; role: signalling question; note: 
> "Were the eligibility criteria appropriate for the review question?"
> - id: RB-1.2; locator: Domain 1; role: signalling question; note: 
> "Were eligibility criteria unambiguous?"
> - id: RB-1.3; locator: Domain 1; role: signalling question; note: 
> "Were any restrictions in eligibility criteria based on study characteristics appropriate (e.g. date, sample size, study quality, outcomes measured)?"
> - id: RB-1.4; locator: Domain 1; role: signalling question; note: 
> "Were any restrictions in eligibility criteria based on sources of information appropriate (e.g. publication status or format, language, availability of data)?"
> - id: RB-1.5; locator: Domain 1; role: signalling question; note: 
> "Did the search include an appropriate range of databases/electronic sources for published and unpublished reports?"
> - id: RB-2.1; locator: Domain 2; role: signalling question; note: 
> "Were methods additional to database searching used to identify relevant reports?"
> - id: RB-2.2; locator: Domain 2; role: signalling question; note: 
> "Were the terms and structure of the search strategy likely to retrieve as many eligible studies as possible?"
> - id: RB-2.3; locator: Domain 2; role: signalling question; note: 
> "Were restrictions based on date, publication format, or language appropriate?"
> - id: RB-2.4; locator: Domain 2; role: signalling question; note: 
> "Were efforts made to minimise error in selection of studies?"
> - id: RB-2.5; locator: Domain 2; role: signalling question; note: 
> "Were efforts made to minimise error in data collection?"
> - id: RB-3.1; locator: Domain 3; role: signalling question; note: 
> "Were sufficient study characteristics available for both review authors and readers to be able to interpret the results?"
> - id: RB-3.2; locator: Domain 3; role: signalling question; note: 
> "Were all relevant study results collected for use in the synthesis?"
> - id: RB-3.3; locator: Domain 3; role: signalling question; note: 
> "Was risk of bias (or methodological quality) formally assessed using appropriate criteria?"
> - id: RB-3.4; locator: Domain 3; role: signalling question; note: 
> "Were efforts made to minimise error in risk of bias assessment?"
> - id: RB-3.5; locator: Domain 3; role: signalling question; note: 
> "Did the synthesis include all studies that it should?"
> - id: RB-4.1; locator: Domain 4; role: signalling question; note: 
> "Were all pre-defined analyses reported or departures explained?"
> - id: RB-4.2; locator: Domain 4; role: signalling question; note: 
> "Was the synthesis appropriate given the nature and similarity in the research questions, study designs and outcomes across included studies?"
> - id: RB-4.3; locator: Domain 4; role: signalling question; note: 
> "Was between-study variation (heterogeneity) minimal or addressed in the synthesis?"
> - id: RB-4.4; locator: Domain 4; role: signalling question; note: 
> "Were the findings robust, e.g. as demonstrated through funnel plot or sensitivity analyses?"
> - id: RB-4.5; locator: Domain 4; role: signalling question; note: 
> "Were biases in primary studies minimal or addressed in the synthesis?"
> - id: RB-4.6; locator: Domain 4; role: signalling question; note: 
> "Did the interpretation of findings address all of the concerns identified in Domains 1 to 4?"
> - id: RB-A; locator: Phase 3; role: signalling question; note: 
> "Was the relevance of identified studies to the review's research question appropriately considered?"
> - id: RB-B; locator: Phase 3; role: signalling question; note: 
> "Did the reviewers avoid emphasizing results on the basis of their statistical significance?"
> - id: RB-C; locator: Phase 3; role: signalling question; note: 

### ROBIS-guidance (sha256 d699009192cd66a26737c47de71fa24c3cd0d9fa306d9908f20a58aaab62c365)
> "If the answers to all signalling questions for a domain are "Yes" or "Probably Yes", then level of concern can be judged as low. If any signalling question is answered "No" or "Probably No", potential for concern about bias exists."
> - id: RB-K1; locator: section on rating, before Domain 1; role: rating rule; note: 
> "The "No Information" category should be used only when insufficient data are reported to permit a judgment."
> - id: RB-K2; locator: section on rating, before Domain 1; role: rating rule; note: 
> "ROBIS users are likely to need both subject content and methodological expertise to complete an assessment."
> - id: RB-K3; locator: section on rating, before Domain 1; role: caveat; note: 
> "By recording the information used to reach the judgment (support for judgment), we aim to make the rating transparent and, where necessary, facilitate discussion among review authors completing assessments independently."
> - id: RB-K4; locator: section on rating, before Domain 1; role: caveat; note: the tool expects more than one assessor
> "Ideally this should be done independently but extraction by one reviewer and detailed checking by a second reviewer is also acceptable."
> - id: RB-G3.1; locator: Table 9, question 3.1; role: guidance; note: 
> "Checking should involve the second reviewer reading the paper in detail to not only check the extracted data for accuracy but also to ensure that no relevant information was missed."
> - id: RB-G3.1b; locator: Table 9, question 3.1; role: guidance; note: 
> "The assessor then needs to judge whether the criteria assessed were likely to identify potential sources of bias in the primary studies, given their study design."
> - id: RB-G3.4; locator: Table 9, question 3.4; role: guidance; note: 
> "As with data collection, risk of bias assessment should involve at least two reviewers."
> - id: RB-G3.5; locator: Table 9, question 3.5; role: guidance; note: 
> "If one or more concerns were identified for any of the previous domains, but these were appropriately considered when interpreting results and drawing conclusions, then this may also be rated as "Yes" and, depending on the rating of the other signalling questions, the review may still be rated as "Low risk of bias"."
> - id: RB-P3a; locator: Phase 3 text; role: guidance; note: 

## Criticality pass iv quotes (severe testing: Mayo), 2026-10-12

Purpose: the statements of the severity requirement applied in [`../criticality/severe-testing-2026-10-12.md`](../criticality/severe-testing-2026-10-12.md), and the passages that pass relies on for how severity differs from long-run performance, from Popper and from probabilist (Bayesian and likelihood) accounts. These are method texts, not sources for any claim file; role codes S/C/N/K do not apply and the role field says what the line is used for. Fetched 2026-10-12 about 23:38 to 23:45 UTC into `sources/raw/crit4-severe-testing-2026-10-12/` (gitignored), one directory per file. All 27 quotes were machine-checked as exact substrings of the extracted text after whitespace, curly-quote and typographic-ligature (fi, fl, ff, ffi, ffl) normalisation, 0 misses; the quotes below are printed in the normalised form. `x0` is the papers' x with subscript 0. Mayo 2018 (the book) was not obtained: the two `MayoBlog` entries are the author's own posts of notes and an excerpt from it, and are quoted as such.

### MayoSpanos2006 (sha256 2e7681ae648c6dbdec3e183b3767820fb5b1d545cd29e83bb7272773cc330b71)
> "A statistical hypothesis H passes a severe test T with data x0 if, (S-1) x0 agrees with H, and (S-2) with very high probability, test T would have produced a result that accords less well with H than x0 does, if H were false."
> - id: SV-MS1; locator: p.329 (section 1); role: definition; note: conditions (S-1) and (S-2); footnote 4 gives the equivalent low-probability form
> "The severity function has three arguments: a test, an outcome or result, and an inference or a claim."
> - id: SV-MS2; locator: p.329; role: definition; note: severity is of a test, an outcome and a claim together
> "the severity evaluation must be sensitive to the particular outcome x0; it must be a post-data assessment."
> - id: SV-MS3; locator: p.330, item (c); role: definition; note: assessed after the data
> "the guide for evaluating, and possibly adjusting, error probabilities (e.g., in multiple hypothesis testing, in data mining) is whether the probativeness is altered with respect to the particular error of interest"
> - id: SV-MS4; locator: p.330; role: selection effects; note: what matters about data-dependent choices is whether they alter probativeness
> "we will also suggest how the idea may be generalized to inferring the presence of 'an error' or flaw, very generally conceived."
> - id: SV-MS5; locator: p.329; role: scope of the concept; note: the authors allow an informal use beyond parametric discrepancies

### MayoSpanos2011 (sha256 6930621e7584961503b032725320b4f447e06c07657786804a23cc0f701ce6d2)
> "Severity Principle (weak). Data x0 (produced by process G) do not provide good evidence for hypothesis H if x0 results from a test procedure with a very low probability or capacity of having uncovered the falsity of H, even if H is incorrect."
> - id: SV-ES1; locator: section 1.3, p.162 (pages of this source are inferred from its running heads); role: principle, weak; note: the negative form
> "Severity Principle (full). Data x0 (produced by process G) provides good evidence for hypothesis H (just) to the extent that test T severely passes H with x0"
> - id: SV-ES2; locator: section 1.3, p.162; role: principle, full; note: the positive form
> "The onus is on the person claiming to have evidence for H to show that they are not guilty of at least so egregious a lack of severity."
> - id: SV-ES3; locator: section 1.3, p.162; role: burden; note: who must show severity
> "were George to have gained δ pounds or more (i.e., were H false), then this method would almost certainly have detected this."
> - id: SV-ES4; locator: section 1.3, p.163; role: example; note: calibration on known weights: the instrument detects a known difference
> "It requires being very specific about which inference is thereby warranted"
> - id: SV-ES5; locator: section 1.3, p.163-164; role: scope; note: severity is for a specific inference
> "what we are calling the error-statistical philosophy goes beyond falsificationism, of both the Popperian and Fisherian varieties, most notably in its consideration of what positive inferences are licensed when data do not falsify but rather accord with a hypothesis or claim."
> - id: SV-ES6; locator: section 1.1, "Objectivity in error statistics", p.158; role: contrast: Popper; note: positive inferences from passing results
> "The reliability of the rule used to infer H is at most a necessary and not a sufficient condition to warrant inferring H."
> - id: SV-ES7; locator: section 1.3, p.163-164; role: contrast: performance; note: long-run reliability is not enough

### MayoBlog2018 (sha256 bc118ed2ae9661fef96ad2b67d31e2488a6135926ab94657c89150c65535783d)
> "severity requirement (weak): One does not have evidence for a claim if little if anything has been done to rule out ways the claim may be false."
> - id: SV-B1a; locator: post body, "Notes from Section1.1 Severity Requirement: Bad Evidence, No Test (BENT)" (Mayo 2018 section 1.1, as posted by the author); role: principle, weak; note: first sentence
> "If data x agree with a claim C but the method used is practically guaranteed to find such agreement, and had little or no capability of finding flaws with C even if they exist, then we have bad evidence, no test (BENT)."
> - id: SV-B1b; locator: same place, next sentence; role: principle, weak; BENT; note: source of the label BENT
> "a difference between finding H poorly tested by data x, and finding x renders H improbable – in any of the many senses the latter takes on."
> - id: SV-B2; locator: post body, notes from Section 1.1; role: contrast: probabilism; note: poorly tested is not the same as improbable

### MayoBlog2019 (sha256 da8d10b8bbb2bba1f1f7c30955f7b3e32d4c3d572769077d93437d7c20e0f867)
> "Severity (strong): We have evidence for a claim C just to the extent it survives a stringent scrutiny. If C passes a test that was highly capable of finding flaws or discrepancies from C, and yet none or few are found, then the passing result, x, is evidence for C."
> - id: SV-B3; locator: post body, excerpt of Mayo 2018 section 1.2; role: principle, strong; note: 
> "The weakest version of the severity requirement (Section 1.1), in the sense of easiest to justify, is negative, warning us when BENT data are at hand, and a surprising amount of mileage may be had from that negative principle alone."
> - id: SV-B4; locator: post body, excerpt of Mayo 2018 section 1.2; role: principle, weak; note: 
> "It is not probabilism or performance we seek to quantify, but probativeness."
> - id: SV-B5; locator: post body, excerpt of Mayo 2018 section 1.2; role: contrast; note: 
> "He shoots all his bullets any old way into the side of a barn and then paints a bull's-eye in spots where the bullet holes are clustered. This fails utterly to severely test his marksmanship ability."
> - id: SV-B6; locator: post body, excerpt of Mayo 2018 section 1.2; role: example; note: criterion fitted after the data (Texas marksman)
> "With probabilism, one has evidence for a claim to the extent that it's probable in some sense, or gets a probability boost, or is comparatively more likely than some other claim."
> - id: SV-B7; locator: comment thread, Mayo reply to "Rick"; role: contrast: Bayesian and likelihood accounts; note: a comment by the author, not book text
> "To block BENT cases requires considering error probabilities of methods and these go beyond likelihoods."
> - id: SV-B8; locator: comment thread, Mayo reply to "Rick"; role: contrast: likelihood accounts; note: a comment by the author, not book text

### MayoHand2022 (sha256 24cb0059688deac275eb9ec89eeb6c5d493d113ed3613786fa0b6cf462c98cf0)
> "Minimal requirement for evidence: We have evidence for H only if H passes a test that probably would have found evidence of flaws in H, if they are present."
> - id: SV-MH1; locator: section "Performance vs probativeness" (full-text XML; no page numbers); role: principle, minimal; note: 
> "In our view, a probative test will generally involve combining several subsidiary tests, deliberately designed to unearth different flaws."
> - id: SV-MH2; locator: section "Performance vs probativeness"; role: design; note: several subsidiary tests aimed at different flaws
> "for a given test of H it is essential to specify in advance at least some outcomes that will not be allowed to count in favor of H."
> - id: SV-MH3; locator: section "A central function of statistics in science is undermined"; role: design; note: outcomes that count against must be named in advance
> "impressive-looking results are easy to achieve if one can ignore unwelcome results, alter what is being tested post-data, or exploit a variety of sources of researcher flexibility (e.g., exclusion criteria, data dredging, stopping rules)."
> - id: SV-MH4; locator: section "P-values are uninterpretable if there has been p-hacking, data-dredging or a variety of biasing selection effects"; role: selection effects; note: flexibility destroys the error probability
> "Good long-run performance is a necessary but not a sufficient condition for a test to calibrate probativeness."
> - id: SV-MH5; locator: section "Performance vs probativeness"; role: contrast: performance; note: 

### MayoCox2006 (sha256 e8389c2fd3418add598740a2952470595a11b2c90b2ee0fdfaa26aa0ae40a3a4)
> "only if there is a high probability the test would have given a worse fit with H0 (i.e., smaller p value) were a discrepancy δ to exist."
> - id: SV-MC1; locator: p.84, FEV(ii) (second half; the sentence starts on p.83); role: principle for non-rejection; note: a passing result is evidence of no discrepancy only if the test could have shown one

## Criticality pass v quotes (argument structure: Toulmin, Walton's schemes, pragma-dialectics), 2026-10-12

Purpose: the definitions, argumentation schemes, critical questions and discussion rules applied in [`../criticality/argument-structure-2026-10-12.md`](../criticality/argument-structure-2026-10-12.md). These are method texts, not sources for any claim file; role codes S/C/N/K do not apply and the role field says what the line is used for. Fetched 2026-10-13 about 00:16 to 01:05 UTC (2026-10-12 evening, -06:00) into `sources/raw/crit5-argument-structure-2026-10-12/` (gitignored), one directory per file. All 95 quotes were machine-checked as substrings of the extracted text after whitespace, curly-quote and ligature normalisation, with line-end hyphens tried three ways (kept with the space, joined, removed); 0 misses. **What is and is not primary:** Walton 2001, Walton 2005, Macagno, Walton and Reed 2017, van Eemeren and Verheij 2017 and the two van Eemeren, Garssen and Meuffels texts are by the frameworks' own authors. The Stanford Encyclopedia entries are secondary. The three Wikipedia pages (raw wikitext, markup stripped for the check), the Carneades scheme file and the Calvo Figueras and Agerri templates are tertiary or derived: they restate Walton, Reed and Macagno 2008, Toulmin 1958 and van Eemeren and Grootendorst's rules, **none of which was obtained**, and their wording was not checked against those books. Quote ids `AT-nn` (argumentation theory) are not finding ids; the pass's findings are `AS-nn`.


### EemerenVerheij2017 (sha256 bb2184b6f6d2173aa22adcdec952cb27dcf8a46042d3a8358ee6e00f56884be6)
> "The validity of argumentation is in his view primarily determined by the degree to which the (usually implicit) warrant that connects the data advanced in the argumentation with the claim at issue is acceptable—or, if challenged, can be made acceptable by a backing."
> - id: AT-01; locator: section 2 (issue p.2109 by running head); role: Toulmin: warrant and backing; note: what the warrant does; it is 'usually implicit'
> "What kind of backing may be required in a particular case depends on the field to which the standpoint at issue belongs."
> - id: AT-02; locator: section 2; role: Toulmin: field dependence; note: backing differs by field
> "view argumentation as part of a discourse aimed at resolving a difference of opinion on the merits by methodically testing the acceptability of the standpoints at issue."
> - id: AT-03; locator: section 2 (pp.2113-2114); role: pragma-dialectics: aim; note: resolution on the merits by testing standpoints; the sentence begins 'As van Eemeren and Grootendorst [1984] explain, pragma-dialecticians'
> "Any violation of any of the rules amounts to making an argumentative move that is an impediment to the resolution of a difference of opinion on the merits and is therefore fallacious"
> - id: AT-04; locator: section 2 (p.2114); role: pragma-dialectics: fallacy as rule violation; note: any violation is a fallacy

### WP-Toulmin (sha256 402b7975a4b6f9d52bfabf98d7fc5b02d3bf4eb3fe368ae369030381fbe6e336)
> "A conclusion whose merit must be established."
> - id: AT-05; locator: section 'The Toulmin model of argument'; role: Toulmin: claim; note: tertiary source; Toulmin 1958 not obtained
> "A fact one appeals to as a foundation for the claim."
> - id: AT-06; locator: same; role: Toulmin: ground (data); note: tertiary
> "A statement authorizing movement from the ground to the claim."
> - id: AT-07; locator: same; role: Toulmin: warrant; note: tertiary
> "Credentials designed to certify the statement expressed in the warrant; backing must be introduced when the warrant itself is not convincing enough to the readers or the listeners."
> - id: AT-08; locator: same; role: Toulmin: backing; note: tertiary
> "Statements recognizing the restrictions which may legitimately be applied to the claim."
> - id: AT-09; locator: same; role: Toulmin: rebuttal; note: tertiary
> "Words or phrases expressing the speaker's degree of force or certainty concerning the claim."
> - id: AT-10; locator: same; role: Toulmin: qualifier; note: tertiary
> "The first three elements, claim, ground, and warrant, are considered as the essential components of practical arguments, while the second triad, qualifier, backing, and rebuttal, may not be needed in some arguments."
> - id: AT-11; locator: same; role: Toulmin: which parts are essential; note: tertiary

### SEP-InformalLogic (sha256 df35565a99bbccba84bc737464a2d05c358cc6b1152febfba43cd5f867014247)
> "Sometimes it is expanded by defining an argument as a premise-conclusion complex which is directed at an audience, or backed by a warrant, or provided as an answer to a questioning opponent."
> - id: AT-12; locator: section 2.1; role: argument and warrant; note: informal logic allows a warrant or an opponent as part of an argument
> "The most common approach to argument schemes combines a pattern of argument with a set of “critical questions” with which it is associated."
> - id: AT-13; locator: section 4.4 (argument schemes); role: scheme = pattern + critical questions; note: 
> "A is an authority in domain D. A says that T is true. T is within D. (Therefore) T is true."
> - id: AT-14; locator: section 4.4; role: scheme: argument from authority; note: SEP's wording of the scheme
> "1. How credible is A? 2. Is A an authority in domain D? 3. What did A assert that implies T? 4. Is A someone who can be trusted? 5. Is T consistent with what other experts assert? 6. Is A’s assertion of T based on evidence?"
> - id: AT-15; locator: section 4.4; role: critical questions: authority; note: six questions
> "The critical question approach to schemes suggests that a credible argument from authority must include acceptable premises of the form outlined in the definition of the scheme, and is valid if it can be backed by answers to the scheme’s critical questions."
> - id: AT-16; locator: section 4.4; role: how critical questions bear on strength; note: 
> "The basic question that must be asked is whether there is a good reason why the arguer’s views should not be taken seriously — a question that subsumes the more specific questions whether they have repeatedly shown poor judgment, are biased, lack expertise in the area in question, or are for some other reason an arguer who should not be listened to."
> - id: AT-17; locator: section 4.4; role: ad hominem as a scheme; its basic question; note: 

### SEP-Fallacies (sha256 45467658874e59756cafdde7e0efcaba81d7f7312ed7804b5560ac6c81db4e2f)
> "Schemes do not identify fallacies but rather argument kinds that are sometimes used fairly, and, other times, fallaciously. With each kind of scheme is associated a set of critical questions which guide us in deciding whether a given use of an argument is correct, weak or fallacious."
> - id: AT-18; locator: section 3.5 (Walton); role: schemes are not fallacies; note: 
> "If one of the questions cannot be answered clearly this is an indication that the argument is weak, and answering No to either of the two questions cancels the presumption for the conclusion"
> - id: AT-19; locator: section 3.5; role: scoring basis: unanswered question = weak; No = presumption cancelled; note: the passage is about the two questions of the expert scheme
> "A set of ten rules has been proposed as constitutive of the critical-discussion ideal, and the proponents of the theory believe that rational arguers would accept them."
> - id: AT-20; locator: section 3.4 (pragma-dialectics); role: ten rules; note: 
> "at the confrontation stage there is a rule which says one may not prevent the other party from expressing their view; for the argumentation stage there is a rule which requires argumentation to be logically strong and in accord with one or another of three general argumentation schemes; at the closing stage there is a rule that the participants themselves are to decide which party was successful based on the quality of the argumentation they have made: if the proponent carries the day, the opponent should acknowledge it, and vice versa."
> - id: AT-21; locator: section 3.4; role: rules by stage; note: freedom, validity/scheme, closure in SEP's paraphrase
> "evading the burden of proof which breaks the rule that you must defend your standpoint if asked to do so"
> - id: AT-22; locator: section 3.4; role: burden of proof rule; note: 
> "equivocation is a violation of the rule that formulations in arguments must be clear and unambiguous; post hoc ergo propter hoc violates the rule that arguments must be instances of schemes correctly applied."
> - id: AT-23; locator: section 3.4; role: usage rule and argument scheme rule; note: 
> "the Pragma-dialectical rules of a critical discussion are not just rules of logic or epistemology, but rules of conduct for rational discussants"
> - id: AT-24; locator: section 3.4; role: status of the rules; note: rules of conduct, not of logic
> "However, the inability of an opponent to produce a better argument is not sufficient reason to think the proponent’s argument must be accepted. Modern versions of this kind of argument take it as a fallacy to infer a proposition to be true because there is no evidence against it"
> - id: AT-25; locator: section 2.3 (Locke); role: argument from ignorance; note: 
> "Similarly, when there is controversy, and authorities are divided, it is an error to base one’s view on the authority of just some of them."
> - id: AT-26; locator: section 1 (core fallacies, item 9); role: appeal to authority where authorities are divided; note: 
> "The fallacy ad populum is similar to the ad verecundiam, the difference being that the source appealed to is popular opinion, or common knowledge, rather than a specified authority."
> - id: AT-27; locator: section 1 (item 10); role: ad populum; note: 
> "straw man fallacies happen when someone in the course of argumentation inaccurately and unfavourable distorts a ground-level argument in an attempt to refute it or discredit its source."
> - id: AT-28; locator: section 4 (Aikin and Casey); role: straw man; note: 'unfavourable' is the entry's wording
> "In the case of bothsiderism, there are conflicting arguments each drawing on prima facie evidence. This can lead to the meta-argument that the truth lies somewhere in the middle between the opposed ground-level conclusions. This is considered a fallacy because purported contrary evidence noticed at the meta-level is insufficient reason to abandon both the ground-level conclusions in favour of a compromise."
> - id: AT-29; locator: section 4; role: false balance ('bothsiderism'); note: 
> "This fallacy ascribes a causal relationship between two states or events on the basis of temporal succession."
> - id: AT-30; locator: section 1 (item 7); role: post hoc; note: 

### SEP-Argument (sha256 4ea18363951c1381cd10a2cc615f9509cd9297957f2e30b85e6ca067df9287d0)
> "Another leading author in argumentation theory is Douglas Walton, who pioneered the argument schemes approach to argumentation that borrows tools from formal logic but expands them so as to treat a wider range of arguments than those covered by traditional logical systems"
> - id: AT-31; locator: section 4 (argumentation theory); role: standing of Walton, Reed and Macagno 2008; note: 

### Walton2001 (sha256 f7e9ce6edee1cbc33fea3b13f1465c334dc34fcd4be8da3bcd519c46992ef822)
> "Major Premise: Source E is an expert in subject domain S containing proposition A. Minor Premise: E asserts that proposition A (in domain S) is true (false). Conclusion: A may plausibly be taken to be true (false)."
> - id: AT-32; locator: p.158; role: scheme: argument from expert opinion; note: Walton's own wording, citing Walton 1997 p.210
> "1. Expertise Question: How credible is E as an expert source? 2. Field Question: Is E an expert in the field that A is in? 3. Opinion Question: What did E assert that implies A? 4. Trustworthiness Question: Is E personally reliable as a source? 5. Consistency Question: Is A consistent with what other experts assert? 6. Backup Evidence Question: Is A's assertion based on evidence?"
> - id: AT-33; locator: p.158; role: critical questions: expert opinion; note: six, citing Walton 1997 p.223
> "An example of argument from sign is the following inference: here are some bear tracks in the snow, therefore a bear recently passed this way"
> - id: AT-34; locator: p.160; role: argument from sign; note: example; Walton classes sign as abductive
> "F is a finding or given set of facts. E is a satisfactory explanation of F. No alternative explanation E' given so far is as satisfactory as E. Therefore, E is plausible, as a hypothesis."
> - id: AT-35; locator: p.162; role: scheme: abductive argument; note: 
> "CQ 1: How satisfactory is E itself as an explanation of F, apart from the alternative explanations available so far in the dialogue? CQ2: How much better an explanation is E than the alternative explanations available so far in the dialogue? CQ3: How far has the dialogue progressed? If the dialogue is an inquiry, how thorough has the search been in the investigation of the case? CQ4: Would it be better to continue the dialogue further, instead of drawing a conclusion at this point?"
> - id: AT-36; locator: p.162; role: critical questions: abduction; note: four

### Walton2005 (sha256 4219210c790e0fdae5f8e34dfdfff8b9246bd5a3c3b7306f4c12d79e246b29e1)
> "If a respondent asks any one of the six appropriate critical questions, a burden of proof is shifted back onto the proponent of the argument to provide a satisfactory answer to the question. If she fails to give such an answer, the appeal to expert opinion loses its previous weight of support."
> - id: AT-37; locator: p.3 (section 2); role: what asking a critical question does; note: burden shifts back to the proponent

### MacagnoWaltonReed2017 (sha256 bb2184b6f6d2173aa22adcdec952cb27dcf8a46042d3a8358ee6e00f56884be6)
> "every scheme has a corresponding set of critical questions, representing its defeasibility conditions and the possible weak points that the interlocutor can use to question the argument and evaluate its strength."
> - id: AT-38; locator: section 1 (p.2494); role: critical questions = defeasibility conditions; note: 
> "Major premise Generally, if A occurs, then B will (might) occur. Minor premise In this case, A occurs (might occur). Conclusion Therefore, in this case B will (might) occur)."
> - id: AT-39; locator: Table 1 (p.2495); role: scheme: argument from cause to effect; note: citing Walton et al. 2008 p.328; the stray bracket is in the source
> "CQ1 What other goals do I have that should be considered that might conflict with G? CQ2 What alternative actions to my bringing about A that would also bring about G should be considered? CQ3 Among bringing about A and these alternative actions, which is arguably the most efficient? CQ4 What grounds are there for arguing that it is practically possible for me to bring about A? CQ5 What consequences of my bringing about A should also be taken into account?"
> - id: AT-40; locator: section 5 (after Table 12); role: critical questions: practical reasoning; note: five; the scheme itself (Table 12: 'I have a goal G' / carrying out A is a means to realise G / therefore I ought to carry out A) is laid out in two columns and is paraphrased here, not quoted
> "According to the scheme for argument from positive consequences, known or estimated consequences that have a positive value for the agent are cited as a reason, or set of reasons, supporting the carrying out of the action initially considered."
> - id: AT-41; locator: section 5 (before Table 13); role: argument from consequences; note: prose statement of the positive form; Tables 13 and 14 give 'If A is brought about, good (bad) consequences will plausibly occur / Therefore A should (should not) be brought about' in two columns, paraphrased here

### CalvoFigueras2024 (sha256 b92becf594ce00ad8464b79cfb3fe05acbba39172763ebf4c5703b19de508e78)
> "templates of argumentation schemes and critical questions defined in Walton et al. (2008)"
> - id: AT-42; locator: Figure 1 caption; role: provenance of the templates; note: secondary source: templates built from Walton et al. 2008, not the book's wording checked against the book
> "Is there a proved relation between ‘< eventB >’ and ‘< eventA >’?"
> - id: AT-43; locator: Appendix C table; role: critical questions: argument from sign; note: placeholders as extracted
> "Are there any events other than < eventB > that would more reliably account for < eventA >?"
> - id: AT-44; locator: Appendix C table; role: critical questions: argument from sign; note: 
> "Is < subjecta > actually a typical case of other < subjectx > that < f eatF >? How widely applicable is the"
> - id: AT-45; locator: Appendix C table; role: critical questions: argument from example; note: 'f eatF' is a text-extraction artefact for featF
> "Are there special circumstances pertaining to < subjecta > that undermine its generalisability to other < subjectx >"
> - id: AT-46; locator: Appendix C table; role: critical questions: argument from example; note: 
> "Is < subjecta > in a position to know whether < eventA >?"
> - id: AT-47; locator: Appendix C table; role: critical questions: position to know; note: 
> "Is < subjecta > an honest (trustworthy, reliable) source?"
> - id: AT-48; locator: Appendix C table; role: critical questions: position to know; note: 
> "Did < subjecta > assert that < eventA >?"
> - id: AT-49; locator: Appendix C table; role: critical questions: position to know; note: 
> "How strong is the generalisation that if < eventA > then < eventB >?"
> - id: AT-50; locator: Appendix C table; role: critical questions: cause to effect; note: 
> "Are there other factors in this particular case that could have interfered with the event of ‘< eventB >’?"
> - id: AT-51; locator: Appendix C table; role: critical questions: cause to effect; note: 
> "If < eventA >, will < eventB > occur? What evidence supports this claim? How likely are the consequences?"
> - id: AT-52; locator: Appendix C table; role: critical questions: consequences; note: 
> "What other consequences should also be taken into account if < neg > < eventA >?"
> - id: AT-53; locator: Appendix C table; role: critical questions: consequences; note: 
> "Are < C1 > and < C2 > similar in the respect cited?"
> - id: AT-54; locator: Appendix C table; role: critical questions: analogy; note: 
> "Are there differences between < C1 > and < C2 > that would tend to undermine the force of the similarity cited?"
> - id: AT-55; locator: Appendix C table; role: critical questions: analogy; note: 
> "Is there some other case that is also similar to < C1 >, but in which < eventA > is false?"
> - id: AT-56; locator: Appendix C table; role: critical questions: analogy; note: 
> "What evidence supports that < eventA > is generally accepted as true?"
> - id: AT-57; locator: Appendix C table; role: critical questions: popular opinion; note: 
> "Even if < eventA > is generally accepted as true, are there any good reasons for doubting that it is true?"
> - id: AT-58; locator: Appendix C table; role: critical questions: popular opinion; note: 
> "How does the allegation made affect the reliability of < subjecta >?"
> - id: AT-59; locator: Appendix C table; role: critical questions: generic ad hominem; note: 
> "Is the reliability of < subjecta > relevant in the current dialogue?"
> - id: AT-60; locator: Appendix C table; role: critical questions: generic ad hominem; note: 
> "What evidence is there that < subjecta > is < subjectx >?"
> - id: AT-61; locator: Appendix C table; role: critical questions: argument from bias; note: 

### WP-ArgScheme (sha256 3bdf6c3c2a7ccfde074aa6fc64fa5ed438217174b9434cb3f3c8593347efd9f1)
> "a is in a position to know whether A is true or false."
> - id: AT-62; locator: Overview, table 'Argument from position to know'; role: scheme: position to know; note: tertiary; cites Walton 2006
> "A may plausibly be taken to be true ([or] false)."
> - id: AT-63; locator: same table; role: scheme: position to know; note: tertiary
> "If A were true, then A would be known to be true."
> - id: AT-64; locator: section 'Argument from ignorance'; role: scheme: argument from ignorance; note: tertiary; cites Walton, Reed and Macagno 2008 p.327
> "It is not the case that A is known to be true."
> - id: AT-65; locator: same; role: scheme: argument from ignorance; note: tertiary
> "How far along has the search for evidence progressed?"
> - id: AT-66; locator: same; role: critical questions: ignorance; note: tertiary
> "Which side has the burden of proof in the dialogue as a whole? In other words, what is the ultimate probandum [claim that is to be proved] and who is supposed to prove it?"
> - id: AT-67; locator: same; role: critical questions: ignorance; note: tertiary
> "How strong does the proof need to be in order for this party to be successful in fulfilling the burden?"
> - id: AT-68; locator: same; role: critical questions: ignorance; note: tertiary

### Carneades-walton-yml (sha256 5f292cfef82ca8412560623466fd215480fcfa33b302bf6747a694bd8dd50977)
> "Events %s and %s are correlated."
> - id: AT-69; locator: language block; scheme `correlation_to_cause` (source field: Walton 1995 p.142); role: correlation to cause: premise, assumption, exception; note: a formalisation by the Carneades project of Walton, Reed and Macagno 2008; this string is the scheme's premise, and AT-70 and AT-71 are its assumption and exception
> "There exists a theory explaining how event %s causes event %s."
> - id: AT-70; locator: same; role: correlation to cause: assumption; note: 
> "Some other event causes both %s and %s."
> - id: AT-71; locator: same; role: correlation to cause: exception; note: 
> "There are relevant differences between case %s and the current case."
> - id: AT-72; locator: scheme `precedent` (source field: Walton 1995 p.148); role: precedent and analogy: exception; note: 
> "Rule %s is inapplicable in this case."
> - id: AT-73; locator: scheme `precedent`; role: precedent: exception; note: 
> "The truth of %s has not been sufficiently investigated."
> - id: AT-74; locator: scheme `ignorance` (source field: Walton 1995 p.150); role: ignorance: exception; note: 
> "%s is false in another case which is more on point than case %s."
> - id: AT-75; locator: scheme `analogy` (source field: Walton 2006 pp.96-97); role: analogy: exception; note: 
> "There exists a more coherent explanation than theory %s of observation %s."
> - id: AT-76; locator: scheme `abduction`; role: abduction: exception; note: 

### WP-PragmaDialectics (sha256 c4db03f3baa692d1f8a5626606df2ca8286d77f8e46708e9418a3a3501110484)
> "Parties must not prevent each other from advancing standpoints or from casting doubt on standpoints."
> - id: AT-77; locator: section 'Rules for critical discussion' (cites van Eemeren, Grootendorst and Snoeck Henkemans 2002 pp.182-183); role: rule 1, freedom; note: tertiary; numbering as in this list
> "A party that advances a standpoint is obliged to defend it if asked by the other party to do so."
> - id: AT-78; locator: same; role: rule 2, burden of proof; note: tertiary
> "A party's attack on a standpoint must relate to the standpoint that has indeed been advanced by the other party."
> - id: AT-79; locator: same; role: rule 3, standpoint; note: tertiary
> "A party may defend a standpoint only by advancing argumentation relating to that standpoint."
> - id: AT-80; locator: same; role: rule 4, relevance; note: tertiary
> "A party may not deny premise that he or she has left implicit or falsely present something as a premise that has been left unexpressed by the other party."
> - id: AT-81; locator: same; role: rule 5, unexpressed premise; note: tertiary; 'deny premise' is the page's wording
> "A party may not falsely present a premise as an accepted starting point nor deny a premise representing an accepted starting point."
> - id: AT-82; locator: same; role: rule 6, starting point; note: tertiary
> "A party may not regard a standpoint as conclusively defended if the defense does not take place by means of an appropriate argumentation scheme that is correctly applied."
> - id: AT-83; locator: same; role: rule 7 in this list, argument scheme; note: tertiary
> "A party may only use arguments in its argumentation that are logically valid or capable of being made logically valid by making explicit one or more unexpressed premises."
> - id: AT-84; locator: same; role: rule 8 in this list, validity; note: tertiary
> "A failed defense of a standpoint must result in the party that put forward the standpoint retracting it and a conclusive defense of the standpoint must result in the other party retracting its doubt about the standpoint."
> - id: AT-85; locator: same; role: rule 9, closure; note: tertiary
> "A party must not use formulations that are insufficiently clear or confusingly ambiguous and a party must interpret the other party's formulations as carefully and accurately as possible."
> - id: AT-86; locator: same; role: rule 10, usage; note: tertiary

### Hitchcock2003 (sha256 9d63419772e547c894a84e83b9dc11d6b35b797712656fffb2009c18f867de18)
> "A fallacy is a violation of one of the ten rules."
> - id: AT-87; locator: p.91; role: ten rules; fallacy; note: 
> "Parties must not prevent each other from advancing standpoints or casting doubt on standpoints"
> - id: AT-88; locator: p.92; role: rule 1 as quoted from van Eemeren (ed.) 2002, p.47 n.4; note: cross-check of AT-77
> "Parties must not use any formulations that are insufficiently clear or confusingly ambiguous, and they must interpret the formulations of the other party as carefully and accurately as possible."
> - id: AT-89; locator: p.106; role: rule 10 as quoted from the same note; note: cross-check of AT-86

### Weger1998 (sha256 913d9b55dac75ac699e49a2fca5e020342a07a6a56a51cd708ed5eaedb2c830a)
> "Rule five deals with the responsibility of arguers to accurately represent the expressed and unexpressed premises that each party is actually accountable for."
> - id: AT-90; locator: section 1; role: rule 5 paraphrased; note: 
> "The ninth rule necessitates that standpoints that are conclusively defeated or upon which doubt has been cast must be withdrawn."
> - id: AT-91; locator: section 1; role: rule 9 paraphrased; note: 

### EemerenGarssenMeuffels2002 (sha256 2cd8e6c132d99118bd1c7af756975a6369dbf0adb93b8bbb5663b33a28b3db03)
> "According to the rule for the confrontation stage (i.e. the freedom rule) the parties are not allowed to prevent each other from advancing standpoints or casting doubt on standpoints."
> - id: AT-92; locator: section 2; role: freedom rule, by the theory's authors; note: cross-check of AT-77

### EemerenGarssenMeuffels2012 (sha256 028f1b8df2ed76a94331ccb80d780f4454781933b0f64720f5620a6a8b83b244)
> "Any move that is an infringement of any of these rules, whichever party performs it and at whatever stage in the discussion, is a possible threat to the resolution of a difference of opinion on the merits and must therefore—and in this particular sense—be regarded as fallacious."
> - id: AT-93; locator: section 2; role: fallacy as rule violation, whichever party; note: 

### Visser2021 (sha256 0d2c597f84eb59d930c15e185054d3cd7abe794d89721c215ec2e081cc2a9b06)
> "divides schemes into three general categories: reasoning, source-based arguments, and applying rules to cases."
> - id: AT-94; locator: section 3.1; role: Walton's classification; note: 'byWalton' is as extracted

### HahnHornikx2016 (sha256 965a29439593ebb539ab28bddc78239223dce8677702b148a87e74f3ddeb4864)
> "in order to justify different argument schemes there must minimally be some consequential difference to either the basic inference or the critical questions."
> - id: AT-95; locator: section 5 (discussion); role: a criticism of scheme lists; note: used as a caution on counting by scheme
