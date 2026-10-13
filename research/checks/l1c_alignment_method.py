"""L1c: does the alignment method make human-chimp dN/dS 0.80 or 0.23? A head-on test of Day's "protein-guided
alignment gaps out divergent codons" mechanism (Q180-Q186), on the same T2T codons as L1b, with misalignment-noise
controls. PRE-REGISTERED: committed before the main run. Only the synthetic `selftest` was run before the commit
(workstation, 0.8 s, 38 MB RSS; 40 simulated genes, no real data). No dN/dS has been computed on real data by this script.

TIER. Not load-bearing by the ROOT path: docs/research/R5-draft.md lists no DN node, and hierarchy.yaml marks DN1-DN5
  `load_bearing: false`. Kept at L1/L1b's tier (three reviews: correctness, steelman-day, steelman-critic) because it
  decides the external verdict of the new alignment-circularity claim (proposed in refresh-2026-10-12-day.md) and
  can move DN1/DN3 together with L1b. A reviewer may downgrade to one combined review; nothing below depends on it.

TARGETS (verbatim; quotes-day.md; voxday.net "The Method is the Conclusion", 2026-10-12 14:12:35 UTC; RH tags as filed)
  Q180 (¶3, dialectic): "discovered that the protein-guided CDS alignment method has a circular reasoning problem
       that's impossible to ignore once you recognize it:"
  Q181 (¶7, dialectic): "Regions too divergent to score well get gapped out or are left unaligned, so they aren't
       counted."
  Q182 (¶10, dialectic): "Those excluded codons are enriched for nonsynonymous substitutions by definition, because
       that's why they scored poorly in the protein alignment."
  Q183 (¶13, dialectic): "It's 73.8% nonsynonymous across every subset we tested. The signal is uniform across the
       genome, it's not concentrated in problematic genes."
  Q184 (¶17-21): table rows A 20,400 / 0.7989 / 73.9%; B 16,995 / 0.7956 / 73.8%; B-HC 15,937 / 0.7939 / 73.8%;
       C 3,405 / 0.8237 / 74.4%; "Published (Consortium 2005)13,4540.2300~40%".
  Q186 (¶15, dialectic): "The difference is not a matter of gene selection, quality filtering, or computational error.
       It is a methodological artifact of using a conservation-dependent alignment to measure conservation."
  Q187 (¶15): "the whole-genome measurement of dN/dS = 0.7989 implies that only 20 percent are actually eliminated"
  Context, not targets: Q188-Q189 (interpretation; DN4 non-sequitur is not moved by any number here), Q190 (scope).
  Q191, Q192: rhetoric (rule RH): not tested.

WHAT THE HELD CSAC 2005 TEXT SAYS (read before registration, sources/raw/sources/txt/CSAC2005.txt, sha256 0b5abab3...;
  Methods, journal p. 83, "Gene annotation" and "Rates of divergence"; verbatim):
  "A total of 19,277 human RefSeq transcripts, representing 16,045 distinct genes, were indirectly aligned to the
   chimpanzee sequence via the genome alignment. After removing low-quality sequences and likely alignment
   artefacts, an initial catalogue containing 13,454 distinct 1:1 human-chimpanzee orthologues was created"
  "A subset of 7,043 of these genes with unambiguous mouse and rat orthologues were realigned using Clustal W"
  "K A and K S were estimated jointly for each orthologue using codeml with the F3x4 codon frequency model"
  "N S/N A, the ratio of synonymous to non-synonymous sites, estimated as 0.36 from the orthologue alignments."
  "Unless otherwise specified, K A/K S for a set of genes was calculated by summing the number of substitutions and
   the number of sites to obtain K A and K S for the concatenated set before taking the ratio."
  And the genome alignment (Methods, "Genome alignment"): "BLASTZ was used to align non-repetitive chimpanzee ...
   and only best reciprocal alignments were retained".
  Consequences fixed now (observations, not verdicts; integration decides):
  (i) Estimand: CSAC's 0.23 is POOLED (sums of substitutions and sites), like Day's "Pooled dN/dS" column. The
      pooled-vs-mean mismatch raised in refresh-2026-10-12-day.md item 4 is therefore not present for the 13,454
      value; the check still reports pooled, mean and median so the point is settled on these data.
  (ii) Alignment: the 13,454-gene 0.23 came from a nucleotide whole-genome alignment (BLASTZ, best reciprocal), not
      a protein-guided CDS alignment; protein-aware realignment (Clustal W) is stated only for the 7,043-gene
      four-species subset (the 0.20 value). The one step that could act as a conservation filter is "removing
      low-quality sequences and likely alignment artefacts" (criteria in the SI, not held).
  (iii) Site ratio: N/S = 1/0.36 = 2.78 (codeml F3x4, transition-aware). Day's rows imply 3.54 (maths review 2).
  (iv) The 13,454-gene list is SI Table S23, not held. It is NOT sourceable for this run; a proxy set CSACp is used
      (below). Queue item: fetch the CSAC Supplementary Information (public, Nature) and rerun on the real list.

DESIGN. One human CDS per gene (L1b's transcript rule), the same chimp material, several ways of pairing codons.
  Inputs are L1b's: the annotation (load_annotation), Ensembl one2one (load_orth), and L1b's segment dump
  (`seg.json.gz`: per transcript the hs1 CDS and every aligned chimp row of the hs1 Cactus MAF), so the MAF is not
  re-streamed. L1c runs AFTER L1b. All code for extraction, sites, path-averaged differences, JC and pooling is
  imported unchanged from l1b_t2t_dnds.py (0fe3c7f) and l1_dnds_genesets.py (868bb60).
  Arms (all keyed by human codon index, so every arm scores the same human codons):
    U0   Cactus nucleotide alignment, no protein guidance: L1b V0 (first chimp row per block), codons with any gap
         skipped (NG). Must equal L1b V0 exactly (audit A0).
    UG   U0, plus every codon within +-3 codons of a Cactus gap or chimp insertion removed ("gap-neighbourhood
         trimming", the Gblocks-style step that removes poorly aligned flanks).
    UT   gap-tolerant naive: L1b X1 (chimp bases concatenated without gaps, chimp insertions kept, compared
         position by position): what ignoring indels does. Upper bound of register errors in real data.
    P    protein-guided realignment of the SAME material: human CDS translated; the V0 chimp bases (insertions
         included, gaps removed, transcript orientation) translated in frame 0; global Gotoh alignment, BLOSUM62,
         gap open 11 / extend 1 (BLAST defaults), banded (half-width 32 + |n - m|, widened 4x and flagged if the path
         touches the band); back-translated to codons (as PAL2NAL / TranslatorX do). Gap codons skipped.
    PG   P + gap-neighbourhood trimming (+-3 codons around protein-alignment gaps).
    PF1  P + divergence trimming, lenient: a codon is dropped if the mean BLOSUM62 score over a 5-residue window
         centred on it is < 1 (gaps score -4). Correctly aligned windows with one or two replacements stay (mean
         ~3-4); misaligned or frame-shifted stretches (mean ~ -1) go. This is Day's Q181 step at a realistic setting.
    PF2  P + divergence trimming, strict: window 3, mean < 3. ADVERSARIAL upper bound: it drops codons around any
         radical replacement by design, i.e. it removes nonsynonymous changes because they are nonsynonymous. If even
         PF2 does not carry 0.80 to ~0.23, Day's mechanism cannot, at any plausible threshold.
    No external aligner is used: none is installed on the workstation, na-workhorse or in research/requirements.txt
    (checked 2026-10-12: no mafft, clustalo, muscle, prank, macse, codeml). The aligner (nw_banded, protein_align) is below and
    self-tested. Queue item (not needed for the verdict): repeat P with MACSE or PRANK+codon model if pinned later.
  Excluded-codon accounting (the observable Day names in Q182 and refresh item 7): for each of UG, P, PG, PF1, PF2,
    codons compared in U0 but not in the arm: count, share of U0 codons, Nd, Sd, sites, pooled dN/dS and
    nonsynonymous fraction of the EXCLUDED codons; and codons gained. Plus P-vs-U0 agreement (share of human codons
    paired with the identical chimp codon in both).
  Estimators (every arm, every set): pooled JC ratio (CSAC's estimand), pooled raw p ratio, mean of per-gene ratios
    (and capped at 2), median per-gene ratio, raw Nd/Sd, nonsynonymous fraction Nd/(Nd+Sd) and single-difference
    share (Day's 73.8% / 71.6% statistics). Transition-aware sites: S and N re-counted with transitions weighted by
    kappa in {1,2,3,4,5,6} (kappa = 1 is NG exactly; selftest), kappa-hat = 2 P/Q from fourfold-degenerate third
    positions on U0; pooled dN/dS and N/S reported at each kappa (tests 3.54 vs ~3.0 vs CSAC 2.78 directly).
  Noise controls (on U0, ALL; seeds random.Random(zlib.crc32((tid + arm).encode()))):
    NR(r)  uniform random substitutions in the chimp CDS at rate r per base, r in {0.002, 0.005, 0.01, 0.02, 0.05,
           0.10}: mis-called bases / assembly error. r* = rate at which pooled reaches 0.80 (linear interpolation).
    NM(f)  misregistration: in a fraction f in {0.1, 0.25, 0.5, 1.0} of genes, from a uniformly drawn codon on, the
           chimp sequence is shifted by one inserted random base (an unhandled 1-bp indel).
    NU     unrelated in-frame pairing: each human codon against the chimp codon half a gene away (circular shift by
           ncod // 2): what pure misplacement gives with real codon usage. The noise ceiling.
  Misalignment diagnostics (U0, per gene): nucleotide identity over compared codons; frameshift runs (Cactus gap or
    insertion runs not a multiple of 3, counted within segments); internal stops (human, chimp); QC failures (L1
    filters S, G, L; any of them); pooled dN/dS and nonsyn fraction by identity bin [>=0.995, 0.99, 0.98, 0.95,
    0.90, <0.90] and in HQ = identity >= 0.98 AND no frameshift run.
  Gene sets (membership fixed from U0 and L1b's diagnostics, the same for every arm): ALL; O121 (Ensembl one2one);
    SYN and O121SYN (L1b's synteny rule); CSACp = O121 AND SYN AND chimp coverage >= 0.95 AND U0 gap codons <= 2%
    AND no internal stop in either species AND >= 300 bp (proxy for "unambiguous 1:1 orthology ... high-quality
    sequence alignments covering virtually the entire coding region"; NOT the 13,454 list); HQ; NONHQ.

PREDICTIONS (fixed now; pooled JC dN/dS unless stated)
  DAY side (Q180-Q187 read as a claim about these data): U0 ALL ~0.80 (>= 0.65) with nonsyn fraction ~74% (>= 0.66);
    protein guidance plus divergence trimming lowers it to the published range: PF1 ALL <= 0.40, drop U0 - PF1
    >= 0.25; excluded codons nonsyn-enriched (Q182): excluded pooled dN/dS >= 2 and excluded nonsyn fraction > U0's;
    uniform across sets (Q183): O121, CSACp, ALL within 0.05; N/S (NG) ~3.5.
  CRITIC side: U0 ALL 0.20-0.35 and CSACp 0.18-0.30 (L1 hg38: 0.271 / 0.207); P within +-0.03 of U0; PF1 drop < 0.03;
    PF1 excluded share < 2% of U0 codons; P-U0 codon agreement >= 98%; high values only from noise: NU nonsyn
    fraction 0.68-0.80 (Day's 73.8% is the noise signature), NR r* >= 2 x U0 pS (identity loss Day's data would
    show), NM(1.0) >= 0.60; genes with identity < 0.98 are < 10% of ALL and carry dN/dS >= 0.50.
  AUDIT predictions (each can fail; scored individually):
    A0 U0 equals L1b V0 on ALL and O121 to 1e-9 (same code path). Fail = bug, stop and fix (post hoc).
    A1 NG N/S on U0 ALL in 3.20-3.40 (L1 3.34); kappa-hat in 3-6; N/S at kappa-hat in 2.6-3.0 (CSAC 2.78); no arm
       other than UT and the noise arms has NG N/S >= 3.50.
    A2 Estimand: median <= pooled <= mean-capped on U0 ALL; pooled on CSACp vs ALL differs by <= 0.06.
    A3 PF2 drop (U0 - PF2) in 0.03-0.15: the adversarial filter lowers dN/dS (by construction) but cannot carry it
       0.80 -> 0.23 or 0.27 -> ~0.
    A4 UG within 0.03 of U0; UT 0.28-0.60 (L1b A4).
    A5 Excluded codons of PF1: pooled dN/dS > 1 (enriched, Q182 true in direction) AND U0 identity of the genes
       carrying >= 50% of them below the ALL median (they are misaligned stretches, not selection signal).
    A6 Band hits in the protein aligner < 1% of genes; P skipped (no chimp material) < 2%.
  Bands (primary, evaluated in this order; U = U0 ALL, Uc = U0 CSACp, D1 = U - PF1 on ALL):
    DAY       U >= 0.65 AND nonsyn fraction(U0 ALL) >= 0.66 AND D1 >= 0.25 AND PF1 ALL <= 0.40
              (unguided high, guidance+trimming produces the low value: Day's mechanism shown on real data)
    HIGH-NOT-METHOD  U >= 0.65 AND D1 < 0.10 AND U0 HQ >= 0.65 (unguided high on clean genes, and the alignment
              method does not lower it: Day's number replicated, his mechanism not the cause)
    NOISE     U >= 0.40 AND (Uc < 0.40 OR HQ < 0.40) (high value confined to misaligned / low-identity genes)
    MIDDLE    0.40 <= Uc < 0.65 (and not above)
    CRITIC    U < 0.40 AND Uc < 0.40 (unguided Cactus alignment gives the textbook range)
  Mechanism-size flag, separately, for P, PF1 and PF2 on ALL and CSACp (drop D = U0 - arm): large >= 0.25;
    moderate 0.10-0.25; small 0.03-0.10; none |D| < 0.03; reverse <= -0.03.
  Intermediate outcomes and meaning: CRITIC + mechanism small (PF1 or PF2) = Day's bias exists in direction but is
    an order of magnitude too small (credit Q180-Q182 Reading A, not B). CRITIC + none = no bias at human-chimp
    divergence. NOISE = Day's high value reproduced and located in misaligned genes; 0.23-vs-0.80 explained by
    extraction noise, not by protein guidance. HIGH-NOT-METHOD = Day's 0.80 replicated on clean genes; the critics'
    textbook value would then need another explanation and Q186's attribution would be wrong but his number right.
    MIDDLE = neither side's range; reported with the numbers, no verdict move proposed beyond `contested`.

RD READINGS THE RESULT BEARS ON (rule RD; all readings recorded, verdict field = most charitable to the speaker)
  Q180-Q182  A: protein-guided pipelines can bias dN/dS down (any size). Supported if any of P/PF1/PF2 has mechanism
               flag >= small with excluded nonsyn fraction > U0's; contested if all `none`.
             B: the published 0.23 is (wholly) this artefact. Supported only under band DAY; contradicted under CRITIC
               or NOISE with PF2 flag < large. Fidelity note (pre-run, held text, see (ii)): CSAC's 13,454-gene value
               used a nucleotide genome alignment; under the reading "0.23 was produced by protein-guided alignment"
               fidelity is `misread` regardless of this run; under the charitable reading "CSAC's removal of
               'likely alignment artefacts' acted as a conservation filter", the test is U0 CSACp vs U0 ALL.
  Q183       A (uniformity shows the gap is not gene-list driven): bears via ALL/O121/CSACp spread on U0.
             B (73.8% is the misalignment signature): bears via NU/NR nonsyn fractions vs U0's.
  Q185       Not decidable here (Day's 13,454 run unpublished); CSACp is a proxy only.
  Q186       "not ... computational error": bears via the NOISE band and the HQ / identity-bin numbers.
  Q187       Arithmetic holds on Day's input; its premise (0.7989) is what U0 tests.
  Q188-Q190  Not moved (interpretation and scope; DN4 non-sequitur is independent of the number).

WHAT MOVES WHICH VERDICT (proposals for integration; owner decides): new alignment-circularity claim external:
  DAY -> supported; HIGH-NOT-METHOD -> contradicted (mechanism) while DN1 -> contested; NOISE or CRITIC with flag
  none -> contradicted; CRITIC with flag small/moderate -> contested (direction real, size insufficient), with the
  numbers. DN1/DN3: as L1b's bands; L1c adds the method dimension, never overrides L1b's band on the same codons.

RESOURCES (estimates): input = L1b seg dump (~0.3-1 GB gz) + the GFF (re-parsed, ~300 MB peak, ~1 min). Per gene:
  ~17 arms x NG counting + one banded protein alignment (~0.05-0.2 s; titin ~10 s). ~2-4 CPU-h total; with 6 workers
  ~30-45 min wall. RAM < 2 GB total (main ~0.5 GB, workers ~0.2 GB each). Host: na-workhorse (the dump and MAF live
  there), 6 workers, counted against the 11-process cap, after `ph` and L1b finish; builder possible with the dump
  copied (<= 4 workers, 5 GB RAM). Outputs: raw/l1c.json, raw/l1c.genes.tsv.gz, raw/l1c.out (few MB), raw/l1c.host.

LAUNCH (after L1b has written sources/raw/l1b-seg-<date>/seg.json.gz on na-workhorse; check `uptime` first):
  rsync -a research/checks/l1c_alignment_method.py research/checks/l1b_t2t_dnds.py research/checks/l1_dnds_genesets.py \
    na-workhorse:projects/evo-sim/research/checks/
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && md5sum research/checks/l1*.py && hostname' (record in
    raw/l1c.host with the L1b hashes)
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup /usr/bin/time -v research/.venv/bin/python -I
    research/checks/l1c_alignment_method.py run sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz
    sources/raw/l1-biomart-2026-10-11/orth_ptro.tsv sources/raw/l1b-seg-<date>/seg.json.gz research/checks/results/raw/l1c 6
    research/checks/results/raw/l1b.json > research/checks/results/raw/l1c.out 2>&1 < /dev/null &'
COLLECT: rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/l1c*' research/checks/results/raw/
  then `l1c_alignment_method.py report research/checks/results/raw/l1c.json`.
Other modes: `selftest` (synthetic, trivial).

======================================================================================================================
Post hoc amendment 2026-10-12 (pre-run, no data seen; before L1b reported)
======================================================================================================================
Answers the pre-run design review results/REVIEW-R4-L1c-prerun.md (017dea9: 1 BLOCKER, 9 MAJOR, 12 MINOR); item-by-item
resolution is appended to that file. Everything above this line is the registration 536b19b, unchanged, and is still
computed and reported as registered (label REGISTERED). Everything below is added beside it (label AMENDED). The
write-up reports both. Where the two disagree the amended result is the one proposed for integration, and the
registered one is shown with the reason.

BLINDNESS (review MAJOR-4, amendment 9). L1c has not run. L1b has not reported: no l1b* file exists under
  research/checks/results/raw/ on the workstation, and na-workhorse was not queried while this was written. The U part
  of every band is fixed by L1b (audit A0: U0 must equal L1b V0), so these amendments are blind only if this commit
  precedes the opening of L1b's result; the commit order in git is the evidence. Known before this amendment and
  therefore NOT blind: L1 on hg38 (0.271 ALL, 0.207 one2one, pS 0.0171 / 0.0153), which already makes CRITIC the
  expected band; the synthetic selftest of this script (below), including a 6-cell, 100-gene miniature of the transfer
  table. New information in L1c is the mechanism part: flags, excluded-codon tables, the dS discriminator, CSAC23.

AMENDMENTS (each: what, and which side it helps)
 1 Frame-aware protein arm PA (BLOCKER-1), with PAG / PAF1 / PAF2 = the registered PG / PF1 / PF2 rules on PA.
   The registered P translates the ungapped chimp string in frame 0 and loses the frame after any indel run or
   uncovered stretch whose length is not a multiple of 3. P, PG, PF1, PF2 and the registered band where it rests on
   PF1 are therefore INVALID AS REGISTERED (BLOCKER-1); their code path is kept (cheap), their outputs are printed
   with '!' and are never scored alone. PA builds the chimp protein in the Cactus codon frame (cactus_frame): clean
   codons as they are, in-frame indel runs translated as the chimp has them, frameshift runs as X (not compared),
   uncovered codons omitted; then the same Gotoh alignment. Reported: genes and codons the registered P reads out
   of frame (diag_amended.P_frame_loss_genes, P_out_of_frame_share_of_clean_codons), PA-U0 agreement.
   Selftest: a correctly placed 1-bp chimp indel FAILS the frame test on P and PASSES on PA, both strands.
   Helps both: Day gets an arm he would recognise and an excluded-codon table not diluted with ordinary codons;
   critics get "P within +-0.03" and "excluded share < 2%" not broken by an artefact.
   Limit: the Cactus-projected human frame stands in for a chimp gene annotation (none is used). Where the real
   chimp CDS differs from the projection (different exon structure) no arm here sees it.
 2 Bounded aligner memory (MAJOR-1). nw_banded keeps only the previous score rows and one byte of traceback per
   cell (same recurrence and tie-breaks as registered; equality with nw_banded_registered is asserted in the
   selftest). Hard cap CELL_CAP = 2e7 cells per alignment (~20 MB, ~11 s measured on the workstation). First pass
   over the cap: the gene is NOT aligned in that arm family, keeps the U0 pairing there (nothing excluded), and is
   counted (diag_amended.cap_skipped_genes per family, cap_skipped_tids); widened pass over the cap: first-pass
   path kept and counted (cap_widening_refused). Set NOSKIP (genes with no skip in any arm) repeats every arm on
   identical genes. Neutral; protects the host.
 3 Closed outcome bands (MAJOR-2): AMENDED BANDS below. A decision tree, so exhaustive and non-overlapping by
   construction (selftest enumerates a grid including missing values). The registered band() is still evaluated and
   printed, plus the registered rule with PAF1 in place of PF1. Symmetric: removes the order effect by which a
   noise world trimmed by PF1 scored DAY, and the unregistered holes that were Day-favourable worlds.
 4 Noise discriminator based on synonymous divergence, not identity (MAJOR-3, MAJOR-6). A misaligned or
   paralogous stretch has saturated pS; a fast-evolving protein has ordinary pS and high pN. Three uses:
   (a) arm UD = U0 minus every window of 10 compared codons holding >= 3 synonymous differences (expected 0.09 at
       1.2%; uses synonymous differences only, so it cannot select on amino-acid conservation; its small bias is
       upward, in Day's favour, and is measured on the clean synthetic cells);
   (b) gene sets DSC (gene pS not above 3x the median gene pS with >= 5 synonymous differences), NONDSC, and
       HQs = DSC and no frameshift run, beside the registered identity-based HQ / NONHQ;
   (c) excluded codons of every arm: their pS relative to the dS-clean pS (UD, same set), 3x band fixed here
       (<= 3x reads as real divergence, Day; > 3x as misalignment, critic), and the share lying within 10 codons
       of a Cactus frameshift run. This REPLACES the second clause of A5, which was nearly automatic. Deviation
       from the review, with reason: the review proposed U0's own pS as the reference; in a noise world U0's pS is
       itself inflated and the ratio collapses (selftest world: 2.6x against U0, far above 3x against UD).
   (d) uniform-noise gate: random base errors add no local dS cluster, so UD cannot see them; they do raise pS.
       Taking dN/dS from a true 0.27 to 0.65 with noise that hits N and S sites alike needs pS >= 2.09x the true
       value. Gate: pS(U0, ALL) <= PS_GATE = 0.023 = 1.5 x 0.0153 (L1 hg38 one2one pS, already reported; L1 ALL was
       0.0171; CSAC's genome-wide 1.23% is lower still). General form: DAY is unreachable for any noise whose
       per-site N:S rate ratio rho is below 1.41 (true 0.27) or 1.15 (true 0.40); arm NU measures rho for pure
       misplacement on these data and is reported for this purpose (assumption stated, not proven for every
       conceivable noise).
   Helps both: Day's objection that "divergent = noisy" is circular is met; critics get a test that separates
   misalignment from divergence.
 5 Protein guidance that CAN gap a substitution-rich region (MAJOR-5). What P and PA can and cannot show: with
   global scoring a replaced residue stays paired unless a run is dearer than two gaps (2 x (10 + k) for k
   residues, e.g. 12 residues at -4; selftest), so P/PA test indel re-placement, not Q181's "left unaligned".
   Added on the PA path:
     PL38, PL16  local segments by X-drop (a segment ends when its running score falls more than X below its
                 maximum; segments scoring < 40 are dropped; everything outside is left unaligned). X = 38 and 16
                 raw BLOSUM62 units, chosen to resemble BLASTP's gapped and ungapped X-drop (from memory, NOT
                 verified: NCBI's page was behind a browser check). This audit's rule, not a named pipeline's.
     PGB         Gblocks block selection with its documented defaults for two sequences (b1 = b2 = 2 identical,
                 b3 = 8, b4 = 10, no gap positions): runs of more than 8 non-identical positions go, isolated
                 replacements stay. Implemented from the documentation; not validated against the binary.
   REALISTIC arms = PA, PAG, PAF1, PL38, PGB. STRESS arms = PAF2, PL16 (upper bounds, decide nothing).
   Helps Day (an arm that can do what Q181 says, and a rule this audit did not invent); the critic side keeps the
   distinction between realistic and adversarial filters.
 6 The mechanism tested where it could work (MAJOR-7).
   (i) Mode `transfer`: synthetic genes at true omega 0.23 / 0.5 / 0.8 / 1.0, 1.2% synonymous divergence, three
       clustering levels of replacements (none; 50% of them in 2% of codons; 80% in 1%; runs of 15 codons), four
       noise settings (clean; correctly placed indels; a misregistered 40-codon stretch in 5% or 25% of genes),
       pushed through every arm; output = dN/dS per arm against the clean-cell truth. Rates are ASSUMED design
       values (uniform codon usage, kappa 1), not sourced; the real run reports the measured indel and frameshift
       shares for comparison.
   (ii) Real data: the protein family applied to extractions that read high: NM(1.0), NR(0.02), NR(0.05) each
       through PA / PAF1 / PL38 / PGB (res.noise_through_protein), and UT, whose bases the registered P family
       realigns (UT - P, UT - PF1, UT - PF2; valid for this purpose, since UT is the frame-0 reading).
   Helps both: Reading B is decided on a test of the mechanism even if U0 is low; neither side can say the arm
   was set where it would find nothing.
 7 The real CSAC list as set CSAC23 beside the stand-in CSACp (MAJOR-8). Source: Table S23, read as bytes
   (sha256 asserted); 13,454 NM_ accessions with their 2005 symbols (parse_s23). Mapping rule, fixed here:
   NM_ (unversioned) -> ENST via GENCODE v35 `gencode.v35.metadata.RefSeq.gz` (REFSEQ_META_URL; fetched
   2026-10-12, sha256 asserted) -> ENSG via the annotation's source_transcript / source_gene -> gene chosen by
   L1b's transcript rule; fallback: the S23 symbol equals the gene_name of exactly one chosen gene. Reported:
   counts per route and per failure reason, ambiguous ids, distinct genes, and the map itself
   (raw/l1c.csac23_map.tsv). Floor (from the review, 017dea9): if fewer than 85% of 13,454 map to a gene present in
   ALL, CSACp stays the source set for the band and CSAC23 is descriptive; otherwise CSAC23 is the source set.
   The band is printed on both. Sets CSAC23nm (NM route only), NOT23 = ALL minus CSAC23 and O121NOT23 give the
   gene-level excluded accounting (count, pooled dN/dS, nonsyn fraction, pS); dN/dS by chimp-coverage stratum.
   Pre-check made after the floor was fixed: 12,637 of 13,454 accessions (93.9%) are in the GENCODE file; the
   gene-level share is unknown until the run. Limit: the 2005 selection was made on the panTro1 draft, so
   membership partly reflects 2004 assembly coverage. Credit rule (RD): a set effect goes to the DN3 form of the
   claim, not to Q186, which says "not a matter of gene selection".
   Helps Day (his selection point becomes testable on the real list) and critics (head-to-head with 0.23).
 8 Reading A on realistic arms only (MAJOR-9); PF2 / PAF2 / PL16 reported as an upper bound. See READINGS.
   Helps critics; makes any credit to Day meaningful.
 9 Relative-drop flags beside the absolute ones (MINOR-7): (U0 - arm) / U0, large >= 50%, moderate 25-50%,
   small 10-25%, none within +-10%, reverse <= -10%. Helps Day (0.27 -> 0.08 is "large", not "moderate").
10 Small. Band also at kappa-hat sites (sensitivity line; NG reads ~17% below a transition-aware estimate);
   NU and NM scored on the p-ratio and nonsyn fraction (NU's p is near 0.75, JC undefined); "NR r* >= 2 x pS" is
   a restatement of U <= 0.40, not an independent hit; excluded share for every set; A0 printed PASS / FAIL;
   conversion table for Day's 73.9% (Nd/Sd 2.83 = dN/dS 1.02 at N/S 2.78, 0.85 at 3.34, 0.80 at 3.54) and the
   no-constraint fraction N/(N+S); trimming-rule table (rules_table); fidelity line printed whatever the band.
   Wording corrected: the gap cost is 10 + k for k residues (BLAST's 11/1 would be 11 + k; immaterial), and
   "at any plausible threshold" in the PF2 text is withdrawn: PF2 is one stress setting, not a bound (a rule that
   drops every non-identical residue gives 0). Threshold asymmetry stated: 0.40 leaves the critic side +74%
   above 0.23, 0.65 leaves Day -19% below 0.80; both inherited (0.65 is Day's own Q175 bound), unchanged.
   O121 comes from Ensembl's protein-tree orthology, itself protein-guided: an instance of Day's gene-level
   concern, while U0 on O121 uses none of its alignments.

AMENDED BANDS (pooled JC dN/dS, kappa = 1; first applicable line; every input lands in exactly one)
  U = U0 ALL; Uc = U0 on the source set (CSAC23 if the floor is met, else CSACp); Ud = UD ALL (dS-clean codons);
  pS = pS of U0 ALL; nf = nonsyn fraction of U0 ALL; Rmin = lowest ALL value among the REALISTIC arms, D = U - Rmin;
  x = pS of the codons that arm excluded / pS of UD ALL.
  INVALID               U, Ud or pS missing (or Rmin missing where needed): no band, fix and rerun.
  CRITIC                U < 0.40 and Uc < 0.40 (or the source set empty)
  CRITIC-ALL/SET-ABOVE  U < 0.40 and Uc >= 0.40: all genes in the textbook range, the source set above it
                        (neither side predicts it; reported, no verdict move beyond `contested`)
  NOISE                 U >= 0.40 and (Ud < 0.40 or pS > 0.023): the excess sits in dS-saturated codons, or pS is
                        itself inflated. Sub-tags: LOCAL, pS-GATE / UNIFORM, FILTERED (a realistic arm removes it).
  GENE-SET              U >= 0.40, not NOISE, Uc < 0.40: high on dS-clean codons of all genes, textbook on the
                        source set: the gap is gene selection (DN3 form; against Q186's own wording)
  HIGH-NOT-METHOD       U >= 0.65, Ud >= 0.65, D < 0.10: Day's number replicated on clean codons, method not the cause
  DAY                   U >= 0.65, Ud >= 0.65, D >= 0.25, Rmin <= 0.40, nf >= 0.66, x <= 3: unguided high on clean
                        codons, a realistic protein rule produces the published range by removing dS-normal codons
  HIGH-PARTIAL-METHOD   U >= 0.65, Ud >= 0.65, neither of the two above (mechanism moderate, or incomplete, or
                        the removed codons are dS-saturated)
  MIDDLE                everything else with U >= 0.40 (e.g. U 0.80 with Ud 0.50); U, Ud, Uc printed
  Pure-noise worlds cannot reach DAY: local misalignment fails Ud >= 0.65 or x <= 3; uniform noise fails the pS
  gate (amendment 4d, under the stated rho assumption). Selftest: two pure-noise worlds at true omega 0.25 (half
  the genes misregistered: U 0.91 with nonsyn fraction 0.74; 3% random base errors) both score NOISE.
  Verdict proposals as registered, with: GENE-SET -> alignment-circularity claim contradicted, DN3 credited;
  HIGH-PARTIAL-METHOD and MIDDLE -> contested; CRITIC-ALL/SET-ABOVE -> contested; INVALID -> none.

AMENDED READINGS (rule RD)
  Q180-Q182 A (protein-guided pipelines can bias dN/dS down, any size): `supported` if a REALISTIC arm has an
      absolute or relative flag >= small AND the codons it excluded are nonsyn-enriched (fraction above U0's)
      AND dS-normal (x <= 3); `contested` if a realistic arm lowers dN/dS only by removing dS-saturated codons
      (noise removal, not a conservation bias) or if none lowers it. Stress arms give the upper bound only.
      In principle (synthetic): the transfer table says for which clustering a realistic arm can move omega.
  Q180-Q182 B (the published 0.23 is this artefact): `supported` only under amended band DAY; `contradicted`
      under CRITIC, NOISE, GENE-SET or CRITIC-ALL/SET-ABOVE when no realistic arm has a large flag (absolute or
      relative), and under HIGH-NOT-METHOD; otherwise `contested`. The transfer table is reported beside it: if
      no realistic arm takes 0.8 to <= 0.40 at any clustering, the mechanism is insufficient in principle; if
      one does only at the extreme level, the real-data question is whether realistic arms exclude that kind of
      codon (dS-normal, replacement-dense) in quantity, which the excluded-codon table answers.
  Fidelity note unchanged (pre-run; printed in every report).

AMENDED PREDICTIONS (fixed now)
  DAY side: amended band DAY; Ud >= 0.65 and pS <= 0.023; a REALISTIC arm with a large flag whose excluded codons
    have x <= 3 and dN/dS >= 2; CSAC23 within 0.05 of ALL on U0 (Q183/Q186); transfer: some REALISTIC arm reads
    <= 0.40 at true 0.8.
  CRITIC side: amended band CRITIC on both source sets; PA within +-0.01 of U0 and PA-U0 agreement >= 99.5%;
    every REALISTIC arm `none` on both flags, excluded share < 1% of U0 codons, with x > 3 (what little is
    removed is misalignment); CSAC23 0.18-0.30 on U0; NOT23 above CSAC23 by >= 0.10 (gene-set effect, L1);
    NM(1.0) p-ratio >= 0.60 and NU nonsyn fraction 0.68-0.80; NM(1.0)>PAF1 at least 0.25 below NM(1.0);
    transfer: REALISTIC arms within 10% of truth on clean cells at clustering 0 and 1 for every omega.
  AUDIT: A5' (replaces A5's second clause) excluded codons of PAF1 have x > 3; their share within 10 codons of
    a Cactus frameshift run is reported without a threshold; A7 cap-skipped genes < 0.5% per family; A8 registered P reads >= 1 clean
    codon out of frame in > 1% of genes (else BLOCKER-1 was immaterial on these data, and is said so);
    A9 CSAC23 floor met (>= 85%); A10 transfer: PA equals U0 on clean cells, UD within
    5% of U0 on clean cells without clustering, U0 above truth by >= 25% under misreg25.
  NOT BLIND (seen in the synthetic selftest miniature, 6 cells x 100 genes x 150 codons, before this commit):
    clean, no clustering: every arm except PF2/PAF2 returned the truth (0.26, 0.82, 1.03); PAF2 read ~30-38% low
    at every omega; at 0.8 with 80% of replacements in 1% of codons PAF1 read 0.25 and PGB 0.29 against a truth
    of 0.66, PA 0.58, PL38 0.57; misreg25 took U0 from 0.26 to 0.79 with UD back at 0.25. So "a realistic arm
    can carry 0.8 to the published range if replacements are extremely clustered" is already known for the
    synthetic; the full table (2,000 genes per cell) is confirmation and the intermediate level is still open.

VERIFICATION OF THE REVIEW'S FROM-MEMORY CLAIMS (2026-10-12)
  Verified from fetched text: PAL2NAL takes a protein alignment plus the corresponding DNA (CDS) sequences
    (bork.embl.de/pal2nal), so a per-species in-frame CDS is its starting point; Gblocks method and defaults
    (documentation mirror home.cc.umanitoba.ca/~psgendb/doc/Castresana/Gblocks_documentation.html; the two
    original hosts did not answer); GENCODE v35 RefSeq metadata file exists, 3 tab columns (ENST, RefSeq RNA,
    RefSeq protein), 76,788 rows.
  Corrected: "a substituted codon is never gapped" under global scoring holds only for runs cheaper than two gaps
    (amendment 5; selftest).
  Not verified: TranslatorX behaviour; BLAST's default gap costs and X-drop values (page not reachable); the
    Gblocks rule against the binary; MACSE / PRANK (not installed; queue item stays); F3x4 codon frequencies
    (no ML tool; queue item stays).
  Found while wiring CSAC23: the held `S23_NM_ids.txt` (strings + regex extraction) has 1,272 accessions with a
    spurious 7th digit (the next string's length byte). The script reads the .xls directly with a
    header-anchored pattern (13,454 six-digit accessions, 13,386 with a symbol) and does not use that list.

RESOURCES (re-estimated; measured on synthetic genes on the workstation): one full gene of 450 codons 0.11 s, of
  2,000 codons 0.51 s; aligner 11 s at the cap. Real run ~1-3 CPU-h (20k genes; long or indel-rich genes dominate),
  8 workers ~10-25 min wall after ~2 min of annotation parsing (twice: transcripts, then transcript-to-gene).
  RAM: main < 1.5 GB, workers < 0.3 GB each (cap bounds the aligner at ~20 MB), total < 4 GB. Transfer: 48 cells x
  2,000 genes x 300 codons, ~1-2 CPU-h, 8 workers, < 2 GB. Both on na-workhorse within the 11-process cap; run
  them one after the other. Selftest: 16 s, 57 MB.

LAUNCH (AMENDED; replaces LAUNCH above; after L1b has written the seg dump; check `uptime` first)
  rsync -a research/checks/l1c_alignment_method.py research/checks/l1b_t2t_dnds.py research/checks/l1_dnds_genesets.py \
    na-workhorse:projects/evo-sim/research/checks/
  rsync -a sources/raw/csac2005-nature-2026-10-12 sources/raw/gencode-v35-refseq-2026-10-12 \
    na-workhorse:projects/evo-sim/sources/raw/
    (or fetch on the host into a new directory: curl -sS -o gencode.v35.metadata.RefSeq.gz <REFSEQ_META_URL>; the
     script refuses a file whose sha256 differs)
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && md5sum research/checks/l1*.py && hostname' (-> raw/l1c.host)
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup /usr/bin/time -v research/.venv/bin/python -I
    research/checks/l1c_alignment_method.py run sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz
    sources/raw/l1-biomart-2026-10-11/orth_ptro.tsv sources/raw/l1b-seg-<date>/seg.json.gz research/checks/results/raw/l1c 8
    research/checks/results/raw/l1b.json sources/raw/csac2005-nature-2026-10-12/S23_MOESM6.xls
    sources/raw/gencode-v35-refseq-2026-10-12/gencode.v35.metadata.RefSeq.gz
    > research/checks/results/raw/l1c.out 2>&1 < /dev/null &'
  then the synthetic table (needs no input file):
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && nohup /usr/bin/time -v research/.venv/bin/python -I
    research/checks/l1c_alignment_method.py transfer research/checks/results/raw/l1c 8 2000 300
    > research/checks/results/raw/l1c.transfer.out 2>&1 < /dev/null &'
  Outputs added: raw/l1c.csac23_map.tsv, raw/l1c.transfer.json, raw/l1c.transfer.out.
  Modes added: `transfer <out_prefix> [workers] [genes per cell] [codons]`, `transfer-report <json>`.

POST HOC (fix pass, 2026-10-13; after the main run, the transfer table and three post-run reviews; new mode
  `transfer-excl`, additive: no registered or amended function, constant, band, reading or prediction is changed)
  Why: REVIEW-R4-L1c-correctness finding 1 (MAJOR). The transfer json does not store what each arm drops, so the
  excluded-codon discriminator was never checked on synthetic cells. The reviewer regenerated three clean cells in
  part and found that x (pS of dropped codons over the dS-clean pS) does NOT separate a saturated replacement run
  from misalignment (x = 9.6 at nominal 0.8, clustering 2), and proposed the nonsynonymous fraction and p-ratio of
  the dropped codons instead. This mode stores, per cell and per arm, the dropped codons' count, pS, x against the
  cell's own UD pS, nonsynonymous fraction and p-ratio (excl_agg, unchanged), using the SAME generator, seeds and
  per-gene function (_tf_one) as `transfer`, for the clean and misreg25 cells (24 of 48).
  Windows fixed here, before the run (the audit's choice, like the 3x band):
    MISPAIRING window  nonsyn fraction <= 0.80 AND p-ratio <= 1.5   (unrelated in-frame pairing, arm NU on real
                       data: 0.774 and 1.018)
    DENSE-RUN window   nonsyn fraction >= 0.90 AND p-ratio >= 3.0
    anything else      AMBIGUOUS
  Known from the real run (not a prediction): the realistic arms' dropped codons have fraction 0.71-0.77 and
  p-ratio 0.76-1.01 on ALL, i.e. inside the MISPAIRING window.
  Scored only for PAF1 and PGB (the two arms that trim) in cells where the arm drops >= 50 codons.
  PREDICTIONS
  X1 consistency (audit): pooled dN/dS per arm equals raw/l1c.transfer.json for every cell rerun, to 1e-9. Fail =
     the mode does not reproduce the table; stop, nothing below is used.
  X2 (audit; NOT BLIND, the reviewer measured 9.6 on 1,344 genes): clean, nominal 0.8, clustering 2: x > 3 for
     PAF1 and PGB. If it holds, the amended DAY clause "excluded codons have x <= 3" was unreachable in the one
     synthetic world built to let the mechanism work: a defect of the amendment, on Day's side.
  X3 (critic side; BLIND for nominal 0.5 and 1.0, and for PGB; NOT BLIND for PAF1 at 0.23 / clustering 2, 0.8 /
     clustering 1 and 0.8 / clustering 2, where the reviewer measured fractions 0.995, 0.986, 0.947): every clean
     clustered cell (clustering 1 and 2, all four omegas) is in the DENSE-RUN window for PAF1 and PGB.
  X4 (critic side; BLIND): every misreg25 cell at clustering 0 (four omegas) is in the MISPAIRING window for PAF1
     and PGB, with x > 3.
  X5 (Day side; BLIND for the same cells as X3): at least one clean clustered cell falls in the MISPAIRING window
     for PAF1 or PGB, i.e. real dense replacement at ordinary synonymous divergence can look exactly like what the
     real arms drop, and the discriminator proposed by the reviewer fails like x did.
  Reading, fixed now: X3 and X4 hold and X5 fails = the fraction / p-ratio pair separates the two on synthetic
     data and "what the realistic arms drop looks like mispairing" may rest on it (with the limits of the
     generator: uniform codon usage, kappa 1, runs of 15, no indels inside runs). X5 holds, or X3 fails in any
     cell = the pair does not separate them there, and the write-up must say the real dropped codons are not
     classified. AMBIGUOUS cells are reported as such and count for neither side.
     Mixed cells (misreg25 with clustering 1 or 2) are reported without a threshold.
  No band, reading or verdict proposal depends on this run (the x clause is never reached under CRITIC).
  NOT BLIND, disclosed: the predictions and windows above were written before any execution of this mode and
     were not changed afterwards, but a smoke test (30 genes per cell, 1 worker, 27 s, workstation, output not
     kept) was run before this commit to see that the mode executes, and its output was seen: X3 5 of 5 and
     X4 8 of 8 arm-cells with >= 50 codons in the predicted window, X5 none, X2 x = 6.8 and 9.1. Commit order
     therefore does not prove blindness for X3-X5; the full run is a confirmation at 2,000 genes per cell.
  LAUNCH (at most 2 workers; another job holds 8 of the host's 12 cores; check `uptime` first)
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && setsid -f nohup /usr/bin/time -v
    research/.venv/bin/python -I research/checks/l1c_alignment_method.py transfer-excl research/checks/results/raw/l1c
    2 2000 300 research/checks/results/raw/l1c.transfer.json > research/checks/results/raw/l1c.transfer_excl.out 2>&1
    < /dev/null'
  Outputs: raw/l1c.transfer_excl.json, raw/l1c.transfer_excl.out. Estimated 25-40 min wall, < 1 GB.
"""
import gzip
import importlib.util
import json
import math
import os
import random
import re
import sys
import time
import zlib
from multiprocessing import Pool

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("l1b", os.path.join(HERE, "l1b_t2t_dnds.py"))
L1B = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L1B)
L1 = L1B.L1

