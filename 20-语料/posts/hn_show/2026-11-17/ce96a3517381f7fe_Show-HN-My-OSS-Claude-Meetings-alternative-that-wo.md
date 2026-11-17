---
type: "corpus"
item_id: "ce96a3517381f7fe"
title: "Show HN: My OSS Claude Meetings alternative that works with any agent or call"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50522602"
project_url: "https://github.com/wanderingstan/vibeconf-app"
author: "wanderingstan"
published_at: "2026-11-16T20:18:57Z"
captured_at: "2026-11-17T11:09:12+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-17"
pub_day: "2026-11-16"
tags:
  - 语料
  - hn_show
  - author_wanderingstan
  - story_50522602
  - show_hn
metrics: {"points": 3, "comments": 1, "engagement_velocity": 3}
comments_count: 1
comments_total: 1
discovered_via: "hn:show_hn:3d"
---

# Show HN: My OSS Claude Meetings alternative that works with any agent or call

> [!info] 一句话导读
> Since February, I've been developing an agent-in-calls solution with a friend. With the announcement of Claude Meetings last week, it's now time to announce Vib…

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50522602>
> 指标：点赞=3 · 评论=1 · engagement_velocity=3
> 作者：wanderingstan　|　发布：2026-11-16T20:18:57Z
> 项目链接：<https://github.com/wanderingstan/vibeconf-app>
> 采集：2026-11-17T11:09:12+08:00　|　id：`ce96a3517381f7fe`

## 正文

Since February, I've been developing an agent-in-calls solution with a friend. With the announcement of Claude Meetings last week, it's now time to announce Vibeconferencing: an open-source project with even more functionality, support for any agent (Codex, Muse, local ollama, etc), and support for more calling platforms: Google Meet, Zoom, MS Teams, WhatsApp, Telegram, and phone calls (via Twilio).Architecture diagram: https://raw.githubusercontent.com/wanderingstan/vibeconf-app...The premise is simple: give your normal agent session the tools it needs to operate all major calling platforms, and teach it basic etiquette of how to behave in a call with others. A simple `/join-call` and boom! your session is talking to you in the call. Anything your agent can do in chat, it can do on the call. The agent is bridged to the calling platforms via a cross-platform electron app. (The raw guts of interacting with calling platforms is abstracted as the npm library `@vibeconferencing/calls`, if you'd rather roll your own.)Everything runs locally and uses your own local agent. (Tho the optional shared whiteboard feature does require being logged in on our server.) It runs on MacOS, Windows, and Linux. (Windows version is not well tested.)Speech generation is done either by Elevenlabs or the OSS Voicebox, with a fallback to the OS's default app (e.g. `say` on MacOS). Voicebox: https://github.com/jamiepine/voiceboxSpeech recognition is done either by the calling platforms' own captioning services (Meet, Zoom, Teams), or with Whistle for those without captioning (WhatsApp, Telegram, Twilio). Whistle: https://cactuscompute.com/blog/whistleThe etiquette was the most fun to code, although done with the knowledge that it's a temporary fix until true interactive voice models are merged with the power of frontier text chat models. We have experimental support for the OpenAI realtime API, but it seems to have been trained as a customer support agent, so it's hard to keep it from dominating multi-person conversations!Highlights from the last nine months of dogfooding and early users:- A WhatsApp bot for my father, an elderly WW2 veteran, that has access to the 20,000 photos he scanned. He can call it to see and hear about any aspect of his life. https://youtu.be/Rs-Z1YeLt98- Collaboratively built a website for a friend's non-profit, with her amazed that she could ask for site changes and see the site change in realtime. https://drive.google.com/file/d/1iSRgY8JGJ0liOzHMl2bOGNd9jwq...- My friend Matt is currently road-tripping across the US, talking with his Codex sessions to develop his Golf app. https://youtu.be/a3uNUdIwqVY- Our friend Bethany uses her bot "Taylor Script", in calls and classrooms with coding students to act as the super-smart TA who can answer technical questions, and monitors student progress. https://youtu.be/c8mZKkcxhJo- I begin most days with a check-in call with my bot Jimmy, where we discuss open repo issues while I have breakfast. https://youtu.be/2uQIR83LwY0 (Apologies for eating with my mouth open...)- In a standup, Seth's bot created a video ad for the service itself, within a call. https://x.com/vibeconf/status/2104427917816234257?s=20Security: There is nothing built in, so only use this on calls with people that you trust. However, I've been amazed at how injection-resistant it has appeared to be on it's own; e.g. my agent asking consent from me before doing things asked by others on the call.Overall, this was a "time machine" experiment (to borrow my old Reality Labs' Research terminology) to experience agents-in-calls before it was purpose built. Claude Meetings just showed that we were thinking in the right direction, and I'm excited to see where this goes!This is a small experimental project built by two friends, so it is rough around the edges, and we'd love feedback and pull requests.

## 评论（1/1）

> **wanderingstan** · 2026-11-16T20:25:39.000Z　
> OP here. It was bittersweet to be effectively sherlocked by Anthropic last week...but also an honor! This really does feel like l"iving in the future". Happy to answer any questions, help get through rough patches of installation, or give demo calls.

## 关联链接

- https://cactuscompute.com/blog/whistleThe
- https://drive.google.com/file/d/1iSRgY8JGJ0liOzHMl2bOGNd9jwq...-
- https://github.com/jamiepine/voiceboxSpeech
- https://raw.githubusercontent.com/wanderingstan/vibeconf-app...The
- https://x.com/vibeconf/status/2104427917816234257?s=20Security:
- https://youtu.be/2uQIR83LwY0
- https://youtu.be/Rs-Z1YeLt98-
- https://youtu.be/a3uNUdIwqVY-
- https://youtu.be/c8mZKkcxhJo-

## 导航

- 项目页：[[10-项目/github.com_693731c5]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
