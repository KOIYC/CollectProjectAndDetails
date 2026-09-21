---
type: "corpus"
item_id: "83aa596bd6571c04"
title: "Spacefree"
source: "indiehackers"
source_name: "Indie Hackers 产品库"
url: "https://www.indiehackers.com/product/spacefree"
captured_at: "2026-09-21T09:47:43+08:00"
lang: "en"
kind: "project"
topic: "AI 工具/Agent"
shard: "2026-09-21"
tags:
  - 语料
  - indiehackers
metrics: {}
comments_count: 0
comments_total: 0
discovered_via: "ih:products"
---

# Spacefree

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+

> [!meta]- 语料信息（点开展开）
> 来源：Indie Hackers 产品库（project）
> 原帖：<https://www.indiehackers.com/product/spacefree>
> 指标：—
> 作者：—　|　发布：—
> 项目链接：—
> 采集：2026-09-21T09:47:43+08:00　|　id：`83aa596bd6571c04`

## 正文

Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+
Starting Up Case Studies
 Ideas DB Products DB Sign in Join
SpaceFree
 Developer Storage debugger for Windows
Visit Website
SpaceFree Developer Storage debugger for Windows
 Post 1
 Revenue $0 / mo
 Website
September 20, 2026
 Where Docker Desktop's disk space goes on Windows, and what is safe to remove
Where Docker keeps its data
 With the WSL 2 backend, Docker's documentation says Docker Desktop stores its data at C:\Users\[USERNAME]\AppData\Local\Docker\wsl by default, and you can change the location in Settings ( Docker Desktop WSL 2 backend ). People on Docker's forum describe a docker_data.vhdx file there that keeps growing ( forum thread ). That is the same kind of virtual disk described in our WSL2 guide .
 See what is using the space
 docker system df shows how much disk space the Docker daemon is using, and the -v flag adds detail ( docker system df ). The example output in the docs has a RECLAIMABLE column showing space that could be freed.
 docker system df docker system df -v
 What docker system prune removes
 By default it removes all stopped containers, all networks not used by at least one container, all dangling images, and unused build cache. Adding -a also removes all unused images, not only dangling ones. Adding --volumes also prunes anonymous volumes. It asks "Are you sure you want to continue? [y/N]" unless you pass -f ( docker system prune ).
 docker system prune docker system prune -a
 Be careful with --volumes. Volumes can hold real data such as a local database. Check what is in a volume before you let anything remove it. Removing images and build cache is low risk because Docker can pull or rebuild them, but it means the next build or pull takes longer.
 Why Windows still shows a big file
 Pruning frees space inside Docker's virtual disk. The file on your Windows drive does not necessarily get smaller. Microsoft's docs note that dynamically expanding virtual disks do not shrink automatically when files are deleted ( compact vdisk ), and there are Docker forum threads from people whose disk file stayed large after cleaning up ( example ).
 To get the space back on Windows you compact the disk file. The steps, including the commands and the warnings, are in Why your WSL2 disk file never shrinks . Quit Docker Desktop before you compact.
 Doing this without the command line
 SpaceFree's WSL and Docker compaction wizard shows how much space is trapped in each virtual disk, so you can decide whether compacting is worth it. Download SpaceFree .
 Sources
 Docker Desktop WSL 2 backend on Windows (Docker Docs)
docker system df (Docker Docs)
docker system prune (Docker Docs)
Docker Desktop WSL2 VHDX grows after every update, no way to reclaim space (Docker Community Forums)
compact vdisk (Microsoft Learn)
bhavikro
1 Like
Comment
About
 I built SpaceFree because my drive kept filling up and I could never tell why. WSL2, Docker, package caches and old builds all hid space, and no tool told me what was safe to delete. So I made one that does.
 People
 bhavikro Founder
Stay informed as an indie hacker.
 Market insights that help you start and grow your business.
Subscribe
Follow @IndieHackers on X for stories and insights about founders building profitable online businesses, and to connect with others in the Indie Hackers community.
 © Indie Hackers, Inc. · FAQ · Terms · Privacy · Cookie Settings / Policy ·
Community
 Top Today Top This Week Top This Month Join
Products
 All Products Highest Revenue Add Yours
Databases
 Ideas Products Stories

## 导航

- 项目页：[[10-项目/Spacefree_83aa596b]]
- 渠道页：[[50-渠道/indiehackers]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
