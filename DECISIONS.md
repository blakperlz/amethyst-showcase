# Decisions Log — Crystal Atelier Showcase

_Last updated: 2026-06-18_

This file records what was decided, when, and why, per Jeff's working standards.

## Scope (decided 2026-06-17)

**Build:** A static, single-page showcase for an amethyst crystal collection — proof of value before investing in a real store.

**Explicitly NOT in this build:**
- No shopping cart, checkout, or payment processing
- No backend, database, or user accounts
- No real product photos yet (see "Open items")

Buyers browse specimens and click **Inquire**, which opens a pre-filled email. Monetization (Shopify or similar) comes later.

### Why this scope
Jeff's reference sites (Rock Paradise, Fossil Era) are full Shopify e-commerce stores. Standing up real card payments means PCI/security liability, a Stripe/Shopify account tied to a business + bank + tax setup, plus shipping and tax logic — none of which is code Claude can shortcut. A static showcase proves the concept and design in hours, at zero ongoing cost, and de-risks the bigger decision. Jeff agreed: "Let's just make the static proof of value page now. I can set up Shopify or something later."

## Tech choices

| Decision | Choice | Why |
|---|---|---|
| Architecture | Single self-contained `index.html` (HTML + CSS + JS inline) | Zero build step; opens by double-click; deploys to Vercel as-is. Easiest possible thing for a non-dev to own and edit. |
| Inventory data | Plain JS array at the top of `index.html`, clearly commented | Jeff can add/edit specimens without touching layout code. |
| Images | Local `/images/*.jpg`, referenced by filename | Real photos drop in by overwriting same-named files — no code change needed. |
| Buy flow | `mailto:` Inquire buttons | No backend required; works the day it deploys. |
| Design | Dark, image-forward, amethyst-purple + gold accents | Jeff said "you pick." Picked a clean-modern base with a premium/mystical tint that suits crystals — splits the difference between his two earlier design options. |

## Open items / known gaps

1. **Real photos missing.** The shared Google Drive folder (Amethyst Pics) is not shared with the Google account connected to this workspace — lookups returned "not found." The page currently uses clearly-labeled **placeholder images**. To fix: either re-share that folder with `jeff.watson00@gmail.com`'s connected Drive, or drop the photos into `/images` directly (see README).
2. **Inventory is sample data.** The 8 specimens are realistic placeholders, not Jeff's actual stock. Replace in the `PRODUCTS` array.
3. **Vercel not yet set up.** Deploy steps are in the README; account creation is Jeff's to do.

## Handoff to Claude Code (decided 2026-06-17)
Jeff is moving the ongoing build into Claude Code. Added the artifacts Claude Code
needs to execute against this repo:
- `CLAUDE.md` — project context, conventions, working agreements, definition of done.
- `BUILD_PLAN.md` — prioritized, executable backlog with acceptance criteria.
- `DEPLOY.md` — exact git + Vercel steps.
- `.gitignore` and `vercel.json` — clean static deploy config.
Deploy path chosen: **GitHub (`blakperlz`) → Vercel auto-deploy on push.** Static
site, no build step, free tier. Custom domain deferred.

## Real specimens, inventory system & first deploy (decided 2026-06-18)

**Photos.** Jeff supplied 7 real photos (a zip + one loose file) plus a video.
Processed 6 usable stills into `images/amethyst-01..06.jpg`: EXIF auto-orientation
(three were rotated), square crop (top-biased for the tall pieces), resized to
1200px, compressed <300 KB. The 7th file (`IMG_3444`) was an iPhone Measure
screenshot — not usable as a product photo, but it confirmed one cathedral is
~20.5″ tall. Raw originals / zip / `.MOV` are kept locally but git-ignored.
- **Known gap:** four of the six (the pallet/garage shots) have cluttered
  backgrounds and visible **red price-dot stickers + inventory labels**. They read
  as supplier lot photos, not storefront shots. Swapping in cleaner photos later is
  a drop-in replacement (same filenames). The two white-shelf shots are clean.

**Inventory system.** Chose a **spreadsheet-as-source-of-truth**, not an app/DB —
right scale for ~6–20 one-of-a-kind pieces, and keeps the site build-step-free.
- `inventory.csv` (repo root) is the human-editable record — open in Excel locally,
  or edit directly on GitHub.com from any device (CSV is editable in the GitHub web
  UI; an `.xlsx` would not be — that drove the format choice).
