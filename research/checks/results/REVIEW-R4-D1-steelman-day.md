# Review of R4 D1 (sequence-space spike): Day-side steelman

Reviewer role: argue as strongly as honestly possible for Day, then judge fairness.
Files read: `R4-D1-spike.md` (cited "D1 §n"), `d1_sequence_space_spike.py` (pre-registration docstring and code), `d1_posthoc_refine.py`, `d1_posthoc_gb1_snv.py`, `raw/d1_aggregate.txt`, `R4-G1.md`, claims D, D2c, D2h, D2i, D3, D4, D10, D11, D12, D15, G3b, and `quotes-day.md`. `sources/raw` was read only as CSV; nothing downloaded was executed.
Verification runs: I re-ran the GB1 SNV reachability code on the ProteinGym CSV with the improvement margin varied (scratchpad copy, no repo file touched). See finding M7 and the G1 numbers in M3, computed from `scipy.stats.binom` and G1's q = 0.381 / 0.047.

## Overall judgement

The check is more careful than most in this audit. It pre-registers, it discloses what it saw, and it removes a real artefact (E2) at its own cost. Its §6 and §7 credit Day correctly (70% of RNA single mutations change the structure, GB1 95% nonfunctional, 87 SNV-level maxima, locus-level λ about 1–6). The two-sided intent is visible.

Where it is not fair to Day is **in what the headline shows**, not in the arithmetic. Four things tilt it:

