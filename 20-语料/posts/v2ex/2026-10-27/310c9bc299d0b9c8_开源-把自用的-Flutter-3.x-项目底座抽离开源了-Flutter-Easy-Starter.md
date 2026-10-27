---
type: "corpus"
item_id: "310c9bc299d0b9c8"
title: "[开源] 把自用的 Flutter 3.x 项目底座抽离开源了： Flutter Easy Starter（已处理国内隐私合规守卫 / Token 并发无感刷新 / GoRouter 多栈路由 / 14+ 预置页面）"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252023"
project_url: "https://github.com/reedtang666/flutter-easy-starter"
author: "reedtang666"
published_at: "2026-10-26T12:55:37"
captured_at: "2026-10-27T23:56:38+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-10-27"
pub_day: "2026-10-26"
tags:
  - 语料
  - v2ex
  - 12
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [开源] 把自用的 Flutter 3.x 项目底座抽离开源了： Flutter Easy Starter（已处理国内隐私合规守卫 / Token 并发无感刷新 / GoRouter 多栈路由 / 14+ 预置页面）

> [!info] 一句话导读
> 平时自己做独立开发和客户端交付时，每次新建 Flutter 工程，最耗精力的往往不是写业务页面，而是立项前两周反复折腾那套基建：

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252023>
> 指标：回复=0
> 作者：reedtang666　|　发布：2026-10-26T12:55:37
> 项目链接：<https://github.com/reedtang666/flutter-easy-starter>
> 采集：2026-10-27T23:56:38+08:00　|　id：`310c9bc299d0b9c8`

## 正文

平时自己做独立开发和客户端交付时，每次新建 Flutter 工程，最耗精力的往往不是写业务页面，而是立项前两周反复折腾那套基建：

- 国内应用商店审核必卡的**“点同意隐私政策前，严禁提前获取设备信息或初始化三方 SDK”**；
- 多个请求同时 401 时，怎么用并发锁优雅地做 **Token 无感刷新** 而不触发重复刷新风暴；
- 底部导航栏多 Tab 切换时，怎么用 `GoRouter` 保持各自独立的路由栈，并把**启动页 -> 隐私弹窗 -> 首次引导页 -> 登录态拦截**做成声明式自动守卫；
- 还有 WebSocket 心跳与断线重连、亮/暗双主题持久化、骨架屏、毛玻璃组件……

为了省去每次新开项目从零搭架子的体力活，我把这套打磨好的工程底座整理开源了：**Flutter Easy Starter**。

### 🔗 项目地址
GitHub： https://github.com/reedtang666/flutter-easy-starter
（ MIT 协议开源，如果刚好能帮你省下搭基建的时间，求顺手点个 Star ⭐ 支持一下！）

---

### 🛠️ 重点解决了哪些“脏活累活”？

1. **国内应用市场隐私合规守卫（防审核被拒）**
   完整封装了 `启动页 -> 隐私政策弹窗 -> 首次引导页 -> 登录检查 -> 首页` 的状态流转，严格保证在用户点击“同意隐私政策”之后，才去初始化设备信息与敏感 SDK 。
2. **Dio + `QueuedInterceptorsWrapper` Token 无感续期**
   基于队列拦截器实现了并发锁无感刷新 Token ，多个请求同时过期时自动排队等待新 Token 并重放请求；刷新失败自动清理态并跳回登录页。
3. **GoRouter (`StatefulShellRoute`) 路由守卫**
   底部多分支独立路由栈（切 Tab 不丢状态），支持 Deep Link ，并且把隐私同意态、首次引导态、登录态全部收敛在全局路由 `redirect` 守卫里，不用在业务代码里到处写 `Navigator.push` 判断。
4. **Riverpod (`Notifier`) + 本地状态恢复**
   采用 Feature-first 的 Clean Architecture 分层结构，使用现代 `Notifier` 范式管理状态，配合本地持久化，冷启动自动恢复用户态与主题配置。
5. **WebSocket 实时通信底座**
   内置了带心跳检测、指数退避断线自动重连的 WebSocket 封装。

---

### 📱 不是只有 Counter 的空壳，直接内置了 14+ 预置页面

为了方便直接改造成社交、内容或工具类 App ，模板里用亮/暗双主题 + 毛玻璃（ Glassmorphism ）+ Shimmer 骨架屏预置了一套完整的页面：
- **前置流程**：品牌动画启动页、支持 HTML 渲染的隐私合规弹窗、平滑指示器引导页、多方式登录页（密码/短信/微信 UI ）、资料完善与图片选择页
- **核心 Tab 与业务页**：
  - 介绍/导航中心页、带 Hero 动画的探索/旅游卡片页
  - 消息列表（带 Story 故事环与侧滑操作）& 实时聊天界面
  - 个人中心、VIP 订阅计划页、礼物商店（含购物车逻辑）、我的相册上传管理、帮助与反馈页

---

### 🚀 快速跑起来体验

环境要求 Flutter 3.0+ / Dart 3.0+，无需配置后端即可直接跑通完整 UI 与交互流：

```bash
git clone https://github.com/reedtang666/flutter-easy-starter.git
cd flutter-easy-starter
flutter pub get
flutter run
```

如果你正好准备用 Flutter 起一个新项目，或者想找一个结构清晰的 `Riverpod + GoRouter + Dio` 实战参考模板，欢迎直接拿去用，有任何问题或建议欢迎提 Issue 交流！

## 关联链接

- https://github.com/reedtang666/flutter-easy-starter.git

## 导航

- 项目页：[[10-项目/github.com_cd3a7197]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
