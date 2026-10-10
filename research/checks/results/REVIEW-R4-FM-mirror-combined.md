# Review of R4-FM fix pass, post hoc follow-ups and mirror test (combined re-review)

Date 2026-10-10. Reviewer: one Opus agent covering correctness, the Day-side steelman and the critic-side steelman. This is a same-agent review, so the independence caveat applies. Scope: only material that is new since the three reviews at 1796620. That means `R4-FM.md` §"Review resolution", §"Post hoc follow-ups" and §"Mirror test", plus the parts of §Reading, §Who this helps and the headline tables that those sections changed.

Reviewed:
- `research/checks/fm_mirror.py` at 737648e (docstring M1-M6, S1, S2, E1, E2, C3, K3, K4, C11) and at HEAD;
- `raw/fm_extra.out` (all lines), `raw/fm_mirror.out` (all lines), `raw/fm_extra.json` (C3 and E1 blocks, read with a one-line local script, < 1 s), `raw/fm_mirror.host`, `raw/fm_mirror_maf.md5`;
- `R4-FM.md` at 5f05791;
- the three FM reviews (MAJOR rows);
- `quotes-day.md` line 1237 (the "sharp boundaries" quote).

Nothing was rerun. The npz files stay on workhorse.

Rules applied: R4-X1 (R1 materiality, S, F, N, C). Severity labels are the same as in the FM reviews (MAJOR, MINOR, NOTE).

## 1. Correctness

### Provenance (passes)
- **Order of events.** Pre-registration 737648e was committed at 16:25:31. The launch was at 16:25:40 (`fm_mirror.host`), and the MAF md5 file was written at 16:26:51, so the input was complete only after the commit. Stage B outputs are dated 16:27:58 and stage A outputs 16:53:53. The write-ups are 6e28c09 (16:32:32) and 5f05791 (16:55:46).
- **Script integrity.** The md5 of `fm_mirror.py` is `88be5400…f1d` at 737648e, at HEAD and in the host record. `fm_mesa_replication.py` is unchanged (`53f99853…4693`). The chimp MAF md5 matches the published value.
- **Disclosure.** The docstring discloses two things before the run: the synthetic smoke test behind the E1 S_null bias, and the observed E2 counts that R4-FM already knew. No threshold differs between the docstring and the scoring.
- **Numbers match the raw output to the stated rounding.** Checked by hand:
  - S1: 60.4%, 44.6%, 5.8% of windows, 25.6% vs 3.8% (6.7x), R 1.517 (9.29 / 6.12), 70.5%, 1.32, F1 control 1.10 / −4.8%.
  - S2: 3.84; 57.3 Mb r_H 131.9, r_C −23.9, repeat 0.98; 131.9² − 23.9² = 16,826 = 95% of Δ 17,698.
  - E1: all S values, 1,362 edges.
  - E2: 35 / 27.1, 70 / 24.05, 2 / 1.0.
  - C3: 0.94-1.10 at 10 kb; 0.94-1.13 at 100 kb.
  - K3 and K4: 36-42%, 39-44%, top 10% holds 13-20%.
  - M1: 15.54 / 62.84 = 0.247 and 35.75 / 188.74 = 0.189; CV² ratio 0.31.
  - M2: 1.155. M3: 16.38 / 4.84 = 3.385; 10 kb 1.506; 1 Mb 1.244.
  - M4: 0.4789 / 0.4794. M5 P3: 2.69 ≤ 0.3 × 13.79 = 4.14, R 1.10. P4: 1.85.
  - chrX F0 on the chimp reference: 0.37. chrX F2: 1.07. M6 values match.
- **Scoring follows the 737648e mappings.** S1 is scored "critic miss by 0.017", which is honest and not rounded into a hit. E1 headline cells are "neither". C3 is an audit miss at 10 kb. K3 is a half miss. M5 P5 is "neither". Every registered Day hit (S2, E2, M3) is reported as a hit.
- **The 1.15 figure.** It comes from (18.16 × 1328 − 17,397) / 1327 = 5.07 and (4.837 × 1328 − 571) / 1327 = 4.41. This is reproducible, but approximate: the null is not refitted after the window is dropped. It is labelled correctly as "post hoc arithmetic, not a registered cell" (see C-2).

