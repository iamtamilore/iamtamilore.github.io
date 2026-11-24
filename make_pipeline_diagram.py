"""Render the episode-pipeline architecture diagram in the house diagram style.

The house style was measured off assets/img/tg_architecture.png rather than guessed.
Canvas 1536x1024 at 160 dpi. Paper #F0EEE6, box fill #E7E6E4, box border #232323
at 2px with a 10px corner radius. The title is bold DejaVu Sans, the box letters
are bold DejaVu Sans, and everything inside a box plus the footer and the
signature is DejaVu Sans Mono. The accent is #FD6507.

Point sizes below are calibrated to the reference diagram's measured ink, and the
box metrics (inset, line spacing, padding) come from the same measurements:

  title ink          399px wide for "TermsGuard AI"   -> DejaVu Sans bold 21.9pt
  subtitle ink       933px wide for 75 characters      -> DejaVu Sans 10.8pt
  box letter         15px cap height                  -> DejaVu Sans bold 9.3pt
  body text          11.3px advance per character     -> DejaVu Sans Mono 8.5pt
  footer             410px for 47 characters          -> DejaVu Sans Mono 6.6pt
  signature          99px for 12 characters           -> DejaVu Sans Mono 6.4pt

Box geometry measured off the reference: left border to letter 19px, letter cap
top 10px below the box top, body first line 38px below the box top, 25px
between body lines, 28px below the last line.

Every fact in the diagram comes from the episode pipeline README and the case
study. The order of the stages is a correctness property of the driver, and the
gates are what make the pipeline refuse an episode rather than publish one.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parent / "assets" / "img" / "episode_pipeline_architecture.png"

PAPER = "#F0EEE6"
BOX_FILL = "#E7E6E4"
BOX_EDGE = "#232323"
INK = "#111111"
ACCENT = "#FD6507"
MUTED = "#7A7F87"

W, H, DPI = 1536, 1024, 160

SANS = "DejaVu Sans"
MONO = "DejaVu Sans Mono"

# Calibrated point sizes, at 160 dpi.
TITLE_PT = 21.9
SUBTITLE_PT = 10.8
LETTER_PT = 9.3
BODY_PT = 8.5
FOOT_PT = 6.6
SIG_PT = 6.4

# Measured box metrics, in pixels.
PAD_LEFT = 19
LETTER_DROP = 10
BODY_DROP = 38
LINE_STEP = 25
PAD_BOTTOM = 28
BOX_PAD_RIGHT = 22
CORNER = 10


def box(ax, x, y, w, h, letter, lines, accent_letter=False):
    """A rounded box: a bold letter in the top-left corner, then monospace body."""
    ax.add_patch(FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0,rounding_size={CORNER}",
        facecolor=BOX_FILL, edgecolor=BOX_EDGE, linewidth=2, zorder=2))
    ax.text(x + PAD_LEFT, y + h - LETTER_DROP, letter, fontsize=LETTER_PT,
            weight="bold", color=ACCENT if accent_letter else INK, ha="left",
            va="top", family=SANS, zorder=3)
    ax.text(x + PAD_LEFT + 3, y + h - BODY_DROP, lines, fontsize=BODY_PT, color=INK,
            ha="left", va="top", family=MONO, linespacing=1.45, zorder=3)


def arrow(ax, x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1), zorder=1,
                arrowprops=dict(arrowstyle="-|>", color=BOX_EDGE, linewidth=1.8,
                                shrinkA=0, shrinkB=0, mutation_scale=15))


def box_height(n_lines: int) -> int:
    """Height a box needs for n body lines, from the measured metrics."""
    return BODY_DROP + (n_lines - 1) * LINE_STEP + 20 + PAD_BOTTOM


def main() -> None:
    fig = plt.figure(figsize=(W / DPI, H / DPI), dpi=DPI)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, W)
    ax.set_ylim(0, H)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((-10, -10), W + 20, H + 20, boxstyle="square,pad=0",
                                facecolor=PAPER, edgecolor="none", zorder=0))

    # ------------------------------------------------------------- title block
    ax.text(W / 2, 972, "Episode Pipeline", fontsize=TITLE_PT, weight="bold",
            color=INK, ha="center", va="center", family=SANS)
    ax.plot([690, 846], [936, 936], color=ACCENT, lw=4, solid_capstyle="butt")
    ax.text(W / 2, 900,
            "Eight stages in a fixed order, then two gates that can refuse the episode.",
            fontsize=SUBTITLE_PT, color="#333333", ha="center", va="center",
            family=SANS)

    # ----------------------------------------------------------- stage row one
    h = box_height(3)
    y1 = 748
    box(ax, 200, y1, 330, h, "A",
        "SOURCE\nsearch the host,\none query per shot need")
    box(ax, 560, y1, 330, h, "B",
        "PREFILTER\nresolution, aspect,\nduplicates")
    box(ax, 920, y1, 330, h, "C",
        "ROTCHECK\nsideways images,\ncorrected before select")
    arrow(ax, 530, y1 + h / 2, 560, y1 + h / 2)
    arrow(ax, 890, y1 + h / 2, 920, y1 + h / 2)

    # ----------------------------------------------------------- stage row two
    y2 = 560
    box(ax, 200, y2, 330, h, "D",
        "PREFILTER\nruns again, on purpose,\nafter rotation")
    box(ax, 560, y2, 330, h, "E",
        "SELECT\nthe model scores,\nthe person decides")
    box(ax, 920, y2, 330, h, "F",
        "CROP\ncut to the vertical\nmaster, 1080x1920")
    arrow(ax, 365, y1, 365, y2 + h)
    arrow(ax, 890, y2 + h / 2, 920, y2 + h / 2)

    # --------------------------------------------------------------- gate row
    hg = box_height(3)
    y3 = 372
    box(ax, 200, y3, 460, hg, "G",
        "FRAME GATE, first run\ncoverage: every shot need has a\nusable accepted candidate",
        accent_letter=True)
    box(ax, 700, y3, 460, hg, "H",
        "FRAME GATE, after crop\nprovenance: no two frames share\na source picture",
        accent_letter=True)
    arrow(ax, 530, y3 + hg / 2, 700, y3 + hg / 2)
    arrow(ax, 365, y2, 365, y3 + hg)
    arrow(ax, 1085, y2, 1085, y3 + hg)

    # -------------------------------------------------------------- final row
    hf = box_height(4)
    y4 = 160
    box(ax, 430, y4, 676, hf, "I",
        "VERIFY, BUILD, POST-RENDER GATE\nlook at every frame at full size, cut to the narration,\n"
        "then five checks on the finished file. Any one of them\nfails and the episode is refused, not published",
        accent_letter=True)
    arrow(ax, 430, y3, 620, y4 + hf)
    arrow(ax, 930, y3, 930, y4 + hf)

    # ----------------------------------------------------------------- footer
    ax.text(35, 40, "68 videos published across three channels, read on 24 November 2026.",
            fontsize=FOOT_PT, color=MUTED, ha="left", va="center", family=MONO)
    ax.text(1501, 40, "Taiwo Alabi", fontsize=SIG_PT, color=MUTED, ha="right",
            va="center", family=MONO)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT, dpi=DPI, facecolor=PAPER)
    plt.close(fig)
    print(f"wrote {OUT}  {W}x{H}")


if __name__ == "__main__":
    main()
