"""L5-C1a -- the random-SNP comparator for C1a's sign: against a matched panel of sites drawn WITHOUT the 1240k panel's
present-day-variable ascertainment, does the expected count of Day's detectable recent fixations go UP (Day, C1a) or
DOWN (the critics, C1) on the ascertained panel, at the same s and the same horizon?

THROWAWAY research check.  PRE-REGISTRATION: this docstring was committed with the script before the main run.
Brief: research/checks/briefs/L5-C1a-analyst.md (lead, 2026-10-13).  Parent check: L5 (R4-L5.md; registration 0e6da82,
launch fixes 369354d / 30e1302, run f99d925).  Review tier: one combined review (brief), unless the escalation clause in
section 5 fires.
Run (isolated venv; the main run on na-workhorse only, AFTER the `ph2` collect task is done):
    research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py selfcheck             # identity / bound / pickling checks
    research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py smoke <outdir>        # tiny sizes, in-process, timing only
    research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py hostsmoke <workers> <outdir>   # real pool, full grid, tiny sizes
    research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py main <workers> <outdir>
    research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py analyse <outdir> [<l5_raw_dir>]
Reuses l5_adna_power.py (imported, never edited; its own imports c1c_call_depth_replacement.py and
c1e_holocene_trajectories.py come with it).  Every L5 parameter is kept: seeds, sizes, grid, demographies, designs,
panel model, sweep engine.  One function is copied, not imported: run_pass, extended by ONE column (xS, the European
frequency at 10,500 BP) that consumes no random numbers, so the L5 random stream and every L5 number reproduce exactly
(V-rep below).  The comparator uses its own random streams.

------------------------------------------------------------------------------------------------------------------------
1. TARGET CLAIMS AND QUOTES
  C1a (Day; claim file docs/research/claims/C1a-day-ascertainment-reply.md; no Q id yet, the statement is in the claim
  file verbatim): "The 1240k panel was designed to capture polymorphisms informative for ancient DNA studies. This could
  bias toward alleles that are polymorphic in modern Europeans--but such bias would favor detecting recent fixations,
  not obscure them. The absence of recent fixations despite this bias strengthens our conclusion."  (Z18525185,
  2026-02-08, s9.4 "Ascertainment bias in the SNP panel", para 261 of the odt text extraction.)
  The claim file's registered predictions: claimant "ascertained-panel neutral expectation of 50-90% completions is
  higher than for a random site sample"; opposing "the expectation is unchanged or lower".
  C1 (audit-raised, side 'literature'): "near-zero fixations ... are expected by design" (panel ascertained on
  present-day variable sites).  Context quotes, same paper: Q107 "A "fixation event" was recorded when an allele that
  was polymorphic (<100%) in an earlier bin reached 100% frequency in a later bin." (s3.3); Q111 "essentially all
  "fixations" were completion events for alleles already near fixation--not new substitutions traversing the frequency
  spectrum." (s4.3).  Day's zero-reported statistics: Q53 (Z23046531 p.6, 2026-09-29: Z50, Z10), Q55 (blog 2026-01-14
  para 5: B10).  L5 left the sign untested (R4-L5.md s6 item 3, s11 item 5): "An unascertained comparator (a random
  SNP panel from the neutral sample) was not computed."

2. THE COMPARATOR (construction fixed here)
  Panels.  Every panel has 1,143,671 sites (v62; v66 and blog scaled by their site counts, as L5), the same density on
  the genetic map (1,143,671 / 36.8 M per Morgan), the same coverage model (per-site call counts drawn by L5's
  event_probs from the AADR call-depth table, identical for every panel: coverage is matched by construction; the real
  panel's capture heterogeneity is modelled for none), the same sample sizes, demographies, sweeps and window.
  They differ ONLY in which sites are included:
    D2  (L5 primary; Haak 2015 design): site heterozygous in one African individual: inclusion c2 * 2a(1-a), a = present
        African frequency (L5 s2).
    D3  (L5 sensitivity): African MAF >= 5% in 100 diploids: c3 * p3(a).
    R   (the comparator; reading (iv)): a RANDOM SNP PANEL: sites drawn uniformly from all sites segregating in the
        European population at 10,500 BP (the start of the frame) in the same neutral model; inclusion cR per such site,
        cR = 1,143,671 / (L x the number of such sites per bp).  Its inclusion depends on no present-day frequency, in
        any population: it is the panel "drawn without the present-day-variable ascertainment".  It is C1's D0 ("all
        polymorphic at start", c1_ascertainment_sim.py) carried into L5's sweep model.
    R+  (bracket, critic-favourable): R, plus the focal sites of new mutations that arose in Europe AFTER 10,500 BP,
        included at cR (a discovery that also sees recent mutations; the matching neutral recent mutations are NOT added
        to the denominator, so R+ overstates their inclusion slightly).  Differs from R only in hard mode.
    D_EU (reading Rd-2 below): Day's described premise, "polymorphic in modern Europeans": site heterozygous in one
        present-day European individual, inclusion proportional to 2f(1-f), f = present European frequency, normalised to
        the same panel size over R's reference set (sites becoming polymorphic after 10,500 BP ignored: about 2% of
        present heterozygosity, 2 mu x 420 generations against theta).  A site fixed at present has inclusion 0.
    R_sfs (decomposition, descriptive): R reweighted so that its distribution of European frequency at 10,500 BP equals
        D2's (weight c2 x E[2a(1-a) | e] / cR, 50 equal-weight bins of e).  D2 / R = (D2 / R_sfs) x (R_sfs / R): the
        first factor is ascertainment at matched spectrum (who is dropped at the same frequency: C1 point 1), the second
        the spectrum shift itself (C1a's "intermediate frequencies" mechanism).
  How the SFS is matched: R is NOT matched to the panel's spectrum, because the spectrum shift IS the ascertainment
  effect under test; R carries the unascertained European spectrum of the same neutral model.  R_sfs is the
  spectrum-matched variant, reported as a decomposition.
  Estimation (paired).  For each simulated sweep the comparator draws its own hitchhiking SNPs from R's reference set
  (same Poisson count per sweep as L5, L5's hitchhiking formula and founder-allele rule unchanged) and evaluates every
  panel on the SAME SNPs by importance weights relative to R: w_D2 = c2 2a_h(1-a_h) / cR (a_h = African frequency after
  the sweep's hitchhiking in hard mode, as L5; the neutral a in standing mode), w_D3 = c3 p3(a_h) / cR, w_EU =
  2f0(1-f0) / H_EU (f0 = hitchhiked present European frequency; H_EU = R-mean of present 2f(1-f), from the neutral
  arm), w_Rsfs as above.  D2 panel sites that are not segregating in Europe at 10,500 BP produce no event (Europe stays
  monomorphic) and need no draw.  Focal (swept) sites: R inclusion cR if the site is segregating in Europe at 10,500 BP
  (always true for standing variants, by L5's construction; false for hard-mode mutations arising after it), D2 / D3 as
  L5, D_EU = 0 for a site fixed at present.  The importance-weighted D2 (D2_iw) is the band's numerator; L5's own D2
  (reproduced) is the validation target for it (V-iw).
  Statistic.  Primary S* = L5's rule C (the largest expected count among Day's zero-reported statistics {Z50 v62,
  Z50 v66, B10 blog} on D2, chosen per cell from the reproduced L5 numbers).  In L5's committed results S* is B10 blog in
  all 24 cells at 25 y with s >= 0.03 (R4-L5 raw json, read at design time; a property of L5's published output, not of
  this comparator).  The same statistic is used on every panel.  Reported per statistic as well: Z50 v62/v66, Z10
  v62/v66, M10, N100 (Day's Z18525185 "fixation event", Q107: descriptive only; its sweep part includes sampling-only
  events of far hitchhikers, as L5's did), and T1 = window completions whose swept site is on the panel.
  Ratio.  rho = E_D2_iw(S*) / E_R(S*) per cell (cell = demography x mode x s; sweep part; F cancels, so rho holds at any
  rate, Day's 15,556 or mainstream's).  95% interval: paired percentile bootstrap over kept sweeps, 2,000 resamples,
  seed SeedSequence([20261011, 5, 29, cell index]).  Informative cell: F_DAY x (sum D2_iw + sum R) / n_wc >= 1 (at least
  one expected event on either panel at Day's rate).

3. READINGS (rule RD, fixed before the run)
  The lead's ruling L-R8 (research/checks/briefs/L5-reviews-reviewer.md, commit 35b196a, 2026-10-13, made while this
  design was being written) records four readings of C1a's "favor detecting ... not obscure": (i) "not obscure" read
  absolutely -- governing for that clause; L5: Day's sign for strong sweeps; (ii) "favor" against a random-site sample
  of the same size (the claim file's wording) -- supported (L5); (iii) against whole-genome data -- wrong (L5);
  (iv) against a random-SNP panel -- not computed; "The separate C1a random-SNP comparator task stands."  THIS CHECK
  COMPUTES READING (iv).  It does not reopen (i)-(iii).  Within (iv):
  Panel:      Rd-1 the panel's actual design (D2; D3 sensitivity) -- governing within (iv).  The paragraph's subject is
              "the 1240k panel"; "could bias toward alleles polymorphic in modern Europeans" is Day's hedged guess at
              what that bias is, and "such bias" refers back to the panel's bias (rule C).  Rd-2 the bias exactly as Day
              describes it (D_EU): reported with its own band.
  Comparator: R (random SNP panel) is reading (iv) itself.  R+ is a bracket of (iv).  Reading (ii) (random base pairs,
              rho_R0 = rho x cR / 3.69e-4, about 250 rho) is printed as a cross-check of L5's (ii) and moves nothing.
  Statistic:  S* (traversing completions, Q53/Q55, Q111's "new substitutions traversing the frequency spectrum": the
              "recent fixations" whose ABSENCE the paragraph asserts; the paper's 22,428 N100-type events are not absent,
              so they cannot be what "the absence of recent fixations" refers to) -- GOVERNING.  Per-statistic and N100
              rows are reported, move nothing.

4. PREDICTIONS (written before any run; the smoke printed timing and structure only, section 7)
  Validations
   V-rep  Every L5 number this script recomputes (all 90 tasks: sums E_hh, E_f, Q for every design, label and statistic;
          n_wc, n_kept, n_hh_snps, entries, passes, wc_x7_lt50, focal_incl_D2/D3; neutral counts) equals L5's committed
          json (research/checks/results/raw/l5/) to relative 1e-9.  Labels are asserted (task name, s, mode, demography,
          gy).  FAIL = L5 not reproduced: no comparator result is read, no band.
   V-iw   D2_iw against L5's own D2 (independent draws): S* sums at s >= 0.05, 25-y cells: ratio in [0.8, 1.25] in each;
          neutral N100 v62: ratio in [0.95, 1.05] in each demography.  FAIL = comparator not validated: band reported,
          moves nothing.
   V-id   selfcheck: the copied run_pass returns arrays identical to L5's run_pass (same seed, both modes).
   V-bnd  selfcheck: the pruning bound (two-point bracket only, section 6) holds on random test SNPs.
  Audit's own numeric predictions
   A1   cR in [0.08, 0.11] (theta x H_1999 = 3.9e-3 segregating sites per bp in the scaled model); share of D2 panel sites
        segregating in Europe at 10,500 BP (phi) in [0.75, 0.95].
   A2   hard mode, s = 0.05 and 0.1: point DOWN (every informative 25-y cell DOWN; median rho <= 0.8).  Basis: the B10
        path for a hitchhiker on the founder haplotype weights p (its frequency) for p < 0.1, and R's 1/p spectrum puts
        as much p-weighted mass there as D2's (density 2p(1-p) phi), while R also holds post-split European swept sites
        that D2 drops (C1 point 1).
   A3   standing mode, s = 0.05 and 0.1: point DOWN (hitchhikers supply 52-89% of L5's S* events there).
   A4   standing mode, s = 0.03 (focal-dominated): point NOT DOWN (FLAT, UNRESOLVED, mixed or UP); median rho in
        [0.6, 1.6].
   A5   band MIXED (follows from A2-A4 when standing s = 0.03 is informative, which L5's D2 values 2.0-4.9 make
        expected).  No escalation.
   A6   two-point bracket: raises rho* in hard mode at s = 0.1 (median rho_tp / rho >= 1.2), and raises D2's Z50 v62 sum
        at s >= 0.05 by >= 2x in every 25-y cell (the direction of L5's V3 understatement).
   A7   R+: hard mode s = 0.1, median rho_R+ / rho <= 0.9; standing: identical (ratio 1 exactly).
   A8   Rd-2 (D_EU vs R): every informative point DOWN, median rho_EU <= 0.5.
   A9   T1 (swept site on the panel, per window completion): hard mode D2 / R <= 0.8 at every s (0 at s >= 0.02);
        standing D2 / R in [0.8, 3.0] at every s.
   A10  neutral arm, N100 v62: D2_iw / R <= 0.5 in every demography (R's rare sites are seen in the Neolithic sample and
        lost by the present).
  WHAT EACH SIDE PREDICTS (numeric)
   Day (C1a "such bias would favor detecting recent fixations, not obscure them"; claim file: "higher than for a random
     site sample"): every informative (s, mode) point UP on S* (band DAY).  Partial: no point DOWN.  Miss: any point
     DOWN.  Reachable: a simulated outcome with sum D2_iw >= 1.25 sum R and CI_lo > 1 in every informative cell, i.e.
     D2's African-weighted spectrum carries more B10 events per site than R's spectrum and R's focal surplus is small;
     w_D2 reaches c2 / (2 cR) (about 4.5) for sites with a near 0.5, so D2_iw can exceed R by that factor.
   Critics (claim file: "the expectation is unchanged or lower"; C1 "expected by design"): no informative point UP;
     every informative point DOWN or FLAT (bands CRITIC, NULL, or MIXED made only of DOWN and FLAT points).  Partial: no
     point UP but some mixed/unresolved.  Miss: any point UP.  Reachable: sum D2_iw <= 0.8 sum R with CI_hi < 1, i.e.
     R's low-frequency mass and R's post-split swept sites outweigh D2's intermediate-frequency enrichment.

5. LABELS, BANDS AND THE VERDICTS EACH MOVES (claims C1a, C1; no move for C, C6)
  Cell label (first match, in this order): UP: rho >= 1.25 and CI_lo > 1.  DOWN: rho <= 0.8 and CI_hi < 1.  FLAT:
  CI inside [0.8, 1.25].  UNRESOLVED: otherwise.  Non-informative cells get no label.
  Point (s, mode), over its four 25-y cells: UP / DOWN / FLAT if every informative cell has that label; MIXED if the
  informative cells differ or any is UNRESOLVED; non-informative if none is informative.
  Band (the band: reading (iv), Rd-1: D2_iw vs R, S*, 25-y cells), exhaustive and exclusive:
    DAY      at least one informative point, every informative point UP.
    CRITIC   at least one informative point, every informative point DOWN.
    NULL     at least one informative point, every informative point FLAT (ascertainment immaterial both ways).
    MIXED    at least one informative point, none of the three above.
    NO-INFO  no informative point.  (Not reachable if V-rep passes: L5's D2 alone gives E >= 167 at s >= 0.05.)
  What the band fills: row (iv) of the C1a Readings table (L-R8): DAY -> (iv) supported; CRITIC -> (iv) contradicted;
  NULL -> (iv) "immaterial both ways"; MIXED -> (iv) contested, with the sign map by mode and s; NO-INFO -> (iv) not
  computable.  rho with its interval is recorded in every case.
  Field moves (proposals for the operator and the lead; this script and its author apply none).  L-R8 makes reading
  (i) governing for the "not obscure" clause and gives it Day's sign; it does not rule which comparator governs the
  "favor detecting" clause.  So:
    DAY      (iv) agrees with (i) and (ii): propose C1a external contested -> supported (scoped: selection-driven
             completions on Day's zero-reported statistic, actual panel design; the >= 90% neutral caveat of R4 C1 stays
             in the comment); C1 external supported -> contested (point 2's direction).
    CRITIC   (iv) disagrees with (i): the field becomes reading-dependent between (i) (absolute) and (iv) (relative to an
             unascertained SNP panel), and which governs the "favor" clause is the lead's to rule (D-24).  This check
             proposes (iv) for that clause (it is the comparator the claim's word "favor" needs: a bias favours relative
             to an unbiased choice of the same kind of object), i.e. C1a external contested -> contradicted (scoped),
             with (i) recorded beside it; C1 stays supported (comment adds the sign).
    NULL, MIXED, NO-INFO   no field move is proposed by this check; the claim comment records row (iv).
  Sensitivity rule: the band is recomputed for (a) D3_iw vs R, (b) the two 20-y cells (const1e4, Gravel), (c) D2_iw vs
  R+, (d) the SFS-tail bracket rho / b, b = H_1999 / H_19999 = 0.780 (the scaled neutral model, N_s = 1000, truncates
  frequencies below 1/2000; the true spectrum at 2N = 2e4 has 1/b more segregating sites per bp, nearly all
  ultra-rare and carrying almost no S* events, which lowers cR and R's hitchhiker yield by b; Day-favourable), (e) the
  two-point bracket D2_tp vs R_tp (section 6; Day-favourable for monomorphy statistics).  If the band is DAY
  or CRITIC and any of (a)-(e) gives a different band, the band is reported SENSITIVE and moves no verdict.
  Escalation clause (brief): if the band is DAY or CRITIC and not SENSITIVE, a proposal would take C1a off
  `contested`: the check becomes load-bearing and takes three reviews, and a CRITIC band also needs the lead's ruling
  on the governing comparator before integration.  Report it; do not apply the move.
  Rd-2 (D_EU) and the reading-(ii) cross-check are reported under rule RD and move no field.  C external: this check
  licenses no move (C's field is being settled under L5: lead ruling 35b196a, fix pass and owner question pending).

6. BRACKETS AND WHAT THIS DESIGN DOES NOT REACH
  Two-point hitchhiking bracket (the brief's "Z50 / Z10 understatement at s >= 0.05").  L5's formula gives every sweep
  the mean non-founder share; the post hoc V3 runs found the real share heavy-tailed (43-90% of sweeps exactly 0), so
  modern monomorphy is understated by 500-10,000x at tight linkage.  The bracket replaces the mean by the extreme
  two-point law with the same mean at each time: a linked chromosome is either fully escaped (frequency p) or fully
  founder-linked, coupled across 7,500 BP, 6,500 BP and the present by one uniform draw (escape by time t iff U < E(t),
  E increasing in t).  Since modern monomorphy f0^(2m) is convex in the non-founder share, this is an upper bound on its
  expectation given the formula's mean; for the joint statistics it is a Day-favourable bracket, not a proven bound.
  It sizes nothing; it bounds the direction.  In the two-point passes SNPs whose Z50 / Z10 / B10 value is provably
  below 1e-12 (Hoeffding: P(Neolithic q < 0.5) <= exp(-200 (f_min - 0.5)^2) for >= 100 Neolithic chromosomes; P(modern
  > 90%) <= exp(-400 (0.9 - f0)^2) for >= 200 modern chromosomes; mirror terms) are set to 0 without simulation
  (V-bnd), times the regime probability and the largest weight.
  Not reached: sweep independence at F = 15,556 (needs a multi-sweep genome simulation; rho is a per-completion ratio,
  and interference acts on both panels' hitchhikers alike to first order, but not on R's focal sites, so its effect on
  rho is unknown in direction); the mainstream s mapping (rho does not depend on F, only on s: it is reported per s);
  D3's partial status in L5 (here D3 is evaluated by importance weights on the comparator's own SNPs, so the L5 caveat
  that D3 reuses D2's hitchhikers does not apply to D3_iw); background selection, admixture, migration, genotype error,
  capture heterogeneity (as L5).  A hitchhiker's own START-time polymorphism under a sweep already running at 10,500 BP
  is not modelled for R (weight 1), the same approximation L5 makes for D2 in standing mode.

7. SEEDS, OUTPUTS, RESOURCES, DISCLOSURES
  Seeds: L5's streams unchanged (neutral sample [20261011, 5, 0, gy]; task k [.., 5, 1, k, pass]); comparator sweep
  pass [.., 5, 21, k, pass]; comparator neutral [.., 5, 20, k]; selfcheck [.., 5, 28, ..]; bootstrap [.., 5, 29, cell].
  Tasks: L5's 90 (6 neutral + 84 sweep), same indices k.  Outputs: <outdir>/c1a_<L5 task name>.json (L5 part + comparator
  sums + T1 + meta) and .npz (per-sweep float32 arrays for S* candidates x {R, R+, D2, D3, EU, R_tp, D2_tp}).
  Cost (measured, not guessed): L5 alone took 4.66 CPU-h (sum of task walls, R4-L5 s1).  Smoke sizes shrink the number
  of sweeps but not the hitchhiker SNPs per sweep, so per-SNP cost is measured as at full size: on the workstation the
  comparator took 1.55-1.6x the L5 part's time on hitchhiker-heavy tasks (hard s = 0.05: 3.9 s vs 2.5 s, 2.7e5 SNPs;
  hard s = 0.1: 20.0 vs 12.5 s, 1.3e6 SNPs; standing s = 0.05: 22.2 vs 14.3 s, 1.6e6 SNPs) and 0.25-0.6x on
  low-s tasks dominated by the forward simulation.  Estimate: at most 4.66 x 2.6 = 12 CPU-h; longest task at most
  ~1,978 s x 2.6 = 1.4 h; with 7 workers about 2-2.5 h wall.  Peak RSS of one process at smoke sizes 437 MB with
  1.6e6 hitchhiker SNPs (chunks capped at 5e5 SNPs).  The host smoke records the children's peak RSS; if it exceeds
  1.5 GB, workers = floor(11 GB / peak).
  Workers: 7 (L5 peak ~1 GB per worker), and only while the host's busy processes across all agents stay <= 11 and RAM
  < ~12 GB.
  Launch (after the `ph2` collect task is done; `uptime` and `free -g` first):
    rsync -a research/checks/l5_c1a_randsnp.py research/checks/l5_adna_power.py research/checks/c1c_call_depth_replacement.py \
          research/checks/c1e_holocene_trajectories.py na-workhorse:projects/evo-sim/research/checks/
    rsync -a research/checks/results/c1c_depth_table.json na-workhorse:projects/evo-sim/research/checks/results/
    rsync -a research/checks/results/raw/l5 na-workhorse:projects/evo-sim/research/checks/results/raw/
    # host smoke (real pool, every grid value, tiny sizes; prints timing/structure only) and full-size cost probe:
    ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && research/.venv/bin/python -I \
         research/checks/l5_c1a_randsnp.py hostsmoke 4 /tmp/c1a_hostsmoke > research/checks/results/raw/l5c1a_hostsmoke.out 2>&1'
    ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && mkdir -p research/checks/results/raw/l5c1a && \
         (hostname; date -u; md5sum research/checks/l5_c1a_randsnp.py research/checks/l5_adna_power.py \
          research/checks/c1c_call_depth_replacement.py research/checks/c1e_holocene_trajectories.py \
          research/checks/results/c1c_depth_table.json) > research/checks/results/raw/l5c1a.host && \
         nohup research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py main 7 research/checks/results/raw/l5c1a \
          > research/checks/results/raw/l5c1a.out 2>&1 < /dev/null &'
  Collect (once, when the measured cost says it is done):
    rsync -a na-workhorse:projects/evo-sim/research/checks/results/raw/l5c1a \
          na-workhorse:projects/evo-sim/research/checks/results/raw/l5c1a.out \
          na-workhorse:projects/evo-sim/research/checks/results/raw/l5c1a.host \
          na-workhorse:projects/evo-sim/research/checks/results/raw/l5c1a_hostsmoke.out research/checks/results/raw/
    research/.venv/bin/python -I research/checks/l5_c1a_randsnp.py analyse research/checks/results/raw/l5c1a \
          > research/checks/results/raw/l5c1a_analysis.txt
  Never commit or push from workhorse.
  Disclosed before the main run: the design read L5's committed outputs (R4-L5.md, raw/l5/*.json, l5_analysis.txt) to
  learn which statistic rule C picks (B10 blog everywhere informative) and the per-cell D2 magnitudes; no comparator
  number existed or was computed.  The local smoke (workstation, one process, tiny sizes) printed timings, task
  structure and exit statuses only; analyse was run on the smoke output with stdout discarded (smoke mode: the files'
  own L5 part as reference, partial task set; it tests the code path, not V-rep).  The smoke was run during
  development, before this commit (a first version picked three hitchhiker-heavy tasks and overran the workstation's
  one-minute limit at 120 s; the pick was cut to neutral + hard 0.05 + hard 0.003 + standing 0.003, 15 s, 276 MB);
  it is rerun unchanged on the committed file and its output committed separately.  `selfcheck` printed two model
  constants at smoke sizes (K_anc = 20,000): cR = 0.0936, phi = 0.924.  A1 was written before they were seen and is
  unchanged, but A1 is therefore not blind.  V-id (copied run_pass identical to L5's, both modes) and V-bnd (0
  violations on 11,985 test SNPs with bound < 1e-6) passed.
"""
import os
import sys
import json
import time
import math

