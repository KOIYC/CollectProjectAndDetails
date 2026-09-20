---
type: "corpus"
item_id: "32c422459add8313"
title: "Show HN: I tracked 55k free proxies for a week – 1.6% were alive"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49507513"
project_url: "https://github.com/proxmint/free-proxy-list"
author: "satineeee"
published_at: "2026-08-31T09:14:56Z"
captured_at: "2026-09-21T03:11:24+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-21"
pub_day: "2026-08-31"
tags:
  - 语料
  - hn_show
  - author_satineeee
  - story_49507513
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:52d"
---

# Show HN: I tracked 55k free proxies for a week – 1.6% were alive

> [!info] 一句话导读
> proxmint/free-proxy-list

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49507513>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：satineeee　|　发布：2026-08-31T09:14:56Z
> 项目链接：<https://github.com/proxmint/free-proxy-list>
> 采集：2026-09-21T03:11:24+08:00　|　id：`32c422459add8313`

## 正文

# proxmint/free-proxy-list

Free proxy list, re-validated every 30 minutes. HTTP/HTTPS/SOCKS4/SOCKS5, measured anonymity, auto-committed as txt + JSON.

- Stars: 1
- Forks: 0
- Watchers: 1
- Open issues: 0
- License: Creative Commons Attribution 4.0 International
- Homepage: https://proxmint.com/free-proxies#api
- Default branch: main
- Created: 2026-08-05T20:50:42Z

## Topics

- free-proxy
- http-proxy
- proxies
- proxy-checker
- proxy-list
- scraping
- socks4
- socks5
- web-scraping

## Top Contributors

- prian3003 (698 contributions)

---

## README

# Free Proxy List — checked every 30 minutes

**618 live proxies** · 67 countries · updated **2026-08-20 13:26 UTC**

Every proxy in this list is re-tested every 30 minutes by a real HTTP
request *through it* to our own echo endpoint — not pinged, not assumed. Every entry here last passed that test within **5.5 hours** (median 1.5 hours).
Entries that stop answering are dropped, not left to rot. That is the only thing
this repo does differently, and it is the whole point: most public lists are
unvalidated scrapes where the majority of entries are already dead when you
download them.

| | |
|---|---|
| Live now | **618** |
| Countries | 67 |
| Median latency | 2684 ms |
| Re-validated | every 30 minutes |

## Files

| File | Count | Format |
|---|---|---|
| `proxies/all.txt` | 618 | `protocol://ip:port` |
| `proxies/http.txt` | 348 | `ip:port` |
| `proxies/https.txt` | 24 | `ip:port` |
| `proxies/socks4.txt` | 128 | `ip:port` |
| `proxies/socks5.txt` | 118 | `ip:port` |
| `proxies/elite.txt` | 313 | `protocol://ip:port`, no leak found |
| `proxies/all.json` | 618 | country, anonymity, latency, uptime, score |

Top countries: United States (75) · Russia (50) · Indonesia (45) · China (38) · Germany (24) · India (23) · Singapore (22) · France (21) · Brazil (19) · Colombia (18)

## Use it

```bash
curl -s https://raw.githubusercontent.com/proxmint/free-proxy-list/main/proxies/socks5.txt
```

Live JSON/text API, same data, with filters (country, protocol) and sorting:

```bash
curl 'https://proxmint.com/api/free-proxies?protocol=socks5&format=txt'
```

No key, no signup, 60 req/min. Docs:

## Where these come from

**We are not the origin of these proxies and do not claim to be.** Candidates are
pulled from the public lists below — all of which are doing the hard part — and
then independently validated by us. Counts are how many of *this* repo's current
live entries each source contributed. Go star them:

| Source | Live entries now |
|---|---|
| monosans/proxy-list | 178 |
| proxylist.geonode.com | 29 |
| TheSpeedX/PROXY-List | 168 |
| proxifly/free-proxy-list | 243 |

## Fields in `all.json`

| Field | Meaning |
|---|---|
| `uptimePct` | share of our checks this proxy has passed (EWMA, 0–100) |
| `latencyMs` | round trip through the proxy on its last successful check |
| `score` | reliability rank combining uptime, latency and recency |
| `anonymity` | `elite` — added nothing a direct request wouldn't · `anonymous` — announces itself as a proxy · `transparent` — leaked the caller's IP · empty — not measurable, see below |

### How anonymity is measured

We fetch our own echo endpoint through the proxy and diff the forwarding headers
it arrives with against the headers a *direct* request arrives with. Whatever the
proxy added is the rating. The source list's own claim is never trusted, and the
baseline is measured on every run rather than hardcoded.

**Where the field is empty, and why.** Our echo is served over https, and an http
proxy carrying an https request opens a CONNECT tunnel: it relays encrypted bytes
it cannot read, so it has no opportunity to add `Via` or `X-Forwarded-For` even
if it normally would. A blank result there is the transport telling us nothing,
so we publish nothing rather than upgrade silence to `elite`. SOCKS proxies are
rated because SOCKS is a layer-4 byte relay with no headers to add in the first
place.

**One further limit, stated plainly:** our echo sits behind a CDN that overwrites
inbound `X-Forwarded-For`, so a proxy that leaks your IP *only* through that
header, and sets no `Via` or `Forwarded`, is rated `elite` here. Read `elite`
as **"we found no leak"**, not "there is none".

## Warning

These are free public proxies run by strangers. They are slow, short-lived, and
some are honeypots that log or tamper with traffic. Use them for testing and
research. **Never send logged-in or sensitive traffic through one.** We verify
that a proxy forwards traffic — nothing more. We do not operate, audit, or
endorse any of them.

Needing proxies that stay up is a different problem, and the one Proxmint sells.

## Licence

Published under CC BY 4.0 — see `LICENSE`. Use this
list for anything, including commercially: republish it, ship it inside a product,
train on it. The one condition is credit — name Proxmint and link back to
. Nothing here is warranted; see the warning above.

The proxies themselves are public infrastructure we did not create and do not own.
What is licensed is this compilation: the selection, the validation results, and the
measured fields attached to each row.

---

*Regenerated automatically every 30 minutes by Proxmint.*

## 评论（1/1）

> **jdndnsd** · 2026-08-31T15:48:50.000Z　
> AI slop

## 关联链接

- https://proxmint.com/api/free-proxies?protocol=socks5&format=txt
- https://proxmint.com/free-proxies#api
- https://raw.githubusercontent.com/proxmint/free-proxy-list/main/proxies/socks5.txt

## 导航

- 项目页：[[10-项目/github.com_63db98e4]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
