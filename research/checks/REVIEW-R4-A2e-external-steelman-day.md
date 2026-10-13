This review argues Day's side as hard as it can be argued honestly; it sets no verdict (the lead rules conflicts, D-24).

# Steelman review (Day side): A2e external, the superseded `contradicted` (scoped) (O5 5/6, D-21)

Reviewer: fresh Opus instance (Reviewer agent), 2026-10-13. Brief `research/checks/briefs/O5-reviews-reviewer.md` (f9e254d). I wrote none of the six O5 reviews before this one and did not author A2e-alpha or its addendum.

**Disclosure.** I did not open the correctness-2 or steelman-critic files. The subject line of commit 2662fed (correctness-2) was on screen in `git log` before I started; it mentions 1,065 "without the arbitrary haircut". I recomputed that figure myself (below).

**Scope.** As the brief says, the D-12 scoping is not reopened: per-generation count of adaptive coding fixations of any effect size, on model-inferred alpha. The question is whether the evidence on record carries `contradicted` within that scope.

**What I read.** Claim file `docs/research/claims/A2e-ltee-as-ceiling.md` l.12-16, 65-74. `research/checks/results/R4-A2e-alpha.md` l.1-30, 127-200. `a2e_alpha_uricchio.py` docstring (grep). GRADE pass row A2e (`criticality/grade-certainty-2026-10-12.md` l.330, 503-507). Gaps ledger RG-03.

**Source.** My own fetch of Uricchio, Petrov & Enard 2019 (PMC6693860) as NCBI BioC XML, 2026-10-13, `sources/raw/a2e-steelday-2026-10-13/bioc.xml` (gitignored), sha256 `4391e2159753fd606c7260e6aa81c9e754b20d97ffdad85152ec4631f6781122`. Europe PMC returned HTTP 500 and the PMC page returned a captcha, so this is a different format from the addendum's copy (`3e7c44cb...`). Every quote below is a substring of the text extracted from it.

## Recomputation (post hoc, arithmetic only, one local process)
Inputs: G1 = 252,000 / 1,322 = 190.6. N2 = 11,090. N3 = 18,180. NS = 29,925. Table 1 is quoted below.

| alpha | N2 count (x G1) | paper's NS count (x G1) | share of the count that must be artefact for A2e to survive (N2) |
|---|---|---|---|
| 0.135, posterior mean | 1,497 (7.85) | 4,040 (21.2) | 87% |
| 0.096, lower HPD | **1,065 (5.59)** | 2,873 (15.1) | **82%** |
| 0.072 (lower HPD x 0.75) | 798 (4.19) | 2,155 (11.3) | 76% |
| 0.076, aMK on the same data | 843 (4.42) | 2,274 (11.9) | 77% |
| 0.09, non-VIP lower HPD | 998 (5.24) | n/a | 81% |
| 0.041, alpha_S mean (strong only) | 455 (2.39) | 1,227 (6.4) | outside the scope |

Every number in the field text (l.14) and the Readings row (l.71) reproduces. The field's arithmetic is right. Day's case is about what the arithmetic is taken to show.

Source, Table 1 ("Datasets and corresponding adaptation rates"; cells tab-separated in the source, shown here with spaces): "Whole-egoism 29925 38135 0.135 (0.096,0.17) 0.097 (0.0,0.21) 0.041 (0.0,0.13)"; "Non-VIPs 23676 27826 0.12 (0.09,0.15)". Caption: "Estimated α values represent the mean of the posterior distribution. [...] Values in parentheses represent the area of 95% highest posterior density."

## Findings

### MAJOR-1: the 25% "charity haircut" has no basis in the source, and under neither reading of the source is it a charity to Day
Where: claim file l.14 ("after a 25% charity haircut") and l.71. R4-A2e-alpha.md l.144, l.173 ("the 0.75 haircut covers it either way") and l.190 (owner summary: "Even with every Day-charitable choice stacked (lowest bound, a 25% haircut, the smallest audit denominator)").