os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import numpy as np
import l5_adna_power as l5
from l5_adna_power import (ROOT_SEED, TAG, NPANEL, L_GENOME, MAP_M, THETA, NE_ANC, T_SPLIT_G, F_DAY, DEMOGS, DESIGNS,
                           STATS, SIZES, SMOKE_SIZES, MODES, S_GRID, X0_KEEP, sel, kimura, times, two_n_europe, p3,
                           design_params, event_probs)

# label assertions: the L5 layout this script depends on (FMnull lesson: never assume another check's keys)
assert l5.COLS == ["xE", "xA", "IE", "IA", "x7", "x6", "I7", "I6", "fixT", "a0"], l5.COLS
assert l5.STATS == ["Z50", "Z10", "M10", "N100", "B10"] and list(l5.DESIGNS) == ["v62", "v66", "blog"]
assert l5.S_GRID == [1e-3, 3e-3, 1e-2, 2e-2, 3e-2, 5e-2, 1e-1] and l5.MODES == ["hard", "standing"]
assert [d[0] for d in l5.DEMOGS] == ["const1e4", "Gravel", "Gazave", "Nelson", "const1e4_gy20", "Gravel_gy20"]

COLS_C = l5.COLS + ["xS"]
CC = {k: i for i, k in enumerate(COLS_C)}
NL5 = len(l5.COLS)
NS_SCALED = 1000                       # l5.neutral_sample's N_s (M = 2000 chromosomes)
B_TAIL = float(np.sum(1.0 / np.arange(1, 2 * NS_SCALED)) / np.sum(1.0 / np.arange(1, int(2 * NE_ANC))))   # 0.780
UNIFORM = NPANEL / L_GENOME
SSTAR_CANDS = [("v62", "Z50"), ("v66", "Z50"), ("blog", "B10")]
TP_STATS = ["Z50", "Z10", "B10"]
EST_F = ["R", "Rp", "D2", "D3", "EU", "Rsfs"]          # formula estimators
EST_TP = ["R_tp", "D2_tp"]                             # two-point bracket estimators
NPZ_EST = ["R", "Rp", "D2", "D3", "EU", "R_tp", "D2_tp"]
PRUNE = 1e-12
CHUNK = 500_000
N_BOOT = 2000
LAB_UP, LAB_DOWN, LAB_FLAT, LAB_UNRES = "UP", "DOWN", "FLAT", "UNRESOLVED"


