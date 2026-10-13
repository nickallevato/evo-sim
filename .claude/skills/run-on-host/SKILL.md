---
name: run-on-host
description: Launch, check and collect a pre-registered evo-sim run on na-workhorse (or builder). Use whenever a check script must run off the workstation.
---
# Run a pre-registered check on a compute host

No computation on the workstation beyond one process, under 500 MB, under a minute. Everything else runs on `na-workhorse` (12 cores, 14 GB). `builder` (`na@builder`, 8 cores, 5 GB) has **no scipy** in its venv; scripts that import scipy cannot run there until the owner approves installing the pinned requirements.

## Before launch
1. The script's commit is pushed (`git log origin/research -1 -- <script>`). Pre-run notes and post hoc fixes are separate, pushed commits.
2. `rsync -a -e 'ssh -o BatchMode=yes' <script and every module it imports> na-workhorse:projects/evo-sim/research/checks/` and any inputs under `sources/raw/` (create the directory on the host first).
3. On the host, `md5sum` / `sha256sum` the script and inputs; they must equal the local values and those stated in the docstring.
4. `ssh -o BatchMode=yes na-workhorse 'uptime; free -g | sed -n 2p'`. Keep total busy processes at or under 11 and RAM under about 12 GB.
5. Run the script's smoke or selftest **on the host, through the real entry point** (real worker pool, every grid value).

## Launch
```sh
ssh -o BatchMode=yes na-workhorse 'cd ~/projects/evo-sim && \
  (hostname; date -u; echo "<commits, workers, exact command>"; md5sum <files>) > research/checks/results/raw/<id>.host && \
  setsid -f nohup research/.venv/bin/python -I research/checks/<script>.py <args> \
    > research/checks/results/raw/<id>.out 2>&1 < /dev/null'
```
Launch and return. Check once after a minute or two that workers are alive and memory is as planned, then do not poll; check once when it should be done.

## Pitfalls met on 2026-10-13
- **zsh does not split unquoted variables.** `SSH='ssh -o BatchMode=yes'; $SSH host ...` fails. Write the options inline.
- **A backgrounded `a && b &` chain keeps the ssh channel open** and the local command hangs. Use `setsid -f` and redirect all three streams.
- **`pgrep -f pattern` matches the shell running it** when the pattern appears in that shell's command line (a waiter loop then never ends; `pkill -f` kills your own session). Use `"[x]yz"` patterns, or put the waiter in a script file.
- To queue job B behind job A, write a small script on the host (`while pgrep -f "[a]_script" >/dev/null; do sleep 30; done; exec python ...`) and start it with `setsid -f nohup`.
- `ssh:5: command not found: _lion_remote_term` is harmless noise.
- The host has rebooted mid-run before. Scripts should skip finished jobs on relaunch; note in the queue whether jobs are checkpointed.
- Output to a file is block-buffered; an empty `.out` does not mean a dead job. Look at the process's CPU time.

## Collect
1. Zero processes (`pgrep -fc "[s]cript_name"`) and the log ends with its completion line.
2. Merge and analyse **on the host** if the script has those modes; a merge must report missing 0, extra 0, mismatches 0.
3. `rsync -a -e 'ssh -o BatchMode=yes' 'na-workhorse:projects/evo-sim/research/checks/results/raw/<id>*' research/checks/results/raw/`. When two hosts hold files of the same name, name each file explicitly so one does not overwrite the other.
4. Append finish times and md5s to the `.host` record. Commit raw outputs with explicit paths. **Never commit or push from a host.**

## If a launch fails
Stop. Keep the failed log under a new name (`<id>_launch1_failed.out`). Find the root cause by evaluating the failing expression alone. The fix is a separate commit labelled "post hoc (pre-run, no task result seen)", with a disclosure of exactly what output had been seen, written before relaunch.
