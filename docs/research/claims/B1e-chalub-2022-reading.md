---
id: B1e
title: "Chalub 2022 shows k = mu is an asymptote / 1/(2N) is imported from Wright-Fisher"
side: day
branch: B
parent: B1
edges: [{type: supports, target: B1}, {type: supports, target: B7}]
load_bearing: false  # cited as support, not as a step in any calculation
sourcing: firsthand
status: extracted
verdicts:
  internal: holds   # reading-dependent: (A) the current Zenodo wording (Q286, Q289; record replaced 2026-10-13) relays Hard Limits' short-time asymptote F(T) ∼ exp(−π²Nₑ/T), T ≪ 4Nₑ: `holds`, with ledger slips S-B2f-1..4 (sets the field: the reading under which the quoted statement is most defensible, rule RD); (B) a literal equality with no domain: `non-sequitur` against the paper's own F_X integral, mean 4Nₑ and SD (Q293, Q294). Was `pending` until R4 B2f (review #82, integrated 2026-10-13). Scope: the value covers the Zenodo statement; the 2026-08-23 blog quote (1/(2N) "imported") was not examined by B2f
  fidelity: partial   # reading-dependent: value unchanged. (A) `partial`: Hard Limits is cited and relayed with its domain omitted; (B) `misread`. The Chalub link itself (is Chalub's Gegenbauer expansion the Kimura 1955 series?) is unchecked and stays `partial` on the ledger basis below
  external: contested   # reading-dependent: (A) the exponent is supported in logarithms (exact as T/Nₑ → 0) and "every application of k = μ ... is guaranteed to be incorrect" is `contested` on the start state only (true from an empty start, the paper's premise; from a stationary start the flux is exactly μ; scored at B1, B1c, B6a): sets the field; (B) `contradicted` by the exact diffusion at every T. Was `pending` until R4 B2f
verdict_scope:
  internal: "Scope: the value covers the Zenodo statement; the 2026-08-23 blog quote (1/(2N) \"imported\") was not examined by B2f"
---

## Statement (verbatim)
> Chalub (2022), solving the neutral Kimura equation explicitly in terms of Gegenbauer polynomials, derives the time-dependent fixation probability as a series of exponential decay terms that converge to the steady-state value only as t → ∞.