# ------------------------------------------------------------------------------------------------ comparator constants
def comp_consts(ns, sz):
    """R's reference set = sites segregating in Europe at START_BP (ns['ce'], ns['ca'], weights ns['cw']).
    Absolute weight sum recovered from cw: cw = W / sum_seg W, W in {W_anc, W_new} (l5.neutral_sample)."""
    M = 2 * NS_SCALED
    H = float(np.sum(1.0 / np.arange(1, M)))
    W_anc, W_new = THETA * H / sz["K_anc"], THETA / 2 / sz["K_new"]
    u = np.unique(ns["cw"])
    assert u.size == 2, "cw should take exactly two values (ancient, new): %r" % (u[:5],)
    lo, hi = u.min(), u.max()
    ratio = W_anc / W_new
    if abs(hi / lo - ratio) / ratio < 1e-9:
        cw_anc = hi
    elif abs(lo / hi - ratio) / ratio < 1e-9:
        cw_anc = lo
    else:
        raise AssertionError("cw ratio %g does not match W_anc/W_new %g" % (hi / lo, ratio))
    sum_seg_w = W_anc / cw_anc                       # segregating sites per bp
    cR = NPANEL / (L_GENOME * sum_seg_w)
    ce, ca, cw = ns["ce"], ns["ca"], ns["cw"]
    phi = float(ns["c2"] / cR * np.sum(cw * 2 * ca * (1 - ca)))
    # R_sfs: E[2a(1-a) | e] in 50 equal-weight bins of e
    o = np.argsort(ce, kind="stable")
    cum = np.cumsum(cw[o])
    edges = [0.0]
    for qq in np.linspace(0.02, 0.98, 49):
        edges.append(float(ce[o][np.searchsorted(cum, qq * cum[-1])]))
    edges = np.unique(np.array(edges + [1.0 + 1e-12]))
    b = np.clip(np.searchsorted(edges, ce, side="right") - 1, 0, edges.size - 2)
    num = np.bincount(b, cw * 2 * ca * (1 - ca), minlength=edges.size - 1)
    den = np.bincount(b, cw, minlength=edges.size - 1)
    g2 = np.where(den > 0, num / np.maximum(den, 1e-300), 0.0)
    return dict(cR=float(cR), sum_seg_w=float(sum_seg_w), phi=phi, c2=float(ns["c2"]), c3=float(ns["c3"]),
                cdf=np.cumsum(cw) / np.sum(cw), ce=ce, ca=ca, edges=edges, g2=g2)


