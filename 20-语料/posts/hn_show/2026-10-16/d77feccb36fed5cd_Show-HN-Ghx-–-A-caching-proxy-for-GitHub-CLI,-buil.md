---
type: "corpus"
item_id: "d77feccb36fed5cd"
title: "Show HN: Ghx – A caching proxy for GitHub CLI, built for AI agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50105322"
project_url: "https://brunoborges.github.io/ghx"
author: "brunoborges"
published_at: "2026-10-15T15:42:54Z"
captured_at: "2026-10-16T09:35:18+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - hn_show
  - author_brunoborges
  - story_50105322
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Ghx – A caching proxy for GitHub CLI, built for AI agents

> [!info] 一句话导读
> ⚡ Built for AI agent workflows

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50105322>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：brunoborges　|　发布：2026-10-15T15:42:54Z
> 项目链接：<https://brunoborges.github.io/ghx>
> 采集：2026-10-16T09:35:18+08:00　|　id：`d77feccb36fed5cd`

## 正文

⚡ ghx
Features
 How It Works
 Install
 gh Shim
 Agent Plugin
 Security
 Docs
GitHub
⚡ Built for AI agent workflows
Stop hitting
 GitHub rate limits
A caching proxy for the GitHub CLI that makes repeated commands instant.
 Singleflight coalescing means 10 agents asking the same thing triggers just 1 API call.
Get Started
 View on GitHub
Why ghx?
🚀
10x Faster
Cached responses return in ~0.1s instead of ~1s. Your scripts and agents feel instant.
🔄
Singleflight Coalescing
Five agents requesting the same PR list simultaneously? Only one API call is made. All five get the result.
🎯
Allowlist-Based
Only known-safe read-only commands are cached. Mutations pass through directly and invalidate related cache entries.
🔌
Drop-In Replacement
Just use ghx instead of gh . The daemon auto-starts. No configuration needed.
📊
Built-In Dashboard
Real-time web dashboard shows hit rates, per-command stats, and a live request log. Helps you tune your TTL.
🛡️
Safe by Design
Context-aware cache keys prevent cross-repo collisions. Unix socket with strict permissions. No tokens stored.
How It Works
Agent 1
ghx
Agent 2
ghx
Agent 3
ghx
IPC
ghxd
daemon
Cache
 Singleflight
 Metrics
exec
gh
GitHub CLI
1
You run ghx pr list
The ghx client resolves your repo, branch, and auth context, then forwards the request to the ghxd daemon over a Unix socket.
2
Daemon checks the cache
Using a context-aware key (repo + branch + host + auth + args), it looks for a valid cached response. If found and within TTL, it returns instantly.
3
Cache miss? One execution only
On a miss, the daemon executes gh once. If other clients request the same thing concurrently (singleflight), they all wait for and share the single result.
4
Response is cached and returned
The stdout, stderr, and exit code are cached with a configurable TTL (default 30s). The client writes stdout/stderr and exits with the original exit code.
Real-World Performance
Measured with gh pr list --repo cli/cli --limit 2 --json number,title
Without ghx (direct gh) 1,129 ms
1.1s
With ghx (cache hit) 105 ms
0.1s
Live Dashboard
Monitor cache performance at http://localhost:9847/
JSON API
The dashboard data is also available as JSON for scripting and automation:
curl http://localhost:9847/api/stats | jq . ⎘
 curl http://localhost:9847/api/log?limit=50 | jq . ⎘
 curl http://localhost:9847/api/ttl-analysis | jq . ⎘
What Gets Cached
Only explicitly allowlisted read-only commands are cached. Everything else passes through.
Command Cached Notes
gh pr list/view/status/checks/diff ✓ Cached With any filter/format flags
gh issue list/view/status ✓ Cached Including --json , --comments
gh repo view/list ✓ Cached
gh run list/view ✓ Cached
gh workflow list/view ✓ Cached
gh release list/view ✓ Cached
gh search repos/issues/prs/commits/code ✓ Cached
gh api (GET) ✓ Cached REST GET only
gh label list ✓ Cached
gh gist list/view ✓ Cached
gh project list/view ✓ Cached
gh cache list ✓ Cached Actions cache
gh ruleset list/view/check ✓ Cached
gh org list ✓ Cached
gh pr create/merge/close ✗ Mutation Invalidates PR cache
gh issue create/edit/delete ✗ Mutation Invalidates issue cache
gh auth/config/codespace ✗ Passthrough Always direct to gh
Custom Cacheable Commands
Add commands to the allowlist without recompiling. Edit ~/.ghx/config.yaml
 and list subcommand prefixes under additional_cacheable .
 Any gh invocation whose arguments start with a listed prefix will be cached.
 Restart the daemon after making changes.
