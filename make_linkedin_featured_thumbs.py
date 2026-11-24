"""Render the two extra LinkedIn Featured thumbnails in the house card style.

Same renderer and same measured layout as make_linkedin_thumbnails.py, so the
Featured section reads as one set. 1200x627, the aspect LinkedIn crops to
without losing the metric line.

Every number here is measured and dated.
"""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

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
        ax.text(MARGIN, H - y_from_top, text, fontsize=fontsize, weight=weight, color=color,
                ha="left", va="top", family=SANS, zorder=3)

    cursor = 66
    ax.add_patch(FancyBboxPatch((MARGIN, H - cursor - 13), 214, 13,
                                boxstyle="square,pad=0",
                                facecolor=ORANGE, edgecolor="none", zorder=2))
    cursor += 13 + 44

    metric = spec["metric"]
    msize = 118
    while measure(metric, msize, "bold") > USABLE and msize > 56:
        msize -= 4
    put(cursor, metric, msize, "bold", ORANGE)
    metric_h = msize * 100 / 72 * 0.72
    cursor += metric_h + (30 if "," in metric else 14)

    put(cursor, spec["metric_label"], 29, "normal", MUTED)
    cursor += 29 * 100 / 72 + 30

    title_lines = wrap(spec["title"], 39, "bold", USABLE)
    title_lead = 45
    for i, line in enumerate(title_lines):
        put(cursor + i * title_lead, line, 39, "bold", WHITE)
    cursor += (len(title_lines) - 1) * title_lead + 39 * 100 / 72 * 0.73 + 22

    sub_lines = wrap(spec["sub"], 23, "normal", USABLE - 300)
    sub_lead = 31
    for i, line in enumerate(sub_lines):
        put(cursor + i * sub_lead, line, 23, "normal", MUTED)
    cursor += (len(sub_lines) - 1) * sub_lead + 23 * 100 / 72 + 18

    ax.plot([MARGIN, W - MARGIN], [58, 58], color="#2A2724", lw=1.5, zorder=2)
    put(H - 38, spec["foot"], 19, "normal", FAINT)

    out = OUT / spec["file"]
    fig.savefig(out, dpi=100, facecolor=BG)
    plt.close(fig)
    return out


THUMBNAILS = [
    {
        "file": "li-thumb-cv.jpg",
        "metric": "2",
        "metric_label": "pages, no filler",
        "title": "Curriculum vitae",
        "sub": "Backend Engineer and AI Engineering graduate roles, with metrics and the honest limits of each system.",
        "foot": "iamtamilore.github.io/Alabi_Taiwo_CV.pdf",
    },
    {
        "file": "li-thumb-portfolio.jpg",
        "metric": "37",
        "metric_label": "verified systems, indexed in public",
        "title": "Portfolio index",
        "sub": "Five full case studies. Every number measured and dated, every limit stated.",
        "foot": "iamtamilore.github.io",
    },
    {
        "file": "li-thumb-github.jpg",
        "metric": "10",
        "metric_label": "public repositories",
        "title": "Open source",
        "sub": "Browser orchestrator, portfolio site, TermsGuard AI, clinical retrieval, care automation, image QA gate.",
        "foot": "github.com/iamtamilore",
    },
]


if __name__ == "__main__":
    for spec in THUMBNAILS:
        p = render(spec)
        print(f"wrote {p}  {W}x{H}")
