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

## Reversibility note
Nothing destructive was done. All work is new files in the project folder. The placeholder-generation script (`images/gen.py`) was left in place because a sandbox permission prevented deleting it — it is harmless and can be deleted manually.
