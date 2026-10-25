---
type: "corpus"
item_id: "0f41a10c24d3647b"
title: "高强度 AI Coding 后，我给自己做了个 ADE App 来解决碰到的痛点"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1250974"
project_url: "https://github.com/user-attachments/assets/1482f20b-31ea-4d82-8e8c-acd63e500cad"
author: "F555"
published_at: "2026-10-22T08:10:48"
captured_at: "2026-10-25T23:34:58+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-25"
pub_day: "2026-10-22"
tags:
  - 语料
  - v2ex
  - 1203
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 高强度 AI Coding 后，我给自己做了个 ADE App 来解决碰到的痛点

> [!info] 一句话导读
> LLM 时代高强度用 AI Agent 搞项目，LLM 很强，但想要高效舒服的开发还是有很多繁琐的流程。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1250974>
> 指标：回复=0
> 作者：F555　|　发布：2026-10-22T08:10:48
> 项目链接：<https://github.com/user-attachments/assets/1482f20b-31ea-4d82-8e8c-acd63e500cad>
> 采集：2026-10-25T23:34:58+08:00　|　id：`0f41a10c24d3647b`

## 正文

LLM 时代高强度用 AI Agent 搞项目，LLM 很强，但想要高效舒服的开发还是有很多繁琐的流程。

例如经常同时推进几个任务，还涉及前后端两个 repo ，并行任务不相互冲突大家都知道用 git worktree 。

手敲 git worktree 命令很繁琐，AI 可以代劳，但每次都要交代一遍却挺烦：从哪个分支创建，前后端项目在哪个目录，做完合回哪里。想去对应目录跑条命令，还得找路径、开终端、切过去。任务一多，就容易忘记哪个目录对应哪件事。

我就在想能不能把常用流程做到一个 ui 界面中管理，于是做了一个 APP 叫 Treefold 。我想把每项任务的代码、终端和进度放在一起，打开就知道做到哪了，接下来可以继续做什么。

## 任务展开以后，要知道怎么收回来

我把工作分成三层：Project 、Workspace 、Fork 。

Project 放一个项目相关的仓库和目录。我一般让原仓库保持在 main 分支，再为每项 feature 创建 Workspace ，各自使用独立分支和 worktree 。创建时默认从原仓库当前分支展开，也可以选择其他本地或远端分支作为起点。

一个 feature 里有可以并行的子任务，就继续创建 Fork 。比如做“商品搜索”，可以让几个 Fork 分别负责接口、页面和测试，各自在独立目录里修改，完成后合回父 Workspace ，再一起联调和交付。

这样，worktree 就有了明确的父子关系，交付时知道应该合回哪里。操作由人确认，发生冲突仍然需要处理。Workspace 还可以选择推送 feature 分支，接着走原来的远端评审流程。

简单任务开一个 Workspace 就够了，不用每次都拆 Fork 。同一 Workspace 里的多个 Session 共享代码目录；需要隔离修改时，再创建 Fork 。

## worktree 多了，目录和状态都得看得清

`git worktree list` 能列出目录和分支，但想知道里面是否有未提交的修改、改动是否已经合回去，还得逐个检查。任务多了，这些小操作也会打断思路。

Treefold 把 worktree list 做成了界面里的管理列表，按仓库展开。每个 worktree 的分支、路径、当前提交和关联任务放在一起，同时显示未提交改动、冲突，以及相对目标分支领先或落后的提交数。已经合入目标分支的状态也会标出来，不用挨个进入目录查 Git 。

