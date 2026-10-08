from common import *
RV2='`research/checks/REVIEW.md#2026-10-07--correctness-review-2-sonnet-on-b0b3`'

add(id='B6',slug='ancestral-pipeline-full-mansfield',title='Mansfield: the ancestral pipeline was full at the split; expected divergence ≈ 2 mu T + theta_anc',side='critic',branch='B',parent='B1',
 edges=[('attacks','B1'),('attacks','B1a')],lb=(True,'if true, the empty-start premise of B1 fails for the human-chimp case'),
 sourcing='firsthand',status='extracted',v=('holds','n/a','pending'),
 quotes=[Q('MFC','The ‘pipeline’ would have been full from the X generations preceding that point in time.','comment UgyhNduYke46IStQ5pd4AaABAg.AbQefbrLxzSAbRHJx-mRP2 (Mansfield)'),
   Q('CSAC','The differences between one copy of the human genome and one copy of the chimpanzee genome include both the sites of fixed divergence between the species and some polymorphic sites within each species.','Main text, "Nucleotide divergence"')],
 formal='''E[d] = 2μT + θ_anc, θ_anc = 4Nₑ,anc μ per site (B4a). Equilibrium start: expected fixed substitutions = μLT (RESULTS B1, P2). The hierarchy attributes the formula to Mansfield and the sources agent; the verbatim Mansfield text is the full-pipe statement only.
Derived illustration: see B4a (Nₑ,anc = 1.0e4 → 0.65%; 1.32e5 → 1.24%; 1.98e5 → 1.56% vs 1.23% observed, μ = 1.2e-8, T = 252,000).''',
 a_stated='A population at equilibrium before the split has a full pipe.',a_impl='Ancestral population at constant size ≥ 4Nₑ,anc (≥ 5.3–7.9×10⁵ generations per Yoo Nₑ,anc) before the split; no demographic upheaval resets the pipe.',
 against='Day (EDU, quoted in B1c): the pipeline is "functionally nonexistent" — later "The pipeline was full, but it was much shorter" (B1d).',support='RESULTS B1: the equilibrium-start simulation gives U·T; Day\'s later concession (B1d).',
 weak='Mansfield gives no ancestral Nₑ, no number, and states it as an assumption; Day\'s reading of it as "it gets reset somehow" is his paraphrase (secondhand).',
 lit=[lit_row('Yoo 2025','Nₑ,anc 198,000 (HCB), 132,000 (HCG)','verified'),
      lit_row('Chimpanzee Sequencing and Analysis Consortium 2005','polymorphism 14–22% of observed divergence','verified')],
 prereg_note='Pre-registered prediction (copied from RESULTS B1; the check has run).',
 p_claim='(Critic) equilibrium start: simulated count = U·T.',p_opp='(Day) empty start: count = U∫F_X ≈ U(T − 4N).',p_change='B1c, B4a.',
 check='Script: `research/checks/b1_start_state.py` (seed 11) · Result: equilibrium start N=100, U=0.5: T=400: 198.5±2.0 vs U·T = 200; T=2000: 1005.1±4.3 vs 1000; empty start: 41.3±0.8 and 802.5±3.4. Review: '+RV2,
 sim=['start state','ancestral Nₑ','θ_anc term shown separately'])

add(id='B6a',slug='day-ancestral-polymorphism-rounding-error',title='Day (IR): ancestral polymorphism contributes 1.44 million differences (0.35%), "a rounding error"',side='day',branch='B',parent='B6',
 edges=[('attacks','B6')],lb=(False,'dismisses the ancestral-polymorphism objection; the B1 deficit is stated net of it'),
 sourcing='firsthand',status='reviewed',v=('arithmetic-error','n/a','contested'),
 quotes=[Q('IR','At Nₑ = 10,000 and μ = 1.2 × 10⁻⁸, this yields approximately 1.44 million differences across the genome, less than half of the 2.4 million fixations the empty-pipe correction removes from the naive prediction. The net adjustment still reduces the expected count.','p.3 (§3)'),
   Q('IR','The ancestral polymorphism objection is not merely trivial. It is a rounding error.','p.3 (§3)')],
 formal='''**Arithmetic audit (derived, python3 -I):** 4 × 10⁴ × 1.2×10⁻⁸ × 3×10⁹ = 1.44×10⁶ ✓; 1.44M/410M = 0.351% ✓ ("0.35%"). The empty-pipe removal in IR's own table at Nₑ = 10⁴ is 30 × 40,000 = 1.2M (loss 15.9%), not 2.4M. 1.44M/1.2M = 1.2 (θ exceeds the removal); 1.44M/2.4M = 0.6, not "less than half". So on IR's own numbers the sign of "the net adjustment still reduces the expected count" reverses (+1.44M − 1.2M = +0.24M). If 2.4M is two lineages × 1.2M, the comparison should use the pairwise count 2μT·L (15.1M) plus θ, not the per-lineage figure.
Comparator: 410M mixes events and bp (A3x); against SNV-only 35M the term is 4.1%. At Yoo ancestral Nₑ (1.32×10⁵ / 1.98×10⁵): θ·L (L = 3.2e9) = 20.3M / 30.4M, i.e. 58% / 87% of 35M (derived; B4a).''',
 a_stated='Nₑ = 10⁴, μ = 1.2e-8, genome 3×10⁹.',a_impl='Nₑ,anc equals the modern human Nₑ (the glossary flags using modern Nₑ for the ancestral population as a common confusion); comparator is the 410M count.',
 against='Camestros (B6b), Mansfield (B6), Yoo 2025 Nₑ,anc, CSAC 14–22%.',support='None independent; Hössjer does not address it.',weak='The critics\' side has not computed the θ term from Yoo\'s Nₑ in print; this file\'s derivation is the first in the corpus and still unchecked by simulation (B4a).',
 lit=[lit_row('Yoo 2025','ancestral Nₑ 132,000–198,000','verified'),
      lit_row('Chimpanzee Sequencing and Analysis Consortium 2005','t2 "may be on the order of 1-2 million years"','verified')],
 p_claim='θ_anc ≈ 0.35% of divergence.',p_opp='θ_anc is 58–87% of the SNV total at Yoo Nₑ,anc.',p_change='B4a.',check='Script: none (arithmetic); proposed B4a.',sim=['Nₑ,anc','θ term'])

