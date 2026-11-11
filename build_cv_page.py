#!/usr/bin/env python3
"""Build the website CV page from the Agent Foundations application CV.

The application Markdown is the single content source for this page and for
the downloadable PDF. The page adds navigation and a beginner glossary. It
does not rewrite the CV claims.
"""
from __future__ import annotations

import html
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = Path("/home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission/Taiwo_Alabi_CV_AgentFoundations.md")
OUT = ROOT / "cv" / "index.html"

GLOSSARY = [
    ("Agent", "A program that can choose and call tools to complete a task, rather than returning one fixed answer."),
    ("MCP", "Model Context Protocol, a standard that lets an AI application call tools through a defined interface."),
    ("RAG", "Retrieval-augmented generation. The system finds relevant source text before asking a model to answer from it."),
    ("Vector search", "A way of comparing records by the numerical meaning of their text, rather than only matching exact words."),
    ("Evaluation harness", "A controlled test that runs a system on known inputs and applies a fixed scoring rule."),
    ("Confidence gate", "A rule that sends an uncertain prediction to a person instead of forcing a decision."),
    ("Orchestration", "The layer that decides what runs, when it runs, and what happens when it fails."),
    ("Append-only ledger", "A record that adds new outcomes without changing earlier entries."),
]


def pandoc_html(markdown: Path) -> str:
    result = subprocess.run(
        ["pandoc", str(markdown), "-f", "markdown", "-t", "html5"],
        capture_output=True,
        text=True,
        check=True,
    )
    return result.stdout


def main() -> None:
    body = pandoc_html(SOURCE)
    # The source opens with the candidate name as a plain line, so promote that
    # first line to the page heading instead of repeating it.
    if body.startswith("<p>Taiwo Alabi</p>"):
        body = "<h1>Taiwo Alabi</h1>" + body[len("<p>Taiwo Alabi</p>"):]
    glossary = "".join(
        f"<div><dt>{html.escape(term)}</dt><dd>{html.escape(definition)}</dd></div>"
        for term, definition in GLOSSARY
    )
    doc = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent Foundations CV | Taiwo Alabi</title>
<meta name="description" content="Taiwo Alabi's application CV for Backend Engineer, Python, AI Engineering: Agent Foundations.">
<script>document.documentElement.setAttribute("data-theme",localStorage.getItem("tw-theme")||"")</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap">
<link rel="stylesheet" href="/assets/css/design-system.css">
<link rel="stylesheet" href="/assets/css/mark-zero.css">
<style>
  .cv-wrap {{ max-width: 900px; margin: 0 auto; padding: var(--space-6) var(--space-4) var(--space-16); }}
  .cv-actions {{ display: flex; gap: var(--space-3); flex-wrap: wrap; margin: var(--space-5) 0 var(--space-8); }}
  .cv-actions a {{ display: inline-block; padding: 10px 18px; border: 1px solid var(--border); text-decoration: none; font-weight: 700; }}
  .cv-actions a.primary {{ background: var(--accent); color: var(--bg); border-color: var(--accent); }}
  .cv-note {{ border: 1px solid var(--border); border-left: 3px solid var(--accent); padding: var(--space-5); margin: var(--space-6) 0; }}
  .cv-note h2 {{ margin-top: 0; }}
  .cv-glossary {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 250px), 1fr)); gap: var(--space-4); }}
  .cv-glossary dt {{ font-weight: 700; margin-bottom: var(--space-1); }}
  .cv-glossary dd {{ margin: 0; color: var(--text-3); font-size: var(--text-sm); }}
  .cv-body {{ max-width: 78ch; }}
  .cv-body h1 {{ font-size: var(--text-2xl); margin-bottom: var(--space-2); }}
  .cv-body h2 {{ font-size: var(--text-xl); margin: var(--space-10) 0 var(--space-4); padding-bottom: var(--space-2); border-bottom: 1px solid var(--border); }}
  .cv-body h3 {{ font-size: var(--text-base); margin: var(--space-6) 0 var(--space-2); }}
  .cv-body p, .cv-body li {{ font-size: var(--text-sm); line-height: 1.65; }}
  .cv-body ul {{ padding-left: var(--space-5); }}
  .cv-body li {{ margin-bottom: var(--space-2); }}
  .cv-body hr {{ margin: var(--space-8) 0; }}
  .cv-body a {{ color: var(--accent); }}
</style>
</head>
<body>
<nav class="util" aria-label="Site">
  <a href="/">index</a>
  <a href="/work/">work</a>
  <a href="/case-studies/">cases</a>
  <a href="/process/">process</a>
  <a href="/gallery/">gallery</a>
  <a href="/cv/" aria-current="page">cv</a>
  <a href="/products/">episodes</a>
  <a href="/how/">how</a>
  <a href="/provenance/">logs</a>
  <a href="/tools/">tools</a>
</nav>
<main class="cv-wrap">
  <div class="cv-actions">
    <a class="primary" href="/Alabi_Taiwo_CV.pdf" download>Download the Agent Foundations PDF</a>
    <a href="/work/">Browse all 37 systems</a>
  </div>
  <aside class="cv-note">
    <p class="eyebrow">How to read this CV</p>
    <h2>Terms used in the application</h2>
    <p>The CV keeps the exact wording used for applications. The definitions below explain the engineering terms for a reader who has not worked with AI systems.</p>
    <dl class="cv-glossary">{glossary}</dl>
  </aside>
  <article class="cv-body">
{body}
  </article>
  <div class="endcta">
    <a class="cta" href="mailto:newalabitaiwo625@gmail.com?subject=Agent%20Foundations%20application">Email Taiwo</a>
    <a class="cta cta-ghost" href="/work/">See the complete work index</a>
  </div>
</main>
</body>
</html>
'''
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(doc, encoding="utf-8")
    print(f"built {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
