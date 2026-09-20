---
type: "project"
title: "Show HN: Quokka – a self-hosting, deterministic programming language"
project_url: "https://quokka.space/"
first_seen: "2026-09-20T14:02:21+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_CFBL
  - story_49755226
  - show_hn
lang: "en"
---

# Show HN: Quokka – a self-hosting, deterministic programming language

> [!info] 一句话导读
> Author: Quokka Language Contributors

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://quokka.space/>
> 首次收录：2026-09-20T14:02:21+08:00
> 来源渠道：HN Show HN
> 标签：author_CFBL, story_49755226, show_hn
> 最新指标：点赞=5 · 评论=2 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:23:24+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/03c09d47cfd86c0c_Show-HN-Quokka-–-a-self-hosting,-deterministic-pro]] |
| 2026-09-20T09:36:39+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/03c09d47cfd86c0c_Show-HN-Quokka-–-a-self-hosting,-deterministic-pro]] |
| 2026-09-20T14:02:21+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-20/03c09d47cfd86c0c_Show-HN-Quokka-–-a-self-hosting,-deterministic-pro]] |

## 摘要正文

Author: Quokka Language Contributors  Quokka — A Deterministic, Self-Hosted Programming Language for AI Workflows  # A predictable language for modern workflows.  v0.1.0 · MIT Licensed · Windows  Quokka is a strictly self-hosted programming language designed for clarity and reliability. It features deterministic programming language design, Result and Option error handling, and seamless LoRA fine-tuning via Unsloth out of the box.  ```shell $ quokka run hello.qka Hello, World! ```  ### Self-hosted by design.  Our entire toolchain is built in Quokka. We use a multi-stage bootstrap process to cryptographically verify correctness.  ```qka // The Quokka compiler is written in Quokka. // Run our built-in check to verify the build. $ quokka check-self ```  ### Predictable errors.  We do not use hidden control flow for exceptions. Handle failures explicitly with Result and Option types.  ```qka let config = fs.read("settings.qka")?  // Errors are returned as values. // No unexpected exceptions thrown at runtime. ```  ### Explicit mutability.  Variables are immutable by default. State changes require explicit opt-in, making your code easier to trace.  ```qka let version = "1.0"      // imm…