add(id='B6b',slug='camestros-all-differences-post-split',title='Camestros: Day treats ALL human-chimp genetic differences as mutations that occurred after the split',side='critic',branch='B',parent='B6',
 edges=[('attacks','B6a')],lb=(False,'first-edition critique; quantified here only through CSAC\'s 14–22%'),
 sourcing='firsthand',status='extracted',v=('holds','accurate','pending'),
 quotes=[Q('CF2','So Day is treating ALL the genetic differences between chimps and humans as mutations that initially only occurred after the point of divergence of the two species.','para 46 (Camestros; first edition)'),
   Q('MAX','it requires a minimum of 15,000,000 mutations to become fixed in the human population, and another 15,000,000 mutations to become fixed in the chimpanzee population',file='day/blog-2019-02-07-maximal-mutations.txt',note='Day, first-edition basis (Q05 in the harvest)')],
 formal='''Day 2019 (second quote above) splits the whole 30M between lineages as post-split fixations. Quantification (derived): if polymorphism is 14–22% of observed SNV divergence (CSAC), the fixed fraction is 0.78–0.86; 35M × (0.78–0.86) = 27.3–30.1M fixed SNVs, 13.7–15.1M per lineage vs 17.5M used in Z23003785 (derived).''',
 a_stated='Day counts all differences as post-split fixations.',a_impl='The 40M/35M count is of fixed differences.',against='Day (B6a).',support='CSAC text.',
 weak='Camestros reviewed the first edition only and writes "ALL" without a figure; the second edition and Z23003785 use SNV 35M with apportioning (17.5M) and do not subtract polymorphism.',
 lit=[lit_row('Chimpanzee Sequencing and Analysis Consortium 2005','"we estimate that polymorphism accounts for 14-22% of the observed divergence rate"','verified')],
 p_claim='Some of the counted differences predate the split.',p_opp='(Day) rounding error (B6a).',p_change='B4a.',check='Script: proposed B4a.',sim=['polymorphic fraction of divergence'])

add(id='B6c',slug='hancock-no-standing-variation-prediction',title='Hancock: a serial one-at-a-time model predicts no genetic variation among individuals except the sweeping allele',side='critic',branch='B',parent='B6',
 edges=[('attacks','B1'),('attacks','G1')],lb=(False,'an empirical-consequence argument; not quantified on screen'),
 sourcing='firsthand',status='extracted',v=('pending','n/a','pending'),
 quotes=[Q('GG','there would basically be no genetic variation amongst individuals except for the mutation that\'s increasing in frequency','t=01:33:59 (auto-caption)'),
   Q('GG','it assumes that each mutation has to both arise and go to fixation before the next','t=01:31:58 (continues "mutation can occur." in the 01:32:18 chunk; Hancock responds to the 180-interval, 252,000/1,400 presentation; the attribution to Day\'s own equation is tested in F1a)')],
 formal='''Under strictly serial fixation (one allele at a time), heterozygosity would be ≈ 0 except at the single segregating site. Observed neutral diversity: θ = 4Nₑμ ≈ 4.8×10⁻⁴ per site at Nₑ = 10⁴, μ = 1.2×10⁻⁸ (derived), i.e. ≈ 1.5×10⁶ segregating differences per genome pair at 3.2×10⁹ sites. Day does not claim a serial model for neutral fixation (B2d: "Fixations run in parallel" is conceded), so the prediction applies to the reading in F1, not to Day\'s stated position.''',
 a_stated='MITTENS encodes sequential fixation.',a_impl='F_max = t/(g G_f) is a serial-throughput bound.',against='Day (EDU): G_f is a throughput measurement that already includes parallelism (F1a).',support='Observed standing variation (π > 0).',
 weak='The attribution rests on Hancock\'s reading; Day\'s Q&A computes 19,800 "generations per fixation" from a latency formula (F1a), which supports the serial reading for that figure.',
 lit=[],p_claim='(Hancock) serial model predicts no standing variation.',p_opp='(Day) not a serial model.',p_change='F1a quote analysis.',check='Script: none.',sim=['standing variation display','serial vs parallel throughput mode'])
