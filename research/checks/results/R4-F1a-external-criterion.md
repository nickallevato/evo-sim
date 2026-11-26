# R4 F1a-external: the 19,800 divisor against the human adaptive fixation rate

**Node:** F1a (`docs/research/claims/F1a-day-reply-throughput-and-serial-use-19800.md`), field `external` (now `pending`). **Brief:** `research/checks/briefs/F1a-analyst-2.md`. **Gap:** F1a. Non-computational: no script, no host, no fetch. **This file fixes a criterion; it scores nothing and moves no field.**

## 0. Reuse gate (what held checks already settle)

R4-F1a and R4-F1b settle the mechanics: the count of fixations in a window is supply × u × window, and the latency (2/s) ln 2N = 19,807 equals the spacing only at the serial boundary (one successful allele per latency; F1b cell C). So "is 19,800 the human spacing?" is the same question as "what is the realized human rate of beneficial fixations ρ_h?". Here the effective width is W = 19,807 ρ_h. Interference cannot take W to about 1 in a recombining genome (F2; R4-GAPS-04-07-02 §1.4-1.5). W&B Eq. 7, validated against F2 at 1.5 M, gives a loss of 2Λ₀/R ≈ 3×10⁻⁶ at Λ₀ = 1/19,807 per generation and R = 35 M. Its asymptote R/2 is about 3.5×10⁵ times the serial rate. So the brief's "interference pushes the width near 1" route to the Day band is closed on held results. What is left is the realized count. A published K_a (adaptive substitutions per lineage) already contains all interference, load and supply, so F2, GAP-04 and H add no row here. K_a is held, in R4-A2e-alpha (Boyko 2008, Uricchio 2019, Gayà-Vidal 2014, Eyre-Walker & Keightley 2009) and R4-L3 (the audit's own asymptotic MK). It is the same quantity A2e external uses, and Day's A2e flip, 252,000/1,322 = 190.6, is the F1a comparison with the LTEE. A new run would only reproduce arithmetic on those counts, so this is a criterion, not a script. The gate does not stop: the held results can reach more than one band (section 3). The governing estimate for these results is still with the owner (A2e: D-21, O-17 / ROADMAP C21), so section 2 takes it from A2e.

## 1. Criterion (committed alone before scoring)

**Pre-registration status.** The analyst read every input value before writing this section: the A2e-alpha tables, the L3 headline and counts, the GAP-04 tables. The reuse gate needs them. So nothing below is blind; for `PREREG-STATUS.md` this is `reproduction` (the A-R7 precedent), not `criterion-only`. What is fixed here is the mapping from a held result to a band.

**K1. Scope (rule S).** Scored: claim-file quotes 2, 3 and 5 (Education ¶18, Q&A ¶5 = Q44, Education ¶24), which together state that T / 19,807 is the "maximum achievable" number of beneficial fixations and that the six/seven count comes from it; and quote 4 (Q&A ¶6, "19,800 > 1,600 ... extremely generous"). Quote 1 (the LTEE G_f is a throughput) is not banded. The held Good 2017 quote (verified, `ledgers/fidelity.md`) supports it, and no party disputes it (Camestros CA-10), so the field is set by the human half. Quotes 1, 2, 4 and 5 have no Q id in the quotes files; the claim-file locators are used. Not scored: F1a internal and fidelity; F1, F1b, F2.

**K2. Quantity.** K_a = adaptive (any effect size), coding-only substitutions on the human lineage since the CHLCA, on the model-inferred alpha, in the scope the owner accepted for A2e (D-12). T = 252,000 generations, which is A2e's G1 basis and the claim file's 252,000 / 19,807 = 12.7. Edges:
- **K_D = 3T / 19,807 = 38.17**: spacing T/K_a within 3x of 19,807 (≥ 6,602; W ≤ 3). This is the standing 3x band of rule RD, fixed here in advance.
- **K_C = T / 1,322 = 190.6**: spacing below the LTEE's own G_f (W ≥ 15.0). This is the Day-favourable LTEE value: 1,600 would give 157.5. Quote 4's comparison fails at K_C.

