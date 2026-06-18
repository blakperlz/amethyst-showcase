# DEPLOY.md — Get the site live (GitHub → Vercel)

One-time setup, then every future change deploys automatically on `git push`.
Run the commands from inside this project folder.

---

## ✅ CURRENT STATUS (2026-06-18) — already live on GitHub Pages
The site is deployed now, for review, via **GitHub Pages** (no build step):
- **Repo:** https://github.com/blakperlz/amethyst-showcase
- **Live URL:** https://blakperlz.github.io/amethyst-showcase/
  (first publish can take 1–2 minutes after enabling Pages)

GitHub Pages was used because it needs no interactive Vercel login. The
GitHub → Vercel path below is still the intended long-term home — connect Vercel
to this same repo when ready (Step 2), then you can disable Pages if you like.

### Updating inventory later
1. Edit `inventory.csv` — in Excel locally, or directly on github.com (it's a
   table you can edit in the browser). Add/replace photos in `images/`.
2. Have Claude run `python tools/sync_inventory.py` (rewrites the catalog in
   `index.html` from the CSV), then `git push`. Pages redeploys automatically.

---

## Prerequisites (one time)
- **Git** installed — check with `git --version`. If missing: https://git-scm.com/downloads
- **GitHub account** — you have one: `blakperlz`.
- **Vercel account** — sign up at https://vercel.com using **"Continue with GitHub"**
  (this links the two so deploys are automatic). No credit card needed for the free tier.

Optional but handy:
- **GitHub CLI** (`gh`) to create the repo from the terminal: https://cli.github.com
- **Vercel CLI** (`npm i -g vercel`) to deploy from the terminal.

---

## Step 1 — Put the code on GitHub

### Option A — GitHub CLI (fastest)
```bash
git init
git add .
git commit -m "Initial commit: amethyst showcase"
git branch -M main
gh repo create blakperlz/amethyst-showcase --public --source=. --remote=origin --push
```

### Option B — Web UI + git
1. Go to https://github.com/new → name it `amethyst-showcase` → **Create repository**
   (leave it empty — no README/license, since this folder already has them).
2. Back in the terminal:
```bash
git init
git add .
git commit -m "Initial commit: amethyst showcase"
git branch -M main
git remote add origin https://github.com/blakperlz/amethyst-showcase.git
git push -u origin main
```
If prompted to authenticate, use a GitHub Personal Access Token as the password
(GitHub no longer accepts your account password for git over HTTPS), or run
`gh auth login` first.

---

## Step 2 — Deploy on Vercel

### Option A — Dashboard (recommended, no terminal)
1. https://vercel.com → **Add New… → Project**.
2. **Import** the `amethyst-showcase` repo.
3. Framework Preset: **Other**. Build Command: leave **empty**. Output Directory:
   leave **empty** (root is served). Root Directory: `./`.
4. Click **Deploy**. In ~30s you get a live URL like
   `https://amethyst-showcase.vercel.app`.

### Option B — Vercel CLI
```bash
npm i -g vercel
vercel            # follow prompts; link to your account
vercel --prod     # publish to the production URL
```

---

## Step 3 — From now on, updates are automatic
Make edits (photos, inventory, etc.), then:
```bash
git add .
git commit -m "Update inventory and photos"
git push
```
Vercel detects the push and redeploys in seconds. Pull requests get their own
preview URLs automatically.

---

## Custom domain (optional, later)
Vercel project → **Settings → Domains → Add**. Buy through Vercel or point an
existing domain's DNS as instructed. HTTPS is automatic.

## Troubleshooting
- **404 on deploy:** make sure `index.html` is at the repo root (it is).
- **Images missing online:** confirm the `images/` folder was committed
  (`git status` should show no untracked images) and filenames match exactly —
  Vercel/Linux is **case-sensitive** (`Amethyst-01.JPG` ≠ `amethyst-01.jpg`).
- **Auth fails on push:** run `gh auth login`, or create a token at
  GitHub → Settings → Developer settings → Personal access tokens.
