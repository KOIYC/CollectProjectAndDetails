---
type: "corpus"
item_id: "157b40dcb4ee0332"
title: "2026 iPhone 侧载保姆级教程： AltStore PAL + LiveContainer/SideStore 双方案"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1242884"
project_url: "https://altstore.io/"
author: "2385347602"
published_at: "2026-09-18T02:22:59"
captured_at: "2026-09-20T09:52:10+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - v2ex
  - 8
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 2026 iPhone 侧载保姆级教程： AltStore PAL + LiveContainer/SideStore 双方案

> [!info] 一句话导读
> 最近折腾了一圈 iPhone 侧载，把 AltStore PAL 、SideStore 、LiveContainer 基本弄明白了。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1242884>
> 指标：回复=0
> 作者：2385347602　|　发布：2026-09-18T02:22:59
> 项目链接：<https://altstore.io/>
> 采集：2026-09-20T09:52:10+08:00　|　id：`157b40dcb4ee0332`

## 正文

最近折腾了一圈 iPhone 侧载，把 AltStore PAL 、SideStore 、LiveContainer 基本弄明白了。

网上最大的问题是很多教程把这几个东西混在一起讲。

实际上目前比较值得折腾的是两套完全不同的方案：

**方案 A：AltStore PAL**

优点：Apple 官方第三方 Marketplace 机制、不用 7 天续签、没有免费开发者账号传统 3 App 限制。

缺点：**不能拿任意 `.ipa` 直接安装。**

**方案 B：LiveContainer + SideStore 一体版**

优点：自己下载的 IPA 可以导入 LiveContainer 运行，非常适合开源 App 、阅读器、漫画 App 、小众工具、模拟器等。

缺点：宿主仍然使用开发者签名，需要定期刷新，而且不是所有 IPA 都兼容。

我的建议不是二选一，而是：

**App Store + AltStore PAL + LiveContainer/SideStore 共存。**

下面从零开始。

---

# 一、先搞清楚最终能实现什么

安装完成以后，你的 iPhone 可以变成：

iPhone

├── App Store  
│　├── 微信  
│　├── B 站  
│　└── 正常 App  
│  
├── AltStore PAL  
│　└── Apple Alternative Marketplace 应用  
│  
└── LiveContainer + SideStore  
　　├── VReader  
　　├── Aidoku  
　　├── 各种开源 App  
　　├── 模拟器  
　　├── 自己的测试 IPA  
　　└── 其他兼容 IPA

简单理解：

**App Store = 苹果官方商店**

**AltStore PAL = Apple 允许的第三方商店**

**SideStore = 开发者签名/刷新工具**

**LiveContainer = IPA 容器**

真正实现：

“我手里有一个 IPA ，我想自己运行”

主要靠最后两个。

---

# 二、方案 A：安装 AltStore PAL

## 需要什么？

目前 AltStore PAL 官方要求：

1. iPhone/iPad
2. iOS/iPadOS 18+
3. 实际位于欧盟、日本或巴西
4. App Store 登录对应地区 Apple Account
5. Safari 、Chrome 或 Vivaldi

AltStore PAL：

https://altstore.io/download

Apple Alternative App Distribution 官方说明：

https://support.apple.com/118110

注意：

网上存在“修改 WLOC 定位 + 对应地区 IP + 对应地区 Apple Account”的玩法。

这是社区方案，不是 Apple 官方保证的方法。

Apple 并没有公布“GPS + IP + Apple ID”三项检测公式，所以即使别人成功，也不能保证换一台手机、换一个系统版本仍然成功。

---

## 第一步：确认资格

以日本为例。

你需要符合日本 Alternative Marketplace 的资格条件，并登录日本地区 App Store 账号。

然后用 Safari 打开：

https://altstore.io/download

找到：

**AltStore PAL**

点击 Download 。

---

## 第二步：允许安装 Marketplace

第一次点击以后，iOS 通常不会直接安装。

进入：

设置

→ 顶部出现类似

**Allow Marketplace From AltStore LLC**

