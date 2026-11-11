#!/usr/bin/env python3
"""Build the case study, process and gallery index routes.

Every route here groups existing verified artefacts. It does not create new
claims. Each page explains the difference between a case study, a process
walkthrough and a gallery before linking the evidence.
"""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent

COMMON_CSS = """
  .route-intro { max-width: 72ch; }
  .index-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 320px), 1fr)); gap: var(--space-5); margin-top: var(--space-6); }
  .index-card { background: var(--surface); border: 1px solid var(--border); border-left: 3px solid transparent; padding: var(--space-5); }
  .index-card:hover { border-left-color: var(--accent); }
  .index-card h2 { font-size: var(--text-xl); margin: var(--space-3) 0; }
  .index-card h3 { font-size: var(--text-base); margin: var(--space-4) 0 var(--space-2); }
  .index-card p, .index-card li { font-size: var(--text-sm); line-height: 1.65; }
  .index-card ul { padding-left: var(--space-5); }
  .index-card .cta { display: inline-block; margin-top: var(--space-3); font-size: var(--text-sm); }
  .definition { border: 1px solid var(--border); border-left: 3px solid var(--accent); padding: var(--space-5); margin: var(--space-6) 0; }
  .definition h2 { margin-top: 0; }
  .media-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 240px), 1fr)); gap: var(--space-4); margin-top: var(--space-6); }
  .media-card { border: 1px solid var(--border); padding: var(--space-4); background: var(--surface); }
  .media-card h2 { font-size: var(--text-lg); margin: var(--space-2) 0; }
  .media-card p { font-size: var(--text-sm); color: var(--text-3); }
  .media-card img { width: 100%; height: auto; display: block; margin-bottom: var(--space-3); }
"""


def page(title: str, description: str, active: str, body: str) -> str:
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | Taiwo Alabi</title>
<meta name="description" content="{description}">
<script>document.documentElement.setAttribute("data-theme",localStorage.getItem("tw-theme")||"")</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap">
<link rel="stylesheet" href="/assets/css/design-system.css">
<link rel="stylesheet" href="/assets/css/mark-zero.css">
<style>{COMMON_CSS}</style>
</head>
<body>
<nav class="util" aria-label="Site">
  <a href="/">index</a>
  <a href="/work/">work</a>
  <a href="/case-studies/"{' aria-current="page"' if active == 'cases' else ''}>cases</a>
  <a href="/process/"{' aria-current="page"' if active == 'process' else ''}>process</a>
  <a href="/gallery/"{' aria-current="page"' if active == 'gallery' else ''}>gallery</a>
  <a href="/cv/">cv</a>
  <a href="/products/">episodes</a>
</nav>
<main class="wrap">
  <header style="padding-top: var(--space-16)">
    <p class="eyebrow">{active}</p>
    <h1 class="claim-display">{title}</h1>
    <p class="route-intro">{description}</p>
  </header>
  <div class="rule"></div>
  {body}
  <div class="endcta">
    <a class="cta" href="/work/">Browse all 37 systems</a>
    <a class="cta cta-ghost" href="/cv/">See the Agent Foundations CV</a>
  </div>
</main>
</body>
</html>
'''


CASE_BODY = '''
<section class="definition">
  <h2>What a case study is</h2>
  <p>A case study explains one engineering decision from the problem through the mechanism, the measured result and the limit. It does not treat a working file as proof by itself. The reader should be able to check what was built, what it was compared against and what remains unproven.</p>
