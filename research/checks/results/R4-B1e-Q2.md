# R4 B1e-Q2: B1e's second Statement quote (the 1/(2N) blog sentence) and the Kimura (1955) link

**Status: run 2026-10-14, written up; not yet reviewed.** Brief `research/checks/briefs/B1e-Q2-analyst.md`; claim B1e (`docs/research/claims/B1e-chalub-2022-reading.md`, not load-bearing). Paperclip: check EVO-7, this write-up EVO-9.

**In one sentence, both sides.** Day is right that Chalub adds the two constraints to the Kimura equation from outside it, that Chalub himself says they come from the discrete process, and that probability conservation alone leaves the fixation/loss split free (P5). Against that, Chalub never writes "1/(2N)", never calls the constraints an assumption, and names Moran as well as Wright-Fisher. The second constraint is also exactly the bookkeeping of the classical solution's own boundary flux (P4, to 5e-64), and P_fix = 1/M holds to 1e-12 in Wright-Fisher, Moran and a beta-binomial Cannings chain alike (P6b). On Q2 the registered call is **P7 MISS, band X**. A post hoc diagnosis traces the miss to the audit's own script (float rounding of the x grid), not to any difference between Chalub's b(t) and the series B2f used; the reviews and the lead rule on which result governs. Whether that series is Kimura's of 1955 stays `unverifiable` (P8 band U, no primary text held).

RH: QB is tagged `dialectic` (a checkable statement about a cited paper), as registered.

## Files
- Script `research/checks/b1e_q2_chalub_link.py`, registered at **68fcefb** (2026-10-13T21:41:53Z, pushed to `origin/research`); not edited since (md5 196b3c78... in the host record).
- Main run: local workstation, 2026-10-14T00:18:19Z, one process, 15.5 s, max RSS 104 MB (within the trivial-check allowance; the docstring planned it there; na-workhorse is busy with `ph2`). Outputs `results/raw/b1e_q2.out`, `b1e_q2.json`, `b1e_q2.host` (commit **b50b6d9**).
- **Post hoc** (not registered; diagnosis of the P7 miss): `research/checks/b1e_q2_posthoc_p7.py`, committed at **56c6847** before it ran, with its expectations H1, H2 in the docstring. Output `results/raw/b1e_q2_posthoc_p7.out`, `.host` (commit **d711d17**). Local, under 5 s.
- **Pre-registration label: criterion-only** (disclosed in the docstring): both source texts were read in full before registration. P4, the P7 coefficient identity and P1s were derived by hand first, so they check hand algebra by an independent numerical route and are not blind predictions. P6c's WF band was informed by B2f's P7. Smokes ran with every value and every call suppressed.
- Sources (gitignored, read only), `sources/raw/b1e-q2-2026-10-13/`: Chalub, arXiv:2208.00148v1 (sha256 a720d24b..., = bib row Chalub2022), text by `pdftotext -layout` (sha256 c7225292...). Blog post of 2026-08-23 (published 09:37:10Z, modified 13:16:18Z; sha256 be40cd76...). The script asserts all three hashes and they passed. **Kimura (1955) not held** (PMC, Europe PMC and PNAS served challenge pages on 2026-10-13; none bypassed).

## Textual facts (verified, not scored; all as printed)
| Id | Result | Printed |
|---|---|---|
| T1 | QB verbatim, once | paragraph `[4]` by `blog_paragraphs()` (the claim file says "¶5 of extracted text"; it is line 7 of the held `.txt` extraction); published 2026-08-23T09:37:10+00:00, modified 13:16:18+00:00 |
| T2 | B2, B2b, B3a-e, B6 verbatim | `missing: []` |
| T3 | C2, C4, C5 present | ok |
| T4 | C1, C3 present; "Wright-Fisher" ×2; "assum" ×1, in C9 | `wright_fisher_count: 2`; context `' C0α (x) = 1. If we assume (in the sense of distributions) t'` |
| T5 | no "1/(2N)", "1/2N", "population size", "effective", "absorb"; every "2N" is the set 2ℕ | all `False`; contexts `'n ∈ 2N ,'`, `'n ∈ 2N +'`, `'0 n∈2N n'`, `'N n∈2N ∞'` |
| T6 | C6, C7, C10, C11 present | ok |
| T7 | C8, C12 present | ok |
| T8 | no held Kimura (1955) | `held_copies: []` |