The 25% comes from the source, but there it describes something else: the effect of background selection on the *realized* human rate.
- Abstract: "We show that in this adaptation regime α is reduced ≈ 25% by linkage genome-wide."
- Results, under the heading "Background selection reduces true α when adaptation is weak": "Integrating across the whole genome, our results suggest that human adaptation rate in coding regions is reduced by approximately 25% by BGS (Fig. S9D)."
- Introduction: "we use a model-based fitting procedure that directly accounts for BGS and weakly-beneficial alleles."

There are two readings.
- **Reading A (most natural).** 0.135 is fitted to the observed alpha(x) of a genome that BGS has already shaped, so it is net of the 25%. Applying x 0.75 then counts the BGS reduction a second time. The factor is a free number that the audit chose, wearing the source's label.
- **Reading B.** 0.135 is a no-BGS counterfactual. Then x 0.75 is a required correction, and 798 is simply the lower bound with no charity in it. In that case the "stack" holds one fewer charity than advertised.

Either way, l.173 is wrong to say the haircut "covers it either way". It also matters for Day. The owner accepted the scoping (D-12) on a summary saying "every Day-charitable choice" had been stacked. Yet the stack contained:
- one factor with no source behind it, and
- none of the adjustments Day would actually ask for: model error (MAJOR-2) and moving alpha from one gene set to another (MINOR-1).

The label makes the result look tested against Day's objections when it was tested against the audit's own choices.

**What the fix costs Day.** Dropping the factor *raises* the count to 1,065 (5.6x). Day gains no number from this finding, only an accurate description.

**Fix.**
- State the basis as "lower 95% HPD on N2: 1,065 (5.6x); 15x on the paper's own NS".
- Withdraw "charity haircut" and "covers it either way". If the 798 row is kept, label it "an unsourced further 25% cut; the source's 25% is BGS acting on the realized rate".
- Tell the owner that the D-12 summary misdescribed the stack.

### MAJOR-2: the lower HPD is an in-model bound, and the three estimators are not independent; the model-error question is unanswered
Where: R4-A2e-alpha.md l.165 ("its HPD excludes the threshold by a factor of 5.5"), l.186 ("three estimators (ABC-MK, aMK baseline, Boyko) would all need a ~4-fold error in the same direction"), claim l.14 ("Basis: Uricchio 2019 lower 95% HPD").

The addendum treats the HPD as the Day-charitable floor. But an ABC posterior is conditional on its model: demography, BGS map, DFE parameterisation and priors. Day's objection is not that alpha is imprecise within ABC-MK. It is that MK-family inference may be wrong. l.186 concedes that "the HPD itself covers parameter, not model, uncertainty". It then answers model uncertainty with three estimators, as if they were independent checks. They are not.
- ABC-MK and aMK use one dataset: "nearly twice the estimate obtained with the same dataset using the original aMK approach" (Results).
- All three rest on the same MK logic: an excess of nonsynonymous divergence over polymorphism, measured against synonymous sites as the neutral reference.
- The source itself names failure modes that all three share: "seven confounding factors (ancestral mispolarization, demographic model misspecification, BGS model misspecification, covariation of BGS and sequence conservation, GC-biased gene conversion, selection on synonymous alleles, and misspecification of strongly- and/or weakly-beneficial [...]" (Discussion).

On the evidence on record, the choice of method moves alpha more than the margin does. On the same data: 0.135 against 0.076 (1.8x). Across the literature in RG-03: 0.2% to 13.5% (about 67x). The margin is 5.6x (4.2x with the haircut). For A2e to survive, 82% of the lower-HPD count has to be artefact. That is large, but it is a claim about model error, and no number in the record bounds model error.

**What it costs Day, stated plainly.**
- The spread is not symmetric. The low values are naive estimates that their own authors flag as biased low (EK and GV quotes, R4-A2e-alpha.md l.75, l.82).
- The source reports that "α estimates were not very sensitive to various types of model misspecification" (Methods, "Using ABC-MK to infer adaptation rate and strength").
- No bias-corrected estimate on record falls below 1.72% on N2 (or 0.64% on NS).

Day has an argument here, not a datum.

**Fix.**
- Replace "three estimators" with "two datasets, one model family".
- Label the basis "conditional on ABC-MK (in-model interval)".
- Record the 82% artefact share at the lower HPD beside the margin.

