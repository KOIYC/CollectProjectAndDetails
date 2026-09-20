---
type: "corpus"
item_id: "3135ace5a6aef7a1"
title: "Show HN: AI command review drill for engineers and vibe coders"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=48340994"
project_url: "https://proreview.dev/"
author: "shaad1337"
published_at: "2026-05-30T21:56:47Z"
captured_at: "2026-09-21T02:52:50+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-05-30"
tags:
  - 语料
  - hn_show
  - author_shaad1337
  - story_48340994
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:144d"
---

# Show HN: AI command review drill for engineers and vibe coders

> [!info] 一句话导读
> ProReview How it works Features Tracks Start reviewing

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=48340994>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：shaad1337　|　发布：2026-05-30T21:56:47Z
> 项目链接：<https://proreview.dev/>
> 采集：2026-09-21T02:52:50+08:00　|　id：`3135ace5a6aef7a1`

## 正文

ProReview How it works Features Tracks Start reviewing
ProReview Training engineering teams to spot AI risks before they reach production.
Contact ez@proreview.dev © 2026 ProReview
AI command review drill Would you run this AI command ?
 Review AI-generated bash, kubectl, and shell one-liners before they touch production. Make the call, flag the risky segment, and see what you missed.
 Try the 60-second challenge
 Free No login Anonymous
proreview-cli
 bash -c "set -euo pipefail
 MOUNT = /var/lib/postgresql
 DEV =$( python3 -c 'import os, subprocess; src=subprocess.check_output(["findmnt","-n","-o","SOURCE","/var/lib/postgresql"], text=True).strip(); print(os.path.realpath(src))' )
 sudo umount -l "$MOUNT" || true
 sudo wipefs -a "$DEV" && sudo mkfs.ext4 -F "$DEV"
 sudo mount "$DEV" "$MOUNT" " Approve this command?
 Y / N
50 + Challenges
 5 Tracks
 0 AI hints
 <3 min Per review
How it works From prompt to production review
 A focused drill designed around the AI-generated artifacts engineers ship every day.
 01 Pick your tracks
 Choose from Kubernetes, cloud infrastructure, SQL, CI/CD, and backend security surfaces.
02 Judge the output
 Read the AI-generated artifact cold. Decide whether it is safe before seeing any explanation.
03 Flag risky lines
 Select the exact commands, config, SQL, or code segments that would break production.
04 Learn the reveal
 Compare your verdict with the expert answer key and learn the pattern for the next review.
Features Built for engineers who ship
 No fluff. Just the loop you need to sharpen AI code review instincts.
Realistic AI output
 Review generated commands, diffs, configs, migrations, and API code shaped like work engineers actually ship.
Blind judgment
 Commit to safe or unsafe before any hints appear. No LLM hand-holding, spoilers, or answer-first training.
Segment-level scoring
 Select the risky lines, not just the verdict. Get credit for the exact production hazard you caught.
Expert reveals
 Compare your call with a curated breakdown of the failure mode, blast radius, and safer review outcome.
Five danger-zone tracks
 Practice Kubernetes ops, cloud infrastructure, data migrations, CI/CD, and security-sensitive backend code.
Shareable results
 Finish a run with a score and summary you can share after catching what AI almost shipped.
Tracks Five surfaces. Fifty ways to fail.
 Each track covers the exact artifact types that break production.
 TRACK 01 Kubernetes Ops # maintenance.sh
 kubectl get nodes
 kubectl cordon worker-node-03
 kubectl drain worker-node-03 \
 --ignore-daemonsets \
 --force \
 --delete-local-data
 kubectl delete node worker-node-03
 12 challenges HARD
 TRACK 02 Database & SQL # billing-cleanup.sql
 psql -h db.internal \
 -d billing_prod \
 -c 'BEGIN;'
 DELETE FROM invoices
 WHERE status = draft;
 DELETE FROM invoice_items;
 COMMIT;'
 10 challenges MED
 TRACK 03 CI / CD # deploy.yml
- name : Update image
 run : |
 DEPLOY_CMD= "kubectl set image
 deployment/${{ github.event.inputs.service }}
 ..."
 eval $DEPLOY_CMD
 11 challenges HARD
 TRACK 04 Infrastructure # backend.tf
 terraform {
 backend "s3" {
 bucket = "company-terraform-state"
 key = "app/terraform.tfstate"
 region = "us-east-1"
 }
}
 9 challenges MED
 TRACK 05 Python & APIs # exports.py
 @router.get ( "/exports/download" )
 async def download_export(
 filename: str ,
 admin=Depends(require_admin)
):
 file_path = f "/var/exports/{filename}"
 return FileResponse(file_path)
 10 challenges MED
Ready to level up? Your next production incident is already written
 Join engineers who review one challenge a day and catch the bugs before deploy time.
 Start reviewing Browse tracks

## 导航

- 项目页：[[10-项目/proreview.dev_265496cb]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
