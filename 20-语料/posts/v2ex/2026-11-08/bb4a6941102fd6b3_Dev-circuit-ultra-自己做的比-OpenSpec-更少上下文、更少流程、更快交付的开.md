---
type: "corpus"
item_id: "bb4a6941102fd6b3"
title: "[Dev-circuit-ultra]-自己做的比 OpenSpec 更少上下文、更少流程、更快交付的开发 loop"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1255229"
project_url: "https://github.com/iswalterwu/dev-circuit-ultra"
author: "iswalterwu"
published_at: "2026-11-07T09:28:38"
captured_at: "2026-11-08T12:55:07+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-08"
pub_day: "2026-11-07"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [Dev-circuit-ultra]-自己做的比 OpenSpec 更少上下文、更少流程、更快交付的开发 loop

> [!info] 一句话导读
> 这两天优化了自己在用的开发工作流，好处是比 OpenSpec 的上下文维护轻量得多，但不丢框架深度和交付细节。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1255229>
> 指标：回复=0
> 作者：iswalterwu　|　发布：2026-11-07T09:28:38
> 项目链接：<https://github.com/iswalterwu/dev-circuit-ultra>
> 采集：2026-11-08T12:55:07+08:00　|　id：`bb4a6941102fd6b3`

## 正文

这两天优化了自己在用的开发工作流，好处是比 OpenSpec 的上下文维护轻量得多，但不丢框架深度和交付细节。

经过测试，在较短的开发周期下，已经能体现较 OpenSpec 超过 -30% 的 token 成本、-48% 的 cache-read 以及 -51% 的文档维护。仓库里还放了一次单会话的开放任务 A/B，方向和这个一致（模型成本 −29.9%、输入+输出 tokens −36.2%、cache-read −48.6%、留存文档 −51.6%）。

同时，记账与开发完全分离，确保开发过程不会被过期设计或旧想法污染。


[项目地址]( https://github.com/iswalterwu/dev-circuit-ultra)
[项目概览]( https://github.com/iswalterwu/dev-circuit-ultra/blob/main/assets/after-setup-en.svg)





## 它是什么

一套面向独立开发者的五步功能开发循环，以 skill 的形式加载到 Claude Code、Codex、pi、DeepSeek Harness 等编码 agent 里：

1. 设计澄清 + 意图卡
2. 单个能独立验收的端到端切片
3. 实现 + 验证
4. 独立审核（普通功能一次；框架级改动加一次结构审）
5. 验收 + 合并

和常见的规格驱动工具不同，它不维护 proposal / tasks / archive，仓库里只保留**现行设计**：设计变了就原地覆盖或删除，功能收尾就删卡。决策历史（包括被否掉的方案）写进项目之外的私有 git 账本；强隔离下，dev 容器没有账本挂载、没有路径、没有凭证，开发 agent 读不到。

这条边界是文件系统级的，不是 prompt 约定。README 里把隔离分成弱 / 中 / 强三档，明确写了只有容器方案才叫"保证"。

## 最新 A/B：省在哪

同一个 records CLI 开放任务、每个 skill 一个会话、最终交付物盲评：

| 相对 OpenSpec | Dev-circuit-ultra | OpenSpec | 差异 |
| --- | ---: | ---: | ---: |
| 模型成本 | $0.0743 | $0.1060 | −29.9% |
| 输入 + 输出 tokens | 72,308 | 113,337 | −36.2% |
| 缓存读取 tokens | 1,891,968 | 3,678,333 | −48.6% |
| assistant 轮次 | 39 | 50 | −22% |
| 留存文档 | 2 文件 / 132 行 | 3 文件 / 273 行 | −51.6% |
| 盲评总分（30） | 27 | 26 | +1 |

欢迎大家一起探讨，跟大家学习！

## 关联链接

- https://github.com/iswalterwu/dev-circuit-ultra/blob/main/assets/after-setup-en.svg
- https://github.com/user-attachments/assets/67ddd91f-9b5e-4e8a-9d8b-eeeb263e6277
- https://github.com/user-attachments/assets/a119dc2c-a44c-4e62-90a5-1d1dc08d036a

## 导航

- 项目页：[[10-项目/github.com_06b9931d]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
