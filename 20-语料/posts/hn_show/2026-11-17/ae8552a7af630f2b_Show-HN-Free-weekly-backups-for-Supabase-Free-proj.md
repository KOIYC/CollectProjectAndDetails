---
type: "corpus"
item_id: "ae8552a7af630f2b"
title: "Show HN: Free weekly backups for Supabase Free projects (pg_dump to R2)"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50526110"
project_url: "https://github.com/liulewis/supabase-free-backup-lite"
author: "agricalc"
published_at: "2026-11-17T01:13:58Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-17"
tags:
  - 语料
  - hn_show
  - author_agricalc
  - story_50526110
  - show_hn
metrics: {"points": 6, "comments": 0, "engagement_velocity": 6}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Free weekly backups for Supabase Free projects (pg_dump to R2)

> [!info] 一句话导读
> liulewis/supabase-free-backup-lite

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50526110>
> 指标：点赞=6 · 评论=0 · engagement_velocity=6
> 作者：agricalc　|　发布：2026-11-17T01:13:58Z
> 项目链接：<https://github.com/liulewis/supabase-free-backup-lite>
> 采集：2026-11-17T11:09:12+08:00　|　id：`ae8552a7af630f2b`

## 正文

# liulewis/supabase-free-backup-lite

Free weekly backup for a Supabase Free-tier database: pg_dump to Cloudflare R2 via GitHub Actions. Lite version of the Supabase Backup Kit.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- Default branch: main
- Created: 2026-11-13T04:01:28Z

## Languages

- Shell

## Top Contributors

- liulewis (4 contributions)

---

## README

# Backup Supabase Free Tier — Free Lite Version

A free, minimal weekly backup for a Supabase Free-tier database.
`pg_dump` → Cloudflare R2. Nothing else. No encryption, no restore
drill, no alerts, no validation.

**Why this exists:** Supabase Free has no automated backups. Pro is
$25/month. This 30-line workflow is the smallest thing that actually
protects your data — and if it ever saves you once, the full kit
(encryption + restore drill + pre-flight checks + watchdog) is $29
launch / $39 standard.

## Setup (10 minutes)

1. **Use a PRIVATE repo.** GitHub disables scheduled workflows in public
 repos after 60 days without activity, silently.
2. **Create an R2 bucket** + API token (Object Read/Write on that bucket).
3. **Copy the Session pooler string** from Supabase Dashboard → Settings →
 Database → Connection string. Port **5432**, host
 `aws-0-.pooler.supabase.com`. NOT port 6543 (transaction
 pooler — `pg_dump` cannot run through it). NOT the direct host
 `db..supabase.co` (IPv6-only on Free; GitHub runners are
 IPv4-only).
4. **Add repo secrets:** `SUPABASE_DB_URL`, `R2_ACCOUNT_ID`,
 `R2_ACCESS_KEY_ID`, `R2_SECRET_ACCESS_KEY`, `R2_BUCKET`.
5. **Copy this folder's files to your repo root** (or use it as its own
 repo — workflows in a subfolder do not run on their own).
6. **Actions → Supabase Backup (Lite) → Run workflow.** Check R2 for
 `supabase-backups/ /supabase-.dump`.

## Egress warning

Every dump pulls the full database out of Supabase against the Free
**5 GB/month cap**. A 500 MB database dumped weekly is ~2 GB/month
(fine); dumped daily it is ~15 GB/month (over the cap). Keep it weekly.

## Scope

- ✅ Full database, including `auth.users` (they live in the database).
- ❌ Storage files are NOT included — they live in S3, not Postgres.
- ❌ No encryption: the dump is uploaded as-is. R2 buckets are private
 by default, but anyone with your R2 credentials can read it.

## Want the full kit?

The paid Supabase Backup Kit adds: GPG AES-256 encryption, a
pre-flight validator that rejects the wrong pooler with a clear error,
SHA-256 + `pg_restore --list` validation, a restore drill into a
throwaway Postgres with a step-by-step runbook, failure alerts, the
cron-watchdog bonus, and an egress calculator.

# debarshibasak/listodo

## 导航

- 项目页：[[10-项目/github.com_b519bc4c]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
