---
type: "corpus"
item_id: "69abbecbf27a8c43"
title: "[开源] UnifyTerm：不只是一个终端，更是一套跨平台统一的命令环境"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1258307"
project_url: "https://dfine.tech/keepane"
author: "stebest"
published_at: "2026-11-19T08:11:51"
captured_at: "2026-11-20T09:49:00+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-20"
pub_day: "2026-11-19"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [开源] UnifyTerm：不只是一个终端，更是一套跨平台统一的命令环境

> [!info] 一句话导读
> 最近开源了一个自己用 Rust 开发的项目：**UnifyTerm**。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1258307>
> 指标：回复=0
> 作者：stebest　|　发布：2026-11-19T08:11:51
> 项目链接：<https://dfine.tech/keepane>
> 采集：2026-11-20T09:49:00+08:00　|　id：`69abbecbf27a8c43`

## 正文

最近开源了一个自己用 Rust 开发的项目：**UnifyTerm**。

现在终端项目越来越多，从 Ghostty、WezTerm 到各种 AI Terminal，大家都在探索终端的不同形态。

所以我也一直在思考一个问题：在已经有这么多优秀终端的情况下，还有什么值得做？

我的切入点不是再做一个更快的终端模拟器，也不是简单地给终端增加一个 AI Chat，而是希望解决几个实际问题：

1. Windows、macOS、Linux 之间的命令环境不一致。
2. 命令历史只是简单记录，缺少工作目录、执行状态等上下文。
3. 终端仍然主要是文本交互，查看图片、文档等内容需要频繁切换工具。
4. AI Agent 越来越多地操作终端，但它们并不总能准确理解当前环境有哪些可用能力。

于是有了 UnifyTerm。

## 一、跨平台统一命令环境

UnifyTerm 不是一个新的 Shell，而是一个跨平台桌面终端应用，兼容现有的 PowerShell、cmd、bash、zsh、fish。

它提供了一套统一的 Unix 命令工具。

例如在 Windows 下，不需要安装 WSL 或 Git Bash，就可以直接使用：

- `cat`、`ls`、`pwd`
- `grep`、`find`、`sed`、`sort`
- `jq`、`diff`、`xargs`

目前 Windows 内置 99 个命令，Linux 内置 114 个命令。

除了命令本身，还处理了不同平台的路径格式和通配符展开问题。

希望达到的效果是：同样的命令和脚本，在不同操作系统上尽可能保持一致。

## 二、让命令历史真正有用

传统终端的命令历史大多只关注输入过什么。

UnifyTerm 使用 SQLite 在本地记录：

- 命令内容
- 执行时的工作目录
- 退出状态
- 执行耗时

输入命令时，会根据历史记录和当前工作目录进行匹配。

例如在项目 A 中经常执行的命令，在进入项目 A 后会获得更高的搜索优先级。

另外，历史记录可以在不同机器之间迁移，Windows 上记录的命令也可以在 Linux 上使用。

密码、Token 和 Key 等敏感内容会在保存前过滤。

我希望命令历史不只是一个日志，而是逐渐成为开发者自己的本地命令知识库。

## 三、让终端不再只有文本

终端其实可以承载更多内容。

UnifyTerm 提供了几个直接可用的能力：

```bash
# 查看图片
ut view photo.png

# 播放视频
ut view clip.mp4

# 阅读 Markdown
ut md README.md
```

支持在终端中显示图片、播放视频，以及渲染 Markdown，包括标题、列表、表格和链接。

对于日常开发来说，查看一张图片、阅读一份 README，不一定都需要离开终端。

## 四、内置命令纠错和 AI 辅助

UnifyTerm 不希望所有辅助功能都依赖云端 AI。

因此提供了两种方式：

**本地命令纠错**

输入错误命令时，根据本地可用命令提供纠错建议，不需要网络，也不需要配置模型。

**LLM 命令辅助**

配置模型后，可以解释命令及其参数，也可以提供命令补全建议。

这里比较在意隐私问题：AI 辅助默认关闭，启用前会说明数据共享范围并征求用户同意，请求中的密码、Token 和 Key 也会过滤。

## 五、专门考虑 AI Agent 的使用方式

这是 UnifyTerm 比较重要的一个设计方向。

现在 Claude Code、Codex 等工具越来越依赖终端执行任务，但 Agent 对运行环境的了解，很大程度上还是依赖模型训练时学到的知识和上下文描述。

例如：

- 当前环境到底有哪些命令？
- 某个命令支持哪些参数？
- 之前执行过什么命令？
- 某条命令上次执行是否成功？

UnifyTerm 提供了 MCP Server 和 Skill，让 Agent 可以主动发现终端能力。

目前 MCP 提供四种只读工具：

- 搜索命令历史
- 查询最近执行的命令
- 获取当前可用命令列表
- 查询命令帮助

这里特意采用只读设计，MCP 本身不提供 Shell 命令执行权限。实际命令执行仍然由 Agent 使用正常的终端工具完成。

这样做的目的，是让 Agent 能够更准确地理解终端环境，而不是再造一个拥有额外执行权限的 Agent Shell。

## 六、它和其他终端项目有什么不同？

我并不认为 UnifyTerm 要替代 Ghostty、WezTerm 或其他优秀终端项目。

不同项目关注的方向不一样。

UnifyTerm 更关注的是终端背后的命令环境、历史上下文，以及人与 AI Agent 如何共同使用这些能力。

目前比较有特点的地方：

- **环境统一**：不只是跨平台显示，而是统一常用命令及相关执行行为。
- **上下文历史**：命令历史与工作目录、执行状态关联，可以迁移和复用。
- **内容集成**：图片、视频和 Markdown 都可以直接在终端处理。
- **Agent 可发现性**：通过 MCP 和 Skill 暴露真实可用的终端能力，而不是让模型猜测。
- **本地优先**：命令历史使用 SQLite 本地存储，AI 辅助由用户自主选择是否启用。

我更希望把它做成一套统一的终端工作环境，而不仅仅是一个命令窗口。

## 项目信息

- 开发语言：Rust
- 数据库：SQLite
- 支持平台：Windows、macOS、Linux
- 开源协议：MIT
- 当前版本：0.2.0

项目主页：https://dfine.tech/unifyterm/

GitHub：https://github.com/newdee/unifyterm

欢迎 Star、试用和提交 Issue。

另外，如果你也在使用我之前开源的终端复用工具 keepane（），可以将两者结合：keepane 负责 Pane 管理和多 Agent 协作，UnifyTerm 负责统一命令环境，还可以在终端中查看运行中 Agent 的模型、费用、Context 使用率和内存信息。两者可以独立使用，也可以组合成一套更完整的 AI Coding 工作环境。

目前还在持续迭代，欢迎大家试用和反馈。

## 关联链接

- https://dfine.tech/keepane/
- https://dfine.tech/unifyterm/
- https://github.com/newdee/unifyterm

## 导航

- 项目页：[[10-项目/dfine.tech_fbf8df13]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
