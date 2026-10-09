# R4 E: founder-event CMMRD hazard (E, E3) and relictation (E4)

Scripts (committed after the main run; see the provenance gap below):
- `research/checks/e_founder_hazard.py`: exact Markov chains plus seeded MC.
- `research/checks/e4_relictation_chain.py`: exact chains plus one seeded MC cross-check.

Runs (each line is `research/.venv/bin/python -I research/checks/<script>.py [arg]`):

| Script | Argument | Time | Status |
|---|---|---|---|
| `e_founder_hazard.py` | none | 437 s | main, pre-registered |
| `e_founder_hazard.py` | `supp` | 25 s | post hoc |
| `e_founder_hazard.py` | `supp2` | 248 s | post hoc, review fix pass |
| `e4_relictation_chain.py` | none | 620 s | main, pre-registered |
| `e4_relictation_chain.py` | `supp` | 48 s | post hoc, review fix pass |

MC seeds are `SeedSequence([20261008, cfg])`. Raw output is in `results/raw/e_founder_hazard{.out,.json,.time}`, `e_founder_hazard_supp{,2}{.out,.time}`, `e4_relictation_chain{.out,.json,.time}` and `e4_relictation_chain_supp{.out,.time}`.

The pre-registered predictions are in each docstring and were written before any run; no timing run came first. Everything produced by `supp`, `supp2` and E4 `supp` is **post hoc and not pre-registered**. In the fix pass the function `p_no_event` was renamed `p_event`; it returns P(event), and no number changed.

**Provenance gap.** Nothing is committed, so the docstring's pre-run state cannot be proven. Its mtime is consistent with the main run, but future runs should hash the docstring first.

## Claims restated (verbatim, punctuation as in the source; sources/raw/day, read only)
| Claim | Quote and locator | Type |
|---|---|---|
| E: 6/12 | "Six of the twelve populations independently evolved hypermutator phenotypes through destruction of DNA repair systems: four via mismatch repair defects (mutS/mutL) and two via oxidative damage repair defects (mutT)." (Z23020792 Abstract). Per-population assignment, §2: "Four populations (Ara−2, Ara−3, Ara−4, Ara+3) acquired defects in mutS or mutL ... Two populations (Ara−1, Ara+6) evolved defects in mutT ... (Couce et al. 2017; Maddamsetti & Grant 2020)." "With n = 12, the exact binomial 95% confidence interval is approximately 21–79%" (§2) | empirical (literature) + arithmetic |
| E: 2.3% | "The probability of sampling at least two carriers — the minimum required to produce a homozygous offspring — is approximately 5–6% per founder event (from the binomial distribution with n = 100, p = 0.0036)." Also: "1 − e⁻⁰·⁵ ≈ 39%. This estimate is conservative". Also: "approximately 0.06 × 0.39 ≈ 2.3% per founder event. This is a per-event risk. Whether it is evolutionarily consequential depends on how many founder events PE's model posits and whether the affected individuals survive long enough to affect population fitness, questions that warrant formal demographic modeling." (Z23020792 §5.1) | arithmetic on a model; consequence explicitly deferred |
| E3 | "At N = 100 founders and G = 50 generations with full selection, the simulation produces P(≥1 CMMRD-equivalent homozygote) = 2.33%" (Z23034852 §3.2). Stronger wording: "The throughput constraint and the CMMRD homozygosity pathway are independently sufficient." (Abstract; again in §6.1). "founder events, rather than being engines of rapid speciation, are minefields" (§6.5). Credit: "The honest correction on hitchhiking probabilities in sexual vertebrates narrows the scope" (§6.4), and the conclusions "rest on the throughput constraint and the CMMRD pathway, not on hitchhiking" (§5.4) | model result + inference |
| E4 | "a single family can replace more than ~10% of the population, the formula t̄ = 4Nₑ breaks ... Below 10% replacement, the formula holds to within the few-percent finite-size offset of the Wright-Fisher chain itself". Also: "exceed 4Nₑ by up to 7–25% at 2N = 20–50, an excess that keeps growing with population size". Also: "p = 1/(2N) ... holds exactly regardless of offspring distribution" (Z23188201 Abstract). Body disclosure, §2: "The thresholds are consequently not fixed percentages", and a fixed family "returns toward the drift baseline as the population grows" | model result (exact chain) + interpretation |

