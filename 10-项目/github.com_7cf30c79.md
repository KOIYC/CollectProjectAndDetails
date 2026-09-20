---
type: "project"
title: "GusAlberto/hired-flow"
project_url: "https://github.com/GusAlberto/hired-flow"
first_seen: "2026-09-20T09:36:32+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - Blade
  - topic:microsaas
lang: "en"
---

# GusAlberto/hired-flow

> [!info] 一句话导读
> A simple **Kanban-style job application tracker** built with Laravel, Livewire and Docker.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/GusAlberto/hired-flow>
> 首次收录：2026-09-20T09:36:32+08:00
> 来源渠道：GitHub 新星仓库
> 标签：Blade, topic:microsaas
> 最新指标：stars=1 · forks=0 · open_issues=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:24:14+08:00 | GitHub 新星仓库 | stars=1 · forks=0 · open_issues=1 | [[20-语料/posts/github_new/2026-09-20/7cf30c79afd4ff1a_GusAlberto-hired-flow]] |
| 2026-09-20T09:36:32+08:00 | GitHub 新星仓库 | stars=1 · forks=0 · open_issues=1 | [[20-语料/posts/github_new/2026-09-20/7cf30c79afd4ff1a_GusAlberto-hired-flow]] |

## 摘要正文

# HiredFlow  A simple **Kanban-style job application tracker** built with Laravel, Livewire and Docker.  HiredFlow helps developers and job seekers track their job applications, interviews and offers in a simple visual board.  ---  ##  Features  *  Kanban board for tracking job applications *  Track company and position *  Application date tracking *  Drag-and-drop status updates *  Application statistics dashboard *  Authentication system *  Fully dockerized development environment  ---  ## Tech Stack  * **Backend:** Laravel * **Frontend:** Livewire + Blade * **Styling:** TailwindCSS * **Database:** MySQL * **Containerization:** Docker (Laravel Sail)  --- ## Project Architecture ```bash app/ ├── Concerns/ │ └── DetectsApplicationColumns.php # Shared trait for detecting application columns │ ├── Repositories/ │ └── ApplicationRepository.php # Handles database access │ ├── Actions/ │ ├── CreateApplication.php # Handles job application creation │ ├── UpdateApplication.php # Handles job application updates │ ├── MoveApplication.php # Handles Kanban column movement │ └── ScheduleInterview.php # Handles interview scheduling │ ├── Services/ │ └── ApplicationService.php # Business logic o…
