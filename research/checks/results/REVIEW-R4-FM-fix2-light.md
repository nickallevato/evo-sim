# Light review of R4-FM fix pass 2 (`fm_fix2.py`, post hoc)

Date 2026-10-10. Low-stakes bookkeeping review (one pass; Sonnet; same-agent-family, so the independence caveat applies). Scope: pre-registration 6aa9bb6, results e201384, the last two sections of `R4-FM.md`, `raw/fm_fix2_*`, `raw/fm_fix2.host`. Nothing rerun.

## 1. Correctness
- **Order of events (passes).** 6aa9bb6 committed 17:04:53; `fm_fix2.host` records launches at 17:05:00 (calib) and 17:05:25 (lt, mapc, maph); outputs are stamped 17:05:18-17:06:41; results commit e201384 at 17:08:38. The script is added only in 6aa9bb6 and unchanged since; `fm_fix2.host` md5 fd062326... recorded.
- **Numbers vs raw (pass).** Hand-checked against `fm_fix2_calib.out`, `_lt.out`, `_mapc.out`, `_maph.out`: all four T1 rows (S_obs, step_offset, ramp10, ramp40, q 0.756 / 0.631, edge counts 841-886 and 103-124); T2 R before/after for chimp and hs1 chrX F1 100 kb (3.39 to 1.11; 3.76 to 1.16; shares 70% / 72%), autosomes F0 100 kb and 1 Mb (0.25 to 0.26, 0.19 to 0.20; 1.97 to 1.73, 1.83 to 1.58; top-1% 0.56 / 0.30 and 1.38 / 1.37), chrX F0 and 10 kb and 1 Mb cells; T3 windows (67 + 32 kb of 99.5 kb; 65 + 36 kb) and the window 2-5 mapping.
- **Scoring vs docstring (pass).** T1: Day needs q >= 0.75 in both 10-kb cells (F2 0.63 misses), critics need q <= 0.25 in both (both miss), so indeterminate and FM4 "sharp boundaries" `pending` by the registered mapping. T2a-c, T3, T4 scored on the stated bounds.
- **Post hoc labels (pass).** Section header, pre-registration commit message and every use of 1.16 / "one window" carry the label; the disclosed prior knowledge (E1 S values, approximate 1.15, smoke test) is stated.
- **MINOR-1.** The "unresolved" 100-kb T1 cells report q 0.84 (F0) and -3.9 (F2) in the raw output; the write-up omits them correctly but says "unresolved" without noting that q is meaningless there. One clause would do.
- **MINOR-2.** T4 is scored "Day miss" on a no-overlap prediction, but the docstring's own caveat (overlap says what the region is, not the cause) means a Day-side reading (real human-lineage change inside satellite transition) is not excluded; the write-up states this. Keep it prominent in the claim paragraph.
- **NOTE-1.** Docstring typo in the composite-repeats md5 is disclosed; full value matches `fm_fix2.host`.
- **NOTE-2.** `raw/fm_mirror_wrapper.log` is 0 bytes (no text); safe to track.

## 2. Day-side steelman
- The leave-top-window result is symmetric (hs1 autosomal F0 R stays 1.73 / 1.58 without the top window; Day hit) and the 10-kb edges reach about 90% of a perfect step's S; "sharp boundaries" is not refuted. The write-up credits both. The chrX window being pericentromeric satellite transition does not settle that its excess is an artefact.

## 3. Critic-side steelman
- chrX F1's Day cell is one orthologous window in a centromeric transition region and R falls to 1.11-1.16 without it; "soft at 100 kb" is correctly withdrawn as a resolution artefact. The write-up leaves the E1 relative reading (H no sharper than C) intact, which is the critics' point.

## Verdict
0 BLOCKER, 0 MAJOR, 2 MINOR, 2 NOTE. Fix pass 2 is faithful to its pre-registration; proceed to integration. MINORs answered at integration (claim paragraph wording).
