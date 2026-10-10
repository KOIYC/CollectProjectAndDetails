---
type: "corpus"
item_id: "fa031e5be7b81094"
title: "XXL-AI v1.1.1 发布｜ Desk 桌面客户端正式上线，云本结合再进一步"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1247214"
project_url: "https://github.com/xuxueli/xxl-ai"
author: "xuxueli"
published_at: "2026-10-08T16:38:57"
captured_at: "2026-10-10T10:02:47+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-10"
pub_day: "2026-10-08"
tags:
  - 语料
  - v2ex
  - 300
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# XXL-AI v1.1.1 发布｜ Desk 桌面客户端正式上线，云本结合再进一步

> [!info] 一句话导读
> 1 、 [优化] 项目合并部署：研发环节前后端分离，部署期前端产物内嵌进后端 Jar ，单进程单端口对外；

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1247214>
> 指标：回复=0
> 作者：xuxueli　|　发布：2026-10-08T16:38:57
> 项目链接：<https://github.com/xuxueli/xxl-ai>
> 采集：2026-10-10T10:02:47+08:00　|　id：`fa031e5be7b81094`

## 正文

### Release Notes

** [云版（ Web 服务端）] **

*   1 、 [优化] 项目合并部署：研发环节前后端分离，部署期前端产物内嵌进后端 Jar ，单进程单端口对外；
*   2 、 [新增]  I18N 模块重构：前后端国际化逻辑优化，统一后端控制；标准化国际化资源文件结构，支持多语言配置，并优化前端国际化加载逻辑；
*   3 、 [优化] 模型 API 请求通参调整，设置 User-Agent: XXL-AI 便于供应商识别；
*   4 、 [优化] 供应商模型请求参数属性优化，支持格式检测与合法性检测；
*   5 、 [升级] 项目依赖升级最新版本；

** [本地版（ Desk 桌面端）] **

> 本地版（ Desk 桌面端）以·与云版零依赖、独立构建发布；详细安装与操作见官方文档。

*   1 、 [重点]  Desk/客户端上线：基于 Electron + Vue3 + TypeScript 构建跨平台桌面客户端，支持 mac / win / linux 一键安装及应用，本地优先、开箱即用；
*   2 、 [新增] 多供应商模型接入：兼容 OpenAI 协议，供应商 + 模型本地配置；首次启动自动预置 OpenCodeGo / Ollama / Deepseek / 智谱 GLM ；
*   3 、 [架构]  Agent 运行时进程隔离：Pi （`pi-ai` + `pi-agent-core`）运行于独立 `utilityProcess`，主进程仅做 IPC 网关与越界审批，长会话与工具重活不阻塞 UI ；
*   4 、 [新增]  Plan / Build 模式：Plan 只读（仅只读文件与检索工具）、Build 全量读写，随会话持久化，默认 Build ；文件操作限定当前项目目录，越界弹原生对话框「允许本次 / 本会话允许 / 拒绝」；
*   5 、 [新增] 流式对话与执行过程可视化：流式输出思考过程 / 工具调用 / 回复内容；助手消息按片段发生顺序渲染时间线（思考 → 工具 → 正文交错），思考折叠、工具调用状态与耗时展示、Markdown 实时渲染与代码高亮；
*   6 、 [新增] 项目与会话管理：项目绑定本地磁盘目录，会话归属项目，支持搜索 / 重命名 / 删除 / 排序；会话与消息落本地 SQLite 单文件，运行时数据目录可自定义；
*   7 、 [新增] 本地系统能力：终端命令行（ node-pty + xterm ）；侧边任务面板含文件（目录树 + 编辑保存 + 预览 + 跟随本地变更）与浏览器（多标签 `webview`）；
*   8 、 [新增] 个性化设置：应用名称 / Slogan / 自定义指令，浅色（默认）/ 深色主题，中 / 英双语；
*   9 、 [优化] 性能与体验：会话落库增量 + 单事务、运行时增量合批、渲染端按需滚动；生成中切换会话不丢内容；退出时回收运行时与终端进程。
*   10 、 [强化]  Desk 命令运行环境（ Node/Python ）支持自定义 PATH 设置，提升本地环境兼容性； Node 默认使用内置版本，降低本地环境依赖；
*   11 、 [强化]  Desk 终端 locale 显示设置 UTF-8 ，解决中文乱码问题；
*   12 、 [新增] 客户端支持自动检测新版本，并引导升级；

