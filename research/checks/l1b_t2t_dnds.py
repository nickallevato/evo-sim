"""L1b: T2T rerun of L1. Human-chimp dN/dS on GENCODE CDS of T2T-CHM13 (hs1) against mPanTro3, extracted from the
8-way T2T-ape Cactus alignment, on the same gene sets, estimator and filter stacks as L1, plus Day's single-SNV count
diagnostic and a paralog/synteny diagnostic. PRE-REGISTERED: committed before the main run (only a synthetic selftest
and the annotation-only step `annot`, which counts transcripts and computes no dN/dS, were run before the commit).

TIER. Load-bearing review tier (three reviews: correctness, steelman-day, steelman-critic), as L1. Recorded honestly:
hierarchy.yaml marks DN1-DN5 `load_bearing: false` (parents ROOT-FM / DN1) and R5-draft.md does not list them among
the 30 load-bearing nodes; the three-review tier is kept because L1 was reviewed at that tier, DN1's external verdict
can flip on this check alone, and the task assigned it. A reviewer may downgrade; nothing below depends on the tier.

TARGETS (verbatim; quotes-day.md, voxday.net "How Biologists Keep 'Proving' Selection", 2026-10-11; RH tag dialectic)
  Q172 (¶7): "We used GENCODE v46 annotations, the same Nei-Gojobori method the original studies used, and the complete
       extraction of human-chimp aligned positions from the T2T-quality assemblies. And we got a result."
  Q173: "Not 0.23. 0.80."
  Q174: "We computed dN/dS on 20,400 protein-coding genes, which is every gene annotated in GENCODE v46 that has coding
       sequence data in the human-chimp alignment."
  Post body (diagnostics ¶): "Single-SNV codons show 71.6% nonsynonymous, 28.4% synonymous. dN/dS = 0.71 for
       single-SNV codons alone."
  Q175: "No combination of quality filters moves the number below 0.65." (same ¶: the strictest stack "still produced
       dN/dS = 0.64 on 10 remaining genes").
  Q176: "If the Consortium's curated subset gives ~0.23 and our complete set gives ~0.80, then the case is closed: the
       published number is an artificial artifact of cherry-picked genes, not an observed property of the human genome."
  Q177 (¶21): "At dN/dS = 0.80, natural selection is not the primary mechanism of adaptive evolution." (DN4: not moved
       by this check; its internal non-sequitur does not depend on the number.)
  Claims: DN1 (0.80 on 20,400 genes), DN2 (filter robustness), DN3 (Q176 conditional), DN5 (CSAC 0.23 as relayed).

WHY (R4-L1.md, Verdicts after the fix pass): L1 used hg38/panTro5 UCSC multiz codon alignments, which are already
  orthology-filtered at the alignment level (syntenic nets). Day's "complete extraction ... from the T2T-quality
  assemblies" route was untested. L1 fixed the overturn condition for DN1 in advance: L1b overturns DN1's external
  `contradicted` only if pooled dN/dS >= 0.65 AND single-SNV nonsyn share >= 66% on genes whose chimp segment passes a
  synteny/orthology check; if the high value appears only in genes failing it, L1b confirms the verdict and locates
  the error. New literature since L1 (refresh-2026-10-11b-lit.md): CSAC 2005 K_A/K_S = 0.23 on 13,454 one-to-one
  orthologues confirmed in the held PDF; no independent genome-wide ML dN/dS found; Nielsen 2005's 0.002578/0.003281
  = 0.786 is per nucleotide site, NOT dN/dS (a trap; this check does not use it).

DATA (public; untrusted, read as text only, never executed; each fetch in its own new dir under sources/raw/, gitignored)
  ANNOT  sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz, fetched 2026-10-11T20:01-06:00
         on the workstation from https://s3-us-west-2.amazonaws.com/human-pangenomics/T2T/CHM13/assemblies/annotation/
         (T2T consortium: GENCODE v35 projected to CHM13 v2.0 by CAT + Liftoff), 158,318,946 bytes,
         sha256 3ff94c1bcdaf8ca6625a17cc1984b92f80d2f339bcd3f077ad6b93849a35d5e9, md5 00fb576ec456d2d97fbb75fc197a4d88.
         (A 3 MB range peek of the same file, sources/raw/l1b-annot-peek-2026-10-11/head.part, sha256 a8a9b833...,
         was read to learn the attribute names; nothing else.) Copied to na-workhorse at launch, sha256 re-checked.
         DISCLOSED before registration (`annot` mode, workstation, 12 s, 274 MB RSS; counts only, no sequence read):
         83,965 protein-coding transcripts; dropped 328 not ortholog-class, 25,450 cds_start/end_NF, 238 CDS length not
         a multiple of 3; 19,407 genes chosen (15,485 MANE_Select), 33.5 Mb CDS; 16,841 Ensembl one2one, 49 gene ids
         absent from the Ensembl 116 BioMart file. The CAT `frameshift` attribute is N/A on every chosen CDS (unused).
  ORTH   Ensembl 116 BioMart human gene x chimp homology type, the L1 file (raw/l1.host: sources/raw/
         l1-biomart-2026-10-11/orth_ptro.tsv on builder, sha256 f30b6ff5bcb682441c3138e9c40bffe454acdd676581925102e869f39797f0f9),
         copied to na-workhorse at launch, sha256 re-checked. Same one2one definition as L1.
  MAF    na-workhorse sources/raw/fm-maf-2026-10-10/hs1.maf.gz = 8-t2t-apes-2023v2.hs1.maf.gz (Cactus, hal2maf
         --refGenome hs1; md5 df51e5c3b842e3be4b81f3dd6486e53b; used by FM and GAP-07t). Chimp = GCA_028858775.2
         (mPanTro3). Blocks list the hs1 reference row first; further hs1/hg38 rows and several chimp rows (paralogous
         copies) can occur in one block.
  Known differences from Day (fixed now): GENCODE v35 projected by CAT, not v46 native (protein-coding gene content
  differs by a few hundred genes; v46 lifted from hg38 via hg38ToHs1.over.chain is a possible later variant, not run
  here); one transcript per gene by the rule below (Day's transcript choice is unstated); the Cactus MAF, not
  whatever aligner Day used.

METHOD (fixed now)
  Transcript per gene (key = source_gene without version): CDS features with transcript_biotype=protein_coding on
    chr1-22, X, Y; transcript_class=ortholog and extra_paralog=False (CAT's primary projection, not Liftoff extra
    copies); no cds_start_NF / cds_end_NF tag; CDS length a multiple of 3. Rank: MANE_Select > Ensembl_canonical >
    appris_principal* > CCDS > basic > longer CDS > transcript id. One transcript per gene.
  Extraction (stream the MAF once): the reference row is the first hs1 row of each block; blocks whose reference is on
    '-' are skipped and counted. For each CDS interval overlapping the reference row, the aligned columns from the
    first to the last CDS base are kept (reference slice plus every chimp row's slice and its chimp start coordinate).
    Human CDS bases come from the reference row (uncovered positions = N, codon skipped). Minus-strand transcripts are
    reverse-complemented after assembly in genomic order.
  Chimp-row variants (one human sequence, codons in the annotated frame):
    V0  first chimp row of each block (hal2maf order; the GAP-07t convention). Primary.
    VS  syntenic row: per gene the modal (chimp sequence, strand) by aligned CDS bases over all rows; per block the row
        on that sequence nearest the previous pick; no such row = gap.
    VR  random chimp row per segment (segment = one block x one CDS exon; seed: random.Random(zlib.crc32(
        transcript_id)), drawn in genomic segment order).
    VL  lowest-identity chimp row per segment (adversarial bound for paralog choice; rows with no aligned CDS base skipped).
    X1  naive ungapped extraction: per transcript, the first-row chimp bases over the CDS columns with gaps removed and
        chimp-only insertion columns INCLUDED, concatenated in genomic order (then reverse-complemented for '-'),
        padded or truncated to the human length and compared position by position. This is a real-data test of the
        W2 class (chimp out of register downstream of an unhandled indel) that fit Day's numbers in L1's per-gene run.
  Estimator, sites, single-difference counts, pooled JC ratio, per-gene ratios, the five filters S G M L O and all
    32 combinations: imported unchanged from l1_dnds_genesets.py (pre-registered 868bb60). S' = S that also counts the
    final codon (as l1_posthoc_pergene.py c04a1f8).
  Synteny/orthology diagnostic per gene (V0 rows): cov = share of CDS bases with a chimp base; m = share of those on
    the modal (chimp sequence, strand); dup = share of CDS bases in blocks with > 1 chimp row; inversions = number of
    consecutive V0 segments on the modal sequence whose chimp start falls below the previous segment's end; span = chimp
    extent on the modal sequence. SYN := cov >= 0.5 AND m >= 0.95 AND dup <= 0.05 AND inversions == 0 AND span <=
    2 x human genomic span + 100 kb. NONSYN := in ALL and not SYN.
  Gene sets: ALL (chosen transcripts with >= 1 aligned chimp base, Day's "has coding sequence data in the
    alignment"); O121 (Ensembl 116 ortholog_one2one); NON121 (rest; split MAPPED / UNMAPPED); O121q (O121 + no
    internal chimp stop, <= 5% gapped codons, >= 300 bp, on V0, as L1); SYN; NONSYN; O121SYN.
  Day's four-part triple (rule from c04a1f8): pooled 0.70-0.90 AND single-diff nonsyn share 66-77% AND min over the 32
    stacks >= 0.60 AND full stack <= 200 genes. Reported for every variant on ALL (S and S' conventions).

PREDICTIONS (fixed now; no dN/dS has been computed on these data)
  Day side (Q172-Q176): V0 ALL pooled ~0.80, at least >= 0.65 (Q175); single-diff nonsyn share ~72% (>= 66%); no
    32-stack combination below 0.65; O121 ~0.23, i.e. the gap ALL - O121 ~ +0.57.
  Critic side: V0 ALL pooled 0.20-0.35; O121 0.18-0.30; SYN 0.18-0.32; share on ALL 35-50%; every 32-stack value on V0
    ALL < 0.40; Q176 arithmetic fails (NON121 pooled p-ratio needed for ALL = 0.80 > 1.5).
  L1 carry-over (audit): the gene-set gap persists in kind: V0 ALL - O121 in [+0.02, +0.12] (L1: +0.064) and
    ALL/O121 in [1.08, 1.60] (L1: 1.31). NON121 pooled 0.30-0.60 (L1: 0.447).
  Audit, further (each can fail):
    A1 V0 ALL within 0.05 of L1's 0.271 (0.22-0.32); V0 site ratio N/S in 3.2-3.4 (L1 3.34).
    A2 VS ALL within 0.03 of V0 ALL; SYN holds >= 80% of ALL genes; NONSYN pooled > SYN pooled.
    A3 VR and VL raise ALL by <= 0.10 over V0 (paralog choice in a Cactus MAF cannot carry 0.27 -> 0.80); share of
       CDS bases with dup > 0 is < 10%.
    A4 X1 (naive ungapped) ALL pooled 0.28-0.60 and does NOT meet the triple: real human-chimp CDS indels that are not
       multiples of 3 are too rare to put most genes out of register (L1's W2 needed a break in every gene).
    A5 ALL holds 18,000-20,000 genes (Day: 20,400; L1 23,183 transcripts incl. non-GENCODE-basic).
    A6 stop-free in both species (V0 ALL) > 90% of genes; full stack S+G+M+L+O keeps > 10,000 genes.
  Bands (pooled JC dN/dS of V0 on the named set; fixed now):
    DAY       ALL >= 0.65 AND SYN >= 0.65 AND share(SYN) >= 66%
    LOCATED   ALL >= 0.65 (or any of VR/VL/X1 meets the triple) but SYN < 0.40: high value confined to non-syntenic
              projection or naive extraction
    MIDDLE    0.40 <= SYN < 0.65, or 0.40 <= ALL < 0.65
    CRITIC    ALL < 0.40 AND SYN < 0.40

WHAT MOVES WHICH VERDICT (proposals for integration; the owner decides)
  DN1 external `contradicted` -> `contested` under DAY (L1's pre-stated condition); stays and the error class is named
    under LOCATED (non-syntenic projection or naive extraction, whichever carries it); MIDDLE on SYN -> `contested`
    proposed with the number stated; CRITIC -> stays, now on T2T and Cactus as well (the "different assembly /
    complete extraction" route is closed for this alignment). DN1 internal stays `pending` (method unreleased).
  DN2 external: re-opened (`contested`) if min over the 32 stacks on V0 ALL or SYN >= 0.60; otherwise stays.
  DN3 external (gene-list and alignment-level versions): `supported` only if ALL - O121 >= +0.40 with O121 <= 0.30 on
    V0 (Q176's antecedent, alignment-level); otherwise stays `contradicted`, now also for the alignment-level version.
    Day's L1 credit (+31%, material by R1) is restated with the T2T value; if the gap is < +0.02 the credit is marked
    pipeline-specific.
  DN5 external `supported` stays if O121 in 0.18-0.30; fidelity is a reading question (CSAC 2005), not moved here.
  DN4: not moved.

WHAT DAY'S PROMISED ZENODO TABLE (Q176) WOULD NEED, to compare gene by gene (out file l1b.genes.tsv.gz has the same
  columns): per gene the GENCODE v46 gene and transcript ids (versioned) and gene symbol; hs1 CDS coordinates or exon
  list; the chimp assembly accession and the chimp coordinates (sequence, strand, start/end) actually paired with each
  CDS; the alignment source (which MAF/chain/aligner) and how chimp-only insertions and multiple chimp hits were
  handled; per gene N and S sites, Nd and Sd differences, codons compared, single-difference codon counts (n1, s1),
  internal and terminal stop flags per species, gap fraction; the filter thresholds and which genes survive each
  stack (the 10 genes); the aggregation (pooled vs mean) and the multiple-hit correction; code or exact commands.

SEEDS: only VR is random: random.Random(zlib.crc32(transcript_id.encode())), one draw per segment, genomic order.

RESOURCES (estimates): one process. Streaming the 3.4 GB MAF ~1-2 h (GAP-07t's heavier pass took ~50-90 min);
  annotation parse ~1 min; analysis ~5-10 min. RAM: segments of ~35 Mb CDS with all chimp rows, < 2.5 GB peak
  (recorded with /usr/bin/time -v). ~2 CPU-h. Fits na-workhorse (14 GB) next to other jobs, counting as 1 of the 11
  allowed busy processes. Builder (5 GB) would also fit, but the MAF lives on na-workhorse. Disk: segment dump ~0.3-1 GB
  under sources/raw/l1b-seg-<date>/ (gitignored); committed outputs l1b.out, l1b.json, l1b.genes.tsv.gz (few MB).

LAUNCH (only after the HF run `ph` has finished; check `uptime` first; at most 11 busy processes across agents):
  rsync -a research/checks/l1b_t2t_dnds.py research/checks/l1_dnds_genesets.py na-workhorse:projects/evo-sim/research/checks/
  ssh -o BatchMode=yes na-workhorse 'mkdir -p ~/projects/evo-sim/sources/raw/l1b-annot-2026-10-11 ~/projects/evo-sim/sources/raw/l1-biomart-2026-10-11'
  rsync -a sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz na-workhorse:projects/evo-sim/sources/raw/l1b-annot-2026-10-11/
  rsync -a builder:projects/evo-sim/sources/raw/l1-biomart-2026-10-11/orth_ptro.tsv <scratch>/ && \
    rsync -a <scratch>/orth_ptro.tsv na-workhorse:projects/evo-sim/sources/raw/l1-biomart-2026-10-11/
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && sha256sum sources/raw/l1b-annot-2026-10-11/*.gz sources/raw/l1-biomart-2026-10-11/orth_ptro.tsv && md5sum research/checks/l1b_t2t_dnds.py research/checks/l1_dnds_genesets.py sources/raw/fm-maf-2026-10-10/hs1.maf.gz'
     (hashes must equal those above; l1_dnds_genesets.py md5 fde848f7b5600d17d73f320ccd4ec707; record all in raw/l1b.host)
  ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && mkdir -p sources/raw/l1b-seg-$(date +%F) && nohup /usr/bin/time -v research/.venv/bin/python -I research/checks/l1b_t2t_dnds.py run sources/raw/l1b-annot-2026-10-11/chm13v2.0_GENCODEv35_CAT_Liftoff.vep.gff3.gz sources/raw/l1-biomart-2026-10-11/orth_ptro.tsv sources/raw/fm-maf-2026-10-10/hs1.maf.gz research/checks/results/raw/l1b sources/raw/l1b-seg-$(date +%F)/seg.json.gz > research/checks/results/raw/l1b.out 2>&1 < /dev/null &'
COLLECT (once, ~2 h later; never commit from workhorse):
  rsync -a 'na-workhorse:projects/evo-sim/research/checks/results/raw/l1b*' research/checks/results/raw/
  research/.venv/bin/python -I research/checks/l1b_t2t_dnds.py report research/checks/results/raw/l1b.json
Other modes: `annot GFF ORTH` (annotation counts only), `selftest` (synthetic MAF + GFF; trivial).
"""
import gzip
import importlib.util
import json
import os
import random
import sys
import tempfile
import time
import zlib
from bisect import bisect_right

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
_spec = importlib.util.spec_from_file_location("l1", os.path.join(HERE, "l1_dnds_genesets.py"))
L1 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(L1)

