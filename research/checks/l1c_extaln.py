"""L1c-b: Day's "protein-guided alignment gaps out divergent codons" (Q180-Q182, Q186) and the audit's own Reading d
("the genome alignment is itself the conservation-dependent filter"), retested with an EXTERNAL aligner (PRANK) on an
INDEPENDENT chimp CDS annotation (NCBI RefSeq RS_2026_05), hard cases first. Follow-up (b) of R4-L1c.
PRE-REGISTERED: committed before any run on real codons. Before this commit only the synthetic `selftest` (PRANK on
simulated gene pairs, no real sequence) and the `pairing` count (gene symbols and CDS lengths only; no alignment, no
dN/dS) were run, on the workstation. No dN/dS has been computed on real data by this script.

BRIEF research/checks/briefs/L1c-b-analyst.md (817d049). Task EVO-21 (design); the run is EVO-22.

TIER. Low-stakes by the brief: one combined review, REVIEW-R4-L1c-b-combined.md. DN6, DN1 and DN3 are not marked
  `load_bearing: true` in docs/research/hierarchy.yaml. ESCALATION CLAUSE (from the brief, fixed now): if the result
  would move DN6 past `contested` in EITHER direction (the field is set by reading b2; rule B2 below can return
  `supported` or `contradicted`), or would change a verdict or defeater on A2e or A3, the check becomes load-bearing
  and takes three reviews (correctness, steelman-day, steelman-critic). The script prints `ESCALATION: fires` or
  `ESCALATION: does not fire` from rule B2's value; the A2e / A3 half is for the write-up to judge. No move is applied
  by this script or its write-up.

TARGETS (verbatim; docs/research/sources/quotes-day.md; voxday.net "The Method is the Conclusion", 2026-10-12
  14:12:35 UTC; RH tag dialectic for each, as filed)
  Q180 (¶3): "discovered that the protein-guided CDS alignment method has a circular reasoning problem that's
       impossible to ignore once you recognize it:"
  Q181 (¶7): "Regions too divergent to score well get gapped out or are left unaligned, so they aren't counted."
  Q182 (¶10): "Those excluded codons are enriched for nonsynonymous substitutions by definition, because that's why
       they scored poorly in the protein alignment."
  Q186 (¶15): "The difference is not a matter of gene selection, quality filtering, or computational error. It is a
       methodological artifact of using a conservation-dependent alignment to measure conservation."
  Q273 (¶11, first sentence): "The whole-genome alignment we utilize doesn’t have this scoring bias."
  Q274 (¶14): "So what the Consortium’s method actually measured is: “among the coding positions conserved enough to
       survive protein alignment, how conserved are they?” That’s not a valid measurement, that’s a tautological
       quantification."
  Q184 (¶17-21), row "A: All GENCODE20,4000.798973.9%" and row "Published (Consortium 2005)13,4540.2300~40%".
  Not tested here: Q183 (no registered rule; a lead decision, brief), Q185, Q187-Q192.

WHAT L1c LEFT OPEN (R4-L1c.md, "The codons no arm sees" and "Which clustering regime"; integrated 2026-10-13)
  (1) Every L1c protein arm re-paired codons Cactus had already paired, with the audit's own in-script aligner; on
  85.7% of genes PA = U0 was near automatic. (2) 1.40% of annotated sense codons (156,633) are outside every arm;
  351 genes with >= 20% of their codons not compared hold 61% of the in-gene total. Reading d was "not tested".
  (3) In the 2,765 genes with an indel run, an insertion, a coverage hole or a gapped codon the realistic arms read
  4.8% to 10.5% lower and "the check cannot say whether that is error removed or signal removed". (4) DN6 external is
  `contested` on reading b2, with the condition: "not to be strengthened beyond `contested` until one external
  codon-aware pipeline has been run from an independent chimp CDS annotation, at least on the 2,765 genes".

INPUTS AND WHY THE CHIMP SOURCE IS INDEPENDENT
  Human CDS: the same strings as L1b/L1c's U0 (T2T-CHM13 hs1, GENCODE v35 CAT/Liftoff chosen transcripts, from L1b's
    segment dump on na-workhorse, sources/raw/l1b-seg-2026-10-13/seg.json.gz, sha256 86b0e672...; annotation
    sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz). Using the same human string makes
    every comparison codon-by-codon in human CDS coordinates.
  Chimp CDS: NCBI RefSeq annotation GCF_028858775.2-RS_2026_05 of NHGRI_mPanTro3-v2.1_pri (GCF_028858775.2).
    url  https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/028/858/775/GCF_028858775.2_NHGRI_mPanTro3-v2.1_pri/
         GCF_028858775.2_NHGRI_mPanTro3-v2.1_pri_cds_from_genomic.fna.gz
    fetched 2026-10-14 00:28 UTC into sources/raw/ncbi-ptro-cds-2026-10-14/ (workstation); 109,244 CDS records;
    sha256 9b52cc8ba46a39121960b33f29c036c5bb35a1b533c0cd9d462549d8a5d06402, md5 c2fc58d5b8656223671a45a1c9c4df78
    (= NCBI's md5checksums.txt line, fetched the same minute into sources/raw/ncbi-ptro-meta-2026-10-14/).
    README_GCF_028858775.2-RS_2026_05 (sha256 b6b10859...), verbatim: "ANNOTATION PIPELINE:	NCBI Eukaryotic Genome
    Annotation Pipeline (EGAP)"; "ANNOTATION SOFTWARE VERSION:	10.5"; "ANNOTATION METHOD:	Best-placed RefSeq; Gnomon;
    cmsearch; tRNAscan-SE"; "ANNOTATION EVIDENCE FREEZE DATE:	20-May-2026"; "ANNOTATION RELEASE DATE:	22-May-2026".
    Assembly report (sha256 ffaf7d6b...): "# Assembly method: Verkko v. 1.4", "# Date:           2024-01-08",
    "# GenBank assembly accession: GCA_028858775.3", "# RefSeq assembly and GenBank assemblies identical: no".
  Independent of the CSAC 2005 pipeline on all three steps that produced its 13,454-gene 0.23 (held text, R4-L1c.md
    top: transcripts "indirectly aligned to the chimpanzee sequence via the genome alignment"; "BLASTZ154 was used to
    align non-repetitive chimpanzee" sequence; "only best reciprocal alignments were retained"):
    (i) assembly: T2T mPanTro3 v2.1 (Verkko, 2024), not the 2005 draft; (ii) chimp gene models: built on the chimp
    assembly by NCBI's EGAP, not human transcripts projected through a BLASTZ human-chimp genome alignment;
    (iii) codon pairing: PRANK aligns the two CDS directly; no genome alignment (BLASTZ or Cactus) enters any X arm.
    Also independent of the audit's U0: U0 comes from the Cactus 2023v2 hs1 MAF built on GCA_028858775.2, an earlier
    version of the same assembly; none of RS_2026_05's CDS strings pass through Cactus.
  NOT independent of homology evidence in general, stated now so that no one has to discover it: EGAP's
    "Best-placed RefSeq" and Gnomon models are built with transcript and protein alignment evidence (from general
    knowledge of EGAP, NOT verified from a fetched EGAP method text in this task; to be checked at the next refresh),
    and RefSeq corrects some models: the CDS file has 596 records tagged "[exception=unclassified translation
    discrepancy]" (header counts, 2026-10-14). That is a conservation-aware step at the GENE-MODEL level, which is
    Day's kind of concern; it is carried by the sensitivity set noTD (genes whose chosen chimp CDS carries that tag
    removed), printed beside every ALLx value. Pairing by gene symbol relies on NCBI's orthology-based naming; that
    selects genes, not codons (DN3's domain), and is reported as the pairing rate per set.

ALIGNER (external, version pinned; rule 4: untrusted, own prefix, never inside the repo)
  PRANK v.170427 (A. Loytynoja), Ubuntu noble/universe package prank 0.0.170427+dfsg-3 amd64, fetched with
  `apt-get download prank` 2026-10-14 00:27 UTC into sources/raw/prank-deb-2026-10-14/;
  .deb sha256 b3f17c834fcaa40f734aa3a9db3ea518c33ce29fdfaa12d4da9247f9c11d213d = the SHA256 field of the signed
  archive index (`apt-cache show prank`, same day). Extracted with `dpkg -x` (no root, no maintainer scripts) into
  /home/na/opt/prank-0.0.170427+dfsg-3; binary usr/bin/prank sha256 63ecfb8798203e211cc95d4d0b0c5166adc26c62fb2fe1cdacff68fdf3006b6c
  (checked by the script before any alignment). `prank -help` prints "prank v.170427". Depends only on libc6,
  libgcc-s1, libstdc++6. Never run with -version (its help line: "-version [check for updates]": a network call).
  Options, the same for every arm, meanings verbatim from `prank -help`:
    -once "[run only once; same as -iterate=1]"; -noanchors "[no Exonerate anchoring]"; -nomafft "[no MAFFT guide
    tree]" (neither tool is installed; the flags make it explicit); +F "[force insertions to be always skipped]";
    -seed=20261014 "[set random number seed]"; -quiet. Arm flags: XD -DNA "[no autodetection: use dna or protein
    model]"; XC -codon "[for coding DNA: use empirical codon model]"; XT -translate "[translate to protein]"
    (aligns the translations; the back-translated DNA alignment is read from <out>.best.nuc.fas).
  Why PRANK and not MACSE: MACSE has no package in the signed Ubuntu archive (apt-cache has no candidate), so it would
  be an unsigned jar from a web page; and one PRANK binary gives three alignment models on the SAME input pair, which
  isolates the protein / codon step from the CDS source. Cost of the choice, for Day's side: PRANK's codon and
  translate modes are not frameshift-aware (MACSE is); chimp models with frameshifts reach PRANK already corrected by
  NCBI (the TD tag above) or not at all.

ARMS (per gene; human string h = U0's human CDS; terminal stop codon removed from both sequences before alignment,
  chimp CDS trimmed to a multiple of 3 if needed (flag mod3); a codon is "compared" in an arm iff neither row has a gap
  in it and both codons are sense codons: L1's gene_stats rule, unchanged)
  U0  Cactus pairing, = L1b V0 = L1c U0 (recomputed from the seg dump; must equal the committed L1c gene table, A0).
  XD  PRANK DNA model on (h, chimp RefSeq CDS): nucleotide alignment, no protein or codon knowledge.
  XC  PRANK empirical codon model on the same pair: codon-aware.
  XT  PRANK -translate on the same pair: protein-guided, back-translated: "the protein-guided CDS alignment method"
      (Q180) as practised (each species' own CDS, an external aligner, PAL2NAL-style back-translation).
  XDL (descriptive only, H351 genes only, where the longest chimp isoform differs from the chosen one) XD on the
      longest isoform.
  The arm outputs are mapped to human coordinates (chimp insertions relative to h dropped, as in U0). A PRANK run
  that exits non-zero, times out (4 h), writes no output, or whose ungapped rows differ from its inputs is FAILED.
  One exception, found in the selftest: XC and XT write an in-frame internal stop codon as NNN; that substitution
  alone is accepted (neither form is a sense codon, so the codon is uncounted either way).

CHIMP ISOFORM AND GENE PAIRING RULE (sequence-blind: lengths and names only)
  A human gene (L1c gene table, column `name`) is paired iff its name is unique in the table and equals the [gene=]
  symbol of chimp CDS records that all carry ONE GeneID. Among that gene's CDS records the chosen one minimises
  |chimp CDS length - human CDS length| (both without terminal stop); ties to the longer, then to the smaller
  protein_id. No substitution content enters the choice.
  Measured before commit (`pairing`, 2026-10-14; names and lengths only): see PAIRING COUNTS at the end of this
  docstring.

GENE SETS (fixed from the committed L1c gene table research/checks/results/raw/l1c.genes.tsv.gz; labels asserted)
  H351   genes with >= 20% of their sense codons not compared in U0 (sense codons = L/3 - 1; compared = round((U0_S +
         U0_N)/3)); must count 351.
  H2765  genes NOT indel-free, indel-free = fs_runs = 0, inframe_runs = 0, fs = 0, ins = 0, cov = 1, U0_gapfrac = 0
         (R4-L1c correctness rule); must count 2,765. IF = the 16,545 indel-free genes (control).
  CSAC23 from the table's `sets` column (12,724 genes). TD / noTD: chosen chimp CDS with / without the TD tag.
  An `x` suffix means the subset of genes where all of U0, XD, XC, XT ran: ALLx, H351x, H2765x, IFx, CSAC23x, noTDx.
  Processing order: H351, then H2765 minus H351, then the rest, so that a partial run yields the hard cases.

STATISTICS (pooled = ratio of totals; Nei-Gojobori sites, Jukes-Cantor, kappa = 1, as in L1/L1b/L1c; the kappa-5
  line is printed as sensitivity and decides nothing)
  dN/dS(arm, set); nonsynonymous fraction Nd/(Nd+Sd); pS; codons compared; coverage = compared / human sense codons.
  e_A = 1 - dN/dS(A)/dN/dS(XD) for A in {XC, XT}: the relative drop from nucleotide to codon-aware / protein-guided
        alignment of the same CDS pair. Positive = Day's direction. A* = the arm with the larger e_A on ALLx (ties XT):
        the more Day-favourable external arm (rule C).
  E_A = codons compared in XD and not in A (as XD pairs them): nonsynonymous fraction, p-ratio (pN/pS), pS.
        enriched_A(set) iff E_A has >= 50 codons and its nonsynonymous fraction exceeds XD's pooled one on the set.
  G   = codons compared in XD and not in U0 (as XD pairs them): the codons the genome alignment left out and the
        independent CDS alignment recovers. rise = dN/dS(U0 codons + G codons) / dN/dS(U0) - 1.
  class(G): DENSE-REAL if nonsyn fraction >= 0.90 and p-ratio >= 3.0; else MISPAIRED if x > 3 and nonsyn fraction
        <= 0.80 and p-ratio <= 1.5; else ORTHO-NORMAL if x <= 3; else AMBIGUOUS; TOO-FEW if G has < 50 codons.
        x = pS(G)/pS(U0, same set). Windows are R4-L1c's transfer-excl windows (drawn there post hoc on the L1c
        arms); here they are fixed BEFORE G has been seen. Synthetic references from R4-L1c: misregistration 0.75 /
        1.0 / x about 63; dense real runs 0.94-0.99 / 4.8-30; unrelated in-frame pairing NU 0.774 / 1.018.
  Secondary comparator (descriptive): 1 - dN/dS(A)/dN/dS(U0) on the same genes; agreement of chimp codons where both
  U0 and XD compare a codon; LOST = codons in U0 and not in XD.

READINGS, BANDS AND VERDICT VALUES (rule RD; every outcome lands in exactly one row; "e" bins: MAT >= 0.25,
  SMALL 0.10-0.25, TRACE 0.01-0.10, NULL (-0.01, 0.01), REV <= -0.01). Hard-case clauses need adequacy: H351x >= 150
  genes and H2765x >= 1,383 genes; otherwise those clauses are not applied and print n/a. (H2765: half the set. H351:
  first written as 176, half the set; lowered to 150, 80% of the 188 genes that can pair, after the pairing count and
  before any alignment, because at 176 a loss of 13 PRANK runs would have voided the hard-case test that the brief puts
  first. Disclosed as a pre-run change; it helps whichever side the H351 result favours.)
  B1 (reading b1: "protein-guided alignment lowers dN/dS by a material amount; the published 0.23 is this artefact";
     scored on ALLx with A*):   e >= 0.25 -> supported;  0.10 <= e < 0.25 -> contested;  e < 0.10 -> contradicted.
  B2 (reading b2, the DN6 field reading: Q180-Q182 as written, a mechanism and a direction):
     1. e(ALLx) >= 0.10 and enriched(ALLx)                       -> supported
     2. e(ALLx) >= 0.10 and not enriched(ALLx)                   -> contested (direction, mechanism not shown)
     3. 0.01 <= e(ALLx) < 0.10 and enriched(ALLx)                -> contested (direction real, size below flag)
     4. 0.01 <= e(ALLx) < 0.10 and not enriched(ALLx)            -> contradicted
     5. e(ALLx) < 0.01 and some A in {XC, XT} has e_A(H2765x) >= 0.01 and enriched_A(H2765x)
                                                                 -> contested (direction only in the hard cases)
     6. otherwise (e(ALLx) < 0.01)                               -> contradicted
  D (reading d: "the genome alignment that feeds U0 is itself the conservation-dependent step"; OK = ORTHO-NORMAL or
     DENSE-REAL):
     1. rise(ALLx) >= 0.10 and class(G, ALLx) in OK              -> supported
     2. rise(ALLx) >= 0.10 and AMBIGUOUS                         -> contested
     3. rise(ALLx) >= 0.10 and MISPAIRED                         -> contradicted (recovered codons read like unrelated
                                                                    pairing: error, not hidden signal)
     4. 0.01 <= rise(ALLx) < 0.10 and class in OK or AMBIGUOUS   -> contested
     5. 0.01 <= rise(ALLx) < 0.10 and MISPAIRED or TOO-FEW       -> contradicted
     6. rise(ALLx) < 0.01 and rise(H2765x) >= 0.10 and class(G, H2765x) in OK
                                                                 -> contested (hard cases only)
     7. otherwise (rise(ALLx) < 0.01)                            -> contradicted
  Completeness: ALLx rows are scored only if >= 98% of paired genes completed all four arms; otherwise every ALLx-based
  value prints `pending (incomplete)` and only the hard-case predictions are scored.
  Reachability, each side, each reading (ST-05 / MA-24):
   B1 supported: XT or XC reads >= 25% below XD on all paired genes, e.g. if PRANK's protein/codon models gap divergent
      stretches that its DNA model pairs. Contradicted: the three PRANK models agree within 10% (L1c's realistic arms:
      2.3% to 5.8%). The selftest shows XT and XC can read below XD on a pair with a dense replacement run.
   B2 supported: as B1 at >= 10% with enriched E_A. Contested: a drop of 1-10% (L1c's value class). Contradicted: no
      drop >= 1% on ALLx and none in the hard cases, or a 1-10% drop not carried by nonsyn-enriched exclusions. All
      three are reachable: the selftest's dense-run pair gives a positive e, its clean pair gives e = 0 exactly.
   D supported: G adds codons at ordinary synonymous divergence that lift the pooled value >= 10% (for U0 ALL that
      needs the 1.40% left-out codons at pN about 0.05 or more: R4-L1c's own bound "a rise of the order of 10% is
      open"). Contradicted: G is small (< 1% rise) or reads like unrelated pairing. Both reachable.

PREDICTIONS (fixed now; pooled JC dN/dS, kappa = 1; each can fail)
  Day side (from Q180-Q182, Q186, Q273, Q274, Q184):
   D1  XD on ALLx >= 0.65. Q273's ground ("doesn't have this scoring bias") and its paragraph ("we get ALL the aligned
       coding positions, not just the ones that are deemed to look conserved at the protein level") apply to any
       alignment with no protein-level scoring, and XD has none. Reachable if the U0 value was a Cactus artefact.
   D2  XT on ALLx <= 0.40 and B1 = supported (e >= 0.25): the protein-guided arm reads low and materially below XD.
   D3  E_XT nonsynonymous fraction on ALLx > XD's pooled fraction (Q182, "enriched ... by definition").
   D4  D = supported (Reading d, the Day review's extended reading of Q181/Q186; not his text, which exempts the
       whole-genome alignment in Q273).
   D5  Hard cases: some A in {XC, XT} has e_A(H2765x) >= 0.10 with enriched_A(H2765x).
   D6  Hard cases: rise(H351x) >= 0.25 with class(G, H351x) in OK.
  Critic side (the published low value is not an alignment artefact; L1b/L1c's numbers):
   C1  XD on ALLx in 0.20-0.35.
   C2  |e_XC| < 0.10 and |e_XT| < 0.10 on ALLx.
   C3  rise(ALLx) < 0.10.
   C4  class(G, H351x) is MISPAIRED or AMBIGUOUS (what Cactus left out in the worst-covered genes is not ordinary
       orthologous protein).
   C5  Hard cases: e_XC(H2765x) < 0.10 and e_XT(H2765x) < 0.10.
   C6  XD on CSAC23x in 0.18-0.30.
  Audit:
   A0  U0 recomputed from the seg dump equals the L1c gene table's U0_S, U0_N, U0_Sd, U0_Nd on every gene, within the
       table's 4-significant-digit rounding. (Sanity; a failure stops scoring.)
   A1  >= 98% of paired genes complete all four arms (no FAILED arm).
   A2  Where U0 and XD both compare a codon, the chimp codons agree on >= 99.0% of codons (ALLx).
   A3  On IFx, XD within +-3% of U0.
   A4  e_XT and e_XC on ALLx each in [-0.02, 0.06].
   A5  rise(ALLx) in [0.00, 0.10]; G holds >= 50% of the codons U0 leaves out in the ALLx genes.
   A6  XD on ALLx in 0.24-0.32; XT on ALLx in 0.23-0.32.
   A7  coverage(XD) > coverage(U0) on H351x.
   A8  B2 = contested.
  Scoring: hit / miss for each, printed by the script from the registered thresholds (function `score_predictions`);
  a prediction whose inputs are pending or underpowered prints n/a. Hits and misses carry equal weight.

WHAT MOVES WHICH VERDICT (proposals for integration; nothing is applied here; integration and the owner decide)
  DN6 external (field reading b2, R4-L1c Readings table): B2's value. supported or contradicted fires the escalation
    clause (three reviews before integration). contested leaves the field as it is and LIFTS L1c's condition (the
    external pipeline from an independent CDS has been run on the 2,765 genes) with the new numbers in the comment.
  DN6 reading b1 and reading d: B1 and D values go into the Readings table; neither sets a field under R4-L1c's RD
    ruling (b1 less defensible than b2; d an extended reading), unless integration re-rules.
  DN1 / DN3: not moved (L1b's bands govern the Cactus codons); XD on ALLx and CSAC23x are added as numbers.
  DN6 fidelity: not touched (it rests on the held CSAC text).

RESOURCES (measured on the workstation, synthetic pairs, PRANK v.170427; one process at a time)
  Per pair, wall: 1,000 codons XD 5.2 s / XC 1.7 s / XT 0.6 s; 3,000 codons 46.7 / 14.1 / 5.0 s; RSS 8-15 MB.
  Time grows about as length squared. Over the 19,310 L1c genes (L from the gene table) that projects to about 20
  CPU-hours for XD, 6 for XC, 2 for XT: about 3-4 h wall on 10 workers, plus the longest genes as stragglers
  (L = 107,976 bp: about 1.9 h for XD alone at workstation speed). RAM: workers < 300 MB each, main < 1 GB.
  The host smoke (below) measures this on na-workhorse before the main run; the estimate is not trusted until then.

HOST SMOKE (run by the launch task, EVO-22, BEFORE the main run; real entry point, real Pool, real worker count)
  `smoke` mode runs the full pipeline on 24 paired genes (two per length decile below the 99th percentile, plus four
  from H351) and prints only diagnostics: per-arm success, seconds, A0 on those genes, a length-squared time fit and
  the projected CPU-hours. It writes no statistics and prints no dN/dS. A launch bug found there is fixed in a separate
  commit labelled "post hoc (pre-run, no data seen)".

LAUNCH (EVO-22; not before the `ph2` collect task frees na-workhorse; `uptime` first; <= 11 busy processes in total,
  RAM < ~12 GB; never commit or push from the host)
  0. On the host: fetch the two untrusted inputs into new directories and verify hashes:
     mkdir sources/raw/prank-deb-$(date +%F) && cd $_ && apt-get download prank && sha256sum *.deb   # b3f17c83...
     mkdir -p /home/na/opt/prank-0.0.170427+dfsg-3 && dpkg -x <deb> /home/na/opt/prank-0.0.170427+dfsg-3
     mkdir sources/raw/ncbi-ptro-cds-$(date +%F) && curl -sS -o <dir>/<file> <url above> && md5sum <file>  # c2fc58d5...
  1. rsync research/checks/l1c_extaln.py and research/checks/results/raw/l1c.genes.tsv.gz to the host.
  2. Smoke:
     ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && /usr/bin/time -v research/.venv/bin/python -I
       research/checks/l1c_extaln.py smoke sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz
       sources/raw/l1b-seg-2026-10-13/seg.json.gz sources/raw/ncbi-ptro-cds-<date>/<file>
       research/checks/results/raw/l1c.genes.tsv.gz research/checks/results/raw/l1c_extaln_smoke 10
       > research/checks/results/raw/l1c_extaln_smoke.out 2>&1 < /dev/null'
  3. Main run (same arguments, mode `run`, prefix research/checks/results/raw/l1c_extaln, workers 10):
     ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && setsid -f nohup /usr/bin/time -v
       research/.venv/bin/python -I research/checks/l1c_extaln.py run <gff> <seg> <cds> <genes.tsv.gz>
       research/checks/results/raw/l1c_extaln 10 > research/checks/results/raw/l1c_extaln.out 2>&1 < /dev/null'
     Record hostname, date, md5 of this script, sha256 of every input and of the PRANK binary in raw/l1c_extaln.host.
  4. `report` mode recomputes every table, band and score from raw/l1c_extaln.genes.jsonl.gz alone (also after a
     partial run).
COLLECT: rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/l1c_extaln*' research/checks/results/raw/
  Outputs: l1c_extaln.out, l1c_extaln.json, l1c_extaln.genes.jsonl.gz (per-gene counts only; no sequence).

BLINDNESS. No alignment of a real human-chimp pair has been made by this script or by any agent for this check. Known
  before registration, and therefore not blind: every L1b and L1c number (U0 0.271 on ALL, 0.219 on CSAC23; the
  realistic arms' 2.3-5.8%; the left-out-codon table; the 351 / 2,765 split); the PAIRING COUNTS below (names and CDS
  lengths only); the selftest's synthetic results (below). The bands, the class windows and the predictions were
  written before the selftest was run, except where SELFTEST notes otherwise.

NOT IN SCOPE (owner approval required; brief): Day's per-gene table, his excluded-codon count, the CSAC SI criteria, a
  registered rule for Q183. Also not here (brief, "if time allows"): the PAF1-PAF2 threshold dose-response and the
  replacement density against Poisson; each needs its own registration.

PAIRING COUNTS (`pairing` mode, workstation, 2026-10-14, 3.0 s, 229 MB; gene table sha256 b92930dd..., CDS sha256
  9b52cc8b...; names and lengths only, no alignment, no dN/dS)
  109,244 chimp CDS records, 596 with the TD tag. Paired 17,699 of 19,310 genes (91.7%); unpaired: no chimp record with
  the human symbol 1,599, human name not unique 12. Chosen chimp CDS with the TD tag: 152. By set: H351 188 / 351
  (53.6%); H2765 2,208 / 2,765 (79.9%); CSAC23 12,306 / 12,724 (96.7%). Longest isoform differs from the chosen one in
  49 paired H351 genes (the XDL arm). Chosen chimp CDS whose length is not a multiple of 3: 2 (none TD-tagged; 10 of
  all 109,244 records).
  What the 163 unpaired H351 genes are (names): mostly multi-copy families whose chimp copies carry only LOC symbols
  (no 1:1 call by NCBI): GOLGA6L / GOLGA8, NBPF, NPIP, HLA, KIR, DAZ, BPY2, HSFY, KRTAP, FAM90A, ANKRD20A/36, CCL3L3,
  and others; 6 clone-named and 7 LINC / orf genes. A fallback pairing would pair paralogues, so none is used.
  Consequence, both sides: the hard-case test reaches about half of the 351; the half it cannot reach is the
  paralogue-rich half, where neither an independent 1:1 CDS nor a clean answer exists. The script prints U0 on each
  whole set beside U0 on the genes it reached (REACH line), from the L1c gene table, so the selection is visible.

SELFTEST (synthetic, workstation, 2026-10-14; 12 simulated pairs of 400 codons, 1 worker, 17.2 s wall, 38 MB peak RSS;
  run after the bands and predictions above were written; it changed none of them; the integrity rule for internal
  stops and the H351 floor were changed after it, as stated in their places)
  - Rules B1, B2, D: one value for every input on a grid (asserted). Class windows return MISPAIRED for NU-like
    (0.774, 1.018, pS 0.75), DENSE-REAL for a synthetic dense run, ORTHO-NORMAL for ordinary divergence (asserted).
  - Clean pairs (1.2% substitutions, no indels): XD = XC = XT = truth exactly, e = 0 (asserted). In-frame 3-codon
    deletion: every arm compares 397 of 400 codons (asserted). Internal stop: all three arms run, 399 compared
    (asserted, after the NNN rule). All three modes return identical output on repeat (asserted).
  - Dense 15-codon replacement run (two differences per codon): ALL THREE PRANK models leave part of the run out; XD
    compares 393 and 389 of 400 codons, XC 385 / 386, XT 390 / 386; on the 12-pair pool e_XC 0.22, e_XT 0.26. So
    (i) positive e is reachable (B1 / B2 can reach `supported`); (ii) XD is not a neutral reference: a nucleotide
    aligner also gaps a dense run, so e measures what the codon / protein step adds BEYOND nucleotide alignment, and
    D's G can only recover codons that a nucleotide CDS alignment pairs (D is a lower bound on what Cactus left out
    that is recoverable). Both points cut toward Day; they are limits, recorded before the run.
  - Uncorrected 1-bp frameshift in the chimp CDS (mod3): XC coverage 0.38 on that pair; XT reads it in a shifted frame.
    Real RefSeq CDS reach PRANK frame-corrected where NCBI corrected them (TD), so noTDx is printed beside ALLx.
  - The analysis, scoring and report path runs end to end on the synthetic records (21 predictions printed).
"""
import gzip
import hashlib
import importlib.util
import json
import math
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from multiprocessing import Pool

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("l1c", os.path.join(HERE, "l1c_alignment_method.py"))
L1C = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L1C)
L1B = L1C.L1B
L1 = L1C.L1

