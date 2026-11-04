---
type: "project"
title: "I built a personal dashboard that pulls my money, running, journal and reading into one place"
project_url: "https://www.reddit.com/r/SideProject/comments/1xept54/i_built_a_personal_dashboard_that_pulls_my_money/"
first_seen: "2026-11-04T09:52:43+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SideProject
lang: "en"
---

# I built a personal dashboard that pulls my money, running, journal and reading into one place

> [!info] 一句话导读
> For the last little while I've been building a self-hosted dashboard that runs on my laptop. It's a Flask (Python) backend with a React/Vite frontend. There are…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://www.reddit.com/r/SideProject/comments/1xept54/i_built_a_personal_dashboard_that_pulls_my_money/>
> 首次收录：2026-11-04T09:52:43+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SideProject
> 最新指标：得分=13 · 评论=18 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-04T09:52:43+08:00 | Reddit 独立开发版块 | 得分=13 · 评论=18 · 赞踩比=1 | [[20-语料/posts/reddit/2026-11-04/e3a37d55b3475f58_I-built-a-personal-dashboard-that-pulls-my-money,]] |

## 摘要正文

For the last little while I've been building a self-hosted dashboard that runs on my laptop. It's a Flask (Python) backend with a React/Vite frontend. There are five sections:  1. Home (a one-screen summary of my week)  2. Financials  3. Running  4. Journal  5. Books  Everything runs locally, and there's no cloud service (yet), and the data is plain CSV and JSON files I own. (The screenshots use made-up data)  Where the data comes from:  * Money: my bank and credit card PDF statements fill in historic data back to 2015, parsed into transactions, plus Plaid runs to keep accounts synced day to day. For Plaid I signed up for my own developer account and connected my accounts to it, so no third-party budgeting app sits in between. A small scikit-learn model and some keyword rules sort transactions into categories. On top of that sit monthly budgets with a "free to spend" number, automatic subscription detection, savings goals, retirement balances and a loan/debt payoff tracker. * Running: synced from Garmin Connect (runs, routes, HRV, sleep, VO2 max, training load) through the community garminconnect Python library. Garmin doesn't offer an official personal API, so this is unofficial. …
