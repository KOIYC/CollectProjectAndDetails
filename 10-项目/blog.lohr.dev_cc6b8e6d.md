---
type: "project"
title: "Show HN: Shrinking my 159-byte x86-64 Hello World ELF to 153 bytes"
project_url: "https://blog.lohr.dev/hello-world-contd"
first_seen: "2026-10-25T23:24:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_michidk
  - story_50230693
  - show_hn
lang: "en"
---

# Show HN: Shrinking my 159-byte x86-64 Hello World ELF to 153 bytes

> [!info] 一句话导读
> Skip to main content Hashnode Michi's Blog

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://blog.lohr.dev/hello-world-contd>
> 首次收录：2026-10-25T23:24:35+08:00
> 来源渠道：HN Show HN
> 标签：author_michidk, story_50230693, show_hn
> 最新指标：点赞=3 · 评论=0 · engagement_velocity=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:24:35+08:00 | HN Show HN | 点赞=3 · 评论=0 · engagement_velocity=3 | [[20-语料/posts/hn_show/2026-10-25/5af0d2b1ea9e5e33_Show-HN-Shrinking-my-159-byte-x86-64-Hello-World-E]] |

## 摘要正文

Skip to main content Hashnode Michi's Blog Back to My Website Back to My Website  Search Ctrl K ⌘K Toggle theme Write Open menu Smallest "Hello World" continued  Updated October 10, 2026 · 13 min read · Markdown M Michael Lohr On this page  Loading the first syscall number directly Loading the message's address directly Loading the message length directly Pushing the syscall number onto the stack Never fail Settling the bill Failing gracefully, for free On to new waters What about Zig? Nearly two years ago, I wrote about the smallest possible "Hello World!" program . It's one of my most read blog posts. Recently, I started playing around a lot with AI (like almost everybody else), so I thought: let's fact-check my previous blog posts! Turns out I was wrong: I actually did not create the smallest possible 'Hello World' program! Buuut, I was pretty close! To summarize the rules of this challenge: runs on modern 64-bit x86 Linux executes directly, without a separate program or decompression step is a proper, specification-compliant executable keeps instructions outside the ELF header and program headers prints Hello, World!\n (14 bytes) to stdout and exits with status 0 My previous re…