CHIMP = "GCA_028858775.2"
REF = "hs1"
CHROMS = {f"chr{i}" for i in range(1, 23)} | {"chrX", "chrY"}
VARIANTS = ["V0", "VS", "VR", "VL", "X1"]
GAP = 45  # ord('-')
SETS = ["ALL", "O121", "NON121", "MAPPED_NON121", "UNMAPPED", "O121q", "SYN", "NONSYN", "O121SYN"]


# ---------------------------------------------------------------- annotation
def parse_attrs(s):
    return dict(kv.split("=", 1) for kv in s.rstrip("\n").split(";") if "=" in kv)


def load_annotation(gff):
    """Return list of chosen transcripts: dict(tid, gene, name, chrom, strand, cds=[(start0, end0)...] sorted, L, flags)."""
    tx = {}
    opener = gzip.open if gff.endswith(".gz") else open
    with opener(gff, "rt") as fh:
        for line in fh:
            if line.startswith("#"):
                continue
            f = line.split("\t", 8)
            if len(f) < 9 or f[2] != "CDS" or "transcript_biotype=protein_coding" not in f[8]:
                continue
            if f[0] not in CHROMS:
                continue
            a = None
            t = None
            p = f[8].find("transcript_id=")
            if p >= 0:
                t = f[8][p + 14:].split(";", 1)[0].strip()
            if t is None:
                continue
            rec = tx.get(t)
            if rec is None:
                a = parse_attrs(f[8])
                rec = dict(tid=t, gene=a.get("source_gene", "N/A").split(".")[0], name=a.get("gene_name", ""),
                           src_tx=a.get("source_transcript", ""), chrom=f[0], strand=f[6],
                           tclass=a.get("transcript_class", ""), extra=a.get("extra_paralog", ""),
                           tags=set(a.get("tag", "").split(",")), frameshift=a.get("frameshift", ""),
                           proper_orf=a.get("proper_orf", ""), valid_start=a.get("valid_start", ""),
                           valid_stop=a.get("valid_stop", ""), cds=[])
                tx[t] = rec
            rec["cds"].append((int(f[3]) - 1, int(f[4])))
    counts = dict(pc_transcripts=len(tx))
    best = {}
    drop = dict(not_ortholog=0, extra_paralog=0, nf_tag=0, len3=0, no_gene=0, chrom_strand_mixed=0)

    def rank(r):
        tg = r["tags"]
        return (int("MANE_Select" in tg), int("Ensembl_canonical" in tg),
                int(any(x.startswith("appris_principal") for x in tg)), int("CCDS" in tg), int("basic" in tg),
                r["L"], r["tid"])

    for r in tx.values():
        r["cds"].sort()
        r["L"] = sum(e - s for s, e in r["cds"])
        if r["gene"] in ("N/A", "", "nan"):
            drop["no_gene"] += 1
            continue
        if r["tclass"] != "ortholog":
            drop["not_ortholog"] += 1
            continue
        if r["extra"] == "True":
            drop["extra_paralog"] += 1
            continue
        if "cds_start_NF" in r["tags"] or "cds_end_NF" in r["tags"]:
            drop["nf_tag"] += 1
            continue
        if r["L"] % 3 != 0 or r["L"] == 0:
            drop["len3"] += 1
            continue
        b = best.get(r["gene"])
        if b is None or rank(r) > rank(b):
            best[r["gene"]] = r
    counts.update(drop)
    out = []
    for r in sorted(best.values(), key=lambda r: (r["chrom"], r["cds"][0][0])):
        r = dict(r)
        r["tags"] = sorted(t for t in r["tags"] if t in ("MANE_Select", "Ensembl_canonical", "CCDS", "basic"))
        out.append(r)
    counts["genes_chosen"] = len(out)
    counts["cds_bp"] = sum(r["L"] for r in out)
    counts["mane"] = sum(1 for r in out if "MANE_Select" in r["tags"])
    counts["frameshift_flag"] = sum(1 for r in out if r["frameshift"] not in ("", "nan", "N/A", "False"))
    counts["proper_orf_false"] = sum(1 for r in out if r["proper_orf"] == "False")
    return out, counts


