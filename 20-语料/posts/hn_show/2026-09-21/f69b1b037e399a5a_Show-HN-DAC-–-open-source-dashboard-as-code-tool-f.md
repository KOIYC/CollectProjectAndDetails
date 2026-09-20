---
type: "corpus"
item_id: "f69b1b037e399a5a"
title: "Show HN: DAC – open-source dashboard as code tool for agents and humans"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47949066"
project_url: "https://github.com/bruin-data/dac"
author: "karakanb"
published_at: "2026-04-29T14:37:20Z"
captured_at: "2026-09-21T01:41:53+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-29"
tags:
  - 语料
  - hn_show
  - author_karakanb
  - story_47949066
  - show_hn
metrics: {"points": 119, "comments": 35, "engagement_velocity": 119}
comments_count: 35
comments_total: 35
discovered_via: "hn:show_hn:174d"
---

# Show HN: DAC – open-source dashboard as code tool for agents and humans

> [!info] 一句话导读
> Hi all, this is Burak.When agents became a reality one of the first things I wanted to do was to automate building dashboards. The first, and the most obvious, …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47949066>
> 指标：点赞=119 · 评论=35 · engagement_velocity=119
> 作者：karakanb　|　发布：2026-04-29T14:37:20Z
> 项目链接：<https://github.com/bruin-data/dac>
> 采集：2026-09-21T01:41:53+08:00　|　id：`f69b1b037e399a5a`

## 正文

Hi all, this is Burak.When agents became a reality one of the first things I wanted to do was to automate building dashboards. The first, and the most obvious, wall that I ran into was that a lot of the tools were just driven by UI. This meant that without the agents handling browser UIs and whatnot, it wasn't possible to have the agents do that. In addition, it would be impossible to review any of the changes the agent would make.The first instinct there is to get your agent to build a React app for the dashboard. This works beautifully for the happy path, but I quickly ran into other issues there:
- every dashboard turns out to be different
- have to implement a backend to centralize the query execution
- there is no centralized mechanism to control the rules and standards around visualizations
- there is no way to get a semantic layer working with the dashboards easilyIn the end, agents ended up reinventing the wheel for every new dashboard, even under the same project. Building a standardized, local project for these turned out to be building a BI tool from scratch.After trying these out, I asked myself: what if the dashboards were built for agents as the primary user?A product like that would need to have a couple of features:
- First of all, everything needs to be driven by version-controllable text. YAML is fine.
- Changes to the dashboards should be easy to review and understand by humans.
- Agents are great at writing code, it'd be great if this were driven by code to have dynamic stuff: JSX would be great.
- Static analysis being a first-class citizen: validate dashboards before deploying. Agents can check their work too.
- A standardized way of deploying these based on a couple of files in a folder: operationally very simple.
- Built-in semantic layer to standardize metrics.That's what I ended up building: dac (Dashboard-As-Code) is an open-source tool and a spec to define dashboards, well, as code. It contains an implementation in Go that can be deployed as a single binary anywhere. The dashboards are defined in YAML and JSX, YAML for static stuff, JSX for dynamic dashboards. You can run queries at load time to define conditional charts, generate tabs on the fly per customer, or list charts for each A/B test you are running.I built it in Go because I do love Go, and I think it is the greatest language at the moment to work with AI agents.dac runs as a single binary, you can get started with a `dac init` command and it'll automatically create some sample dashboards for you based on duckdb. It supports 10+ SQL backends, with more to come. It supports validation, custom themes and whatnot.You can see it here: https://github.com/bruin-data/dacI would love to hear what can be improved here, please let me know your thoughts.

## 评论（35/35）

> **lexh** · 2026-05-02T10:53:48.000Z　
> Consider adding that snazzy gif in the README to the docs landing page. I went straight to the docs and then hunted for a screenshot to no avail.

---

> **5-0** · 2026-05-02T11:36:38.000Z　
> DaC might be more distinguishable from DAC, although the context obviously also helps readers telling them apart.Yours sincerely, came here for another DAC

---

