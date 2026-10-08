# Review Log

## 2026-10-07 — Steelman review #1 (Sonnet; both sides) of B0.4, B1, B3
Quotes came through a summarizing fetcher and must be re-verified against PDFs in R1 pass 2.

### Day's side: tests and claims the checks do not yet address
| # | Claim | Critique | Action |
|---|---|---|---|
| D1 | B1 | His real claim, quoted from 22129121: "k=μ holds only after a population has held one size for the roughly 4Nₑ generations". That claim is about size changes, which the empty/equilibrium extremes don't test. | **B1b**: equilibrium start, then bottleneck, expansion, founder event. Report per-window k/U. |
| D2 | B2 | No check exists for exp(−π²Nₑ/G) or the ceiling X. | **B2a**: exact WF Markov chain, fit the exponent. **B2b**: expected fixation count across all mutations. |
| D3 | B3 | The exchangeable Cannings model is not his target. The real argument concerns structured or non-exchangeable populations (census/Nₑ 19–46×, sexual species, Nₑ/N ~0.1). | **B3b-i…v**: overlapping generations + fluctuating N; reproductive value; source–sink; sweepstakes; linked selection. |
| D4 | F | He uses sweep time as latency and makes a separate throughput argument (LTEE 1,322 = throughput). His best version is interference or cost capping throughput. | **F2**: multi-locus sweeps with r=0 vs r>0, clonal interference. |
| D5 | A | Window arithmetic. | Full-scale lineage count (G≈252k, N=10⁴, μ=1.2e-8, L=3e9) vs ~35M SNVs; separate out the effect of counting basis in 32.3μ. |

### Critics' side: places the checks are too generous to Day, or miss cases
| # | Claim | Critique | Action |
|---|---|---|---|
| C1 | B1 | "Exact for an empty start" must be framed as a counterfactual boundary. An empty pipeline means zero heterozygosity, which contradicts observed human π. | Add a data-consistency panel (π=4Nμ vs observed; implied θ_anc). **RESULTS wording updated.** |
| C2 | B1/B4 | No two-lineage or ancestral-polymorphism accounting. | **B4a**: two-population split; d = 2μT + 2N_aμ; fixed vs polymorphic; ILS with outgroup. |
| C3 | F | The latency table distracts from throughput; F1 hasn't been run. | **F1**: Poisson arrivals × P_fix; Little's law. |
| C4 | B3 | Day himself states 1/(2N) (Hard Limits paper; blog 2026-10-01: "1/2N is the fixation probability"). | Record as an internal-contradiction ledger item (text check). Also vary N at fixed variance in the Cannings model. |
| C5 | C | No check yet on aDNA panel ascertainment. | **C1**: panel ascertained at MAF>5% today gives ~0 fixations by construction. |
| C6 | general | B1 used only 60 reps. The N=50 z=−2.75 needs an exact-chain check (E4). G has no check. | Exact chain added in B2a; G queued. |

## 2026-10-07 — Correctness review #2 (Sonnet), on B0–B3
No simulation-code bugs. Findings and their resolution:
1. **BLOCKER:** `-I` broke the `wf` import. → Each script now inserts its own directory into `sys.path`. FIXED.
2. **MAJOR:** B0.2 target was a flat 4N. → Now the diffusion value at p=1/(2N). N=50 z = −2.15 (≈ −0.8 against the exact chain). FIXED.
3. **MINOR:** the stochastic sweep-time formula should use ln(4Ns), not ln(2Ns). FIXED in all scripts and in RESULTS.
4. **MINOR:** "within 1%" was not supported. → SEs added; claim restated against the 5% tolerance. FIXED.
5. **MINOR:** B1 matches by construction, its T ≤ 100 grid points were vacuous, and the prediction's noise was ignored. → Grid points removed, caveat added, burn-in raised to 20N. Multiplicity correction: NOT DONE (noted).
6. **MINOR:** a 10N burn-in leaves about a 2% flux deficit. → Raised to 20N in B1. FIXED.
7. **MINOR:** B3 had no z-scores and was missing the α=4 row. → z and SE now printed; row added; "provisional" hedge added. FIXED.
8. **MINOR:** kimura_u is a diffusion approximation (about 0.4% gap from the exact chain). Noted; SEs cannot distinguish them at current replicate counts.

Reviewer's independent verification: an exact WF Markov chain (in session scratchpad, not committed). It confirmed `single_locus`, `diffusion_cond_fix_time` (within 0.2% for 4Ns ≥ 20), and the Cannings BetaBinomial marginal.

## Pending reviews
B1b, B2a and F1 need a correctness review and a two-sided steelman review.
