---
type: "project"
title: "Show HN: Bulk-harden all your GitHub repos' settings without an API token"
project_url: "https://gist.github.com/1ch4k/ba726954db1cc509c2071d54f93b5304"
first_seen: "2026-11-09T09:39:29+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_1ch4k
  - story_50416829
  - show_hn
lang: "en"
---

# Show HN: Bulk-harden all your GitHub repos' settings without an API token

> [!info] 一句话导读
> Bulk-harden your GitHub repo settings

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://gist.github.com/1ch4k/ba726954db1cc509c2071d54f93b5304>
> 首次收录：2026-11-09T09:39:29+08:00
> 来源渠道：HN Show HN
> 标签：author_1ch4k, story_50416829, show_hn
> 最新指标：点赞=2 · 评论=1 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-09T09:39:29+08:00 | HN Show HN | 点赞=2 · 评论=1 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-09/3d1c8a8c72eaa5e0_Show-HN-Bulk-harden-all-your-GitHub-repos'-setting]] |

## 摘要正文

# Bulk-harden your GitHub repo settings  - Owner: 1ch4k - Created: 2026-11-08T20:23:03Z - Public: yes - Comments: 0 - Forks: 0  ## harden_github_repos.py  Language: Python  # /// script # requires-python = ">=3.10" # dependencies = ["playwright"] # /// """ harden_github_repos.py: bulk-harden the settings of every public repo you own on GitHub.  For each repo it opens the settings in a real browser window and:  * Features -> turns the Wiki off (or only restricts editing, see --wiki)  * Advanced Security -> enables Private vulnerability reporting,  Secret Protection and Push protection Steps that are already done are skipped, so it is safe to re-run after creating new repos.  Why a browser and not the API? It needs no token at all: you sign in to GitHub yourself in the window that opens, and the script only clicks the same buttons you would.  Usage (needs uv: https://docs.astral.sh/uv/):  uv run harden_github_repos.py --dry-run # show what would change, click nothing  uv run harden_github_repos.py # apply Options:  --owner NAME account to process (default: the account you sign in with)  --wiki restrict keep wikis but only collaborators can edit (default: off)  --no-pvr don't touch Pr…
