---
type: "corpus"
item_id: "0a10e2182e000c98"
title: "Show HN: I built a tool that reviews any GitHub PR and quizzes you on it"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49123662"
project_url: "https://makesensegithub.com/"
author: "atomicnature"
published_at: "2026-07-31T14:32:29Z"
captured_at: "2026-09-21T02:55:06+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-07-31"
tags:
  - 语料
  - hn_show
  - author_atomicnature
  - story_49123662
  - show_hn
metrics: {"points": 6, "comments": 2, "engagement_velocity": 6}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:83d"
---

# Show HN: I built a tool that reviews any GitHub PR and quizzes you on it

> [!info] 一句话导读
> Prepend any Github PR URL with `makesense` to get a- quick review for all sorts of issues (cleanly designed issue explorer)- summary of changes in concise slide…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49123662>
> 指标：点赞=6 · 评论=2 · engagement_velocity=6
> 作者：atomicnature　|　发布：2026-07-31T14:32:29Z
> 项目链接：<https://makesensegithub.com/>
> 采集：2026-09-21T02:55:06+08:00　|　id：`0a10e2182e000c98`

## 正文

Prepend any Github PR URL with `makesense` to get a- quick review for all sorts of issues (cleanly designed issue explorer)- summary of changes in concise slide deck to grasp the essence of changes- a 5 question quiz on the changes to make sure there's "cognitive coverage" of the changeThere's also a handy bookmarklet using which you can trigger a review for any publicly accessible Github PRFeedback welcome

## 评论（2/2）

> **levi840714** · 2026-07-31T15:43:49.000Z　
> Is the quiz meant for the reviewer or the author? The quiz is the part I find genuinely new here. My one hesitation: since the questions come from the same model that wrote the summary, passing might just prove I absorbed the AI's reading of the diff, not that the reading was correct or that I understood the actual code. Curious whether the questions are grounded in the diff itself. Only tried the example on the landing page.

---

> **atomicnature** · 2026-07-31T15:51:34.000Z　
> The underlying assumption here is -- at least part of code is AI generated.Also another unstated assumption is that both the "author" and "reviewer" are reading AI-generated stuff, at least partlyFirst of all -- the author should not be surprised by any of the things the AI is reporting. If the author is -- either the reviewer AI went wrong, or the generative component went wrong. Either way -- there is something worth looking at in greater depth.For the reviewer -- or "traditional reviewer" as we may term them -- they are dealing with much greater volume per day now, again due to AI generation. This is supposed to help them get through things faster while not losing comprehension altogether.There's a reason we still have the code diff right below -- they are encouraged to check things themselves if they feel "something is off" with the quiz.The point is -- a few questions hopefully gets the wheels spinning in the reader rather than looking at the diff passively and saying "LGTM"And yes -- all the review results are grounded strictly in the diff

## 导航

- 项目页：[[10-项目/makesensegithub.com_b4b33329]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
