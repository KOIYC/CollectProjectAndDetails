---
type: "corpus"
item_id: "4b6a3cc82d7e08b3"
title: "做了个 PDF 分享工具：除了生成链接，我更想知道对方到底有没有认真看"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1247458"
project_url: "https://pdf-to-link.com/"
author: "digiplanp"
published_at: "2026-10-09T13:39:55"
captured_at: "2026-10-10T10:02:47+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-10-10"
pub_day: "2026-10-09"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 做了个 PDF 分享工具：除了生成链接，我更想知道对方到底有没有认真看

> [!info] 一句话导读
> 最近做了一个比较小的 PDF SaaS ，叫 **PDF to Link**。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1247458>
> 指标：回复=0
> 作者：digiplanp　|　发布：2026-10-09T13:39:55
> 项目链接：<https://pdf-to-link.com/>
> 采集：2026-10-10T10:02:47+08:00　|　id：`4b6a3cc82d7e08b3`

## 正文

最近做了一个比较小的 PDF SaaS ，叫 **PDF to Link**。

地址：

https://pdf-to-link.com/

最开始想做它，其实不是因为“PDF 转链接”这个功能本身有多难，而是我发现现有的 PDF 分享流程有一个挺明显的断层：

> 文件发出去了，然后呢？

比如我给别人发一个 20 页的 PDF：

- 对方打开了吗？
- 看到了第几页？
- 哪几页停留时间比较长？
- 是不是看两页就关掉了？
- 最后有没有点击我希望他点击的链接？

如果只是通过邮件附件、Google Drive 、Dropbox 之类发出去，这些信息基本是看不到的。

于是就做了这个工具。

---

## 现在的基本流程

目前逻辑比较简单：

```text
上传 PDF
↓
生成一个独立阅读页面
↓
得到分享链接 / QR Code
↓
别人通过浏览器阅读
↓
后台查看阅读数据
```

它不是把 PDF 转成 HTML ，也不是把 PDF 内容重新排版。

原始内容还是 PDF ，只是在浏览器里提供一个独立的阅读页面。

这样做之后，就可以在 PDF 外面增加一些东西，比如：

- Logo
- Favicon
- 页面背景
- CTA 按钮
- 社交链接
- 密码访问
- Lead Capture
- QR Code

我比较在意的其实不是这些外观功能，而是后面的阅读数据。

---

## 目前做了哪些阅读数据

现在后台主要统计：

- Views / Reading Sessions
- Visitors
- Active Reading Time
- Reading Depth
- 每一页的 Engagement
- Reader Location
- Exit Page
- Downloads
- CTA Clicks

例如一个 20 页 PDF：

如果 100 个人打开：

```text
Page 1  100
Page 2   92
Page 3   85
Page 4   81
Page 5   43
Page 6   38
...
Page 20  12
```

那至少可以看到第 5 页附近发生了比较明显的流失。

当然我不认为这就代表：

> “第 5 页内容一定有问题。”

因为也可能用户已经找到了想看的信息。

所以我现在对 Analytics 的定位是：

**它提供行为信号，而不是替用户解释行为。**

---

## Active Reading Time 我没有直接用页面停留时间

这里我之前纠结了一段时间。

假设：

用户打开 PDF → 切到另一个 Tab → 30 分钟以后回来。

如果简单用：

```text
close_time - open_time
```

那结果可能会显示这个人读了 30 多分钟，但实际上完全不是。

所以现在 Active Time 更偏向统计：

- 页面处于可见状态
- 浏览器 Tab 是 active
- 阅读器存在实际活动

当然，这依然不能证明用户“认真阅读”。

我觉得只能做到尽可能接近真实行为，不能把它包装成“阅读理解检测”。

---

## 为什么不用 Google Drive ？

这个问题应该是最容易被问到的。

我自己的理解是，它们解决的问题不完全一样。

### Google Drive / Dropbox

更偏：

- 文件存储
- 文件夹管理
- 权限
- 团队协作

### PDF to Link

更偏：

- 对外发布一个 PDF
- 提供独立阅读体验
- 品牌展示
- 查看阅读行为
- 引导下一步操作

所以如果只是：

> “我要给同事传一个 PDF 。”

我自己也会直接用 Google Drive 。

但如果是：

- Pitch Deck
- Proposal
- 产品目录
- Portfolio
- White Paper
- 报告
- 培训资料

这类 PDF ，我觉得“分享之后发生什么”会更有价值。

---

