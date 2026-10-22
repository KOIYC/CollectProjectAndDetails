---
type: "corpus"
item_id: "40ffd3d13b20a818"
title: "开源自用的多 Agent 桌面工作台， Agent 放一起管，订阅额度一点不浪费"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1250538"
project_url: "https://github.com/flyhero/antumi"
author: "iflyapi"
published_at: "2026-10-21T02:49:58"
captured_at: "2026-10-22T09:49:30+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 开源自用的多 Agent 桌面工作台， Agent 放一起管，订阅额度一点不浪费

> [!info] 一句话导读
> 用 Claude Code 和 Codex 写代码大半年了，后来又加了 Cursor 的 CLI ，桌面上常开着四五个终端。攒下来的烦恼大概是这些：

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1250538>
> 指标：回复=0
> 作者：iflyapi　|　发布：2026-10-21T02:49:58
> 项目链接：<https://github.com/flyhero/antumi>
> 采集：2026-10-22T09:49:30+08:00　|　id：`40ffd3d13b20a818`

## 正文

用 Claude Code 和 Codex 写代码大半年了，后来又加了 Cursor 的 CLI ，桌面上常开着四五个终端。攒下来的烦恼大概是这些：

- Claude 的 5 小时额度用完，换 Codex 接着做，得把前因后果重新讲一遍
- 某个 Agent 早就停下来等我批准了，我在另一个窗口里完全没注意到
- 它在回复里说「上线前记得把 xx 配上」，第二天我就忘了
- 周额度明天就重置、还剩一大半，我却一直舍不得用 Opus
- 每次模型总返回英语，还得发送一次转中文，白白浪费贵的模型 Token
- 想要白天规划任务，晚上自动执行，次日验收成果

后来干脆给自己写了个桌面端来管它们，叫 **Antumi**（安图米）。自己用了一段时间，觉得别人可能也用得上，就整理了一下开源出来。

![任务看板](  )

先说清楚它不是什么：它不是一个新 Agent ，也不代理任何 API 。它驱动的是你电脑上已经装好、登录好的 `claude`、`codex`、`cursor-agent`，额度走你自己的订阅。不用注册账号，不用填 key ，数据全在本机。

## 跟多开几个终端比

| | 多开终端 | Antumi |
|---|---|---|
| 换个 Agent 接着做 | 复制粘贴上下文，再解释一遍 | 输入框里换个 Agent ，聊天记录和工作目录一起交过去 |
| 谁在等我 | 挨个窗口切过去看 | 「总览」汇总等批准、等回答、待验收的，窗口不在前台时发系统通知 |
| 额度还剩多少 | 各家分别去查 | 底部状态栏三家并排，悬停看重置时间 |
| Agent 交代你之后要做的事 | 埋在聊天记录里 | 自动记成待办，可以逐项勾掉 |

## 几个我每天都在用的功能

### 移交：额度用完换个 Agent 接着干

点输入框左下角的 Agent 名字，换一个，补一句说明就行。新 Agent 会收到之前能看到的聊天记录，在同一个目录里继续。切回原来的 Agent 时，会恢复它自己的原生会话，并补上中间那段记录。

![移交]( https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/handoff.webp)

### 额度一眼看清，还会提醒你「该花了」

状态栏同时显示 Claude Code 、Codex 和 Cursor 的用量。它会按每个窗口的重置时间算节奏：周额度快重置了还剩很多，就提醒你放心用 Opus ；照现在的速度会提前用完，就建议换个模型，或者把轻活交给另一个 Agent 。

这个功能是我自己最离不开的，以前每周都在浪费额度。

![额度]( https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/quota.webp)

### 分屏：两个 Agent 并排

⌘ 点另一个会话就并排打开，一边让 Claude 写实现，一边让 Codex 看方案，两边各自输入、各自批准。

![分屏]( https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/split.webp)

### 群聊：让几个 Agent 先吵一架

拉 2–5 个 Agent 进同一个对话，先各自独立回答，再互相回应。你随时可以插话、 @ 某个成员追问，最后由主持人总结共识和分歧。群聊全程只读，不会改代码。我做技术选型、或者想听听不同模型对一段设计的意见时会用。

![群聊]( https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/discussion.webp)

### 任务看板和验收

任务从「未执行」到「已完成」。开始执行时自动建 worktree 和分支，Agent 先在规划模式里读代码、拿出计划，你点头了它才开始改。做完后看整条分支的 diff ，跑项目检查，再选接受、接着改或者重做。任务之间可以设依赖，前一个验收通过，后一个才解锁，而且能接着前一个任务的分支往下做。

worktree 永远不会被自动删除：里面可能有 Agent 唯一一份成果。只有你确认清理、并且它确实没有未提交改动或独有提交时才会删。

![总览](  )

### 待办

Agent 在回复里提到要你之后去做的事，比如上线前要配的环境变量、要你手动验证的页面，会记成这条会话的待办。「总览」里能看到所有会话的待办，标着「 Agent 可做」的还能一键交回给它。

![待办]( https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/todos.webp)

其他的就简单列一下：选中一段内容「交给小助手」用轻量模型单独解释、英文回复一键翻译、研发小队（队长 + 开发 + 评审分别配 Agent 和模型）、定时任务和消息预约（可以预约到「额度恢复后」）、内置终端和浏览器（ Agent 能自己打开页面验证）、接入 Jira / GitHub / Obsidian 当任务来源、管理 Skills 和 MCP 。

> 更多小功能就不在这里介绍了

## 支持的 Agent

| Agent | 接入方式 | 计划审批 | 移交 | 定时 / 预约 |
|---|---|:-:|:-:|:-:|
| Claude Code | `claude -p`（ stream-json ） | ✓ | ✓ | ✓ |
| Codex | `codex app-server` | ✓ | ✓ | ✓ |
| Cursor | `cursor-agent acp` | ✓ | ✓ | — |
| OpenCode | 接入中 | - | - | — |
| Pi | 接入中 | - | - | — |

三家都是走官方的结构化接口，不抓 TUI 输出。权限模式和各自 CLI 的一致，「全部放行」不会默认选中。


## 现状和坑

- 还是开发者预览版（ 0.19.x ），我一个人在做，更新比较勤，最近一天能发好几个版本
- 主要在 macOS （ Apple Silicon ）上开发和测试。Windows 能装能跑，Releases 里也有安装包，但实机验证不多，遇到问题欢迎提 issue
- dmg 没做 Apple 公证，拖进「应用程序」后要执行一次 `xattr -dr com.apple.quarantine /Applications/Antumi.app`，或者去「隐私与安全性」里点「仍要打开」

## 地址

GitHub： https://github.com/flyhero/antumi

下载： https://github.com/flyhero/antumi/releases （ macOS arm64 的 dmg ，Windows x64 的 exe ）

也可以从源码跑：`pnpm install && pnpm dev`，需要 Node ≥ 22.13 。

名字来自 ant （蚂蚁）：一只蚂蚁很小，一群能搬大东西。图标上是一只抱着三块积木的小蚂蚁。

想接哪个 Agent （比如 Gemini CLI ）、哪里用着别扭，回帖或者提 issue 都行，我会一个个看。觉得有用的话，给个 star 我会很开心。

## 关联链接

- https://github.com/flyhero/antumi/releases
- https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/discussion.webp
- https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/handoff.webp
- https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/quota.webp
- https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/split.webp
- https://raw.githubusercontent.com/flyhero/antumi/v0.19.3/docs/assets/features/todos.webp

## 导航

- 项目页：[[10-项目/github.com_21d10bb7]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
