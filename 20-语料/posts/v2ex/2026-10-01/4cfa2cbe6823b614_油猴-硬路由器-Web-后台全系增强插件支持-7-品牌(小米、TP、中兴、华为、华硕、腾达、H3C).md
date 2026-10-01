---
type: "corpus"
item_id: "4cfa2cbe6823b614"
title: "[油猴] 硬路由器 Web 后台全系增强插件支持 7 品牌（小米、TP、中兴、华为、华硕、腾达、H3C）"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1245917"
author: "sxguka"
published_at: "2026-09-30T14:33:07"
captured_at: "2026-10-01T09:47:33+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-10-01"
pub_day: "2026-09-30"
tags:
  - 语料
  - v2ex
  - 108
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [油猴] 硬路由器 Web 后台全系增强插件支持 7 品牌（小米、TP、中兴、华为、华硕、腾达、H3C）

> [!info] 一句话导读
> ZTE-Stat_Max

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1245917>
> 指标：回复=0
> 作者：sxguka　|　发布：2026-09-30T14:33:07
> 项目链接：—
> 采集：2026-10-01T09:47:33+08:00　|　id：`4cfa2cbe6823b614`

## 正文

ZTE-Stat_Max | Bro-Stat

 演示

强烈建议搭配实战演示食用：

https://www.bilibili.com/video/BV1PtR7B8ECC/

『无线不能超二定则』（ 提示：地址在简介）



Bro-Stat 是一个致力于改善各大品牌路由器、硬路由原生 Web 后台体验的浏览器扩展组件。目前通用版主要适配并优化 TP-Link （普联）、小米（ MiWiFi ）、华硕 (ASUS/ROG)、华为（或许还有 HONOR ） 等常见品牌的路由器后台，是一款 哥哥科技 开发的一套网络数据遥测与多端转发解决方案。



本脚本通过接管原生 Vue 框架的底层 XML API 数据流，在不破坏官方原有拓扑与结构的前提下，重构了“组网管理”与“接入设备”页面的 UI 布局。引入了梯形积分算法、异常流量雷达以及双轨制流量对齐显示，为网络工程人员和进阶玩家提供。

全屋智能家居平台联动接入插件：Home Assistant 极客集成、UI 增强，硬路由+NPU 最佳伴侣、无需刷机，支持全系 ZTE ！设备列表平铺化，大屏可视化一点通，你所要的，都在这里，无需频繁切换页面…

原生路由器后台通常只能提供最基础的瞬时网速，且数据往往在设备掉线或路由器重启后直接清零。我们希望通过这套轻量级的组件，为你提供更持久、更直观的家庭网络流量可视化面板→支持定期导出.csv 数据。

中兴路由器 Web UI 增强插件，已验证：星云 MAX 全屋 2.5G 有线主路由/BE 5100Pro+ ！分别统计上下行流量，查看流量占比速率、上下比值，打击 P2P 偷上行，支持 1000/1024 进制，支持 Mbps/GiB ，可统计内网和公网作对比！设备列表平铺化，大屏可视化一点通，你所要的，都在这里，无需频繁切换页面…



官方 Web 后台虽然稳定，但在数据展示的交互设计上存在一些不便。例如，实时的网速数据和设备历史累积流量被隐藏在了二级菜单中，需要频繁点击具体设备才能查看，无法在全局列表形成直观的对比。本插件的核心目的就是“拍平”这些层级。将单台设备的上下行网速、本次在线期间的积分流量，以及底层的累积总吞吐量，全部提取并前置到主设备列表中，无需任何多余的操作，所有设备的网络吞吐状态一目了然。

✨ 功能特性 (Features)

🏠 联动 Home Assistant：搭配专属的 哥哥科技 中枢集成，支持通过 Webhook 将状态实时推送到 HACS 插件。避免 Web 只能单端接入，实现多端并发观测。详见兄弟项目：ZTE-Stat_HA

