# R4 B2f: the "closed-form" F(T) = exp(−π²Nₑ/T) in the revised Zenodo 22903977 ("k ≠ μ")

**Status: run and written up; awaiting one combined review (low-stakes tier, see "Tier"). All verdicts below are proposals.** Quoted statements scored here (Q286, N1, N2) are tagged dialectic (an equation, a definition, a stated consequence). The new title's "Collapse" is not scored (no statement attaches a number to it).

## Files
- Script `research/checks/b2f_finite_time_formula.py`, registered at **4213c5e** and pushed to both remotes before the run; not edited after. Local run 2026-10-13 (na-garage, one process, 1.4 s, 104 MB). Output `results/raw/b2f.out`, `b2f.json`, `b2f.host` (md5s).
- **Pre-registration label: criterion-only.** The source texts and B2's reviewed numbers were read before registration (disclosed in the docstring). Bands came from hand arithmetic. T1-T6 are textual verifications, P7 and P6a are identities, two P2 values and the x = 4 row reproduce B2. Every prediction hit; with bands set this way that is weak evidence of anything beyond correct arithmetic, and it is reported as such.
- Sources (gitignored): NEW `sources/raw/refresh-2026-10-13/zenodo-22903977-new/new.txt` (from `k_neq_mu.pdf`, md5 739634e9..., record modified 2026-10-13T15:07:16Z); OLD `old.txt` in the same folder (from `Kimura.pdf`, md5 e325def9..., 2026-09-22); HL `sources/raw/day/zenodo-22129121.txt` (Hard Limits, 2026-08-27).
- B2 is not redone. Reused: `cond_fix_cdf` from `b2_hard_limits_internal.py`; the Kimura (1955) series from `b2_posthoc.py`.