</section>
<section class="index-grid" aria-label="Published case studies">
  <article class="index-card">
    <span class="eyebrow">Contract analysis</span>
    <h2>TermsGuard AI</h2>
    <h3>The problem</h3>
    <p>Similarity alone can treat a sentence that says data is <em>not</em> sold in the same way as a sentence that says it is sold.</p>
    <h3>The decision</h3>
    <p>Rule checks run around the similarity result, and every flagged clause carries the reference material used to justify it.</p>
    <h3>The evidence</h3>
    <ul><li>102 hand-labelled reference clauses</li><li>4,527 searchable reference chunks</li><li>Matching-only fallback when the model service is unavailable</li></ul>
    <a class="cta cta-ghost" href="/p/termsguard/">Read the case study</a>
  </article>
  <article class="index-card">
    <span class="eyebrow">Clinical retrieval</span>
    <h2>Smart Medical Records</h2>
    <h3>The problem</h3>
    <p>A similarity search across many patients can return the wrong patient's note when both records use similar words.</p>
    <h3>The decision</h3>
    <p>The patient's identifier is applied before ranking, so other patients' notes are excluded before the model can read them.</p>
    <h3>The evidence</h3>
    <ul><li>30 adversarial probes designed to retrieve another patient's note</li><li>30 of 30 passed and zero leaked</li><li>Four services on one private network</li></ul>
    <a class="cta cta-ghost" href="/p/clinical-rag/">Read the case study</a>
  </article>
  <article class="index-card">
    <span class="eyebrow">Human escalation</span>
    <h2>Care Agent</h2>
    <h3>The problem</h3>
    <p>A wrong automatic route sends a customer to a team that cannot resolve the complaint.</p>
    <h3>The decision</h3>
    <p>The confidence gate sends uncertain tickets to a person instead of forcing every ticket into one of five categories.</p>
    <h3>The evidence</h3>
    <ul><li>210 labelled tickets, with 42 in each category</li><li>40 of 42 held-out tickets routed correctly</li><li>Confidence threshold of 0.55 before human escalation</li></ul>
    <a class="cta cta-ghost" href="/p/care-agent/">Read the case study</a>
  </article>
  <article class="index-card">
    <span class="eyebrow">Image quality</span>
    <h2>Image QA Gate</h2>
    <h3>The problem</h3>
    <p>An image can have the correct pose while showing the wrong identity. Accepting that image is the more serious error.</p>
    <h3>The decision</h3>
    <p>A Siamese network compares identity features, and the threshold was selected on validation data before the sealed test was opened.</p>
    <h3>The evidence</h3>
    <ul><li>90 sealed test pairs</li><li>Precision 1.00, recall 0.82 and F1 0.90</li><li>Pixel difference F1 0.59 and kNN F1 0.26 as simpler comparisons</li></ul>
    <a class="cta cta-ghost" href="/p/image-qa/">Read the case study</a>
  </article>
</section>
'''

PROCESS_BODY = '''
<section class="definition">
  <h2>What a process walkthrough is</h2>
  <p>A process walkthrough shows the order of work. It explains what enters the process, what each step changes, where a check refuses the result and what leaves the process. A pipeline is a sequence of automated steps. A workflow also includes the decisions and handovers made by people or services.</p>
</section>
<section class="index-grid" aria-label="Process walkthroughs">
  <article class="index-card">
    <span class="eyebrow">Production method</span>
    <h2>How I build things</h2>
    <p>This walkthrough explains the general method used across the media systems: define the failure, choose the gate, keep the evidence, and check the result before release.</p>
    <h3>What it shows</h3>
    <ul><li>The order of production steps</li><li>Where human review enters</li><li>Why the order is part of correctness</li></ul>
    <a class="cta cta-ghost" href="/how/">Open the walkthrough</a>
  </article>
  <article class="index-card">
    <span class="eyebrow">Episode pipeline</span>
    <h2>Episode production workflow</h2>
    <p>This page follows one short-form episode through source selection, frame filtering, rotation correction, model selection, cropping, verification and rendering. The order is fixed because a later check depends on an earlier correction.</p>
    <h3>What it shows</h3>
    <ul><li>Each pipeline stage and its input</li><li>The quality checks that can refuse a render</li><li>Contact sheets for the selected shots</li></ul>
    <a class="cta cta-ghost" href="/products/workflow/">Open the workflow</a>
  </article>
  <article class="index-card">
    <span class="eyebrow">Production specification</span>
    <h2>Episode blueprint</h2>
    <p>This specification records the production contract: what a shot must contain, how narration becomes timed beats, which checks run before rendering and what the finished file must contain.</p>
    <h3>What it shows</h3>
    <ul><li>The input and output contract</li><li>The gate sequence</li><li>The known failure modes</li></ul>
    <a class="cta cta-ghost" href="/products/blueprint.html">Open the blueprint</a>
  </article>
  <article class="index-card">
    <span class="eyebrow">Evaluation interface</span>
    <h2>Human rating systems</h2>
    <p>The rating interfaces let a reviewer compare candidates against a fixed rubric. They are tools for recording judgements, not proof that the chosen candidate is correct.</p>
    <h3>What it shows</h3>
    <ul><li>How a candidate enters the review</li><li>How a verdict is recorded</li><li>Why model agreement is not the same as validity</li></ul>
    <a class="cta cta-ghost" href="/rater/">Open the first rater</a>
  </article>