Source: [Z22903977, The Intrinsic Irrelevance of Kimura's Substitution Rate (Day & Athos)](https://zenodo.org/records/22903977), Zenodo 2026-09-22 (v1), §1 The Identity

Version note (2026-10-13): **this sentence is superseded in the source.** It is quoted from the file published 2026-09-22 (`Kimura.pdf`, md5 e325def9ecd74611e6e75f1befcc788f; held copy `sources/raw/day/zenodo-22903977.pdf`). On 2026-10-13 15:07:16 UTC the record was retitled "k ≠ μ: The Finite-Time Collapse of Neutral Substitution Theory" and its file replaced (`k_neq_mu.pdf`, md5 739634e97a80c8f9d0d31d125544b94c), with the same record id, DOI and version number; the sentence above is not in the new file (`ledgers/versions.md`). Current wording of the same passage, sentences 2 and 3 of the paragraph:

> Chalub (2022), solving the neutral Kimura diffusion equation with absorbing boundaries, derives the explicit transient solution as a Gegenbauer polynomial expansion whose terms converge to the steady-state fixation probability u(p) = p only as t → ∞.

Source: [Z22903977, k ≠ μ: The Finite-Time Collapse of Neutral Substitution Theory (Day & Athos)](https://zenodo.org/records/22903977), Zenodo, record modified 2026-10-13 (file md5 739634e9...), §1 The Identity, last paragraph, sentence 2 (Q288)

> Day and Athos (2026b) extract the dominant eigenvalue of that expansion via diffusion asymptotics in the arcsine-transformed coordinate system, converting Chalub's abstract series into the closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T) — the proportion of theoretically destined fixations that actually complete within T generations.

Source: [Z22903977, k ≠ μ: The Finite-Time Collapse of Neutral Substitution Theory (Day & Athos)](https://zenodo.org/records/22903977), Zenodo, record modified 2026-10-13 (file md5 739634e9...), §1 The Identity, last paragraph, sentence 3 (Q286)

> Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model. It is not a result produced by the mathematics.

Source: [Day, "Chalub and the Kimura Cancellation" (blog)](https://voxday.net/2026/08/23/chalub-and-the-kimura-cancellation/), 2026-08-23, ¶5 of extracted text


RH tag (2026-10-10 pass): dialectic (stated as a checkable claim or derivation; no rhetorical device scored).
## Formal statement
Chalub 2022: PDE for a two-allele neutral population "without mutation or selection", classical solution decays; two point masses at the boundaries plus integral constraints (probability conservation, conservation of mean frequency) fix the split between fixation and loss. Day's reading: the 1/(2N) is imported, not derived.

Note (derived reasoning, not a verdict): conservation of mean frequency is the definition of neutrality (equal expected offspring), so it is the neutral assumption itself rather than an extra premise. Day's point that the PDE alone does not fix the boundary split is consistent with the paper's abstract.

## Assumptions
- Stated: The diffusion machinery cannot independently confirm P_fix = p₀.
- Implicit: Chalub's model (no mutation, no selection) bears on k = μ only through P_fix and time-dependence; k also needs mutation input, which the paper does not model.

## Responses
- Against: Ledger: math correct but the paper does not address the substitution rate k. The Day post itself says Chalub "gives no sign that he is even aware that anyone is contesting neutral theory".
- In support: The literature quote below confirms the integral-constraint structure.
- Weaknesses in the responses: Day's own post also states the outcome: "Impose that assumption and the fixation probability comes out equal to the starting frequency", which agrees with the critics' P_fix = 1/(2N) at the census start (B7); the same author later conceded N/Nₑ (B3g).

## Primary literature
| Cited work | What it actually says (quote) | Fidelity |
|---|---|---|
| Chalub 2022 | "we consider a population of two types evolving without mutation or selection, the so-called neutral evolution" | verified-partial (ledger): relevant to finite-time P_fix, not to k vs μ |
| Chalub 2022 | "Its solution is required to satisfy not only the equation but a series of conservation laws formulated as integral constraints." | accurate |
| Chalub 2022 | "Finally, the time-dependent fixation probability is given by" | finite-time P_fix is given for a stated initial condition |

## Pre-registered prediction
No simulation check applies to this claim. The arithmetic audit was computed in this extraction pass, so the statements below are not pre-registered predictions; they state what each side's model implies.
- Under the claimant's model: If the 1/(2N) were an assumption absent from the mathematics, exact finite chains with a different offspring law could give a different P_fix.
- Under the opposing model: Any exchangeable neutral model has P_fix = p₀ by the martingale property; exact chains give 1/(2N_census) (keruru KR-02; B3 check).
- Result that would change a verdict: A neutral, non-exchangeable model with E[Δp] = 0 but P_fix ≠ p₀ would support Day; none is in the corpus.

## Check
Script: none specific. Related: `research/checks/b3_N_vs_Ne.py` (B3).

R4 B2f (`research/checks/results/R4-B2f.md`; script `b2f_finite_time_formula.py` pre-registered 4213c5e, label criterion-only; combined review #82 `REVIEW-R4-B2f-combined.md`, 0 BLOCKER, 2 MAJOR, 11 MINOR; fix pass de3c1a2; integrated 2026-10-13; low-stakes tier). The revision of 2026-10-13 replaced this claim's Zenodo sentence and added a formula. Diff of the held texts: title, this paragraph, one reference; §2-§6 and the abstract word-identical. No new claim node was made: the law already has one (B2a), so a second would count it twice. "B2f" is the check id only.

**For Day.** The exponent π²Nₑ/T is exact in the short-time limit (local exponent 9.795, 9.499, 8.432 at T/Nₑ = 0.05, 0.25, 1, against π² = 9.870). The derivation route the new sentence describes is real: the arcsine coordinate is Hard Limits' own transform (Q295; distance π√(2Nₑ)), and the eigenfunction series for the conditional fixation time, resummed by the Jacobi identity, has exp(−π²Nₑ/T) in its leading term, a single term that equals the exact F to 1 part in 10⁸ for T ≤ 4Nₑ. In the stated domain the missing prefactor does not touch the conclusion (at T = Nₑ/4: 2.6e-15 exact against 7.2e-18). From an empty start, which is the paper's stated premise, k(T) < μ at every finite T, and the paper's unchanged 15.9% at Nₑ = 10,000 is the exact value (15.87%).

**For critics.** Written as an equality the formula understates the exact F at every T, by (4πNₑ/T)^1.5 e^(T/16Nₑ) in the short-time limit: 3,997x at T = Nₑ/20, 47x at T = Nₑ, 7.2x at T = 4Nₑ. At the paper's own three inputs (T = 252,000; Nₑ = 10,000, 50,000, 63,000) it gives 0.676, 0.141, 0.085 against the exact 0.99999, 0.761, 0.606 (these values of the formula are the audit's substitutions; Day prints none of them). The word "eigenvalue" is wrong: the dominant eigenvalue gives the opposite, long-time law 1 − F ≈ 3 exp(−T/2Nₑ). From a stationary start the flux is exactly μ at every T.

**Readings of Q286 and Q289 (rule RD; integrated 2026-10-13).**
| reading | internal | fidelity (to Hard Limits, self-citation) | external | basis |
|---|---|---|---|---|
| A: a relay of Hard Limits' short-time asymptote, "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ" (Q31), which is what the cited source says. Narrower than the literal text | **`holds`** (sets the field), with ledger slips S-B2f-1 ("=", "closed-form", domain dropped), S-B2f-2 ("eigenvalue"), S-B2f-3 (own-record URL). No number in the paper is derived from the formula | **`partial`** (sets the field): cited, relayed with a flagged omission | Q286 supported in logarithms as T/Nₑ → 0; "guaranteed to be incorrect" **`contested`** on the start state only (sets the field) | R4-B2f P1, T2, T3, T6 |
| B: the literal equality, no domain, replacing k = μ wherever it is used, including the paper's T/4Nₑ ≈ 6.3 (Q291) | `non-sequitur` on the paper's own quantities: its F(T) is "the proportion of theoretically destined fixations that actually complete within T generations", the same object as F_X in its "E[F(T)] = μL ∫₀ᵀ F_X(u) du"; with F_X = exp(−π²Nₑ/u) the integral of 1 − F_X diverges, so there is no mean, against "t̄ = 4Nₑ" (Q293), "SD ≈ 0.538 × 4Nₑ" (Q294) and "≈ T − 4Nₑ". Under R1(ii) no downstream number moves, so this is an error verdict only if the formula is taken as the stated conclusion of the revision (R1(i)); that is a judgement and is recorded as one | `misread` (Hard Limits restricts the law to T ≪ 4Nₑ) | `contradicted` by the exact diffusion at every T | paper §1-§3 (own text); R4-B2f P3, P4, P6a |

What Reading A costs: under it the formula applies to none of the paper's own inputs (T/4Nₑ = 6.3, 1.26, 1.0, none ≪ 1), and the paper's two finite-time formulas have opposite domains (T − 4Nₑ needs T well above 4Nₑ), so no T satisfies both. "Drops exponentially with effective population size" has no instance at those inputs: the exact F falls by 24% and 39% from Nₑ = 10,000 to 50,000 and 63,000, the formula by factors of 4.8 and 8.0.

Fields set by this integration (B1e is not load-bearing): internal `pending` → `holds`; fidelity `partial` (unchanged); external `pending` → `contested`. Counted with the reading-dependent verdicts. Not covered: the 2026-08-23 blog quote in this Statement block, and whether Chalub's expansion is the Kimura (1955) series (that decides how far the credit for the route reaches). Rules SC and U do not apply (the edit introduced the wording; the authors cite themselves). The replacement of the file is a version fact, scored by nothing. The check becomes load-bearing, and needs two further reviews, if a verdict value or defeater on B1, B1a, B2 or B is changed on its strength, if Reading B is adopted as field-setting, or if Day derives a number from the formula; none of those has happened.

## Simulator variables implied
- neutral model class selector (exchangeable Cannings | non-exchangeable)