def load_orth(orth):
    otype = {}
    rank = {"ortholog_one2one": 3, "ortholog_one2many": 2, "ortholog_many2many": 1}
    with open(orth) as fh:
        next(fh)
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if not f[0]:
                continue
            otype.setdefault(f[0], "")
            if len(f) >= 3 and f[2] and rank.get(f[2], 0) > rank.get(otype[f[0]], 0):
                otype[f[0]] = f[2]
    return otype


# ---------------------------------------------------------------- extraction
def build_index(txs):
    idx = {}
    for ti, r in enumerate(txs):
        goff = 0
        for s, e in r["cds"]:
            idx.setdefault(r["chrom"], []).append((s, e, ti, goff))
            goff += e - s
    out = {}
    for ch, iv in idx.items():
        iv.sort()
        out[ch] = (np.array([x[0] for x in iv], dtype=np.int64), iv, max(x[1] - x[0] for x in iv))
    return out


def extract(txs, maf, log_every=2_000_000):
    t0 = time.time()
    index = build_index(txs)
    human = [bytearray(b"N" * r["L"]) for r in txs]
    hcount = [0] * len(txs)
    segs = [[] for _ in txs]
    st = dict(blocks=0, ref_not_first=0, ref_minus=0, no_ref=0, cds_blocks=0, cds_blocks_multi_chimp=0,
              cds_blocks_no_chimp=0, double_cover_bp=0)
    refp = REF + "."
    chp = CHIMP + "."

    def flush(block):
        st["blocks"] += 1
        ref = None
        for k, ln in enumerate(block):
            if ln.startswith("s\t" + refp) or ln.startswith("s " + refp):
                ref = ln
                if k:
                    st["ref_not_first"] += 1
                break
        if ref is None:
            st["no_ref"] += 1
            return
        p = ref.split(None, 6)
        chrom = p[1][len(refp):]
        ent = index.get(chrom)
        if ent is None:
            return
        bstart, bsize = int(p[2]), int(p[3])
        bend = bstart + bsize
        starts, iv, maxlen = ent
        hi = bisect_right(starts, bend - 1)
        lo = bisect_right(starts, bstart - maxlen - 1)
        hits = [iv[j] for j in range(lo, hi) if iv[j][1] > bstart]
        if not hits:
            return
        if p[4] != "+":
            st["ref_minus"] += 1
            return
        st["cds_blocks"] += 1
        rtext = p[6].rstrip()
        rarr = np.frombuffer(rtext.encode(), np.uint8)
        cols = np.flatnonzero(rarr != GAP)
        crows = []
        for ln in block:
            if ln.startswith("s\t" + chp) or ln.startswith("s " + chp):
                q = ln.split(None, 6)
                q[6] = q[6].rstrip()
                carr = np.frombuffer(q[6].encode(), np.uint8)
                cnz = np.cumsum(carr != GAP)  # chimp bases up to and including each column
                crows.append((q[1][len(chp):], q[4], int(q[2]), q[6], cnz))
        if not crows:
            st["cds_blocks_no_chimp"] += 1
        elif len(crows) > 1:
            st["cds_blocks_multi_chimp"] += 1
        for s, e, ti, goff in hits:
            a, b = max(s, bstart), min(e, bend)
            if a >= b:
                continue
            c0, c1 = int(cols[a - bstart]), int(cols[b - 1 - bstart]) + 1
            rs = rtext[c0:c1]
            hb = rs.replace("-", "")
            g0 = goff + (a - s)
            if human[ti][g0:g0 + len(hb)] != b"N" * len(hb):
                st["double_cover_bp"] += len(hb)
            human[ti][g0:g0 + len(hb)] = hb.encode()
            hcount[ti] += len(hb)
            rows = []
            for src, strand, cst, ctext, cnz in crows:
                before = int(cnz[c0 - 1]) if c0 > 0 else 0
                rows.append((src, strand, cst + before, ctext[c0:c1]))
            segs[ti].append((g0, rs, rows))

    block = []
    with gzip.open(maf, "rt") as fh:
        for line in fh:
            c = line[:1]
            if c == "s":
                block.append(line)
            elif c == "a":
                if block:
                    flush(block)
                    if st["blocks"] % log_every == 0:
                        print(f"[{time.time() - t0:7.0f}s] blocks {st['blocks']}", flush=True)
                block = []
        if block:
            flush(block)
    st["seconds"] = time.time() - t0
    st["human_bp_covered"] = sum(hcount)
    return dict(human=[h.decode() for h in human], segs=segs, stats=st)


