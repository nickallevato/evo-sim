# Correctness review: R4 B2 (with B, rule N): Hard Limits checked against its own text

Reviewer: correctness pass, 2026-10-10. Read: `results/R4-B2.md`, `research/checks/b2_hard_limits_internal.py` (identical to the pre-registered 3d07343; `git diff 3d07343 HEAD` on the script is empty), `results/raw/b2_hard_limits.out`, the HL text `sources/raw/day/zenodo-22129121.txt` (read as data, by line range), claim files B, B2, B1c, B1d, `R5-draft.md` (B2 rows), `R4-X1-verdict-rule.md` (C, S, SC, N, RH), `quotes-day.md` Q29-Q34.

Independent work: one scratch evaluation of the closed-form neutral diffusion series (Kimura 1955, conditional on fixation, p -> 0), F(T) = 1 + sum_i (-1)^i (2i+1) exp(-i(i+1) T / 4N_e), and its time average (1/T) int_0^T F dt, in `python3 -I` in the session scratchpad (< 1 s, no numpy, nothing in the repo). It checks the chain's discreteness and gives the cumulative-count column used in findings 2 and 3. No check script was run; nothing in the repo was edited except this file.

**Verdict: no BLOCKER.** The mechanical results (P1-P5, the P6 arithmetic) are right, and the pre-registration is clean. Three MAJOR findings concern the rule-N section for B: (1) it scores a paraphrase, not a verbatim Statement; (2) the "fill" numbers are the end-of-window flux, not the delivered count that "rescue the shortfall" needs; (3) the input table leaves out HL's own accepted lineage window, and with that window the "H7 vs H8" conflict goes away.

## What I verified (all reproduce)
1. **Pre-registration integrity.** The script is unchanged since 3d07343 (12:36:44). `raw/b2_hard_limits.out` mtime is 12:36:45, so the run came after the commit. The run was local: 0.8 s and 100 MB, inside the AGENTS.md "trivial" limit.
2. **Quotes and locators.** H2 (l.287), H3 (l.301), H4 (l.304-311), H5 (l.329-331), H6 (l.124-126), H7 (l.353-356), H8 (l.363-366), H9 (l.52-56) and H10 (l.206-207) are verbatim, at or within a line or two of the locators the write-up gives (the numbers here are the ones I found).
3. **k(T) = mu F(T) with conditional F is the correct transient flux.** Destined mutations enter at 2N mu x 1/(2N) = mu. One entering at s completes at T with density f(T - s), so the completion rate at T from an empty start is the integral over s in [0, T] of mu f(T - s) ds = mu F(T). Reading 1 is the reading under which HL's own formula is right.
4. **Exact chain.** Conditioning by v[2N] x 2N is exact, because P(fix) = 1/(2N) from one copy. The mean is 396.5. The diffusion series gives a mean of exactly 4N_e (the sum telescopes to ln 2 + (1 - ln 2)).
5. **Arithmetic.** P4: pi^2 x 1.825e7 / ln 10 = 7.823e7. P5: 4(4N - 2)/(V_k + 2) < G gives N < (V_k + 2)G/16 + 1/2. H8: 4N_e = 4 x 57,143 = 228,571 and G = 80,000, so 0.350.
6. **Diffusion vs chain (2N = 200).**

| T/N_e | chain F | diffusion F | diffusion (1/T) int F |
|---|---|---|---|
| 1.0 | 3.09e-3 | 2.5e-3 | (< 0.001) |
| 1.4 (H8, 2 My) | 0.0287 | 0.0255 | 0.0034 |
| 2.0 | 0.136 | 0.128 | 0.024 |
| 4.0 (at the ceiling X: T = 4N_e) | n/a | 0.606 | 0.201 |
| 4.55 (census 1e5, V_k 5, **6.5 My**) | not run | 0.697 | 0.256 |
| 8.0 (N_e 1e4, 2 My) | 0.947 | 0.945 | 0.514 |
| 10.4 (N_e 2.5e4, 6.5 My) | 0.984 | 0.984 | 0.619 |
| 26 (N_e 1e4, 6.5 My) | 1.000 | 1.000 | 0.846 |

At large T the time average is 1 - 4N_e/T + ..., as it should be (26: 0.846 vs 0.846).

## Findings

### 1. MAJOR: the provisional non-sequitur for B scores a paraphrase, not a verbatim Statement (rule S1, N2b scope)
Locator: R4-B2 "Rule N" section, sentence "B's step to 'neutral theory ... cannot rescue the shortfall'".