点击：

**Allow**

然后重新回到：

https://altstore.io/download

再次点击 Download 。

这次应该出现：

**Install App Marketplace**

确认安装。

成功以后，桌面出现：

**AltStore**

这就是 PAL 。

---

## 第三步：怎么用 PAL ？

使用方式和 App Store 很接近。

打开：

AltStore PAL

→ 找应用

→ Install

→ 安装

最大的好处是：

**不用每 7 天重新签名。**

但千万注意：

AltStore PAL **不能把网上随便下载的 xxx.ipa 直接安装进去。**

所以如果你的目标是：

“GitHub 下载 IPA → 安装”

继续看下面。

---

# 三、方案 B：LiveContainer + SideStore 一体版

这套才是折腾 IPA 的重点。

它的逻辑是：

Apple 免费开发者签名

↓

LiveContainer + SideStore

↓

LiveContainer 内运行 Guest Apps

↓

Reader.ipa / Manga.ipa / Tool.ipa / Emulator.ipa……

相比“SideStore + LiveContainer 分开安装”，推荐直接用：

**LiveContainer + SideStore 一体版**

因为二者可以共享一个免费 App 槽位。

---

# 四、需要准备什么

iPhone：

iOS 15+

电脑：

Windows 8+

macOS High Sierra+

或者 Linux 。

另外需要：

**Apple Account**

**Wi-Fi**

**数据线**

**LocalDevVPN**

Windows 用户还需要 Apple 设备通信驱动。

建议第一次操作预留半小时。

---

# 五、所有官方下载地址

## 1. SideStore

官网：

https://sidestore.io/

官方安装文档：

https://docs.sidestore.io/docs/installation/install

中文：

https://docs.sidestore.io/zh/docs/installation/install

准备工作：

https://docs.sidestore.io/docs/installation/prerequisites

---

## 2. LiveContainer

官方 GitHub：

https://github.com/LiveContainer/LiveContainer

官方 Releases：

https://github.com/LiveContainer/LiveContainer/releases

官方文档：

https://livecontainer.github.io/

中文版：

https://livecontainer.github.io/zh-CN/

LiveContainer + SideStore 教程：

https://livecontainer.github.io/zh-CN/docs/installation/lc_sidestore

---

## 3. LiveContainer + SideStore 一体版 IPA

稳定版直接下载：

https://github.com/LiveContainer/LiveContainer/releases/latest/download/LiveContainer+SideStore.ipa

Nightly：

https://github.com/LiveContainer/LiveContainer/releases/download/nightly/LiveContainer+SideStore.ipa

小白：

**直接稳定版。**

不要没事追 Nightly 。

---

## 4. LocalDevVPN

直接在：

**Apple App Store 搜索 LocalDevVPN**

安装。

SideStore 安装、更新和刷新 App 时需要连接 LocalDevVPN 。

---

# 六、Windows 用户安装前准备

如果你是 Windows：

先安装 iTunes/Apple 相关驱动，让电脑能够正常识别 iPhone 。

然后：

数据线连接 iPhone

↓

iPhone 弹出

“是否信任此电脑？”

↓

点击

**信任**

↓

输入手机密码。

电脑必须能够正常识别 iPhone ，再继续。

---

# 七、使用 iloader 安装一体版

SideStore 当前官方推荐的首次安装工具之一是：

**iloader**

按照 SideStore 官方 prerequisites 页面下载最新版：

https://docs.sidestore.io/docs/installation/prerequisites

打开 iloader 。

然后：

1. USB 连接 iPhone
2. 登录 Apple Account
3. 选择自己的 iPhone
4. 选择安装应用

普通教程会让你选择：

**Install SideStore**

我们这里不要选这个。

选择：

**LiveContainer+SideStore**

等待安装完成。

如果 iloader 版本太老，可能无法正确签名 LiveContainer ，所以不要从百度网盘或者论坛附件下载几个月前的 iloader 。

直接跟官方文档走。

---

# 八、iPhone 信任开发者

