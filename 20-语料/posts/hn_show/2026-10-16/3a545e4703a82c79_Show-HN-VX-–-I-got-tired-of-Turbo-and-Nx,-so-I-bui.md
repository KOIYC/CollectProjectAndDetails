---
type: "corpus"
item_id: "3a545e4703a82c79"
title: "Show HN: VX – I got tired of Turbo and Nx, so I built vx"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50106776"
project_url: "https://vznjs.github.io/vx"
author: "exelord"
published_at: "2026-10-15T17:07:22Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_exelord
  - story_50106776
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: VX – I got tired of Turbo and Nx, so I built vx

> [!info] 一句话导读
> Skip to content vx Features Speed Low overhead on every run, cold or cached.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50106776>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：exelord　|　发布：2026-10-15T17:07:22Z
> 项目链接：<https://vznjs.github.io/vx>
> 采集：2026-10-16T09:35:18+08:00　|　id：`3a545e4703a82c79`

## 正文

Skip to content vx Features Speed Low overhead on every run, cold or cached.
 Cache you can trust A hit replays exactly what a run would have made.
 Correct by default Nothing leaks in, nothing wrong comes back.
 Run what you mean Pick tasks precisely, and stop the ones that hang.
 Output that fits As much as you want to read, where you read it.
 See inside a run Every key, plan and past run, on request.
 Config TypeScript you can read, with errors that point.
 Everyday use The small things you meet every day.
 CI Run less, and read the result where you work.
 Adoption From install to cached in minutes.
 Plugins Seams for where tasks run, cache and report.
 Every feature, one line each
 All of features →
Docs Quickstart Install, configure, cached in a minute.
 Configure Tasks, inputs, outputs, env.
 Sandboxing A task touches only what it declares.
 CI and remote Affected runs, remote cache, execution.
 Migrate From Turborepo or Nx in one command.
 AI agents The agent skill, JSON output, vx why.
 Plugins Every stage is a seam.
 Playground The planner, in your browser.
 All of docs →
Reference Commands Every verb and flag.
 vx.config.ts Every config key.
 Caching in depth How a key is made.
 Benchmarks vx against Turborepo and Nx.
 Compare vx, Turborepo, Nx, Bazel.
 Security model What a task and a cache can reach.
 All of reference →
Blog vx on real repos: wall times Oct 15, 2026
 Say which projects may depend on which Oct 14, 2026
 One name per setting Oct 14, 2026
 Where a task run spends its time Oct 14, 2026
 All of blog →
Releases v0.0.638 · Clear output, kept CI runs, shared timings Oct 15, 2026
 v0.0.637 · Any language, one lock, a cache PRs share Oct 15, 2026
 v0.0.636 · Choose how vx treats inputs that move Oct 13, 2026
 v0.0.635 · vx skips the save when an input moves Oct 12, 2026
 All of releases →
Search Ctrl K Cancel
Home Features Docs Reference Blog Releases GitHub
 GitHub Bluesky dev.to RSS Select theme Dark Light Auto
New v0.0.638 Clear output, kept CI runs, shared timings → Task orchestration you own .
 vx runs and caches your task graph correctly, and every stage after that is a seam you can fill.
 15 pipeline stages a plugin can fill
 MIT sandbox, remote cache and remote execution, no paid tier
 0 daemons, accounts or cloud services to run it
 $ npm install -g @vzn/vx
 Quickstart → GitHub
// ai first
 The build your agents can run.
npx skills add vznjs/vx
 One skill teaches any coding agent the CLI: run tasks, read failures and history, ask why.
 vx run
 vx last --failed
 vx last --stats
 vx why
 vx docs
 Built for agents → vx why
 A re-run names its cause, down to the file that changed.
 $ vx why @demo/web#build
 verdict cache key changed: upstream @demo/ui#build
 root cause:
 @demo/web#build ← @demo/ui#build ← file packages/ui/src/index.ts How vx why works → --format json
 Every report verb prints JSON with a published schema, and failures keep their full log.
 vx show
 vx info
 vx last
 vx why
 --dry=json
 Every command →
// extensibility is king
 What vx can do. Not what it is limited to.
Every plugin below is a separate package on core’s public seams, and yours can be too.
 Remote cache and remote execution
 @vzn/vx-reapi Any Bazel REAPI server: NativeLink, BuildBuddy, your own.
 Keep the cache you have
 @vzn/vx-migrate Keep Turbo’s or Nx’s remote cache while you move to native config.
 Observability
 @vzn/vx-otel Every run and task in any OpenTelemetry backend.
 CI results on the PR
 @vzn/vx-ci GitHub job summary and Checks.
 Smarter scheduling
 @vzn/vx-schedule-history Order by the critical path learned from your run history.
 Precise lockfile keys
 @vzn/vx-lockfile Each task keyed on its own dependency closure: pnpm, bun, npm, yarn.
 Your own
 definePlugin() Fill any of the 15 stages: where tasks run, where the cache lives, who watches, what the terminal draws, which commands exist.
// 9,603 tasks · 1,601 projects · 30 levels · identical commands, identical concurrency
 Fast, never at the cost of a correct cache.
Nothing changed vx 856 ms
 Turborepo 855 ms
 Nx 23.22 s
 Vite Task 11.24 s
 Nothing changed, outputs restored vx 1.45 s
 Turborepo 1.50 s
 Nx 21.64 s
 Vite Task 11.21 s
 Cold build vx 7.73 s
 Turborepo 10.32 s
 Nx 3 min 23 s
 Vite Task 9.44 s
 Cold build: CPU the runner burns vx 36.42 s
 Turborepo 1 min 3 s
 Nx 5 min 35 s
 Vite Task 25.64 s
