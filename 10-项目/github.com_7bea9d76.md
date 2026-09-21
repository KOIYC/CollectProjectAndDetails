---
type: "project"
title: "Show HN: Bailout – The coding agent meant to be deleted"
project_url: "https://github.com/storozhenko98/bailout"
first_seen: "2026-09-21T09:44:03+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_mst98
  - story_49778390
  - show_hn
lang: "en"
---

# Show HN: Bailout – The coding agent meant to be deleted

> [!info] 一句话导读
> hey hn,i made bailout for a pretty specific problem. you boot a fresh vm and want an agent to help get it set up, except you dont have your agent set up yet. no…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/storozhenko98/bailout>
> 首次收录：2026-09-21T09:44:03+08:00
> 来源渠道：HN Show HN
> 标签：author_mst98, story_49778390, show_hn
> 最新指标：点赞=2 · 评论=3 · engagement_velocity=2

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-21T09:44:03+08:00 | HN Show HN | 点赞=2 · 评论=3 · engagement_velocity=2 | [[20-语料/posts/hn_show/2026-09-21/870a9cee0fffc076_Show-HN-Bailout-–-The-coding-agent-meant-to-be-del]] |

## 摘要正文

hey hn,i made bailout for a pretty specific problem. you boot a fresh vm and want an agent to help get it set up, except you dont have your agent set up yet. no gh, no config, no api key handy. might not even have codex / claude code / opencode curled and loaded. or you already have a setup but opencode / pi / whatever stopped launching, and the thing you'd normally ask to fix it is the thing that's broken.for me, and this is embarrassing, but at work we switched from per-dev keys to oai / ant to just an internal litellm router, which required configuring opencode. i use opencode2 which can dynamically reload its config. well, while rewriting the config to work with self hosted litellm, it broke, and i was stranded w/ no coding agent. bailout is for that sort of thing, like break glass, agent pls fix.think of bailout like a spare agent for these sorts of things. install it, ask it to set up the machine or fix your usual tools, then remove it. the idea is “the harness meant to be deleted.” i like having a tool whose last useful action can be uninstalling itself. plus a play on hinge, the whole app meant to be deleted.you install it with `curl -fsSL https://bailout.dev/install.sh | b…
