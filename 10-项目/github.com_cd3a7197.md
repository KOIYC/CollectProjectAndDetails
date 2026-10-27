---
type: "project"
title: "[开源] 把自用的 Flutter 3.x 项目底座抽离开源了： Flutter Easy Starter（已处理国内隐私合规守卫 / Token 并发无感刷新 / GoRouter 多栈路由 / 14+ 预置页面）"
project_url: "https://github.com/reedtang666/flutter-easy-starter"
first_seen: "2026-10-27T23:56:38+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 12
lang: "zh"
---

# [开源] 把自用的 Flutter 3.x 项目底座抽离开源了： Flutter Easy Starter（已处理国内隐私合规守卫 / Token 并发无感刷新 / GoRouter 多栈路由 / 14+ 预置页面）

> [!info] 一句话导读
> 平时自己做独立开发和客户端交付时，每次新建 Flutter 工程，最耗精力的往往不是写业务页面，而是立项前两周反复折腾那套基建：

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://github.com/reedtang666/flutter-easy-starter>
> 首次收录：2026-10-27T23:56:38+08:00
> 来源渠道：V2EX
> 标签：12
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-27T23:56:38+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-27/310c9bc299d0b9c8_开源-把自用的-Flutter-3.x-项目底座抽离开源了-Flutter-Easy-Starter]] |

## 摘要正文

平时自己做独立开发和客户端交付时，每次新建 Flutter 工程，最耗精力的往往不是写业务页面，而是立项前两周反复折腾那套基建：  - 国内应用商店审核必卡的**“点同意隐私政策前，严禁提前获取设备信息或初始化三方 SDK”**； - 多个请求同时 401 时，怎么用并发锁优雅地做 **Token 无感刷新** 而不触发重复刷新风暴； - 底部导航栏多 Tab 切换时，怎么用 `GoRouter` 保持各自独立的路由栈，并把**启动页 -> 隐私弹窗 -> 首次引导页 -> 登录态拦截**做成声明式自动守卫； - 还有 WebSocket 心跳与断线重连、亮/暗双主题持久化、骨架屏、毛玻璃组件……  为了省去每次新开项目从零搭架子的体力活，我把这套打磨好的工程底座整理开源了：**Flutter Easy Starter**。  ### 🔗 项目地址 GitHub： https://github.com/reedtang666/flutter-easy-starter （ MIT 协议开源，如果刚好能帮你省下搭基建的时间，求顺手点个 Star ⭐ 支持一下！）  ---  ### 🛠️ 重点解决了哪些“脏活累活”？  1. **国内应用市场隐私合规守卫（防审核被拒）**    完整封装了 `启动页 -> 隐私政策弹窗 -> 首次引导页 -> 登录检查 -> 首页` 的状态流转，严格保证在用户点击“同意隐私政策”之后，才去初始化设备信息与敏感 SDK 。 2. **Dio + `QueuedInterceptorsWrapper` Token 无感续期**    基于队列拦截器实现了并发锁无感刷新 Token ，多个请求同时过期时自动排队等待新 Token 并重放请求；刷新失败自动清理态并跳回登录页。 3. **GoRouter (`StatefulShellRoute`) 路由守卫**    底部多分支独立路由栈（切 Tab 不丢状态），支持 Deep Link ，并且把隐私同意态、首次引导态、登录态全部收敛在全局路由 `redirect` 守卫里，不用在业务代码里到处写 `Navigator.push` 判断。 4. **Riverpod (`Notifier`) + 本地状态恢复**    采用 Feature-first 的 Clean Architecture 分层结构，使用现代 `Notifier` 范式管理状态，配合本地持久化，冷启动自动恢复用户态与主题配置。 5. **WebSocket 实时通信底座**    内置了带心跳检测、指数退避断线自动重连的 WebSocket 封装。  ---  ### 📱 不是只有 Counter 的空壳，直接内置了 14+ 预置页面  为了方便直接改…
