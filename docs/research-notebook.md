# Maintaining the research notebook

Public section: `/research/`. Goldbach notebook: `/research/goldbach/`.

The content lives in `src/data/goldbach.ts`; the layout and interactive experiments are separate. To publish a meaningful research update:

1. Read the relevant new turns in **Explore the Goldbach conjecture**, local chat `01a143b3-9b6a-7392-b123-76cf52eb1355`. Summarize mathematical work; do not export the conversation, attachments, or private details. The public website cannot read a local Codex chat.
2. Add a milestone to the start of `milestones`, with a unique stable `id`, actual date, evidence label, title, summary, and mathematical detail. Include domains, assumptions, derivations, reproducible commands or public artifact links where relevant. Distinguish proposals, computations, exact identities, reviewed results, and rejected approaches. Never invent results, novelty, or a percentage toward proof.
3. Update `research.updated`, `research.through`, `research.phase`, and `research.next` to reflect the evidence. The public update date and the date of the latest research are distinct. Keep `directions` accurate. Both research pages derive their update labels from this data.
4. Run `npm run check`, `npm run build`, and `node --experimental-strip-types --test tests/primes.test.ts`. Preview the notebook at desktop and mobile sizes if UI changed.
5. Commit and push to `main` through the usual repository workflow. GitHub Actions builds and deploys Pages. Confirm deployment succeeded before reporting the update live.

Updates are curated and versioned through Git. No background synchronization or recurring automation is configured by this feature. The notebook links to its public content revision history; local `codex://` links are intentionally omitted from public UI.

## Experiments

`src/lib/primes.ts` supplies the exact sieve, unordered Goldbach pair enumeration (including equal-prime pairs), bounded coordinates, and Ulam spiral positions. `GoldbachLab.astro` uses them in the browser for N between 4 and 2,000. The 999 counts are a finite educational sample, not a research verification record. The hero Ulam spiral is computed at build time, with a prime at each correctly assigned spiral position.

The page retains static notes and initial pairs without JavaScript. The experiment tabs support arrow, Home, and End keys; input errors preserve the last valid plot. Native details elements expose the mathematical arguments.

## November 5, 2026 publication

The notebook now incorporates research saved through October 30. The latest chat turn contains commentary and working notes but no final completion report; the Fourier comparison and combined almost-all conclusion therefore retain a draft-under-review label. The earlier positive-average and positive-proportion arguments are labeled project derivations, without implying external peer review or novelty. Preserve that distinction unless a later mathematical audit supports a change.

`public/research/goldbach/2026-10-30/` contains the curated evidence snapshot, individual notes and small certificates, full source hashes, and a ZIP with the large finite populations. The public `summary.json` supplies the finite-result metrics and band totals in the page. Rebuild this dated snapshot from the original research directory with:

```text
python scripts/build-goldbach-snapshot.py <research-workspace>
```

The helper validates the full consecutive population, checks the finite-certificate fields, and copies only the explicit mathematical files in its allowlist. It excludes chat logs and checks selected files for private local paths. Use a new dated snapshot for later research; retain previous evidence URLs. The site does not execute the Python experiments for visitors. The archive README gives reproduction commands, scope, and dependencies.
