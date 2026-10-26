---
type: "corpus"
item_id: "24bc98a339adcf89"
title: "Show HN: Farol – A risk map of a pull request for the person who approves it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50231349"
project_url: "https://github.com/winnin/farol"
author: "ericholiveira"
published_at: "2026-10-25T13:28:06Z"
captured_at: "2026-10-26T09:42:36+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-25"
tags:
  - 语料
  - hn_show
  - author_ericholiveira
  - story_50231349
  - show_hn
metrics: {"points": 59, "comments": 37, "engagement_velocity": 59}
comments_count: 37
comments_total: 37
discovered_via: "hn:show_hn:3d"
---

# Show HN: Farol – A risk map of a pull request for the person who approves it

> [!info] 一句话导读
> Know the risk of merging a pull request, and where it lives. Free, open-source CLI and GitHub Action: after your AI review, farol shows the riskiest files, what…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50231349>
> 指标：点赞=59 · 评论=37 · engagement_velocity=59
> 作者：ericholiveira　|　发布：2026-10-25T13:28:06Z
> 项目链接：<https://github.com/winnin/farol>
> 采集：2026-10-26T09:42:36+08:00　|　id：`24bc98a339adcf89`

## 正文

# winnin/farol

Know the risk of merging a pull request, and where it lives. Free, open-source CLI and GitHub Action: after your AI review, farol shows the riskiest files, what they reach, diff coverage and contract breaks. TypeScript/React, Go, Python.

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 5
- License: MIT License
- Homepage: https://winnin.github.io/farol/
- Default branch: main
- Created: 2026-10-21T21:52:58Z

## Languages

- Go
- HTML
- JavaScript
- Python
- TypeScript

## Topics

- ai-code-review
- cli
- code-review
- developer-tools
- diff-coverage
- fastapi
- github-actions
- golang
- nextjs
- pull-requests
- python
- react
- risk-analysis
- static-analysis
- typescript

## Top Contributors

- erich-oliveira-winnin (9 contributions)

---

## README

 Know the risk of merging a pull request, and where it lives.

 A free, open-source CLI and GitHub Action. After your AI review, farol tells the person who approves how risky the
 merge is and which files carry the risk, so the riskiest changes get the most attention.

 Website ·
 Live demo ·
 Get started ·
 Reference

---

Agents write the code and agents review it. The last call is still a person's: approve the merge or not. That
approval is the scarce part, and spread evenly over every pull request it turns into a skim, which is how a one-line
change to a shared hook takes down forty pages.

