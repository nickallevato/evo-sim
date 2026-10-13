# Pre-run notes for L1b and L5 (2026-10-13)

Written and committed before either run was launched; no output of either script has been seen. Both scripts are unchanged (`l1b_t2t_dnds.py` as pre-registered at 0fe3c7f, `l5_adna_power.py` at 0e6da82). These notes answer findings ST-08 and ST-09 of [`severe-testing-2026-10-12.md`](../../../docs/research/criticality/severe-testing-2026-10-12.md). They fix readings; they change no band threshold, prediction or verdict move already registered.

## L1b (ST-08): the two outcome regions no registered band covers

The registered bands (docstring, "Bands"; function `band`) return `UNCLASSIFIED` in the cases below. Each is assigned here, before the run.

| Region (pooled JC dN/dS of V0) | Assigned reading | Verdict move |
|---|---|---|
| ALL >= 0.65 and SYN >= 0.65, single-difference share on SYN < 66% | **DAY-VALUE**: Day's number is reproduced on his stated assemblies, without the single-difference signature of his table | Same as band DAY: DN1 external `contradicted` -> `contested`. The write-up states that the value is reproduced and that the share differs from his 71.6%, so the two pipelines are not shown to be the same. The missing signature does not reduce the move |
| ALL < 0.40 and SYN >= 0.65 | **MIDDLE (anomalous)**: the syntenic subset reads high while the full set reads low, which audit prediction A2 (SYN holds >= 80% of ALL genes, within 0.03) excludes | Same as "MIDDLE on SYN": DN1 external `contested` proposed with the number stated, and the anomaly is diagnosed in the write-up before integration |
| ALL or SYN not a number (empty set, failed run) | **INVALID** | None. The run is reported as failed and repeated after the fault is found, as a post hoc run |

Every other combination is already covered by the registered order of tests (DAY, then LOCATED, then MIDDLE, then CRITIC). The first region is the larger one and lies on Day's side; it is assigned the reading most favourable to him.

Expected band, stated before the run: CRITIC (L1 on hg38/panTro5 gave 0.207 and 0.271). A CRITIC result is therefore not a surprise; its weight comes from the assemblies and alignment being the T2T ones Day names.

## L5 (ST-09): the registered predictions and the band rule disagree

The band rule in the script (`analyse`, l.796-812) gives CRITIC when model (iii) has E <= 1 for every s <= 1e-2 in every cell and the mainstream model (ii) has E <= 0.1. Predictions P3 (E < 1 for s <= 1e-2 in every cell) and P2 (mainstream E < 0.01) together imply CRITIC. Prediction P7 says MIDDLE. All three cannot hold.

Recorded before the run:

1. **Which one is expected to fail.** The band clause of P7. P2 and P3 follow from arithmetic stated in the docstring (about 1,000 generations for such a sweep against a 280-generation window); P7's "MIDDLE" was written without checking it against the rule. If P2 and P3 hold, P7's band clause is scored a miss caused by the registration, and it is reported as such. P7's second clause (crossover s* at 2e-2 or 3e-2 in both modes) is independent and is scored on its own.
2. **The band is taken from the script's rule as registered**, whatever P7 said.
3. **The DAY band is not reachable in part.** It needs median E >= 3 at s = 3e-3 and 1e-2, which P3's own arithmetic excludes. The informative contrast is CRITIC against MIDDLE. This is a limit of the test, on Day's side, and the write-up says so.
4. **Positive control.** The s >= 5e-2 cells (P3: median E >= 10 in both modes) show whether the simulated panel can register completed sweeps at all. If they fail, the run is reported as "model not validated" and no band moves a verdict.
5. **Weight of a CRITIC result.** Because CRITIC is what the registered arithmetic expects, a CRITIC outcome is a weak test of the registered move "C external `contested` -> `contradicted` (scoped)". That move stays a proposal for the three reviews; the write-up reports the severity limit beside it.

Neither note changes what Day or his critics are predicted to say in the two docstrings.

## L5 launch failure and post hoc launch fix (2026-10-13, after the notes above)

The first launch of `l5_adna_power.py main 8` on na-workhorse (script md5 5ecde49e..., as registered) stopped before any task ran: `PicklingError: Can't pickle local object <function const.<locals>.<lambda>>`. A task tuple carries the constant-size demography function, and the forkserver pool cannot send it to a worker. The local smoke of 2026-10-11 called `run_task` in-process, so it did not meet this. No task output exists (`raw/l5/` held only `l5_selftest.json`); no expected count was produced or seen.

**Fix (separate commit, post hoc, pre-run):** the pool is sent the task index and the worker rebuilds the tuple (`run_task_k`). Task order, seeds (keyed on the index) and output files are unchanged. No model, parameter, prediction or band is touched.

**What was seen before the fix, disclosed:** the selftest printed by that launch. V2 (fixation probability, event sanity cases) passed. **V3 missed in one of three cells:** at r = 1e-4 the simulated mean final non-founder share was 0.0185 against the formula's 0.0084 (n = 300), a difference of 0.0102 against the registered tolerance of max(0.01, 30%); r = 1e-3 (0.0823 against 0.0786) and r = 5e-3 (0.3091 against 0.3083) passed. The docstring states a consequence only for V1. Reading fixed here, before any task result: the run proceeds; the write-up reports V3 as a miss at tight linkage, by a margin of 0.0002 in absolute share; the formula understates the non-founder share there, so it overstates how completely a linked panel SNP is carried, which raises expected S* counts (a bias toward Day's band). The tolerance is not changed and the selftest is not rerun with other seeds. Reviewers decide whether the miss qualifies any band.
