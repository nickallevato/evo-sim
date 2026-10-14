# Review R4 B1e-Q2: correctness

Reviewer: fresh reviewer instance (Paperclip EVO-10), no part in the design, run or write-up. Reviewed: `R4-B1e-Q2.md` at **e2bc2f1**; script `b1e_q2_chalub_link.py` at 68fcefb; post hoc `b1e_q2_posthoc_p7.py` at 56c6847; raw `b1e_q2.out`, `.json`, `.host`, `b1e_q2_posthoc_p7.out`, `.host`. Brief: the EVO-10 task text (one combined review; one agent must not write both steelmen; run correctness first). The lead's suspicions were not given to me. Date 2026-10-14.

**File form.** The brief set one combined file. Finding C1 shows that D-23 asks for three reviews here, and the task forbids one agent writing both steelmen. So the three reviews are three files: this one, `REVIEW-R4-B1e-Q2-steelman-day.md` and `REVIEW-R4-B1e-Q2-steelman-critic.md`, each by a separate instance. Together they hold what the combined file would have held.

## Run integrity (verified)
- Registration 68fcefb, committed 2026-10-13T21:41:53Z, first in `origin/research` at the push of 21:41:54Z (local reflog). Main run 2026-10-14T00:18:19Z. Order holds.
- md5 now: script `196b3c78...` = host record; `b1e_q2.out` `9e78f0ec...`, `b1e_q2.json` `3cb2ca1e...` = host record. Host HEAD 89fd785 contains 68fcefb. The script was not edited after registration (`git log` shows one commit).
- Workstation run: 15.5 s, 104 MB, one process. This is inside the AGENTS.md trivial-check allowance, and the docstring planned it there.
- Post hoc: 56c6847 committed 00:19:30Z. It ran at 00:19:40Z (host record), so it was committed before it ran. It was pushed only together with its output (d711d17, push 00:19:51Z). Rule 5 needs the commit order only (NOTE C9).
- Source hashes (recomputed by me): `chalub2022v1.pdf` a720d24b..., `.txt` c7225292..., blog be40cd76... All three match the docstring.

## Numbers (every write-up figure against `b1e_q2.out`)
All match. Checked: P1 to P5 details. P4: the worst cell is 4.98e-64 at (x0 = 0.001, t = 0.05), and "12 of 20 cells print 0.0 in at least one column" is right (I counted 1 + 1 + 3 + 4 + 3). P5: three d/dt ∫xp values and three b/m ratios. P6a/b: per-chain figures. P6c: max abs WF 0.00558 (τ 1), Moran 0.00229 (τ 0.5), BB 0.00548 (τ 1); max rel at τ ≥ 1 0.918%, 0.303%, 0.901%; τ = 0.25 rel 15.9%, 8.3%, 13.1%; abs 0.00022 to 0.00042; F_chain/F_C at τ = 1; BB N_e 50.25. P7: six value pairs, six rel figures, 18 finite-x0 figures, large-t 3.43e-9, coef_err 0.0. P8. Summary 10 of 11. Post hoc table: all 18 figures and H1, H2. Wrong numbers: **none**.

**Recomputed independently (post hoc, reviewer; one local mpmath process, under a second, dps 170).** I used my own sum of 1 + Σ_{i≥1} (−1)^i (2i+1) e^{−i(i+1)x/4} and Chalub's x0 → 0 limit with the closed form C_n^{3/2}(−1) = (−1)^n (n+1)(n+2)/2 (not the script's recurrence). With matched exact-decimal x, the relative difference is **0.0 at all six x**. With x passed as a binary float on Chalub's side only, it is **1.09e-14, 0, 0, 0, 5.45e-18, 3.59e-21**. These are the registered figures to every printed digit. The float offsets are 2.78e-18 (0.05), 3.55e-17 (5.04) and −7.11e-16 (25.2). I also checked C_n^{3/2}(1) = (n+1)(n+2)/2 for n < 30 (mpmath `gegenbauer`): it holds exactly.

## Findings

### C1. MAJOR: the tier is three reviews under D-23, not one combined review
- **Evidence.** D-23 (DECISIONS.md l.39, owner answer 2026-10-13 21:22 UTC) says: "a check whose registration carries a verdict-field flip ... gets three reviews". The registration's P7 X line carries one: "propose fidelity of the Chalub link `misread`" (docstring l.230-231). That would flip B1e fidelity from `partial` to `misread`. The registration was committed at 21:41:53Z, 20 minutes after D-23, but its first lines still set "one combined review". The write-up (l.102) reads D-23 as conditional on the lead keeping the X move live. D-23's wording looks at the registration, not at the outcome or a later ruling. This repeats MA-23 (L5).
- **Fix.** Three reviews (done here as three files by separate instances). In the write-up's "Escalation and tier", say that D-23 applies because of the registration as committed. Make it a design-check item that a registered flip line sets the tier at registration time.