import hashlib

# REGISTERED (536b19b)
ARMS_REG = ["U0", "UG", "UT", "P", "PG", "PF1", "PF2"]
EXCL_REG = ["UG", "P", "PG", "PF1", "PF2"]
NR_GRID = [0.002, 0.005, 0.01, 0.02, 0.05, 0.10]
NM_GRID = [0.1, 0.25, 0.5, 1.0]
NOISE_ARMS = [f"NR{r}" for r in NR_GRID] + [f"NM{f}" for f in NM_GRID] + ["NU"]
KAPPAS = [1, 2, 3, 4, 5, 6]
SETS_REG = ["ALL", "O121", "SYN", "O121SYN", "CSACp", "HQ", "NONHQ"]
IDBINS = [(0.995, 1.01), (0.99, 0.995), (0.98, 0.99), (0.95, 0.98), (0.90, 0.95), (-1.0, 0.90)]
GO, GE = 11, 1
BLOCKER1_ARMS = ["P", "PG", "PF1", "PF2"]            # invalid as registered (BLOCKER-1); shown, never scored alone

# AMENDED 2026-10-12 (pre-run, no data seen; before L1b reported)
ARMS_AM = ["UD", "PA", "PAG", "PAF1", "PAF2", "PL38", "PL16", "PGB"]
ARMS = ARMS_REG + ARMS_AM
EXCL_ARMS = EXCL_REG + ARMS_AM
REALISTIC = ["PA", "PAG", "PAF1", "PL38", "PGB"]     # Reading A and the DAY band are scored on these only
STRESS = ["PAF2", "PL16"]                            # upper bounds / stress tests, never decide a reading
NOISE_P_BASES = ["NM1.0", "NR0.02", "NR0.05"]        # noise worlds pushed through the protein family (MAJOR-7 ii)
NOISE_P_SUFFIX = ["PA", "PAF1", "PL38", "PGB"]
NOISE_P_ARMS = [f"{b}>{s}" for b in NOISE_P_BASES for s in NOISE_P_SUFFIX]
SETS_AM = ["CSAC23", "CSAC23nm", "NOT23", "O121NOT23", "DSC", "NONDSC", "HQs", "NOSKIP"]
SETS = SETS_REG + SETS_AM
COVBINS = [(0.99, 1.01), (0.90, 0.99), (0.50, 0.90), (-1.0, 0.50)]
CELL_CAP = 20_000_000        # hard cap on DP cells per alignment (~20 MB of traceback, ~20-40 s of CPU)
UD_W, UD_T = 10, 3.0         # dS-saturation window: 10 compared codons holding >= 3 synonymous differences
PL_SMIN = 40                 # minimum score of a kept local segment
T_LO, T_HI = 0.40, 0.65      # registered thresholds, unchanged
PS_REF = 0.0153              # L1 (hg38, Ensembl alignments, already reported) pS on one2one genes
PS_GATE = 0.023              # = 1.5 x PS_REF: uniform-noise gate on pS(U0, ALL); see amendment 3
XRATIO_MAX = 3.0             # excluded-codon pS / U0 pS above this = misaligned, not divergent (3x band, rule RD)
CSAC_N = 13454
CSAC_FLOOR = 0.85
S23_SHA256 = "ac9e966cb41ff72d8f3446c26ded8d2fcb771d681e8c3117091b08de4a3f5bb9"
REFSEQ_META_URL = ("https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_human/release_35/"
                   "gencode.v35.metadata.RefSeq.gz")
