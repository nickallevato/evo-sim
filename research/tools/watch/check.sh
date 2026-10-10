#!/usr/bin/env bash
# Hourly watcher for long runs on na-workhorse. Prints one line per run and lists runs that finished since the last
# check (state in $STATE). Cheap: one ssh call, no Python. Used by the session cron (see COLLECT.md).
STATE=${STATE:-$HOME/.cache/evo-sim-watch.state}; mkdir -p "$(dirname "$STATE")"; touch "$STATE"
RUNS="d15:d15_waiting_time.py xt:xt_cross_tool.py h8:h8_haldane_regime.py a2e:a2e_ltee_transfer.py g2c:g2c_standing_variation.py"
out=$(ssh -o BatchMode=yes -o ConnectTimeout=15 na-workhorse "uptime | sed 's/.*load/load/'; for r in $RUNS; do n=\${r%%:*}; p=\${r#*:}; if pgrep -f \"research/checks/\$p\" >/dev/null; then echo \"\$n RUNNING\"; else echo \"\$n DONE\"; fi; done; echo d15_cells \$(wc -l < ~/projects/evo-sim/research/checks/results/raw/d15_sweep.jsonl)/714" 2>/dev/null) || { echo "WATCH: ssh to na-workhorse failed"; exit 1; }
echo "$out"
new=""
for n in $(echo "$out" | awk '$2=="DONE"{print $1}'); do grep -qx "$n" "$STATE" || { new="$new $n"; echo "$n" >> "$STATE"; }; done
running=$(echo "$out" | awk '$2=="RUNNING"' | wc -l)
echo "NEWLY_DONE:${new:- none}"
echo "STILL_RUNNING: $running"
