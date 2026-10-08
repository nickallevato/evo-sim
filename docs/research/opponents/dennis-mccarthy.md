# Dennis McCarthy (Substack "All The Mysteries That Remain")

- **Side:** critic
- **Role:** Public-facing rebuttal of the first-edition fixation arithmetic and the Darwillion; also argues for evolution generally (biogeography, speciation, fossils).
- **Stated credentials (as self-described or as introduced; unverified here):** Says he has "published multiple peer-reviewed papers on evolution and biogeography" and a 2009 OUP book (MC-13). No population-genetics credential claimed.
- **Sources (see `sources/bib-critics.md`):** MC-1, MC-1p, MC-2, MC-2p, MC-3..MC-6, MC-arch

## Arguments mapped to branches
(Branch IDs from `hierarchy.yaml`. Quote IDs are in `sources/quotes-critics.md`.)

| Branch | Argument | Quote refs |
|---|---|---|
| G3 (also D) | (1/20,000)^20,000,000 prices one pre-specified list of 20M mutations; history needs any 20M of a huge pool | MC-01, MC-02 |
| B5 | Using Day's inputs: 50,000 new mutations/yr x 9 My = 450 billion; x 1/20,000 = 22.5 million fixed (about the 20M observed) | MC-03, MC-04 |
| B1 | Time-adjusted version: only mutations older than 4Ne=40,000 gens count -> 400 billion x 1/20,000 = 20M | MC-09 |
| F / G2 | Fixations do not queue; many alleles sweep at once | MC-08 |
| A5 | E. coli genome ~690x smaller than human; 60-100 de novo mutations per newborn vs ~1 per 1,000-2,400 E. coli divisions | MC-05, MC-06, MC-07 |
| B2 | Day's "3x more harmful than neutral" applies to coding DNA only; genome-wide only 3% deleterious | MC-10 |
| A3x | 410 Mb = structural variation; one event can alter millions of bp | MC-11 |
| B4 | Divergence dates are themselves derived using neutral theory | MC-12 |

## Weaknesses noted (own math / inputs / reading of Day)
- Uses N = Ne = 10,000 for both mutation supply and fixation probability, i.e. assumes N/Ne = 1. That is exactly what B3 (k = mu N/Ne) disputes, so the arithmetic answers Day only if N = Ne.
- All 450 billion mutations are treated as fixation-eligible at 1/20,000 (neutral). The 3% deleterious figure (MC-10) is uncited. A 20M result then depends on ~100% of mutations being effectively neutral; with a neutral fraction f the expectation scales to f x 22.5M.
- Expected value only; derived: Poisson sd for mean 22.5M is ~4.7 thousand, so variance is immaterial for this particular claim.
- The "60 to 100 de novo mutations" and "dates are based on Kimura theory" statements carry no citation in the post. The second is at least partly contested (fossil and pedigree calibrations exist; see Langergraber in fidelity ledger).
- Targets the first-edition Darwillion. Day later calls the Darwillion "a rhetorical device" (PLAN.md; not re-verified here), so the rebuttal does not touch MITTENS 3.0 (1,322 gens/fixation, 205M).
- Paid posts (2026-01-26, 02-03) are known only as previews; the free reposts (2026-09) may have been edited since.

## Strongest technical point
The "specific vs any 20M" correction plus the expected-count calculation (MC-03/MC-04) is the cleanest critique of Darwillion and needs only Day's own inputs.

## Unknown / not checked
Whether the 2026-09 free text differs from the 2026-01 paid original.