流量与占比统计：分别统计单设备的上下行流量，实时查看流量占比速率及上下行、内外网比值。

异常上传监控：支持检测上下行比例，直观标记异常上传，打击 PCDN / P2P 偷跑上行。

精准单位换算：严格区分网络传输速率与存储容量，支持 1000/1024 双进制，支持 Mbps / GiB 显示。

全局数据对比：支持内网（局域网代数和）与公网（ WAN 口）数据大盘统计与直观对比。

高精流量计数器 ⏱️ UI 栅格重构 🖥️：完美支持手机端

事件驱动和组时间：当上下行任意方向速度变化瞬间，认定为新采样，避免错误的读到缓存值。此举有效缓解了不同接口刷新时间不同，更是解决了当轮询频率高于刷新频率时，越高频、越不准的谬误；此外，Group Time 机制使得网速上下帧撞车的概率大大降低。

双轨制流量统计对比：除展示路由器接口自带的历史总吞吐量外，还会在页面前端独立进行高频的数据采样，统计设备在当前页面打开期间的真实流量消耗。两者并排显示，互为参考。单位统一成本次，注重变化的观察。特别说明：这里的高精流量源自于官方的逐 Mac 累计计数器，用于统计每台设备的流量，但是校准了官方的回流、归零等问题，有别于 APP 周报，区分了上下行。前端是为了避免抽风时，连个大概的流量数据都看不了而进行的独立参照，微积分频率本身并不影响“高精”数值。

自定义支持：尊重网络工程习惯，支持通过脚本变量自定义 1000 进制 Mbps 、1024 进制 MiB/s 显示逻辑。

🛡️ 隐私保护、UI 优化：

DOM 原地突变（ Mutation ）渲染时，自动覆写敏感的 MAC 地址与 IPv6 临时地址，确保在录屏、截屏及分享网络状态时的安全。

无痕注入，不破坏原生 Vue 状态机，保障浏览器运行性能。

🌈 事件驱动：优化微积分算法，避免采样时间不对齐或相位差导致误算流量面积。以网络速率变化为采样区间基准。

 界面预览 (Screenshots)

小米插件参考

中兴原生界面

增强版







 安装指南 (Installation)

环境要求

在使用本脚本之前，请确保您的浏览器已安装用户脚本管理器扩展，例如：

Tampermonkey （推荐, 支持 Chrome, Edge, Firefox, Safari ）

Violentmonkey

脚本安装

点击此处安装全面版 Bro-Stat

从 GreasyFork 安装

从 OpenUserJS （直连推荐：无需科学上网）

国产脚本猫（推荐）

在弹出的 Tampermonkey 界面中点击“安装”或“更新”。

登录您的路由器 Web 管理后台，输入管理员密码，登录成功后刷新网页，进入“组网管理”界面，脚本将自动生效。

Important

备用唤醒入口：若不生效，请检查左侧工具边栏导航，找到  哥哥科技面板 点开进行使用，效果基本一致。

请确保 篡改猴 插件运行正常！！也就是 浏览器 拓展图标这里，正常显示数字！允许用户脚本注入教程如下图。

 Symlinks 友情链接

 个性化配置 (Configuration)

若脚本仍未生效，请使用如下教程：



脚本顶部暴露了全局环境变量 CONFIG 对象，支持用户根据自身网络环境进行微调：

const CONFIG = {
calcMode: 1, // 1: 绝对倍数模式 (上行/下行), 0: 传统占比模式
ratioExtremeUp: 10, // 极端上传触发阈值 (默认 1000%，触发红色⚠️告警)
ratioWarnUp: 0.07, // 重度上传触发阈值 (默认 7%，触发红色高亮)
ratioExtremeDown: 0.01, // 极端下载触发阈值 (默认 1%，触发蓝色下载倍数显示)
// 物理端口与无线频段中文映射字典 (可根据你的具体路由型号增删)
portMap: {
"eth1": "端口 1",
"eth2": "端口 2",
"eth3": "端口 3",
"eth4": "端口 4",
"wl0": "Wi-Fi 2.4G",
"wl1": "Wi-Fi 5.2G",
"wl2": "Wi-Fi 5.8G"
}
};


 注意事项 (Notes)

