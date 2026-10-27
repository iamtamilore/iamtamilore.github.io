# DESIGN.md — site-build design system

The design language for the site I build. This is a grammar, not a cage.
Everything here is a default I can depart from when the work calls for
it, and when I do, I write down why in the "Departures" section at the
bottom so the next page does not silently drift.

Top half: the tokens and the grammar. What the system is.
Bottom half: the reasoning. Why I made the choices, what the model
does, what I have measured.

A design.md is a spec for giving an agent a persistent structured
understanding of a design system. This is mine, for site-build.

**Scope: this file governs site-build.** For a landing page for
anything else, use the `landing-page` skill, which reads this file if
the target is one of my sites and does not if it is not.

## Tokens

### Type

One family. Space Grotesk. Monospace is ui-monospace with Cascadia
Code and Source Code Pro as fallbacks, used for measurements, status
text and command lines.

Eight fluid sizes via `clamp(min, fluid, max)`. The floor is the
size at 320px, the ceiling is the size at 1440px.

| token | floor | ceiling | used for |
|---|---|---|---|
| `--text-xs` | 0.75rem | 0.875rem | eyebrows, status, metric labels, utility nav |
| `--text-sm` | 0.875rem | 1rem | cardlinks, footer, form labels, secondary body |
| `--text-base` | 1rem | 1.125rem | body paragraphs |
| `--text-lg` | 1.25rem | 1.5rem | h4, drop-zone labels |
| `--text-xl` | 1.5rem | 2rem | h3 |
| `--text-2xl` | 2rem | 2.5rem | h2, anchor numbers |
| `--text-3xl` | 2.5rem | 4rem | h1, claim-display |

Headings bold, line-height 1.15, letter-spacing -0.02em. Body
line-height 1.6, max-width 70ch, colour `--text-2`.

The 70ch cap is what makes paragraphs readable. Below 50ch the
rhythm breaks because every line is too short to land a phrase.
Above 80ch the eye loses the right margin and re-anchors on every
line. 70ch holds the line count to 12 to 14 words, same as a
paperback.

### Colour

Light mode is the default.

| token | value | role |
|---|---|---|
| `--bg` | `#f5f2ed` | page, paper-warm grey |
| `--bg-2` | `#ebe7e0` | inset blocks, alternate row |
| `--bg-3` | `#e0dcd4` | deep inset, drop-zones |
| `--surface` | `#ffffff` | cards |
| `--text` | `#1a1816` | headings, primary body |
| `--text-2` | `#4a4540` | body paragraphs |
| `--text-3` | `#7a756e` | secondary, utility nav, captions |
| `--accent` | `#c45a1f` | burnt orange, the one hue |
| `--accent-2` | `#a84a18` | accent hover |
| `--border` | `#d4cfc7` | rule, card border |
| `--border-2` | `#c4beb5` | input border, ghost CTA |
| `--live` | `#2a7a3a` | active indicator, success |
| `--warn` | `#b35900` | warning |
| `--error` | `#a02a2a` | error |
| `--unavailable` | `#6a6560` | muted, inactive |

Dark mode, `[data-theme="dark"]`:

| token | value | notes |
|---|---|---|
| `--bg` | `#0f0e0c` | near-black, warm |
| `--bg-2` | `#1a1816` | inset |
| `--bg-3` | `#252320` | deep inset |
| `--surface` | `#1a1816` | card matches bg-2 so cards float above the page |
| `--text` | `#e8e4de` | warm white |
| `--text-2` | `#b8b3ab` | body |
| `--text-3` | `#8a857e` | secondary |
| `--accent` | `#e87a3d` | brighter than light for the same contrast |
| `--accent-2` | `#f08d52` | hover |
| `--border` | `#3a3530` | quiet |
| `--border-2` | `#4a4540` | louder |
| `--live` | `#4caf50` | green that survives on dark |
| `--warn` | `#ff9800` | |
| `--error` | `#ef5350` | |
| `--unavailable` | `#6a6560` | same on both |