# ---------------------------------------------------------------- per-gene assembly
def aligned_bases(rs, cs):
    """chimp bases at reference (non-gap) columns of one segment, as bytes (gap = '-')."""
    r = np.frombuffer(rs.encode(), np.uint8)
    c = np.frombuffer(cs.encode(), np.uint8)
    return c[r != GAP].tobytes()


def ident(rs, cs):
    r = np.frombuffer(rs.upper().encode(), np.uint8)
    c = np.frombuffer(cs.upper().encode(), np.uint8)
    m = (r != GAP) & (c != GAP)
    n = int(m.sum())
    return (int((r[m] == c[m]).sum()) / n) if n else None, n


def revcomp(s):
    return s.translate(L1.COMP)[::-1]


def assemble(r, human, segs):
    """Return dict variant -> chimp CDS (transcript orientation), human CDS, and the synteny diagnostics."""
    L = r["L"]
    out = {}
    # weights for modal (seq, strand), over all rows
    w_all = {}
    w_first = {}
    for g0, rs, rows in segs:
        for k, (src, strand, cst, cs) in enumerate(rows):
            n = int(np.count_nonzero(np.frombuffer(aligned_bases(rs, cs), np.uint8) != GAP))
            w_all[(src, strand)] = w_all.get((src, strand), 0) + n
            if k == 0:
                w_first[(src, strand)] = w_first.get((src, strand), 0) + n
    modal_all = max(w_all, key=w_all.get) if w_all else None
    modal_first = max(w_first, key=w_first.get) if w_first else None
    rng = random.Random(zlib.crc32(r["tid"].encode()))
    ch = {v: bytearray(b"-" * L) for v in ("V0", "VS", "VR", "VL")}
    naive = []
    prev_end = None
    dup_bp = 0
    v0_segs = []
    for g0, rs, rows in segs:
        nref = len(rs) - rs.count("-")
        if not rows:
            continue
        if len(rows) > 1:
            dup_bp += nref
        # V0
        ab = aligned_bases(rs, rows[0][3])
        ch["V0"][g0:g0 + nref] = ab
        naive.append(rows[0][3].replace("-", ""))
        v0_segs.append((rows[0][0], rows[0][1], rows[0][2], rows[0][2] + len(rows[0][3]) - rows[0][3].count("-")))
        # VR
        k = rng.randrange(len(rows))
        ch["VR"][g0:g0 + nref] = aligned_bases(rs, rows[k][3])
        # VL
        best = None
        for k2, row in enumerate(rows):
            idn, n = ident(rs, row[3])
            if n and (best is None or idn < best[0]):
                best = (idn, k2)
        if best is not None:
            ch["VL"][g0:g0 + nref] = aligned_bases(rs, rows[best[1]][3])
        # VS
        cand = [row for row in rows if (row[0], row[1]) == modal_all]
        if cand:
            if prev_end is None or len(cand) == 1:
                pick = cand[0]
            else:
                pick = min(cand, key=lambda row: abs(row[2] - prev_end))
            ch["VS"][g0:g0 + nref] = aligned_bases(rs, pick[3])
            prev_end = pick[2] + len(pick[3]) - pick[3].count("-")
    x1 = "".join(naive)
    h = human
    if r["strand"] == "-":
        h = revcomp(h)
        x1 = revcomp(x1)
    x1 = (x1 + "-" * L)[:L]
    for v in ("V0", "VS", "VR", "VL"):
        s = ch[v].decode()
        out[v] = revcomp(s) if r["strand"] == "-" else s
    out["X1"] = x1
    # diagnostics on V0
    v0 = ch["V0"]
    cov_bp = L - v0.count(b"-")
    on_modal = sum(n for k, n in w_first.items() if k == modal_first) if modal_first else 0
    tot_first = sum(w_first.values())
    inv = 0
    span = 0
    ms = [x for x in v0_segs if (x[0], x[1]) == modal_first]
    if ms:
        last_end = None
        for src, strand, a, b in ms:
            if last_end is not None and a < last_end:
                inv += 1
            last_end = b if last_end is None else max(last_end, b)
        span = max(x[3] for x in ms) - min(x[2] for x in ms)
    hspan = r["cds"][-1][1] - r["cds"][0][0]
    diag = dict(cov=cov_bp / L, m=(on_modal / tot_first) if tot_first else 0.0, dup=dup_bp / L, inv=inv,
                span=span, hspan=hspan, nloci=sum(1 for n in w_first.values() if n >= 30),
                modal=f"{modal_first[0]}{modal_first[1]}" if modal_first else "")
    diag["SYN"] = int(diag["cov"] >= 0.5 and diag["m"] >= 0.95 and diag["dup"] <= 0.05 and inv == 0
                      and span <= 2 * hspan + 100_000)
    return h, out, diag


