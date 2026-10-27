# iamtamilore.github.io

Personal site. https://iamtamilore.github.io

Project pages are generated from the same markdown that produces the PDFs:

```bash
python3 build.py
```

## Design

The design language for this site is in [`DESIGN.md`](./DESIGN.md). Tokens (colours, type scale, spacing, motion), the component vocabulary, the image-generation defaults, and the do's and don'ts all live there. The live CSS at `assets/css/design-system.css` matches DESIGN.md token-for-token; if they drift, DESIGN.md wins.

The design pipeline runs through three skills at `~/.claude/skills/`:

- **`brief`** produces a one-page marketing brief
- **`taste`** produces an image prompt that uses the site's palette and tokens
- **`landing-page`** places the result on the page using the existing component vocabulary

A fourth skill, **`install`**, is the meta-skill for adding new tools without breaking what is already wired.
