---
type: "project"
title: "Show HN: (alter)native-Linux-builder for Nix on Darwin"
project_url: "https://github.com/quinneden/alternative-linux-builder"
first_seen: "2026-09-20T09:37:07+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_qeden
  - story_49721253
  - show_hn
lang: "en"
---

# Show HN: (alter)native-Linux-builder for Nix on Darwin

> [!info] 一句话导读
> quinneden/alternative-linux-builder

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/quinneden/alternative-linux-builder>
> 首次收录：2026-09-20T09:37:07+08:00
> 来源渠道：HN Show HN
> 标签：author_qeden, story_49721253, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/887603ba496ea2d6_Show-HN-(alter)native-Linux-builder-for-Nix-on-Dar]] |
| 2026-09-20T09:37:07+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-20/887603ba496ea2d6_Show-HN-(alter)native-Linux-builder-for-Nix-on-Dar]] |

## 摘要正文

# quinneden/alternative-linux-builder  (alter)native-linux-builder for nix-darwin with upstream nix (no determinate-nixd).  - Stars: 2 - Forks: 0 - Watchers: 2 - Open issues: 0 - Default branch: main - Created: 2026-09-12T23:36:57Z  ## Languages  - Nix - Shell - Swift  ## Top Contributors  - quinneden (3 contributions)  ---  ## README  # (alter)native-linux-builder  A swift-based binary that can be used as an external builder for nix (via `external-builders` experimental feature) to build linux packages on darwin without having to setup a full remote build VM. This project aims to reproduce the functionality of Determinate Nix's native-linux-builder for upstream Nix installs. It also provides a Nix-darwin module to configure the external builder.  ## Setup  If you manage your system with Nix-darwin, import the module exposed by the flake into your configuration and enable the option:  ```nix { inputs, ... }:  imports = [ inputs.alternative-linux-builder.darwinModules.default ];  programs.alternative-linux-builder = {   enable = true; }; ```  If you don't use Nix-darwin, you can install the package via profiles:  ```sh nix profile add github:quinneden/alternative-linux-builder ```  …
