#!/usr/bin/env python3
"""Extract all live site content and links into one consolidated Markdown
file, for a full-site plain-language pass. Reads the built HTML directly,
not the live URL, since this repo IS the source of truth for what's live.

The page list is derived from the tracked files in this repo rather than
hardcoded, because a hardcoded list went stale once already: it still called
image-qa unpublished after that page went live, and it missed every route
added since. Deriving it means the export cannot claim to cover "all live
pages" while silently skipping some.

The output is a snapshot. The date it was generated is printed in the header
so a reader can see how old it is instead of assuming it is current.
"""
import subprocess
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).parent

# Order the export reads like the site does: the landing page, then the
# portfolio spine, then the project write-ups, then everything else.
PRIORITY = [
    "index.html",
    "cv/index.html",
    "work/index.html",
    "case-studies/index.html",
    "process/index.html",
    "gallery/index.html",
    "skim/index.html",
    "jobs/index.html",
    "study/index.html",
    "study/eeai/index.html",
    "p/termsguard/index.html",
    "p/clinical-rag/index.html",
    "p/care-agent/index.html",
    "p/image-qa/index.html",
]


def tracked_pages():
    """Every tracked HTML page in this repo, in reading order."""
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.splitlines()
    pages = [
        p
        for p in out
        if p.endswith("index.html") or p == "404.html"
    ]
    rank = {p: i for i, p in enumerate(PRIORITY)}
    return sorted(pages, key=lambda p: (rank.get(p, len(PRIORITY)), p))


def route(rel: str) -> str:
    if rel == "index.html":
        return "/"
    if rel == "404.html":
        return "/404.html"
    return "/" + rel[: -len("index.html")]


def extract(path: Path):
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    for tag in soup(["script", "style"]):
        tag.decompose()
    body = soup.body or soup
    lines = []
    for el in body.find_all(
        ["h1", "h2", "h3", "h4", "p", "li", "a", "div", "span", "button"]
    ):
        text = el.get_text(" ", strip=True)
        if not text:
            continue
        name = el.name
        if name in ("h1", "h2", "h3", "h4"):
            lines.append(f"\n{'#' * (int(name[1]) + 1)} {text}")
        elif name == "a" and el.get("href"):
            href = el["href"]
            lines.append(f"- LINK: [{text}]({href})")
        elif name in ("li", "p"):
            lines.append(text)
    # de-duplicate consecutive identical lines (nested tags repeat text)
    out = []
    for l in lines:
        if not out or out[-1] != l:
            out.append(l)
    return "\n".join(out)


def main():
    pages = tracked_pages()
    chunks = [
        "# Full site content export, all live pages\n\n",
        f"Generated on {date.today().isoformat()} directly from the built HTML in this "
        "repo, which is the source of truth for what's actually live. This is a "
        "snapshot: regenerate it with `python3 extract_site_content.py` after any "
        "copy change.\n",
    ]
    hidden = []
    for rel in pages:
        p = ROOT / rel
        if not p.exists():
            continue
        chunks.append(f"\n---\n\n## PAGE: {route(rel)}\n")
        chunks.append(extract(p))
    hidden = sorted(
        p.name
        for p in (ROOT / "p").iterdir()
        if p.is_dir() and not (p / "index.html").exists()
    )
    if hidden:
        chunks.append(
            f"\n---\n\nProject source exists but is not published: {', '.join(hidden)}"
            " - not included above because it is not on the site.\n"
        )
    out = "\n".join(chunks)
    out_path = ROOT / "SITE_CONTENT_EXPORT.md"
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote {out_path} ({len(out)} chars, {len(out.splitlines())} lines, "
          f"{len(pages)} pages)")
    if hidden:
        print(f"not published, so excluded: {', '.join(hidden)}")


if __name__ == "__main__":
    main()