### 一、简介

XXL-AI 是一个「**云本结合**」的 AI Agent 开发平台，提供两种同源同品牌、能力互补的交付形态，可按团队规模与使用场景独立选用，也可组合使用：

> *   **云版**：以 Agent 编排为中枢，标准化扩展「 MCP + SKILL + RAG 」，配套多供应商、空间隔离、RBAC 权限与流式对话等工程化底座，可快速构建并一键发布 Agent 。开源、开箱即用，支持集群部署与生产落地。
> *   **本地版**：跨平台桌面客户端：面向个人的本地工作台，围绕本机项目目录提供对话、文件读写、终端命令、文件 / 浏览器侧边任务等能力；安装即用、离线可用，数据仅落本地 SQLite 。

| 项  | 云版（ Web 服务端）                                   | 本地版（ Desk 桌面端）                     |
| -- | --------------------------------------------- | --------------------------------- |
| 形态 | B/S Web 应用，浏览器访问                              | C/S 桌面应用，一键安装（ mac / win / linux ）  |
| 面向 | 团队——多用户、多业务空间（ Tenant ）                         | 个人——单用户本地工作台                      |
| 定位 | Agent 编排、一键发布、权限治理                            | 本地优先，直接操作本机项目与系统能力                |
| 扩展 | MCP + SKILL + RAG ，多供应商，流式对话                   | 本地文件 / 终端 / 浏览器面板，Plan / Build 模式 |
| 模块 | `xxl-ai-api` + `xxl-ai-ui`（+ `xxl-ai-sample`） | `xxl-ai-desk`                     |
| 依赖 | MySQL + Redis + Milvus                        | 零依赖（仅本地 SQLite ）                   |

### 二、文档地址

*   中文文档：
*   Github 地址：

### 三、架构设计

XXL-AI 采用「**云本结合**」：云版（ Web / 服务端）与本地版（ Desk 桌面端）同源互补。整体自上而下分为**入口、前端、应用、运行时、支撑、外部**六层：