安装完成以后如果直接打开报错，很正常。

进入：

设置

→ 通用

→ VPN 与设备管理

→ 开发者 App

→ 找到自己的 Apple Account

→ 信任

然后进入：

设置

→ 隐私与安全性

→ 开发者模式

→ 打开

iPhone 会要求重启。

重启后再次确认开发者模式。

---

# 九、配置 LocalDevVPN

打开：

**LocalDevVPN**

第一次会弹出：

Allow VPN Configurations

点击：

**Allow**

输入手机密码。

然后：

**Connect**

以后只要 SideStore 需要：

安装

更新

刷新

都应该先保证：

**Wi-Fi + LocalDevVPN**

处于正常状态。

注意：

LocalDevVPN 不是普通“科学上网 VPN”。

它主要是给 SideStore 与设备内部服务通信使用的。

---

# 十、配置内置 SideStore

打开：

**LiveContainer**

进入 Apps 页面。

左上角应该可以进入：

**SideStore**

第一次进入 SideStore：

Settings

→ 登录刚才 iloader 使用的 Apple Account

然后：

LocalDevVPN → Connect

再进入：

SideStore

→ My Apps

→ Refresh All

如果看到类似：

**7 DAYS**

并且刷新成功：

恭喜，SideStore 部分基本搞定。

这里的 7 DAYS 就是签名剩余时间。

不要等到 0 天再想起来刷新。

---

# 十一、配置 LiveContainer 的 JIT-Less

这一步非常重要。

回到：

LiveContainer

→ Settings

→ Import Certificate from SideStore

点击。

SideStore 会请求导出签名证书。

允许。

成功以后：

**Import Certificate**

应该变成类似：

**Remove Certificate**

然后：

LiveContainer

→ Settings

→ JIT-Less Mode Diagnose

→ Test JIT-Less Mode

如果显示：

**JIT-Less Mode Test Passed**

基本毕业。

这意味着很多普通 Guest App 不需要你每次折腾 JIT 才能启动。

---

# 十二、怎么安装一个 IPA ？

这部分非常简单。

假设下载：

**Aidoku.ipa**

Safari 下载以后通常进入：

文件 App

→ 下载项

然后：

打开 LiveContainer

→ 右上角 +

→ 选择 Aidoku.ipa

→ Import / Install

完成。

以后：

LiveContainer

→ Apps

→ Aidoku

→ Run

就能运行。

所以日常流程基本就是：

Safari / GitHub

↓

下载 xxx.ipa

↓

文件

↓

LiveContainer

↓

+

↓

选择 IPA

↓

运行

---

# 十三、能不能把 Guest App 放桌面？

可以。

LiveContainer 支持通过快捷指令创建启动入口。

所以最后桌面可以做成：

Aidoku

VReader

某游戏

某工具

……

点桌面图标后调用 LiveContainer 启动对应 Guest App 。

这样视觉上已经很接近普通 App 。

官方教程：

https://livecontainer.github.io/docs/guides/add-to-home-screen

---

# 十四、推荐 IPA：小说阅读

这里开始是我认为真正值得折腾的部分。

不要为了“能侧载”就装几十个垃圾 App 。

---

## ① VReader

GitHub：

https://github.com/lllyys/vreader

这是一个原生 iOS 阅读器项目。

支持：

EPUB

AZW3/MOBI

PDF

TXT

Markdown

以及：

TTS

注释

全文搜索

AI Assistant

WebDAV

书源等功能。

如果你想把 iPhone 变成真正的小说阅读器，这种项目比“某某小说破解版”更值得研究。

下载方法：

打开 GitHub 项目

→ Releases

→ 找 `.ipa`

→ 下载

→ LiveContainer 导入。

如果当前 Release 没提供预编译 IPA ，就不要去不明网站找别人魔改的版本，等官方 Release 或自己构建。

---

# 十五、推荐 IPA：漫画

## ② Aidoku

这是我比较推荐的 iOS 漫画阅读器。

官方 GitHub：

