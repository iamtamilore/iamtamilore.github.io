"""Build the project pages from the same markdown that produces the PDFs.

One source per project. Run this after editing any README.
"""
import os
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# where the project READMEs live locally; override with SYMPLICITY_SRC if needed
SRC = Path(os.environ.get("SYMPLICITY_SRC", Path.home() / "Desktop/NCI/CV VARIANTS/symplicity"))

# slug, source README, page title, og description, and how each image name maps
PROJECTS = [
    dict(slug="image-qa", src=SRC / "imageqa/README.md",
         title="Image QA Gate",
         desc="Catches the moment an AI-generated model stops being the same person. "
              "F1 0.90, zero false positives.",
         card="image_qa.jpg",
         imgmap={"architecture.png": "architecture.jpg",
                 "roc_curves.png": "roc_curves.jpg",
                 "cm_siamese.png": "cm_siamese.jpg",
                 "fn_siamese.png": "fn_siamese.jpg",
                 "grade_drift_examples.png": "grade_drift_examples.jpg"}),

    dict(slug="care-agent", src=SRC / "careagent/README.md",
         title="Care Agent",
         desc="Complaint routing at 95.2% accuracy, with a confidence gate that escalates "
              "rather than guesses.",
         card="care_agent.jpg",
         imgmap={"as_is.png": "as_is.jpg", "to_be.png": "to_be.jpg",
                 "fig1_classification_report.png": "fig1_classification_report.png",
                 "fig2_confusion_matrix.png": "fig2_confusion_matrix.jpg",
                 "fig3_rpa_validation.png": "fig3_rpa_validation.jpg",
                 "fig4_confidence_scores.png": "fig4_confidence_scores.png"}),

    dict(slug="termsguard", src=SRC / "termsguard/README.md",
         title="TermsGuard AI",
         desc="Reads the small print and flags what is unfair to you, grounded in GDPR. "
              "87% F1, live on the internet.",
         card="termsguard.jpg",
         imgmap={"TermsGuard_architecture.png": "tg_architecture.jpg"}),

    dict(slug="surge-pricing", src=SRC / "surgepricing/README.md",
         title="RL vs Genetic Algorithm",
         desc="Two ways to learn a surge pricing policy, tested on 637,976 real Boston "
              "ride records. GA +21.4% over fixed pricing.",
         card="surge_pricing.jpg",
         imgmap={"3_revenue_comparison.png": "3_revenue_comparison.jpg",
                 "1_rl_learning_curve.png": "1_rl_learning_curve.jpg",
                 "2_ga_fitness_curve.png": "2_ga_fitness_curve.jpg",
                 "4_policy_heatmaps.png": "4_policy_heatmaps.jpg"}),

    dict(slug="clinical-rag", src=SRC / "clinicalrag/README.md",
         title="Smart Medical Records",
         desc="A doctor asks in plain English and gets an answer from that patient's own "
              "notes. Self-hosted, scoped, audited.",
         card="clinical_rag.jpg",
         imgmap={"architecture.png": "rag_architecture.jpg",
                 "data_model.png": "rag_data_model.jpg"}),
]

# labelled links shown under the title on each project page
RESOURCES = {
 "image-qa": [("Full write-up", "/assets/docs/image_qa_writeup.pdf", "pdf"),
              ("Source code", "https://github.com/iamtamilore/campaign-image-qa", "")],
 "care-agent": [("Full write-up", "/assets/docs/care_agent_writeup.pdf", "pdf"),
                ("Source code", "https://github.com/iamtamilore/customer-care-automation", "")],
 "termsguard": [("Live demo", "https://newtazer-terms-guard-ai.hf.space", "live"),
                ("Full write-up", "/assets/docs/termsguard_writeup.pdf", "pdf"),
                ("Source code", "https://github.com/iamtamilore/terms-guard-ai", "")],
 "clinical-rag": [("Full write-up", "/assets/docs/clinical_rag_writeup.pdf", "pdf"),
                  ("Source code", "https://github.com/iamtamilore/agentic_rag_fastapi", "")],
 "surge-pricing": [("Watch the walkthrough", "https://youtu.be/Q_6xYLD4ykA", "video"),
                   ("Full report", "/assets/docs/surge_pricing_report.pdf", "pdf"),
                   ("Slides", "/assets/docs/surge_pricing_slides.pdf", "pdf")],
}