## Results against predictions (REGISTERED; every band line as printed)
| Id | Band (registered) | Printed | Call |
|---|---|---|---|
| P1 | Chalub's (3)-(6) and the α = 3/2 integrals on [0,1], ≤ 1e-20 | worst_36 1.88e-37; worst_01 4.59e-45 | **HIT** |
| P1s | C12 false as written: RHS(4) at n = 0 is 2; α = 0.75, n = 1 RHS = LHS = 0.25 | rhs4_n0 = 2.0 at all six α; rhs4 0.25, lhs4 0.25 | **HIT** (scored for neither side) |
| P2 | eigenfunctions, λ_n = (n+1)(n+2), and Chalub's ODE, ≤ 1e-12 | worst_eig 7.0e-39; worst_ode 2.61e-39 | **HIT** |
| P3 | Beta(4,5) start: d_n, sums, a(t), b(t), b(∞) = 4/9, a(∞) = 5/9, ≤ 1e-25 | worst 1.38e-40; b_inf 0.444444444444; a_inf 0.555555555556 | **HIT** |
| P4 | b′ = −J(1), a′ = +J(0), 20 cells, relative ≤ 1e-15 (**the severe item**) | worst_rel 4.98e-64 (x0 = 0.001, t = 0.05); 12 of 20 cells print 0.0 in at least one column | **HIT** |
| P5 | constraint 1 alone: d/dt ∫xp ≠ 0 (≥ 1e-6) for θ = 0, 0.5, 1; Chalub's b/m not constant | d/dt ∫xp = −0.101205, 0.107758, 0.31672; b/m at t = 0.05, 0.5, 2: 1.116333e-13, 0.022195177, 0.096006537 | **HIT** |
| P6a | neutral rows, ≤ 1e-10; τ mapping (asserted) | max\|E[j\|i]−i\| WF 5.68e-14, Moran 2.84e-14, BB 5.68e-14 | **HIT** |
| P6b | P_fix·M = 1 within 1e-9, all three chains | WF, Moran, BB each 1.000000000000 | **HIT** |
| P6c | \|F_chain − F_C\| ≤ 0.02 everywhere; relative ≤ 5% (WF, Moran) / 10% (BB) at τ ≥ 1 | max abs: WF 0.00558 (τ = 1), Moran 0.00229 (τ = 0.5), BB 0.00548 (τ = 1). Max rel at τ ≥ 1: WF 0.92%, Moran 0.30%, BB 0.90% | **HIT** |
| P7 | coefficient ≤ 1e-40; value vs B2f ≤ 1e-30 at six x; finite-x0 monotone and ≤ 1e-3 at x ≥ 1; large-t ≤ 1e-3 | coef_err 0.0; **worst_value_rel 1.09e-14**; finite_monotone True; within 1e-3 True; large_t_worst 3.43e-9 | **MISS, band X** |
| P8 | band U if no held copy | band U, held [] | **HIT (U)** |

Summary as printed: 10 of 11 HIT; `Q2 bands: P7 X, P8 U`.

**The P7 miss, in full.** Four of P7's five items held. The value item failed at three of the six x and held at the other three:

| x | Chalub limit | B2f F_dec | rel (printed) |
|---|---|---|---|
| 0.05 | 7.50623852038086e-83 | 7.50623852038078e-83 | **1.09e-14** |
| 0.25 | 2.59078703142138e-15 | same | 1.12e-138 |
| 1 | 0.00245269457898704 | same | 7.08e-157 |
| 4 | 0.606344920236374 | same | 1.07e-160 |
| 5.04 | 0.761223656896024 | same | **5.45e-18** |
| 25.2 | 0.999989883954298 | same | **3.59e-21** |

