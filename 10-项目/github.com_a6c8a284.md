---
type: "project"
title: "[开源分享] MemDock： Claude Code 和 Codex 的双助手工作台，支持会话互转、记忆和 Skills 管理"
project_url: "https://github.com/LingyiChen-AI/MemDock"
first_seen: "2026-11-10T09:55:59+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 300
lang: "zh"
---

# [开源分享] MemDock： Claude Code 和 Codex 的双助手工作台，支持会话互转、记忆和 Skills 管理

> [!info] 一句话导读
> MemDock：管好 AI 编程记忆和 Skill

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/LingyiChen-AI/MemDock>
> 首次收录：2026-11-10T09:55:59+08:00
> 来源渠道：V2EX
> 标签：300
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-10T09:55:59+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-10/0fd87f369c707328_开源分享-MemDock-Claude-Code-和-Codex-的双助手工作台,支持会话互转、记忆]] |

## 摘要正文

# MemDock：管好 AI 编程记忆和 Skill  用 Claude Code 和 Codex 久了，我常遇到两件事。测试命令早就换了，新会话还在按旧规则跑。想更新一个 Skill ，又要先翻目录，确认当初装在了哪个工具里。我做了 **MemDock**，把这些散在不同地方的记忆和 Skill 放到一个桌面工作台里。  ![在记忆总览里编辑和预览项目规则]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-cover.png)  ## 规则散在哪，先找得着  在「记忆总览」里，可以按全局或项目搜索 `CLAUDE.md`、`AGENTS.md` 和 Claude Code 的自动记忆，也能浏览只读的 Codex 记忆库。规则文件支持分栏编辑和版本回滚。想知道一条规则从哪来，可以在项目记忆图谱中查看关联并跳回来源。  ## 每周翻一遍，有依据再更新  比如项目已经换了测试命令，你在对话里纠正过助手，规则文件却还写着旧命令。**可以设成每周提取一次**，让 MemDock 从近期对话里找出值得补充的经验和需要修订的规则。也可以每天定时提取，或者手动运行。  ![设置记忆提取的频率、项目范围和回看天数]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-memory-extraction.png)  提取结果先进入「待审核记忆」。你可以对照旧内容、新建议和原对话，再决定采纳、改完再采纳，或者驳回。采纳后才写回文件。  ![审核记忆更新建议，查看差异和对话依据]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-memory-review.png)  ## 我到底装了哪些 Skill ？  「 Skill 管理」会列出 Claude Code 和 Codex 已装的 Skill ，区分全局和项目范围，也能看来源和文件。Superpowers 这类插件会按包展示。可以从 GitHub 、本地目录或 ZIP 安装，在两个工具之间复制，也可以检查更新、批量更新或从备份恢复。  ![查看已装 Skill 的来源和文件]( https://cdn.jsdelivr.net/gh/LingyiChen-AI/images@main/MemDock/images/2026/11/20261108-74a20e-skill…
