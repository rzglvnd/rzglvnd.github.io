# rzglvnd.com

Official personal website and technical blog for Reza Ghalavand.

This project is a static Astro site designed to serve as a professional portfolio and long-term resume replacement.

## Highlights

- Multi-page portfolio: Home, Projects, Blog, About, Contact
- Resume-backed profile content
- Markdown-driven blog with dated posts from 2024 to present
- RSS feed and sitemap generation
- Responsive, production-ready frontend with no backend dependency

## Stack

- Astro
- TypeScript configuration via Astro strict preset
- Markdown content collections

## Run locally

```bash
npm install
npm run dev
```

Default local URL: `http://localhost:4321`

Build and preview:

```bash
npm run build
npm run preview
```

Preview URL is printed by the command (usually `http://localhost:4321` or `http://localhost:4173`).

## Dependencies and local requirements

- Node.js 20 LTS (recommended)
- npm 10+ (bundled with recent Node releases)

No backend services, database, or API keys are required for local development or preview.

## Deployment: GitHub Pages

This repository includes a GitHub Actions workflow at `.github/workflows/deploy-github-pages.yml`.

### One-time GitHub setup

1. Push this repository to GitHub.
2. In GitHub, open repository settings.
3. Navigate to **Pages**.
4. Under **Build and deployment**, set **Source** to **GitHub Actions**.
5. Ensure default branch is `main`.

### Deploy flow

- Every push to `main` triggers build and deploy.
- You can also trigger deployment manually from the **Actions** tab using `workflow_dispatch`.

## Project structure

- src/pages: route pages
- src/layouts: shared page layouts
- src/components: reusable UI blocks
- src/content/blog: blog posts and metadata
- src/data/profile.ts: profile, experience, competencies, and project data
- public/assets: images and resume PDF

## Writing a new blog post

1. Create a new markdown file in src/content/blog.
2. Add frontmatter fields:
   - title
   - description
   - publishedAt
   - tags
   - readingTime
   - featured
3. Write the article body in markdown.
4. Run npm run dev and verify listing order on /blog.
5. Run npm run build before opening a pull request.

## Content update workflow

- Resume information and profile facts should be updated in src/data/profile.ts.
- Blog content should remain implementation-focused and experience-backed.
- Keep project descriptions aligned with corresponding GitHub repositories.

## Domain and deployment

Site metadata is currently configured for https://rzglvnd.github.io in astro.config.mjs for pre-domain launch.

After custom domain setup, change this value to your final domain (for example `https://rzglvnd.com`) and redeploy.

The site is static and can be deployed on any static host such as GitHub Pages, Cloudflare Pages, Netlify, or Vercel static output.

## License

MIT License.
