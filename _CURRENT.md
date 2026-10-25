# _CURRENT.md — personal-site
# Last updated: 2026-08-24 by Claude (seeded from engineering-log/personal-site.jsonl)
# DO NOT append to this file. Overwrite it at session start/close.

## Broken (ordered by severity)
- None currently open. Atom Browser, O.A.P. Trainer, and /bank/ dashboard were all
  recovered/fixed and verified live on 2026-08-24.

## In Progress
- Nothing active on this project right now.

## Blocked
- **Open decision, not defaulted into any action**: whether/how to make the Atom
  Browser's real frame images publicly visible on GitHub Pages. GitHub Pages is fully
  public regardless of "it's my own site" framing — this was explicitly raised and left
  unresolved. Do not publish the real `atoms/frames` symlink target without this being
  decided first.

## Next Up (prioritized)
1. Confirm the two `github_token.txt` files (`Young Mooch/github_token.txt`,
   `streaming/github_token.txt`) have actually been deleted after use — advised, not
   confirmed. Both are LIVE credentials.
2. Decide the Atom Browser public-visibility question (demo-with-safe-images vs
   screen-recording vs private-sharing vs publish-as-is) — user's call.

## Rejected Approaches
- `oap/index.html` `API_BASE = ''` (same-origin assumption): 404s every API call when
  the static site and the FastAPI backend are served on different ports. Replaced with
  a hardcoded `http://localhost:8000` — user's explicit choice over changing the
  backend's serving route. `entry: 01M0RS3SWDCNP4WE`.

## Open Ideas
- None logged yet for this project beyond what's in Next Up.

## Recent Log Entries (last 5, personal-site.jsonl)
- `01M0RS3SWD33C7RM` session_close — library filters/pagination fixed+verified; 2
  more real bugs found+fixed (script corruption, cross-origin API calls)
- `01M0RS3SWDEJK0W0` verification — live end-to-end: OAP count 866, pagination,
  dashboard 1212, all real DB numbers
- `01M0RS3SWDCNP4WE` fix — restored broken constructor; hardcoded API_BASE; fixed
  checkBackend/loadStats race
- `01M0RS3SWDKCD0Q8` diagnosis — cross-origin 404 + JS syntax corruption found while
  testing (not the original report)
- `01M0RPRV39SB7R04` fix — rebuilt /bank/ as a real dashboard into idea_bank repo

## Handoff for Non-Filesystem AI (Kimi/Qwen)
If you have no file access: read this file. Do NOT assume the Atom Browser's images
are safe to reference/link publicly — that's an explicitly open, unresolved decision,
not an oversight. Draft designs, prose, or research only; flag anything needing
file/DB verification for the next Claude Code session.
