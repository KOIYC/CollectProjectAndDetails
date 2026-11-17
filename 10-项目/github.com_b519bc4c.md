---
type: "project"
title: "Show HN: Free weekly backups for Supabase Free projects (pg_dump to R2)"
project_url: "https://github.com/liulewis/supabase-free-backup-lite"
first_seen: "2026-11-17T11:09:12+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_agricalc
  - story_50526110
  - show_hn
lang: "en"
---

# Show HN: Free weekly backups for Supabase Free projects (pg_dump to R2)

> [!info] 一句话导读
> liulewis/supabase-free-backup-lite

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/liulewis/supabase-free-backup-lite>
> 首次收录：2026-11-17T11:09:12+08:00
> 来源渠道：HN Show HN
> 标签：author_agricalc, story_50526110, show_hn
> 最新指标：点赞=6 · 评论=0 · engagement_velocity=6

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-17T11:09:12+08:00 | HN Show HN | 点赞=6 · 评论=0 · engagement_velocity=6 | [[20-语料/posts/hn_show/2026-11-17/ae8552a7af630f2b_Show-HN-Free-weekly-backups-for-Supabase-Free-proj]] |

## 摘要正文

# liulewis/supabase-free-backup-lite  Free weekly backup for a Supabase Free-tier database: pg_dump to Cloudflare R2 via GitHub Actions. Lite version of the Supabase Backup Kit.  - Stars: 0 - Forks: 0 - Watchers: 0 - Open issues: 0 - Default branch: main - Created: 2026-11-13T04:01:28Z  ## Languages  - Shell  ## Top Contributors  - liulewis (4 contributions)  ---  ## README  # Backup Supabase Free Tier — Free Lite Version  A free, minimal weekly backup for a Supabase Free-tier database. `pg_dump` → Cloudflare R2. Nothing else. No encryption, no restore drill, no alerts, no validation.  **Why this exists:** Supabase Free has no automated backups. Pro is $25/month. This 30-line workflow is the smallest thing that actually protects your data — and if it ever saves you once, the full kit (encryption + restore drill + pre-flight checks + watchdog) is $29 launch / $39 standard.  ## Setup (10 minutes)  1. **Use a PRIVATE repo.** GitHub disables scheduled workflows in public  repos after 60 days without activity, silently. 2. **Create an R2 bucket** + API token (Object Read/Write on that bucket). 3. **Copy the Session pooler string** from Supabase Dashboard → Settings →  Database → Connect…
