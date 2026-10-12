# Refresh 2026-10-12, Day side (since the 2026-10-11 pass)

Checked 2026-10-12 about 15:10-15:40 UTC (cut-off of the last pass: 2026-10-11 about 18:30 UTC). Procedure: `HOWTO-refresh.md`. Raw copies: `sources/raw/refresh-2026-10-12/` (gitignored; one directory per fetch). Read-only public access; nothing executed; no posting or contact. Critic side is a separate file by another agent. Nothing here changes a verdict; all verdict items below are proposals.

## Bottom line
- **One new relevant Day post:** "The Method is the Conclusion" (voxday.net, 2026-10-12 14:12:35 UTC, tags evolution, science, trainwreck). It is Day's follow-up to the dN/dS post: it changes the explanation for 0.80 versus 0.23 from gene curation (10-11) to "the protein-guided CDS alignment method has a circular reasoning problem", and adds a four-row gene-set table with new numbers (0.7989 on 20,400 genes; 0.7956, 0.7939, 0.8237 on subsets; 73.8-74.4% nonsynonymous). Q180-Q192.
- **Second new post, on topic but number-free:** "Natural Philosophy" (2026-10-12 05:01:10 UTC, tags evolution, philosophy, science): a relay of an unnamed third party's two-definitions argument on natural selection, with a short Day paragraph tying it to Veriphysics and the Triveritas. Q193-Q194 (RELAY, rule U).
- **No code, per-gene table, gene list, Zenodo deposit, methods appendix or correction** for either the dN/dS work or "The Fourth Mechanism". Zenodo "Day, Vox": still 39 records, every id, modified time and file md5 identical to the 2026-10-11 listing (0 new, 0 changed). The promised dN/dS paper is not there.
- **"The Fourth Mechanism" (10-10) re-fetched:** body text byte-identical (after whitespace normalisation) to the 10-10b copy (same sha256 of normalised text, d47f8cfb...). No new mesa numbers, no window size, no statistic named. Overdispersion ">80 times" is unchanged and still unparameterised.
- **"How Biologists Keep 'Proving' Selection" (10-11) re-fetched:** modified stamp still 16:35:43 UTC; text identical to the 10-11 copy apart from paragraph breaks in the diagnostic and "pattern" lists (the 10-11 extraction had run list items together). No edit.
- **Excluded Day posts:** "The Cracking Pillars of the Petrodollar" (10-12 11:36), economics. Sigma Game 10-12 "Avoiding Accountability", 10-11 "Destroying Hierarchy", 10-10 "The Significance of Alpha" (social, "alpha" here is not the adaptive fraction; title only, not opened); AI Central posts: off topic.
- **Not verified:** X, Gab, Telegram, Rumble, Locals, UATV/Darkstream recordings (where the machine results may be discussed), SG cross-posts of the three evolution posts, the dN/dS paper on any non-Zenodo host.

## What was checked
| Source | Result |
|---|---|
| voxday.net feed, 10 newest | 3 new posts (2 relevant) |
| voxday.net `/tag/evolution/` | lists the same two new evolution posts, nothing else new |
| Post pages: Method, Natural Philosophy; re-fetch of Fourth Mechanism and dN/dS post | fetched; two unchanged |
| Zenodo "Day, Vox" pages 1-2 | 39 records, ids, modified and md5 identical to 10-11 |
| Zenodo free text ("dN/dS", "mesas substitution", "GENCODE chimp Cactus", "Athos Vox") | no Day-related record; hits unrelated |
| Sigma Game, AI Central Substack archives (8 newest each) | nothing on evolution |
| X, Gab, Telegram, Rumble, Locals, UATV | inaccessible, not retried |

## Day items
| Item | Quote ids | Touches (claim files) | Type | Proposal |
|---|---|---|---|---|
| Alignment-circularity explanation | Q180-Q182, Q191 | DN3 (Consortium gene-set artefact), DN5 (CSAC 2005 value), DN1 | new mechanism claim, no test shown | new claim "protein-guided alignment biases dN/dS down" (side day, internal pending, external pending); retarget DN3 note: Day himself now says the gene set is not the cause |
| Gene-set table, uniform 73.8% nonsynonymous | Q183, Q184 | DN1, DN2 | new numbers | record rows as parameters (provenance Day, unreleased); nested sets, see Maths review |
| Reversal of the 10-11 explanation | Q185, Q186 | DN3, versions.md | self-correction (credit) / internal tension | versions row added; DN3 readings table (below) |
| Interpretation: canonical evidence "incorrect", near-neutral coding | Q187-Q189 | DN4, B (neutral theory), A2e-alpha | non-sequitur candidate unchanged | no new verdict; DN4 external text already covers it |
| Decoupling from MITTENS | Q190 | ROOT-FM, FM10 | scope statement (credit) | add to DN1/DN4 as a Day-side scope note |
| Rhetoric: Kevin Hart analogy; "how would anyone tell the difference" | Q191, Q192 | slips.md | RH | rhetoric tags, no verdict |
| Natural Philosophy (relay) | Q193, Q194 | ROOT philosophy-of-selection branch | relay | RELAY, rule U; not scored internal |
| Fourth Mechanism follow-up | none | FM3-FM10 | **no follow-up found** | FM10 stays `pending until Day releases method` |

