---
type: "project"
title: "Show HN: Who and where are your anagranames?"
project_url: "https://louisabraham.github.io/anagranames"
first_seen: "2026-11-05T11:21:45+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_Labo333
  - story_50371286
  - show_hn
lang: "en"
---

# Show HN: Who and where are your anagranames?

> [!info] 一句话导读
> Hi HN!I made this fun app which combines quite a few ideas, I thought you might like the story:A few months ago I had the idea of looking for anagrams of names.…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://louisabraham.github.io/anagranames>
> 首次收录：2026-11-05T11:21:45+08:00
> 来源渠道：HN Show HN
> 标签：author_Labo333, story_50371286, show_hn
> 最新指标：点赞=2 · 评论=0 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-05T11:21:45+08:00 | HN Show HN | 点赞=2 · 评论=0 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-11-05/84f7f1ede5071a92_Show-HN-Who-and-where-are-your-anagranames]] |

## 摘要正文

Hi HN!I made this fun app which combines quite a few ideas, I thought you might like the story:A few months ago I had the idea of looking for anagrams of names. I started with french names using official statistics about first and last names, which also gave me a pretty simple model for likely anagrams: P(first + last) = P(first) * P(last).Then, I started checking which anagra-names (I coined the term) appeared in the 2021 Facebook leak.Finally, I improved my ranking using a factorization model.All this is available as a light and fast webpage thanks to a lot of cool algorithmic tricks detailed here: https://louisabraham.github.io/anagranames/how.htmlAbout the use of AI:Claude Code was fantastic for building the frontend (including the interactive globe) and writing the MLX code (I would otherwise have used PyTorch, which is slower on my machine). It also handled the quantization with very little guidance, which was particularly useful since I'm not an expert in that area.That said, I'm glad I learned CS before LLMs existed and still master it enough to work out the ideas and specs for everything else in my head / on paper before handing the implementation over to the agent.