**K3. Readings (rule RD), set in advance.**
- **R-cap** (quotes 2, 3, 5): T/19,807 is a cap on beneficial fixations. A cap is contradicted only by a count above it (beyond the 3x band), never by a count below it.
- **R-cmp** (quote 4 alone): human spacing exceeds the LTEE's. It is contradicted at K_a ≥ K_C.
- **R-all** (all fixations, 17.5M): reported only. It is the least defensible reading, because Day ties 19,800 to the "beneficial fixation time" (quote 5).

The field takes **R-cap**. R-cmp would be more defensible, but it is not a reading of the Statement: it leaves out quotes 2, 3 and 5, which state the count. R-cap is the most defensible reading that covers every scored quote, because "maximum" licenses a count below the cap. The Readings table reports R-cmp beside R-cap in every row.

**K4. Bands** (governing row: point P and interval [L, U] of K_a; exhaustive; branch on P first; ties go to the more central band):

| band | condition | external value (R-cap) | R-cmp, reported |
|---|---|---|---|
| C | L > K_D | `contradicted` (scoped as K2). Qualifier "comparison fails too" if L ≥ K_C, else "cap exceeded > 3x; comparison survives" | contradicted if L ≥ K_C, else not |
| M1 | P > K_D ≥ L | `contested` (lean contradicted) | as P vs K_C |
| M2 | P ≤ K_D ≤ U | `contested` | not contradicted |
| D | U < K_D | `supported` (scoped as K2) if the governing estimator corrects for slightly deleterious polymorphism; `contested, leaning supported` if it is documented to be biased low (asymptotic or naive MK, L3 HM7) | not contradicted |
| X | the owner rules that no MK-family estimate can carry an external value | `untestable` (on held material) | same |

Robustness, symmetric: the band must be the same at T = 252,000 and T = 325,000 (Day 2025; K_D = 49.2, K_C = 245.8). If the two differ, the move row is the more central band (C → M1, D → M2). Yoo's 257,143 (K_D 38.9) is reported only.

## 2. Which held result governs (coupled to A2e; no second ranking)

The F1a row uses the estimate, interval and denominator that the A2e external basis names when that value is set after D-21 / O-17. Under A-R3 the denominator is N2 = 11,090, and the other denominators are reported only. If A2e external stays `pending`, F1a external stays `pending`: section 3 may be scored, but no value is proposed. F1a does not rank the A2e evidence again (OPERATING-PROCESS, "Don't re-litigate"). One consequence is fixed here: F1a cannot be `contradicted` with "comparison fails too" unless A2e's basis also clears 190.6.

## 3. Reachability (ST-05, MA-24): the result that puts each side in its band

- **Critic side (C):** a governing lower bound above K_D, which is alpha_L > 0.344% on N2 (0.444% at T = 325,000). The R4-A2e-alpha fix-pass basis (Uricchio lower HPD) is such a result if A2e adopts it. This is not reached by construction: it depends on the governing estimate and on its value.
- **Day side (D):** a governing upper bound below K_D, which is alpha_U < 0.344% on N2 (0.134% on L3's own Dn 28,565). **No held result reaches D.** L3's bootstrap upper bound is 0.0921. Gayà-Vidal's 0.2% is a null, not a count, and A-R4 set it aside; read as a count it is 29-49, which straddles K_D. A new estimate would be needed, and that is a fetch, out of scope.
- **Day avoids `contradicted` (M2):** L3's row (point below K_D, interval above it) reaches M2 if A2e takes L3 as its basis.
- **X:** reached by an owner ruling only.

So on held material the reachable outcomes are C, M2 and X (or `pending`). Each side can lose. Day's `supported` is not reachable without a new source.

**Expectations at criterion time (not tests).** Day-side reader: M2 or D; the 3x band and R-cap are generous to the cap. Critic-side reader: C, because every bias-corrected estimate on record is far above 38. Analyst: C ("comparison fails too") under the A2e fix-pass basis; M2 under an L3 basis. The F1a outcome therefore follows the owner's O-17 choice for A2e, and the two belong on the same owner card.
