# Skill capture — Adding specimens to the Crystal Atelier / Amethyst showcase

Reusable, repo-specific procedure for adding one or more crystal specimens (with
photos) to this site. Written so it can be promoted into a formal Claude skill later.

## Repo shape (what to know before touching anything)
- `index.html` — the ENTIRE site (HTML + CSS + JS inline). No framework, no build step,
  no npm. Must open by double-click and deploy static.
- Inventory **source of truth = `inventory.csv`** (repo root). Columns:
  `id, name, category, height_in, weight_kg, price, status, photo, description, grade`
  - `price`: number → rendered `$N`; blank → no price shown.
  - `status`: `Available` (default) or `Sold` (`Sold` disables Inquire).
  - `height_in` (inches) / `weight_kg` (kilograms): numbers, either may be blank;
    formatted into the meta line as `~N" tall · ~N kg`.
  - `grade`: integer count of red-dot stickers on the specimen → renders a grade badge
    (N red dots) on the card. Blank → no badge.
- `tools/sync_inventory.py` — regenerates the `PRODUCTS = [...]` array in `index.html`
  from the CSV. **Never hand-edit the array; edit the CSV and run the script.**
- `images/` — specimen photos `amethyst-0N.jpg`, square ~1200 px, <300 KB, EXIF-oriented.
- Categories (filter chips) are derived automatically from each row's `category`.
- `.gitignore` ignores raw `IMG_*`, `*.zip`, `*.MOV`, and `images/_source/`.

## Procedure
1. **Confirm the repo.** Title/brand should read "Crystal Atelier"; `inventory.csv` +
   `tools/sync_inventory.py` present. If not, STOP.
2. **Inspect the photos** (Read each image). Note size overlays, price/weight tags,
   orientation, and any background/quality issues. Flag anything ambiguous to Jeff —
   especially numbers that might be weight vs. price (see note below).
3. **Process images** with the standard pipeline (Pillow):
   - `ImageOps.exif_transpose` (auto-orient — fixes phone-rotated shots),
   - convert RGB, top-biased square crop (`top = int((H-side)*0.08)`),
   - resize 1200×1200 LANCZOS,
   - save JPEG, step quality 90→… until file ≤ 300 KB (`optimize`, `progressive`).
   - Write to a temp dir first, eyeball, then copy into `images/` as `amethyst-0N.jpg`
     continuing the existing number sequence.
4. **Append rows to `inventory.csv`** (one per specimen) — match column order exactly,
   quote descriptions containing commas.
5. **Run** `python tools/sync_inventory.py` (regenerates `PRODUCTS`; header count auto-updates).
6. **Preview** (`python -m http.server 8000`): verify every card renders, no broken
   images, no console errors, filter chips correct.
7. **Write/append** a short PRD and a `DECISIONS.md` entry (what + why).
8. **Stage only** (`git add` the specific files). **Do NOT commit/push/deploy without
   Jeff's explicit "proceed"** (CLAUDE.md working agreement #4).
9. **Deploy = push to `main`.** Both Vercel (project `amethyst-showcase`, team
   SilverCrowz) and GitHub Pages auto-deploy from `main`. There's no local Vercel
   CLI/token and no `.vercel/` dir — that's expected; the GitHub→Vercel link lives in
   the Vercel dashboard, so a push to `main` is the deploy. Pages serves from `main`
   too, so if work is on a branch (e.g. `rename/crystal-atelier`), fast-forward `main`
   to it before pushing. Live URLs: https://amethyst-showcase.vercel.app and
   https://blakperlz.github.io/amethyst-showcase/.

## Gotchas learned (2026-06-19 batch)
- **The handwritten tag numbers on the rocks are weights in KG, not prices** — they
  track size and are far below the site's price range. They go in `weight_kg`. Set
  draft prices by size; Jeff sets real prices in the CSV later. Never publish a tag
  number as the price.
- **The red dots are the GRADE.** Count them precisely per photo (zoom in — don't
  assume a number; adjacent dots can touch). Put the count in `grade`. (In the
  2026-06-19 batch all five happened to be 3.)
- **"Landscape" phone photos** often just carry EXIF orientation 8 — `exif_transpose`
  stands them upright; no manual rotation.
- **Supplier-style photos** (red dots, handwritten tags, iPhone-Measure ruler overlays,
  cluttered backgrounds) can't be cleaned without real photo editing. They're drop-in
  replaceable later (keep the same filename). Flag the quality gap; don't pretend it's clean.
