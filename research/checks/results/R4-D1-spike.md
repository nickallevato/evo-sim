# R4 D1 spike: how many interchangeable alternatives per needed change do real(ish) sequence spaces offer?

Branch D. This measures the quantity G1 left open (R4-G1.md section 3). G1 found that Day's "specific outcome" product p^n stops binding once the Poisson mean number of successful arisings per required change, λ = m·(−ln(1−q)), passes **λ₅₀ = 12.3–17.2** (n_f = 1.6e5 to 2e7; 7.3 at n_f = 1e3; 9.6 at 1e4). With Day-family inputs (N = 1e4, μ = 1.2e-8, s = 0.01, T = 3e5; q = 0.381) one alternative is worth λ_alt = 0.48, so the flip needs m* = 15–36 alternatives per change. Other G1 bases give m* = 31–73 (T = 146,250, s = 0.01), 151–357 (T = 3e5, s = 0.001) and 313–738 (T = 146,250, s = 0.001). Whether real sequence spaces sit above or below that was untested. Two stand-ins were measured: RNA folding (ViennaRNA) as a genotype-to-phenotype map, and deep mutational scanning (ProteinGym v1.3).

Claims touched or informed: D, D2h (directly), D2c, D3, D4, D10–D12, D15 (context), and the G3b dilemma. No claim file, argmap, README or gaps.md was edited.

## 0. Headline

All m are per genotype (K = 1) unless stated. λ uses the Day-family basis q = 0.381, λ_alt = 0.48. "Reach" is the share of (genotype, needed-outcome) pairs with at least one single-mutation route; "m∣reach" is the mean number of distinct single mutations that reach the outcome, given at least one does.

| Reading of "the same needed change" | Medium | m∣reach (median [range over targets or datasets]) | Reach | λ (T=3e5, s=0.01) | vs flip 12.3–17.2 |
|---|---|---|---|---|---|
| Exact structure S2 (accessible, uniform over distinct S2) | RNA, 15 targets | **2.3** [1.5–4.5] | 1.8% [0.5–3.0] | 1.1 | far below |
| Exact S2, frequency-weighted over neighbours | RNA | 2.9 [2.2–5.8] | 18% [9–32] | 1.4 | far below |
| Within 2 base pairs of S2 (S2 ≥ 5 bp from S1) | RNA | 3.4 [2.1–5.1] | 3.1% [0.6–8.5] | 1.7 | far below |
| Same abstract topology as S2 (pre-registered E2) | RNA | **28** [14.5–45] | 91% [67–100] | 13.4 | in the band, but see below: dominated by "lost a helix" |
| Same topology, S2 not a loss of helices (post hoc E2g) | RNA | 7.2 [1–25] (L≥76: 11.8 [4.5–25]) | 59% | 3.4 (L≥76: 5.7) | below; one L=100 target reaches 12 |
| Same topology, rare shapes only (post hoc E2rare) | RNA | 4.5 [1–6.6] | 21% | 2.2 | below |
| Double mutants only (no single route), exact S2 | RNA | 4.7 [3–19] | 3.8% | needs two arisings | not comparable |
| Functional alternatives at one codon (nonsynonymous SNVs, s*≥0.5) | DMS, 114 non-stability sets | **5.1** of 7.0 [2.5–6.5] | – | 2.4 | below |
| Functional SNVs anywhere in the mutated region (s*≥0.5) | DMS | 1,110 [68–5,570] | – | 530 | not a "change" count (neutral alternatives) |
| Beneficial-proxy SNVs anywhere in the region (s*≥1.2, an upper bound) | DMS | **51** [0–1,760] | – | 24 | above at s=0.01 and T=3e5; 12 with Day's d-corrected T; 2.4 at s=0.001 |

