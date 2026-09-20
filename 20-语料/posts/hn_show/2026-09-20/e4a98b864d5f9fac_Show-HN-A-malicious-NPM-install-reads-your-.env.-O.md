---
type: "corpus"
item_id: "e4a98b864d5f9fac"
title: "Show HN: A malicious NPM install reads your .env. On my Mac it reads a decoy"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49714094"
project_url: "https://jitpass.com/"
author: "bukershok"
published_at: "2026-09-15T15:31:52Z"
captured_at: "2026-09-20T09:37:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-15"
tags:
  - 语料
  - hn_show
  - author_bukershok
  - story_49714094
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: A malicious NPM install reads your .env. On my Mac it reads a decoy

> [!info] 一句话导读
> jit · just-in-time passwords for developer endpoints

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49714094>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：bukershok　|　发布：2026-09-15T15:31:52Z
> 项目链接：<https://jitpass.com/>
> 采集：2026-09-20T09:37:12+08:00　|　id：`e4a98b864d5f9fac`

## 正文

Author: jitpass

jit · just-in-time passwords for developer endpoints

# There is a live API key in plaintext on your Mac.

It sits in `.env`, in `~/.aws/credentials`, in `~/.zsh_history`. One compromised package or one hijacked agent, and it is gone, silently. jit locks the real values away and leaves decoys in your files. Your tools keep working. Whatever gets stolen is worthless.

jit protects your secrets from:

prompt-injected agents compromised npm packages trojanized IDE extensions rogue MCP servers infostealer malware shell-history scrapers stolen backups and dotfiles

~/acme-checkout

```
$ jit scan
jit scan  ~/ · 4 files · 1ms

  YOUR SECRETS: 6 — 0 protected by jit (0%)
  ▱▱▱▱▱▱▱▱▱▱  to 100%: one command +100%

  jit will protect these — 6 secrets in 4 files, 0% → 100%
      → jit migrate
        ~/.aws/credentials      acme-prod/aws_secret_access_k…
        ~/.zsh_history          GitHub Personal Access Token,
                                AWS Access Key ID
        ~/acme-checkout/.env    secret-shaped values
        ~/acme-checkout/.npmrc  //registry.npmjs.org/:_authTo…

  No secret values are ever printed in full.
```

Real output, on a machine with four ordinary files on it. Nothing here is a mock-up.

## Find your exposed secrets before malware does.

`jit scan` looks in the same places malware looks: `.env`, `~/.aws`, your shell history, your agent's caches. Sixty seconds, and you are looking at the full list, file and line. Then lock them away.

```
# install jit (macOS · Apple Silicon)
$ brew install jitpass/tap/jitpass
```

free for personal & internal company use· no account· no telemetry· every change reversible

# ethanplusai/jarvis

## 导航

- 项目页：[[10-项目/jitpass.com_bab90b05]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
