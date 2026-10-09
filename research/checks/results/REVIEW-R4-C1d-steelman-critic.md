# REVIEW R4 C1d: critic-side steelman

Reviewer role: argue as strongly as honestly possible for Day's critics (the C1c/C1d model-builders, McCarthy-type "neutral predicts thousands", and keruru), then judge whether `R4-C1d.md` gives them their due. Read: `AGENTS.md`, `results/R4-C1d.md` (cited as "R4-C1d L<line>"), the pre-registration docstring of `research/checks/c1d_aadr_real.py`, claim files B2e, C5b, C, C1, C6, C7, `quotes-critics.md` RF-12 to RF-14, keruru's draft and code (`sources/raw/refresh-2026-10-09/zenodo-22184713/x/adna-temporal-ne/`, read only), Day's Z18525185 and Z23046531 raw text (read only), and the raw outputs `results/raw/c1d_v66_ne.txt`, `c1d_v62_posthoc.txt`. Nothing was executed against genotypes (they live only on na-workhorse). Where I do arithmetic of my own it is labelled "reviewer arithmetic" and is not a result.

## Bottom line

The check gives the critics most of their due: non-reproduction is item 1 of the brief, keruru's N_e replicates to 4% and the numbers are given, P14/P16 failures (admixture matters less than the author expected) are recorded, and the critic-side errors are listed. It does not fully give them their due in five places. Three are MAJOR and touch the verdicts proposed in section 7:

1. The transversion result is over-used on Day's side and used inconsistently (MAJOR, F1).
2. "Not established" for keruru is symmetric in wording but not in the evidence, and the region-composition point is unquantified, contradicted by data already in hand, and mis-scaled (MAJOR, F4 and F5).
3. C6 external `untestable` is the wrong word for a statistic that was tested 132 times and missed by a factor of about 200; and the missing-scripts point is attached to the wrong paper (MAJOR, F3).

Against the critics, I also record what the check gets right and where the steelman fails (section "Where the critic steelman fails").

---

## MAJOR findings

### F1 (MAJOR). "Transversions-only is the same order as Day's 21" is over-read, and the check uses it in three incompatible ways

**What the check says.**
- R4-C1d L9: "So the number is highly sensitive to the substitution class (about 100-fold), and a transversion-only count is the same order as Day's 21 while his eligible total and his bin profile are still not matched."
- R4-C1d L132 (Day bullet): "The 97-99% pre-7000 share in the transversion class matches his \"99.8% before 7000 BP\" better than the all-site 91%."
- R4-C1d L131 (Day bullet): "roughly 900 expected against 36-113 seen; not run as a calibrated comparison"
- R4-C1d L140 (critics bullet): "the same data show a transversion-only count of 36-113 that is near Day's number, so \"neutral predicts thousands\" is not the full picture once error is controlled"

**The steelman.** Six points, each checkable from the check's own raw output (`raw/c1d_v62_posthoc.txt` lines 10 and 12).

