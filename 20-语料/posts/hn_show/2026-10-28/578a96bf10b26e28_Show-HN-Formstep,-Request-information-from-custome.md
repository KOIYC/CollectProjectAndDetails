---
type: "corpus"
item_id: "578a96bf10b26e28"
title: "Show HN: Formstep, Request information from customers without the back-and-forth"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50261285"
project_url: "https://formstep.io/"
author: "mellosty"
published_at: "2026-10-27T16:03:31Z"
captured_at: "2026-10-28T09:39:16+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-28"
pub_day: "2026-10-27"
tags:
  - 语料
  - hn_show
  - author_mellosty
  - story_50261285
  - show_hn
metrics: {"points": 3, "comments": 0, "engagement_velocity": 3}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: Formstep, Request information from customers without the back-and-forth

> [!info] 一句话导读
> I built Formstep: https://formstep.ioThe idea came from a problem I kept running into while working on loan applications.A workflow could automate a large part …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50261285>
> 指标：点赞=3 · 评论=0 · engagement_velocity=3
> 作者：mellosty　|　发布：2026-10-27T16:03:31Z
> 项目链接：<https://formstep.io/>
> 采集：2026-10-28T09:39:16+08:00　|　id：`578a96bf10b26e28`

## 正文

I built Formstep: https://formstep.ioThe idea came from a problem I kept running into while working on loan applications.A workflow could automate a large part of the process, but eventually it would need something only the customer could provide: a document, a correction, a signature, an explanation, or confirmation of some information.At that point, workflow automation basically did not work.The forms themselves were also often the source of the problem. Applications came in with wrong documents, misunderstood questions, incomplete answers, or people simply forgetting to finish.Someone had to email the customer, explain what was missing, wait for a reply then follow up again. It was always back-and-forth.So I built Formstep to make requesting information from customers easier, not only for humans, but also for workflows and AI agents.The idea is: A person, workflow, or AI agent sends a customer a request through email or a link. Either re-use existing form or create unique for each customer.You can prefill what you already know, lock fields, pass context, and only ask the customer what you need.For example, we might already know:* Address that you already have in the CRM* Company description from the internet* What a agreement document must contain* How a good answer should beFormstep can check inputs and uploaded files while the customer is filling out the form and tell them if something is missing or inconsistent before they submit.
For example “The PDF does not contain your signature” or “Invoice total does not match the order amount”.The goal is to catch problems while the customer is still there, rather than letting bad data continue through the workflow and discovering it later.On the automation side, requests can currently be created through n8n, Zapier, the REST API, or by an AI agent over MCP.
When the customer finishes, the structured answers can go back into the workflow so it can continue.Forms and invitation/reminder are multilingual, and submitted answers can be translated inside the dashboard with one click. If you want, Formstep can be used as normal form builder and shared through public links, QR, embeds etc. It support custom themes for dark/light mode, with cover image, has Notion-style editor and much more. The list is too long to fit here.I want to make Formstep a plattform where it becomes more intelligent over time and ensures that we can get better answers from customers for any use case.My question to you:
Where do your automations currently stop because they need input from a customer or user, and how are you handling that today?If you are interested in trying out the n8n node: https://www.npmjs.com/package/n8n-nodes-formstepZapier integration: https://zapier.com/apps/formstep/integrationsConnecting your AI agent: https://docs.formstep.io/developers/mcp-server/Docs: https://docs.formstep.ioI would love your feedback and please try a quick demo at https://app.formstep.io/try

## 关联链接

- https://app.formstep.io/try
- https://docs.formstep.io/developers/mcp-server/Docs:
- https://docs.formstep.ioI
- https://formstep.ioThe
- https://www.npmjs.com/package/n8n-nodes-formstepZapier
- https://zapier.com/apps/formstep/integrationsConnecting

## 导航

- 项目页：[[10-项目/formstep.io_70284f67]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