**farol comes after the AI review, not instead of it.** Your review agent comments on the lines in the diff. farol
gives the person who approves what the agent cannot reliably give: **the risk of accepting the change, and where it
lives**. The goal is not only a faster review: low-risk pull requests can go fast, and the risky ones get read line by
line, starting with the files that carry the risk. It works from static analysis (the compilers' own view of your
code, not a model's guess), so the same pull request always gets the same answer.

The Claude Code team describes the same principle in
How the Claude Code team does code review: review effort
follows the risk of the change. As they put it, "The change sets the tier, not the author."

**farol** (Portuguese for *lighthouse*) does the triage before the reviewer opens the diff:

- **What does this change reach?** Every existing page, API operation, RPC method, job and script that runs the changed code, with the call chain to each.
- **How risky is the merge?** A verdict (*fast track*, *quick review*, *careful review*) and a 0–100 risk score from reach, diff coverage, security findings, contract breaks and dependency changes.
- **Where do I start?** The riskiest files first, with inline diffs, untested lines marked, and a checklist of what to try by hand.

**Free and open source (MIT).** Run it as a CLI with `npx @winninjs/farol`, or on every pull request with the GitHub
Action `winnin/farol/action`. No account, no hosted service: it runs on your machine or in your CI runner, comments on
every PR and never blocks a merge. It **never executes your code** and never sends it anywhere.

## Live demo

**See farol on a real pull request →**

The demo holds the reports farol produced in CI for a pull request on the
FastAPI full-stack template: a FastAPI backend and a React
frontend with TanStack Router. The pull request adds a status to items and an Insights page, with the kind of problems
a reviewer should catch: a breaking API change, SQL built with an f-string, a shared component without tests.

- Backend report: ⚠ careful review, a breaking contract change and a high-severity security finding.
- Frontend report: ⚠ careful review, a new page and the existing pages a shared component reaches.

The reports are interactive: mark files as reviewed, mark a page as behind a feature flag, open the inline diffs,
follow the test plan and copy the review record from the Result tab. They are the same files the pull request's
comments link to (the pull request); the
copies live in `docs/demo/`.

## farol after your AI review

| | AI review agents | farol |
|---|---|---|
| **Reads** | the diff, and whatever context fits in the prompt | the whole program at the base and the head, with the compilers (TypeScript type checker, `go/types`, Python `ast`) |
| **Tells you** | what may be wrong in these lines | what these lines reach, how risky the merge is, and where to look first |
| **Answers are** | probabilistic: worded differently on every run | deterministic: the same PR gives the same report, and every claim comes with its call chain |
| **When unsure** | may sound confident anyway | says `unknown` and asks for a careful review |
| **Runs** | a model, usually a hosted service | locally or in your CI: it never executes your code and never sends it anywhere |

Use both, in that order. The agent reviews the lines first; then farol tells the person who approves how much attention
the merge needs, which files deserve it, which pages and endpoints to test by hand and which contract changes need
their clients checked. The agent's review is not enough exactly when a small change has a large reach, and that is
what farol shows.

## Why farol

- **Review attention goes where the risk is.** A 40-file PR usually has two or three files that can actually hurt. farol ranks them, so the reviewer reads those closely and skims the rest with a clear conscience.
- **It follows the code, not the file names.** farol builds a declaration graph with the real compilers (the TypeScript type checker, `go/types`, Python's `ast`). A change to `formatPrice` lists the twelve pages that render it, not "1 file changed".
- **Contract breaks are caught before clients are.** Removed response fields, new required parameters, changed types in GraphQL, FastAPI, Go handlers and gRPC, with the services that call each endpoint.
- **Review the whole PR, or just what changed since your last look.** Every push gets two reports: the full pull request, and only the commits since the previous push. After a round of fixes, the reviewer checks the new commits instead of starting over.
- **It uses what your CI already has.** Coverage, lint, security and audit reports become diff coverage and findings on the changed lines. Nothing runs twice.
- **Fail closed.** When farol cannot read part of a change, it says so (`unknown`) and asks for a careful review. It never calls something safe because it did not understand it.
- **Built for the human in the loop.** Mark files as reviewed, mark pages as behind a feature flag, check off findings, and paste the result back in the PR as a record of what was reviewed.

## Contents

- Live demo
- farol after your AI review
- Get started
- Recipes: React Router · Next.js · TanStack Router · TypeScript API · Go · Python · Datadog
- What is supported
- Reading the review
- How it works · Security · Limitations · FAQ
- Reference (every command, option and configuration key)

## Get started

You need **Node.js 22+** and **git** (plus `go` for Go projects, `python3` 3.11+ for Python ones). Nothing to
install: run farol with `npx @winninjs/farol`.

**1. Describe your project** in a `farol.config.json` at its root. One line is enough to start; pick your stack:

| Your project | `farol.config.json` | Full recipe |
|---|---|---|
| React app with React Router | `{ "routes": { "file": "src/routes.tsx" } }` (the file that builds the route table) | React Router |
| Next.js app (Pages or App Router) | `{ "routes": { "adapter": "next" } }` | Next.js |
| React app with TanStack Router | `{ "routes": { "adapter": "tanstack-router", "dir": "src/routes" } }` | TanStack Router |
| TypeScript API (GraphQL, REST) | `{ "surface": "backend" }` | TypeScript API |
| Go service | `{ "language": "go", "surface": "backend" }` | Go |
| Python service (FastAPI, Flask, Django, Celery…) | `{ "language": "python", "surface": "backend" }` | Python |

**2. Check what farol sees:** the pages, endpoints, jobs and scripts it found.

```sh
npx @winninjs/farol routes
```

**3. Analyze a branch** against its target and open the report.

```sh
npx @winninjs/farol analyze --base origin/main --head HEAD --out farol.json
npx @winninjs/farol html --in farol.json --out farol.html && open farol.html     # xdg-open on Linux
```

### Example: a React app with React Router

```sh
cd path/to/your/react-app
echo '{ "routes": { "file": "src/routes.tsx" } }' > farol.config.json

npx @winninjs/farol routes                                        # lists your pages: "/", "/products", "/settings"…
git checkout my-feature-branch
npx @winninjs/farol analyze --base origin/main --head HEAD --out farol.json
npx @winninjs/farol html --in farol.json --out farol.html && open farol.html
```

The report already shows the verdict, the score, the files to start with, the pages the change reaches and what to
test by hand. **Next steps:** add your coverage, lint and audit reports and run farol on every PR with the
recipe for your stack. Every option is in the reference and, per stack, in
examples/README.md.

> Running it often? `npm install --global @winninjs/farol` gives you a plain `farol` command.

## Recipes

Each recipe has three parts: the `farol.config.json` to commit, the reports to produce, and the GitHub Actions
workflow. The workflows in `examples/` are complete and share one shape:

1. **`tests`** runs your tests, linter and audit and keeps the reports. It runs the PR's code, so it has no secrets and a read-only token. If you already have a test job, keep it and add its upload step.
2. **`farol`** runs after it (pass or fail), reads git and the reports, and posts a **new comment on every push** with a link that opens the HTML report in the browser, plus a second report with only the commits since the previous push. It never runs the PR's code.
3. Drafts are skipped, fork PRs get no comment (their token is read-only), and every farol step is `continue-on-error`.

Pin the action to a commit once it works for you: `winnin/farol/action@ # main as of `.

`examples/README.md` goes deeper for each stack: every configuration key, CLI parameter and
action input, and how to check a setup.

### React frontend (React Router)

React Router route tables (object and JSX forms, lazy routes, split route modules), reach per declaration.

```json
{
  "routes": { "file": "src/routes.tsx" },
  "roles": { "global": ["src/main.tsx", "src/App.tsx", "src/styles/global.css", "package.json", "vite.config.ts"] }
}
```

```sh
npx vitest run --coverage.enabled --coverage.reporter=json --coverage.reportsDirectory=reports/coverage
npx eslint -f json -o reports/eslint.json <changed files>
npm audit --json > reports/audit.json                     # or pnpm audit --json

npx @winninjs/farol analyze --base origin/main --head HEAD \
  --coverage reports/coverage/coverage-final.json --eslint reports/eslint.json --audit reports/audit.json --out farol.json
```

**CI:** copy `examples/workflow.yml` to `.github/workflows/farol.yml`.

Set `coverage.include: ['src/**/*.{ts,tsx}']` in the Vitest config so files no test loads are reported as untested.
Split route trees go in `routes.extraFiles`; a fuller config is in examples/farol.config.json.

### Next.js

Pages Router and App Router: every page, API route, layout, `_app`/`_document` and middleware, read from the file
names. Dynamic segments (`[id]`), catch-alls, route groups and parallel slots are understood.

```json
{
  "routes": { "adapter": "next" },
  "roles": { "global": ["next.config.*", "package.json"] }
}
```

`pages/` and `app/` are found in the project or in its `src/`; set `"dir"` when they live elsewhere. Reports and CI
are the same as for React Router (Jest or Vitest coverage, ESLint, audit). In a
monorepo whose tsconfig extends a workspace package (`"extends": "tsconfig/nextjs.json"`), install dependencies
before analyzing, so the package is in `node_modules`.

### TanStack Router

File-based routing: every module calling `createFileRoute(' ')` under the routes directory, with the root route,
pathless layouts (`_app`) and parent routes as layouts of their children.

```json
{ "routes": { "adapter": "tanstack-router", "dir": "src/routes" } }
```

Reports and CI are the same as for React Router.

### TypeScript API (GraphQL or REST)

GraphQL root operations (schema files and `gql` templates, per resolver) and Fastify/Express-style REST endpoints.

```json
{
  "surface": "backend",
  "backend": { "graphql": true, "rest": true },
  "roles": { "global": ["package.json", "src/app.ts"] }
}
```

Reports and CI are the same as for React Router: `examples/workflow.yml`. If
resolvers reach data through an injected context (`ctx.loaders.Brand.byId()`), tell farol where the providers live:
`"backend": { "context": { "loaders": ["src/modules/*/loaders/index.ts"] } }`.

### Go service

chi, gin, echo and net/http routes, gRPC service methods and `main` binaries, reach per declaration with interface
calls resolved to their implementations.

```json
{ "language": "go", "surface": "backend" }
```

```sh
go test -coverpkg=./... -coverprofile=reports/cover.out ./...
golangci-lint run --output.json.path=reports/golangci.json --issues-exit-code=0 ./...   # enable gosec
govulncheck -json ./... > reports/govulncheck.json

npx @winninjs/farol analyze --base origin/main --head HEAD \
  --coverage reports/cover.out --eslint reports/golangci.json --audit reports/govulncheck.json --out farol.json
```

**CI:** copy `examples/workflow-go.yml`. farol reads modules offline, so the workflow runs
`go mod download` for the base and the head first.

### Python service

FastAPI and Flask routes (routers, blueprints, prefixes), Django URLs, MCP tools/resources/prompts, Celery tasks,
Temporal workflows and activities, Prefect flows and `__main__` scripts. farol parses your code; it never imports it.

```json
{ "language": "python", "surface": "backend", "python": { "roots": ["src", "."] } }
```

```sh
pytest --cov=src --cov-report=json:reports/coverage.json
ruff check --output-format json --extend-select S --exit-zero . > reports/ruff.json    # S = flake8-bandit
pip-audit --format json -o reports/pip-audit.json

npx @winninjs/farol analyze --base origin/main --head HEAD \
  --coverage reports/coverage.json --eslint reports/ruff.json --audit reports/pip-audit.json --out farol.json
```

**CI:** copy `examples/workflow-python.yml` (uses `uv`; swap in your installer).

### Add Datadog traffic and errors

Optional, and information only: it never changes the score. With it the report shows how much traffic each affected
page or operation gets, its **distinct production errors** (linked to Datadog), the changed files that already throw
errors, and the services that call each changed endpoint.

```json
{
  "datadog": {
    "env": "prod",
    "rum": { "applicationId": "<RUM application id>" },
    "apm": { "service": "orders-api", "operations": ["fastapi.request"] }
  }
}
```

```sh
DD_API_KEY=… DD_APP_KEY=… npx @winninjs/farol usage --out usage.json      # last 14 days
npx @winninjs/farol analyze … --usage usage.json
```

**CI:** the example workflows have a `farol-usage` job: set the `DD_API_KEY` and `DD_APP_KEY` secrets and the
repository variable `FAROL_DATADOG=true`. It reads Datadog once a day and never sees the PR's code. Keys, scopes and
matching rules are in the reference.

## What is supported

| | TypeScript / React frontends | TypeScript / JavaScript backends | Go | Python |
|---|---|---|---|---|
| **Entry points** | React Router route tables (object and JSX forms, lazy routes, split route modules); Next.js Pages and App Router (pages, API routes, layouts, middleware); TanStack Router file-based routes | GraphQL root operations (schema files and `gql` templates) and REST endpoints (Fastify/Express style) | chi, gin, echo and net/http routes; gRPC service methods; `main` binaries | FastAPI and Flask routes (routers, blueprints, prefixes); Django URLs; MCP tools, resources and prompts; Celery tasks; Temporal workflows and activities; Prefect flows; `__main__` scripts |
| **Reach precision** | per declaration (TypeScript type checker) | per module, per resolver for GraphQL | per declaration (`go/types`, interface calls resolved to implementations) | per declaration (Python `ast` with local type inference) |
| **Contract changes** | — | GraphQL schema (breaking / dangerous / safe) | Handler request and response types (net/http, chi, gin, echo); gRPC messages | FastAPI parameters, body, response and Pydantic models |
| **Dependencies** | `package.json` + npm/pnpm/yarn/bun lockfiles | same | `go.mod` + `go.sum` | `pyproject.toml` (PEP 621, extras, groups, uv, Poetry), `requirements.txt` + `uv.lock`/`poetry.lock`/`Pipfile.lock` |
| **Diff coverage** | Istanbul `coverage-final.json` (Vitest, Jest) | same | `go test -coverprofile` | coverage.py JSON (`pytest --cov`) |
| **Lint** | `eslint -f json` | same | golangci-lint JSON | ruff JSON |
| **Security** | built-in rules (XSS sinks, `eval`, hard-coded secrets, `javascript:` URLs…) | same | gosec (through golangci-lint) | flake8-bandit (ruff `S` rules) |
| **Vulnerabilities** | `npm audit --json`, `pnpm audit --json` | same | `govulncheck -json` | `pip-audit --format json` |
| **Suppressions** | `eslint-disable`, `@ts-ignore`, `@ts-expect-error`, `as any`… | same | `//nolint`, `//lint:ignore`, `#nosec` | `# noqa`, `# type: ignore`, `# nosec`, `# pragma: no cover`… |
| **Traffic and errors** (optional) | Datadog RUM page views and errors | Datadog APM requests, error spans and callers | same | same |

In every language: environment, infrastructure and CI files (`.env*`, Dockerfiles, compose, CI pipelines, helm, k8s,
terraform…) in a section of their own; incremental analysis since any commit (`--since`); suggested reviewers from
git blame and CODEOWNERS; reports as a GitHub comment, Markdown or a single-file HTML page.

## Reading the review

farol produces two things: a **PR comment** with the verdict, the top files and a test checklist, and a
**single-file HTML report** (linked from the comment) where the review happens. Here is what each part is for and how
to use it.

### Verdict and merge risk score

What it tells you is how much of your time the PR deserves.

| Verdict | Means | What to do |
|---|---|---|
| ✓ **Fast track** | Only new code, tests or low-risk changes. | Skim the diff and approve. |
| ◐ **Quick review** | Existing code changed in a contained way, or a weaker signal (low coverage, lint errors, a config file). | Check the *Start here* files, then approve. |
| ⚠ **Careful review** | Wide or silent breakage is possible: a score of 60+, a breaking contract change, a high-severity finding, an untested central file, or code farol could not read. | Read the *Start here* files line by line and test what they reach. |

The **score** (0–100) is the chance that at least one risky item breaks something. Expand *What adds to it* to see
each item and its points: the files by reach × untested share, findings, contract changes, dependencies. The verdict
always comes with its reasons; read them before the diff.

### Start here

The changed code files, riskiest first. Each row shows how many existing pages or operations run the file, its diff
coverage, its findings and its own risk points; with Datadog, also its traffic and production errors. Open the inline
diff: added lines no test runs are marked **○**, lines with findings **⚠**.

**How to use it:** review top-down and tick **Mark as reviewed** on each file. The score drops as you go, so you
always know how much risk is left. Below it come the low-risk files to skim, environment/infrastructure/CI files
(check their values per environment), and files that need no review (docs, lockfiles, tests).

### Behind a feature flag

On every page or operation row, and in a panel at the top: mark an entry point that is entirely behind a flag. Files
that **only** flagged entry points use leave the review, labeled *behind a flag* rather than reviewed. Use it for
work-in-progress features shipped dark, so the remaining score reflects what users will actually hit.

### Pages / Operations

Every new and affected entry point, as a list or a tree by module. Opening one draws **how** the change reaches it,
file by file. With Datadog each one shows its traffic share and its distinct errors, busiest first. **Use it** to
judge blast radius: a change reaching 3 rarely used admin pages is not the same as one reaching the checkout.

### Contracts (backends)

Each endpoint whose request or response shape changed, as **breaking** (clients built for the base can fail),
**dangerous** (they may misbehave) or **safe** (compatible additions), with the exact field and the calling services
from Datadog. **Use it** to confirm every breaking change is intended and its clients are updated, then tick
*checked with clients*.

### Security, Dependencies, Coverage

The evidence behind the score: security findings on the changed lines (with a *checked* box each), added or bumped
dependencies with known vulnerabilities, and diff coverage per file. A report that was not given shows as
**not verified**, never as passing.

### Test plan

The new and affected pages or operations to try by hand, new ones first, then by the risk of the file that reaches
them. The PR comment has it as a task list. **Use it** when you run the branch locally or on a preview environment.
It follows your review: once every changed file behind an item is marked as reviewed, the item is marked too
(✓ files reviewed), or 🚩 behind a flag. Its own checkbox, for the manual test, stays yours to tick.

### Reviewers

Who should review: the people who wrote the code this PR changes (git blame, weighted by each file's risk), plus
CODEOWNERS. The PR's own authors and bots are left out, and inactive people are labeled. **Use it** to request the
person who knows the riskiest file, not just whoever is free.

### Result

A Markdown record of the review: the initial verdict and score, the score left now, the flagged entry points, the
reviewed files, and the checked findings and contract changes. **Copy as Markdown** and paste it in the PR as your
review comment, so the next person knows what was looked at.

### Since the last push

After a push to an open PR, the comment carries a second report with only the commits since the previous push
(`analyze --since `; after a force-push, from its merge-base). Its verdict, score and *Start here* cover just
those changes. **Use it** for the second round of a review: check that the fixes do what was asked and nothing
else, then go back to the full report only if the new commits reach somewhere new.

### Class and reasons

Kept in *Details* and a collapsed block of the comment, so reviewers form their own opinion first:
`isolated` (only adds), `touches-existing` (existing code changed), `global` (a global file, manifest or critical
dependency) and `unknown` (part of the change could not be read: never safe). Every reason code is in
docs/reasons.md.

## How it works

1. **Diff** the merge-base and the head, detecting renames and ignoring whitespace-only and trailing-comma lines.
2. **Read both trees without running anything**: the TypeScript compiler API, `go list` + `go/types` (offline), Python `ast`. From them, the entry points and a graph of which declaration uses which.
3. **Compare declarations** by a hash of their code, so comments and formatting never count. New declarations and entry points are additive.
4. **Reach**: from each changed declaration to every entry point that runs it, keeping the shortest chain.
5. **Classify, weigh and plan**: class, score, verdict, files to start with, test checklist.

On 662 past commits of four repositories, *fast track* had **0 problems in 56 commits** and the score's AUC was
**0.72–0.83**; run `farol calibrate` on your own history.
The details per language are in docs/how-it-works.md, and the reasons behind every choice in
docs/DECISIONS.md.

## Security and privacy

- `analyze` **never executes code** of the analyzed repository and **never uses the network**. The Go and Python helpers use only their standard libraries and only parse.
- Only `comment` (GitHub API) and `usage` (Datadog API) talk to the network. Error messages are not copied from Datadog, only error types.
- In CI the job that runs your code has no secrets and no write token; the job that comments never runs your code.
- Shadow mode: farol informs, it never approves, requests changes or fails a check.

## Limitations

- Static reading: values built at runtime are invisible (computed route paths, `getattr`, `importlib`, DI containers, registries filled in loops). When an entry point cannot be read, the PR is `unknown`; when a call cannot be resolved, farol assumes it reaches more, never less.
- TypeScript frontends: React Router, Next.js and TanStack Router (file-based) only: no code-based TanStack route trees, Remix/React Router file conventions, Vue or Svelte. JavaScript files, renamed files and TypeScript backends use module-level reach.
- Go: route prefixes from middleware stacks other than chi/gin/echo groups are not applied, and project types that wrap a router with their own registration API (Gitea's `web.Router`) are not read. Python: Django REST Framework routers are not read.
- The score and verdict thresholds are heuristics checked on a few repositories. Calibrate them on yours.

## FAQ

**We already have an AI reviewer. Why add farol?** They answer different questions. The agent comments on the lines
in the diff; after it, farol tells the person who approves how risky the merge is and which files carry the risk, from
static analysis of the whole program. Run both: farol's comment and report sit next to the agent's, and neither blocks
the merge.

**Is it free?** Yes. farol is open source under the MIT license, with no account, hosted service or paid tier: run it
with `npx @winninjs/farol` or the GitHub Action `winnin/farol/action`.

**Will it slow down CI?** No. farol runs after your tests and reuses their reports. The analysis takes about 3 s for
a 300-file Python service, 8–10 s for a large TypeScript monorepo or a Go service with a cold cache, and under a
second for the base when its helper output is cached.

**Can I use it outside GitHub?** Yes. `analyze`, `html` and `report` work anywhere; only `comment` is
GitHub-specific. Post the output of `npx @winninjs/farol report` with your platform's API.

**The report says "not verified".** That report was not given, or the path is wrong. Paths given to `analyze` are
relative to the current directory; paths in `farol.config.json` are relative to the project.

**A page I changed is not listed.** Run `npx @winninjs/farol routes` to see the entry points farol reads, and
`npx @winninjs/farol impact `
to see what reaches a file. Unreadable route constructs are listed under diagnostics.

**Go: "farol reads Go modules offline: run go mod download".** The module cache lacks a dependency of the base or the
head. Run `go mod download` for both before analyzing.

**Monorepo?** Point `--cwd` at the app. Paths stay relative to the repository root, and changes in apps the project
does not use are listed as outside it.

## Contributing

Contributions are welcome: route adapters, frameworks, languages, report formats and better heuristics. See
CONTRIBUTING.md for the setup, the architecture and the conventions, and
SECURITY.md to report a vulnerability.

## License

MIT © 2026 Winnin

# assembledev/edgepad

## 评论（37/37）

> **ericholiveira** · 2026-10-25T13:28:48.000Z　
> Hi HN, I built farol at Winnin, where we open-sourced it (MIT).AI agents now write a lot of our code, and AI reviewers catch a lot of
> the line-level problems. But someone still has to press "merge", and
> that person has the same question every time: how risky is this, and
> where should I spend my attention? A 40-file PR where 38 files are
> isolated is very different from a 3-file PR that changes a model used
> by 23 endpoints.farol is a CLI (and a GitHub Action) that answers that statically:- classifies the PR (global / touches-existing / isolated / unknown)
>  and gives a 0-100 merge risk score
> - ranks the files by risk and says why: what each one reaches
>  (routes, endpoints, jobs), contract breaks in API responses,
>  dependency changes, security patterns
> - diff coverage from your existing coverage report, so "38% of the
>  changed lines are tested" sits next to the risky files
> - an HTML report where you mark files as reviewed and the score and
>  test plan follow; incremental mode for "what changed since my last
>  review"; suggested reviewers from git blameHow: it uses the TypeScript compiler API for TS/React (React Router,
> Next.js, TanStack Router) and TS backends, a small go/types helper for
> Go, and Python's ast for FastAPI/Flask/Django and friends. No LLM, no
> network during analysis, and it never executes the analyzed repo's
> code. It's deterministic and informs only; it never blocks a merge.Live demo (two reports from a real PR, nothing to install):
> https://winnin.github.io/farol/demo/Try it on a branch: npx @winninjs/farol --helpLimitations: only TS, Go and Python for now, and the reachability is
> static, so dynamic dispatch and reflection make it fail closed
> ("unknown") rather than guess. I'd love feedback on the risk score
> and on false positives in your codebase.

---

> **ccvannorman** · 2026-10-25T14:02:09.000Z　
> why is the only comment by the OP flagged and dead? Is it because they were supposed to include that data in the description text rather than a comment, was it flagged as AI generated, or..?Trying to understand why the poster's own comment was flagged and killed but the original article remains up.

---

> **sikozu** · 2026-10-25T14:12:07.000Z　
> I like the concept, a risk map could be useful in some circumstances but I absolutely hate the UI design; it reeks of AI with no human thought or care put into it.

---

> **looperhacks** · 2026-10-25T14:25:11.000Z　
> Or you could, you know, read the changes your approving

---

> **alsiola** · 2026-10-25T14:38:36.000Z　
> Looked at the backend demo, and the first lines suggested to look at were importing things. Exactly what I really don't need to be reviewing

---

> **fcarraldo** · 2026-10-25T14:45:44.000Z　
> I think tools like this are needed and will become standard in the near future.However, the backend demo report seems longer and more complex than just reading the code. I’m trying to build something similar as well, and no one has quite nailed this yet.The risk map / assisted review needs to be succinct and information dense, to guide your attention. My current philosophy is that we need to be annotating code, not replacing the entire code review interface with a bunch of text.

---

> **munro** · 2026-10-25T14:51:50.000Z　
> IDK lot of noise in report, I need more signal to noise ratio, already reading so much AI output as it is.But the example PR... It said code generate with Claude, is it really still this bad? Last I was using SQLAlchemy with Claude was Opus 4.5, and it took some heavy coaching and skill gen not to generate code like this--but why even use SQLAlchemy at all if you're just going to use string interpolation jeezhttps://github.com/erich-oliveira-winnin/full-stack-fastapi-... owner = "" if current_user.is_superuser else f"WHERE owner_id = '{current_user.id}'"
>  query = f"SELECT status, count(*) FROM item {owner} GROUP BY status"
>  rows = session.execute(text(query)).all()
>
> Part of me thinks maybe because it's not popular or well documented, but SQLAlchemy has an eDSL of SQL, so you can skip the whole ORM/table mapping layer, and just use it to programmatically construct SQL syntax

---

> **osigurdson** · 2026-10-25T15:01:50.000Z　
> >> Claude Code lives in its own repository, separate from the monorepoI thought mono meant one.

---

> **messia** · 2026-10-25T15:05:57.000Z　
> it's hard for me to imagine something made with so little taste can be any good...

---

> **timcobb** · 2026-10-25T15:08:06.000Z　
> This looks nice, but I would use it with caution.There was a post here recently, "Using LLM for confidence scoring is a bad idea", my mind went immediately to using LLMs for scoring risk. Seems like a bad idea. If there's anything we still need a human for, it's assessing risk.

---

> **cowlevel** · 2026-10-25T15:24:41.000Z　
> Good idea. Do you take bribes to exclude certain lines from the risk map? Asking for my good friend Jia Tan.

---

> **hbcdbff** · 2026-10-25T17:11:48.000Z　
> I want off this train. Please, make it stop…

---

> **realitylabs** · 2026-10-25T17:58:25.000Z　
> An engineer where I work built something like this so that when QA is about to deploy, they have a better indication of who to call and what is potentially going to be impacted. Our implementation is done prior to production deploy (which requires human approval) and compares currrebt deployed build code to new build changes diff and then analyses. I think there is a lot of room for tools like this in the future. Scoping/homing/etc

---

> **cpan22** · 2026-10-25T20:39:56.000Z　
> this is very needed - I don't think we'll see a world where agents approve all our PRs but there can definitely be better tooling for focusing human attention during review

---

> **shiandow** · 2026-10-25T14:07:23.000Z　
> I'm not sure either. The comments don't look wrong to me.

---

> **rubyn00bie** · 2026-10-25T14:17:04.000Z　
> You can vouch for it, if you view the comment by clicking the time since posted a “vouch” option appears. I did it. I’ve noticed this happening more and more on here for show HN posts especially. I’m not sure if it’s like some sort of troll gang or what…

---

> **BalinKing** · 2026-10-25T14:17:41.000Z　
> AI-edited or -generated comments are disallowed by HN guidelines: https://news.ycombinator.com/newsguidelines.html#generated. I don't think any such restriction exists for submissions themselves, so that's my guess as to why the comment but not the submission has been flagged to death.

---

> **tomhow** · 2026-10-25T17:20:38.000Z　
> It was classified by our software as genai, which is explicitly against the guidelines: https://news.ycombinator.com/newsguidelines.html#genai

---

> **ericholiveira** · 2026-10-25T14:45:51.000Z　
> Thats is surely true... i did it with AI and i do lack design skills

---

> **y42** · 2026-10-25T14:27:15.000Z　
> Sire, wouldst thou perchance elaborate upon this ancient, forgotten technique, long buried in the mists of antiquity and shrouded in mysterious lore?

---

> **esafak** · 2026-10-25T15:46:35.000Z　
> Assuming it works this could focus your attention.

---

> **ericholiveira** · 2026-10-25T14:45:03.000Z　
> It suggested based on the files most used (through graph dependency), for this reason it appears as a important file (as if it breaks, it can break several places in your codebase), but that being said, you can add some files to be ignored (if you have special files, like consts or i18n)

---

> **ericholiveira** · 2026-10-25T14:48:38.000Z　
> Thanks... it surely is possible to try to reduce the amount of information

---

> **benglish11** · 2026-10-25T14:57:00.000Z　
> That’s my favorite part of sqlalchemy. I don’t even use the orm anymore.

---

> **alex_suzuki** · 2026-10-25T15:23:37.000Z　
> > SQLAlchemy has an eDSL of SQL, so you can skip the whole ORM/table mapping layer, and just use it to programmatically construct SQL syntaxYes, this is called SQLAlchemy Core: http://docs.sqlalchemy.org/en/latest/core/You can also just use psycopg (the Postgres driver layer) directly, it’s surprisingly ergonomic in my (limited) experience.

---

> **nico** · 2026-10-25T15:52:35.000Z　
> > It said code generate with Claude, is it really still this bad?Anecdata, datapoint of 1 personal experience: I had been using Opus 4.6 with no problems until yesterday, then it seemed like it was missing things constantly, introducing random bugs, forgetting basic stuff that was in its memory and skills and should never missSame thing happened on 2 separate sessions I had with Opus 4.6Ended up switching to 5.5 and Fable, things improved instantlyThis left me with a weird taste

---

> **Zambyte** · 2026-10-25T16:00:02.000Z　
> If there couldn't be multiple monorepos, there would be no such thing as a monorepo.

---

> **lubujackson** · 2026-10-25T16:38:14.000Z　
> Monorepo -> microservices -> monoreposervices

---

> **hbcdbff** · 2026-10-25T17:12:12.000Z　
> Birepo

---

> **pixl97** · 2026-10-25T17:13:44.000Z　
> >we still need a human forA trained human mind that is.Your average human in any given topic will give confidently incorrect risk assessments just like an LLM.

---

> **b473a** · 2026-10-25T16:30:44.000Z　
> What, are you doubting in the integrity of the large language binary blob?

---

> **ericholiveira** · 2026-10-25T19:22:40.000Z　
> I do agree those kinds of tools are needed... great to know youve been working on something similar

---

> **nico** · 2026-10-25T15:59:11.000Z　
> In my personal experience, it’s very rare to catch a comment/story while vouchable. Not sure how many flags does it take for something to be killed, but it seems like almost as soon as something gets flagged, it becomes a signal for others to flag it too immediately without thought (similar thing kinda happens too when you post a comment and the first vote is a downvote, it almost never recovers, even if it was a good comment, as the initial drop/greying biases anyone that sees it before they even read it)

---

> **nico** · 2026-10-25T15:55:40.000Z　
> No restriction for the submission itself, unless it’s something like an Ask/Tell/Show HN, in which the content goes directly on the post (and will get flagged if AI-generated/assisted)

---

> **lurkshark** · 2026-10-25T17:09:58.000Z　
> Out of curiosity, was this on a codebase where other folks started using Opus 5.5? I’ve been curious if each generation of model has its own biases that make it generate output that’s more difficult for other models/previous models to work with. That’s been my personal suspicion when I’ve hit situations like yours

---

> **dboreham** · 2026-10-25T16:25:21.000Z　
> Well there's one at Google, one at Facebook...

---

> **nico** · 2026-10-25T17:20:43.000Z　
> It was on 2 separate private repos, personal projects. No one else working on thoseBut now that you asked, I recently had a similar experience with Codex, but on a shared repo. I also was using a slightly older model, and the all of a sudden it kinda stopped running tasks. I would ask it to do something and the it would just kind of do an analysis, then give me a recommendation of what to do. I had to tell it to execute the task, and then it would “be lazy”, like run one part then give me a recap and recommendation again instead of just goingSwitched to a newer model, and the issue was instantly gone

## 关联链接

- https://winnin.github.io/farol/

## 导航

- 项目页：[[10-项目/github.com_61cc1fd2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
