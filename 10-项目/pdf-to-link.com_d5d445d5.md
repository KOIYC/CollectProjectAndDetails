---
type: "project"
title: "做了个 PDF 分享工具：除了生成链接，我更想知道对方到底有没有认真看"
project_url: "https://pdf-to-link.com/"
first_seen: "2026-10-10T10:02:47+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 做了个 PDF 分享工具：除了生成链接，我更想知道对方到底有没有认真看

> [!info] 一句话导读
> 最近做了一个比较小的 PDF SaaS ，叫 **PDF to Link**。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://pdf-to-link.com/>
> 首次收录：2026-10-10T10:02:47+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-10T10:02:47+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-10/4b6a3cc82d7e08b3_做了个-PDF-分享工具-除了生成链接,我更想知道对方到底有没有认真看]] |

## 摘要正文

最近做了一个比较小的 PDF SaaS ，叫 **PDF to Link**。  地址：  https://pdf-to-link.com/  最开始想做它，其实不是因为“PDF 转链接”这个功能本身有多难，而是我发现现有的 PDF 分享流程有一个挺明显的断层：  > 文件发出去了，然后呢？  比如我给别人发一个 20 页的 PDF：  - 对方打开了吗？ - 看到了第几页？ - 哪几页停留时间比较长？ - 是不是看两页就关掉了？ - 最后有没有点击我希望他点击的链接？  如果只是通过邮件附件、Google Drive 、Dropbox 之类发出去，这些信息基本是看不到的。  于是就做了这个工具。  ---  ## 现在的基本流程  目前逻辑比较简单：  ```text 上传 PDF ↓ 生成一个独立阅读页面 ↓ 得到分享链接 / QR Code ↓ 别人通过浏览器阅读 ↓ 后台查看阅读数据 ```  它不是把 PDF 转成 HTML ，也不是把 PDF 内容重新排版。  原始内容还是 PDF ，只是在浏览器里提供一个独立的阅读页面。  这样做之后，就可以在 PDF 外面增加一些东西，比如：  - Logo - Favicon - 页面背景 - CTA 按钮 - 社交链接 - 密码访问 - Lead Capture - QR Code  我比较在意的其实不是这些外观功能，而是后面的阅读数据。  ---  ## 目前做了哪些阅读数据  现在后台主要统计：  - Views / Reading Sessions - Visitors - Active Reading Time - Reading Depth - 每一页的 Engagement - Reader Location - Exit Page - Downloads - CTA Clicks  例如一个 20 页 PDF：  如果 100 个人打开：  ```text Page 1  100 Page 2   92 Page 3   85 Page 4   81 Page 5   43 Page 6   38 ... Page 20  12 ```  那至少可以看到第 5 页附近发生了比较明显的流失。  当然我不认为这就代表：  > “第 5 页内容一定有问题。”  因为也可能用户已经找到了想看的信息。  所以我现在对 Analytics 的定位是：  **它提供行为信号，而不是替用户解释行为。**  ---  ## Active Reading Time 我没有直接用页面停留时间  这里我之前纠结…
