---
type: "project"
title: "I Vibe-Coded My Way Out of Angular Upgrades"
project_url: "https://angular.dev/update-guide"
first_seen: "2026-10-28T00:18:18+08:00"
sources:
  - devto
tags:
  - 项目
  - devto
  - ai
  - vibecoding
  - angular
  - showdev
lang: "en"
---

# I Vibe-Coded My Way Out of Angular Upgrades

> [!info] 一句话导读
> Do you also hate upgrading Angular versions? Because I do. I maintain a few open-source projects, and upgrading Angular is probably my least favorite maintenanc…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://angular.dev/update-guide>
> 首次收录：2026-10-28T00:18:18+08:00
> 来源渠道：dev.to
> 标签：ai, vibecoding, angular, showdev
> 最新指标：reactions=90 · 评论=64 · reading_time=3

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:48:59+08:00 | dev.to | reactions=90 · 评论=64 · reading_time=3 | [[20-语料/posts/devto/2026-10-22/8237951271bb0076_I-Vibe-Coded-My-Way-Out-of-Angular-Upgrades]] |
| 2026-10-22T09:57:25+08:00 | dev.to | reactions=90 · 评论=64 · reading_time=3 | [[20-语料/posts/devto/2026-10-22/8237951271bb0076_I-Vibe-Coded-My-Way-Out-of-Angular-Upgrades]] |
| 2026-10-25T23:48:07+08:00 | dev.to | reactions=90 · 评论=64 · reading_time=3 | [[20-语料/posts/devto/2026-10-22/8237951271bb0076_I-Vibe-Coded-My-Way-Out-of-Angular-Upgrades]] |
| 2026-10-26T00:38:45+08:00 | dev.to | reactions=90 · 评论=64 · reading_time=3 | [[20-语料/posts/devto/2026-10-22/8237951271bb0076_I-Vibe-Coded-My-Way-Out-of-Angular-Upgrades]] |
| 2026-10-26T09:53:38+08:00 | dev.to | reactions=90 · 评论=64 · reading_time=3 | [[20-语料/posts/devto/2026-10-22/8237951271bb0076_I-Vibe-Coded-My-Way-Out-of-Angular-Upgrades]] |
| 2026-10-28T00:18:18+08:00 | dev.to | reactions=90 · 评论=64 · reading_time=3 | [[20-语料/posts/devto/2026-10-22/8237951271bb0076_I-Vibe-Coded-My-Way-Out-of-Angular-Upgrades]] |

## 摘要正文

Do you also hate upgrading Angular versions? Because I do. I maintain a few open-source projects, and upgrading Angular is probably my least favorite maintenance task. That's also why my frontend updates often get postponed for far too long.  But we have AI now, right? It should be able to handle this with some instructions. So I decided to create (or rather vibe-code) an **Angular Update Skill for Codex**.  ## Creating the skill  Upgrading Angular isn't just about running `ng update`. There are several things I normally have to take care of, so I created a prompt describing what the skill should do:  - Follow the official [Angular Update Guide](https://angular.dev/update-guide). - Create a separate Git branch for the upgrade. - Handle migrations and dependency updates. - Validate that everything still builds and works. - Follow the same good practices I would use when upgrading Angular manually.  (Updating NuGet packages in .NET feels so much simpler.)  Codex generated the first version of the skill, and surprisingly, it worked!  Well... locally.  ### First problem: npm ci  After pushing my changes to GitHub, the CI pipeline failed with:  ```plaintext npm ci can only install packa…
