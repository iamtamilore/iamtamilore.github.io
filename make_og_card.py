"""Render the square social card for a case study.

LinkedIn fetches the og:image of a linked page and shows it as a near-square
tile on a project card. It crops to fill that tile, so the 1200x900 landscape
card lost its first digit: "68 videos published" rendered as "8 videos
published". A wrong number on a public profile is a false claim, so the card
is drawn square and the content is kept inside the band that survives both
crops LinkedIn applies:

  - project tile, near square (1:1): crops the sides
  - feed link preview (1.91:1): crops the top and the bottom

The safe band is therefore x 90..1110 and y 320..880 of a 1200x1200 canvas.
Everything measurable is measured on the renderer's own extents and the rows
are stacked downward from a fixed top margin, so nothing collides.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "assets" / "img"

BG = "#0f0e0c"
ORANGE = "#FF7A3D"
WHITE = "#ECE7DD"
MUTED = "#968C7E"
FAINT = "#6A6257"

SANS = "DejaVu Sans"

W, H = 1200, 1200
MARGIN = 90
USABLE = W - 2 * MARGIN

# the band that survives a 1.91:1 crop of a 1200x1200 canvas
TOP, BOTTOM = 320, 880

CARDS = [
    {
        "file": "episode_pipeline_og.jpg",
        "metric": "68",
        "metric_label": "videos published",
        "title": "Episode Pipeline",
        "sub": "a gate that refuses the episode",
        "foot": "Taiwo Alabi",
    },
    {
        "file": "og_site.jpg",
        "metric": "37",
        "metric_label": "verified systems, indexed in public",
        "title": "Portfolio index",
        "sub": "68 videos and 53,376 model calls, every one dated.",
        "foot": "iamtamilore.github.io",
    },
]


def render(spec) -> Path:
    fig = plt.figure(figsize=(W / 100, H / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((-10, -10), W + 20, H + 20, boxstyle="square,pad=0",
                                facecolor=BG, edgecolor="none", zorder=0))

    renderer = fig.canvas.get_renderer()

    def measure(text, fontsize, weight):
        """Width in px of a single line, measured on the real renderer."""
        probe = ax.text(0, 0, text, fontsize=fontsize, weight=weight, family=SANS)
        width = probe.get_window_extent(renderer=renderer).width
        probe.remove()
        return width

    def wrap(text, fontsize, weight, max_px):
        words = text.split()
        lines, current = [], ""
        for word in words:
            candidate = word if not current else current + " " + word
            if measure(candidate, fontsize, weight) <= max_px or not current:
                current = candidate
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines

    def put(y_from_top, text, fontsize, weight, color, align="left"):
        x = MARGIN if align == "left" else W - MARGIN
        ax.text(x, H - y_from_top, text, fontsize=fontsize, weight=weight, color=color,
                ha=align, va="top", family=SANS, zorder=3)

    cursor = TOP

    ax.add_patch(FancyBboxPatch((MARGIN, H - cursor - 16), 240, 16,
                                boxstyle="square,pad=0",
                                facecolor=ORANGE, edgecolor="none", zorder=2))
    cursor += 16 + 52

    metric = spec["metric"]
    msize = 168
    while measure(metric, msize, "bold") > USABLE and msize > 80:
        msize -= 6
    put(cursor, metric, msize, "bold", ORANGE)
    cursor += msize * 100 / 72 * 0.72 + 22

    put(cursor, spec["metric_label"], 36, "normal", MUTED)
    cursor += 36 * 100 / 72 + 46

    title_lines = wrap(spec["title"], 62, "bold", USABLE)
    title_lead = 70
    for i, line in enumerate(title_lines):
        put(cursor + i * title_lead, line, 62, "bold", WHITE)
    cursor += (len(title_lines) - 1) * title_lead + 62 * 100 / 72 * 0.73 + 24

    # the claim is sized down until the whole block fits the safe band, so a
    # longer line can never push it into the rule
    rule_y = BOTTOM - 46
    sub_size = 32
    while sub_size >= 22:
        sub_lines = wrap(spec["sub"], sub_size, "normal", USABLE)
        sub_lead = sub_size * 100 / 72 * 1.35
        end = cursor + (len(sub_lines) - 1) * sub_lead + sub_size * 100 / 72
        if end <= rule_y - 26:
            break
        sub_size -= 2
    for i, line in enumerate(sub_lines):
        put(cursor + i * sub_lead, line, sub_size, "normal", MUTED)

    # the rule and the name sit on the bottom edge of the safe band
    ax.plot([MARGIN, W - MARGIN], [H - rule_y, H - rule_y], color=ORANGE, lw=1.6, zorder=2)
    put(rule_y + 16, spec["foot"], 24, "normal", FAINT, align="right")

    out = OUT / spec["file"]
    fig.savefig(out, dpi=100, facecolor=BG)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for spec in CARDS:
        path = render(spec)
        print(f"wrote {path}  {W}x{H}")
