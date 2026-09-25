---
type: "corpus"
item_id: "9438300c78337e81"
title: "I added Mages to my RTS Prototype and now it's all the AI wants to build"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/IndieDev/comments/1wgqwel/i_added_mages_to_my_rts_prototype_and_now_its_all/"
author: "Perfect-Macaron2041"
published_at: "2026-09-15T13:03:39+08:00"
captured_at: "2026-09-25T13:43:34+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-25"
pub_day: "2026-09-15"
tags:
  - 语料
  - reddit
  - r/indiedev
  - Screenshots
metrics: {"score": 15, "comments": 4, "upvote_ratio": 0.84}
comments_count: 4
comments_total: 4
discovered_via: "reddit:14d+settle10"
---

# I added Mages to my RTS Prototype and now it's all the AI wants to build

> [!info] 一句话导读
> document.addEventListener("DOMContentLoaded",async function(){var e=document.forms[0],n=(e.onsubmit=function(t){return new URLSearchParams(document.location.sea…

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/IndieDev/comments/1wgqwel/i_added_mages_to_my_rts_prototype_and_now_its_all/>
> 指标：得分=15 · 评论=4 · 赞踩比=0.84
> 作者：Perfect-Macaron2041　|　发布：2026-09-15T13:03:39+08:00
> 项目链接：—
> 采集：2026-09-25T13:43:34+08:00　|　id：`9438300c78337e81`

## 正文

Reddit

 document.addEventListener("DOMContentLoaded",async function(){var e=document.forms[0],n=(e.onsubmit=function(t){return new URLSearchParams(document.location.search).forEach((e,n)=>t.target.appendChild(Object.assign(document.createElement("input"),{name:n,type:"hidden",value:e}))),!0},await(async e=>e+e)("f08e4f5bbe0473f6"));e.elements.namedItem("solution").value=n,e.requestSubmit()},{once:!0});

 main{align-items:center;display:flex;height:100vh;isolation:isolate;justify-content:center;position:relative;width:100vw}main:before{animation:scaleout 1.5s infinite ease-in-out;background-color:#d93900;border-radius:100%;content:'';height:8rem;opacity:.75;position:absolute;width:8rem}.logo{align-items:center;display:flex;fill:currentColor;font-size:4rem;justify-content:center;z-index:1}.logo svg{fill:currentColor;height:8rem;width:auto}@keyframes scaleout{0%{transform:scale(1)}100%{transform:scale(1.5);opacity:0}}.snoo-cls-1{fill:url(#snoo-radial-gragient) white}.snoo-cls-1,.snoo-cls-2,.snoo-cls-3,.snoo-cls-4,.snoo-cls-5,.snoo-cls-6,.snoo-cls-7,.snoo-cls-8,.snoo-cls-9,.snoo-cls-10,.snoo-cls-11{stroke-width:0}.snoo-cls-2{fill:url(#snoo-radial-gragient-2) white}.snoo-cls-3{fill:url(#snoo-radial-gragient-3) white}.snoo-cls-4{fill:url(#snoo-radial-gragient-4) #fc4301}.snoo-cls-5{fill:url(#snoo-radial-gragient-6) black}.snoo-cls-6{fill:url(#snoo-radial-gragient-8) black}.snoo-cls-7{fill:url(#snoo-radial-gragient-5) #fc4301}.snoo-cls-8{fill:url(#snoo-radial-gragient-7) white}.snoo-cls-9{fill:#842123}.snoo-cls-10{fill:#ff4500}.snoo-cls-11{fill:#ffc49c}

Error fetching https://v.redd.it/tcbdio40xlph1: CRAWL_LIVECRAWL_TIMEOUT
Error fetching https://i.redd.it/lfkani353mph1.png: CRAWL_LIVECRAWL_TIMEOUT

## 评论（4/4）

> **gleeptime**（4 分） · 2026-09-15T13:07:53+08:00　
> Make limiters on mages for the bots

---

> **acorbinelli**（-5 分） · 2026-09-15T13:46:48+08:00　
> Ha, the AI found the dominant strategy before your playtesters did, which is honestly a useful tool. Two separate fixes, because they solve different problems:
>
> For the AI, stop it choosing the single best unit and give it a composition target instead, something like "no more than a quarter mages", and have it build whatever is furthest below its target. That's also a nice knob for difficulty and personality: a turtle AI and a rush AI are just different targets.
>
> For the balance, give mages a real answer rather than only nerfing numbers: a fast unit that can reach the backline, a longer cast time they're vulnerable during, or a splash that hurts their own side when enemies close in. If a mage-only army loses badly to the right counter, the AI stops being wrong for building them and starts being wrong for not scouting.
>
> The mage burst reads really clearly in the first screenshot, by the way, even at that zoom.

---

> **cococommandos**（9 分） · 2026-09-15T13:49:19+08:00　
> Thanks Claude

---

> **AshenThroneDev**（3 分） · 2026-09-15T14:58:11+08:00　
> Honestly the AI spamming them is useful data, it's a free balance bot telling you mages have no answer yet. Two things worth trying:
>
> 1. Give every unit a hard counter instead of only nerfing stats. In Ashen Throne we went with a three-way counter triangle, so a pure stack of anything loses to the thing that beats it, which kills mono-builds for players and AI alike.
> 2. Have the AI pick its build against what the other side is fielding rather than raw strength, so once mages dominate it starts building whatever counters them.
>
> Nerfing mages alone usually just moves the spam to the next best unit.

## 关联链接

- https://i.redd.it/lfkani353mph1.png:
- https://v.redd.it/tcbdio40xlph1:

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