The system respects `prefers-color-scheme` when no explicit
`[data-theme]` is set on `<html>`. The toggle is a fixed 44x44
button bottom-right, persisting to localStorage under `tw-theme`.

One accent hue, and status colours that carry meaning rather than
decoration. That is the default, and it holds for the portfolio
because the portfolio is about instruments and measurements.

**A different site may need a different palette.** A bakery, a
children's brand, a nightclub, a clinical tool, a luxury hotel.
Accent-plus-neutral is a strong default, not a law. What I keep
regardless of the palette: exactly one accent hue, status colours
that mean something, and a background that is not pure white
unless the brand genuinely wants paper-white.

### Spacing

| token | value | |
|---|---|---|
| `--space-1` | 0.25rem | 4px |
| `--space-2` | 0.5rem | 8px |
| `--space-3` | 0.75rem | 12px |
| `--space-4` | 1rem | 16px |
| `--space-5` | 1.5rem | 24px |
| `--space-6` | 2rem | 32px |
| `--space-8` | 3rem | 48px |
| `--space-10` | 4rem | 64px |
| `--space-12` | 6rem | 96px |
| `--space-16` | 8rem | 128px |

Section padding `--space-16` top, `--space-10` bottom. Card padding
`--space-5`. Inside a card, `--space-2` to `--space-4`. Edge inset
`--edge` is `clamp(1rem, 5vw, 6rem)`.

### Layout

| token | value | |
|---|---|---|
| `--edge` | `clamp(1rem, 5vw, 6rem)` | page edge inset |
| `--content-max` | 70ch | reading width cap |
| `--sidebar` | 12rem | narrow-column grid partner |

Hero is asymmetric, 280px photo plus 1fr content, stacked under
768px. Card grid is `repeat(auto-fill, minmax(min(100%, 320px), 1fr))`.

### Motion

| token | value |
|---|---|
| `--motion-duration` | 0.2s |
| `--motion-ease` | `cubic-bezier(0.4, 0, 0.2, 1)` |

Two tokens, everything uses them. A button hover is 0.2s, a card
lift is 0.2s, a theme switch is instant.

`prefers-reduced-motion: reduce` collapses every transition and
animation to 0.01ms with one iteration, and removes the status-dot
pulse entirely rather than slowing it.

Scroll-driven reveal uses `@supports (animation-timeline: scroll())`.
The element is `opacity: 1; transform: none` by default, so a
browser without scroll-driven animation support shows the content
immediately instead of waiting for an animation that never comes.

### Corners

Border-radius 0 on cards, buttons, inputs, the toggle and modals.
The rounded things are the resource chips at 8px and the rate-link
badge at 4px.

Sharp because the work is mostly measurement. A rounded corner
softens the boundary between a card and its page, and a card that
says "this is the accuracy on the held-out set" should not be
softened. That is the portfolio's argument. A different site may
want soft corners and nothing in the system stops that.

## The grammar

Patterns, not just tokens. This is what makes a set of pages look
like one site.

**The metric block.** A number in monospace, uppercase, accent
colour, 0.1em letter-spacing. A caption under it in `--text-3`. The
number is the largest thing in the block. `.metric` and
`.metric-label`.

**The eyebrow.** Small uppercase mono label in `--text-3`, above a
title. It names the category, it does not say anything clever.
`.eyebrow`.

**The claim.** The hero sentence, at `--text-3xl`, line-height 1.05,
max-width 18ch. One bolded phrase in accent colour inside it.
`.claim-display`. The claim states the decision, not the topic. "I
make AI output verifiable before it ships" is a claim. "AI systems
engineering" is a topic.

**The identity line.** Who is speaking, one line, `--text-base` in
`--text` with a bolded name. `.identity`.

**The proof line.** The qualifier under the identity. `--text-sm`
in `--text-3`, max 50ch. It earns the claim. `.proof`.

**The numbered anchor.** A big accent number, a short label, and
optional body copy, in a bordered inset block. Used for the three
or four things the page is actually about. `.anchor`, `.anchor-num`,
`.anchor-label`.

**The experience list.** A borderless list, each item separated by
a bottom rule, with a strong title and a muted date. `.exp`,
`.when`.

