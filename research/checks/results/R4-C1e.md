# R4 C1e: the C1c model on each published Holocene N_e trajectory

**Status: run, written up, reviewed (combined, `REVIEW-R4-C1e-combined.md`), fix pass done.** Everything here is dialectic (rule RH): a model-conditional simulation. Not a measurement of the real past.

## Files
- Script: `research/checks/c1e_holocene_trajectories.py`, pre-registered at **2c245ec** (imports `c1c_call_depth_replacement.py` unchanged). Run on na-workhorse 2026-10-09 17:47 -06:00, `main 3` (3 workers, one replicate each, C1c panels 0-2, 16 scenarios, 2 sampling draws, so 6 draws per cell). md5s in `raw/c1e.host`. Outputs `raw/c1e_rep{0,1,2}.json`, `raw/c1e.out`, `raw/c1e_analysis.txt` (the `analyse` stage, run on workhorse). No post hoc runs.
- Targets: C1c / C4 (Holocene N_e varied), C5b, B2e, and Day's statistic "21" (nodes C, C6).

## Results (S21 = tracked E1-T2 events dated 5000-6000 BP or younger, mean of 6 draws; Day's value 21)
| Trajectory | N_e at 5 kya | R0 S21 | R0 / 21 | R2 S21 | R2 / 21 | R0 tracked total (Day 16,299) | R0 pre-7000 share |
|---|---|---|---|---|---|---|---|
| constant 1e4 (control) | 10,000 | 3,897 | 186 | 2,281 | 109 | 15,120 | 0.69 |
| constant 1.4e5 (control) | 140,000 | 16.5 | 0.8 | 86.2 | 4.1 | 1,353 | 0.98 |
| Gravel 2011 | 16,813 | 1,127 | 54 | 738 | 35 | 7,603 | 0.78 |
| Gazave 2014 | 5,633 | 5,164 | 246 | 1,900 | 91 | 17,225 | 0.60 |
| Coventry 2010 | 7,700 | 5,102 | 243 | 2,550 | 121 | 17,380 | 0.64 |
| Nelson 2012, 1.7%/gen (central) | 137,363 | 42.0 | 2.0 | 50.8 | 2.4 | 1,308 | 0.92 |
| Nelson, 1.2%/gen | 368,093 | 5.3 | 0.3 | 33.8 | 1.6 | 790 | 0.98 |
| Nelson, 2.3%/gen | 42,358 | 602 | 28.7 | 107 | 5.1 | 4,143 | 0.47 |

