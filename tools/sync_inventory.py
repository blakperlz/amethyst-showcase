#!/usr/bin/env python3
"""
sync_inventory.py — regenerate the PRODUCTS array in index.html from inventory.csv.

inventory.csv is the human-editable source of truth (open it in Excel, or edit it
right on GitHub.com). After changing it, run:

    python tools/sync_inventory.py

…then preview index.html and commit. The website stays a single self-contained
file with no build step; this script is the only "sync" and you run it on demand.

CSV columns: id, name, category, height_in, weight_lb, price, status, photo, description
  - price:  a number (e.g. 585) -> shown as "$585".  Leave blank -> no price shown.
  - status: "Available" (default) or "Sold".  "Sold" disables the Inquire button.
  - height_in / weight_lb: numbers; formatted into the dimension line. Either may be blank.
"""
import csv, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "inventory.csv"
HTML = ROOT / "index.html"


def fmt_dims(row):
    parts = []
    h = (row.get("height_in") or "").strip()
    w = (row.get("weight_lb") or "").strip()
    if h:
        parts.append(f'~{h}" tall')
    if w:
        parts.append(f"~{w} lb")
    return " · ".join(parts)


def fmt_price(row):
    p = (row.get("price") or "").strip()
    if not p:
        return ""
    return p if p.startswith("$") else f"${p}"


def main():
    rows = list(csv.DictReader(CSV.open(encoding="utf-8-sig")))
    if not rows:
        sys.exit("inventory.csv has no rows")

    lines = ["const PRODUCTS = ["]
    for r in rows:
        sold = (r.get("status") or "").strip().lower() == "sold"
        obj = (
            f"  {{ name:{json.dumps(r['name'].strip())}, "
            f"category:{json.dumps(r['category'].strip())}, "
            f"image:{json.dumps(r['photo'].strip())}, "
            f"dims:{json.dumps(fmt_dims(r))}, "
            f"price:{json.dumps(fmt_price(r))}, "
            f"sold:{'true' if sold else 'false'},\n"
            f"    desc:{json.dumps(r['description'].strip())} }},"
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
    print(f"Synced {len(rows)} specimens from inventory.csv into index.html")


if __name__ == "__main__":
    main()
