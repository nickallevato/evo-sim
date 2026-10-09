# Balance Ledger: Strongest and Weakest Points per Side, by Branch
Version: R1 pass 2 (2026-10-07); R4 additions 2026-10-08 (section below). Sources are in `sources/quotes-*.md` (exact-match verified) and `opponents/*.md`. Check results are in `research/checks/RESULTS.md`.

Rule: every row names the best argument on *each* side, and records weaknesses with the same scrutiny for both.

| Branch | Best for Day / allies | Best for critics | Check status |
|---|---|---|---|
| A / A5 LTEE→human scaling | Hössjer re-derives 127 → 15,800 → ~10M, leaving a ~2× gap. *Concedes most of A5.* | "KITTENS" (Reddit) decomposes the 1.075M shortfall using the paper's own numbers: 94,000 (mutation supply per genome) × 11.7 (counting bases instead of events) | A-sim + F2 done (R4): asexual a = 0.23–0.34; free recombination linear to 272 loci; LTEE-scale factor extrapolated |
| A3x bp vs events | none found | 205M counts each base of a structural variant as a fixation; Yoo 2025 has no 410 or 187 Mb (fidelity ledger) | fidelity: Day **not-found** |
| A2 LTEE rate G_f | Day/Duffy: G_f is a measured aggregate that already includes parallelism (Camestros concedes it is an average) | The paper's own estimator gives −906 fixations in Ara-2, and Ara+5 drops 38 → 0; Day's later 23105291 self-corrects | queued |
| B1 empty pipeline | Exact for an empty start (B1); the expansion deficit is real (B1b) | Equilibrium start gives k=μ; contraction gives an excess; the real ancestral Nₑ is 132k–198k (Yoo 2025) | B1, B1b, B1c, B4a done (R4) |
| B2 Hard Limits | Exponent −π² is the correct asymptotic (B2a) | It is a per-allele latency tail, not a throughput bound | B2a done |
| B3 N vs Nₑ | Nₑ sets the timescale (B3); Balloux & Lehmann: k≠μ with overlapping generations plus fluctuating N | Kimura 1962 / Kimura & Ohta 1969 say 1/2N (census); keruru retracted on exactly this point; B3 simulation | B3, B3b, B3c done (R4) |
| B4 clock recalibration | Hössjer/McCarthy agree that dating carries circularity | none engaged | queued |
| C aDNA | Day: keruru's Nₑ ≈ 10⁴ input is circular | keruru: zero fixations in 240 generations is the neutral prediction; 1240k panel ascertained on present-day array SNPs | C1, C1b done (R4); C6 21-count not reproducible |
| D Wistar / sequence space | Eden's 10^325 vs 10^52 is verified (p.7); Rosenhouse ch.4 lacks quantification | Ulam: random construction "is not the problem at all"; Wright's twenty-questions rebuttal; Rosenhouse ch.6 (not accessed) | catalogue only |
| F latency vs throughput | Day: G_f is throughput, and he does not divide time by latency (per fetcher, 2026-10-01) | Hancock/Mansfield: interval between fixations ≠ time to fixation; F1 confirms pipelining is possible | F1, F2 done (R4) |
| G Bernoulli Barrier / average | G1: an average rate is indifferent to parallel vs serial (partly valid against the "marathon" analogy) | Specific-vs-any outcome (McCarthy, Camestros) | F2 covers G/Gc capacity (R4); G1/G3 queued |
| H cost of selection | Hössjer asserts a cost step (not computed); Haldane 300 verified via Nunney | Nesslig20 separates cost from drift; Nunney 2003: cost "substantially less", soft selection "eliminates" it. **No critic engaged Nunney.** | H, H2-hard done (R4) |

## R4 additions (2026-10-08, after review #4)
Credit goes to whoever made the argument. Results that come from the audit's own checks or from the literature (Nunney, Euler–Lotka d, Yoo ancestral Nₑ) are not credited to "critics", because no critic in the corpus made them.

