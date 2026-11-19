---
type: "project"
title: "CardputerZero 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）"
project_url: "https://api.github.com/repos/xjasonlyu/tun2socks/releases/latest"
first_seen: "2026-11-19T09:46:37+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 22
lang: "zh"
---

# CardputerZero 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）

> [!info] 一句话导读
> 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://api.github.com/repos/xjasonlyu/tun2socks/releases/latest>
> 首次收录：2026-11-19T09:46:37+08:00
> 来源渠道：V2EX
> 标签：22
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-19T09:46:37+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-19/65d2665fa0095664_CardputerZero-通过-USB-ADB-实现-Linux-设备全系统共享-Mac-网络(a]] |

## 摘要正文

# 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）  > **适用环境：** Linux 开发板（如 CardputerZero / Debian 13 / ARM64） + macOS 宿主机（已通过 USB ADB 连接，本地代理运行在 `7890` 端口） > > **实现效果：** 无需配置 Wi-Fi，仅凭一根 USB 数据线即可让 Linux 设备的**全系统（包括桌面 GUI App、系统设置、命令行工具）**透明联网，并在 macOS 上封装为一键“开启 / 关闭”的原生 `.app` 工具。  ---  ## 一、 方案背景与架构设计  在没有 Wi-Fi 或无法连接无线网络的场景下，通常可以通过 `adb reverse tcp:17890 tcp:7890` 将设备本地端口映射到 Mac 的网络代理端口，再在终端里设置 `export http_proxy` 实现命令行联网。但这种基础做法存在四个明显局限：  1. **桌面 GUI App 无法联网：** 图形界面浏览器、桌面应用和系统底层服务通常不读取终端环境变量，甚至完全无视代理配置。 2. **UDP DNS 丢包导致网络极不稳定：** `adb reverse` **仅支持转发 TCP 流量，不支持 UDP**。Linux 系统默认通过 UDP 53 端口发送域名解析请求，数据包进入隧道后会被直接丢弃，导致网页加载卡死或频繁超时。 3. **虚拟网卡网段冲突与分片卡顿：** 若虚拟网卡使用 `198.18.0.0/16` 等常见保留网段，容易与代理软件的 Fake-IP 网段重叠引发路由冲突；同时默认 `1500` MTU 在二次封装后也容易导致大包丢帧。 4. **后台进程随 ADB 退出而终止：** 通过 `adb shell` 启动的普通后台进程在会话结束时容易被系统回收，导致虚拟网卡断开（`NO-CARRIER / state DOWN`）。  ### 核心解决方案与数据流向  为了实现**全系统透明接管**与**秒级稳定解析**，本方案采用三层组合架构：  * **`tun0` + `tun2socks`（全流量透明接管）：** 创建独立网段（`10.254.254.1/30`、`MTU 1400`）的虚拟网卡并设为默认路由，将设备所有 TCP 流量封装进 SOCKS5 通道发往 `127.0.0.1:17890`。 * **本地 DoH（DNS-over-HTTPS）缓存服务：** 在设备本地 `127.0.0.54:53` 运行一个轻量级 Python DNS 代理，接收全系统的 UDP 53 域名查询并转换为走 HTTPS 代理的…