## 一个我目前还没完全想清楚的问题：下载到底应该默认开还是关？

这个目前我自己也比较纠结。

如果允许下载：

优点：

- 用户可以保存
- 使用习惯自然
- 离线阅读方便

缺点：

PDF 下载以后，后面的阅读行为就完全不可见了。

如果禁止下载：

优点：

- 数据比较完整
- 更适合一些 Proposal / Pitch Deck

缺点：

- 用户可能觉得限制太强
- 真正想下载的人可能截图或者用其他方式保存

所以目前我更倾向于：

**让发布者自己选择。**

但不知道 V 友们实际使用时更喜欢哪种默认值。

---

## 另外一个问题：Raw PDF URL 还是 Viewer URL ？

我现在产品默认生成的是阅读页，例如：

```text
example.com/page/xxxxx
```

而不是：

```text
example.com/file.pdf
```

因为只有 Reading Page 才能加 Analytics 、Password 、CTA 等东西。

但是实际调研下来，确实还有一批用户搜索的是：

> “我就想要一个真正以 .pdf 结尾的 URL 。”

特别是开发/API/嵌入类需求。

所以我现在觉得这其实是两个完全不同的需求：

### Raw PDF URL

更适合：

- API
- 程序直接读取
- iframe / embed
- 下载
- 文件引用

### Viewer URL

更适合：

- 给人阅读
- Analytics
- Branding
- Password
- CTA

现在产品主要做后者。

这块如果 V 友里面有做文档系统或者 SaaS 的，也挺想听听你们实际更常遇到哪一种。

---

## 免费版目前怎么做

目前免费版：

- $0
- 1 个 Published PDF
- 单 PDF 最大 50 MB

主要核心功能也可以体验。

我暂时没有做那种“上传一次以后所有东西都锁住必须付费”的模式，因为早期更想知道：

**用户究竟会不会真的用这个东西，而不是注册以后就走。**

现在最想验证的指标其实不是注册量，而是：

```text
上传 PDF
↓
成功发布
↓
真的把链接分享出去
↓
产生真实 Reader Session
↓
回来查看 Analytics
```

如果这个闭环不成立，后面加再多功能意义也不大。

---

## 接下来我比较想做的

目前考虑的方向主要有：

### 1. 更细的 Reading Analytics

例如：

- Page revisit
- 阅读路径
- Reader Session timeline
- 不同链接来源的 engagement

### 2. Expiring Link

例如：

```text
24 小时后失效
7 天后失效
指定日期失效
```

### 3. Custom Domain

这个已经在做更完整的体验。

例如：

```text
docs.company.com/proposal
```

而不是平台自己的域名。

### 4. 更方便的销售/营销工作流

我之后可能会考虑：

- Webhook
- Zapier
- HubSpot
- Slack notification

例如：

> 某个 Proposal 被打开了  
> 对方读到第 12 页  
> 再次回来阅读

然后发通知。

不过这一块我暂时不想太早做，因为容易从一个很简单的 PDF 工具膨胀成一个很重的销售 SaaS 。

---

## 有几个问题特别想听听 V 友意见

如果你们平时会分享 PDF ，我比较想知道下面几个问题：

**1. 你们实际有没有“想知道对方看到第几页”的需求？**

还是说这个需求看起来合理，但实际上根本不会看数据？

**2. 如果是 Pitch Deck / Proposal ，你更希望默认允许下载，还是禁止下载？**

**3. 你更需要 Raw `.pdf` URL ，还是浏览器 Viewer URL ？**

**4. 阅读 Analytics 里，你觉得哪个数据最有价值？**

- Active Time
- Reading Depth
- 每页停留
- Exit Page
- 是否重新打开
- CTA Click
- 其他？

**5. 如果让你付费，什么功能才会真正让你付？**

我自己现在比较怀疑单纯：

> “上传 PDF → 生成链接”

其实没有太强的付费价值。

真正可能产生价值的还是后面的：

> Analytics + Branding + Access Control + Workflow

所以现在还在验证这件事。

---

产品地址：

https://pdf-to-link.com/

如果大家愿意试的话，比较希望收到真实的吐槽，特别是：

- 哪一步不好理解
- 哪个功能完全没必要
- Analytics 哪里看不懂
- 分享页有哪些明显问题
- 哪些功能你觉得我是在自嗨

这些反馈对我现在比“挺好的，加油”更有用。

## 导航

- 项目页：[[10-项目/pdf-to-link.com_d5d445d5]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
