# CLAUDE.md — Blakperlz Crystals (Amethyst Showcase)

Instructions for Claude Code working in this repository. Read this first.

## What this project is
A static, single-page website showcasing an amethyst crystal collection. It is a
**proof-of-value showcase**, not a store. Buyers browse specimens and click
**Inquire**, which opens a pre-filled email. Real e-commerce (Shopify) comes later.

Owner: Jeff Watson · GitHub: `blakperlz` · Contact email: jeff.watson00@gmail.com

## Current state (as of 2026-06-17)
- Fully working static page in `index.html`.
- 8 sample specimens with **placeholder** images in `images/`.
- Not yet pushed to GitHub. Not yet deployed to Vercel.
- See `DECISIONS.md` for why things are the way they are, and `BUILD_PLAN.md`
  for what to do next.

## Architecture & conventions
- **One self-contained file.** `index.html` holds HTML, CSS, and JS inline. Keep it
  that way unless the build plan says otherwise — it must open by double-click and
  deploy to Vercel with **no build step**.
- **No frameworks, no bundler, no npm dependencies** for the site itself. Plain
  HTML/CSS/vanilla JS. Do not introduce React, Tailwind, etc. without explicit sign-off.
- **Inventory lives in one place:** the `PRODUCTS` array near the bottom of
  `index.html`, under the `EDIT YOUR INVENTORY HERE` comment. Category filter chips
  are derived automatically from each item's `category`.
- **Images** are local files in `images/`, referenced by filename. Keep them
  square-ish (~1000×1000) and optimized (<300 KB each ideally).
- **Buy flow** is `mailto:` only. No backend, no forms posting to a server, unless
  the build plan introduces one (e.g. Formspree) with sign-off.

## File map
- `index.html` — the entire site (layout + styles + inventory data).
- `images/` — specimen photos (currently placeholders `amethyst-01..08.jpg`).
- `vercel.json` — static deploy config (clean URLs, image caching).
- `DECISIONS.md` — decision log; **append to it** when you make a notable choice.
- `BUILD_PLAN.md` — prioritized backlog with acceptance criteria.
- `DEPLOY.md` — exact git + Vercel steps.
- `README.md` — end-user (Jeff) guide for editing and deploying.
- `images/gen.py` — script that generated the placeholders; safe to delete.

## How to preview locally
Just open `index.html` in a browser. Or, for correct relative paths:
`python3 -m http.server 8000` then visit `http://localhost:8000`.

## Deploy process (summary; full steps in DEPLOY.md)
1. Commit changes to git.
2. Push to `https://github.com/blakperlz/<repo>`.
3. Vercel is connected to that repo and auto-deploys `main` on every push.

## Working agreements (Jeff's standards — follow these)
1. **PRD / plan first for non-trivial work.** Before building anything beyond a
   small edit, write a short plan (problem, success criteria, scope, steps), surface
   open questions, and get explicit sign-off. Don't surprise Jeff with a big build.
2. **Document decisions** in `DECISIONS.md` — what, when, and why.
3. **Push back.** If a request seems off-strategy, technically wrong, or inconsistent
   with prior decisions, say so and flag trade-offs. No sycophancy. Check what already
   exists before proposing custom work.
4. **Reversibility.** Before anything destructive or hard to undo (deleting files,
   overwriting content, force-pushing, anything in Jeff's name), show the plan, flag
   what's irreversible, and wait for an explicit "proceed."
5. **Explain reasoning** for decisions in writing so they can be reviewed later.

## Definition of done for any change
- Page still opens with no build step and no console errors.
- All `image:` paths in `PRODUCTS` resolve to real files in `images/`.
- Inquire links generate correctly; SOLD items are disabled.
- `DECISIONS.md` updated if a notable choice was made.
- Changes committed with a clear message.