> **crefiz** · 2026-05-02T12:08:00.000Z　
> I reckon this is a simplification of existing BIAC tools (eg, https://github.com/lightdash/lightdash)

---

> **SomeHacker44** · 2026-05-02T12:27:10.000Z　
> The blurb about this is repeated several times but it is unclear to me what it actually does.

---

> **MuffinFlavored** · 2026-05-02T13:11:27.000Z　
> Might want to add how this compares to other products in the space.Some that come to mind that are potentially tangentially related/similar:https://github.com/evidence-dev/evidence

---

> **hasyimibhar** · 2026-05-02T13:23:44.000Z　
> Why not use Vega-Lite[0]? It’s my go-to data viz DSL with Claude.[0] https://vega.github.io/vega-lite/

---

> **MSaiRam10** · 2026-05-02T14:28:49.000Z　
> Semantic layer + validation is the interesting part imo, everything else is table stakes. would lead with that

---

> **xixixao** · 2026-05-02T15:38:07.000Z　
> Why do ppl think building something through yaml is ever a good idea??(I know why: for a platform it’s simpler to parse a yaml than to run code, but it’s almost never a good idea for anything that needs to scale in complexity)

---

> **pryanshu89** · 2026-05-02T15:53:21.000Z　
> I would really hesitate to use a 1000 lines of yaml and modify them. I never found YAML easy to modify after a certain size.

---

> **Hnrobert42** · 2026-05-02T17:01:32.000Z　
> Have you thought about how these dashboards could be built for an eink screen?For a while, I was thinking about starting a side project of selling E-ink screens with easily configured dashboards. The project would support hobbies who want to build dashboards powered by a raspberry pi or something. I never pursued it, but it seems like you are now halfway there.

---

> **m_ramdhan** · 2026-05-02T18:36:29.000Z　
> The "agents as primary user" framing is what makes this stand out from other dashboard-as-code tools. Having agents generate dashboards is one thing, but making those dashboards reviewable and standardized is the actual hard part. Curious about the semantic layer — when an agent modifies a metric definition in semantic/, how does validation work? Does DAC flag downstream widgets that would break, or is it more of a "trust but verify" model where you catch issues at render time?

---

> **sumeno** · 2026-05-02T18:51:37.000Z　
> Yet another "Show HN" that has existed for less than a week. I wish the rules against AI generated content were applied to all these too.

---

> **gervwyk** · 2026-05-02T20:50:28.000Z　
> Well done on the launch! We’ve doubled down on the apps as YAML paradigm a few years ago and its pay great dividends on all fronts, esp now with code gen spinning out apps faster than ever for us (generated yaml). Our largest app is well over 500k lines of yaml - for those complaining about 1000 lines lol. With the right tool stack and conventions its so much easier to read, write. review and maintain.
>  Shameless plug, we’ve built Lowdefy (open source) and 100s of dashboards using it. Have a look and keen to unpack if you’re interested in sharing experiences. Specially have a look at what we did with operators for dynamic needs.
> https://github.com/lowdefy/lowdefy

---

> **laurels-marts** · 2026-05-03T11:18:41.000Z　
> What I’ve heard often is that the customer might want to build a dashboard using AI on the fly.Like imagine you have a site and there’s blank canvas. It has access to some data in the background. The user might be like “build a dashboard showing YoY performance of X and break down the shipments in a table by Y and Z”. Then the agent builds it and persists it such that when they log out and log back in they can see their custom dashboard they assembled themselves.

---

> **ktrnka** · 2026-05-03T22:03:34.000Z　
> Love the idea. The ability to PR a dashboard would've helped us in multiple companies.The two big areas that could use some docs/work:
> - Auth (one company was healthtech, so we needed auth even on VPN. The other didn't have a VPN so we needed auth)
> - Hosting: If it just needs to be run in a container and it doesn't need to be restarted that's fine. Though if there isn't a hosting document it's often a sign of a service that will need someone to keep it running all the time

---

> **karakanb** · 2026-05-02T11:29:03.000Z　
> That's a great idea, will do very quickly, thanks!

---

> **karakanb** · 2026-05-02T12:48:25.000Z　
> Point taken, thanks! Out of curiosity, which DAC did you come here for?

---

> **karakanb** · 2026-05-02T12:47:28.000Z　
> Partly, yes. It is a simplification with the perspective that the agents would be the primary builders.

---

> **karakanb** · 2026-05-02T12:46:34.000Z　
> You write a few lines of YAML or JSX and you get a dynamic, interactive dashboard out of it. Do you have any suggestions on how to make it simpler?

---

> **karakanb** · 2026-05-02T13:48:06.000Z　
> There are quite a few libraries for charts and visualization, there are not as many for actually combining many of them with layouts, different components and including the actual implementation of the backend. Dac aims to provide all that as a standard and an implementation.

---

> **dleeftink** · 2026-05-02T17:34:16.000Z　
> Observable Framework[0] attempted to fill this niche for a while as well, and we'll likely see some of the implementation details in the new Observable Notebook 2.0 format too.[0]: https://github.com/observablehq/framework

---

> **karakanb** · 2026-05-02T19:43:34.000Z　
> That's a good point, thanks!

---

> **cyberge99** · 2026-05-02T15:53:54.000Z　
> What is a better format that allows inline comments, is human readable, and can be easily converted to other formats (json, xml, et al)

---

> **karakanb** · 2026-05-02T19:41:48.000Z　
> DAC currently supports YAML and JSX, what else would be a good alternative?

---

> **Hnrobert42** · 2026-05-02T16:55:57.000Z　
> You have trouble with them when you are modifying them by hand or using an LLM to do it? The purpose of this project is having LLMs do it. I found they are about as good at writing yaml as they are writing anything else.

---

> **karakanb** · 2026-05-02T19:41:02.000Z　
> Thanks! DAC does that kind of validation partially, although doesn't validate the usage of the downstream dashboards. That's a very nice idea though.In terms of validation it will validate queries, metric definitions, chart definitions and all ahead of time, before render. That way agents tend to validate their work much quicker.

---

> **seattle_spring** · 2026-05-02T21:38:17.000Z　
> Is this an AI generated comment? The format follows almost exactly the format of your other comments, down to the location of the em-dash.

---

> **karakanb** · 2026-05-02T19:43:18.000Z　
> The project has been under development for over 6 months. We just open sourced it with a clean history. I am not sure what you expect here, should a project exist for months before it is worthy of a show post?

---

> **ggrelet** · 2026-05-02T13:04:50.000Z　
> Most probably: https://en.wikipedia.org/wiki/Digital-to-analog_converter

---

> **bpev** · 2026-05-02T17:15:49.000Z　
> yup yup I also came here for electronics/digital audio without finishing reading the title. DAC is super standard to read in those spaces.

---

> **hasyimibhar** · 2026-05-02T14:45:14.000Z　
> I mean that's what the Vega team is doing no? They are building the standard grammar (Vega-Lite), along with an implementation (Vega). And they are already quite established with rich ecosystem, and supports a ton of components[0]. The only thing missing is that it expects a CSV or inline data source. But it's probably not too hard to build an extension that connects to a data warehouse with an SQL query.[0] https://vega.github.io/vega-lite/examples

---

> **Hnrobert42** · 2026-05-02T16:58:08.000Z　
> The comments are why I prefer YAML for config over JSON. Of course, JSON is great for many purposes, especially machine to machine. For human to machine, I prefer YAML.

---

> **pryanshu89** · 2026-05-03T06:11:46.000Z　
> I do it by hand.

---

> **sumeno** · 2026-05-03T22:51:33.000Z　
> Yes.

---

> **karakanb** · 2026-05-02T19:39:20.000Z　
> I am not sure we are on the same page, as far as I am aware Vega doesn't do layout, does it? E.g DAC could use Vega for the charts and still take care of everything else around it.

## 关联链接

- https://github.com/bruin-data/dacI

## 导航

- 项目页：[[10-项目/github.com_233f5b98]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
