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

ARMS = ["U0", "UG", "UT", "P", "PG", "PF1", "PF2"]
EXCL_ARMS = ["UG", "P", "PG", "PF1", "PF2"]
NR_GRID = [0.002, 0.005, 0.01, 0.02, 0.05, 0.10]
NM_GRID = [0.1, 0.25, 0.5, 1.0]
NOISE_ARMS = [f"NR{r}" for r in NR_GRID] + [f"NM{f}" for f in NM_GRID] + ["NU"]
KAPPAS = [1, 2, 3, 4, 5, 6]
SETS = ["ALL", "O121", "SYN", "O121SYN", "CSACp", "HQ", "NONHQ"]
IDBINS = [(0.995, 1.01), (0.99, 0.995), (0.98, 0.99), (0.95, 0.98), (0.90, 0.95), (-1.0, 0.90)]
GO, GE = 11, 1

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
def nw_banded(a, b, B):
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


def protein_align(hcds, cseq):
    """Codon-level pairing from a protein alignment. Returns (chimp string in human codon frame with '---' for
    unpaired, per-human-codon BLOSUM score list (gap = -4), band flag 0/1/2, n chimp-only residues)."""
    ha, ca = translate(hcds), translate(cseq)
    B = 32 + abs(len(ha) - len(ca))
    pairs, hit = nw_banded(ha, ca, B)
    flag = 0
    if hit:
        pairs, hit = nw_banded(ha, ca, 4 * B)
        flag = 2 if hit else 1
    ncod = len(hcds) // 3
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
            out[i] = cseq[3 * j:3 * j + 3].upper()
            score[i] = B62.get((ha[i], ca[j]), -1)
    return "".join(out), score, flag, ins, gap_codons


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


def process(args):
    """One gene: returns dict(meta, arms={arm: stats}, excl={arm: stats}, gained, agree)."""
    r, human, segs, ot = args
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
    cu = chimp_ungapped(r, segs)
    cP, score, bflag, pins, pgap = protein_align(h, cu)
    arms["P"] = stats(h, cP)
    cPG = mask_codons(cP, neighbourhood(pgap, ncod))
    arms["PG"] = stats(h, cPG)
    cPF1 = mask_codons(cP, window_drop(score, 2, 1.0))
    arms["PF1"] = stats(h, cPF1)
    cPF2 = mask_codons(cP, window_drop(score, 1, 3.0))
    arms["PF2"] = stats(h, cPF2)
    strs = dict(UG=cUG, P=cP, PG=cPG, PF1=cPF1, PF2=cPF2)
    excl, gained = {}, {}
    for a, cx in strs.items():
        ex = list("-" * len(c0))
        ga = list("-" * len(c0))
        for i in range(ncod):
            u, x = c0[3 * i:3 * i + 3], cx[3 * i:3 * i + 3]
            if "-" not in u and "-" in x:
                ex[3 * i:3 * i + 3] = u
            if "-" in u and "-" not in x:
                ga[3 * i:3 * i + 3] = x
        excl[a] = stats(h, "".join(ex), extra=False)
        gained[a] = stats(h, "".join(ga), extra=False)
    both = same = 0
    for i in range(ncod):
        u, x = c0[3 * i:3 * i + 3], cP[3 * i:3 * i + 3]
        if "-" not in u and "-" not in x:
            both += 1
            same += (u.upper() == x.upper())
    for a, cx in noise_arms(h, c0, tid).items():
        arms[a] = stats(h, cx, extra=False)
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
                ident=g0["ident"], sets=sets, chimp_len=len(cu))
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


def band(res):
    A = res["arms"]
    g = lambda arm, st: (A.get(arm, {}).get(st) or {}).get("dnds", float("nan"))
    U, Uc, HQ = g("U0", "ALL"), g("U0", "CSACp"), g("U0", "HQ")
    D1 = U - g("PF1", "ALL")
    nf = (A["U0"]["ALL"] or {}).get("nonsyn_frac") or float("nan")
    if U >= 0.65 and nf >= 0.66 and D1 >= 0.25 and g("PF1", "ALL") <= 0.40:
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


