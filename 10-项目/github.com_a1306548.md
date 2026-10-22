---
type: "project"
title: "LangAlpha 2.0 正式上线: 最先进的 Open-source Harness for Agentic Trading"
project_url: "https://github.com/ginlix-ai/LangAlpha"
first_seen: "2026-10-22T09:49:30+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 1192
lang: "zh"
---

# LangAlpha 2.0 正式上线: 最先进的 Open-source Harness for Agentic Trading

> [!info] 一句话导读
> LangAlpha 2.0 正式上线：开源金融 Agent ，从投资研究到 Agentic Trading**

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/ginlix-ai/LangAlpha>
> 首次收录：2026-10-22T09:49:30+08:00
> 来源渠道：V2EX
> 标签：1192
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:49:30+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-22/c26498ecd675452b_LangAlpha-2.0-正式上线-最先进的-Open-source-Harness-for-Ag]] |

## 摘要正文

**LangAlpha 2.0 正式上线：开源金融 Agent ，从投资研究到 Agentic Trading**  大家好，我们做的 LangAlpha 2.0 上线了，想和社区分享一下。  LangAlpha 是一个面向金融市场的 Agent 产品。用自然语言提出投资想法，Agent 就能协作完成资料搜索、数据分析、报告生成和交易计划，并通过连接的券商账户执行交易。  例如：“研究半导体行业有哪些趋势已经确认的投资机会，结合财报、估值和价格走势进行比较，生成报告，并持续跟踪重要变化。”  **已经有 Claude Code 、Codex ，为什么还要做 LangAlpha ？**  我们关注的是金融场景的 Harness：围绕模型建立数据、工具、记忆、任务编排和执行控制。同一个模型、同一个 Skill ，实际效果也取决于能拿到什么数据、如何计算、怎样验证，以及研究过程能否持续积累。  LangAlpha 的技术设计主要围绕这几个方面：  - **PTC：用代码处理金融数据。** Agent 通过 Python 调用 MCP 工具，在沙箱中完成数据清洗、指标计算和分析，再把必要结果交回模型。大量行情、财务表格保留在文件和计算环境中，减少对上下文的占用，也方便检查计算过程。 - **多 Agent 并行，过程中可以介入。** 基于 LangGraph 编排任务，子 Agent 使用独立上下文，分别处理搜索、数据准备、分析和报告。用户可以在运行中补充条件、修正研究方向。 - **Workspace：让研究可以接着做。** 数据、图表、报告和研究笔记持续保留，通过 `agent.md` 与 Skills 积累上下文和方法。结合 Checkpoint 、后台任务及 Redis/SSE 事件回放，支持长任务的状态保存和断线后进度恢复。 - **可追溯、可交付。** 保留研究来源，输出 PDF 、Excel 、PPT 和交互式看板；支持图表分析、定时任务和价格触发，把一次研究延伸为持续跟踪。 - **从研究走向受控交易。** 已支持连接 Robinhood 等券商，将研究进一步转化为交易操作。连接权限、订单审批和执行校验由宿主系统控制，券商凭据与 Agent 的代码执行环境分离。 - **开放扩展与部署。** 支持多种模型、自带 API Key 、Skills 和 MCP 插件。整体采用 React 、FastAPI 、LangGraph 、PostgreSQL 、Redis 与沙箱执行架构，可自行部署、接入自己的数据和工具。  **适合谁使用？**  有持续研究需求的个人投资者、投研人员和小型团队，以及希望搭建金融 Agent 工作流的开发者。  研究分析覆盖美股、港股、A 股、日本、韩国、德国、印度等市场，也包括 …
