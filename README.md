# Blakperlz Crystals — Amethyst Showcase

A static, one-page showcase for your amethyst collection. No build tools, no server. Open `index.html` in any browser to view it.

---

## 1. See it right now
- **Live online:** https://blakperlz.github.io/amethyst-showcase/
- **Or locally:** double-click **`index.html`**. That's the whole site.

## 2. Edit your inventory (the easy way)
Your inventory lives in one spreadsheet: **`inventory.csv`**.

- **On your computer:** double-click it — it opens in Excel. Edit names, prices,
  sizes, status; save.
- **On any other device:** open `inventory.csv` on github.com and edit it right in
  the browser (it shows as a table).

Columns: `id, name, category, height_in, weight_lb, price, status, photo, description`.
- **Price** — a number like `585` (blank = "inquire for price").
- **Status** — `Available` or `Sold` (Sold shows a badge and disables Inquire).
- **Category** — the filter chips build themselves from these values.

After editing, the website catalog is regenerated from the CSV by running
`python tools/sync_inventory.py` (ask Claude to do this) — then push to GitHub.
The site itself stays one self-contained `index.html` with no build step.

> Heads-up: the prices currently in the CSV are **draft estimates** — replace them
> with your real numbers.

## 3. Swap in your real photos
Photos live in `images/`, named `amethyst-01.jpg` … `amethyst-06.jpg`. To replace
one, drop a new file with the **same name** into `images/` (square-ish, ~1000×1000,
under 300 KB). No code change needed. Or use a new filename and point the row's
`photo` column at it.

## 4. Online hosting
The site is **already live on GitHub Pages** (URL above) — it redeploys on every
push. If you later want Vercel (the original plan) or a custom domain, see
`DEPLOY.md`; you connect Vercel to the same `blakperlz/amethyst-showcase` repo.

Your contact email is set in `inventory.csv`-driven `index.html` (`CONTACT_EMAIL`).

---

## Files
- `index.html` — the entire site (layout, styling, generated catalog).
- `inventory.csv` — your editable inventory (source of truth).
- `tools/sync_inventory.py` — regenerates the catalog in `index.html` from the CSV.
- `images/` — specimen photos + `og-cover.jpg` (social share image).
- `DECISIONS.md` — what was decided and why.

## Next step when you're ready to actually sell
This page is intentionally a showcase. When you want a real cart + checkout, the lowest-friction path is **Shopify** (what your reference sites use). The inventory list here can be exported into Shopify, so nothing is wasted.
