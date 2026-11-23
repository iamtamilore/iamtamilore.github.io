# _CURRENT.md: personal site
# Last updated: 2026-11-23 by OpenCode
# DO NOT append to this file. Overwrite it at session start/close.

## Broken

- None verified in this sync pass. The site build and link check were not run in this pass, so this is not a release-readiness claim.

## In Progress

- The public portfolio is at `https://iamtamilore.github.io`. The repository is `/home/newtazer/site-build`, branch `main`, remote `iamtamilore/iamtamilore.github.io`.
- The Agent Foundations CV family is generated from `/home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission/Taiwo_Alabi_CV_AgentFoundations.md` through `bash /home/newtazer/site-build/update_cv.sh`. The script builds the DOCX and PDF, regenerates the CV and project routes, verifies the output, then commits and pushes both repositories.
- The rater v2 route was committed on 8 November 2026. The independent human rater evaluation is still pending. No final rater metric may be stated on the site or in a CV until that execution is verified.
- The portfolio source for project pages remains the README files under `~/Desktop/NCI/CV VARIANTS/symplicity/<project>/`. Generated files under `p/*/index.html` must not be hand-edited.

## Blocked

- Final thesis and human-rater claims are blocked on execution and verification. The public rater route existing is not evidence that human evaluation has happened.
- Any CV claim that has already been sent to an ATS cannot be silently retired from the live site. Check the CV variants in circulation before removing a metric or capability.

## Next Up

1. Audit the portfolio against the synced master documents and `DESIGN.md`.
2. Edit the CV master Markdown and project READMEs only.
3. Run `bash /home/newtazer/site-build/update_cv.sh --no-push`.
4. Run the site build and link sanity check.
5. Show a compact diff summary and ask Taiwo before any live push.

## Source-of-truth map

| Surface | Source |
|---|---|
| Public site | `/home/newtazer/site-build/` |
| CV content | `/home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission/Taiwo_Alabi_CV_AgentFoundations.md` |
| Project pages | `~/Desktop/NCI/CV VARIANTS/symplicity/*/README.md` |
| Design and recruiter-copy rules | `/home/newtazer/site-build/DESIGN.md` |
| Career handling rules | `~/Desktop/NCI/CV VARIANTS/_HANDOFF_CAREER.md` |
| Laura call rules | `~/Desktop/NCI/CV VARIANTS/LAURA_CV_RULES.md` |

## Handoff for a non-filesystem AI

Read this file and `DESIGN.md`. Do not edit generated pages. Do not claim that human-rater or thesis metrics are final. Flag any proposed public copy that needs source verification.