Pooling over the K = 40–60 neutral genotypes I sampled raises the RNA counts: exact S2 2.1 (uniform) to 30 (frequency-weighted); topology-class E2g 207; E2rare 43. That is a population quantity (it presumes many distinct neutral genotypes segregating at once), not the per-genotype m.

**Reading, kept neutral:**
- **Site-level or exact-outcome needs sit well below the flip.** Every exact, ≤2 bp, or non-degrading-topology RNA class and every single-codon DMS class has λ of about 1–6, against a flip of 7–17. At those granularities Day's p^n regime stands (G1: P ≈ 10^−176 for n_f = 1e3 at λ = 1.1).
- **Gene-level "any beneficial change in this region" needs sit at or above the flip, but the number is soft.** It is an upper bound (assay noise inflates it), it depends on s and T, and it changes the unit of a "required change" from a locus to a gene.
- **Neither side's strong form is supported.** Day's m ≈ 1 is too low even for exact-structure RNA (m∣reach about 2) and for DMS codons (5 of 7). The critics' "plenty of interchangeable alternatives, so the barrier vanishes" is not supported at the locus level. It is conditional on the unit of the requirement and on s.

## 1. Runs, provenance, labelling

| Item | Value |
|---|---|
| Pre-registered script | `research/checks/d1_sequence_space_spike.py`, commit d72c733. Predictions P1–P11 are in its docstring and were written before any main run. |
| Summarizer-only edit | commit 582428a (post hoc: NaN-safe medians and a coverage ≥ 0.5 group). No measurement code changed. |
| Host and versions | na-workhorse, ViennaRNA **2.7.2**, numpy 2.5.3, Python 3.14.4. Same pin on the workstation. Pinned in `research/requirements.txt`. |
| Main runs | `nn` 2231 s; `rna` 2123 s (12 processes). `dms` (14 s) and `gb1` (22 s) ran on the workstation at nice 19, one process. Script md5 on workhorse: 42f8da52… |
| Seeds | `SeedSequence([20261090, part, config, rep])` |
| Data | ProteinGym v1.3 substitutions zip (217 sets) and reference file, downloaded to `sources/raw/d1-dms/` (gitignored, never executed, read as CSV). |
| Post hoc, labelled | `d1_posthoc_refine.py` (workhorse, 732 s; same genotypes as the main run, same seeds), `d1_posthoc_gb1_snv.py`, `d1_aggregate.py`. All written after the main output was seen. |
| Outputs | `results/raw/d1_nn.json`, `d1_rna.json`, `d1_dms.json`, `d1_gb1.json`, `d1_posthoc.json`, `d1_posthoc_gb1_snv.json`, `d1_summary.txt`, `d1_aggregate.txt`, `d1.host`. |

**Disclosures:**
- Before the commit I looked at the GB1 score quantiles (to fix WT = 1) and at the metadata of the DMS sets (assay type, cutoff method). The first clause of P11 (more than 90% of variants nonfunctional) is therefore not a blind prediction.
- The tiny RNA smoke runs printed ν ≈ 0.32.
- The first look at the DMS output (before any change) showed NaN site statistics for sparse datasets. That is why a coverage ≥ 0.5 subset was added (post hoc). The headline DMS group is "non-stability, coverage ≥ 0.5" (n = 114 of 140 non-stability sets; 206 analysed in all, 66 of them stability).

## 2. Definitions used

**RNA.** The genotype is an RNA sequence. The phenotype is the MFE structure at 37 °C. A "neutral" mutation leaves the MFE structure unchanged.

| Class | Meaning |
|---|---|
| m_E0 (strict) | Number of distinct single-nucleotide mutants of x (which folds to S1) whose structure is exactly S2. |
| m_E1 (medium) | The same, with the mutant's structure within 2 base-pair differences of S2. S2 is restricted to d_bp(S1,S2) ≥ 5. |
| m_E2 (lenient) | The same, with the mutant sharing S2's level-5 abstract shape (helix nesting and branching only). S2's shape differs from S1's. The cloverleaf is `[[][][]]`. |
| m_ben (graded) | Number of single mutants strictly closer in base-pair distance to a target S*. |
| Doubles | All C(L,2)·9 double mutants that reach the class while neither single component does. |

