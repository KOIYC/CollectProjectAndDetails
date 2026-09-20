---
type: "project"
title: "Show HN: A malicious NPM install reads your .env. On my Mac it reads a decoy"
project_url: "https://jitpass.com/"
first_seen: "2026-09-20T09:37:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_bukershok
  - story_49714094
  - show_hn
lang: "en"
---

# Show HN: A malicious NPM install reads your .env. On my Mac it reads a decoy

> [!info] 一句话导读
> jit · just-in-time passwords for developer endpoints

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://jitpass.com/>
> 首次收录：2026-09-20T09:37:12+08:00
> 来源渠道：HN Show HN
> 标签：author_bukershok, story_49714094, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/e4a98b864d5f9fac_Show-HN-A-malicious-NPM-install-reads-your-.env.-O]] |
| 2026-09-20T09:37:12+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/e4a98b864d5f9fac_Show-HN-A-malicious-NPM-install-reads-your-.env.-O]] |

## 摘要正文

Author: jitpass  jit · just-in-time passwords for developer endpoints  # There is a live API key in plaintext on your Mac.  It sits in `.env`, in `~/.aws/credentials`, in `~/.zsh_history`. One compromised package or one hijacked agent, and it is gone, silently. jit locks the real values away and leaves decoys in your files. Your tools keep working. Whatever gets stolen is worthless.  jit protects your secrets from:  prompt-injected agents compromised npm packages trojanized IDE extensions rogue MCP servers infostealer malware shell-history scrapers stolen backups and dotfiles  ~/acme-checkout  ``` $ jit scan jit scan  ~/ · 4 files · 1ms    YOUR SECRETS: 6 — 0 protected by jit (0%)   ▱▱▱▱▱▱▱▱▱▱  to 100%: one command +100%    jit will protect these — 6 secrets in 4 files, 0% → 100%       → jit migrate         ~/.aws/credentials      acme-prod/aws_secret_access_k…         ~/.zsh_history          GitHub Personal Access Token,                                 AWS Access Key ID         ~/acme-checkout/.env    secret-shaped values         ~/acme-checkout/.npmrc  //registry.npmjs.org/:_authTo…    No secret values are ever printed in full. ```  Real output, on a machine with four ordinary fi…
