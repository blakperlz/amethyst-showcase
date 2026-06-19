# PRD — Add 5 new amethyst cathedrals to the catalog (2026-06-19)

Status: **SHIPPED** — Jeff reviewed, answered the open questions, and authorized
commit + push + deploy. See "Resolution" at the bottom for what changed after review.

## Problem / goal
Jeff supplied 5 new specimen photos (amethyst cathedrals / cave geodes) and wants them
added to the Crystal Atelier showcase. Add them to the catalog using the existing
inventory workflow, matching the established pattern exactly. No new project, no new
schema, no build-step changes.

## What I found (existing structure — confirmed)
- **Single self-contained `index.html`** (HTML+CSS+JS inline). Inventory is the
  `PRODUCTS = [...]` array under the `EDIT YOUR INVENTORY HERE` comment.
- **Source of truth is `inventory.csv`** (repo root). Columns:
  `id, name, category, height_in, weight_lb, price, status, photo, description`.
- **`tools/sync_inventory.py`** regenerates the `PRODUCTS` array from the CSV. This is
  the only "build step" — run on demand. I used it; I did not hand-edit the array.
- **Images** live in `images/`, named `amethyst-0N.jpg`, square-ish, ~1200 px,
  optimized to <300 KB, EXIF auto-oriented. Existing pipeline documented in
  `DECISIONS.md` (2026-06-18 entry).
- **Categories** are derived automatically from each item's `category`
  (current set: Cathedrals, Geodes). Filter chips build from these.
- **No `grade` field exists** in the schema. (See "red dots" below.)

## What I changed (staged, not committed)
1. **5 new images** → `images/amethyst-07.jpg … amethyst-11.jpg`
   - Pipeline matches the existing one exactly: `ImageOps.exif_transpose` (auto-orient)
     → top-biased square crop → resize 1200×1200 → JPEG, quality stepped down until
     <300 KB. Final sizes 168–242 KB.
   - The two photos Jeff flagged as "landscape" (IMG_4367, IMG_4366) carry **EXIF
     orientation 8**; auto-orient stands them upright (base at bottom) automatically —
     no manual rotation needed.
2. **5 new rows** appended to `inventory.csv` (the source of truth).
3. **Regenerated `PRODUCTS`** in `index.html` via `tools/sync_inventory.py`
   (11 specimens total; header count auto-updates to 11).
4. **This PRD** + a **reusable skill capture** (`docs/SKILL-add-specimen.md`) +
   a new entry appended to `DECISIONS.md`.

## Photo → catalog mapping
| File | Source | Tag # | Size overlay | Name | Category | height_in | weight_kg | grade | price (DRAFT) |
|---|---|---|---|---|---|---|---|---|---|
| amethyst-07 | IMG_4368 | 6.50 | 10″ | Banded Agate Cathedral | Cathedrals | 10 | 6.5 | 3 | $240 |
| amethyst-08 | IMG_4370 | 8.10 | 11″ | Grape Cave Cathedral | Cathedrals | 11 | 8.1 | 3 | $265 |
| amethyst-09 | IMG_4369 | 11.40 | 16½″ | Slender Spire Cathedral | Cathedrals | 16.5 | 11.4 | 3 | $455 |
| amethyst-10 | IMG_4367 | 17.40 | none | Statement Lilac Cathedral | Cathedrals | _(unknown)_ | 17.4 | 3 | $450 |
| amethyst-11 | IMG_4366 | partial | none | Pale Lilac Cathedral | Cathedrals | _(unknown)_ | _(unknown)_ | 3 | $340 |

## Open questions / decisions for Jeff (the reason this is staged, not committed)

1. **The "price tag" numbers are weights, not prices — confirm.**
   6.50 / 8.10 / 11.40 / 17.40 track size monotonically (10″ < 11″ < 16½″ < biggest).
   $6.50 for a 10″ cathedral is implausible vs. the site's existing $285–$640 range.
   I recorded them as **`weight_lb`** and set **DRAFT prices** estimated by size
   (consistent with the existing pieces, which DECISIONS.md already notes are draft
   estimates for you to overwrite). **If these tags mean something else, tell me.**

2. **Real prices.** All 5 prices are my estimates so the page is reviewable. The two
   without a size overlay (10, 11) are the roughest. Set real numbers in `inventory.csv`
   and re-run the sync.

3. **Photo quality — same "supplier lot photo" gap as the existing 4.** Every new
   photo has burned-in **red price-dot stickers, a handwritten price tag, and (on 3 of
   them) an iPhone-Measure ruler overlay**, plus cluttered carpet/garage backgrounds.
   I can't remove burned-in overlays without real photo editing. These are **drop-in
   replaceable** later (same filenames), exactly like the existing dirty shots. Cleaner
   reshoots on a plain background would noticeably lift the storefront.

4. **Tall-piece cropping.** Top-biased square crop (the documented existing behavior)
   truncates the base of the two tallest pieces (09, 10). Matches the existing pattern,
   but if you'd rather show the whole specimen I can switch those to a letterboxed
   (padded) square on the dark card background.

5. **"Red-dot grade."** All 5 photos appear to carry ~3 red dots. The schema has **no
   grade field** and I did not add one (would need sign-off; and they look uniform). If
   the dots encode a grade you want shown, I can add a `grade` column + a small badge —
   say the word.

6. **Missing sizes (10, 11).** No size overlay was provided. Heights left blank (the
   CSV/formatter handle blanks). Add measured heights when you have them.

## Verification done
- Served locally (`python -m http.server`): 11 cards render, all 11 images load at
  1200×1200, **0 broken images, 0 console errors**, filter chips = All/Cathedrals/Geodes,
  header specimen count = 11.

## Resolution (after Jeff's review, 2026-06-19)
1. **Weights = kilograms.** Renamed CSV column `weight_lb` → `weight_kg`; sync formatter
   prints `~N kg`. The 5 tag numbers were already kg; the existing 6 had no weight data,
   so nothing to convert. amethyst-11 weight left blank (tag only partially legible).
2. **Prices:** left as DRAFT estimates; Jeff edits real prices in `inventory.csv` later.
3. **Grade:** added a `grade` column + a card badge (N red dots, bottom-left). Counted
   precisely from each photo — **all five = 3 dots** → grade 3. Existing 6 = no badge.
4. **Crop + photo quality:** kept as-is per Jeff (supplier photos fine for now,
   swappable later).
5. **Shipped:** committed, pushed, and deployed. Commit hash + live URL recorded in
   `DECISIONS.md` / reported to Jeff.
