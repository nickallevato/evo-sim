import sys; sys.path.insert(0,os.environ.get("EVO_WORK","work")+"")
from gen_lib import *
NB="n/a"
# ROOT-B book blurb
qb=ex('book',"Day demonstrates that the Modern Synthesis isn't just flawed-it is absolutely impossible.")
write('ROOT-b-book-blurb-absolutely-impossible','ROOT-B','Probability Zero sales copy: the Modern Synthesis is "absolutely impossible"','day','ROOT','ROOT',
 "[{type: supports, target: ROOT}]",'false','marketing wording of ROOT; ROOT is stated in the papers independently','firsthand',
 'n/a','promotional text, no argument','n/a','no source cited','pending','same as ROOT',
 qb+"\n\nSource: Probability Zero hardcover product page on the publisher's store (ndmexpress.com, `sources/raw/day/book/ndm-probability-zero.html`, bib-day K-PZ-hc; retrieved 2026-10-07; authorship of the blurb not stated on the page, so attribution to Day himself is unverified). Locator: product description, first paragraph block.",
 "Same logical form as ROOT: the Modern Synthesis (selection + drift + mutation + recombination + population structure) cannot generate observed divergence. 'Absolutely impossible' is stronger than ROOT's 'in the available time': it drops the time qualifier.",
 "- Stated: 'the pitiless light of statistical and mathematical analysis' of Darwin, Haldane, Mayr, Kimura and Dawkins.\n- Implicit: the 'man walked from New York City to Los Angeles in under five minutes' analogy (same page) treats the shortfall as an order-of-magnitude impossibility, not a probability.",
 "- Against: critics who read only the book's blurb (none located). Jan 2026 reviews (Camestros, Myers) address chapters, not the blurb.\n- In support: n/a.\n- Weaknesses: marketing copy; do not weight as an argument. Recorded so that the 'impossible' vs 'in the available time' wording difference is on file.",
 "| Cited work | What it actually says | Fidelity |\n|---|---|---|\n| none cited | | n/a |",
 "Not applicable (wording claim). Prediction for the ROOT file applies.","None.","None.")

# ROOT-K Keen
k1=ex('qc',"The reason it fails, as Vox Day and Claude Athos show in this book, is time.")
k5=ex('qc',"is orders of magnitude greater than the age of the Universe, let alone the age of the Earth.")
write('ROOT-k-keen-time-is-the-reason','ROOT-K','Steve Keen: the Blind Watchmaker hypothesis fails because of time; the required time exceeds the age of the Universe','ally','ROOT','ROOT',
 "[{type: supports, target: ROOT}]",'false','an endorsement; ROOT does not depend on Keen','firsthand',
 'pending','Keen gives no equations; his figure depends on ROOT/A inputs','partial','endorses The Frozen Gene, not the MITTENS papers; scope differs','contested','checked arithmetic only reaches the claim if the bacterial rate is a fixed ceiling',
 k1+"\n\nSource: Steve Keen, [Natura Facit Saltum](https://profstevekeen.substack.com/p/natura-facit-saltum) (preface to The Frozen Gene), 2026-02-03, para 7 (quotes-critics KE-01).\n\n"+k5+"\n\nSource: same, para 7 (KE-05). The sentence's subject is truncated in the extracted quote; the full sentence is in the source.",
 "Keen's claim: `T_required >> T_universe`. Under MITTENS 3.0 numbers: `T_required = T_div * shortfall = 6.3e6 y * 1.075e6 = 6.77e12 y` (derived; parameters.yaml `divergence.t_div_years.day_2026_mittens3`, `shortfall.mittens3_full`); `6.77e12 / 1.38e10 = 491` universe-ages. Recomputed. 'Orders of magnitude greater' holds (2.7 orders) only if the shortfall is read as a time multiplier at a fixed per-fixation rate. For the older 220,000x shortfall: 6.3e6 * 2.2e5 = 1.4e12 y (100 universe-ages).",
 "- Stated: the Frozen Gene's statistical implications of the 'Blind Watchmaker' hypothesis.\n- Implicit: a Lamarckian/quantum mechanism (McFadden 2001; Schwartz 2000, per the note in quotes-critics) is the preferred alternative; the preface has no equations. Keen's references to 'time' rely on the book, not the preface.",
 "- Against: the A5/A3x/B7 findings on inputs undermine the 491-universe-ages figure at its source (205M counts bp of SVs; Kimura 1962 gives 1/2N).\n- In support: none beyond Day's papers.\n- Weaknesses: Keen's endorsement is of The Frozen Gene; it is not evidence about Probability Zero's calculations. Credentials (economics PhD, evolutionary programming) self-described.",
 "| Cited work | What it actually says | Fidelity |\n|---|---|---|\n| McFadden 2001; Schwartz 2000 | not retrieved | unverified |",
 "Written before the (arithmetic-only) check. Under the claimant: 6.3e6*1.075e6/1.38e10 >> 1. Under the opposing model: the shortfall figure is a bound on a fixed-ceiling rate model only; with validated scaling (A5) and SNV-only counts (A3x) the time multiplier falls to ~10-10^2, i.e. well below universe-ages. A verdict changes if the A-branch checks establish the SNV-only, scaled shortfall.",
 "`python3 -I -c \"print(6.3e6*1.075e6, 6.3e6*1.075e6/1.38e10)\"` -> 6.7725e12, 490.8. Reconciles with the note in quotes-critics (KE-05).","T_div, shortfall factor (A), age of Universe as comparator; no simulator variables of its own.")

