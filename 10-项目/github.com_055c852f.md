---
type: "project"
title: "Show HN: BitBang – Reach machines behind NAT from a browser, no account"
project_url: "https://github.com/richlegrand/bitbang-cli"
first_seen: "2026-09-21T03:11:06+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_narragansett
  - story_49123789
  - show_hn
lang: "en"
---

# Show HN: BitBang – Reach machines behind NAT from a browser, no account

> [!info] 一句话导读
> richlegrand/bitbang-cli

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/richlegrand/bitbang-cli>
> 首次收录：2026-09-21T03:11:06+08:00
> 来源渠道：HN Show HN
> 标签：author_narragansett, story_49123789, show_hn
> 最新指标：点赞=97 · 评论=39 · engagement_velocity=97

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:31:46+08:00 | HN Show HN | 点赞=97 · 评论=39 · engagement_velocity=97 | [[20-语料/posts/hn_show/2026-09-21/71a256a6eb591e5b_Show-HN-BitBang-–-Reach-machines-behind-NAT-from-a]] |
| 2026-09-21T02:55:04+08:00 | HN Show HN | 点赞=97 · 评论=39 · engagement_velocity=97 | [[20-语料/posts/hn_show/2026-09-21/71a256a6eb591e5b_Show-HN-BitBang-–-Reach-machines-behind-NAT-from-a]] |
| 2026-09-21T03:11:06+08:00 | HN Show HN | 点赞=97 · 评论=39 · engagement_velocity=97 | [[20-语料/posts/hn_show/2026-09-21/71a256a6eb591e5b_Show-HN-BitBang-–-Reach-machines-behind-NAT-from-a]] |

## 摘要正文

# richlegrand/bitbang-cli  Proxy server that uses BitBang  - Stars: 5 - Forks: 1 - Watchers: 5 - Open issues: 4 - License: MIT License - Default branch: main - Created: 2026-04-23T02:19:30Z  ## Languages  - Go - HTML - JavaScript - Python - Shell  ## Top Contributors  - richlegrand (63 contributions)  ---  ## README  # BitBang CLI  BitBang CLI is a single static binary remote-access multitool: open an interactive shell, browse and transfer files, and access web apps on the remote machine's network from any browser, no port forwarding, no configuring, and no account.  Tests License  Install bitbang, run bitbang serve, and open the printed URL in a browser to get a shell, a file browser, and a proxy to the machine's network  On the machine you want to reach:  ``` curl -sSfL bitba.ng/install | sh bitbang serve ```  `serve` prints a URL. Open it in any browser and you get a terminal, a file browser, and a proxy to that machine's network -- or connect from another terminal with `bitbang connect ` using the same binary. The connection is end-to-end encrypted and peer-to-peer; the `bitba.ng` server introduces the two ends, then steps aside.  `bitbang` is a single static Go binary. It's pa…