1. The only critic-favourable headline rows (functional alternatives at a codon, gene-level beneficial proxy) answer a question Day did not ask, or use a unit he did not use.
2. Day-favourable numbers that the scripts **did** compute are absent from the report: RNA exact-outcome far from S1 (post hoc `E0far`, m|reach 1.5), the DMS per-codon beneficial count (0.21, λ 0.10), and the unconditional exact-outcome m (0.05).
3. "Day's m ≈ 1" is a strawman built by the checker, and the report then marks it "too low".
4. GB1, the one dataset that tests multi-change ruggedness (Day's strongest empirical result), is missing from the §0 headline.

None of these is a BLOCKER. All can be fixed by editing the report and rerunning no code, except M3 and M5, which need a small post hoc computation.

---

## MAJOR findings

### M1. The "functional alternatives" rows are tolerated substitutions, which is Day's second horn, not alternatives to a needed change

**What the report says.**
- §0 table, row 8: "Functional alternatives at one codon (nonsynonymous SNVs, s*≥0.5) | DMS, 114 non-stability sets | **5.1** of 7.0 [2.5–6.5] | – | 2.4 | below".
- §0 reading, bullet 3: "Day's m ≈ 1 is too low even … for DMS codons (5 of 7)."
- §6 critic credit: "Destroyed singles are a median 11% … Fully intolerant sites are rare (4%)."

**What Day wrote** (G3b, voxday.net 2026-10-01 ¶28): "Either the specific fixations matter — in which case the Darwillion applies — or they’re interchangeable — in which case they’re neutral noise that can’t explain the observed functional divergence."

**The problem.** A substitution that retains at least 50% of WT activity is by construction a tolerated, near-neutral change. The report's own definition says so (§2: "functional s* ≥ 0.5"). Interchangeable tolerated substitutions are precisely what Day's second horn calls "neutral noise". They are not alternatives that satisfy a *requirement*. G1's middle case needs interchangeable alternatives that are each beneficial enough to arise and fix with q = 0.381 at s = 0.01 (G1 §3: "each alternative independently succeeds (arises *and* fixes in the window) with probability q"). A variant at 50% of WT cannot do that. Applying λ_alt = 0.48 to it is a category slip, and the report's "λ 2.4" for that row is not a G1 quantity.

The slip is harmless to the sign of the conclusion (it still lands below the flip), but it hands the critics a "5 of 7" headline that is not about needed changes. It also feeds the §0 statement that Day's m ≈ 1 "is too low".

**The Day-favourable number that is the correct one is already computed and not shown.** `raw/d1_aggregate.txt`, last block:
`ben_proxy_1.2: m_snv per codon med 0.206 [0..2.6] -> lam@0.48 0.10`.
The beneficial proxy is the closest DMS stand-in for "a needed adaptive change at this codon". Its median per-codon count is 0.21, which is below 1. (A grep of the report finds no "0.206" or "per codon … beneficial".) The lower quartile is 0 beneficial alternatives at any nonsynonymous SNV of the codon.

**Fix.**
- Relabel the §0 row: "tolerated (neutral-class) substitutions at a codon; not alternatives to a needed change; this is G3b's neutral horn".
- Add the row "beneficial-proxy SNVs at one codon (the needed-change analogue): 0.21 [0–2.6], λ 0.10, far below".
- Reword §0 bullet 3 to say that for needed (beneficial) changes at one codon the DMS count is below 1, which is **less than** Day's m = 1, not more.

### M2. "Day's m ≈ 1" is the checker's construction; the report scores it as too low while omitting that the unconditional and far-from-S1 numbers are at or below 1

**What the report says.** §0 reading, bullet 3: "Neither side's strong form is supported. Day's m ≈ 1 is too low even for exact-structure RNA (m∣reach about 2)". The pre-registration docstring writes the Day model as "each requirement has m ~ 1 (the specific mutation)". No Day quote supplies m = 1; the nearest Day text is the "specific" horn of G3b above.

**Omitted facts, all in the repo's own output.**

| Quantity | Source | Value |
|---|---|---|
| Exact S2, unconditional mean over (genotype, outcome) pairs (m_all) | `d1_aggregate.txt`, E0_uniform | median **0.051** [0.007–0.112]; λ 0.024 |
| Exact S2, reach | same | 1.8% [0.5–3.0]. 98% of pairs have **no** one-step route, even though S2 was drawn from outcomes known to be accessible |
| Exact S2 at least 5 bp from S1 (post hoc `E0far`), m∣reach | `d1_aggregate.txt` "post hoc refined classes" | **1.5** [1–2.27]; p90 = 2; tRNA = 1.0; L ≥ 76: 1.5, reach 0.15% |
| E0far pooled over K = 40–60 genotypes | same | **0.12** (median; <1) |

`E0far` strips the frayed one-or-two-base-pair neighbours that the E0 pool contains (`d1_posthoc_refine.py` docstring: "E0's pool contains many near-S1 frayed structures"). It is the cleanest test of "the specific outcome" and it gives m|reach 1.5, λ 0.72. That is the closest the check comes to testing Day's literal "specific outcome", and it returns about Day's value.

The report ran `E0far` and reported the analogous refinements for E2 (E2g, E2rare), which lower the critic-favourable number, but **not** `E0far`. `grep E0far R4-D1-spike.md` finds nothing. The omission is one-directional, even if unintended.

The "m|reach about 2" is also conditional on reach, and the report concedes the unconditional chance "is lower" (§2) only in a methods paragraph. When the claim is about a needed change, a 98% probability of no one-step route is the load-bearing number.

**Fix.**
- Report `E0far` in §0 and §3.3 beside E0, E1 and the refined E2 classes.
- Add a column "m_all (unconditional)" to the §0 table.
- Replace "Day's m ≈ 1 is too low" with: "For an exact outcome at least 5 bp from S1, the per-genotype count is 1.5 given a route (p90 2) and 0.05–0.001 unconditionally; Day's single-route picture is a fair description of this class. The deviation from 1 is upward only for fraying-type neighbours."
- State that "m ≈ 1" is the audit's rendering of Day's "specific" horn, not a Day quote.

### M3. The gene-level "at or above the flip" is computed with a pooled-alternatives λ that ignores how many adaptive changes a gene must supply, and mixes a locus-level n_f with a gene-level m

**What the report says.** §0 row 10 and reading bullet 2: "Beneficial-proxy SNVs anywhere in the region (s*≥1.2, an upper bound) | DMS | **51** [0–1,760] … above at s=0.01 and T=3e5"; "Gene-level 'any beneficial change in this region' needs sit at or above the flip, but the number is soft." §6 part 2: "Per-gene … about the flip."

**Problem A: the unit.** G1's model has n_f separate requirements, each met by one of m alternatives, so a gene is **one** requirement only if one adaptive change is all that gene needs. Day's count is differences: "approximately 205 million required fixations" (A3a); G1 uses n_f = 1e3 to 2e7. The gene pool of about 51 beneficial changes is *shared* by every requirement in that gene. If a gene must supply k adaptive substitutions, the right quantity is P(at least k of m alternatives succeed), not (1−e^−λ) per requirement with λ = 0.48 × 51 for each of the k. I computed this with G1's q (Binomial(m = 51, q)):

| Basis | k = 10 needed | k = 25 | k = 50 |
|---|---|---|---|
| q = 0.381 (T = 3e5, s = 0.01) | P ≥ k = 0.999 | 0.073 | 4e-20 |
| q = 0.047 (T = 3e5, s = 0.001) | 1e-4 | – | – |

Since the median is 51 and the lower quartile is 0 (so a quarter of datasets give no beneficial change anywhere in the region), a gene-level pool is exhausted at k of 25 or more adaptive substitutions per gene, or at s = 0.001 with k as low as 10. This is the "stepping-stone / diminishing returns" direction G1 already flags (G1 §3: "Stepping-stone dependence … would lower the effective m"), but D1 does not apply it to the one place it matters.

**Problem B: the proxy.** The same generous bound is stated as "an upper bound (assay noise inflates it)". Whether it is inflated by noise is untested. With no replicate noise estimate and no mirror-image null (fraction at s* ≤ 0.8 among near-WT sites), the 3.6% could be mostly noise, mostly lab-assay gain with no field fitness effect (ProteinGym sets are chosen for assay gain, binding, expression), or real. A lab assay "beneficial" at 1.2 × WT-like level does not map to s = 0.01; the report's own §7 says "lab benefit is not natural fitness". The number should not support a headline cell labelled "above".

**Problem C: spread.** The 51 is a median of a distribution that runs from 0 to 1,760 (IQR). The report's own aggregate says only 66% of datasets reach m* = 15 at n_f = 1e3 and 18% reach 151 at s = 0.001. The spread is wide enough that "at or above the flip" holds for about two-thirds of genes at the most favourable basis, and about one-fifth at s = 0.001.

**Fix.**
- Present the gene-level result as a k-of-m table (above) rather than as λ against λ₅₀, and say that the answer depends on adaptive substitutions per gene.
- Show the dataset shares (66% / 56% / 18%) alongside the median.
- Add the noise null (mirror fraction) or demote the row to "not interpretable as m".
- Say that the headline "at or above the flip" holds only for k of about 10 or fewer adaptive substitutions per gene at s = 0.01.

### M4. DMS verdict splits Day's disjunction and then reports half of it as unsupported

**What Day wrote** (D2h, voxday.net 2026-10-06 ¶5): "Single-residue changes to most proteins tend to reduce or destroy function. The fitness landscape is rugged, not smooth. Eden’s 1966 concerns about the rarity of functional proteins in sequence space have been confirmed by subsequent experimental work, not refuted by it."

**What the report says.**
- D1 §4.1: "**'Reduce':** supported … **'Destroy':** not supported as a majority statement."
- §9: "the harvest can now say 'supports "reduce", not "destroy"'".
- §0 headline: "DMS supports 'reduce' but not 'destroy'" (the task summary).

**Problem.** "Reduce or destroy" is a disjunction. "Reduced" in the check (s* < 0.8) contains the destroyed class (s* < 0.2). The check's own pre-registration read it that way: P7 says Day's wording "is literally true for a majority in about half of datasets". The result (61% of non-stability datasets with a majority below 80% of WT-like) is therefore **a pass of the claim as worded**, with "most proteins" met at 61% > 50%. Day never claimed that a majority is destroyed, so scoring "destroy" as "not supported" tests a claim he did not make. The §9 wording would be copied into D2h's external verdict comment and reads as a partial refutation.

**Honest counterweights** (also missing, and they must be stated for balance):
- The independent anchor is the 54 author-cutoff sets: median fit fraction 0.67. By that measure most singles are *fit*, so "tend to reduce or destroy" fails there. The check's s* < 0.8 criterion is generous to Day because "reduced" at 79% of WT-like is still functional, and assay noise puts some near-WT variants below 0.8.
- The 53% "reduced" is relative to a W_hat built from the most tolerant quartile of sites (§2), so 25% of sites are near-WT by construction.

**Fix.** Rewrite as: "As worded ('reduce or destroy'), supported by the check's criterion (61% of datasets; median 53% reduced below 80% of WT-like). By the authors' own cutoffs a majority of singles are fit (0.67). 'Destroy' alone is a minority in 98% of datasets, but Day did not claim a majority." Give both numbers in the same cell. Keep "internal/fidelity" unchanged; this is an external-evidence comment.

### M5. The check does not test Day's actual D2h/Eden claim (rarity of function with distance and ruggedness across multiple changes), and the one dataset that does is not in the headline

**What the claim says.** D2h: ruggedness "confirms Eden" and "concerns about the rarity of functional proteins in sequence space have been confirmed". D (Wistar frame) is a statement about multi-change search from sequences far from function, and the D claim file's own pre-registration says the decisive DMS evidence is p(neighbour functional) and percolation. Eden's dichotomy (D3b) is path length versus abundance.

**What D1 measured.**
- The DMS survey is **single substitutions only**. `load_dms` drops all multi-mutants (`if ":" in m: continue`). ProteinGym v1.3 carries double and higher-order sets. Rarity and ruggedness show up in how fast functional fraction decays with the number of substitutions, which a one-step survey cannot see. The report acknowledges that "one-step data cannot test" ruggedness (§4.1) but then reports the 71% single-mutant functional fraction as the main DMS finding.
- GB1 four-site data is the only multi-change test. In it: 95.0% of 149,360 variants are below 0.3 of WT; only 3.9% are functional; 53% of the 76 WT single mutants are below 0.2 (compare the survey median of 11% destroyed for whole proteins); and at the SNV level 87 functional local maxima and **only 44%** of functional variants have a strictly uphill path to the global maximum (§4.2).
- **GB1 does not appear in the §0 table or in the "Reading, kept neutral" bullets.** The reader of §0 sees the 71% functional singles, the RNA numbers and the critic-favourable gene-level cell. The 95% / 44% / 87 appear first in §4.2 and as a bullet in §6.

The GB1 interface sites were chosen for strong epistasis (the report says so, §7), so it overstates typical proteins. But that is also a reason it is the right place for ruggedness to appear; the 71% single-site tolerance and the 95% four-site nonfunction are both measured in the same family (GB1 itself: 0.783 functional in the Olson 2014 single survey vs 3.9% across four sites). That contrast is the Day-side result in the data: per-site tolerance compounds fast.

**Fix.**
- Put GB1 in the §0 table and in the reading ("95% of the four-site space nonfunctional; at SNV granularity 44% of functional variants reach the best by an uphill walk").
- Run (post hoc, labelled) the ProteinGym multi-mutant sets that exist: fraction functional for doubles versus the product of the singles' functional fractions (negative epistasis reading). Report the decay with substitution count.
- Add one line: "Axe, Taylor and Keefe & Szostak (D10–D12) and Hössjer's regulatory waiting time (D15) are untouched by this check; the 71% is a statement about one-step neighbours of an optimised protein". It is already in §7 but should be in §0.

### M6. Pooling across neutral genotypes assumes a population that no real population is

**What the report says.** §0, after the table: "Pooling over the K = 40–60 neutral genotypes I sampled raises the RNA counts: exact S2 2.1 (uniform) to 30 (frequency-weighted); topology-class E2g 207 … That is a population quantity (it presumes many distinct neutral genotypes segregating at once), not the per-genotype m." §6 critic credit: "tens to thousands pooled across genotypes".

**Problem.** The disclosure is correct and is to the report's credit. But it understates how far the pool is from a population:
- §3.1 says the sampled genotypes differ from each other at **0.56·L** positions on average (random pair 0.75·L). `d1_aggregate.txt`: "Hamming mean/L among samples … med 0.561; seed->last med 0.592".
- A species differs at roughly 1e-3 of positions. The pooled sets are 500 times more diverged. Standing variation within a population can open only the one-step neighbourhoods of near-identical genotypes, which overlap almost entirely. Pooling over 56%-divergent sequences is closer to "alternatives across homologs", i.e. the connectivity-across-families assumption that Day disputes (that functional sequences form one network at all), not "standing variation".
- The §6 credit line then counts the pooled numbers as a critic point ("tens to thousands pooled across genotypes") alongside per-genotype findings.
- Each real mutation arises in one individual against one genotype (m with K = 1 is the right single-arising quantity). The pooling assumption is the point in dispute.

**Fix.**
- Delete or heavily qualify "tens to thousands pooled across genotypes" in §6's critic credit.
- Add a pooled count over genotypes within a realistic divergence (for example, genotypes within 1–5 substitutions of one another; derivable from the same neutral-walk code with short walks), and report that alongside K = 40–60.
- State plainly that the K = 60 pool is a "neutral network of homologs", which presupposes the connected network that the check cannot prove (§3.1: "This is not proof of one connected component").

### M7. Some Day-favourable features are not carried into the headline or are not stress-tested symmetrically

Group of related points that, taken together, show the tilt.

(a) **Post hoc refinements run in one direction in the text.** E2 → E2g, E2rare appear (they lower critic-favourable numbers, correctly). E0 → E0far (which lowers critic-favourable numbers further) is not reported (M2). I do not suspect intent; the effect is that the displayed table has only one kind of tightening.

(b) **GB1 sensitivity, checked by me and found robust.** The ruggedness numbers depend on the "improvement margin" 0.1 (a variant counts as having an uphill neighbour only if it is higher by more than 0.1 WT). I varied it:

| margin | local maxima among functional | functional variants reaching the global max by an uphill SNV path | functional with an uphill neighbour |
|---|---|---|---|
| 0.0 | 67 | **51%** | 98.8% |
| 0.05 | 79 | 47% | 98.6% |
| 0.1 (reported) | 87 | 44% | 98.5% |
| 0.2 | 109 | 37% | 98.1% |

So the result is a bit margin-dependent but is not an artefact of the 0.1 choice. At margin 0 the "< 50% reach the top" pre-registered prediction (P11) is marginally missed (51%). The report should show this range; it strengthens a result that currently looks fragile to a reader who sees one number. It is also fair to critics to note that 98.5% of functional variants have at least one improving neighbour, so the 87 maxima are 1.5% of the functional set.

(c) **The SNV-union adjacency is permissive.** The report states this ("upper bounds on reachability"). A single real genotype has fewer SNV neighbours than the codon union, so true reachability is lower than 44% and true ruggedness higher. The report states the direction correctly but does not put it in §0.

**Fix.** Add the margin sensitivity (two lines) to §4.2. Say in §0 that SNV-level ruggedness is robust to the margin choice (maxima 67–109; uphill reach 37–51%).

---

## MINOR findings

### m1. "Functional at ≥ 50% of WT" is lenient, and this is not in the same place as the numbers that use it
D1 §2: "Thresholds are my choices: functional s* ≥ 0.5". Natural selection at N_e about 1e4 purges variants at s of about −1e-4; a 50% loss of assay activity is not selectively invisible, whatever the assay's saturation. §7 says "DMS … saturating selection, WT buffered by design" favours the critics, which is right. But the 71%, 5.06 of 7 and 13.5 of 19 numbers are quoted in §0, §4.1 and §6 without that caveat attached. Put a second set of numbers at s* ≥ 0.8 beside them: the aggregate already has them (`nearWT_0.8: m_snv per codon 3.51 [1.51–5.74]`, λ 1.69; gene-level 764). The 0.8 row reduces the "5 of 7" headline to 3.5 of 7 with no extra computation.

### m2. Author-cutoff cross-check is underused
The 0.67 (author cutoff) versus 0.71 (s* ≥ 0.5) cross-check is called "reassuring". The same cross-check supports a Day-side point (0.33 of singles are unfit by the authors' own cutoffs in 54 sets) and a critic point (0.67 are fit). State the 0.33 as well as the 0.67.

### m3. RNA "pair-partner redundancy" caveat is right, but the direction is not applied to the table
§7 says RNA partner redundancy "inflates m_E0 relative to protein residues … Favours the critics". Then the table (§0) row 1 is not marked with this direction. A reader will take "2.3" as a generic exact-outcome number. Mark RNA rows "(upper bound for proteins; partner symmetry)" in the table, and cross-reference E0far, which removes much of the fraying (M2).

### m4. "RNA's own gene-level analogue (m_ben …) points the same way" (§6.2)
The graded `m_ben` count at d0 ≥ 11 is "partly bookkeeping" by the report's own words (§3.4: "Removing any wrong pair lowers d_bp"). It should not be cited as independent support for gene-level λ being high. Remove or state that it carries no weight.

### m5. The tRNA datum is the closest to a selected, specific structure and has the smallest m
tRNA76: E0 reach 0.5%, m|reach 1.5 (E0far: 1.0), pooled 0.29 over K = 60. The report gives this in a table cell and a caveat row ("Favours Day for selected, specific structures"). Since the other 14 targets are random-sequence-derived, biased to common structures (§2 itself says so), the median over 15 is a critic-leaning summary of the specific question. Report tRNA separately in §0.

### m6. WT = 1 and GB1 functional threshold
"WT = 1 normalisation was assumed (not checked in the file)" (§8). It affects every GB1 count (functional ≥ 0.5 is 3.9% vs, say, ≥ 0.3 or ≥ 0.8). Show GB1 at two thresholds (the data are in memory), and note that the quantile disclosure (median 0.003, 95th percentile 0.31) makes WT = 1 very likely correct because the score is a ratio. A quick sensitivity table closes this at no cost.

### m7. Fidelity of the framing to Day's terms: "specific outcomes"
The task asks whether the check tests "specific outcomes". Day's G3b text speaks of "specific fixations" and the Darwillion, which is a pre-specified list. `E0far` / exact-S2 is the right analogue; E2 (topology) and the DMS functional rows move toward the interchangeable horn. The report's §0 table interleaves them without saying which is which Day horn. Add a column "Day horn: specific / interchangeable-neutral / middle (beneficial & interchangeable)". Under that column only the gene-level beneficial proxy is a middle-case row, and it is the one M3 weakens.

### m8. "Neither side's strong form is supported" is a symmetric-sounding sentence on asymmetric evidence
The critics' strong form ("the barrier vanishes") is rejected at locus level; Day's strong form ("m ≈ 1, rugged, isolated") is rejected only through (i) the conflated DMS rows (M1), (ii) the conditional-on-reach RNA figure (M2), and (iii) the GB1 giant component. Of these, (iii) is solid and the others are weaker than the sentence implies. Reword: "Day's strong form (functional sequences isolated) is not supported in GB1 (one giant component of 99.8%); his weaker form (locus-level m of about 1, SNV-level ruggedness, multi-change nonfunction at 95%) is supported."

---

## What the check gets right for Day (so the final text keeps it)

- Exact-structure λ of about 1 (E0: 1.1; E0far: 0.72), against a flip of 7–17, and the 98% "no route" rate.
- 70% of single mutations change the exact structure; paired sites are 9% neutral.
- GB1: 95% nonfunctional at four sites; 87 functional local maxima at SNV level; 44% (37–51% over margins) of functional variants cannot reach the best by an uphill walk. Day's "rugged" is true in this subspace.
- 61% of DMS datasets have a majority below 80% of WT-like.
- A candid "Credit" list in §6 and an explicit list of caveats in §7.
- Correct handling of E2: the degradation artefact is identified and the pre-registered failure (28 vs 2–12) is reported as a failure.
- Honest statement that the Axe/Taylor/Keefe-Szostak regime and regulatory sequence (D10–D12, D15) are untouched.

## What the check gets right for the critics (so the fixes above stay balanced)

- GB1 functional set is one giant component (99.8–99.9%); isolated islands are essentially absent; 98.5% of functional variants have an improving neighbour.
- Destroyed singles are a median 11%, intolerant sites 3.8%.
- Neutral networks are huge (10^33 for the tRNA cloverleaf) and spread over sequence space.
- "Mostly deleterious" does not imply "rugged" (D2h Assumptions).
- At the pooled-gene level, the beneficial pool is non-trivial for a modest number of adaptive substitutions per gene.

None of the Day-side fixes above removes those points; M3 narrows the gene-level one to "k of about 10 or fewer".

## Suggested priority

1. M1, M2, M4 (relabel and add the missing rows; no new computation).
2. M5 and M7 (headline GB1; margin table already computed here; optional ProteinGym doubles run, labelled post hoc).
3. M3 (k-of-m table; mirror-null for the proxy).
4. M6 (qualify pooled credit; optional short-walk pooled count).
5. m1–m8.

Pre-registration note for any new run: write the predictions and the script commit before running; label as post hoc; the numbers in M3 and M7 were produced by this review on existing data and are scratch values, not results, and the author should recompute them in the fix pass.
