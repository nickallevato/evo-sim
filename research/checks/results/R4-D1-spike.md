# R4 D1 spike: how many interchangeable alternatives per needed change do real(ish) sequence spaces offer?

Branch D. This measures the quantity G1 left open (R4-G1.md section 3). G1 found that Day's "specific outcome" product p^n stops binding once the Poisson mean number of successful arisings per required change, λ = m·(−ln(1−q)), passes **λ₅₀ = 12.3–17.2** (n_f = 1.6e5 to 2e7). λ₅₀ is 7.3 at n_f = 1e3, 9.6 at 1e4 and 10.3 at n_f = 2e4 (about the number of human genes; the gene count is my figure, not from the corpus). With Day-family inputs (N = 1e4, μ = 1.2e-8, s = 0.01, T = 3e5; q = 0.381) one alternative is worth λ_alt = 0.48, so the flip needs m* = 15–36 alternatives per change. G1's own m* table gives 16–36 at this basis and 32–74, 152–358, 311–735 on its other bases (d-corrected T 146,250 with s = 0.01; T = 3e5 with s = 0.001; both). λ_alt is exactly linear in s (λ_alt = 48·s at T = 3e5), so every λ below can be rescaled to any s. Two stand-ins were measured: RNA folding (ViennaRNA 2.7.2) as a genotype-to-phenotype map, and deep mutational scanning (ProteinGym).

Claims touched or informed: D, D1, D1a, D1b, D1d, D2c, D2h (directly), D2i, D3, D4, D9a, D10–D12, D15 (context), and the G3b dilemma. No claim file, argmap, README, gaps.md, RESULTS.md or REVIEW.md was edited.

**Revision note.** This is the revised version after three reviews (correctness, Day steelman, critic steelman). The first version, committed as e70363d, is in git history. Every review finding is answered, with status, in the "Review resolution" section at the end. New computations are post hoc scripts committed before they ran (§1).

## 0. Headline

### 0.1 What is being asked, and the axis of readings

The two steelman reviews pull in opposite directions on one point: which reading of "the same needed change" counts. I do not choose. The measurement is shown along that axis, from the most specific reading to the most inclusive, and along a second axis, selection strength s. The four argumentative positions it touches are:

| Tag | Position | Source |
|---|---|---|
| H1 | **Day's specific-outcome horn.** The particular fixations matter, so p^n applies. | Day, voxday.net 2026-10-01, ¶28–29 (G3b): "Either the specific fixations matter — in which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t explain the observed functional divergence." |
| H2 | **Day's "neutral noise" horn.** Interchangeable, tolerated substitutions. | same sentence |
| H3 | **The middle case.** Alternatives that each achieve the same needed function (G1's formalisation: n_f requirements, m alternatives each). | R4-G1 §3 |
| H4 | **Any n of M.** Evolution needs only that some n of a large pool of candidate mutations fix, not a pre-specified set. | Camestros, CA4 ¶10 (2026-01-29): "the probability that SOME number is picked is close to 1"; McCarthy, MC1 ¶48: evolutionary history "does not require that an exact group of 20 million mutations become fixed—only that some 20 million out of an enormous pool of candidate mutations become fixed." (as quoted in the claim and quote files) |

**H4 is not tested by the per-requirement rows below.** Camestros and McCarthy argue about which loci, drawn from a pool; the per-requirement m measures something else. The H4 comparison that the data can support is the beneficial-fraction comparison in Table B. G1 §3 formalised H4 as "any n of M" and credited the logic ("the lottery logic is correct, but has no numbers"). D1 supplies a first measured fraction.

### 0.2 Table A: alternatives per requirement, across the axis of readings

m∣reach is the mean number of distinct single mutations reaching the outcome, given at least one does. m_all is the same averaged over all (genotype, outcome) pairs (zero where there is no route), which is the per-requirement number in G1's sense. For DMS rows m is an expected count over codons, so m_all = m. λ = m·λ_alt(s = 0.01) = 0.48·m. The last column is the s at which λ (using m∣reach, or m for DMS) reaches λ₅₀ for n_f = 1e3 and for n_f = 2e7 (T = 3e5; double it for T = 146,250). Values above about 0.05 are outside any plausible s, and the Haldane 2s used by G1 overstates q at s ≥ 0.03, so 0.03–0.05 is a stress test.

| Reading (loosest at the bottom) | Tests | Medium | m given reach (median [range over targets or datasets]) | m_all | λ at s=0.01: given reach / m_all | s at which λ hits λ₅₀ (n_f 1e3 → 2e7) |
|---|---|---|---|---|---|---|
| Exact structure S2 | H1 | RNA, 15 targets (upper bound for proteins; partner redundancy) | 2.3 [1.5–4.5] | 0.051 | 1.1 / 0.024 | 0.066 → 0.155 |
| Exact S2, ≥ 5 bp from S1 (post hoc E0far) | H1 | RNA | **1.5** [1–2.3] | 0.003 | 0.72 / 0.0014 | 0.10 → 0.24 |
| Exact S2, the selected tRNA cloverleaf | H1 | RNA, L=76 | 1.5 (E0far 1.0) | 0.007 | 0.73 / 0.0035 | 0.10 → 0.23 |
| Within 2 base pairs of S2 | H3 (strict) | RNA | 3.4 [2.1–5.1] | 0.088 | 1.65 / 0.042 | 0.044 → 0.104 |
| Same abstract shape, pre-registered E2 (dominated by "a helix was lost") | H3 (lenient; degradation-inflated) | RNA | **28** [14.5–45] | 24.9 | 13.4 / 12.0 | 0.005 → 0.013 |
| Same shape, S2 not a loss of helices, L ≥ 76 (post hoc E2g) | H3 | RNA | 11.8 [4.5–25] | 7.5 | 5.7 / 3.6 | 0.013 → 0.030 |
| Same shape, rare shapes only (post hoc E2rare; low by construction) | H3 | RNA | 4.5 [1–6.6] | 1.06 | 2.2 / 0.51 | 0.034 → 0.08 |
| Tolerated nonsynonymous SNVs at one codon (s* ≥ 0.5; not a needed change) | **H2** | DMS, 114 non-stability sets | 5.06 of 6.6 missense [2.5–6.5] | = m | 2.4 | 0.030 → 0.071 |
| Near-WT tolerated at one codon (s* ≥ 0.8) | H2 | DMS | 3.51 [1.5–5.7] | = m | 1.69 | 0.043 → 0.102 |
| **Beneficial-proxy SNVs at one codon** (s* ≥ 1.2, upper bound; the needed-change analogue) | H3 | DMS | **0.21** [0–2.6] | = m | **0.10** | 0.74 → 1.74 (never) |
| Beneficial-proxy SNVs anywhere in the mutated region (a gene-level pool) | H3 at gene granularity; H4 within a gene | DMS | **51** [0–1,760]; 17% of datasets have zero | = m | 24 | 0.003 → 0.007 |

How to read Table A:
- **Exact readings (H1) are below the flip at s = 0.01 and stay below at s = 0.05 for every n_f** (λ of 1.1 to 5.5 for exact S2 across s = 0.01–0.05, against λ₅₀ of 7–17). The ≤ 2 bp class (strict H3) is below at s = 0.01 and reaches the flip near s = 0.044 for n_f = 1e3. Using m_all instead of m∣reach lowers λ by a further factor of about 45 (exact S2) or 500 (E0far).
- **The tolerance reading (H2, one codon): below at s = 0.01, at the flip at s of about 0.03–0.04 for n_f of 1e3–1e4.** The critic review's s of 0.03–0.05 is right for this row. These DMS rows count tolerated substitutions. By G3b's own words that is the "neutral noise" horn. They are not alternatives that each carry s = 0.01, so applying λ_alt to them is an upper-bound exercise. The needed-change analogue is the beneficial-proxy row, which is below 1 per codon.
- **The lenient topology reading (E2) sits in the flip band; the refined versions do not.** That depends on which version is believed (see 0.4).
- **The gene-level beneficial pool is the only row far above the flip at s = 0.01, and it is the least secure** (see 0.5).

### 0.3 Key facts for each side (both stated here, not only in §6)

**For Day (H1, ruggedness, rarity):**
- Exact-outcome λ is about 1 or below: RNA exact S2 m∣reach 2.3 and m_all 0.05; the post hoc far-from-S1 class E0far gives m∣reach 1.5, m_all 0.003; the selected tRNA gives 1.5 and 0.007. Only 1.8% of (genotype, accessible-outcome) pairs have any one-step route (tRNA 0.5%).
- 70% of single RNA mutants change the exact structure; paired sites are neutral only 9% of the time.
- GB1 four-site landscape (Wu 2016): **95.0% of variants are below 0.3 of WT**; at single-nucleotide steps there are **87 functional local maxima** (67–158 across improvement margins 0–0.3) and only 44% of functional variants have a monotone uphill path to the best variant (30–51% across margins). A random-uphill walk ends at the global maximum for 5.8% of functional starts and 1.1% from WT.
- D2h's sentence "reduce or destroy", scored as worded, passes: a majority of single substitutions fall below 80% of the WT-like level in 61% of datasets (51–74% across my six normalisations; 51–77% in the correctness review's).
- Beneficial singles per codon: 0.21, so the per-codon needed-change pool is empty for most codons.
- A gene's beneficial pool is shared: with 51 proxy-beneficial SNVs, a gene that needs k = 25 adaptive changes succeeds with probability 0.07 at s = 0.01 (k = 50: 4e-20); at s = 0.001 even k = 10 gives 1e-4 (Table C).
- At Day-family μ a short locus fixes only 0.03–0.06 neutral substitutions per window, against a median of 36–80 neutral steps needed to reach a background with a one-step route to an exact S2 (§3.5). Drifting across the network does not rescue a single short locus.

