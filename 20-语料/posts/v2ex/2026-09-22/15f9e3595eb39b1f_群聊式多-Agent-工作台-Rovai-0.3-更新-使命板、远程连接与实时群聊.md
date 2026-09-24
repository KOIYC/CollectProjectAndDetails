---
type: "corpus"
item_id: "15f9e3595eb39b1f"
title: "群聊式多 Agent 工作台 | Rovai 0.3 更新：使命板、远程连接与实时群聊"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1243553"
project_url: "https://github.com/murray17/rovai-ai"
author: "RMurray"
published_at: "2026-09-21T02:27:03"
captured_at: "2026-09-22T12:57:40+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-22"
pub_day: "2026-09-21"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 群聊式多 Agent 工作台 | Rovai 0.3 更新：使命板、远程连接与实时群聊

> [!info] 一句话导读
> 朋友们，憋了两个星期，继续更新一下 Rovai ，这次是 V0.3 大版本。这次主要加了使命板和远程连接；也改了群聊的执行方式，实现真正的实时群聊，同一个群聊中 ClaudeCode 正忙时，可以实时找 Codex 或者 PI 、Deepseek Harness 推进其他任务。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1243553>
> 指标：回复=0
> 作者：RMurray　|　发布：2026-09-21T02:27:03
> 项目链接：<https://github.com/murray17/rovai-ai>
> 采集：2026-09-22T12:57:40+08:00　|　id：`15f9e3595eb39b1f`

## 正文

朋友们，憋了两个星期，继续更新一下 Rovai ，这次是 V0.3 大版本。这次主要加了使命板和远程连接；也改了群聊的执行方式，实现真正的实时群聊，同一个群聊中 ClaudeCode 正忙时，可以实时找 Codex 或者 PI 、Deepseek Harness 推进其他任务。

从七月中旬折腾到现在，前前后后大概烧了 340 亿 token ，只能说在 UI 上和 gpt 互相折磨了很久（ Astra 来了之后还不错）。

https://github.com/murray17/rovai-ai

## 使命板 ##
> 创建一个使命，写清要做什么，选好项目和队员，然后静静等待队员们交付任务。Git 项目的使命会准备独立 Worktree ，适用场景就是多分支并行开发。

![使命板 3](  )

![使命会话](  )

## 远程连接 ##
> 电脑上运行 Rovai 后，可以直接从手机、平板或另一台电脑的浏览器继续访问；除了 Desktop 版可以开启远程访问外，纯 Server 也在当前版本支持了。
远程方案参考： https://github.com/murray17/rovai-ai/blob/main/docs/guides/server-access.md ；建议走 Tailscale 或 HTTPS ，不直接暴露 HTTP 端口。

### 手机远程访问

| **会话区** | **执行区** |
| --- | --- |
| ![mobileUI 会话区](  ) | ![mobileui 执行区](  ) |

| **会话列表** | **定时任务** | **队友** | **记忆** |
| --- | --- | --- | --- |
| ![mobileUI 会话列表](  ) | ![mobileUI 定时任务](  ) | ![mobileUI 队友](  ) | ![mobileUI 记忆](  ) |

### PC 远程访问

![webUI](  )

## 实时群聊

找奥黛丽的同时，爱丽丝也能受理需求，不需要像之前一样所有队员共用一个轮次。

![消息重构](  )

**当然，群聊的核心机制 A2A 是必不可少的。**

![A2A](  )

### 支持设置个人资料 ##

![队员界面个人资料](  )

## 支持 Linux 部署 ##

> Rovai 现在也可以以纯 Server 的方式运行在 Linux 机器上，不需要桌面环境。项目文件、Harness 和执行文件存储在服务器，电脑、平板或手机通过浏览器远程访问。

构建基线: **Ubuntu 22.04 / Debian 12 / Ubuntu 24.04**，glibc 2.35 。

![Linux 部署](  )

> 历史版本
>
> [ [开源]  Rovai AI 多 Agent 工作台｜组建一支长期协作的 Agent 队伍]( https://v2ex.com/t/1238939)
>
> [ [开源]  Rovai AI 0.2.0：在智能体群聊中新增单聊]( https://v2ex.com/t/1240317)

最后欢迎大佬们提 PR / Issue ，也欢迎顺手点个 Star 。

## 关联链接

- https://github.com/murray17/rovai-ai/blob/main/docs/guides/server-access.md
- https://v2ex.com/t/1238939
- https://v2ex.com/t/1240317

## 导航

- 项目页：[[10-项目/github.com_e03a67dc]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
