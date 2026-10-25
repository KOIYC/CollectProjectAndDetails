---
type: "project"
title: "高强度 AI Coding 后，我给自己做了个 ADE App 来解决碰到的痛点"
project_url: "https://github.com/user-attachments/assets/1482f20b-31ea-4d82-8e8c-acd63e500cad"
first_seen: "2026-10-25T23:34:58+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 1203
lang: "zh"
---

# 高强度 AI Coding 后，我给自己做了个 ADE App 来解决碰到的痛点

> [!info] 一句话导读
> LLM 时代高强度用 AI Agent 搞项目，LLM 很强，但想要高效舒服的开发还是有很多繁琐的流程。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/user-attachments/assets/1482f20b-31ea-4d82-8e8c-acd63e500cad>
> 首次收录：2026-10-25T23:34:58+08:00
> 来源渠道：V2EX
> 标签：1203
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-25T23:34:58+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-25/0f41a10c24d3647b_高强度-AI-Coding-后,我给自己做了个-ADE-App-来解决碰到的痛点]] |

## 摘要正文

LLM 时代高强度用 AI Agent 搞项目，LLM 很强，但想要高效舒服的开发还是有很多繁琐的流程。  例如经常同时推进几个任务，还涉及前后端两个 repo ，并行任务不相互冲突大家都知道用 git worktree 。  手敲 git worktree 命令很繁琐，AI 可以代劳，但每次都要交代一遍却挺烦：从哪个分支创建，前后端项目在哪个目录，做完合回哪里。想去对应目录跑条命令，还得找路径、开终端、切过去。任务一多，就容易忘记哪个目录对应哪件事。  我就在想能不能把常用流程做到一个 ui 界面中管理，于是做了一个 APP 叫 Treefold 。我想把每项任务的代码、终端和进度放在一起，打开就知道做到哪了，接下来可以继续做什么。  ## 任务展开以后，要知道怎么收回来  我把工作分成三层：Project 、Workspace 、Fork 。  Project 放一个项目相关的仓库和目录。我一般让原仓库保持在 main 分支，再为每项 feature 创建 Workspace ，各自使用独立分支和 worktree 。创建时默认从原仓库当前分支展开，也可以选择其他本地或远端分支作为起点。  一个 feature 里有可以并行的子任务，就继续创建 Fork 。比如做“商品搜索”，可以让几个 Fork 分别负责接口、页面和测试，各自在独立目录里修改，完成后合回父 Workspace ，再一起联调和交付。  这样，worktree 就有了明确的父子关系，交付时知道应该合回哪里。操作由人确认，发生冲突仍然需要处理。Workspace 还可以选择推送 feature 分支，接着走原来的远端评审流程。  简单任务开一个 Workspace 就够了，不用每次都拆 Fork 。同一 Workspace 里的多个 Session 共享代码目录；需要隔离修改时，再创建 Fork 。  ## worktree 多了，目录和状态都得看得清  `git worktree list` 能列出目录和分支，但想知道里面是否有未提交的修改、改动是否已经合回去，还得逐个检查。任务多了，这些小操作也会打断思路。  Treefold 把 worktree list 做成了界面里的管理列表，按仓库展开。每个 worktree 的分支、路径、当前提交和关联任务放在一起，同时显示未提交改动、冲突，以及相对目标分支领先或落后的提交数。已经合入目标分支的状态也会标出来，不用挨个进入目录查 Git 。  ![worktree 管理列表：查看分支、目录、任务归属、未提交改动和领先／落后状态]( https://github.com/user-attachments/assets/f15239f8-c0b2-482c-9e4a-4749e5ce6f26) …
