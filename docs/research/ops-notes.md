# Orchestrator notes (Paperclip)

Mechanics of the agent platform, not of the audit. At most five lines per incident; no rules, no D- ids. If the orchestrator blocks work, stop and tell the owner. History before 2026-10-31 is in DECISIONS.md D-29..D-37.

- 2026-11-01: company onboarding auto-creates a chief-of-staff agent with permissive defaults plus an onboarding issue in todo; pause it before adding the AI connection. AI connections are per company.
- 2026-11-01 (GitHub Pages, EVOA-20): pushes to `master` 2-6 min apart made the deploy job fail ("in progress deployment, cancel 8f768df first"); the site kept serving the older commit. Fix: `gh api -X POST repos/nickallevato/evo-sim/pages/builds` once no deploy is running, then confirm the run is green and status.html returns 200. Wait for one Pages run to finish before the next `research:master` push.
