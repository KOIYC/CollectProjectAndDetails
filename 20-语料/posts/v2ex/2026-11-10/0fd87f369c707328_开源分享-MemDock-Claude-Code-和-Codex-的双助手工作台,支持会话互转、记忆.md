---
type: "corpus"
item_id: "0fd87f369c707328"
title: "[开源分享] MemDock： Claude Code 和 Codex 的双助手工作台，支持会话互转、记忆和 Skills 管理"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1255502"
project_url: "https://github.com/LingyiChen-AI/MemDock"
author: "chturing184"
published_at: "2026-11-09T03:07:22"
captured_at: "2026-11-10T09:55:59+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - v2ex
  - 300
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [开源分享] MemDock： Claude Code 和 Codex 的双助手工作台，支持会话互转、记忆和 Skills 管理

> [!info] 一句话导读
> MemDock：管好 AI 编程记忆和 Skill

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1255502>
> 指标：回复=0
> 作者：chturing184　|　发布：2026-11-09T03:07:22
> 项目链接：<https://github.com/LingyiChen-AI/MemDock>
> 采集：2026-11-10T09:55:59+08:00　|　id：`0fd87f369c707328`

## 正文

# MemDock：管好 AI 编程记忆和 Skill

用 Claude Code 和 Codex 久了，我常遇到两件事。测试命令早就换了，新会话还在按旧规则跑。想更新一个 Skill ，又要先翻目录，确认当初装在了哪个工具里。我做了 **MemDock**，把这些散在不同地方的记忆和 Skill 放到一个桌面工作台里。

![在记忆总览里编辑和预览项目规则]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-cover.png)

## 规则散在哪，先找得着

在「记忆总览」里，可以按全局或项目搜索 `CLAUDE.md`、`AGENTS.md` 和 Claude Code 的自动记忆，也能浏览只读的 Codex 记忆库。规则文件支持分栏编辑和版本回滚。想知道一条规则从哪来，可以在项目记忆图谱中查看关联并跳回来源。

## 每周翻一遍，有依据再更新

比如项目已经换了测试命令，你在对话里纠正过助手，规则文件却还写着旧命令。**可以设成每周提取一次**，让 MemDock 从近期对话里找出值得补充的经验和需要修订的规则。也可以每天定时提取，或者手动运行。

![设置记忆提取的频率、项目范围和回看天数]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-memory-extraction.png)

提取结果先进入「待审核记忆」。你可以对照旧内容、新建议和原对话，再决定采纳、改完再采纳，或者驳回。采纳后才写回文件。

![审核记忆更新建议，查看差异和对话依据]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-memory-review.png)

## 我到底装了哪些 Skill ？

「 Skill 管理」会列出 Claude Code 和 Codex 已装的 Skill ，区分全局和项目范围，也能看来源和文件。Superpowers 这类插件会按包展示。可以从 GitHub 、本地目录或 ZIP 安装，在两个工具之间复制，也可以检查更新、批量更新或从备份恢复。

![查看已装 Skill 的来源和文件]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-skills.png)

## 换台电脑，规则和清单一起带走

旧电脑可以把记忆和 Skill 安装清单同步到自己的 GitHub 私有仓库。新电脑登录同一个账号，从同一个仓库拉取记忆，再按清单补装缺少的 Skill 。有冲突时可以逐块处理，外观和记忆提取等偏好也能单独恢复。

![新电脑检测到云端已有记忆，可以一键同步]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-sync.png)

## 平时写代码，还能用到这些

- **对话和终端**。按项目查看两边的历史会话，支持 Claude Code 与 Codex 双向转换。可以切换图形聊天和原生命令行，也可以开独立的分屏终端。

  ![转换会话后，可用目标工具的恢复命令继续]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-session-conversion.png)

  ![左边继续对话，右边开终端跑测试]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-terminal.png)

- **代码和并行开发**。在对话旁搜索、编辑文件和查看 Git 差异。多条任务可以各开一个 Git Worktree ，分别开发，做完再合并。

  ![在对话旁打开文件树和代码编辑器]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-project-chat.png)

- **用量和额度**。查看两个工具的 Token 、估算费用和活跃热力图，支持导出 CSV ，也可以选择开启实时额度查询。

  ![查看 Token 用量、额度和每日活跃热力图]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-usage.png)

- **飞书连接**。用自建机器人在飞书里调用本机助手，按项目和使用者控制访问权限。

  ![在飞书连接中配置机器人和项目权限]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-feishu.png)

- **桌面设置**。检测或安装助手 CLI ，设置语言、主题和开机自启，安装版支持自动检查更新。

MemDock 支持 macOS 和 Windows 。可以先打开一个常用项目，看看有哪些规则还在用、哪些 Skill 已经装了。

项目地址  
https://github.com/LingyiChen-AI/MemDock

## 关联链接

- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-cover.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-feishu.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-memory-extraction.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-memory-review.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-project-chat.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-session-conversion.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-skills.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-sync.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-terminal.png
- https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-usage.png

## 导航

- 项目页：[[10-项目/github.com_a6c8a284]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
