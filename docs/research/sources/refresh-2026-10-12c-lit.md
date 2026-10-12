# Refresh 2026-10-12c-lit: sourcing the FMnull variance components

Scope: the parameters that `research/checks/fm_mesa_null.py` (pre-registered in 48241c7) labels UNSOURCED. The script is NOT edited; any change to a bracket is a post hoc decision for the parent. Quote ids `FML-*` are in `quotes-literature.md` ("Refresh 2026-10-12c-lit quotes"); all were machine-checked against the fetched text. Items marked **derived** are my arithmetic on quoted numbers, not quotes.

## Papers
| Paper | Obtained? | Note |
|---|---|---|
| Smith, Arndt, Eyre-Walker 2018 (PLoS Genet) | yes, OA full | germline DNM, human, 10 kb-10 Mb |
| Phung, Huber, Lohmueller 2016 (PLoS Genet) | yes, OA full | 100 kb windows |
| Duret & Arndt 2008 (PLoS Genet) | yes, OA full | 1 Mb |
| McVicker et al. 2009 (PLoS Genet) | yes, OA full | 1 Mb (Fig 7C), 4 kb-4 Mb (Fig S6) |
| Hobolth et al. 2007 (PLoS Genet) | yes, OA full | 1.9 Mb of HCGO alignments |
| Hodgkinson & Eyre-Walker 2011 (Nat Rev Genet) | NO: paywalled; abstract only (no numbers) | no bypass |
| Hwang & Green 2004 (PNAS) | NO full text: pnas.org bot challenge (403), Europe PMC XML 500; abstract only | context-dependent rate ranges not obtained |

## Parameter table
Bracket status: inside / outside / not found (no number in the obtained text). "Window" is the scale at which the cited number applies.

| Parameter in script (bracket) | Sourced value(s) (id; scale; species) | Bracket contains it? |
|---|---|---|
| M0 chromosome-scale: sigma [0.02, 0.10], ell 5-20 Mb | Smith: windows up to 10 Mb were fitted (FML-S4) and the abstract says variation at 10 Mb is significant but modest; CV at 10 Mb not in text (figure). Duret & Arndt: GC* falls with distance to telomere (FML-D1, qualitative) | not found (sigma); direction consistent |
| M1 replication/large-scale mu: sigma [0.05, 0.20], ell 0.5-2 Mb | FML-S2: DNM-density CV at 1 Mb = 0.18 (Francioli), 0.27 (Wong), 0.15 (Jonsson), human germline. Script's M0+M1 combined upper = sqrt(0.10^2 + 0.20^2) = 0.224 (derived) | inside for 0.15 and 0.18; **outside (above) for Wong 0.27**. Smith: the datasets differ "probably as a consequence of differences in sequencing technology and processing" (abstract), so Wong may be technical. Mutation CV only; divergence adds gBGC and BGS |
| M2 meso-scale: sigma [0.05, 0.20], ell 20-100 kb | 100-kb CV not in text. **Derived** from FML-S2 and FML-S5 slopes (CV x 10^(-b)): 0.18 x 10^0.25 = 0.32 (Francioli), 0.27 x 10^0.10 = 0.34 (Wong), 0.15 x 10^0.16 = 0.22 (Jonsson); assumes a pure power law between 1 Mb and 100 kb. Script's M0+M1+M2 upper = sqrt(0.01 + 0.04 + 0.04) = 0.30 | inside for Jonsson (0.22); **slightly outside above for Francioli and Wong (0.32, 0.34)**; derived, flag |
| M3 fine-scale: sigma [0.10, 0.40], ell 0.2-2 kb | FML-S7: "the largest amounts of variation are at the smallest scales"; no number in text | not found |
| CPG: sigma [0.03, 0.15], ell 5-50 kb | Hwang & Green abstract only (FML-HG1: CpG transitions "relatively clock-like"); no number | not found |
| GBGC: sigma [0.02, 0.10], ell 50 kb-1 Mb; lambda [0.3, 1.0] | FML-D4: average hotspot impact on local substitution rate "relatively modest" (text elsewhere: 1.1% vs 0.5%, i.e. 2x, model); FML-D5: most extreme hotspot (~450 cM/Mb) ~20x, model; FML-D2/D3: crossover rate explains 31-36% of variance in GC* at 1 Mb (GC*, not substitution density). FML-S8: divergence-DNM correlation about half its maximum, gBGC proposed | not found (no sigma); direction supports a localised, lineage-limited gBGC term (hotspots move) |
| ILS: sigma [0.125, 0.25] = T2/(t1+T2) | FML-H1: speciation 4.1 +/- 0.4 My; N_HC 65,000 +/- 30,000; N_HCG 45,000 +/- 10,000 (1.9 Mb, human-chimp-gorilla-orangutan, assuming orangutan 18 My, 25 y generations). **Derived** for exponential two-lineage coalescence in the HC ancestor, mean = 2N generations, sd = mean: N = 65k gives 3.25 My, so sd/(tau + mean) = 3.25 / 7.35 = 0.44; N 35k-95k gives 0.30-0.54. The ratio is calibration-independent (all times scale together) | **outside (above)**: derived 0.30-0.54 vs script 0.125-0.25. The script's T2 1-2 My is about 2-3x too small for Hobolth's N. Caveats: the sigma is per locus (tract scale), so window means are barely affected at >= 10 kb; BGS lowers effective N in the ancestor (McVicker) |
| ILS ell [0.1, 2] kb | FML-H5: HC1-state tract length correlates with pedigree recombination rate; the numbers are in Hobolth Table 2, not in extracted text | not found |
| ALN (alignment error): sigma [0.016, 0.42], ell 10-100 kb | none of the seven papers quantifies it | not found |
| BGS: sd(B) [0.05, 0.25]; ell 0.2-2 Mb | FML-M2: mean autosomal B = 0.74-0.81 (90% CI), diversity reduced 19-26% (FML-M1); B distribution only in a figure. Scale: McVicker uses 1 Mb (FML-M6) | not found (sd(B)); mean implies B spans below 1 |
| BGS sigma = [T2/(t1+T2)] sd(B) = [0.006, 0.0625] | with the ILS ratio above (0.30-0.54) and sd(B) 0.05-0.25: **derived** 0.015-0.135 | **partly outside (above)**: upper 0.0625 vs 0.135 |
| P7: BGS adds <= 25% to N_hi | McVicker claims BGS "explains the large intragenomic variation in human/chimpanzee divergence" (FML-M3); Phung: BGS "can still explain a large proportion of the variance" (FML-P1) via variance in ancestral polymorphism (FML-P5); but McVicker finds GC and recombination "only weakly correlated" with H/C divergence (FML-M5). Phung: rho(recomb, divergence) 0.108 observed, 0.042 with no BGS, 0.107 with McVicker B (FML-P2, FML-P3; 100 kb) | prediction P7 is in tension with both papers (they say BGS is a major share of divergence variance, not <= 25%). Both are model-based claims; Day-side and critic-side steelmen should both cite them |
| Sweeps negligible (variance ~ pi_anc/2 W) | not addressed | not found |
| Window scales used by the literature | Smith 10 kb-10 Mb (FML-S4); Phung 100 kb (FML-P4); McVicker 1 Mb and 4 kb-4 Mb (FML-M6, FML-M7); Duret & Arndt 1 Mb (FML-D2) | n/a |
| Context-dependent substitution rate ranges | Hwang & Green only as abstract | not found |