def terminal(h, c):
    n = len(h) // 3
    a, b = h[3 * (n - 1):3 * n].upper(), c[3 * (n - 1):3 * n].upper()
    return int(L1.CODE.get(a) == "*"), int(L1.CODE.get(b) == "*")


FILTERS_SP = dict(L1.FILTERS)
FILTERS_SP["S"] = lambda g: g["stop_h"] == 0 and g["stop_c"] == 0 and g["term_h"] == 0 and g["term_c"] == 0


def grid(gs, filters):
    old = L1.FILTERS
    L1.FILTERS = filters
    try:
        fg = L1.filter_grid(gs)
    finally:
        L1.FILTERS = old
    full = [g for g in gs if all(f(g) for f in filters.values())]
    return fg, L1.pooled(full)


def triple(s, fg, full):
    d = s.get("dnds", float("nan"))
    sh = s.get("single_nonsyn_share", float("nan"))
    parts = [0.70 <= d <= 0.90, 0.66 <= sh <= 0.77, fg["min"] is not None and fg["min"] >= 0.60, full["n"] <= 200]
    return dict(parts=[int(x) for x in parts], meets=int(all(parts)))


def analyse(txs, ext, otype, out_prefix):
    t0 = time.time()
    per = {v: {k: [] for k in SETS} for v in VARIANTS}
    rows_tsv = []
    nzero = 0
    for ti, r in enumerate(txs):
        h, chs, diag = assemble(r, ext["human"][ti], ext["segs"][ti])
        if diag["cov"] <= 0:
            nzero += 1
            continue
        ot = otype.get(r["gene"])
        is121 = ot == "ortholog_one2one"
        sets = ["ALL", "O121" if is121 else "NON121"]
        if not is121:
            sets.append("UNMAPPED" if ot is None else "MAPPED_NON121")
        sets.append("SYN" if diag["SYN"] else "NONSYN")
        if is121 and diag["SYN"]:
            sets.append("O121SYN")
        rec = [r["gene"], r["name"], r["tid"], r["src_tx"], r["chrom"], r["strand"], str(r["L"]),
               ot or "unmapped", f"{diag['cov']:.4f}", f"{diag['m']:.4f}", f"{diag['dup']:.4f}", str(diag["inv"]),
               str(diag["span"]), str(diag["hspan"]), str(diag["nloci"]), diag["modal"], str(diag["SYN"])]
        for v in VARIANTS:
            g = L1.gene_stats(h, chs[v])
            g["term_h"], g["term_c"] = terminal(h, chs[v])
            g["tx"] = r["tid"]
            ss = list(sets)
            if (v == "V0" and is121 and g["stop_c"] == 0 and g["gapfrac"] <= 0.05 and g["len_bp"] >= 300):
                ss.append("O121q")
            for k in ss:
                per[v][k].append(g)
            rec += [f"{g[k]:.4g}" if isinstance(g[k], float) else str(g[k])
                    for k in ("S", "N", "Sd", "Nd", "s1", "n1", "stop_h", "stop_c", "term_h", "term_c", "gapfrac")]
        rows_tsv.append(rec)
    res = dict(n_chosen=len(txs), n_no_chimp=nzero, extract=ext["stats"], variants={})
    for v in VARIANTS:
        d = {k: L1.summarise(gs) for k, gs in per[v].items() if gs}
        for setname in ("ALL", "SYN"):
            if not per[v][setname]:
                continue
            fg, full = grid(per[v][setname], L1.FILTERS)
            fgp, fullp = grid(per[v][setname], FILTERS_SP)
            d[f"filters_{setname}"] = fg
            d[f"full_{setname}"] = full
            d[f"filtersSp_{setname}"] = fgp
            d[f"fullSp_{setname}"] = fullp
            d[f"triple_{setname}"] = triple(d[setname], fg, full)
            d[f"tripleSp_{setname}"] = triple(d[setname], fgp, fullp)
        res["variants"][v] = d
    o, non = res["variants"]["V0"].get("O121"), res["variants"]["V0"].get("NON121")
    if o and non and "S" in o and "S" in non:
        res["q176_required_non121_p_ratio"] = L1.required_non121(o, non)
        res["q176_non121_share_of_sites"] = non["N"] / (o["N"] + non["N"])
    res["band"] = band(res)
    res["analyse_seconds"] = time.time() - t0
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    hdr = ["gene", "name", "tid", "src_tx", "chrom", "strand", "L", "otype", "cov", "m", "dup", "inv", "span", "hspan",
           "nloci", "modal", "SYN"]
    for v in VARIANTS:
        hdr += [f"{v}_{k}" for k in ("S", "N", "Sd", "Nd", "s1", "n1", "stop_h", "stop_c", "term_h", "term_c", "gapfrac")]
    with gzip.open(out_prefix + ".genes.tsv.gz", "wt") as fh:
        fh.write("\t".join(hdr) + "\n")
        for rec in rows_tsv:
            fh.write("\t".join(rec) + "\n")
    return res


