---
type: "corpus"
item_id: "c19bb90ff99d17ca"
title: "Show HN: Shellroute – give each shell its own proxy IP"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49751994"
project_url: "https://github.com/shellroute/shellroute-cli"
author: "civilis"
published_at: "2026-09-18T09:34:02Z"
captured_at: "2026-09-20T14:02:32+08:00"
lang: "en"
kind: "post"
topic: 开发者工具
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_civilis
  - story_49751994
  - show_hn
metrics: {"points": 2, "comments": 3, "engagement_velocity": 2}
comments_count: 3
comments_total: 3
discovered_via: "hn:show_hn:90d"
---

# Show HN: Shellroute – give each shell its own proxy IP

> [!info] 一句话导读
> shellroute/shellroute-cli

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49751994>
> 指标：点赞=2 · 评论=3 · engagement_velocity=2
> 作者：civilis　|　发布：2026-09-18T09:34:02Z
> 项目链接：<https://github.com/shellroute/shellroute-cli>
> 采集：2026-09-20T14:02:32+08:00　|　id：`c19bb90ff99d17ca`

## 正文

# shellroute/shellroute-cli

A proxied shell for terminal workflows. Open a session and run commands through a proxy.

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- License: Apache License 2.0
- Homepage: https://shellroute.com
- Default branch: main
- Created: 2026-06-02T10:58:26Z

## Languages

- Go
- JavaScript
- Makefile
- Shell

## Topics

- automation
- cli
- command-line-tool
- developer-tools
- geo-testing
- http-proxy
- network-debugging
- proxy
- shell
- terminal

## Top Contributors

- cvl (8 contributions)
- dependabot[bot] (3 contributions)

---

## README

# shellroute CLI

License

**Every terminal can be somewhere else.** Open a proxied shell or route one command, then run your terminal workflow normally. Learn more at shellroute.com.

## Install

```bash
npm install -g shellroute
```

Or via Homebrew:

```bash
brew install shellroute/tap/shellroute
```

Or via Go:

```bash
go install github.com/shellroute/shellroute-cli/cmd/shellroute@latest
```

Or download binaries from GitHub Releases.

Supports macOS and Linux.

## Quick start

```bash
# Log in. A new account is created automatically.
shellroute login

# Shellroute opens after login. Run these inside it:
/connect US
curl https://ipinfo.io/json
```

### Or route one command

```bash
shellroute run DE -- curl https://ipinfo.io/json
```

Read the full quickstart.

## Commands

### Authentication

| Command | Description |
|---|---|
| `shellroute login` | Log in with email OTP |
| `shellroute logout` | Remove stored credentials |
| `shellroute reveal-key` | Print stored API key |

### Proxy

| Command | Description |
|---|---|
| `shellroute` | Interactive shell with `/connect`, `/rotate`, `/disconnect` |
| `shellroute run -- ` | Run one command through the proxy |
| `shellroute proxy --country ` | Persistent proxy (blocks until Ctrl+C) |
| `shellroute proxy stop` | Stop running proxy sessions |

#### Local proxy mode

For tools configured with an explicit proxy URL:

```bash
shellroute proxy --country US

# In another terminal
curl -x http://127.0.0.1:41900 https://ipinfo.io/ip
```

### Info

| Command | Description |
|---|---|
| `shellroute status` | Active sessions |
| `shellroute balance` | Credit balance and rates |
| `shellroute countries` | Available countries |
| `shellroute cities ` | Cities in a country |

All info commands support `--format json`.

## Build from source

```bash
git clone https://github.com/shellroute/shellroute-cli.git
cd shellroute-cli
./scripts/rebuild-cli.sh
./shellroute version
```

Run all checks (lint, tests, audit, cross-compile): `./scripts/run-tests.sh`. Requires Go 1.22+.

## How it works

```
Your terminal -> shellroute CLI (local proxy) -> shellroute API -> Gateway -> Exit IP -> Internet
```

Shellroute implements each active route as a local HTTP proxy and provides standard proxy environment variables to the shell or child process. Clients that use those variables send requests through the selected proxy. Each session remains independent, while shellroute manages credentials, rotation, usage, and cleanup.

See what shellroute proxies.

## Important

The shellroute CLI is open source and connects to the shellroute service. The service uses prepaid credits. See pricing and the acceptable use policy.

## Privacy

- Config stored in `~/.shellroute/config.toml` (mode 600)
- API key generated locally, only the hash is sent to the server
- No analytics or telemetry collected
- Health probe sends a CONNECT to `httpbin.org:443` through the proxy to verify upstream connectivity

## Contributing

See CONTRIBUTING.md.

## License

Apache 2.0. See LICENSE.

"shellroute" is a trademark. This license covers the code, not the brand. See NOTICE.

# Atlarix for Chrome — an AI agent in the browser you already use

## 评论（3/3）

> **sshussain270** · 2026-09-18T09:55:03.000Z　
> Curious, what's the advantage of this over ngrok?

---

> **sightspinner** · 2026-09-18T10:41:10.000Z　
> not sure but I'm guessing it's serving a different purpose. I think ngrok is just giving you a single url so that you can whitelist your machine and this is giving you potentially several different ips, I assume for scraping and such.

---

> **vcivilis** · 2026-09-18T10:55:11.000Z　
> Hi. Created new account, as my post author comments get blocked by HN.To answer your question: with ngrok’s tunnels, you make a service you’re running reachable from outside. Shellroute lets you choose a country proxy IP for outgoing requests in each shell or for one command. For example, you could run the same curl request through US and German sessions to compare how a site redirects visitors from each country. Shellroute supplies the proxies, so you don’t need to set up servers in those countries. Think of choosing a VPN location, but for one shell or even command using an HTTP proxy rather than a full VPN.

## 关联链接

- http://127.0.0.1:41900
- https://github.com/shellroute/shellroute-cli.git
- https://ipinfo.io/ip
- https://ipinfo.io/json
- https://shellroute.com

## 导航

- 项目页：[[10-项目/github.com_c56e8576]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