S2 is drawn from the distinct non-neutral structures seen in the 1-mutation neighbourhoods of an independent sample A of neutral genotypes. m is then measured on genotypes B, which are disjoint from A. So S2 is always accessible from the neutral network. The unconditional chance that an arbitrary needed S2 is reachable is lower than the "reach" shown.

**Targets (15).**
- Yeast tRNA-Phe cloverleaf (L = 76). It folds exactly to the cloverleaf under MFE.
- Random-sequence-derived structures: four each at L = 30 and 50, three each at L = 76 and 100. They need ≥ 0.25·L pairs and ≥ 2 helices.
- Neutral genotypes were sampled by a symmetric-proposal Metropolis walk, which is uniform on the connected neutral set. There were 70–100 samples per target (K_A = 30–40, K_B = 40–60).

**DMS.** ProteinGym's own binarisation is a median split for 126 of the 217 sets, so it cannot give fractions. I normalised each dataset:
- s* = (score − N̂)/(Ŵ − N̂).
- N̂ is the median of the lowest 5% of singles.
- Ŵ is the median score at the most tolerant quartile of sites (a WT-like proxy).
- Thresholds are my choices: functional s* ≥ 0.5, near-WT s* ≥ 0.8, "reduced" s* < 0.8, "destroyed" s* < 0.2, and beneficial proxy s* ≥ 1.2.
- Cross-check: the 54 sets with an author-chosen manual cutoff give a fit fraction of 0.67 [0.56–0.76]. My s* ≥ 0.5 gives 0.71 on the whole group.

## 3. RNA results

### 3.1 Neutral networks and neutrality (P1, P2)

- **Neutral-network size** is N_NN = 6^bp·4^unp·f, with f the fold frequency among pair-compatible sequences. A pair-compatible set must contain every sequence that folds to S1, because MFE pairs are canonical.
- **tRNA cloverleaf:** f = 2.2e-4 (67 hits in 300,000 draws), N_NN ≈ **10^33.2** (95% interval 10^33.1–33.3), a fraction **10^−12.6** of the 4^76 space.

| L | log10 N_NN | log10 fraction of 4^L |
|---|---|---|
| 30 | 11.4–13.3 | −4.7 to −6.6 |
| 50 | 19.4–21.6 | −8.5 to −10.7 |
| 76 | 31.6–33.2 | −12.5 to −14.1 |
| 100 | 41.8–42.4 | −17.8 to −18.5 |

- One L=76 and one L=100 target had zero hits. Only upper bounds exist: ≤ 10^32.3 and ≤ 10^44.0.
- Every network is enormous in absolute terms, even at L = 30.
- **Spread:** sampled neutral genotypes differ from each other at 0.56·L positions on average (a random pair differs at 0.75·L; range over targets 0.40–0.59). The network is spread across sequence space. This is not proof of one connected component.
- **Mean neutrality ν** is 0.30 [0.23–0.43] over the 15 targets. tRNA is 0.313.
  - Paired-site neutrality is 0.094 [0.03–0.14] and unpaired 0.545 [0.44–0.78].
  - The simple threshold ν_c = 1 − 4^(−1/3) = 0.37 (quoted from memory) is exceeded by the mean ν of only 1 of 15 targets. So ν alone does not show percolation here. The wide Hamming spread is the better evidence of a connected, broad network.

### 3.2 Day's ruggedness framing in RNA (P5)

Fraction of the 3L single mutants that are "deleterious", under three equivalence rules:

| Rule | All 15 targets | tRNA |
|---|---|---|
| Structure changed (strict) | **0.70** [0.58–0.77] | 0.69 |
| More than 2 bp from S1 | 0.56 [0.40–0.68] | 0.57 |
| Different abstract topology | 0.27 [0.16–0.50] | 0.44 |