def band(res):
    V = res["variants"]
    v0 = V["V0"]
    a = v0.get("ALL", {}).get("dnds", float("nan"))
    s = v0.get("SYN", {}).get("dnds", float("nan"))
    sh = v0.get("SYN", {}).get("single_nonsyn_share", float("nan"))
    other = any(V[v].get("triple_ALL", {}).get("meets") or V[v].get("tripleSp_ALL", {}).get("meets")
                for v in ("VR", "VL", "X1"))
    if a >= 0.65 and s >= 0.65 and sh >= 0.66:
        return "DAY"
    if (a >= 0.65 or other) and s < 0.40:
        return "LOCATED"
    if 0.40 <= s < 0.65 or 0.40 <= a < 0.65:
        return "MIDDLE"
    if a < 0.40 and s < 0.40:
        return "CRITIC"
    return "UNCLASSIFIED"


# ---------------------------------------------------------------- report
def report(res):
    nz = lambda x: float("nan") if x is None else x
    print(f"chosen transcripts {res['n_chosen']}, no chimp base {res['n_no_chimp']}")
    print("extract:", json.dumps(res["extract"]))
    print("variant set            n   pooledJC  NdSd_raw  N/S   mean   median  1diff_share stopfree_both")
    for v, d in res["variants"].items():
        for k in SETS:
            if k not in d:
                continue
            s = d[k]
            print(f"{v:3s} {k:14s} {s['n']:6d}  {nz(s.get('dnds')):.3f}    {nz(s.get('NdSd_raw')):.3f}    "
                  f"{nz(s.get('NS_ratio')):.2f}  {nz(s.get('mean_ratio')):.3f}  {nz(s.get('median_ratio')):.3f}   "
                  f"{nz(s.get('single_nonsyn_share')):.3f}       {s['stopfree_both']}")
        for setname in ("ALL", "SYN"):
            if f"filters_{setname}" not in d:
                continue
            fg, full = d[f"filters_{setname}"], d[f"full_{setname}"]
            fgp, fullp = d[f"filtersSp_{setname}"], d[f"fullSp_{setname}"]
            print(f"    {setname}: 32 stacks min {nz(fg['min']):.3f} max {nz(fg['max']):.3f}; full n={full['n']} "
                  f"dnds={nz(full.get('dnds')):.3f}; S' min {nz(fgp['min']):.3f} full n={fullp['n']} "
                  f"dnds={nz(fullp.get('dnds')):.3f}; triple {d[f'triple_{setname}']} S' {d[f'tripleSp_{setname}']}")
    if "q176_required_non121_p_ratio" in res:
        print(f"Q176: NON121 share of N sites {res['q176_non121_share_of_sites']:.3f}; NON121 p-ratio needed for "
              f"ALL = 0.80: {res['q176_required_non121_p_ratio']:.3f}")
    v0 = res["variants"]["V0"]
    if "ALL" in v0 and "O121" in v0:
        print(f"gap ALL - O121 {v0['ALL']['dnds'] - v0['O121']['dnds']:+.3f}; ratio "
              f"{v0['ALL']['dnds'] / v0['O121']['dnds']:.3f} (L1: +0.064, 1.31)")
    print(f"BAND: {res['band']}")


