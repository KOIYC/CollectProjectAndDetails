---
type: "corpus"
item_id: "eff95f06266bdb92"
title: "alifanov/ai-garage-launch"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/alifanov/ai-garage-launch"
project_url: "https://github.com/alifanov/ai-garage-launch"
author: "alifanov"
published_at: "2026-07-16T08:29:48Z"
captured_at: "2026-09-20T09:36:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-07-16"
tags:
  - 语料
  - github_new
  - topic:indie-hacker
metrics: {"stars": 2, "forks": 0, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# alifanov/ai-garage-launch

> [!info] 一句话导读
> Плагин для **Claude Code**, который превращает методологию курса **AI Garage** в исполняемые команды. Не «на словах», а пошаговый пайплайн: от идеи до приёма пл…

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/alifanov/ai-garage-launch>
> 指标：stars=2 · forks=0 · open_issues=0
> 作者：alifanov　|　发布：2026-07-16T08:29:48Z
> 项目链接：<https://github.com/alifanov/ai-garage-launch>
> 采集：2026-09-20T09:36:30+08:00　|　id：`eff95f06266bdb92`

## 正文

# AI Garage — Launch

Плагин для **Claude Code**, который превращает методологию курса **AI Garage** в исполняемые команды. Не «на словах», а пошаговый пайплайн: от идеи до приёма платежей. Каждая команда делает один шаг, пишет артефакт в `docs/` и подсказывает следующую.

Принцип курса: **не придумывай — копируй валидированное. 1 канал, 1 фича. Цель — 5k MRR.**

## Установка

Внутри Claude Code:

```
/plugin marketplace add alifanov/ai-garage-launch
/plugin install garage@ai-garage-launch
```

Или из терминала:

```bash
claude plugin marketplace add alifanov/ai-garage-launch
claude plugin install garage@ai-garage-launch
```

После установки в Claude Code доступны команды `/garage:*`. (Замени `alifanov` на свой GitHub-логин, если форкнул.)

## Пайплайн

Каждая команда в конце указывает следующую — просто иди по цепочке.

```
/garage:start      →  идеи и конкуренты-доноры        →  docs/01-ideas.md
/garage:validate   →  5 вопросов-фильтров (go/no-go)   →  docs/02-validation.md
/garage:channel    →  один канал трафика               →  docs/03-channel.md
/garage:spec       →  бриф: ЦА, боль, 1 фича           →  docs/04-product.md
/garage:scaffold   →  Next.js + Tailwind + shadcn      →  docs/05-build.md
/garage:deploy     →  GitHub + Vercel + домен          →  docs/06-deploy.md
/garage:db-auth    →  Neon + Clerk                     →  docs/07-infra.md
/garage:analytics  →  Plausible/PostHog + воронка      →  docs/08-analytics.md
/garage:launch     →  первый шаг канала                →  docs/09-launch.md
/garage:metrics    →  CAC / LTV / retention / UTM      →  docs/10-metrics.md
/garage:payments   →  Polar (монетизация)              →  docs/11-payments.md

/garage:status     →  чек-лист: что сделано / что осталось
```

## Как это работает

- **Артефакты в `docs/`.** Каждая команда пишет результат в `docs/NN-*.md`. Следующие команды **читают** эти файлы — контекст не теряется между шагами и сессиями.
- **Единый статус.** `docs/STATE.md` — чек-лист пайплайна (Продукт / Донор / Канал + галочки). Команды его обновляют, `/garage:status` показывает.
- **Проверка предусловий.** Каждая команда сверяется с `docs/`: если предыдущий шаг не сделан — подскажет, что запустить сначала.
- **Скиллы-справочники** подтягиваются автоматически: `stack-reference`, `traffic-channels`, `unit-economics`, `payments-polar`.
- **Сабагенты** для тяжёлых шагов: `competitor-researcher` (ресёрч/валидация), `deploy-runner` (деплой).

## Стек

Всё бесплатное или с бесплатным тиром: **Next.js · GitHub · Vercel · Neon · Clerk · Plausible/PostHog · Resend · Polar**.

## Смежные скиллы (опционально)

Пайплайн использует, если установлены: `namecheap` (домены), `dataforseo-keyword-research`, `similarweb`, `ads-funnel`, `seo-audit`, `content-strategy`.

## Структура репозитория

```
.claude-plugin/
  plugin.json          # манифест плагина (name: garage)
  marketplace.json     # репо сам себе маркетплейс (name: ai-garage-launch)
commands/              # 12 команд пайплайна
skills/                # 4 справочника
agents/                # 2 сабагента
```

## Лицензия

MIT

## 导航

- 项目页：[[10-项目/github.com_eff95f06]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