def resource_strip(slug):
    items = []
    for label, href, kind in RESOURCES.get(slug, []):
        if kind == "live":
            # the one place a project page mirrors the homepage's solid CTA:
            # "try the running software" gets the same visual weight both times.
            items.append(f'<a class="cta" href="{href}" target="_blank" rel="noopener">{label}</a>')
        else:
            tag = f'<span class="tag">{kind}</span>' if kind else ""
            items.append(f'<a href="{href}">{label}{tag}</a>')
    return '<div class="resources">' + "".join(items) + "</div>" if items else ""


# headline numbers for the 45-second skimmer, shown before any narrative prose.
# care-agent keeps the honest eval-set size (42) rather than softening it away -
# hiding it here while the CV states a different number would read as evasive.
METRICS = {
 "image-qa": ["precision 1.00", "0 false passes in 90 sealed pairs", "133ms per image"],
 "care-agent": ["95.2% routing accuracy (40 of 42 held-out)", "escalates below 0.55",
                "2 manual processes replaced"],
 "termsguard": ["87% F1", "hallucination rate cut 77%", "latency 28s to under 10s"],
 "clinical-rag": ["0/30 leak probes succeeded", "every access logged",
                   "scoped by patient before ranking"],
 "surge-pricing": ["+21.4% revenue vs fixed pricing", "637,976 real records",
                    "both methods converged on the same policy"],
}


def metrics_strip(slug):
    stats = METRICS.get(slug, [])
    if not stats:
        return ""
    items = "".join(f'<span class="stat">{s}</span>' for s in stats)
    return '<div class="stats-strip">' + items + "</div>"


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Taiwo Alabi</title>
<meta name="description" content="{desc}">
<script>document.documentElement.setAttribute("data-theme",localStorage.getItem("tw-theme")||"g5")</script>
<link rel="stylesheet" href="/assets/css/style.css">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%232E2C6E'/><text y='72' x='50' font-size='62' text-anchor='middle' fill='%23FF7A3D' font-family='sans-serif' font-weight='bold'>T</text></svg>">
<meta property="og:title" content="{title} | Taiwo Alabi">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://iamtamilore.github.io/assets/img/{card}">
<meta property="og:url" content="https://iamtamilore.github.io/p/{slug}/">
<meta property="og:type" content="article">
<meta name="twitter:card" content="summary_large_image">
</head>
<body>
<nav class="util" aria-label="Personal">
  <a href="/study/eeai/">study</a>
  <a href="/jobs/">tracker</a>
  <a href="/bank-pwa/">bank</a>
</nav>
<div class="topbar">
  <a href="/cv/">&larr; Back to CV</a>
  <a href="/">All work</a>
</div>
<div class="wrap">
{body}
<div class="endnav">
  <a class="cta cta-ghost" href="/cv/">&larr; Back to CV</a>
  <a class="cta cta-ghost" href="/">All work</a>
</div>
<footer>
  <div>Taiwo Alabi &middot; <a href="mailto:alabitaiwo625@gmail.com">alabitaiwo625@gmail.com</a>
   &middot; <a href="https://www.linkedin.com/in/tami-alabi/">LinkedIn</a>
   &middot; <a href="https://github.com/iamtamilore">GitHub</a></div>
</footer>
</div>

<div class="theme-picker" role="group" aria-label="colour theme">
  <button type="button" class="theme-dot" data-set-theme="g5" style="--sw:#ff7a3d" title="G5 Tri-X" aria-pressed="true"></button>
  <button type="button" class="theme-dot" data-set-theme="teal" style="--sw:#3fc2b4" title="Teal &amp; Orange" aria-pressed="false"></button>
  <button type="button" class="theme-dot" data-set-theme="contact" style="--sw:#b8541f" title="Contact Sheet" aria-pressed="false"></button>
  <button type="button" class="theme-dot" data-set-theme="cyano" style="--sw:#175a9c" title="Cyanotype" aria-pressed="false"></button>