# ---------------------------------------------------------------- selftest (synthetic; trivial)
def selftest():
    d = tempfile.mkdtemp()
    gff = os.path.join(d, "a.gff3")
    A = ("source_gene=ENSG01.1;gene_name=G{n};source_transcript=ENST0{n}.1;transcript_biotype=protein_coding;"
         "transcript_class=ortholog;extra_paralog=False;tag=basic,MANE_Select;transcript_id=T{n}")
    with open(gff, "w") as fh:
        # T1 on +: CDS 1-based [11,16] and [21,26] -> 0-based [10,16),[20,26): 12 bp
        fh.write(f"chr1\tCAT\tCDS\t11\t16\t.\t+\t0\t{A.format(n=1)}\n")
        fh.write(f"chr1\tCAT\tCDS\t21\t26\t.\t+\t0\t{A.format(n=1)}\n".replace("ENSG01", "ENSG01"))
        # T2 on -: CDS 0-based [40,49), different gene
        fh.write(f"chr1\tCAT\tCDS\t41\t49\t.\t-\t0\t{A.format(n=2).replace('ENSG01', 'ENSG02')}\n")
    txs, counts = load_annotation(gff)
    assert counts["genes_chosen"] == 2, counts
    maf = os.path.join(d, "t.maf.gz")
    # block 1: hs1 chr1 0..20 (20 bp); chimp has an insertion 'TT' after ref pos 12 and a deletion at ref pos 14
    r1 = "AAAAAAAAAA" + "ATG" + "--" + "GCA" + "AAAA"          # ref: 10 + 3 + 3 + 4 = 20 bases
    c1 = "AAAAAAAAAA" + "ATA" + "TT" + "G-A" + "AAAA"
    p1 = "CCCCCCCCCC" + "CCC" + "--" + "CCC" + "CCCC"           # second chimp row (paralog), all C
    # block 2: hs1 chr1 20..30: CDS [20,26) = 'TGGTAA'
    r2 = "TGGTAACCCC"
    c2 = "TGGTAGCCCC"
    # block 3: hs1 chr1 40..49 minus-strand gene CDS genomic 'TTACCACAT' -> revcomp 'ATGTGGTAA'
    r3 = "TTACCACAT"
    c3 = "TTACCGCAT"
    blocks = [
        ("hs1.chr1", 0, 20, r1, [(CHIMP + ".CM1", 100, c1), (CHIMP + ".CM9", 500, p1)]),
        ("hs1.chr1", 20, 10, r2, [(CHIMP + ".CM1", 121, c2)]),
        ("hs1.chr1", 40, 9, r3, [(CHIMP + ".CM1", 150, c3)]),
    ]
    with gzip.open(maf, "wt") as fh:
        fh.write("##maf version=1\n\n")
        for src, st, sz, rt, crows in blocks:
            fh.write(f"a\ns\t{src}\t{st}\t{sz}\t+\t1000\t{rt}\n")
            fh.write(f"s\thg38.chr1\t{st}\t{sz}\t+\t1000\t{rt}\n")
            for csrc, cst, ct in crows:
                fh.write(f"s\t{csrc}\t{cst}\t{len(ct) - ct.count('-')}\t+\t1000\t{ct}\n")
            fh.write("\n")
    ext = extract(txs, maf)
    t1 = [i for i, r in enumerate(txs) if r["tid"] == "T1"][0]
    t2 = [i for i, r in enumerate(txs) if r["tid"] == "T2"][0]
    assert ext["human"][t1] == "ATGGCATGGTAA", ext["human"][t1]
    h, chs, diag = assemble(txs[t1], ext["human"][t1], ext["segs"][t1])
    assert h == "ATGGCATGGTAA"
    assert chs["V0"] == "ATAG-ATGGTAG", chs["V0"]
    assert chs["VL"] == "CCCCCCTGGTAG", chs["VL"]
    assert chs["X1"] == "ATATTGATGGTA", chs["X1"]   # insertion kept, deletion dropped: out of register
    assert abs(diag["dup"] - 0.5) < 1e-9 and diag["inv"] == 0, diag
    h2, chs2, diag2 = assemble(txs[t2], ext["human"][t2], ext["segs"][t2])
    assert h2 == "ATGTGGTAA" and chs2["V0"] == "ATGCGGTAA", (h2, chs2["V0"])
    assert diag2["SYN"] == 1 and diag["SYN"] == 0
    g = L1.gene_stats(h2, chs2["V0"])
    assert g["n1"] == 1 and g["s1"] == 0, g
    res = analyse(txs, ext, {"ENSG01": "ortholog_one2one", "ENSG02": "ortholog_one2many"}, os.path.join(d, "o"))
    assert res["variants"]["V0"]["ALL"]["n"] == 2
    print("selftest ok", d)