| Branch | New strong points for Day / allies | New strong points for critics (or the audit) | New weak points |
|---|---|---|---|
| B1/B4 pipeline | U(T−4Nₑ)/T is exact for post-split new mutations (B1c new-mutation column 0.84). At Day's Nₑ = 1e4, two-lineage d = 0.65%, about half the observed 1.23%. The fit has three parameters, and Yoo's μ is unrecorded. | The empty start is contradicted (Day withdrew it, B1d). d − 2μT = θ_anc holds in forward simulation. CSAC's 14–22% polymorphic share matches poly-but-diff (22–25%). Day's 2μ(T−4Nₑ) is below the simulated fixed differences. | **Day:** B6a "rounding error" holds only at Nₑ,anc = 1e4. **Audit:** at the correct HCB node, d overshoots 1.23% by ~25%. **Critics:** Hancock 38M and Nesslig20 37.8M double-count on an SNV basis. 2μT already supplies ≈19M, and the remaining ≈15M is ancestral (B5c, B5e). |
| B3 k vs μ | The Balloux–Lehmann k≠μ effect is real (eq. 3 reproduced), so critics' blanket "k = μ" is only a discrete-generation result. | RRME 0.743 is a window artefact. The 1/(2N_t) fixation step is falsified by simulation. The realistic B&L sign is upward, opposite to RRME. | **Day:** "RRME confirms B&L" is opposite in sign, and 32.3 has no derivation. **Critics:** stationarity is assumed in all the stated totals. |
| C aDNA | C1a's sign is right for the 10–90% bands (1.2–3.4×). The tail is extremely Nₑ-sensitive, and Nₑ = 1e4 is unverified. v66 is 3.8× below the neutral model. | "0 from <50%" is the neutral expectation, so the test does not discriminate. The 630 denominator is wrong for an ascertained panel. Observed 1 and 3 completions are faster than neutral at Nₑ = 1e4. | **Day:** the 21-count could not be reproduced from the published procedure (C1b) and does not match even his own bin profile in the model. **Audit:** the earlier "does not rescue Day" and "deficit vs neutral" wording was withdrawn as unsupported. |
| C2 / A4 d | d·s is exact for hazard-scale s (V1). The derivation (d = mean cumulative hazard at the age of mothers) is correct. Critics have not explained the trajectory-vs-published-s anomaly at d = 1. | For per-generation s the factor is 1. "d = 1 for discrete generations" fails on Day's own formula. d is not identifiable from three trajectories. The C2c ratio is an identity. | **Day:** Table 1 is not reproduced (Coale-Demeny tables not retrieved). **Critics:** Camestros's time-variation point (CA-12) is untested. |
| F2 / G / A5 interference | Interference is real under linkage (clonal R_int 0.09–0.65; 0.2 at 0.1 M). The asexual response is sublinear (a = 0.23–0.34). KITTENS's 94,000× linearity is not established. | No collapse up to 272 active loci with free recombination (R_int 0.975; fwdpy11 agrees). Recombination raises the rate (A5f). | **Both:** human-scale active loci (~1e4–1e5) are untested. **Critics:** asexual saturation was the critics' own prediction, so it is no special credit to Day. The 1.5–172× LTEE factor is an extrapolation. |
| H cost of selection | Soft selection did not remove the cost in the reconstruction: soft T50 exceeded hard at equal supply. For new mutations D ≈ 20 gives ≈200 generations, the same order as 300. Hard selection at U = 2.2 needs ≈18 offspring per female (Keightley). Haldane's own regime (R≈1.1, D≈20–30) is untested. | 10% is not a general bound: the hard-selection cap is ln R / D, and at R ≥ 1.3 with D ≈ 7 the flip lies 9–100× above 1/300. Hössjer's 15,800 is a rate scaling, not a cost (10.5× Haldane's 1,500). Day's own H1 scope concession applies to the 20M comparison. | **Day:** Term 3 vs Haldane ratio corrected to 17.1. The corpus has two unreconciled cost figures. **Critics:** "soft selection eliminates the cost" is unproven. Nothing shows humans are in the M > ½ regime. **Audit:** the Nunney reconstruction misses absolute values by 2–12×. |

## Weaknesses recorded with equal scrutiny
**Day**
- Basis error in 205M: counts base pairs, not events.
- Zeng 2021 s misread: the coefficient is for negative selection, not beneficial.
- Nₑ misused in place of N for fixation probability: Kimura 1962 and Kimura & Ohta 1969 both give 1/2N.
- Misattributes recombination claims to Kimura & Ohta 1969.
- Misreads Langergraber 2012.
- "Chalub 2012" not found.
- Parameter drift across versions.
- The Hard Limits and aDNA papers have no references.
- R4: RRME 0.743 rests on a falsified 1/(2N_t) step (B3c). The empty-start premise is contradicted for sourced histories (B1c). "d = 1 for discrete generations" fails on his own formula (C2). The aDNA 21-count is not reproducible from the stated procedure (C1b). The Term 3 vs Haldane comparison mixed bases (17.1, not 7.7).

**Allies**
- Hössjer's gaps (corrected 2026-10-08; this line earlier said a single "2.2× gap" came entirely from d). His quoted "only by a factor of 2" is the rate scaling, eq. 2.4: 20M/10.30M = 1.94. His neutral count, eq. 3.1, is 7.59M: 20M/7.59M = 2.63. The 2.2 is d's own factor, 1/0.45 = 2.22, which is in both. Without d: eq. 3.1 gives 16.9M (1.19× short) and eq. 2.4 gives 22.9M (above 20M) (claims A5a, H5).
- Hössjer's cost step is asserted, not computed. R4: his 15,800 comes from rate scaling and is 10.5× Haldane's own 1,500 (H5).
- Keen gives no equations; Dembski gives no calculation.

**Critics**
- Hancock: his first pass used diploid 76.8 but he corrected it on screen. The retained 76 is an SV-inclusive haploid *event* count; SNV-only haploid gives 19.35M vs 35M (1.8× short). His 205M→407/gen halves an already per-lineage figure. His bacterial μ of 1e-11 is below the measured 8.9e-11. (Corrected in R2.)
- Nesslig20: basis of μ_G = 75 not stated; the factor-of-2 charge is unsettled (R2). R4: on a haploid SNV basis 18.9M ≈ 2μT, and the observed ~35M ≈ 19M + ~15M ancestral, so the 37.8M match would be a double count (B5e).
- Hancock (R4): the "38M matches 35–40M SNVs" agreement double-counts on an SNV basis. The correct split is ≈19M post-split (2μT) + ≈15M ancestral polymorphism (B4a, B5c). His retained 76 is an SV-inclusive event count, so the event-basis comparison is not contradicted.
- Critics generally (R4): the soft-selection rescue of the cost is not reproduced (H). Parallel-sweep feasibility has been shown only under soft selection or under hard selection with ample R (F2, H2). The stated neutral totals assume stationarity (B1c, B3b).
- McCarthy: assumes N = Nₑ and that all mutations are neutral; cites an uncited 3% figure.
- Mansfield: his 2% illustration comes out ~44× short.
- Myers: gives no numbers.
- Camestros: reviewed the first edition only, and has a typo.
- KITTENS: AI-assisted, cites from memory.
- Hancock's video answers the Duffy version (22 Sep), not MITTENS 3.0.

## Coverage gaps (both sides)
- **Day's side:** *Probability Zero* (paid; includes Tipler's foreword); the original Bowers review; the Gariépy debate.
- **Critics' side:** McCarthy's paid posts; the Rosenhouse book (ch.6); Reddit body-text search; Moran/Felsenstein (inconclusive search); Gutsick Gibbon's promised roundtable.
- **Neither side:** no peer-reviewed treatment exists.
