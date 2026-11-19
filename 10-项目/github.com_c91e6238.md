---
type: "project"
title: "Show HN: HimitsuShell – Shell scripts that evade kernel tracing"
project_url: "https://github.com/HimitsuShell/HimitsuShell"
first_seen: "2026-11-19T09:43:31+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mushstory
  - story_50551093
  - show_hn
lang: "en"
---

# Show HN: HimitsuShell – Shell scripts that evade kernel tracing

> [!info] 一句话导读
> HimitsuShell/HimitsuShell

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/HimitsuShell/HimitsuShell>
> 首次收录：2026-11-19T09:43:31+08:00
> 来源渠道：HN Show HN
> 标签：author_mushstory, story_50551093, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:43:31+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-19/c1da20f639693cfd_Show-HN-HimitsuShell-–-Shell-scripts-that-evade-ke]] |

## 摘要正文

# HimitsuShell/HimitsuShell  shell script protector (obfuscation, embedded interpreter, anti-tamper, DRM) - linux, IoT  - Stars: 9 - Forks: 3 - Watchers: 9 - Open issues: 0 - License: Other - Homepage: https://himitsushell.com/ - Default branch: main - Created: 2026-02-28T12:35:14Z  ## Languages  - Shell  ## Topics  - bash - compiler - drm - embedded-linux - encryption - iot - llvm - musl - obfuscator - protection - shc - shell - shell-script  ## Top Contributors  - MushStory (25 contributions)  ---  ## README  **README:** English | 中文 | 日本語  # HimitsuShell Protects shell scripts from leaks, tampering, and unauthorized use.  Converts shell scripts into static binaries with an embedded interpreter, obfuscation, and anti-debug protections (shc alternative).   Block Flow Graph (Ghidra)  ## Usage ```shell # 1. download and load docker image curl -LO https://github.com/HimitsuShell/Himitsu/releases/download/v1.2.0/himitsu_core_v1.2.0.tar.gz docker load -i himitsu_core_v1.2.0.tar.gz  # 2. start container docker run --name himitsu_core -d -it himitsu_core:v1.2.0  # 3. upload your shell script (must be named launcher.sh) docker cp launcher.sh himitsu_core:/var/work/  # 4. build and downloa…