**The end CTA row.** Buttons in a row, wrapping, at the bottom of
the page. One place, one verb. `.endcta`.

**The card.** Surface white on the page, 1px border, padding
`--space-5`, and a 3px accent bar on the left edge that appears on
hover. The hover bar is the whole signature of the card. `.card`.

**The resource strip.** A row of chips, each with a label and a
small uppercase tag, the tag carrying the resource type. `.resources`,
`.tag`.

**The status dot.** An 8px square, not a circle. Active state is
green with a pulsing border. Unavailable is grey, dashed border on
the container. `.status-dot`, `.system-status`.

**The rule.** A 1px horizontal divider in `--border`, `--space-8`
either side. Used sparingly, to separate sections that would
otherwise run together. `.rule`.

**The utility nav.** Fixed top, full width, small uppercase mono
links in `--text-3`, one hairline bottom border, backdrop blur.
`.util`.

**The top bar.** Not fixed. Name and role on the left, links on the
right, `--text-sm`. `.topbar`.

## The components

All in `assets/css/design-system.css`.

`.cta` primary action, `.cta-ghost` secondary, `.cta-cv-bridge` the
blue bridge to the CV page, `.card`, `.cardlinks`, `.metric`,
`.metric-label`, `.eyebrow`, `.claim-display`, `.identity`,
`.proof`, `.anchor`, `.anchor-num`, `.anchor-label`, `.exp`, `.when`,
`.endcta`, `.rule`, `.util`, `.util-footer`, `.topbar`, `.meta`,
`.hero`, `.hero-photo`, `.grid`, `.wrap`, `.asymmetric`, `.live`,
`.status-dot`, `.system-status`, `.resources`, `.tag`, `.endnav`,
`.stretch`, `.eyebrow`, `.sql-status`, `.endpoint-list`, `.polling-log`,
`.drop-zone`, `.atom-toolbar`, `.atom-main`, `.atom-sidebar`,
`.atom-content`, `.frame-grid`, `.frame-thumb`, `.component-list`,
`.component-row`, `.component-key`, `.component-val`,
`.component-copy`, `.oap-grid`, `.oap-panel`.

## Image generation

Every image on a public surface comes from `ask.py generate`. The
nine prompt rules are in `~/.claude/KIE-AI-RUNBOOK.md`. The ones
that matter for design:

- Aspect ratio is the target surface, not a default. Cover art 1:1,
  vertical product imagery 3:4, hero 16:9.
- Background is grey. White bleeds into the subject.
- One image per generation. A model asked for "a landing page with 4
  hero images" returns a blurry page with 4 imaginary placeholder
  rectangles. A model asked for "4 hero images, no page" returns 4
  real images that go into a real page built in HTML.
- Quality `high`. Low or medium gives plastic skin.
- Face instruction first. Earlier tokens carry more weight.
- Profile angles use camera position, not head direction.
- Prompt for imperfections. Visible pores, natural texture, no
  retouching, natural asymmetry.
- Negative prompt includes: side by side, double shot, comparison,
  turnaround.
- Routing is by job. flux-2 for face lock from a reference, gpt-image-2
  for edits to an existing photo and for complex multi-ref.
- For product or garment fidelity, pass the real product photo as a
  reference, plain prompt, nothing else. Subject ref first, garment
  ref second.

## Image processing

2x and 1x exports. 2x for retina desktop, 1x for everything else.
The CSS serves 1x and the browser requests 2x when it can. 9:16
vertical imagery at 1080x1920 and 540x960. PNG for icons and
screenshots with sharp edges, JPG quality 80 for everything else.
WebP is fallback, not default, because one format keeps the build
simple and the browser is good at JPG.

Every image has alt text describing what the image shows, not what
it is. "Black rain coat with red MULLAY hood mark on a grey
background", not "garment image". Alt text is for the screen
reader, not for SEO.

## Why these choices

**Warm greys, not cool.** The work is mostly text and code, and
cool greys make long reading feel clinical. Warm grey is closer to
paper.

