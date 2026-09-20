---
type: "corpus"
item_id: "392e5cb1b2f36c4e"
title: "Show HN: Kibana-agent – query Kibana logs from CLI"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49770502"
project_url: "https://github.com/hyzyla/kibana-agent"
author: "hyzyla"
published_at: "2026-09-19T22:07:16Z"
captured_at: "2026-09-20T09:48:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-19"
tags:
  - 语料
  - hn_show
  - author_hyzyla
  - story_49770502
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Kibana-agent – query Kibana logs from CLI

> [!info] 一句话导读
> Kibana/ES CLI for logs

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49770502>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：hyzyla　|　发布：2026-09-19T22:07:16Z
> 项目链接：<https://github.com/hyzyla/kibana-agent>
> 采集：2026-09-20T09:48:16+08:00　|　id：`392e5cb1b2f36c4e`

## 正文

# hyzyla/kibana-agent

Kibana/ES CLI for logs

- Stars: 5
- Forks: 0
- Watchers: 5
- Open issues: 0
- License: MIT License
- Homepage: https://pypi.org/project/kibana-agent/
- Default branch: main
- Created: 2026-04-07T20:58:13Z

## Languages

- Python

## Topics

- elastic
- elasticsearch
- kibana
- logs

## Top Contributors

- hyzyla (14 contributions)

---

## README

# kibana-agent

Read-only Kibana/ES CLI for AI agents. Queries Elasticsearch through Kibana's console proxy API.

## Install

```bash
uv tool install kibana-agent

# or just run:
# uvx kibana-agent
```

## Setup

```bash
kibana-agent profile create prd --url https://kibana.example.com --auth 1password \
  --op-username "op://vault/item/username" --op-password "op://vault/item/password" --use
```

Auth: `1password` (Touch ID, cached 30 min), `keychain` (OS keyring — macOS Keychain / Linux Secret Service / Windows Credential Locker via the `keyring` library; on Linux requires a running Secret Service provider such as gnome-keyring, KWallet, or KeePassXC), `plain`.

## Usage

```bash
kibana-agent context                                            # index overview
kibana-agent search 'my-index-*' --last 1h -n 10                 # search logs
kibana-agent count 'my-index-*' -q '{"match":{"level":"ERROR"}}'   # count docs
kibana-agent tail 'my-index-*' -f @timestamp,level,message        # live stream
kibana-agent histogram 'my-index-*' --last 6h --interval 10m     # date histogram
kibana-agent discover 'my-index-*' --kql "level:ERROR"            # Kibana URL
```

## Agent setup

Add to your `CLAUDE.md` (or equivalent system prompt):

```markdown
Use `kibana-agent` to query Elasticsearch. Start with `kibana-agent context` to
discover indices and fields, then use `kibana-agent search`, `kibana-agent count`,
`kibana-agent histogram` to investigate. Run `kibana-agent agent-help` for full
usage reference.
```

Output is JSON. All operations are read-only.

## MCP server

The same operations are also available as an MCP server (`kibana-agent mcp`) for use with Claude Code, Claude Desktop, Cursor, etc. Profiles and credentials are shared with the CLI.

## License

MIT

# thissayantan/frost-icon-theme

## 关联链接

- https://kibana.example.com
- https://pypi.org/project/kibana-agent/

## 导航

- 项目页：[[10-项目/github.com_d28a5343]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