本脚本仅在前端对获取到的 API 数据进行重新排版与计算，不会修改路由器底层的核心配置。

若您的路由器管理地址为非标准 IP ，请在脚本的 @match 或 @include 头部规则中自行添加。

本脚本属于纯前端 DOM 注入与数据重组工具，不涉及对中兴路由器底层固件的修改。

脚本利用油猴环境，并发请求路由器的 vue_home_device_data_no_update_sess 和 vue_client_data 接口。为解决官方前端轮询刷新带来的滞后感，脚本内部通过 performance.now() 实现了独立的设定，从而推导出更为精准的瞬时流量数据。所有的 UI 修改均在原页面的 CSS 框架基础上通过 Mutation 完成，确保了界面的原生质感与兼容性。

 安装与使用说明

确保你的浏览器已安装 Tampermonkey 或 ScriptCat （脚本猫） 扩展。

点击本页面的“安装脚本”。

登录你的路由器 Web 后台（如 tplogin.cn 或 192.168.31.1 ）。

页面右侧会自动出现  悬浮按钮，点击即可展开监控面板。（你也可以点击面板上的  图标，将监控数据冻结在页面顶端）。

“在一个文明社会，干净的、不被监视与吸血的网络，是我们每个人的基本权利。”

Required Notice: Copyright © 2026 哥哥科技 (BroTech)

所有的“许可证”不以名称定义、请勿自行推断，法律效力以仓库中的实际 'License' 文件为准。

您可以收取通常范围内交易双方认为合理的、与本程序没有直接或间接关联的技术服务费，例如帮助用户上门安装路由器时附赠增值服务，但不得以哥哥科技的字号宣传；服务原则上应当以含有明确物理成本的线下服务为主，但不得以附带安装调试该脚本为由收取任何附加费用；禁止以该程序的取得、复制、下载方式、配置、调试、更新、维护为对价；也不得在在线平台以辅助安装、调试、排错之类的收取任何维护费用，来掩盖实质上为分发该软件所收取的任何费用。

总之无论如何、任何情况下不得将本软件本身源码或可执行产物打包倒卖，也不得作为售卖的商品的赠品。中兴官方可以自行、先行、直接集成该程序，但是必须保留署名；署名具体的方式可以商榷，我或将对 ZTE 公司提供更加合理的许可。

License

Copyright © 2026 哥哥科技 (Bro-Tech) This project is available under either of the following licensing options:

Regardless of the licensing path chosen, it is subject to the BroTech Prominent Attribution Terms set forth in this document. 无论选择何种授权路径，均同时受本文件所载 哥哥科技显著署名附加条款 约束。

Adaptive Public License - Bro 0.1 （已经包含额外的署名要求条件） ; or

Sustainable Use License 1.0 (SUL-1.0) WITH BroTech-Prominent-Attribution-Terms AND Broware Attribution–Noncommercial License （ Bro-BY-NC ） 1.0.

可以根据自己的使用场景自行抉择，第二种看似严格多，但是针对个人、非商业使用，条款相对较简练通俗，方便非英语母语者理解。

You may choose either licensing option.

In SPDX notation:

SPDX-License-Identifier: LicenseRef-APL-Bro-0.1 OR (SUL-1.0 WITH AdditionRef-BroTech-Prominent-Attribution-Terms AND BR-BY-NC-1.0)

许可证名称、SPDX 标识及其他简写仅用于识别。实际授权范围、条件及义务，以本仓库随软件发布的实际许可证文本、补充文件以及本文件中明确纳入的附加条款为准。

Adaptive Public License for BroTech: license.txt

