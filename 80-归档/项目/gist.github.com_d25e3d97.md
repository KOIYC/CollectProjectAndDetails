---
type: "project"
title: "kicking the tires on jev (TypeSafe's System One model) with 2048"
project_url: "https://gist.github.com/cablehead/bdf9ad946ceb26d9008976e49c9bfbbb"
first_seen: "2026-09-20T03:06:43+08:00"
sources:
  - lobsters
tags:
  - 项目
  - lobsters
  - ai
  - games
lang: "en"
stale: true
---

# kicking the tires on jev (TypeSafe's System One model) with 2048

- **项目链接**：https://gist.github.com/cablehead/bdf9ad946ceb26d9008976e49c9bfbbb
- **首次收录**：2026-09-20T03:06:43+08:00
- **来源渠道**：Lobsters
- **标签**：ai, games
- **最新指标**：得分=9 · 评论=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-20T02:36:26+08:00 | Lobsters | 得分=9 · 评论=2 | [[80-归档/posts/lobsters/2026-09-20/8ee234d85301e282_kicking-the-tires-on-jev-(TypeSafe's-System-One-mo]] |
| 2026-09-20T02:48:08+08:00 | Lobsters | 得分=9 · 评论=2 | [[80-归档/posts/lobsters/2026-09-20/8ee234d85301e282_kicking-the-tires-on-jev-(TypeSafe's-System-One-mo]] |
| 2026-09-20T02:57:31+08:00 | Lobsters | 得分=9 · 评论=2 | [[80-归档/posts/lobsters/2026-09-20/8ee234d85301e282_kicking-the-tires-on-jev-(TypeSafe's-System-One-mo]] |
| 2026-09-20T03:06:43+08:00 | Lobsters | 得分=9 · 评论=2 | [[80-归档/posts/lobsters/2026-09-20/8ee234d85301e282_kicking-the-tires-on-jev-(TypeSafe's-System-One-mo]] |

## 摘要正文

# kicking the tires on jev with 2048  - Owner: cablehead - Created: 2026-09-19T05:39:18Z - Public: yes - Comments: 0 - Forks: 0  ## jev-2048.md  Language: Markdown  # kicking the tires on jev with 2048  I finally got a chance to kick the tires on jev (`jev-1.13.0`). I thought it'd do really well playing 2048.  the strategy I used was: hand it the current board state and give it the option of up, down, left, right. I tried that 4 ways (the jev rows in the table).. each row links to the request I sent.  with just the board it does about as well as making random moves. it does best when code works out what each move would do to the board and jev picks from those.. then it's about as good as a fixed rule (e.g. always left if that moves anything, else down, else right, else up).  I didn't have long to spend on it, so I'm likely missing something.  ## scores  every game was played to the end.  | player | games | min | median | max | best tile | first choice did nothing | |---|---|---|---|---|---|---| | random moves | 48 | 512 | 1102 | 2672 | 256 | n/a | | fixed rule: down if it moves anything, else left, else right, else up | 48 | 720 | 1964 | 7196 | 512 | n/a | | fixed rule: left if it …
