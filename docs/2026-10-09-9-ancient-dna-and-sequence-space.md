# Milestone 9: Day's 21 on real genomes, and how many routes a mutation has
*2026-10-09 · stage: R4 (in progress)*

> **Update (later 2026-10-09):** the in-progress items below are reported in [milestone 10](2026-10-09-10-fairness-audit.md): X1 (one verdict rule for both sides; the Day-vs-critic error gap is not robust), GAP-07c (205M is 10.6–12.6× fixed events), the mapping round and the Holocene Nₑ retrieval.

This milestone covers three checks:
- **C1c:** what Day's ancient-DNA "21 fixations" would mean, in a model with the real sequencing depth of the ancient samples and the known ancestry turnovers in Europe;
- **C1d:** the same statistic computed directly on the real public genotypes (AADR), plus an independent replication of keruru's measured population size;
- **D1:** the first check on branch D, sequence space. It measures the number G1 left open: how many interchangeable routes there are per needed change.

Each check had its script and predictions committed before the main run, went through three reviews (correctness, Day-side steelman, critic-side steelman) and a fix pass. Every number below is after review. The ancient-DNA genotypes (about 7 GB) were downloaded and processed on a second machine (na-workhorse) only; host and checksums sit next to the raw outputs.

Also this round: **A3, the required-fixation count, is now marked load-bearing.** Day's root argument rests on it (ROOT P1, A P4), and the 205M-vs-events bracket from GAP-07b is the largest quantified factor in the audit.

## C1c: what would the 21 mean?
**The question.** Day's 2026 clock paper reports that, of 22,428 alleles that went from polymorphic to 100% in his European sample, only 21 did so in the last 6,000 years, against a clock expectation of about 630. The audit's earlier check (C1b) could not reproduce the statistic and guessed that sparse calls in the oldest samples were the reason.

- **Sparse calls are not the reason.** Mean depth in the three oldest time bins is 49, 62 and 282 chromosomes per site.
- **For Day:** at the textbook Holocene effective size (Nₑ ≈ 10,000), a neutral model predicts 1,500–3,900 post-6000 events, 70–190× his 21. Mixing in Anatolian farmers and steppe herders does not close the gap; at high Nₑ it widens it. keruru's own measured Nₑ (about 8,000–10,000) sits in the range where the 21 is a deficit.
- **For the critics:** a closed population of Nₑ ≈ 100,000–300,000, or growth from 10⁴ to 10⁶ within the window, gives 15–67 events, close to 21. Day's own turnover coefficient (d = 0.45) gives 739, so his parameter does not produce the 21 either.
- **Against both:** no model setting reproduces his eligible count, his profile across time bins, his tracked fraction and his start table together. What the 21 means turns on the Holocene Nₑ, which nobody in the repo has sourced. A retrieval of the published estimates is in progress.
- **Corrected in review:** an early "thousands" result came from giving the modern samples the same uneven coverage as the ancient ones; it was withdrawn.

## C1d: Day's statistic on the real genotypes
**The question.** Rather than model the data, run Day's stated method on it. The AADR genotypes (releases v62.0.p1 and v66.p1) were rebuilt into his European sample: 8,808 individuals against his 8,738, within 1–5% per bin.

- **Against Day:** his method, read literally, gives **62,757 eligible alleles and 4,957 events after 6,000 BP** (v62; v66: 48,888 and 3,649), against his 22,428 and 21. 132 variants of the method do not close the gap. His second paper documents a different pipeline; it reproduces his sample (1,377 / 683 against 1,372 / 680) and his SNP count (to 0.02%) but not his event total (63,631 against 17,814, 3.6×). No analysis code was found on Zenodo, GitHub or OSF; the "scripts available" sentence is in the second paper and may mean "on request".
- **Not damage.** 98% of the excess events are transitions, the class ancient-DNA damage inflates. A test by library preparation, with matched random controls, shows the excess is not concentrated in damage-prone libraries. What it is remains open.
- **For Day:** his start-frequency table reproduces to 0.4 points on v62, and his description of the events as completions of alleles already near fixation is right in kind (98.8%). Counting only transversions, the damage-resistant class, gives 36–44 events on autosomes, the same order as his 21; whether that is below a neutral expectation is open.
- **keruru, replicated.** His temporal Nₑ replicates within 1–8% in two releases (7,812 and 9,672 against his 8,139 and 9,835). His sampling correction is half the standard one for pseudo-haploid data; fixing it raises his numbers by 7–19%, in the direction he disclosed. The estimate is a lower bound on a drift Nₑ.
- **keruru against Wright's formula.** For Wright's 4N/(Vₖ+2) to hold, 83% of the measured drift would have to be something other than drift at a census of 10⁵, 98% at 10⁶ and 99.8% at 10⁷. "Three orders of magnitude" rests on the unsourced 10⁷ census and is not established; a gap of at least about 6× survives at any census of 10⁵ or more. Day's own Nₑ ≈ 2 is excluded by the data.