Day's "most single changes alter the outcome" holds for exact-structure identity. It weakens as "same function" is loosened to topology, but it does not vanish. For the tRNA cloverleaf it takes 44% of single mutations to change the topology. This is a higher fraction than I predicted.

### 3.3 Alternatives per change (P3, P4)

Medians over the 15 targets (the table in section 0 has λ). By size class, m∣reach and reach:

| Class (pool) | L=30 | L=50 | L=76 (random) | L=100 | tRNA76 |
|---|---|---|---|---|---|
| E0 uniform | 2.5, 2.4% | 2.1, 1.7% | 1.9, 1.5% | 3.1, 1.8% | 1.5, 0.5% |
| E1 uniform | 4.1, 7.8% | 3.6, 2.8% | 3.1, 1.8% | 2.6, 2.5% | 2.6, 0.6% |
| E2 uniform (pre-reg) | 37, 100% | 24, 92% | 17, 77% | 27, 76% | 29, 90% |

Observed versus predicted:
- **E0:** I predicted 1.0–1.6 and found 2.3 (median over reachable pairs 1–3, 90th percentile 3–6). The likely cause, which I did not test separately, is that the two partners of a lost pair and the up to three alternative bases at one site can give the same disrupted structure. If so, this "structure, not sequence, is the outcome" redundancy is real, and larger than I guessed.
- **E1:** I predicted 1.3–3 and found 3.4.
- **E2:** I predicted 2–12 and found 28. See the next paragraph.

**Why E2 is inflated.**
- The neighbourhood of a genotype contains very few abstract shapes: a median of 5 [2–18] distinct shapes. The top 3 shapes make up 99% of neighbour instances. On average 33% of changed neighbours are "fewer helices than S1" and 62% keep S1's shape.
- Drawing S2 uniformly over distinct structures therefore lands mostly in a handful of common shapes, typically "a helix was lost".
- This is a property of the abstraction I chose, not a measure of functional equivalence. A shape class holding 38 of 90 L=30 neighbours is a class of "damaged versions". The post hoc refined classes (section 0) remove that artefact: E2g gives m∣reach 7.2 and λ 3.4, and E2rare gives 4.5 and λ 2.2.
- At L ≥ 76, E2g has m∣reach 11.8 [4.5–25] and λ 5.7. One L = 100 target (rand100_2) reaches m∣reach 25 and λ 12.2, the lower edge of the flip band.
- Also post hoc: for the L = 30 targets E2g and E2rare have almost no candidates (0–2 of the pool). The one-step shape repertoire of a 30-mer is just 2–3 shapes, so "topology-equivalent alternative" is undefined there.

**Doubles.**
- For pairs with no single-mutation route, the chance a double mutant reaches exact S2 is 3.8% [1.8–7.7] with m2∣reach 4.7. For E1 it is 8.6% [3–30], with m2∣reach 8.9.
- For E2 it is 93% (m2∣reach 105 [20–398]), but the E2 caveat applies again.
- I predicted 10–300 routes for double mutations on E1 and E2, and the E1 figure is lower. The doubles provide many more routes only for the degrading-shape E2 classes.

### 3.4 Graded fitness: −d_bp to a target (P5, P6)

Fitness is minus the base-pair distance to S*. "Near" S* are accessible structures; "far" S* are MFE structures of random sequences. Values are medians over targets.

| Start distance d0 | Targets | Improving neighbours | Worse neighbours | At least one improver | Strict local optimum |
|---|---|---|---|---|---|
| 1–4 bp | near | 1.0% | 69% | 0.53 | **0.47** |
| 5–10 bp | near | 3.4% | 65% | 0.88 | 0.12 |
| ≥ 11 bp | near | 31% | 33% | 0.996 | 0.004 |
| ≥ 11 bp | far | 41% | 19% | 1.0 | 0 |