ttl: 60s
additional_cacheable:
 # Cache `gh status` output
 - "status"
 # Cache Actions variable listings
 - "variable list"
 # Cache team member queries
 - "api graphql"
Install
# Install with Homebrew (macOS)
 brew install brunoborges/tap/ghx ⎘
 # Or one-liner (macOS / Linux)
 curl -fsSL https://raw.githubusercontent.com/brunoborges/ghx/main/install.sh | bash ⎘
 # Windows (PowerShell)
 irm https://raw.githubusercontent.com/brunoborges/ghx/main/install.ps1 | iex ⎘
 # From Source
 git clone https://github.com/brunoborges/ghx.git ⎘
 cd ghx && make build ⎘
GitHub Releases
Pre-built binaries are available for macOS (Apple Silicon), Linux (x64 & arm64), and Windows (x64 & arm64).
 Browse releases →
gh Shim for Transparent Caching
When you install ghx, a lightweight gh shim is automatically placed on your PATH
 if no existing GitHub CLI is detected. This is especially powerful for AI coding agents —
 they call gh by default, and the shim ensures every command is routed through the ghx caching layer
 before hitting the real GitHub CLI. No agent configuration needed.
1
Install ghx — a gh shim is created automatically
During installation (Homebrew, install script, or PowerShell), ghx checks if a real gh binary exists on your system. If not, it installs a tiny shim at gh that routes all commands through ghx .
2
Agents call gh — caching happens automatically
AI agents like GitHub Copilot and Claude Code use gh for GitHub API calls. With the shim in place, every gh pr list , gh issue view , or gh api call flows through ghx's cache — eliminating redundant API requests and preventing rate limits, with zero changes to the agent.
3
The real GitHub CLI is obtained on first use
If ghx needs the real GitHub CLI to execute a command, it automatically downloads and installs gh for you. No manual setup required — just run your commands and ghx takes care of the rest.
⚠️ Already have the GitHub CLI installed?
When a real gh binary is detected, ghx will not install the shim — so agents will keep calling gh directly, bypassing the cache. You have two options:
Option A
Remove the GitHub CLI and reinstall ghx. The shim will be created, and agents automatically get caching via gh . ghx will download the real gh binary on first use.
Option B
Keep the GitHub CLI and install the agent plugin instead. The plugin teaches agents to call ghx directly instead of gh .
Agents Plugin
For Claude Code and
 GitHub Copilot CLI —
 install the plugin and your agent automatically prefers ghx over gh .
1
Add the marketplace
/plugin marketplace add brunoborges/agent-plugins ⎘
2
Install the plugin
/plugin install ghx@agent-plugins ⎘
3
Agent learns to use ghx
A built-in skill teaches the agent to prefer ghx for all GitHub CLI commands. Binaries are lazy-installed on first use — no manual setup needed.
Plugin Docs
 Marketplace Repo
Security
ghx is designed to be safe by default — no secrets stored, no network exposure.
🔒
Owner-Only Socket
The Unix domain socket uses 0600 permissions. Only your user can communicate with the daemon.
🔑
No Tokens Stored
Auth tokens are never written to disk or cache. Only a SHA-256 fingerprint is used in cache keys to prevent cross-account collisions.
🌐
Localhost-Only Dashboard
The web dashboard binds to 127.0.0.1 only — it is not accessible from the network.
💨
In-Memory Cache
All cached data lives in memory and is lost on daemon restart. Nothing is persisted to disk.
👤
Per-User Isolation
Each user runs their own isolated daemon instance. No shared state between users on the same machine.
ghx — MIT License —
 Made by Bruno Borges

## 关联链接

- http://localhost:9847/
- http://localhost:9847/api/log?limit=50
- http://localhost:9847/api/stats
- http://localhost:9847/api/ttl-analysis
- https://github.com/brunoborges/ghx.git
- https://raw.githubusercontent.com/brunoborges/ghx/main/install.ps1
- https://raw.githubusercontent.com/brunoborges/ghx/main/install.sh

## 导航

- 项目页：[[10-项目/brunoborges.github.io_4a8118a9]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
