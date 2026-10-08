from gen import *

claim('A','mittens-formula','MITTENS rate-limit formula F_max = (t_div x d) / (g_len x G_f)','day','A','ROOT',
 [('supports','ROOT')],True,'firsthand','checked',('holds','n/a','contested'),
 q('F_max = (t_div × d) / (g_len × G_f) F_max = maximum achievable fixations t_div = divergence time (in years) g_len = generation length (in years) d = Selective Turnover Coefficient G_f = generations per fixation',
   '[Response to Dennis McCarthy, Round 2](https://voxday.net/2026/02/04/response-to-dennis-mccarthy-round-2/) (key B2026-02-04), blog, 2026-02-04, ¶10. Day introduces it as "the core equation that is integral to MITTENS". Zenodo texts (Z18441321, Z18452504) use the equivalent "Achievable = (Generations x d) / G_f". The 3.0 paper (Z23003785) uses 252,000 nominal generations / 1,322 with no d term (see A4d).')
 ,
 '''F_max = (t_div_years · d) / (generation_time_years · G_f)

Parameters (keys in `parameters.yaml`): `divergence.t_div_years`, `generation_time_years`, `selection.turnover_d`, `ltee.gens_per_fixation`. The claim compares F_max with the required count R (`divergence.required_fixations`, per lineage). Shortfall = R / F_max.

`derived:` (recomputed 2026-10-07, python3 -I; scratch script, not committed). Every headline number on the Day side, by version:

| Version | Inputs | F_max | Shortfall | Reconciles? |
|---|---|---|---|---|
| 2019 blog (B2019-02-07) | 9.0e6 y / 20 y = 450,000 gens; G_f = 1,600 | 450,000/1,600 = 281.25 (text says 562 = 2 x 281; table says 125) | 30e6 − 562 = 29,999,438 "short" (reconciles with 562) | **No.** 125 is not reproduced by the table's own inputs (9,000,000/32,000 = 281.25; 125 would need 4.0e6 y). 562 needs an unstated doubling. |
| 2025 (Z18165980) | 325,000 x 0.45 = 146,250 effective gens; G_f = 1,600 | 146,250/1,600 = 91.4 (paper rounds to 91) | 20e6/91 = 219,780 (paper: 219,780-fold); 20e6/91.4 = 218,803 | Yes (rounding of 91.4 to 91). |
| 3.0 (Z23003785) | 6.3e6/25 = 252,000 gens; G_f = 1,322; no d | 252,000/1,322 = 190.6 (paper: 191) | 205e6/190.6 = 1,075,437 (paper: 1,075,000) | Yes. |
| 3.0 SNV-only (s7.3) | R = 17.5e6 | 191 | 17.5e6/190.6 = 91,806 (paper: 91,600) | Yes (rounding). |
| Hössjer (HO-01) | 9e6 x 0.45 / (20 x 1,600) | 126.6 (he writes 127) | — | Yes. |
| Duffy (DU-02) / DeDzjang (DZ-02) | 252,000/1,400 | 180 | — | Yes. |
| Tree of Woe (TW-01) "202,500 generations" | 450,000 x 0.45 = 202,500 | — | — | Reconciles as 2019 gens x d (derived; the interview does not show it). |

Sensitivity (derived): over the t_div and g_len ranges in the sources (5.5 My/32.5 y = 169,231 gens to 9 My/20 y = 450,000 gens), N_gen varies by 2.7x. The shortfall claimed is 1e5 to 1e6. The input ranges for A1 therefore cannot by themselves close the gap.''',
 '''- Stated: G_f is a measured aggregate throughput that already includes parallelism and all mechanisms (see G1, A2); the LTEE rate is a ceiling for sexual mammals (A2e); R is a per-lineage count (A3).
- Implicit: G_f is constant in time and transfers between organisms with different genome size, mutation supply and recombination (A5). d, when used, is a constant multiplier on generations (A4). Linear scaling of fixations with generations: no depletion of standing variation and no change in selection regime.''',
 '''- Against: Hancock (GG-01) reads the formula as sequential (see G2). Critics argue the LTEE rate does not scale to humans (A5, A5a, A5b). Camestros (CA-07, CA-11): G_f is an average, not the fastest fixation rate (A2d). Camestros reviewed only the first edition (CA-14 "core argument hasn't changed since February 2019" is contradicted by the version drift, see A2b, A3a, A4d).
- In support: Camestros (CA-02): "Aside from whatever d is, the arithmetic itself isn’t wrong". Hössjer (HO-06): "I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli." Keruru (KR-09) endorses the thesis (LLM-assisted; advocacy).
- Weaknesses in the responses: Hössjer's residual ~2x gap (A5a) rests on putting d = 0.45 inside the neutral rate, which is not standard; without d the figure is 16.9M vs 20M. The KITTENS decomposition (A5b) assumes linear scaling of adaptive fixations with mutation supply and says so (RE-09). Camestros's "arithmetic isn't wrong" is a statement about the 2019-edition arithmetic, not about the 2026 numbers.''',
 LITH+'''| Good et al. 2017; Tenaillon et al. 2016 (source of G_f) | see A2, A2g | unverified (Good: the "≥95%" rule is not in the main text) |
| Yoo et al. 2025 (t_div, R) | see A1a, A3x1 | t_div accurate; 410 Mb not-found |''',
 '''No check has run on this claim as a whole. Component checks are linked from A1–A5.
- Under the claimant's model: F_max is an upper bound on fixations by selection; R/F_max >> 1 for any version (1e5 to 1e6).
- Under the opposing model: F_max is not an upper bound for a recombining genome with 38.4 new mutations per haploid genome per generation (versus 4.1e-4 for E. coli), so a forward simulation with human-scale supply and parallel sweeps will fix far more than F_max.
- Proposed check (A-sim, not run): Wright-Fisher forward simulation, N = 1e4 (scaled), L loci, per-generation beneficial supply U_b swept over 4.1e-4 x [1, 1e2, 1e4, 9.4e4] of the LTEE value, recombination off versus free; record fixations per generation. A prediction that would change a verdict: if fixations per generation grow roughly linearly in U_b with free recombination, the unscaled formula is not a ceiling (verdict external: contradicted); if it saturates near 1/1,322 regardless of U_b, the ceiling reading (A2e) gains support.''',
 'Script: none yet (arithmetic audit run in scratch only). Result: arithmetic reconciles for 2025 and 3.0; 2019 table (125) and text (562) do not reconcile with each other or with 281. Review: pending.',
 '- `t_div`, `g_len`, `G_f`, `d` as user-controllable inputs; displayed output F_max and shortfall R/F_max for each version preset (2019, 2025, 3.0).\n- Toggle: serial reading (T/latency) versus aggregate reading (T/G_f).',
 'ROOT is a conjunction over mechanisms; if branch A fails, selection is an admissible mechanism and ROOT fails.')