## Maths review (light)
**1. Table arithmetic (Q184).** Gene counts: 16,995 + 3,405 = 20,400 (A = B + C, consistent). B-HC (15,937) is a subset of B. 20,400 - 13,454 = 6,946 and 6,946/20,400 = 34% ("one-third" in the 10-11 text holds); 20,400/13,454 = 1.516 ("51.6% more" holds). Gene-count-weighted mean of B and C dN/dS = 0.800 versus 0.7989 in A and weighted nonsynonymous fractions 73.9% match A: consistent (pooled values would weight by sites, so exact equality is not expected).

**2. "dN/dS" versus nonsynonymous fraction.** dN/dS is a per-site rate ratio; the table reports the fraction of substitutions that are nonsynonymous. The conversion needs the nonsynonymous-to-synonymous site ratio N/S: dN/dS = [f/(1-f)] / (N/S). Using Day's own pairs (my arithmetic, using only Day's numbers; not a replication): 73.9% with 0.7989 implies N/S = 3.54; 73.8% with 0.7956 gives 3.54; 73.8% with 0.7939 gives 3.55; 74.4% with 0.8237 gives 3.53; the single-SNV 71.6% with 0.71 gives 3.55. So every row uses one constant N/S of about 3.54, i.e. about 78% of sites nonsynonymous. This is a useful consistency check (credit: the numbers are mutually coherent, and the uniform 73.8% is a restatement of an essentially constant dN/dS, not independent evidence). Two cautions: (a) the usual Nei-Gojobori site split for the standard code is nearer 3:1 (about 75% nonsynonymous sites; background knowledge, not checked in fetched text). At N/S = 3.0 the same fractions give dN/dS about 0.94; Day's 0.80 depends on a site count he does not report. (b) Day's own "~40%" for the Consortium's 0.23 implies N/S = 2.9 (0.40/0.60/0.23); with N/S = 3.54 it would be 44.9%. A "~" figure, so a slip not an error (R1: does not move 0.23 or 0.80), but the two rows cannot use the same site ratio.

**3. What 0.80 means.** Not a different quantity from the 10-11 post: 1 - 0.7989 = 20.1% removed, 1 - 0.23 = 77%, ratio 3.8 ("nearly four times" holds). The statement "purifying selection removes one in five" uses the standard simplification and so inherits its limits: dN/dS averages over all sites, so it cannot separate strong constraint on a few sites from weak on many.