## What the literature adds that the script lacks
- Smith: **covariates explain little**: genomic features explain "less than 40% of the explainable variance" (FML-S6; Discussion says less than 50%). A bracket on how much of the rate variance is *covariate-predictable* (the S3 test uses |Spearman| < 0.1) should expect weak, not absent, correlations. This supports Day's S3 side as much as it limits it: a mesa that correlates weakly with covariates is the norm for neutral variance.
- McVicker and Phung: **linked selection in the ancestor is a documented, large contributor to H/C divergence variance**; the script's BGS arm (troughs, shared by H and C) is directionally right but its amplitude is bracketed low (see above). This favours the critic-side null (selection and drift together explain more) but the same papers say the variance is *selection-driven*, which is a point Day can use against "neutral" in FM10 (the null being tested is neutral drift; BGS is selection).
- Smith: the Abstract and the Results disagree on what CV 0.18 means (within 50% vs within 30%); recorded, not resolved.

## Maps for covariate arms (URLs only; nothing downloaded)
- **Liftover chains hg38/hg19 <-> CHM13 v1.1:** `https://t2t.gi.ucsc.edu/chm13/dev/t2t-chm13-v1.1/downloads/` (stated in the Massey & Koren data-availability, FML-R1); assembly at `https://github.com/marbl/CHM13`. UCSC also documents hs1 liftOver at `https://hgdownload.gi.ucsc.edu/gbdb/hs1/hubs/public/hgLiftOver.html` (seen in a search result, page not fetched).
- **Recombination maps in CHM13 coordinates:** no pre-lifted map found. Route: lift an hg19/hg38 map (HapMap/deCODE/Halldorsson, sources not re-verified here) with the chains above. Caveat: lifted maps cover human only; the ape lineages need their own maps or the human map as a proxy (hotspots turn over: FML-D4/D5 context, Hobolth FML-H5).
- **Replication timing in CHM13 coordinates:** Massey & Koren 2022, Sci Rep 12:9560, PMC9187705, T2T replication-timing profiles for five cell lines from SRA PRJNA419407 (FML-R1). Where the processed bigWig/bedGraph tracks are hosted is NOT stated in the open text; check the article's supplementary material before relying on them.

## Unobtainable
Hodgkinson & Eyre-Walker 2011 (paywalled; abstract only). Hwang & Green 2004 full text (bot challenge; Europe PMC 500). Numbers living only in figures, tables or supplements of the obtained papers (Smith 100-kb CV, McVicker B distribution and Fig 3 ratios, Hobolth Table 2).

## Mismatches to hand to the parent (script NOT edited)
1. ILS sigma [0.125, 0.25] sits below the Hobolth-implied 0.30-0.54 (derived).
2. BGS sigma upper 0.0625 below derived 0.135; P7 "<= 25%" conflicts with McVicker/Phung's claim of a large BGS share.
3. M1 upper edge: Wong 1 Mb CV 0.27 exceeds the M0+M1 combined upper 0.224; M2: derived 100-kb total CV 0.32-0.34 exceeds 0.30 for two datasets.
All other components: not found.
