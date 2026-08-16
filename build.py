"""Build the project pages from the same markdown that produces the PDFs.

One source per project. Run this after editing any README.
"""
import os
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# where the project READMEs live locally; override with SYMPLICITY_SRC if needed
SRC = Path(os.environ.get("SYMPLICITY_SRC", Path.home() / "Desktop/NCI/CV VARIANTS/symplicity"))

# slug, source README, page title, og description, and how each image name maps
# published=False hides a project completely: no page is built, any previously
# built page is removed, and no card is emitted on the home page. Used while
# coursework is still being graded. Flip to True to bring one back.
# blurb is the one-line subtitle used by the prev/next navigation.
# cmetric/clabel/cdesc/clive/ccta/clinks drive the home page card, so the
# published flag cannot leave an orphaned link behind.
PROJECTS = [
    dict(slug="termsguard", src=SRC / "termsguard/README.md",
         title="TermsGuard AI",
         desc="Reads the small print and flags what is unfair to you, grounded in GDPR. "
              "87% F1, live on the internet.",
         card="termsguard.jpg",
         published=True,
         blurb="grounding against hallucination",
         cmetric="87%", clabel="F1, with invented content cut 77%",
         cdesc="Reads the small print and flags what is unfair to you, grounded in\n"
               "        4,527 chunks of GDPR text. Deployed and publicly reachable.",
         clive=True,
         ccta=("Try the live demo", "https://newtazer-terms-guard-ai.hf.space"),
         clinks=[("Code", "https://github.com/iamtamilore/terms-guard-ai")],
         imgmap={"TermsGuard_architecture.png": "tg_architecture.jpg"}),

    dict(slug="clinical-rag", src=SRC / "clinicalrag/README.md",
         title="Smart Medical Records",
         desc="A doctor asks in plain English and gets an answer from that patient's own "
              "notes. Self-hosted, scoped, audited.",
         card="clinical_rag.jpg",
         published=True,
         blurb="wrong-patient retrieval",
         cmetric="on site", clabel="patient data never leaves the network",
         cdesc="A doctor asks a question in plain English and gets an answer from that\n"
               "        patient's own notes. Self-hosted, scoped, audited.",
         clive=False, ccta=None,
         clinks=[("Code", "https://github.com/iamtamilore/agentic_rag_fastapi")],
         imgmap={"architecture.png": "rag_architecture.jpg",
                 "data_model.png": "rag_data_model.jpg"}),

    dict(slug="care-agent", src=SRC / "careagent/README.md",
         title="Care Agent",
         desc="Complaint routing at 95.2% accuracy, with a confidence gate that escalates "
              "rather than guesses.",
         card="care_agent.jpg",
         published=True,
         blurb="the confidence gate",
         cmetric="95.2%", clabel="routing accuracy, 40 of 42 held-out",
         cdesc="Two bots replacing two manual back-office jobs on a mobile network. The\n"
               "        interesting part is when it refuses to decide.",
         clive=False, ccta=None,
         clinks=[("Code", "https://github.com/iamtamilore/customer-care-automation")],
         imgmap={"as_is.png": "as_is.jpg", "to_be.png": "to_be.jpg",
                 "fig1_classification_report.png": "fig1_classification_report.png",
                 "fig2_confusion_matrix.png": "fig2_confusion_matrix.jpg",
                 "fig3_rpa_validation.png": "fig3_rpa_validation.jpg",
                 "fig4_confidence_scores.png": "fig4_confidence_scores.png"}),

    dict(slug="image-qa", src=SRC / "imageqa/README.md",
         title="Image QA Gate",
         desc="Catches the moment an AI-generated model stops being the same person. "
              "F1 0.90, zero false positives.",
         card="image_qa.jpg",
         published=False,
         blurb="which error to make",
         cmetric="zero", clabel="false alarms in 90 test pairs",
         cdesc="Catches the moment an AI-generated model stops being the same person.\n"
               "        Siamese network on a frozen ResNet50, plus an autoencoder for colour drift.",
         clive=False, ccta=None,
         clinks=[("Code", "https://github.com/iamtamilore/campaign-image-qa")],
         imgmap={"architecture.png": "architecture.jpg",
                 "roc_curves.png": "roc_curves.jpg",
                 "cm_siamese.png": "cm_siamese.jpg",
                 "fn_siamese.png": "fn_siamese.jpg",
                 "grade_drift_examples.png": "grade_drift_examples.jpg"}),

    dict(slug="surge-pricing", src=SRC / "surgepricing/README.md",
         title="RL vs Genetic Algorithm",
         desc="Two ways to learn a surge pricing policy, tested on 637,976 real Boston "
              "ride records. GA +21.4% over fixed pricing.",
         card="surge_pricing.jpg",
         published=False,
         blurb="the baseline nobody sets",
         cmetric="+21.4%", clabel="revenue over fixed pricing",
         cdesc="Two ways to learn a surge pricing policy, tested against each other\n"
               "        on 637,976 real Boston ride records. Both found the same structure.",
         clive=False, ccta=None,
         clinks=[("Walkthrough", "https://youtu.be/Q_6xYLD4ykA"),
                 ("Report", "/assets/docs/surge_pricing_report.pdf")],
         imgmap={"3_revenue_comparison.png": "3_revenue_comparison.jpg",
                 "1_rl_learning_curve.png": "1_rl_learning_curve.jpg",
                 "2_ga_fitness_curve.png": "2_ga_fitness_curve.jpg",
                 "4_policy_heatmaps.png": "4_policy_heatmaps.jpg"}),
]