### Findings
| # | Sev. | Locator | What is wrong | Fix needed |
|---|---|---|---|---|
| C-1 | MINOR | §Stage B reading "no cell shows human-mesa edges sharper than chimp-mesa edges (S_H/S_C 0.35-1.10)"; §Reading FM4 "never sharper for H than for C" | F2 100 kb (a headline cell) has S_H 0.22 vs S_C −0.05, ratio −3.95. Numerically, H is sharper there. The range 0.35-1.10 leaves this cell out. With only 16 edges it means nothing, but the sentence as written is false. | Say "in the three cells with ≥ 50 edges"; report F2 100 kb as uninformative (16 edges, S near 0 for H, C and the null). |
| C-2 | MINOR | §S2 score cell; §Reading of stage B "chrX F1"; §Who this helps (Day) (b); §Verdict consequence | **Dropping the 57.3 Mb window was not pre-registered.** S2 registered only the removal of windows with SD coverage ≥ 10%. The table labels the 1.15 correctly, but the Reading, Who this helps and the Verdict consequence then use it to call the cell "one region, not a chromosome-wide excess" without repeating the label. The leave-one-out was also applied only to the Day-favourable cell. No critic-favourable cell (for example the chimp-reference M1 excess) was checked for single-window dominance. | Repeat "post hoc, not registered" wherever 1.15 or "one window" is used. Either run the same leave-top-window step on every R cell in the mirror and S1 tables (cheap, post hoc), or state that it was applied to one cell only. |
| C-3 | MINOR | §Mirror reading "Not tested here: … whether the same region drives the chimp-referenced ratio" | This is untested but easy to bound. On the chimp reference, Σr_H² ≈ 16.38 × 1324 ≈ 21,700. If the orthologous window carries r_H ≈ 130 there too, R without it is ≈ (21,700 − 16,900) / 1323 / 4.8 ≈ 0.75. So M3's Day hit very likely rests on the same single window. | Run the S2 top-20 listing on `fm_mirror_bins.npz` (workhorse, post hoc) before integration, or state the bound. |
| C-4 | MINOR | §S2; correctness C2 fix text (asked for overlap with the XTR and ampliconic annotations) | S2 reports SD coverage and repeat share only. The window's content is still unknown. Pointer, from memory and **not verified**: the CHM13 chrX centromeric array begins near 57.8 Mb, so a 98%-repeat window at 57.3 Mb may be pericentromeric satellite. That is a classic region for alignment and assembly differences. | Intersect the window with the CHM13 cenSat, XTR and ampliconic annotations, fetched as data. One grep, no run. |
| C-5 | MINOR | `fm_mirror.py` `sd_cov` / S1 (`sdw` = SD bases over W × 1000) | SD coverage is measured on all bases of the window, not on its core columns. A window that is half core can be classed SD ≥ 10% or < 10% by SDs lying entirely in its non-core half. The S1 scores are probably robust (60-70% share; R 1.52 vs 1.5 is the only knife-edge), but the 0.017 miss sits on this definition. | State the definition in the S1 row. No rerun needed unless S1 becomes load-bearing. |
| C-6 | MINOR | §Review resolution D3 row "FM4 now reads 'clustering supported; sharp boundaries untested'" | This is stale. §Reading now proposes "sharp boundaries `contested`" and calls the claim "not supported". | Align the row with whatever FM4 wording survives D-1. |
| C-7 | NOTE | Docstring M1 "[hs1: R = 1.97, 1.82]" vs write-up 1.83 | The raw value is 1.8314, so this is rounding only. | None. |
| C-8 | NOTE | §M6 | No uncertainty is given. A rough Poisson SE on the W→S / S→W ratio over about 18 mesas is about 0.01-0.02, so the +3% for H is about 2 SE. "Small" is the right word. | Optional: give the counts. |
| C-9 | NOTE | §E2 F2 10 kb | The registered Day hit in this cell is 2 observed vs a null whose maximum over 20 reps is 1. It is correct as registered, but it rests on two events. | None. |