# ROOT-T Tipler
t1=ex('qc',"describes it as “the most rigorous mathematical challenge to Neo-Darwinian theory ever published.”")
t3=ex('qc',"Tipler gave it a glowing endorsement and also contributed an appendix to the book.")
write('ROOT-t-tipler-endorsement','ROOT-T','Frank Tipler: Probability Zero is the most rigorous mathematical challenge to Neo-Darwinian theory ever published','ally','ROOT','ROOT',
 "[{type: supports, target: ROOT}]",'false','an endorsement; carries no calculation','secondhand',
 'n/a','no argument given in the retrieved sources','unverifiable','Tipler\'s own foreword/appendix not retrieved','untestable','a superlative judgement about the literature',
 t1+"\n\nSource: Tree of Woe interview, [Why is the Probability Zero?](https://treeofwoe.substack.com/p/why-is-the-probability-zero), 2026-01-08, para 1 (quotes-critics TI-01; `secondhand`: the interviewer's paraphrase of Tipler's foreword, ending in a quoted phrase).\n\n"+t3+"\n\nSource: Dembski, [Vox Day Interview on Evolutionary Theory](https://billdembski.substack.com/p/vox-day-interview-on-evolutionary), 2026-09-28, para 2 (TI-03; `secondhand` for the foreword content).",
 "No formal content. A ranking claim: rigor(PZ) > rigor(all other published mathematical challenges to neo-Darwinism).",
 "- Stated: Tipler contributed a foreword/introduction and an appendix (also TI-02, Day via Myers).\n- Implicit: Tipler's own mathematical work (not retrieved here) is the standard of rigor.",
 "- Against: Myers (PZ-02) notes there was no peer review (process point, not math); no critic addresses Tipler's appendix.\n- In support: n/a.\n- Weaknesses: the foreword and appendix are in the paywalled book; contents unknown. A superlative cannot be checked without a comparison set.",
 "| Cited work | What it actually says | Fidelity |\n|---|---|---|\n| Tipler foreword/appendix | not retrieved | unverifiable |",
 "None (no checkable content). Recorded so the appendix can be extracted if the book is later accessed.","None.","None.")