claim('A1','generations-available','Generations available since the split: about 252,000 (6.3 My at 25 y)','day','A','A',
 [('depends-on','A1a'),('depends-on','A1b')],False,'firsthand','checked',('holds','accurate','supported'),
 q('The divergence time is 6.3 million years. At 25 years per human generation, this provides 252,000 generations.',
   '[MITTENS 3.0, Zenodo 23003785](https://zenodo.org/records/23003785) (key Z23003785), 2026-09-28 (modified 2026-10-04), p.11 (s7.1).'),
 '''N_gen = t_div_years / generation_time_years = 6.3e6 / 25 = 252,000   (`divergence.t_div_years.day_2026_mittens3`, `generation_time_years.day_2026`, `generations_available.day_2026`)

`derived:` version history of the same quantity:

| Version | t_div | g_len | N_gen | Note |
|---|---|---|---|---|
| 2019 | 9.0e6 | 20 | 450,000 | B2019-02-07 |
| 2025 | 6–7e6 (6.5e6) | 20 | 300,000–350,000 (325,000) | Z18165980, Q12 |
| 2025 effective | — | — | 325,000 x 0.45 = 146,250 | with d (A4) |
| 2026 3.0 | 6.3e6 | 25 | 252,000 | Z23003785 |
| alt. | 6.3e6 | 32.5 | 193,846 | parameters.yaml `day_alt` (B2025-01-18, not re-verified here) |

All arithmetic reconciles. Range over the sources: 169,231 (5.5 My, 32.5 y) to 450,000 (9 My, 20 y), a factor of 2.7.''',
 '- Stated: 6.3 My divergence time and 25 y generation length.\n- Implicit: constant generation length over the whole lineage; t_div applies to the whole genome (population split later than the species split by an ancestral-coalescence term, which would add mutational time, not remove it; see A1a).',
 '''- Against: none engaged the 252,000 figure as an error. Keruru and Hössjer use 300,000 and 450,000 in their own recalculations (KR-08, HO-04), i.e. more generations, not fewer.
- In support: Duffy and DeDzjang both recompute 6.3e6/25 = 252,000 (DZ-02).
- Weaknesses in the responses: Day's own later statement (2026-05-07) moves the CHLCA to 250 kya–1.3 Mya, which is incompatible with 6.3 My; see A1c. Day's 2019 value (9 My, 20 y) is not a "generous" choice relative to the current 6.3 My, since it gives 1.8x more generations.''',
 LITH+'''| Yoo et al. 2025 | "Our analyses dated the human-chimpanzee split between 5.5 and 6.3 million years ago" | verified-accurate (see ledger) |
| Langergraber et al. 2012 | "We date the human-chimpanzee split to at least 7-8 million years" | verified-misread when cited for 6–7 My |''',
 '''No check yet. The result is arithmetic and is already recorded above.
- Under the claimant's model: 252,000 generations.
- Under the opposing model: 220,000–450,000 depending on source; conclusions insensitive to the factor of 2.7.
- Result that would change a verdict: a sourced g_len for the ancestral hominin lineage substantially above 32.5 y.''',
 'Arithmetic audit (python3 -I, scratch): all rows reconcile. Review: pending.',
 '- `t_div_years` (5.5e6 to 9e6), `generation_time_years` (20 to 32.5), derived `N_gen`.')