**For the critics (H3, H4, connectivity, smoothness):**
- **71%** of single substitutions keep at least half of the WT-like level (68–77% across my six normalisations; 65–77% in the correctness review's). "Destroy" (below 20%) is a median 11% (6–15%), and a majority is destroyed in 1–3% of datasets. Fully intolerant sites are 3.8%.
- GB1: the functional set is **one giant connected component** (99.8–99.9% of functional variants, with WT in it). **98.5%** of functional variants have an uphill SNV neighbour (97–99% across margins; 99.7% at amino-acid level). Monotone uphill SNV paths reach WT-level fitness from 99.9% of functional variants, and a random-uphill walk ends at a mean of 5.9 times WT.
- RNA neutral networks are huge: the tRNA cloverleaf has about 10^33 sequences. Samples drawn uniformly from the network differ from each other at 0.73·L positions (a random pair: 0.75·L).
- Several distinct mutations give the same outcome: m∣reach 2–5 for exact structures. The RNA topology class without helix loss has m∣reach 11.8 at L ≥ 76, and one L = 100 target reaches 25 (λ 12 at s = 0.01).
- **Any-n-of-M (H4), the first measured comparison (Table B):** the within-gene proxy beneficial fraction (3.6%, an upper bound) exceeds G1's required fraction by 82–1,600× for n ≤ 2e5 (p = 0.02 or 0.002 as in G1; 84–1,600× in the critic review's rounding), and by 8–16× for n = 2e7 at p = 0.02 (0.8–1.6× at p = 0.002).
- Mean "deleterious" does not imply "rugged": ruggedness needs local optima, and RNA graded landscapes have almost none away from the target.

**Where the data are silent:** Axe, Taylor, Keefe & Szostak per-sequence prevalence (D10–D12), cross-family connectivity (Eden's arithmetic, D3), and regulatory waiting times (D15) are untouched. The DMS leg measures single-step neighbours of extant optimised proteins.

### 0.4 Fired triggers, and how the reading changed

The pre-registration docstring (commit d72c733) lists four conditions that "would change the reading". Two fired outright, one partly, one not:

| Trigger | Observed | Status |
|---|---|---|
| m_E2 per genotype ≥ 16 at L = 30–50 | **37.3 (L=30), 24.4 (L=50)** | **FIRED** |
| DMS destroyed fraction a majority in > 30% of datasets or < 3% | **2%** (fires on the "< 3%" side) | **FIRED** |
| m_E0 conditional mean ≥ 3 | L=30: max 4.45; L=100: median 3.1; 15-target median 2.3 | partly met |
| RNA strict deleterious fraction < 0.4 | 0.70 | not fired |

How the reading changed:
1. **E2.** The pre-registered claim "λ below 12–17 for every single-genotype definition" is **falsified for the pre-registered lenient class** (λ = 13.4, in the band). I then judged it a degradation artefact (§3.3) and introduced refined classes after seeing the result. Those are post hoc and must be read with that in mind. They are shown in **both directions**: E2g (λ 3.4; 5.7 at L ≥ 76; one L = 100 target at 12) and E2rare (λ 2.2) lower the critic-favourable number, and E0far (m∣reach 1.5, m_all 0.003) lowers the exact-outcome number toward Day's. E2rare is low by construction (it selects shapes seldom reached, §3.3), so E2g is the defensible refined class. The honest range for "same topology" is therefore 3–13 in λ at s = 0.01, depending on the definition, and the flip is inside that range at s = 0.01–0.03 for the larger molecules. My earlier summary ("below for every single-genotype definition") is withdrawn.
2. **"Destroy".** The pre-registered reading allowed that a < 3% share would change the reading. It does, in the critics' direction for "destroy alone", and it leaves "reduce or destroy" (61%) standing (§4.1). The earlier sentence "neither side's strong form is supported" is replaced by statements tied to specific claims (0.3, §6).
3. **E0.** The partial trigger (m_E0 ≥ 3 at some sizes) moves in the critics' direction, and E0far moves it back.

### 0.5 Gene-level pool, Table B (H4) and Table C (shared pool)

**Table B: G1's required beneficial fraction against the measured within-gene proxy fraction.** Required fraction = n/(p·supply), G1 §3 with supply 4.5e11 (McCarthy) or 2.3e11 (G1's Gd basis). Measured proxy fraction (s* ≥ 1.2; an upper bound with no noise null): median 0.0357, IQR 0.0056–0.0918; 14% of datasets have exactly zero.

| n required | p | Required fraction | Median measured / required | Datasets at or above | If only 1% of mutations fall in such genes |
|---|---|---|---|---|---|
| 2e5 | 0.02 | 2.2e-5 to 4.3e-5 | 820 to 1,600× | 86% | 8 to 16× |
| 2e5 | 0.002 | 2.2e-4 to 4.3e-4 | 82 to 160× | 85–86% | 0.8 to 1.6× |
| 2e7 | 0.02 | 2.2e-3 to 4.3e-3 | 8 to 16× | 76–80% | 0.08 to 0.16× |
| 2e7 | 0.002 | 2.2e-2 to 4.3e-2 | 0.8 to 1.6× | 47–57% | 0.008 to 0.016× |

The genome-share row is illustrative (the 1% is not sourced) and shows that the comparison depends on how much of the genome behaves like the scanned genes. Nothing here covers noncoding or regulatory sequence (D15). Bias: noise inflates the proxy (it cuts for Day); saturated assays with WT-buffered scores hide improvements and deflate it (it cuts for the critics). Both are untested. A lab-assay gain is not natural fitness, and the proxy's fraction above W is not the fraction with s = 0.01.

**Table C: a gene as k needed changes drawing on one shared pool of m proxy-beneficial SNVs.** P(at least k of m succeed), each succeeding with G1's q.

| Basis | k = 10 | k = 25 | k = 50 |
|---|---|---|---|
| s = 0.01, T = 3e5 (q = 0.381), median m = 51 | 0.999 | 0.074 | 4e-20 |
| s = 0.01, T = 146,250 (q = 0.209) | 0.64 | 7e-6 | 4e-33 |
| s = 0.001, T = 3e5 (q = 0.047) | 1.1e-4 | 4e-20 | 2e-65 (1.7e-65) |
| Share of the 114 datasets with P ≥ 0.5 (first basis) | 61% | 42% | 21% |

So the gene-level pool does clear the flip for a gene needing about ten adaptive changes at s = 0.01 and not for a gene needing twenty-five or more, and it does not at s = 0.001. This is the stepping-stone direction G1 §3 flags. The per-requirement λ of 24 in Table A treats each requirement as having the whole pool to itself, so it overstates for k > 1.

