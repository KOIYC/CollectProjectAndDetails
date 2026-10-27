---
type: "corpus"
item_id: "39d30f8825bea998"
title: "DirMerge 2.0.4 正式版：专为 Mac 雕琢的原生文件夹合并工具， APFS 零空间写时复制 + ⌘Z 撤销 + 较新文件保护（送内购码）"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1252179"
project_url: "https://apps.apple.com/app/dirmerge-safe-folder-sync/id6809635885"
author: "jasun"
published_at: "2026-10-27T03:38:24"
captured_at: "2026-10-27T23:56:38+08:00"
lang: "zh"
kind: "post"
topic: "移动 App"
shard: "2026-10-27"
pub_day: "2026-10-27"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# DirMerge 2.0.4 正式版：专为 Mac 雕琢的原生文件夹合并工具， APFS 零空间写时复制 + ⌘Z 撤销 + 较新文件保护（送内购码）

> [!info] 一句话导读
> 各位 V 友大家好，我是独立开发者 jasun 。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1252179>
> 指标：回复=0
> 作者：jasun　|　发布：2026-10-27T03:38:24
> 项目链接：<https://apps.apple.com/app/dirmerge-safe-folder-sync/id6809635885>
> 采集：2026-10-27T23:56:38+08:00　|　id：`39d30f8825bea998`

## 正文

各位 V 友大家好，我是独立开发者 jasun 。

在日常使用 Mac 时，我们常常遇到这样的场景：从外置移动硬盘、摄影 SD 卡或者旧的备份文件夹中，把资料合并整理到本地工作区。
然而 macOS 自带的访达（ Finder ）在处理同名文件夹时让人心惊胆战——一旦点错“替换”，里面的子文件就会被整层抹掉；而用 Beyond Compare 等老牌工具，界面老旧且每次跨目录合并都在对 SSD 进行全量物理读写。

为此，我用 **Swift 6 + SwiftUI** 原生写了这款小巧、纯净的单窗口工具：**DirMerge**。经过一段时间的打磨，今天正式向大家汇报 **v2.0.4 (Build 5)** 版本的上线进展！

---

### 🌟 核心设计与特性

1. **APFS 零空间秒级克隆（ Zero-Space CoW ）**
   在 APFS 文件系统上，DirMerge 直接调用 Darwin 底层的 `copyfile(..., COPYFILE_CLONE)` 系统调用。克隆的是文件指针与 Extents ，即便合并几十 GB 的高分辨率摄影 RAW 图库或开发工程，也仅需数毫秒，且**消耗 0 字节额外物理磁盘空间**，绝不平白磨损 SSD 。
   *(注：当跨磁盘卷如移动硬盘拷入本地时，会自动无缝切换为带缓冲的高精度安全传输)*

2. **较新目标文件防覆盖保护（ Target-Newer Protection ，2.0.4 新特性）**
   合并前自动比对双方修改时间。如果目标文件夹中的文件比源文件修改时间更新，DirMerge 会自动高亮黄色警示并默认跳过，坚决避免使用陈旧备份意外覆盖最新修改进度。

3. **一键 ⌘Z 撤销回滚（ Safe Snapshot Rollback ）**
   在替换目标目录中任何发生冲突的文件前，DirMerge 会在目标卷中建立原子备份快照。万一合并错文件，随时按下 `⌘Z`，被替换的项目瞬时原样复原。

4. **高分辨率屏幕字号缩放（ 2.0.4 新特性）**
   吸纳了前次发帖中 V 友的细致建议，现已提供 100%、115%、130% 三档字号调节，并支持 `⌘+` / `⌘-` 快捷键，在 Studio Display 或 4K/5K 大显示器下显示格外舒适。

5. **极致原生与 100% 离线沙盒**
   - Universal 原生二进制（ Apple Silicon M1-M4 & Intel ），安装包仅 **2.4 MB**，运行时内存占用 <25 MB ；
   - 运行于 Apple 严格沙盒内，**未申领任何网络访问权限**（ Network Entitlements ），0 数据埋点、0 遥测上报，纯净离线。

---

### 🎁 获取方式与 V 友福利

- 🌐 **官方网站**（含免费版 .dmg 下载与技术细节）： https://dirmerge.com/zh/
- 🍎 **Mac App Store**： https://apps.apple.com/app/dirmerge-safe-folder-sync/id6809635885

**免费版特性**：完全开放核心功能，单次支持合并最多 25 项，体验完整的 APFS 零空间克隆与快照撤销。

**V 友专属福利**：
大家在 App Store 内购界面中，点击“兑换优惠代码”，输入活动兑换码：
👉 `DIRMERGEVIP2026`
即可直接通过苹果官方 App Store 兑换优惠！

另外，**楼内留言交流任何使用感受或建议，我将每隔几楼抽取送出 Pro 终身无门槛兑换码（直接私信发送）**！非常期待听到大家的真实反馈，感谢大家的支持！❤️

## 关联链接

- https://dirmerge.com/zh/

## 导航

- 项目页：[[10-项目/apps.apple.com_55c1a828]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`移动 App`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
