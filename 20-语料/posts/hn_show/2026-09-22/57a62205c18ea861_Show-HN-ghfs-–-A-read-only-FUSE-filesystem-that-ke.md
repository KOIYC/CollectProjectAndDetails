---
type: "corpus"
item_id: "57a62205c18ea861"
title: "Show HN: ghfs – A read-only FUSE filesystem that keeps GitHub issues on disk"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49796385"
project_url: "https://ghfs.dev/"
author: "ghfs_dev"
published_at: "2026-09-22T03:11:11Z"
captured_at: "2026-09-22T12:53:31+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-22"
tags:
  - 语料
  - hn_show
  - author_ghfs_dev
  - story_49796385
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: ghfs – A read-only FUSE filesystem that keeps GitHub issues on disk

> [!info] 一句话导读
> already has the issue.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49796385>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：ghfs_dev　|　发布：2026-09-22T03:11:11Z
> 项目链接：<https://ghfs.dev/>
> 采集：2026-09-22T12:53:31+08:00　|　id：`57a62205c18ea861`

## 正文

gh fs
Story
Benchmarks
Download
Releases
Developer Tool
Your coding agent
already has the issue.
ghfs keeps your GitHub Issues on disk as read-only files, fetched before the agent starts.
 No tool call in the middle of a task, no copy-paste,
 no guessing at gh flags.
macOS / Linux
Windows (WSL 2)
Windows (Native)
Copy
$ curl -fsSL https://ghfs.dev/install.sh | sh
Run inside your WSL 2 terminal:
$ curl -fsSL https://ghfs.dev/install.sh | sh
Native Windows support is on the
 roadmap .
 Use WSL 2 to get started today.
Install free
Watch the 30-second demo
macOS (Apple Silicon, 26 or later, with macFUSE 5.4.0) and Linux. Free for one repository.
Demo
ghfs, in 30 seconds
An illustration of the workflow, not a screen recording. The file layout and format are what ghfs writes.
Before / After
The fetch moves out of the task.
Before
You start a task. The agent reaches for gh issue view , gets a flag wrong, retries, and finally pastes the whole issue into the conversation. Later in the same task it needs the comments again, and fetches them again.
After
The issue is already at .ghfs/github/issues/open/42.md . The agent opens it the way it opens any other file, greps across the open ones, and never leaves the working tree.
Why files
Why a file, and not a tool call.
Fetched before the task, not during it
Context is on disk before the agent starts, so nothing in the middle of a task depends on a call succeeding.
Ordinary local files
No integration to install on the agent's side. Anything that can open a file can read an issue.
The same context for every agent
Claude Code, Codex, Cursor and Copilot all read the same files, because they are just files.
Get started
Three commands.
curl -fsSL https://ghfs.dev/install.sh | sh
ghfs init
cd your-repo && ghfs
ghfs init signs you in to GitHub and installs the background service. Running ghfs inside a repository registers it. The issues appear under .ghfs/ and stay there.
On macOS, install macFUSE 5.4.0 before the first command. The full requirements are on the download page .
AI Integration
Pre-fetched for AI. No tool call in the middle of the task.
ghfs syncs issues in the background so they are already on disk when your AI needs them.
 Add one rule to your AI tool’s config, and it reads issues as local files
 — no tool call in the middle of the task, and no round-trip to GitHub to get one.
Tell your AI where issues live
Every major AI coding assistant supports project-level rules, and ghfs writes the rule for you. ghfs register offers to generate it; ghfs rules writes it any time, for the tools you pick. The rule tells the agent where the issues are and how to read them, so it opens pre-fetched issues as ordinary files instead of calling out to fetch them.
Claude Code — .claude/rules/ghfs.md
Cursor — .cursor/rules/ghfs.md
Windsurf — .windsurf/rules/ghfs.md
Cline — .clinerules/ghfs.md
GitHub Copilot — .github/copilot-instructions.md
Aider — CONVENTIONS.md
AGENTS.md — AGENTS.md
Copilot, Aider and AGENTS.md share their file with your own instructions; ghfs appends its section between markers and only ever touches that section. The other four get a file of their own.
.claude/rules/ghfs.md (excerpt)
# ghfs - GitHub Issues as Local Files
.ghfs/
└── {provider}/ # e.g., "github" or "github-work"
 └── issues/
 ├── open/
 │ └── {number}.md # e.g., "42.md"
 └── closed/
 └── {number}.md
- Read a specific issue: cat .ghfs/github/issues/open/{number}.md
- Browse open issues: ls .ghfs/github/issues/open/
- Search issues: grep -r "keyword" .ghfs/github/issues/
Read-only by design
ghfs is built read-only: there is no write path back to GitHub, so an agent
 cannot change an issue while working on it.
 What that does and does not cover, including the scopes the device flow asks for, is on the security page .
Measured, not estimated
Investigating a single issue and implementing a fix —
 10 runs each with and without ghfs, using Claude Opus 4.6.
Without ghfs
 1,356K tokens
With ghfs
 1,164K tokens
0
 AI API calls during the task
10 of 10 runs
1,356K → 1,164K
tokens (avg)
lower in 6 of 10
151s → 131s
time (avg)
faster in 6 of 10
See full benchmark results including multi-issue analysis →
10 runs per condition, Claude Opus 4.6, single issue + fix, on a pre-release build.
 The token and time differences are not separable at ten runs —
 the full results show every run.
