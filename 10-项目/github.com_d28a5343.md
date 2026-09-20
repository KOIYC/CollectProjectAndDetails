---
type: "project"
title: "Show HN: Kibana-agent – query Kibana logs from CLI"
project_url: "https://github.com/hyzyla/kibana-agent"
first_seen: "2026-09-20T09:48:16+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_hyzyla
  - story_49770502
  - show_hn
lang: "en"
---

# Show HN: Kibana-agent – query Kibana logs from CLI

> [!info] 一句话导读
> Kibana/ES CLI for logs

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/hyzyla/kibana-agent>
> 首次收录：2026-09-20T09:48:16+08:00
> 来源渠道：HN Show HN
> 标签：author_hyzyla, story_49770502, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/392e5cb1b2f36c4e_Show-HN-Kibana-agent-–-query-Kibana-logs-from-CLI]] |
| 2026-09-20T09:36:35+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/392e5cb1b2f36c4e_Show-HN-Kibana-agent-–-query-Kibana-logs-from-CLI]] |
| 2026-09-20T09:48:16+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/392e5cb1b2f36c4e_Show-HN-Kibana-agent-–-query-Kibana-logs-from-CLI]] |

## 摘要正文

# hyzyla/kibana-agent  Kibana/ES CLI for logs  - Stars: 5 - Forks: 0 - Watchers: 5 - Open issues: 0 - License: MIT License - Homepage: https://pypi.org/project/kibana-agent/ - Default branch: main - Created: 2026-04-07T20:58:13Z  ## Languages  - Python  ## Topics  - elastic - elasticsearch - kibana - logs  ## Top Contributors  - hyzyla (14 contributions)  ---  ## README  # kibana-agent  Read-only Kibana/ES CLI for AI agents. Queries Elasticsearch through Kibana's console proxy API.  ## Install  ```bash uv tool install kibana-agent  # or just run: # uvx kibana-agent ```  ## Setup  ```bash kibana-agent profile create prd --url https://kibana.example.com --auth 1password \   --op-username "op://vault/item/username" --op-password "op://vault/item/password" --use ```  Auth: `1password` (Touch ID, cached 30 min), `keychain` (OS keyring — macOS Keychain / Linux Secret Service / Windows Credential Locker via the `keyring` library; on Linux requires a running Secret Service provider such as gnome-keyring, KWallet, or KeePassXC), `plain`.  ## Usage  ```bash kibana-agent context                                            # index overview kibana-agent search 'my-index-*' --last 1h -n 10       …
