---
type: "corpus"
item_id: "4ea0cde3b6c76ffd"
title: "Show HN: Mullvad as a rotating connect proxy"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50315686"
project_url: "https://github.com/nicorobinreal/molehill"
author: "albinstman"
published_at: "2026-10-31T12:45:55Z"
captured_at: "2026-11-01T09:38:09+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-01"
pub_day: "2026-10-31"
tags:
  - 语料
  - hn_show
  - author_albinstman
  - story_50315686
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Mullvad as a rotating connect proxy

> [!info] 一句话导读
> nicorobinreal/molehill

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50315686>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：albinstman　|　发布：2026-10-31T12:45:55Z
> 项目链接：<https://github.com/nicorobinreal/molehill>
> 采集：2026-11-01T09:38:09+08:00　|　id：`4ea0cde3b6c76ffd`

## 正文

# nicorobinreal/molehill

Mullvad as a rotating HTTP CONNECT proxy with sticky sessions and country support.

- Stars: 3
- Forks: 0
- Watchers: 3
- Open issues: 0
- License: MIT License
- Default branch: main
- Created: 2026-10-31T00:47:54Z

## Languages

- Dockerfile
- Go

## Top Contributors

- nicorobinreal (4 contributions)

---

## README

# molehill

Mullvad as a rotating connect proxy with sticky sessions and country support.

## Usage

1. Register a WireGuard key on your Mullvad account (needs `wg`, `curl`, `jq`):

   ```sh
   ACCOUNT=<your account number> && KEY=$(wg genkey) && \
   TOKEN=$(curl -s -X POST https://api.mullvad.net/auth/v1/token -H 'Content-Type: application/json' \
     -d "{\"account_number\":\"$ACCOUNT\"}" | jq -r .access_token) && \
   IPV4=$(curl -s -X POST https://api.mullvad.net/accounts/v1/devices -H "Authorization: Bearer $TOKEN" \
     -H 'Content-Type: application/json' -d "{\"pubkey\":\"$(echo "$KEY" | wg pubkey)\",\"hijack_dns\":false}" \
     | jq -r .ipv4_address)
   ```

2. Build and run the image:

   ```sh
   docker build -t molehill https://github.com/nicorobinreal/molehill.git#v0.1.0 && \
   docker run -d --name molehill --cap-add NET_ADMIN --sysctl net.ipv4.conf.all.src_valid_mark=1 \
     -p 127.0.0.1:8080:8080 -p 127.0.0.1:8081:8081 \
     -e MULLVAD_DEVICES="[{\"id\":\"d1\",\"private_key\":\"$KEY\",\"ipv4\":\"$IPV4\"}]" molehill
   ```

3. Send a request through a session named `s1` exiting in the US:

   ```sh
   curl -x 'http://session-s1-cc-us:x@localhost:8080' https://am.i.mullvad.net/json
   ```

The full reference (username format, configuration, response codes,
behavior, management API) is in docs.md.

## License

MIT

Error fetching https://github.com/samamatariq3527/Deferred-Cognitive-Architecture: CRAWL_LIVECRAWL_TIMEOUT

## 关联链接

- http://session-s1-cc-us:x@localhost:8080
- https://am.i.mullvad.net/json
- https://api.mullvad.net/accounts/v1/devices
- https://api.mullvad.net/auth/v1/token
- https://github.com/nicorobinreal/molehill.git#v0.1.0
- https://github.com/samamatariq3527/Deferred-Cognitive-Architecture:

## 导航

- 项目页：[[10-项目/github.com_3eb119a1]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
