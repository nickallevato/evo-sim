import json,collections
Q=json.load(open('quotes.json'))
order=['Kimura1962','KimuraOhta1969','Kimura1968','Chalub2022','Zeng2021','Bergeron2023','Keightley2012','Kong2012','BallouxLehmann2012','CSAC2005','Yoo2025','Langergraber2012','Scally2012','PradoMartinez2013','Nunney2003','Tenaillon2016','Good2017','Barrick2009','Mathieson2015','Fu2015','Haak2015','Mallick2024','Wistar1967','Axe2004','Taylor2001','KeefeSzostak2001']
G=collections.defaultdict(list)
for e in Q: G[e[0]].append(e)
use={ # how Day (per PLAN pass-1, not re-verified) uses the work -> match verdict
'Chalub2022':('Day cites it for the claim that k = mu is steady-state only / neutral fixation takes time (B1, "empty pipeline"). Also sought "Chalub 2012".','Math is not disputed. Paper is a two-allele PDE solution with no mutation or selection, so it does not address substitution rates; it does give a finite-time fixation probability for a stated initial condition. Use as support for "finite-time behaviour differs from the asymptote" is compatible with the paper; use as evidence about k vs mu is not.'),
'Zeng2021':('Day uses s ~ 0.001 as a beneficial-selection coefficient for fixation-time arithmetic (PLAN: t = (2/s) ln(2Ne)).','Does not match: the quoted value is a predicted mean selection coefficient against trait-affecting variants under negative selection (abstract). Positive selection appears only as a simulation sensitivity scenario.'),
'Bergeron2023':('Day cites 40-fold variation in mutation rates.','Matches (Fig. 1 legend and Results).'),
'BallouxLehmann2012':('Day cites for k < mu / N-dependence of neutral substitution rate; "k = 0.743 mu" is Day\'s own figure.','Partly matches: the paper shows N- and demography-dependence for neutral k only when generations overlap AND population size fluctuates; k = mu stays exact for non-overlapping generations. No 0.743 or 32.3 in the text.'),
'CSAC2005':('Day uses ~35M SNV + ~5M indels as required fixations (A3).','Partly matches: the counts are in the abstract, but the same paper says they are differences between one human and one chimp copy, include polymorphic sites, and that fixed divergence is <=1.06% vs 1.23% total.'),
'Yoo2025':('Day uses 410 Mb (-> 205M per lineage) from Yoo 2025 and cites inversion counts.','Not matched: neither 410 Mb nor 187 Mb found. SDR average is 327 Mb per lineage; inversion count 1,140 is across the six-ape set vs human reference; divergence measures differ by method (see derived table).'),
'Langergraber2012':('Day uses 6.3-9 My and g_len 20-32.5 y.','Paper states at least 7-8 My for human-chimp and that its method is independent of fossil calibration; chimp generation ~24-25 y.'),
'Nunney2003':('Day cites Haldane 1957 (300 gens) and the cost-of-selection bound (H).','Nunney reports Haldane\'s ~1 per 300 generations accurately and confirms hard selection can impose a cost, but finds the cost "substantially less" than Haldane\'s for M > 1/2 and notes soft selection eliminates it.'),
'Tenaillon2016':('Day uses LTEE for G_f, hypermutator hazard (A2, E).','Hypermutator share (96.5% of point mutations in six populations) matches; neutral mutations accumulating at constant rate also appears and is the basis for critic arguments about k = mu in asexuals.'),
'Good2017':('Day uses the dynamics for G_f, ">=95% rule", fixation counts.','">=95%" is not in the main text; Good et al. report clade structure, deficit of population-wide fixations, and rejection of periodic-selection (sweep-by-sweep) models.'),
'Mathieson2015':('Day uses it for aDNA selection signals / s values and the 1240k panel (C).','No s values in the main text. Panel is built from known present-day polymorphic sites (array SNPs).'),
'Wistar1967':('Day cites Eden 10^325 vs 10^52, Ulam, Schutzenberger (D).','Eden\'s numbers match the text. Ulam and Wright in the same volume reject the random-construction framing; Schutzenberger argues a "gap", not a probability calculation.'),
'Axe2004':('Day cites 1e-77 functional fraction (D).','Matches the abstract; scope is one domain-sized beta-lactamase fold extrapolated.'),
}
parts=['# Quotes: primary literature (R1 pass 2)','',
'Each quote is verbatim (<=60 words), machine-checked against the extracted text of the local copy (Unicode-normalised: ligatures, dashes, apostrophes and superscript-lost exponents may differ from print). Locator = section/page of the paper. **Role codes:** S = bears in favour of the use Day makes (per PLAN pass-1); C = bears against it; N = context; K = bears against a critic\'s use; KS = supports a critic\'s use. "Params" = `parameters.yaml` key (or `new:` proposed). Verdicts are "matches / does not match the cited use" only; no wider adjudication. Day\'s uses are taken from PLAN.md pass-1 and were not re-verified against his texts in this slice.','']
for k in order:
    if k not in G: continue
    parts.append(f'## {k}')
    if k in use:
        parts.append(f'- **Cited use (PLAN pass-1):** {use[k][0]}')
        parts.append(f'- **Fidelity (this pass):** {use[k][1]}')
    parts.append('')
    for key,loc,role,params,quote,note in G[k]:
        parts.append(f'> "{quote}"')
        parts.append(f'> - locator: {loc}; role: {role}; params: {params}'+(f'; note: {note}' if note else ''))
        parts.append('')