## What is new versus Hard Limits
1. **Same object, same symbols.** NEW: "the proportion of theoretically destined fixations that actually complete within T generations" and "k(T) = μ·F(T)". HL l.287: "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)". T is in generations in both. Nₑ is the diploid effective size in both (HL's distance π√(2Nₑ) counts 2Nₑ gene copies; the exact chain at 2N = 200 confirms the exponent with Nₑ = 100). NEW cites "Day and Athos (2026b)", which its reference list gives as Hard Limits (N3).
2. **What changed in the statement.** HL (Q31): "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ", called "the short-time first-passage law" (N6). NEW (Q286): "the closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T)". The "∼" became "=", "closed-form" was added, and the domain T ≪ 4Nₑ is gone (NEW contains no "≪" and no "∼").
3. **What changed in the stated derivation.** NEW says Day and Athos (2026b) "extract the dominant eigenvalue of that expansion [Chalub's Gegenbauer series] via diffusion asymptotics in the arcsine-transformed coordinate system". HL contains none of "Chalub", "eigenvalue", "arcsine", "Gegenbauer"; it gives the transform-to-random-walk distance argument (N6).
4. **What NEW derives from it.** No number. "F(T)" occurs twice outside "E[F(T)]" (a different F, the expected count) and "exp(" once. The consequences drawn are verbal: N1 ("a function that drops exponentially with effective population size") and N2 ("every application of k = μ to a finite-time calculation is guaranteed to be incorrect").
5. **Diff of the held texts, complete.** Three changes: the title; the §1 Chalub paragraph (one sentence reworded, Q286 and N1 added, N5 replaced by N2); one reference added (N3). §2-§6 and the PDF abstract are word-identical, so Q34 and Q36 and every number in B1a stand as quoted.
6. **Effect on existing claim files.** Ten claim files cite the record under its old title (B1, B1a, B1e, B3b, B4a, B4d, B6a, F, F5, and A3c / B3g by id). Only **B1e's first Statement quote** ("Chalub (2022), solving the neutral Kimura equation explicitly in terms of Gegenbauer polynomials, derives the time-dependent fixation probability as a series of exponential decay terms...") is text that no longer exists in the current file; it must be pinned to md5 e325def9 with a versions-ledger row. B1's two Statement quotes are unchanged in NEW.
7. **Citation slip (ledger).** N3 gives Hard Limits the URL `https://zenodo.org/records/22903977`, this record's own id; Hard Limits is Zenodo 22129121.

## The exact law (derived before the run, confirmed by it)
x = T/Nₑ. Exact: F(x) = 1 + Σᵢ (−1)ⁱ(2i+1) exp(−i(i+1)x/4) (Kimura 1955, conditional on fixation, p → 0). By the Jacobi θ₁′ modular identity the same function is

F(x) = (4π/x)^{3/2} e^{x/16} Σₙ (−1)ⁿ(2n+1) exp(−π²(2n+1)²/x).

The two series agree to 3e-14 relative at 13 values of x from 0.05 to 60. So the exact short-time law is **F ≈ (4πNₑ/T)^{3/2} exp(−π²Nₑ/T)**: Day's exponent with a prefactor of (4πNₑ/T)^{3/2}, which closes B2's "roughly (Nₑ/T)^1.5". The long-time law, from the dominant eigenvalue, is F ≈ 1 − 3 exp(−T/2Nₑ). C(x) = exp(−π²/x) denotes NEW's formula.

## Results against predictions
| Pred. | Prediction | Result | Score |
|---|---|---|---|
| T1-T6 | Quotes present / absent as listed; HL lacks the eigenvalue vocabulary; NEW lacks the domain; nothing numeric derived from C | All 27 string checks true | verified (not predictions) |
| P1 | Local exponent −d ln F/d(Nₑ/T) below π² and within 1% / 5% / 16% at x = 0.05 / 0.25 / 1 | 9.795 (−0.76%), 9.499 (−3.76%), 8.432 (−14.56%); equals π² − 1.5x + x²/16 | **holds**. Day side: the exponent is exact in the limit T/Nₑ → 0 |
| P2 | F/C > 1 on the whole grid, decreasing; equals (4π/x)^{3/2}e^{x/16} within 1% for x ≤ 2; B2's 47.4 and 17.8 reproduced | 3,997 (x = 0.05), 362 (0.25), 47.42 (1), 17.85 (2), 7.15 (4), 3.25 (8), 1.48 (25.2), 1.18 (60); all four sub-parts true | **holds**. Critic side: C understates the exact F at every T; there is no T at which it is exact |
| P3 | At the paper's T = 252,000: exact F in [0.9999, 1], [0.70, 0.82], [0.59, 0.62]; C = 0.676, 0.141, 0.085; C more than 25% below exact at all three | Nₑ = 1e4 (x = 25.2): exact 0.99999, C 0.676 (32% below). 5e4 (5.04): 0.761 vs 0.141 (81% below). 6.3e4 (4.0): 0.606 vs 0.085 (86% below) | **holds**. Critic side. The Day-side alternative (within 25% at one input or more) did not occur |
| P4 | C within 25% of exact only for x ≥ x*, x* in [40, 48]; deficit ratio there > 1e6 | x* = 44.2 (T/4Nₑ = 11.1); (1 − C)/(1 − F) = 2.7e8 there. Within a factor 3 for x ≥ 8.7 (reported, no band) | **holds** |
| P5 | The eigenvalue term 1 − 3e^{−x/2} is within 1% of exact for x ≥ 8 and negative below x = 2.197; at x = 25.2, (1 − C)/(1 − F) > 1e4; C never tracks the deficit within 25% on x ≥ 8 | All true; ratio 3.2e4 at x = 25.2 (1 − F = 1.01e-5, 1 − C = 0.324) | **holds**. C is not the dominant-eigenvalue term; that term gives the long-time law, and C is the short-time one, as HL itself says |
| P6a | Exact mean 4.000Nₑ; C as a CDF has no finite mean (partial integral grows π² ln 10 = 22.73 per decade) | 4.000000; 49.8, 72.5, 95.2 Nₑ at X = 1e3, 1e4, 1e5 (22.68, 22.72 per decade) | **holds** (first half an identity) |
| P6b | Loss at Nₑ = 1e4: exact in [15.5, 16.5]%; C in [55, 67]% | exact 15.87% (paper: 15.9%); C 60.5% | **holds**. Day side for the unchanged §4 number; critic side for C |
| P6c | Nₑ = 5e4: exact [65, 75]%, C [93, 98]%. Nₑ = 6.3e4: exact [79, 81]%, C [96, 99]% | 69.8% and 96.0% (paper 79.4%); 79.9% and 97.9% (paper 100%) | **holds**. The paper-vs-exact gap is B1a's (already recorded there; no new verdict) |
| P7 | Chain 2N = 200: stationary-start flux/μ = 1 at every T; empty-start flux/μ = chain F(T), within 5% of diffusion at x ≥ 4 | Stationary 1.000000000000 at T = 1, 100, 400, 504, 2520; empty 0, 0.0031, 0.614, 0.766, 0.99999; chain vs diffusion within 1.2% at x ≥ 4. Counts over T = 2520: stationary 1.000 μT, empty 0.843 μT | **holds** (an identity; non-severe) |

No prediction missed. That would normally be reported with the same weight as a miss; here the weight is small for the reason given under "Files". The last line of `b2f.out` ("segregating copies-classes ...") is an unused, loosely labelled diagnostic.

**Audit-derived, not stated by Day:** taken as an equality at the paper's own inputs, k(T) = μ·C gives 0.68μ, 0.14μ and 0.085μ at Nₑ = 1e4, 5e4, 6.3e4 for an allele cohort at the end of the window; the exact values are 0.99999μ, 0.76μ, 0.61μ.

## Readings (rule RD)
**Q286 + N1 (the formula and what it "replaces")**

| Reading | Internal | Fidelity (to HL, self-citation) | Basis |
|---|---|---|---|
| **A (rule C).** "closed-form ... F(T) = exp" relays HL's F(T) ∼ exp, T ≪ 4Nₑ, which is what the cited source says | `holds`, with a ledger slip: "=" and "closed-form" for an asymptote, domain dropped, derivation re-described (not the dominant eigenvalue: P5). R1: no number in NEW is derived from C (T6) and N2 needs only F < 1, so the correction moves no stated number or conclusion | `partial` (cited, read with a flagged omission) | P1; T2, T3, T6 |
| **B (literal).** An equality for any T, replacing k = μ wherever k = μ is used, including this paper's T/4Nₑ ≈ 6.3 (N4) | `non-sequitur`: N2a (the paper's own T and Nₑ in its own formula give a 60.5% loss where its §4 prints 15.9%, and 0.68μ where the exact rate is 0.99999μ); N2b (a fixation-time law with no finite mean, against its own "t̄ = 4Nₑ", N7) | `misread` (HL's text in hand restricts the law to T ≪ 4Nₑ) | P3, P4, P6 |

Most defensible reading of the quoted statement: A (the statement is then true of the limit it cites). Against A as the natural reading: "closed-form", "finite-time", and N1's "replaces the steady-state identity", since a replacement has to work where the identity is used. Proposed field value: internal `holds`, `reading-dependent:` A → holds, B → non-sequitur; counted with the reading-dependent verdicts.

**N2 ("guaranteed to be incorrect")**

| Reading | Internal | Basis |
|---|---|---|
| (i) Counts started from an empty pipe | `holds`: exact F < 1 at every finite T. Size at the paper's inputs: end-of-window rate short by 1.0e-5 at Nₑ = 1e4 (24% at 5e4, 39% at 6.3e4); count short by 15.9% (69.8%, 79.9%) | P3, P6b-c, P7 empty row |
| (ii) Every application, whatever the start state | Stronger than the premises (N2d): from mutation-drift equilibrium the flux is exactly μ at every T. No new verdict proposed: the start state is a premise dispute (rule N1) scored at B1, B1c and B6a, and NEW keeps §3's reply to that objection | P7 stationary row |

Ledger (S2), no verdict: N2's "cannot be utilized in any finite-time equation" sits beside N4, where the same paper applies a T → large approximation at finite T and calls it "comfortably in the regime".

## Proposed verdicts (proposals only)
- **New node B2f** (Day side, child of B2, supports B1; not load-bearing: no number is derived from it). Internal `holds` (reading-dependent; B → `non-sequitur`). Fidelity `partial` (B → `misread`); the Chalub link is not checked here and stays with B1e. External `contested`: the exponent is `supported` (P1); the equality is `contradicted` by the exact diffusion for T ≳ Nₑ and is within 25% only for T ≥ 44Nₑ, where F is 1 to eight decimal places (P3, P4; mathematics, not data); N2 as a statement about real lineages turns on the start state (B1, B1c, B6a).
- **B2** (Hard Limits): no change. HL's own text keeps "∼" and "T ≪ 4Nₑ". HL's "order-one" prefactor slip (already ledgered) gets its exact size: (4πNₑ/T)^{3/2}.
- **B1, B1a:** no change (their quoted text is identical in NEW). **B1e:** pin the old Statement sentence to md5 e325def9; consider adding Q286's first clause as the current wording.
- **Ledger entries for integration:** "=" / "closed-form" / dropped domain (slips, Day); "dominant eigenvalue" description (slips, Day); N3's URL (slips, Day); N2 beside N4 (slips, Day); silent revision with N5 replaced by N2 (versions).

## Tier
**Low-stakes; one combined review.** No ROOT-path node moves under either reading: B2's verdict rests on HL's text, and B1's on quotes that did not change. If integration adopted Reading B, the `non-sequitur` would sit on the new node B2f inside B1's source paper, not on B1's Statement (S2). The reviewer should say if they think N1 ("replaces the steady-state identity") makes B2f a step in B1's argument; that would make it load-bearing.

## Who this helps
- **Day side:** the exponent π²Nₑ/T is exactly right in the short-time limit, confirmed by a second, analytic route (P1). "Drops exponentially with effective population size" is true of the exact short-time law as well as of his formula. The cited source (Hard Limits) states the law with its domain, so the charitable reading is his own earlier text, not audit generosity. From an empty pipe no finite window reaches k = μ exactly, and his unchanged §4 figure of 15.9% at Nₑ = 10,000 is the exact value (15.87%). The empty-start count on the exact chain is 0.843 μT at his T/Nₑ.
- **Critic side:** the formula is an asymptote for T ≪ 4Nₑ presented as a closed form with the domain removed. It is below the exact F at every T (by 4,000x at T = Nₑ/20, 47x at T = Nₑ, 7x at T = 4Nₑ) and is more than 25% off at each of the three Nₑ the paper itself uses; at Nₑ = 10,000 it gives 0.68μ where the exact rate is 0.99999μ. It is not the dominant-eigenvalue term, which gives the opposite regime and shows k → μ exponentially fast (1 − F = 3e^{−T/2Nₑ}). Read literally it contradicts the paper's own mean fixation time and its own 15.9%. From standing variation at equilibrium the flux is μ at every finite T, so N2 holds only for an empty start.
- **Both:** nothing numeric in the paper depends on the new formula, so neither side's count changes. What separates readings (i) and (ii) of N2 is the start state, which this check does not decide (B1c, B6a).

## Quotes for integration to file (verbatim; no Q id yet; quotes files not edited here)
- N1, NEW §1 Chalub paragraph, sentence 4, record modified 2026-10-13: "Multiplied through the mutation supply, this yields the time-dependent substitution rate k(T) = μ·F(T), which replaces the steady-state identity with a function that drops exponentially with effective population size (Day and Athos 2026b)."
- N2, NEW §1, sentences 5-6 (already under Q286 as "following sentence"; the first of the two sentences is also new): "The steady state requires infinite time. It therefore cannot be utilized in any finite-time equation, and every application of k = μ to a finite-time calculation is guaranteed to be incorrect."
- N3, NEW References: "Day, V. and Athos, C. (2026b). The Hard Limits of Fixation Through Genetic Drift. Zenodo. https://zenodo.org/records/22903977."
- N4, NEW §3 ¶5 (unchanged from 2026-09-22): "For the human-chimpanzee application, T = 252,000 generations and 4Nₑ = 40,000, giving T/4Nₑ ≈ 6.3 — comfortably in the regime where the approximation holds."
- N5, OLD §1 last two sentences (2026-09-22, removed 2026-10-13): "The steady state is the destination; it is not the journey, and it is not the starting point. Every finite-time application of k = μ treats the destination as though it were the departure."
- N6, HL l.296-299 (2026-08-27): "under the transform that turns neutral drift into a symmetric random walk, the distance from a single copy to fixation is a fixed length, π√(2Nₑ), and the chance of covering it in time T is the short-time first-passage law"
- N7, NEW §2 (unchanged): "t̄ = 4Nₑ generations This is the mean time to fixation for a neutral mutation, conditional on fixation."

## Limits
- Constant-size neutral Wright-Fisher diffusion, one new copy, p → 0; the chain is 2N = 200. No demography, no selection, no overlap (those belong to B1c, B3).
- "Day and Athos (2026b)" is identified from NEW's reference list by title only. The refresh of 2026-10-13 found Hard Limits' record unchanged, so the held HL text is taken as the cited one; a later HL revision containing an eigenvalue derivation would change the fidelity reading, not the numbers.
- Whether Chalub's series yields this exponent by any route was not examined (B1e).
- The stationary-start flux in P7 is a martingale identity, not an independent test; it shows what the two readings of N2 rest on, nothing more.

## Open
1. Combined review (correctness, steelman-day, steelman-critic).
2. Integration: Q ids for N1-N7; node B2f or a paragraph in B2 / B1e; RD comment and Readings table; versions-ledger row for the silent revision; B1e old quote pinned to md5 e325def9; slips rows; QUEUE.md item closed.
3. Next refresh: check whether Hard Limits (Z22129121) is revised to match the new wording.