def analyse(recs, out_prefix, l1b_json=None):
    res = dict(n_genes=len(recs), arms={}, excluded={}, gained={}, flags={}, idbins={}, diag={})
    bysets = {s: [x for x in recs if s in x["meta"]["sets"]] for s in SETS}
    for arm in ARMS + NOISE_ARMS:
        res["arms"][arm] = {s: (agg([x["arms"][arm] for x in xs]) if xs else None) for s, xs in bysets.items()}
    for arm in EXCL_ARMS:
        res["excluded"][arm] = {s: excl_agg([x["excl"][arm] for x in xs]) for s, xs in bysets.items() if xs}
        res["gained"][arm] = {s: excl_agg([x["gained"][arm] for x in xs]) for s, xs in bysets.items() if xs}
        u0c = sum(round((x["arms"]["U0"]["S"] + x["arms"]["U0"]["N"]) / 3.0) for x in recs)
        res["excluded"][arm]["ALL"]["share_of_U0_codons"] = res["excluded"][arm]["ALL"]["codons"] / u0c if u0c else None
        # where the excluded codons sit: identity of the genes holding them
        w = sorted(((x["meta"]["ident"] or 0.0, x["excl"][arm]["S"] + x["excl"][arm]["N"]) for x in recs))
        tot = sum(v for _, v in w)
        acc, med_id = 0.0, None
        for idn, v in w:
            acc += v
            if tot and acc >= tot / 2:
                med_id = idn
                break
        res["excluded"][arm]["ALL"]["weighted_median_gene_ident"] = med_id
        for s in ("ALL", "CSACp"):
            d = None
            if res["arms"][arm][s] and res["arms"]["U0"][s]:
                d = res["arms"]["U0"][s]["dnds"] - res["arms"][arm][s]["dnds"]
            res["flags"][f"{arm}_{s}"] = dict(drop=d, flag=flag(d))
    ids = sorted(x["meta"]["ident"] for x in recs if x["meta"]["ident"] is not None)
    res["diag"]["ident_median_ALL"] = ids[len(ids) // 2] if ids else None
    for lo, hi in IDBINS:
        xs = [x for x in recs if x["meta"]["ident"] is not None and lo <= x["meta"]["ident"] < hi]
        res["idbins"][f"{lo}-{hi}"] = dict(n=len(xs), U0=agg([x["arms"]["U0"] for x in xs]) if xs else None)
    m = [x["meta"] for x in recs]
    u0 = [x["arms"]["U0"] for x in recs]
    res["diag"].update(
        genes_frameshift=sum(1 for x in m if x["fs"] > 0), frameshift_runs=sum(x["fs"] for x in m),
        stop_h=sum(1 for g in u0 if g["stop_h"]), stop_c=sum(1 for g in u0 if g["stop_c"]),
        fail_S=sum(1 for g in u0 if not L1.FILTERS["S"](g)), fail_G=sum(1 for g in u0 if not L1.FILTERS["G"](g)),
        fail_L=sum(1 for g in u0 if not L1.FILTERS["L"](g)),
        fail_any_SGL=sum(1 for g in u0 if not all(L1.FILTERS[k](g) for k in "SGL")),
        band_hit_widened=sum(1 for x in m if x["band"] == 1), band_hit_final=sum(1 for x in m if x["band"] == 2),
        P_no_chimp=sum(1 for x in m if x["chimp_len"] < 3),
        agree_P_U0=(sum(x["agree_same"] for x in m) / sum(x["agree_both"] for x in m)) if m else None,
        set_sizes={s: len(xs) for s, xs in bysets.items()})
    # noise: rate r* reaching 0.80
    pts = [(0.0, res["arms"]["U0"]["ALL"]["dnds"])] + [(r, res["arms"][f"NR{r}"]["ALL"]["dnds"]) for r in NR_GRID]
    rstar = None
    for (r0, v0), (r1, v1) in zip(pts, pts[1:]):
        if v0 == v0 and v1 == v1 and v0 < 0.80 <= v1:
            rstar = r0 + (0.80 - v0) * (r1 - r0) / (v1 - v0)
            break
    res["diag"]["NR_rstar_080"] = rstar
    res["diag"]["U0_pS_ALL"] = res["arms"]["U0"]["ALL"].get("pS")
    if l1b_json and os.path.exists(l1b_json):
        lb = json.load(open(l1b_json))["variants"]["V0"]
        res["A0"] = {s: dict(l1b=lb.get(s, {}).get("dnds"), l1c=(res["arms"]["U0"].get(s) or {}).get("dnds"))
                     for s in ("ALL", "O121", "SYN")}
    res["band"] = band(res)
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    hdr = ["tid", "gene", "name", "L", "otype", "cov", "SYN", "fs", "ins", "band", "ident", "agree_both",
           "agree_same", "sets"]
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
    print("arm   set       n     pooled  p-ratio mean_c2 median  NdSd  nonsynF 1diffSh  N/S(NG) N/S(k4) dnds(k4) kappa^")
    for arm in ARMS + NOISE_ARMS:
        for s in SETS:
            d = res["arms"][arm].get(s)
            if not d or (arm in NOISE_ARMS and s != "ALL"):
                continue
            print(f"{arm:6s}{s:8s}{d['n']:6d}  {f(d.get('dnds'))}   {f(d.get('dnds_p'))}   {f(d.get('mean_ratio_cap2'))}"
                  f"   {f(d.get('median_ratio'))}  {f(d.get('NdSd_raw'))} {f(d.get('nonsyn_frac'))}   "
                  f"{f(d.get('single_nonsyn_share'))}    {f(d.get('NS_ratio'), 2)}    {f(d.get('NS_k4'), 2)}    "
                  f"{f(d.get('dnds_k4'))}    {f(d.get('kappa_hat'), 2)}")
    print("excluded vs U0 (ALL): arm codons share nonsynF dnds_p median_gene_ident | gained codons")
    for a in EXCL_ARMS:
        e, gn = res["excluded"][a]["ALL"], res["gained"][a]["ALL"]
        print(f"  {a:4s} {e['codons']:9d} {f(e.get('share_of_U0_codons'), 4)} {f(e['nonsyn_frac'])} {f(e['dnds_p'])} "
              f"{f(e.get('weighted_median_gene_ident'), 4)} | {gn['codons']}")
    print("mechanism flags:", json.dumps(res["flags"]))
    print("identity bins (U0):", {k: (v["n"], f((v["U0"] or {}).get("dnds"))) for k, v in res["idbins"].items()})
    print("diag:", json.dumps(res["diag"], default=float))
    if "A0" in res:
        print("A0 (L1b V0 vs L1c U0):", res["A0"])
    print("BAND:", res["band"])


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


def run(gff, orth, seg_path, out_prefix, workers="6", l1b_json=None):
    t0 = time.time()
    txs, counts = L1B.load_annotation(gff)
    print("annotation:", json.dumps(counts), flush=True)
    otype = L1B.load_orth(orth)
    recs = []
    with Pool(int(workers)) as pool:
        for k, x in enumerate(pool.imap(process, gen_tasks(txs, seg_path, otype), chunksize=8)):
            if x is not None:
                recs.append(x)
            if k % 2000 == 0:
                print(f"[{time.time() - t0:7.0f}s] genes {k}", flush=True)
    res = analyse(recs, out_prefix, l1b_json)
    res["annotation"] = counts
    res["seconds"] = time.time() - t0
    with open(out_prefix + ".json", "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    report(res)


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
    report(res)
    print("selftest ok", d)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "selftest":
        selftest()
    elif a and a[0] == "run" and len(a) in (5, 6, 7):
        run(*a[1:])
    elif len(a) == 2 and a[0] == "report":
        report(json.load(open(a[1])))
    else:
        print(__doc__)
