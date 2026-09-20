---
type: "corpus"
item_id: "7cf30c79afd4ff1a"
title: "GusAlberto/hired-flow"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/GusAlberto/hired-flow"
project_url: "https://github.com/GusAlberto/hired-flow"
author: "GusAlberto"
published_at: "2026-03-10T20:27:52Z"
captured_at: "2026-09-20T09:36:32+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-03-10"
tags:
  - 语料
  - github_new
  - Blade
  - topic:microsaas
metrics: {"stars": 1, "forks": 0, "open_issues": 1}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# GusAlberto/hired-flow

> [!info] 一句话导读
> A simple **Kanban-style job application tracker** built with Laravel, Livewire and Docker.

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/GusAlberto/hired-flow>
> 指标：stars=1 · forks=0 · open_issues=1
> 作者：GusAlberto　|　发布：2026-03-10T20:27:52Z
> 项目链接：<https://github.com/GusAlberto/hired-flow>
> 采集：2026-09-20T09:36:32+08:00　|　id：`7cf30c79afd4ff1a`

## 正文

# HiredFlow

A simple **Kanban-style job application tracker** built with Laravel, Livewire and Docker.

HiredFlow helps developers and job seekers track their job applications, interviews and offers in a simple visual board.

---

##  Features

*  Kanban board for tracking job applications
*  Track company and position
*  Application date tracking
*  Drag-and-drop status updates
*  Application statistics dashboard
*  Authentication system
*  Fully dockerized development environment

---

## Tech Stack

* **Backend:** Laravel
* **Frontend:** Livewire + Blade
* **Styling:** TailwindCSS
* **Database:** MySQL
* **Containerization:** Docker (Laravel Sail)

---
## Project Architecture
```bash
app/
├── Concerns/
│ └── DetectsApplicationColumns.php # Shared trait for detecting application columns
│
├── Repositories/
│ └── ApplicationRepository.php # Handles database access
│
├── Actions/
│ ├── CreateApplication.php # Handles job application creation
│ ├── UpdateApplication.php # Handles job application updates
│ ├── MoveApplication.php # Handles Kanban column movement
│ └── ScheduleInterview.php # Handles interview scheduling
│
├── Services/
│ └── ApplicationService.php # Business logic orchestrator
│
└── Livewire/
└── ApplicationsBoard.php # UI layer (validation + user interaction)
```
## Screenshot

Add a screenshot of the board here:

```
/docs/screenshot.png
```

Example:

![HiredFlow Dashboard](docs/screenshot.png)

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/hired-flow.git
cd hired-flow
```

Start Docker containers:

```bash
./vendor/bin/sail up -d
```

Run migrations:

```bash
./vendor/bin/sail artisan migrate
```

Install frontend dependencies:

```bash
./vendor/bin/sail npm install
./vendor/bin/sail npm run dev
```

Open the application:

```
http://localhost
```

---

## Roadmap

Future improvements:

* Job link storage (LinkedIn / Indeed)
* Notes per application
* File uploads (job description PDF)
* Email reminders
* Application analytics dashboard

---

## Motivation

Job searching often involves sending dozens or even hundreds of applications.

HiredFlow was created to help organize that process visually and make it easier to track which companies have responded.

---

## License

This project is open-source and available under the MIT License.

## 关联链接

- http://localhost
- https://github.com/YOUR_USERNAME/hired-flow.git

## 导航

- 项目页：[[10-项目/github.com_7cf30c79]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