- Near the target there are few improving neighbours, and a strict local optimum is common. At d0 of 1–4 bp, 47% of (genotype, S*) pairs have no improving neighbour.
- Away from the target, almost every genotype can improve.
- The metric flatters smoothness at large d0. Removing any wrong pair lowers d_bp, so the "improving" fraction is partly bookkeeping.
- **Adaptive walks** (random improving neighbour, neutral drift allowed up to a budget of 100, or 60 for tRNA):
  - Success was 0.77 [0.17–0.85] for near targets and 0.73 [0–0.93] for far targets.
  - Trapped with no move: 0 in every case. All failures are drift-budget exhaustion at a mean final d_bp of 0.2–2.4 for L ≤ 50 (tRNA: 5–6 from a start of 36–40, with only 6 walkers).
  - The walk reaches within about 1 pair of the target and stalls on a plateau. The tight budgets are not evolutionary timescales, so I do not read the failures as ruggedness traps.

## 4. DMS results

### 4.1 What the 114 non-stability sets show (P7–P10)

Medians, with the inter-quartile range in brackets (the earlier tables use the range over targets or datasets).

| Quantity | Value | Predicted |
|---|---|---|
| Single substitutions functional (s* ≥ 0.5) | **0.71** [0.59–0.79] | 0.45–0.75 |
| Near-WT (s* ≥ 0.8) | 0.47 [0.37–0.57] | 0.25–0.55 |
| Reduced (s* < 0.8) | **0.53** [0.43–0.63] | 0.45–0.75 |
| Destroyed (s* < 0.2) | **0.11** [0.08–0.18] | 0.10–0.40 |
| Datasets where a majority of singles are reduced | 61% | – |
| Datasets where a majority are destroyed | 2% | ≤ 15% |
| Sites with at most 10% of substitutions functional | **3.8%** [1–10] | 10–35% |
| Sites with at least 90% functional | 38% [22–53] | 10–40% |
| Functional alternatives per site, of 19 amino acids | 13.5 [11.3–15.1] | 6–13 |
| Functional alternatives per codon, of ~7 nonsynonymous SNVs | **5.06** [4.5–5.7] | 1.8–4.0 |
| Beneficial proxy fraction (s* ≥ 1.2, upper bound) | 3.6% [0.6–9.2] | 0.5–6% |

- The 66 stability sets (ΔG proxies, not function) look similar: 0.77 functional, 0.47 reduced, 0.087 destroyed, 32% with a reduced majority.
- Named cases:
  - TEM-1 is split by assay: Stiffler 2015 gives 0.575 functional, 0.20 destroyed, 8.8% fully intolerant sites; Firnberg 2014 gives 0.448, 0.376 and 22%.
  - GB1 Olson 2014 gives 0.783 functional.
- Mean-effect "deleterious" does not equal "rugged" in either direction here: these are one-step distributions around an optimum, not tests of local optima (see 4.2).

**D2h, claim by claim.** The quoted claim is "single-residue changes to most proteins tend to reduce or destroy function. The landscape is rugged, not smooth."
- **"Reduce":** supported. In 61% of non-stability datasets a majority of singles fall below 80% of the WT-like level; the median is 53%.
- **"Destroy":** not supported as a majority statement. The median is 11%, and 2% of datasets have a majority destroyed. A median of 5.1 of ~7 nonsynonymous codon neighbours stay functional.
- **"Rugged, not smooth":** a statement about local optima and epistasis, which one-step data cannot test. See GB1 below.
- Day cites no study. The measured numbers are mine, using my normalisation.

### 4.2 GB1 four-site complete landscape (Wu 2016; 149,360 of 160,000 variants plus the WT; WT = 1 assumed)