PRANK = "/home/na/opt/prank-0.0.170427+dfsg-3/usr/bin/prank"
PRANK_SHA256 = "63ecfb8798203e211cc95d4d0b0c5166adc26c62fb2fe1cdacff68fdf3006b6c"
CDS_SHA256 = "9b52cc8ba46a39121960b33f29c036c5bb35a1b533c0cd9d462549d8a5d06402"
PRANK_COMMON = ["-once", "-noanchors", "-nomafft", "+F", "-quiet", "-seed=20261014"]
PRANK_MODE = {"XD": ["-DNA"], "XC": ["-codon"], "XT": ["-translate"]}
PRANK_TIMEOUT = 4 * 3600
XARMS = ["XD", "XC", "XT"]
ARMS = ["U0"] + XARMS
STOPS = {"TAA", "TAG", "TGA"}

N_H351, N_H2765, N_ALL, N_CSAC23 = 351, 2765, 19310, 12724
ADEQ = {"H351x": 150, "H2765x": 1383}    # see PAIRING COUNTS: H351 floor set after the pairing count, before any alignment
COMPLETE_MIN = 0.98
MINCOD = 50
EBINS = [(0.25, "MAT"), (0.10, "SMALL"), (0.01, "TRACE")]
SETNAMES = ["ALLx", "H351x", "H2765x", "IFx", "CSAC23x", "noTDx", "TDx"]
GENE_COLS = ["tid", "gene", "name", "L", "cov", "fs", "ins", "fs_runs", "inframe_runs", "sets",
             "U0_S", "U0_N", "U0_Sd", "U0_Nd", "U0_gapfrac"]


