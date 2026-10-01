---
type: "corpus"
item_id: "e94ebeb3aba92da5"
title: "I got tired of filling out the same job applications, so I built this"
source: "reddit"
source_name: "Reddit 独立开发版块"
url: "https://www.reddit.com/r/SaaS/comments/1wlxfpd/i_got_tired_of_filling_out_the_same_job/"
project_url: "https://pypi.org/project/job-applier"
author: "No_Kangaroo_4454"
published_at: "2026-09-21T08:16:47+08:00"
captured_at: "2026-10-01T09:42:58+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-01"
pub_day: "2026-09-21"
tags:
  - 语料
  - reddit
  - r/SaaS
metrics: {"score": 3, "comments": 4, "upvote_ratio": 1}
comments_count: 4
comments_total: 4
discovered_via: "reddit:14d+settle10"
---

# I got tired of filling out the same job applications, so I built this

> [!info] 一句话导读
> I’ve been building a job application automation tool for myself and finally packaged it up.

> [!meta]- 语料信息（点开展开）
> 来源：Reddit 独立开发版块（post）
> 原帖：<https://www.reddit.com/r/SaaS/comments/1wlxfpd/i_got_tired_of_filling_out_the_same_job/>
> 指标：得分=3 · 评论=4 · 赞踩比=1
> 作者：No_Kangaroo_4454　|　发布：2026-09-21T08:16:47+08:00
> 项目链接：<https://pypi.org/project/job-applier>
> 采集：2026-10-01T09:42:58+08:00　|　id：`e94ebeb3aba92da5`

## 正文

I’ve been building a job application automation tool for myself and finally packaged it up.

Job Applier is a Python CLI that can actually open job applications in your browser, work through supported ATS/company flows, fill forms using any LLM model you choose, handle questions, and submit the application. It runs locally and connects to your existing Chrome session through CDP.

Answers are generated based on your own resume. You can also set company-specific answer preferences or define general answer preferences using natural language.

pip install job-applier

PyPI: https://pypi.org/project/job-applier/

It’s still early and definitely not perfect. I’ve spent a ridiculous amount of time dealing with all the annoying differences between Workday, Greenhouse, Ashby, etc., and there’s still a lot to improve.

Would love some real feedback from people who have built or used job application automation. What would you change, what would you want it to support, and what would make you actually use something like this?

## 评论（4/4）

> **chenforreal**（1 分） · 2026-09-21T08:43:54+08:00　
> The ATS edge cases are probably the moat here, not the LLM bit. I’d keep a simple supported-sites list and log every field that needs a manual fix. The first time it burns someone on a weird knockout question, trust is gone. How are you handling applications that need custom uploads or one-off questions?

---

> **No_Kangaroo_4454**（1 分） · 2026-09-21T08:54:59+08:00　
> Nice feedback. The core of this is the workflow engine.
> That deals with multiple hr systems and multiple companies.
> HR System this supports:
> 1. Ashby
> 2. BambooHR
> 3. ApplyToJobs
> 4. Greenhouse
> 5. Rippling ATS
> 6. Jobvite
> 7. Workday
> Companies it currently supports are:
> 1. Amazon
> 2. Henry Schein
>
> The workflow engine is the part I will keep developing.
>
> I built this in a way that I can switch between using Playwright and Pydoll with 1 single configuration setting.
>
> For your original question of how do I handle one-off questions, the form fields scanner is generic. It doesn't fetch questions by text.
>
> Once a question is fetched, it check for the user preferred answer for that question which is in an md file which is sent to the llm. If the question isn't there, it scans for the user's resume and answers the question based on user's resume.

---

> **SeaPsychological4022**（1 分） · 2026-09-21T09:41:00+08:00　
> 有趣的应用，为什么不把它做成一个 SaaS 应用

---

> **No_Kangaroo_4454**（1 分） · 2026-09-21T09:45:33+08:00　
> I want to eventually turn this to a SaaS product. Right now, looking for cofounder to build this with to a SaaS level. Until then, Ill continue working on adding more HR systems and Companies and use it myself and help others as much as possible.

## 关联链接

- https://pypi.org/project/job-applier/

## 导航

- 项目页：[[10-项目/pypi.org_75cd751f]]
- 渠道页：[[50-渠道/reddit]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