## Procedure
**E/E3.** The script uses an exact chain on the newborn allele count j. The aa count k given j comes from random pairing: C(N,k)C(N−k,j−2k)2^(j−2k)/C(2N,j). The event of interest is made absorbing.

Two selection formulations are run:
- **`real`:** finite-individual selection on realized genotype counts. This is the literal reading of §3.1.
- **`hwe`:** mean-field selection on Hardy-Weinberg *expected* genotype frequencies. This is the textbook diploid WF-with-selection form, and §3.1's "genotype-frequency-weighted fitnesses" admits it.

Cross-checks:
- An independent "no-hit kernel" implementation agrees to 4 digits.
- MC at 50k and 200k reps agrees.
- The correctness reviewer independently checked the chain: brute-force path enumeration matches to 1e-15, and the reviewer's own MC agrees.

Consequence endpoints: cohort mean fitness w̄ below a threshold in some generation, q ≥ 10%, and expected aa births. Growth variant (post hoc): N_t = min(N0·gᵗ, 1000).

Inputs:
- **Sourced:** q = 0.0018, N 50–1,000, G, s_hom 0.95, s_het 0.05, CMMRD incidence 1e-6.
- **Assumed:** an equal four-gene split.
- **From memory, unverified:** the Win 2017 per-gene carrier frequencies, used for sensitivity only.

**E4.** Day's jackpot chain is built exactly as specified, with m = min(round(f·2N), 2N−1). P_fix comes from a linear solve. t̄ uses the h-transform, which equals Day's (I−Q)g = 1 to 1e-13 (reviewer). Ne_var is computed at every i.

Baselines: WF, Moran, and a copy-level MC. The SD of t̄ comes from the second moment of the h-transformed chain (post hoc).

Diploid pair-family chain (my construction): two parents, K offspring individuals replacing K others, and copies randomly re-paired into individuals each generation. A post-hoc variant has the parents die.

## Results: E / E3 (N = 100, G = 50, q = 0.0018 unless stated)
**Day's arithmetic.**
- P(≥2 carriers | Bin(100, 0.0036)) = 0.0509. That is inside Day's own "5–6%"; he used the top of his range (0.06). 0.0509 × 0.3935 = 2.00%, which is also inside his range.
- The real faults are elsewhere:
  - **The "≥2 carriers, the minimum required" premise.** Founders with one copy give 68% of the modelled hazard.
  - **The 39% conditional.** It assumes Hardy-Weinberg sampling with replacement (N·q² = 0.010 aa per generation). Two copies randomly paired give 1/(2N−1) = 0.0050 per generation. 1 − (1 − 1/199)⁵¹ = 22.7%, which almost equals the exact pure-drift value of 22.8%. Drift adds only about +0.1 point.
- Clopper-Pearson 21–79% and cumulative 21.0 / 69.2 / 90.5% hold.
- Day's "This estimate is conservative" is **right about expected aa births** and wrong about P(≥1). Given 2 founder copies, E[aa births over 50 generations] = **6.1** under pure drift, against his Poisson mean of 0.5. Under full selection it is 0.39 (post hoc).

**The literal model vs Day's simulation:**
| Regime | exact `real` | exact `hwe` | MC `real` (50k) | MC `real` (200k, 2nd seed) | Day |
|---|---|---|---|---|---|
| full | **2.752%** | 2.383% | 2.61 ± 0.07 | 2.750 ± 0.037 | 2.33% |
| s_het = 0 | 4.077% | 3.561% | 4.05 ± 0.09 | | 3.62% |
| pure drift | 4.077% | 4.077% | 4.02 ± 0.09 | | 3.94% |

**`real` formulation.**
- s_hom cannot affect P(≥1 aa), because the metric stops at the first aa. This is a property of the metric.
- The selection reduction is 33%, all from s_het, against Day's 41%. That figure is model-dependent (33–41%), not wrong.

**`hwe` formulation.** It is the better-fitting of the two tested formulations; uniqueness was not tested. Day's code was not seen. Evidence for it:
- s_hom visibly matters in Day's Table 4 (3.62 vs 3.94; ≈ 2.7 SE by my count at 50k reps each, about 5 SE per the correctness reviewer). That cannot happen under `real`.
- Tables 2–5 (supplement) agree within 2 MC SE, with two exceptions. Table 3 at N = 500, G = 100 (5.68 vs 6.01) is −3.1 SE. Table 2's selection-free P(≥2 copies) at N = 500 (52.8 vs exact 53.74) is −4.2 SE, which suggests Day's per-cell sampling noise at N = 500 exceeds a 50k-rep SE.
- `real` is rejected against Day's tables by 5–6 SE.