# ---------------------------------------------------------------- inputs
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def load_gene_table(path):
    """L1c gene table -> dict tid -> row; the hard-case sets with asserted counts."""
    import csv
    rows = list(csv.DictReader(gzip.open(path, "rt"), delimiter="\t"))
    miss = [c for c in GENE_COLS if c not in rows[0]]
    assert not miss, f"gene table lacks columns {miss}"
    assert len(rows) == N_ALL, f"gene table has {len(rows)} genes, expected {N_ALL}"
    gt, h351, h2765, csac = {}, set(), set(), set()
    for r in rows:
        L = int(r["L"])
        sense = L // 3 - 1
        comp = round((float(r["U0_S"]) + float(r["U0_N"])) / 3.0)
        if sense > 0 and (sense - comp) / sense >= 0.20:
            h351.add(r["tid"])
        indel_free = (int(r["fs_runs"]) == 0 and int(r["inframe_runs"]) == 0 and int(r["fs"]) == 0
                      and int(r["ins"]) == 0 and float(r["cov"]) == 1.0 and float(r["U0_gapfrac"]) == 0.0)
        if not indel_free:
            h2765.add(r["tid"])
        st = r["sets"].split(",")
        assert "ALL" in st, f"set label ALL missing for {r['tid']}"
        if "CSAC23" in st:
            csac.add(r["tid"])
        gt[r["tid"]] = r
    assert len(h351) == N_H351, f"H351 counts {len(h351)}"
    assert len(h2765) == N_H2765, f"H2765 counts {len(h2765)}"
    assert len(csac) == N_CSAC23, f"CSAC23 counts {len(csac)}"
    return gt, h351, h2765, csac