def g2_of(cx, e):
    e = np.asarray(e, float)
    b = np.clip(np.searchsorted(cx["edges"], np.nan_to_num(e), side="right") - 1, 0, cx["g2"].size - 1)
    return cx["g2"][b]


def draw_R(cx, n, rng):
    return np.minimum(np.searchsorted(cx["cdf"], rng.random(n), side="right"), cx["ce"].size - 1)


_CX = {}


def get_cx(gy, sz):
    if gy not in _CX:
        _CX[gy] = comp_consts(l5.get_ns(gy, sz), sz)
    return _CX[gy]


# ------------------------------------------------------------------------------------------------ sweep engine (copy + xS)
class PoolC:
    def __init__(self, cap=1 << 15):
        self.A = np.zeros((len(COLS_C), cap))
        self.n = 0

    def add(self, block):
        k = block.shape[1]
        if self.n + k > self.A.shape[1]:
            B = np.zeros((len(COLS_C), max(2 * self.A.shape[1], self.n + k)))
            B[:, :self.n] = self.A[:, :self.n]
            self.A = B
        self.A[:, self.n:self.n + k] = block
        self.n += k

    def v(self):
        return self.A[:, :self.n]

    def compact(self, keep):
        w = self.A[:, :self.n][:, keep]
        self.A[:, :w.shape[1]] = w
        self.n = w.shape[1]


def run_pass_c(s, mode, twoN, T_hi, n_per_gen, gy, ns, rng):
    """l5.run_pass, line for line, plus column xS (European frequency at START_BP; NaN for hard-mode origins after it;
    the START_BP frequency ke for standing onsets after it, as L5 enters them).  No extra random numbers."""
    tm = times(gy)
    P = PoolC()
    entries = 0
    CI = CC
    for t in range(T_hi, -1, -1):
        if n_per_gen > 0:
            blk = np.zeros((len(COLS_C), n_per_gen))
            if mode == "hard":
                if t > T_SPLIT_G:
                    blk[CI["xE"]] = 1.0 / (2 * NE_ANC)
                    blk[CI["xA"]] = np.nan
                else:
                    blk[CI["xE"]] = 1.0 / twoN[t]
                    blk[CI["xA"]] = 0.0
                blk[CI["a0"]] = np.nan
                blk[CI["xS"]] = np.nan
            else:
                ix = rng.integers(0, ns["ke"].size, n_per_gen)
                blk[CI["xE"]] = ns["ke"][ix]
                blk[CI["xA"]] = ns["ka"][ix]
                blk[CI["a0"]] = ns["ka"][ix]
                blk[CI["IE"]] = ns["kI"][ix]
                blk[CI["xS"]] = ns["ke"][ix]
            blk[CI["x7"]] = blk[CI["xE"]]
            blk[CI["x6"]] = blk[CI["xE"]]
            blk[CI["I7"]] = blk[CI["IE"]]
            blk[CI["I6"]] = blk[CI["IE"]]
            blk[CI["fixT"]] = -1.0
            P.add(blk)
            entries += n_per_gen
        V = P.v()
        if t == tm["start"]:
            V[CI["xS"]] = V[CI["xE"]]
        if t == tm["t7"]:
            V[CI["x7"]] = V[CI["xE"]]
            V[CI["I7"]] = V[CI["IE"]]
        if t == tm["t6"]:
            V[CI["x6"]] = V[CI["xE"]]
            V[CI["I6"]] = V[CI["IE"]]
        if t == 0:
            break
        N2 = twoN[t - 1]
        V[CI["xE"]] = rng.binomial(N2, sel(V[CI["xE"]], s)) / N2
        V[CI["IE"]] += 1.0 - V[CI["xE"]]
        if mode == "hard" and t - 1 < T_SPLIT_G:
            if t - 1 == T_SPLIT_G - 1:
                pre = np.isnan(V[CI["xA"]])
                V[CI["xA"], pre] = V[CI["xE"], pre]
                V[CI["IA"], pre] = V[CI["IE"], pre]
            nA = int(2 * l5.NE_AFR)
            V[CI["xA"]] = rng.binomial(nA, sel(V[CI["xA"]], s)) / nA
            V[CI["IA"]] += 1.0 - V[CI["xA"]]
        nf = (V[CI["xE"]] >= 1.0) & (V[CI["fixT"]] < 0)
        V[CI["fixT"], nf] = t - 1
        if (t % 16 == 0) or t - 1 in (tm["t7"], tm["t6"], 0):
            keep = (V[CI["xE"]] > 0) & ~(V[CI["fixT"]] > tm["t7"])
            P.compact(keep)
    V = P.v()
    keep = (V[CI["xE"]] > 0) & ~(V[CI["fixT"]] > tm["t7"])
    V = V[:, keep]
    wc = (V[CI["fixT"]] >= 0) & (V[CI["fixT"]] <= tm["win"])
    kept = V[:, V[CI["xE"]] >= X0_KEEP]
    return dict(V=kept, n_wc=int(wc.sum()), entries=entries,
                wc_x7_lt50=int(((V[CI["x7"]] < 0.5) & wc).sum()),
                wc_a=(V[CI["xA"]][wc] if mode == "hard" else V[CI["a0"]][wc]),
                wc_xS=V[CI["xS"]][wc])


# ------------------------------------------------------------------------------------------------ comparator events
def ev_bound(f7, f6, f0):
    """Upper bound on each of Z50, Z10, B10 for one SNP (Hoeffding; >= 100 Neolithic and >= 200 modern chromosomes
    whenever L5's 'ok' filter admits the SNP; otherwise the value is 0)."""
    fmin, fmax = np.minimum(f7, f6), np.maximum(f7, f6)
    a_hi = np.where(fmin > 0.5, np.exp(-200.0 * (fmin - 0.5) ** 2), 1.0)
    a_lo = np.where(fmax < 0.5, np.exp(-200.0 * (0.5 - fmax) ** 2), 1.0)
    g90 = np.where(f0 < 0.9, np.exp(-400.0 * (0.9 - f0) ** 2), 1.0)
    l10 = np.where(f0 > 0.1, np.exp(-400.0 * (f0 - 0.1) ** 2), 1.0)
    return g90 * a_hi + l10 * a_lo


