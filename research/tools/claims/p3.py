from gen import *
Z3='[MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04)'
Z25='[MITTENS 2025, Zenodo 18165980](https://zenodo.org/records/18165980) (key Z18165980), pub. 2025-12-28 (modified 2026-01-06)'

claim('A3','required-fixations-2019-2025','Required fixations: 30M (2019) then 20M on the human lineage (2025)','day','A','A',
 [('supports','A'),('depends-on','A3c')],False,'firsthand','checked',('holds','partial','contested'),
 q('it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000 mutations to become fixed in the chimpanzee population',
   '[Maximal Mutations](https://voxday.net/2019/02/07/maximal-mutations/) (key B2019-02-07), blog, 2019-02-07, ¶26.')+'\n'+
 q('Genetic divergence: ~40 million single-nucleotide variants; ~20 million fixations required on human lineage. Time available: 6–7 million years at 20 years/generation = 300,000–350,000 nominal generations.',
   Z25+', ¶34.'),
 '''R_2019 = 15e6 per lineage (30e6 total); R_2025 = 40e6 / 2 = 20e6 per lineage   (`divergence.required_fixations.day_2019`, `.day_2025`)

`derived:` 35e6 SNV + 5e6 indel events (CSAC 2005) = 40e6 events, /2 = 20e6 (reconciles). Correcting for polymorphism: CSAC fixed fraction 0.0106/0.0123 = 0.862; 35e6 x 0.862 = 30.2e6 fixed SNV differences, /2 = 15.1e6 per lineage (python3 -I). That is close to the 2019 figure of 15e6, although the 2019 post does not give this derivation.''',
 '- Stated: the SNV and indel differences in one human and one chimp genome are the substitutions to be explained; symmetric split between lineages.\n- Implicit: polymorphic sites are fixed differences (CSAC says 14–22% of the divergence is polymorphism, A3c); every SNV or indel event is a separate fixation (true for SNV; for indels the CSAC count is events).',
 '''- Against: Hancock (GG-02) says a factor-of-two issue exists (A3d, where it is assessed); Mansfield (MF-06) says "around 25 million give or take" is the number he has seen (uncited; consistent with this claim, not a disagreement).
- In support: Mansfield\'s 25 million is the same order as 20M.
- Weaknesses: the 2019 "30,000,000" is used with 450,000 generations and 281/562/125 achievable (A-file): the three achievable numbers do not reconcile with each other.''',
 LITH+'''| Chimpanzee Sequencing and Analysis Consortium 2005 | "constituting approximately thirty-five million single-nucleotide changes, five million insertion/deletion events, and various chromosomal rearrangements" | verified-partial (one genome per species; includes polymorphism; see A3c) |''',
 '''Not a simulation target. Prediction (claimant): R_2025 = 20M. Prediction (critic): fixed differences are 14–22% fewer, so R = 15–17M per lineage (derived: 35e6 x 0.78–0.86 / 2 = 13.7–15.1M for SNV only). A change in R by 1.3x has no effect on a shortfall of 1e5.''',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- `required_fixations` per lineage with a polymorphism-correction toggle (fixed fraction 0.78–0.86).')

claim('A3a','205m-headline','Required fixations rise to 205M: 410M genomic differences from Yoo 2025, halved per lineage','day','A','A3',
 [('supersedes','A3'),('depends-on','A3x1')],False,'firsthand','checked',('arithmetic-error','misread','contested'),
 q('approximately 35 million SNVs, 1,140 interspecific inversions, and approximately 187 megabases of structurally divergent regions, for a total of approximately 410 million genomic differences. Apportioned symmetrically to the human lineage this yields approximately 205 million required fixations.',
   Z3+', p.11 (s7.1).')+'\n'+
 q('the genetic difference between chimps and humans turned out to be 14.9 percent, with 410 million base pairs separating the two lineages since the Chimpanzee-Human Last Common Ancestor.',
   '[Probability Zero 2nd edition](https://voxday.net/2026/05/23/probability-zero-2nd-edition/) (key B2026-05-23), blog, 2026-05-23, ¶6.'),
 '''R_2026 = 410e6 / 2 = 205e6 per lineage (`divergence.required_fixations.day_2026`, derived: 410e6 bp / 2).

`derived:` the stated components do not sum to the stated total: 35e6 + 1,140 + 187e6 = 222,001,140, not 410e6; the text does not show the arithmetic and mixes units (SNVs, events, megabases). 410e6 = 14.9% of 2.75e9 bp (410/0.149 = 2,752 Mb), whereas a haploid human genome is 3.1–3.2e9 bp (0.149 x 3.1e9 = 462e6). The only reconciling arithmetic in the repo is 410/35 = 11.7 (the KITTENS ratio, A5b). Yoo 2025 SDR averages 327 Mb per lineage (x2 = 654 Mb); no pair or sum of the Yoo SDR totals gives 187 or 410 (closest: 412.1, flagged a coincidence).
Version arithmetic that does reconcile: 1,075,000 = 205e6 / 190.6 (1,075,437); 17.5e6 SNV-only: 91,806 (paper 91,600).''',
 '- Stated: complete T2T assemblies reveal more divergence than the 2005 draft; each affected base counts as a required fixation.\n- Implicit: a structural variant of length n bp requires n separate fixations (A3x); the 410M figure comes from Yoo 2025.',
 '''- Against: McCarthy (MC-11), Dumb-and-Dumber (RE-05), Hancock (GG-10–GG-12), Sparky_6_4 (RE-08) argue the count mixes bases and events (A3x). Mansfield (MF-06): numbers he has seen are ~25 million, not 200 million.
- In support: Day concedes in s7.3: "This is a legitimate methodological concern" and runs MITTENS on SNVs alone (A3b).
- Weaknesses in the responses: the critics\' event-count alternative (about 40M) is itself derived from the 2005 consortium counts, not recomputed from Yoo 2025; Hancock (GG-10) only "suspects" the 205M includes gap divergence.''',
 LITH+'''| Yoo et al. 2025 | "We catalogued all structurally divergent regions (SDRs) among the ape genomes and found an average of 327 Mb of sequence (10%) per ape lineage"; "we curated 1,140 interspecific inversions" | **not-found** for 410 Mb and 187 Mb (ledger); see A3x1 |''',
 '''Not run. Prediction (claimant): a lineage-aware count of independent fixed mutational events from Yoo 2025 exceeds 100M. Prediction (critic): it is within 1.5x of 40M events (35M SNV + ~5M indels + ~1,140 inversions + other SV events).
- Result that would change a verdict: a published count of fixed SV events in human–chimp comparisons.''',
 'Arithmetic audit (python3 -I, scratch): the 410M total does not reconcile with its stated parts. Review: pending.',
 '- `required_fixations` presets: events (about 40M total, 20M per lineage), SNV only (17.5M), bp-affected (205M).')

claim('A3b','snv-only-concession','Day\'s SNV-only variant: 17.5M required fixations still gives a 91,600-fold shortfall','day','A','A3a',
 [('revises','A3a')],False,'firsthand','checked',('holds','partial','contested'),
 q('A reasonable objection holds that large structural variants such as inversions, deletions, insertions of mobile elements, should not each count as a single fixation event in the same sense as a point mutation. This is a legitimate methodological concern.',
   Z3+', p.12 (s7.3).')+'\n'+
 q('Restricting to the approximately 35 million SNVs and apportioning symmetrically: 17.5 million required fixations on the human lineage.',Z3+', p.12 (s7.3).')+'\n'+
 q('At 1,322 gen/fix (non-mutator): 191 achievable. Shortfall: 91,600×. At 105 gen/fix (mutator): 2,407 achievable. Shortfall: 7,271×.',Z3+', p.13 (s7.3).'),
 '''R_SNV = 35e6 / 2 = 17.5e6; achievable = 252,000/1,322 = 190.6 (191); shortfall = 17.5e6/191 = 91,623 (paper 91,600); mutator: 252,000/105 = 2,400 (paper 2,407, i.e. G_f = 104.7), 17.5e6/2,407 = 7,270 (paper 7,271). All reconcile (python3 -I). The pass-1 figure ~94,000 is not in the text.''',
 '- Stated: SNV-only is the conservative counting; the shortfall persists at four to five orders of magnitude.\n- Implicit: the 35M SNVs are all fixed differences (CSAC: 14–22% polymorphic, A3c); LTEE rate transfers unscaled (A5).',
 '''- Against: Sparky_6_4 (A5b) shows that after scaling by per-genome mutation supply, the achievable count is about the same as 17.5M.
- In support: this is a self-correction by Day; Camestros\'s observation (CA-02) that the arithmetic is not wrong applies here too.
- Weaknesses in the responses: A5b\'s scaling is linear (flagged by its author); using Day\'s own mutator exponent gives 80–450x residual (A5b).''',
 LITH+'''| CSAC 2005 | 1.23% total, "1.06% or less corresponding to fixed divergence" | verified-partial |''',
 'Covered by A5/A5b predictions. Result recorded above.', 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- Preset: SNV-only requirement.')

claim('A3c','csac-polymorphism','The 35M SNV and 5M indel counts are human–chimp genome differences that include polymorphism','literature','A','A3',
 [('revises','A3')],False,'firsthand','extracted',('n/a','partial','supported'),
 '''> The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species.

Source: Chimpanzee Sequencing and Analysis Consortium 2005 (key CSAC2005), main text, "Nucleotide divergence".

> we estimate that polymorphism accounts for 14-22% of the observed divergence rate

Source: same, "Genome-wide rates".

> Single-nucleotide substitutions occur at a mean rate of 1.23% between copies of the human and chimpanzee genome, with 1.06% or less corresponding to fixed divergence between the species.

Source: same, Introduction findings.
''',
 '''`divergence.snv_divergence_fraction.csac_2005_total` = 0.0123; `.csac_2005_fixed_max` = 0.0106; proposed key `divergence.fixed_fraction_of_observed` = 0.78–0.86.
`derived:` 0.0106/0.0123 = 0.862; 35e6 x 0.78–0.86 = 27.3e6–30.2e6 fixed SNV differences; per lineage 13.7e6–15.1e6.''',
 '- Stated: one copy per species.\n- Implicit (in uses by both sides): reference-genome differences equal fixed differences; Nesslig20 (PS-03) states this point in the form "not all of the differences they identified between genomes are actually fixed in either the human or chimp populations".',
 '''- Against: none in the Day corpus addresses polymorphism in the 35M count (the 2025 and 3.0 papers use 35M as required fixations).
- In support: Nesslig20 (PS-03, critic) and Camestros (CA-04: "treating ALL the genetic differences … as mutations that initially only occurred after the point of divergence") both press ancestral polymorphism.
- Weaknesses: the effect is 14–22%, not an order of magnitude. Yoo 2025 SNV divergence is internally inconsistent (0.15–0.16% in SI text vs 1.46% in Table III.14, unresolved).''',
 LITH+'''| CSAC2005 | above | verified-partial (as used by Day and by critics) |
| Yoo2025 | SNV divergence 0.15–0.16% (text) vs 1.46% (Table III.14) | discrepancy, unresolved |''',
 'Prediction: removing polymorphism lowers the SNV requirement by 14–22% (derived above); it does not change the verdict on the shortfall unless A5 closes the remaining gap, where it would matter (KITTENS: 17.9M vs 17.5M).',
 'No script. Review: pending.', '- `fixed_fraction_of_observed` toggle on the requirement.')

claim('A3d','factor-of-two-both-lineages','Hancock: the achievable count should be doubled, since fixation happens in both lineages (a "classic factor of two error")','critic','A','A3',
 [('attacks','A3')],False,'firsthand','checked',('holds','partial','n/a'),
 q('this basic math is off by a factor of two',
   '[Gutsick Gibbon and Zach Hancock video](https://www.youtube.com/watch?v=_Vu0ZVVjwHc), 2026-10-03, t=01:37:07 (GG-02; auto-caption). In the same passage: "So at at least this should be two times this ... So this really should be at least 360".'),
 '''Hancock\'s point: the achievable count (180 on Duffy\'s slide = 252,000/1,400) should be 2x180 = 360 because fixation accrues in both lineages.

`derived:` this changes the shortfall only if the required count is the total divergence. In MITTENS the required count is already per lineage (2025: 40M/2 = 20M; 3.0: 410M/2 = 205M; 2019: the post doubles the achievable instead, 562 = 2 x 281). The ratio R_total/(2F) = (R_total/2)/F is invariant, so the 3.0 shortfall (205e6/191) is unchanged by Hancock\'s correction. If Duffy\'s slide compared 180 with a total (both-lineage) count, the slide would be off by 2x; the slide text is not in the repo.''',
 '- Stated: fixation is happening in both lineages since the split.\n- Implicit: the required count on the slide was a two-lineage total (not shown).',
 '''- Against (Day): MITTENS counts per lineage, halving 410M to 205M (Z23003785 s7.1).
- In support: the 2019 post doubles achievable (562 = 2 x 281.25), consistent with Hancock\'s accounting.
- Weaknesses in the responses: the repo cannot confirm which comparison Duffy\'s slide made. Hössjer notes (HO-05 context) both lineages in his own accounting; no one disputes the factor of two as a principle.''',
 NOLIT, 'Arithmetic; no pre-registration needed beyond the invariance statement above.', 'Arithmetic only. Review: pending.', '- A "per lineage / both lineages" accounting toggle.')

claim('A3x','bp-vs-events','The 205M requirement counts base pairs in structural variants as if each were a separate fixation event','critic','A','A3',
 [('attacks','A3a')],False,'firsthand','checked',('holds','accurate','supported'),
 q('The 410 million base pair difference refers to structural variation, which includes duplications, insertions, etc., in which a single mutational event can cause hundreds, thousands, or even millions of base-pair differences.',
   '[Dennis McCarthy, Vox Day Responds](https://dennismccarthy.substack.com/p/vox-day-responds), 2026-09-17, para 26 (MC-11).')+'\n'+
 q('bases affected by a rearrangement are not separate mutation events: one structural change can affect millions of bases.',
   '[r/DebateEvolution, Dumb-and-Dumber](https://www.reddit.com/r/DebateEvolution/comments/1wss2wj/), 2026-09-28 (RE-05).'),
 '''Claim: fixations are events; R_events = (SNV + indel events + inversions + other SV events)/2 ≈ 20M per lineage, not 205M.

`derived:` (python3 -I) 35e6 SNV + 5e6 indel events (CSAC) + 1,140 inversions = 40.0e6 events; /2 = 20.0e6. 410e6/40.0e6 = 10.25; 410e6/35e6 = 11.7. Day\'s own wording in the 2nd edition is "410 million base pairs" (A3a), i.e. the critics\' reading of the unit matches Day\'s text.
Related critic statements: Hancock (GG-10) "the number is 205 million differences, right?" and GG-11 (his "something like 407" = 205e6/(2 x 252,000) = 406.7 mutations per generation over both lineages, an accounting choice); Nesslig20 (PS-03) reference genome differences vs fixed; Mansfield (MF-06) "around 25 million give or take, not 200 million" (uncited).''',
 '- Stated: one mutational event can affect many bases.\n- Implicit: a structural change fixes as a single event with probability comparable to a point mutation (not required for the logic here, which is about counting units).',
 '''- Against (Day): s7.3 concedes the concern and runs the SNV-only variant (A3b). Day has not, in the corpus, defended counting bp as separate fixations.
- In support: CSAC 2005 counts 5M indel events as far fewer than 35M substitutions; Yoo 2025 reports gap divergence as megabases affected (5–15x SNV megabases) and inversions as events (1,140); both are unit distinctions consistent with the critics.
- Weaknesses in the responses: critics do not give an independently derived event count from Yoo 2025; Hancock\'s 407 is arithmetic on Day\'s number, not an event count. Per-base fixation of large indels may involve selection on the whole event, which supports event counting but does not tell us how many events there were.''',
 LITH+'''| Yoo et al. 2025 | "Gap divergence showed a 5-fold to 15-fold difference in the number of affected megabases when compared to single-nucleotide variants" | verified; supports bp ≠ events |
| CSAC 2005 | "Of course, the number of indel events is far fewer than the number of substitution events (,5 million compared with ,35 million, respectively)." (extraction renders "~" as ",") | verified |''',
 '''Pre-registration: not run. Prediction (critic): the number of independent mutational events in the human–chimp divergence is 40M ± 30%. Prediction (claimant): n/a (Day concedes the unit; he reports both).
- Result that would change a verdict: a published count of fixed SV events well above 100M.''',
 'Arithmetic audit (python3 -I, scratch). Review: pending.', '- `required_fixations` unit selector: bp / events / SNV-only.')

claim('A3x1','yoo-2025-fidelity','Yoo 2025 reports 327 Mb average SDR per lineage; the 410 Mb and 187 Mb figures are not in it','literature','A','A3x',
 [('supports','A3x')],False,'firsthand','checked',('n/a','misread','supported'),
 '''> We catalogued all structurally divergent regions (SDRs) among the ape genomes and found an average of 327 Mb of sequence (10%) per ape lineage

Source: Yoo et al. 2025 (key Yoo2025), main text, "Divergence and selection".

> 12.5-27.3% of an ape genome failed to align or was inconsistent with a simple one-to-one alignment

Source: same.

> we curated 1,140 interspecific inversions, of which 522 are newly discovered

Source: same, "Structural variation".
''',
 '''`divergence.structurally_divergent_Mb_per_lineage.yoo_2025` = 327. `derived:` 327 x 2 = 654 Mb (both lineages, if additive); 410/327 = 1.25. Brute-force search over SDR totals (Table V.24: human h1/h2 147.8/183.6 Mb; chimp h1/h2 288.9/308.2 Mb) found no combination giving 187 or 410 (closest 412.1 = HSA h2 + PAB h1, flagged as coincidence). 1,140 inversions is across six apes versus the human reference. Ledger status: **not-found** (the figures are absent from main text, SI text and tables). Classified here as `misread` for the fidelity verdict on Day\'s citation because Yoo supplies a different, specific, sourced figure (327 Mb); the ledger label remains not-found.''',
 '- Stated by Yoo: SDRs are average per lineage; gap divergence is reported in megabases.\n- Implicit: whether SDR megabases are fixed differences or include polymorphism between haplotypes.',
 '''- Against (Day): Day may have derived 410M from sources outside Yoo 2025 (the 2nd-edition post reports 14.9% and 410M bp); the repo cannot exclude this.
- In support (critics): the figure is not in Yoo.
- Weaknesses in the responses: the harvest of Yoo SI is complete only to the extent of the downloaded files; supplementary tables other than 14, 24, 67 were not searched cell-by-cell.''',
 LITH+'''| Yoo2025 | above | Day\'s 410 Mb / 187 Mb: not-found |''',
 'No prediction. Result recorded.', 'Brute-force table search done in R1 (ledger). Review: pending.', '- None.')
