---
type: "project"
title: "用 Cloudflare 免费额度搭域名邮箱后，我顺手给它写了个原生 iOS 客户端"
project_url: "https://apps.apple.com/us/app/cf-mail-self-hosted-email/id6798590577"
first_seen: "2026-11-04T09:58:05+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 用 Cloudflare 免费额度搭域名邮箱后，我顺手给它写了个原生 iOS 客户端

> [!info] 一句话导读
> ![CF Mail]( https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-01-cover.png)

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://apps.apple.com/us/app/cf-mail-self-hosted-email/id6798590577>
> 首次收录：2026-11-04T09:58:05+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-11-04T09:58:05+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-11-04/9c864ed75039015b_用-Cloudflare-免费额度搭域名邮箱后,我顺手给它写了个原生-iOS-客户端]] |

## 摘要正文

---  ![CF Mail]( https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-01-cover.png)  大家好，分享一个自己做了挺久的东西：**CF Mail**，一个原生 SwiftUI 写的 iPhone / iPad 邮件客户端。  ## 起因  之前用 [maillab/cloud-mail]( https://github.com/maillab/cloud-mail) 在 Cloudflare 上搭了域名邮箱。Worker + D1 + Email Routing ，基本零成本，一个域名可以开无限个地址，注册各种服务时一个站一个邮箱，很爽。  问题是手机上只能开网页版，没有推送，也没法和 Gmail 、QQ 这些常用邮箱放在一起看。系统自带的「邮件」 App 又连不上它（它没有 IMAP ）。所以就自己写了一个客户端，顺带把服务端也改了一版。  ## 能干什么  **两种账户放在一个 App 里：**  - **普通邮箱**：走 IMAP/SMTP 直连，已经内置了 Gmail 、iCloud 、Outlook 、Yahoo 、Fastmail 、QQ/Foxmail 、163/126/yeah 等服务商的预设。QQ 和网易会提示你用「授权码」，不用自己去查服务器地址。「收件箱、已发送、草稿箱、已删除」这些中文文件夹名会自动识别。 - **自建 CloudMail**：填上你的 Worker 地址就能用。如果你有管理员权限，App 里还能直接管用户、角色权限、邀请码、全部邮件和系统设置，不用再开电脑。  ![架构]( https://raw.githubusercontent.com/readori/Case-word/refs/heads/main/CF%20Mail/v2ex-03-architecture.png)  **其他功能：**  - 统一收件箱，以及服务端搜索：可以按主题、正文、发件人、收件人来搜 - 分开发送：群发时每个收件人各自收到一封，互相看不到对方，发通知、发邀请很好用 - 富文本编辑、附件、草稿、联系人，回复和转发 - iPad 分栏布局，大屏上列表和正文可以同时看 - 新邮件推送（ CloudMail 账户，可选）  ## 隐私这块我比较在意  - 没有广告，没有第三方统计或跟踪 SDK ，也不需要注册 CF Mail 账号 - 账号凭据只存在 iOS 钥匙串里，可以用 Face ID / Touch ID 锁住 App - 远程图片可以设成默认拦截、每封邮件询问或始终加载，防追踪像素 - IMAP 邮箱是手机直连邮件服务器，中…