def comp_events(V, mode, ns, cx, rng, max_snps=CHUNK):
    """Per-sweep expected events on every panel, from hitchhiking SNPs drawn from R's reference set (importance
    weights relative to R) plus the focal site.  Returns per-sweep arrays acc[(est, dn, k)] split hh / focal."""
    nsw = V.shape[1]
    g = lambda c: V[CC[c]]
    x7, x6, x0 = g("x7"), g("x6"), g("xE")
    I7, I6, I0 = g("I7"), g("I6"), g("IE")
    aN = np.nan_to_num(g("xA") if mode == "hard" else g("a0"))
    IA, xS = g("IA"), g("xS")
    cR, c2, c3 = cx["cR"], cx["c2"], cx["c3"]
    lam = NPANEL / MAP_M
    rmax = np.minimum(0.5, 8.0 / np.maximum(I0, 1.0))
    nh = rng.poisson(lam * 2 * rmax)
    dps = {dn: design_params(dn) for dn in DESIGNS}
    hh = {}
    for dn in DESIGNS:
        for k in STATS:
            for e in EST_F:
                hh[(e, dn, k)] = np.zeros(nsw)
        for k in TP_STATS:
            for e in EST_TP:
                hh[(e, dn, k)] = np.zeros(nsw)
    bounds, cur, acc = [], 0, 0
    for jsw in range(nsw):
        acc += int(nh[jsw])
        if acc >= max_snps:
            bounds.append((cur, jsw + 1))
            cur, acc = jsw + 1, 0
    if cur < nsw:
        bounds.append((cur, nsw))
    nsnp, n_tp_eval = 0, 0
    wmax = c2 * 0.5 / cR
    for lo, hi in bounds:
        sid = np.repeat(np.arange(lo, hi), nh[lo:hi])
        if sid.size == 0:
            continue
        nsnp += sid.size
        r = rng.random(sid.size) * rmax[sid]
        j = draw_R(cx, sid.size, rng)
        p, ap = cx["ce"][j], cx["ca"][j]
        beta = (rng.random(sid.size) < p).astype(float)
        E7, E6, E0 = (-np.expm1(-r * Ik[sid]) for Ik in (I7, I6, I0))
        c7, c6, c0 = (xk[sid] * beta + (1 - xk[sid]) * p for xk in (x7, x6, x0))
        f7, f6, f0 = (1 - E7) * c7 + E7 * p, (1 - E6) * c6 + E6 * p, (1 - E0) * c0 + E0 * p
        if mode == "hard":
            EA = -np.expm1(-r * IA[sid])
            ah = aN[sid] * ((1 - EA) * beta + EA * ap) + (1 - aN[sid]) * ap
        else:
            ah = ap
        W = {"R": np.ones(sid.size), "Rp": np.ones(sid.size), "D2": c2 * 2 * ah * (1 - ah) / cR,
             "D3": c3 * p3(ah) / cR, "EU": 2 * f0 * (1 - f0), "Rsfs": c2 * g2_of(cx, p) / cR}
        regimes = []
        for pr, a7, a6, a0 in ((E7, p, p, p), (E6 - E7, c7, p, p), (E0 - E6, c7, c6, p), (1 - E0, c7, c6, c0)):
            pr = np.maximum(pr, 0.0)
            ix = np.flatnonzero(pr * ev_bound(a7, a6, a0) * max(1.0, wmax) >= PRUNE)
            regimes.append((pr, a7, a6, a0, ix))
        for dn in DESIGNS:
            sc = dps[dn]["npanel"] / NPANEL
            ev = event_probs(f7, f6, f0, dps[dn], rng)
            for k in STATS:
                for e in EST_F:
                    hh[(e, dn, k)] += np.bincount(sid, W[e] * ev[k] * sc, minlength=nsw)
            for pr, a7, a6, a0, ix in regimes:
                if ix.size == 0:
                    continue
                n_tp_eval += ix.size
                evr = event_probs(a7[ix], a6[ix], a0[ix], dps[dn], rng)
                for k in TP_STATS:
                    hh[("R_tp", dn, k)] += np.bincount(sid[ix], pr[ix] * evr[k] * sc, minlength=nsw)
                    hh[("D2_tp", dn, k)] += np.bincount(sid[ix], pr[ix] * W["D2"][ix] * evr[k] * sc, minlength=nsw)
    inR = (xS > 0) & (xS < 1)
    inRp = inR | np.isnan(xS)
    WF = {"R": cR * inR, "Rp": cR * inRp, "D2": c2 * 2 * aN * (1 - aN), "D3": c3 * p3(aN),
          "EU": cR * 2 * x0 * (1 - x0), "Rsfs": c2 * g2_of(cx, xS) * inR, "R_tp": cR * inR,
          "D2_tp": c2 * 2 * aN * (1 - aN)}
    foc = {}
    for dn in DESIGNS:
        evf = event_probs(x7, x6, x0, dps[dn], rng)
        for k in STATS:
            for e in EST_F:
                foc[(e, dn, k)] = WF[e] * evf[k]
        for k in TP_STATS:
            for e in EST_TP:
                foc[(e, dn, k)] = WF[e] * evf[k]
    return hh, foc, int(nsnp), int(n_tp_eval), int(inR.sum()), int(inRp.sum())


# ------------------------------------------------------------------------------------------------ neutral arm
def neutral_comp(demog, ns, cx, sz, rng):
    name, fn, gy = demog
    tm = times(gy)
    twoN = two_n_europe(fn, gy, tm["start"])
    K = sz["K_panel"]
    j = draw_R(cx, K, rng)
    x, a, e0 = cx["ce"][j].copy(), cx["ca"][j], cx["ce"][j]
    rec = {}
    for t in range(tm["start"], -1, -1):
        if t == tm["t7"]:
            rec[7] = x.copy()
        if t == tm["t6"]:
            rec[6] = x.copy()
        if t == 0:
            break
        x = rng.binomial(twoN[t - 1], x) / twoN[t - 1]
    H_EU = float(np.mean(2 * x * (1 - x)))
    W = {"R": np.ones(K), "D2": cx["c2"] * 2 * a * (1 - a) / cx["cR"], "D3": cx["c3"] * p3(a) / cx["cR"],
         "EU": 2 * x * (1 - x) / max(H_EU, 1e-300), "Rsfs": cx["c2"] * g2_of(cx, e0) / cx["cR"]}
    out = {}
    for dn in DESIGNS:
        dp = design_params(dn)
        ev = event_probs(rec[7], rec[6], x, dp, rng)
        sc = dp["npanel"] / K
        out[dn] = {e: {k: float(np.sum(W[e] * ev[k]) * sc) for k in STATS} for e in W}
    return dict(E=out, H_EU=H_EU, present_seg_share=float(np.mean((x > 0) & (x < 1))))


