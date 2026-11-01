---
type: "project"
title: "我用 Eclipse 的核心技术，给 AI 写了一个 Java 启动器"
project_url: "https://github.com/locationtech/jts"
first_seen: "2026-11-01T09:43:04+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 300
lang: "zh"
---

# 我用 Eclipse 的核心技术，给 AI 写了一个 Java 启动器

> [!info] 一句话导读
> 最近做了一个开源工具，叫 **joLink**。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/locationtech/jts>
> 首次收录：2026-11-01T09:43:04+08:00
> 来源渠道：V2EX
> 标签：300
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-01T09:43:04+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-01/37918aae8d5276c8_我用-Eclipse-的核心技术,给-AI-写了一个-Java-启动器]] |

## 摘要正文

最近做了一个开源工具，叫 **joLink**。  它通过 MCP 接入现有的 AI 编程助手，提供 Java 增量编译、测试、应用启动、热更新和调试能力。底层用到了 Eclipse JDT ，不过不需要打开 Eclipse ，也不需要让 AI 操作 IDE 界面。  做它的想法很简单：**我们在 IDE 里已经习惯了“改完接着跑”，我想把这种开发体验也提供给 Agent 。**  ## 目标：让 AI 更快、更顺手地运行自己写的代码  让 Agent 修改 Java 代码，再启动项目、跑单元测试，已经不是新鲜事了。  我更关心的是后面这段过程： ```text 修改代码 → 运行测试 → 发现问题 → 继续修改 → 再次运行 ```  一个需求通常不止执行一次。第一次实现遗漏了边界，补一下；测试发现行为不对，再改一下；接口结果符合预期了，还要检查有没有影响其他功能。  AI 可以很快写完一段代码，但接下来仍然需要等待编译、启动和执行结果。**如果每次只是小改动，却要重复做很多准备工作，那么几轮下来，等待就成了开发过程里很明显的一部分。**  joLink 想做的，就是把这段反复“修改—运行—排查”的过程接起来，减少重复工作，让 Agent 尽快拿到下一步判断所需要的结果。  下面先看实际过程，再讲它是怎么实现的。  ## 迅速：对比一次“测试—修改—再测试”  这次使用的是 **CodeBuddy 客户端，模型为 DeepSeek-V4.1-Flash-1017 官方 api**。  示例项目：[JTS Topology Suite]( https://github.com/locationtech/jts)，固定版本 **1.20.0**，只运行 `modules/core` 模块中的 `org.locationtech.jts.geom.EnvelopeTest`。   固定提交：`6e95fe82feb986a7aa657f4ffa406d8c290af509`。   运行环境：**macOS 、Zulu JDK 17.0.16 、Maven 3.9.11  joLink 0.1.0a10**。。  这个模块本轮参与编译的源码包括 **612 个生产文件和 369 个测试文件，共 981 个文件**。  这次模拟一次小范围重构：先运行已有的 17 项测试，再把 `Envelope.java` 中的 `getWidth()` 做等价改写，保持功能不变，然后运行同一组测试。两轮之间只改了下面这一处，测试文件没有修改：  ```diff  public double getWidth() { -  if (isNull()) { -    return 0; -  } -  r…