**Table 8 (§4.2, different code with load and fitness feedback)** is **not reproduced by either formulation**:
- `real` fits the mid-range f_m (0.005–0.01).
- Day is above both formulations at f_m = 0.001.
- Day is 3–11 SE below `real` at f_m ≥ 0.02.

**Decomposition (real, full selection).**
- One founder copy: P = 0.2515, P(hom | 1) = 7.5%, giving 68% of the hazard.
- Two copies: 15.9% (22.8% under drift).
- ≥2 copies: 17.0%, giving 32% of the hazard.
- P(hom | c) is nearly linear in c (7.5, 15.9, 24.9%).

**Sweep (real, full selection, G = 50 → 10,000).**
- P(≥1 aa) = 1.85% (N = 50), 2.75% (100), 4.02% (200), 6.5% (500) and 9.2% (1,000), flat in G beyond about 200. Pure drift also saturates.
- **Isolate growth (post hoc)** *raises* it, because more births occur at the inherited frequency. From N0 = 100, g = 1.02 / 1.05 / 1.1 / 1.2 / 1.5 / 2 per generation (cap 1,000) give 3.03 / 3.53 / 4.46 / 6.00 / 8.05 / 9.02% at G = 50. The per-birth rate still falls.

**Per-gene treatment.**
- Pooled q as one locus implies CMMRD at 1 in 309,000, which is 3× Day's own 1 in 1,000,000.
- An equal 4-gene split gives 1 in 1.23M, and the Win-memory split gives 1 in 0.98M.
- Day's "per-gene allele frequency q ≈ 0.002" is the pooled figure.
- The **hazard barely moves**: 0.97× at N = 100 and 0.92× at N = 500. This also means "multiple loci omitted, so conservative" (§3.1) adds little.

**Consequences: threshold sweep (post hoc; real, full selection, G = 50).** A single aa birth lowers that generation's w̄ by s_hom/N (0.0475 at N = 20, 0.0095 at N = 100). Heterozygotes (s_het) also count, so at small N, P(w̄ < 0.99) can exceed P(≥1 aa).

| N | P(≥1 aa) | E[aa births \| hit] | ratio P(≥1 aa) / P(w̄ < t), t = 0.99 / 0.98 / 0.97 / 0.95 / 0.90 | P(w̄ < 0.5) |
|---|---|---|---|---|
| 20 | 1.07% | 2.49 | 0.88 / 1.0 / 1.0 / **1.35** / 5.6 | 6e-10 |
| 30 | 1.37% | 2.53 | 0.95 / 1.0 / 1.0 / 4.9 / 24 | 3e-13 |
| 50 | 1.85% | 2.54 | 0.99 / 1.2 / 4.8 / 18 / 550 | below floor |
| 100 | 2.75% | 2.45 | **1.15 / 6.4 / 31 / 619** / 1e6 | below the 1e-13 numerical floor |
| 200 | 4.02% | 2.26 | 7.2 / 130 / 2,500 / 9e5 / – | below floor |

At N = 100 the absolute values are P(w̄ < 0.99) = 2.40%, < 0.98 = 0.43%, < 0.97 = 0.088% and < 0.95 = 0.0044%. Under `hwe` they are 2.08 / 0.34 / 0.060 / 0.0020%.

Over 100 independent events at N = 100, ≥1 aa birth has probability 93.9% and a ≥5% dip 0.44%.

Hits come in clusters: a hit means about **2.5 affected births**, not one. These thresholds are the audit's own choice (0.95 and 0.5 were pre-registered; the rest is post hoc). No demographic or extinction model was run.