1. *Rate, not count.* The comparable quantity is events per eligible allele, because the eligible count is the denominator the 21 sits on. Day: 21 / 22,428 = 9.4e-4. Transversions, all chromosomes: 113 / 9,260 = 1.2e-2 (13x Day). Autosomal: 36 / 6,306 = 5.7e-3 (6x). v66: 66 / 7,614 = 8.7e-3 (9x). (Reviewer arithmetic from the numbers at R4-C1d L65 and the posthoc file.) "Same order" holds only for the raw count, and the raw count is the part that depends on discarding 70-80% of the eligible set.
2. *Profile.* In the transversion class the 10000+ bin is 7,896 / 9,260 = 85% (autosomal 5,382 / 6,306 = 85%) of tracked events; Day's is 3,038 / 16,299 = 18.6%, with 8000-10000 BP the plurality at 53.6% (his 8,741). The "pre-7000 share" of 0.98-0.99 is not discriminating when one bin dominates, so L132 credits Day with a match that is only a share coincidence. The post-6000 events also sit in the wrong place: 0-500 BP holds 61 of 113 (16 of 36 autosomal) against Day's 2.
3. *Start table.* The one quantity the all-site reading reproduces (79.0 / 19.8 / 0.7 / 0.5 % against Day's 79.2 / 20.2 / 0.5 / 0.2, R4-C1d L50 and L52) is destroyed by the transversion filter: 99.0 / 0.8 / 0.1 / 0.0 autosomal (raw posthoc line 12; 92.3 / 5.1 / 1.3 / 1.3 all chromosomes, line 10), about 20 points off Day's [99,100) share. R4-C1d L65 prints "[99,100) 99.0 / 99.5%" without saying that this loses the one match. So no single filter fits Day: all-site fits the start table and misses everything else; transversions fit the pre-7000 share and the raw 21 and miss the start table, the profile and the rate. The Day bullet should say so.
4. *Sensitivity inside the class.* 113 becomes 36 by dropping non-autosomes (X, Y, mito), a factor of 3 inside a number the text calls a "same order". Day's Z18525185 states 1,233,013 SNPs (all), so 113 is the literal one; 36 is the Z23046531 convention.
5. *Post hoc.* The filter was chosen after seeing 97.7% transitions (R4-C1d L9, L63). It is a legitimate damage-robustness filter (transversion-only calls are standard for non-UDG aDNA), which is why it is worth reporting, but then the right comparison is a transversion-restricted neutral model at the same call noise, not Day's unrestricted 21.
6. *Internally contradictory use.* The Day bullet (L131) says the neutral expectation on this subset is roughly 900 against 36-113 seen, i.e. an 8-25x deficit, which is the pro-Day reading. The critics bullet (L140) says the transversion count is "near Day's number" and that "21 is a deficit against neutral thousands is not supported either". Both cannot stand. The 900 comes from scaling C1c's R0 output by the 22% transversion share (4,217 x 0.22 = 930; or 3,925 x 0.22 = 860), and C1c's eligible/S21 had a 0.1% flat error term in the first number. If the transversion expectation really is of order 900 at Ne 1e4 the transversion residual is a deficit (a finding for Day, to be reported as such); if it is not, the 900 should be deleted. The check should either run the calibrated comparison (the C1c simulator exists; restrict to 22% of sites with a transversion error rate) or state both readings next to each other and drop "near Day's number" from the critics bullet.

**Is a transversion-only count the right neutral comparator at all?** Not by itself. It is a robustness filter that makes the data less damage-prone; the comparator still has to be a model with the same filter. Two further reasons it is not a clean neutral baseline: transitions carry most of real mutation (CpG), so removing them also removes real recurrent/hypermutable sites; and the panel's ascertainment SFS differs by class. Both are untested here.

**Fix.**
- Replace "is the same order as Day's 21" (L9, L123) by the rate comparison and the three mismatches (eligible 6.3-10.0k against 22.4k; 10000+ bin 85% against 18.6%; start table 99.0% against 79.2%), and print the autosomal and all-chromosome numbers together with the 3x gap between them.
- Remove "near Day's number" from L140 or tie it to a calibrated transversion-restricted model run (label post hoc). Reconcile L131 with L140 in one sentence.
- In section 7 C6 reason, say "36-113, with eligible, profile and start table not matching" rather than a bare "36-113".

### F2 (MAJOR). Damage is asserted in section 8 and disclaimed in section 3; the discriminating test is cheap and not run

R4-C1d L66: "this check cannot tell damage from real mutation-class-dependent differences between the ancient and modern bins." R4-C1d L145: "Event anatomy shows transitions are 97% of the excess, not that the cause is deamination damage; library-type (UDG) stratification, per-individual damage rates and reference bias were not tested." Yet R4-C1d L138 (critics bullet) says "the \"21\" is therefore a statement about assay and error class as much as about the clock", and L140 says the thousands are "mostly an error-class artefact".

The critics' position (C1c and the C claim file) is that the thousands are what a sampled, noisy, polymorphism-ascertained panel gives. That position is only half supported if transitions are real mutational/recurrent variation instead of damage: then the thousands are not "assay", and the critics' "neutral predicts thousands" has to be re-argued on different grounds. Whichever way it goes, the claim is load-bearing for both critic and Day readings of the check. The AADR anno has a library-type column and the C1c reviews already pointed to it as "available, unused" (R4-C1c scope note on damage and library-type columns). The test is: S21 and the transition share of events in UDG-treated ("plus"/"half") versus non-UDG ("minus") libraries, per bin.

**Fix.** Either run the UDG stratification (post hoc, separate commit) or soften L138 and L140 to the L66/L145 wording ("consistent with an error-class artefact; not isolated"). The soft wording is what the evidence supports today.

### F3 (MAJOR). The non-reproduction is under-weighted in the verdict (`untestable`), while the scripts point is attached to the wrong paper

**Under-weighted.** The proposed edit (R4-C1d L123): "C6 external: keep `untestable`, but replace the reason." The claim was tested: 120 configurations on V1 plus 12 on V2, none within 10% of the eligible count together with S21 within 50% (R4-C1d L8), closest eligible 2.4x Day's (L104), S21 4,957 / 3,649 against 21 (about 170-240x, L137). The claim being tested is concrete: "99.8% of fixation events occurred within a single 2,000-year window (8000-10000 BP), with essentially zero fixations in the subsequent 7,000 years" (C6 statement, Z18525185 abstract). The check's own critics bullet says "His own statement \"essentially zero fixations in the subsequent 7,000 years\" is false under his own rule on real data" (L137). `untestable` in the vocabulary means "cannot be tested"; the right readings are either `contradicted` (for the statement under the literal stated rule on the public data) or, if the reviewer insists the unpublished choices could rescue it, `contested`. Keeping `untestable` while saying "false under his own rule" is inconsistent. Day-side reservations (the p1 patch is not the original v62.0 of Sept 2024; unpublished QC; L143) are real and favour `contested` at least; they do not support `untestable`. Suggest: external `contradicted` for the literal reading, with a comment that the actual pipeline behind 21 is unknown and not recoverable; and the C6 sentence "cannot adjudicate" in the Check paragraph should be replaced.

**Wrong paper for the scripts.** R4-C1d L123 and L7: "Day's scripts, named in Z23046531, are not on Zenodo." The sentence is in Z23046531 §5 (raw text line 237): "Analysis scripts are available from the authors at Zenodo." Z18525185, the paper that produces the 21, makes no script promise (its only availability sentence, raw line 301, names the AADR). So missing scripts is evidence about the later paper's two-period statistic (1 and 3 of 1,143,671, and 17,806 newly 100%), which this check does not compute (R4-C1d L18: "a different quantity and is not computed here"). Also, "available from the authors at Zenodo" can be read as "on request from the authors"; the check did not contact authors (rule 6), so "no target" is fair for a Zenodo search but "unfulfilled" (L17) is firmer than the text allows.

**Should missing scripts and non-reproduction dominate?** Non-reproduction should lead, and it does (item 1-2 of the brief). Missing scripts should not dominate the C6 verdict because the C6 source promises none. But the critic point stands in a different place: the C claim's headline (one and three of 1,143,671 in Z23046531) is the statistic the scripts were promised for, and it is the one whose reproduction is cheap now that the per-SNP group counts exist on workhorse (the pipeline already produces the Neolithic-pooled and modern frequencies; the start table shows about 0.5% of eligible v62 alleles start below 90%, roughly 300 alleles by reviewer arithmetic of 0.5% x 62,757, against Z23046531's single 50-90% completion; the samples and filters differ, min-100-genotyped and autosomal-only, so this is a pointer and not a comparison).

