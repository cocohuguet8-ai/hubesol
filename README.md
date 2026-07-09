# HubESOL — hubesol.com

Astro static site. Content lives in `src/content/lessons/` (Markdown) and quizzes in `src/data/quizzes/` (JSON).

## Local commands
- `npm install` — first time only
- `npm run dev` — local preview at localhost:4321
- `npm run build` — production build to `dist/`

## Deploy (one-time setup, ~15 min)
1. Create a GitHub repo `hubesol` and push this folder.
2. Cloudflare Dashboard → Workers & Pages → Create → Pages → Connect to Git → select the repo.
   - Framework preset: **Astro** · Build command: `npm run build` · Output: `dist`
3. In the Pages project → Custom domains → add `hubesol.com` (and `www.hubesol.com`).
   Cloudflare handles SSL automatically.
4. Every future `git push` deploys automatically.

## Adding a lesson (the agent workflow)
1. New `.md` file in `src/content/lessons/<hub-slug>/<lesson-slug>.md` (copy present-perfect.md as template).
2. New quiz JSON in `src/data/quizzes/` and reference its id in the lesson frontmatter (`quiz:`).
3. Commit + push. Schema (LearningResource, Quiz, FAQPage, Breadcrumbs) is generated automatically.

## Pending TODOs
- Replace newsletter form `action="#"` in `src/pages/index.astro` with your MailerLite/Brevo endpoint.
- Add analytics snippet (Cloudflare Web Analytics) in `src/layouts/Base.astro` when ready.