Problem. "Cannot rescue the shortfall" is the title of claim B, not a quote. B has two Statement quotes:
- (a) the blog of 2026-02-04 ("the second is flat-out wrong"). It predates HL by seven months, so HL is not its derivation. N2b's exposure note limits "own text" to the same source and the texts the claim cites, and B3c's cross-document basis was dropped for this reason.
- (b) HL's abstract sentence "The domain of k = μ is confined to ...". That is B2's quote, which the write-up scores as `holds`.

HL also says, two lines earlier in the same abstract (l.22-24): "What substitution these abundant populations show is not produced at their current size; it is residual drainage from the smaller populations they descend from." At l.425-428 it says "This hard limit to fixation does not kill neutral theory ... Drift does fix neutral alleles". So nothing in B's Statement, as quoted, asserts that ancestral drainage is insufficient.

HL does contain B-type sentences: l.453-457, "And now the neutral channel closes on the same window ... the neutral substitutions cannot be finished, because the pipe that would finish them never fills. Both the priced channel and the free channel shut inside the same lineage duration", and l.464-467, "the pipe was nearly empty". The write-up neither quotes nor RH-tags them.

Fix. Choose one route and record it:
- (i) Under S1, add l.453-457 (and l.464-467) to B's Statement, tag them under RH1 with rule C on kind, and score N2b against l.22-24, H7 and l.437-441 ("loaded, at least partially") within the same source.
- (ii) Score B's HL quote `holds` (identical to B2), log HL l.425-428 as a later softening of the Feb quote (`ledgers/versions.md`, SC "corrected in a later source"), and keep B internal `pending` on route (i).

The steelman reviews take opposite sides on the RH tag. The current "non-sequitur (provisional), against H7" has no valid target as scored.

### 2. MAJOR: "fill" is the end-of-window flux F(T); the shortfall question needs the delivered count, mu times the integral of F
Locator: the Rule N table, "fill is 95-100%", "the pipe is 95-100% full", and P6 "the pipe is about 3% loaded".

Problem. k(T)/mu = F(T) is the rate at the end of the window. The number of substitutions delivered from an empty start over the window is mu times the integral of F from 0 to T, which is Day's own later formula E[F(T)] = μL ∫₀ᵀ F_X(u) du (Q34, Z22903977, 2026-09-22). Its time average is much lower: 0.3% (H8, not 3%), 51% (N_e 1e4, 2 My, not 95%), 62% (2.5e4, 6.5 My) and 85% (1e4, 6.5 My). The Limits section says this ("lower still"), but the critic paragraph headlines the flux figures. HL's own word "fill" means flux (l.361-363, "Kimura's rate is approached"), so the table is not wrong. The prose uses it for the count question, though.

Fix. Add a "(1/T) ∫F" column (diffusion series, or the same chain summed: post hoc). Label F(T) "end-of-window flux / mu". State that the pre-window fill (finding 3, and B1d) raises both columns.

### 3. MAJOR: the input table omits HL's own accepted lineage window; with it, H7 and H8 cohere and the "opposite directions" claim fails
Locator: the Rule N table, and the sentence "H7 and H8 therefore pull in opposite directions inside the same paper."

Problem. HL Table 1 (l.157) runs humans on the lineage window, 6.5 My, and l.244-253 accepts the first objection: "The objection is valid, the correction triples the ceiling". The human lineage ceiling is X = 114,000 (Q33: "a hundred thousand as a lineage"). H8's census of 1e5 is therefore at the lineage ceiling, which is what H8 itself says ("the near-ceiling regime the small population occupies"). l.361-363 says that near X "the pipe substantially fills". At census 1e5, V_k 5 and 6.5 My, T/N_e = 4.55, F = 0.70 and the time average is 0.26. At X exactly, T = 4N_e by definition, so F = 0.61.

On that reading H7 ("short enough to fill"), H8 and l.361-363 agree. The tension exists only because H8 pairs a lineage-ceiling census with the species window ("the full two million years"). That mismatch is H8's own internal inconsistency, and it should be recorded as such (a slip, R1 test below), not as a contradiction between H7 and H8.

Fix. Add the row (census 1e5, 6.5 My) and the at-X row. Restate the section as three readings of Day's ancestral input: field 1e4; H8 at 2 My; H8 at 6.5 My, which equals the at-X case. Note the window mismatch in H8.

