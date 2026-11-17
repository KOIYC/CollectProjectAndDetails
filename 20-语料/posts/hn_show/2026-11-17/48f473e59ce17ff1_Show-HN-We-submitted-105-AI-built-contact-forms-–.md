---
type: "corpus"
item_id: "48f473e59ce17ff1"
title: "Show HN: We submitted 105 AI-built contact forms – 27 said \"sent\", sent nothing"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50524591"
project_url: "https://github.com/formgong/dead-forms-study"
author: "Formgong"
published_at: "2026-11-16T22:47:31Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_Formgong
  - story_50524591
  - show_hn
metrics: {"points": 4, "comments": 0, "engagement_velocity": 4}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: We submitted 105 AI-built contact forms – 27 said "sent", sent nothing

> [!info] 一句话导读
> formgong/dead-forms-study

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50524591>
> 指标：点赞=4 · 评论=0 · engagement_velocity=4
> 作者：Formgong　|　发布：2026-11-16T22:47:31Z
> 项目链接：<https://github.com/formgong/dead-forms-study>
> 采集：2026-11-17T11:09:12+08:00　|　id：`48f473e59ce17ff1`

## 正文

# formgong/dead-forms-study

Do contact forms on AI-built sites send anything? A Playwright harness that checks without sending, with known-answer fixtures and the study's method and results.

- Stars: 0
- Forks: 0
- Watchers: 0
- Open issues: 0
- License: MIT License
- Homepage: https://formgong.com/en/blog/contact-forms-that-send-nothing/
- Default branch: main
- Created: 2026-10-07T22:58:26Z

## Languages

- HTML
- JavaScript

## Topics

- bolt
- contact-form
- formgong
- lovable
- playwright
- research
- testing
- web-forms

## Top Contributors

- formgong-hq (1 contributions)
- VitaliiNemyrovskyi (1 contributions)

---

## README

# Contact forms that send nothing — study and test harness

We submitted the contact form on public Lovable and Bolt sites while recording every network request and **blocking all of them**, so no message ever reached a site owner. On the final run, **27 of 105** forms showed a success message ("Message sent!") and sent nothing; 54 of 105 sent the typed message. On sites without demo signs, 16 of 73 were fake.

Write-up: https://formgong.com/en/blog/contact-forms-that-send-nothing/

| File | What it is |
| --- | --- |
| `PREREG.md` | Rules written before testing, and every later change with the reason (seven harness faults found by manual checks) |
| `RESULTS.md` | Final numbers with denominators |
| `harness.mjs` | The test: Playwright + installed Chrome, one visit per site |
| `fixtures/` | 23 local pages with known answers (`expected.tsv`) |

## Run it

```bash
npm install
npm run fixtures                       # 23 known-answer pages; all must match
node harness.mjs https://your-site.example --out result.jsonl
```

Requires Google Chrome (the harness launches it with `channel: "chrome"`).

## How it decides

After the contact form is found, every request is intercepted. Same-origin static files and cross-origin scripts, styles and fonts load; **everything else is recorded and aborted**. The harness fills visible fields with obvious test values (never honeypots), presses send and watches the page for five seconds.

- `SENDS` — a request carried what was typed.
- `FAKE_SUCCESS` — no such request, no other outgoing request, and a success message (or `alert()`) appeared.
- `NO_EFFECT`, `MAILTO`, `RELOAD`, `REDIRECT_NO_SEND`, `OTHER_REQUEST`, `INVALID`, `VOID` — see PREREG.md.

## If your form sends nothing

Open DevTools → Network and press send: a working form adds a request that carries the text you typed. The write-up's fix section lists three ways to fix it. Coding agents (Claude Code, Cursor, Codex) can install a skill that adds a working form and replaces fake handlers:

```bash
npx skills add formgong/skills
```

## Ethics

Nothing is submitted to anyone. The site list and per-site results are not published, and the write-up names no site. Please use the harness the same way.

MIT licensed. Made by Formgong.

# skanga/Emergency-AI

## 关联链接

- https://formgong.com/en/blog/contact-forms-that-send-nothing/
- https://your-site.example

## 导航

- 项目页：[[10-项目/github.com_bac42b8a]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