def parse_cds_headers(path):
    """One pass: per record (symbol, GeneID, protein_id, length, td flag, pseudo flag). No sequence kept."""
    recs = []
    cur = None
    n = 0
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(">"):
                if cur is not None:
                    cur["len"] = n
                    recs.append(cur)
                g = re.search(r"\[gene=([^\]]+)\]", line)
                gid = re.search(r"\[db_xref=[^\]]*GeneID:(\d+)", line)
                pid = re.search(r"\[protein_id=([^\]]+)\]", line)
                cur = dict(sym=g.group(1) if g else None, gid=gid.group(1) if gid else None,
                           pid=pid.group(1) if pid else line.split()[0][1:],
                           td=int("unclassified translation discrepancy" in line),
                           pseudo=int("[pseudo=true]" in line), hdr_id=line.split()[0][1:])
                n = 0
            else:
                n += len(line.strip())
        if cur is not None:
            cur["len"] = n
            recs.append(cur)
    return recs


def _len_nostop(n):
    return n - 3 if n >= 3 else n     # chimp terminal stop is checked on the sequence later; lengths for the rule only


def choose_pairs(gt, recs):
    """Sequence-blind pairing: unique human name == chimp symbol with one GeneID; isoform by closest CDS length."""
    names = {}
    for tid, r in gt.items():
        names.setdefault(r["name"], []).append(tid)
    bysym = {}
    for x in recs:
        if x["sym"] and not x["pseudo"]:
            bysym.setdefault(x["sym"], []).append(x)
    pairs, why = {}, {}
    for tid, r in gt.items():
        nm = r["name"]
        if len(names[nm]) != 1:
            why[tid] = "human-name-not-unique"
            continue
        cand = bysym.get(nm)
        if not cand:
            why[tid] = "no-chimp-symbol"
            continue
        if len({x["gid"] for x in cand}) != 1:
            why[tid] = "symbol-on-several-GeneIDs"
            continue
        hl = int(r["L"]) - 3
        best = min(cand, key=lambda x: (abs(_len_nostop(x["len"]) - hl), -x["len"], x["pid"]))
        longest = min(cand, key=lambda x: (-x["len"], x["pid"]))
        pairs[tid] = dict(pid=best["pid"], hdr_id=best["hdr_id"], clen=best["len"], td=best["td"],
                          niso=len(cand), longest=longest["hdr_id"] if longest["hdr_id"] != best["hdr_id"] else None)
        why[tid] = "paired"
    return pairs, why


def load_cds_seqs(path, want):
    out = {}
    cur = None
    buf = []
    with gzip.open(path, "rt") as fh:
        for line in fh:
            if line.startswith(">"):
                if cur is not None:
                    out[cur] = "".join(buf).upper()
                hid = line.split()[0][1:]
                cur = hid if hid in want else None
                buf = []
            elif cur is not None:
                buf.append(line.strip())
        if cur is not None:
            out[cur] = "".join(buf).upper()
    return out


# ---------------------------------------------------------------- alignment
def check_prank(path=PRANK):
    assert os.path.exists(path), f"PRANK not found at {path}"
    got = sha256_file(path)
    assert got == PRANK_SHA256, f"PRANK sha256 {got} != pinned {PRANK_SHA256}"
    return got


def read_fasta(path):
    d, cur = {}, None
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if line.startswith(">"):
                cur = line[1:].split()[0]
                d[cur] = []
            elif cur is not None:
                d[cur].append(line)
    return {k: "".join(v).upper() for k, v in d.items()}


def stops_to_n(s):
    """PRANK's codon and translate modes write an in-frame internal stop codon as NNN (selftest). Neither is a
    sense codon, so the codon is uncounted either way; any other change of a row is still FAILED."""
    s = s.upper()
    return "".join("NNN" if s[i:i + 3] in STOPS else s[i:i + 3] for i in range(0, len(s), 3))


def prank_pair(mode, h, c, prank=PRANK, timeout=PRANK_TIMEOUT):
    """Align (h, c) with PRANK in one mode. Returns (ha, ca, seconds, status)."""
    wd = tempfile.mkdtemp(prefix="l1cx-")
    t0 = time.time()
    try:
        fa = os.path.join(wd, "in.fa")
        with open(fa, "w") as fh:
            fh.write(f">h\n{h}\n>c\n{c}\n")
        out = os.path.join(wd, "out")
        cmd = [prank, f"-d={fa}", f"-o={out}"] + PRANK_COMMON + PRANK_MODE[mode]
        try:
            p = subprocess.run(cmd, cwd=wd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, timeout=timeout)
        except subprocess.TimeoutExpired:
            return None, None, time.time() - t0, "timeout"
        if p.returncode != 0:
            return None, None, time.time() - t0, f"exit{p.returncode}"
        fn = out + (".best.nuc.fas" if mode == "XT" else ".best.fas")
        if not os.path.exists(fn):
            return None, None, time.time() - t0, "no-output"
        al = read_fasta(fn)
        if set(al) != {"h", "c"} or len(al["h"]) != len(al["c"]):
            return None, None, time.time() - t0, "bad-output"
        exp = (h.upper(), c.upper()) if mode == "XD" else (stops_to_n(h), stops_to_n(c))
        if al["h"].replace("-", "") != exp[0] or al["c"].replace("-", "") != exp[1]:
            return None, None, time.time() - t0, "rows-changed"
        return al["h"], al["c"], time.time() - t0, "ok"
    finally:
        shutil.rmtree(wd, ignore_errors=True)