```┌──────────────────────────────────────────────────────────────────────────────────────────────────────┐
    │ 入口层   管理端 admin （浏览器） · 公开端访客 /#/chat/{uuid} · Desk 桌面客户端（ mac / win / linux ）   │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ 前端层   云版   xxl-ai-ui —— Vue3 + Vite + Element Plus + TS ；开发 :3000 ，生产内嵌进 API （ Hash 路由）│
    │          本地版 Desk Renderer —— Vue3 + Element Plus ； contextBridge → window.desk.*                  │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ 应用层   云版   xxl-ai-api —— SpringBoot + MyBatis + XXL-SSO ，:8080                                  │
    │                  framework：登录鉴权 · RBAC 菜单/按钮 · 系统管理 · 审计日志                          │
    │                  business：空间 · 供应商 · 知识库 · MCP · SKILL · Agent · Chat                       │
    │          本地版 Desk Main —— IPC 网关 · SQLite(Drizzle) 持久化 · Agent 托管 · 越界审批               │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ 运行时层 云版   harness —— llm · chat · rag · mcp · skill · supplier （运行时支撑，无 Controller ）    │
    │          本地版 Pi 运行时 —— pi-ai + pi-agent-core ，独立 utilityProcess                              │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ 支撑层   云版   MySQL （业务/平台） · Redis （登录态 + 对话流） · Milvus （向量库）                     │
    │          本地版 SQLite 单文件（零依赖） · 本地文件 / 终端 / 浏览器                                   │
    ├──────────────────────────────────────────────────────────────────────────────────────────────────────┤
    │ 外部层   OpenAI 兼容供应商（对话/嵌入） · 远程/本地 MCP 服务 · 示例 xxl-ai-sample （可选）            │
    └──────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 四、安装部署

XXL-AI 是一个「**云本结合**」的 AI Agent 开发平台，提供两种同源同品牌、能力互补的交付形态，可按团队规模与使用场景选用合适版本安装和部署。

### 4.1  [云版（ Web 服务端）] 

XXL-AI 云版项目，支持 Docker Compose 一键部署，部署脚本如下：

        # 第一步：代码 clone 本部 + 前往仓库目录
        git clone https://github.com/xuxueli/xxl-ai.git
        cd ./xxl-ai

        # 第二步：构建前端并同步产物（ npm run build 构建 dist ，npm run sync:dist 复制到 xxl-ai-api 静态资源目录）
        cd xxl-ai-ui && npm install && npm run build && npm run sync:dist && cd ..

        # 第三步：构建后端
        mvn clean package

        # 第四步：进入 docker 目录（支持自定义 .env 配置，如修改 MYSQL_PATH 配置设置 Mysql 数据持久化目录）
        cd ./docker/
        cat .env

        # 第五步：启动/停止项目
        docker compose up -d
        docker compose down

### 4.2  [本地版（ Desk 桌面端）] 

XXL-AI 本地版项目，支持跨平台客户端一键安装，下载对应版本（如 mac/win ）安装程序即可。

*   **下载地址**：

### 五、核心功能操作指南

### 5.1  [本地版（ Desk 桌面端）] 

*   安装并打开 Desk 客户端

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/178218b024054af3b3dc0ad4e21ee220~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=zjcRPZ81crkG2doX91hDomnMhH8%3D)

*   配置供应商模型

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/a8fe8481fef44c45bc5b88a9a9a19718~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=aBS50XXt9Di1zRmbRtS2j5dmr0s%3D)

*   使用示例：Desk 客户端/Agent 通过 本地系统能力（ Node/Python ）进行文件操作。

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/25e688b8979f476eb39add1de02e2275~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=s44%2BZlhtB6CQ%2BKregRzd%2B6eCzvw%3D)

### 5.3  [云版（ Web 服务端）] 

*   登录工作台

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/cfed048359874a4c8ff2ced9238c0d88~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=a3og1WeXQx3znafNBgWwqMmf0EY%3D)

*   编排 Agent

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/c7167e7141254e3fabe94ca4b86443c9~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=oNodGADeT8475N%2FJnFeNAHXmxQE%3D)

*   发布 Agent

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/fd29bc55335e48d1a53332d9e1953b95~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=uJjMfMtzNRXmMH0YTXFKtniZqyk%3D)

*   使用示例：Agent 调用 MCP 工具（网页抓取）汇总「今日热点社会新闻」

![image.png]( https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/7f8ae3e756794eb6a7051f0440a50588~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=aSuYXPGF2ZpknuTzSwDpbnpeP9Q%3D)

## 关联链接

- https://github.com/xuxueli/xxl-ai.git
- https://github.com/xuxueli/xxl-ai/releases
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/178218b024054af3b3dc0ad4e21ee220~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=zjcRPZ81crkG2doX91hDomnMhH8%3D
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/25e688b8979f476eb39add1de02e2275~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=s44%2BZlhtB6CQ%2BKregRzd%2B6eCzvw%3D
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/7f8ae3e756794eb6a7051f0440a50588~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=aSuYXPGF2ZpknuTzSwDpbnpeP9Q%3D
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/a8fe8481fef44c45bc5b88a9a9a19718~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=aBS50XXt9Di1zRmbRtS2j5dmr0s%3D
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/c7167e7141254e3fabe94ca4b86443c9~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=oNodGADeT8475N%2FJnFeNAHXmxQE%3D
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/cfed048359874a4c8ff2ced9238c0d88~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=a3og1WeXQx3znafNBgWwqMmf0EY%3D
- https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/fd29bc55335e48d1a53332d9e1953b95~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg6K646Zuq6YeM:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMjU0NzQyNDI2ODE1NDA1In0%3D&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1792082151&x-orig-sign=uJjMfMtzNRXmMH0YTXFKtniZqyk%3D
- https://www.xuxueli.com/xxl-ai/

## 导航

- 项目页：[[10-项目/github.com_a83c2c17]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
