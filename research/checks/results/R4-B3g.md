# R4 B3g: what Day's 2026-08-27 concession removes, and what it leaves

**Status: written up; awaiting one combined review (low-stakes tier: bookkeeping).** Not integrated. Everything scored here is dialectic (rule RH); no rhetoric is scored.

## Files
- Script `research/checks/b3g_concession_bookkeeping.py`, pre-registered at **ef6e8aa** (predictions P1-P6 in the docstring) and not edited after the run. It ran locally on 2026-10-10 (string matching and arithmetic, < 1 s, one process). Output: `results/raw/b3g.out`.
- Target claims: B3g (concession), B3 (k/mu family), B3a, B3f, B4; the versions ledger row "N vs N_e in k".

## Results against predictions
| Pred. | Prediction | Result | Score |
|---|---|---|---|
| P1 | All 11 quotes found in the local raw text | 10 exact, 1 after NFKC/whitespace normalisation (E4, Z23188201); sha256 prefixes in `raw/b3g.out` | **holds** |
| P2 | 2N mu x 1/(2N) = mu for every N; the withdrawn form gives (N/N_e) mu | True; (N/N_e) form gives 30.3 at N = 1e5, N_e = 3,300 and 8e5 at 8e9 / 1e4 | **holds** |
| P3 | The N/N_e family reproduces as plain N/N_e within 1%; B4's 200-580 kya reproduces within 5% | 30.3, 15.15, 9.09, 30.3, 800,000 all within 1%; B4 corners 198 and 576 kya. Under the concession each k/mu becomes 1 (a change of 9.1x to 800,000x) and B4's divergence returns to t_clock = 6-7 My (12-30x) | **holds** |
| P4 | 0.743 and 32.3 are not N/N_e ratios; the concession does not remove them | 0.743 is a census-history Balloux-Lehmann ratio (k < mu, wrong sign for N/N_e >= 1); 32.3 is a rate comparison with no derivation. Classification from the stated bases, not computed | **holds (classification only)** |
| P5 | 740,000 and 330,000 reproduce; implied census supply about 3.4e9 genomes per generation | 7.44e5 (within 1%); 3.38e5 (within 3%); implied 3.36e9 | **holds**; the 2.5e11 input itself is uncited (rule F: unverifiable, not re-sourced) |
| P6 | Q105's 1/(2N_e) (2026-09-15) vs E4's 1/(2N) (2026-10-06) | Equal only if N = N_e; Q105 draws no k/mu number | **versions ledger, not scored** (R1) |

## What the concession removes (R1 bookkeeping)
- **Removed, error-level by R1:** every value that is an N/N_e ratio: 19-46 (mammals, Z18429937), 15.2-30.3 (human) and 9.1-30.3 (chimp) (Z18525547), 800,000 (B3f, secondhand Grok text posted by Day), and the downstream B4 clock (200-580 kya returns to 6-7 My). Each moves by far more than 25%. Rule SC does not rescue them: the correction is in a later, different source, and the Zenodo records are unrevised (versions ledger).
- **Not removed:** 0.743 (B3c; its own status stands: window-dependent) and 32.3 (B3d; underived). The concession does not touch k = mu at steady state, the transit-time / fill-state argument (B1, B2), or the qualitative Balloux-Lehmann effect (B3b).
- Day's census-supply arithmetic in the same post is correct, and his remark that it "does not touch his repaired algebra" is consistent with the identity: k = mu does not depend on N. The 330,000x is a supply ratio. It bears on in-transit counts, not on k.

## Who this helps
- **Day side:** the concession is accurate, and P2 confirms it. His census arithmetic reproduces. The concession is narrower than "k != mu is withdrawn". The values that rest on other mechanisms (0.743, 32.3) are not removed by it, and B1/B2 are untouched. The covariance objection was already in the 08-27 post (para 3), so the concession was never unqualified. Credit: an author correcting his own load-bearing formula in public within a day of the critique.
- **Critic side (keruru, McCarthy):** the concession removes, by its author's own algebra, every N/N_e value in the family and the 200-580 kya recalibration (B4), a 12-30x change. The unrevised Zenodo records still carry them. Q105 restates 1/(2N_e) nineteen days later.
- **Both:** neither side's numbers are disputed here. What remains open is whether genotype-fecundity covariance, which is Day's later objection (09-21), bears on *neutral* P(fix). No model in the corpus tests it.

## Limits
- P4 is a classification from stated bases, not a derivation. If a later Day text derives 32.3 from an N/N_e ratio, P4 would fail and the concession's reach would widen.
- The quote check confirms the strings in the local raw copies. It does not confirm that the live pages are unchanged since they were fetched.
- No B3g verdict moves. B3g stays holds / accurate / supported. The result is the list of B3-family values that the concession removes, for integration into B3, B3a, B3f, B4 and `ledgers/versions.md`.
