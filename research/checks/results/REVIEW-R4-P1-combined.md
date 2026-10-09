# Review of R4 P1 (combined, low-stakes tier: re-confirmation)

Date 2026-10-09. Method: read `R4-P1.md` and the raw output; spot checks re-derived by hand, nothing rerun. Labels: MAJOR (changes a conclusion), MINOR (needs a fix or caveat), NOTE (informational).

## 1. Correctness
Spot checks re-derived from the printed inputs, all agree with the table:
- Q03: 9,000,000 / 20 / 1,600 = 281.25 (printed table 125). Agrees.
- Q14: 205e6 x 1322 / 252,000 = 1,075,437. Agrees.
- Q19: 252,000 / 27,600 = 9.13 (printed 8). Agrees.
- Q30: pi^2 x 1.8e7 / ln 10 = 77.15e6 (printed 78M, +1.1%). Agrees.
- D3: 30 / 0.1 = 300; 2 ln(2e4) = 19.8. Agrees.
- B3 ratio at N = 1e4, s = 0.001 (0.9996) is consistent with the monotone trend 0.978 (N = 50) to 0.9996.
- C2 trend (3.727N at N = 10 rising to 3.9995N at N = 1e4) is monotone and approaches 4N.

Issues:
- **MINOR-1.** Q03 is labelled "discrepancy" while Q19 and Q30 are "slip". The report does not say why Q03 is not a slip. It is the same kind of object (a printed table value that does not follow from the stated inputs). Fix: say it is labelled "discrepancy" only because the source for the 125 is not located; under rule S and R1 it is a ledger entry unless a node holds it.
- **MINOR-2.** Q33 passes only at a 2% tolerance, which was pre-registered but is looser than the other rows. The elephant row is -1.4%. State that this is rounding, not agreement to the digit.
- **MINOR-3.** D1 and D3 use the textbook definition of Haldane's cost because the 1957 primary is not retrieved (the report says so). The "D is not a constant" statement is therefore about the textbook D. Flag it in the node comments instead of treating it as a fact about Haldane's own text.
- **NOTE-1.** "Prediction met 33/33" in block E should be read as a re-confirmation (the report already discloses prior R2 hand work). No novelty is claimed.
- **NOTE-2.** E-B2a proves the transform only. Varadhan is cited, not proved, and the prefactor is open. The report states this correctly.

No MAJOR issues. No failed prediction was hidden or re-scored.

## 2. Day-side steelman
- The report gives Day credit for 30/33 rows, for the empty-start formula as an exact identity, for the -pi^2 N_e/G exponent and for Q45. Fair.
- **MINOR-4.** A3 shows P_fix = 1/M in an exchangeable Dirichlet-multinomial model, which is the critics' reading. Day can answer that his N_e arises from non-exchangeable offspring variance that is heritable or fitness-linked (e.g. strong skew from selection), where P_fix is not 1/M. P1 does not test that case. The A3 line should say "exchangeable" wherever it supports B3a/B7, and not be read as covering all low-N_e mechanisms. (Day's own 2026-08-27 position, B3g, concedes the point, so this is a limit on scope, not a rescue.)
- **NOTE-3.** The "4N_e generations" check (Q45) is exact for a neutral allele only. It does not support the selected-allele timescale (2/s) ln(2N), which B0 and D1 address separately.
- **NOTE-4.** The report's wording that the identities "settle" the B1 / B1c formulas as mathematics is fair to Day: his formula is exact for its boundary case. The dispute stays external, as the report says.

## 3. Critic-side steelman
- The report credits the critics for k = mu, P_fix = 1/(2N), the stationary start, Q03, Q19 and D not being a constant. Fair.
- **MINOR-5.** The line "Day's Q03 (125) and Q19 do not reconcile with his own inputs" is placed in the critics' column. Under rule R1 these are slips (Q19 -12%; Q03 -56% but in a table that no scored node's conclusion depends on, to be confirmed in the Q03 node). The report should not suggest they are errors that move his case. Add "not scored here; see slips ledger".
- **NOTE-5.** A critic might claim P1 shows the 1,075,000x figure is "correct" only because inputs were fixed; Q14 checks the arithmetic, not the 252,000 or 1,322 inputs. The report's own caveat (Q118) applies equally here and should be repeated for Q14, Q17.
- **NOTE-6.** The 30/33 headline is easily quoted out of context by either side. Both sides' use of it should note it covers arithmetic only.

## Verdict on P1
Sound as a machine re-confirmation. Fix pass: MINOR-1 to MINOR-5 are wording fixes in `R4-P1.md` (no new run needed). NOTE-5 and NOTE-6 added as caveats.
