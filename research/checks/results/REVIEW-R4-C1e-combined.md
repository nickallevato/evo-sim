# Review of R4 C1e (combined, low-stakes tier)

Date 2026-10-09. Method: read `R4-C1e.md`, `raw/c1e_analysis.txt`, the script's trajectory functions; hand checks; nothing rerun.
**Escalation check:** C1e informs C4 (pending), C, C6, C5b, B2e. None is on the ROOT path as load-bearing in `hierarchy.yaml`, and no verdict changes. Combined tier applies.

## 1. Correctness
Hand checks: Nelson 1.7% N_e at 5 kya = 4.0e6 x 1.017^-200 = 1.37e5 (table 137,363); Gravel 35,900 x 1.0038^-200 = 16.8k; R0/R2 ratios as tabled; Coventry 5,102.3/2,550.3 = 2.0007; P6 check against every row. All agree.
- **MAJOR-1.** Generation-time mismatch. The trajectories are published for 25 y per generation, but the C1c engine steps 20 y and takes N_e as the size parameter, so drift per calendar year is 1.25x too large (equivalent to N_e x 0.8). C1c measured that 25 y per generation lowers S21 to 0.6-0.7x. So every non-control S21 here is biased high by about 1.4-1.7x. It cannot flip a verdict (Gravel 54x -> about 35x, Gazave 246x -> about 160x, Coventry 243x -> about 160x, all still deficits; Nelson central 2.0x -> about 1.3x) but it narrows the Nelson gap and the pre-registration did not mention it. Not rerun; resolution gives the bracket.
- **MINOR-1.** P5 sensitivity (1.2%, 2.3%) and P7 (R2 within 2x) missed; the write-up discloses both and the P5 miss is a sign error in the pre-registration reasoning.
- **MINOR-2.** Nelson's present N_e (4.0M) is not a coalescent size; the three flat fits and the Nelson fit are different quantities. The write-up says Nelson's date is secondhand; add that its N_e is a growth-model size.
- **MINOR-3.** S21 is a mean of 6 draws over 3 panels; the draw spread (e.g. R0 Nelson 37-45) is small, but panel-to-panel spread is not reported.
- **NOTE-1.** Controls reproduce C1c (3,897 vs 3,925; 16.5 in range), so the panel is unchanged.

## 2. Day-side steelman
- The write-up credits the 35-246x deficit and the tracked-total tension. Fair.
- **MINOR-4.** Day's "21" is computed by his own unpublished call rules (C1d: 3.6x unreproduced), so "deficit of 35x-246x" compares the model with his number, not with data. The write-up should say the C1d replication is on the data side (3.6-5k events) and C1e on the model side; both exceed 21.

## 3. Critic-side steelman
- **MINOR-5.** The critic reading's strength is that three of four published fits are not the only information: IBD and short-ROH sharing indicate growth from the Mesolithic (holocene-ne.md). The write-up should say the three flat fits are SFS fits dominated by recent rare variants and that Nelson-type earlier growth is a published, not ad hoc, alternative.
- **NOTE-2.** The write-up correctly notes Nelson worsens the tracked-total tension (1.3k vs 16.3k), which hurts the critic combination.

## Verdict on C1e
Sound with MAJOR-1 handled by a bracket. No verdict change. 1 MAJOR, 5 MINOR.