Time each tool adds over the ideal run; lower is better.
 Benchmark workload: a synthetic monorepo of 1,601 projects and 9,603 tasks in 30 dependency levels, five core libraries a quarter of the projects use; build 300 ms, test and typecheck 150 ms, lint 75 ms, publish 30 ms; real repos with uneven task times will differ.
 Run 2026-10-12 on linux x64, 4 cores: vx at commit 126d60a93, Turborepo 2.11.7, Nx 23.3.0, Vite Task (vite-plus) 1.1.0.
Nothing boots per task. No daemon, no Node process per task: vx spawns your command.
 Hashing without reading. On a clean tree, cache keys come from git’s index.
 One pass over the repo. One git walk per run; each stat and lookup happens once.
 Benchmarks: tables, methodology, reproduce it → When another tool is the better pick →
// shipping every day
 New in vx.
Every release → The blog →
Latest release · v0.0.638 Clear output, kept CI runs, shared timings
 Every vx verb now speaks in one shape and says how to fix what it refuses, a CI run keeps the logs and outputs you need to debug it, a new branch forecasts from main's timings, and a run your local cache answers stays off the network.
 Oct 15, 2026 Read the release → Oct 15, 2026 v0.0.637 Any language, one lock, a cache PRs share
 Oct 13, 2026 v0.0.636 Choose how vx treats inputs that move
 Oct 12, 2026 v0.0.635 vx skips the save when an input moves
From the blog
 benchmarks
 vx on real repos: wall times
vx on real repos: wall times Oct 15, 2026 config
 Say which projects may depend on which
Say which projects may depend on which Oct 14, 2026 DX
 One name per setting
One name per setting Oct 14, 2026
// vx vs Turborepo vs Nx
 Built in, free, on your own machines.
vx Turborepo Nx
 A file sandbox for every task ✓ Local and free, Linux and macOS ✕ None $ Nx Cloud add-on
 Remote execution you host ✓ Bazel’s open REAPI protocol ✕ None $ Nx Agents on Nx Cloud
 A remote cache on any backend ✓ REAPI, Turborepo’s or Nx’s wire, by plugin ✕ Its own HTTP API ✕ Nx Cloud or its own API
 Config is code ✓ TypeScript, evaluated and hashed ✕ JSON ✕ JSON, merged with inferred tasks
 No background daemon ✓ None ✓ None for turbo run ✕ On by default
 Every choice, with sources, and when another tool fits better →
// four commands
 Start in a minute.
npm install -D @vzn/vx
npx @vzn/vx init # a vx.config.ts per package; add the cache block each TODO shows
npx @vzn/vx run build --all # builds in dependency order; stores what is cached
npx @vzn/vx run build --all # again: the cached tasks are up-to-date Coming from Turbo or Nx: the same vx init writes the native vx config from it.
 Quickstart: a cache block, the first hit → Migrate from Turbo or Nx →
// one run, after you edit app
 Everything vx does, in one picture.
One run of vx run build, after you edit app. 1 Tasks. app builds after what it uses.
 2 Parallel. ui and api build at once.
 3 Cache. Unchanged work comes back from the cache.
 4 Only what changed. You edited app ; only app runs.
 5 Sandbox. A workspace file you did not declare is out of reach.
 6 Plugins. Swap the cache, runner or telemetry. No fork.
// what you can count on
 Correct. Sandboxed. Extensible. Free.
Correctness
 A task’s cache key covers every file, setting and env var it declares.
 Caching in depth → Sandbox
 A sandboxed task cannot read a workspace file it did not declare.
 Sandboxing → Extensibility
 Plugins decide where tasks run, where the cache lives and who watches.
 Writing a plugin → Freedom
 MIT, no paywall, no cloud, no account.
 Migrate →
// 116 features, a page each
 And everything else.
Cache you can trust Sandboxed tasks
 An undeclared read or write fails the task and names the path.
See inside a run vx why
 Ask why a task re-ran, and get the input that changed.
Cache you can trust Outputs are exactly the snapshot
 A module you deleted never comes back from the cache.
CI Run only what a change reaches
 --affected follows task edges from the change, and nothing else runs.
Everyday use Dev servers in the graph
 A server is ready when it prints a line, not after sleep 5 .
Everyday use Watch mode
 Every change takes the same path as vx run , and the key decides what re-runs.
Plugins Remote cache and execution
 Distributed builds over Bazel’s open Remote Execution API.
See inside a run A skill for your coding agent
 An installable skill teaches an agent to run, debug and query vx.
All features →
vx
 One binary · MIT licensed · no account.
docs
 Features Quickstart Configure Sandboxing CI and remote Migrate Plugins Try it
reference
 CLI Config Benchmarks vx, Turborepo, Nx, Bazel Parity map for Turbo and Nx Glossary
community
 GitHub Bluesky dev.to Blog
© 2026 vx contributors MIT licensed · @vzn/vx
 Turborepo, Nx and other product names are trademarks of their owners. vx is not affiliated with or endorsed by them.
Turborepo, Nx and other product names are trademarks of their owners. vx is not affiliated with or endorsed by them.

## 导航

- 项目页：[[10-项目/vznjs.github.io_c7f80260]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