**Verdicts.**
- **C6 (Day's 21):** external moves from *untestable* to *contradicted*, as stated, under his described method. His best defence is that the method is underspecified (it gives no damage, quality, coverage or country rule); the verdict reopens as *contested* if he documents a pipeline.
- **C7 ("no drift in 7,000 years"):** external *contradicted* for "no allele-frequency movement". Whether the movement is drift or admixture is open.
- **C5b (keruru's Nₑ):** *holds* (the factor-of-2 slip goes in the slip ledger under the new single verdict rule: under 25% and it doesn't change his conclusion) / *supported* as a lower-bound measurement.
- **B2e (keruru vs Wright):** *contested*.
- **C (Day's two-period completions):** unchanged, *contested*. It concerns alleles starting at intermediate frequency, which neither check addresses.

## D1: how many routes per needed change?
**The question.** G1 showed that Day's "specific outcome" product p^n stops binding once each needed change can be met in enough interchangeable ways: about 7–17 successful arisings per change, or roughly 15–36 alternative mutations at Day's own parameters. D1 measured that number in two stand-ins: RNA folding (ViennaRNA) and real lab mutation scans (114 ProteinGym datasets plus the complete four-site landscape of the protein GB1).

Because the steelman reviews disagreed about which reading of "the same needed change" counts, the result is shown along that axis:

| Reading | Alternatives | Against the flip |
|---|---|---|
| Exact same RNA structure | 1.5–2.3 one-step routes when any exists | far below (λ ≈ 1) |
| Within 2 base pairs of it | 3.4 | below |
| Same RNA shape, without simply losing a helix | 11.8 (long molecules) | below at s = 0.01; reaches it at s ≈ 0.013–0.03 |
| Tolerated substitutions at one protein site | 5 of 6.6 | below; these are "neutral noise" in Day's own dilemma, not alternatives |
| Beneficial substitutions at one protein site | 0.21 | far below |
| Beneficial substitutions anywhere in a gene | 51 (median; 0–1,760) | above, but shared by every change that gene needs |

- **For Day:** if the need is a specific outcome at a specific site, there are about 1–6 routes, so his multiplication holds there. In GB1, 95% of variants don't work, and at single-letter steps the landscape has 67–158 local peaks; only 30–51% of working variants can climb to the best one. "Reduce or destroy", as he wrote it, holds in 61% of datasets. A short locus cannot drift its way to a useful starting point either: it needs a median of 36–80 neutral steps and gets 0.03–0.06 in the time available.
- **For the critics:** 71% of single mutations keep at least half of function, and "destroy" alone is a majority in only 2% of datasets. GB1's working variants form one connected network, and 98.5% have an uphill single-letter neighbour. RNA neutral networks are enormous (about 10³³ sequences for a tRNA shape). Within genes, the beneficial fraction exceeds G1's requirement by 82–1,600× for up to 2×10⁵ needed changes (an upper bound).
- **The shared pool.** A gene's beneficial mutations serve every change that gene needs: with 51, a gene needing 10 changes succeeds almost surely at s = 0.01, one needing 25 succeeds 7% of the time, one needing 50 essentially never, and at s = 0.001 even 10 fails.
- **Untouched:** how rare function is among random sequences (Axe, Taylor, Keefe–Szostak), connectivity between protein families, and regulatory waiting times.
- **Corrected in review:** two pre-registered "this would change the reading" triggers had fired without being acknowledged; a "Day's m ≈ 1" line came from the audit's own notes, not from Day; counts pooled across genotypes were withdrawn as a supply of routes.

**Verdicts.** D1d (Camestros: the post-1966 literature exists) moves to *supported* for that existence claim. D2h (Day: deep mutational scans show ruggedness) stays *contested*, with partial support as worded. The rest of branch D is unchanged and annotated; G3b's open item now carries the measured numbers.

## In progress
- **X1:** an arithmetic audit of every critic and ally number, plus one written verdict rule applied to both sides. The fix pass is done; a blind audit of how the rule was applied is running. It found that critic slips cluster in sourcing and units rather than arithmetic, and that the gap in error verdicts between the sides persists under one rule; the blind audit tests that.
- **GAP-07c:** the share of human–chimp differences still polymorphic in humans (15.6% for single-letter differences, from 1000 Genomes); reviews running.
- **XT:** core results re-run in a second simulator (fwdpy11), as the plan requires.
- **D15:** Hössjer's claim that coordinated regulatory changes take far more than 9 million years.
- **Holocene Nₑ:** the published estimates that decide the C1c reading.
- **Mapping:** the 41 critic and ally arguments not yet placed in the argument map, and the missing parts of the Hancock video.

## Where things stand
```
R0 ██████████  R1 ██████████  R2 ██████████  R3 ██████████  R4 █████████░  R5 ░░░░░░░░░░
```
- **Argument map:** 293 typed objections, 196 dated versions, 204 claims, 31 load-bearing.
- **Surviving their objections:** 111 as argued; 162 under a strict reading of the audit's verdicts; 120 under a lenient one.
- **Checks reviewed:** 27.
