---
type: "corpus"
item_id: "887603ba496ea2d6"
title: "Show HN: (alter)native-Linux-builder for Nix on Darwin"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49721253"
project_url: "https://github.com/quinneden/alternative-linux-builder"
author: "qeden"
published_at: "2026-09-16T01:55:22Z"
captured_at: "2026-09-20T09:37:07+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-16"
tags:
  - 语料
  - hn_show
  - author_qeden
  - story_49721253
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: (alter)native-Linux-builder for Nix on Darwin

> [!info] 一句话导读
> quinneden/alternative-linux-builder

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49721253>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：qeden　|　发布：2026-09-16T01:55:22Z
> 项目链接：<https://github.com/quinneden/alternative-linux-builder>
> 采集：2026-09-20T09:37:07+08:00　|　id：`887603ba496ea2d6`

## 正文

# quinneden/alternative-linux-builder

(alter)native-linux-builder for nix-darwin with upstream nix (no determinate-nixd).

- Stars: 2
- Forks: 0
- Watchers: 2
- Open issues: 0
- Default branch: main
- Created: 2026-09-12T23:36:57Z

## Languages

- Nix
- Shell
- Swift

## Top Contributors

- quinneden (3 contributions)

---

## README

# (alter)native-linux-builder

A swift-based binary that can be used as an external builder for nix (via `external-builders` experimental feature) to build linux packages on darwin without having to setup a full remote build VM. This project aims to reproduce the functionality of Determinate Nix's native-linux-builder for upstream Nix installs. It also provides a Nix-darwin module to configure the external builder.

## Setup

If you manage your system with Nix-darwin, import the module exposed by the flake into your configuration and enable the option:

```nix
{ inputs, ... }:

imports = [ inputs.alternative-linux-builder.darwinModules.default ];

programs.alternative-linux-builder = {
  enable = true;
};
```

If you don't use Nix-darwin, you can install the package via profiles:

```sh
nix profile add github:quinneden/alternative-linux-builder
```

and configure it directly in `/etc/nix/nix.conf`:

```conf
extra-experimental-features = external-builders

# external-builders takes a list of JSON objects as it's value. Required fields
# are:
#   - program: path to the executable
#   - args: CLI arguments passed to the executable
#   - systems: list of systems this builder can build for
external-builders = [{"program": "/Users/<user>/.nix-profile/bin/alternativeLinuxBuilder", "args": [], "systems": ["aarch64-linux", "x86_64-linux"]}]

# Optionally, you can configure the number of CPU cores and amount of memory in
# the 'args' field via the '-c,--cores' and '-m,--memory' flags, respectively.
# E.g.:
#   external-builders = [{"program": "...", "args": ["-c" "8", "-m", "8192"], ...}]
```

then restart the nix-daemon:

```sh
sudo launchctl kickstart -k system/org.nixos.nix-daemon
```

## Module options

| Option | Type | Default | Description |
| -------- | ------------- | ------------ | -------------------------------------------------- |
| `cores` | _int_ | `1` | Number of CPU cores allocated to the VM. |
| `kernel` | _package_ | `pkgs.linux` | The kernel package to use. |
| `memory` | _null or int_ | `null` | Amount of memory allocated to the VM in mebibytes. |

## 导航

- 项目页：[[10-项目/github.com_ced1a580]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
