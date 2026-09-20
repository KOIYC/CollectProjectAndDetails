---
type: "corpus"
item_id: "9b5c0ed172872385"
title: "Show HN: Review agent changes locally before pushing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49721156"
project_url: "https://github.com/marcparadise/reviewer"
author: "GrinningFool"
published_at: "2026-09-16T01:39:55Z"
captured_at: "2026-09-20T09:37:07+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_GrinningFool
  - story_49721156
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: Review agent changes locally before pushing

> [!info] 一句话导读
> marcparadise/reviewer

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49721156>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：GrinningFool　|　发布：2026-09-16T01:39:55Z
> 项目链接：<https://github.com/marcparadise/reviewer>
> 采集：2026-09-20T09:37:07+08:00　|　id：`9b5c0ed172872385`

## 正文

# marcparadise/reviewer

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: GNU Affero General Public License v3.0
- Default branch: main
- Created: 2026-09-14T04:22:52Z

## Languages

- CSS
- Go
- HTML
- JavaScript

## Top Contributors

- marcparadise (1 contributions)

---

## README

This document written and maintained by a human.

# reviewer

`reviewer` is a small self-hosted code review tool and light-weight workflow for reviewing agent-generated changes locally.

Somewhere around the thousandth time you give your agent permission to continue working, something slips through: an architectural choice that isn't what you meant, an object that's getting bloated, or some weird backwards-compatibility code gymnastics the agent applies to an internal-only implementation. Taking a step back to view the entirety of the changes -- instead of just as scroll-by approval blobs in the harness -- often makes it easier to catch issues.

This tool helps by allowing you to perform a local review (similar to GitHub PRs), and annotate the code with comments for your agents to address. Once you approve the changes, you or the agent can push the branch to your normal upstream such as GitHub, GitLab, etc for collaborative review. By design, the agent can fix the issues you raise but it can't reply like on a PR. This is intentional -- if you need a conversation with the agent, your preferred harness is the best tool for that job.

This repository contains a sample workflow in which the agent does most of the work: creating commits, pushing, waiting for review comments, applying changes based on comments, and merging the approved branch locally. The instructions to do this can be turned into a skill or used directly. They're pretty lightweight at an estimated 500-700 tokens depending on model and can be adapted for other workflows such as pushing to an upstream instead of merging.

## Features

* local-only lightweight code review workflow for agent-generated code
* minimal agent instructions required, even for local agents (500-700 tokens)
* web UI for reviewing changes and leaving comments
 * see open reviews and their status
 * dark-mode support
 * supports multi-line code selection for comments, and comments on deleted lines.
 * syntax coloring (toggleable) for many languages via chroma
 * side-by-side and unified diff views
 * per-commit diff filtering
 * view changes since last review
* handles rebases/force pushes with reasonable grace.
* comments/change requests can be preserved with the commit message to retain context without relying on a local tool

## Screen Captures

Dark Mode: Diff view with commit details

Light Mode: Commit view

Light Mode: Diff view with comments inline

Light Mode: List of open reviews

## Architectural Overview

 * running `reviewer init` creates a local bare-bones git repository (default: `~/.config/reviewer/repos/.git`) and adds it to your repository as remote named `review`. The repo contains two hooks:
 * pre-receive: verifies that the reviewer service is locally available, and rejects the push if not.
 * post-receive: creates the review (via POST to api/hooks/post-receive), and replies with the review URL for the operator.
 * project and review records are stored in a SQLite database (default: `~/.config/reviewer/reviewer.db`).
 * `reviewer serve` starts the REST and UI services. You can access the UI from the browser at http://localhost:8192 (default port)
 * webui is a plain html/js/css SPA that does not make use of any third party resources/external deps
 * this is a single-user tool, with no authentication - therefore it will only listen on loopback.

It also does some work to keep things in sync, so that if branches are force-pushed or deleted it correctly resyncs/tracks them in the DB .

## Other notes

The AGENTS.md file contains information on repository layout and contents.

In addition you'll see a package.json/lock. This project makes use of node for testing of the webui bits only. It has no runtime usage.

## Requirements

- (for building or installing via `go install`) Go 1.26+
- `git`
- `curl` (used by the server-side git hook)

## Quick Start

This quick start is for manual usage. I recommend instead instructing your agent on how to handle these review process steps directly. A sample agent instruction set is provided in docs/examples/basic-flow/git.md. It can be used as a skill, or added to your project/global AGENTS.md equivalent. This is similar to the workflow I use.

0. Install from source or via: `go install marcparadise.io/projects/reviewer/cmd/reviewer@latest`
1. Start the server or use the included systemd unit: `reviewer serve`, which starts the service on the default port 8091.
2. In your project directory, run `reviewer init`
3. Once you have something to review, push the branch to the `review` remote: `git push review `. Pushes to the `review` remote will be rejected unless the `reviewer` service is running.
4. Instruct your agent to wait with no timeout for the review to complete: `reviewer wait`
5. Follow the link provided from the `push` to review the changes

Typically the agent would repeat the cycle starting with step 3: make the changes, commit, push, and wait for the review to complete. In my workflow (project-dependent), approval signals either a merge to main or a push to remote upstream for full review. The merge path is shown in the example.

For more detailed instructions, see docs/getting_started.md

### Updates

Updates that change the hooks will need you to run `reviewer install-hooks` to ensure the hooks are up to date before killing and restarting the server. This operation effectively idempotent.

## Contributions and Future Maintenence

Use at your own risk. This is a personal tool I've found very useful as I've built it over the last few months. I shared it in hopes it would also be useful to you. I will keep updating this tool for as long as I continue to find it useful and in need of changes. I'm unlikely to accept contributions.

I'll accept suggestions and bug reports in the form of issues, but I'm highly allergic to AI-generated text in public discourse. If I suspect an issue is LLM word-vomit, I'll close it without looking too closely.

### Support

Support is available for an exhorbitant fee that scales with with customer revenue.

## License

This is licensed under the AGPLv3. In addition, teams or individuals who modify this to suit their needs are free to do so, and are released from any obligation to share their changes unless distributing externally.

Dual licensing is available for a fee.

## Partial CLI reference

For a full list of commands and options, run `reviewer --help` or `reviewer --help`. Following are what you're most likely to need:

```
# Run the server
reviewer serve          [--port PORT] [--data-dir DIR]

# Initialize a project for use with reviewer
reviewer init           [--base-branch BRANCH] [--port PORT] [--data-dir DIR]

# Wait for a review to be completed (blocking)
reviewer wait           [BRANCH] [--json] [--timeout DURATION] [--data-dir DIR] [--port PORT]

# Format a block of text indicating the review comments with line number context, suitable for inclusion in a commit message
reviewer response-block [BRANCH] [--data-dir DIR] [--port PORT]

# reinstall the git hooks for all repositories. Useful if they've been modified or you have made changes to e.g. listen port number.
reviewer install-hooks  [--data-dir DIR] [--port PORT]
```

`--data-dir` defaults to `$XDG_CONFIG_HOME/reviewer`. `--branch` defaults to the current branch. `--port` defaults to 8091.

# Thurbeen/thurbox

## 关联链接

- http://localhost:8192

## 导航

- 项目页：[[10-项目/github.com_a1049eda]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
