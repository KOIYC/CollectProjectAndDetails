---
type: "project"
title: "Show HN: go-iroh – iroh compatible networking for Go"
project_url: "https://github.com/tmc/go-iroh"
first_seen: "2026-09-21T03:11:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_traviscline
  - story_48725005
  - show_hn
lang: "en"
---

# Show HN: go-iroh – iroh compatible networking for Go

> [!info] 一句话导读
> iroh networking for go

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/tmc/go-iroh>
> 首次收录：2026-09-21T03:11:03+08:00
> 来源渠道：HN Show HN
> 标签：author_traviscline, story_48725005, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/68d4c791573f7727_Show-HN-go-iroh-–-iroh-compatible-networking-for-G]] |
| 2026-09-21T03:11:03+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-09-21/68d4c791573f7727_Show-HN-go-iroh-–-iroh-compatible-networking-for-G]] |

## 摘要正文

# tmc/go-iroh  iroh networking for go  - Stars: 6 - Forks: 1 - Watchers: 6 - Open issues: 0 - License: MIT License - Default branch: main - Created: 2026-06-02T00:33:23Z  ## Languages  - Go - Rust - Shell  ## Top Contributors  - tmc (249 contributions)  ---  ## README  # go-iroh  `go-iroh` is a Go implementation of the iroh connectivity layer. It provides peer-to-peer QUIC endpoints identified by ed25519 public keys, with direct paths, relay fallback, QUIC Retry, multipath, QAD observed addresses, and QNT NAT traversal support.  The module is a clean-room Go port targeting wire compatibility with upstream Rust iroh. It is not affiliated with the n0 team.  ## Packages  | Package | Purpose | |---|---| | `key` | endpoint IDs, Ed25519 keys, signatures | | `netaddr` | endpoint addresses, transport addresses, relay URLs | | `dns` | pkarr TXT encoding and stdlib/DoH/DoT lookupers | | `relay` | public relay maps and relay configuration | | `watch` | small generic watch values | | `iroh` | Endpoint, Conn, Router, address lookup, metrics | | `cmd/iroh-relay` | minimal local relay server | | `cmd/iroh-dns-server` | minimal pkarr HTTP server |  The transport internals live under `internal/`: r…