### C2. MAJOR: the registered P7 MISS is reported correctly, but band X's inference ("they differ") is contradicted by the run's own registered items; the X move against Day is not supported
- **Evidence.** The write-up reports the call exactly as registered (MISS, band X) and does not change it. That is correct. Band X's verdict line rests on the inference "Band X: any item outside -> they differ" (docstring l.171-172). The registered output already refutes that inference, without the post hoc script:
  (i) coef_err printed **0.0** over n = 0..200. Chalub's limit has coefficients −(−1)^n(2n+3). With i = n + 1, B2f's `F_dec` (b2f_finite_time_formula.py l.199-208) is the same expression term by term. Given the coefficient item, the value item can differ only through numerics.
  (ii) The three x that are exact in binary (0.25, 1, 4) agree to ≤ 1.12e-138.
  (iii) The cause is in the code: `t = mp.mpf(x) / 4` takes a Python float (l.704), while `F_dec(str(x))` takes the exact decimal (l.708).
  My independent recomputation (above) reproduces the three failing figures exactly from that mismatch alone, and gives 0.0 with matched arguments. The post hoc diagnosis is right, and its H1 and H2 were stated in a docstring that was committed before the script ran.
- **Consequence.** Applying the registered X move would score Day `misread` for the audit's own argument mismatch. The registration does license it as written, so this is a lead ruling under D-24, not a write-up error.
- **Recommended ruling (for the lead).** Option (b): the value item was mis-specified. The basis is the *registered* evidence (i) and (ii), and the post hoc result confirms it. Under (b) no field value moves. The E-line sentence ("Chalub's b(t) is the series B2f resummed ...") may replace B1e's "unchecked" caveat, labelled "post hoc: registered value item mis-specified (R4-B1e-Q2, REVIEW C2)". The MISS stays in every tally as a miss of the audit's script. Option (c) would add little: the post hoc script already pre-stated H1 at the registered 1e-30 band, before it ran. If the lead prefers (c), its re-run is a one-line change. Option (a) is not supported by the evidence.

### C3. MAJOR: P4 and the P7 value item could fail only through a bug, so the Day-side Q1 and Q2 bands were unreachable on the mathematics; the write-up calls P4 "the severe item"
- **Evidence.** With J = ∂x[x(1−x) r] and modes C_n^{3/2}(2x−1), ∂x[x(1−x)C_n(2x−1)] at x = 1 is −C_n^{3/2}(1) = −(n+1)(n+2)/2 = −λ_n/2. So −J(1) = (1/2) Σ d_n λ_n e^{−λ_n t}, which is b′ term by term from b = x0 − (1/2) Σ d_n e^{−λ_n t}. The same holds at x = 0 with C_n(−1). So P4 is an exact identity (checked above for n < 30). The registration says P4 was "derived by hand" (l.8-10). It also calls P4 "the severe item" (l.184) and makes "P4 miss" Day's Q1 band (l.181). The write-up repeats this: "the severe item" (l.35), "P4 and P6b could still have failed" (l.123), "DQ1b's two failure routes (P4 miss, P6b miss) both failed to occur" (l.115). P6b was registered as non-severe (optional stopping). The P7 value item, as C2 shows, is entailed by the coefficient item. So all three items through which Day's side could have gained a band could fail only through a defect in the audit's code. This repeats MA-24 / ST-05.
- **Not affected.** The truth of the critic-side Q1 statements. P4 and P6b are true mathematics: they are derivations checked numerically, not predictions that survived a risk.
- **Fix.** Relabel P4 "identity (hand-derived; numerical check of algebra)" wherever it says "severe". In the bullets at l.115 and l.123, say that DQ1b's operationalised routes were reachable only through a bug. Add to "Limits" that the registration turned DQ1b ("not a fact about diffusion") into a flux identity that Day could not win. Whether DQ1b deserved a different operationalisation is for the Day-side steelman. For PREREG-STATUS / severe-testing: Q1 has no Day-reachable band.

