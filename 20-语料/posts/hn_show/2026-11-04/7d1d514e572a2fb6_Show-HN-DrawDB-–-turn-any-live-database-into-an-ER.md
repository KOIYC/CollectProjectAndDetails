---
type: "corpus"
item_id: "7d1d514e572a2fb6"
title: "Show HN: DrawDB – turn any live database into an ER diagram with one query"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50355761"
project_url: "https://github.com/drawdb-io/drawdb"
author: "1ilit"
published_at: "2026-11-03T18:10:57Z"
captured_at: "2026-11-04T09:51:43+08:00"
lang: "en"
kind: "post"
topic: "开发者工具"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - hn_show
  - author_1ilit
  - story_50355761
  - show_hn
metrics: {"points": 5, "comments": 1, "engagement_velocity": 5}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: DrawDB – turn any live database into an ER diagram with one query

> [!info] 一句话导读
> GitHub - drawdb-io/drawdb: Free, simple, and intuitive online database diagram editor and SQL generator.

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50355761>
> 指标：点赞=5 · 评论=1 · engagement_velocity=5
> 作者：1ilit　|　发布：2026-11-03T18:10:57Z
> 项目链接：<https://github.com/drawdb-io/drawdb>
> 采集：2026-11-04T09:51:43+08:00　|　id：`7d1d514e572a2fb6`

## 正文

Author: Thedan-1

GitHub - drawdb-io/drawdb: Free, simple, and intuitive online database diagram editor and SQL generator. · GitHub

Oct 31, 2026

1,242 Commits

Open commit details

## Folders and files

| Name | Name | Last commit message | Last commit date |
| --- | --- | --- | --- |
| .github | .github | Use node 20 and 22 in build workflow, depracate 18 (#1057) | Jun 24, 2026 |
| .husky | .husky | Add husky (#1160) | Oct 4, 2026 |
| public | public | Pass backend url to docker image at start time (#1157) | Sep 28, 2026 |
| src | src | Fix autosave for enum-only diagrams and empty edits (#1186) | Oct 31, 2026 |
| .dockerignore | .dockerignore | Create .dockerignore | May 22, 2024 |
| .env.sample | .env.sample | Remove octokit (#417) | Apr 21, 2025 |
| .eslintrc.cjs | .eslintrc.cjs | Diagram versioning (#560) | Aug 24, 2025 |
| .gitignore | .gitignore | Migrate to Vite from CRA | Dec 16, 2023 |
| .prettierrc.json | .prettierrc.json | Add prettier | Apr 6, 2024 |
| CONTRIBUTING.md | CONTRIBUTING.md | Create CONTRIBUTING.md | May 22, 2024 |
| Dockerfile | Dockerfile | Pass backend url to docker image at start time (#1157) | Sep 28, 2026 |
| LICENSE | LICENSE | Update LICENSE | Jul 21, 2024 |
| README.md | README.md | Pass backend url to docker image at start time (#1157) | Sep 28, 2026 |
| compose.yml | compose.yml | Expose host directly in compose | Jun 1, 2024 |
| drawdb.png | drawdb.png | Update readme | Nov 10, 2024 |
| index.html | index.html | Pass backend url to docker image at start time (#1157) | Sep 28, 2026 |
| package-lock.json | package-lock.json | Bump vite from 8.1.0 to 8.3.5 (#1181) | Oct 23, 2026 |
| package.json | package.json | Bump vite from 8.1.0 to 8.3.5 (#1181) | Oct 23, 2026 |
| postcss.config.js | postcss.config.js | Migrate to tailwind v4 (#370) | Mar 20, 2025 |
| tailwind.config.js | tailwind.config.js | Redo signup page | Jan 3, 2024 |
| vercel.json | vercel.json | Add vercel.json | Feb 27, 2024 |
| vite.config.js | vite.config.js | Migrate to Vite from CRA | Dec 16, 2023 |
| View all files | | | |

### Free, simple, and intuitive database schema editor and SQL generator.

DrawDB is a robust and user-friendly database entity relationship diagram (ERD) editor right in your browser. Build diagrams with a few clicks, export and import SQL scripts, generate migrations, customize your editor, and more without creating an account. See the full set of features on here.

### Local Development

```
git clone https://github.com/drawdb-io/drawdb
cd drawdb
npm install
npm run dev
```

### Build

```
git clone https://github.com/drawdb-io/drawdb
cd drawdb
npm install
npm run build
```

### Docker Build

```
docker build -t drawdb .
docker run -p 3000:80 drawdb
```

If you want to enable sharing, set up the server and environment variables according to `.env.sample`. This is optional unless you need to share files.

With the Docker image, pass the server URL when starting the container. No rebuild is needed:

```
docker run -p 3000:80 -e VITE_BACKEND_URL=https://your-drawdb-server.example.com ghcr.io/drawdb-io/drawdb:latest
```

## Contributing

Please see CONTRIBUTING.md for guidelines on how to contribute to this project.

# anthonyGosme/speedrunner

## 评论（1/1）

> **1ilit** · 2026-11-03T18:13:46.000Z　
> Try it at https://www.drawdb.app/editor, then File > Import from database.Happy to hear your feedback

## 关联链接

- https://your-drawdb-server.example.com

## 导航

- 项目页：[[10-项目/github.com_25966dd2]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
