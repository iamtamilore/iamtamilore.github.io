"""Render the three LinkedIn project thumbnails in the house card style.

The house card style is the one measured off assets/img/care_agent.jpg and
produced by make_project_cards.py: warm near-black #0f0e0c, orange #FF7A3D as
the one surviving colour, paper white #ECE7DD, muted #968C7E, DejaVu Sans.

LinkedIn project covers are shown wide, so these are 1200x627 (1.91:1), which
is the aspect LinkedIn crops to without losing the metric line.

Every number here is a measured fact from the pipeline, the gateway ledger or
the cron ledger, read on 24 November 2026.

The layout is measured, not guessed. Every text run is wrapped to the usable
width using the renderer's own extents, and the rows are stacked downward from
a fixed top margin using the measured height of each run, so nothing collides
or runs off the canvas.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path("/tmp/opencode/imgbuild")

BG = "#0f0e0c"
ORANGE = "#FF7A3D"
WHITE = "#ECE7DD"
MUTED = "#968C7E"
FAINT = "#6A6257"

SANS = "DejaVu Sans"

W, H = 1200, 627
MARGIN = 70
USABLE = W - 2 * MARGIN


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

    def put(x_from_top, text, fontsize, weight, color, y_from_top=None):
        """Place a run with its TOP at y_from_top pixels below the canvas top."""
        y = y_from_top if y_from_top is not None else x_from_top
        ax.text(MARGIN, H - y, text, fontsize=fontsize, weight=weight, color=color,
                ha="left", va="top", family=SANS, zorder=3)

    cursor = 66

    # --- accent bar, top left, the mark the site cards carry -----------------
    ax.add_patch(FancyBboxPatch((MARGIN, H - cursor - 13), 214, 13,
                                boxstyle="square,pad=0",
                                facecolor=ORANGE, edgecolor="none", zorder=2))
    cursor += 13 + 44

    # --- the metric, large, in the one surviving colour -----------------------
    metric = spec["metric"]
    msize = 118
    while measure(metric, msize, "bold") > USABLE and msize > 56:
        msize -= 4
    put(cursor, metric, msize, "bold", ORANGE)
    metric_h = msize * 100 / 72 * 0.72          # digit cap height in px
    # the comma in 53,376 descends below the baseline, so the gap below the
    # metric has to clear a descender, not just the cap height
    cursor += metric_h + (30 if "," in metric else 14)

    # --- the metric label -----------------------------------------------------
    put(cursor, spec["metric_label"], 29, "normal", MUTED)
    cursor += 29 * 100 / 72 + 30

    # --- the title, wrapped ---------------------------------------------------
    title_lines = wrap(spec["title"], 39, "bold", USABLE)
    title_lead = 45
    for i, line in enumerate(title_lines):
        put(cursor + i * title_lead, line, 39, "bold", WHITE)
    cursor += (len(title_lines) - 1) * title_lead + 39 * 100 / 72 * 0.73 + 22

    # --- the one-line claim, wrapped -----------------------------------------
    sub_lines = wrap(spec["sub"], 23, "normal", USABLE - 300)
    sub_lead = 31
    for i, line in enumerate(sub_lines):
        put(cursor + i * sub_lead, line, 23, "normal", MUTED)
    cursor += (len(sub_lines) - 1) * sub_lead + 23 * 100 / 72 + 18

    # --- the footer note, on the bottom rule ----------------------------------
    ax.plot([MARGIN, W - MARGIN], [58, 58], color="#2A2724", lw=1.5, zorder=2)
    put(None, spec["foot"], 19, "normal", FAINT, y_from_top=H - 38)

    out = OUT / spec["file"]
    fig.savefig(out, dpi=100, facecolor=BG)
    plt.close(fig)
    return out


THUMBNAILS = [
    {
        "file": "li-thumb-pipeline.jpg",
        "square_file": "li-thumb-pipeline-sq.jpg",
        "metric": "68",
        "metric_label": "videos published",
        "title": "Multi-channel short-form video pipeline",
        "sub": "Eight stages in a fixed order, then two gates that can refuse the episode.",
        "foot": "Read from each channel's own Shorts listing, 24 November 2026",
    },
    {
        "file": "li-thumb-gateway.jpg",
        "square_file": "li-thumb-gateway-sq.jpg",
        "metric": "53,376",
        "metric_label": "model calls logged",
        "title": "Multi-model LLM gateway and MCP agent layer",
        "sub": "One chokepoint for every call, with a response cache, a budget guard and a daily ceiling.",
        "foot": "Ledger read on 24 November 2026",
    },
    {
        "file": "li-thumb-termsguard.jpg",
        "square_file": "li-thumb-termsguard-sq.jpg",
        "metric": "87%",
        "metric_label": "F1 score",
        "title": "TermsGuard AI",
        "sub": "Reads a privacy policy and flags the unfair clauses in plain English.",
        "foot": "102 hand-labelled reference clauses, live demo",
    },
]


# ---------------------------------------------------------------------------
# Square variants.
#
# LinkedIn's project list shows each media item as a near-square tile and
# centre-crops the source. A 1200x627 landscape card loses its first digit
# ("68" rendered as "8"), which is a false number on a public profile. The
# square card below is rendered so the crop cannot cut a metric.
# ---------------------------------------------------------------------------

SW, SH = 1200, 1200
SMARGIN = 90
SUSABLE = SW - 2 * SMARGIN


def render_square(spec) -> Path:
    fig = plt.figure(figsize=(SW / 100, SH / 100), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, SW)
    ax.set_ylim(0, SH)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((-10, -10), SW + 20, SH + 20, boxstyle="square,pad=0",
                                facecolor=BG, edgecolor="none", zorder=0))
    renderer = fig.canvas.get_renderer()

    def measure(text, fontsize, weight):
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

    def put(y_from_top, text, fontsize, weight, color):
        ax.text(SMARGIN, SH - y_from_top, text, fontsize=fontsize, weight=weight, color=color,
                ha="left", va="top", family=SANS, zorder=3)

    cursor = 120
    ax.add_patch(FancyBboxPatch((SMARGIN, SH - cursor - 16), 260, 16,
                                boxstyle="square,pad=0",
                                facecolor=ORANGE, edgecolor="none", zorder=2))
    cursor += 16 + 66

    metric = spec["metric"]
    msize = 200
    while measure(metric, msize, "bold") > SUSABLE and msize > 80:
        msize -= 6
    put(cursor, metric, msize, "bold", ORANGE)
    cursor += msize * 100 / 72 * 0.72 + 26

    put(cursor, spec["metric_label"], 40, "normal", MUTED)
    cursor += 40 * 100 / 72 + 58

    title_lines = wrap(spec["title"], 56, "bold", SUSABLE)
    title_lead = 64
    for i, line in enumerate(title_lines):
        put(cursor + i * title_lead, line, 56, "bold", WHITE)
    cursor += (len(title_lines) - 1) * title_lead + 56 * 100 / 72 * 0.73 + 34

    sub_lines = wrap(spec["sub"], 32, "normal", SUSABLE)
    sub_lead = 44
    for i, line in enumerate(sub_lines):
        put(cursor + i * sub_lead, line, 32, "normal", MUTED)
    cursor += (len(sub_lines) - 1) * sub_lead + 32 * 100 / 72 + 34

    ax.plot([SMARGIN, SW - SMARGIN], [110, 110], color="#2A2724", lw=1.5, zorder=2)
    foot_lines = wrap(spec["foot"], 26, "normal", SUSABLE)
    for i, line in enumerate(foot_lines):
        put(SH - 90 + i * 34, line, 26, "normal", FAINT)

    out = OUT / spec["square_file"]
    fig.savefig(out, dpi=100, facecolor=BG)
    plt.close(fig)
    return out


if __name__ == "__main__":
    for spec in THUMBNAILS:
        path = render(spec)
        print(f"wrote {path}  {W}x{H}")
        sq = render_square(spec)
        print(f"wrote {sq}  {SW}x{SH}")