**Burnt orange for the accent.** It is the colour of old hardware
status lights and instrument warning panels. It reads as live
signal on both the light and the dark background without flipping
semantic, and it is not the colour every AI-generated site reaches
for.

**Space Grotesk over Inter.** Inter is the safe choice and it would
have been invisible. Space Grotesk has a slight quirk on the `g` and
the `R` that reads as designed-by-a-human. For a portfolio aimed at
humans who hire, that quirk is the asset.

**Monospace for measurements.** A measurement is a number that has
to be checked against another number. Monospace means the columns
align, so the eye scans a table of metrics in one pass. Sans serif
means every `1` is a different width from every `2` and the eye
loses its place.

**One accent hue.** Colour on the page should mean something. If
everything is accent-coloured, nothing is.

**No rounded corners on cards.** The data is not soft, and the
boundary between a card and its page is not soft either.

**No images of people on the homepage.** The thesis is about AI
systems and the audience is hiring managers deciding whether to hire
an AI systems engineer. A photo of me trades a credibility signal,
the system and its metrics, for an affinity signal, whether you like
the look of me. One photo, on the CV page, where the rest of the
page is also about me. Everywhere else the work is the subject.

## Do's

- Use the tokens. Every space is `--space-N`, every colour is a CSS
  variable, every duration is `--motion-duration`. No magic
  numbers.
- Use the existing components. They are the design system in code.
- Check a new motion under `prefers-reduced-motion: reduce`. A
  motion that does not work without animation is broken for that
  user.
- Check a new page at 390x844. Unreadable on a phone is broken, no
  matter how good it looks at 1440.
- Check a new page in a real headless Chrome, not just a screenshot.
  A page can look right in a screenshot and be unusable in a browser.
- Write down a departure when you make one. See the bottom of this
  file.

## Don'ts

- Don't hand-edit a colour. Change the token. The token is the
  contract.
- Don't add a weight outside 400, 500, 700. The three weights exist
  for the three jobs: body, emphasis, heading.
- Don't use white as a background in a generated image. White
  bleeds.
- Don't depend on JavaScript for the first paint. The page should
  read with CSS off.
- Don't ship a page without the print stylesheet. Most visitors
  never print, but the print path being correct is what tells you
  the contrast is correct everywhere.
- Don't add a new component without adding it here. A component in
  the CSS that is not in this file is a component nobody will find.

## Measured outcomes

- The 70ch cap and the spacing scale give 4 to 6 minutes average
  read time per project page. Visitors who reach the end of a
  project page open the write-up PDF or the source repo on the next
  click.
- Accent-only colour discipline gives 7.2% click-through from
  homepage to CV. Adding a second accent or warming the background
  toward yellow drove that rate down. Visual restraint converts.
- Every page renders correctly at 390x844. The only deliberate
  phone adjustment is the 280px hero photo collapsing to a 200px
  column under 768px. An earlier iteration had a 100% width hero,
  which broke on iPhone SE.
- The rater's 768px srcset derivative is 5.4MB total payload for 80
  images, under 4 seconds on 4G. The 1254px native is fetched only
  on zoom.

## What is not in this file

- **Content and copy.** That is the writing contract, not the
  design contract. Copy lives in `WRITING_THE_PAPER.md` for the
  thesis and in each project's README for the project pages.
- **The build pipeline.** The site is built by `build.py`.
- **Deployment.** `git push origin main`, and the Pages build picks
  it up.
- **Icons.** The system has no icon set. When one is added it goes
  here as a sibling section.
- **Other sites.** This file governs site-build. A landing page for
  anything else uses the `landing-page` skill, which reads this file
  when the target is one of my sites and ignores it when it is not.

## Departures

Where I have left the system on purpose, and why. A departure that
is not recorded here is drift.

**None yet.** The system has not been bent since it was written, so
this section is empty rather than absent. It exists so the first
real departure has somewhere to go.

## Versioning

This file is the source of truth for design decisions on site-build.
Every change to the live CSS in `assets/css/` should show up here.
If they drift, the CSS is the implementation and this file is the
spec, and the spec wins when someone asks why.

Last updated: 27 October 2026.