## 2. Day-side steelman
| # | Sev. | Locator | Point | Fix needed |
|---|---|---|---|---|
| D-1 | MAJOR | §Stage B reading "Sharp boundaries (E1)"; §Reading FM4 ("'sharp boundaries' `contested` (half-steps at 10 kb … soft at 100 kb)") | **E1 does not measure absolute sharpness, so it cannot support "not step-like", "half-steps" or "soft".** Day's statement (quotes-day l.1237) is descriptive: "contiguous blocks … with sharp boundaries". It does not say the boundaries are sharper on the human lineage than on the chimp lineage. E1's registered criteria are relative (S_H/S_C, shared fraction), and both comparators inherit the real landscape. The 1-kb null takes ρ from the real C+G counts, so any genuine step in the shared landscape is a step in the null too. S_H ≈ S_null ≈ S_C therefore says only that H edges look like the shared landscape's edges. No benchmark says what S a perfect step gives under this estimator. Mesa edges are placed at window granularity, so a true step anywhere inside the boundary window dilutes the 5-kb inside/outside contrast. At 100 kb this dilution is severe (a 5-kb probe at a ±100-kb-uncertain edge), so "soft at 100 kb" is a resolution artefact, not a property of the genome. Rule C (most charitable reading) and R1: the absolute statements drive the proposed verdict word. | Either calibrate S on a synthetic perfect step through the same mesa caller and `edge_stats`, which the pre-run smoke test already almost does (post hoc, cheap, workhorse). Or drop the absolute wording and propose: "sharp boundaries: H edges no sharper than C or the shared landscape (relative reading `contested`/critic-leaning); absolute sharpness **untested** at this resolution (`pending`)". FM4 is not ready until then. |
| D-2 | MAJOR | §Reading FM10 "The autosomal mesa route is `contradicted` on alignable sequence"; §Verdict consequence | **This reopens the original D4 MAJOR.** M1 shows that the *F0 human-heavy excess* follows the reference. It says nothing new about whether drift with variable μ produces the mesas. The shared-rate null is still descriptive, and the residual (φ_res 2.3-2.7 for every lineage, G 4.4) is still unattributed. What the data contradict is a **human-specific** mesa signal on autosomal alignable sequence (P3, P4, P7, M1, M5). That is a premise of the human-lineage reading, not FM10's conclusion "neither selection nor drift". Giving one claim two external words ("contested" overall, "contradicted" for a route) will be integrated inconsistently. | Replace with: "A human-specific autosomal mesa signal is contradicted on alignable sequence; FM10 external `contested`, leaning critic." Keep the D4 sentence. |
| D-3 | MINOR | §Reading of stage B chrX; §Mirror reading | **The 57.3 Mb window is itself Day's best object, not noise to subtract.** It is a 100-kb window with a human-lineage residual of +132 SD while the chimp lineage is below expectation (−24). It survives F1, the SD filter and (very likely, C-3) the change of reference. Calling it "one repeat-dense window" is accurate, but the Day-side description is "a single extreme human-lineage hotspot on chrX of unknown cause". It is not a mesa (lag-1 low; one window), so it does not support FM4 or FM7 as worded. It is the one open cell. | Add this description to Who this helps (Day) beside the 1.15. Integrate it as an open item (C-4 annotation check), not as resolved. |
| D-4 | MINOR | §Reading (no FM7 line); docstring SCORING "E2 decides … FM7's lineage-specific mesas" | **E2 was registered to inform FM7, but the write-up proposes no FM7 change.** The registered E2 result is a Day hit (2 of 4). Both lineages carry lineage-specific mesas beyond a shared-rate null, chimp more. | Add an FM7 line: lineage-specific regional excess exists on both branches, larger on chimp, so it does not discriminate for a human-lineage mechanism. Keep the "Day hit as registered" wording. |
| D-5 | NOTE | §M5 P5 | On the chimp reference the shared-rate null reproduces only 42% of human mesas, which misses the critic bound of 0.5. This is reported correctly. It is the one registered cell that weakens on the mirror. | None. |