extra='''## Works with no quotable raw text obtained

- **Kimura 1962 (Genetics 47:713)**, **Kimura & Ohta 1969 (Genetics 61:763)**: free on PMC but automated download is blocked by a bot challenge; no abstract exists in PubMed/Europe PMC. No quotes recorded. The fidelity ledger's "accurate" verdicts for both rest on the pass-1 summarizer and are **unverified**.
- **Kimura 1983 p.44 ("2Nv new, distinct mutants")**: not located (Google Books API quota exhausted; no snippet). Unverified. Secondary lecture slides confirm only that k = (2N)(mu)(1/(2N)) = mu is the textbook derivation; those are not quotes from the book.
- **Haldane 1957**: not retrieved. The "about one allelic substitution per 300 generations" figure is confirmed only as reported in Nunney 2003 (quoted above).
- **Crow & Kimura 1970, ReMine 2005, Maruyama 1970/1974, Cannings 1974, Frankham 1995**: record only (paywalled or not retrievable).

## Derived numbers from Yoo 2025 supplementary tables (MOESM4.xlsx)

These are computed by the harvest agent from the xlsx rows (Python/openpyxl, no manual edits) and are NOT quotes. Method and file hash are in `bib-literature.md`; label any use `derived:`.

| item | value | how |
|---|---|---|
| Table III.14 mean autosome SNV divergence, chimp (mPanTro3#1/2) vs human (hg002#M/P) | 0.0146 (1.46%) | sheet "14", column "Mean SNV Div. Autosomes (A)" |
| same, bonobo vs human | 0.0146 | same sheet |
| same, human hap vs human hap (hg002#M vs #P) | 0.0016 | same sheet |
| Table III.14 mean autosome gap divergence, chimp vs human | 0.1247 (12.5%) | same sheet, "Mean Gap Div." |
| Table V.24 SDR total, human-specific (HSA) h1 / h2 | 147.8 Mb / 183.6 Mb | sum of `SDR_Size` by Lineage and Haplotype, sheet "24" |
| Table V.24 SDR total, chimp-specific (PTR) h1 / h2 | 288.9 Mb / 308.2 Mb | same |
| Table V.24 euchromatic SDR only, HSA h1 / h2 | 40.8 Mb / 81.6 Mb | rows with `SDR_Euchromatin` = TRUE |
| Table V.24 euchromatic SDR only, PTR h1 / h2 | 13.2 Mb / 20.1 Mb | same |
| Table XII.67 inversion rows (SYRI+PAV calls vs T2T-CHM13), all six apes | 1,175 rows | sheet "67"; main text says 1,140 curated inversions (>10 kb); chimp assembly contributes 171 rows (96 hom, 75 het) |
| search for 187 Mb or 410 Mb as any single or pairwise sum of the SDR totals above | no match (closest: HSA h2 + PAB h1 = 412.1) | brute force over lineage/haplotype totals; coincidence, not evidence |

**Observation, not a verdict:** the SI text of Note III says autosome SNV divergence for human-chimpanzee and human-bonobo "(0.15-0.16%)", whereas Table III.14 gives 0.0146, i.e. 1.46%, for the same pairs (0.0016 for within-human). The two differ by a factor of ~10; the table value is the one consistent with CSAC 2005's 1.23% total divergence order of magnitude. Not confirmed with the authors.

## Candidate values for `parameters.yaml` (from verified quotes only; nothing edited in that file)

| key | value | source quote above |
|---|---|---|
| divergence.t_div_years (new entry) yoo_2025 | 5.5e6-6.3e6 | Yoo 2025 main text |
| divergence.t_div_years langergraber_2012 | ">=7e6-8e6" (confirms existing entry) | Langergraber abstract |
| divergence.snv_differences_total chimp_consortium_2005 | 3.5e7 (confirms; add note: one copy each, includes polymorphic) | CSAC abstract + Genome-wide rates |
| divergence.indel_events_total | 5.0e6 (confirms) | CSAC abstract |
| new divergence.fixed_fraction_of_observed | 0.78-0.86 (polymorphism 14-22%) | CSAC Genome-wide rates |
| mutation.mu_per_site_per_gen pedigree_human | 1.1e-8 (Keightley), 1.20e-8 (Kong) | abstracts |
| population.Ne_ancestral_hc | 1.32e5 (HCG ancestor), 1.98e5 (HCB ancestor) per Yoo 2025; current entry [5e4,1e5] has no verified source | Yoo 2025 main text |
| selection.s_zeng_2021 | confirmed: 0.001, sign negative | Zeng abstract |
| haldane.gens_per_substitution | 300 (as reported by Nunney 2003; Haldane original unread) | Nunney abstract |
| population.Ne_over_N Frankham1995 | 0.1 (unverified here; abstract not retrieved verbatim) | - |
'''
open('/home/na/projects/evo-sim/docs/research/sources/quotes-literature.md','w').write('\n'.join(parts)+'\n'+extra)
print(len('\n'.join(parts)))