Caveats specific to this row: the 0–1,760 spread is wide (17% of datasets have no proxy-beneficial SNV, the 90th percentile is 369). The proxy is relative to my W estimate and is not tested against replicate noise: at the W-defining sites the share at s* ≥ 1.2 (median 9.7%) exceeds the mirror share at s* ≤ 0.8 (14.2%, which includes real damage) in only 29% of datasets. So in about 70% of datasets the proxy cannot be distinguished from a symmetric noise tail, using the damage-contaminated mirror as the upper bound on noise.

## 1. Runs, provenance, labelling

| Item | Value |
|---|---|
| Pre-registered script | `research/checks/d1_sequence_space_spike.py`, commit d72c733. Predictions P1–P11 and the "what would change the reading" block are in its docstring, written before any main run. |
| Summarizer-only edit | commit 582428a (post hoc: NaN-safe medians, coverage ≥ 0.5 group). The workhorse ran the 582428a version (md5 42f8da52…); the DMS and GB1 parts ran locally on d72c733, and the measurement code is identical. |
| Host and versions | na-workhorse, ViennaRNA **2.7.2**, numpy 2.5.3, scipy 1.18.1, Python 3.14.4. `research/requirements.txt` pins ViennaRNA, numpy and scipy to these (the original run pinned only ViennaRNA; numpy and scipy were then unpinned but at the same versions; pandas is not used). |
| Main runs | `nn` 2231 s; `rna` 2123 s (12 processes); `dms` 14 s and `gb1` 22 s on the workstation. |
| Seeds | `SeedSequence([20261090, part, config, rep])` |
| Data | ProteinGym substitutions zip, retrieved 2026-10-09 from `https://marks.hms.harvard.edu/proteingym/ProteinGym_v1.3/DMS_ProteinGym_substitutions.zip`, sha256 `3a83766254ac9ac9984ec25cb73c6e010ea4418f5e35f143933e6b6e6473b921`; reference file from `https://raw.githubusercontent.com/OATML-Markslab/ProteinGym/main/reference_files/DMS_substitutions.csv`, sha256 `a8f498011532a74aa9fe556a50555a75e928c5837d19c06a87592ae04049b308`. Under `sources/raw/d1-dms/` (gitignored, read as CSV only, never executed). The "v1.3" label is from the URL; the reference file's own version column reads "1" and "0.1". |
| Post hoc, labelled, in order | `d1_posthoc_refine.py` (committed 88dda5a before its run, workhorse 732 s). `d1_posthoc_gb1_snv.py` and `d1_aggregate.py` were first committed together with their outputs (8b4acfd), not before; the main outputs themselves were also committed only at that point (02:32), so the order of main output and post hoc design rests on file times and docstrings. **Fix pass:** `d1_fix_dms.py`, `d1_fix_gb1.py`, `d1_fix_rna_fp.py` (commit 40d9261 before any run; the RNA script ran on workhorse with 6 processes, 1039 s, md5 70f3a275…) and `d1_fix_aggregate.py`. |
| Outputs | `results/raw/d1_*.json`, `d1_*.out`, `d1_summary.txt`, `d1_aggregate.txt`, `d1_fix_*`, `d1.host`, `d1_fix.host`. |

**Disclosures.**
- Before the pre-registration commit I looked at the GB1 score quantiles (to fix WT = 1) and the DMS metadata. The first clause of P11 is not blind.
- The tiny RNA smoke runs printed ν ≈ 0.32.
- A coverage ≥ 0.5 subset was added after the first DMS look (post hoc), because sparse datasets gave NaN site statistics. The headline group is the 114 of 140 non-stability sets that pass it; the all-non-stability group (n = 140) gives similar medians (functional 0.725 vs 0.711).
- The DMS sets are not independent: the 114 datasets cover 91 distinct proteins (TEM-1 appears four times). Protein-level medians (averaging within protein) are the same to within 0.01 for the fractions (functional 0.713, reduced 0.542, destroyed 0.115) and 4.30% vs 3.57% for the proxy.

## 2. Definitions used

**RNA.** The genotype is an RNA sequence; the phenotype is the MFE structure at 37 °C; "neutral" means unchanged MFE structure.

