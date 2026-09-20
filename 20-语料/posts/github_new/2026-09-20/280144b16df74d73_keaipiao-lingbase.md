---
type: "corpus"
item_id: "280144b16df74d73"
title: "keaipiao/lingbase"
source: "github_new"
source_name: "GitHub 新星仓库"
url: "https://github.com/keaipiao/lingbase"
project_url: "https://github.com/keaipiao/lingbase"
author: "keaipiao"
published_at: "2026-06-12T04:52:51Z"
captured_at: "2026-09-20T09:36:30+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-06-12"
tags:
  - 语料
  - github_new
  - topic:indie-hacker
metrics: {"stars": 2, "forks": 1, "open_issues": 0}
comments_count: 0
comments_total: 0
discovered_via: "github:14d"
---

# keaipiao/lingbase

> [!info] 一句话导读
> 独立开发者的 **AI 编程工作流脚手架** —— 让 AI 编程工具按标准化流程**自动帮你做产品、做功能**，配套 [灵计一动](https://lingji1dong.com) 看板边做边维护进度。

> [!meta]- 语料信息（点开展开）
> 来源：GitHub 新星仓库（post）
> 原帖：<https://github.com/keaipiao/lingbase>
> 指标：stars=2 · forks=1 · open_issues=0
> 作者：keaipiao　|　发布：2026-06-12T04:52:51Z
> 项目链接：<https://github.com/keaipiao/lingbase>
> 采集：2026-09-20T09:36:30+08:00　|　id：`280144b16df74d73`

## 正文

# 灵基 · lingbase

> 独立开发者的 **AI 编程工作流脚手架** —— 让 AI 编程工具按标准化流程**自动帮你做产品、做功能**，配套 [灵计一动](https://lingji1dong.com) 看板边做边维护进度。
>
> 克隆它起新项目，AI 就按固定结构走，不再每次自由发挥、另起一套文档。任何能读项目规则文件 + 连 MCP 的 AI 工具都能用（[Claude Code](https://claude.com/claude-code) 开箱即用、其它工具一行映射，详见下文）。

![灵计一动看板：AI 边做边勾计划](https://github.com/user-attachments/assets/ab6fe720-47ff-430f-afce-1ace16d7172d)

---

## 解决什么问题

AI 编码工具每次都按自己的想法新建文档结构 —— 文档位置飘忽、回头找不到、风格各不相同。换个项目、过几个月回来，全得重新摸。

灵基把「做哪些文档、放哪里、什么时候写、按什么顺序推进」固定下来：**AI 只复制模板填空、按 SOP 推进，不自由发挥**。

---

## 能让 AI 自动做什么

- 🤖 **按标准化六阶段开发**：立项 → UI 设计 → 技术方案 → 实现 → 测试 → 发布归档。每阶段都有明确产出位置和完成条件，**关键节点停下等你确认**，不会跑偏。
- 📝 **自动写 / 维护项目文档**：架构总览、设计规范、部署手册、踩坑记录 —— 随开发**增量沉淀**，不是事后补。
- 📋 **自动管理灵计一动看板**：拆计划、勾进度、记决策 / 踩坑 / 验证笔记，全程由 AI 边做边维护，**计划和进度永不写进文档**。
- 🎯 **一个里程碑 = 一条灵感**：每条里程碑灵感的计划就是它的六阶段；一个产品 = 一串里程碑灵感。**新产品**第一条是打地基（架构 / 设计规范 / 脚手架），之后每个功能各一条灵感、走一遍六阶段流水线。

---

## 快速开始·三步

1. **拿到模板** —— 在 GitHub 点「Use this template」起新仓库，或 clone 本仓库。
2. **接入灵计一动 MCP** —— 注册账号并配好 MCP（见 [lingji1dong.com](https://lingji1dong.com)）。
3. **打开你的 AI 编码工具，说出你的想法** —— 比如「我想做个 XX 产品」（非 Claude Code 工具先按下方说明把 `CLAUDE.md` 映射到其入口文件）。AI 会读 `CLAUDE.md` 自动接好看板、和你聊清产品、把想法拆成几个里程碑（各记一条灵感）→ 从打地基（架构 / 设计规范 / 脚手架）开始，逐个推进。

> **支持任何能读项目规则文件 + 连接 MCP 的 AI 编码工具**。
> - **Claude Code**：开箱即用，自动读 `CLAUDE.md`。
> - **其他工具**（Cursor / Copilot / Codex / Aider 等）：把 `CLAUDE.md` 复制或软链到对应入口文件（如 `.cursorrules` / `.github/copilot-instructions.md` / `AGENTS.md` / `CONVENTIONS.md`），即可同样使用。

> AI 协作规则在根目录 `CLAUDE.md`，**开箱即用**——AI 进项目先读它。

---

## 这套工作流怎么运作：看板管进度，文档管知识

两类信息**严格分家** —— 这是整套工作流的地基：

| | 放哪 | 装什么 |
|---|---|---|
| **进度 / 计划 / 过程** | [灵计一动](https://lingji1dong.com) 看板 | 任务拆分、完成状态、踩坑 / 决策 / 验证笔记 |
| **长期知识** | 仓库内 Markdown 文档 | 需求、架构、设计规范、上线快照 |

**为什么进度不写进文档？** 文档里的待办 / 时间线会立刻过时、和代码脱节、没人维护。进度是**活的**，交给灵计一动看板：写计划大纲 → 边做边勾 → 笔记成日志，配套 MCP 让 AI 直接读写。

→ 计划和进度**永远只在看板**，文档只留沉淀下来的知识。两边不重复，各管一摊。

---

## 目录结构

```
你的项目/
├── README.md        ← 这份（起项目后可换成你应用的介绍）
├── CLAUDE.md        ← AI 协作规则（开箱即用，先读它）
├── CHANGELOG.md     ← 版本变更总账
└── docs/
    ├── 开发流程SOP.md   ← 开发流程元规范（里程碑模型 + 六阶段 + 横切动作）
    ├── 架构总览.md      技术栈 / 架构 / 数据模型 / 全局决策
    ├── 设计规范.md      前端设计系统（含 UI 出图三路线；无前端可不建）
    ├── 部署手册.md      从零冷启动
    ├── 踩坑记录.md      跨功能可复用坑
    ├── 资源/           项目级资源：logo / 品牌 / 全局原型
    └── 功能/
        ├── _模板/      ← 新功能复制此目录
        └── NN-功能名/  每个功能一个目录
```

`docs/` 根只放项目级的「长期文档」，所有功能集中在 `docs/功能/` 下，几十个功能也不乱。

---

## 文档导航

| 看什么 | 去哪 |
|---|---|
| 开发流程怎么走 | `docs/开发流程SOP.md` |
| AI 协作规则 | `CLAUDE.md` |
| 技术架构 | `docs/架构总览.md` |
| UI 设计规范 / 出图路线 | `docs/设计规范.md` |
| 部署 | `docs/部署手册.md` |
| 已知坑 | `docs/踩坑记录.md` |
| 某个功能 | `docs/功能/NN-功能名/{设计, 测试, 发布部署}.md` |

---

> 🛠 **起项目后可按需替换本 README**：把上面对灵基的介绍换成你应用的门面；下面的「目录结构 / 文档导航」对任何用本套件的项目都成立，保留即可。

## License

[MIT](LICENSE)

## 关联链接

- https://claude.com/claude-code
- https://github.com/user-attachments/assets/ab6fe720-47ff-430f-afce-1ace16d7172d
- https://lingji1dong.com

## 导航

- 项目页：[[10-项目/github.com_280144b1]]
- 渠道页：[[50-渠道/github_new]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