https://github.com/Aidoku/Aidoku

官方 Releases：

https://github.com/Aidoku/Aidoku/releases

Release 页面会直接提供：

**Aidoku.ipa**

支持：

漫画阅读

CBZ 本地漫画

下载

Komga

Kavita

Suwayomi

外部 Source

AniList

MyAnimeList

Bangumi 等追踪功能。

下载：

GitHub Releases

↓

最新版

↓

Assets

↓

**Aidoku.ipa**

↓

文件

↓

LiveContainer

↓

+

↓

Aidoku.ipa

Aidoku 官方自己就明确提供 IPA ，所以比网上那些不知道谁重新打包的“漫画神器”靠谱得多。

需要特别注意：

**Aidoku 官方明确说明 AltStore PAL 不支持。**

所以它反而非常适合：

**LiveContainer / SideStore**

这就是为什么 PAL 不能完全替代 LiveContainer 。

---

# 十六、影视：先搞清楚“播放器”和“盗版资源 App”

影视类我建议走：

**客户端 + 自己合法拥有/获授权的媒体服务器或媒体文件**

而不是去装来历不明的“免费看全网 VIP”魔改 IPA 。

---

## ③ Swiftfin

如果你用 Jellyfin：

Swiftfin 非常值得装。

官方 GitHub：

https://github.com/jellyfin/Swiftfin

它是原生 Jellyfin iOS/tvOS 客户端。

支持：

Jellyfin 媒体库

Native Player

VLC Player

iPhone/iPad/tvOS

如果官方 App Store / TestFlight 能满足需求：

**直接官方渠道安装。**

没必要为了侧载而侧载。

---

## ④ VLC

本地影视播放：

**VLC**

非常经典。

支持大量视频/音频格式、网络流媒体、本地文件。

如果 App Store 能直接安装：

**App Store 安装。**

理由还是一样：

侧载是解决限制的手段，不是人生目标。

正常渠道已经能解决的问题，不要额外制造维护成本。

---

# 十七、我的推荐组合

如果主要需求是：

**小说 + 漫画 + 动漫/影视**

我会这样装：

小说：

**VReader**

漫画：

**Aidoku**

自己的 Jellyfin：

**Swiftfin**

自己的 Emby：

**官方 Emby 客户端优先**

本地视频：

**VLC**

模拟器：

**Delta / PPSSPP 等正规或官方开源项目**

最终：

iPhone

├── 小说  
│　└── VReader  
│  
├── 漫画  
│　└── Aidoku  
│  
├── 影视  
│　├── VLC  
│　├── Swiftfin  
│　└── Emby  
│  
├── 模拟器  
│　├── Delta  
│　└── PPSSPP  
│  
└── LiveContainer  
　　└── 其他 IPA

这样已经够玩很久了。

---

# 十八、不要乱装这些东西

看到：

“永久 VIP”

“破解付费”

“全网影视”

“免登录”

“去广告增强版”

“内购破解”

“证书永久”

“大神魔改”

先别兴奋。

IPA 可以被重新打包。

你根本不知道里面加了什么。

尤其不要在来源不明 IPA 中登录：

Apple Account

邮箱主账号

Telegram 主账号

银行

支付宝

密码管理器

加密货币钱包

公司账号

重要社交账号。

推荐来源优先级：

**开发者官方网站**

↓

**开发者官方 GitHub Releases**

↓

**项目官方 AltStore Source / TestFlight**

↓

**自己从开源代码构建**

↓

**可信社区**

↓

**来历不明 IPA 站**

越往下风险越高。

---

# 十九、常见问题

## Q1：为什么 SideStore 显示 7 DAYS ？

免费 Apple 开发者签名有有效期。

需要定期 Refresh 。

---

## Q2：刷新为什么失败？

先检查：

Wi-Fi 是否连接

↓

LocalDevVPN 是否 Connect

↓

Apple Account 是否正常

↓

SideStore 是否登录

↓

pairing 是否失效。

---

## Q3：升级 iOS 后突然不能用了？

