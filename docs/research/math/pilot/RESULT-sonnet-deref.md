# Pilot result: Sonnet 5.5 de-referencing (scored 2026-10-31 against PREREG-sonnet-deref.md)

Both agents ran as `operator` on Sonnet with the `deref-source` skill, in parallel. Neither saw the answer key. Outputs are in `V/` and `A/`.

## Test V: video window 00:31:24-00:59:35
| Criterion | Registered pass | Result |
|---|---|---|
| Recall K1-K8 | 6 or more of 8 | **8 of 8.** K1 M-005 (A4, A4e, A4f); K2 flagged (0.8 vs d = 0.45); K3 M-002/M-003 linked to **B5c** (Hancock's 76.8 claim, a better node than the key's A3); K4 flagged "may be circular"; K5 M-006 linked to **G1, G2** (the exact rate-vs-serial nodes; better than the key's A/F1a); K6 M-008 (F1c); K7 M-010 (A2e, B6c, G2c); K8 the Lynch relay is in the source map (no separate object) |
| Quote fidelity | 100% | **37 of 37** quote rows match the transcript verbatim (lead's own normalised grep) |
| Arithmetic | 169,344 and 201,600 reproduced | Both reproduced. **One false flag:** the agent says that with 38.4, 169,344 becomes 84,672. That drops the factor of 2 for two lineages (2 x 38.4 = 76.8), so Duffy's arithmetic is consistent and the flag is wrong |
| Balance | both positions; valid points on both sides | Both positions filled for all 13 objects. Duffy's valid points (SNV vs SV, LTEE clonal) and Erica's concessions are recorded |
| Precision | count spurious | 0 spurious. Two extra objects are good finds the key missed: M-014 ("D has nothing to do with MITTENS", yet d enters F_max) and the MITTENS-uses-no-mu claim against kappa |
| Cost | report | 76k tokens, 12 tool calls, 2.2 min |

**Verdict: pass (strong), with one arithmetic false positive.**

## Test A: backfill of 43 branch A claim files
| Criterion | Registered pass | Result |
|---|---|---|
| Lint | 0 errors | **Pass** |
| Dedup ratio (objects / claims) | under 0.7 | **0.98 (42 / 43): fail.** Objects do link several nodes (41 of 42 are shared), but the agent made about one object per claim instead of merging |
| Seeded sample of 8 (seed 20261031: M-020, M-016, M-025, M-005, M-033, M-003, M-014, M-041) | 7 or more of 8 | **7 of 8.** Statements and resolved_by files check out against the claim files (906 in A2c, 94,000 x 11.7 in A5b, 327 Mb in A3x1, R4 paths exist). M-025 (d) is marked `resolved` by R4-H-C2 while the d-vs-N_e dispute (A4e/A4f) is live; test V's M-005 has it open. Minor: M-020 lists A3z, which does not carry the 327 figure; M-025 omits A4a |
| Resolved status | named file | Done for 21 objects; all files exist |
| Statement-level deref | (skill steps 1-2) | **Not done.** The steps column is generic and there are no Q ids. The agent read excerpts, not whole files, despite the brief |
| Cost | report | 95k tokens, 11 tool calls, 2.5 min |

**Verdict: mechanics and correctness pass; dedup and step depth fail.**

## What this decides (per the registration)
Sonnet is good at **de-referencing a source** (statements, steps, objects, links, arithmetic) and weaker at **merging across many files**. For the backfill:
1. Sonnet does the per-source / per-branch deref with `deref-source`.
2. One merge pass per branch (Opus, or Sonnet with an explicit merge checklist) collapses objects and reconciles conflicting `status` between maps (here: M-025 vs V/M-005).
3. The skill gains: a definition of `resolved` (the maths question is settled by a named result; the claim's verdict may still be contested for other reasons); "recompute with every factor the speaker uses, and state the formula before flagging"; and "Q ids required on every statement row".
4. Opus spot check: a seeded sample of 8 per branch.

Projected cost of the full backfill: about 234/43 x 95k = about 0.5M Sonnet tokens, plus merge passes.