| Quantity | Any amino acid at a site (pre-registered) | SNV-accessible steps only (post hoc, codon union) |
|---|---|---|
| Variants below 0.3 of WT | 95.0% (not a blind prediction) | – |
| Functional (≥ 0.5 WT) | 5,822 (3.9%) | same |
| Functional variants with no functional neighbour | 0 | 0.03% |
| Share of a functional variant's neighbours that are functional | 38% (of 76) | 41% (of ~12 on average) |
| Local maxima among functional | 18 | **87** |
| Functional variants with a strictly uphill path to the global maximum | **98.5%** | **44%** |
| Share in the largest connected functional component | 99.9% | 99.8% |

- **Day:**
  - 95% of the four-site space is nonfunctional.
  - Of the 76 single substitutions from WT, 53% are below 0.2.
  - At SNV granularity, 56% of functional variants cannot reach the best variant by a monotone path.
  - The ruggedness claim is true for this subspace.
- **Critics:**
  - The functional set is one connected component holding 99.8–99.9% of functional variants, with WT in it.
  - Isolated islands are essentially absent here.
  - Allowing any amino acid at a site makes the top reachable from nearly everywhere.
- The SNV adjacency used the union over codons of the WT amino acid, which is more permissive than any one genotype. The SNV figures are upper bounds on reachability.
- My P11 predictions held at SNV level and failed at the any-amino-acid level.

## 5. Prediction scorecard

| # | Prediction | Result |
|---|---|---|
| P1 | ν 0.25–0.55; tRNA 0.25–0.50; ≥ 70% of targets above 0.37; unpaired 0.6–0.9, paired 0.15–0.45 | ν **held** (0.30, tRNA 0.313). Percolation share **failed** (1 of 15). Unpaired **partly failed** (median 0.545, below the band). Paired **failed** (0.09, below the band). |
| P2 | tRNA 10^30–37; L=30 fraction 1e-4..1e-1; L=100 1e-12..1e-5 | tRNA **held** (10^33.2). L=30 **partly failed** (10^−4.7 to −6.6). L=100 **failed** (10^−17.8 to −18.5). |
| P3 | m∣reach E0 1.0–1.6, E1 1.3–3, E2 2–12; λ below 12–17 for every single-genotype definition | E0 **failed** (2.3), E1 **failed** (3.4), E2 **failed** (28). "λ below the flip" **held for E0 and E1**, **failed for pre-registered E2** (13.4), and **held for the refined E2g and E2rare** (post hoc). |
| P3 pooled | E2 pooled over ≥ 40 genotypes is 50–400 | Direction **held**, magnitude higher (445–2,700; degradation-inflated). |
| P4 | Doubles: P(m2≥1) 0.3–0.9 and 10–300 routes for E1 and E2 | E2 **held** (0.93, 105). E1 **failed** (0.086). |
| P5 | Deleterious: strict 0.45–0.75, medium 0.25–0.55, lenient 0.05–0.30 | Strict **held** (0.70). Medium **marginal** (0.56). Lenient **held on the median** (0.27) but not at L=30 or tRNA (0.40–0.50). |
| P6 | At least one improver 0.6–0.95; improving 1–8%; strict optima ≤ 30%; near walks ≥ 85%; far walks 20–70% | **Held for d0 5–10** (0.88, 3.4%, 0.12). **Failed at d0 1–4** (0.53; local optima 0.47). **Near walks failed** (0.77, budget-limited). **Far walks slightly above the band** (0.73). |
| P7 | Functional 0.45–0.75; reduced 0.45–0.75; destroyed 0.10–0.40; majority destroyed in ≤ 15% | **All held** (0.71, 0.53, 0.11, 2%). |
| P8 | Intolerant sites 10–35%; tolerant 10–40% | Intolerant **failed** (3.8%). Tolerant **held** (38%, top edge). |
| P9 | m_aa 6–13; m_snv 1.8–4.0; λ_site 0.9–1.9; gene-level functional in the hundreds to thousands; beneficial 5–150 | m_aa **marginally failed** (13.5). m_snv **failed** (5.06). λ_site **failed in magnitude** (2.4), **same direction**. Gene-level **held** (1,110; 51). |
| P10 | Beneficial proxy 0.5–6% | **Held** (3.6%). |
| P11 | > 90% nonfunctional; ≥ 30 local maxima; < 50% reach the top; ≥ 70% in one component | Nonfunctional **held** (not blind). Maxima and reach **failed at any-amino-acid** (18; 98.5%), **held at SNV level** (87; 44%, post hoc). Component **held** (99.9%). |