def to_human(ha, ca, L):
    """Map an alignment of (h without stop, c) to a chimp string of length L in human coordinates."""
    out = [y for x, y in zip(ha, ca) if x != "-"]
    return ("".join(out) + "-" * L)[:L]


def prep_pair(h, c):
    """Strip terminal stops; trim chimp to a multiple of 3. Returns (h_in, c_in, flags)."""
    fl = {}
    hn = h[:-3] if len(h) >= 3 and h[-3:].upper() in STOPS else h
    cn = c[:-3] if len(c) >= 3 and c[-3:].upper() in STOPS else c
    fl["c_stop_term"] = int(len(cn) != len(c))
    if len(cn) % 3:
        cn = cn[:len(cn) - len(cn) % 3]
        fl["mod3"] = 1
    else:
        fl["mod3"] = 0
    fl["c_stop_int"] = sum(1 for i in range(0, len(cn) - 2, 3) if cn[i:i + 3] in STOPS)
    fl["h_stop_int"] = sum(1 for i in range(0, len(hn) - 2, 3) if hn[i:i + 3].upper() in STOPS)
    return hn, cn, fl


def compared(h, c):
    n = len(h) // 3
    out = []
    for i in range(n):
        a, b = h[3 * i:3 * i + 3].upper(), c[3 * i:3 * i + 3].upper()
        out.append("-" not in a and "-" not in b and a in L1.SITES and b in L1.SITES)
    return out


def masked(c, keep):
    s = list("-" * len(c))
    for i, k in enumerate(keep):
        if k:
            s[3 * i:3 * i + 3] = c[3 * i:3 * i + 3]
    return "".join(s)


def derived(h, strs):
    """Codon-set comparisons for one gene. strs: arm -> chimp string in human coordinates (len(h))."""
    K = {a: compared(h, strs[a]) for a in strs}
    n = len(h) // 3
    out = {}
    if "XD" in K:
        for a in ("XC", "XT"):
            if a in K:
                out[f"E_{a}"] = L1C.stats(h, masked(strs["XD"], [K["XD"][i] and not K[a][i] for i in range(n)]),
                                          extra=False)
                out[f"GA_{a}"] = L1C.stats(h, masked(strs[a], [K[a][i] and not K["XD"][i] for i in range(n)]),
                                           extra=False)
    if "U0" in K:
        for a in XARMS + ["XDL"]:
            if a in K:
                g = [K[a][i] and not K["U0"][i] for i in range(n)]
                out[f"G_{a}"] = L1C.stats(h, masked(strs[a], g), extra=False)
                uni = list(masked(strs["U0"], K["U0"]))
                for i in range(n):
                    if g[i]:
                        uni[3 * i:3 * i + 3] = strs[a][3 * i:3 * i + 3]
                out[f"UNI_{a}"] = L1C.stats(h, "".join(uni), extra=False)
        if "XD" in K:
            out["LOST_XD"] = L1C.stats(h, masked(strs["U0"], [K["U0"][i] and not K["XD"][i] for i in range(n)]),
                                       extra=False)
            both = [i for i in range(n) if K["U0"][i] and K["XD"][i]]
            out["agree"] = dict(both=len(both),
                                same=sum(1 for i in both if strs["U0"][3 * i:3 * i + 3] == strs["XD"][3 * i:3 * i + 3]))
    out["ncomp"] = {a: sum(K[a]) for a in K}
    out["sense"] = sum(1 for i in range(n) if h[3 * i:3 * i + 3].upper() in L1.SITES)
    return out


def align_gene(h, c, L, prank=PRANK, arms=XARMS, c_long=None):
    hn, cn, fl = prep_pair(h, c)
    strs, st = {}, {}
    for a in arms:
        ha, ca, sec, status = prank_pair(a, hn, cn, prank)
        st[a] = dict(status=status, sec=round(sec, 3))
        if status == "ok":
            strs[a] = to_human(ha, ca, L)
    if c_long is not None:
        hl, cl, _ = prep_pair(h, c_long)
        ha, ca, sec, status = prank_pair("XD", hl, cl, prank)
        st["XDL"] = dict(status=status, sec=round(sec, 3))
        if status == "ok":
            strs["XDL"] = to_human(ha, ca, L)
    return strs, st, fl


# ---------------------------------------------------------------- per gene (real data, host only)
def process(task):
    r, human, segs, cseq, clong, meta, prank, smoke = task
    h, chs, diag = L1B.assemble(r, human, segs)
    if diag["cov"] <= 0:
        return dict(meta=meta, skipped="no-U0")
    L = r["L"]
    strs, st, fl = align_gene(h, cseq, L, prank, XARMS, clong)
    strs["U0"] = chs["V0"]
    arms = {a: L1C.stats(h, strs[a]) for a in strs}
    der = derived(h, strs)
    rec = dict(meta=dict(meta, **fl), status=st, ok=int(all(st[a]["status"] == "ok" for a in XARMS)))
    if smoke:
        rec["u0_counts"] = {k: arms["U0"][k] for k in ("S", "N", "Sd", "Nd")}
        return rec
    rec.update(arms=arms, der=der)
    return rec


def gen_tasks(path_seg, txs, order, pairs, seqs, prank, smoke=False, only=None):
    by = {r["tid"]: r for r in txs}
    for group in order:
        with gzip.open(path_seg, "rt") as fh:
            for line in fh:
                d = json.loads(line)
                tid = d["tid"]
                if tid not in group or (only is not None and tid not in only):
                    continue
                r = by.get(tid)
                if r is None or tid not in pairs:
                    continue
                p = pairs[tid]
                meta = dict(tid=tid, name=r["name"], L=r["L"], pid=p["pid"], clen=p["clen"], td=p["td"],
                            niso=p["niso"])
                yield (r, d["human"], d["segs"], seqs[p["hdr_id"]], seqs.get(p["longest"]) if p.get("xdl") else None,
                       meta, prank, smoke)


# ---------------------------------------------------------------- aggregation and scoring
def agg(gs):
    if not gs:
        return dict(dnds=float("nan"))
    return L1C.agg(gs)


def tol4(b):
    b = abs(b)
    return 1e-9 if b == 0 else 0.5 * 10 ** (math.floor(math.log10(b)) - 3) + 1e-9


def a0_check(rec, gt):
    row = gt[rec["meta"]["tid"]]
    u = rec.get("u0_counts") or {k: rec["arms"]["U0"][k] for k in ("S", "N", "Sd", "Nd")}
    bad = [k for k in ("S", "N", "Sd", "Nd") if abs(u[k] - float(row["U0_" + k])) > tol4(float(row["U0_" + k]))]
    return not bad


def ebin(e):
    if e is None or e != e:
        return "n/a"
    for t, nm in EBINS:
        if e >= t:
            return nm
    return "NULL" if e > -0.01 else "REV"


def gclass(ex, ps_ref):
    if ex is None or ex["codons"] < MINCOD:
        return "TOO-FEW"
    nf, pr, ps = ex["nonsyn_frac"], ex["dnds_p"], ex["pS"]
    if nf is not None and pr is not None and nf >= 0.90 and pr >= 3.0:
        return "DENSE-REAL"
    x = (ps / ps_ref) if (ps is not None and ps_ref) else float("inf")
    if x > 3 and nf is not None and pr is not None and nf <= 0.80 and pr <= 1.5:
        return "MISPAIRED"
    if x <= 3:
        return "ORTHO-NORMAL"
    return "AMBIGUOUS"


OK_CLASSES = ("ORTHO-NORMAL", "DENSE-REAL")


def rule_b1(e):
    if e is None or e != e:
        return "pending"
    return "supported" if e >= 0.25 else ("contested" if e >= 0.10 else "contradicted")


def rule_b2(eA, enA, hard):
    """hard: list of (e_A(H2765x), enriched_A(H2765x)) for A in {XC, XT}, or None if underpowered."""
    if eA is None or eA != eA:
        return "pending"
    if eA >= 0.10:
        return "supported" if enA else "contested"
    if eA >= 0.01:
        return "contested" if enA else "contradicted"
    if hard and any((e is not None and e == e and e >= 0.01 and en) for e, en in hard):
        return "contested"
    return "contradicted"


def rule_d(rA, cA, rH, cH):
    if rA is None or rA != rA:
        return "pending"
    if rA >= 0.10:
        return {"AMBIGUOUS": "contested", "MISPAIRED": "contradicted"}.get(cA, "supported" if cA in OK_CLASSES
                                                                          else "contradicted")
    if rA >= 0.01:
        return "contested" if cA in OK_CLASSES + ("AMBIGUOUS",) else "contradicted"
    if rH is not None and rH == rH and rH >= 0.10 and cH in OK_CLASSES:
        return "contested"
    return "contradicted"


def gt_pooled(gt, tids):
    """U0 pooled JC dN/dS from the L1c gene table (4-digit rounding): reach of a set before and after pairing."""
    S = sum(float(gt[t]["U0_S"]) for t in tids)
    N = sum(float(gt[t]["U0_N"]) for t in tids)
    Sd = sum(float(gt[t]["U0_Sd"]) for t in tids)
    Nd = sum(float(gt[t]["U0_Nd"]) for t in tids)
    return (L1.jc(Nd / N) / L1.jc(Sd / S)) if (S and N and Sd) else None


