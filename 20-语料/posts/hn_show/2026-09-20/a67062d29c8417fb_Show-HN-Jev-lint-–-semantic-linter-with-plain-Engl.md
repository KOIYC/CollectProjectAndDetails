---
type: "corpus"
item_id: "a67062d29c8417fb"
title: "Show HN: Jev-lint – semantic linter with plain English rules"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49771155"
project_url: "https://github.com/zdenham/jev-lint"
author: "zdenham"
published_at: "2026-09-19T23:52:12Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_zdenham
  - story_49771155
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Jev-lint – semantic linter with plain English rules

> [!info] 一句话导读
> Lint JavaScript and TypeScript against plain-English project conventions with Jev.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49771155>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：zdenham　|　发布：2026-09-19T23:52:12Z
> 项目链接：<https://github.com/zdenham/jev-lint>
> 采集：2026-09-20T09:48:16+08:00　|　id：`a67062d29c8417fb`

## 正文

# zdenham/jev-lint

Lint JavaScript and TypeScript against plain-English project conventions with Jev.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- Default branch: main
- Created: 2026-09-19T22:59:50Z

## Languages

- TypeScript

## Top Contributors

- zdenham (6 contributions)

---

## README

# jev-lint

Check JavaScript and TypeScript against project conventions written in plain English. Define inline or Markdown rules; Jev reports possible violations. Built for coding agents, with compact output by default and optional pretty or JSON output.

Early release: review findings before making them block CI. Checks use whole-file context without resolving imports, locate top-level declarations or class members, and count uncertain results separately from compliance. The tool does not edit code.

## Install and set up

Requires Node.js **22.22+** and Git:

```sh
git clone https://github.com/zdenham/jev-lint.git
cd jev-lint
npm ci
npm run build
npm link
```

The global command links to this checkout; keep it in place. If needed, add npm's global executable directory to PATH (`$(npm prefix --global)/bin` on macOS/Linux). Update with `git pull`, `npm ci`, and `npm run build`; remove with `npm uninstall --global jev-lint`.

In your project, create `jev.config.json` without installing project dependencies:

```sh
cd /path/to/your-project
jev-lint init
```

For live checks, get a Vercel AI Gateway API key and export it or set it in `.env.local` beside the config:

```sh
export AI_GATEWAY_API_KEY="your-key"
```

Selected source and rules are sent to Jev through Vercel AI Gateway using your credits; no deployment is needed. Add `.env.local` and `.jev/reports/` to your project's `.gitignore`.

## Write rules

Edit `jev.config.json`:

```json
{
  "files": ["src/**/*.{ts,tsx}"],
  "ignore": ["src/generated/**"],
  "rules": {
    "preserve-error-cause": {
      "instruction": "When rethrowing an unexpected error, preserve the original error as its cause.",
      "severity": "error"
    },
    "user-facing-errors": {
      "files": ["src/ui/**"],
      "instruction": { "file": "docs/conventions.md#user-facing-errors" }
    }
  }
}
```

Paths are relative to the config. Rule-specific `files` narrow the top-level selection. Severity defaults to `warning`; `error` fails the check.

Markdown rules should include examples and exceptions:

```markdown
## User-facing errors

Explain what went wrong and what the user can do next.

Good: "We couldn't save your changes. Check your connection and try again."
Bad: "Mutation failed: ERR_UPSTREAM_502."

This applies to messages shown to users, not internal logs.
```

A `#heading` includes subsections and code examples; omit it to use the whole file. Markdown files must stay within the config directory or its descendants. Examples guide judgment and are never executed.

## Run and inspect

```sh
jev-lint --dry-run          # Preview files, rules, and cost estimate offline
jev-lint                   # Check configured files
jev-lint src/ui             # Narrow to a file or directory
jev-lint --changed main     # Check whole tracked files changed from main's merge-base
jev-lint --format pretty    # Human-readable code frames
jev-lint --format json      # Programmatic output
```

Output includes locations, rule references, token usage, billed/market costs, and a saved report path. Missing usage or costs are marked incomplete or unavailable. Output defaults to 20 findings and 16 KiB, with explicit truncation; use `--summary` for counts or `--max-output-bytes` to adjust the budget.

Inspect saved reports without API calls:

```sh
jev-lint report /path/to/report.json --finding f_1
jev-lint report /path/to/report.json --offset 20 --limit 20
```

Exit codes: **0** within finding limits, **1** error findings or excess warnings, **2** configuration or execution failure. Use `--max-warnings 0` to fail CI on warnings and `--help` for all options.

## Cost and run limits

Defaults are **$1, 10 files, 10 requests, and 100,000 total input bytes**. Set a top-level `limits` object in `jev.config.json`; omitted values keep their defaults:

```json
"limits": {
  "maxCostUsd": 1,
  "maxFiles": 10,
  "maxRequests": 10,
  "maxInputBytes": 100000
}
```

Override per run with `--max-cost-usd 0.25`, `--max-files 30`, or `--max-requests 30`. Each selected file uses at most one evaluation request; fresh runs are not cached.

Costs depend on source size, rules, and pricing. Live runs check current Gateway pricing before evaluation; dry runs use a dated local snapshot. Over-budget estimates block evaluation, and costs are checked between requests using market value even when credits reduce the bill.

**The dollar budget is a client-side guardrail, not a guaranteed billing cap:** an in-flight request may exceed its estimate. Budget stops exit `2` and save partial results; a zero dollar budget blocks evaluation.

## Contributing

See CONTRIBUTING.md for development commands, architecture, and extension points.

# DH Tools - 46+ Free Online Web & Developer Tools | Fast & Private

## 关联链接

- https://github.com/zdenham/jev-lint.git

## 导航

- 项目页：[[10-项目/github.com_9b5afa65]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
