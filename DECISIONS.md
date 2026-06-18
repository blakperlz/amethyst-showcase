# Decisions Log — Blakperlz Crystals Showcase

_Last updated: 2026-06-17_

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

## Reversibility note
Nothing destructive was done locally. New this session: a public GitHub repo under
`blakperlz` and a GitHub Pages site — both reversible (delete repo / disable Pages).
Jeff authorized deployment explicitly ("just deploy already"). The site exposes only
intended content (showcase + the already-public inquiry email). The placeholder
generator (`images/gen.py`) remains, git-ignored.
