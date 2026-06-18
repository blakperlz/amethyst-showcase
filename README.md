# Blakperlz Crystals — Amethyst Showcase

A static, one-page showcase for your amethyst collection. No build tools, no server. Open `index.html` in any browser to view it.

---

## 1. See it right now
Double-click **`index.html`**. That's the whole site.

## 2. Swap in your real photos
The page uses placeholder images in the `images/` folder, named `amethyst-01.jpg` through `amethyst-08.jpg`.

**Easiest way:** rename each of your photos to match (`amethyst-01.jpg`, etc.) and drop them into the `images/` folder, replacing the placeholders. No code changes needed.

**Or** keep your own filenames and update the `image:` line for each item (see next section). Use square-ish photos (~1000×1000) for the cleanest grid.

## 3. Edit your inventory
Open `index.html` in any text editor. Near the bottom, find the block that starts:

```js
/* EDIT YOUR INVENTORY HERE */
const PRODUCTS = [ ... ];
```

Each `{ ... }` is one specimen. To:
- **Change details** — edit `name`, `price`, `dims`, `desc`.
- **Mark as sold** — set `sold: true` (shows a SOLD badge, disables Inquire).
- **Hide a price** — set `price: ""`.
- **Add a specimen** — copy a whole `{ ... }` block, paste it, edit it. The category filter chips build themselves automatically from the `category` values.

Your contact email is set in `CONTACT_EMAIL` just below the list.

## 4. Put it online with Vercel (free)
1. Push this folder to your GitHub (`blakperlz`):
   - Create a new repo, e.g. `crystals-site`.
   - Upload these files (or `git push`).
2. Go to **vercel.com** → sign in **with GitHub** → **Add New Project** → import `crystals-site`.
3. Framework preset: **Other**. No build command needed. Click **Deploy**.
4. You'll get a live URL in ~30 seconds (e.g. `crystals-site.vercel.app`). You can add a custom domain later in Vercel's settings.

Every time you push changes to GitHub, Vercel redeploys automatically.

---

## Files
- `index.html` — the entire site (layout, styling, and your inventory list).
- `images/` — specimen photos (placeholders for now).
- `DECISIONS.md` — what was decided and why.
- `images/gen.py` — script that made the placeholders; safe to delete.

## Next step when you're ready to actually sell
This page is intentionally a showcase. When you want a real cart + checkout, the lowest-friction path is **Shopify** (what your reference sites use). The inventory list here can be exported into Shopify, so nothing is wasted.