SideStore 的 pairing file 可能失效。

重新按照官方教程处理 pairing 。

---

## Q4：为什么某个 IPA 导入后打不开？

LiveContainer 不是越狱。

有些 App 依赖：

特殊 Entitlement

App Extension

VPN

Widget

推送

特殊后台服务

Apple 系统 Framework

特殊 DRM

这类 App 不一定兼容。

---

## Q5：所有 IPA 都应该装 LiveContainer 吗？

不是。

推荐：

App Store 有正版

→ App Store

AltStore PAL 有正式版本

→ PAL

普通开源 IPA

→ LiveContainer

LiveContainer 不兼容

→ 考虑 SideStore 独立安装

这才是最省事的方案。

---

# 二十、最终效果

全部配置完成以后，你得到的不是“越狱 iPhone”。

而是：

**正常 iOS + 官方第三方 Marketplace + 开发者侧载 + IPA Container**

也就是：

App Store

+

AltStore PAL

+

LiveContainer

+

SideStore

四套能力互补。

如果你的核心目标是：

“我拿到一个可信 IPA ，就希望自己在 iPhone 上运行。”

目前最值得先搞定的是：

**LiveContainer + SideStore 。**

如果你满足 Alternative Marketplace 的官方地区资格：

再装：

**AltStore PAL 。**

不要反过来。

因为 PAL 虽然更省心，但它解决不了“任意 IPA 导入”这个需求。

---

# 官方地址汇总

AltStore：

https://altstore.io/

AltStore PAL 下载：

https://altstore.io/download

SideStore：

https://sidestore.io/

SideStore 安装：

https://docs.sidestore.io/docs/installation/install

SideStore 中文安装：

https://docs.sidestore.io/zh/docs/installation/install

LiveContainer：

https://github.com/LiveContainer/LiveContainer

LiveContainer Releases：

https://github.com/LiveContainer/LiveContainer/releases

LiveContainer 官方文档：

https://livecontainer.github.io/

LiveContainer 中文文档：

https://livecontainer.github.io/zh-CN/

LiveContainer + SideStore：

https://livecontainer.github.io/zh-CN/docs/installation/lc_sidestore

LiveContainer + SideStore 稳定版 IPA：

https://github.com/LiveContainer/LiveContainer/releases/latest/download/LiveContainer+SideStore.ipa

Aidoku：

https://github.com/Aidoku/Aidoku

Aidoku Releases / IPA：

https://github.com/Aidoku/Aidoku/releases

VReader：

https://github.com/lllyys/vreader

Swiftfin：

https://github.com/jellyfin/Swiftfin

所有版本、系统要求和安装方式，都建议以项目官方文档的最新说明为准。

尤其是 SideStore 、LiveContainer 和 iOS 更新都很快，看到一两年前还让你装一堆旧工具的教程，先看发布日期。

## 关联链接

- https://altstore.io/download
- https://docs.sidestore.io/docs/installation/install
- https://docs.sidestore.io/docs/installation/prerequisites
- https://docs.sidestore.io/zh/docs/installation/install
- https://github.com/Aidoku/Aidoku
- https://github.com/Aidoku/Aidoku/releases
- https://github.com/LiveContainer/LiveContainer
- https://github.com/LiveContainer/LiveContainer/releases
- https://github.com/LiveContainer/LiveContainer/releases/download/nightly/LiveContainer+SideStore.ipa
- https://github.com/LiveContainer/LiveContainer/releases/latest/download/LiveContainer+SideStore.ipa
- https://github.com/jellyfin/Swiftfin
- https://github.com/lllyys/vreader
- https://livecontainer.github.io/
- https://livecontainer.github.io/docs/guides/add-to-home-screen
- https://livecontainer.github.io/zh-CN/
- https://livecontainer.github.io/zh-CN/docs/installation/lc_sidestore
- https://sidestore.io/
- https://support.apple.com/118110

## 导航

- 项目页：[[10-项目/altstore.io_a470ad8a]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
