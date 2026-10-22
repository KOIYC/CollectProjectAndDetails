---
type: "corpus"
item_id: "db75f5c9da297f4c"
title: "QuotaPanel：基于 Wails 的 AI 订阅额度管理工具"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1250750"
project_url: "https://gitee.com/open-tecmz/quotapanel"
author: "ModStart"
published_at: "2026-10-21T14:19:22"
captured_at: "2026-10-22T09:49:30+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-22"
pub_day: "2026-10-21"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# QuotaPanel：基于 Wails 的 AI 订阅额度管理工具

> [!info] 一句话导读
> 在 AI 开发日益普及的今天，开发者需要同时管理 Claude 、ChatGPT 、GitHub Copilot 、Kimi 等多个平台的订阅与 API 额度。这些额度信息分散在各个控制台，难以快速掌握整体使用情况。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1250750>
> 指标：回复=0
> 作者：ModStart　|　发布：2026-10-21T14:19:22
> 项目链接：<https://gitee.com/open-tecmz/quotapanel>
> 采集：2026-10-22T09:49:30+08:00　|　id：`db75f5c9da297f4c`

## 正文

# 引言

在 AI 开发日益普及的今天，开发者需要同时管理 Claude 、ChatGPT 、GitHub Copilot 、Kimi 等多个平台的订阅与 API 额度。这些额度信息分散在各个控制台，难以快速掌握整体使用情况。

**QuotaPanel** 是一款开源的桌面端 AI 额度管理工具，基于 **Go + Wails + Vue3** 技术栈开发，支持 16 种 AI 订阅与 API 额度来源，本地优先保护隐私，跨平台支持 macOS/Windows/Linux 。

![](  ?t=202609261508)

## 核心特性

### 本地优先设计

QuotaPanel 采用**本地优先**架构，所有账号密钥与浏览器会话数据均保存在本机（默认 `~/.quotapanel/`），不会上传到云端。数据目录支持通过 `QUOTAPANEL_DATA_ROOT` 环境变量自定义位置。

### 多源额度聚合

工具支持 16 种 AI 订阅与 API 额度来源，分为两大类：

**浏览器登录类**：
- Claude 订阅（ 5 小时及每周额度）
- ChatGPT/Codex （订阅使用窗口）
- Cursor （当前周期用量）
- Xiaomi MiMo Token Plan （套餐积分与账户余额）

**API Key 类**：
- GitHub Copilot （ Premium 、聊天与补全额度）
- Z.ai Coding Plan 、Kimi Coding Plan 、MiniMax Token Plan
- Devin/Windsurf 、Grok CLI 、OpenCode
- Command Goat 、DeepSeek API 、Kimi API
- OpenRouter 、OpenAI API

### 额度可视化

通过进度条、余额明细、账期/重置时间等可视化元素，系统提供正常、即将用尽、超限三档状态色，超出阈值时会主动提示。

![](  ?t=202609261508)

## 技术架构

### 技术栈

- **Go 1.24+**：后端核心逻辑与额度查询服务
- **Wails v2**：跨平台桌面应用框架
- **Vue3 + TypeScript**：前端界面开发
- **AntDesign Vue**：UI 组件库
- **TailwindCSS**：样式框架
- **SQLite**：本地数据存储

### 项目结构

```
quotapanel/
├── main.go              # Wails 应用配置与入口
├── app*.go              # App 暴露给前端的方法
├── backend/
│   ├── base/            # 基础库（数据库、配置、日志、窗口、平台差异等）
│   └── quota/           # 各额度供应商适配器与查询服务
├── frontend/
│   └── packages/
│       ├── ui/          # 主界面（ Vue3 + AntDesignVue + TailwindCSS ）
│       └── quota/       # 额度业务模块
├── demo/image/          # 界面截图
├── docs/                # 文档（额度来源调研等）
└── Makefile             # 开发、构建与发布命令
```

### 开发环境

- Go 1.24+
- Wails v2
- Node.js 20 + pnpm

```bash
# 安装 Wails CLI
go install github.com/wailsapp/wails/v2/cmd/wails@latest

# 安装 pnpm
npm install -g pnpm
```

### 开发命令

```bash
# 安装依赖
make install

# 启动开发模式（前端热重载）
make dev

# 构建生产版本
make build

# 构建并安装到 /Applications （ macOS ）
make build-install
```

修改 Go 暴露给前端的方法后，执行 `wails generate module` 重新生成 JS 绑定。

![](  ?t=202609261508)

## 功能亮点

### 新增账号管理

支持选择来源并填写 API Key 或发起浏览器登录，可自定义账号名称与备注，密钥默认脱敏展示并支持一键复制。

### 浏览器登录

需要网页登录的订阅（ Claude/ChatGPT/Cursor ）通过独立 Chrome/Edge 窗口登录，登录会话持久保存，删除账号时一并清理其浏览器资料。

### 卡片截图

一键将单张订阅卡片导出为 PNG ，方便分享或记录。

### 定时刷新

默认每 5 分钟自动轮询一次，额度变化实时可见。同时也支持随时手动刷新单个或全部账号。

### 托盘常驻

macOS 菜单栏/Windows 、Linux 系统托盘，快捷显示、重启、退出。关闭窗口行为可配置为「每次询问/直接退出/隐藏到后台」。

### 多语言支持

简体中文/English 切换，界面与后端文档页配色集中到设计 token 管理，支持浅色/深色两套取值。

![](  ?t=202609261508)

## 总结

QuotaPanel 是一款功能完善、设计优雅的 AI 订阅额度管理工具，采用 **Go + Wails + Vue3** 技术栈，支持 16 种 AI 订阅与 API 额度来源。

**核心优势**：

- ✅ **开源免费**：采用 Apache-2.0 许可证，可自由使用、修改和商用
- ✅ **跨平台支持**：macOS 、Windows 、Linux 全覆盖
- ✅ **隐私保护**：所有数据本地存储，不上传云端
- ✅ **持续更新**：社区活跃，支持新增额度来源

**适用人群**：

- AI 重度用户，需要管理多个平台的订阅额度
- 开发者，希望参与开源项目或自定义额度来源
- 技术爱好者，对 Go/Wails/Vue3 技术栈感兴趣

如果你也是 AI 重度用户，或者需要管理多个平台的订阅额度，不妨试试 QuotaPanel 。让它成为你开发工作流中不可或缺的一部分。

> ⭐ 如果这个项目对你有帮助，请在 [GitHub]( https://github.com/open-tecmz/quotapanel) / [Gitee]( https://gitee.com/open-tecmz/quotapanel) 上点亮 Star 支持开发者！

## 关联链接

- https://github.com/open-tecmz/quotapanel

## 导航

- 项目页：[[10-项目/gitee.com_025ee75c]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