def set_members(recs, gt, h351, h2765, csac):
    ok = [x for x in recs if x.get("ok")]
    s = {"ALLx": ok}
    s["H351x"] = [x for x in ok if x["meta"]["tid"] in h351]
    s["H2765x"] = [x for x in ok if x["meta"]["tid"] in h2765]
    s["IFx"] = [x for x in ok if x["meta"]["tid"] not in h2765]
    s["CSAC23x"] = [x for x in ok if x["meta"]["tid"] in csac]
    s["noTDx"] = [x for x in ok if not x["meta"]["td"]]
    s["TDx"] = [x for x in ok if x["meta"]["td"]]
    return s


def summarise_set(gs):
    out = {"genes": len(gs)}
    for a in ARMS:
        p = agg([g["arms"][a] for g in gs])
        out[a] = {k: p.get(k) for k in ("dnds", "dnds_k5", "nonsyn_frac", "pS", "pN", "Nd", "Sd", "S", "N")}
        out[a]["codons"] = sum(g["der"]["ncomp"][a] for g in gs)
    sense = sum(g["der"]["sense"] for g in gs)
    out["sense"] = sense
    for a in ARMS:
        out[a]["coverage"] = out[a]["codons"] / sense if sense else None
    d = lambda a: out[a]["dnds"]
    for a in ("XC", "XT"):
        out[f"e_{a}"] = (1 - d(a) / d("XD")) if d("XD") and d("XD") == d("XD") else None
        out[f"eU_{a}"] = (1 - d(a) / d("U0")) if d("U0") and d("U0") == d("U0") else None
        ex = L1C.excl_agg([g["der"][f"E_{a}"] for g in gs])
        out[f"E_{a}"] = ex
        nfx = out["XD"]["nonsyn_frac"]
        out[f"enriched_{a}"] = bool(ex["codons"] >= MINCOD and ex["nonsyn_frac"] is not None and nfx is not None
                                    and ex["nonsyn_frac"] > nfx)
        out[f"GA_{a}"] = L1C.excl_agg([g["der"][f"GA_{a}"] for g in gs])
    for a in XARMS:
        out[f"G_{a}"] = L1C.excl_agg([g["der"][f"G_{a}"] for g in gs])
        uni = agg([g["der"][f"UNI_{a}"] for g in gs])
        out[f"rise_{a}"] = (uni["dnds"] / d("U0") - 1) if d("U0") and d("U0") == d("U0") else None
        out[f"class_{a}"] = gclass(out[f"G_{a}"], out["U0"]["pS"])
    out["LOST_XD"] = L1C.excl_agg([g["der"]["LOST_XD"] for g in gs])
    both = sum(g["der"]["agree"]["both"] for g in gs)
    out["agree_XD_U0"] = (sum(g["der"]["agree"]["same"] for g in gs) / both) if both else None
    left = sum(g["der"]["sense"] - g["der"]["ncomp"]["U0"] for g in gs)
    out["U0_left_out"] = left
    out["G_share_of_left_out"] = (out["G_XD"]["codons"] / left) if left else None
    xdl = [g for g in gs if "G_XDL" in g["der"]]
    if xdl:
        out["XDL_genes"] = len(xdl)
        out["G_XDL"] = L1C.excl_agg([g["der"]["G_XDL"] for g in xdl])
        u0 = agg([g["arms"]["U0"] for g in xdl])["dnds"]
        out["rise_XDL"] = agg([g["der"]["UNI_XDL"] for g in xdl])["dnds"] / u0 - 1 if u0 == u0 and u0 else None
        out["rise_XD_same_genes"] = agg([g["der"]["UNI_XD"] for g in xdl])["dnds"] / u0 - 1 if u0 == u0 and u0 else None
    return out


def analyse(recs, gt, h351, h2765, csac, npaired):
    ok = [x for x in recs if x.get("ok")]
    sets = set_members(recs, gt, h351, h2765, csac)
    res = {"paired": npaired, "returned": len(recs), "complete": len(ok),
           "failed": {a: sum(1 for x in recs if "status" in x and x["status"][a]["status"] != "ok") for a in XARMS},
           "skipped": sum(1 for x in recs if x.get("skipped"))}
    res["a0_fail"] = [x["meta"]["tid"] for x in ok if not a0_check(x, gt)]
    res["sets"] = {k: summarise_set(v) for k, v in sets.items() if v}
    if "L" in next(iter(gt.values())):     # the real gene table (the selftest's fake table has no L column)
        full_sets = {"ALLx": set(gt), "H351x": h351, "H2765x": h2765, "IFx": set(gt) - h2765, "CSAC23x": csac}
        res["reach"] = {k: dict(set_genes=len(v), reached=len(sets[k]), U0_full_set=gt_pooled(gt, v),
                                U0_reached=gt_pooled(gt, [x["meta"]["tid"] for x in sets[k]]))
                        for k, v in full_sets.items()}
    full = npaired > 0 and len(ok) / npaired >= COMPLETE_MIN
    res["complete_share"] = len(ok) / npaired if npaired else None
    res["full"] = full
    res["adequate"] = {k: len(sets[k]) >= v for k, v in ADEQ.items()}
    res.update(score(res))
    return res


def _g(res, s, k, sub=None):
    x = res["sets"].get(s)
    if x is None:
        return None
    v = x.get(k)
    if sub is not None and isinstance(v, dict):
        v = v.get(sub)
    return v


def score(res):
    full = res["full"]
    adq = res["adequate"]
    out = {}
    eXT, eXC = _g(res, "ALLx", "e_XT"), _g(res, "ALLx", "e_XC")
    if full and eXT is not None and eXC is not None:
        astar = "XC" if (eXC > eXT) else "XT"
        eA = _g(res, "ALLx", f"e_{astar}")
        enA = _g(res, "ALLx", f"enriched_{astar}")
    else:
        astar, eA, enA = None, None, None
    hard = None
    if adq["H2765x"]:
        hard = [(_g(res, "H2765x", f"e_{a}"), _g(res, "H2765x", f"enriched_{a}")) for a in ("XC", "XT")]
    out["A_star"] = astar
    out["B1"] = rule_b1(eA) if full else "pending (incomplete)"
    out["B2"] = rule_b2(eA, enA, hard) if full else "pending (incomplete)"
    rA, cA = _g(res, "ALLx", "rise_XD"), _g(res, "ALLx", "class_XD")
    rH, cH = (_g(res, "H2765x", "rise_XD"), _g(res, "H2765x", "class_XD")) if adq["H2765x"] else (None, None)
    out["D"] = rule_d(rA, cA, rH, cH) if full else "pending (incomplete)"
    # descriptive, not governing: the same rules with U0 (Day's literal comparator, Q273) in place of XD
    if full:
        eU = {a: _g(res, "ALLx", f"eU_{a}") for a in ("XC", "XT")}
        au = max(eU, key=lambda a: (eU[a] if eU[a] is not None else -9, a == "XT"))
        out["B1_vs_U0 (descriptive)"] = rule_b1(eU[au])
        out["B2_vs_U0 without the enrichment clause (descriptive)"] = (
            "direction (e >= 0.01)" if eU[au] is not None and eU[au] >= 0.01 else "no direction")
    out["ESCALATION"] = ("fires" if out["B2"] in ("supported", "contradicted") else
                         "does not fire" if out["B2"] == "contested" else "pending")
    out["predictions"] = score_predictions(res, out)
    return out


def _hm(cond):
    return "n/a" if cond is None else ("hit" if cond else "miss")


def score_predictions(res, bands):
    full, adq = res["full"], res["adequate"]
    g = lambda s, k, sub=None: _g(res, s, k, sub)
    A = lambda s: (g(s, "XD") is not None)
    P = {}
    xd = g("ALLx", "XD", "dnds") if full else None
    xt = g("ALLx", "XT", "dnds") if full else None
    P["D1 XD ALLx >= 0.65"] = _hm(None if xd is None else xd >= 0.65)
    P["D2 XT ALLx <= 0.40 and B1 supported"] = _hm(None if xt is None else (xt <= 0.40 and bands["B1"] == "supported"))
    ex = g("ALLx", "E_XT") if full else None
    nfx = g("ALLx", "XD", "nonsyn_frac") if full else None
    P["D3 E_XT nonsyn frac > XD's"] = _hm(None if (ex is None or ex["nonsyn_frac"] is None or nfx is None)
                                          else ex["nonsyn_frac"] > nfx)
    P["D4 D supported"] = _hm(None if not full else bands["D"] == "supported")
    if adq["H2765x"]:
        P["D5 hard: some e_A(H2765x) >= 0.10 and enriched"] = _hm(any(
            (g("H2765x", f"e_{a}") or -1) >= 0.10 and g("H2765x", f"enriched_{a}") for a in ("XC", "XT")))
        P["C5 hard: e_XC, e_XT (H2765x) < 0.10"] = _hm(all((g("H2765x", f"e_{a}") or 0) < 0.10 for a in ("XC", "XT")))
    else:
        P["D5 hard: some e_A(H2765x) >= 0.10 and enriched"] = P["C5 hard: e_XC, e_XT (H2765x) < 0.10"] = "n/a"
    if adq["H351x"]:
        r351, c351 = g("H351x", "rise_XD"), g("H351x", "class_XD")
        P["D6 hard: rise(H351x) >= 0.25, class OK"] = _hm(r351 is not None and r351 >= 0.25 and c351 in OK_CLASSES)
        P["C4 class(G, H351x) MISPAIRED or AMBIGUOUS"] = _hm(c351 in ("MISPAIRED", "AMBIGUOUS"))
        cov = (g("H351x", "XD", "coverage"), g("H351x", "U0", "coverage"))
        P["A7 coverage XD > U0 on H351x"] = _hm(None if None in cov else cov[0] > cov[1])
    else:
        P["D6 hard: rise(H351x) >= 0.25, class OK"] = P["C4 class(G, H351x) MISPAIRED or AMBIGUOUS"] = "n/a"
        P["A7 coverage XD > U0 on H351x"] = "n/a"
    P["C1 XD ALLx in 0.20-0.35"] = _hm(None if xd is None else 0.20 <= xd <= 0.35)
    P["C2 |e_XC|, |e_XT| < 0.10 on ALLx"] = _hm(None if not full else
                                               (abs(g("ALLx", "e_XC")) < 0.10 and abs(g("ALLx", "e_XT")) < 0.10))
    rA = g("ALLx", "rise_XD") if full else None
    P["C3 rise(ALLx) < 0.10"] = _hm(None if rA is None else rA < 0.10)
    cs = g("CSAC23x", "XD", "dnds") if full else None
    P["C6 XD CSAC23x in 0.18-0.30"] = _hm(None if cs is None else 0.18 <= cs <= 0.30)
    P["A0 U0 equals L1c gene table"] = _hm(not res["a0_fail"]) if res["complete"] else "n/a"
    P["A1 >= 98% complete"] = _hm(res["complete_share"] is not None and res["complete_share"] >= COMPLETE_MIN)
    ag = g("ALLx", "agree_XD_U0") if full else None
    P["A2 codon agreement U0/XD >= 0.99"] = _hm(None if ag is None else ag >= 0.99)
    xi, ui = g("IFx", "XD", "dnds"), g("IFx", "U0", "dnds")
    P["A3 XD within 3% of U0 on IFx"] = _hm(None if (not full or xi is None or not ui) else abs(xi / ui - 1) <= 0.03)
    P["A4 e_XT, e_XC in [-0.02, 0.06]"] = _hm(None if not full else all(
        -0.02 <= g("ALLx", f"e_{a}") <= 0.06 for a in ("XC", "XT")))
    gs = g("ALLx", "G_share_of_left_out") if full else None
    P["A5 rise in [0, 0.10] and G >= 50% of left-out"] = _hm(None if (rA is None or gs is None) else
                                                            (0.0 <= rA <= 0.10 and gs >= 0.50))
    P["A6 XD 0.24-0.32 and XT 0.23-0.32 on ALLx"] = _hm(None if (xd is None or xt is None) else
                                                      (0.24 <= xd <= 0.32 and 0.23 <= xt <= 0.32))
    P["A8 B2 contested"] = _hm(None if not full else bands["B2"] == "contested")
    return P


