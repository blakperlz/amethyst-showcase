#!/usr/bin/env python3
"""
sync_inventory.py — regenerate the PRODUCTS array in index.html from inventory.csv.

inventory.csv is the human-editable source of truth (open it in Excel, or edit it
right on GitHub.com). After changing it, run:

    python tools/sync_inventory.py

…then preview index.html and commit. The website stays a single self-contained
file with no build step; this script is the only "sync" and you run it on demand.

CSV columns:
  id        - stable internal id (not shown on the site), e.g. piece-01.
  number    - the display number; renders as a "No. N" badge on the card.
  name      - the descriptive piece name.
  category  - must match a filter chip (chips are auto-built from these).
  height_in - inches; formatted into the dimension line. May be blank.
  weight_kg - kilograms; formatted into the dimension line. May be blank.
  price     - a number (e.g. 585) -> "$585". Leave blank -> no price shown.
  status    - "Available" (default) or "Sold". "Sold" disables Inquire.
  photos    - ONE OR MORE image paths separated by "|" (pipe). The first is the
              card/primary photo; the rest appear in the detail lightbox gallery.
              e.g. images/amethyst-01.jpg|images/amethyst-02.jpg
  grade     - integer count of red-dot stickers -> grade badge. Blank -> no badge.
  blurb     - short one-line teaser shown on the card.
  story     - longer evocative description shown in the detail lightbox.
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "inventory.csv"
HTML = ROOT / "index.html"


def fmt_height(row):
    h = (row.get("height_in") or "").strip()
    return f'~{h}" tall' if h else ""


def fmt_weight(row):
    w = (row.get("weight_kg") or "").strip()
    return f"~{w} kg" if w else ""


def fmt_price(row):
    p = (row.get("price") or "").strip()
    if not p:
        return ""
    return p if p.startswith("$") else f"${p}"


def fmt_grade(row):
    g = (row.get("grade") or "").strip()
    if not g:
        return "null"
    try:
        return str(int(float(g)))
    except ValueError:
        return "null"


def fmt_photos(row):
    raw = (row.get("photos") or row.get("photo") or "").strip()
    items = [p.strip() for p in raw.split("|") if p.strip()]
    return "[" + ", ".join(json.dumps(p) for p in items) + "]"


def main():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8-sig")))
    if not rows:
        sys.exit("inventory.csv has no rows")

    lines = ["const PRODUCTS = ["]
    for r in rows:
        sold = (r.get("status") or "").strip().lower() == "sold"
        num = (r.get("number") or "").strip()
        obj = (
            f"  {{ num:{json.dumps(num)}, "
            f"name:{json.dumps(r['name'].strip())}, "
            f"category:{json.dumps(r['category'].strip())}, "
            f"price:{json.dumps(fmt_price(r))}, "
            f"sold:{'true' if sold else 'false'}, "
            f"grade:{fmt_grade(r)},\n"
            f"    height:{json.dumps(fmt_height(r))}, "
            f"weight:{json.dumps(fmt_weight(r))},\n"
            f"    images:{fmt_photos(r)},\n"
            f"    blurb:{json.dumps((r.get('blurb') or '').strip())},\n"
            f"    story:{json.dumps((r.get('story') or '').strip())} }},"
        )
        lines.append(obj)
    lines.append("];")
    block = "\n".join(lines)

    html = HTML.read_text(encoding="utf-8")
    new_html, n = re.subn(
        r"const PRODUCTS = \[.*?\n\];",
        block.replace("\\", "\\\\"),
        html,
        count=1,
        flags=re.DOTALL,
    )
    if n != 1:
        sys.exit("Could not find the PRODUCTS array block in index.html")
    HTML.write_text(new_html, encoding="utf-8")
    print(f"Synced {len(rows)} pieces from inventory.csv into index.html")


if __name__ == "__main__":
    main()
