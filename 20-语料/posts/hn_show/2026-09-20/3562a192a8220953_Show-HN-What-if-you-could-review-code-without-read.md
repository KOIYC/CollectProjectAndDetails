---
type: "corpus"
item_id: "3562a192a8220953"
title: "Show HN: What if you could review code without reading code?"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49743932"
project_url: "https://github.com/coldteadotai/pr-lens"
author: "ohans"
published_at: "2026-09-17T17:30:19Z"
captured_at: "2026-09-20T09:36:49+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-17"
tags:
  - 语料
  - hn_show
  - author_ohans
  - story_49743932
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: What if you could review code without reading code?

> [!info] 一句话导读
> coldteadotai/pr-lens

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49743932>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：ohans　|　发布：2026-09-17T17:30:19Z
> 项目链接：<https://github.com/coldteadotai/pr-lens>
> 采集：2026-09-20T09:36:49+08:00　|　id：`3562a192a8220953`

## 正文

# coldteadotai/pr-lens

PR Lens draws every PR as animated architecture and data-flow diagrams, inside the pull request itself. Use it as a GitHub App, GitHub Action, CLI, or a skill for your coding agent

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: MIT License
- Homepage: https://prlens.dev
- Default branch: main
- Created: 2026-08-20T19:16:16Z

## Languages

- JavaScript
- Shell
- TypeScript

## Topics

- ai-agents
- ai-code-review
- architecture-diagram
- claude-code
- code-review
- code-visualization
- cursor
- data-flow
- developer-tools
- devtools
- diagram
- diagrams
- github-action
- github-actions
- github-app
- pull-request
- pull-requests
- sequence-diagram
- software-architecture
- svg

## Top Contributors

- ohansemmanuel (81 contributions)

---

## README

# PR Lens

Reduce the cognitive load on AI-generated PRs. PR Lens draws a pull request as animated diagrams **inside the pull request itself**: architecture blast radius and data-flow pipelines, not another findings table.

 This is what lands in your pull request: a bot comment, drawn here card and all. Green is new, amber changed, red gone, and the pulse is the data moving along the new path.

Two lenses ship: **architecture** (what this change touches, against the existing system) and **data flow** (the ordered pipeline, animated). Every diagram on this page was rendered by this repo's renderer from a JSON document in this repo. This page _is_ the product demo.

## Start here

> [!TIP]
> **Paste this into your coding agent.** It installs the skill, walks you through the GitHub App, and proves the setup by diagramming the last change in your repository.

```text
Set up PR Lens (prlens.dev) for me: it draws each pull request as animated architecture and data-flow diagrams, inside the pull request itself.

1. Install the agent skill: `npx skills add coldteadotai/pr-lens`.

2. Walk me through installing the GitHub App at https://github.com/apps/coldtea-pr-lens on every repository where I review pull requests. It posts one sticky comment per pull request and updates it on every push, with no model key of mine involved.

3. If I'd rather run it from CI with a model key of mine, offer the Action instead: `.github/workflows/pr-lens.yml` using `coldteadotai/pr-lens/packages/action@v0`, with the key as a repository secret. It takes Gemini by default, OpenAI, or any endpoint speaking `/chat/completions`.

4. Then prove it: diagram the most recent change in this repository and show me the rendered SVGs.
```

No coding agent to hand? **Install the PR Lens GitHub App** on its own, that gets every pull request the comment, with no key of yours involved.

## Ways to use it

Five ways in, the prompt above sets up the first two. Every mode produces the same diagrams from the same document; pick the one that matches where you review.

 1. In your pull requests: the GitHub App · hosted · live checkboxes · no key of yours

Install the PR Lens GitHub App on your repository and open a pull request. That is the whole setup: every pull request gets the comment (the framed mockups at the top of this page are what lands), and each push updates it in place. This is the hosted mode, and the only one where the view-option checkboxes are live: tick one and the comment re-renders within seconds from the stored graph, no re-analysis, no key of yours involved.

 2. Via your coding agent · it writes the document itself · no second model bill

Your agent is usually the model. Rather than spending a provider key to describe a diff it already understands, it writes the graph document itself and lets the validator hold it to the contract.

```bash
npx skills add coldteadotai/pr-lens
```

Then say, literally:

> Diagram the change you just made with PR Lens and attach it to the pull request.

The agent reads the diff, writes the document, runs `npx @coldtea/pr-lens-cli validate` until the contract is satisfied, renders, and attaches the ` ` pair. When someone says the diagram names things wrongly, the same skill teaches it to fix `.github/pr-lens.yml` instead of editing generated output. Details in `packages/agent-skill`.

 3. As a workflow: the GitHub Action · your CI · your key · one static comment

The same comment from your own CI, drawn with your own model key. Add that key as a repository secret — `GEMINI_API_KEY` below, because `provider` defaults to Gemini — then commit this as `.github/workflows/pr-lens.yml`:

```yaml
name: PR Lens

on:
  pull_request:

permissions:
  contents: write # to publish the rendered SVGs
  pull-requests: write # to post the comment

concurrency: # one run per pull request; a push supersedes the last
  group: pr-lens-${{ github.event.pull_request.number }}
  cancel-in-progress: true

jobs:
  lens:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0 # the diff is between two commits, so both must be here
      - uses: coldteadotai/pr-lens/packages/action@v0
        with:
          api-key: ${{ secrets.GEMINI_API_KEY }}
```

