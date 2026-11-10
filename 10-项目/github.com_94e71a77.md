---
type: "project"
title: "Show HN: Vork – headless 3D and VFX engine for agents"
project_url: "https://github.com/voyager-so/vork"
first_seen: "2026-11-10T09:49:42+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_raviparikh
  - story_50432998
  - show_hn
lang: "en"
---

# Show HN: Vork – headless 3D and VFX engine for agents

> [!info] 一句话导读
> I made an agent-native 3d/vfx engine.Agents are good at making interesting scenes in Blender/Unreal/Nuke/etc. But these tools are fundamentally limited compared…

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/voyager-so/vork>
> 首次收录：2026-11-10T09:49:42+08:00
> 来源渠道：HN Show HN
> 标签：author_raviparikh, story_50432998, show_hn
> 最新指标：点赞=5 · 评论=2 · engagement_velocity=5

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:49:42+08:00 | HN Show HN | 点赞=5 · 评论=2 · engagement_velocity=5 | [[20-语料/posts/hn_show/2026-11-10/3511ef1a4690d9ce_Show-HN-Vork-–-headless-3D-and-VFX-engine-for-agen]] |

## 摘要正文

I made an agent-native 3d/vfx engine.Agents are good at making interesting scenes in Blender/Unreal/Nuke/etc. But these tools are fundamentally limited compared to what coding agents are capable of. Many simplifying assumptions are baked into these tools in order to fit human authoring methods.In vork, agents write the whole scene as code, including their own shaders, materials, cameras and physics, and vork renders it on the GPU. The core API fits in about 2,500 tokens.So, for example, almost every 3d engine assumes light moves in a straight line. Light near a black hole does not; so the best you can do in e.g. Blender is faking gravitational lensing. In vork, you can model it for real.If you want a camera lens that simulates a dragonfly's eye, or realistically-modeled Fata Morgana, this is also possible in vork.
