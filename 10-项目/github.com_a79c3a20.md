---
type: "project"
title: "预算 1000 美金的开源软件， DeepSeek 只花 1 美金就做完了（Day 6）"
project_url: "https://github.com/chaxiu/OpenCompare"
first_seen: "2026-10-22T09:49:30+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 300
lang: "zh"
---

# 预算 1000 美金的开源软件， DeepSeek 只花 1 美金就做完了（Day 6）

> [!info] 一句话导读
> 原本我准备了 1,000 美金预算，让 Gemini 4 当公司高管，DeepSeek 打下手。让它们帮我写一个开源软件。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/chaxiu/OpenCompare>
> 首次收录：2026-10-22T09:49:30+08:00
> 来源渠道：V2EX
> 标签：300
> 最新指标：回复=1

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-22T09:49:30+08:00 | V2EX | 回复=1 | [[20-语料/posts/v2ex/2026-10-22/698f0d624f910140_预算-1000-美金的开源软件,-DeepSeek-只花-1-美金就做完了(Day-6)]] |

## 摘要正文

原本我准备了 1,000 美金预算，让 Gemini 4 当公司高管，DeepSeek 打下手。让它们帮我写一个开源软件。  结果跑完这两天，**DeepSeek 只花了大约 10 美金（换算到我的 Token 套餐里，实际成本只要 1 美金），就把 [OpenCompare]( https://github.com/chaxiu/OpenCompare) 整套开源软件和自动维护闭环全部做完了。**  在这个过程中，我基本上只 prompt 过两次，指一个大方向，让 Agent 自行迭代，直到完成我的目标。  ![Token 账单：5.9 亿 Token 仅花 12.64 美金](  )  ### 1. 1 美金跑完 5.9 亿 Token ，DeepSeek 连产品经理的活都扛了  跑到现在，我们团队的分工自然演进成了这样： **Gemini 作为公司最高负责人，平时基本只负责派发人类的指令，在产品负责人拿不准、不确定的时候才会被唤醒；而 DeepSeek 不仅扛下了全部研发，还承担了产品负责人（ Product Owner ）的职责。**  所以最终下来，Gemini 的 Token 消耗几乎可以忽略不计。 账单上，DeepSeek 独自跑了 **9,993 次请求、吞吐 5.9 亿 Token**（靠高缓存命中省下了大头），账面金额 **12.64 美金**，换算到我的 Token 套餐，**实际成本大约只要 1 美金。**  这 1 美金经历了多少迭代？看下面这张需求演进全貌图：  ![OpenCompare 经历的需求集与 Agent 调度网络](  )  从双栏代码对比、三向合并、快照协议，到 Apple 开发者签名公证、三端打包发版，**4 大需求集、30 多个子需求、上百次 Agent 调度接力**，全是从我那两次大方向指令里自己长出来的。  ### 2. Computer Use 亮眼表现：DeepSeek 的临场反应太聪明了  写完代码只是第一步，更让我惊喜的是 DeepSeek 在操控电脑（ Computer Use ）做真机验收时的表现。分享两个真实的测试 case：  **Case 1：Dock 栏呼不出来，它换思路打开 Finder 切「大图标」验 Icon**  OpenCompare 安装后，需要在电脑的 Dock 栏看到正确的 Icon 。 DeepSeek 自己控制电脑，把鼠标挪到了屏幕最底部，希望 Dock 能出现。结果受系统限制，并不支持。 DeepSeek 很聪明，立刻换了个思路：自己打开了 Finder 进入编译目录：  ![打开 Finder 找到应用目录](  )  接着它把视图切换到了**「大图标」模式**，清清楚楚看清了 App 的 Ico…
