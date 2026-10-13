# R4 B2f: the "closed-form" F(T) = exp(−π²Nₑ/T) in the revised Zenodo 22903977 ("k ≠ μ")

**Status: run, reviewed (combined review `REVIEW-R4-B2f-combined.md`, e442d46: 0 BLOCKER, 2 MAJOR, 11 MINOR, 7 NOTE) and fix-passed 2026-10-13; see "Review resolution" at the end.** "B2f" is the id of this check only. No claim node of that name is proposed (review C2): the law already has a claim file (B2a), and the readings are recorded on B1e.

**In one sentence, both sides.** Day's exponent π²Nₑ/T is exact in the short-time limit, the derivation route he describes exists (all but the word "eigenvalue"), k(T) < μ at every finite T from an empty start as he says, and his 15.9% is the exact value to four digits; written as an equality with no domain, the same formula understates the exact F at every T by a factor (4πNₑ/T)^{3/2}·e^{T/16Nₑ}, misses the exact value by more than 25% at each of the three Nₑ the paper uses, and from a stationary start the flux is exactly μ.

Quoted statements scored here (Q286, N1, N2) are tagged dialectic (an equation, a definition, a stated consequence). The new title is tagged `rhetoric` (rule RH; ledger row proposed below; no verdict).

## Files
- Script `research/checks/b2f_finite_time_formula.py`, registered at **4213c5e**; not edited after. Local run 2026-10-13 (na-garage, one process, 1.4 s, 104 MB). Output `results/raw/b2f.out`, `b2f.json`, `b2f.host` (md5s). The commit is timestamped 19:32:53Z and the run 19:33:23Z; that the push preceded the run cannot be checked from history (review C7; MA-04 caveat).
- **Pre-registration label: criterion-only.** The source texts and B2's reviewed numbers were read before registration (disclosed in the docstring). Bands came from hand arithmetic. T1-T6 are textual verifications, P7 and P6a are identities, two P2 values and the x = 4 row reproduce B2. Every prediction hit; with bands set this way that is weak evidence of anything beyond correct arithmetic and an agreeing second route (two series to 3e-14), and it is reported as such.
- Sources (gitignored): NEW `sources/raw/refresh-2026-10-13/zenodo-22903977-new/new.txt` (from `k_neq_mu.pdf`, md5 739634e9..., record modified 2026-10-13T15:07:16Z); OLD `old.txt` in the same folder (from `Kimura.pdf`, md5 e325def9..., 2026-09-22); HL `sources/raw/day/zenodo-22129121.txt` (Hard Limits, 2026-08-27).
- B2 is not redone. Reused: `cond_fix_cdf` from `b2_hard_limits_internal.py`; the Kimura (1955) series from `b2_posthoc.py`.
- Post hoc (fix pass, 2026-10-13; not registered; a few lines of mpmath at 120 digits, one process, under 5 s, not committed as a script): the identity in "The exact law" re-verified and the share of its leading term computed (review D1).