# ------------------------------------------------------------------------------------------------ tasks
def sweep_task_c(s, mode, demog, ns, cx, seed_key, sz):
    """l5.sweep_task's loop unchanged (same seeds, same pass logic); comparator after each pass on its own stream."""
    name, fn, gy = demog
    tm = times(gy)
    tfix = 4.0 * math.log(max(NE_ANC * s, 2.0)) / s
    T_hi = int(tm["win"] + 3 * tfix)
    if mode == "standing":
        T_hi = min(T_SPLIT_G, T_hi)
        pf = float(np.sum(ns["cw"] * kimura(ns["ce"], s, NE_ANC)))
    else:
        pf = s
    twoN = two_n_europe(fn, gy, max(T_hi, T_SPLIT_G) + 1)
    B = float(np.clip(sz["N_TARGET"] * T_hi / (pf * tm["win"] * 0.8), 1e4, sz["B_CAP"]))
    acc, n_wc, entries, x7lt, nsnp, nkept, passes = {}, 0, 0, 0, 0, 0, 0
    wa, wxs = [], []
    per_hh, per_f = {}, {}
    c_nsnp, c_tp, c_inR, c_inRp = 0, 0, 0, 0
    t0 = time.time()
    t_l5, t_c = 0.0, 0.0
    while passes < sz["MAXPASS"]:
        rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 1, seed_key, passes]))
        npg = max(1, int(math.ceil(B / (T_hi + 1))))
        ta = time.time()
        r = run_pass_c(s, mode, twoN, T_hi, npg, gy, ns, rng)
        ev, ns_snp = l5.sweep_events(np.ascontiguousarray(r["V"][:NL5]), mode, ns, rng)
        t_l5 += time.time() - ta
        l5.add_into(acc, ev)
        tb = time.time()
        rng_c = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 21, seed_key, passes]))
        hh, foc, a1, a2, a3, a4 = comp_events(r["V"], mode, ns, cx, rng_c)
        t_c += time.time() - tb
        for kk in hh:
            per_hh.setdefault(kk, []).append(hh[kk])
            per_f.setdefault(kk, []).append(foc[kk])
        c_nsnp += a1
        c_tp += a2
        c_inR += a3
        c_inRp += a4
        n_wc += r["n_wc"]
        entries += r["entries"]
        x7lt += r["wc_x7_lt50"]
        nsnp += ns_snp
        nkept += r["V"].shape[1]
        wa.append(r["wc_a"])
        wxs.append(r["wc_xS"])
        passes += 1
        if n_wc >= sz["N_MIN"] or entries >= sz["B_CAP"]:
            break
        B = min(sz["B_CAP"] - entries, B * min(10.0, sz["N_TARGET"] / max(n_wc, 1)))
        if B < 1:
            break
    wa = np.nan_to_num(np.concatenate(wa) if wa else np.empty(0))
    wxs = np.concatenate(wxs) if wxs else np.empty(0)
    per_hh = {kk: np.concatenate(v) for kk, v in per_hh.items()}
    per_f = {kk: np.concatenate(v) for kk, v in per_f.items()}
    comp = {}
    for (e, dn, k) in per_hh:
        comp.setdefault(e, {}).setdefault(dn, {})[k] = dict(E_hh=float(per_hh[(e, dn, k)].sum()),
                                                           E_f=float(per_f[(e, dn, k)].sum()))
    cR = cx["cR"]
    inR_wc = (wxs > 0) & (wxs < 1)
    T1 = dict(D2=float(np.sum(ns["c2"] * 2 * wa * (1 - wa))), D3=float(np.sum(ns["c3"] * p3(wa))),
              R=float(cR * inR_wc.sum()), Rp=float(cR * (inR_wc | np.isnan(wxs)).sum()), EU=0.0,
              n_wc_after_start=int(np.isnan(wxs).sum()))
    meta = dict(s=s, mode=mode, demog=name, gy=gy, T_hi=T_hi, entries=entries, passes=passes, n_wc=n_wc,
                wc_x7_lt50=x7lt, n_kept=nkept, n_hh_snps=nsnp, secs=round(time.time() - t0, 1),
                c2=ns["c2"], c3=ns["c3"], uniform_share=NPANEL / L_GENOME,
                focal_incl_D2=float(np.sum(ns["c2"] * 2 * wa * (1 - wa))),
                focal_incl_D3=float(np.sum(ns["c3"] * p3(wa))),
                cR=cR, phi=cx["phi"], comp_hh_snps=c_nsnp, comp_tp_evals=c_tp, kept_inR=c_inR, kept_inRp=c_inRp,
                secs_l5=round(t_l5, 1), secs_comp=round(t_c, 1))
    arrays = {}
    for e in NPZ_EST:
        for dn, k in SSTAR_CANDS:
            arrays["%s|%s|%s" % (e, dn, k)] = (per_hh[(e, dn, k)] + per_f[(e, dn, k)]).astype(np.float32)
    return dict(meta=meta, sums=acc, comp=comp, T1=T1), arrays


def task_name_c(tk):
    return "c1a_" + l5.task_name(tk)


def run_task_c_k(a):
    k, outdir, sz = a
    tk = l5.task_list()[k]
    kind, s, mode, d = tk
    fn = os.path.join(outdir, task_name_c(tk) + ".json")
    if os.path.exists(fn):
        return fn
    t0 = time.time()
    ns = l5.get_ns(d[2], sz)
    cx = get_cx(d[2], sz)
    arrays = None
    if kind == "neutral":
        rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 1, k, 0]))
        res = dict(meta=dict(demog=d[0], gy=d[2], c2=ns["c2"], c3=ns["c3"]), neutral=l5.neutral_task(d, ns, rng))
        rng_c = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 20, k]))
        res["comp_neutral"] = neutral_comp(d, ns, cx, sz, rng_c)
        res["meta"].update(cR=cx["cR"], phi=cx["phi"], sum_seg_w=cx["sum_seg_w"], b_tail=B_TAIL)
    else:
        res, arrays = sweep_task_c(s, mode, d, ns, cx, k, sz)
    res["meta"]["task"] = l5.task_name(tk)
    res["meta"]["k"] = k
    res["meta"]["wall"] = round(time.time() - t0, 1)
    if arrays is not None:
        np.savez_compressed(fn[:-5] + ".tmp.npz", **arrays)
        os.replace(fn[:-5] + ".tmp.npz", fn[:-5] + ".npz")
    with open(fn + ".tmp", "w") as f:
        json.dump(res, f)
    os.replace(fn + ".tmp", fn)
    print("done %s %.0fs" % (task_name_c(tk), time.time() - t0), flush=True)
    return fn


def jobs_for(outdir, sz):
    tl = l5.task_list()
    return [(k, outdir, sz) for k, tk in sorted(enumerate(tl), key=lambda a: -l5.cost(a[1]))]


# ------------------------------------------------------------------------------------------------ selfcheck
def selfcheck():
    import pickle
    ok = True
    sz = SMOKE_SIZES
    ns = l5.get_ns(25, sz)
    cx = get_cx(25, sz)
    print("selfcheck: cR=%.4g phi=%.3g sum_seg_w=%.4g b_tail=%.4f (model constants, not results)"
          % (cx["cR"], cx["phi"], cx["sum_seg_w"], B_TAIL), flush=True)
    # V-id: copied run_pass == L5 run_pass, both modes
    d = DEMOGS[0]
    tm = times(d[2])
    for mode, s in (("hard", 0.05), ("standing", 0.05), ("hard", 0.003)):
        T_hi = int(tm["win"] + 3 * 4.0 * math.log(max(NE_ANC * s, 2.0)) / s)
        if mode == "standing":
            T_hi = min(T_SPLIT_G, T_hi)
        twoN = two_n_europe(d[1], d[2], max(T_hi, T_SPLIT_G) + 1)
        sd = np.random.SeedSequence([ROOT_SEED, TAG, 28, int(s * 1e4), mode == "hard"])
        a = l5.run_pass(s, mode, twoN, T_hi, 3, d[2], ns, np.random.default_rng(sd))
        b = run_pass_c(s, mode, twoN, T_hi, 3, d[2], ns, np.random.default_rng(sd))
        same = (np.array_equal(a["V"], b["V"][:NL5], equal_nan=True) and a["n_wc"] == b["n_wc"]
                and a["entries"] == b["entries"] and a["wc_x7_lt50"] == b["wc_x7_lt50"]
                and np.array_equal(a["wc_a"], b["wc_a"], equal_nan=True))
        print("V-id %s s=%g: %s (kept %d, n_wc %d)" % (mode, s, "ok" if same else "FAIL", a["V"].shape[1], a["n_wc"]),
              flush=True)
        ok &= bool(same)
    # V-bnd: bound >= L5 event values on random SNPs (exact modern part, MC Neolithic, many draws)
    rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 28, 99]))
    n = 20_000
    f7 = rng.random(n) ** rng.choice([0.3, 1, 3], n)
    f6 = np.clip(f7 + rng.normal(0, 0.05, n), 0, 1)
    f0 = np.where(rng.random(n) < 0.5, np.clip(f7 + rng.normal(0, 0.3, n), 0, 1), rng.random(n) ** 0.2)
    U = ev_bound(f7, f6, f0)
    viol, nsmall = 0, int(np.sum(U < 1e-6))
    for dn in DESIGNS:
        ev = event_probs(f7, f6, f0, design_params(dn), rng)
        for k in TP_STATS:
            # the bound is on the expectation; a 32-draw MC value can exceed a moderate bound by chance, so the test is
            # where pruning acts (U < 1e-6): there any MC hit or exact-term excess is a violation
            viol += int(np.sum((U < 1e-6) & (ev[k] > U)))
    print("V-bnd violations where bound < 1e-6: %d (%d SNP x 9 stat-designs tested, %d SNPs with bound < 1e-6)"
          % (viol, n, nsmall), flush=True)
    ok &= viol == 0 and nsmall > 1000
    # pickling of real jobs (the L5 launch-1 bug)
    try:
        pickle.dumps(jobs_for("/tmp/x", SIZES))
        print("pickle jobs: ok", flush=True)
    except Exception as ex:
        print("pickle jobs: FAIL", ex, flush=True)
        ok = False
    print("SELFCHECK", "OK" if ok else "FAIL", flush=True)
    return ok