### MAJOR-3: what moved the field was one source, read before registration and gathered with no search strategy; that does not carry `contradicted` at the strength the word implies
Where: claim l.14. R4-A2e-alpha.md l.128-129, 162, 188, 192.

Before the addendum the field stood at "contested, leaning contradicted" (l.127). l.128 gave two reasons for holding there: (a) Boyko was the only full-text source, and (b) Uricchio was abstract only. The full text then added:
- confirmation that the estimate is human-branch;
- confirmation that it is bias-corrected;
- one new number, the in-model HPD (0.096).

The central value (0.135) was already known from the abstract. The addendum's own reviews accepted that its predictions were written with the full text and Table 1 already read (MINOR-1, l.192). They also accepted that its trigger and blockers were written by the person who scored them (MAJOR-2, l.188). So the severity of the step is low: once the abstract value was known, the pass was near certain.

The audit's own criticality passes agree:
- GRADE rates A2e external very low under all three mappings (grade-certainty l.330, l.503-505).
- AR-05: "published alpha estimates gathered with no search strategy on a point where they differ".
- RG-03 lists no search for low human or primate bias-corrected alpha. I recall that cross-species alpha-versus-Ne literature may bear on primates. That is memory only: not fetched, not a datum.

On Day's side, therefore, the evidence carries at most "contested, leaning contradicted (scoped)". Failing that, it carries `contradicted` only with an explicit certainty qualifier ("single post hoc source, in-model interval, very-low GRADE certainty").

**What it costs Day.** This attacks how much weight the result can bear, not its direction. Every bias-corrected, human-branch estimate on record clears 191 at its lower bound, and Day offers no rival estimate.

**Fix.**
- Run a structured, two-directional search for human-lineage bias-corrected alpha (RG-03) before the field leaves `pending`; or
- carry the certainty qualifier in the field text itself.

### MINOR-1: the transfer of alpha across gene sets is untested, and alpha varies by gene set
Where: claim l.71; R4-A2e-alpha.md l.175 ("denominators are the audit's (N1-N3), not the paper's").

Alpha from Uricchio's gene set is multiplied by counts from other gene sets (Boyko, Gayà-Vidal). Table 1 shows that alpha is not uniform across genes: 0.224 for VIPs, 0.12 for non-VIPs. The non-VIP lower HPD gives 998 on N2 (5.2x).

**What it costs Day.** N2 (11,090) is about 2.7x below the paper's own human-specific NS (29,925). On balance the transfer favours Day, and it moves nothing.

**Fix.** Add one sentence naming the transfer as an assumption.

### MINOR-2: "point estimate" is a posterior mean, and the HPD is not an equal-tailed interval
Where: R4-A2e-alpha.md l.142 ("point"), l.145.

The caption says "the mean of the posterior distribution". For a skewed ABC posterior whose component HPDs touch 0 (alpha_W 0.0-0.21, alpha_S 0.0-0.13), the lower edge of the HPD is not a 2.5th percentile. No number moves.

**Fix.** Use "posterior mean" and "lower edge of the 95% HPD".

### NOTE-1: the strongest Day-side argument lies outside this brief
The question is like-for-like in effect size. The LTEE's 1/G_f counts the fixations a large clonal population completes within the experiment. Seventy-two per cent of Uricchio's alpha is weak. Strong-only gives 455 at the mean and 0 at the lower HPD. The GRADE row also records that Day's stated basis is total throughput (`rd` 1). Both points are scope questions (D-12), recorded here for the lead and not argued.

### NOTE-2: what the evidence costs Day
- Within the scope, no bias-corrected human-branch estimate on record is below the flip.
- N2 is a large concession in Day's favour.
- aMK on the same data gives 843.
- Removing the unsourced factor raises the floor from 798 to 1,065.

### NOTE-3: credit
The addendum reported the strong-only lower HPD of 0, the VIP strong-only figure of 112, and the unreconciled NS. Its fix pass accepted MAJOR-2 and MINOR-1 openly. Those Day-side points are on record. This review's complaint is with the "charity" framing and the certainty attached to the word, not with any hidden datum.

## Counts
0 BLOCKER, 3 MAJOR, 2 MINOR, 3 NOTE.
