---
type: "corpus"
item_id: "9c864ed75039015b"
title: "用 Cloudflare 免费额度搭域名邮箱后，我顺手给它写了个原生 iOS 客户端"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1254094"
project_url: "https://apps.apple.com/us/app/cf-mail-self-hosted-email/id6798590577"
author: "1024ba"
published_at: "2026-11-03T04:41:23"
captured_at: "2026-11-04T09:58:05+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 用 Cloudflare 免费额度搭域名邮箱后，我顺手给它写了个原生 iOS 客户端

> [!info] 一句话导读
> ![CF Mail]( https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-01-cover.png)

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1254094>
> 指标：回复=0
> 作者：1024ba　|　发布：2026-11-03T04:41:23
> 项目链接：<https://apps.apple.com/us/app/cf-mail-self-hosted-email/id6798590577>
> 采集：2026-11-04T09:58:05+08:00　|　id：`9c864ed75039015b`

## 正文

---

![CF Mail]( https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-01-cover.png)

大家好，分享一个自己做了挺久的东西：**CF Mail**，一个原生 SwiftUI 写的 iPhone / iPad 邮件客户端。

## 起因

之前用 [maillab/cloud-mail]( https://github.com/maillab/cloud-mail) 在 Cloudflare 上搭了域名邮箱。Worker + D1 + Email Routing ，基本零成本，一个域名可以开无限个地址，注册各种服务时一个站一个邮箱，很爽。

问题是手机上只能开网页版，没有推送，也没法和 Gmail 、QQ 这些常用邮箱放在一起看。系统自带的「邮件」 App 又连不上它（它没有 IMAP ）。所以就自己写了一个客户端，顺带把服务端也改了一版。

## 能干什么

**两种账户放在一个 App 里：**

- **普通邮箱**：走 IMAP/SMTP 直连，已经内置了 Gmail 、iCloud 、Outlook 、Yahoo 、Fastmail 、QQ/Foxmail 、163/126/yeah 等服务商的预设。QQ 和网易会提示你用「授权码」，不用自己去查服务器地址。「收件箱、已发送、草稿箱、已删除」这些中文文件夹名会自动识别。
- **自建 CloudMail**：填上你的 Worker 地址就能用。如果你有管理员权限，App 里还能直接管用户、角色权限、邀请码、全部邮件和系统设置，不用再开电脑。

![架构]( https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-03-architecture.png)

**其他功能：**

- 统一收件箱，以及服务端搜索：可以按主题、正文、发件人、收件人来搜
- 分开发送：群发时每个收件人各自收到一封，互相看不到对方，发通知、发邀请很好用
- 富文本编辑、附件、草稿、联系人，回复和转发
- iPad 分栏布局，大屏上列表和正文可以同时看
- 新邮件推送（ CloudMail 账户，可选）

## 隐私这块我比较在意

- 没有广告，没有第三方统计或跟踪 SDK ，也不需要注册 CF Mail 账号
- 账号凭据只存在 iOS 钥匙串里，可以用 Face ID / Touch ID 锁住 App
- 远程图片可以设成默认拦截、每封邮件询问或始终加载，防追踪像素
- IMAP 邮箱是手机直连邮件服务器，中间不经过我的任何服务器
- 推送走一个独立的网关。自建的 Worker 只发「有新邮件」这类脱敏事件，不直连 APNs ，也不保存设备 Token
- 诊断日志只存在本地，并且做了脱敏，只有你手动导出时才会离开手机

## 服务端也开源了

我在上游基础上维护了一个分支：[CF Mail cloud-mail]( https://github.com/readori/cloud-mail)

主要改动有：安全加固（初始化保护、Webhook 签名、密钥加密存储、会话加固）、CC/BCC 、更多邮件 API 、通知钩子、数据库迁移保护，以及一套部署前的契约测试。

用一个域名加一个 Cloudflare 账号就能跑起来，个人用基本在免费额度内。

## 收费说明

先说清楚，App 有内购：

- **免费版**：1 个 CloudMail 服务器（每个服务器 1 个身份），加最多 10 个 IMAP/SMTP 邮箱，所有功能都能用
- **Pro**：不限服务器和账户数量，有订阅版和买断版，价格以 App Store 显示为准 [可在这里写具体价格] 

个人用的话，免费版应该就够了。

## 下载

- App Store： [ https://apps.apple.com/us/app/cf-mail-self-hosted-email/id6798590577 ] 
- 目前没上架国区，只能用外区 ID 下载
- 要求 iOS 16 及以上

还在持续迭代，欢迎大家提 bug 和需求，帖子里回复或者去 GitHub 提 issue 都可以。在 V2EX 回复里留言想要的功能，我会优先考虑 🙏

## 关联链接

- https://github.com/maillab/cloud-mail
- https://github.com/readori/cloud-mail
- https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-01-cover.png
- https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-03-architecture.png

## 导航

- 项目页：[[10-项目/apps.apple.com_8cc4da79]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