**LTEE (text checks).**
- Tenaillon 2016: "six populations (Ara–1, Ara–2, Ara–3, Ara–4, Ara+3 and Ara+6) had 96.5% of the point mutations, having evolved hypermutable phenotypes caused by mutations that affect DNA repair or removal of oxidized nucleotides". Ara+1 is a seventh, IS150, hypermutator.
- Good 2017: "Six populations evolved a mutator phenotype".
- The two-pathway statement is corroborated by Tenaillon's Extended Data phylogeny legend (text copy, lines 238/240). It names "lineages with mismatch-repair defects" and "mutT mutators", without counts.
- Day's per-population 4+2 assignment is sourced to Couce 2017 and Maddamsetti & Grant 2020 (Z23020792 §2). The citation sits after the mutT sentence. Neither paper was retrieved.
- Both LTEE papers report later antimutator decline. This supports Day's cost premise. It concerns the *rate* of further accumulation and does not contradict irreversibility of load already accumulated.

## Results: E4 relictation
**Baselines (pass).**
- WF t̄/4N = 0.9318 / 0.9523 / 0.9697 at 2N = 20 / 30 / 50 (Day: 0.932 / 0.952 / 0.970).
- Moran = 1 − 1/(2N).
- |u(i) − i/2N| ≤ 1e-12 in every chain printed (≤ 1.2e-13 over Day's table; 5.7e-13 for WF at 2N = 3,200).
- MC at 2N = 30, f = 0.5: P_fix 0.0336 (1/30) and t̄ 82.5 ± 0.5, against exact 83.1.

**Day's table reproduces to ≤ 0.0004** with Python `round`; half-up misses one cell. The ratio is independent of pj. Excess over the WF chain:

| f | 2N = 20 / 30 / 50 |
|---|---|
| 5% | +2.0 / +3.2 / +2.4% |
| 10% | +3.9 / +4.9 / +6.6% |
| 50% | +14.9 / +20.3 / +27.7% |

**Ne and growth.**
- Ne_var = 1/(2c), with c = pj·m(m+1)/(2N(2N−1)), the pairwise coalescence probability. It is constant in i, and the leading eigenvalue rate equals c exactly. **Variance, pairwise-coalescent and eigenvalue Ne all coincide here, and t̄ still departs from 4Ne.** The departure therefore comes from multiple mergers (higher moments), not from plugging in the "wrong" single Ne. This supports Day's description and qualifies the critic-side "mis-specified Ne" reading.
- At fixed f, Ne saturates at 1/(2pj f²) (19.98 at f = 0.5, 2N = 3,200; census 1,600). t̄ grows by a nearly constant increment per doubling of 2N over 200–3,200:

| f | per-doubling increment | heuristic f²ln2/(2(−ln(1−f))) |
|---|---|---|
| 0.05 | 0.0172–0.0195 | 0.0169 |
| 0.10 | 0.0331–0.0347 | 0.0329 |
| 0.20 | 0.0622–0.0630 | 0.0621 |
| 0.50 | 0.1244–0.1248 | 0.1250 |

- Day's large-N numbers reproduce: 1.363 and 1.737 at f = 0.5 (2N = 100, 800); 1.179 at f = 0.1, 2N = 800.
- The growth is about logarithmic through 2N = 3,200. "Without bound" would be an extrapolation (heuristic mine; Λ-coalescent literature not retrieved).

**Growth needs family size ∝ N.** At f = 0.5 and 2N = 3,200, a single copy's family is 1,600 copies (sweepstakes, Nₑ/N ≈ 1%). For a **fixed family** (m = 6) the excess shrinks: 1.0445 (2N = 60), 1.0130 (480), 1.0045 (1,920). Kingman is recovered, as Day's body says.

**Thresholds.**
- Exact f* (post hoc bisection) for +5% over the WF chain: 15% (2N = 20), 13% (30), 8% (50), 6% (100), 4.5% (200), 3.75% (400), 3.0% (800), **2.5% (1,600)**. The main run's 2.69% at 1,600 was a coarse-grid upper bound.
- The +5% cut is the audit's reading of "few-percent".
- The claim file's Day-side clause 2 ("f = 5% stays within the WF baseline offset") holds only to 2N ≲ 100. The excess at f = 5% is +4.3% at 2N = 100, +5.7% at 200 and +12% at 3,200.

**Eigenvalues (2N = 30, f = 0.5).** The leading rate is c, and the ratios are 1 : 2.00 : 2.72 : 3.17 : 3.41 (Day: 1 : 2 : 2.7 : 3.2 : 3.4).

**Spread (post hoc).** The SD of the conditional fixation time is 0.50–0.56 of its mean in WF and in the jackpot chain alike (2N = 20–50). A 7–25% shift in the mean is therefore systematic, but it is well inside lineage-to-lineage variation.

**Diploid family mapping (my construction; tests the mapping to diploid families, not Day's mathematics).** Day's example is "a family of 6 offspring in a population of 20", 30% of individuals. His text leaves open whether this means 2N = 20 or 40.

| Case | excess over WF |
|---|---|
| Day's literal case, 20 individuals (2N = 40), K = 6 | +2.9% (parents survive), +2.8% (parents die) |
| Haploid chain at f = 0.30, same 2N | +17.4% |
| Diploid peak, 2N ≤ 50, either variant | ≤ 3.7% |

- With parents surviving, the diploid excess turns negative at F ≥ 0.6–0.8. With parents dying, it stays about +2% to F = 0.6 and near 0 at 0.8.
- "Matches the haploid chain at about F/6" is an observation, not a derivation. At 2N = 20 it is only an upper bound set by integer resolution.
- Bias: random re-pairing every generation removes sibling genotype correlation and sib-mating (haplotype identity), so it biases toward a *smaller* effect. One construction only.

## Pre-registered predictions: held / failed
"Opposing" below means the claim file's prediction, written by the auditor, not by any critic.

**E (e_founder_hazard.py):**
- P1 held.
- **P2 FAILED:** the literal model gives 2.75%, outside the predicted 2.1–2.6%.
- P3 held: the row equality is exact. The numeric "~3.9%" was 4.08%.
- P4 held: the one-copy route is 68%, and P(hom | 2, drift) = 22.8% < 39%. The *reason* I gave (drift) was wrong; it is HW sampling with replacement.
- **P5 partly FAILED:** the tables match only `hwe`, and "drift rises with G" is wrong.
- **P6 split:** the incidence arithmetic held; the hazard reduction from the split FAILED (0.92–0.98×, against a predicted 50–85%).
- P7 held as pre-registered (0.95 and 0.5 thresholds). Its framing is now conditional; see the threshold sweep.
- P8 held.

**The claim file's own E3 falsifier fired.** "An independent run outside 2.33 ± 0.15%" is met by the literal reading (2.75%, +18%; also 2.736 ± 0.030% in the reviewer's MC). Day's 2.33% reproduces only under the inferred `hwe` formulation.

**E4 (e4_relictation_chain.py):**
- P1–P7 held. P6 used a coarse grid above 2N = 200 and is now exact.
- The claim file's auditor-written "opposing" guess (converges to 1.2–1.3) FAILED.
- Day-side clause 1 (≥ 1.3 at 2N = 100–200) held. Clause 2 holds only to 2N ≲ 100.
- **P8 partly FAILED:** the direction and the < 8% bound held, but the predicted F/4–F/2 equivalence is wrong (≤ about F/6).

## Adjudication
**E (paper Z23020792).**
- The quantity Day states, a per-event risk of ≥1 repair-deficient homozygote, is reproduced: 2.0% (exact arithmetic), 2.3% (Day), 2.38% (`hwe`), 2.75% (literal). That is within about 20%.
- It survives the gene-pooling slip, rises with N and with isolate growth, and is front-loaded.
- 6/12 is accurate to both LTEE papers.
- The route to it is wrong in its premise (≥2 carriers) and its conditional (39%). The two errors partly offset.
- The paper explicitly defers consequences, so the bridge to "hazard to the peripatric mechanism" is **untested** in E, not a non-sequitur in E.
- Mayr symmetry: whether one exposure changes population fitness is symmetric. A single beneficial recessive exposure is equally small, so Day's central symmetry point (§5.1, §6.4) is untouched by the consequence analysis.

**E3 (paper Z23034852).**
- The numbers reproduce under `hwe`. The literal reading gives a *higher* hazard, which helps Day numerically. It also makes s_hom inert for this metric and the selection reduction 33%, not 41%. This is a model-choice difference, not a defect.
- E3 also says the hazard is "independently sufficient" and that founder events are "minefields". On the endpoints tested, that is overreach:
  - At N = 100, a ≥2% cohort-fitness dip is 6× rarer than one affected birth, and a ≥5% dip 620× rarer.
  - At N = 20–30 the gap is 1–5×, because one CMMRD birth is itself a 3–5% dip.
  - So the reversal is in size and is N- and threshold-dependent, not in sign. It is not "every parameter".
  - E3 §4's own pathways (heterozygote mutation load, lethal equilibrium, meltdown shift) and the fertility of homozygotes were not modelled. The overreach finding applies to the direct-viability endpoint only.
- Credit to Day: E3 withdrew the sexual-vertebrate hitchhiking pathway itself (§5.4, §6.4).

**Critic engagement.** No critic engaged E or E3 directly. The nearest is the KITTENS/arctic review (Sparky_6_4, AI-assisted, r/DebateEvolution 1wxgsjm), which addresses the same LTEE mutator data (E7):
- "Its mutator result (8.5-fold instead of 100-fold) is an artifact of averaging in a negative count and two lines that are not 100-fold mutators" (about 17-fold otherwise).
- "in a recombining genome hitchhiking is confined to the neighborhood of a sweep".

The transfer of the asexual, large-N 6/12 outcome to a recombining vertebrate germline is the unargued step. Day's E3 concedes it for hitchhiking.

**E4 (paper Z23188201).**
- Day's mathematics is fully reproduced: table, large-N numbers, fixed-family numbers, eigenvalues and P_fix. "Keeps growing" holds about logarithmically through 2N = 3,200, at fixed f.
- **Prior art on the critic side.** Keruru, "The Epicycle Was Elsewhere" (2026-08-26; sources/raw/critics/ck-the-epicycle-was-elsewhere.json), built the same exact sweepstakes chain six weeks earlier: "half the time, half the population is replaced wholesale by clones of a single randomly chosen parent". Keruru reported Ne "5.6 times smaller" and P_fix "exactly 1/(2N_census), to fifteen decimal places", concluding that it "leaves k = μ exactly where it was". The 5.6× cannot be checked, since Keruru's N is not stated. Day's new content is the t̄-based extension.
- **What E4 does not change.** E4 changes the time per fixation, never P_fix or the neutral substitution rate k. It cannot support the rate arguments in A, B or F. It is the known multiple-merger result.
- **Day's stated scope.** Growth requires family size scaling with N. For bounded (vertebrate) family sizes, the excess shrinks with N, which matches Day's own "noise" statement and fixed-family numbers.
- The abstract's unqualified "Below 10%" is N-dependent, which the body discloses.
- The mapping from diploid families to the chain's f is untested by Day. One alternative construction, biased low, gives about +3%.

## Caveats and follow-ups
- **Founder model:** single locus, random mating, no sexes or inbreeding avoidance, no new mutation input. Growth was tested only as a deterministic N_t.
- **Untested endpoints:** isolate extinction or demography; the fertility of CMMRD-equivalent homozygotes (whether the allele or a mutator lineage is transmitted); heterozygote mutation-rate load, lethal equilibrium and meltdown (E3 §4); a benchmark against the standing recessive load at all other loci (a magnitude is not in the corpus; recalled values were not used).
- **`hwe` inference:** made from matching numbers, not from seeing the code; Tables 6 and 8 are unexplained.
- **Win frequencies** are from memory.
- **E4:** the diploid model is one construction with re-pairing bias. The Λ-coalescent literature (Möhle & Sagitov, Eldon & Wakeley, Schweinsberg) was not retrieved. §5 (Θ equation), Viluma 2022 and the mesa/spike predictions were not checked.
- **Not checked here:** E7, plus E1/E2/E5/E6/E9. The E1 "Taylor" attribution remains unsourced (Barrick 2009 carries the point; Day already reports all-cause and beneficial-only figures).

## Suggested verdict edits
- **E.**
  - internal: `holds approximately`. The per-event figure is within about 20% of the exact models (2.0–2.75%). The analytic route is wrong in premise ("≥2 carriers") and conditional (39% from HW-with-replacement), with partly offsetting errors.
  - fidelity: `accurate` for 6/12 (Tenaillon, Good) and the two pathways (Tenaillon ED legend). The 4+2 per-population split is sourced by Day to Couce 2017 and Maddamsetti & Grant 2020, not retrieved.
  - external: `untested bridge`. The model result holds. The consequence is unestablished and Day concedes it in E ("warrant formal demographic modeling"). The ancestral-mammal q is unknown, which E3 §3.6 concedes. The relevance of asexual LTEE mutators to sexual vertebrates is unargued.
- **E3.**
  - internal: `reproduces only under an inferred mean-field (HW-expected) selection formulation`. The literal §3.1 reading gives 2.75% (+18%), outside the claim file's pre-registered 2.33 ± 0.15% band. Under it, s_hom is inert for this metric and the selection reduction is 33%. Table 8 is not reproduced by either formulation. Cumulative and G-insensitivity hold.
  - external: `overreach` for "independently sufficient" and "minefields" on the direct-viability endpoint. Population-level dips are 1–5× rarer at N = 20–30 and 6–620× rarer at N = 100 (2–5% thresholds). The §4 pathways were untested. Credit the withdrawal of the hitchhiking pathway.
- **E4.**
  - internal: `holds` (everything reproduces).
  - fidelity: `accurate`. Λ-coalescent framing is Day's own; the body discloses the N-dependent thresholds. Flag the abstract's unqualified "Below 10%".
  - external: `contested`. Growth with N needs family size ∝ N (sweepstakes); for fixed family size the excess shrinks. The diploid mapping is untested (one construction gives about +3%). The wolf case is untested.
  - Responses: replace "none located" with Keruru 2026-08-26 (same chain, P_fix 1/(2N), Ne reduced, k unchanged).
  - B7 ledger: Day states P_fix = 1/(2N) "regardless of offspring distribution" (confirmed exactly). E4 alters t̄, not P_fix or k.

## Review resolution (REVIEW-R4-E-correctness, -steelman-day, -steelman-critic)
| MAJOR | Change |
|---|---|
| Correctness 1 / Day 2: the 600× rests on one threshold | Post-hoc threshold sweep (0.99–0.5) at N = 20–200. Conclusion reworded as conditional, in size, and N-dependent. About 2.5 births per hit added. Endpoints labelled as the audit's; §4 pathways and demography listed as untested. |
| Correctness 2 / Day 3: E3 falsifier; "artefact" | States that the pre-registered falsifier fired under the literal reading. `hwe` is called a textbook mean-field formulation, the better fit and not proven unique. "Artefact" removed. "Within 2 SE" corrected (−3.1 and −4.2 SE exceptions). Table 8 not reproduced by either formulation. |
| Day 1 / critic 1 / correctness 18: the E non-sequitur | Split: E is `untested bridge` (Day defers consequences); E3's "independently sufficient" and "minefields" are `overreach`. |
| Day 5 / correctness 9: "fails as stated" | Now `holds approximately`. Day used the top of his 5–6% range. The 39% gap is attributed to HW sampling with replacement (verified: 22.66% vs exact 22.76%). Day's "conservative" holds for expected births (6.1 vs 0.5, drift). |
| Day 4 / critic 12: diploid model | Labelled one construction testing the mapping, with re-pairing bias noted. Day's literal 2N = 40, K = 6 case and a parents-die variant added (+2.8–2.9%). F/6 marked an observation and an upper bound. N vs 2N ambiguity in Day's text noted. |
| Critic 3 / 4 / 5: E4 scaling, known result, k | Growth stated to need family size ∝ N, with the fixed-family decay shown. "Known multiple-merger result" stated. P_fix and k are unchanged. Added that variance, coalescent and eigen Ne coincide, so the deviation is multiple-merger, not a mis-specified Ne (partial rebuttal). SD of t̄ added. |
| Critic 6: "none located" | Keruru 2026-08-26 credited (verified in the local copy). |
| Critic 7: growth, constant N | Exact growth variant run. The hazard *rises* (2.75 → 9.0%), so the critic's dilution expectation fails for this metric. Sexes and inbreeding avoidance listed as untested. |
| Critic 8: 6/12 transfer, arctic review | Arctic/KITTENS mutator-averaging and recombination points credited (verified). Transfer to sexual vertebrates marked unargued, with Day's §5.4 concession. |

MINORs applied:
- Quotes restored with dashes.
- P3 numeric miss stated.
- `p_event` rename.
- Numerical floor wording.
- Tenaillon legend locator.
- The 1e-12 statement.
- Exact f* (2.5% at 1,600).
- Day-side clause 2.
- "About logarithmic through 3,200".
- Integer-resolution floor on F/6.
- Auditor-written "opposing" guess.
- Antimutator rate vs load.
- 4+2 sourcing.
- Day's body disclosures.
- Mayr symmetry.
- "Common ground" recast.
- "Taylor" listed.

Not done:
- The lethal-equivalents benchmark: no source in the corpus.
- Retrieving the Λ-coalescent literature.
- An extinction or demographic endpoint.