# ROOT-H Hossjer
h6=ex('qc',"I agree with this conclusion, also after adjusting the MITTENS equation for the different mutation rates of humans and E. coli.")
h7=ex('qc',"Note that his positive remarks apply to Vox Day’s main argument, not to the book as a whole.")
h10=ex('qc',"I rather advocate uncommon descent between the two species.")
h2=ex('qc',"which still is less than 20 million, but only by a factor of 2.")
write('ROOT-h-hossjer-agrees-with-main-argument','ROOT-H','Ola Hossjer: agrees with Day\'s conclusion after rescaling, but advocates "uncommon descent" and limits the endorsement to the main argument','ally','ROOT','ROOT',
 "[{type: supports, target: ROOT},{type: revises, target: A5}]",'false','Hossjer\'s agreement is conditional on the Haldane step (H), which he asserts without calculation','firsthand',
 'pending','his rescaled gap is ~2x; the further step to ROOT relies on an uncomputed cost-of-selection argument (HO-03)','n/a','the quotes are Hossjer\'s own words in a reviewed PDF/Substack post; fidelity applies to his reading of Day, covered in branch A5','contested','depends on H and A5 checks',
 h6+"\n\nSource: Hossjer, [MITTENS - Convincing Arguments Against Neo-Darwinism](https://billdembski.substack.com/api/v1/file/f5a8533e-7b7c-407b-880b-1ecbd256784c.pdf) (PDF), 2026-09-14, p.3 (quotes-critics HO-06).\n\n"+h2+"\n\nSource: same, p.3 (HO-02): the rescaled upper bound (~10 million) is within 2x of the 20 million required.\n\n"+h10+"\n\nSource: Dembski Substack, [A Review of Vox Day's Main Argument in PROBABILITY ZERO](https://billdembski.substack.com/p/a-review-of-vox-days-main-argument), 2026-09-14, para 75 (HO-10).\n\n"+h7+"\n\nSource: same, para 34 (HO-07); text by Dembski, not Hossjer.",
 "Hossjer's chain: `F_max(127) -> x(1.25e-8/1e-10) = 15,800 -> x(3e9/4.6e6) = ~1.0e7` vs 2.0e7 required; then the Haldane cost step (HO-03) is said to cut the adaptive share (asserted, not computed). Neutral version: `F = L*d*mu*t = 3e9*0.45*1.25e-8*450,000 = 7.6e6` (HO-04). Recomputed: 15,800*(3e9/4.6e6) = 1.03e7; 3e9*0.45*1.25e-8*4.5e5 = 7.59e6; without d: 1.69e7 (balance ledger).",
 "- Stated: he agrees with Day's conclusion about natural selection; both calcs assume parallel fixation between loci; common descent is not needed for his view (uncommon descent).\n- Implicit: d = 0.45 applies inside the neutral rate (an input choice that creates the 2.2x gap); the cost step reduces adaptive fixations (HO-03).",
 "- Against: the Day-side numbers collapse from ~10^6 to ~2 after rescaling, per Hossjer himself (concedes most of A5; balance ledger).\n- In support: Day's own response to Dembski's question (DE-01) says the scaling element 'doesn't apply at all' without equations (opponents/bill-dembski.md).\n- Weaknesses: the agreement 'also after adjusting' and the 2x gap are in tension in the same review; the sentence 'I agree with this conclusion' refers to the pre-scaling bound. Endorsement does not extend to the book (HO-07).",
 "| Cited work | What it actually says | Fidelity |\n|---|---|---|\n| Haldane 1957 (via Nunney 2003) | ~1 substitution per 300 generations; Nunney 2003: cost 'substantially less', soft selection 'eliminates' it | verified via Nunney only (ledger) |",
 "Written before the arithmetic check. Under the claimant: Hossjer's rescaled bound reproduces to 2 sig figs. Under the opposing model: any inclusion of d in a neutral rate is non-standard (k = mu per generation) and removing it makes the neutral figure 1.7e7, i.e. 0.85 of required (no gap). Result that would change a verdict: a computed cost-of-selection bound (H) that cuts adaptive substitutions by >10x while the neutral share stays small.",
 "Arithmetic: `python3 -I -c \"print(15800*3e9/4.6e6, 3e9*0.45*1.25e-8*450000, 3e9*1.25e-8*450000)\"` -> 1.03e7, 7.59e6, 1.69e7. Reconciles with HO-01/02/04 notes.",
 "mu_human vs mu_E.coli, genome length scaling, d (turnover) placement, parallel-fixation switch, cost-of-selection (hard vs soft selection) switch.")

# ROOT-DE Dembski
d3=ex('qc',"As an intelligent design proponent, I have my own arguments for thinking that evolutionary mechanisms face serious explanatory shortfalls.")
d1=ex('qc',"Why does that result not bypass the fixation bottleneck MITTENS identifies?")
write('ROOT-de-dembski-own-arguments','ROOT-DE','Bill Dembski: has independent arguments that evolutionary mechanisms face serious explanatory shortfalls; presses Day on k=mu and scaling','ally','ROOT','ROOT',
 "[{type: supports, target: ROOT},{type: depends-on, target: B5}]",'false','host framing and questions; no calculation','firsthand',
 'n/a','no calculation given','n/a','host/interviewer role','untestable','a statement of position',
 d3+"\n\nSource: Dembski Substack, [Vox Day Interview on Evolutionary Theory](https://billdembski.substack.com/p/vox-day-interview-on-evolutionary), 2026-09-28, para 3 (DE-03).\n\n"+d1+"\n\nSource: same, para 63 (DE-02), a question put to Day about k = mu (branch B5).",
 "None. A position statement plus a question.",
 "- Stated: ID proponent; has 'own arguments'.\n- Implicit: that ROOT and ID are compatible but distinct (Hossjer, a Dembski guest, advocates 'uncommon descent').",
 "- Against: none.\n- In support: his question DE-02 is the best compact statement of the B5 objection from an ally.\n- Weaknesses: Dembski's own earlier critique of Rosenhouse ('Jason Rosenhouse's Whoppers') is linked by Day but was not retrieved (see D13).",
 "| Cited work | What it actually says | Fidelity |\n|---|---|---|\n| none | | n/a |",
 "None.","None.","None.")
