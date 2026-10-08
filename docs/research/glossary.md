# Glossary: Pinned Definitions

Every claim file must say which sense of each term it uses. Many disputes in this debate come from the two sides using one word in different senses.

## Fixation and divergence
| Term | Definition here | Common confusion |
|---|---|---|
| **fixation** (in a species) | An allele reaches frequency 1 in one population. | Treated as the same thing as a fixed difference. |
| **fixed difference** | A site where two lineages carry different alleles, each fixed in its own lineage. | Human–chimp differences split across **both** lineages, so the per-lineage count is about half the total. Divergence measured from one genome per species also includes polymorphism. |
| **substitution** | One fixation event of a new mutation along a lineage. | — |
| **SNV / indel / SV / bp** | SNV: one base changed. Indel: a small insertion or deletion, one mutational *event* that may span many bp. SV: a structural variant (inversion, duplication, large deletion), also one event. bp: base pairs affected. | Counting bp affected as if each were a separate fixation. |

## Rates and times
| Term | Definition | Common confusion |
|---|---|---|
| **throughput, k** | Substitutions per generation along a lineage, measured at steady state or over a window. | Treated as 1 / latency. |
| **latency, t_fix** | Generations for one allele to go from arising to fixation, given that it fixes. | Dividing elapsed time by latency treats fixations as strictly serial. |
| **generations per fixation, G_f** | Observed window length ÷ fixations observed in it. This is an inverse throughput. | Read as a latency. |
| **μ** | Mutation rate. Always state per site or per genome, and per generation or per year. | — |

## Population size
| Term | Definition | Common confusion |
|---|---|---|
| **N** | Census number of diploid individuals; 2N gene copies. | Mixing N with 2N. Mixing census N with Nₑ. |
| **Nₑ** | Effective size: the size of an ideal Wright–Fisher population with the same drift (state which Nₑ: variance, inbreeding or coalescent). | Neutral fixation probability is **1/(2N)**, the starting frequency, not 1/(2Nₑ). Nₑ governs the timescale of drift. |
| **ancestral Nₑ** | Nₑ of the human–chimp common ancestor (≈5×10⁴–10⁵, to verify). | Using the modern human Nₑ (≈10⁴) instead. |
| **Vₖ** | Variance in offspring number. Wright: Nₑ ≈ (4N−2)/(Vₖ+2). | — |

## Selection
| Term | Definition |
|---|---|
| **s** | Selection coefficient. State its sign, whether it is a per-locus or per-trait estimate, and whether it is a mean or a distribution. |
| **hard vs soft selection** | Hard: selective deaths are added on top of other deaths. Soft: they replace deaths that would have happened anyway. Haldane's cost of selection depends on this distinction. |
| **hitchhiking** | A neutral allele that fixes because it is linked to a sweeping beneficial allele. |
| **clonal interference** | In asexual populations, competing beneficial lineages slow one another's fixation. |

## LTEE-specific
| Term | Definition |
|---|---|
| **fixed (≥95% rule)** | Allele at ≥95% of sequencing reads. This overcounts when coexisting lineages are present (Good 2017). |
| **fixed (lineage-aware)** | Allele fixed in the whole population according to Good 2017's lineage calls. Day's Zenodo 23105291 uses this. |
| **mutator / hypermutator** | Lineage with an elevated mutation rate (mutS/mutL/mutT etc.). Its counts are reported separately. |

## Day-specific terms
- MITTENS
- d (selective turnover coefficient)
- Bernoulli Barrier
- Hard Limits
- Darwillion
- Bio-Cycle model
- Relictation
- "pipeline"

Each term is defined only by quoting its source; see `claims/`.