Nothing here is tied to one model. `provider` takes `gemini` (the default), `openai`, or `openai-compatible` with a `base-url` and `model`, so the same workflow runs against OpenRouter, DeepSeek or a server of your own. The key reaches the CLI through the environment, never a command line, and the diff goes to the provider you name and nowhere else. The comment here is deliberately static. An Action cannot hold state between runs, so the checkboxes live in the App. Providers, lenses, branding and the rest of the inputs are in `packages/action`.

 4. From the CLI · every step on your machine, one at a time

Everything the other modes do, one step at a time, on your machine. Only `analyze` talks to a model, and its key is read from the environment, never from a flag:

```bash
export GEMINI_API_KEY=…    # the default provider; OPENAI_API_KEY with --provider openai

# Diff in, graph document out — measured against the merge base, not the branch tip.
npx @coldtea/pr-lens-cli analyze --base origin/main

# The document as light and dark SVGs, plus the manifest a comment is built from.
npx @coldtea/pr-lens-cli render .pr-lens/graph.json

# The pull request comment as markdown, on stdout. Posting is your business.
npx @coldtea/pr-lens-cli comment --graph .pr-lens/drawn.graph.json --manifest .pr-lens/manifest.json \
  --asset-base-url https://raw.githubusercontent.com/owner/repo/pr-lens/42

# Any PR Lens document, checked against the contract — every problem, not just the first.
npx @coldtea/pr-lens-cli validate .pr-lens/graph.json .github/pr-lens.yml

# After the merge: the pull-request document as a stored map of the system, worth committing.
npx @coldtea/pr-lens-cli export .pr-lens/graph.json -o .github/pr-lens.map.json
```

Everything lands in `.pr-lens/`, which the CLI adds to your `.gitignore` the first time it writes there. Treat it as scratch: the files are rebuilt from the diff on demand, and the only one worth committing is the map `export` writes. `--out` puts them somewhere else if you would rather.

Ollama, DeepSeek, OpenRouter and anything else speaking `/chat/completions` are reached with `--provider openai-compatible --base-url `. The full command reference, the correction file, and the failure codes a script can branch on are in `packages/cli`.

 5. In your terminal · the diagram before the pull request exists

Nothing about the diagrams needs a pull request. Render locally and look at the change before anyone else does:

```bash
npx @coldtea/pr-lens-cli analyze --base origin/main
npx @coldtea/pr-lens-cli render .pr-lens/graph.json
open .pr-lens/*-dark-*.svg    # macOS; the SVGs are self-contained, any browser reads them
```

This is also the shape of reviewing an agent's work: while you read the diff, the agent that wrote it renders it. With the skill installed, "render this change with PR Lens and open the SVGs" gets you the diagram beside the diff, the same picture its pull request will carry, minutes earlier.

## From one card to a monorepo

The renderer answers for every size of change with the same visual grammar: lanes, node cards, delta colours, and routes you can trace with the eye alone.

 The smallest honest diagram: 1 lane · 1 node · 0 edges.

 The dense synthetic: 3 lanes · 15 nodes · 19 edges. Crossings happen inside corridors and read as wiring, not spaghetti.

 Tier 4: a checkout flow · 5 lanes · 21 nodes · 24 edges

 Tier 5: a monorepo · 6 lanes · 37 nodes · 49 edges

 Collapsed tiers dogfood the same ` ` drill-down pattern the PR comment uses.

## The data-flow lens

The ordered pipeline of the change, drawn in the same design system: participants are real node cards, labels are the same pills, colours are the same deltas. **The pulses are moving right now**: PR Lens diagrams are animated SVG, and the animation survives GitHub's image proxy, a hook no findings table has.

 The reference pull request's send pipeline: 7 steps sharing one cycle and taking it in turn. One dot crosses one arrow at a time, in the order the steps happen, and the next arrow lights as the last dot lands.

 Every message kind at once: a filled head waits for an answer, an open head is fire-and-forget, a dashed line _is_ the answer, and only waited-on work lights an activation bar.

Every render above comes from a checked-in fixture, regenerated deterministically by `docs/showcase/render.mts`: the teaser, the reference pull request, the dense synthetic, the upper tiers, the mixed-kinds flow. The comment mockups up top are framed by `docs/showcase/frame.ts` around the same renders, with the composer's real text.

## Packages

| Package | What it is |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `packages/schema` | `@coldtea/pr-lens-schema`: the contract every other component speaks |
| `packages/renderer` | `@coldtea/pr-lens-renderer`: deterministic JSON graph → the animated, theme-paired SVGs on this page |
| `packages/cli` | `@coldtea/pr-lens-cli`: read a diff with your own model key, render it, compose the comment |
| `packages/action` | the GitHub Action: analyze, publish, post one static comment |
| `packages/agent-skill` | `@coldtea/pr-lens-agent-skill`: teaches a coding agent to draw the change it just made |

## Working in this repo

```bash
pnpm install
pnpm verify      # build, typecheck, test
```

Node 20.11+ and pnpm 10.

## License

MIT © Coldtea AI.

# Custom Relevance

## 关联链接

- https://github.com/apps/coldtea-pr-lens
- https://prlens.dev
- https://raw.githubusercontent.com/owner/repo/pr-lens/42

## 导航

- 项目页：[[10-项目/github.com_bfc01f4b]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