def report(res):
    print("\n=== L1c-b report ===")
    print(json.dumps({k: res[k] for k in ("paired", "returned", "complete", "complete_share", "full", "failed",
                                          "skipped", "adequate")}, default=str))
    print("A0 failures:", len(res["a0_fail"]), res["a0_fail"][:20])
    if "reach" in res:
        print("REACH (U0 from the L1c gene table: whole set against the genes this check reached): "
              + json.dumps(res["reach"], default=float))
    fmt = lambda v: "n/a" if v is None or v != v else (f"{v:.4f}" if isinstance(v, float) else str(v))
    for s in SETNAMES:
        x = res["sets"].get(s)
        if not x:
            continue
        print(f"\n[{s}] genes {x['genes']}  sense codons {x['sense']}  U0 left out {x['U0_left_out']}")
        for a in ARMS:
            y = x[a]
            print(f"  {a:3s} dN/dS {fmt(y['dnds'])}  k5 {fmt(y.get('dnds_k5'))}  nonsyn {fmt(y['nonsyn_frac'])}  "
                  f"pS {fmt(y['pS'])}  codons {y['codons']}  coverage {fmt(y['coverage'])}")
        for a in ("XC", "XT"):
            e = x[f"E_{a}"]
            print(f"  e_{a} {fmt(x[f'e_{a}'])} ({ebin(x[f'e_{a}'])})  vs U0 {fmt(x[f'eU_{a}'])}  E_{a}: codons "
                  f"{e['codons']} nonsyn {fmt(e['nonsyn_frac'])} p-ratio {fmt(e['dnds_p'])} pS {fmt(e['pS'])} "
                  f"enriched {x[f'enriched_{a}']}  | gained {x[f'GA_{a}']['codons']}")
        for a in XARMS:
            G = x[f"G_{a}"]
            print(f"  G_{a}: codons {G['codons']} nonsyn {fmt(G['nonsyn_frac'])} p-ratio {fmt(G['dnds_p'])} "
                  f"pS {fmt(G['pS'])} class {x[f'class_{a}']}  rise {fmt(x[f'rise_{a}'])}")
        print(f"  LOST_XD codons {x['LOST_XD']['codons']}  agreement U0/XD {fmt(x['agree_XD_U0'])}  "
              f"G share of left-out {fmt(x['G_share_of_left_out'])}")
        if "XDL_genes" in x:
            print(f"  XDL (longest isoform, descriptive): genes {x['XDL_genes']} rise {fmt(x['rise_XDL'])} "
                  f"(XD on the same genes {fmt(x['rise_XD_same_genes'])}) G codons {x['G_XDL']['codons']}")
    print("\nBANDS: " + json.dumps({k: res[k] for k in ("A_star", "B1", "B2", "D", "ESCALATION")}))
    print("DESCRIPTIVE (not governing): " + json.dumps({k: v for k, v in res.items() if "descriptive" in k}))
    print("PREDICTIONS:")
    for k, v in res["predictions"].items():
        print(f"  {v:5s} {k}")


# ---------------------------------------------------------------- modes
def _prepare(gff, cds, genes_tsv):
    print("inputs sha256:", json.dumps({"cds": sha256_file(cds), "genes_tsv": sha256_file(genes_tsv)}), flush=True)
    assert sha256_file(cds) == CDS_SHA256, "chimp CDS sha256 differs from the registered file"
    gt, h351, h2765, csac = load_gene_table(genes_tsv)
    recs = parse_cds_headers(cds)
    pairs, why = choose_pairs(gt, recs)
    for tid in pairs:
        pairs[tid]["xdl"] = int(tid in h351 and pairs[tid]["longest"] is not None)
    want = {p["hdr_id"] for p in pairs.values()} | {p["longest"] for p in pairs.values() if p["xdl"]}
    seqs = load_cds_seqs(cds, want)
    txs, counts = L1B.load_annotation(gff) if gff else ([], {})
    return gt, h351, h2765, csac, pairs, why, seqs, txs


def run(gff, seg, cds, genes_tsv, out_prefix, workers="10", prank=PRANK, smoke=False):
    t0 = time.time()
    print("PRANK sha256:", check_prank(prank), flush=True)
    gt, h351, h2765, csac, pairs, why, seqs, txs = _prepare(gff, cds, genes_tsv)
    print("pairing:", json.dumps(pair_counts(gt, pairs, why, h351, h2765, csac)), flush=True)
    order = [h351, h2765 - h351, set(gt) - h2765]
    only = None
    if smoke:
        only = smoke_pick(gt, pairs, h351)
        order = [only]
    outj = out_prefix + (".smoke.jsonl.gz" if smoke else ".genes.jsonl.gz")
    recs = []
    with Pool(int(workers), maxtasksperchild=200) as pool, gzip.open(outj, "wt") as fo:
        it = pool.imap_unordered(process, gen_tasks(seg, txs, order, pairs, seqs, prank, smoke, only), chunksize=1)
        for k, x in enumerate(it):
            if not smoke:
                fo.write(json.dumps(x, default=float) + "\n")
            recs.append(x)
            if k % 500 == 0:
                print(f"[{time.time() - t0:7.0f}s] genes {k}", flush=True)
    if smoke:
        smoke_report(recs, gt)
        return
    finish(recs, gt, h351, h2765, csac, len(pairs), out_prefix, time.time() - t0)


def finish(recs, gt, h351, h2765, csac, npaired, out_prefix, secs):
    res = analyse(recs, gt, h351, h2765, csac, npaired)
    res["seconds"] = secs
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    report(res)


def report_mode(genes_tsv, cds, out_prefix):
    gt, h351, h2765, csac = load_gene_table(genes_tsv)
    pairs, why = choose_pairs(gt, parse_cds_headers(cds))
    recs = [json.loads(l) for l in gzip.open(out_prefix + ".genes.jsonl.gz", "rt")]
    finish(recs, gt, h351, h2765, csac, len(pairs), out_prefix, None)


def smoke_pick(gt, pairs, h351):
    tids = sorted((int(gt[t]["L"]), t) for t in pairs)
    cut = tids[: int(len(tids) * 0.99)]
    pick = set()
    for d in range(10):
        lo, hi = len(cut) * d // 10, len(cut) * (d + 1) // 10
        pick.update(t for _, t in cut[lo:lo + 2] if hi > lo)
    pick.update(sorted(t for t in pairs if t in h351 and int(gt[t]["L"]) < 6000)[:4])
    return pick


def smoke_report(recs, gt):
    print("\n=== SMOKE (diagnostics only; no dN/dS) ===")
    pts = {a: [] for a in XARMS}
    for x in recs:
        if x.get("skipped"):
            print(x["meta"]["tid"], "skipped", x["skipped"])
            continue
        L = x["meta"]["L"]
        st = {a: x["status"][a]["status"] for a in x["status"]}
        print(x["meta"]["tid"], "L", L, "status", st, "sec", {a: x["status"][a]["sec"] for a in x["status"]},
              "A0", "pass" if a0_check(x, gt) else "FAIL")
        for a in XARMS:
            if st.get(a) == "ok":
                pts[a].append((L, x["status"][a]["sec"]))
    tot = 0.0
    Ls = [int(r["L"]) for r in gt.values()]
    for a in XARMS:
        if pts[a]:
            k = sum(s * L * L for L, s in pts[a]) / sum(L ** 4 for L, s in pts[a])
            proj = k * sum(L * L for L in Ls) / 3600
            tot += proj
            print(f"  {a}: seconds ~ {k:.3e} x L^2; projected over {len(Ls)} genes: {proj:.1f} CPU-h")
    print(f"  total projected CPU-h {tot:.1f}")


