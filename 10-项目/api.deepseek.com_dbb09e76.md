---
type: "project"
title: "用 Rust 写了一个行式 coding agent"
project_url: "https://api.deepseek.com/"
first_seen: "2026-09-28T09:51:06+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 用 Rust 写了一个行式 coding agent

> [!info] 一句话导读
> title: 用 Rust 写了一个行式 coding agent

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://api.deepseek.com/>
> 首次收录：2026-09-28T09:51:06+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-28T09:51:06+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-09-28/397cadb0dec7dfbb_用-Rust-写了一个行式-coding-agent]] |

## 摘要正文

--- title: 用 Rust 写了一个行式 coding agent date: 2026-09-26 ---  用了一年多 Claude Code ，从[本地配合 DeepSeek 跑生信流程](/5v7pe/)，到[在曙光服务器上公共部署](/9z3sa/)，越用越觉得这类工具没必要那么复杂。模型 API 说白了就是一个 HTTP 请求加一个 SSE 流，工具无非是读写文件和跑命令，交互界面就是个终端，连 TUI 都不用做，普通的行式会话就够。抱着这个想法，最近用 Rust 写了一个自己的 agent ，就叫 [llm]( https://github.com/imjiaoyuan/llm)，一个静态链接的二进制文件，没有任何运行时依赖，扔到机器上就能跑。和之前 [vibe coding 博客框架](/5xbok/) 是同一个思路，核心只做必须做的事，其余的全部留出扩展的缝，这样出问题也知道去哪修。  ## 安装  Linux 和 macOS 下面一行命令，下载预编译二进制，校验 sha256 之后装进 `~/.local/bin`，全程不需要 root  ```bash curl -fsSL https://jiaoyuan.org/llm/install.sh | sh ```  PATH 里没有这个目录的话安装脚本会顺手加上。重复执行同一条命令就是更新器，版本有变化会打印 `updating 0.2.1 -> 0.2.2`，没变化就不动，`LLM_VERSION` 可以固定某个 release ，`LLM_REPO` 可以从 fork 装，`LLM_FORCE=1` 强制重装。Windows 下面从 PowerShell 做同样的事  ```powershell irm https://jiaoyuan.org/llm/install.ps1 | iex ```  Linux 用的是静态 musl 构建，同一个二进制在任何发行版上都能跑，目前提供 x86_64 和 aarch64 的 Linux ，x86_64 和 aarch64 的 macOS ，还有 x86_64 的 Windows 。之前在曙光服务器上部署 Claude Code 的时候，CentOS 7 的 glibc 老得连 conda 都得搬出来兜底，现在这个 musl 二进制 scp 过去 `chmod +x` 直接就能用，省心多了。  想从源码编译也很简单，装好 Rust 工具链以后  ```bash git clone https://github.com/imjiaoyuan/llm cd llm cargo build --release ```  二进制在 `target/release/llm`。所有状态…
