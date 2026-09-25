---
type: "corpus"
item_id: "a6a3137edc56e160"
title: "Show HN: Headwire – WireGuard with NAT traversal via Tailscale's magicsock"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49834349"
project_url: "https://github.com/brofranks/headwire"
author: "brof"
published_at: "2026-09-24T17:51:40Z"
captured_at: "2026-09-25T13:42:25+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-25"
pub_day: "2026-09-24"
tags:
  - 语料
  - hn_show
  - author_brof
  - story_49834349
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Headwire – WireGuard with NAT traversal via Tailscale's magicsock

> [!info] 一句话导读
> WireGuard meshes with NAT traversal and DERP relay fallback.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49834349>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：brof　|　发布：2026-09-24T17:51:40Z
> 项目链接：<https://github.com/brofranks/headwire>
> 采集：2026-09-25T13:42:25+08:00　|　id：`a6a3137edc56e160`

## 正文

# brofranks/headwire

WireGuard meshes with NAT traversal and DERP relay fallback.

- Stars: 0
- Forks: 1
- Watchers: 0
- Open issues: 1
- License: BSD 3-Clause "New" or "Revised" License
- Default branch: main
- Created: 2026-09-24T05:26:31Z

## Languages

- C
- Go
- Shell

## Top Contributors

- brofranks (1 contributions)

---

## README

 Headwire

Headwire statically configures WireGuard peers with support for NAT traversal
using DERP relays. It is experimental.

Initial connections will happen over DERP, then upgrade to a direct path if
one is found:

```text
$ headwire ping 100.64.0.2
pong from 100.64.0.2 via relay:1 in 122ms
pong from 100.64.0.2 via relay:1 in 118ms
pong from 100.64.0.2 via 203.0.113.10:41198 in 1ms
```

Headwire is built using Tailscale's open-source data plane libraries.

## Features

- establish direct connections where possible
- fall back to relayed connections
- continue using ordinary WireGuard peers
- a macOS app

## Configuration Example

Run your own
DERP servers. Tailscale runs "free rate-limited DERP relays" for
Tailcat, see its DERP map.

```ini
[DERPRegion]
ID = 1
Nodes = derp1.example.com, derp2.example.com

[Interface]
PrivateKey = <base64 private key from headwire genkey>
Address = 100.64.0.1/32
HomeDERP = 1

[Peer]
PublicKey = <peer base64 public key>
DiscoKey = <peer base64 disco key>
AllowedIPs = 100.64.0.2/32, 10.20.0.0/16
HomeDERP = 1
```

- Every peer has a WireGuard `PublicKey`.
- Ordinary WireGuard peers use a fixed `Endpoint`.
- Headwire peers have a `DiscoKey` and `HomeDERP` region.
- See the more complete example.

## Usage

Install a release from the
project releases page, then
create a configuration:

```sh
sudo install -d -o root -g "$(id -g root)" -m 755 /etc/headwire
sudo install -o root -g "$(id -g root)" -m 600 /dev/null /etc/headwire/main.conf
sudoedit /etc/headwire/main.conf
sudo headwire check
```

Run Headwire:

```sh
sudo headwire run
```

Or as a service:

```sh
sudo systemctl enable --now headwire
sudo systemctl status headwire
```

## CLI Reference

```text
usage: headwire <command>

Commands:
  show [FIELD]           status of the running node, --help lists fields
  ip [-1|-4|-6]          local addresses of the running node
  ping IP                disco-ping up to 10 times, stopping at a direct response
  check [NAME | FILE]    validate the configuration (default: main)
  genkey                 print a new private key
  pubkey                 read a private key on stdin, print its WireGuard public key
  discokey               read a private key on stdin, print its discovery public key
  genpsk                 print a new preshared key
  netcheck [NAME | FILE] probe connectivity to configured relay regions
  version                print the build version
  run [NAME | FILE]      run the node on a TUN interface (root, default: main)

NAME selects /etc/headwire/NAME.conf, any other argument is a file.
Use help COMMAND or COMMAND --help for command-specific help.
```

## Configuration Reference

| Section | Key | Meaning |
| --- | --- | --- |
| `[Interface]` | `PrivateKey` | required |
| | `Address` * | required, one or more IPv4 or IPv6 addresses |
| | `ListenPort` | UDP port number, `0` or omitted picks a random one |
| | `MTU` | defaults to 1280 |
| | `DNS` * | addresses are nameservers, other entries search domains |
| | `HomeDERP` | this node's relay region |
| | `AllowIn` * | default inbound policy for peers that set none |
| `[Peer]` | `PublicKey` | required |
| | `DiscoKey` | makes this a discovery peer |
| | `AllowedIPs` * | valid routes and sources, overlaps go to the longest prefix |
| | `PresharedKey` | optional |
| | `Endpoint` | fixed `host:port`, a static candidate for a discovery peer |
| | `HomeDERP` | relay region the peer is reached through |
| | `MasqueradeAddress` * | source address for packets sent to this peer |
| | `AllowIn` * | replaces the `[Interface]` policy for this peer |
| `[DERPRegion]` | `ID` | required, 1-65535 |
| | `Nodes` | required, relay hostnames in preference order |

A key marked `*` may be repeated or given as a comma-separated list.

`AllowIn` is `any`, `none`, or `PROTO[/PORT[-PORT]]`, optionally followed by
`to self|any|IP|CIDR`. `PROTO` is `tcp`, `udp`, `sctp`, `icmp` or a protocol
number, and only the first three take ports. The default is `any`. Examples:

```ini
AllowIn = tcp/22, icmp
AllowIn = udp/5000-5100 to self
```

## Legal

This project is not associated with Tailscale Inc. or WireGuard.

Tailscale is a registered trademark of Tailscale Inc.

WireGuard is a registered trademark of Jason A. Donenfeld.

## 导航

- 项目页：[[10-项目/github.com_7f1376b6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