### C4. MAJOR: R-A's external rationale scores a meaning that R-A's own gloss reads away
- **Evidence.** R-A glosses "imported from the Wright-Fisher model" as "constraint 2 enters from the discrete process" (docstring l.195-197; write-up l.81). R-A's external `contested` is then justified partly by P6b: "P_fix = 1/M holds in Moran and beta-binomial chains too" (write-up l.81; docstring l.213-215). That argues against Wright-Fisher *specificity*, a meaning R-A has already set aside. Under R-A's gloss, the "false" half has to rest on P4 and C1 alone: given constraint 1, constraint 2 adds only absorbing-boundary bookkeeping, and Chalub calls it "derived", not assumed. Against that stands a reading the table does not record. From the continuum model's standpoint, a law "derived directly from the discrete process" (C1) and "introduced into the model" (C2) is an input to (7), and that is close to what "assumption" means. If that carries, R-A external would be `supported`, a Day-favourable flip of a field-setting value. The write-up applied the registered mapping exactly (P4 hit and P6b hit give `contested`), so this is a registration defect, not a write-up slip.
- **Fix.** (1) State R-A's external rationale only in R-A's own terms. (2) Add the literal reading, R-A0 ("imported from the Wright-Fisher model" = specific to Wright-Fisher), as its own row: fidelity `misread` (C3 names Moran too), external `contradicted` (P6b). (3) Give the steelmen and the lead the question whether R-A external stays `contested` or becomes `supported`. Under C, RD and D-24 that is a ruling on a field-setting value, so a fresh reviewer must check it if it moves.

### C5. MINOR: C12 is in Section 2, not in Chalub's Appendix
- **Evidence.** `chalub2022v1.txt` l.125-126 ("To the best of our knowledge, Eqs. (3)–(6) are new. For α < 3/2, the right hand side of Eqs. (3)–(6) are identically zero.") comes right after Eq. (6) and the footnote, and before Appendix A is reached (l.93: "We will prove at Appendix A"). `grep` finds one occurrence. The write-up (l.121, "Chalub's Appendix sentence C12") and the docstring (l.9 and l.132-133, "a slip in Chalub's Appendix") give the wrong locator. The P1s substance is right: RHS(4) = (1/(α−1))·C(2α+2n−2, 2n+1), which at n = 0 is (2α−2)/(α−1) = 2, and at α = 0.75, n = 1 it is (−0.0625)/(−0.25) = 0.25.
- **Fix.** Change the locator to "§2, after Eq. (6), p. 2" in the write-up and in the slip-ledger entry at integration.

### C6. MINOR: the strongest passage on where the laws come from is not quoted
- **Evidence.** `chalub2022v1.txt` l.46-49: "The finite population Markov processes referred above are associated with a number of conservation laws to be satisfied by their solutions. Most notably, the solution of the Markov process should satisfy the conservation of probability, but, in fact, the number of conservation laws is equal to the number of different alleles modeled by the associated Markov process." Here "referred above" means Moran and Wright-Fisher (l.39). This bears on QB's fidelity under every reading. It supports Day's "inherited from the discrete process" (B3e). It also says the laws belong to both processes (against WF-specificity) and are "to be satisfied by their solutions" (a property of the processes, not a modelling assumption).
- **Fix.** Add it as C13 (§1, ¶4) to "Quotes for integration" and cite it in R-A's fidelity basis.

### C7. NOTE: QB's locator is not shown to be a discrepancy
`blog_paragraphs()` returns body paragraphs, and T1 prints `i + 1` (l.364): a 1-based ¶4 of the post body, line 7 of the held `.txt`. The claim file's "¶5 of extracted text" may count the title or a lead line in a different extraction. Neither is wrong as shown. At integration, record "post body ¶4 (1-based, `blog_paragraphs`), held .txt l.7".

### C8. NOTE: P6a-c record empty detail dicts
I agree with the write-up's own flag (l.145). I checked every figure against the per-chain lines and all agree. Fix in the next script that reuses `record()`.

### C9. NOTE: post hoc push order
56c6847 was committed before its run but was not pushed before it. That is adequate for a post hoc script (rule 5 requires commit order). The H1/H2 text is in the committed docstring.

### C10. NOTE: textual absences re-checked in the extraction
I grepped the held `.txt` for `assum|suppos|hypothes|postul|impos` (one hit, l.234, C9), `Wright|Fisher|Moran` (l.39 and l.359 only) and `popul.*size|effective|absorb|1/N|1/(2` (none), and found no line-end hyphen splits of "assum". T4 and T5 hold in the extraction. I did not check the PDF by eye either, so the write-up's l.146 caveat stands.

## Verdict moves (against the registration)
- Q1: R-A fields `partial` / `holds` / `contested` are exactly what the registered mapping gives for T3-T5 and the P4 and P6b hits. No value moves, and the write-up says so. C4 questions the mapping, not its application.
- Q2: the registration licenses the X move. The write-up states that, flags it and does not apply it, which is correct under the brief. My recommendation is in C2.
- Escalation clause: it did not fire (nothing touches B1, B1a, B2 or B; Reading B of B2f is not adopted; there is no number from F(T)). I agree.

## Counts
BLOCKER 0, MAJOR 4 (C1-C4), MINOR 2 (C5, C6), NOTE 4 (C7-C10). Wrong numbers (old -> right): none. Wrong locator: C12 "Appendix" -> "§2, after Eq. (6)".
