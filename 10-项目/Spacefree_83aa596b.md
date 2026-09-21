---
type: "project"
title: "Spacefree"
project_url: "https://www.indiehackers.com/product/spacefree"
first_seen: "2026-09-21T09:47:43+08:00"
sources:
  - indiehackers
tags:
  - 项目
  - indiehackers
lang: "en"
---

# Spacefree

> [!info] 一句话导读
> Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://www.indiehackers.com/product/spacefree>
> 首次收录：2026-09-21T09:47:43+08:00
> 来源渠道：Indie Hackers 产品库
> 标签：—
> 最新指标：—

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:47:43+08:00 | Indie Hackers 产品库 | — | [[20-语料/posts/indiehackers/2026-09-21/83aa596bd6571c04_Spacefree]] |

## 摘要正文

Home Starting Up Case Studies DB Products Ideas DB Subscribe to IH+ Starting Up Case Studies  Ideas DB Products DB Sign in Join SpaceFree  Developer Storage debugger for Windows Visit Website SpaceFree Developer Storage debugger for Windows  Post 1  Revenue $0 / mo  Website September 20, 2026  Where Docker Desktop's disk space goes on Windows, and what is safe to remove Where Docker keeps its data  With the WSL 2 backend, Docker's documentation says Docker Desktop stores its data at C:\Users\[USERNAME]\AppData\Local\Docker\wsl by default, and you can change the location in Settings ( Docker Desktop WSL 2 backend ). People on Docker's forum describe a docker_data.vhdx file there that keeps growing ( forum thread ). That is the same kind of virtual disk described in our WSL2 guide .  See what is using the space  docker system df shows how much disk space the Docker daemon is using, and the -v flag adds detail ( docker system df ). The example output in the docs has a RECLAIMABLE column showing space that could be freed.  docker system df docker system df -v  What docker system prune removes  By default it removes all stopped containers, all networks not used by at least one container…
