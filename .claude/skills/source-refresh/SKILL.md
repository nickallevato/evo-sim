---
name: source-refresh
description: Pre-milestone source refresh for evo-sim per HOWTO-refresh.md: read-only fetches of the watch list, verbatim quotes filed, refresh-YYYY-MM-DD.md written. Run as the operator agent.
---
# Source refresh

You follow `docs/research/sources/HOWTO-refresh.md`.

Read-only fetches; each fetch in its own new directory; never execute a download; no Wayback snapshots, no contact, no posting, no paywall bypass. Anything dated after the model's knowledge cutoff comes from fetched text, never memory. File new quotes verbatim with locator and date and the next Q ids. Record sha256 of every new raw file, what could not be fetched and why, and a "What this changes for the audit" list. Check whether any watched record was silently replaced (compare md5 with the bib).