claim('A1a','divergence-time-literature','Independent dating of the human-chimp split: 5.5–6.3 My (Yoo), at least 7–8 My (Langergraber), about 6 My (Scally)','literature','A','A1',
 [('supports','A1')],False,'firsthand','extracted',('n/a','partial','supported'),
 '''> Our analyses dated the human-chimpanzee split between 5.5 and 6.3 million years ago (Ma; minimum to maximum estimate of divergence)

Source: Yoo et al. 2025 (key Yoo2025), main text, "Divergence and selection".

> We date the human-chimpanzee split to at least 7-8 million years and the population split between Neanderthals and modern humans to 400,000-800,000 y ago.

Source: Langergraber et al. 2012 (key Langergraber2012), Abstract.

> We propose a synthesis of genetic and fossil evidence consistent with placing the human-chimpanzee and human-chimpanzee-gorilla speciation events at approximately 6 and 10 million years ago (Mya).

Source: Scally et al. 2012 (key Scally2012), Abstract.
''',
 '''Literature values for `divergence.t_div_years`: yoo_2025 [5.5e6, 6.3e6] (verified), langergraber_2012 ">=7e6-8e6" (verified), Scally ~6e6. Day 2026 uses 6.3e6 (the Yoo maximum); Day's earlier papers cite Langergraber for 6–7 My.''',
 '- Stated by the papers: each uses its own calibration. Langergraber states independence from fossil calibration.\n- Implicit: molecular dates depend on mutation-rate calibration, which Hössjer (HO-05) and McCarthy (MC-12) say is partly neutral-theory based (branch B4, circularity).',
 '''- Against (Day side): the molecular-clock recalibration claims (B4) put the CHLCA at 200–580 kya, 68 kya, or 250 kya–1.3 Mya (see A1c).
- In support: Hössjer and McCarthy both treat the date as circular in the sense that it uses a neutral rate (B4); this affects Day's use of the date and the critics' use of neutral rates symmetrically.
- Weaknesses in the responses: neither HO-05 nor MC-12 gives a citation; the ledger notes pedigree rates are independent of divergence data.''',
 LITH+'''| Yoo2025 | 5.5–6.3 My | verified-accurate |
| Langergraber2012 | ">=7–8 My", independent of fossil calibration | verified; Day's use as 6–7 My is a misread |
| Scally2012 | about 6 My | verified (abstract) |''',
 'No check needed; descriptive.\n- Prediction: a sensitivity of the shortfall to t_div in [5.5, 8] My changes the shortfall by a factor <= 1.5 (derived: 8/5.5 = 1.45).',
 'No script. Review: pending.',
 '- Preset list of t_div values with citation keys.')

