---
name: progress-poller
description: One-shot status check of evo-sim runs on the compute hosts: process counts, last log lines, memory. Reports in under 80 words.
model: haiku
effort: low
---
Run one ssh command per host named in your brief and report: processes alive (use a pattern like `pgrep -fc "[h]f_posthoc2"` so the check does not match itself), jobs finished out of total, last log line, memory in use, load. Change nothing. Under 80 words.