Finite x0 (printed): the relative gap to the limit falls by a factor 100 for each factor 100 in x0, at every x. For x0 = 1e-10 it is 7.84e-7 (x = 0.05), 3.04e-8, 1.69e-9, 6.09e-11, 3.07e-11, 1.01e-15 (x = 25.2).

P6c detail (printed; τ = 0.25 and 0.5 are under the absolute band only): F_chain / F_C at τ = 1 is WF 0.61377 / 0.60819, Moran 0.61004 / 0.60819, BB 0.61367 / 0.60819. At τ = 0.25 the relative gaps are 15.9% (WF), 8.3% (Moran), 13.1% (BB): large in relative terms, but on values near 0.003. BB's N_e per generation prints 50.25 against WF's 100.0 at M = 200, the halved N_e the registration intended.

## Post hoc diagnosis of the P7 miss (not registered; descriptive; cannot change the registered call)
Cause, read from the code before the post hoc script was written: `p7_relay()` evaluates Chalub's side at `t = mp.mpf(x) / 4` from a Python float, while B2f's side gets `F_dec(str(x))`, an exact decimal. 0.25, 1 and 4 are exact in binary; 0.05, 5.04 and 25.2 are not. The two functions were therefore compared at arguments about 1e-17 apart, and the steep F at x = 0.05 (F ≈ 7.5e-83) amplifies that gap.

Output of `b1e_q2_posthoc_p7.py` (as printed):

| x | rel, exact-decimal x on both sides | registered rel | first-order prediction \|d ln F/dx\|·\|mpf(float x) − x\| | prediction / registered |
|---|---|---|---|---|
| 0.05 | 2.17e-68 | 1.09e-14 | 1.09e-14 | 0.9976 |
| 0.25 | 1.12e-138 | 1.12e-138 | 0 | (x exact) |
| 1 | 7.08e-157 | 7.08e-157 | 0 | (x exact) |
| 4 | 1.07e-160 | 1.07e-160 | 0 | (x exact) |
| 5.04 | 1.41e-160 | 5.45e-18 | 5.45e-18 | 1.0 |
| 25.2 | 9.27e-161 | 3.59e-21 | 3.59e-21 | 1.001 |

H1 (all six ≤ 1e-30 with exact x): **HOLDS**. H2 (first-order prediction within 1.1× of the registered figure; 0 where x is exact): **HOLDS**. The remaining 2.17e-68 at x = 0.05 is the same order as B2f's `F_dec` stopping rule (absolute 1e-150) divided by F ≈ 7.5e-83 (≈ 1.3e-68). That is my inference, not a printed check.

Reading of the two together: with matched arguments, Chalub's b(t; x0)/x0 as x0 → 0 equals, at t = T/(4Nₑ), the eigen-series B2f used, to 68-160 digits. Term by term, mode n of Chalub is term i = n + 1 of B2f's series (coef_err printed 0.0), and Chalub's large-time asymptote b ≈ x0 − 3x0(1 − x0)e^{−2t} holds to 3.43e-9 at t = 5. Had the value item passed, every P7 item would have been in band E. This is post hoc and is labelled so. The registered call stays MISS / X.

