#!/usr/bin/env python3
"""Extract all live site content and links into one consolidated Markdown
file, for a full-site plain-language pass. Reads the built HTML directly,
not the live URL, since this repo IS the source of truth for what's live."""
import re
from pathlib import Path
from bs4 import BeautifulSoup

ROOT = Path(__file__).parent
PAGES = [
    ("index.html", "/"),
    ("cv/index.html", "/cv/"),
    ("jobs/index.html", "/jobs/"),
    ("study/index.html", "/study/"),
    ("study/eeai/index.html", "/study/eeai/"),
    ("p/termsguard/index.html", "/p/termsguard/"),
    ("p/clinical-rag/index.html", "/p/clinical-rag/"),
    ("p/care-agent/index.html", "/p/care-agent/"),
    ("404.html", "/404.html"),
]

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
    chunks = ["# Full site content export, all live pages\n"]
    chunks.append(
        "Generated directly from the built HTML in this repo, which is the "
        "source of truth for what's actually live. Two projects exist as "
        "source content but are not published: image-qa, surge-pricing - "
        "not included here since they're not on the site.\n"
    )
    for rel, url in PAGES:
        p = ROOT / rel
        if not p.exists():
            continue
        chunks.append(f"\n---\n\n## PAGE: {url}\n")
        chunks.append(extract(p))
    out = "\n".join(chunks)
    out_path = ROOT / "SITE_CONTENT_EXPORT.md"
    out_path.write_text(out, encoding="utf-8")
    print(f"wrote {out_path} ({len(out)} chars, {len(out.splitlines())} lines)")

if __name__ == "__main__":
    main()