def run(gff, orth, maf, out_prefix, seg_out=None):
    t0 = time.time()
    txs, counts = load_annotation(gff)
    print("annotation:", json.dumps(counts), flush=True)
    otype = load_orth(orth)
    ext = extract(txs, maf)
    print("extract:", json.dumps(ext["stats"]), flush=True)
    if seg_out:
        with gzip.open(seg_out, "wt") as fh:
            for r, h, s in zip(txs, ext["human"], ext["segs"]):
                fh.write(json.dumps(dict(tid=r["tid"], human=h, segs=s)) + "\n")
    res = analyse(txs, ext, otype, out_prefix)
    res["annotation"] = counts
    res["total_seconds"] = time.time() - t0
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    report(res)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "selftest":
        selftest()
    elif len(a) == 3 and a[0] == "annot":
        txs, counts = load_annotation(a[1])
        ot = load_orth(a[2])
        counts["o121_of_chosen"] = sum(1 for r in txs if ot.get(r["gene"]) == "ortholog_one2one")
        counts["unmapped_of_chosen"] = sum(1 for r in txs if r["gene"] not in ot)
        print(json.dumps(counts))
    elif len(a) in (5, 6) and a[0] == "run":
        run(*a[1:])
    elif len(a) == 2 and a[0] == "report":
        report(json.load(open(a[1])))
    else:
        print(__doc__)
