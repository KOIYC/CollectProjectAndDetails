---
type: "project"
title: "alifanov/ai-garage-launch"
project_url: "https://github.com/alifanov/ai-garage-launch"
first_seen: "2026-09-20T09:36:30+08:00"
sources:
  - github_new
tags:
  - 项目
  - github_new
  - topic:indie-hacker
lang: "en"
---

# alifanov/ai-garage-launch

> [!info] 一句话导读
> Плагин для **Claude Code**, который превращает методологию курса **AI Garage** в исполняемые команды. Не «на словах», а пошаговый пайплайн: от идеи до приёма пл…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/alifanov/ai-garage-launch>
> 首次收录：2026-09-20T09:36:30+08:00
> 来源渠道：GitHub 新星仓库
> 标签：topic:indie-hacker
> 最新指标：stars=2 · forks=0 · open_issues=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T09:24:07+08:00 | GitHub 新星仓库 | stars=2 · forks=0 · open_issues=0 | [[20-语料/posts/github_new/2026-09-20/eff95f06266bdb92_alifanov-ai-garage-launch]] |
| 2026-09-20T09:36:30+08:00 | GitHub 新星仓库 | stars=2 · forks=0 · open_issues=0 | [[20-语料/posts/github_new/2026-09-20/eff95f06266bdb92_alifanov-ai-garage-launch]] |

## 摘要正文

# AI Garage — Launch  Плагин для **Claude Code**, который превращает методологию курса **AI Garage** в исполняемые команды. Не «на словах», а пошаговый пайплайн: от идеи до приёма платежей. Каждая команда делает один шаг, пишет артефакт в `docs/` и подсказывает следующую.  Принцип курса: **не придумывай — копируй валидированное. 1 канал, 1 фича. Цель — 5k MRR.**  ## Установка  Внутри Claude Code:  ``` /plugin marketplace add alifanov/ai-garage-launch /plugin install garage@ai-garage-launch ```  Или из терминала:  ```bash claude plugin marketplace add alifanov/ai-garage-launch claude plugin install garage@ai-garage-launch ```  После установки в Claude Code доступны команды `/garage:*`. (Замени `alifanov` на свой GitHub-логин, если форкнул.)  ## Пайплайн  Каждая команда в конце указывает следующую — просто иди по цепочке.  ``` /garage:start      →  идеи и конкуренты-доноры        →  docs/01-ideas.md /garage:validate   →  5 вопросов-фильтров (go/no-go)   →  docs/02-validation.md /garage:channel    →  один канал трафика               →  docs/03-channel.md /garage:spec       →  бриф: ЦА, боль, 1 фича           →  docs/04-product.md /garage:scaffold   →  Next.js + Tailwind + shadcn      …