![worktree 管理列表：查看分支、目录、任务归属、未提交改动和领先／落后状态]( https://github.com/user-attachments/assets/f15239f8-c0b2-482c-9e4a-4749e5ce6f26)

从列表可以直接打开关联任务；不再使用的 worktree ，可以在界面里确认后删除，也能清理失效的 worktree 记录。哪些还在开发、哪些改动已经合入、哪些目录可以收拾，都有地方查看。

完成的任务可以归档，先保留分支、worktree 和工作记录，之后再按需清理。Project 里可以批量清理已归档的 Workspace ，Workspace 里也能清理已归档的 Fork 。隔天回来看时，活跃任务和已完成的工作分开，也能找到之前的交付记录。

创建 worktree 、启动 Session 和批量清理都可以在后台继续，不用一直守着弹窗。切去做其他任务后，也能回来查看状态和失败原因。

## Agent 写完，检查代码和提交

我一直挺喜欢 JetBrains 的 Git 集成：修改在哪里，提交了什么，都可以直接看。

Treefold 里也放了 Git Changes 和 History 。开发过程中看 diff ，交付前检查提交；几个零散提交可以用 Squash 整理成一个，也可以 Reset 到指定提交。当前分支最新一次提交的说明写得不合适，也可以直接在 History 里修改。如果本地记录显示它被远端分支、标签或其他分支引用，会先提醒，再由我决定是否继续。

![查看 Git Changes 、提交历史和常用 Git 操作]( https://github.com/user-attachments/assets/4e7cf442-4375-42ed-8901-62331cf8020b)

完成交付时，可以选择 Squash ，把这项工作的成果合成一个提交放进父分支。前后端改动不一样，就分别填写提交说明，在同一个弹窗里检查后一起确认。源分支上的开发记录仍然保留，父分支收到的是整理后的提交。

![Squash 交付：为前端和后端分别填写提交说明]( https://github.com/user-attachments/assets/c533f978-9d84-4834-8916-fe651d601c85)

我没有做完整的交互式 rebase 和冲突编辑器。常用操作放在界面里，更复杂的 Git 操作继续交给终端和 Agent ，处理完再回来检查结果。

Project 里也能直接查看和搜索本地、远端分支，切换分支，或者删除不再需要的分支。这些短操作，不用每次都通过聊天交给 Agent 。

检查代码时，也不想每次都重新告诉 Agent：“这是哪几个仓库，应该和哪个分支比较，别漏掉还没提交的修改。”所以加了 AI Review：在 Workspace 或 Fork 里选一个 Agent ，确认提示词，就会打开一个专门检查这项工作的 Session 。

Fork 和父 Workspace 比较，Workspace 和 Project 当前分支比较。Treefold 会把各仓库的路径、分支和比较范围交给 Agent ，要求同时检查已提交、未提交的修改和新文件。默认提示词让它先报告问题，我确认后，可以在同一个 Session 里继续讨论、修复和验证。也可以给 Project 保存自己的 Review 提示词。

这样，从开发、检查到修复都留在同一项任务里，最后再决定怎么交付。完成交付前，如果还有将被停止的 Session 在运行，界面会先列出来，让我选择暂缓交付，或者确认停止后继续。这里检查的是进程是否还活着，不能替我判断 Agent 是否已经做完。

![AI Review：编辑提示词，选择 Agent 和工作目录]( https://github.com/user-attachments/assets/be50aea7-79c7-45ff-b89b-18baf05f72f4)

## 暂缓的任务，先记在 Todo 里

和 AI 讨论方案时，经常会冒出一些现在不做、以后值得试的点子。以前我会开个文件记 Todo ，接下来还得记得这个文件放在哪。

现在可以直接记到 Workspace 的 Todo list 。要做的时候，把 Todo 分配给 Fork ，展开成一项独立工作；完成并合回父 Workspace 后，关联的 Todo 也会完成。

![Workspace 中的 Todo 、Fork 和 Session]( https://github.com/user-attachments/assets/5daeff35-b6cb-4c05-ba3f-aeff03e02318)

Treefold 也带了 CLI 和 Skill ，Agent 能读取、添加和修改 Todo ，遇到问题时也能记录阻塞原因。换一个 Session 接着做，代码、Todo 和交付记录都还留在 Workspace 里，不用依赖某一次聊天记住所有事情。

比如接口开发时发现一个值得单独处理的问题，可以先留下 Todo ，继续完成手头的工作。等有空了再把它分出去，也不用为了保留这个点子一直开着原来的 Session 。

## Agent 把服务跑起来了，我却看不到它在干什么

调试的时候，我经常要让 Agent 启动前后端服务。以前它通常在自己的会话后台启动，再告诉我“服务已经起来了”。我只知道启动了，眼前却没有一个能持续看日志的终端。想知道请求有没有进来、服务有没有报错，还得让它再查一遍。

两个 Agent 并行工作时更麻烦：各自的会话没有共享的进程列表，不知道对方已经启动了什么。一个刚把服务跑起来，另一个又启动一遍，端口就冲突了。

Treefold 用 amux 管理这些需要持续运行的进程。服务可以跟着任务列出来，人能在界面里看日志、输入命令，Agent 也能通过 amux 查询进程、读取日志、停止或重启服务。几个 Session 可以共同观察同一个服务，启动前先查看已有进程，再决定复用还是另开一套。

![在任务中切换 Agent Session 和开发服务日志]( https://github.com/user-attachments/assets/1482f20b-31ea-4d82-8e8c-acd63e500cad)

切走页面不影响进程运行，也不用再回忆服务藏在哪次聊天里。不过并行启动多套服务时，端口仍然需要分别配置，Treefold 目前不会自动隔离端口。

关闭窗口时，可以选择让 App 留在后台，或者直接退出。退出 App 后是否保留 amux 和受管进程，则由单独的设置控制。

## 一个任务，可能要改几个仓库

有些项目的前后端是两个 Git 仓库。一个功能要两边一起改，就得告诉 AI 两边的位置，同步创建分支和 worktree ，再检查是不是进了对应的目录。

所以 Treefold 的一个 Project 可以放多个仓库。创建 Workspace 或 Fork 时，相关仓库一起准备分支和 worktree ，后续查看修改、同步和交付也在同一个任务里完成，各仓库的结果分别展示。

接手已有工作也不用从头开始。创建 Workspace 时，每个仓库可以分别新建分支，或者选一个已有的本地或远端分支继续做。分支列表可以搜索，已经被其他 worktree 占用的本地分支会标出来，避免选错工作目录。前端从 main 开始，后端接着已有 feature 开发，也可以放进同一个 Workspace 。

![同一个 Workspace 中，前端新建分支，后端继续使用已有分支]( https://github.com/user-attachments/assets/be23ceb4-78d1-41e9-9df7-a234199da15e)

还有 monorepo：一个仓库里放了很多项目，我可能只关心其中几个目录。Treefold 可以把这些子目录设为工作入口，也可以加入外部资料目录，方便 Agent 找到相关上下文。目录选择帮助组织工作，Git worktree 仍然以整个仓库为单位。

需要换回熟悉的工具时，Open With 可以直接在 IDE 、终端或 Finder 中打开当前目录，也能一键复制路径。选中了哪个任务，就打开它对应的工作目录。

## 保留终端习惯，少记几个快捷键

我日常主要用 Agent 的 CLI 和 TUI ，所以 Treefold 里的 Agent 也是原来的终端界面。目前支持 Codex 、Claude Code 、OpenCode 和 Pi ，也可以单独开 Shell 跑命令。终端使用 xterm.js 。

Agent 使用本机安装的 CLI ，沿用自己的登录和模型配置。喜欢哪个就用哪个，同一项任务里也可以开不同的 Agent Session 。使用前先确认相应 CLI 在终端里能正常运行；没有配置 Agent ，也可以先用 Shell 。

我喜欢 Command Palette ，但不想记一大堆快捷键。所以默认只给少数高频操作绑定快捷键，其他操作从 Palette 找，也可以按自己的习惯修改绑定。

这里我比较在意上下文：在某个 Fork 里打开 Palette ，新建 Session 、开始 AI Review 或打开目录，就应该接着使用这个 Fork 的上下文，不用重新选一遍。

## 免费开源，本地运行

Treefold 免费开源，使用 AGPL-3.0-only 许可证。App 在本机运行，项目状态、任务、Session 元数据和配置保存在自己的电脑上，核心管理功能不依赖云端服务。

Agent 沿用你自己的模型和服务配置，模型调用、网络访问和费用由对应服务及配置决定。目前支持 Apple Silicon Mac ，需要 macOS 14 或更新版本。

官网：[treefold.win5do.top]( https://treefold.win5do.top/)

GitHub：[win5do/treefold]( https://github.com/win5do/treefold)

下载：[GitHub Releases]( https://github.com/win5do/treefold/releases)

如果你也遇到过这些问题，欢迎下载试用。哪里不顺手、想增加什么功能，都可以提 [Issue]( https://github.com/win5do/treefold/issues)，或者通过 [README 里的飞书交流群]( https://github.com/win5do/treefold/blob/main/README.zh-CN.md#%E9%A3%9E%E4%B9%A6%E4%BA%A4%E6%B5%81%E7%BE%A4)找我交流 AI Coding 经验。

也欢迎 Fork ，按自己的习惯修改、贡献代码。觉得有用的话，帮忙点个 Star 。

## 关联链接

- https://github.com/user-attachments/assets/4e7cf442-4375-42ed-8901-62331cf8020b
- https://github.com/user-attachments/assets/5daeff35-b6cb-4c05-ba3f-aeff03e02318
- https://github.com/user-attachments/assets/be23ceb4-78d1-41e9-9df7-a234199da15e
- https://github.com/user-attachments/assets/be50aea7-79c7-45ff-b89b-18baf05f72f4
- https://github.com/user-attachments/assets/c533f978-9d84-4834-8916-fe651d601c85
- https://github.com/user-attachments/assets/f15239f8-c0b2-482c-9e4a-4749e5ce6f26
- https://github.com/win5do/treefold
- https://github.com/win5do/treefold/blob/main/README.zh-CN.md#%E9%A3%9E%E4%B9%A6%E4%BA%A4%E6%B5%81%E7%BE%A4
- https://github.com/win5do/treefold/issues
- https://github.com/win5do/treefold/releases
- https://treefold.win5do.top/

## 导航

- 项目页：[[10-项目/github.com_767d56b2]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