claim('A1b','generation-length-literature','Generation length: chimpanzee about 24–25 y; Day uses 20 y (2019) and 25 y (2026)','literature','A','A1',
 [('supports','A1')],False,'firsthand','extracted',('n/a','accurate','supported'),
 '''> The average generation time for the former communities was 24.9, whereas it was 24.3 for the latter.

Source: Langergraber et al. 2012 (key Langergraber2012), Results (chimpanzee generation time). The two groups are chimpanzee communities with and without high infection-induced mortality.

Day, secondhand within his own Q&A, uses another figure: "T = 22 years (generation, Gurven & Kaplan 2007)" ([Probability Zero Q&A](https://voxday.net/2026/01/19/probability-zero-qa/), 2026-01-19, ¶5).
''',
 '`generation_time_years`: day_2019 = 20, day_2026 = 25, day_alt = 32.5, Q&A = 22; Langergraber: 24.3–24.9 (chimpanzee). `derived:` 6.3e6/24.9 = 253,012; 6.3e6/20 = 315,000; 6.3e6/32.5 = 193,846.',
 '- Stated: generation length averaged over the lineage.\n- Implicit: the same g_len for the human and chimp branches and for the ancestor.',
 '''- Against: none in corpus.
- In support: the 25 y value agrees with the chimpanzee measurement (24.3–24.9).
- Weaknesses: only chimpanzee data in the repo; no sourced figure for the human lineage or ancestors, and Day's 32.5 y alternative is unquoted here.''',
 LITH+'''| Langergraber2012 | 24.9 / 24.3 y for chimpanzee communities | verified |''',
 'No check needed. Prediction: no plausible g_len moves N_gen outside 190,000–320,000 (derived).',
 'No script.', '- `generation_time_years` input.')

claim('A1c','chlca-revision-vs-63my','Day later places the CHLCA at 250 kya–1.3 Mya, while MITTENS 3.0 (Sept 2026) uses 6.3 My','day','A','A1',
 [('revises','A1'),('depends-on','B4')],False,'firsthand','checked',('pending','n/a','pending'),
 q('the CHLCA event falls somewhere in the 250 kya to 1.3 Mya range rather than the 6.3 Mya presently assumed. But it cannot be as recent as the lower end of the 68 kya to 330 kya range',
   '[A Retraction and a Revision](https://voxday.net/2026/05/07/a-retraction-and-a-revision/) (key B2026-05-07), blog, 2026-05-07, ¶7.'),
 '''t_CHLCA ∈ [2.5e5, 1.3e6] y (2026-05-07)  versus  t_div = 6.3e6 y (Z23003785, 2026-09-28).

`derived:` generations at 25 y: 250 kya/25 = 10,000; 1.3 My/25 = 52,000; 6.3 My/25 = 252,000. At G_f = 1,322 the achievable count is 7.6 to 39 fixations (10,000/1,322 to 52,000/1,322) under the May dating, versus 191 under the Sept dating. The version drift ledger records the chain 6.3–9 My → 200–580 kya → 68 kya → 250 kya–1.3 Mya.''',
 '- Stated: the statement is about the CHLCA date in the framework of the k ≠ μ claim (B3, B4).\n- Implicit: a molecular-clock recalibration (B4) moves the date but the MITTENS 3.0 text keeps the conventional 6.3 My.',
 '''- Against: none engaged this internal tension in the corpus.
- In support: Day could argue that the 3.0 paper uses the conventional date deliberately, as the most favourable case for the standard model ("generous" framing in Z23003785 s8.5/8.6).
- Weaknesses: the retraction post is about Term 3 (Haldane cost); the date change is a side statement. No text in the corpus reconciles the two dates.''',
 NOLIT,
 '''Not testable by simulation; it is a consistency question.
- Prediction: if the 250 kya–1.3 Mya dating were used in the 3.0 formula, the achievable count falls by 5x to 25x and the shortfall rises correspondingly. If the 6.3 My date is used, any argument for a recent CHLCA is not part of MITTENS 3.0.''',
 'Arithmetic only (above). Review: pending.', '- Preset for alternative CHLCA dates.')