Features
Manage issues with file operations
📁
FUSE Mount
Mount GitHub Issues as a virtual filesystem. Browse issues as a directory tree on your local machine.
🔧
Standard Tool Integration
Use cat, grep, find, jq, and any other command-line tool to work with issues directly.
🤖
AI-Ready
Feed issue context directly to AI tools like Claude Code and Cursor. They can read issues as files.
🔒
Read-Only
There is no write path back to GitHub, so an agent cannot change an issue while working on it.
👤
Multi-Profile
Switch between multiple GitHub accounts and organizations seamlessly.
🔄
Background Sync
A daemon syncs data in the background on a schedule. Always see the latest issues.
Use Cases
Built for real workflows
Give AI assistants full issue context
Claude Code and Cursor can read issue content directly as files. Just say "implement this issue" and the AI already knows every detail, comment, and label.
Terminal
# AI reads issue context from your project
$ cat .ghfs/github/issues/open/42.md
---
number: 42
title: Add OAuth2 authentication
state: open
author: mia
url: https://github.com/acme/tally/issues/42
created_at: 2026-01-08T09:12:00Z
updated_at: 2026-01-14T17:40:00Z
labels:
 - feature
 - auth
---
We need to support Google and GitHub OAuth...
$ claude "Implement issue #42"
# → Reads .ghfs/github/issues/open/42.md
# → Starts coding with full context
Search across all issues with grep
Find what you need across every issue instantly. No clicking through browser tabs one by one. Pipe, redirect, and transform however you like.
Terminal
# Find issues mentioning "memory leak"
$ grep -rl "memory leak" .ghfs/github/issues/
.ghfs/github/issues/open/87.md
.ghfs/github/issues/open/198.md
# Search by label in frontmatter
$ grep -l "bug" .ghfs/github/issues/open/*.md
Automate issue workflows with shell scripts
Read issue data programmatically to generate reports, export to spreadsheets, or build dashboards. No API wrappers needed.
Terminal
# List all issue files
$ ls .ghfs/github/issues/open/
123.md
42.md
87.md
# Extract titles from frontmatter
$ grep "^title:" .ghfs/github/issues/open/*.md
123.md:title: Dark mode support
42.md:title: Add OAuth2 authentication
87.md:title: Fix memory leak
Pricing
Simple, transparent pricing
All prices in USD. Cancel anytime. Full refund within 14 days of any charge.
Monthly
Yearly
 save 20%
Free
Get started for free
$0
No credit card required
Issues
1 repository
Background sync
Get Started
Hobby
For individual developers
$5
 /mo
$48/yr (save 20%)
Issues (all)
Unlimited repositories
Background sync
Subscribe
Pro
Everything in Hobby, plus the sources we are still building.
$15
 /mo
$144/yr (save 20%)
Issues (all)
Projects
Coming soon
Discussions
Coming soon
Pull Requests
Coming soon
Unlimited repositories
Coming soon
Enterprise
For teams and organizations
Contact
Everything in Pro
Team license management
Coming soon
Contact Us
We accept
Visa
 ·
 Mastercard
 ·
 American Express
Payments processed securely.
 See our Legal Notice .
Roadmap
What's next
We're actively building. Here's what's coming.
All
Smart Query Files
Filter issues by state, label, date, or author using filenames as queries. Read only what you need — no more loading everything at once.
Planned
Pro
Semantic Search
Search issues by meaning, not just keywords. Powered by Embedding AI, find "authentication problems" even when issues say "login error".
Planned
All
IDE Plugins
First-class integration with VSCode and JetBrains IDEs. Manage the daemon and browse issues without leaving your editor.
Planned
Pro
Projects, Discussions & Pull Requests
Browse GitHub Projects, Discussions, and Pull Requests as files — not just Issues.
Planned
All
Windows Support
Bring ghfs to Windows with WinFSP integration. Mount your issues on any platform.
Planned
Pro
Jira & Other Ticket Systems
Not just GitHub. We're exploring support for Jira, Linear, and other issue trackers as mountable filesystems.
Exploring
Enterprise
Deleted Issue Cleanup
Automatically remove deleted or transferred issues from your local mount. Essential for compliance, data retention policies, and reducing information exposure risk.
Exploring
FAQ
Questions worth asking first.
Isn't MCP enough for this?
Often it is. ghfs is for the case where you want the context already there, as files, without a call in the middle of the task.
Why not just gh issue view ?
For a single lookup, that works. ghfs is about not doing it repeatedly, and about the agent not having to remember to.
Does it sync in real time?
No. The background service fetches on a schedule, and ghfs refresh fetches on demand. What is on disk is as recent as the last fetch.
Does it write to my issues?
No. ghfs never calls a write API, and you cannot write through the mount. Worth knowing: the scopes ghfs asks for in the device flow include repo , which also grants write. Read-only is something ghfs does, not something GitHub enforces on the token.
Does it put anything in my repository?
A .ghfs symlink to the mount, and nothing else. ghfs offers to add it to your gitignore when you register the repository.
Why does it need macOS 26? I'm on 15.
macFUSE ships two File System Extensions, and the one ghfs mounts through is allowed only on macOS 26. The other one covers physically attached storage, and reaching it needs a mount option macFUSE itself calls experimental. We would rather publish the version we have actually run than the one that reads better.
I don't want to install macFUSE.
Then ghfs is not for you today, and that is a fair answer. On Linux the dependency is libfuse3 instead.
What about Windows?
Inside WSL 2 today. Native Windows is on the roadmap on this page, with no date attached.
Why is it paid, and why isn't it open source?
I have watched open-source maintainers wear themselves out, and I would rather charge for something and keep it alive. The longer answer is on the story page .
Ready to try it?
Install ghfs and start browsing GitHub Issues as local files.
Download
Release Notes
Benchmarks
 Download
 Releases
Security
 Legal Notice
contact@ghfs.dev
© 2026 ghfs. All rights reserved.

## 关联链接

- https://ghfs.dev/install.sh
- https://github.com/acme/tally/issues/42

## 导航

- 项目页：[[10-项目/ghfs.dev_ef932191]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