</div>
<script>
(function () {{
  var K = "tw-theme", R = document.documentElement;
  function M() {{
    var c = R.getAttribute("data-theme") || "g5";
    var d = document.querySelectorAll("[data-set-theme]");
    for (var i = 0; i < d.length; i++) {{
      d[i].setAttribute("aria-pressed", d[i].getAttribute("data-set-theme") === c ? "true" : "false");
    }}
  }}
  document.addEventListener("click", function (e) {{
    var b = e.target.closest ? e.target.closest("[data-set-theme]") : null;
    if (!b) return;
    var t = b.getAttribute("data-set-theme");
    R.setAttribute("data-theme", t);
    localStorage.setItem(K, t);
    M();
  }});
  M();
}})();
</script>
</body>
</html>
"""


def reading_time(path: Path) -> int:
    """Minutes at 220 words per minute, the usual figure for technical prose."""
    words = len(re.findall(r"[A-Za-z][A-Za-z'-]*", path.read_text(encoding="utf8")))
    return max(1, round(words / 220))


def md_to_html(path: Path) -> str:
    return subprocess.run(
        ["pandoc", str(path), "-f", "gfm", "-t", "html5"],
        capture_output=True, text=True, check=True).stdout


def transform(html: str, imgmap: dict) -> str:
    # point images at the optimised copies in /assets/img/
    for old, new in imgmap.items():
        html = html.replace(f'src="{old}"', f'src="/assets/img/{new}"')

    # every image becomes tap-to-open-full-size, with its caption below
    def fig(m):
        src, alt = m.group("src"), m.group("alt")
        return (f'<figure><a href="{src}" target="_blank" rel="noopener">'
                f'<img src="{src}" alt="{alt}" loading="lazy"></a>')
    html = re.sub(r'<p><img src="(?P<src>[^"]+)" alt="(?P<alt>[^"]*)"[^>]*>\s*'
                  r'<em>(?P<cap>.*?)</em></p>',
                  lambda m: fig(m) + f'<figcaption>{m.group("cap")}</figcaption></figure>',
                  html, flags=re.S)
    html = re.sub(r'<p><img src="(?P<src>[^"]+)" alt="(?P<alt>[^"]*)"[^>]*></p>',
                  lambda m: fig(m) + '</figure>', html)

    # tables scroll horizontally on a phone instead of breaking the layout
    html = html.replace("<table>", '<div class="tablewrap"><table>')
    html = html.replace("</table>", "</table></div>")

    # style the contents block
    # pandoc emits <ol type="1">, so match any attributes
    html = re.sub(r'<h2 id="contents">Contents</h2>\s*<ol[^>]*>',
                  '<div class="toc"><h3 style="margin-top:0">Contents</h3><ol>', html, count=1)
    html = re.sub(r'</ol>\s*<hr />', '</ol></div>', html, count=1)

    # the h1 gets the accent rule above it, matching the home page
    html = html.replace("<h1", '<hr class="rule"><h1', 1)
    return html


def main():
    for p in PROJECTS:
        if not p["src"].exists():
            print(f"  MISSING {p['src']}")
            continue
        body = transform(md_to_html(p["src"]), p["imgmap"])
        # a stated reading time lowers the barrier to starting
        mins = reading_time(p["src"])
        body = body.replace("</h1>", f'</h1>\n<p class="readtime">{mins} min read</p>', 1)
        out_dir = ROOT / "p" / p["slug"]
        out_dir.mkdir(parents=True, exist_ok=True)
        # headline numbers go right after the subtitle, before the reader hits
        # the Contents block or any narrative prose - the 45-second skimmer's entrance
        mstrip = metrics_strip(p["slug"])
        if mstrip:
            body = re.sub(r'(<p><strong>.*?</strong></p>)', r'\1' + mstrip, body, count=1, flags=re.S)
        # resource links sit directly under the intro, before the contents block
        strip = resource_strip(p["slug"])
        if strip:
            body = body.replace('</ol></div>', '</ol></div>' + strip, 1)
        (out_dir / "index.html").write_text(
            TEMPLATE.format(title=p["title"], desc=p["desc"], card=p["card"],
                            slug=p["slug"], body=body), encoding="utf8")
        print(f"  built /p/{p['slug']}/")


if __name__ == "__main__":
    main()
