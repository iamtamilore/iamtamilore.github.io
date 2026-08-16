# Qwen task: write one CSS block. Nothing else.

You are writing an appended CSS block for an existing static portfolio site. You are
writing **CSS only**. Do not write HTML. Do not write JavaScript. Do not rewrite the
existing stylesheet. Output one fenced CSS block and a short list of any assumption you
had to make. Nothing else.

## Hard constraints, all of them non negotiable

1. **Use only the CSS custom properties listed below.** Never write a hex colour, an
   `rgb()`, or a named colour anywhere in your output. Not one. The site has four themes
   that swap these ten tokens, and a single hardcoded colour breaks three of them.
   Where you need a translucent version of a token, use `color-mix(in srgb, var(--panel) 88%, transparent)`.
2. **No em dashes and no en dashes** anywhere, including inside comments. Hyphen only.
3. Mobile first. Write the base rule for narrow screens, then widen with
   `@media (min-width: 720px)`.
4. Every animation and transition must sit inside
   `@media (prefers-reduced-motion: no-preference)`, and the element must be fully
   visible and correctly positioned when that query does not match. Never rely on the
   absence of a rule to make something visible.
5. No external fonts, no `@import`, no CDN reference. The site loads Archivo already.
6. Do not use `backdrop-filter` as the only thing making text legible. Put a solid
   token background behind it first, then add the blur as an enhancement.

## The tokens you may use

```
--ink        page background, darkest
--ink-2      a second, slightly lifted page background
--panel      raised surface, cards
--line       hairline borders
--text       body text
--muted      secondary text
--muted-2    tertiary text, captions
--accent     the single accent colour
--accent-dim a darker accent, for borders and hover
--on-accent  text colour when sitting on an accent-filled surface
--max        900px, the content column width
--pad        20px, the horizontal gutter
```

Existing type scale, do not redefine these: `h1` is
`clamp(28px, 7vw, 46px)`, `h2` is `clamp(21px, 4.5vw, 27px)`, body is 16px/1.65.

## What to write

### 1. `.sitehead` and `.sitenav` - a persistent fixed header

The landing page currently has no navigation of any kind. Give it a fixed header, full
width, sitting above everything at `z-index: 100`.

- Transparent with no border at scroll position zero.
- When it carries the class `is-stuck` (JavaScript adds this, you do not write the
  JavaScript): a solid `--ink` background at high opacity, a `--line` bottom border, and
  the blur enhancement.
- Inside it, a flex row constrained to `var(--max)` with `var(--pad)` gutters:
  a wordmark on the left, nav links on the right.
- Nav links are `--muted`, go `--text` on hover, and grow a 2px `--accent` underline from
  left to right over 220ms on hover and on `:focus-visible`.
- The link with `aria-current="page"` sits at `--text` with its underline already full.
- Below 720px the nav links collapse: hide all but the last child, which is a CTA link.
  Do not build a burger menu, there are only five links.
- Content below must not slide under the header, so provide a `.has-shell` class for
  `body` that adds top padding equal to the header height.

### 2. `#scrollbar` - a scroll progress line

A 3px bar fixed to the very top at `z-index: 101`, `--accent`, width driven by an inline
style JavaScript sets. It must be invisible, not full width, when width is zero. Give it
`transform-origin: left` if you prefer a scaleX approach, and say which you chose.

### 3. `.band` - full bleed background sections

This is the single most important piece. The site is currently one flat column with no
sectioning, which is why it reads as a document rather than a designed page.

- `.band` spans the full viewport width and holds an inner `.band-inner` constrained to
  `var(--max)`, centred, with `var(--pad)` gutters.
- Vertical rhythm: 68px top and bottom below 720px, 104px above it.
- `scroll-margin-top` of 90px so anchor jumps clear the fixed header.
- Variants: `.band--base` uses `--ink`, `.band--lift` uses `--ink-2`, `.band--panel`
  uses `--panel` and gets a `--line` border on its top and bottom edges only.
- Two adjacent bands of the same variant must not show a seam. Handle it.

### 4. `.eyebrow-num` - numbered section labels

A small uppercase label that precedes a section heading, in the form `01 / The work`.
Letter spacing around 0.16em, 12px, `--muted`. The number itself sits in a `<b>` and is
`--accent`. Preceded by a 26px by 2px `--accent-dim` rule, vertically centred, using flex
and a gap rather than a pseudo element with absolute positioning.

### 5. `.ticker` - a marquee band

A full bleed strip with an `--ink-2` background and `--line` borders top and bottom,
rotated by -0.5deg and scaled to 1.02 so the rotation does not expose the page background
at the edges. Inside, a track that translates from 0 to -50% over 34 seconds, linear,
infinite. The markup will contain the item group twice, so a -50% translation loops
seamlessly. Items are 13px, uppercase, 0.12em tracking, `--muted`, separated by a
`--accent` glyph. Pause the animation on hover. Under reduced motion the animation must
stop and the strip must remain readable, not blank.

### 6. `.split` - an asymmetric two column layout

Single column below 720px. Above it, `1.05fr 0.95fr` with a 44px gap and
`align-items: start`. Add `.split--flip` which reverses the visual order using
`grid-auto-flow` or explicit column placement, never `direction: rtl`.

### 7. `.sitefoot` - a real footer

Currently the footer is one muted line. Make it a three column grid above 720px and a
single stacked column below: identity block, a link column, a contact column. Top border
in `--line`, `--ink-2` background, 44px of internal padding. Links are `--muted-2` going
`--accent` on hover.

### 8. Print

Every one of the above must be hidden or neutralised at print: `.sitehead`, `#scrollbar`
and `.ticker` display none, `.band` loses its background and its vertical padding drops to
16px, `.sitefoot` loses its background.

## Output format

One fenced CSS block, prefixed by a comment banner reading
`/* ---------- site shell ---------- */`. Then, below the block, a short bulleted list of
any assumption you made or anything in this spec you could not satisfy. Do not apologise,
do not explain CSS basics, and do not restate the spec back to me.
