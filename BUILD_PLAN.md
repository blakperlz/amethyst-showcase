# BUILD_PLAN.md — Amethyst Showcase

Prioritized, executable backlog for Claude Code. Work top-down. Each item has
acceptance criteria. Get sign-off before starting anything marked **[needs sign-off]**.

---

## P0 — Make it real (do these first)

### 1. Replace placeholder photos with real specimens
- **Source:** Jeff's "Amethyst Pics" Google Drive folder (not yet shared with the
  connected account — confirm access or have Jeff drop files into `images/`).
- **Do:** For each specimen, add an optimized square-ish JPG (~1000×1000, <300 KB)
  to `images/`. Either reuse the `amethyst-0N.jpg` names or update the `image:` field.
- **Done when:** Every product shows a real photo; no placeholder text visible;
  all `image:` paths resolve.

### 2. Replace sample inventory with real stock
- **Do:** Update the `PRODUCTS` array in `index.html` with Jeff's actual specimens —
  real names, dimensions, prices, descriptions, categories, and `sold` status.
- **Done when:** Counts/stats are accurate and categories make sense as filters.

---

## P1 — Ship quality

### 3. SEO, social, and favicon
- Add a favicon (amethyst icon).
- Add Open Graph + Twitter card meta tags with a share image so links preview well.
- Confirm `<title>` and meta description reflect real inventory/branding.
- **Done when:** Pasting the URL into a chat/social preview shows a proper card.

### 4. Custom domain **[needs sign-off]**
- Help Jeff buy/connect a domain (e.g. blakperlzcrystals.com) in Vercel settings.
- **Done when:** Site loads on the custom domain over HTTPS.

### 5. Lightweight inquiry upgrade (optional) **[needs sign-off]**
- `mailto:` works but loses buyers without a mail client. Consider a no-backend form
  (Formspree/Basin) that emails Jeff. Keeps the site static.
- **Done when:** Submitting the form emails Jeff; mailto remains as fallback.

---

## P2 — Toward selling **[needs sign-off — strategy decision]**

### 6. Decide monetization path
- Two realistic options, documented in `DECISIONS.md` before building:
  - **Shopify** (what reference sites use): fastest real store; monthly fee;
    migrate this inventory in. Recommended if Jeff wants to sell soon.
  - **Stripe Payment Links / Checkout** bolted onto this static site: cheaper,
    more custom, more work; cards handled by Stripe (no PCI burden).
- **Do not build either without an explicit decision.** Present trade-offs first.

---

## Guardrails
- Keep `index.html` self-contained and build-step-free unless an item above
  explicitly changes that (and it's signed off).
- Update `DECISIONS.md` whenever you make a notable choice.
- Commit after each completed item with a clear message.