# labelled links shown under the title on each project page
RESOURCES = {
# labels name the reader's intent, not the artefact type, so each visitor can
# find their own link in one pass: recruiter tries it, manager reads it,
# engineer checks the code.
 "image-qa": [("Read the detail", "/assets/docs/image_qa_writeup.pdf", "pdf"),
              ("Check the code", "https://github.com/iamtamilore/campaign-image-qa", "")],
 "care-agent": [("Read the detail", "/assets/docs/care_agent_writeup.pdf", "pdf"),
                ("Check the code", "https://github.com/iamtamilore/customer-care-automation", "")],
 "termsguard": [("Try it", "https://newtazer-terms-guard-ai.hf.space", "live"),
                ("Read the detail", "/assets/docs/termsguard_writeup.pdf", "pdf"),
                ("Check the code", "https://github.com/iamtamilore/terms-guard-ai", "")],
 "clinical-rag": [("Read the detail", "/assets/docs/clinical_rag_writeup.pdf", "pdf"),
                  ("Check the code", "https://github.com/iamtamilore/agentic_rag_fastapi", "")],
 "surge-pricing": [("Watch it", "https://youtu.be/Q_6xYLD4ykA", "video"),
                   ("Read the detail", "/assets/docs/surge_pricing_report.pdf", "pdf"),
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
 "care-agent": ["escalates rather than guesses, below 0.55",
                "95.2% on 40 of 42 held-out tickets",
                "2 manual processes replaced"],
 "termsguard": ["invented content cut 77%", "87% F1 on unfair-clause detection",
                "latency 28s to under 10s"],
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


def published(projects=None):
    return [p for p in (projects or PROJECTS) if p["published"]]


def card_html(p):
    """One home page card, matching the hand-written markup exactly.

    Cards are generated rather than hand-maintained so that hiding a project
    cannot leave a live link pointing at a page that no longer exists.
    """
    live = ' <span class="live">Live</span>' if p["clive"] else ""
    cta = ""
    if p["ccta"]:
        label, href = p["ccta"]
        cta = ('\n      <a class="cta" style="position:relative;z-index:2" '
               f'href="{href}" target="_blank" rel="noopener">{label}</a>')
    sep = '<span aria-hidden="true">|</span>'
    links = sep.join(f'<a href="{h}">{l}</a>' for l, h in p["clinks"])
    return (f'''    <div class="card" id="{p['slug']}">
      <div class="metric">{p['cmetric']}</div>
      <div class="metric-label">{p['clabel']}</div>
      <div class="title">{p['title']}{live}</div>
      <div class="desc">{p['cdesc']}</div>
      <div class="go"><a class="stretch" href="/p/{p['slug']}/">Read it &rarr;</a></div>{cta}
    <div class="cardlinks">{links}</div></div>''')


def update_index_cards():
    """Rewrite only what sits between the CARDS markers in the home page."""
    path = ROOT / "index.html"
    text = path.read_text(encoding="utf8")
    start, end = "<!-- CARDS:START -->", "<!-- CARDS:END -->"
    i, j = text.find(start), text.find(end)
    if i == -1 or j == -1:
        print(f"  SKIPPED index.html: add {start} and {end} around the card grid")
        return
    cards = "\n\n".join(card_html(p) for p in published())
    path.write_text(text[:i + len(start)] + "\n\n" + cards + "\n\n  " + text[j:],
                    encoding="utf8")
    print(f"  rewrote index.html cards ({len(published())} shown)")


def lateral_nav(slug):
    """Previous and next across published projects only.

    No wrapping. The last project points at the CV on purpose: finish the
    evidence, land on the ask.
    """
    pub = published()
    idx = next(i for i, p in enumerate(pub) if p["slug"] == slug)
    left = ""
    if idx > 0:
        q = pub[idx - 1]
        left = (f'<a class="latnav prev" href="/p/{q["slug"]}/">&larr; {q["title"]}'
                f'<span>{q["blurb"]}</span></a>')
    if idx < len(pub) - 1:
        q = pub[idx + 1]
        right = (f'<a class="latnav next" href="/p/{q["slug"]}/">{q["title"]} &rarr;'
                 f'<span>{q["blurb"]}</span></a>')
    else:
        right = ('<a class="latnav next" href="/cv/">CV &rarr;'
                 '<span>the short version</span></a>')
    return f'<div class="lateral">{left}{right}</div>'


TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Taiwo Alabi</title>
<meta name="description" content="{desc}">
<script>document.documentElement.setAttribute("data-theme",localStorage.getItem("tw-theme")||"g5")</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;600;700;800&display=swap">
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
<div class="topbar">
  <a href="/#{slug}">&larr; All work</a>
</div>
<div class="wrap">
{body}
{latnav}
<div class="endnav">
  <a class="cta cta-ghost" href="/#{slug}">&larr; All work</a>
  <a class="cta cta-ghost" href="/cv/">CV</a>
  <a class="cta cta-ghost" href="https://github.com/iamtamilore">GitHub</a>
</div>
<footer>
  <div>Taiwo Alabi &middot; <a href="mailto:alabitaiwo625@gmail.com">alabitaiwo625@gmail.com</a>
   &middot; <a href="https://www.linkedin.com/in/tami-alabi/">LinkedIn</a>
   &middot; <a href="https://github.com/iamtamilore">GitHub</a></div>
  <div class="util-footer"><a href="/study/eeai/">study</a>
   &middot; <a href="/jobs/">tracker</a>
   &middot; <a href="/bank-pwa/">bank</a></div>
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
    hidden = []
    for p in PROJECTS:
        out_dir = ROOT / "p" / p["slug"]
        if not p["published"]:
            # remove any page built while this project was still published,
            # otherwise the old page stays reachable by direct URL
            if out_dir.exists():
                shutil.rmtree(out_dir)
                print(f"  removed /p/{p['slug']}/ (unpublished)")
            hidden.append(p["slug"])
            continue
        if not p["src"].exists():
            print(f"  MISSING {p['src']}")
            continue
        body = transform(md_to_html(p["src"]), p["imgmap"])
        # a stated reading time lowers the barrier to starting
        mins = reading_time(p["src"])
        body = body.replace("</h1>", f'</h1>\n<p class="readtime">{mins} min read</p>', 1)
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
                            slug=p["slug"], body=body,
                            latnav=lateral_nav(p["slug"])), encoding="utf8")
        print(f"  built /p/{p['slug']}/")

    update_index_cards()
    print(f"published: {len(published())}  |  hidden: {', '.join(hidden) or 'none'}")


if __name__ == "__main__":
    main()