def pair_counts(gt, pairs, why, h351, h2765, csac):
    from collections import Counter
    c = Counter(why.values())
    out = dict(reasons=dict(c), paired=len(pairs), td=sum(p["td"] for p in pairs.values()),
               xdl_H351=sum(1 for t in pairs if t in h351 and pairs[t]["longest"] is not None))
    for nm, s in (("ALL", set(gt)), ("H351", h351), ("H2765", h2765), ("CSAC23", csac)):
        out[f"paired_{nm}"] = f"{sum(1 for t in s if t in pairs)} / {len(s)}"
    return out


def pairing(genes_tsv, cds):
    """Local, trivial: names and lengths only. No alignment, no dN/dS."""
    print("sha256:", sha256_file(cds), sha256_file(genes_tsv))
    gt, h351, h2765, csac = load_gene_table(genes_tsv)
    recs = parse_cds_headers(cds)
    pairs, why = choose_pairs(gt, recs)
    print("records", len(recs), "TD records", sum(r["td"] for r in recs))
    print(json.dumps(pair_counts(gt, pairs, why, h351, h2765, csac), indent=1))


# ---------------------------------------------------------------- synthetic selftest (workstation; no real data)
def _sim(seed, ncod, kind):
    import random
    rng = random.Random(seed)
    sense = sorted(L1.SITES)
    h = [rng.choice(sense) for _ in range(ncod)]
    c = list(h)

    def mutate(cod, k=1):
        for _ in range(100):
            x = list(cod)
            for p in rng.sample(range(3), k):
                x[p] = rng.choice([b for b in "ACGT" if b != x[p]])
            x = "".join(x)
            if x in L1.SITES:
                return x
        return cod
    for i in range(ncod):
        if rng.random() < 0.012:
            c[i] = mutate(c[i])
    if kind == "dense":            # a 15-codon run where every codon carries a replacement (Day's divergent region)
        for i in range(100, 115):
            c[i] = mutate(c[i], 2)
    if kind == "nonhom":           # 30 chimp codons unrelated to the human ones (wrong exon)
        for i in range(200, 230):
            c[i] = rng.choice(sense)
    if kind == "intstop":
        c[150] = "TGA"
    cs = "".join(c)
    ct = cs                        # the true pairing in human coordinates (gaps where chimp lost bases)
    if kind == "indel":            # 3-codon deletion in chimp
        cs = cs[:3 * 120] + cs[3 * 123:]
        ct = ct[:3 * 120] + "---------" + ct[3 * 123:]
    if kind == "frame":            # 1-bp deletion in chimp (uncorrected frameshift; chimp length % 3 != 0)
        cs = cs[:3 * 150 + 1] + cs[3 * 150 + 2:]
        ct = ct[:3 * 150 + 1] + "-" + ct[3 * 150 + 2:]
    return "".join(h) + "TAA", cs + "TAG", ct + "TAG"


def _st_one(args):
    seed, ncod, kind, prank = args
    h, c, c_true = _sim(seed, ncod, kind)
    L = len(h)
    strs, st, fl = align_gene(h, c, L, prank)
    strs["U0"] = c_true            # synthetic stand-in for the Cactus pairing: the truth
    out = dict(kind=kind, seed=seed, status={a: st[a]["status"] for a in st}, sec={a: st[a]["sec"] for a in st},
               flags=fl)
    out["arms"] = {a: {k: L1C.stats(h, strs[a])[k] for k in ("S", "N", "Sd", "Nd")} for a in strs}
    out["ncomp"] = {a: sum(compared(h, strs[a])) for a in strs}
    ok = int(all(st[a]["status"] == "ok" for a in XARMS))
    tid = f"SIM_{kind}_{seed}"
    out["rec"] = dict(meta=dict(tid=tid, name=tid, L=L, td=int(kind == "frame"), **fl), status=st, ok=ok,
                      arms={a: L1C.stats(h, strs[a]) for a in strs}, der=derived(h, strs) if ok else {})
    return out


def selftest(prank=PRANK, workers="1"):
    t0 = time.time()
    print("PRANK sha256:", check_prank(prank))
    # rule exhaustiveness: every input lands in exactly one value
    grid = [x / 100 for x in range(-30, 40)] + [None]
    for e in grid:
        for en in (True, False):
            for hard in (None, [(0.0, False), (0.05, True)], [(0.0, False), (0.0, False)]):
                v = rule_b2(e, en, hard)
                assert v in ("supported", "contested", "contradicted", "pending"), v
        assert rule_b1(e) in ("supported", "contested", "contradicted", "pending")
    classes = ["ORTHO-NORMAL", "DENSE-REAL", "MISPAIRED", "AMBIGUOUS", "TOO-FEW"]
    for r in grid:
        for c in classes:
            for rh in (None, 0.0, 0.2):
                for ch in classes:
                    assert rule_d(r, c, rh, ch) in ("supported", "contested", "contradicted", "pending")
    assert rule_b2(0.05, True, None) == "contested" and rule_b2(0.005, False, [(0.03, True)]) == "contested"
    assert rule_b2(0.005, True, [(0.0, True)]) == "contradicted" and rule_b2(0.2, True, None) == "supported"
    assert rule_d(0.15, "MISPAIRED", None, None) == "contradicted" and rule_d(0.15, "ORTHO-NORMAL", None, None) == "supported"
    assert rule_d(0.0, "TOO-FEW", 0.2, "DENSE-REAL") == "contested"
    # class windows on the R4-L1c reference values
    ref = 0.0177
    mk = lambda nf, pr, ps, n=500: dict(codons=n, nonsyn_frac=nf, dnds_p=pr, pS=ps)
    assert gclass(mk(0.774, 1.018, 0.75), ref) == "MISPAIRED"            # NU / misregistration
    assert gclass(mk(0.95, 5.9, 0.12), ref) == "DENSE-REAL"              # synthetic dense run
    assert gclass(mk(0.60, 0.6, 0.02), ref) == "ORTHO-NORMAL"            # ordinary divergence
    assert gclass(mk(0.85, 2.0, 0.12), ref) == "AMBIGUOUS"
    assert gclass(mk(0.85, 2.0, 0.12, 10), ref) == "TOO-FEW"
    print("rules: exhaustive on the grid; class windows reproduce the R4-L1c references")
    # PRANK on synthetic pairs, through the real Pool
    kinds = ["clean", "indel", "dense", "nonhom", "intstop", "frame"]
    tasks = [(s, 400, k, prank) for k in kinds for s in (1, 2)]
    with Pool(int(workers)) as pool:
        rows = pool.map(_st_one, tasks)
    for x in rows:
        print(json.dumps({k: x[k] for k in ("kind", "seed", "status", "sec", "flags", "ncomp")}))
        dn = {a: (round(v["Nd"], 2), round(v["Sd"], 2)) for a, v in x["arms"].items()}
        print("   (Nd, Sd):", dn)
    clean = [x for x in rows if x["kind"] == "clean"]
    for x in clean:
        for a in XARMS:
            assert x["status"][a] == "ok", x["status"]
            assert x["arms"][a] == x["arms"]["U0"], f"clean pair: {a} differs from truth"
    print("clean pairs: XD = XC = XT = truth exactly (e = 0)")
    for x in [x for x in rows if x["kind"] == "indel"]:
        for a in XARMS:
            assert x["status"][a] == "ok" and x["ncomp"][a] >= 399 - 3 - 3, (a, x["ncomp"])
    print("in-frame deletion: every arm compares >= n - 6 codons")
    for x in [x for x in rows if x["kind"] == "intstop"]:
        for a in XARMS:
            assert x["status"][a] == "ok" and x["ncomp"][a] == 399, (a, x["status"], x["ncomp"])
    print("internal stop: all three arms run (PRANK's NNN accepted) and leave out only the stop codon")
    # the analysis, scoring and report path end to end on the synthetic records (fake gene table and sets)
    recs = [x["rec"] for x in rows]
    gt = {r["meta"]["tid"]: {**{"U0_" + k: str(r["arms"]["U0"][k]) for k in ("S", "N", "Sd", "Nd")}}
          for r in recs}
    hard = {t for t in gt if not t.startswith("SIM_clean")}
    res = analyse(recs, gt, {t for t in gt if "dense" in t or "nonhom" in t}, hard, set(gt), len(recs))
    report(res)
    assert res["B1"] in ("supported", "contested", "contradicted") and res["ESCALATION"] != "pending", res["B1"]
    assert not res["a0_fail"] and len(res["predictions"]) == 21, (res["a0_fail"], len(res["predictions"]))
    print("analysis path: runs end to end; 21 predictions scored or n/a")
    # determinism: same input twice gives the same alignment
    h, c, _ = _sim(7, 300, "dense")
    hn, cn, _ = prep_pair(h, c)
    for a in XARMS:
        r1, r2 = prank_pair(a, hn, cn, prank), prank_pair(a, hn, cn, prank)
        assert r1[:2] == r2[:2], f"{a} not deterministic"
    print("determinism: identical output on repeat, all three modes")
    print(f"selftest done in {time.time() - t0:.1f} s")


if __name__ == "__main__":
    m = sys.argv[1] if len(sys.argv) > 1 else "selftest"
    if m == "selftest":
        selftest(*sys.argv[2:])
    elif m == "pairing":
        pairing(*sys.argv[2:4])
    elif m in ("run", "smoke"):
        a = sys.argv[2:]
        run(a[0], a[1], a[2], a[3], a[4], a[5] if len(a) > 5 else "10", a[6] if len(a) > 6 else PRANK, m == "smoke")
    elif m == "report":
        report_mode(*sys.argv[2:5])
    else:
        sys.exit(f"unknown mode {m}")
