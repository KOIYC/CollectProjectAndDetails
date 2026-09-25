---
type: "corpus"
item_id: "179c66c2436f5f92"
title: "Show HN: A live Git diff view cli to stay on top of what agents are doing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49712345"
project_url: "https://github.com/stagas/livediff"
author: "stagas"
published_at: "2026-09-15T13:37:25Z"
captured_at: "2026-09-25T13:54:52+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_stagas
  - story_49712345
  - show_hn
metrics: {"points": 6, "comments": 3, "engagement_velocity": 6}
comments_count: 2
comments_total: 3
discovered_via: "hn:show_hn:90d"
---

# Show HN: A live Git diff view cli to stay on top of what agents are doing

> [!info] 一句话导读
> A live Git diff view cli

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49712345>
> 指标：点赞=6 · 评论=3 · engagement_velocity=6
> 作者：stagas　|　发布：2026-09-15T13:37:25Z
> 项目链接：<https://github.com/stagas/livediff>
> 采集：2026-09-25T13:54:52+08:00　|　id：`179c66c2436f5f92`

## 正文

# stagas/livediff

A live Git diff view cli

- Stars: 9
- Forks: 0
- Watchers: 9
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-09-15T13:33:31Z

## Languages

- Go
- Shell

## Top Contributors

- stagas (2 contributions)

---

## README

# livediff

Stay on top of what your coding agents are doing with a live diff feed, right in
your terminal.

`livediff` watches the current Git repository and shows every edit as it happens,
whether it comes from an agent, an editor, or another tool. Changes appear like a
regular Git diff: added lines are green, removed lines are red, and unchanged
lines provide context. Each edit is shown once, keeping the feed focused on what
your agents are changing now.

## Install

Run this in your terminal:

```sh
curl -fsSL https://raw.githubusercontent.com/stagas/livediff/main/install.sh | sh
```

The installer supports Linux and macOS on x64 or ARM64, and Windows x64 through
Git Bash. It downloads a standalone executable; only Git needs to be installed.

## Get started

Open a terminal in any Git repository and run:

```sh
livediff
```

Now edit and save a file. You will see output similar to:

```diff
diff --git a/example.ts b/example.ts 3:47:12 PM
--- a/example.ts
+++ b/example.ts
@@ -1,3 +1,3 @@
-const greeting = "Hello";
+const greeting = "Hello, world!";
```

Only edits made after `livediff` starts are displayed. It watches tracked files
and new files that are not excluded by your Git ignore rules.

Press `q` or Ctrl-C to stop.

## Compact mode

For a quieter view with only the filename, time, and changed lines, run:

```sh
livediff --compact
```

The short form works too:

```sh
livediff -c
```

Compact output looks like this:

```diff
example.ts 3:47:12 PM
-const greeting = "Hello";
+const greeting = "Hello, world!";
```

## Color and install location

Disable colors when redirecting output or using a terminal without color support:

```sh
NO_COLOR=1 livediff
```

The installer uses `/usr/local/bin` when it is writable and `~/.local/bin`
otherwise. To choose a different directory:

```sh
curl -fsSL https://raw.githubusercontent.com/stagas/livediff/main/install.sh | INSTALL_DIR="$HOME/bin" sh
```

Release checksums are available as `SHA256SUMS` on the GitHub Releases page.

## Development

The project uses Go. To test or compile it from source:

```sh
go test ./...
go build -o dist/livediff .
```

## License

MIT © 2026 stagas

# Infinite Shaders - Shaderfrog

## 评论（2/3）

> **frogperson** · 2026-09-15T22:33:59.000Z　
> Is this essentially `watch git diff --compact-summary` or is there a benefit or feature of livediff I'm missing?

---

> **stagas** · 2026-09-16T10:49:29.000Z　
> That will repeat the `git diff` whereas livediff shows only the changes that happened now.

## 关联链接

- https://raw.githubusercontent.com/stagas/livediff/main/install.sh

## 导航

- 项目页：[[10-项目/github.com_80cd4d45]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
