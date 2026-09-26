---
type: "project"
title: "Built an open-model AI music studio (silens.ai) on Cloudflare & Modal. Going back to a full time job soon and looking for advice"
project_url: "https://silens.ai/"
first_seen: "2026-09-26T09:42:50+08:00"
sources:
  - reddit
tags:
  - 项目
  - reddit
  - r/SideProject
lang: "en"
---

# Built an open-model AI music studio (silens.ai) on Cloudflare & Modal. Going back to a full time job soon and looking for advice

> [!info] 一句话导读
> 👋 I built [Silens](https://silens.ai/) as a personal side project.

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://silens.ai/>
> 首次收录：2026-09-26T09:42:50+08:00
> 来源渠道：Reddit 独立开发版块
> 标签：r/SideProject
> 最新指标：得分=3 · 评论=5 · 赞踩比=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-26T09:42:50+08:00 | Reddit 独立开发版块 | 得分=3 · 评论=5 · 赞踩比=1 | [[20-语料/posts/reddit/2026-09-26/3814c6a13723760f_Built-an-open-model-AI-music-studio-(silens.ai)-on]] |

## 摘要正文

👋 I built [Silens](https://silens.ai/) as a personal side project.  I wanted to see how far open-source music models have come compared to closed platforms like Suno or Udio, and whether it was possible to create a full, end-to-end studio experience — lyrics, arrangement, vocal synthesis, and mixing — on a completely serverless, zero-maintenance stack.  It’s live now, and you can try it here: [https://silens.ai](https://silens.ai/)  # The Tech Stack  I designed the architecture to be as lightweight and cost-effective as possible, so it wouldn't incur huge hosting bills while idle:  * **Frontend:** Next.js (static export) hosted on Cloudflare Pages * **Backend / Edge API:** Cloudflare Workers handles auth, rate limiting, job dispatching, and API routes * **Database & Storage:** Cloudflare D1 (serverless SQLite) for songs/user metadata, and Cloudflare R2 for streaming audio files * **Prompt & Lyrics AI:** Cloudflare Workers AI (Llama models) for structured prompt analysis and lyrics generation * **Audio Inference Engine:** Modal running serverless GPU containers (T4 / A10G) * **Open-weights models:** ACE-Step 1.5 for vocal synthesis/singing and MusicGen for instrumental arrangements …