## What is new versus Hard Limits
1. **Same object, same symbols.** NEW: "the proportion of theoretically destined fixations that actually complete within T generations" and "k(T) = μ·F(T)". HL l.287: "k(T) = μ · F(T), F(T) = P(τ ≤ T | fixation)". T is in generations in both. Nₑ is the diploid effective size in both (HL's distance π√(2Nₑ) counts 2Nₑ gene copies; the exact chain at 2N = 200 confirms the exponent with Nₑ = 100). NEW cites "Day and Athos (2026b)", which its reference list gives as Hard Limits (N3).
2. **What changed in the statement.** HL (Q31): "F(T) ∼ exp( − π² Nₑ / T ), T ≪ 4Nₑ", called "the short-time first-passage law" (N6). NEW (Q286): "the closed-form finite-time completion fraction F(T) = exp(−π²Nₑ/T)". The "∼" became "=", "closed-form" was added, and the domain T ≪ 4Nₑ is gone (NEW contains no "≪" and no "∼").
3. **What changed in the stated derivation, and how much of it is real.** NEW says Day and Athos (2026b) "extract the dominant eigenvalue of that expansion [Chalub's Gegenbauer series] via diffusion asymptotics in the arcsine-transformed coordinate system, converting Chalub's abstract series into" the formula. HL contains none of the strings "Chalub", "eigenvalue", "arcsine", "Gegenbauer". **The route described is nonetheless a real one (Day-side credit, review D1):**
   - *The arcsine coordinate is HL's own transform.* HL l.296-298 (N6): "the transform that turns neutral drift into a symmetric random walk", with distance "π√(2Nₑ)". The transform that gives neutral drift constant variance is the angular (arcsine) one, y = arccos(1 − 2p), whose range is π (already in the audit: R4 P1, claim file B2a). NEW names what HL used without naming.
   - *The eigen-expansion, resummed, yields his exponent as its leading term.* The identity in the next section rewrites the eigenfunction series as a dual series whose first (n = 0) term is (4πNₑ/T)^{3/2} e^{T/16Nₑ} · exp(−π²Nₑ/T). Post hoc numbers: that single term equals the exact F to better than 1 part in 10⁹ at T ≤ 2Nₑ, to 8e-9 at T = 4Nₑ and 5e-7 at T = 5.04Nₑ (it is 15% high at T = 25.2Nₑ). So "converting Chalub's abstract series into" this law describes a derivation that exists, to the extent that Chalub's Gegenbauer expansion is the Kimura (1955) one; that last link is a fidelity question for B1e and was not checked here.
   - *What is wrong is one word.* The **dominant eigenvalue** of the expansion gives the long-time law, 1 − F ≈ 3 exp(−T/2Nₑ) (P5). The short-time law is the **dominant term of the resummed (dual) series**. The slip is the word "eigenvalue", not the route.
4. **What NEW derives from it.** No number. "F(T)" occurs twice outside "E[F(T)]" (a different F, the expected count) and "exp(" once. The consequences drawn are verbal: N1 ("a function that drops exponentially with effective population size") and N2 ("every application of k = μ to a finite-time calculation is guaranteed to be incorrect").
5. **Diff of the held texts, complete (confirmed independently by the review, word level).** Three changes: the title; the §1 Chalub paragraph (sentence 2 reworded, Q286 and N1 added, N5 replaced by N2); one reference added (N3). §2-§6 and the PDF abstract are word-identical, so Q34 and Q36 and every number in B1a stand as quoted.
6. **Effect on existing claim files.** Eleven claim files cite the record: nine under its old title (B1, B1a, B1e, B3b, B4a, B4d, B6a, F, F5) and two by id (A3c, B3g). Only **B1e's first Statement quote** ("Chalub (2022), solving the neutral Kimura equation explicitly in terms of Gegenbauer polynomials, derives the time-dependent fixation probability as a series of exponential decay terms...") is text that no longer exists in the current file. B1's **three** Statement quotes (abstract; §1 "It is a rate, not a count..."; §3 "At generation zero, the subsitution pipeline is empty.") are unchanged in NEW (l.14-16, l.33-34, l.72). All eleven files need the old md5 e325def9 pinned and the retitling noted, since their Source lines name a title the record no longer carries (review K3).
7. **Citation slip (ledger).** N3 gives Hard Limits the URL `https://zenodo.org/records/22903977`, this record's own id; Hard Limits is Zenodo 22129121. The list has a "(2026b)" and no "(2026a)".
8. **The replacement itself is a versions-ledger fact, scored by nothing** (review K5). Same record id, same DOI, still v1, `publication_date` still 2026-09-22, `modified` 2026-10-13T15:07:16Z, new title and new file. No rule turns that into a verdict. "Silent" means only this: the record's metadata as fetched carries no version bump and no dated change note; the audit did not look for an announcement elsewhere.

## The exact law (derived before the run, confirmed by it)
x = T/Nₑ. Exact: F(x) = 1 + Σᵢ (−1)ⁱ(2i+1) exp(−i(i+1)x/4) (Kimura 1955, conditional on fixation, p → 0). By the Jacobi θ₁′ modular identity the same function is

F(x) = (4π/x)^{3/2} e^{x/16} Σₙ (−1)ⁿ(2n+1) exp(−π²(2n+1)²/x).

The two series agree to 3e-14 relative at 13 values of x from 0.05 to 60 (script, double precision); post hoc at 120 digits they agree to 6e-40 or better at x = 0.05, 0.25, 1, 2, 4, 5.04, 25.2, 60 (the 6e-40 at x = 0.05 is cancellation in the first series, whose sum there is 7.5e-83). So the exact short-time law is **F ≈ (4πNₑ/T)^{3/2} exp(−π²Nₑ/T)**: Day's exponent with a prefactor of (4πNₑ/T)^{3/2}, which closes B2's "roughly (Nₑ/T)^1.5". The long-time law, from the dominant eigenvalue, is F ≈ 1 − 3 exp(−T/2Nₑ). C(x) = exp(−π²/x) denotes NEW's formula.

## Results against predictions
**Convention for "within 25%" (review C3).** The script's P4 uses the ratio F/C ≤ 1.25, which gives x* = 44.2. The "% below" figures in P3 are (F − C)/F; on that convention "within 25%" means C ≥ 0.75F, x ≥ π²/ln(4/3) = **34.3**. On rule R1's basis (the correction relative to the stated number, F/C − 1) the three paper-scale gaps are **+48%, +440%, +615%**. All three of the paper's inputs fail on every convention; no result depends on the choice.

| Pred. | Prediction | Result | Score |
|---|---|---|---|
| T1-T6 | Quotes present / absent as listed; HL lacks the eigenvalue vocabulary; NEW lacks the domain; nothing numeric derived from C | All 27 string checks true | verified (not predictions) |
| P1 | Local exponent −d ln F/d(Nₑ/T) below π² and within 1% / 5% / 16% at x = 0.05 / 0.25 / 1 | 9.795 (−0.76%), 9.499 (−3.76%), 8.432 (−14.56%); equals π² − 1.5x + x²/16 | **holds**. Day side: the exponent is exact in the limit T/Nₑ → 0 |
| P2 | F/C > 1 on the whole grid, decreasing; equals (4π/x)^{3/2}e^{x/16} within 1% for x ≤ 2; B2's 47.4 and 17.8 reproduced | 3,997 (x = 0.05), 362 (0.25), 47.42 (1), 17.85 (2), 7.15 (4), 3.25 (8), 1.48 (25.2), 1.18 (60); all four sub-parts true | **holds**. Critic side: C understates the exact F at every T; there is no T at which it is exact |
| P3 | At the paper's T = 252,000: exact F in [0.9999, 1], [0.70, 0.82], [0.59, 0.62]; C = 0.676, 0.141, 0.085; C more than 25% below exact at all three | Nₑ = 1e4 (x = 25.2): exact 0.99999, C 0.676 (32% below; correction +48%). 5e4 (5.04): 0.761 vs 0.141 (81% below; +440%). 6.3e4 (4.0): 0.606 vs 0.085 (86% below; +615%) | **holds**. Critic side. The Day-side alternative (within 25% at one input or more) did not occur |
| P4 | C within 25% of exact only for x ≥ x*, x* in [40, 48]; deficit ratio there > 1e6 | x* = 44.2 on F/C ≤ 1.25 (T/4Nₑ = 11.1); 34.3 on (F − C)/F ≤ 25% (not registered). (1 − C)/(1 − F) = 2.7e8 at 44.2. Within a factor 3 for x ≥ 8.7 (reported, no band) | **holds** |
| P5 | The eigenvalue term 1 − 3e^{−x/2} is within 1% of exact for x ≥ 8 and negative below x = 2.197; at x = 25.2, (1 − C)/(1 − F) > 1e4; C never tracks the deficit within 25% on x ≥ 8 | All true; ratio 3.2e4 at x = 25.2 (1 − F = 1.01e-5, 1 − C = 0.324) | **holds**. C is not the dominant-eigenvalue term; that term gives the long-time law. C is the exponential factor of the dominant term of the dual series, the short-time law, as HL itself calls it |
| P6a | Exact mean 4.000Nₑ; C as a CDF has no finite mean (partial integral grows π² ln 10 = 22.73 per decade) | 4.000000; 49.8, 72.5, 95.2 Nₑ at X = 1e3, 1e4, 1e5 (22.68, 22.72 per decade) | **holds** (first half an identity) |
| P6b | Loss at Nₑ = 1e4: exact in [15.5, 16.5]%; C in [55, 67]% | exact 15.87% (paper: 15.9%); C 60.5% | **holds**. Day side for the unchanged §4 number; critic side for C |
| P6c | Nₑ = 5e4: exact [65, 75]%, C [93, 98]%. Nₑ = 6.3e4: exact [79, 81]%, C [96, 99]% | 69.8% and 96.0% (paper 79.4%); 79.9% and 97.9% (paper 100%) | **holds**. The paper-vs-exact gap is B1a's (already recorded there; no new verdict) |
| P7 | Chain 2N = 200: stationary-start flux/μ = 1 at every T; empty-start flux/μ = chain F(T), within 5% of diffusion at x ≥ 4 | Stationary 1.000000000000 at T = 1, 100, 400, 504, 2520; empty 0, 0.0031, 0.614, 0.766, 0.99999; chain vs diffusion within 1.2% at x ≥ 4. Counts over T = 2520: stationary 1.000 μT, empty 0.843 μT | **holds** (an identity; non-severe) |

No prediction missed. That would normally be reported with the same weight as a miss; here the weight is small for the reason given under "Files". The last line of `b2f.out` ("segregating copies-classes ...") is an unused, loosely labelled diagnostic.

**Where the formula belongs, and where the paper uses its inputs (review D2).** Exact F against C, in HL's stated domain and at the paper's three inputs:

| T/Nₑ | T/4Nₑ | Regime | Exact F | C = exp(−π²Nₑ/T) | F/C | What both say |
|---|---|---|---|---|---|---|
| 0.05 | 0.0125 | in HL's domain (T ≪ 4Nₑ) | 7.5e-83 | 1.9e-86 | 3,997 | no destined fixation completes |
| 0.25 | 0.0625 | in HL's domain | 2.6e-15 | 7.2e-18 | 362 | no destined fixation completes |
| 4.0 | 1.0 | paper, Nₑ = 63,000 | 0.606 | 0.085 | 7.15 | differ: 61% against 8.5% |
| 5.04 | 1.26 | paper, Nₑ = 50,000 | 0.761 | 0.141 | 5.39 | differ: 76% against 14% |
| 25.2 | 6.3 | paper, Nₑ = 10,000 | 0.99999 | 0.676 | 1.48 | differ: complete against 68% |

In domain the missing prefactor does not touch the conclusion, which is HL's own point ("What matters is the exponent", l.303). None of the paper's three inputs is in that domain.

**Audit-derived, not stated by Day (review D5: these must keep this label wherever they are copied):** taken as an equality at the paper's own inputs, k(T) = μ·C gives 0.68μ, 0.14μ and 0.085μ at Nₑ = 1e4, 5e4, 6.3e4 for an allele cohort at the end of the window, and a 60.5% count loss at Nₑ = 1e4; the exact values are 0.99999μ, 0.76μ, 0.61μ and 15.87%. Day prints none of 0.68μ, 0.14μ, 0.085μ or 60.5%.

## Readings (rule RD)
**Q286 + N1 (the formula and what it "replaces").** These readings are recorded on claim B1e (whose Statement sentence the new text replaced), with dated paragraphs in B2a and B2.

| Reading | Internal | Fidelity (to HL, self-citation) | External | Basis |
|---|---|---|---|---|
| **A. A relay of Hard Limits' short-time asymptote.** "closed-form ... F(T) = exp" relays HL's F(T) ∼ exp, T ≪ 4Nₑ, which is what the cited source says. A is narrower than the literal text, not an extended reading. **Sets the fields** | `holds`, with ledger slips: "=" and "closed-form" for an asymptote, domain dropped, "eigenvalue" for "term of the resummed series", own-record URL. R1(ii): no number in NEW is derived from C (T6) and N2 needs only F < 1, so the correction moves no stated number | `partial` (cited, read with a flagged omission) | Q286: `supported` in logarithms (ln F ∼ −π²Nₑ/T as T/Nₑ → 0; the plain ratio F/C diverges there, which HL's already-ledgered "order-one" slip covers). N2: `contested`, on the start state only | P1; T2, T3, T6 |
| **B. The literal equality, no domain.** An equality for any T, replacing k = μ wherever k = μ is used, including this paper's T/4Nₑ ≈ 6.3 (N4) | `non-sequitur`, on Day's own quantities in the same paper (rule N2b; no audit-derived number in the chain): NEW defines F(T) as "the proportion of theoretically destined fixations that actually complete within T generations", the same object as F_X in its "E[F(T)] = μL ∫₀ᵀ F_X(u) du"; §3 states "∫₀ᵀ F_X(u) du = T − ∫₀ᵀ (1 − F_X(u)) du ≈ T − 4Nₑ" from "∫₀^∞ (1 − F_X(u)) du = E[X] = 4Nₑ". With F_X = exp(−π²Nₑ/u), 1 − F_X ≈ π²Nₑ/u and the integral diverges: no mean, so no T − 4Nₑ, against "t̄ = 4Nₑ generations" (N7) and against "SD ≈ 0.538 × 4Nₑ under Kimura's diffusion treatment" (N8; 0.538 = √(π²/3 − 3) is the exact law's value; a law with no mean has no SD). **Judgement recorded as such (review C4):** under R1(ii) no downstream number moves under either reading, so B reaches an error verdict only if the formula is itself the stated conclusion of the revision (R1(i): omitted prefactor and domain) | `misread` (HL's text in hand restricts the law to T ≪ 4Nₑ) | `contradicted` by the exact diffusion at every T; by more than 25% at all three of the paper's inputs | NEW §1, §2, §3 (own text); P3, P4, P6a |

Most defensible reading of the quoted statement: **A** (the statement is then what its cited source says, and true of the limit). Fields under RD: internal `holds`, fidelity `partial`, external `contested`; `reading-dependent:` A → holds / partial / contested, B → non-sequitur / misread / contradicted; counted with the reading-dependent verdicts.

**What Reading A costs (critic side, review K1).** A buys truth with relevance. Under A the formula applies to **none of the paper's own inputs**: they sit at T/4Nₑ = 6.3 ("comfortably in the regime where the approximation holds", N4), 1.26 and 1.0, none ≪ 1. The paper's two formulas have opposite domains: §3's T − 4Nₑ needs "any T sufficiently larger than that mean" (l.86) and HL's law needs T ≪ 4Nₑ, so there is no T at which both hold. N1's "drops exponentially with effective population size" has no instance at the paper's inputs either: from Nₑ = 10,000 to 50,000 and 63,000 the exact F falls by 24% and 39%, where C falls by factors of 4.8 and 8.0. Against A as the natural reading stand "closed-form", "finite-time" and N1's "replaces the steady-state identity": a replacement has to work where the identity is used.

**N2 ("guaranteed to be incorrect")**

| Reading | Internal | Basis |
|---|---|---|
| (i) Counts started from an empty pipe. **This is the paper's own stated premise, not a charity (review D3):** "At generation zero, the subsitution pipeline is empty." (§3 l.72, unchanged since 2026-09-22), and the paper names the objection itself: "A predictable objection will be raised that at speciation the pipeline is not truly empty because the ancestral population carries segregating variation" (§3 l.91-92) | `holds`: exact F < 1 at every finite T. Size at the paper's inputs: end-of-window rate short by 1.0e-5 at Nₑ = 1e4 (24% at 5e4, 39% at 6.3e4); count short by 15.9% (69.8%, 79.9%) | P3, P6b-c, P7 empty row |
| (ii) Every application, whatever the start state | Stronger than the premises (N2d): from mutation-drift equilibrium the flux is exactly μ at every T. No new verdict: the start state is a premise dispute (rule N1) scored at B1, B1c and B6a, and NEW keeps §3's reply to that objection. The stationary-start identity answers a question the paper does not ask | P7 stationary row |

Ledger (S2), no verdict: N2's "cannot be utilized in any finite-time equation" sits beside N4, where the same paper applies a T → large approximation at finite T and calls it "comfortably in the regime"; and the paper's two finite-time formulas have opposite domains (T ≫ 4Nₑ for T − 4Nₑ, T ≪ 4Nₑ for the cited law).

**Title (rule RH; review K2).** "k ≠ μ: The Finite-Time Collapse of Neutral Substitution Theory": tag `rhetoric`. Device: an inequality sign set against a named identity, plus "Collapse" (a totalising noun). Audience and function: readers of the record and of the blog; converts a transient shortfall into the fall of a theory. Dialectical core, checkable and computed above: from an empty start the count is short by 15.9% / 69.8% / 79.9% at Nₑ = 10,000 / 50,000 / 63,000 and the end-of-window rate by 1e-5 / 24% / 39%; from a stationary start by nothing. Not literal-fact-checked; changes no verdict.

## Verdicts and where they go (the lead accepted the review's rulings)
- **No new verdict-bearing node (review C2).** The proposal of a node "B2f" is **withdrawn**: `B2a-exp-pi2-ne-over-g.md` already holds this law (internal `holds`), so a node B2f would count one law twice for Day under Reading A and one slip twice against him under Reading B. "B2f" remains the check id only.
- **B1e** (not load-bearing; its first Statement sentence is the one NEW replaced): keep the old sentence pinned to md5 e325def9 and marked superseded in the source as of 2026-10-13; add the new sentence 2 and Q286 as the current wording; carry the `reading-dependent:` comment and the Readings table. Fields under Reading A: internal `pending` → `holds`; fidelity `partial` (unchanged); external `pending` → `contested` (start state only). Scope of that internal value: the current Zenodo wording (Q286, N1, N2). The Chalub link itself (whether Chalub's expansion is the Kimura 1955 one) stays a fidelity matter at `partial`, and B1e's second Statement quote (blog, 2026-08-23) was not examined by this check.
- **B2a, B2** (Hard Limits): no field changes. Dated paragraph in each recording the restatement without domain and the exact prefactor. HL's own text keeps "∼" and "T ≪ 4Nₑ". HL's "order-one" prefactor slip (ledger S-B2-1) gets its exact size: (4πNₑ/T)^{3/2} e^{T/16Nₑ}.
- **B1, B1a, B:** no change to any verdict value and no defeater (their quoted text is identical in NEW; see "Tier").
- **Rules SC and U do not apply (review C6).** SC covers a slip corrected in the same source; here the edit introduced the wording, and the version with the domain is a separate, earlier source. U covers unidentified authors and allies relaying others; these are the same named authors citing themselves.
- **Ledger entries:** slips: "=" / "closed-form" / dropped domain; "eigenvalue" (narrowed to the word); N3's own-record URL; N2 beside N4 with the opposite domains; RH row for the title. Versions: what changed per the diff, with the metadata behind "silent". None changes a verdict.

## Tier
**Low-stakes; one combined review; the review confirmed the tier on conditions.** B1's verdict rests on three quotes that did not change and on T − 4Nₑ, which the new formula does not feed; B2's rests on HL's text. "Replaces the steady-state identity" is asserted, but nothing downstream is computed from the replacement, so the check is not a step on the path through B1 / B. **It becomes load-bearing, and then needs two further reviews (separate steelman-day and steelman-critic), if any of these happens:**
1. integration changes a verdict value, or adds a defeater, on B1, B1a, B2 or B on the strength of this check;
2. Reading B is adopted as the field-setting reading;
3. Day later derives a number from the formula.

Integration must observe condition 1: no verdict value of B1, B1a, B2 or B is touched and no defeater is added against them.

## Who this helps
- **Day side:** the exponent π²Nₑ/T is exactly right in the short-time limit, confirmed by a second, analytic route (P1). **The derivation he describes is real:** the arcsine coordinate is Hard Limits' own transform, and the eigen-expansion, resummed, has exp(−π²Nₑ/T) as the exponential of its leading term, a single term that reproduces the exact F to within 1 part in 10⁸ for T ≤ 4Nₑ; only the word "eigenvalue" is wrong. In the domain where the law belongs the missing prefactor changes nothing: at T = Nₑ/4 the exact F is 2.6e-15 against 7.2e-18, and either way no destined fixation completes, which is what Hard Limits says matters. "Drops exponentially with effective population size" is true of the exact short-time law as well as of his formula. The cited source (Hard Limits) states the law with its domain, so the charitable reading is his own earlier text, not audit generosity. From an empty pipe, which is the paper's stated premise, no finite window reaches k = μ exactly, in the direction he states; his unchanged §4 figure of 15.9% at Nₑ = 10,000 is the exact value (15.87%). The empty-start count on the exact chain is 0.843 μT at his T/Nₑ.
- **Critic side:** the formula is an asymptote for T ≪ 4Nₑ presented as a closed form with the domain removed. It is below the exact F at every T (by 4,000x at T = Nₑ/20, 47x at T = Nₑ, 7x at T = 4Nₑ) and is more than 25% off, on any convention, at each of the three Nₑ the paper itself uses; at Nₑ = 10,000 it gives 0.68μ (audit-derived) where the exact rate is 0.99999μ. Read as its source states it, it applies to none of the paper's inputs, and no T satisfies both of the paper's finite-time formulas. It is not the dominant-eigenvalue term, which gives the opposite regime and shows k → μ exponentially fast (1 − F = 3e^{−T/2Nₑ}). Read literally it contradicts the paper's own mean fixation time, its own SD figure and its own T − 4Nₑ. From standing variation at equilibrium the flux is μ at every finite T, so N2 holds only for an empty start; the empty start is what the paper assumes in its own words, and the paper itself names the standing-variation objection.
- **Both:** nothing numeric in the paper depends on the new formula, so neither side's count changes. What separates readings (i) and (ii) of N2 is the start state, which this check does not decide (B1c, B6a).

## Quotes for integration to file (verbatim; quotes files not edited here)
- N0 (title), NEW title block, record modified 2026-10-13: "k ≠ μ: The Finite-Time Collapse of Neutral Substitution Theory"
- N0b, NEW §1 Chalub paragraph, sentence 2 (reworded 2026-10-13): "Chalub (2022), solving the neutral Kimura diffusion equation with absorbing boundaries, derives the explicit transient solution as a Gegenbauer polynomial expansion whose terms converge to the steady-state fixation probability u(p) = p only as t → ∞."
- N1, NEW §1 Chalub paragraph, sentence 4, record modified 2026-10-13: "Multiplied through the mutation supply, this yields the time-dependent substitution rate k(T) = μ·F(T), which replaces the steady-state identity with a function that drops exponentially with effective population size (Day and Athos 2026b)."
- N2, NEW §1, sentences 5-6 (already under Q286 as "following sentence"; the first of the two sentences is also new): "The steady state requires infinite time. It therefore cannot be utilized in any finite-time equation, and every application of k = μ to a finite-time calculation is guaranteed to be incorrect."
- N3, NEW References: "Day, V. and Athos, C. (2026b). The Hard Limits of Fixation Through Genetic Drift. Zenodo. https://zenodo.org/records/22903977."
- N4, NEW §3 ¶5 (unchanged from 2026-09-22): "For the human-chimpanzee application, T = 252,000 generations and 4Nₑ = 40,000, giving T/4Nₑ ≈ 6.3 — comfortably in the regime where the approximation holds."
- N5, OLD §1 last two sentences (2026-09-22, removed 2026-10-13): "The steady state is the destination; it is not the journey, and it is not the starting point. Every finite-time application of k = μ treats the destination as though it were the departure."
- N6, HL l.296-299 (2026-08-27): "under the transform that turns neutral drift into a symmetric random walk, the distance from a single copy to fixation is a fixed length, π√(2Nₑ), and the chance of covering it in time T is the short-time first-passage law"
- N7, NEW §2 (unchanged): "t̄ = 4Nₑ generations This is the mean time to fixation for a neutral mutation, conditional on fixation."
- N8, NEW §3 ¶1 (unchanged): "The process has a mean length of 4Nₑ generations and a broad distribution around that mean (SD ≈ 0.538 × 4Nₑ under Kimura's diffusion treatment)."

## Limits
- Constant-size neutral Wright-Fisher diffusion, one new copy, p → 0; the chain is 2N = 200. No demography, no selection, no overlap (those belong to B1c, B3).
- "Day and Athos (2026b)" is identified from NEW's reference list by title only. The refresh of 2026-10-13 found Hard Limits' record unchanged, so the held HL text is taken as the cited one; a later HL revision containing an eigenvalue derivation would change the fidelity reading, not the numbers.
- The eigen-expansion does yield this exponent, as the leading term of its resummed (dual) form: shown above for the Kimura (1955) series. Not examined: whether Chalub's (2022) Gegenbauer expansion is that series term for term (B1e), and whether Day and Athos carried out the resummation or took the law from the random-walk distance argument that Hard Limits prints.
- The stationary-start flux in P7 is a martingale identity, not an independent test; it shows what the two readings of N2 rest on, nothing more.
- The post hoc 120-digit check was run after the review named the result; it confirms an identity and is not a test.

## Open
1. Integration (Q ids; B1e wording, comment and Readings table; B2a / B2 paragraphs; md5 pinned in the eleven citing claim files; versions and slips rows; argmap registration; QUEUE.md items closed).
2. B1e: confirm whether Chalub's expansion is the Kimura (1955) one (fidelity; decides how far the D1 credit reaches).
3. Next refresh: check whether Hard Limits (Z22129121) is revised to match the new wording, and whether Day derives a number from the formula (tier condition 3).
4. Bookkeeping outside this write-up (review C8): Q286's locator says "sentences 3-5" (the quote is sentence 3, the following sentences are 5-6); `R5-draft.md` still shows B2 as "I pending" while the claim file has `holds`.

## Review resolution (fix pass, 2026-10-13)
Combined review `REVIEW-R4-B2f-combined.md` (e442d46). The script and its raw outputs are unchanged; the only new computation is the post hoc identity check under "Files".

**MAJOR**
- **C2 (the proposed node duplicates B2a): accepted.** Node proposal withdrawn; "B2f" is the check id only. Readings, `reading-dependent:` comment and Readings table go on B1e; dated paragraphs on B2a and B2; no node, no double count. See "Verdicts and where they go".
- **D1 (the described route is real): accepted.** Item 3 of "What is new" now credits the arcsine coordinate as HL's own transform and the resummed eigen-expansion as the source of the exponent, with post hoc numbers for the leading term; the slip is narrowed to the word "eigenvalue"; "Who this helps" and the opening sentence carry the credit; the Limits line is corrected. The identity was re-verified at 120 digits before being restated.

**MINOR**
- **C1 (wrong count): corrected in place.** B1 has three Statement quotes, all three unchanged in NEW (item 6).
- **C3 (two conventions for "within 25%"): corrected.** Convention stated once above the results table; 34.3 given beside 44.2; R1-basis gaps +48% / +440% / +615% added. No result changes.
- **C4 (basis of `non-sequitur` under B): accepted.** Reading B now rests on Day's own F_X integral, mean and SD (N2b); the N2a comparison with the audit-derived 60.5% is removed from the basis. The R1(i) judgement is stated as a judgement in the table.
- **C5 (external field mixed readings): corrected.** External column added: A → supported in logarithms (Q286) and contested on the start state (N2); B → contradicted. Field `contested`, on the start state only.
- **D2 (no in-domain row): added.** Table "Where the formula belongs" with x = 0.05 and 0.25, and a sentence in "Who this helps".
- **D3 (reading (i) is the paper's premise): added** to the N2 table and to the critic-side bullet, with both §3 quotes.
- **D4 (equal prominence): done.** One opening sentence carries both sides; the status line no longer leads with the 25% miss.
- **K1 (under A the formula applies to no case in the paper): added** as its own paragraph under the Readings table, with the opposite-domain point and the 24% / 39% against 4.8x / 8.0x comparison; the S2 ledger line extended.
- **K2 (title untagged): done.** Tagged `rhetoric` with device, audience, function and core; ledger row for integration.
- **K3 (stale titles): accepted.** Item 6 now calls for the md5 pin and retitling note in all eleven citing claim files.
- **K4 (second own-text contradiction): added.** The SD ≈ 0.538 × 4Nₑ sentence (N8) is cited beside N7 under Reading B.

**NOTES**
- C6: stated under "Verdicts and where they go" (SC and U do not apply). C7: the weak-evidence sentence is kept, and the unverifiable push order is stated under "Files". C8: listed under "Open" item 4; the "(2026b)" without "(2026a)" is in item 7. D5: the audit-derived label is strengthened and attached to 60.5%. D6, K6: no action. K5: item 8 states the metadata behind "silent" and that the replacement is scored by nothing.