</section>
'''

GALLERY_BODY = '''
<section class="definition">
  <h2>What a gallery is here</h2>
  <p>This gallery groups evidence by what it proves. An architecture diagram shows how a system is separated. A confusion matrix shows which mistakes remained after a decision rule. A contact sheet shows which frames entered a video. A raw log shows that a scheduled job ran and recorded an outcome. Nothing is included only as decoration.</p>
</section>
<section class="media-grid" aria-label="Evidence galleries">
  <article class="media-card">
    <img src="/assets/img/rag_architecture.jpg" alt="Architecture diagram for the Smart Medical Records Engine" loading="lazy">
    <h2>Clinical architecture</h2>
    <p>Shows the API, database, model service, patient boundary and audit path used by the clinical retrieval system.</p>
    <a class="cta cta-ghost" href="/p/clinical-rag/">Open the case study</a>
  </article>
  <article class="media-card">
    <img src="/assets/img/fig2_confusion_matrix.jpg" alt="Confusion matrix for the customer care routing agent" loading="lazy">
    <h2>Routing confusion matrix</h2>
    <p>Shows which ticket categories the classifier confused during the held-out evaluation.</p>
    <a class="cta cta-ghost" href="/p/care-agent/">Open the case study</a>
  </article>
  <article class="media-card">
    <img src="/assets/img/roc_curves.jpg" alt="Receiver operating characteristic curves for the image quality gate" loading="lazy">
    <h2>Image QA curves</h2>
    <p>Shows how the acceptance threshold changed the balance between correct acceptances and missed pairs.</p>
    <a class="cta cta-ghost" href="/p/image-qa/">Open the case study</a>
  </article>
  <article class="media-card">
    <img src="/assets/img/tg_architecture.png" alt="Architecture diagram for TermsGuard AI" loading="lazy">
    <h2>Contract analysis architecture</h2>
    <p>Shows the first-stage classifier, reference retrieval, model verification and visible fallback path.</p>
    <a class="cta cta-ghost" href="/p/termsguard/">Open the case study</a>
  </article>
  <article class="media-card">
    <h2>Episode gallery</h2>
    <p>Published episodes, production stills, narration timing and the quality-check records for the rendered files.</p>
    <a class="cta cta-ghost" href="/products/">Open the episode gallery</a>
  </article>
  <article class="media-card">
    <h2>Process contact sheets</h2>
    <p>The selected frames for a short-form episode, shown as a sequence so the visual rhythm and repeated-frame checks can be inspected.</p>
    <a class="cta cta-ghost" href="/products/workflow/contact-sheets.html">Open the contact sheets</a>
  </article>
  <article class="media-card">
    <h2>Channel gallery</h2>
    <p>The creative channels built with the production pipeline, including the visual identity and published work for each channel.</p>
    <a class="cta cta-ghost" href="/channels/">Open the channel gallery</a>
  </article>
  <article class="media-card">
    <h2>Provenance logs</h2>
    <p>Raw evidence that scheduled work ran, media calls were recorded and evaluation decisions were written down.</p>
    <a class="cta cta-ghost" href="/provenance/">Open the logs</a>
  </article>
</section>
'''


def main() -> None:
    routes = {
        "case-studies/index.html": page("Case studies", "Four deep cases. Each one starts with the failure it prevents, then explains the mechanism, the measured result and the limit.", "cases", CASE_BODY),
        "process/index.html": page("Process walkthroughs", "The order of work, explained slowly. These pages show what enters each process, what changes at each step and where a check refuses the result.", "process", PROCESS_BODY),
        "gallery/index.html": page("Evidence gallery", "Diagrams, evaluation tables, episode stills, contact sheets and raw logs, grouped by the question each artefact can answer.", "gallery", GALLERY_BODY),
    }
    for relative, content in routes.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"built /{relative}")


if __name__ == "__main__":
    main()