- `tools/sync_inventory.py` regenerates the `PRODUCTS` array in `index.html` from
  the CSV. The "build step" is this script, run on demand by Claude — the site stays
  one self-contained file. Fully automatic edit-→-site sync would need a GitHub
  Action (deferred; breaks the no-build rule and needs sign-off).

**Prices are DRAFT.** Jeff hasn't set prices; the displayed numbers are my
estimates so the page is reviewable. Footer already says prices are indicative.
Real prices go in `inventory.csv`.

**P1 polish done without sign-off** (BUILD_PLAN item 3, not gated): favicon (inline
SVG amethyst), Open Graph + Twitter share cards, and a generated `images/og-cover.jpg`.

**Deploy path — interim GitHub Pages, not Vercel (decided 2026-06-18).** Jeff asked
for a live product to review. Vercel deployment needs his interactive browser login
(the CLI wasn't installed and `vercel login` can't be automated). The connected
`gh` CLI (account `blakperlz`) let me push and enable **GitHub Pages** for an
immediate public URL with no build step — same self-contained `index.html`.
- Repo: `https://github.com/blakperlz/amethyst-showcase` (public).
- The original GitHub→Vercel plan in `DEPLOY.md` still stands; Jeff connects Vercel
  to this same repo when ready (it's a dashboard step). Pages can be turned off then.

## Brand rename: Blakperlz Crystals → Crystal Atelier (decided 2026-06-18)

Jeff renamed the brand from "Blakperlz Crystals" to **Crystal Atelier**. Updated all
visible brand text and docs.
- **Site (`index.html`):** title, `og:`/`twitter:` card titles, header logo, intro
  copy, Inquire/email button, footer brand + copyright — all now read "Crystal Atelier."
- **Docs:** `CLAUDE.md`, `README.md`, `DECISIONS.md` headings, and the example custom
  domain in `BUILD_PLAN.md` (`blakperlzcrystals.com` → `crystalatelier.com`).
- **Deliberately left as `blakperlz`:** the GitHub account name, the
  `blakperlz/amethyst-showcase` repo, and the `https://blakperlz.github.io/...` URLs in
  the social-share meta tags. Those are live hosting infrastructure tied to the GitHub
  account (which is not changing); rewriting them would break the deployed URL and the
  social-card preview image. If Jeff later wants a matching domain/handle, that's a
  separate task (buy `crystalatelier.com`, or rename the GitHub repo + re-point Pages).

## Reversibility note
Nothing destructive was done locally. New this session: a public GitHub repo under
`blakperlz` and a GitHub Pages site — both reversible (delete repo / disable Pages).
Jeff authorized deployment explicitly ("just deploy already"). The site exposes only
intended content (showcase + the already-public inquiry email). The placeholder
generator (`images/gen.py`) remains, git-ignored.

## Added 5 more cathedrals (decided 2026-06-19, shipped)
Jeff supplied 5 new specimen photos. Processed them through the existing pipeline
(`exif_transpose` → top-biased square crop → 1200 px → JPEG <300 KB) into
`images/amethyst-07..11.jpg`, appended 5 rows to `inventory.csv`, and regenerated
`PRODUCTS` via `tools/sync_inventory.py` (now 11 specimens). Full plan and per-photo
mapping in `PRD-2026-06-19-add-5-cathedrals.md`; reusable procedure in
`docs/SKILL-add-specimen.md`. Jeff reviewed and signed off ("proceed… commit, push, deploy").

**Weights are kilograms (schema change).** The on-rock tag numbers
(6.50/8.10/11.40/17.40) are kg, not prices — Jeff confirmed. Renamed the CSV column
`weight_lb` → `weight_kg` and the sync formatter now prints `~N kg`. No numeric
conversion was needed: the 5 new specimens' tag numbers were already kg, and the
existing 6 specimens had **no** weight data (the column was blank for all of them), so
there was nothing to convert. amethyst-11's tag was only partially legible, so its
weight is left blank.

**Prices remain DRAFT.** Jeff will set real prices directly in `inventory.csv` later
(then re-run the sync). Footer already states prices are indicative.

**Grade column + badge added (schema change).** The red-dot stickers are the grade.
Added a `grade` column to `inventory.csv` and a grade badge to the card (N red dots,
bottom-left, with a "Grade" label and a `title` tooltip). Counts were read precisely
from each photo (zoomed crops + verification) — **all five specimens have exactly 3
red dots**, so grade = 3 for 07–11. The existing 6 have no red-dot data and show no
badge (grade blank → `grade:null` → hidden).

**Photos kept as-is.** Same supplier-photo characteristics as the existing 4 (red dots,
handwritten tags, iPhone-Measure ruler overlays, cluttered backgrounds). Jeff chose to
keep them for now; they're drop-in replaceable later (same filenames). Crop unchanged
(top-biased square, matching the existing pieces).

**Reversibility.** All changes additive/forward (new images, new CSV rows, two additive
schema columns, a CSS/JS badge). The `weight_lb`→`weight_kg` rename is safe because no
prior weight values existed. Committed, pushed, and deployed per explicit go-ahead.

**Deploy correction — Vercel IS connected now.** The earlier (2026-06-18) note that
Vercel wasn't set up is outdated. The repo is linked to a Vercel project
**`amethyst-showcase`** (team **SilverCrowz**) that **auto-deploys on every push to
`main`** — no CLI/token needed locally (the absence of a `.vercel/` dir in the working
tree is not evidence it's unlinked; the link lives in the Vercel dashboard). Pushing
`main` (commit `952b24d`) triggered a production deploy automatically. Both deploy
paths are now live and current:
- **Vercel (production):** https://amethyst-showcase.vercel.app
- **GitHub Pages:** https://blakperlz.github.io/amethyst-showcase/

## De-duplicate, number, multi-photo + detail lightbox (decided 2026-06-19)

Jeff updated the contact email and flagged that the catalog had duplicates ("several
pics for one image"). Reviewed all 11 photos and confirmed with Jeff: they are really
**6 physical pieces**, several shot from multiple angles. Major restructure:

**Contact email** changed to **jeff@silverocean.net** across the site (`CONTACT_EMAIL`
const + the contact button; Inquire links are generated from the const) and the
`CLAUDE.md` owner line. Left `DECISIONS.md`'s 2026-06-17 reference to
`jeff.watson00@gmail.com` unchanged — that's a historical note about which *Google
Drive* account to share with, not contact info.

**One piece = one entry, with multiple photos (schema change).** `inventory.csv` now
has `id, number, name, category, height_in, weight_kg, price, status, photos, grade,
blurb, story`. `photos` holds pipe-separated paths (first = card photo, rest = gallery).
The 11 rows collapsed to **6** confirmed pieces:
1. Grand Calcite Cathedral — photos 01+02+03+04 (deep-purple, white calcite); grade **8**
   (counted from the dot stickers — these originals DO have red dots, ~8; earlier they
   were left ungraded). Height ~20.5"; weight unknown (originals never had a kg tag).
2. Slender Spire Cathedral — photo 09 (16.5"/11.4 kg, grade 3).
3. Sculptural Lilac Cathedral — photos 11+10 (17.4 kg, grade 3).
4. Lilac Mantel Cathedral — photos 05+06 (~13"; no red dots → no grade).
5. Grape Cave Cathedral — photo 08 (11"/8.1 kg, grade 3).
6. Banded Agate Cathedral — photo 07 (10"/6.5 kg, grade 3).

**Numbering + labeling.** Per Jeff: keep descriptive names **and** add a numbered badge.
Cards show a "No. N" badge (bottom-right) plus the existing category/grade badges.

**Clickable detail lightbox (new feature).** Each card opens an in-page modal (not a
separate page — keeps the single-file, no-build architecture). The lightbox shows a photo
gallery (all angles, thumbnail switching), a spec list (piece no., category, height,
weight, grade dots), the full evocative description, price, and an Inquire button.
Keyboard-accessible (Enter/Space to open, Esc/outside-click/× to close).

**Selling copy rewritten.** Every piece has a short `blurb` (card) and a longer `story`
(lightbox) that frames its *role* by actual size — desk/shelf companion (No. 6) →
mantel/bookshelf statement (No. 4, 5) → tall console statement (No. 2) → room-dominating
floor centerpiece (No. 1, 3) — written to make the viewer want it.

**Specimen count** is now an accurate **6** (hero stat is derived from the array).

**Sync script updated** to emit `num`, `images[]`, `height`, `weight`, `grade`, `blurb`,
`story`. Still CSV-driven, single self-contained `index.html`, no build step.
