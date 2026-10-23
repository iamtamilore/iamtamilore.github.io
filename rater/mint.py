#!/usr/bin/env python3
"""Mint per-rater invite URLs for the static rater UI.

Usage:
  python3 mint.py alice bob carol
  python3 mint.py -f raters.txt          # one rater name per line
  python3 mint.py --base https://iamtamilore.github.io/rater
  python3 mint.py --out raters_log.csv

Each rater gets:
  rater_id   - human-readable label, becomes the ?rater= URL parameter
  token      - random 32-char URL-safe secret, the ?token= URL parameter
  url        - the full invite URL you send

The CSV is the log. Rows are append-only; existing rater_ids are skipped
unless --force is passed. If you want to roll a token for an existing
rater (e.g. they lost their link), re-run without --force to skip, then
add a new row with --force.

Tokens are random 32-char strings from secrets.token_urlsafe. The token
is the URL's only secret; if lost, the rater starts over. For thesis
use this is fine - reroll and resend the link.

NOTE: the CSV contains tokens. Don't commit it to a public repo unless
you accept that anyone reading the repo can submit as any rater. Keep
the file local, or gitignore it, or commit a redacted copy.
"""

from __future__ import annotations

import argparse
import csv
import re
import secrets
import sys
from pathlib import Path

DEFAULT_BASE = "https://iamtamilore.github.io/rater"
DEFAULT_OUT = Path(__file__).parent / "raters_log.csv"
TOKEN_LEN = 32
VALID_RE = re.compile(r"^[A-Za-z0-9_\-]{1,32}$")


def gen_token() -> str:
    # 32 chars from a URL-safe alphabet - long enough to make guessing
    # impossible without the URL itself.
    return secrets.token_urlsafe(48)[:TOKEN_LEN]


def mint(names, base: str, out: Path, force: bool) -> int:
    existing: dict[str, dict[str, str]] = {}
    if out.exists():
        with open(out) as f:
            for row in csv.DictReader(f):
                existing[row["rater_id"]] = row

    written = 0
    new_rows: list[dict[str, str]] = []
    for name in names:
        if not VALID_RE.match(name):
            print(f"  SKIP {name!r}: invalid (alphanumeric / dash / underscore, ≤32 chars)",
                  file=sys.stderr)
            continue
        if name in existing and not force:
            print(f"  SKIP {name}: already in {out.name} (use --force to overwrite)",
                  file=sys.stderr)
            continue
        token = gen_token()
        url = f"{base}?rater={name}&token={token}"
        new_rows.append({"rater_id": name, "token": token, "url": url})
        print(url)
        written += 1

    if not new_rows:
        return written

    write_header = not out.exists() or force
    mode = "w" if force and out.exists() else "a"
    if force and out.exists():
        # --force rewrites the whole file: existing rows for raters
        # NOT in this batch are kept as-is (we merge). This is the only
        # sane semantics; otherwise --force would silently drop raters.
        kept = [r for name, r in existing.items() if name not in {n["rater_id"] for n in new_rows}]
        write_header = True
        mode = "w"
        with open(out, mode, newline="") as f:
            w = csv.DictWriter(f, fieldnames=["rater_id", "token", "url"])
            w.writeheader()
            for r in kept:
                w.writerow(r)
            for r in new_rows:
                w.writerow(r)
    else:
        with open(out, mode, newline="") as f:
            w = csv.DictWriter(f, fieldnames=["rater_id", "token", "url"])
            if write_header:
                w.writeheader()
            w.writerows(new_rows)

    print(f"\n--> {written} new URL(s) appended to {out}", file=sys.stderr)
    return written


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("names", nargs="*", help="rater_ids to mint (one URL each)")
    ap.add_argument("-f", "--file", help="read rater_ids from file, one per line")
    ap.add_argument("-o", "--out", default=str(DEFAULT_OUT))
    ap.add_argument("--base", default=DEFAULT_BASE,
                    help="base URL of the deployed rater UI")
    ap.add_argument("--force", action="store_true",
                    help="overwrite existing rater_id rows (re-rolls token)")
    args = ap.parse_args()

    names: list[str] = list(args.names)
    if args.file:
        with open(args.file) as f:
            names.extend(line.strip() for line in f if line.strip())

    if not names:
        ap.error("provide rater_ids as positional args or via -f")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    n = mint(names, args.base.rstrip("/"), out, args.force)
    return 0 if n > 0 or names else 1


if __name__ == "__main__":
    sys.exit(main())
