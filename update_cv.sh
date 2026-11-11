#!/usr/bin/env bash
# One command to refresh the CV everywhere and publish it.
#
#   bash /home/newtazer/site-build/update_cv.sh          # build, verify, commit, push
#   bash /home/newtazer/site-build/update_cv.sh --no-push  # build and verify only
#
# Pipeline:
#   master Markdown -> docx -> verified PDF -> site CV page -> site PDFs
#   -> generated pages -> verification gate -> commit and push both repos
#
# The master file is the only place CV content is edited:
#   /home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission/
#     Taiwo_Alabi_CV_AgentFoundations.md
#
# Nothing here touches the stale generator at "CV VARIANTS/build_cv.py" and
# nothing hand-edits a generated page under p/*/index.html.

set -euo pipefail

RESEARCH="/home/newtazer/Desktop/NCI/2ND/IMAGE VID GEN/research/ca2_submission"
SITE="/home/newtazer/site-build"
CVVARIANTS="/home/newtazer/Desktop/NCI/CV VARIANTS"

STEM="Taiwo_Alabi_CV_AgentFoundations"
MASTER="$RESEARCH/$STEM.md"
DOCX="$RESEARCH/$STEM.docx"
PDF="$RESEARCH/$STEM.pdf"
REF_DOCX="$RESEARCH/cv_build/reference.docx"

PUSH=1
if [[ "${1:-}" == "--no-push" ]]; then
  PUSH=0
fi

say() { printf '\n== %s\n' "$1"; }
die() { printf '\nFAILED: %s\n' "$1" >&2; exit 1; }

# ---------------------------------------------------------------- preflight
say "Preflight"
[[ -f "$MASTER" ]] || die "master file missing: $MASTER"
[[ -f "$REF_DOCX" ]] || die "pandoc reference doc missing: $REF_DOCX"
for tool in pandoc google-chrome python3 git; do
  command -v "$tool" >/dev/null 2>&1 || die "missing tool: $tool"
done
[[ -d "$SITE/.git" ]] || die "site repo not found: $SITE"
[[ -d "$RESEARCH/.git" ]] || die "research repo not found: $RESEARCH"
echo "master: $MASTER"

# ------------------------------------------------------------- docx and pdf
say "Build the docx"
pandoc "$MASTER" -f markdown -t docx --reference-doc="$REF_DOCX" -o "$DOCX"
echo "wrote $DOCX"

say "Build the PDF (verification gate runs inside)"
python3 "$RESEARCH/cv_build/build_cv.py" "$MASTER" --out "$PDF"

# --------------------------------------------------------------- copy files
say "Copy the CV where the site and the variants folder expect it"
cp "$PDF" "$SITE/Alabi_Taiwo_CV.pdf"
cp "$PDF" "$SITE/assets/Taiwo_Alabi_CV.pdf"
cp "$DOCX" "$CVVARIANTS/Alabi_Taiwo_CV_AgentFoundations.docx"
cp "$PDF" "$CVVARIANTS/Alabi_Taiwo_CV_AgentFoundations.pdf"

# ------------------------------------------------------------ site rebuilds
say "Rebuild the generated site pages"
cd "$SITE"
python3 build_work_index.py     # /work/ from the verified inventory
python3 build_indexes.py        # /case-studies/, /process/, /gallery/
python3 build_cv_page.py        # /cv/ from the same master Markdown
python3 build.py                # project pages and 404.html

# ------------------------------------------------------------------ verify
say "Verify"
python3 - "$SITE" "$PDF" <<'PY'
import subprocess, sys
from pathlib import Path

site = Path(sys.argv[1])
pdf = Path(sys.argv[2])
failures = []

# PDF gate: page count, contact line, dashes, placeholders
text = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
pages = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout
page_count = next((int(line.split(":")[1]) for line in pages.splitlines() if line.startswith("Pages:")), 0)
if page_count not in (1, 2):
    failures.append(f"PDF page count is {page_count}")
if "newalabitaiwo625@gmail.com" not in text:
    failures.append("PDF is missing the current contact email")
if "alabitaiwo625@gmail.com" in text.replace("newalabitaiwo625@gmail.com", ""):
    failures.append("PDF still carries the stale email")
for dash in ("\u2014", "\u2013"):
    if dash in text:
        failures.append(f"PDF contains a {'em' if dash == chr(0x2014) else 'en'} dash")
if "{{" in text:
    failures.append("PDF contains an unfilled placeholder")

# generated pages exist and carry a heading
for route in ("cv", "work", "case-studies", "process", "gallery"):
    page = site / route / "index.html"
    if not page.exists():
        failures.append(f"/{route}/ was not built")
    elif "<h1" not in page.read_text(encoding="utf-8"):
        failures.append(f"/{route}/ has no h1")

# no machine paths leaked into the public pages
for route in ("cv", "work", "case-studies", "process", "gallery", "skim"):
    page = site / route / "index.html"
    if page.exists():
        body = page.read_text(encoding="utf-8")
        for needle in ("/home/newtazer", "/mnt/2tb"):
            if needle in body:
                failures.append(f"/{route}/ leaks the path {needle}")

if failures:
    print("VERIFICATION FAILED")
    for item in failures:
        print(f"  - {item}")
    raise SystemExit(1)
print(f"verification passed: PDF {page_count} page(s), routes built, no leaked paths")
PY

# --------------------------------------------------------------- commit/push
say "Commit and push"
cd "$RESEARCH"
git add "$STEM.md" "$STEM.docx" "$STEM.pdf" cv_build/reference.docx
if ! git diff --cached --quiet; then
  git commit -m "Refresh the Agent Foundations CV from the master Markdown"
  echo "research repo committed"
else
  echo "research repo: nothing to commit"
fi

cd "$SITE"
git add Alabi_Taiwo_CV.pdf assets/Taiwo_Alabi_CV.pdf cv/index.html work/index.html \
  case-studies/index.html process/index.html gallery/index.html 404.html index.html skim/index.html \
  tools/index.html build_cv_page.py update_cv.sh
if ! git diff --cached --quiet; then
  git commit -m "Refresh the CV and the published indexes"
  echo "site repo committed"
else
  echo "site repo: nothing to commit"
fi

if [[ "$PUSH" == "1" ]]; then
  git push origin main
  cd "$RESEARCH"
  git push origin main
  echo "pushed both repos"
else
  echo "skipped push (--no-push)"
fi

say "Done"
echo "Master file: $MASTER"
echo "Live CV page: https://iamtamilore.github.io/cv/"
echo "Live PDF: https://iamtamilore.github.io/Alabi_Taiwo_CV.pdf"
