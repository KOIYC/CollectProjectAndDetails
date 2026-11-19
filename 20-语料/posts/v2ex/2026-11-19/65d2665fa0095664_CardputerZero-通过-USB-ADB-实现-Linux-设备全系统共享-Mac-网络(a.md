---
type: "corpus"
item_id: "65d2665fa0095664"
title: "CardputerZero 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1258076"
project_url: "https://api.github.com/repos/xjasonlyu/tun2socks/releases/latest"
author: "jiajia007"
published_at: "2026-11-18T09:55:32"
captured_at: "2026-11-19T09:46:37+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-11-19"
pub_day: "2026-11-18"
tags:
  - 语料
  - v2ex
  - 22
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# CardputerZero 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）

> [!info] 一句话导读
> 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1258076>
> 指标：回复=0
> 作者：jiajia007　|　发布：2026-11-18T09:55:32
> 项目链接：<https://api.github.com/repos/xjasonlyu/tun2socks/releases/latest>
> 采集：2026-11-19T09:46:37+08:00　|　id：`65d2665fa0095664`

## 正文

# 通过 USB ADB 实现 Linux 设备全系统共享 Mac 网络（adb reverse + tun2socks + 本地 DoH）

> **适用环境：** Linux 开发板（如 CardputerZero / Debian 13 / ARM64） + macOS 宿主机（已通过 USB ADB 连接，本地代理运行在 `7890` 端口）
>
> **实现效果：** 无需配置 Wi-Fi，仅凭一根 USB 数据线即可让 Linux 设备的**全系统（包括桌面 GUI App、系统设置、命令行工具）**透明联网，并在 macOS 上封装为一键“开启 / 关闭”的原生 `.app` 工具。

---

## 一、 方案背景与架构设计

在没有 Wi-Fi 或无法连接无线网络的场景下，通常可以通过 `adb reverse tcp:17890 tcp:7890` 将设备本地端口映射到 Mac 的网络代理端口，再在终端里设置 `export http_proxy` 实现命令行联网。但这种基础做法存在四个明显局限：

1. **桌面 GUI App 无法联网：** 图形界面浏览器、桌面应用和系统底层服务通常不读取终端环境变量，甚至完全无视代理配置。
2. **UDP DNS 丢包导致网络极不稳定：** `adb reverse` **仅支持转发 TCP 流量，不支持 UDP**。Linux 系统默认通过 UDP 53 端口发送域名解析请求，数据包进入隧道后会被直接丢弃，导致网页加载卡死或频繁超时。
3. **虚拟网卡网段冲突与分片卡顿：** 若虚拟网卡使用 `198.18.0.0/16` 等常见保留网段，容易与代理软件的 Fake-IP 网段重叠引发路由冲突；同时默认 `1500` MTU 在二次封装后也容易导致大包丢帧。
4. **后台进程随 ADB 退出而终止：** 通过 `adb shell` 启动的普通后台进程在会话结束时容易被系统回收，导致虚拟网卡断开（`NO-CARRIER / state DOWN`）。

### 核心解决方案与数据流向

为了实现**全系统透明接管**与**秒级稳定解析**，本方案采用三层组合架构：

* **`tun0` + `tun2socks`（全流量透明接管）：** 创建独立网段（`10.254.254.1/30`、`MTU 1400`）的虚拟网卡并设为默认路由，将设备所有 TCP 流量封装进 SOCKS5 通道发往 `127.0.0.1:17890`。
* **本地 DoH（DNS-over-HTTPS）缓存服务：** 在设备本地 `127.0.0.54:53` 运行一个轻量级 Python DNS 代理，接收全系统的 UDP 53 域名查询并转换为走 HTTPS 代理的 POST 请求（内置内存缓存），彻底绕过 `adb reverse` 不支持 UDP 的限制。
* **`systemd-run` 进程托管：** 使用系统服务管理器独立拉起隧道与 DNS 进程，确保稳定运行，关闭时一键清理路由与还原系统配置。

```text
[Linux 桌面 GUI App / 系统设置 / 终端命令]
        │
        ├─── 域名解析 (UDP 53) ──▶ [127.0.0.54:53 本地 DoH 缓存服务 (cardputer-dns)]
        │                                  │ (转为标准 HTTPS POST 请求)
        └─── 全部 IP 流量 ───────▶ [tun0 虚拟网卡 (10.254.254.1/30, MTU 1400)]
                                           │
                                           ▼
                              [tun2socks 服务 (cardputer-tun)]
                                           │ (封装为 SOCKS5 / TCP)
                                           ▼
                              [设备本地 127.0.0.1:17890]
                                           │
                                    ══ USB 数据线 ══
                                    (adb reverse)
                                           │
                                           ▼
                              [macOS 127.0.0.1:7890 代理端口] ──▶ 互联网
```

---

## 二、 完整部署步骤

### 第 1 步：在 Linux 设备上安装 `tun2socks`

连接 USB 数据线后，先在 Mac 终端临时执行一次 `adb reverse tcp:17890 tcp:7890` 打通下载通道，随后在 **Linux 设备（如 CardputerZero）的 root 终端**中安装 ARM64 架构的 `tun2socks`：

```bash
export https_proxy="http://127.0.0.1:17890"
URL=$(curl -sL https://api.github.com/repos/xjasonlyu/tun2socks/releases/latest | grep -oE 'https://[^"]+tun2socks-linux-arm64\.zip' | head -n 1)
curl -L "$URL" -o /tmp/tun2socks.zip
python3 -m zipfile -e /tmp/tun2socks.zip /usr/local/bin/
mv /usr/local/bin/tun2socks-linux-arm64 /usr/local/bin/tun2socks
chmod +x /usr/local/bin/tun2socks
rm -f /tmp/tun2socks.zip

# 验证安装（注意 v2.7+ 版本使用双横线参数 --device 和 --proxy）
tun2socks -v
```

### 第 2 步：在 macOS 上创建一键控制脚本

打开 **Mac 自身的终端**，执行以下命令生成 `~/.local/bin/cardputer-net`。该脚本支持 `status`、`on`、`off` 三种指令，自动完成端口转发、DoH 服务部署、虚拟网卡配置及关闭时的环境还原：

```bash
mkdir -p ~/.local/bin

cat << 'SCRIPT_EOF' > ~/.local/bin/cardputer-net
#!/bin/bash
export PATH="/opt/homebrew/bin:/usr/local/bin:$HOME/Library/Android/sdk/platform-tools:$PATH"

ACTION="${1:-status}"

if ! command -v adb >/dev/null 2>&1; then
  [ "$ACTION" = "status" ] && echo "未找到 adb 命令" && exit 0
  osascript -e 'display notification "未找到 adb 命令，请检查安装路径" with title "CardputerZero 网络"'
  exit 0
fi

if ! adb get-state >/dev/null 2>&1; then
  [ "$ACTION" = "status" ] && echo "未检测到 USB 设备" && exit 0
  osascript -e 'display notification "未检测到设备，请检查 USB 数据线连接" with title "CardputerZero 网络"'
  exit 0
fi

case "$ACTION" in
  status)
    if adb reverse --list | grep -q "tcp:17890"; then
      echo "已开启（tun0 + DoH 缓存隧道运行中）"
    else
      echo "已关闭"
    fi
    ;;
  on)
    adb reverse tcp:17890 tcp:7890
    adb shell '
# 1. 清理旧服务与残留网卡
systemctl stop cardputer-dns cardputer-tun 2>/dev/null || true
pkill -x tun2socks 2>/dev/null || true
ip link del tun0 2>/dev/null || true

# 2. 部署本地 DoH (DNS-over-HTTPS) 缓存解析服务（监听独立地址 127.0.0.54:53）
cat << "PYEOF" > /usr/local/bin/cardputer-dns.py
#!/usr/bin/env python3
import socket, threading, time, urllib.request

PROXY = urllib.request.ProxyHandler({"http": "http://127.0.0.1:17890", "https": "http://127.0.0.1:17890"})
OPENER = urllib.request.build_opener(PROXY)
URLS = ["https://223.5.5.5/dns-query", "https://1.1.1.1/dns-query"]
CACHE = {}
LOCK = threading.Lock()

def resolve_doh(query):
    if len(query) < 12:
        return None
    txid = query[:2]
    key = query[2:]
    now = time.time()
    with LOCK:
        cached = CACHE.get(key)
        if cached and cached[1] > now:
            return txid + cached[0]
    payload = b"\x00\x00" + key
    for url in URLS:
        try:
            req = urllib.request.Request(
                url,
                data=payload,
                headers={"Content-Type": "application/dns-message", "Accept": "application/dns-message"},
                method="POST"
            )
            with OPENER.open(req, timeout=4) as resp:
                body = resp.read()
                if len(body) >= 12:
                    with LOCK:
                        CACHE[key] = (body[2:], now + 120)
                    return txid + body[2:]
        except Exception:
            continue
    return None

def handle(sock, data, addr):
    ans = resolve_doh(data)
    if ans:
        sock.sendto(ans, addr)

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(("127.0.0.54", 53))
    while True:
        data, addr = sock.recvfrom(4096)
        threading.Thread(target=handle, args=(sock, data, addr), daemon=True).start()

if __name__ == "__main__":
    main()
PYEOF
chmod +x /usr/local/bin/cardputer-dns.py

# 3. 创建无网段冲突的虚拟网卡 (10.254.254.1/30) 并使用 systemd 托管服务
ip tuntap add mode tun dev tun0
ip addr add 10.254.254.1/30 dev tun0
ip link set dev tun0 mtu 1400 up
systemd-run --unit=cardputer-tun /usr/local/bin/tun2socks --device tun0 --mtu 1400 --proxy socks5://127.0.0.1:17890
systemd-run --unit=cardputer-dns /usr/bin/python3 /usr/local/bin/cardputer-dns.py
sleep 1

# 4. 接管默认路由与系统 DNS
ip route replace default dev tun0 metric 50
[ -f /etc/resolv.conf ] && [ ! -f /etc/resolv.conf.cardputer-bak ] && cp -L /etc/resolv.conf /etc/resolv.conf.cardputer-bak 2>/dev/null || true
printf "nameserver 127.0.0.54\n" > /etc/resolv.conf
'
    osascript -e 'display notification "全设备虚拟网卡与 DoH 缓存解析已开启" with title "CardputerZero 网络" subtitle "当前状态：已开启"'
    ;;
  off)
    adb shell '
ip route del default dev tun0 2>/dev/null || true
systemctl stop cardputer-dns cardputer-tun 2>/dev/null || true
pkill -x tun2socks 2>/dev/null || true
ip link del tun0 2>/dev/null || true
[ -f /etc/resolv.conf.cardputer-bak ] && mv -f /etc/resolv.conf.cardputer-bak /etc/resolv.conf || true
rm -f /etc/apt/apt.conf.d/99proxy /etc/profile.d/proxy.sh
sed -i "/127\.0\.0\.1:17890/d" /etc/environment 2>/dev/null || true
'
    adb reverse --remove tcp:17890 >/dev/null 2>&1 || true
    osascript -e 'display notification "虚拟网卡、DNS 服务与端口转发已关闭" with title "CardputerZero 网络" subtitle "当前状态：已关闭"'
    ;;
esac
SCRIPT_EOF

chmod +x ~/.local/bin/cardputer-net
```

### 第 3 步：打包为原生 macOS 一键“开 / 关”应用

继续在 **Mac 终端**中运行以下命令，利用系统自带的 `osacompile` 在 `/Applications` 目录下生成 **`Cardputer联网.app`**：

```bash
rm -rf "/Applications/Cardputer联网.app"

cat << 'APPLESCRIPT_EOF' > /tmp/cardputer_net.applescript
set statusText to do shell script "$HOME/.local/bin/cardputer-net status"
set userChoice to button returned of (display dialog "CardputerZero 全设备网络共享（USB 隧道）" & return & return & "当前状态：" & statusText buttons {"取消", "关闭", "开启"} default button "开启" cancel button "取消" with title "CardputerZero 网络")
if userChoice is "开启" then
    do shell script "$HOME/.local/bin/cardputer-net on"
else if userChoice is "关闭" then
    do shell script "$HOME/.local/bin/cardputer-net off"
end if
APPLESCRIPT_EOF

osacompile -o "/Applications/Cardputer联网.app" /tmp/cardputer_net.applescript
rm -f /tmp/cardputer_net.applescript
```

生成完成后，打开访达（Finder）进入 **应用程序**，将 **`Cardputer联网`** 拖到屏幕底部的 **程序坞（Dock）** 上即可。

---

## 三、 日常使用与连通性验证

* **一键开启：** 插上 USB 数据线并确保 Mac 代理软件监听在 `7890` 端口，点击程序坞中的 **`Cardputer联网`** 图标，选择 **“开启”**，等待右上角弹出 **`当前状态：已开启`** 系统通知即可。
* **一键关闭：** 准备拔掉 USB 线或改用无线网络前，点击 **`Cardputer联网`** 并选择 **“关闭”**，工具会自动撤销端口转发、清理 `tun0` 默认路由并还原原始 DNS 配置。
* **设备端快速自检命令：**

```bash
# 1. 检查隧道与 DoH 服务是否均处于运行状态（预期输出两行 active）
systemctl is-active cardputer-tun cardputer-dns

# 2. 检查 tun0 虚拟网卡状态（预期包含 LOWER_UP 与 state UP）
ip addr show tun0

# 3. 无需设置任何代理环境变量，直接测试 DNS 解析与 HTTPS 连通性
curl -s -o /dev/null -w "HTTP %{http_code}, DNS耗时 %{time_namelookup}s, 总耗时 %{time_total}s\n" https://deb.debian.org
```

## 关联链接

- http://127.0.0.1:17890
- https://1.1.1.1/dns-query
- https://223.5.5.5/dns-query
- https://[^
- https://deb.debian.org

## 导航

- 项目页：[[10-项目/api.github.com_f3d82d70]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
