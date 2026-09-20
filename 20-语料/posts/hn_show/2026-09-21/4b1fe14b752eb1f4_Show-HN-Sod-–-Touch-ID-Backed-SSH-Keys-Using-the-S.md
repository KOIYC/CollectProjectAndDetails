---
type: "corpus"
item_id: "4b1fe14b752eb1f4"
title: "Show HN: Sod – Touch ID-Backed SSH Keys Using the Secure Enclave"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48731704"
project_url: "https://botanica-consulting.github.io/sod"
author: "botanica_labs"
published_at: "2026-06-30T12:22:50Z"
captured_at: "2026-09-21T02:53:08+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-06-30"
tags:
  - 语料
  - hn_show
  - author_botanica_labs
  - story_48731704
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:113d"
---

# Show HN: Sod – Touch ID-Backed SSH Keys Using the Secure Enclave

> [!info] 一句话导读
> sod — SSH keys sealed in the Secure Enclave

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48731704>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：botanica_labs　|　发布：2026-06-30T12:22:50Z
> 项目链接：<https://botanica-consulting.github.io/sod>
> 采集：2026-09-21T02:53:08+08:00　|　id：`4b1fe14b752eb1f4`

## 正文

sod — SSH keys sealed in the Secure Enclave

sod

➜ alon git:(main) ✗ sd install

The sod agent is running and will start at every login (serving id_sod).

Point your shell at it:

 echo 'export SSH_AUTH_SOCK="$HOME/.ssh/sod-agent.sock"' >> ~/.zshrc

 exec $SHELL

➜ alon git:(main) ✗ echo 'export SSH_AUTH_SOCK="$HOME/.ssh/sod-agent.sock"' >> ~/.zshrc

➜ alon git:(main) ✗ exec $SHELL

➜ alon git:(main) ✗ ssh -T git@github.com

## 导航

- 项目页：[[10-项目/botanica-consulting.github.io_16e202f0]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