**Net.**
- The directional headline held: exact and near-exact alternatives per change are far below the flip, and the DMS overall fractions came out as predicted.
- My point estimates for RNA alternatives, neutrality components and network sizes were often off.
- The largest miss was E2. I expected an abstract-topology class to give a moderate m, and instead found a number dominated by shape-degradation multiplicity.

## 6. Reading for the G1 flip

Illustrative G1 bookkeeping, log10 P_all = n_f·log10(1 − e^−λ):

| λ | n_f = 1e3 | 1e4 | 2e5 | 2e7 |
|---|---|---|---|---|
| 0.5 | −405 | −4,051 | −81,018 | −8.1e6 |
| 1.1 (RNA exact S2) | −176 | −1,758 | −35,158 | −3.5e6 |
| 2.4 (DMS one codon) | −41 | −413 | −8,260 | −8.3e5 |
| 5.7 (RNA topology-no-loss, L ≥ 76) | −1.5 | −14.6 | −291 | −29,111 |
| 12.3 | −0.00 | −0.02 | −0.4 | −39.5 |

The answer to "above or below 12–17?" has three parts:
1. **Per-locus or exact-outcome needs: below.** λ is 1–6. The p^n regime is binding if the n_f requirements are site-specific.
2. **Per-gene or per-molecule "any improving change": about the flip.** λ about 24 for the DMS beneficial proxy at the generous basis, and 12 at the d-corrected T. It drops to about 2.4 at s = 0.001. If one gene-level need counts as one requirement, n_f is also limited by the number of genes, so the relevant λ₅₀ is lower than 17.2. RNA's own gene-level analogue (m_ben of a few for small d0, but many at large d0) points the same way, with the metric caveat of section 3.4.
3. **The G1 caveats remain.** The assumptions of independence and equal s favour the interchangeable case; stepping-stone dependence and functional-island structure lower the effective m. Everything here is single-step, single-genotype, and takes alternatives as equally good.

**Credit:**
- **Day:**
  - 70% of single RNA mutations change the exact structure.
  - 95% of GB1's four-site space is nonfunctional.
  - Sign-epistasis ruggedness exists at SNV level (87 local maxima, 56% unable to reach the top monotonically).
  - Locus-level λ is far below the flip.
  - In 61% of DMS datasets a majority of singles are reduced.
  - Paired RNA sites are almost never neutral (9%).
- **Critics:**
  - The neutral networks are enormous: 10^33 sequences for a tRNA cloverleaf, spread across sequence space.
  - Destroyed singles are a median 11% (a majority in 2% of datasets).
  - Fully intolerant sites are rare (4%).
  - The functional set in GB1 is one giant component.
  - The RNA graded landscape has almost no strict traps away from the target.
  - There are several routes to the same phenotype (m∣reach about 2–5 for exact structures, and tens to thousands pooled across genotypes).
  - "Mostly deleterious" does not imply "rugged": ruggedness needs local optima, and the RNA graded data show few away from the target.

## 7. External validity: how each caveat cuts

RNA secondary structure is a toy for proteins and regulation. The DMS leg is real protein data, but it is a different kind of evidence.

