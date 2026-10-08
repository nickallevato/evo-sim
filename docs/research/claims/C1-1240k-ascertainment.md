---
id: C1
title: "The 1240k capture panel is ascertained on present-day variable sites, so near-zero fixations (and zero new-mutation substitutions) are expected by design"
side: critic
branch: C
parent: C
edges: [{type: attacks, target: C}, {type: attacks, target: C6}]
load_bearing: false  # Does not bear on ROOT directly; it removes C and C6 as independent support. No published critic has made it (hierarchy note); it is the repo's formulation, from the literature below.
sourcing: firsthand
status: extracted
verdicts:
  internal: pending
  fidelity: accurate
  external: pending
---

## Statement (verbatim)
No published critic of Day was found making this point. The assertion is the repo's (R1 sources agent), and its premises are literature statements on how the panel was built:

> "The targeted sites include nearly all SNPs on the Affymetrix Human Origins and Illumina 610-Quad arrays, 49,711 SNPs on chromosome X and 32,681 on chromosome Y, and 47,384 SNPs with evidence of functional importance."

Source: [Mathieson et al. 2015, Nature 528:499](https://pmc.ncbi.nlm.nih.gov/articles/PMC4918750/), main text, first results paragraph; checked against `sources/raw/sources/txt/Mathieson2015.txt`.

> "we used three sets of oligonucleotide probes that cover about two million sites that are single nucleotide polymorphisms (SNPs) in present-day humans"

Source: [Fu et al. 2015, Nature 524:216](https://pmc.ncbi.nlm.nih.gov/articles/PMC4537386/), Results (Oase 1 capture).

> "(discovered as heterozygous in a Yoruba male: HGDP00927)"

Source: [Haak et al. 2015, Nature 522:207](https://pmc.ncbi.nlm.nih.gov/articles/PMC5048219/), Methods, description of the 390k capture design, the "Yoruba SNPs" class (124,106 SNPs; a "San SNPs" class of 146,135 is defined the same way from a San male); checked against the user-downloaded `sources/raw/sources/manual/Haak2015.txt`.

> "We process these bams to produce genotypes at a set of about 1.23 million SNPs that have been assayed for nearly all published individuals with ancient DNA data."

Source: [Mallick et al. 2024, Sci Data 11:182](https://pmc.ncbi.nlm.nih.gov/articles/PMC10858950/), Main text, "Data processing".

Selection-scan filter in Mathieson 2015 (Methods, selection analysis):
> "We removed SNPs that were monomorphic in all four of these modern populations"

## Formal statement
Let S be the panel (sites chosen because they were polymorphic in a discovery set D of present-day individuals or arrays: Yoruba/San single-individual heterozygotes, Human Origins, 610-Quad, plus functional SNPs). Two separate consequences:

1. New-mutation substitutions are mostly absent from S. A mutation that arose and fixed in Europe within the window would not have been polymorphic in D, so it is not a panel site. The panel can register frequency changes of standing variants and cannot register most substitutions along a lineage. The quantity Day compares (about 20 million substitutions required; 15,556 expected in 7,000 y) is a substitution count over the whole genome.
   derived: genome-wide neutral substitutions in 350 generations at k = mu = 1.2e-8 (`mutation.mu_per_site_per_gen.pedigree_human`) x 3.1e9 sites = 37.2 per generation x 350 = 13,020 (haploid-lineage count; Day's 15,556 is the same order). Panel fraction = 1,143,671 / 3.1e9 = 3.7e-4, so a uniform sample would give 4.8 events even if every panel site could register a new substitution (derived: 13,020 x 3.69e-4).
2. Direction of bias for intermediate-frequency completions is unsettled. The African-male discovery step selects alleles polymorphic in Africans, which are mostly old, intermediate-frequency variants in Europeans too. That enriches the panel for the very class (intermediate start) in which completions could be seen (Day's reply, C1a). Against this, sites already near-fixed in Europeans are inflated among "newly 100%" (17,806 of 1,143,671 at 90-99% start, Z23046531 Table 3).

Panel size parameters: 1,233,013 SNPs (AADR), 1,143,671 autosomal after Day's filter.

## Assumptions
- Stated: (literature) panel targets are SNPs "in present-day humans".
- Implicit: that Day's expectation of ~15,500 (or Z18525185's 630) is meant to be read against panel counts; that new substitutions have the same chance of being on the panel as any site (they do not); that array content discovered from European samples (610-Quad, in part) does not offset the African-male discovery design.

## Responses
- Against: Day, anticipating it in Z18525185 §9.4 (C1a): the bias "would favor detecting recent fixations, not obscure them".
- In support: none published.
- Weaknesses in the responses: C1a addresses only the intermediate-frequency class, not the new-substitution class (point 1), and it asserts the direction without a simulation. The repo's point 1 depends on a rough uniform-sampling scaling.

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Mathieson 2015 | targeted set built from array SNPs and functional SNPs (quote above) | accurate (fidelity ledger: "Mathieson 2015 / Fu 2015 / Mallick 2024 ... verified") |
| Fu 2015 | probes cover SNPs "in present-day humans" | accurate |
| Haak 2015 | "Yoruba SNPs" and "San SNPs" discovered as heterozygous in one male each; "Compatibility SNPs" from overlapping arrays | accurate; adds that discovery was in African individuals, not Europeans (not in the ledger yet) |
| Mallick 2024 | 1.23 million SNP target set | accurate |

## Pre-registered prediction
- Under the claimant's model (critic): (a) new-mutation substitutions in the 350-generation window are registered on panel sites at far below the genome-wide rate (order 0-5 per 1.14M sites under uniform sampling, probably less because new mutations are not in S); (b) for standing variants, neutral completions from a 50-90% start are ~0 at Ne ~1e4, so the observed 1 and 3 are noise or admixture.
- Under the opposing model (Day, C1a): ascertainment on present-day polymorphism raises the chance of seeing an intermediate-to-fixed transition, so the observed near-zero is not an artefact of design.
- Result that would change a verdict: a simulation that ascertains sites exactly as the panel did (African-male heterozygosity plus array SNPs) and shows (i) a non-negligible expected count of panel-registered new substitutions (verdict on point 1 reverses) or (ii) that the ascertained panel increases the neutral expected count of 50-90% completions above ~0.1 (verdict on point 2 reverses toward C1a).

## Check
Script: none yet (spec: `research/checks/c1_ascertainment_sim.py`, planned). Spec: msprime baseline only for the discovery sample (README rule 6); forward Wright-Fisher for the 350-generation window. Steps: (1) simulate a pre-window population of Ne = 1e4 with mutation; (2) draw discovery sets D mimicking one Yoruba male, one San male and a 2,345-person array panel; keep sites polymorphic in D; (3) run 350 generations forward with new mutations arising genome-wide; (4) count, on the ascertained panel versus genome-wide, (a) substitutions of mutations that arose in-window and (b) completions of standing variants by start-frequency band; (5) repeat at Ne = 2e3 and with a 2:1 growth. Report both counts and the panel/genome ratio. · Result: not run · Review: pending

## Simulator variables implied
Discovery sample (size, ancestry), MAF cut-off for panel inclusion, panel fraction of genome, window length, standing versus new variation.
