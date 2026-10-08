# Balance Ledger: Strongest and Weakest Points per Side, by Branch
Version: R1 pass 2 (2026-10-07). Sources are in `sources/quotes-*.md` (exact-match verified) and `opponents/*.md`. Check results are in `research/checks/RESULTS.md`.

Rule: every row names the best argument on *each* side, and records weaknesses with the same scrutiny for both.

| Branch | Best for Day / allies | Best for critics | Check status |
|---|---|---|---|
| A / A5 LTEE→human scaling | Hössjer re-derives 127 → 15,800 → ~10M, leaving a ~2× gap. *Concedes most of A5.* | "KITTENS" (Reddit) decomposes the 1.075M shortfall using the paper's own numbers: 94,000 (mutation supply per genome) × 11.7 (counting bases instead of events) | queued (A, F2) |
| A3x bp vs events | none found | 205M counts each base of a structural variant as a fixation; Yoo 2025 has no 410 or 187 Mb (fidelity ledger) | fidelity: Day **not-found** |
| A2 LTEE rate G_f | Day/Duffy: G_f is a measured aggregate that already includes parallelism (Camestros concedes it is an average) | The paper's own estimator gives −906 fixations in Ara-2, and Ara+5 drops 38 → 0; Day's later 23105291 self-corrects | queued |
| B1 empty pipeline | Exact for an empty start (B1); the expansion deficit is real (B1b) | Equilibrium start gives k=μ; contraction gives an excess; the real ancestral Nₑ is 132k–198k (Yoo 2025) | B1, B1b done; B1c queued |
| B2 Hard Limits | Exponent −π² is the correct asymptotic (B2a) | It is a per-allele latency tail, not a throughput bound | B2a done |
| B3 N vs Nₑ | Nₑ sets the timescale (B3); Balloux & Lehmann: k≠μ with overlapping generations plus fluctuating N | Kimura 1962 / Kimura & Ohta 1969 say 1/2N (census); keruru retracted on exactly this point; B3 simulation | B3 done; B3b queued |
| B4 clock recalibration | Hössjer/McCarthy agree that dating carries circularity | none engaged | queued |
| C aDNA | Day: keruru's Nₑ ≈ 10⁴ input is circular | keruru: zero fixations in 240 generations is the neutral prediction; 1240k panel ascertained on present-day array SNPs | C1 queued |
| D Wistar / sequence space | Eden's 10^325 vs 10^52 is verified (p.7); Rosenhouse ch.4 lacks quantification | Ulam: random construction "is not the problem at all"; Wright's twenty-questions rebuttal; Rosenhouse ch.6 (not accessed) | catalogue only |
| F latency vs throughput | Day: G_f is throughput, and he does not divide time by latency (per fetcher, 2026-10-01) | Hancock/Mansfield: interval between fixations ≠ time to fixation; F1 confirms pipelining is possible | F1 done; F2 queued |
| G Bernoulli Barrier / average | G1: an average rate is indifferent to parallel vs serial (partly valid against the "marathon" analogy) | Specific-vs-any outcome (McCarthy, Camestros) | G queued |
| H cost of selection | Hössjer asserts a cost step (not computed); Haldane 300 verified via Nunney | Nesslig20 separates cost from drift; Nunney 2003: cost "substantially less", soft selection "eliminates" it. **No critic engaged Nunney.** | H queued |

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

**Allies**
- Hössjer's 2.2× gap comes entirely from d = 0.45 inside the neutral rate; without d, 16.9M vs 20M.
- Hössjer's cost step is asserted, not computed.
- Keen gives no equations; Dembski gives no calculation.

**Critics**
- Hancock: his first pass used diploid 76.8 but he corrected it on screen. The retained 76 is an SV-inclusive haploid *event* count; SNV-only haploid gives 19.35M vs 35M (1.8× short). His 205M→407/gen halves an already per-lineage figure. His bacterial μ of 1e-11 is below the measured 8.9e-11. (Corrected in R2.)
- Nesslig20: basis of μ_G = 75 not stated; the factor-of-2 charge is unsettled (R2).
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