**Fix.**
- Change the C6 external recommendation from `untestable` to `contradicted` (narrow literal statement) or `contested`, and keep the "pipeline unrecoverable" caveat in the comment.
- Move the scripts sentence off C6 and onto C / Z23046531. Quote the sentence in full (it is ambiguous as to "from the authors").
- Add a queued item: compute the Z23046531 two-period statistic (6000-8000 BP vs present-day Europeans, autosomes, min 100 genotyped per period, MAF >= 10% start) on v62.p1 and v66.p1, pre-registered. This is the largest gap in "does the check give the critics their due", because the C claim's `contested` verdict currently rests on Day's own numbers.

### F4 (MAJOR). "Not established" for keruru is accurate on the headline wording but hides an asymmetry the check's own evidence supports

**What the check says.**
- R4-C1d L83: "Arithmetic, not a test: the data fix F, not N."
- R4-C1d L85: "The data neither confirm that Wright's N_e is wrong by three orders of magnitude (that needs F_nondrift to be a small fraction of 0.005) nor rescue it (that needs F_nondrift to be nearly all of it)."
- R4-C1d L133 (placed under "Day / allies"): "keruru's \"three orders of magnitude\" is not established (section 4, point 6)".

**Steelman.**
1. *The census is not what the claim turns on.* The check dismisses 1e7 as unsourced. But the comparison is robust over the census: with N_e = 0.571 N and F_drift = t / (2 N_e) (t = 102), reviewer arithmetic gives: N = 1e7 gives F_drift 9e-6 (590x below the measured corrected F of 0.00525); N = 1e6 gives 9e-5 (59x); N = 1e5 gives 8.9e-4 (5.9x). Wright matches the measured corrected N_e of 9,665 only if the entire sampled population is N = 9,665 / 0.571 = about 16,900. So the claim fails to reconcile at any census a reviewer would accept for Bronze Age to Medieval Europe, not merely at 1e7. The check should print this break-even, because "unsourced census" otherwise reads as undermining the claim when it only changes the factor from about 600 to about 6 across two orders of census. "Three orders" then needs N around 1e7; "two orders" survives 1e6; one order survives 1e5. keruru's draft is itself inconsistent between 1e-4, 4e-4 and 8e-4 (RF-14 note), which the check could cite as the fair criticism of the headline wording.
2. *Rescue needs non-drift share of 99.8%.* The check's own non-drift accounting: the admixture axis explains about 0-4% of BA-Med F (top/bottom quintile 0.96, intercept N_e 9,530, L84); the composition-shift term is about 20% on the check's own regional numbers (see F5); relatedness and batch are untested and unquantified. None approaches 99.8%. A symmetrical "neither confirm nor rescue" treats F_nondrift = small and F_nondrift = 99.8% as equally open; they are not. The check pre-registered exactly this at 85%: P15 (R4-C1d L114): "drift-only (intercept) N_e < 1e5 (85%)", held, with 9,530-14,089. The right summary is: direction and a discrepancy of at least one to two orders are robust to every non-drift component tested; the exact factor is census-dependent; the untested components could change the factor but would have to supply nearly all of F to restore Wright.
3. *keruru's simulation shows the estimator reproduces Wright when Wright holds.* Draft section 6.1 (lines 637-672): structure "inflates the estimate" (N_e/N 0.83-2.44), a moving sampling frame "does essentially nothing" (1.13, 1.02, 1.01, 1.02), and the V_k table returns 0.535 against Wright's 0.571 at V_k = 5. So a real-data ratio of about 1e-3 is not what the estimator returns when the population obeys Wright's formula at census, in his simulations. The check's simulation (c1d_sim.json) tests admixture only; it neither confirms nor refutes this island/moving-frame result, and R4-C1d never mentions that keruru ran it (nor his section 3.2 spatial-spread check). In the critic section this is a credit omitted.
4. *"Not established" is the right reading of RF-13's own words.* RF-13 says "We do not claim the ceiling argument is refuted. We claim its input is measurably wrong where it can be tested". So the claim the check should be scored against is "input is measurably wrong where it can be tested", not "refuted". The check's "not established" is a fair score against RF-12 ("wrong by three orders of magnitude") and a harsh score against RF-13. It should state which.
5. *Placement.* The "not established" bullet sits first in the "Day / allies" block; the lower-bound and "growing population" qualifications favour keruru's own stated biases ("Three known biases, all downward", draft line 212; "This bias is downward", line 193), i.e. the check's "lower bound" is keruru's own position, not a new criticism of it. The check should say so (see F6 for the credit).
6. *"Arithmetic, not a test" is fair as a label for the 600x* (the data fix F; Wright's frame is applied by hand). It is not fair if read as "so the data say nothing about Wright": F fixes a minimum N_e-equivalent, and for Wright to hold N must be about 17k.

**Fix.**
- Add a census-sensitivity line and the break-even N of about 17k (reviewer arithmetic above; recompute from the corrected F in the final text).
- Reword L85/L133/L125 to: "the direction and a gap of at least one order at any census above 1e5 are robust to the non-drift terms tested (ancestry axis under 4%, composition about 20% on the check's own regional numbers); the headline three orders needs a census near 1e7 that is unsourced; reconciling to Wright would need F to be more than 99% non-drift, which is not supported". Then `contested` for B2e external stands, but with this reason.
- Score RF-12 and RF-13 separately.
- Cite keruru's draft sections 3.2 and 6.1 as already tested by him.

### F5 (MAJOR). The sampling-region F point is speculative as written, mis-scaled, and contradicted by data already computed

**What the check says.** R4-C1d L84: "A shift in where the sampled people came from ... can therefore contribute F of the measured order without drift. Not quantified as a share." R4-C1d L140: "his own measurement shows regional composition alone can produce F of the observed size." R4-C1d L146: "Regional strata for N_e mostly fail the power rule (regional Modern bins of 6-228 individuals) and are listed in `c1d_*_ne.txt`, not interpreted."

**Steelman.** Three separate problems.

1. *Mis-scaling.* The same-time F between two regions (0.008-0.055) is a full-differentiation number: it is the F you would get if the whole sample were replaced by the other region. A composition shift contributes only through the weight changes. With regional weights w, x - y = sum Δw_i (p_i - pbar), and the F contributed is -(1/2) sum_ij Δw_i Δw_j F_ij (reviewer derivation; uses sum Δw = 0). With the check's own shares (BA to Medieval: Central +28 points, Iberia -8, Italy/Balkans -15, Scandinavia +9, Eastern Europe -15), the pairs the check gives (Iberia-Central 0.019, Central-Italy/Balkans 0.016, Central-Scandinavia 0.008, Central-East 0.023, Italy/Balkans-East 0.049) sum to about +0.0008, and with the five unreported pairs set to a guessed 0.03 the total is about +0.001 (reviewer arithmetic, order of magnitude only). That is about 20% of 0.00525, not "of the measured order". The scale factor is roughly Δw^2 (0.28^2 = 0.08 for the dominant region), not 1. The statement "1-10 times the whole BA-to-Medieval temporal F" (L12) compares the wrong things.
2. *Contradicted by the within-region results the check already has.* `raw/c1d_v66_ne.txt` section "regions (form B)": BA-Med within-region N_e is Iberia 4,442 (S 79/56), CentralEur 3,407 (S 262/887), Italy/Balkans 7,166 (S 168/112), Scandinavia 14,637 (S 51/220), EastEur 3,909 (S 179/112), against the pooled 9,665. A composition artefact predicts within-region N_e at or above the pooled value, because holding region fixed removes the artefact. Four of five are lower, and the best-powered one (Central Europe, S 262/887, F 0.0214, correction 0.0064) is 3x lower. The check's L146 sentence disposes of this ("fail the power rule", "not interpreted"). That is too quick: Central Europe's S is within 25% of the requirement 10 N_e / t = 10 x 3,407 / 102 = 334, and the direction is the opposite of what the artefact predicts. Caveats on the critics' side as well: within-region samples are smaller (more correction noise) and themselves substructured (cemeteries, sub-regions), so lower N_e is also what local structure gives. So the data say "region composition cannot be the main driver" at most, not that structure is absent.
3. *Misattribution.* "his own measurement shows" (L140) is false as written: the composition-to-F inference is this check's, not keruru's measurement. His own section 3.2 shows the sampled geographic spread in the two anchoring bins is the narrowest in the series and not trending (draft lines 263-300), and section 6.1 simulates a moving frame. The check's regional percentages are a finer, better test than his coarse "spread" proxy and the check deserves credit for them; they just have not been run through to a number.

**Fix.**
- Run the post-stratified recomputation (reweight Medieval to the BA regional composition, or restrict both bins to the five regions with fixed weights) and report F_adj and N_e. Label it post hoc. This takes the stratified per-SNP group counts that already exist on workhorse.
- Until then, replace "can therefore contribute F of the measured order" with "could contribute at most a fraction set by the squared weight changes (on the reported pairs, about 20% on a rough count); the within-region BA-Med N_e (3.4k-14.6k, Central Europe 3.4k at S 262/887) does not move toward Wright". Delete "his own measurement shows".
- Interpret the regional table, with the power caveat stated, instead of "not interpreted".

---

## MINOR findings

### F6 (MINOR). The sampling correction is an error by keruru's own definitions, not a convention for a different S; the check should cite his lines, and credit his disclosure

**What the check says.** R4-C1d L11: "His formula `1/(2 S0) + 1/(2 St)` is right when S counts diploid individuals; his code feeds it a pseudo-haploid allele count."

**Steelman for the convention reading.** The Nei-Tajima/Waples form uses S as diploid individuals, so someone who defines S as "alleles sampled" and keeps 1/(2S) would be using a convention that is inconsistent, not different. A critic could say: keruru states the estimator in the draft with S undefined (draft lines 79-83) and S values (842 / 1,548) are individuals called; if S is "number of called individuals" the formula is the textbook one for diploid data and the pseudo-haploid adjustment is a separate step.

**Why that fails.** keruru's code says the opposite:
- `code/adna_validate.r` lines 45-46: "## F and Ne. S is the ALLELE count: for pseudohaploid ancients that is the" / "## number of individuals, for diploid moderns twice it." Line 50 then uses `cr <- 1/(2*S0) + 1/(2*St)`.
- `code/adna_temporal_ne.r` line 14: "An ancient individual contributes ONE allele, not two, so S is the".
- Draft line 190: "Simulation puts the working requirement at S ≳ 10·N_e/t alleles."
His simulator `samp_pseudohap(p, S)` draws S binomial alleles, whose sampling variance of x - y is m(1-m)(1/S0 + 1/St), so the correct subtraction in his own validation is 1/S0 + 1/St, twice what line 50 subtracts. The recovery ratio of about 0.82 he reports at the power margin (draft line 193, "recovery in simulation ran around 0.82 of true. This bias is downward") is of the size the factor-2 error gives (the check's own simulation: (K)/true 0.84, R4-C1d L91), but he attributes it to power. So it is an internal inconsistency, not a convention, and the check's wording "half the standard one" is accurate. The check should cite the code lines above: they remove the convention defence without needing the check's own simulation. (Label: that his 0.82 is the same effect is my inference from the match in size; the draft does not say which run it came from.)

**Proportion and credit.** The error moves N_e by 8-24% (R4-C1d L11) and raises the numbers. That moves N_e/N from 8.1e-4 to 9.7e-4 (700x to 590x), negligible against "three orders". keruru also named the trap explicitly ("the pseudohaploid trap", `adna_validate.r`) and stated that residual biases run downward. The check records the error first in its critic-error list (L140) as if a defect of the argument; it is better described as a small, disclosed-direction implementation error that the author's own warning covered. Not a MAJOR, but the list ordering overweights it.

**Fix.** Cite the code lines; state the effect on N_e/N (about 17% on the ratio); say the direction was one he warned of.

### F7 (MINOR). Critic errors: recorded fairly in count, not fully in proportion, and one is mis-assigned

R4-C1d L140 lists, as cuts against critics: the transversion near-match; the claim that "neutral also predicts ~0" is false for the literal rule; the half-size correction; the unsourced census and lower-bound estimator; the region regex excluding Britain; unfiltered relatives; and the regional composition point.

Assessment:
- *Mis-assigned.* "The \"neutral also predicts ~0\" reading is false for the literal rule" has no critic source. It is the wording of the repo's own earlier C verdict comment ("neutral also predicts ~0 from <50% and 0.04-0.11 from 50-90%", C claim internal verdict comment) and the C6 text ("earlier audit wording"). Placing it under "Cuts against critics" attributes the repo's own earlier verdict to critics. It is a correction of the repo's audit, and should be labelled that, together with the effect on C's internal verdict (`non-sequitur`) in the integration step: the Z23046531 statistic (1 and 3) is a different quantity, so C's verdict should not be changed by the 21 result until F3's computation is done.
- *Unquantified items listed at full weight.* "Region regex excludes Britain" and "relatives unfiltered" have no measured effect in the check, and keruru discloses the second ("No relatedness filtering ... this biases N̂_e downward", draft line 703) and flags the census in his ledger. Listing them next to a quantified item (the 8-24% correction) overstates them. Say "disclosed by the author; not quantified here".
- *Omitted credits on the critic side.* (i) Pre-registered P14 failure (admixture axis explains less than predicted by the check's author) and P16 (10% pulse does not bias; needs m >= 0.4) both support keruru; they are in the table but not in the "Who this helps / critics" bullets except as "does not wipe it out". (ii) The C1c model's literal-statistic prediction (eligible 61,353 / S21 4,217 against real 62,757 / 4,957, R4-C1d L120) was made before the real run and is the strongest single pro-critic result; section 6 files it under "may be partly coincidence". That caution is right (the profile, tracked fraction and start table were not matched), but the critics bullet does not mention it at all. One sentence in the critics bullet would fix this.
- *Absent from the check altogether:* keruru's own section 6.1 simulations (see F4.3), and that RF-14's ratio inconsistency (1e-4 / 4e-4 / 8e-4) is in the claim file but not in the check's discussion of "three orders".

**Fix.** Re-label the "neutral predicts ~0" item as the repo's earlier wording; mark region-regex and relatives as "disclosed, unquantified"; add the P14/P16 and C1c-prediction credits; move the half-size correction below the substantive points.

### F8 (MINOR). The "Day / allies" block contains items that are reviewer judgements about keruru

R4-C1d L133 and L134 put "keruru's \"three orders of magnitude\" is not established" and "The estimate N_e = 8-10k does not by itself support the claim that N is small either" under "Day / allies". Both are claims about the critic's argument, and the second restates Day's C4 caution that keruru's own draft does not dispute (RF-13). They are fair findings but belong under "Cuts against critics" or a neutral "Open" heading, as the structure in the check's own template ("Who this helps ... crediting both sides") implies by sorting on who benefits. As placed, the Day block gets four items that are mostly qualifications of critic claims, and the critic block gets items 1-3 (non-reproduction, thousands, keruru replicates) plus a long "cuts against" list. Count is balanced; the allocation is not quite.

**Fix.** Move L133-134 to a third bullet "Open or neutral", and keep the Day block to things that help Day (his §4.3 description accurate in kind and the start table to 0.4 points on v62; the transversion share at pre-7000 share, with the F1 caveats).

### F9 (MINOR). Smaller items

1. *"Day's cited scripts do not exist"* (the prompt's summary) is stronger than the check: the check says "not found" in Zenodo records returned by the API on 2026-10-09 (R4-C1d L7, L15-17). "Not found" is right; "do not exist" is not established (private records, other hosts, on-request). Keep the check's wording in RESULTS.md and the milestone post.
2. *"Mostly transitions" and the panel base rate.* The check gives the panel's transition share (77.6%) at L9, good. The 10x over-representation is relative to the panel, while mutation-class-dependent recurrent changes at CpG are expected to over-represent transitions among real "events" too; the check mentions this at L66. Keep both together in any summary.
3. *The ratio of the post-6000 events by bin.* 4,177 of 4,957 (84%) are in 0-500 BP, where Day has 2; a single bin dominated by diploid shotgun genomes (rs11260588 example, L64) drives the headline. The check says so; the one-line summary "thousands" should say "thousands, 84% in the youngest bin" to avoid being read as a spread across 7,000 years.
4. *Generation time.* The check's own sensitivity (25-31 y: BA-Med 10,438-8,418) is given; fine. No change.

---

## Where the critic steelman fails (credit the check)

1. *Non-reproduction.* The check does lead with it, runs a labelled grid, pre-registers 25% for reproduction, and gives the result without softening ("No such configuration", L104). Fair. The only change I ask for is the verdict word (F3).
2. *Replication of keruru.* Reported plainly: -4.0% and -1.7%, all seven windows within 1-8%, SNPs within 0.3%. The headline "The number is real" (L10) gives the critic what is theirs. Fair.
3. *Not calling the sampling correction a refutation.* The check says the correction runs against Day, not for him ("does not rescue Day", L11). Fair.
4. *Lower bound.* The lower-bound label is both the check's and keruru's. Not a new criticism; F4.5 asks only for credit.
5. *Scripts.* The scripts point is real, documented (hashes in `sources/raw/day-scripts-search-2026-10-09/`), and not over-claimed in the check body. The overreach is only in the summary phrase and in attaching it to C6 (F3, F9.1).
6. *Section 8 critic bullet 1* ("Day's table does not reproduce under the stated method (2.2-2.8x eligible, 170-240x on the 21, wrong profile, wrong tracked fraction)") is accurate to the numbers in section 3.
7. *Transversions* are reported with the right caveat in the Result in brief (L9); the problem is the reuse in L132 and L140 (F1), not the first statement.

## Summary table

| # | Sev | Topic | Fix in one line |
|---|---|---|---|
| F1 | MAJOR | Transversions over-read and used inconsistently (L9, L131, L132, L140) | State the rate (6-13x Day), the 85% 10000+ share, the lost start table; run or drop the "~900 expected" comparison |
| F2 | MAJOR | Damage asserted in section 8, disclaimed in section 3 | Run the UDG split or soften L138 and L140 |
| F3 | MAJOR | C6 `untestable` after 132 tests; scripts promise is in Z23046531, not Z18525185 | `contradicted` (literal) or `contested`; move scripts to C; compute the Z23046531 statistic |
| F4 | MAJOR | "Not established" hides the asymmetry (rescue needs more than 99% non-drift; break-even N about 17k) | Add census sensitivity and required non-drift share; score RF-12 and RF-13 separately |
| F5 | MAJOR | Region-composition F unquantified, mis-scaled by Δw^2 (about 20% on reviewer arithmetic), contradicted by within-region N_e; "his own measurement" is misattributed | Post-stratified run; delete the misattribution; interpret the regional table |
| F6 | MINOR | Correction is an error by his own code comments; cite lines; effect is about 17% on the ratio | Cite `adna_validate.r` 45-50, `adna_temporal_ne.r` 14, draft 190 |
| F7 | MINOR | Critic-error list: one item is the repo's own wording; unquantified items at full weight; credits omitted | Re-label; add P14/P16 and C1c prediction credits |
| F8 | MINOR | Day/allies block holds critic-qualifying items | Add an "Open or neutral" bullet |
| F9 | MINOR | "do not exist" vs "not found"; 84% in the youngest bin | Keep "not found"; add the bin share to summaries |

## What I did not check

- I did not re-run any genotype computation (data only on na-workhorse); every number above is read from the check's text or raw outputs, or labelled reviewer arithmetic. The Δw^2 estimate in F5 uses five pair values from the check and a guess for five unreported pairs, so it is an order-of-magnitude bound, not a result.
- I did not verify the Wright formula or keruru's census (the check did not either, R4-C1d L147).
- I did not review the Day-side or correctness questions beyond what bears on the critic side; those are in the other two reviews.