REFSEQ_META_SHA256 = "02c7a3e7f0416b124b78d845f4d0076dc9c292548e92181fbae8f9af9cf19edb"
BANDS_AM = ["INVALID", "CRITIC", "CRITIC-ALL/SET-ABOVE", "NOISE", "GENE-SET", "DAY", "HIGH-NOT-METHOD",
            "HIGH-PARTIAL-METHOD", "MIDDLE"]

# ---------------------------------------------------------------- BLOSUM62 (NCBI matrix, 20 aa; '*' and X added)
_AA = "ARNDCQEGHILKMFPSTWYV"
_B62 = """
 4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
-1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
-2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
-2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
 0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
-1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
-1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
 0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
-2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
-1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
-1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
-1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
-1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
-2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
-1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
 1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
 0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
-3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
-2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
 0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""
B62 = {}
for _i, _row in enumerate(_B62.strip().splitlines()):
    for _j, _v in enumerate(_row.split()):
        B62[(_AA[_i], _AA[_j])] = int(_v)
for _a in _AA + "*X":
    B62[(_a, "*")] = B62[("*", _a)] = -4
    B62[(_a, "X")] = B62[("X", _a)] = -1
B62[("*", "*")] = 1
B62[("X", "X")] = -1
B62[("*", "X")] = B62[("X", "*")] = -4


def translate(s):
    s = s.upper()
    return "".join(L1.CODE.get(s[i:i + 3], "X") for i in range(0, len(s) - len(s) % 3, 3))



# ---------------------------------------------------------------- banded Gotoh global alignment
def nw_banded_registered(a, b, B):
    """Global affine alignment of protein strings a, b in a diagonal band of half-width B.
    Returns (pairs, band_hit): pairs = list of (i or None, j or None) in order."""
    n, m = len(a), len(b)
    NEG = -(10 ** 9)
    if n == 0 or m == 0:
        return [(i, None) for i in range(n)] + [(None, j) for j in range(m)], False
    lo = [0] * (n + 1)
    hi = [0] * (n + 1)
    for i in range(n + 1):
        c = (i * m) // n
        lo[i], hi[i] = max(0, c - B), min(m, c + B)
    M, X, Y, P = [], [], [], []
    for i in range(n + 1):
        w = hi[i] - lo[i] + 1
        Mi, Xi, Yi, Pi = [NEG] * w, [NEG] * w, [NEG] * w, [0] * w
        if i == 0:
            for k in range(w):
                j = lo[0] + k
                if j == 0:
                    Mi[k] = 0
                else:
                    Yi[k] = -(GO - GE) - GE * j
                    Pi[k] = 2 * 9 if j > 1 else 0
        else:
            pl, ph = lo[i - 1], hi[i - 1]
            Mp, Xp, Yp = M[i - 1], X[i - 1], Y[i - 1]
            ai = a[i - 1]
            for k in range(w):
                j = lo[i] + k
                pm = px = py = 0
                if j == 0:
                    Xi[k] = -(GO - GE) - GE * i
                    Pi[k] = (1 * 3) if i > 1 else 0
                    continue
                # M: from (i-1, j-1)
                if pl <= j - 1 <= ph:
                    q = j - 1 - pl
                    v0, v1, v2 = Mp[q], Xp[q], Yp[q]
                    if v0 >= v1 and v0 >= v2:
                        best, pm = v0, 0
                    elif v1 >= v2:
                        best, pm = v1, 1
                    else:
                        best, pm = v2, 2
                    if best > NEG // 2:
                        Mi[k] = best + B62.get((ai, b[j - 1]), -1)
                # X: from (i-1, j), gap in b
                if pl <= j <= ph:
                    q = j - pl
                    v0, v1, v2 = Mp[q] - GO, Xp[q] - GE, Yp[q] - GO
                    if v0 >= v1 and v0 >= v2:
                        Xi[k], px = v0, 0
                    elif v1 >= v2:
                        Xi[k], px = v1, 1
                    else:
                        Xi[k], px = v2, 2
                # Y: from (i, j-1), gap in a
                if k > 0:
                    v0, v1, v2 = Mi[k - 1] - GO, Yi[k - 1] - GE, Xi[k - 1] - GO
                    if v0 >= v1 and v0 >= v2:
                        Yi[k], py = v0, 0
                    elif v1 >= v2:
                        Yi[k], py = v1, 2
                    else:
                        Yi[k], py = v2, 1
                Pi[k] = pm + 3 * px + 9 * py
        M.append(Mi)
        X.append(Xi)
        Y.append(Yi)
        P.append(Pi)
    i, j = n, m
    k = j - lo[i]
    vals = (M[i][k], X[i][k], Y[i][k])
    state = max(range(3), key=lambda s: vals[s])
    pairs = []
    hit = False
    while i > 0 and j > 0:
        k = j - lo[i]
        if (j == lo[i] and lo[i] > 0) or (j == hi[i] and hi[i] < m):
            hit = True
        p = P[i][k]
        if state == 0:
            pairs.append((i - 1, j - 1))
            state = p % 3
            i -= 1
            j -= 1
        elif state == 1:
            pairs.append((i - 1, None))
            state = (p // 3) % 3
            i -= 1
        else:
            pairs.append((None, j - 1))
            state = (p // 9) % 3
            j -= 1
    while i > 0:
        pairs.append((i - 1, None))
        i -= 1
    while j > 0:
        pairs.append((None, j - 1))
        j -= 1
    pairs.reverse()
    return pairs, hit


# ---------------------------------------------------------------- AMENDED 2026-10-12: bounded-memory aligner (MAJOR-1)
def nw_banded(a, b, B):
    """Same recurrence, tie-breaking and traceback as nw_banded_registered (536b19b); only the storage differs:
    the three score rows are rolled (previous row only) and the traceback is one byte per cell. Equality of the
    returned pairs is asserted in the selftest. Memory: ~1 byte per filled cell instead of ~116."""
    n, m = len(a), len(b)
    NEG = -(10 ** 9)
    if n == 0 or m == 0:
        return [(i, None) for i in range(n)] + [(None, j) for j in range(m)], False
    lo = [0] * (n + 1)
    hi = [0] * (n + 1)
    for i in range(n + 1):
        c = (i * m) // n
        lo[i], hi[i] = max(0, c - B), min(m, c + B)
    P = []
    Mp = Xp = Yp = None
    for i in range(n + 1):
        w = hi[i] - lo[i] + 1
        Mi, Xi, Yi, Pi = [NEG] * w, [NEG] * w, [NEG] * w, bytearray(w)
        if i == 0:
            for k in range(w):
                j = lo[0] + k
                if j == 0:
                    Mi[k] = 0
                else:
                    Yi[k] = -(GO - GE) - GE * j
                    Pi[k] = 2 * 9 if j > 1 else 0
        else:
            pl, ph = lo[i - 1], hi[i - 1]
            ai = a[i - 1]
            for k in range(w):
                j = lo[i] + k
                pm = px = py = 0
                if j == 0:
                    Xi[k] = -(GO - GE) - GE * i
                    Pi[k] = (1 * 3) if i > 1 else 0
                    continue
                if pl <= j - 1 <= ph:
                    q = j - 1 - pl
                    v0, v1, v2 = Mp[q], Xp[q], Yp[q]
                    if v0 >= v1 and v0 >= v2:
                        best, pm = v0, 0
                    elif v1 >= v2:
                        best, pm = v1, 1
                    else:
                        best, pm = v2, 2
                    if best > NEG // 2:
                        Mi[k] = best + B62.get((ai, b[j - 1]), -1)
                if pl <= j <= ph:
                    q = j - pl
                    v0, v1, v2 = Mp[q] - GO, Xp[q] - GE, Yp[q] - GO
                    if v0 >= v1 and v0 >= v2:
                        Xi[k], px = v0, 0
                    elif v1 >= v2:
                        Xi[k], px = v1, 1
                    else:
                        Xi[k], px = v2, 2
                if k > 0:
                    v0, v1, v2 = Mi[k - 1] - GO, Yi[k - 1] - GE, Xi[k - 1] - GO
                    if v0 >= v1 and v0 >= v2:
                        Yi[k], py = v0, 0
                    elif v1 >= v2:
                        Yi[k], py = v1, 2
                    else:
                        Yi[k], py = v2, 1
                Pi[k] = pm + 3 * px + 9 * py
        P.append(bytes(Pi))
        Mp, Xp, Yp = Mi, Xi, Yi
    i, j = n, m
    k = j - lo[i]
    vals = (Mp[k], Xp[k], Yp[k])
    state = max(range(3), key=lambda s: vals[s])
    pairs = []
    hit = False
    while i > 0 and j > 0:
        k = j - lo[i]
        if (j == lo[i] and lo[i] > 0) or (j == hi[i] and hi[i] < m):
            hit = True
        p = P[i][k]
        if state == 0:
            pairs.append((i - 1, j - 1))
            state = p % 3
            i -= 1
            j -= 1
        elif state == 1:
            pairs.append((i - 1, None))
            state = (p // 3) % 3
            i -= 1
        else:
            pairs.append((None, j - 1))
            state = (p // 9) % 3
            j -= 1
    while i > 0:
        pairs.append((i - 1, None))
        i -= 1
    while j > 0:
        pairs.append((None, j - 1))
        j -= 1
    pairs.reverse()
    return pairs, hit


def band_cells(n, m, B):
    """Number of DP cells nw_banded fills for lengths n, m and half-width B (exact, O(n))."""
    if n == 0 or m == 0:
        return 0
    return sum(min(m, (i * m) // n + B) - max(0, (i * m) // n - B) + 1 for i in range(n + 1))


def align_capped(ha, ca):
    """Banded alignment under the hard cell budget CELL_CAP. Returns (pairs or None, flag):
    0 ok; 1 band hit, widened 4x, ok; 2 band still hit after widening; 3 band hit but the widened band exceeds the
    cap (first-pass path kept); 4 first pass exceeds the cap: NOT aligned (pairs None, gene skipped for this arm)."""
    n, m = len(ha), len(ca)
    B = 32 + abs(n - m)
    if band_cells(n, m, B) > CELL_CAP:
        return None, 4
    pairs, hit = nw_banded(ha, ca, B)
    if not hit:
        return pairs, 0
    if band_cells(n, m, 4 * B) > CELL_CAP:
        return pairs, 3
    pairs, hit = nw_banded(ha, ca, 4 * B)
    return pairs, (2 if hit else 1)


def apply_pairs(ha, ca, ccod, pairs, ncod):
    """Back-translation of an alignment path (the loop of the registered protein_align, unchanged): chimp codon
    string in the human codon frame ('---' unpaired), per-human-codon BLOSUM62 score (gap -4), chimp-only residues,
    human codons at or next to a gap."""
    out = ["---"] * ncod
    score = [-4] * ncod
    ins = 0
    gap_codons = set()
    last_h = -1
    for i, j in pairs:
        if i is None:
            ins += 1
            if last_h >= 0:
                gap_codons.add(last_h)
            if last_h + 1 < ncod:
                gap_codons.add(last_h + 1)
            continue
        last_h = i
        if j is None:
            gap_codons.add(i)
            continue
        if i < ncod:
            out[i] = ccod[j]
            score[i] = B62.get((ha[i], ca[j]), -1)
    return "".join(out), score, ins, gap_codons


def protein_align(hcds, cseq):
    """REGISTERED arm P (536b19b): chimp bases translated in frame 0. Invalid as registered wherever the ungapped
    chimp string has lost the frame (BLOCKER-1); kept so the registered outputs can be shown beside PA. Only change:
    the memory cap. Returns None when the gene is skipped by the cap, else the registered 5-tuple."""
    ha, ca = translate(hcds), translate(cseq)
    pairs, flag = align_capped(ha, ca)
    if pairs is None:
        return None
    cu = cseq.upper()
    out, score, ins, gap_codons = apply_pairs(ha, ca, [cu[3 * j:3 * j + 3] for j in range(len(ca))], pairs,
                                              len(hcds) // 3)
    return out, score, flag, ins, gap_codons


def codon_scores(h, c):
    """Per-codon BLOSUM62 score of an existing codon pairing (gap -4): the fallback when an arm is cap-skipped."""
    out = []
    for i in range(len(h) // 3):
        a, b = h[3 * i:3 * i + 3].upper(), c[3 * i:3 * i + 3].upper()
        out.append(-4 if "-" in b or "-" in a else B62.get((L1.CODE.get(a, "X"), L1.CODE.get(b, "X")), -1))
    return out


# ---------------------------------------------------------------- AMENDED: frame-aware chimp protein (BLOCKER-1)
def cactus_frame(r, segs, c0):
    """Chimp protein read in the Cactus codon frame (the human frame carried through the alignment), so that an
    indel or an uncovered stretch cannot shift everything downstream.
    Per human codon the chimp 'chunk' is its aligned bases plus the chimp insertions after each of its positions.
      clean  : three aligned bases, no insertion inside the codon, boundary insertion a multiple of 3 -> one residue
               (plus one residue per inserted triplet);
      uncovered (no chimp row on any of its positions) -> nothing emitted (missing data);
      otherwise 'dirty'. A maximal run of consecutive dirty codons is read as ONE unit: if its chimp bases total a
      multiple of 3 it is an in-frame event and is translated as the chimp has it (e.g. a 3-bp deletion across two
      codons gives one joined codon); if not, it is a frameshift run and every codon in it becomes X (codon '---',
      i.e. not compared), and the frame is restored at the next clean codon.
    Returns dict(prot, ccod, fs_codons, oof, nclean, fs_runs, inframe_runs). `oof` counts clean codons whose first
    base sits at an offset not divisible by 3 in the registered ungapped chimp string, i.e. the codons the
    registered arm P reads out of frame (the size of BLOCKER-1 on these data)."""
    L = r["L"]
    ncod = L // 3
    cov = bytearray(L)
    insg = {}
    for g0, rs, rows in segs:
        if not rows:
            continue
        p = g0 - 1
        for a, b in zip(rs, rows[0][3]):
            if a == "-":
                if b != "-":
                    insg[p] = insg.get(p, "") + b
            else:
                p += 1
                if 0 <= p < L:
                    cov[p] = 1
    if r["strand"] == "-":
        cov = cov[::-1]
        ins = {L - 2 - q: L1B.revcomp(s) for q, s in insg.items()}
    else:
        ins = insg
    c0u = c0.upper()
    kinds, chunks = [], []
    nb = oof = nclean = 0
    for i in range(ncod):
        b = c0u[3 * i:3 * i + 3]
        i0, i1, i2 = ins.get(3 * i, "").upper(), ins.get(3 * i + 1, "").upper(), ins.get(3 * i + 2, "").upper()
        pre = ins.get(-1, "").upper() if i == 0 else ""
        unc = not (cov[3 * i] and cov[3 * i + 1] and cov[3 * i + 2])
        chunk = (pre + b[0] + i0 + b[1] + i1 + b[2] + i2).replace("-", "")
        clean = (not unc) and "-" not in b and not i0 and not i1 and len(i2) % 3 == 0 and len(pre) % 3 == 0
        if clean:
            nclean += 1
            if (nb + len(pre)) % 3:
                oof += 1
        nb += len(chunk)
        kinds.append("U" if unc else ("C" if clean else "D"))
        chunks.append(chunk)
    prot, ccod, fsc = [], [], set()
    fs_runs = inframe_runs = 0

    def emit(s):
        for q in range(0, len(s), 3):
            t = s[q:q + 3]
            prot.append(L1.CODE.get(t, "X"))
            ccod.append(t)

    i = 0
    while i < ncod:
        k = kinds[i]
        if k == "U":
            i += 1
        elif k == "C":
            emit(chunks[i])
            i += 1
        else:
            j = i
            while j < ncod and kinds[j] == "D":
                j += 1
            s = "".join(chunks[i:j])
            if len(s) % 3 == 0:
                inframe_runs += 1
                emit(s)
            else:
                fs_runs += 1
                for q in range(i, j):
                    prot.append("X")
                    ccod.append("---")
                    fsc.add(q)
            i = j
    return dict(prot="".join(prot), ccod=ccod, fs_codons=fsc, oof=oof, nclean=nclean, fs_runs=fs_runs,
                inframe_runs=inframe_runs)


# ---------------------------------------------------------------- AMENDED: local-segment and Gblocks rules (MAJOR-5)
def path_columns(ha, ca, pairs, ncod):
    """Alignment path as columns: (score, type, human codon index or None). Substitution columns score BLOSUM62;
    a gap column costs GO (first of a run) or GE. type: I identical residue, N non-identical or X, G gap."""
    cols = []
    prev = None
    for i, j in pairs:
        if i is None or j is None:
            kind = "gi" if i is None else "gj"
            cols.append((-GO if prev != kind else -GE, "G", i if (i is not None and i < ncod) else None))
            prev = kind
        else:
            x, y = ha[i], ca[j]
            cols.append((B62.get((x, y), -1), "I" if (x == y and x != "X") else "N", i if i < ncod else None))
            prev = None
    return cols


def xdrop_segments(scores, X, smin):
    """Greedy X-drop segmentation along a fixed path. A segment starts at a positive column and runs until its
    running score falls more than X below its running maximum; it is cut back to the maximum and kept if the
    maximum is >= smin; the scan resumes after it. Columns outside kept segments are 'left unaligned' (Q181)."""
    keep = []
    n = len(scores)
    k = 0
    while k < n:
        if scores[k] <= 0:
            k += 1
            continue
        start, run, best, best_end = k, 0, 0, k
        while k < n:
            run += scores[k]
            if run > best:
                best, best_end = run, k
            if best - run > X:
                break
            k += 1
        if best >= smin:
            keep.append((start, best_end))
        k = best_end + 1
    return keep


def gblocks2(types, b3=8, b4=10):
    """Gblocks block selection with its documented defaults, for TWO sequences (so 'conserved' = 'highly
    conserved' = identical residue: b1 = 50% of N + 1 = 2, b2 = 85% of N rounded up to >= b1 = 2), b3 = 8, b4 = 10,
    b5 = no gap positions. Steps as in the Gblocks documentation: (1) stretches of contiguous nonconserved
    positions longer than b3 are rejected; (2) flanks are removed until each block ends on a conserved position;
    blocks shorter than b4 are rejected; (3) gap positions and the nonconserved positions adjacent to them are
    removed until a conserved position is reached; (4) blocks shorter than b4 after gap cleaning are rejected.
    Implemented from the documentation text; NOT validated against the Gblocks binary (not installed)."""
    n = len(types)
    keep = [True] * n
    k = 0
    while k < n:
        if types[k] != "I":
            e = k
            while e < n and types[e] != "I":
                e += 1
            if e - k > b3:
                keep[k:e] = [False] * (e - k)
            k = e
        else:
            k += 1

    def blocks():
        out, s = [], None
        for q in range(n + 1):
            on = q < n and keep[q]
            if on and s is None:
                s = q
            elif not on and s is not None:
                out.append((s, q))
                s = None
        return out

    for s, e in blocks():
        while s < e and types[s] != "I":
            keep[s] = False
            s += 1
        while e > s and types[e - 1] != "I":
            keep[e - 1] = False
            e -= 1
        if e - s < b4:
            keep[s:e] = [False] * (e - s)
    for q in range(n):
        if types[q] == "G" and keep[q]:
            keep[q] = False
            a = q - 1
            while a >= 0 and types[a] == "N":
                keep[a] = False
                a -= 1
            a = q + 1
            while a < n and types[a] == "N":
                keep[a] = False
                a += 1
    for s, e in blocks():
        if e - s < b4:
            keep[s:e] = [False] * (e - s)
    return keep


def kept_codons(cols, keepflags):
    return {c[2] for c, kf in zip(cols, keepflags) if kf and c[1] != "G" and c[2] is not None}


# ---------------------------------------------------------------- AMENDED: synonymous-divergence filter (MAJOR-6)
def dsat_drop(h, c, W=None, T=None):
    """Codons inside any window of W consecutive compared codons that holds >= T synonymous differences (NG
    path-averaged). Uses synonymous differences only, so it does not select on amino-acid conservation."""
    W = UD_W if W is None else W
    T = UD_T if T is None else T
    idx, ds = [], []
    for i in range(len(h) // 3):
        a, b = h[3 * i:3 * i + 3].upper(), c[3 * i:3 * i + 3].upper()
        if "-" in a or "-" in b or a not in L1.SITES or b not in L1.SITES:
            continue
        idx.append(i)
        ds.append(L1.DIFF[(a, b)][0] if a != b else 0.0)
    drop = set()
    n = len(idx)
    if not n:
        return drop
    w = min(W, n)
    cs = np.concatenate([[0.0], np.cumsum(ds)])
    for k in np.nonzero(cs[w:] - cs[:-w] >= T - 1e-9)[0]:
        drop.update(idx[int(k):int(k) + w])
    return drop



# ---------------------------------------------------------------- codon masks and stats
def mask_codons(c, drop):
    if not drop:
        return c
    cl = list(c)
    for k in drop:
        cl[3 * k:3 * k + 3] = "---"
    return "".join(cl)


def neighbourhood(codons, ncod, w=3):
    out = set()
    for k in codons:
        out.update(range(max(0, k - w), min(ncod, k + w + 1)))
    return out


def window_drop(score, half, thr):
    n = len(score)
    if not n:
        return set()
    cs = np.concatenate([[0], np.cumsum(score)])
    drop = set()
    for i in range(n):
        a, b = max(0, i - half), min(n, i + half + 1)
        if (cs[b] - cs[a]) / (b - a) < thr:
            drop.add(i)
    return drop


def syn_sites_k(c, kappa):
    s = 0.0
    for p in range(3):
        for bse in "ACGT":
            if bse == c[p]:
                continue
            w = kappa if {bse, c[p]} in ({"A", "G"}, {"C", "T"}) else 1.0
            m = c[:p] + bse + c[p + 1:]
            if L1.CODE[m] == L1.CODE[c]:
                s += w / (kappa + 2.0)
    return s


SITES_K = {k: {c: syn_sites_k(c, k) for c in L1.SITES} for k in KAPPAS}
FOURFOLD = {c[:2] for c in L1.SITES if all(L1.CODE.get(c[:2] + x) == L1.CODE[c] for x in "ACGT")}
TS = ({"A", "G"}, {"C", "T"})


def stats(h, c, extra=True):
    """L1's gene_stats (unchanged) plus identity, kappa-weighted S per kappa, fourfold ts/tv counts."""
    g = L1.gene_stats(h, c)
    if not extra:
        return g
    nt = mm = 0
    Sk = {k: 0.0 for k in KAPPAS}
    f4 = ts = tv = 0
    for i in range(len(h) // 3):
        a, b = h[3 * i:3 * i + 3].upper(), c[3 * i:3 * i + 3].upper()
        if "-" in a or "-" in b or a not in L1.SITES or b not in L1.SITES:
            continue
        nt += 3
        mm += (a[0] != b[0]) + (a[1] != b[1]) + (a[2] != b[2])
        for k in KAPPAS:
            Sk[k] += (SITES_K[k][a] + SITES_K[k][b]) / 2.0
        if a[:2] == b[:2] and a[:2] in FOURFOLD:
            f4 += 1
            if a[2] != b[2]:
                if {a[2], b[2]} in TS:
                    ts += 1
                else:
                    tv += 1
    g.update(nt=nt, mm=mm, ident=(1 - mm / nt) if nt else None, f4=f4, ts4=ts, tv4=tv,
             **{f"S_k{k}": Sk[k] for k in KAPPAS})
    return g


def chimp_ungapped(r, segs):
    s = "".join(rows[0][3].replace("-", "") for g0, rs, rows in segs if rows)
    return L1B.revcomp(s) if r["strand"] == "-" else s


def indel_runs(r, segs):
    """Frameshift runs (len % 3 != 0) and insertion sites (human CDS offsets, transcript orientation) on V0."""
    fs = 0
    ins_sites = []
    for g0, rs, rows in segs:
        if not rows:
            continue
        ra = np.frombuffer(rs.encode(), np.uint8)
        ca = np.frombuffer(rows[0][3].encode(), np.uint8)
        mk = np.full(len(ra), ord("."), np.uint8)
        mk[(ra != L1B.GAP) & (ca == L1B.GAP)] = ord("D")
        mk[(ra == L1B.GAP) & (ca != L1B.GAP)] = ord("I")
        hpos = np.cumsum(ra != L1B.GAP)
        for mo in re.finditer(r"D+|I+", mk.tobytes().decode()):
            if (mo.end() - mo.start()) % 3:
                fs += 1
            if mo.group()[0] == "I":
                ins_sites.append(g0 + int(hpos[mo.start()]) - 1 if mo.start() else g0)
    L = r["L"]
    if r["strand"] == "-":
        ins_sites = [L - 1 - p for p in ins_sites]
    return fs, [p // 3 for p in ins_sites if 0 <= p < L]


def noise_arms(h, c, tid):
    c = c.upper()
    out = {}
    ncod = len(h) // 3
    for rr in NR_GRID:
        rng = random.Random(zlib.crc32((tid + f"NR{rr}").encode()))
        cl = list(c)
        for p, x in enumerate(cl):
            if x in "ACGT" and rng.random() < rr:
                cl[p] = rng.choice([y for y in "ACGT" if y != x])
        out[f"NR{rr}"] = "".join(cl)
    rng = random.Random(zlib.crc32((tid + "NM").encode()))
    u, k = rng.random(), rng.randrange(max(ncod, 1))
    shifted = (c[:3 * k] + rng.choice("ACGT") + c[3 * k:])[:len(c)]
    for f in NM_GRID:
        out[f"NM{f}"] = shifted if u < f else c
    half = ncod // 2
    cc = [c[3 * i:3 * i + 3] for i in range(ncod)]
    out["NU"] = "".join(cc[(i + half) % ncod] for i in range(ncod)) if ncod else c
    return out


def _keep_only(c, keep, ncod):
    return mask_codons(c, set(range(ncod)) - keep)


PFAM = ["PA", "PAG", "PAF1", "PAF2", "PL38", "PL16", "PGB"]


def protein_family(ha, prot, ccod, ncod, fallback):
    """AMENDED arms on one chimp protein. Returns ({arm: chimp codon string}, band/cap flag, chimp-only residues,
    codon scores). When the cap skips the alignment every arm keeps `fallback` (nothing excluded) and flag = 4."""
    pairs, fl = align_capped(ha, prot)
    if pairs is None:
        return {k: fallback for k in PFAM}, fl, 0
    cPA, score, ins, pgap = apply_pairs(ha, prot, ccod, pairs, ncod)
    cols = path_columns(ha, prot, pairs, ncod)
    sc = [c[0] for c in cols]
    out = dict(PA=cPA, PAG=mask_codons(cPA, neighbourhood(pgap, ncod)),
               PAF1=mask_codons(cPA, window_drop(score, 2, 1.0)), PAF2=mask_codons(cPA, window_drop(score, 1, 3.0)))
    for name, X in (("PL38", 38), ("PL16", 16)):
        kf = [False] * len(cols)
        for s, e in xdrop_segments(sc, X, PL_SMIN):
            kf[s:e + 1] = [True] * (e - s + 1)
        out[name] = _keep_only(cPA, kept_codons(cols, kf), ncod)
    out["PGB"] = _keep_only(cPA, kept_codons(cols, gblocks2([c[1] for c in cols])), ncod)
    return out, fl, ins


def _excl(h, c0, cx, ncod, nearfs):
    ex = list("-" * len(c0))
    ga = list("-" * len(c0))
    n = near = 0
    for i in range(ncod):
        u, x = c0[3 * i:3 * i + 3], cx[3 * i:3 * i + 3]
        if "-" not in u and "-" in x:
            ex[3 * i:3 * i + 3] = u
            n += 1
            near += (i in nearfs)
        if "-" in u and "-" not in x:
            ga[3 * i:3 * i + 3] = x
    e = stats(h, "".join(ex), extra=False)
    e["ncod_x"], e["near_fs"] = n, near
    return e, stats(h, "".join(ga), extra=False)


def _agree(c0, cx, ncod):
    both = same = 0
    for i in range(ncod):
        u, x = c0[3 * i:3 * i + 3], cx[3 * i:3 * i + 3]
        if "-" not in u and "-" not in x:
            both += 1
            same += (u.upper() == x.upper())
    return both, same


def process(args):
    """One gene: returns dict(meta, arms={arm: stats}, excl={arm: stats}, gained). args = (r, human, segs, otype
    [, lite]); lite (synthetic transfer runs) skips the noise arms."""
    r, human, segs, ot = args[:4]
    lite = len(args) > 4 and args[4]
    h, chs, diag = L1B.assemble(r, human, segs)
    if diag["cov"] <= 0:
        return None
    ncod = r["L"] // 3
    tid = r["tid"]
    arms = {}
    c0 = chs["V0"]
    arms["U0"] = stats(h, c0)
    fs, ins_cod = indel_runs(r, segs)
    gap_cod = {i for i in range(ncod) if "-" in c0[3 * i:3 * i + 3]}
    ug_drop = neighbourhood(gap_cod | set(ins_cod), ncod)
    cUG = mask_codons(c0, ug_drop)
    arms["UG"] = stats(h, cUG)
    arms["UT"] = stats(h, chs["X1"])
    # REGISTERED P family (frame 0 of the ungapped chimp string; invalid as registered where the frame is lost)
    cu = chimp_ungapped(r, segs)
    pa = protein_align(h, cu)
    if pa is None:
        cP, score, bflag, pins, pgap = c0, codon_scores(h, c0), 4, 0, gap_cod
        cPG = cPF1 = cPF2 = c0
    else:
        cP, score, bflag, pins, pgap = pa
        cPG = mask_codons(cP, neighbourhood(pgap, ncod))
        cPF1 = mask_codons(cP, window_drop(score, 2, 1.0))
        cPF2 = mask_codons(cP, window_drop(score, 1, 3.0))
    strs = dict(UG=cUG, P=cP, PG=cPG, PF1=cPF1, PF2=cPF2)
    # AMENDED arms
    strs["UD"] = mask_codons(c0, dsat_drop(h, c0))
    fr = cactus_frame(r, segs, c0)
    ha = translate(h)
    fam, aflag, ains = protein_family(ha, fr["prot"], fr["ccod"], ncod, c0)
    strs.update(fam)
    for a in ARMS:
        if a not in arms:
            arms[a] = stats(h, strs[a])
    nearfs = neighbourhood(fr["fs_codons"], ncod, 10)
    excl, gained = {}, {}
    for a in EXCL_ARMS:
        excl[a], gained[a] = _excl(h, c0, strs[a], ncod, nearfs)
    both, same = _agree(c0, cP, ncod)
    bothA, sameA = _agree(c0, strs["PA"], ncod)
    nskip = 0
    if not lite:
        nz = noise_arms(h, c0, tid)
        for a, cx in nz.items():
            arms[a] = stats(h, cx, extra=False)
        for base in NOISE_P_BASES:
            cx = nz[base]
            cc = [cx[3 * i:3 * i + 3] for i in range(ncod)]
            cc = [x for x in cc if "-" not in x]
            famn, nfl, _ = protein_family(ha, "".join(L1.CODE.get(x, "X") for x in cc), cc, ncod, cx)
            nskip += (nfl == 4)
            for sfx in NOISE_P_SUFFIX:
                arms[f"{base}>{sfx}"] = stats(h, famn[sfx], extra=False)
    g0 = arms["U0"]
    is121 = ot == "ortholog_one2one"
    hq = (g0["ident"] is not None and g0["ident"] >= 0.98 and fs == 0)
    sets = ["ALL", "HQ" if hq else "NONHQ"]
    if is121:
        sets.append("O121")
    if diag["SYN"]:
        sets.append("SYN")
        if is121:
            sets.append("O121SYN")
    if (is121 and diag["SYN"] and diag["cov"] >= 0.95 and g0["gapfrac"] <= 0.02 and g0["stop_h"] == 0
            and g0["stop_c"] == 0 and g0["len_bp"] >= 300):
        sets.append("CSACp")
    meta = dict(tid=tid, gene=r["gene"], name=r["name"], L=r["L"], otype=ot or "unmapped", cov=diag["cov"],
                SYN=diag["SYN"], fs=fs, ins=len(ins_cod), band=bflag, pins=pins, agree_both=both, agree_same=same,
                ident=g0["ident"], sets=sets, chimp_len=len(cu),
                bandA=aflag, pinsA=ains, agreeA_both=bothA, agreeA_same=sameA, oof=fr["oof"], nclean=fr["nclean"],
                fs_runs=fr["fs_runs"], inframe_runs=fr["inframe_runs"], fs_codons=len(fr["fs_codons"]),
                noise_skip=nskip, skip_any=int(bflag == 4 or aflag == 4 or nskip > 0))
    return dict(meta=meta, arms=arms, excl=excl, gained=gained)


# ---------------------------------------------------------------- aggregation
def agg(gs):
    s = L1.summarise(gs)
    Nd, Sd = s.get("Nd", 0.0), s.get("Sd", 0.0)
    s["nonsyn_frac"] = Nd / (Nd + Sd) if (Nd + Sd) else None
    if gs and "S_k1" in gs[0]:
        nt = sum(g["nt"] for g in gs)
        s["ident"] = 1 - sum(g["mm"] for g in gs) / nt if nt else None
        f4 = sum(g["f4"] for g in gs)
        ts, tv = sum(g["ts4"] for g in gs), sum(g["tv4"] for g in gs)
        s["kappa_hat"] = (2.0 * ts / tv) if tv else None
        s["f4_div"] = (ts + tv) / f4 if f4 else None
        tot = sum(g["S"] + g["N"] for g in gs)
        for k in KAPPAS:
            S = sum(g[f"S_k{k}"] for g in gs)
            N = tot - S
            if S > 0 and N > 0 and Sd > 0:
                s[f"NS_k{k}"] = N / S
                s[f"dnds_k{k}"] = L1.jc(Nd / N) / L1.jc(Sd / S)
    return s


def excl_agg(gs):
    S, N = sum(g["S"] for g in gs), sum(g["N"] for g in gs)
    Sd, Nd = sum(g["Sd"] for g in gs), sum(g["Nd"] for g in gs)
    cod = sum(round((g["S"] + g["N"]) / 3.0) for g in gs)
    out = dict(codons=cod, S=S, N=N, Sd=Sd, Nd=Nd, genes_with=sum(1 for g in gs if g["S"] + g["N"] > 0))
    out["nonsyn_frac"] = Nd / (Nd + Sd) if (Nd + Sd) else None
    out["dnds_p"] = (Nd / N) / (Sd / S) if (S and N and Sd) else None
    # AMENDED (MAJOR-3): synonymous divergence of the excluded codons, and their distance to frameshift runs
    out["pS"] = Sd / S if S else None
    nx = sum(g.get("ncod_x", 0) for g in gs)
    out["ncod_x"] = nx
    out["near_fs_share"] = (sum(g.get("near_fs", 0) for g in gs) / nx) if nx else None
    return out


def flag(d):
    if d is None or d != d:
        return "n/a"
    if d >= 0.25:
        return "large"
    if d >= 0.10:
        return "moderate"
    if d >= 0.03:
        return "small"
    if d > -0.03:
        return "none"
    return "reverse"


def rflag(x):
    """AMENDED (MINOR-7): relative drop (U0 - arm) / U0."""
    if x is None or x != x:
        return "n/a"
    if x >= 0.50:
        return "large"
    if x >= 0.25:
        return "moderate"
    if x >= 0.10:
        return "small"
    if x > -0.10:
        return "none"
    return "reverse"


def band(res, pf1="PF1"):
    """REGISTERED bands (536b19b), logic unchanged. pf1='PF1' is the registered evaluation (invalid as registered
    where it rests on PF1: BLOCKER-1); pf1='PAF1' is the same rule on the frame-aware arm."""
    A = res["arms"]
    g = lambda arm, st: (A.get(arm, {}).get(st) or {}).get("dnds", float("nan"))
    U, Uc, HQ = g("U0", "ALL"), g("U0", "CSACp"), g("U0", "HQ")
    D1 = U - g(pf1, "ALL")
    nf = (A["U0"]["ALL"] or {}).get("nonsyn_frac") or float("nan")
    if U >= 0.65 and nf >= 0.66 and D1 >= 0.25 and g(pf1, "ALL") <= 0.40:
        return "DAY"
    if U >= 0.65 and D1 < 0.10 and HQ >= 0.65:
        return "HIGH-NOT-METHOD"
    if U >= 0.40 and (Uc < 0.40 or HQ < 0.40):
        return "NOISE"
    if 0.40 <= Uc < 0.65:
        return "MIDDLE"
    if U < 0.40 and Uc < 0.40:
        return "CRITIC"
    return "UNCLASSIFIED"


def _nan(v):
    return v is None or v != v


def band_amended(U, Uc, Ud, pS, nf, Rmin, xratio):
    """AMENDED bands: a decision tree, so exactly one band for every input (selftest enumerates a grid).
    U = U0 ALL; Uc = U0 on the source set (CSAC23 if the mapping floor is met, else CSACp; None = set empty);
    Ud = UD ALL (dS-clean codons); pS = pS of U0 ALL; nf = nonsyn fraction of U0 ALL; Rmin = lowest ALL value among
    the REALISTIC protein arms; xratio = pS of the codons that arm excluded / pS of the dS-clean codons (UD ALL)."""
    if _nan(U) or _nan(Ud) or _nan(pS):
        return "INVALID"
    if U < T_LO:
        return "CRITIC" if (_nan(Uc) or Uc < T_LO) else "CRITIC-ALL/SET-ABOVE"
    if Ud < T_LO or pS > PS_GATE:
        return "NOISE"
    if not _nan(Uc) and Uc < T_LO:
        return "GENE-SET"
    if U >= T_HI and Ud >= T_HI:
        if _nan(Rmin):
            return "INVALID"
        D = U - Rmin
        if D < 0.10:
            return "HIGH-NOT-METHOD"
        if D >= 0.25 and Rmin <= T_LO and not _nan(nf) and nf >= 0.66 and not _nan(xratio) and xratio <= XRATIO_MAX:
            return "DAY"
        return "HIGH-PARTIAL-METHOD"
    return "MIDDLE"


def score_amended(res, uc_set, key="dnds"):
    A = res["arms"]
    g = lambda arm, st, k=key: (A.get(arm, {}).get(st) or {}).get(k)
    U, Uc, Ud = g("U0", "ALL"), g("U0", uc_set), g("UD", "ALL")
    pS, nf = g("U0", "ALL", "pS"), g("U0", "ALL", "nonsyn_frac")
    vals = [(g(a, "ALL"), a) for a in REALISTIC if not _nan(g(a, "ALL"))]
    Rmin, Rarm = min(vals) if vals else (None, None)
    xr = res["excluded"].get(Rarm, {}).get("ALL", {}).get("pS_ratio_vs_clean") if Rarm else None
    b = band_amended(U, Uc, Ud, pS, nf, Rmin, xr)
    sub = None
    if b == "NOISE":
        sub = []
        if not _nan(Ud) and Ud < T_LO:
            sub.append("LOCAL (dS-saturated codons carry the excess)")
        if pS > PS_GATE:
            sub.append("pS-GATE (pS of U0 ALL above the gate)" + ("; UNIFORM: dS-clean codons are not low"
                                                               if not _nan(Ud) and Ud >= T_LO else ""))
        if not _nan(Rmin) and Rmin <= T_LO and U - Rmin >= 0.10:
            sub.append("FILTERED (a realistic protein arm removes it)")
    return dict(band=b, U=U, Uc=Uc, uc_set=uc_set, Ud=Ud, pS=pS, nonsyn_frac=nf, Rmin=Rmin, Rmin_arm=Rarm,
                excl_pS_ratio=xr, noise_subtag=sub)


# ---------------------------------------------------------------- AMENDED: real CSAC 2005 list (Table S23)
def sha256_file(path):
    hsh = hashlib.sha256()
    with open(path, "rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            hsh.update(blk)
    return hsh.hexdigest()


def parse_s23(b):
    """{NM_ accession (6 digits, unversioned): HGNC symbol or None} from the bytes of S23 (Excel 97 / BIFF8).
    Read as bytes only; nothing in the file is executed. Each shared string is stored as a 2-byte length, a flag
    byte and the characters, so an accession is found as b'\\x09\\x00\\x00NM_' + 6 digits and the symbol is the
    string just before it (its own 3-byte header, 1-40 printable characters). Anchoring on the header matters: a
    plain 'NM_[0-9]+' scan swallows the next string's length byte when that byte is an ASCII digit (it did, for
    1,272 ids of the held S23_NM_ids.txt)."""
    out = {}
    for mo in re.finditer(rb"\x09\x00\x00NM_(\d{6})", b):
        p = mo.start()
        sym = None
        for ln in range(1, 41):
            if b[p - ln - 3:p - ln] == bytes([ln, 0, 0]) and all(33 <= c < 127 for c in b[p - ln:p]):
                sym = b[p - ln:p].decode()
                break
        out.setdefault("NM_" + mo.group(1).decode(), sym)
    return out


def load_tx2gene(gff):
    """source_transcript (ENST, unversioned) -> source_gene (ENSG, unversioned) for every annotated feature."""
    m = {}
    opener = gzip.open if gff.endswith(".gz") else open
    with opener(gff, "rt") as fh:
        for line in fh:
            p = line.find("source_transcript=")
            if p < 0:
                continue
            t = line[p + 18:line.find(";", p)].split(".")[0]
            if t in m:
                continue
            q = line.find("source_gene=")
            if q >= 0:
                m[t] = line[q + 12:line.find(";", q)].split(".")[0]
    return m


def map_csac23(s23, nm2enst, tx2gene, txs):
    """Registered mapping rule: NM_ -> ENST (GENCODE v35 RefSeq metadata, unversioned match) -> ENSG (annotation)
    -> gene chosen by L1b's transcript rule; fallback: the S23 symbol equals the gene_name of exactly one chosen
    gene. Everything else is reported unmapped with its reason. Returns dict(gene_route, rows, acct)."""
    chosen = {r["gene"]: r["name"] for r in txs}
    name2 = {}
    for gid, nme in chosen.items():
        name2.setdefault(nme, []).append(gid)
    route, rows = {}, []
    acct = dict(n_nm=len(s23), nm=0, symbol=0, nm_ambiguous=0, unmapped_nm_absent_from_gencode_v35=0,
                unmapped_transcript_not_in_annotation=0, unmapped_gene_not_in_L1b_universe=0, no_symbol=0)
    for nm in sorted(s23):
        sym = s23[nm]
        if not sym:
            acct["no_symbol"] += 1
        ensts = nm2enst.get(nm, ())
        genes = sorted({tx2gene[e] for e in ensts if e in tx2gene})
        hit = [x for x in genes if x in chosen]
        gene, how = None, None
        if hit:
            gene = next((x for x in hit if chosen[x] == sym), hit[0])
            how = "nm"
            acct["nm_ambiguous"] += len(hit) > 1
        else:
            cand = name2.get(sym, []) if sym else []
            if len(cand) == 1:
                gene, how = cand[0], "symbol"
            else:
                how = ("unmapped_nm_absent_from_gencode_v35" if not ensts else
                       "unmapped_transcript_not_in_annotation" if not genes else
                       "unmapped_gene_not_in_L1b_universe")
        acct[how] += 1
        rows.append((nm, sym or "", how, gene or ""))
        if gene and route.get(gene) != "nm":
            route[gene] = how
    acct["distinct_genes"] = len(route)
    acct["distinct_genes_nm_route"] = sum(1 for v in route.values() if v == "nm")
    return dict(gene_route=route, rows=rows, acct=acct)


def load_csac23(xls, meta, gff, txs):
    hx, hm = sha256_file(xls), sha256_file(meta)
    assert hx == S23_SHA256, f"S23 sha256 mismatch: {hx}"
    assert hm == REFSEQ_META_SHA256, f"GENCODE RefSeq metadata sha256 mismatch: {hm}"
    with open(xls, "rb") as fh:
        s23 = parse_s23(fh.read())
    assert len(s23) == CSAC_N, len(s23)
    nm2enst = {}
    with gzip.open(meta, "rt") as fh:
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) >= 2 and f[1].startswith("NM_"):
                nm2enst.setdefault(f[1].split(".")[0], set()).add(f[0].split(".")[0])
    out = map_csac23(s23, nm2enst, load_tx2gene(gff), txs)
    out["acct"].update(s23_sha256=hx, refseq_meta_sha256=hm, refseq_meta_url=REFSEQ_META_URL,
                       nm_in_gencode_v35=sum(1 for x in s23 if x in nm2enst))
    return out


def augment_sets(recs, csac=None):
    """AMENDED set membership, fixed from U0 only. DSC: the gene's U0 pS is not above 3x the median gene pS (genes
    with >= 100 synonymous sites) with at least 5 synonymous differences; HQs = DSC and no frameshift run."""
    ps = sorted(x["arms"]["U0"]["Sd"] / x["arms"]["U0"]["S"] for x in recs if x["arms"]["U0"]["S"] >= 100)
    med = ps[len(ps) // 2] if ps else None
    for x in recs:
        m, g, s = x["meta"], x["arms"]["U0"], x["meta"]["sets"]
        noisy = bool(med is not None and g["S"] > 0 and g["Sd"] / g["S"] > 3 * med and g["Sd"] >= 5)
        m["dS_noisy"] = int(noisy)
        s.append("NONDSC" if noisy else "DSC")
        if not noisy and m["fs"] == 0:
            s.append("HQs")
        if not m["skip_any"]:
            s.append("NOSKIP")
        if csac is not None:
            rt = csac["gene_route"].get(m["gene"])
            if rt:
                s.append("CSAC23")
                if rt == "nm":
                    s.append("CSAC23nm")
            else:
                s.append("NOT23")
                if "O121" in s:
                    s.append("O121NOT23")
    return med


def conversions(extra=None):
    """MINOR-11: what a nonsynonymous fraction f means as a p-ratio dN/dS under different site ratios N/S."""
    rows = {}
    fs_ = {"Day row A 73.9%": 0.739}
    fs_.update(extra or {})
    for lab, f in fs_.items():
        if f is None or f != f or f >= 1:
            continue
        nd_sd = f / (1 - f)
        rows[lab] = dict(Nd_over_Sd=nd_sd, at_NS_2p78_CSAC=nd_sd / 2.78, at_NS_3p34_NG_L1=nd_sd / 3.34,
                         at_NS_3p54_Day_implied=nd_sd / 3.54)
    rows["no-constraint nonsyn fraction N/(N+S)"] = {"NS_2.78": 2.78 / 3.78, "NS_3.34": 3.34 / 4.34,
                                                     "NS_3.54": 3.54 / 4.54}
    return rows


def rules_table():
    """MINOR-5: what the two divergence-trimming rules do to ONE replacement between unchanged neighbours of
    BLOSUM62 self-score a. PF2/PAF2 (window 3, mean < 3) drops the codon when score < 9 - 2a, and each neighbour
    (with its synonymous sites) when its own window fails. PF1/PAF1 (window 5, mean < 1) needs sum < 5."""
    t = {}
    for a in (4, 5, 6, 7, 9, 11):
        t[f"self{a}"] = dict(PF2_drops_centre_if_score_below=9 - 2 * a, PF2_drops_neighbours_if_score_below=9 - 2 * a,
                             PF1_drops_centre_if_score_below=5 - 4 * a)
    return t


def analyse(recs, out_prefix, l1b_json=None, csac=None):
    med_pS = augment_sets(recs, csac)
    res = dict(n_genes=len(recs), arms={}, excluded={}, gained={}, flags={}, idbins={}, diag={})
    bysets = {s: [x for x in recs if s in x["meta"]["sets"]] for s in SETS}
    have_noise = bool(recs) and "NU" in recs[0]["arms"]
    all_arms = ARMS + (NOISE_ARMS + NOISE_P_ARMS if have_noise else [])
    for arm in all_arms:
        res["arms"][arm] = {s: (agg([x["arms"][arm] for x in xs]) if xs else None) for s, xs in bysets.items()}
    u0c = {s: sum(round((x["arms"]["U0"]["S"] + x["arms"]["U0"]["N"]) / 3.0) for x in xs) for s, xs in bysets.items()}
    for arm in EXCL_ARMS:
        res["excluded"][arm] = {s: excl_agg([x["excl"][arm] for x in xs]) for s, xs in bysets.items() if xs}
        res["gained"][arm] = {s: excl_agg([x["gained"][arm] for x in xs]) for s, xs in bysets.items() if xs}
        for s in res["excluded"][arm]:                       # MINOR-6: every set, not ALL only
            e = res["excluded"][arm][s]
            e["share_of_U0_codons"] = e["codons"] / u0c[s] if u0c[s] else None
            ps0 = (res["arms"]["U0"][s] or {}).get("pS")
            e["pS_ratio_vs_U0"] = (e["pS"] / ps0) if (e["pS"] is not None and ps0) else None
            psc = (res["arms"]["UD"][s] or {}).get("pS")     # dS-clean reference: U0's own pS is inflated by noise
            e["pS_ratio_vs_clean"] = (e["pS"] / psc) if (e["pS"] is not None and psc) else None
        # REGISTERED A5 second clause (kept, not discriminating: MAJOR-3): identity of the genes holding them
        w = sorted(((x["meta"]["ident"] or 0.0, x["excl"][arm]["S"] + x["excl"][arm]["N"]) for x in recs))
        tot = sum(v for _, v in w)
        acc, med_id = 0.0, None
        for idn, v in w:
            acc += v
            if tot and acc >= tot / 2:
                med_id = idn
                break
        res["excluded"][arm]["ALL"]["weighted_median_gene_ident"] = med_id
    for arm in EXCL_ARMS + ["UT"]:
        for s in ("ALL", "CSACp", "CSAC23"):
            d = rel = None
            if res["arms"][arm][s] and res["arms"]["U0"][s]:
                u = res["arms"]["U0"][s]["dnds"]
                d = u - res["arms"][arm][s]["dnds"]
                rel = d / u if u == u and u > 0 else None
            res["flags"][f"{arm}_{s}"] = dict(drop=d, flag=flag(d), rel_drop=rel, rel_flag=rflag(rel))
    ids = sorted(x["meta"]["ident"] for x in recs if x["meta"]["ident"] is not None)
    res["diag"]["ident_median_ALL"] = ids[len(ids) // 2] if ids else None
    for lo, hi in IDBINS:
        xs = [x for x in recs if x["meta"]["ident"] is not None and lo <= x["meta"]["ident"] < hi]
        res["idbins"][f"{lo}-{hi}"] = dict(n=len(xs), U0=agg([x["arms"]["U0"] for x in xs]) if xs else None)
    res["covbins"] = {}
    for lo, hi in COVBINS:
        xs = [x for x in recs if lo <= x["meta"]["cov"] < hi]
        res["covbins"][f"{lo}-{hi}"] = dict(n=len(xs), U0=agg([x["arms"]["U0"] for x in xs]) if xs else None)
    m = [x["meta"] for x in recs]
    u0 = [x["arms"]["U0"] for x in recs]
    sm = lambda k: sum(x[k] for x in m)
    res["diag"].update(
        genes_frameshift=sum(1 for x in m if x["fs"] > 0), frameshift_runs=sum(x["fs"] for x in m),
        stop_h=sum(1 for g in u0 if g["stop_h"]), stop_c=sum(1 for g in u0 if g["stop_c"]),
        fail_S=sum(1 for g in u0 if not L1.FILTERS["S"](g)), fail_G=sum(1 for g in u0 if not L1.FILTERS["G"](g)),
        fail_L=sum(1 for g in u0 if not L1.FILTERS["L"](g)),
        fail_any_SGL=sum(1 for g in u0 if not all(L1.FILTERS[k](g) for k in "SGL")),
        band_hit_widened=sum(1 for x in m if x["band"] == 1), band_hit_final=sum(1 for x in m if x["band"] == 2),
        P_no_chimp=sum(1 for x in m if x["chimp_len"] < 3),
        agree_P_U0=(sm("agree_same") / sm("agree_both")) if m and sm("agree_both") else None,
        set_sizes={s: len(xs) for s, xs in bysets.items()})
    # AMENDED diagnostics: cap skips per arm family, frame loss of the registered P, frame-aware agreement
    res["diag_amended"] = dict(
        cell_cap=CELL_CAP,
        cap_skipped_genes={"P,PG,PF1,PF2": sum(1 for x in m if x["band"] == 4),
                           "PA,PAG,PAF1,PAF2,PL38,PL16,PGB": sum(1 for x in m if x["bandA"] == 4),
                           "noise>protein arms (gene-arm pairs)": sm("noise_skip")},
        cap_widening_refused={"P family": sum(1 for x in m if x["band"] == 3),
                              "PA family": sum(1 for x in m if x["bandA"] == 3)},
        cap_skipped_tids=[x["tid"] for x in m if x["skip_any"]][:200],
        PA_band_hit_widened=sum(1 for x in m if x["bandA"] == 1), PA_band_hit_final=sum(1 for x in m if x["bandA"] == 2),
        P_frame_loss_genes=sum(1 for x in m if x["oof"] > 0),
        P_out_of_frame_share_of_clean_codons=(sm("oof") / sm("nclean")) if sm("nclean") else None,
        cactus_frameshift_runs=sm("fs_runs"), cactus_inframe_indel_runs=sm("inframe_runs"),
        genes_with_cactus_frameshift_run=sum(1 for x in m if x["fs_runs"] > 0),
        agree_PA_U0=(sm("agreeA_same") / sm("agreeA_both")) if sm("agreeA_both") else None,
        median_gene_pS=med_pS, dS_noisy_genes=sm("dS_noisy"), PS_REF=PS_REF, PS_GATE=PS_GATE)
    if have_noise:
        # noise: rate r* reaching 0.80 (REGISTERED; a restatement of U once U is known: MINOR-3)
        pts = [(0.0, res["arms"]["U0"]["ALL"]["dnds"])] + [(r, res["arms"][f"NR{r}"]["ALL"]["dnds"]) for r in NR_GRID]
        rstar = None
        for (r0, v0), (r1, v1) in zip(pts, pts[1:]):
            if v0 == v0 and v1 == v1 and v0 < 0.80 <= v1:
                rstar = r0 + (0.80 - v0) * (r1 - r0) / (v1 - v0)
                break
        res["diag"]["NR_rstar_080"] = rstar
        # AMENDED (MINOR-2): NU and NM on the p-ratio (NU's p is near saturation, JC undefined)
        res["diag_amended"]["noise_p_ratio"] = {a: res["arms"][a]["ALL"].get("dnds_p") for a in
                                                ["NU"] + [f"NM{f}" for f in NM_GRID]}
        # AMENDED (MAJOR-7 ii): protein family applied to extractions that read high
        res["noise_through_protein"] = {
            b: dict(raw=res["arms"][b]["ALL"].get("dnds"), raw_p=res["arms"][b]["ALL"].get("dnds_p"),
                    **{s: res["arms"][f"{b}>{s}"]["ALL"].get("dnds") for s in NOISE_P_SUFFIX},
                    **{s + "_p": res["arms"][f"{b}>{s}"]["ALL"].get("dnds_p") for s in NOISE_P_SUFFIX})
            for b in NOISE_P_BASES}
        ut = res["arms"]["UT"]["ALL"].get("dnds")
        res["noise_through_protein"]["UT (registered P family realigns exactly UT's bases)"] = dict(
            raw=ut, P=res["arms"]["P"]["ALL"].get("dnds"), PF1=res["arms"]["PF1"]["ALL"].get("dnds"),
            PF2=res["arms"]["PF2"]["ALL"].get("dnds"))
    res["diag"]["U0_pS_ALL"] = res["arms"]["U0"]["ALL"].get("pS")
    if l1b_json and os.path.exists(l1b_json):
        lb = json.load(open(l1b_json))["variants"]["V0"]
        res["A0"] = {s: dict(l1b=lb.get(s, {}).get("dnds"), l1c=(res["arms"]["U0"].get(s) or {}).get("dnds"))
                     for s in ("ALL", "O121", "SYN")}
        res["A0_pass"] = all(v["l1b"] is not None and v["l1c"] is not None and abs(v["l1b"] - v["l1c"]) <= 1e-9
                             for k, v in res["A0"].items() if k in ("ALL", "O121"))     # MINOR-6: asserted
    # CSAC23 accounting and floor
    if csac is not None:
        acct = dict(csac["acct"])
        present = {x["meta"]["gene"] for x in recs}
        acct["distinct_genes_in_ALL"] = sum(1 for gid in csac["gene_route"] if gid in present)
        acct["share_of_13454"] = acct["distinct_genes_in_ALL"] / CSAC_N
        acct["floor"] = CSAC_FLOOR
        acct["floor_met"] = acct["share_of_13454"] >= CSAC_FLOOR
        res["csac23"] = acct
        with open(out_prefix + ".csac23_map.tsv", "w") as fh:
            fh.write("nm\tsymbol_2005\troute\tgene\n")
            for row in csac["rows"]:
                fh.write("\t".join(row) + "\n")
    uc_set = "CSAC23" if (res.get("csac23") or {}).get("floor_met") and bysets["CSAC23"] else "CSACp"
    # bands: REGISTERED, registered rule on the frame-aware arm, AMENDED (both source sets, and at kappa-hat)
    res["band"] = band(res)
    res["band_registered_note"] = "invalid as registered (BLOCKER-1) wherever the outcome depends on PF1"
    res["band_registered_rule_on_PAF1"] = band(res, "PAF1")
    res["amended"] = score_amended(res, uc_set)
    res["amended_by_source_set"] = {s: score_amended(res, s)["band"] for s in ("CSACp", "CSAC23")}
    kh = (res["arms"]["U0"]["ALL"] or {}).get("kappa_hat")
    if not _nan(kh):
        kn = min(KAPPAS, key=lambda k: abs(k - kh))
        res["amended_kappa"] = dict(kappa_hat=kh, kappa_used=kn, **score_amended(res, uc_set, f"dnds_k{kn}"))
    # readings (rule RD): A on realistic arms only (MAJOR-9); stress arms as an upper bound
    nf0 = (res["arms"]["U0"]["ALL"] or {}).get("nonsyn_frac")
    hits = {}
    for a in REALISTIC + STRESS + ["PF2"]:
        fl = res["flags"][f"{a}_ALL"]
        e = res["excluded"][a]["ALL"]
        hits[a] = dict(drop=fl["drop"], flag=fl["flag"], rel_flag=fl["rel_flag"],
                       is_drop=fl["flag"] in ("small", "moderate", "large") or fl["rel_flag"] in
                       ("small", "moderate", "large"),
                       excl_nonsyn_enriched=bool(e["nonsyn_frac"] is not None and nf0 is not None
                                                 and e["nonsyn_frac"] > nf0),
                       excl_pS_ratio=e["pS_ratio_vs_clean"],
                       excl_dS_normal=bool(e["pS_ratio_vs_clean"] is not None
                                           and e["pS_ratio_vs_clean"] <= XRATIO_MAX))
    real = [hits[a] for a in REALISTIC]
    if any(x["is_drop"] and x["excl_nonsyn_enriched"] and x["excl_dS_normal"] for x in real):
        ra = "supported"
    elif any(x["is_drop"] for x in real):
        ra = "contested (a realistic arm lowers dN/dS, but the codons it removes are dS-saturated or not " \
             "nonsynonymous-enriched: noise removal, not a conservation bias)"
    else:
        ra = "contested (no realistic arm lowers dN/dS)"
    big = any(x["flag"] == "large" or x["rel_flag"] == "large" for x in real)
    b = res["amended"]["band"]
    rb = ("supported" if b == "DAY" else
          "contradicted" if (b in ("CRITIC", "NOISE", "GENE-SET", "CRITIC-ALL/SET-ABOVE") and not big)
          or b == "HIGH-NOT-METHOD" else "contested")
    res["readings"] = dict(
        Q180_182_A=ra, Q180_182_B=rb, arms=hits,
        A_upper_bound_stress_arms={a: hits[a]["drop"] for a in STRESS},
        A_registered_PF2="invalid as registered (BLOCKER-1); drop %s" % hits["PF2"]["drop"],
        note="A is scored on REALISTIC arms only; PAF2/PL16 are stress tests and decide nothing. B also needs the "
             "synthetic transfer table (mode `transfer`): see docstring amendment 6.")
    res["conversions"] = conversions({"this run U0 ALL": nf0,
                                      "this run NU": (res["arms"].get("NU", {}).get("ALL") or {}).get("nonsyn_frac")})
    res["rules_table"] = rules_table()
    res["fidelity_note"] = ("Pre-run, from the held CSAC 2005 text, whatever the band: the 13,454-gene 0.23 came from "
                            "a BLASTZ genome alignment; Clustal W was used only for the 7,043-gene subset (MINOR-10).")
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    hdr = ["tid", "gene", "name", "L", "otype", "cov", "SYN", "fs", "ins", "band", "ident", "agree_both",
           "agree_same", "bandA", "oof", "nclean", "fs_runs", "inframe_runs", "dS_noisy", "skip_any", "sets"]
    with gzip.open(out_prefix + ".genes.tsv.gz", "wt") as fh:
        fh.write("\t".join(hdr + [f"{a}_{k}" for a in ARMS for k in ("S", "N", "Sd", "Nd", "stop_c", "gapfrac")]
                           + [f"excl{a}_{k}" for a in EXCL_ARMS for k in ("S", "N", "Sd", "Nd")]) + "\n")
        for x in recs:
            mt = x["meta"]
            row = [str(mt[k]) if k != "sets" else ",".join(mt[k]) for k in hdr]
            row += [f"{x['arms'][a][k]:.4g}" if isinstance(x["arms"][a][k], float) else str(x["arms"][a][k])
                    for a in ARMS for k in ("S", "N", "Sd", "Nd", "stop_c", "gapfrac")]
            row += [f"{x['excl'][a][k]:.4g}" for a in EXCL_ARMS for k in ("S", "N", "Sd", "Nd")]
            fh.write("\t".join(row) + "\n")
    return res


def report(res):
    f = lambda v, p=3: "nan" if v is None or v != v else f"{v:.{p}f}"
    print(f"genes {res['n_genes']}; sets {res['diag']['set_sizes']}")
    print("Arms marked ! are invalid as registered (BLOCKER-1: frame-0 translation of the ungapped chimp string);")
    print("their frame-aware counterparts are PA, PAG, PAF1, PAF2. REGISTERED and AMENDED outputs are both shown.")
    print("arm   set       n     pooled  p-ratio mean_c2 median  NdSd  nonsynF 1diffSh  N/S(NG) N/S(k4) dnds(k4) kappa^   pS")
    for arm in [a for a in res["arms"] if a in ARMS] + [a for a in res["arms"] if a not in ARMS]:
        for s in SETS:
            d = res["arms"][arm].get(s)
            if not d or (arm not in ARMS and s != "ALL"):
                continue
            nm = arm + ("!" if arm in BLOCKER1_ARMS else "")
            print(f"{nm:11s}{s:10s}{d['n']:6d}  {f(d.get('dnds'))}   {f(d.get('dnds_p'))}   {f(d.get('mean_ratio_cap2'))}"
                  f"   {f(d.get('median_ratio'))}  {f(d.get('NdSd_raw'))} {f(d.get('nonsyn_frac'))}   "
                  f"{f(d.get('single_nonsyn_share'))}    {f(d.get('NS_ratio'), 2)}    {f(d.get('NS_k4'), 2)}    "
                  f"{f(d.get('dnds_k4'))}    {f(d.get('kappa_hat'), 2)}  {f(d.get('pS'), 4)}")
    print("excluded vs U0 (ALL): arm codons share nonsynF dnds_p median_gene_ident(reg. A5) pS pS/clean-pS nearFS | gained")
    for a in EXCL_ARMS:
        e, gn = res["excluded"][a]["ALL"], res["gained"][a]["ALL"]
        print(f"  {a + ('!' if a in BLOCKER1_ARMS else ''):6s} {e['codons']:9d} {f(e.get('share_of_U0_codons'), 4)} "
              f"{f(e['nonsyn_frac'])} {f(e['dnds_p'])} {f(e.get('weighted_median_gene_ident'), 4)} {f(e.get('pS'), 4)} "
              f"{f(e.get('pS_ratio_vs_clean'), 2)} {f(e.get('near_fs_share'))} | {gn['codons']}")
    print("mechanism flags (absolute REGISTERED, relative AMENDED):")
    for k, v in res["flags"].items():
        print(f"  {k:14s} drop {f(v['drop'])} {v['flag']:9s} rel {f(v['rel_drop'])} {v['rel_flag']}")
    print("identity bins (U0):", {k: (v["n"], f((v["U0"] or {}).get("dnds"))) for k, v in res["idbins"].items()})
    print("chimp-coverage strata (U0):", {k: (v["n"], f((v["U0"] or {}).get("dnds"))) for k, v in res["covbins"].items()})
    print("diag:", json.dumps(res["diag"], default=float))
    print("diag (amended):", json.dumps(res["diag_amended"], default=float))
    if "noise_through_protein" in res:
        print("noise worlds through the protein family:", json.dumps(res["noise_through_protein"], default=float))
    if "csac23" in res:
        print("CSAC23 mapping:", json.dumps(res["csac23"], default=float))
    if "A0" in res:
        print("A0 (L1b V0 vs L1c U0):", res["A0"], "PASS" if res["A0_pass"] else "FAIL: stop, fix, rerun post hoc")
    print("conversions (nonsyn fraction -> p-ratio dN/dS):", json.dumps(res["conversions"], default=float))
    print("trimming rules, one replacement between unchanged neighbours:", json.dumps(res["rules_table"]))
    print(res["fidelity_note"])
    print("BAND (REGISTERED, invalid as registered where it rests on PF1):", res["band"])
    print("BAND (registered rule, PAF1 in place of PF1):", res["band_registered_rule_on_PAF1"])
    print("BAND (AMENDED, primary):", json.dumps(res["amended"], default=float))
    print("BAND (AMENDED) by source set:", res["amended_by_source_set"])
    if "amended_kappa" in res:
        print("BAND (AMENDED, sites at kappa-hat; sensitivity):", json.dumps(res["amended_kappa"], default=float))
    print("READINGS:", json.dumps({k: v for k, v in res["readings"].items() if k != "arms"}, default=float))


# ---------------------------------------------------------------- driver
def gen_tasks(txs, seg_path, otype):
    by = {r["tid"]: r for r in txs}
    with gzip.open(seg_path, "rt") as fh:
        for line in fh:
            d = json.loads(line)
            r = by.get(d["tid"])
            if r is None:
                continue
            yield (r, d["human"], d["segs"], otype.get(r["gene"]))


def run(gff, orth, seg_path, out_prefix, workers="6", l1b_json=None, s23_xls=None, refseq_meta=None):
    t0 = time.time()
    txs, counts = L1B.load_annotation(gff)
    print("annotation:", json.dumps(counts), flush=True)
    otype = L1B.load_orth(orth)
    csac = None
    if s23_xls and refseq_meta:
        csac = load_csac23(s23_xls, refseq_meta, gff, txs)
        print("CSAC23 mapping (before the run):", json.dumps(csac["acct"]), flush=True)
    recs = []
    with Pool(int(workers), maxtasksperchild=500) as pool:
        for k, x in enumerate(pool.imap(process, gen_tasks(txs, seg_path, otype), chunksize=8)):
            if x is not None:
                recs.append(x)
            if k % 2000 == 0:
                print(f"[{time.time() - t0:7.0f}s] genes {k}", flush=True)
    res = analyse(recs, out_prefix, l1b_json, csac)
    res["annotation"] = counts
    res["seconds"] = time.time() - t0
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    report(res)


# ---------------------------------------------------------------- AMENDED: synthetic transfer function (MAJOR-7 i)
TF_OMEGAS = [0.23, 0.5, 0.8, 1.0]
TF_CLUSTER = {0: None, 1: (0.02, 0.5), 2: (0.01, 0.8)}   # (share of codons in hot runs, share of replacements there)
TF_NOISE = ["clean", "indel", "misreg05", "misreg25"]
TF_DS = 0.012
TF_RUN = 15
SENSE_LIST = sorted(L1.SITES)


def _tf_gene(seed, ncod, omega, cluster, noise):
    """One synthetic human-chimp gene. Substitutions: each position is hit with probability TF_DS * max(1, w);
    a synonymous hit is accepted with probability 1 / max(1, w), a nonsynonymous one with w / max(1, w), where w
    is the codon's omega (stops rejected). Clustering: hot runs of TF_RUN codons hold the stated share of
    replacements, the gene-wide mean omega is unchanged in expectation. Uniform codon usage, kappa = 1 (ASSUMED,
    unlike real genes). Noise (ASSUMED design rates, not sourced; the real run reports the measured ones):
      indel     10% of genes carry one in-frame 3/6/9-bp chimp deletion or insertion at an arbitrary base, 5% a
                1-bp chimp indel, all placed correctly by the aligner (gapped rows);
      misregNN  NN% of genes have a 40-codon stretch in which the chimp row is shifted by one base with NO gap
                (a misaligned stretch that the unguided arm compares as is)."""
    rng = random.Random(seed)
    h = "ATG" + "".join(rng.choice(SENSE_LIST) for _ in range(ncod - 2)) + "TAA"
    w = [omega] * ncod
    cl = TF_CLUSTER[cluster]
    if cl:
        frac, share = cl
        w = [omega * (1 - share) / (1 - frac)] * ncod
        x = frac * ncod / TF_RUN
        nrun = int(x) + (rng.random() < x - int(x))
        for _ in range(nrun):
            s = rng.randrange(1, max(2, ncod - TF_RUN - 1))
            for q in range(s, min(ncod - 1, s + TF_RUN)):
                w[q] = omega * share / frac
    c = []
    for i in range(ncod):
        b = h[3 * i:3 * i + 3]
        if 0 < i < ncod - 1:
            wm = max(1.0, w[i])
            for p in range(3):
                if rng.random() < TF_DS * wm:
                    mcod = b[:p] + rng.choice([y for y in "ACGT" if y != b[p]]) + b[p + 1:]
                    if L1.CODE[mcod] == "*":
                        continue
                    if rng.random() < ((1.0 if L1.CODE[mcod] == L1.CODE[b] else w[i]) / wm):
                        b = mcod
        c.append(b)
    rs, cs = h, "".join(c)
    L = len(h)
    if noise == "indel":
        u = rng.random()
        p = rng.randrange(30, L - 30)
        if u < 0.10:
            k = rng.choice([3, 6, 9])
            if rng.random() < 0.5:
                cs = cs[:p] + "-" * k + cs[p + k:]
            else:
                rs = rs[:p] + "-" * k + rs[p:]
                cs = cs[:p] + "".join(rng.choice("ACGT") for _ in range(k)) + cs[p:]
        elif u < 0.15:
            if rng.random() < 0.5:
                cs = cs[:p] + "-" + cs[p + 1:]
            else:
                rs = rs[:p] + "-" + rs[p:]
                cs = cs[:p] + rng.choice("ACGT") + cs[p:]
    elif noise.startswith("misreg"):
        if rng.random() < int(noise[6:]) / 100.0:
            k = 3 * rng.randrange(10, max(11, ncod - 50))
            cs = cs[:k] + rng.choice("ACGT") + cs[k:k + 119] + cs[k + 120:]
    tid = f"S{seed}"
    r = dict(tid=tid, gene=tid, name=tid, src_tx="", chrom="chr1", strand="+", L=L, cds=[(0, L)], tags=[])
    return r, h, [[0, rs, [["chrS", "+", 0, cs]]]]


def _tf_one(a):
    seed, ncod, omega, cluster, noise = a
    r, h, segs = _tf_gene(seed, ncod, omega, cluster, noise)
    x = process((r, h, segs, "ortholog_one2one", True))
    return None if x is None else dict(arms=x["arms"], excl=x["excl"], meta=dict(oof=x["meta"]["oof"]))


def transfer_cells(G, ncod, mapper, only=None):
    out = []
    for ci, (om, cl, nz) in enumerate((o, c, z) for o in TF_OMEGAS for c in TF_CLUSTER for z in TF_NOISE):
        if only is not None and (om, cl, nz) not in only:
            continue
        xs = [x for x in mapper(_tf_one, [(1_000_000 * (ci + 1) + gi, ncod, om, cl, nz) for gi in range(G)]) if x]
        row = dict(omega_in=om, cluster=cl, noise=nz, n=len(xs),
                   P_frame_loss_genes=sum(1 for x in xs if x["meta"]["oof"] > 0), out={}, out_p={}, excl_share={})
        u0c = sum(round((x["arms"]["U0"]["S"] + x["arms"]["U0"]["N"]) / 3.0) for x in xs)
        for a in ARMS:
            s = agg([x["arms"][a] for x in xs])
            row["out"][a], row["out_p"][a] = s.get("dnds"), s.get("dnds_p")
            if a in EXCL_ARMS:
                row["excl_share"][a] = excl_agg([x["excl"][a] for x in xs])["codons"] / u0c if u0c else None
        out.append(row)
    truth = {(r["omega_in"], r["cluster"]): r["out"]["U0"] for r in out if r["noise"] == "clean"}
    for r in out:
        r["truth_U0_clean"] = truth[(r["omega_in"], r["cluster"])]
    return out


def transfer_report(rows):
    f = lambda v: " nan " if v is None or v != v else f"{v:5.3f}"
    print("synthetic transfer function: pooled JC dN/dS out, per arm (! = invalid as registered, BLOCKER-1)")
    print("omega cl noise     truth  " + " ".join(f"{a + ('!' if a in BLOCKER1_ARMS else ''):>6s}" for a in ARMS))
    for r in rows:
        print(f"{r['omega_in']:4.2f}  {r['cluster']}  {r['noise']:9s} {f(r['truth_U0_clean'])}  "
              + " ".join(f"{f(r['out'][a]):>6s}" for a in ARMS))
    hi = [r for r in rows if r["omega_in"] == 0.8]
    print("Scored statements (docstring amendment 6):")
    for r in hi:
        low = [a for a in REALISTIC if r["out"][a] == r["out"][a] and r["out"][a] <= T_LO]
        print(f"  omega 0.80 cluster {r['cluster']} {r['noise']:9s}: realistic arms reading <= 0.40: {low or 'none'}; "
              f"stress arms: " + ", ".join(f"{a} {f(r['out'][a])}" for a in STRESS))


def transfer(out_prefix, workers="8", genes="2000", ncod="300"):
    t0 = time.time()
    with Pool(int(workers), maxtasksperchild=2000) as pool:
        rows = transfer_cells(int(genes), int(ncod), lambda fn, it: pool.imap(fn, it, chunksize=16))
    res = dict(rows=rows, genes_per_cell=int(genes), ncod=int(ncod), ds=TF_DS, cluster=TF_CLUSTER, run=TF_RUN,
               seconds=time.time() - t0)
    with open(out_prefix + ".transfer.json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    transfer_report(rows)


# ---------------------------------------------------------------- POST HOC (fix pass, 2026-10-13): transfer-excl
# Additive mode. Reuses _tf_one, agg and excl_agg unchanged; same cell index and seeds as transfer_cells.
TFX_NOISE = ["clean", "misreg25"]
TFX_SCORED = ["PAF1", "PGB"]
TFX_MINCOD = 50


def _tfx_window(nf, pr):
    if nf is None or pr is None:
        return "undefined"
    if nf <= 0.80 and pr <= 1.5:
        return "MISPAIRING"
    if nf >= 0.90 and pr >= 3.0:
        return "DENSE-RUN"
    return "AMBIGUOUS"


def transfer_excl_cells(G, ncod, mapper):
    out = []
    for ci, (om, cl, nz) in enumerate((o, c, z) for o in TF_OMEGAS for c in TF_CLUSTER for z in TF_NOISE):
        if nz not in TFX_NOISE:
            continue
        xs = [x for x in mapper(_tf_one, [(1_000_000 * (ci + 1) + gi, ncod, om, cl, nz) for gi in range(G)]) if x]
        u0c = sum(round((x["arms"]["U0"]["S"] + x["arms"]["U0"]["N"]) / 3.0) for x in xs)
        ud = agg([x["arms"]["UD"] for x in xs])
        ps_ud = (ud["Sd"] / ud["S"]) if ud.get("S") else None
        row = dict(omega_in=om, cluster=cl, noise=nz, n=len(xs), U0_codons=u0c, pS_UD=ps_ud, out={}, excl={})
        for a in ARMS:
            row["out"][a] = agg([x["arms"][a] for x in xs]).get("dnds")
        for a in EXCL_ARMS:
            e = excl_agg([x["excl"][a] for x in xs])
            pn = (e["Nd"] / e["N"]) if e["N"] else None
            row["excl"][a] = dict(codons=e["codons"], share=(e["codons"] / u0c if u0c else None), Sd=e["Sd"],
                                  Nd=e["Nd"], S=e["S"], N=e["N"], pS=e["pS"], pN=pn,
                                  x_vs_cell_UD=(e["pS"] / ps_ud if (e["pS"] is not None and ps_ud) else None),
                                  nonsyn_frac=e["nonsyn_frac"], p_ratio=e["dnds_p"],
                                  window=_tfx_window(e["nonsyn_frac"], e["dnds_p"]))
        out.append(row)
    return out


def transfer_excl_report(rows, ref=None):
    f = lambda v, w=6, d=3: " " * (w - 3) + "nan" if v is None or v != v else f"{v:{w}.{d}f}"
    print("POST HOC transfer-excl: what each arm drops on synthetic cells (windows fixed in the docstring)")
    if ref is not None:
        key = {(r["omega_in"], r["cluster"], r["noise"]): r for r in ref}
        worst = 0.0
        for r in rows:
            q = key[(r["omega_in"], r["cluster"], r["noise"])]
            for a in ARMS:
                u, v = r["out"][a], q["out"][a]
                if (u is None or u != u) and (v is None or v != v):
                    continue
                worst = max(worst, abs(u - v))
        print(f"X1 consistency against the committed transfer table: max |difference| = {worst:.3e} "
              f"({'PASS' if worst <= 1e-9 else 'FAIL'})")
    print("omega cl noise     arm   codons  share%     pS      x     pN  nsfrac  p-ratio  window")
    for r in rows:
        for a in ["UD", "PA", "PAG", "PAF1", "PL38", "PGB", "PAF2", "PL16"]:
            e = r["excl"][a]
            print(f"{r['omega_in']:4.2f}  {r['cluster']}  {r['noise']:9s} {a:5s} {e['codons']:7d} "
                  f"{f(100 * e['share'] if e['share'] is not None else None, 7, 3)} {f(e['pS'], 6, 4)} "
                  f"{f(e['x_vs_cell_UD'], 6, 1)} {f(e['pN'], 6, 3)} {f(e['nonsyn_frac'], 7, 3)} "
                  f"{f(e['p_ratio'], 8, 2)}  {e['window'] if e['codons'] >= TFX_MINCOD else 'under 50 codons'}")
    print("Scored statements (PAF1, PGB; cells with >= 50 dropped codons):")
    for lab, sel in (("X3 clean clustered cells in DENSE-RUN", lambda r: r["noise"] == "clean" and r["cluster"] > 0),
                     ("X4 misreg25 clustering-0 cells in MISPAIRING", lambda r: r["noise"] == "misreg25"
                      and r["cluster"] == 0)):
        want = "DENSE-RUN" if lab.startswith("X3") else "MISPAIRING"
        cells = [(r, a) for r in rows if sel(r) for a in TFX_SCORED if r["excl"][a]["codons"] >= TFX_MINCOD]
        bad = [(r["omega_in"], r["cluster"], a, r["excl"][a]["window"]) for r, a in cells
               if r["excl"][a]["window"] != want]
        print(f"  {lab}: {len(cells) - len(bad)} of {len(cells)} arm-cells; exceptions: {bad or 'none'}")
    x5 = [(r["omega_in"], r["cluster"], a) for r in rows if r["noise"] == "clean" and r["cluster"] > 0
          for a in TFX_SCORED if r["excl"][a]["codons"] >= TFX_MINCOD and r["excl"][a]["window"] == "MISPAIRING"]
    print(f"  X5 clean clustered arm-cells in MISPAIRING: {x5 or 'none'}")
    for r in rows:
        if r["noise"] == "clean" and r["cluster"] == 2 and r["omega_in"] == 0.8:
            print("  X2 clean 0.8 clustering 2, x: " + ", ".join(f"{a} {f(r['excl'][a]['x_vs_cell_UD'], 5, 1)}"
                                                                 for a in TFX_SCORED))
        if r["noise"] == "misreg25" and r["cluster"] == 0:
            print(f"  X4 misreg25 clustering 0 omega {r['omega_in']:4.2f}, x: "
                  + ", ".join(f"{a} {f(r['excl'][a]['x_vs_cell_UD'], 5, 1)}" for a in TFX_SCORED))


def transfer_excl(out_prefix, workers="2", genes="2000", ncod="300", ref_json=None):
    t0 = time.time()
    with Pool(int(workers), maxtasksperchild=2000) as pool:
        rows = transfer_excl_cells(int(genes), int(ncod), lambda fn, it: pool.imap(fn, it, chunksize=16))
    ref = json.load(open(ref_json))["rows"] if ref_json else None
    res = dict(rows=rows, genes_per_cell=int(genes), ncod=int(ncod), ds=TF_DS, cluster=TF_CLUSTER, run=TF_RUN,
               noise=TFX_NOISE, windows=dict(MISPAIRING="nonsyn_frac <= 0.80 and p_ratio <= 1.5",
                                             DENSE_RUN="nonsyn_frac >= 0.90 and p_ratio >= 3.0"),
               min_codons=TFX_MINCOD, ref_json=ref_json, seconds=time.time() - t0)
    with open(out_prefix + ".transfer_excl.json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    transfer_excl_report(rows, ref)


# ---------------------------------------------------------------- selftest (synthetic; trivial)
def _sim_gene(rng, ncod, omega, ds):
    sense = [c for c in L1.SITES]
    h = "ATG" + "".join(rng.choice(sense) for _ in range(ncod - 2)) + "TAA"
    c = []
    for i in range(ncod):
        a = h[3 * i:3 * i + 3]
        b = a
        if 0 < i < ncod - 1:
            for p in range(3):
                if rng.random() < ds:
                    m = b[:p] + rng.choice([x for x in "ACGT" if x != b[p]]) + b[p + 1:]
                    if L1.CODE[m] == "*":
                        continue
                    if L1.CODE[m] == L1.CODE[b] or rng.random() < omega:
                        b = m
        c.append(b)
    return h, "".join(c)


def _mkrec(tid, h, rs, cs, strand="+"):
    r = dict(tid=tid, gene="G" + tid, name="N" + tid, src_tx="", chrom="chr1", strand=strand, L=len(h),
             cds=[(0, len(h))], tags=[])
    return r, [[0, rs, [["chrS", "+", 0, cs]]]]


def selftest_amended():
    """Tests added 2026-10-12 for the pre-run amendments. Includes the BLOCKER-1 test: it FAILS on the registered
    arm P and PASSES on the frame-aware arm PA."""
    global CELL_CAP
    rng = random.Random(7)
    # (1) rolled-row aligner returns exactly the registered alignment
    for _ in range(150):
        a = "".join(rng.choice(_AA) for _ in range(rng.randrange(1, 60)))
        b = list(a)
        for _k in range(rng.randrange(0, 6)):
            q = rng.randrange(len(b) + 1)
            if rng.random() < 0.5 and b:
                del b[min(q, len(b) - 1)]
            else:
                b.insert(q, rng.choice(_AA))
        b = "".join(b) or "A"
        for B in (2, 8, 40):
            assert nw_banded(a, b, B) == nw_banded_registered(a, b, B), (a, b, B)
    assert band_cells(10, 10, 100) == 11 * 11
    # (2) BLOCKER-1: a 1-bp chimp deletion that the genome aligner placed correctly (gapped row), at codon 60 of 200
    h, c = _sim_gene(rng, 200, 0.25, 0.015)
    cs = c[:181] + "-" + c[182:]
    r, segs = _mkrec("FB", h, h, cs)
    x = process((r, h, segs, "ortholog_one2one", True))
    m = x["meta"]

    def frame_ok(same, both):
        return both > 0 and same / both > 0.99

    assert m["fs"] == 1 and m["fs_runs"] == 1 and m["oof"] >= 130, m
    assert not frame_ok(m["agree_same"], m["agree_both"]), "registered P should lose the frame here"   # old arm FAILS
    assert frame_ok(m["agreeA_same"], m["agreeA_both"]), "frame-aware PA must keep the Cactus frame"   # new arm PASSES
    u, pa, pr = x["arms"]["U0"], x["arms"]["PA"], x["arms"]["P"]
    assert abs(pa["Nd"] - u["Nd"]) < 1e-9 and abs(pa["Sd"] - u["Sd"]) < 1e-9 and abs(pa["S"] - u["S"]) < 1e-9
    assert pr["Nd"] > 3 * u["Nd"] + 5, (pr["Nd"], u["Nd"])
    assert x["excl"]["PAF1"]["ncod_x"] <= 3 and x["excl"]["PF1"]["ncod_x"] >= 50, (x["excl"]["PAF1"], x["excl"]["PF1"])
    # same on the minus strand, and with a 1-bp insertion
    rs2 = h[:300] + "-" + h[300:]
    cs2 = c[:300] + "A" + c[300:]
    for strand in "+-":
        hh = h if strand == "+" else L1B.revcomp(h)
        r, segs = _mkrec("FI" + strand, hh, rs2 if strand == "+" else L1B.revcomp(rs2), cs2 if strand == "+"
                         else L1B.revcomp(cs2), strand)
        x = process((r, hh, segs, "ortholog_one2one", True))
        m = x["meta"]
        assert m["oof"] >= 90 and not frame_ok(m["agree_same"], m["agree_both"]), (strand, m)
        assert m["agreeA_same"] == m["agreeA_both"] and m["agreeA_both"] >= 199, (strand, m)
    # in-frame 3-bp deletion across two codons: read as one joined chimp codon, no frameshift, no X
    cs3 = c[:181] + "---" + c[184:]
    r, segs = _mkrec("IF", h, h, cs3)
    fr = cactus_frame(r, segs, cs3)
    assert fr["fs_runs"] == 0 and fr["inframe_runs"] == 1 and len(fr["prot"]) == 199 and "---" not in fr["ccod"]
    assert fr["ccod"][60] == c[180] + c[184:186], fr["ccod"][60]
    # uncovered stretch of 100 bp (not a multiple of 3): nothing emitted there, frame intact after it
    r = dict(tid="UC", gene="GUC", name="N", src_tx="", chrom="chr1", strand="+", L=600, cds=[(0, 600)], tags=[])
    segs = [[0, h[:200], [["chrS", "+", 0, c[:200]]]], [300, h[300:], [["chrS", "+", 300, c[300:]]]]]
    x = process((r, h, segs, "ortholog_one2one", True))
    assert x["meta"]["oof"] > 50 and x["meta"]["agreeA_same"] == x["meta"]["agreeA_both"], x["meta"]
    assert x["meta"]["agree_same"] < 0.8 * x["meta"]["agree_both"]
    # (3) hard cap: skip and count, arms fall back to the U0 pairing
    old = CELL_CAP
    CELL_CAP = 1000
    r, segs = _mkrec("CAP", h, h, c)
    x = process((r, h, segs, "ortholog_one2one", True))
    CELL_CAP = old
    assert x["meta"]["band"] == 4 and x["meta"]["bandA"] == 4 and x["meta"]["skip_any"] == 1
    assert x["excl"]["PAF1"]["ncod_x"] == 0 and x["arms"]["PGB"]["Nd"] == x["arms"]["U0"]["Nd"]
    assert align_capped("A" * 10, "A" * 10)[1] == 0
    # (4) local segments and Gblocks rule: an isolated replacement stays, a substitution-rich run goes
    sc = [5] * 30 + [-2] * 12 + [5] * 30
    assert xdrop_segments(sc, 38, 40) == [(0, 71)] and xdrop_segments(sc, 16, 40) == [(0, 29), (42, 71)]
    assert xdrop_segments([5] * 30 + [-3] + [5] * 30, 16, 40) == [(0, 60)]
    assert xdrop_segments([5] * 5 + [-9] * 9 + [5] * 5, 16, 40) == []
    t = list("I" * 20 + "N" + "I" * 20 + "N" * 9 + "I" * 20 + "NGGN" + "I" * 5 + "N" * 9 + "I" * 12)
    k = gblocks2(t)
    assert k[20] and not any(k[41:50]) and not any(k[70:74]) and all(k[50:70]), "".join("x" if q else "." for q in k)
    assert not any(k[74:79]) and all(k[88:100])                       # 5-long block between rejects is dropped
    # protein family on a gene with a 12-codon run of replacements (V -> D, BLOSUM62 -3 each, no synonymous change):
    # global alignment keeps it paired (PA), the lenient local rule keeps it (PL38), the strict local rule, the
    # Gblocks rule and the window rule drop it; the dS filter does not touch it (real divergence, normal dS)
    hh = "ATG" + "GCT" * 60 + "GTT" * 12 + "GCT" * 60 + "TAA"
    cc = "ATG" + "GCT" * 60 + "GAT" * 12 + "GCT" * 60 + "TAA"
    r, segs = _mkrec("DV", hh, hh, cc)
    x = process((r, hh, segs, "ortholog_one2one", True))
    nx = {a: x["excl"][a]["ncod_x"] for a in EXCL_ARMS}
    assert nx["PA"] == 0 and nx["PL38"] == 0 and nx["PGB"] == 12 and nx["PL16"] == 12 and nx["PAF1"] >= 8, nx
    assert nx["UD"] == 0, nx
    # ... and a run of 12 at -4 each (L -> D) IS gapped by the global aligner itself (two gaps cost 44 < 48), so
    # "global scoring never gaps a substituted codon" (review MAJOR-5) holds only for runs cheaper than two gaps
    cc = "ATG" + "GCT" * 60 + "GAT" * 12 + "GCT" * 60 + "TAA"
    hh = "ATG" + "GCT" * 60 + "CTG" * 12 + "GCT" * 60 + "TAA"
    r, segs = _mkrec("DV2", hh, hh, cc)
    assert process((r, hh, segs, "ortholog_one2one", True))["excl"]["PA"]["ncod_x"] == 12
    # (5) dS-saturation filter: flags a misregistered stretch, leaves ordinary divergence alone
    h, c = _sim_gene(rng, 300, 0.25, 0.012)
    cm = c[:300] + "G" + c[300:419] + c[420:]
    d = dsat_drop(h, cm)
    assert len([q for q in d if 100 <= q < 140]) >= 30 and len(dsat_drop(h, c)) <= 20
    # (6) amended bands: exactly one registered band for every input, including missing values
    grid = [None, float("nan"), 0.1, 0.39, 0.40, 0.5, 0.649, 0.65, 0.9]
    seen = set()
    for U in grid:
        for Uc in grid:
            for Ud in grid:
                for pS in (None, 0.012, 0.023, 0.0231, 0.05):
                    for Rm in (None, 0.2, 0.40, 0.41, 0.6, 0.9):
                        for xr in (None, 1.0, 3.0, 3.01):
                            for nf in (None, 0.5, 0.66, 0.74):
                                b = band_amended(U, Uc, Ud, pS, nf, Rm, xr)
                                assert b in BANDS_AM, b
                                seen.add(b)
                                if b == "DAY":
                                    assert U >= 0.65 and Ud >= 0.65 and pS <= PS_GATE and Uc != 0.1 and Uc != 0.39
                                    assert Rm <= 0.40 and U - Rm >= 0.25 and xr <= 3.0 and nf >= 0.66
    assert seen == set(BANDS_AM), set(BANDS_AM) - seen
    assert band_amended(0.80, 0.78, 0.79, 0.016, 0.74, 0.25, 1.2) == "DAY"
    assert band_amended(0.80, 0.78, 0.79, 0.016, 0.74, 0.25, 9.0) == "HIGH-PARTIAL-METHOD"   # trimmed codons saturated
    assert band_amended(0.80, 0.78, 0.30, 0.016, 0.74, 0.25, 1.2) == "NOISE"                 # excess in dS-noisy codons
    assert band_amended(0.80, 0.78, 0.79, 0.040, 0.74, 0.25, 1.2) == "NOISE"                 # uniform noise
    assert band_amended(0.80, 0.25, 0.79, 0.016, 0.74, 0.25, 1.2) == "GENE-SET"
    assert band_amended(0.80, 0.78, 0.50, 0.016, 0.74, 0.25, 1.2) == "MIDDLE"
    assert band_amended(0.27, 0.21, 0.27, 0.016, 0.6, 0.27, None) == "CRITIC"
    assert rflag(0.19 / 0.27) == "large" and flag(0.19) == "moderate"                         # MINOR-7 example
    # (7) pure-noise worlds (true omega 0.25) must never score DAY
    import tempfile
    tdir = tempfile.mkdtemp()
    for world in ("misreg", "uniform"):
        recs = []
        for gi in range(60):
            h, c = _sim_gene(rng, 200, 0.25, 0.015)
            if world == "misreg" and gi % 2 == 0:
                c = c[:150] + "G" + c[150:-1]
            if world == "uniform":
                cl = list(c)
                for p in range(3, len(cl) - 3):
                    if rng.random() < 0.03:
                        cl[p] = rng.choice([y for y in "ACGT" if y != cl[p]])
                c = "".join(cl)
            r, segs = _mkrec(f"{world}{gi}", h, h, c)
            y = process((r, h, segs, "ortholog_one2one", True))
            if y:
                recs.append(y)
        res = analyse(recs, os.path.join(tdir, world))
        am = res["amended"]
        assert am["U"] >= 0.40, (world, am)
        assert am["band"] == "NOISE", (world, am)
        assert res["readings"]["Q180_182_B"] != "supported"
        if world == "misreg":
            assert am["Ud"] < 0.40 and am["nonsyn_frac"] > 0.66, am       # Day's 74% signature, from noise alone
            assert res["readings"]["Q180_182_A"].startswith("contested"), res["readings"]["Q180_182_A"]
            e = res["excluded"]["PAF1"]["ALL"]
            assert e["pS_ratio_vs_clean"] > XRATIO_MAX > e["pS_ratio_vs_U0"], e   # why the clean reference is used
    # (8) S23 parser and mapping rule on synthetic bytes
    def sst(s):
        return bytes([len(s), 0, 0]) + s.encode()
    blob = b"junk" + sst("GENE1") + sst("NM_000015") + sst("d" * 53) + sst("OLDSYM") + sst("NM_000016") + \
        sst("x") + sst("GENE3") + sst("NM_000017") + sst("7 desc") + sst("GENE4") + sst("NM_000018") + sst("d")
    s23 = parse_s23(blob)
    assert s23 == {"NM_000015": "GENE1", "NM_000016": "OLDSYM", "NM_000017": "GENE3", "NM_000018": "GENE4"}, s23
    assert re.findall(rb"NM_\d+", blob)[0] == b"NM_0000155"               # the artefact the anchored parser avoids
    txs = [dict(gene="ENSG1", name="GENE1"), dict(gene="ENSG2", name="NEWSYM"), dict(gene="ENSG3", name="GENE3")]
    mp = map_csac23(s23, {"NM_000015": {"ENST1"}, "NM_000016": {"ENST2"}, "NM_000018": {"ENST9"}},
                    {"ENST1": "ENSG1", "ENST2": "ENSG2", "ENST9": "ENSG9"}, txs)
    assert mp["gene_route"] == {"ENSG1": "nm", "ENSG2": "nm", "ENSG3": "symbol"}, mp["gene_route"]
    assert mp["acct"]["unmapped_gene_not_in_L1b_universe"] == 1 and mp["acct"]["symbol"] == 1
    # (9) transfer function, tiny: clean cells return the input; the registered P breaks on Cactus-placed 1-bp indels
    only = [(0.23, 0, "clean"), (1.0, 0, "clean"), (0.23, 0, "indel"), (0.23, 0, "misreg25"), (0.8, 0, "clean"),
            (0.8, 2, "clean")]
    rows = transfer_cells(100, 150, lambda fn, it: map(fn, it), only)
    by = {(r["omega_in"], r["cluster"], r["noise"]): r for r in rows}
    assert len(rows) == len(only)
    transfer_report(rows)
    lo, hi = by[(0.23, 0, "clean")]["out"], by[(1.0, 0, "clean")]["out"]
    assert lo["U0"] < 0.45 < 0.65 < hi["U0"], (lo["U0"], hi["U0"])
    assert abs(lo["PA"] - lo["U0"]) < 1e-9 and abs(hi["PA"] - hi["U0"]) < 1e-9
    assert by[(0.23, 0, "indel")]["P_frame_loss_genes"] >= 1
    assert by[(0.23, 0, "misreg25")]["out"]["U0"] > lo["U0"]
    assert by[(0.8, 2, "clean")]["excl_share"]["PGB"] > by[(0.8, 0, "clean")]["excl_share"]["PGB"]
    assert conversions()["Day row A 73.9%"]["at_NS_2p78_CSAC"] > 1.0
    print("selftest (amended) ok")


def selftest():
    import tempfile
    # matrix sanity
    assert all(B62[(x, y)] == B62[(y, x)] for x in _AA for y in _AA)
    assert [B62[(x, x)] for x in _AA] == [4, 5, 6, 6, 9, 5, 5, 6, 8, 4, 4, 5, 5, 6, 7, 4, 5, 11, 7, 4]
    # kappa = 1 equals NG sites
    assert all(abs(SITES_K[1][c] - L1.SITES[c]) < 1e-12 for c in L1.SITES)
    # aligner: identity, one deletion, terminal frameshift
    p, hit = nw_banded("MKVLAAGIL", "MKVLAAGIL", 4)
    assert p == [(i, i) for i in range(9)] and not hit
    p, _ = nw_banded("MKVLWWAAGIL", "MKVLAAGIL", 6)
    assert sum(1 for i, j in p if j is None) == 2 and len(p) == 11, p
    rng = random.Random(1)
    h, c = _sim_gene(rng, 120, 0.25, 0.02)
    cP, score, fl, ins, gaps = protein_align(h, c)
    assert cP == c and fl == 0 and ins == 0, "identical-length protein alignment must keep the Cactus pairing"
    fsc = c[:180] + "A" + c[180:-1]                      # 1-bp insertion at codon 60: tail out of frame
    cP2, score2, _, _, _ = protein_align(h, fsc)
    drop = window_drop(score2, 2, 1.0)
    assert len([k for k in drop if k > 62]) > 30, "PF1 must trim the frame-shifted tail"
    # indel runs: 2-bp chimp insertion after human base 2, 1-bp deletion at human base 4 -> 2 frameshift runs
    fs, insc = indel_runs(dict(L=6, strand="+"), [[0, "ATG--GCA", [["c", "+", 0, "ATGTTG-A"]]]])
    assert fs == 2 and insc == [0], (fs, insc)
    fs, insc = indel_runs(dict(L=6, strand="-"), [[0, "ATG--GCA", [["c", "+", 0, "ATGTTG-A"]]]])
    assert insc == [1], insc
    # synthetic end-to-end: 40 genes, omega 0.25, one gene frame-shifted in the chimp
    txs, lines = [], []
    for gi in range(40):
        h, c = _sim_gene(rng, 200, 0.25, 0.015)
        if gi == 7:
            c = c[:300] + "G" + c[300:-1]
        tid = f"T{gi}"
        r = dict(tid=tid, gene=f"G{gi}", name=f"N{gi}", src_tx="", chrom="chr1", strand="+", L=len(h),
                 cds=[(1000 * gi, 1000 * gi + len(h))], tags=[])
        txs.append(r)
        lines.append(dict(tid=tid, human=h, segs=[[0, h, [["chrS", "+", 1000 * gi, c]]]]))
    d = tempfile.mkdtemp()
    sp = os.path.join(d, "seg.json.gz")
    with gzip.open(sp, "wt") as fh:
        for x in lines:
            fh.write(json.dumps(x) + "\n")
    ot = {f"G{gi}": "ortholog_one2one" for gi in range(30)}
    recs = [x for x in map(process, gen_tasks(txs, sp, ot)) if x]
    res = analyse(recs, os.path.join(d, "o"))
    A = res["arms"]
    u, pf1, nu = A["U0"]["ALL"]["dnds"], A["PF1"]["ALL"]["dnds"], A["NU"]["ALL"]
    uh = A["U0"]["HQ"]["dnds"]
    # clean genes (HQ excludes the frame-shifted T7): protein guidance changes nothing
    assert "HQ" not in [x for x in recs if x["meta"]["tid"] == "T7"][0]["meta"]["sets"]
    assert res["diag"]["set_sizes"]["HQ"] >= 36, res["diag"]["set_sizes"]
    assert 0.12 < uh < 0.40, uh
    assert abs(A["P"]["HQ"]["dnds"] - uh) < 1e-9 and abs(A["PF1"]["HQ"]["dnds"] - uh) < 0.03, (uh, A["PF1"]["HQ"])
    # one misregistered gene inflates the unguided pooled value; divergence trimming removes most of it
    assert u > uh + 0.05 and pf1 < u - 0.05, (u, uh, pf1)
    assert res["excluded"]["PF1"]["ALL"]["nonsyn_frac"] > A["U0"]["HQ"]["nonsyn_frac"]
    assert nu["nonsyn_frac"] > 0.6, nu["nonsyn_frac"]
    assert A["NR0.05"]["ALL"]["dnds"] > u + 0.2
    assert abs(A["UT"]["ALL"]["dnds"] - u) < 1e-9  # no indels in the synthetic MAF rows: UT == U0
    assert res["diag"]["agree_P_U0"] > 0.98, res["diag"]["agree_P_U0"]
    # AMENDED on the same synthetic data: no gapped rows here, so PA equals P; the misregistered gene T7 is dS-noisy
    assert abs(A["PA"]["ALL"]["dnds"] - A["P"]["ALL"]["dnds"]) < 1e-9
    assert "NONDSC" in [x for x in recs if x["meta"]["tid"] == "T7"][0]["meta"]["sets"]
    assert A["UD"]["ALL"]["dnds"] < u - 0.05 and res["excluded"]["PAF1"]["ALL"]["pS_ratio_vs_clean"] > XRATIO_MAX
    assert res["amended"]["band"] == "NOISE" and res["amended"]["Ud"] < 0.40 < u, res["amended"]
    assert res["noise_through_protein"]["NM1.0"]["PAF1"] < res["noise_through_protein"]["NM1.0"]["raw"]
    report(res)
    selftest_amended()
    print("selftest ok", d)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "selftest":
        selftest()
    elif a and a[0] == "run" and len(a) in (5, 6, 7, 9):
        run(*a[1:])
    elif a and a[0] == "transfer" and len(a) in (2, 3, 4, 5):
        transfer(*a[1:])
    elif len(a) == 2 and a[0] == "report":
        report(json.load(open(a[1])))
    elif len(a) == 2 and a[0] == "transfer-report":
        transfer_report(json.load(open(a[1]))["rows"])
    elif a and a[0] == "transfer-excl" and len(a) in (2, 3, 4, 5, 6):   # POST HOC (fix pass, 2026-10-13)
        transfer_excl(*a[1:])
    else:
        print(__doc__)