| Class | Meaning |
|---|---|
| m_E0 (strict) | Number of distinct single-nucleotide mutants of x (folding to S1) whose structure is exactly S2. |
| m_E1 (medium) | The same, structure within 2 base-pair differences of S2; S2 restricted to d_bp(S1,S2) ≥ 5. |
| m_E2 (lenient) | The same, sharing S2's level-5 abstract shape (helix nesting and branching only; helix length and loops ignored); S2's shape differs from S1's. The cloverleaf is `[[][][]]`. |
| Post hoc | E0far (d_bp ≥ 5); E2g (shape differs and helix count ≥ S1's); E2rare (shape accounts for ≤ 1% of the neighbourhood); E2g_rare (both). |
| m_ben | Number of single mutants strictly closer in base-pair distance to a target S*. |
| Doubles | All C(L,2)·9 double mutants reaching the class while neither single component does. |

S2 is drawn from the distinct non-neutral structures in the one-step neighbourhoods of a sample A of neutral genotypes; m is measured on a different sample B. A and B come from the same Metropolis chain, so they are distinct but not independent. "S2 uniform over distinct structures" is dominated by rare, mostly large-change structures (median d_bp(S1,S2) = 22); the frequency-weighted pool is shown too. Fitness for the graded analysis and the walks is minus the base-pair distance to a named target S*, so those walks are known-target constructions in the sense of D2i and D9a (§3.4). The λ = m·0.48 mapping is exactly G1's model: λ_alt = −ln(1−q) = 0.480, provided each counted alternative is one specific single-nucleotide change (rate μ/3), which is how RNA m and DMS m_snv are defined. It assumes reach = 1 when m∣reach is used; the unconditional m_all is shown beside it.

**Targets (15).** Yeast tRNA-Phe (L = 76, folds exactly to the cloverleaf), plus random-sequence-derived structures: four each at L = 30 and 50, three each at L = 76 and 100, with ≥ 0.25·L pairs and ≥ 2 helices. These are drawn from folded random sequences, so they are biased toward common structures. 70–100 neutral genotypes per target.

**DMS.** ProteinGym's own binarisation is a median split for 126 of 217 sets, so I normalised: s* = (score − N̂)/(Ŵ − N̂), with N̂ the median of the lowest 5% of singles and Ŵ the median score at the most tolerant quartile of sites. Thresholds are my choices: functional s* ≥ 0.5, near-WT s* ≥ 0.8, "reduced" s* < 0.8 (contains "destroyed"), "destroyed" s* < 0.2, beneficial proxy s* ≥ 1.2. The proxy is relative to Ŵ, not to a measured WT score (ProteinGym files carry no WT row). **Sensitivity** (`d1_fix_dms.py`, six estimator combinations): functional 0.68–0.77 (stored 0.711), reduced 0.50–0.63 (0.534), destroyed 0.06–0.15 (0.111), majority-reduced in 51–74% of datasets (61%), majority-destroyed in 1–3% (2%), proxy fraction 0.6–4.2% (3.6%). "A few points" in the first version understated this. Also: at the W-defining (most tolerant) sites themselves, 14% [9–23%] of substitutions already fall below s* = 0.8, so part of the "reduced" share is assay spread or mild damage at the most tolerant sites. The 54 sets with an author-chosen manual cutoff give fit 0.672 (unfit 0.328) against my s* ≥ 0.5 on the whole group at 0.711.

## 3. RNA results

### 3.1 Neutral networks and neutrality (P1, P2)

- **Network size** N_NN = 6^bp·4^unp·f, with f the fold frequency among pair-compatible sequences (validated against exact enumeration of 4^10 sequences: ratios 0.99–1.02, in the correctness review). tRNA cloverleaf: f = 2.2e-4 (67 hits), N_NN ≈ **10^33.2** (95% interval 10^33.1–33.3), a fraction **10^−12.6** of the 4^76 space.

| L | log10 N_NN | log10 fraction of 4^L | Hits behind the estimates |
|---|---|---|---|
| 30 | 11.4–13.3 | −4.7 to −6.6 | 240–19,724 |
| 50 | 19.4–21.6 | −8.5 to −10.7 | 3 (rand50_3: ±0.5 dex), 46, 132, 3,330 |
| 76 | 31.6–33.2 | −12.5 to −14.1 | 201, 14, 67 (tRNA); one target has 0 hits (≤ 10^32.3) |
| 100 | 41.8–42.4 | −17.8 to −18.5 | 3 and 2 (each ±0.5 dex); one target has 0 hits (≤ 10^44.0) |

- **Spread.** The first version quoted "0.56·L between sampled genotypes" as evidence of spread, which is a mixing diagnostic of the walk and not a property of the network. Genotypes drawn **uniformly** from the neutral set (rejection from pair-compatible sequences, 40 + 40 per target, seven targets with f ≥ 1e-4) differ at **0.73·L** on average (0.70–0.74), against 0.55·L for the walk samples (0.50–0.59) of the same size. The network is wide. The walk under-mixes at paired sites. Mean neutrality from the walk and from uniform draws differ by +0.008 on average (per-target −0.016 to +0.025; uniform SE about 0.008), which is not distinguishable from zero.
- **Reach is mildly inflated by the walk.** On the seven targets the walk gives 1.3× (E0) and 1.25× (E1) the uniform reach in aggregate (sums of reach), with a per-target scatter of 0.3–3.3× and 20–60 pairs behind each. This is the same order as the correctness review's 1.1–1.7× (and the same direction: toward the critics). m∣reach is not distinguishable between samplers at this sample size (E0: 2.1 uniform, 3.6 walk; E1: 4.6, 3.2). The main-run reach numbers should therefore be read as upper values by about a quarter.
- **Neutrality.** Mean ν is 0.30 [0.23–0.43] over 15 targets; tRNA 0.313. Paired sites 0.094 [0.03–0.14], unpaired 0.545 [0.44–0.78]. Only one of 15 targets exceeds ν_c = 1 − 4^(−1/3) = 0.37 (quoted from memory), so ν alone does not show percolation. The samples are joined to their seed by explicit neutral paths, so the walk shows a spread-out connected region; it does not show that all structure-S1 sequences lie in one component.

### 3.2 Day's ruggedness framing in RNA (P5)

Fraction of the 3L single mutants that are "deleterious" under three equivalence rules:

| Rule | All 15 targets | tRNA |
|---|---|---|
| Structure changed (strict) | **0.70** [0.58–0.77] | 0.69 |
| More than 2 bp from S1 | 0.56 [0.40–0.68] | 0.57 |
| Different abstract topology | 0.27 [0.16–0.50] | 0.44 |

Day's "most single changes alter the outcome" holds for exact-structure identity. It weakens but does not vanish as "same function" is loosened; for the tRNA cloverleaf 44% of single mutations change the topology.

### 3.3 Alternatives per change (P3, P4)

By size class, m∣reach and reach (E0far and E2g are post hoc):

| Class (pool) | L=30 | L=50 | L=76 (random) | L=100 | tRNA76 |
|---|---|---|---|---|---|
| E0 uniform | 2.5, 2.4% | 2.1, 1.7% | 1.9, 1.5% | 3.1, 1.8% | 1.5, 0.5% |
| E0far (post hoc) | 1.8–2.3 | 1.3–1.8 | 1.0–1.8 | 1.4–1.7 | 1.0, 0.03% |
| E1 uniform | 4.1, 7.8% | 3.6, 2.8% | 3.1, 1.8% | 2.6, 2.5% | 2.6, 0.6% |
| E2 uniform (pre-reg) | 37, 100% | 24, 92% | 17, 77% | 27, 76% | 29, 90% |
| E2g (post hoc) | n/a (0–2 candidates) | 2.6–9.4 | 4.5–15 | 12–25 | 5.9, 19% |

Observed versus predicted:
- **E0:** predicted 1.0–1.6, found 2.3. **The post hoc E0far class gives 1.5 [1–2.3], inside the predicted band**, so part of the miss is pool composition. The likely further cause, untested, is that the two partners of a lost pair and the up to three alternative bases at one site give the same disrupted structure.
- **E1:** predicted 1.3–3, found 3.4. **E2:** predicted 2–12, found 28.

**Why E2 is inflated.** A genotype's one-step neighbourhood contains few abstract shapes (median 5 [2–18]; the top 3 hold 99% of neighbour instances); on average 33% of changed neighbours have fewer helices than S1 and 62% keep S1's shape. Level 5 ignores helix length, so "a helix was lost" dominates. A shape class that holds 38 of the 90 neighbours at L=30 is a class of damaged versions. **E2rare** removes the commonest shapes, but it also selects shapes seldom reached, so it is low by construction; I do not rely on it. **E2g** (shape changes without a loss of helices) is the defensible refinement: m∣reach 7.2 over 12 targets, 11.8 at L ≥ 76 (λ 5.7); per target at L ≥ 76: 20.0, 11.9, 25.3 (L=100), 15.4, 8.4, 4.5 (L=76), and the tRNA 5.9. With the unconditional m_all the corresponding λ at s = 0.01 are 7.2, 3.6, 9.4 at L=100 and 0.5–4.8 at L=76. At L=100, two of three targets are therefore at or near λ₅₀ for n_f = 1e3–1e4 (7.3–9.6). Real proteins are longer than these molecules, so the L trend is in the direction of the critics. At L=30 E2g is undefined: the one-step shape repertoire of a 30-mer is 2–3 shapes.

**Doubles** (pairs with no single route): exact S2 3.8% [1.8–7.7] with m2∣reach 4.7; E1 8.6% [3–30] with 8.9; E2 93% with 105 [20–398] (degradation again). I predicted 10–300 routes for E1/E2 doubles; E1 was lower.

### 3.4 Graded fitness (−d_bp to a target) and walks (P5, P6)

| Start distance d0 | Targets | Improving neighbours | Worse neighbours | At least one improver | Strict local optimum |
|---|---|---|---|---|---|
| 1–4 bp | near | 1.0% | 69% | 0.53 | **0.47** |
| 5–10 bp | near | 3.4% | 65% | 0.88 | 0.12 |
| ≥ 11 bp | near | 31% | 33% | 0.996 | 0.004 |
| ≥ 11 bp | far | 41% | 19% | 1.0 | 0 |

- "Near" S* are accessible structures that are mostly damaged versions (median d_bp from S1 of 22); "far" are MFE structures of random sequences. Neither is a functional structure, so these tables test how a path to a damaged or random structure behaves, not adaptation toward a functional one. The "improving" fraction at large d0 is partly bookkeeping (removing any wrong pair lowers d_bp). I withdraw the first version's use of the large-d0 m_ben as support for a gene-level λ.
- **Adaptive walks** (random improving neighbour, neutral drift up to a budget): success 0.77 [0.17–0.85] near and 0.73 [0–0.93] far; trapped with no move 0 in every case, because an equal-distance neighbour always exists, so the "trapped" column cannot measure ruggedness; failures are drift-budget exhaustion at a mean final d_bp of 0.2–2.4 for L ≤ 50 (tRNA: 5–6 with 6 walkers).
- **These walks are known-target.** Fitness is the distance to a target the programmer names, which is the construction D2i and D9a criticise (Day: "it works because Dawkins specified the target string, the fitness function, and the selection rule", as quoted in D2i). They show that RNA structure space is navigable under a smooth designed metric; they do not show that biology supplies one. The measured-landscape version of the walk is on GB1 (§4.2).

### 3.5 Multi-step exploration of the neutral network (first passage, post hoc)

This tests the critic argument that a population need not sit on one genotype. From 16 start genotypes per target (8 targets, L ≤ 50), a neutral walk makes accepted single-nucleotide substitutions that keep the structure (4.5 proposals per accepted step), and at every step I check whether the current genotype has a one-step route to each of 60 sampled S2 (pool from independent genotypes). Fraction of (start, S2) pairs with a route by step n, median over targets:

| Class | step 0 | 5 | 20 | 50 | 150 | median first passage among those found |
|---|---|---|---|---|---|---|
| E0 exact | 1.2% | 2.5% | 3.5% | 5.9% | 11.2% | 54 steps (36–80) |
| E1 ≤ 2 bp | 5.2% | 8.2% | 14.1% | 21.1% | 34.1% | 30 steps (26–46) |
| E2g (L=50 targets) | 43% | 61% | 88% | 95% | 100% | 1 step (0–59) |

Conversion to the Day-family window: a locus of L sites fixes L·μ·ν·T neutral substitutions over T generations: **0.033–0.058 for L = 30–50 at T = 3e5 (0.016–0.028 at T = 146,250)**. The expected number of segregating neutral variants at any time is 4NμLν ≈ 0.004–0.008 per locus. So at Day-family μ a single short locus cannot walk across its network within the window, either for exact outcomes (tens of steps needed) or for E1. For E2g the answer is mostly "already adjacent" (step 0 for 43% of pairs). Neutral exploration matters at much larger μ·L (viral or bacterial scales, or many loci in parallel), which is outside the Day-family basis of G1. The static "pooled over K genotypes" counts of the first version (2 to 30 for exact S2, hundreds for E2g) are withdrawn as a supply measure: with K genotypes sharing a population of size N, each carries N/K copies, so the arising rate of a given S2 is 2Nμ/3 times the mean (not the sum) of the per-genotype m. The first-passage numbers are the time-resolved replacement. They were run on L ≤ 50 only.

## 4. DMS results

### 4.1 What the 114 non-stability sets show (P7–P10)

Medians, with the inter-quartile range in brackets (earlier tables use the range over targets or datasets).

| Quantity | Value | Predicted |
|---|---|---|
| Single substitutions functional (s* ≥ 0.5) | **0.71** [0.59–0.79] (0.68–0.77 across normalisations) | 0.45–0.75 |
| Near-WT (s* ≥ 0.8) | 0.47 [0.37–0.57] | 0.25–0.55 |
| Reduced (s* < 0.8) | **0.53** [0.43–0.63] (0.50–0.63) | 0.45–0.75 |
| Destroyed (s* < 0.2) | **0.11** [0.08–0.18] (0.06–0.15) | 0.10–0.40 |
| Datasets with a majority reduced | 61% (51–74%) | – |
| Datasets with a majority destroyed | 2% (1–3%) | ≤ 15% |
| Sites with ≤ 10% of substitutions functional | **3.8%** [1–10] | 10–35% |
| Sites with ≥ 90% functional | 38% [22–53] | 10–40% |
| Functional alternatives per site, of 19 amino acids | 13.5 [11.3–15.1] | 6–13 |
| Functional alternatives per codon (tolerated SNVs; 6.6 missense + 0.4 stop SNVs per codon) | **5.06** [4.5–5.7]; 77% of missense SNVs | 1.8–4.0 |
| Near-WT alternatives per codon (s* ≥ 0.8) | 3.51 [1.5–5.7] | – |
| Beneficial-proxy alternatives per codon | **0.21** [0.03–0.57] | – |
| Beneficial proxy fraction (s* ≥ 1.2, upper bound) | 3.6% [0.6–9.2] (0.6–4.2% across normalisations) | 0.5–6% |

The first version divided by "7.0", which includes 0.4 stop-codon SNVs; the missense total is 6.6. The count of functional alternatives per codon is unaffected. 66 stability sets (ΔG proxies) look similar: functional 0.77, reduced 0.47, destroyed 0.087. Named cases: TEM-1 Stiffler 2015 functional 0.575, destroyed 0.20; Firnberg 2014 functional 0.448, destroyed 0.376, 22% fully intolerant sites; GB1 Olson 2014 functional 0.783.

**D2h, claim by claim (Day, voxday.net 2026-10-06 ¶5).** "Single-residue changes to most proteins tend to reduce or destroy function. The fitness landscape is rugged, not smooth."
- **"Reduce or destroy", as worded: passes.** The disjunction is scored by "reduced" (s* < 0.8, which contains "destroyed"): a majority of singles is reduced in **61%** of datasets (median share 0.53; 51–74% across normalisations), which meets "most proteins". Two qualifications: 14% of substitutions at the most tolerant sites already score below 0.8 (assay spread or mild damage), and by the authors' own cutoffs in the 54 manual-cutoff sets the median fit fraction is 0.67 (so 0.33 unfit), which is not "most singles reduce or destroy".
- **"Destroy" alone: a minority** in 98% of datasets (median 0.11). Day did not claim a majority is destroyed, so this is not a refutation of his sentence; it bounds the strong reading.
- **"Rugged, not smooth":** a statement about local optima and epistasis, which one-step data cannot test. GB1 (§4.2) supports it at single-nucleotide steps in one subspace and does not support isolation.
- **"Eden's concerns confirmed":** not tested here; DMS covers neighbours of extant proteins, not the rarity of function in sequence space.
- Day cites no study. The numbers are mine, with my normalisation.

### 4.2 GB1 four-site complete landscape (Wu 2016; 149,360 of 160,000 variants plus the WT; WT = 1 assumed)

An "uphill" step here means a gain of **more than 0.1 of WT** (the first version called it "strictly uphill" without stating the 0.1 margin; the margin guards crudely against assay noise, which has no calibrated model, and ProteinGym provides no replicate SEs). Unobserved variants are treated as absent. Margin sensitivity (functional = fitness ≥ 0.5; 5,822 variants):

| Margin | Amino-acid steps: maxima, reach top | SNV steps: maxima | SNV: functional with an uphill neighbour | SNV: reach top (best variant) |
|---|---|---|---|---|
| 0 | 15, 98.9% | 67 | 98.8% | 51% |
| 0.05 | 16, 98.7% | 79 | 98.6% | 47% |
| **0.1 (reported)** | 18, 98.5% | 87 | 98.5% | 44% |
| 0.2 | 21, 97.3% | 109 | 98.1% | 37% |
| 0.3 | 26, 94.6% | 158 | 97.3% | 30% |

- The ruggedness result at SNV level is robust to the margin (maxima 67–158, reach 30–51%). At margin 0 the pre-registered "less than half reach the top" is marginally missed (51%).
- **Counts at other thresholds:** functional variants are 7,534 (≥ 0.3), 5,822 (≥ 0.5), 4,309 (≥ 0.8), 3,644 (≥ 1.0), 3,142 (≥ 1.2). 95.0% are below 0.3. Of the 76 single substitutions from WT, 36% are ≥ 0.5, 26% ≥ 1 and 20% ≥ 1.2 (the beneficial-proxy threshold), and 53% are below 0.2.
- **What the "reach the best variant" criterion is.** It is the exact-outcome reading again. Evolution needs a good variant, not the single best. Monotone uphill SNV paths reach fitness ≥ WT from 99.9% of functional variants (the maxima's fitness: median 4.0 times WT, quartiles 2.2–5.3, minimum 0.52). A **random-uphill walk** (each step uniform among uphill neighbours, exact by dynamic programming, margin 0.1) ends at the global maximum for 5.8% of functional starts (from WT: 1.1%; amino-acid steps: 31% and 9%), at a mean of 5.9 times WT at SNV steps (7.1 at amino-acid steps) and at ≥ WT level in 99.9% of cases. This is the D1b/D2i test on a measured, designer-independent landscape (complete, one subspace). It does not get trapped at poor optima and it rarely finds the top.
- **Day:** 95% nonfunctional; 87 maxima; 44% reach the top; the global maximum is rarely found by a walk.
- **Critics:** one giant component holding 99.8–99.9% of functional variants (2 components at amino-acid steps, 5 at SNV steps; the WT in the largest); 98.5% of functional variants have an uphill neighbour; 87 maxima are 1.5% of the functional set; walks end at 5.9 times WT.
- The SNV adjacency is the union over codons of the WT amino acid and is more permissive than any one genotype, so SNV reach is an upper bound and the maxima counts are lower bounds. 6.6% of the 160,000 variants are unobserved (only 42 of the 87 SNV maxima have all neighbours observed, per the correctness review).

## 5. Prediction scorecard (corrected)

| # | Prediction | Result |
|---|---|---|
| P1 | ν 0.25–0.55 (tRNA 0.25–0.50); ≥ 70% of targets above 0.37; unpaired 0.6–0.9, paired 0.15–0.45 | ν **held** (0.30; tRNA 0.313). Percolation share **failed** (1 of 15). Unpaired **partly failed** (median 0.545; only L=30 inside the band). Paired **failed** (0.09). |
| P2 | tRNA 10^30–37; L=30 fraction 1e-4..1e-1; L=100 1e-12..1e-5 | tRNA **held** (10^33.2). L=30 **failed** (all four at 10^−4.7 to −6.6, below the band). L=100 **failed** (10^−17.8 to −18.5). |
| P3 | m∣reach E0 1.0–1.6, E1 1.3–3, E2 2–12; unconditional reach E0 0.03–0.3, E1 0.1–0.5, E2 0.2–0.8; λ below 12–17 for every single-genotype definition | m∣reach **failed** for E0 (2.3), E1 (3.4), E2 (28); post hoc E0far (1.5) is inside the band. Reach **failed** (0.018, 0.031, 0.91, all outside; the frequency-weighted E0 reach, 0.18, is inside). "λ below the flip" **held for E0 and E1, failed for pre-registered E2 (13.4)**, held for the post hoc E2g and E2rare. |
| P3 pooled | Pooled E2 over ≥ 40 genotypes is 50–400, above m* | **Failed on magnitude** (445–2,700), and the premise is withdrawn: pooled counts do not measure supply (§3.5). |
| P4 | Doubles: P(m2≥1) 0.3–0.9 and 10–300 routes for E1 and E2 | E2 **held** (0.93; 105). E1 **failed** (0.086). |
| P5 | Deleterious: strict 0.45–0.75, medium 0.25–0.55, lenient 0.05–0.30 | Strict **held** (0.70). Medium **marginal** (0.56). Lenient **held on the median** (0.27) but not at L=30 or tRNA (0.40–0.50). |
| P6 | At least one improver 0.6–0.95; improving 1–8%; equal 30–60%; worse 30–65%; strict optima ≤ 30%; near walks ≥ 85%; far walks 20–70% | d0 5–10: **held** (0.88; 3.4%; equal 0.3–0.45; worse 0.65 at the edge; optima 0.12). d0 1–4: **failed** (0.53; worse 0.69; optima 0.47). Near walks **failed** (0.77, budget-limited). Far walks **slightly above** the band (0.73). |
| P7 | Functional 0.45–0.75; reduced 0.45–0.75; destroyed 0.10–0.40; majority destroyed ≤ 15% | **All held** (0.71, 0.53, 0.11, 2%). |
| P8 | Intolerant sites 10–35%; tolerant 10–40% | Intolerant **failed** (3.8%). Tolerant **held** (38%, top edge). |
| P9 | m_aa 6–13; m_snv 1.8–4.0; λ_site 0.9–1.9; gene-level functional hundreds to thousands; beneficial 5–150 | m_aa **marginally failed** (13.5). m_snv **failed** (5.06). λ_site **failed in magnitude** (2.4), same direction. Gene-level **held** (1,110; 51). |
| P10 | Proxy fraction 0.5–6%; compare to G1's required fraction | Fraction **held** (3.6%). The pre-registered **comparison** was omitted from the first version and is now in Table B. |
| P11 | > 90% nonfunctional; ≥ 30 local maxima; < 50% reach the top; ≥ 70% in one component | Nonfunctional **held** (not blind). Maxima and reach **failed at amino-acid steps** (18; 98.5%), **held at SNV steps** (87; 44%, post hoc; the correctness review recomputed 82 maxima over fitness ≥ 1, as the prediction was worded). Component **held** (99.9%). |

**Net.** The direction held for exact and near-exact classes and for the DMS fractions. My point estimates for RNA alternatives, neutrality components and network sizes were often off. The largest miss was E2, and it fired a pre-registered trigger (§0.4).

## 6. Reading for the G1 flip

### 6.1 Across s

λ = m·λ_alt(s), with λ_alt = 48·s at T = 3e5 (Haldane 2s; overstated at s ≥ 0.03, so those columns are stress tests), using m∣reach for RNA rows:

| Row | m | s=0.001 | s=0.01 | s=0.03 | s=0.05 |
|---|---|---|---|---|---|
| RNA exact S2 | 2.3 | 0.11 | 1.1 | 3.3 | 5.5 |
| RNA exact, ≥ 5 bp (E0far) | 1.5 | 0.07 | 0.72 | 2.2 | 3.6 |
| RNA ≤ 2 bp (E1) | 3.4 | 0.17 | 1.65 | 4.9 | 8.2 |
| RNA topology without helix loss, L ≥ 76 (E2g) | 11.8 | 0.57 | 5.7 | 17 | 28 |
| DMS one codon, tolerated | 5.06 | 0.24 | 2.4 | 7.3 | 12.1 |
| DMS one codon, near-WT | 3.51 | 0.17 | 1.7 | 5.1 | 8.4 |
| DMS one codon, beneficial proxy | 0.21 | 0.01 | 0.10 | 0.30 | 0.49 |
| DMS gene, beneficial proxy | 51 | 2.4 | 24 | 73 | 122 |
| λ₅₀ for n_f = 1e3 / 1e4 / 2e4 (genes) / 2e5 / 2e7 | | 7.3 / 9.6 / 10.3 / 12.6 / 17.2 | | | |

At s = 0.01 the exact and near-exact rows are below the flip. The one-codon tolerance row reaches the flip near s = 0.03–0.04 (n_f of 1e3–1e4); the exact rows need s of 0.07 or more. The gene-level beneficial pool is above the flip at s = 0.01 and below it at s = 0.001, and at the 0.001 basis the k-of-m probabilities in Table C are negligible. Using the unconditional m_all instead of m∣reach lowers every RNA exact row by a further factor of 40 or more.

### 6.2 The answer, by granularity

1. **Per-locus or exact-outcome needs (H1): below.** λ of about 1 or below; G1 gives P ≈ 10^−176 for n_f = 1e3 at λ = 1.1. This reproduces Day's specific horn at m of about 1.5–5 per genotype; it is close to definitional (the exact-structure class is the specific-outcome reading) and does not test whether requirements are site-specific. It does not support "m ≈ 1" as a description of biology, and it does not refute it either (see 0.3 and below).
2. **Tolerance (H2): below at s = 0.01,** crossing near s = 0.03–0.04. These are Day's "neutral noise".
3. **Middle case with a topology criterion (H3): inside or below the flip depending on the definition and on L,** 3–13 in λ at s = 0.01, with a trend upward with molecule size.
4. **Gene-level beneficial pool and the beneficial fraction (H3 at gene granularity, H4): above the flip for genes needing about ten changes at s = 0.01, not for twenty-five or more, not at s = 0.001, and wide in spread.** Table B puts the within-gene proxy fraction well above G1's required fraction for n ≤ 2e5.
5. **G1's caveats stand.** Independence and equal s favour the interchangeable case; stepping-stone dependence and functional-island structure lower the effective m. All numbers are single-step, single-genotype, equal-s.

**On the "m ≈ 1" and "strong form" sentences of the first version.** "Day's m ≈ 1" came from my own pre-registration docstring, not from a Day quote; the nearest Day text is the G3b "specific" horn. It is withdrawn as an attribution. Likewise "the critics' strong form (plenty of interchangeable alternatives, so the barrier vanishes)" has no quoted source. The critics' position is H4 (Camestros CA4 ¶10; McCarthy MC1 ¶48), which D1 does not test beyond Table B, and Bowers' qualitative "multiple mutational paths can lead to similar phenotypes" (as quoted in R4-G1 §7), which D1 supports qualitatively (m∣reach 2–5 for exact RNA structures). What the data support, tied to claims:
- Day's weaker form (locus-level m of a few, SNV-level ruggedness in GB1, 95% nonfunction across four sites, and "reduce or destroy" in most datasets) is supported.
- Day's reading that functional sequences are isolated is not supported in GB1 (one component of 99.8%).
- The critics' qualitative point that several routes reach the same outcome and neutral networks are large is supported; their numerical H4 comparison (Table B) favours them for n ≤ 2e5 and is borderline for n = 2e7 at p = 0.002.
- Rosenhouse, p.124 (as transcribed in D1a): protein-space geometry makes Eden's combinatorial calculations "look hopelessly naive". The local connectivity quantities he alludes to are now measured (neutral networks of 10^33 in RNA, 71% of singles functional, a 99.8% giant component in GB1), which is partial support at the local level; "hopelessly naive" is an unquantified overstatement relative to this evidence, because D1 does not touch Eden's cross-family 20^250 arithmetic or the per-sequence prevalence figures.
- Camestros' D1d observation that the book ignores post-1966 developments is supported in the sense that the quantitative post-1966 literature (ProteinGym, MaveDB-type data, Wu 2016) exists and is usable.

**Credit.**
- **Day:** exact-outcome λ about 1; 98% of accessible-outcome pairs lack a one-step route; 70% of single RNA mutants change the structure; paired sites 9% neutral; GB1 95% nonfunctional with SNV-level ruggedness robust to the margin; "reduce or destroy" in 61% of datasets; zero or near-zero beneficial pool per codon; the shared-pool and diminishing-returns structure of a gene; the neutral-network walk is too slow at Day-family μ. Day's prediction D2h that DMS shows ruggedness is partly right.
- **Critics:** large, wide neutral networks; several routes per outcome; destroyed singles a minority; intolerant sites rare; GB1's functional set connected, with uphill neighbours for 98.5% and walks ending well above WT; the within-gene beneficial fraction exceeds G1's requirement by 82–1,600× for n ≤ 2e5; "mostly deleterious" does not mean "rugged". McCarthy conceded the specific-list case (G1) and Camestros' CA4 logic is correct as logic; D1 supplies the first number for its premise.
- **Critic and Day errors recorded, with sources:** Day (G3b) frames the choice as a dilemma that omits the middle case (G1). D2h cites no study. Rosenhouse's "hopelessly naive" is stronger than the local data allow. McCarthy and Camestros' arguments are about pool and loci, which the per-requirement analyses here do not touch.

## 7. External validity: how each caveat cuts

RNA secondary structure is a toy for proteins and regulation. The DMS leg is real protein data, but it is single-step evidence about extant optimised proteins. Convention in this table: "Favours X" means the measurement artefact makes X look better than it is.

| Caveat | Direction |
|---|---|
| RNA toy status: 4-letter alphabet with base pairing, a unique MFE structure as "function", no tertiary structure, ligands or kinetics. | Unknown overall. |
| RNA partner redundancy (either partner of a pair, up to three bases) inflates m_E0 relative to protein residues. Marked on the RNA rows of Table A. | **Favours the critics** (m too high for proteins). |
| Structure identity is a stricter definition of function than a real element has. | **Favours Day** for E0/E1 (m too low); the E2 numbers go the other way (too high, degradation). |
| Random-sequence-derived targets are biased to common structures. The selected tRNA reaches less (reach 0.5% for E0; m_all 0.007; E0far 1.0). | **Favours the critics** for the 14 random targets, and Day for selected structures. The 15-target median is a critic-leaning summary of the specific question; the tRNA is shown separately. |
| S2 is drawn from structures accessible from the network (reach is conditional). | **Favours the critics.** |
| The walk sampler inflates reach by about a quarter (1.25–1.3× in aggregate). | **Favours the critics.** |
| Post hoc classes: E2g and E2rare lower critic-favourable numbers, E0far lowers Day-favourable ones; they were designed after seeing E2, and E2rare is low by construction. | Net: E2g/E2rare **favour Day**, E0far **favours Day**, E2g at L ≥ 76 shows the critic-leaning trend. |
| Equal s for all alternatives (G1's assumption and mine). | **Favours the critics.** |
| Per-genotype m, no standing variation. Real populations carry few neutral variants (about 0.004–0.008 neutral variants per locus at Day-family μ); they also do not aggregate m by summation (§3.5). | Per-genotype m is the correct supply measure; the earlier "pooled" counts **flattered the critics** and are withdrawn. |
| DMS: lab assays at saturating selection, WT buffered by design; ProteinGym chooses well-behaved sets; stability sets measure folding. | **Favours the critics** for tolerance, and also **hides improvements** (deflates the beneficial proxy: favours Day). |
| DMS: normalisation and Ŵ are mine; the beneficial proxy has no noise null and is inflated by noise (and by the 14% baseline of the "reduced" share). | **Favours the critics** for the proxy and its gene-level count (upper bound); the "reduced" share is also inflated by baseline spread (**favours Day**). |
| DMS covers neighbours of extant optimised proteins and nothing about connectivity across families. Axe, Taylor and Keefe & Szostak (D10–D12) are a separate regime. | **Favours neither;** it leaves Day's cross-family claim untested. |
| DMS sets are not independent (91 proteins in 114 sets). | Small; protein-level medians are the same. |
| GB1: one interface subspace chosen for epistasis; SNV adjacency is the codon union (reach is an upper bound); margin 0.1. | **Favours Day** for ruggedness (chosen subspace); the permissive adjacency **favours the critics**. |
| RNA walks (and "far/near") use a designed target (D2i/D9a). | **Favours the critics** (smoothness is by construction); the GB1 measured-landscape walk is the discriminating one. |
| First-passage: only L ≤ 50, one μ basis. | **Favours Day** at Day-family μ; unknown at larger μ·L. |
| Regulatory and noncoding sequence (D15) was not measured. | Open. |

## 8. Limits and open items

- 15 RNA targets, 70–100 genotypes each, and one tRNA. Ranges are across targets, not confidence intervals; some NN-size estimates rest on 2–3 hits.
- MFE only; d_bp is crude; the walks have tight budgets and 6 walkers on the tRNA.
- E2 is shape-level 5 only. The ProteinGym multi-mutant sets (doubles and higher) were not analysed: how fast the functional fraction decays with the number of substitutions is the Day-relevant rarity test that one-step data cannot give. Not done in this pass.
- The first-passage run covers L ≤ 50 and the Day-family μ. A short-walk pooled count within realistic divergence was not run.
- DMS thresholds and the W proxy are mine (sensitivity in §2). GB1 WT = 1 is assumed (the file has no WT row). The mirror check for the proxy is damage-contaminated and does not replace a replicate-based null.
- Not done: protein folding maps (lattice or HP), real multi-site sets across families, regulatory alternatives per change.

## 9. Verdict suggestions (not applied; the lead integrates)

Existing vocabulary: internal (holds / pending / non-sequitur / arithmetic-error / n/a), fidelity (accurate / partial / unverifiable / misread / n/a), external (supported / contested / contradicted / untestable / pending / n/a).

| Claim | Suggested | Comment |
|---|---|---|
| D (sequence-space-wistar) | external: **contested** (unchanged) | The spike bears on local landscape structure only: exact-outcome λ about 1; GB1 rugged at SNV steps yet one connected component. Per-sequence prevalence (D10–D12) and cross-family connectivity are untouched. |
| D1 (Rosenhouse ch.4) | external: **contested** (unchanged) | Not tested directly; sub-claims D1a, D1b below. |
| D1a (protein-space geometry makes Eden naive) | external: **contested** (unchanged), comment: partial support at the local level | Local connectivity he alludes to is now measured and favours him (10^33 RNA networks, 71% functional singles, 99.8% GB1 component). "Hopelessly naive" is unquantified and goes beyond: Eden's cross-family arithmetic is untouched, and the exact-outcome λ is about 1. |
| D1b (simulations are commonplace) | external: **contested** (unchanged) | RNA walks are known-target (D2i). On the measured GB1 landscape, random-uphill walks end at a mean of 5.9 times WT and rarely at the best variant (5.8%): navigable, not trapped, not finding the top. |
| D1c | external: **contested** (unchanged; chapter not read) | No evidence from D1. |
| D1d (no developments since 1966) | external: **pending → supported** for the existence part (comment) | The quantitative post-1966 literature exists and is usable (ProteinGym, Wu 2016); Day's D2h cites none. Whether it settles the Wistar question is separate. |
| D2c (Wald hemoglobin) | external: **contested** (unchanged), comment | Hemoglobin is not tested. Modern DMS: 53% of singles score below 80% of the WT-like level, but 71% keep at least half; Wald's "markedly change the properties" is compatible with retained function. |
| D2h (DMS shows ruggedness) | external: **contested**, comment: partial support | "Reduce or destroy" passes as worded in 61% of datasets (51–74% across normalisations; 14% baseline); "destroy" alone is a minority (11%; majority in 2%); author cutoffs give 0.67 fit. "Rugged": real at SNV steps in GB1, but the functional set is connected. "Eden confirmed": untested. Fidelity stays unverifiable (no study cited). |
| D2i (designed fitness) | external: **contested** (unchanged), comment | The RNA walks here are known-target and so illustrate the objection. The discriminating test is on a measured landscape (GB1): uphill walks do not get trapped at poor optima. Internal stays holds (existence-proof reading). |
| D3 (Eden arithmetic) | unchanged (internal holds, fidelity accurate); external **contested** | Arithmetic is unaffected; whether the comparison bears on search depends on landscape structure, which is what D1 measured locally. |
| D4 (Ulam serial) | external: **contested** (unchanged), comment | The serial assumption is not tested. The shared-pool structure (Table C: k = 25 changes from 51 beneficial SNVs gives 0.07 at s = 0.01) is the stepping-stone logic. |
| D9a (Weasel opposite) | external: **contested** (unchanged), comment | Known-target; RNA walk results are Weasel-like and uninformative on this. |
| D10, D11, D12 | external: **contested** (unchanged) | Per-sequence prevalence regime untouched. The 71% functional singles refer to neighbours of a functional sequence, not to random sequence space. |
| G3b / G1 open item | replace "per-site m is not established" | Measured per-locus λ of about 1–6 (RNA and DMS at s = 0.01); gene-level pool of 51 beneficial SNVs (median; spread 0–1,760) that clears the flip for k ≈ 10, not k ≥ 25, not at s = 0.001; within-gene beneficial fraction 82–1,600× G1's requirement for n ≤ 2e5, 8–16× for n = 2e7 at p = 0.02. |

## Review resolution

Status: **applied**, **partly applied**, **declined** (with reason). Reviews: C = correctness; DM/Dm = Day steelman major/minor; KM/Km = critic steelman major/minor.

### Correctness review (REVIEW-R4-D1-correctness.md)

| # | Status | Resolution |
|---|---|---|
| C1 triggers fired | **applied** | §0.4 lists the four triggers; E2 and the DMS-destroyed one fired; reading restated; refinements shown in both directions (E0far, E2g, E2rare). |
| C2 pooled counts | **applied** | Pooled-count credit removed; 1/K copy-number point stated (§3.5, §7); per-genotype mean used; first-passage run added (post hoc). The pre-registered P3-pooled flaw is noted in §5. |
| C3 GB1 margin | **applied** | 0.1 margin stated and full margin table in §4.2; "strictly uphill" replaced; noise and unobserved-neighbour caveats added. |
| C4 Hamming/under-mixing | **applied** | §3.1: uniform-draw numbers (0.73·L vs 0.55·L), reach inflation about a quarter (1.25–1.3× aggregate, scatter 0.3–3.3×), "disjoint" reworded; ν difference reported. My own run gives a smaller inflation than the review's upper figure. |
| C5 mapping, m_all, m* | **applied** | λ = m·0.48 stated as assuming reach = 1; m_all column in Table A; G1's m* quoted. |
| C6 scorecard slips | **applied** | §5 corrects P2, P3 (unconditional reach scored), P3-pooled, P6, P11 (82 maxima ≥ 1), P1. |
| C7 E0far | **applied** | In Table A, §3.3 and §5. |
| C8 normalisation range, 14% baseline | **applied** | §2 and §4.1 with the six-variant sensitivity and the 14% baseline. |
| C9 stop codons | **applied** | "of 6.6 missense (plus 0.4 stop)" in Table A and §4.1. (The review's 6.8/0.48 is a different averaging; mine is the site-weighted median over the 114 sets.) |
| C10 NN uncertainty | **applied** | Hits per target in §3.1; ±0.5 dex noted for 2–3 hits. |
| C11 provenance | **applied** | URL, date, sha256 in §1; requirements pins numpy and scipy (pandas unused). |
| C12 provenance order | **applied** | §1 states that the two post hoc scripts were committed with outputs and that workhorse ran 582428a. |
| C13 walks, S* nature | **applied** | §3.4: success is budget-limited, "trapped" cannot measure ruggedness, S* are damaged or random structures, E0 pool composition. |
| C14 non-independence | **applied** | §1: 91 proteins in 114 sets, protein-level medians, n = 140 group cited. |

### Day steelman (REVIEW-R4-D1-steelman-day.md)

| # | Status | Resolution |
|---|---|---|
| DM1 tolerated is the neutral horn | **applied** | Rows relabelled H2; beneficial-proxy-per-codon row added (0.21, λ 0.10); the "5 of 7" sentence replaced. |
| DM2 "m ≈ 1" strawman, E0far, m_all | **applied** | Attribution withdrawn (§6.2); E0far and m_all in Table A; "too low" statement removed; unconditional reach stated. |
| DM3 gene-level unit, k-of-m, proxy | **applied** (noise null **partly**) | Table C (k = 10/25/50, two s); datasets with zero beneficial (17%); spread; share at or above; the mirror check is the only null available and is damage-contaminated, so the proxy is flagged as having no replicate-based noise null. |
| DM4 disjunction | **applied** | §4.1 scores "reduce or destroy" (61%) and "destroy" alone (2%), author cutoffs (0.67 fit, 0.33 unfit), the 14% baseline and normalisation ranges. |
| DM5 multi-change/GB1 in headline, doubles | **partly applied** | GB1 in §0.3 and §4.2 with the margin table. The ProteinGym multi-mutant decay analysis was **declined for this pass** (not in the coordinator's list; needs a new design); listed as open in §8. |
| DM6 pooling | **applied** (short-walk pooled count **declined**) | Pooled credit removed; first-passage run instead of a within-divergence pooled count (which would answer the same question less directly). The "pooled sets are 56% diverged" point is accepted and superseded by the uniform-draw numbers. |
| DM7 symmetric refinement, margin, adjacency | **applied** | E0far in headline; margin table; SNV-union direction stated in §0.3 and §7. |
| Dm1 ≥ 0.8 rows | **applied** | Table A row near-WT (3.51; λ 1.69). |
| Dm2 author-cutoff 0.33 | **applied** | §4.1. |
| Dm3 RNA partner-redundancy mark | **applied** | Table A medium column and §7. |
| Dm4 m_ben as support | **applied** | Withdrawn in §3.4. |
| Dm5 tRNA separate | **applied** | Row in Table A, §3.3 table column, §7. |
| Dm6 GB1 thresholds, WT = 1 | **applied** | Counts at 0.3/0.5/0.8/1/1.2 in §4.2; WT absence noted. |
| Dm7 horn column | **applied** | Table A "Tests" column and the tag table in §0.1. |
| Dm8 "neither side's strong form" | **applied** | Replaced by claim-specific statements (§0.3, §6.2). |

### Critic steelman (REVIEW-R4-D1-steelman-critic.md)

| # | Status | Resolution |
|---|---|---|
| KM1 specific = tautology; H4 untouched | **applied** | §0.1 tags, "Tests" column, explicit statement that H4 is not tested by the per-requirement rows; Camestros and McCarthy named. |
| KM2 P10 comparison | **applied** | Table B, with the omission acknowledged (§5 P10). |
| KM3 gene-count λ₅₀, saturation, zero share | **applied** | λ₅₀ for n_f = 2e4 (10.3) in the text and §6.1; saturation bias in §0.5 and §7; zero share 17%/14%. The reword "at or above the flip" is replaced by a k-dependent statement. |
| KM4 upward s | **applied** | §0.2 crossing column and §6.1 table for s = 0.001–0.05; the one-codon and exact rows reach the flip at s of about 0.03–0.04 and 0.07+. |
| KM5 multi-step exploration | **applied** | First-passage run (post hoc, script before run) and the supply-sharing argument in §3.5; the check that the argument fails at Day-family μ is reported, with its limits (L ≤ 50). |
| KM6 E2rare selection, E2g by L | **applied** | E2rare flagged low by construction; E2g per-target and by L in §3.3; L ≥ 76 line in Table A. |
| Km7 GB1 outputs | **applied** | 98.5%, 20% of WT singles ≥ 1.2, 36% ≥ 0.5, maxima fitness quantiles, reach to ≥ WT, "reach the best" tagged as the exact-outcome criterion (§4.2). |
| Km8 known-target walks, measured-landscape walk | **applied** | §3.4 flags D2i/D9a; random-uphill walks on GB1 run (post hoc). |
| Km9 balanced §0 | **applied** | §0.3 states both sides' facts with numbers. |
| Km10 unsourced "strong form" | **applied** | Removed; quoted critics named; Bowers noted as G1-quoted. |
| Km11 claims list, D1a credit | **applied** | Header list extended (D1, D1a, D1b, D1d, D2i, D9a); D1a credited and bounded (§6.2, §9). |
| Km12 "Favours" convention, single-genotype row | **applied** | Convention defined and rows re-tagged (§7). |
| Km13 connectedness wording | **applied** | §3.1: explicit neutral paths show a connected region; not all of NN. |
| Km14 reduce-baseline tag and m_all column | **applied** | §7 tag; m_all column in Table A. |