# ------------------------------------------------------------------------------------------------ analyse
def _boot_ratio(num, den, seed_key, B=N_BOOT):
    rng = np.random.default_rng(np.random.SeedSequence([ROOT_SEED, TAG, 29, seed_key]))
    n = num.size
    rs = []
    for _ in range(B // 200):
        idx = rng.integers(0, n, size=(200, n))
        a, b = num[idx].sum(1, dtype=np.float64), den[idx].sum(1, dtype=np.float64)
        with np.errstate(divide="ignore", invalid="ignore"):
            rs.append(np.where(b > 0, a / np.where(b > 0, b, 1), np.where(a > 0, np.inf, np.nan)))
    rs = np.concatenate(rs)
    rs = rs[~np.isnan(rs)]
    if rs.size == 0:
        return float("nan"), float("nan")
    return float(np.percentile(rs, 2.5)), float(np.percentile(rs, 97.5))


def label(rho, lo, hi):
    if not np.isfinite(lo) and not np.isfinite(hi):
        return LAB_UNRES
    if rho >= 1.25 and lo > 1:
        return LAB_UP
    if rho <= 0.8 and hi < 1:
        return LAB_DOWN
    if lo >= 0.8 and hi <= 1.25:
        return LAB_FLAT
    return LAB_UNRES


def point_label(labs):
    labs = [x for x in labs if x is not None]
    if not labs:
        return None
    if all(x == labs[0] for x in labs) and labs[0] != LAB_UNRES:
        return labs[0]
    return "MIXED"


def band_of(points):
    pl = [v for v in points.values() if v is not None]
    if not pl:
        return "NO-INFO"
    for lab, band in ((LAB_UP, "DAY"), (LAB_DOWN, "CRITIC"), (LAB_FLAT, "NULL")):
        if all(v == lab for v in pl):
            return band
    return "MIXED"


def analyse(outdir, l5dir=None, smoke=False):
    """smoke=True: code-path test on a partial smoke output; the L5 reference is the files' own L5 part."""
    l5dir = l5dir or os.path.join(HERE, "results", "raw", "l5")
    tl = l5.task_list()
    R, A = {}, {}
    for k, tk in enumerate(tl):
        fn = os.path.join(outdir, task_name_c(tk) + ".json")
        if os.path.exists(fn):
            r = json.load(open(fn))
            assert r["meta"]["task"] == l5.task_name(tk) and r["meta"]["k"] == k, (fn, r["meta"]["task"])
            if tk[0] == "sweep":
                assert (r["meta"]["s"], r["meta"]["mode"], r["meta"]["demog"], r["meta"]["gy"]) == \
                    (tk[1], tk[2], tk[3][0], tk[3][2]), fn
                A[k] = dict(np.load(fn[:-5] + ".npz"))
            R[k] = r
    print("tasks loaded: %d of %d" % (len(R), len(tl)))
    # ---------------- V-rep
    fails, ncmp = [], 0

    def close(a, b):
        return a == b or abs(a - b) <= 1e-9 * max(abs(a), abs(b), 1e-300)
    for k, r in R.items():
        tk = tl[k]
        f5 = os.path.join(l5dir, "l5_%s.json" % l5.task_name(tk))
        if smoke:
            q = r
        elif not os.path.exists(f5):
            fails.append((l5.task_name(tk), "L5 json missing"))
            continue
        else:
            q = json.load(open(f5))
        assert q["meta"]["task"] == l5.task_name(tk), f5
        if tk[0] == "neutral":
            for lab in ("D2", "D3"):
                for dn in DESIGNS:
                    for st in STATS:
                        ncmp += 1
                        if not close(r["neutral"][lab][dn][st], q["neutral"][lab][dn][st]):
                            fails.append((l5.task_name(tk), lab, dn, st))
        else:
            for f in ("n_wc", "n_kept", "n_hh_snps", "entries", "passes", "wc_x7_lt50", "focal_incl_D2",
                      "focal_incl_D3", "s", "mode", "demog", "gy"):
                ncmp += 1
                a, b = r["meta"][f], q["meta"][f]
                if not (a == b if isinstance(a, str) else close(float(a), float(b))):
                    fails.append((l5.task_name(tk), f))
            for dn in DESIGNS:
                for lab in ("D2", "D3"):
                    for st in STATS:
                        for f in ("E_hh", "E_f", "Q"):
                            ncmp += 1
                            if not close(r["sums"][dn][lab][st][f], q["sums"][dn][lab][st][f]):
                                fails.append((l5.task_name(tk), dn, lab, st, f))
    vrep = (not fails) and (len(R) == len(tl) or smoke)
    print("V-rep: %s (%d numbers compared, %d mismatches; tasks %d of %d)" %
          ("PASS" if vrep else "FAIL", ncmp, len(fails), len(R), len(tl)))
    for f in fails[:20]:
        print("   mismatch:", f)
    if not vrep:
        print("== L5 NOT REPRODUCED: no comparator result is read; no band.")
        return
    # ---------------- constants
    k0 = next(k for k, tk in enumerate(tl) if tk[0] == "neutral" and k in R)
    m0 = R[k0]["meta"]
    print("constants: cR=%.4g phi=%.3g c2=%.4g sum_seg_w=%.4g per bp; b_tail=%.4f; uniform share=%.3g"
          % (m0["cR"], m0["phi"], m0["c2"], m0["sum_seg_w"], m0["b_tail"], UNIFORM))
    H_EU = {R[k]["meta"]["demog"]: R[k]["comp_neutral"]["H_EU"] for k, tk in enumerate(tl) if tk[0] == "neutral" and k in R}
    for k, tk in enumerate(tl):
        if tk[0] == "neutral" and k in R:
            assert R[k]["meta"]["demog"] == tk[3][0]
    # ---------------- V-iw
    print("\n== V-iw: D2_iw (comparator draws) against L5's D2 (reproduced)")
    viw = True
    for k, tk in enumerate(tl):
        if tk[0] == "neutral" and k in R:
            c = R[k]["comp_neutral"]["E"]["v62"]["D2"]["N100"]
            o = R[k]["neutral"]["D2"]["v62"]["N100"]
            okk = 0.95 <= c / o <= 1.05 if o > 0 else False
            viw &= okk
            print("  neutral %-14s N100 v62: D2_iw %.4g  L5 %.4g  ratio %.3f %s" % (tk[3][0], c, o, c / o if o else
                                                                                       float("nan"), "ok" if okk else "FAIL"))
    for k, tk in enumerate(tl):
        if tk[0] == "sweep" and tk[1] >= 0.05 and tk[3][2] == 25 and k in R:
            r = R[k]
            for dn, st in SSTAR_CANDS:
                if (dn, st) != sstar(r):
                    continue
                c = r["comp"]["D2"][dn][st]
                o = r["sums"][dn]["D2"][st]
                cv, ov = c["E_hh"] + c["E_f"], o["E_hh"] + o["E_f"]
                okk = ov > 0 and 0.8 <= cv / ov <= 1.25
                viw &= okk
                print("  %-8s s=%-5g %-9s %s/%s: ratio %.3f %s" % (tk[2], tk[1], tk[3][0], dn, st,
                                                                 cv / ov if ov else float("nan"), "ok" if okk else "FAIL"))
    print("V-iw: %s" % ("PASS" if viw else "FAIL (comparator not validated: band moves nothing)"))
    # ---------------- cells
    def cell(k, num_e, den_e, cmp_id, cand=None, num_scale=1.0, den_scale=1.0):
        r = R[k]
        dn, st = cand or sstar(r)
        key = lambda e: "%s|%s|%s" % (e, dn, st)
        num = A[k][key(num_e)].astype(np.float64) * num_scale
        den = A[k][key(den_e)].astype(np.float64) * den_scale
        n = r["meta"]["n_wc"]
        Sn, Sd = float(num.sum()), float(den.sum())
        info = F_DAY * (Sn + Sd) / n >= 1.0 if n > 0 else False
        rho = Sn / Sd if Sd > 0 else (float("inf") if Sn > 0 else float("nan"))
        lo, hi = _boot_ratio(num, den, k * 100 + cmp_id) if info else (float("nan"),) * 2
        return dict(rho=rho, lo=lo, hi=hi, info=info, E_num=F_DAY * Sn / n, E_den=F_DAY * Sd / n, stat="%s/%s" % (dn, st),
                    lab=(label(rho, lo, hi) if info else None))

    def scan(num_e, den_e, cmp_id, gys=(25,), tag="", num_scale_fn=None, rho_div=1.0, cand=None, verbose=True):
        pts, cells = {}, {}
        for mode in MODES:
            for s in S_GRID:
                labs = []
                for k, tk in enumerate(tl):
                    if tk[0] != "sweep" or tk[1] != s or tk[2] != mode or tk[3][2] not in gys or k not in R:
                        continue
                    ns_ = num_scale_fn(tk) if num_scale_fn else 1.0
                    c = cell(k, num_e, den_e, cmp_id, cand=cand, num_scale=ns_)
                    if rho_div != 1.0:
                        c["rho"] /= rho_div
                        c["lo"] /= rho_div
                        c["hi"] /= rho_div
                        c["lab"] = label(c["rho"], c["lo"], c["hi"]) if c["info"] else None
                    cells[(mode, s, tk[3][0])] = c
                    labs.append(c["lab"])
                pts[(mode, s)] = point_label(labs)
        b = band_of(pts)
        if verbose:
            print("\n== %s  (%s vs %s, gy %s)" % (tag, num_e, den_e, gys))
            for (mode, s, dname), c in cells.items():
                print("  %-8s s=%-6g %-14s %-9s E_num=%-10.4g E_den=%-10.4g rho=%-8.4g [%.4g, %.4g] %s"
                      % (mode, s, dname, c["stat"], c["E_num"], c["E_den"], c["rho"], c["lo"], c["hi"],
                         c["lab"] or "-"))
            for (mode, s), v in pts.items():
                rhos = [c["rho"] for (m_, s_, _), c in cells.items() if m_ == mode and s_ == s and c["info"]]
                print("  point %-8s s=%-6g %-10s median rho %s" % (mode, s, v or "non-informative",
                                                                    ("%.4g (range %.4g-%.4g)" % (np.median(rhos), min(rhos), max(rhos))) if rhos else "-"))
            print("  BAND: %s" % b)
        return b, pts, cells

    gov, gpts, gcells = scan("D2", "R", 1, tag="THE BAND: reading (iv), Rd-1: D2_iw vs R, S*")
    sens = {}
    sens["D3"] = scan("D3", "R", 2, tag="sensitivity (a) D3_iw vs R")[0]
    sens["gy20"] = scan("D2", "R", 1, gys=(20,), tag="sensitivity (b) 20-y cells")[0]
    sens["R+"] = scan("D2", "Rp", 3, tag="sensitivity (c) D2_iw vs R+")[0]
    sens["SFS-tail"] = scan("D2", "R", 1, tag="sensitivity (d) SFS-tail bracket rho / b", rho_div=B_TAIL)[0]
    sens["two-point"] = scan("D2_tp", "R_tp", 4, tag="sensitivity (e) two-point bracket")[0]
    eu = scan("EU", "R", 5, tag="reading Rd-2: D_EU vs R",
              num_scale_fn=lambda tk: 1.0 / H_EU[tk[3][0]])
    print("\n== reading (ii) cross-check (random base pairs): rho_R0 = rho x cR / uniform = rho x %.1f" % (m0["cR"] / UNIFORM))
    sensitive = gov in ("DAY", "CRITIC") and any(v != gov for v in sens.values())
    print("\n== BAND (reading iv): %s%s;  sensitivities: %s;  Rd-2 band: %s;  V-iw %s"
          % (gov, " -> SENSITIVE (no verdict move)" if sensitive else "", sens, eu[0], "PASS" if viw else "FAIL"))
    esc = gov in ("DAY", "CRITIC") and not sensitive and viw
    print("== escalation clause: %s" % ("FIRES (three reviews; report, do not apply)" if esc else "does not fire"))
    # ---------------- descriptive tables
    print("\n== per statistic, 25-y cells (sums at F_DAY; formula; D2_iw / R; two-point factor D2_tp / D2 on Z-stats)")
    for k, tk in enumerate(tl):
        if tk[0] != "sweep" or tk[3][2] != 25 or tk[1] < 0.02 or k not in R:
            continue
        r, n = R[k], R[k]["meta"]["n_wc"]
        row = []
        for dn in DESIGNS:
            for st in STATS:
                d2 = r["comp"]["D2"][dn][st]
                rr = r["comp"]["R"][dn][st]
                D, Rv = d2["E_hh"] + d2["E_f"], rr["E_hh"] + rr["E_f"]
                if dn == "v62" or (dn, st) in (("v66", "Z50"), ("v66", "Z10"), ("blog", "B10")):
                    row.append("%s/%s %.3g/%.3g" % (dn, st, F_DAY * D / n, F_DAY * Rv / n))
        tp = []
        for dn, st in (("v62", "Z50"), ("v66", "Z50"), ("v62", "Z10"), ("blog", "B10")):
            a = r["comp"]["D2_tp"][dn][st]
            b = r["comp"]["D2"][dn][st]
            ra, rb = a["E_hh"] + a["E_f"], b["E_hh"] + b["E_f"]
            tp.append("%s/%s x%.3g" % (dn, st, ra / rb if rb > 0 else float("nan")))
        print("  %-8s s=%-5g %-9s %s | tp %s" % (tk[2], tk[1], tk[3][0], "  ".join(row), " ".join(tp)))
    print("\n== T1: window completions with the swept site on the panel, per completion (D2, R, R+, D2/R)")
    for k, tk in enumerate(tl):
        if tk[0] != "sweep" or k not in R:
            continue
        T, n = R[k]["T1"], R[k]["meta"]["n_wc"]
        print("  %-8s s=%-6g %-14s D2 %.4g  R %.4g  R+ %.4g  D2/R %s  (after-start completions %d of %d)"
              % (tk[2], tk[1], tk[3][0], T["D2"] / n, T["R"] / n, T["Rp"] / n,
                 "%.3g" % (T["D2"] / T["R"]) if T["R"] > 0 else "-", T["n_wc_after_start"], n))
    print("\n== decomposition, S*, 25-y cells: D2/R = (D2/R_sfs) x (R_sfs/R)")
    for k, tk in enumerate(tl):
        if tk[0] != "sweep" or tk[3][2] != 25 or tk[1] < 0.03 or k not in R:
            continue
        dn, st = sstar(R[k])
        v = {e: R[k]["comp"][e][dn][st]["E_hh"] + R[k]["comp"][e][dn][st]["E_f"] for e in ("D2", "R", "Rsfs")}
        if v["R"] > 0 and v["Rsfs"] > 0:
            print("  %-8s s=%-5g %-9s D2/R %.3g = %.3g x %.3g" % (tk[2], tk[1], tk[3][0], v["D2"] / v["R"],
                                                              v["D2"] / v["Rsfs"], v["Rsfs"] / v["R"]))
    print("\n== neutral arm (expected counts; D2_iw, R, D3_iw, EU, Rsfs) and D2_iw/R")
    for k, tk in enumerate(tl):
        if tk[0] != "neutral" or k not in R:
            continue
        E = R[k]["comp_neutral"]["E"]
        for dn in DESIGNS:
            print("  %-14s %-4s " % (tk[3][0], dn) + "  ".join(
                "%s: %s D2/R %s" % (st, "/".join("%.3g" % E[dn][e][st] for e in ("D2", "R", "D3", "EU", "Rsfs")),
                                    ("%.3g" % (E[dn]["D2"][st] / E[dn]["R"][st])) if E[dn]["R"][st] > 0 else "-")
                for st in ("N100", "M10")))
    for k, tk in enumerate(tl):
        if tk[0] == "neutral" and k in R:
            print("  H_EU %-14s %.4g; present segregating share of R sites %.3f" %
                  (tk[3][0], R[k]["comp_neutral"]["H_EU"], R[k]["comp_neutral"]["present_seg_share"]))
    secs = [(R[k]["meta"].get("secs_l5", 0), R[k]["meta"].get("secs_comp", 0), R[k]["meta"]["wall"]) for k in R]
    print("\ncost: sum of task walls %.2f h (L5 part %.2f h, comparator %.2f h)" %
          (sum(s[2] for s in secs) / 3600, sum(s[0] for s in secs) / 3600, sum(s[1] for s in secs) / 3600))


def sstar(r):
    """L5 rule C on the reproduced L5 D2 sums (sweep part; the neutral part is 0 for all three candidates)."""
    best, bv = None, -1.0
    for dn, st in SSTAR_CANDS:
        c = r["sums"][dn]["D2"][st]
        v = c["E_hh"] + c["E_f"]
        if v > bv:
            best, bv = (dn, st), v
    return best


# ------------------------------------------------------------------------------------------------ main
if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "selfcheck"
    if cmd == "selfcheck":
        sys.exit(0 if selfcheck() else 1)
    elif cmd == "smoke":
        import resource
        outdir = sys.argv[2]
        os.makedirs(outdir, exist_ok=True)
        t0 = time.time()
        ok = selfcheck()
        print("selfcheck %.1fs" % (time.time() - t0), flush=True)
        tl = l5.task_list()
        pick = [0] + [k for k, tk in enumerate(tl) if tk[0] == "sweep" and tk[3][0] == "const1e4"
                      and (tk[1], tk[2]) in ((5e-2, "hard"), (3e-3, "hard"), (3e-3, "standing"))]
        for k in pick:
            t1 = time.time()
            fn = run_task_c_k((k, outdir, SMOKE_SIZES))
            meta = json.load(open(fn))["meta"]
            print("smoke %s: %.1fs %s" % (task_name_c(tl[k]), time.time() - t1,
                  {k2: meta[k2] for k2 in ("n_wc", "n_kept", "n_hh_snps", "comp_hh_snps", "comp_tp_evals", "passes",
                                           "secs_l5", "secs_comp") if k2 in meta}), flush=True)
        print("smoke tasks %.1fs, peak RSS %.0f MB" % (time.time() - t0,
              resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024), flush=True)
        so = sys.stdout
        try:
            sys.stdout = open(os.devnull, "w")          # code path only: no number is shown
            analyse(outdir, smoke=True)
            st = "ok"
        except Exception as ex:
            st = "FAIL %r" % (ex,)
        finally:
            sys.stdout.close()
            sys.stdout = so
        print("analyse(smoke, stdout discarded): %s; smoke total %.1fs" % (st, time.time() - t0), flush=True)
    elif cmd in ("main", "hostsmoke"):
        import multiprocessing as mp
        workers = int(sys.argv[2])
        outdir = sys.argv[3]
        os.makedirs(outdir, exist_ok=True)
        sz = SIZES if cmd == "main" else SMOKE_SIZES
        if cmd == "hostsmoke" and not selfcheck():
            sys.exit("selfcheck failed")
        t0 = time.time()
        with mp.get_context("forkserver").Pool(workers, maxtasksperchild=4) as pool:
            for _ in pool.imap_unordered(run_task_c_k, jobs_for(outdir, sz)):
                pass
        print("all done %.1fs" % (time.time() - t0), flush=True)
        if cmd == "hostsmoke":
            import resource
            print("hostsmoke children peak RSS %.0f MB" %
                  (resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss / 1024), flush=True)
    elif cmd == "analyse":
        analyse(sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else None)
    else:
        sys.exit("unknown command")
