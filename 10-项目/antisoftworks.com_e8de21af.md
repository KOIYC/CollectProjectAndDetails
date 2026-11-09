---
type: "project"
title: "Show HN: Search Everywhere at Once. Instantly"
project_url: "https://antisoftworks.com/antifind"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_civnode
  - story_50415469
  - show_hn
lang: "en"
---

# Show HN: Search Everywhere at Once. Instantly

> [!info] 一句话导读
> I've made AntiFind, to allow you to search everywhere at once, vastly increasing the efficiency of LLMs and your own searches:AntiFind indexes filesystems, not …

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://antisoftworks.com/antifind>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_civnode, story_50415469, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/91be42d82bb60a3b_Show-HN-Search-Everywhere-at-Once.-Instantly]] |

## 摘要正文

I've made AntiFind, to allow you to search everywhere at once, vastly increasing the efficiency of LLMs and your own searches:AntiFind indexes filesystems, not folders.It maintains a live view of storage by reading filesystem metadata directly. Because it understands the underlying filesystems, it can search across storage that the operating system is not currently exposing, including unmounted partitions.Allowing you to search for and play media from Linux in your Windows and the other way around. Without mounting the drives.This works on Linux, Windows and MacOS.The underlying idea is simple: instead of walking directories, read the filesystem's file tables directly.Most tools discover the filesystem again every time you search. AntiFind reads the drive's metadata in one pass and then follows changes as they happen.AntiFind supports Windows, Linux and macOS. It includes both a GUI and a command line. The CLI supports JSON output (--json) and was designed to integrate cleanly with automation and LLM workflows.There's a lot more to it, and you can find timings on my site, but that's the core idea.More information: https://antisoftworks.com/antifindCheers!