**4. Estimand mismatch (new, not in Day's text).** Day's table column is "Pooled dN/dS" (sum of substitutions over all genes divided by sum of sites). The published 0.23 is, as I recall (2005 paper not re-read this pass; unverified), an average of per-gene ratios over 13,454 orthologs. Pooled, mean-of-ratios and median per-gene values differ, so "same Nei-Gojobori method" does not by itself make the two comparable. This predicts that run on the Consortium list, Day's pooled number may not return 0.23 and the mean/median could still differ. It cuts both ways: it may be part of the gap (critic point) and Day has not reported the per-gene median on his own set (Day-side gap).

**5. Plausibility of 74% nonsynonymous.** If synonymous and nonsynonymous sites had equal substitution rates (dN/dS = 1) the nonsynonymous fraction would equal the site fraction, 78% at N/S 3.54 and about 75% at 3.0. Day's 73.9% is therefore close to the no-constraint value. Genome-wide values near 1 are what random mismatches from misalignment, mis-assigned paralogs or assembly errors produce, whatever the true constraint. A mixture of true signal (about 0.2) with a modest fraction of noise rises quickly toward 1. The test Day cites does not exclude this: the single-SNV-codon check (71.6%) fixes the classification of codons that were already aligned and does not test whether those codons were aligned to the right locus.

**6. Self-undermining numbers.** The 10-11 text says the strictest filter stack (no stop codons in either species, low gap frequency, minimum substitutions, length, outlier removal) left 10 genes out of 20,400. If the extraction were clean at 1.2% human-chimp divergence, "no stop codons in either species" alone should remove very few genes. Dropping to 10 implies most extracted coding sequences carry premature stops, large gaps or frameshifts, i.e. a noisy projection of GENCODE coordinates onto the Cactus alignment. That is Day-side evidence against "the data is complete, the code is correct" in the same post. Which filter did the removal is not reported.

**7. The circularity argument itself.** A protein-aware aligner scoring with a substitution matrix can, in principle, bias towards conservation when divergence is high (this is a recognised direction of bias for deep comparisons). Day's argument is a legitimate hypothesis (credit). For human-chimp, amino-acid sequences differ at very few residues (about 1% nucleotide divergence in total), so a gap penalty is unlikely to remove many codons for being "too divergent". The size of the effect is an empirical question Day can answer with one number he has not given: how many codons the protein-guided pipeline excludes that his Cactus pipeline keeps, and their dN/dS. Also unsupported: his description of how the 2005 Consortium produced alignments (protein-guided) was not checked here.

**8. Overdispersion (Fourth Mechanism), neutral expectations; no new data.** ">80 times more variable than a uniform-rate process predicts" is a variance-to-mean (dispersion) statistic without a window size. Under neutral evolution with ordinary rate heterogeneity (CpG content, replication timing, recombination, GC isochores, plus variation in ancestral coalescence times among loci) the index grows linearly with window size. Illustration (my arithmetic, assumed not sourced): a 100 kb window at 1.2% divergence has mean 1,200 substitutions and Poisson variance 1,200; a coefficient of variation of 0.3 across windows gives variance 129,600 and index 108; CV 0.2 gives 48; CV 0.5 gives 300. An index of 80 is therefore compatible with unremarkable heterogeneity at 100 kb scale. Without window size, expected index and a null built by permuting along the genome with matched local rates, ">80" cannot separate mesas from neutral heterogeneity. The lineage asymmetry within a mesa (human-lineage excess) needs a third-ape outgroup comparison, which the six-ape data allow, but Day reports no per-mesa numbers. Unchanged since 10-10.

## Tags and readings (rules RH and RD)
| Q | Tag | Reading A (most defensible to Day; verdict field) | Reading B |
|---|---|---|---|
| Q180-Q182 | dialectic | The alignment-score filter can bias dN/dS down; plausible and testable: external `untestable` until the excluded-codon count exists | Asserts the Consortium's 0.23 is wholly this artefact: `contested` (maths review 7) |
| Q183 | dialectic | Uniformity across subsets shows the gap is not gene-list driven: holds as arithmetic | Nested sets are not independent: no inference from uniformity |
| Q185 | dialectic | "their smaller subset" = the 1:1 ortholog sets B / B-HC in the table: holds, subset statement matches rows | The Consortium 13,454 list was rebuilt and run: no row, no number, fidelity `unverifiable`; then Q176's own test is answered in Day's favour only if the number is shown |
| Q186 (vs 10-11 text "only way to get 0.23 is a pre-selected gene set") | dialectic | Day revised after his own test showed gene sets did not matter; a correction (rule SC, same author, one day later: ledger, credit for the update) | Two incompatible explanations in 24 hours without noting the change; internal tension (no verdict change) |
| Q187 | dialectic | Arithmetic holds under the standard simplification | n/a |
| Q188, Q189 | dialectic | "compromised" and "near-neutral" as a statement about the dN/dS average: defensible if 0.80 stands | As statements about adaptive evolution: non-sequitur (DN4 reading already recorded) |
| Q190 | dialectic | Scope statement; credit | Second sentence overreaches ("impossibility") |
| Q191, Q192 | rhetoric | Device, function and dialectical core noted in the quotes; no verdict | |
| Q193, Q194 | dialectic, RELAY | Valid conditional form; antecedent contested | Not scored |

## Valid points
- Day (credit): the circularity hypothesis is clearly stated, falsifiable and names the observable that decides it (codons kept by Cactus but dropped by the protein aligner). He ran his own diagnostics and, when the gene-set test failed to explain the gap, changed his explanation instead of keeping it (Q185, Q186). He states the result is separate from MITTENS (Q190). Table values are mutually coherent (maths 2).
- Day-side gap: still no code, no codon counts, no per-gene median, no site counts N and S, and the result is the same unreleased number as 10-11.
- Critic-side (for balance, no critic has answered): the Consortium's 0.23 is not shown here to be an artefact; the nonsynonymous fraction is close to the value expected without constraint, which is also what alignment noise produces; the 10-gene filter result suggests noisy extraction.

## Verdict flags and proposals
Proposals only; no claim, hierarchy or argmap file edited.
- DN1 (0.80 on 20,400 genes): keep `pending`; note the table rows now exist with 0.7989 (supersedes "0.80" as the precise value).
- DN3 (Consortium gene-set artefact): Day now says the gene set is not the cause (Q186). Reading A (self-correction) is the most defensible to Day; propose the DN3 verdict follow Reading A (the claim in its 10-11 form is withdrawn by its author) with a Readings table (A/B above).
- New claim candidate: alignment circularity (Q180-Q182), side day, internal `pending`, fidelity n/a, external `untestable` until Day releases the excluded-codon count.
- Rule N check candidate: Q188/Q189/Q190 second sentence (average constraint to "impossibility"); same family as DN4.
- Slip ledger candidates: "~40%" for 0.23 vs N/S inconsistency (maths 2b); "Lebron" capitalisation and "Kevin Hart" are rhetoric, no entry.
- Test candidate (for the checks owner, not run): rerun the pooled and per-gene-median dN/dS on the 13,454 list and on 20,400 with both estimators; report codons gained or lost by protein alignment.
- FM10 unchanged.

## Inaccessible or unverified
X (@voxday), Gab, Telegram, Rumble, Locals, SocialGalactic, UATV and Darkstream recordings, SG cross-posts of the three posts, Reddit and Peaceful Science (not retried in this half). The 2005 Consortium paper was not re-read, so every statement of how it computed 0.23 is Day's, or my recollection and marked so. Who "Erika" is (Method post, opening) is not stated in the fetched text. Whether a Zenodo record appears under a name other than "Day, Vox" (e.g. Athos) was checked by free text only (no hit).

## Hashes (sha256)
| File (under sources/raw/refresh-2026-10-12/) | sha256 |
|---|---|
| post-the-method-is-the-conclusion/page.html | b765b0eb4152b358862a84898f987b27d61654b15571947e8f70d5378be59f50 |
| post-the-method-is-the-conclusion/body.txt (extracted) | c6b2c4db11b34a309599482587ecdd6ca44e0e088f0060c569a14729e534e0b9 |
| post-natural-philosophy/page.html | b9bf8e45e46243c7df3ef8f71bd04ffbd75428169fe9f3e09ffb6a172c205b4d |
| post-natural-philosophy/body.txt (extracted) | bf68100b798e4b146c9a75c4c15db8fee848e9bbd749541acbe5e7cab681dd53 |
| post-the-fourth-mechanism/page.html (re-fetch) | e7a4aa6ad995ce704a70e281477f6765c09c00a869de2c5b956116d9a4be78eb |
| post-the-fourth-mechanism/body.txt (extracted) | 5101ec122efff10eb5a3f4067e7e2cd75b02dace5df9e3b56fdf272bbaa589f5 |
| post-how-biologists-keep-proving-selection/page.html (re-fetch) | fec1f525f4031f58c4beb2c141bf66ceb6c710290a288c2e9bde3b3f4a05afb6 |
| post-how-biologists-keep-proving-selection/body.txt (extracted) | ecbc97115d7e80b47af0072e102c10b48d793f9e3ee755e4fc16446afbaf188d |
| feed/feed.xml | a90f30aeb8e97e1acd618dd4b394a7894e92af3f69752ce40ab4f6e64da8d243 |
| zen/p1.json | 9224b474ecf6c9abc254e09972322b68d1ba8ec7717fd0b71a161980a415b7f6 |
| zen/p2.json | 4453e253a51e67a27bf687e127720e2b1c5f68292034e23f6e518884d05a5f74 |
| tag/evo.html | 8319c2b0b96af06ebe0e2ef5971165661a953842ae6f2cfc20d012fca01d865c |
| sub/sg.json | 379a13b5cb0a0b913e888cce4b77f4980a3f771698f342f74b0ac76bdd1d7528 |
| sub/ai.json | 460af2fc48d2407eb23b9a53c7a16358744aa0871b3fbd7b7670b1527d76358e |

Note: Zenodo p1/p2 hashes differ from 10-11 (`2074df6d...`, `094cd187...`) because the JSON carries volatile fields (view counts, stats); the id, modified and md5 comparison is identical.