## Readings of QB (rule RD; all as registered)
| Reading | Fidelity (to Chalub 2022) | Internal (post's own material) | External (mathematics) | Basis |
|---|---|---|---|---|
| **R-A** "the 1/(2N)" = neutral P_fix = p0; "the mathematics" = PDE (7) on the open interval; "imported from the Wright-Fisher model" = constraint 2 enters from the discrete process. **Most defensible; sets the fields** | `partial`: the laws are added to (7), which is accurate (C2: "two additional conservation laws had to be introduced into the model"). But Chalub calls them "derived directly from the discrete process" (C1), names "the Moran and the Wright-Fisher processes" (C3), never uses "assum" about them (T4) and never writes 1/(2N) (T5). Relabelled and narrowed | `holds` (T2: B3d says the fixation probability follows once the constraint is imposed; nothing in the post contradicts QB) | `contested`: true that (7) on the open interval fixes no split (P5); false that what fixes it is a Wright-Fisher import. It is the classical solution's own boundary-flux bookkeeping (P4), and P_fix = 1/M holds in Moran and beta-binomial chains too (P6b) | T3, T4, T5; P4, P5, P6b |
| **R-B** as R-A, but "the mathematics" = the neutral diffusion model with its boundary behaviour (the post's own B6: "The diffusion cannot produce it") | `misread`: Chalub counts the laws as part of "the correct solution of the continuous models" (C4) and derives b(∞) = ∫x p^I (P3: 4/9 for the Beta(4,5) start) | `holds` | `contradicted` (P4 hit and P6b hit) | C4; P3, P4, P6b |
| **R-C** "the 1/(2N)" = the initial frequency of one copy among 2N | `misread` (Chalub has no N and no initial frequency 1/(2N): T5) | `holds` | `contradicted` (P6b hit: a count of copies, not a model assumption) | T5; P6b |

Proposed fields under RD (proposals; integration decides): R-A → fidelity `partial`, internal `holds`, external `contested`. These are **B1e's current values: Q1 moves no field value.** It adds QB's Readings table, a `reading-dependent:` comment naming R-A / R-B / R-C, and a quote id (Q296 is the next free id; no id above Q295 exists in `quotes-*.md` today). As registered, not tested: whether real neutral alleles have E[Δp] = 0. That is the definition of neutrality; B3c's "successfully disputed" premise is scored at B3/B7 (rule N1).

**What R-A costs Day (critic side).** R-A is narrower than the post's own context. Earlier in the same post Day calls the second constraint "not a fact about diffusion" (B3c), and later it says "The diffusion cannot produce it" (B6). Both are R-B, and under R-B the fidelity is `misread` and the external value `contradicted`. R-A is the governing reading because rule RD takes the most defensible reading of the quoted statement, not because the author meant it.

**What R-A leaves Day (Day side).** Under R-A the core of QB is true: the PDE in the interior does not determine the split (P5: three splits, each conserving probability, give three different limits θ = 0, 0.5, 1), Chalub does add the laws to (7) before solving (C2, C4; his (8)-(9) precede the solution), and Day's paraphrase B3e "he says plainly that the constraints are inherited from the discrete process" is a fair rendering of C1.

## Q2: is Chalub's expansion the Kimura (1955) series?
Registered mapping and result: **P7 X + P8 U.** The docstring's verdict line for P7 X reads: "B2f's credit does not reach Chalub's expansion; propose fidelity of the Chalub link `misread` (Reading A) and flag to the lead." **That is the proposal the registration licenses, and it is stated here as such.** It is flagged to the lead below.

The write-up's own position, for the reviews to rule on: the post hoc diagnosis shows the X result comes from the audit's script, not from the mathematics. Applying the X move would score Day `misread` for a bug of ours. Had P7 landed in E, the registered line "P7 E + P8 U" would apply. Under it, Chalub's b(t) is the series B2f resummed, so B2f's route credit reaches "Chalub's ... series" as Q286 and Q288 describe it. Whether that series is Kimura's (1955) stays `unverifiable` from primary text, and no field value moves. A post hoc result cannot by itself replace a registered call (AGENTS rule 5). The choice between (a) applying the registered X move, (b) a ruling that the registered value item was mis-specified (and on what basis), or (c) a re-registration of P7 alone, is the lead's under D-24, not mine.

The "old" half is `unverifiable` on every option: P8 is U. Context only (registered as not setting a band): Chalub writes that the neutral solution "is known to be written in terms of Gegenbauer polynomials, cf. [2, 3, 4, 5, 6]" (C6), cites Kimura's 1955 paper (C10), and says "The main difference between this and previous works on the same subject is that the conservation laws are taken into consideration" (C7). Day's own post calls the classical solution "the one Kimura wrote down in 1955" (B2). Both authors describe the transient as the classical one. The brief rules descriptions out as evidence, so this is recorded, not scored.

Q288 read against the mathematics (descriptive, from P3 and P7's held items): "derives the explicit transient solution as a Gegenbauer polynomial expansion whose terms converge to the steady-state fixation probability u(p) = p only as t → ∞". Chalub's b(t) is such an expansion, its limit is x0 (P3: b(∞) = ∫x p^I), and its approach is e^{−2t} (P7 large-t). That part of Q288 is accurate to Chalub.

## Escalation and tier
- **Escalation clause (brief): did not fire on its listed conditions.** No proposed move touches B1, B1a, B2 or B; Reading B of B2f is not adopted; nothing here shows Day deriving a number from F(T). The registered X line itself says "flag to the lead", so this is flagged.
- **Tier: flagged.** D-23 gives three reviews to a check "whose registration carries a verdict-field flip". The registered X line carries one (B1e fidelity `partial` → `misread`). If the lead keeps the X move live, my reading is that D-23 asks for three reviews (correctness, steelman-day, steelman-critic), not the combined one. If the lead rules the move off, nothing in Q1 or Q2 moves a field and the combined review the brief set suffices. The lead decides.

## Who this helps
- **Day side:**
  - The interior PDE does not fix the fixation/loss split (P5; DQ1a hit).
  - The laws are added to (7) "from outside" in Chalub's own framing ("had to be introduced into the model", C2), and Chalub says they come from the discrete process (C1; DQ1c hit; B3e is a fair paraphrase).
  - The classical solution alone decays and "cannot be the correct solution from the modeling point of view" (C5), as Day's post says (B2).
  - Q288's description of Chalub's expansion is accurate (P3, P7 large-t).
  - On the mathematics, Chalub's b(t) and the series B2f credited Day for resumming agree once the audit's own rounding bug is removed (post hoc). Read that way, the route credit B2f gave Day reaches the 2022 paper's series as Day describes it.
  - QB's internal value is `holds` under every reading.
- **Critic side:**
  - "1/(2N)" is nowhere in Chalub (T5). Chalub calls the laws derived, never assumed (T4), and names Moran as well as Wright-Fisher (C3; KQ1a hit).
  - Constraint 2 is the classical solution's own outward flux at x = 1, to 5e-64 in 20 of 20 cells (P4, the severe item; KQ1b hit): "probability that leaves at x = 1 stays there", not a Wright-Fisher premise.
  - P_fix·M = 1 to 12 printed digits in Wright-Fisher, Moran and a beta-binomial Cannings chain with N_e halved (P6b; KQ1b hit). DQ1b's two failure routes (P4 miss, P6b miss) both failed to occur.
  - The exact chains match Chalub's b(t) within 0.92% (WF), 0.30% (Moran) and 0.90% (BB) at τ ≥ 1 (P6c).
  - Under the post's own context (R-B, B3c, B6) QB is `misread` and `contradicted`.
- **Both / the audit's own errors:**
  - **P7's value item was mis-specified by the audit:** float x on one side, exact decimal on the other. That produced the registered MISS / band X and a licensed move against Day (`misread`) that the mathematics does not support (post hoc H1, H2). It is the audit's bug and is credited to neither side.
  - The audit's files label B2f's series "Kimura (1955)" (`b2_posthoc.py` l.3, 53) without the primary text held. P8 = U shows that label is unverified from primary text.
  - P1s (HIT): Chalub's Appendix sentence C12 ("For α < 3/2, the right hand side of Eqs. (3)–(6) are identically zero") is false as written. Section 3 uses α = 3/2 only, so it is immaterial (R1); it is a slip in the cited source, scored for neither side.
  - The claim file's locator "¶5 of extracted text" is paragraph 4 of the post body by this script's extraction (line 7 of the held `.txt`): a locator to reconcile at integration.
  - Label criterion-only: every Q1 hit was predicted with both texts in hand and with hand algebra done, so the hits show correct arithmetic and a second route agreeing, not a risky test passed. P4 and P6b could still have failed.

## Quotes for integration (verbatim; quotes files not edited here)
- QB (proposed Q296): "Chalub shows that the 1/(2N) is an assumption imported from the Wright-Fisher model. It is not a result produced by the mathematics." voxday.net/2026/08/23/chalub-and-the-kimura-cancellation/, published 2026-08-23T09:37:10Z (modified 13:16:18Z), post body paragraph 4 (script extraction).
- Context, same post (proposed ids at the operator's discretion): B3c "The second is that the average allele frequency never changes, which is not a fact about diffusion but an inherited assumption from the Wright-Fisher model, the very assumption that has been successfully disputed by me and three scientists before me."; B3e "he says plainly that the constraints are inherited from the discrete process."; B6 "The initial-frequency theorem is not a theorem of the diffusion. The diffusion cannot produce it."
- Chalub 2022 (arXiv:2208.00148v1, 30 Jul 2022): C1 "two conservation laws derived directly from the discrete process" (§2, before Eq. (9)); C2 "However, to obtain the correct solution, two additional conservation laws had to be introduced into the model." (§1); C3 "limit of the Moran and the Wright-Fisher processes" (§1); C4 "correct solution of the continuous models, in the sense of being a continuous approximation of the discrete process, is a measure that not only satisfy the Kimura equation (7) but also the two conservation laws given by Eqs. (9)." (§1); C7 "The main difference between this and previous works on the same subject is that the conservation laws are taken into consideration." (§1).

## Limits
- Q2's "old" half needs Kimura (1955) itself; it is not obtainable within the rules (HOWTO-refresh). An owner-supplied copy would let P8 be decided as registered (S or D).
- P4 and P5 test Chalub's neutral case (ψ = 0) only, at the registered starts and times.
- P6 uses M = 200 copies and three exchangeable neutral chains. A neutral, non-exchangeable chain with E[Δp] = 0 but P_fix ≠ p0 (the claim file's stated Day-favourable result) was not constructed. For a bounded martingale it cannot exist (optional stopping), which is why P6b is non-severe, as registered.

## Open
1. **Lead ruling on P7** (D-24): apply the registered X move (B1e fidelity `misread`, flagged), rule the value item mis-specified, or re-register P7 alone with exact-decimal x. The ruling also settles the tier question under D-23.
2. Q296 for QB and ids for B3c, B3e, B6 if the operator files them.
3. Reconcile QB's locator (¶4 of the post body vs "¶5 of extracted text").
4. Kimura (1955) primary text: an owner decision whether to supply a copy (outside input).

## Things that looked wrong (for the reviews to rule on)
- The P7 value item compares at mismatched arguments. Diagnosed above; the registered call is reported unchanged.
- P6c's relative gaps at τ = 0.25 (8-16%) are large. They sit only under the absolute band (≤ 0.02, met at 0.00022-0.00042). Whether τ < 1 should have had a relative band is a design question.
- P1s is registered as a HIT "for neither side". It confirms a slip in Chalub, a cited source and not a party, so it changes no verdict.
- `record()` prints P6a-c with empty detail dicts (`{}`). Their figures appear only in the per-chain lines above them, so a reader of the summary alone cannot see the numbers.
- QB's fidelity under R-A rests partly on absence counts (T4, T5) in a `pdftotext` extraction. A ligature or line-break artefact could hide a match. "Wright-Fisher" ×2 and "assum" ×1 were checked by context strings, but the absences were not checked against the PDF by eye.