Supplement File: suppfile.txt

Sustainable Use License 1.0: SUL-1.0.md

Broware Attribution–Noncommercial License 1.0: BR-BY-NC-1.0.md

无论使用何种许可证，都应当保留作者的显著署名。Regardless of the license used, the 哥哥科技's prominent attribution must be retained.

绝对一定必须保留哥哥科技这几个字，并且不得以任何形式降低“原有的署名方式的显著程度”，而不仅仅是显著降低。

无论何种原因，哪怕是技术困难导致在更大的作品中或其他编程语言中无法原样显示“哥哥科技”，“您” 也必须保留字面量，仅追加其他可以显著表达哥哥科技的方式，并及时通过 GitHub 或者邮件联系告知。保留“哥哥科技”的完整可见性是我许可的任何权利所不可分割的部分。

哥哥科技显著署名附加条款

当引用我的项目能明确地表明领域的时候，可以不再引用 GitHub 用户名或者项目名（但我不主动推荐）、仓库链接。

在任何情况下，均不得在最终用户界面中删除、篡改、遮蔽、隐藏、替换、改写、缩写、截断、弱化、降低可见性、降低显著性、误导性呈现以任何形式呈现的：

“哥哥科技”

这四个汉字。原则上必须原样保留所有“哥哥”和“哥哥科技”。BroTech 、Bro-Tech 、GitHub 用户名、项目名称、仓库链接或其他英文、拉丁字符形式，仅可作为补充署名，不得用于替代“哥哥科技”。

即使目标运行环境、显示设备、编程语言或其他技术环境无法正常显示中文，凡能够保存 Unicode 、UTF-8 、GB 18030 或其他能够表示该字面量的源码、许可证文本、元数据或其他载体中，仍必须原样保留“哥哥科技”。

如果用户可见界面因客观技术限制无法正常呈现“哥哥科技”，可以在不删除程序中实质性表达中文“哥哥科技”的前提下，追加 BroTech 、Bro-Tech 、作者用户名、项目链接或其他能够清楚识别作者身份的表示方式，并应通过 GitHub 或电子邮件及时告知作者。

任何再分发、修改、移植、合并、集成、翻译、转换编程语言或形成更大作品的行为，均不得使“哥哥科技”的署名显著程度低于原作品中与作者身份相对应的署名程度。

保留“哥哥科技”的完整字面量和实质显示、可见性与显著性，是作者授予本软件任何许可权利所不可分割的条件。

BroTech Prominent Attribution Terms

Regardless of the license or licensing route used, the Bro-Tech's prominent attribution MUST be retained.

Where the reference to my project makes the relevant field clear, you may omit the GitHub username, project name, or repository link, although myself don't recommend it.

Under no circumstances may the following Chinese characters be removed, altered, obscured, concealed, replaced, reworded, abbreviated, truncated, weakened, made less visible, made less prominent, or presented in a misleading manner:

『哥哥科技』

The only exception concerns displaying these characters in an integration environment that is technically incapable of supporting UTF-8, Unicode, GB 18030, or other encodings capable of representing them. You may add “Brotech” as supplementary attribution, accompanied by the author's username, but you must NEVER delete or replace the literal string “哥哥科技”.

The characters “哥哥科技” must always be retained, without exception. The prominence of the original form of attribution must not be reduced in any way; **this prohibits any reduction, not merely a significant reduction.**

Regardless of the reason, even if technical difficulties prevent “哥哥科技” from being displayed unchanged within a larger work or in another programming language, you must still retain the literal string “哥哥科技” and may only add other forms of attribution that prominently identify 哥哥科技. You must also promptly notify me via GitHub or email. Preserving the full visibility of “哥哥科技” is an inseparable condition of any rights I grant.

## 关联链接

- https://www.bilibili.com/video/BV1PtR7B8ECC/

## 导航

- 项目页：—（本条不是项目，按设计不建实体页）
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