| Caveat | Direction |
|---|---|
| **RNA toy status.** A 4-letter alphabet with base pairing, a unique MFE structure as "function", no tertiary structure, no ligand binding, no kinetics or multiple structures. Real function depends on 3D structure. | Unknown overall. |
| RNA pair-partner redundancy (either partner, up to three bases) inflates m_E0 relative to protein residues, where there is no such partner symmetry. | **Favours the critics** (m too high for proteins). |
| Structure identity is a stricter definition of function than a real protein or regulatory element has. Real function tolerates structural change. | **Favours Day** for E0 and E1 (m too low). The E2 numbers go the other way (too high, degradation). |
| Random-sequence-derived targets are biased to common structures. tRNA, a selected structure, reaches less (reach 0.5% for E0). | **Favours Day** for selected, specific structures. |
| S2 is drawn from structures accessible from the network. | **Favours the critics** (reach is conditional). |
| Equal s is assumed for all alternatives in G1, and in my pooling. | **Favours the critics** (flatters m). |
| Single genotype per m. Real populations carry many neutral variants. | **Favours the critics** (pooled counts are tens to thousands). |
| DMS: lab assays, saturating selection, WT buffered by design, ProteinGym chooses well-behaved sets, and stability sets measure folding rather than function. | **Favours the critics** for tolerance (the majority of singles retained). |
| DMS: s* and Ŵ are my normalisation. The beneficial proxy is inflated by noise (an upper bound), and lab benefit is not natural fitness. | **Favours Day** for the beneficial pool. The 3.6% and the gene-level 51 are upper bounds. |
| DMS covers extant, optimised proteins and one-step neighbours of the optimum. It says nothing about the connectivity of functional sequences across families. Axe 2004 (≈1e-77), Taylor 2001 (≈2e-24) and Keefe & Szostak 2001 per-sequence prevalences (D10–D12) remain a separate regime and are untouched. | **Favours Day** (no connectivity claim is made across folds). |
| GB1: one interface subspace, chosen for epistasis. | **Favours Day** for ruggedness. Its giant component favours the critics. |
| Codon mapping used the standard code and averaged synonymous codons; no genome context. | Small, either way. |
| Regulatory and noncoding sequence (D15, Hössjer) was not measured. | Open. |

## 8. Limits and open items

- The RNA sample is 15 targets, 70–100 genotypes each, and one tRNA. Ranges are across targets, not confidence intervals. Several classes have only 3–4 targets per length.
- MFE only; no ensemble or suboptimal structures. d_bp is crude; the "improving neighbour" count at large d0 is partly bookkeeping.
- The walks had tight budgets and 6 walkers on tRNA. They are not a trap test at evolutionary scale.
- Two of the 15 targets had no hits in the NN-size estimate (upper bounds only). The estimate counts all pair-compatible sequences that fold to S1, including any other components.
- E2 is shape-level 5 only. Other abstractions (a different level, a motif-based one) would give a different m.
- DMS thresholds are mine (s* cutoffs, WT proxy). A different W estimator would move the fractions by a few points; the author-cutoff cross-check (0.67 vs 0.71) is reassuring but only covers 54 sets.
- The GB1 WT = 1 normalisation was assumed (not checked in the file).
- The post hoc classes use the same genotypes as the main run (same seeds) but fresh S2 draws, so they are not a re-count of the same pairs.
- Not done: protein folding maps (lattice or HP), real multi-site sets across families, and alternatives per change in the regulatory regime.

## 9. Suggested use by the lead (not applied)

- **D2h (external):** the harvest can now say "supports 'reduce', not 'destroy'; ruggedness in the sign-epistasis sense is real at SNV level in one complete 4-site set, but the functional set is connected". Day's fidelity stays unverifiable (no citation).
- **G3b / G1 open item:** replace "per-site m is not established" with the measured per-locus λ of about 1–6 (RNA and DMS) and the soft gene-level value of about 24 or 12 or 2.4 (by basis).
- **D2c (Wald):** unchanged; this does not test hemoglobin.
