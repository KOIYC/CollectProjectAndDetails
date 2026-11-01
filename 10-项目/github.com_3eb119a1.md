---
type: "project"
title: "Show HN: Mullvad as a rotating connect proxy"
project_url: "https://github.com/nicorobinreal/molehill"
first_seen: "2026-11-01T09:38:09+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_albinstman
  - story_50315686
  - show_hn
lang: "en"
---

# Show HN: Mullvad as a rotating connect proxy

> [!info] 一句话导读
> nicorobinreal/molehill

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/nicorobinreal/molehill>
> 首次收录：2026-11-01T09:38:09+08:00
> 来源渠道：HN Show HN
> 标签：author_albinstman, story_50315686, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:38:09+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-01/4ea0cde3b6c76ffd_Show-HN-Mullvad-as-a-rotating-connect-proxy]] |

## 摘要正文

# nicorobinreal/molehill  Mullvad as a rotating HTTP CONNECT proxy with sticky sessions and country support.  - Stars: 3 - Forks: 0 - Watchers: 3 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-10-31T00:47:54Z  ## Languages  - Dockerfile - Go  ## Top Contributors  - nicorobinreal (4 contributions)  ---  ## README  # molehill  Mullvad as a rotating connect proxy with sticky sessions and country support.  ## Usage  1. Register a WireGuard key on your Mullvad account (needs `wg`, `curl`, `jq`):     ```sh    ACCOUNT=<your account number> && KEY=$(wg genkey) && \    TOKEN=$(curl -s -X POST https://api.mullvad.net/auth/v1/token -H 'Content-Type: application/json' \      -d "{\"account_number\":\"$ACCOUNT\"}" | jq -r .access_token) && \    IPV4=$(curl -s -X POST https://api.mullvad.net/accounts/v1/devices -H "Authorization: Bearer $TOKEN" \      -H 'Content-Type: application/json' -d "{\"pubkey\":\"$(echo "$KEY" | wg pubkey)\",\"hijack_dns\":false}" \      | jq -r .ipv4_address)    ```  2. Build and run the image:     ```sh    docker build -t molehill https://github.com/nicorobinreal/molehill.git#v0.1.0 && \    docker run -d --name molehill --cap-add NET_ADM…