R1 for H8's window: correcting 2 My to 6.5 My moves H8's "thirty-five percent" to 114% (linear), i.e. above the ceiling. It flips "partly-loaded" for the linear bound. But H8 is an aside inside the second objection, not a Statement quote, so under S2 it is a ledger entry.

### 4. MINOR: P7's numeric sub-prediction failed and is scored "holds in part"
P7 pre-registered "F of order 0.05-0.35" for an ancestral population near 1e4. The result is 0.95 (2 My). That is a failure in the critics' favour, the mirror image of P6. Record it as failed, as P6 is.

### 5. MINOR: P6 failed on two sub-parts; the table names one
The pre-registered exact/exp ratio was >= 50; the result is 33. Add it to the P6 row.

### 6. MINOR: P3's ratios mix discreteness with the prefactor; HL's "order-one ... two orders" is a ledger slip either way
At T = N_e the diffusion ratio is 48 (chain 60). At T = N_e/4 (25 generations, 2N = 200) the 4,850 is likely dominated by discreteness, so "exceeds HL's stated two orders" at N_e/4 is not shown. The diffusion values at T/N_e = 1 and 2 imply a prefactor growing roughly as (N_e/T)^1.5. That is not an order-one constant. Extrapolated to H5 (N_e/T = 1.8e7) it is about 11 decimal orders against 7.8e7: immaterial (R1). It is a slip ledger entry for "an order-one detail that could be wrong by two orders of magnitude" (l.303-304). Fix: quote diffusion values and state that the chain is at 2N = 200.

### 7. MINOR: HL l.361-363 is not scored
"When Nₑ is of the same order as T ... the exponent is order one: the pipe substantially fills". At T = N_e the exponent is pi^2 ≈ 9.9 and F = 0.3%. The fill is "substantial" only near T ≈ 4N_e (0.61). The slip concedes more fill than HL's own law gives (in the critics' favour), and it does not move HL's conclusion. Ledger.

### 8. MINOR: P1 settles the body definition, but the abstract and H5 are phrased unconditionally; and "which probability" is not a fidelity question
Q30 (abstract) reads "a neutral allele's chance of fixing within the generations its lineage will ever have". l.329-331 reads "the probability that a neutral mutation arising now fixes within that era". Read literally, both are the unconditional chance (F/(2N)). Under rule C the conditional reading holds, and the gap of 1/(2N), about 10 decimal orders, is immaterial against 7.8e7 (R1). "Which probability" was a driver of internal reading (R5-draft l.120), not a citation question. B2's fidelity `unverifiable` rests on uncited inputs: Maruyama was not retrieved, V_k is unsourced, and there is no reference list. Fix: state that P1 resolves the reading, and propose the fidelity verdict separately (unchanged unless the citations are checked).

### 9. MINOR: the pre-registered H9/H10 item is missing from the write-up
The docstring P7 says H9 with H10 "is also scored ... recorded, not scored as an error". The write-up does not mention H10. Add the line (see steelman-critic F5).

### 10. MINOR: quote ids
H1-H10 are local labels. H2-H4 and H7-H10 have no Q ids (Q29-Q33 cover abstract and table text). Integration must add Q entries with locators and dates (hard rule 2), together with the l.22-24, l.425-428 and l.453-457 quotes.

## Not wrong, but worth knowing
- P2: Day says "a quarter of the mean time" (97.75 generations), and the script uses t = 100. The expected count is slightly below 9.3, and 6 is still inside. The SD of the conditional fixation time is about 2.15 N_e = 215, so the standard error of a 3,000-fixation mean is about 3.9. Day's 391 against 396.5 is 1.4 SE, so it is consistent with sampling, which is better than calling it "1.4% low".
- H5 uses N_e = 7.3e9 at census scale (Table 3 note). Wright's formula with V_k = 5 gives 4.7e9, or 5.0e7 decimal orders. HL flags this as immaterial in the same source (SC), and B1d already records the 0.91 vs 0.57 ratio.
- The diffusion F(1.4) = 0.0255 agrees with the chain's 0.0287 to 13%, so P6's failure is not a discreteness artefact.

## View of the verdicts
- **B2 internal `holds`:** agreed, on stronger grounds than rule C. The abstract itself (l.22-24) confines the claim to current size.
- **P2 holds; P4, P5 hold; P6 failed (two parts); P7's numeric part failed.**
- **B internal:** not `non-sequitur` as scored (finding 1). Use `pending` until route (i) or (ii) is chosen. If (i) is chosen, the score turns on the RH tag and rule-C reading of l.453-457, and on finding 3's three-reading table.