## 3. Critic-side steelman
| # | Sev. | Locator | Point | Fix needed |
|---|---|---|---|---|
| K-1 | MINOR | §M1 reading | **The magnitudes give a stronger critic point than the one stated.** If the projection inflation factor is similar on both references, the de-artefacted F0 ratio is about √(R_hs1 × R_chimp): √(1.97 × 0.25) ≈ 0.70 at 100 kb and √(1.83 × 0.19) ≈ 0.59 at 1 Mb. That is no human excess at all, chimp-leaning. The asymmetry (C/H 4-5 on the chimp reference vs H/C ≈ 2 on hs1) may instead reflect more chimp-reference SD or assembly content, which would make the bound less clean. | Add one sentence with the bound and its caveat. Post hoc arithmetic, labelled. |
| K-2 | MINOR | §E2 score; §Who this helps (Day) | **The E2 critic prediction was mis-specified against the critics' own model.** The paired null has no lineage-specific rate variation. The critics' neutral model includes it (gBGC, PRDM9 turnover, assembly differences; see the review K3 and M6). So "observed > null" is expected under both views and does not discriminate. The Reading already says this. The score cell should too, so that "Day hit" is not cited alone. | Add "non-discriminating (null lacks lineage-specific neutral variation)" to the E2 score cell. |
| K-3 | MINOR | §M3; §Verdict consequence "one open cell" | **The chimp-reference crossing holds at one window size and one filter.** M3 gives R 3.39 at 100 kb, but 1.51 at 10 kb and 1.24 at 1 Mb, and chrX F2 is symmetric (1.07). P3 was registered on autosomes. G is also elevated in that cell (chimp reference: φ_res G 10.6 vs C 4.8), which fits an alignment-difficult region better than a human-lineage mechanism. This is suggestive only, and untested. | State "one cell (chrX, F1, 100 kb); not at 10 kb or 1 Mb on the chimp reference" in the Verdict consequence. |
| K-4 | NOTE | §C3 | The calibration uses a landscape smoothed over ±5 windows, so it shows the null procedure is calibrated for smooth shared landscapes. That is sufficient for the original C3 concern (borrowed-ρ noise). The claim "G's excess is a property of the gorilla data" is fair; its cause is untested. | None. |
| K-5 | NOTE | §K4 | The Lorenz bound (half of DHC needs the densest 36-44% of core columns) is the cleanest new support for FM8b. It holds for any mesa rule. | None. |

## 4. Original MAJORs (reviews at 1796620)
| finding | status |
|---|---|
| C1 projection asymmetry | **Resolved.** The mirror was pre-registered with both sides' predictions; M1 is a critic hit (R 0.25 / 0.19); the Day-side point is withdrawn for autosomes. |
| C2 chrX omitted | **Resolved for reporting** (rows, note, Who this helps). The requested XTR/ampliconic overlap was not done (C-4, MINOR). |
| D1 rule S on FM5 | **Resolved.** |
| D2 Day-favourable cells unreported | **Resolved.** Items (a)-(d) were added, and the mirror outcome is stated for each. |
| D3 sharp boundaries untested; chance rate | **Partly resolved.** E1 and E2 ran and were scored as registered, but the FM4 absolute reading is uncalibrated (D-1, MAJOR), and E2 is not mapped to FM7 (D-4). |
| D4 shared-rate null descriptive | **Resolved in the FM10 text, reopened** by "autosomal mesa route `contradicted`" (D-2, MAJOR). It is a one-line fix. |
| K1 rule F on 80x | **Resolved.** |
| K2 "real" not established | **Resolved.** "Real" is withdrawn, and M1 scores the excess as reference-following. |

## Verdict
Process: clean. Pre-registration preceded the inputs and outputs, the md5s match, and the scores follow the registered mappings, including the near misses on both sides.

Counts: 2 MAJOR (D-1, D-2), 11 MINOR, 6 NOTE.

Readiness of the proposed verdicts:

| claim | ready? | condition |
|---|---|---|
| FM3 | ready | none |
| FM5 | ready | none |
| FM8b | ready | none; K4 strengthens it |
| FM10 | ready after the D-2 wording fix | external `contested`, leaning critic; internal stays `pending` until the rule-N grep at integration |
| FM4 | not ready | the clustering part is ready; "sharp boundaries" needs the D-1 calibration or the `pending` wording |

The MINORs can be answered in the same fix pass. The only optional runs are C-2/C-3 (leave-top-window on the mirror npz) and the D-1 step calibration. Both are post hoc and on workhorse.