## Predictions versus results
- **P1 (controls) met.** 1e4: 3,897 vs C1c 3,925 (0.99x); 1.4e5: 16.5, inside [10, 45].
- **P2 (Gravel) met.** 1,127 in [300, 3,000]; 54x Day's 21 (needed >= 15x).
- **P3 (Coventry) met.** 5,102 in [1,500, 6,000]; 243x (needed >= 70x).
- **P4 (Gazave) met.** 5,164 in [2,000, 8,000] and above the 1e4 control (3,897).
- **P5 central met; both sensitivity clauses MISSED.** Central Nelson 42 in [25, 250], and it is the only trajectory within 12x of 21 (2.0x). The pre-registration predicted S21 >= 300 at 1.2%/gen and 5-80 at 2.3%/gen. Observed 5.3 and 602. The direction was wrong: with the present size held at 4.0M, a lower growth rate means a **larger** N_e in the window (368k at 5 kya), hence fewer events; a higher rate means smaller N_e (42k) and more events. The error was in the pre-registered reasoning, not in the run; the miss stands and the ordering is monotone in late-window N_e as the docstring's own rule said.
- **P6 (tension survives) met.** No cell has all three of: tracked total within 3x of 16,299, S21 in [7, 63], pre-7000 share >= 90%. Gazave and Coventry have the tracked total (17k) but S21 about 245x; Nelson central has S21 near 21 but a tracked total of 1.3k (8% of Day's). R2 does the same (no cell with total in range and S21 in range).
- **P7 (R2 within 2x of R0) MISSED.** Ratios R0/R2: Gravel 1.5, Nelson 0.8, Gazave 2.7, Coventry 2.0 (2.0007, a hair over), Nelson 1.2% 0.16, Nelson 2.3% 5.6, control 1e4 1.7, control 1.4e5 0.19. Replacement is second-order only when the late-window N_e is near 2e4 to 1.4e5; at the extremes it moves S21 by 3x to 6x in either direction (it adds events when drift alone gives few, removes them when drift gives many). C1c's P4 was stated for its own grid; this extends it.
- **Result that would change a verdict: did not fire.** No flat fit lands within 3x of 21 (closest Gravel R2, 35x). Nelson central is not above 500.

## What this does and does not settle
- **Settles (model-conditional):** the RG-01 question. Of the four published trajectories, three (Gravel, Gazave, Coventry) leave Day's 21 as a deficit of 35x to 246x; only the Nelson-type fast growth (reaching 1e5 by about 5 kya) gets within 2.4x, in both R0 and R2. A reading on which 21 "needs no clock failure" requires choosing Nelson, whose growth start (9.3 kya) is secondhand and whose present N_e (4.0M) sits far from the coalescent-based fits (holocene-ne.md).
- **Does not settle:** which trajectory is right (the literature does not decide); that Day's 21 itself is reproducible from his genotypes (C1d: it is not, by 3.6x); the tracked-total tension, which Nelson makes **worse** for the critic reading (total 1.3k vs 16.3k). The controls reproduce C1c, so the panel and AADR depth are unchanged.

## Who this helps
- **Day:** under the three flatter fits (the coalescent and SFS estimates closest to textbook N_e of 1e4) his 21 is 35x to 246x below the neutral expectation, so the "something stopped" reading is not removed by plausible Holocene demography unless fast Nelson-type growth is assumed. Nelson, the one rescue, also removes 92% of his tracked total.
- **Critics (McCarthy, keruru, Hancock):** the demographic route does work: a published trajectory (Nelson 2012, 1.7% per generation) gives S21 = 42 (R0) or 51 (R2), within 2.4x of 21 with no clock failure, and the 1.2-2.3% CI gives 5 to 600 (R0) and 34 to 107 (R2). The data do not force a constant 1e4. The critic reading is then conditional on a growth model, not on special pleading about the call set.

## Review resolution
- **MAJOR-1 (generation-time mismatch).** The trajectories are for 25 y per generation, the engine steps 20 y, so drift per calendar year is 1.25x too large (equivalent to N_e x 0.8). C1c measured that 25 y per generation lowers S21 to 0.6-0.7x. Bracket, **not rerun**: multiply the S21 columns by 0.6-0.7: Gravel R0 about 680-790 (32-38x), Gazave about 3,100-3,600 (150-170x), Coventry about 3,100-3,600 (150-170x), Nelson central about 25-29 (1.2-1.4x), Nelson 2.3% about 360-420. No conclusion changes; the Nelson gap narrows. A corrected-clock rerun is queued as a follow-up (it would be post hoc).
- MINOR-1: P5 sensitivity and P7 misses disclosed above. MINOR-2: Nelson's 4.0M is a growth-model size, not a coalescent size, and its start date is secondhand. MINOR-3: panel-to-panel spread is not reported (the draws pool 3 panels). MINOR-4: C1d shows 3.6-5k events on the real genotypes under Day's described method, so both the data side and the model side exceed his 21; the 35-246x compares the model with his number. MINOR-5: the three flat fits are SFS-dominated by recent rare variants; IBD and short-ROH sharing point to growth from the Mesolithic (holocene-ne.md), so the Nelson-type earlier growth is a published, not ad hoc, alternative.
- No verdict changes.
