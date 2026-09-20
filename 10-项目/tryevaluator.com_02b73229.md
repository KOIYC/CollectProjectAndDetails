---
type: "project"
title: "Show HN: Don't ask if devs cheat with AI, test if they're good with it"
project_url: "https://tryevaluator.com/"
first_seen: "2026-09-21T02:53:01+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_skyepstein
  - story_48734393
  - show_hn
lang: "en"
---

# Show HN: Don't ask if devs cheat with AI, test if they're good with it

> [!info] 一句话导读
> Evaluator Pricing Sample Blog Log in Sign up

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://tryevaluator.com/>
> 首次收录：2026-09-21T02:53:01+08:00
> 来源渠道：HN Show HN
> 标签：author_skyepstein, story_48734393, show_hn
> 最新指标：点赞=5 · 评论=4 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T01:29:55+08:00 | HN Show HN | 点赞=5 · 评论=4 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/5a379b01fea9f66a_Show-HN-Don't-ask-if-devs-cheat-with-AI,-test-if-t]] |
| 2026-09-21T01:44:19+08:00 | HN Show HN | 点赞=5 · 评论=4 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/5a379b01fea9f66a_Show-HN-Don't-ask-if-devs-cheat-with-AI,-test-if-t]] |
| 2026-09-21T02:53:01+08:00 | HN Show HN | 点赞=5 · 评论=4 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-09-21/5a379b01fea9f66a_Show-HN-Don't-ask-if-devs-cheat-with-AI,-test-if-t]] |

## 摘要正文

Evaluator Pricing Sample Blog Log in Sign up Every engineer uses AI now. Hire the ones who use it well.  Evaluator scores how well a candidate actually works with AI: reading its output, fixing it, prompting it, and overriding it when it is wrong. Scored next to the fundamentals that still decide whether someone ships.  Generate a free assessment See a sample first  10 free every month No card required See what is tested AI critique Question 14 of 17  20 points An AI assistant produced this. It looks reasonable. It is not. Find every flaw and fix it.  async function fetchUserPosts(userId: string) {  const res = await fetch(`/api/users/${userId}/posts`)  const posts = res.json.parse()  return posts.filter((p, i) => i <= posts.length ) } What the candidate found  res.json.parse() is invented. The real call is await res.json() .  i <= posts.length is off by one, and the filter does nothing useful anyway.  Critique score 92 / 100 Five fundamentals, plus the one most tests skip.  Every assessment is generated for the role you are hiring for, in the stack you use. The questions change. The dimensions do not. AI collaboration  How it is scored  Five sub-tests covering prompt quality, read…
