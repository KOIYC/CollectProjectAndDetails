---
type: "corpus"
item_id: "02afbef1e6af0958"
title: "送码：又一个让你的 Kindle 不吃灰的工具"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1257010"
project_url: "https://global.v2ex.co/index.xml"
author: "VeeSong"
published_at: "2026-11-14T03:18:07"
captured_at: "2026-11-16T10:06:33+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-16"
pub_day: "2026-11-14"
tags:
  - 语料
  - v2ex
  - 864
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:副业"
---

# 送码：又一个让你的 Kindle 不吃灰的工具

> [!info] 一句话导读
> [书接上文]( https://www.v2ex.com/t/1223788)

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1257010>
> 指标：回复=0
> 作者：VeeSong　|　发布：2026-11-14T03:18:07
> 项目链接：<https://global.v2ex.co/index.xml>
> 采集：2026-11-16T10:06:33+08:00　|　id：`02afbef1e6af0958`

## 正文

[书接上文]( https://www.v2ex.com/t/1223788)

之前做了一个 RSS 阅读 App ，有一天秃发奇想，kindle 上阅读体验似乎比手机好，但是现有的自部署方案 miniflux 和 FreshRSS 却不太适合在 kindle 上使用。于是我自己做了一个 RSS 云同步服务 [x6o4 RSS Cloud]( https://rss-cloud.x6o4.com/) https://rss-cloud.x6o4.com/ 。现在，我可以用专门适配电纸书的页面阅读 RSS 了。

但新的问题又来了，App 中的拉取原文和图片解除防盗链在网页中无法实现，于是又搞了一个 [skill]( https://reader.x6o4.com/tools) https://reader.x6o4.com/tools ，现在，我可以在 AI agent 中直接说一句「把未读文章推送到 kindle 」，不一会儿就可以用 kindle 原生的阅读器更舒服地阅读了。

当然，对于那些不想自己搭建 RSS 同步服务器或者对技术不太了解但又想体验 RSS 的朋友，用 RSS Cloud 也可以直接做到在 App 中开箱即用，省时省心。

送码是微信小程序码，扫码登录后可领取 7 天试用，目前试用名额 100 个。主要是目前没有用太好的服务器，怕一时太多人扛不住。如果没有抢到前 100 名的朋友，后续这批试用期过了的名额还会释放出来，可以保持关注。当然，如果等不及抢名额直接付费购买也是可以的。

![x6o4 试用二维码](  )

大家如果使用过程中有什么意见或建议欢迎在评论区反馈。或者对于个人开发者怎么做支付和收款的等类似业务问题，或用的什么 AI 开发之类的，也可以讨论。

**推广的内容就到此为止了，下面还有一些 RSS Cloud 的使用技巧、开发历程、vibe 作品现状，大家觉得太长可以不看。**



## 业余 vibe 状态和心得

上面说到一开始我想在 kindle 中阅读 RSS ，就让 AI 搭了个云服务，想了想既然做都做了，那就转成 SaaS 应用，顺水推舟把 RSS 云同步也接入到之前的阅读 APP 中。当时只接了 Google play 的支付，也就是上面的 RSS Cloud 注册之后想要用起来还需要下载 App 来购买开通。

看过我之前帖子的朋友可能了解，我作为一个 996 的奔五平庸码农，业余时间很少，想要分出精力作为副业来维护这个东西有点困难。也就是支付和使用体验不太好同时觉得没精力搞，所以在 RSS Cloud 上线之后很长一段时间并没有主动去推广。

后面又陆陆续续搞了 [skill]( https://reader.x6o4.com/tools)，进一步提升 kindle 的阅读体验。这里我分享下目前我的使用方式，我会在 RSS Cloud 后台中设置订阅源分类，有 kindle 和 kindle-web 两个，平时一些适合在 kindle 中阅读的订阅源就放在 kindle 分类下，每天用 workbuddy 或者 glm 送的 token 定时跟 agent 说「帮我推送 kindle 分类下的未读」，然后就会将未读文章转成 epub 发送到 kindle 了。另外 kindle-web 分类的 RSS 适合直接在电纸书浏览器打开，我会直接在电纸书页面选择这个分类来阅读，不用再让 AI 转一手。

## 使用进阶

用 skill 的好处还有一个就是可以让他记住你的一些偏好，比如可以让他始终记住只拉取 kindle 分类，将一些广告贴和低质量的文章自动标记已读等，这样在 kindle 中读到的就是更高质量的文章了。

skill 我也放在 github 上，如果不想购买 RSS Cloud 的老哥，fork 下 skill 然后让 AI 按自己的需求调整，对接自己部署的 RSS 服务器，应该也可以做到上面的效果。对于使用其他电纸书设备的老哥也可以让 AI agent 调整 skill 的发布方式。

## 项目现状

直到目前，我看了下 Google play 的统计，App 有十几个下载量，从 6 月份上线到现在全都流失了，目前日活就我一个在用。突然觉得上面我说的 100 个试用名额似乎还是太乐观了，还说什么「抢不到的朋友不要急」，到时又是只有十几个试用的话，这话听得就很尴尬。

那么，是什么让我突然想要来这里推广一波呢？只能说我是个又菜又爱玩的人，看到很多人都在用 AI 搞创业，所以自己也想把从做系统到推广和维护整条链路走一走，像是一副有着自己事业的老板一样。说真的，自从我用了 AI ，真的感觉自己像老板一样指挥 AI 这个员工干活，看到 AI 闲着自己就浑身不自在，总想让他干点什么，巴不得他 24 小时全年无休的干。可见如果我真的当了老板，也是个压榨员工的货。

距离我上次发帖推广 App 已经有 4 个多月了，其实 RSS Cloud 如果专门放下时间来做估计也就两三天 AI 就可以做好了。主要是 996 对业余时间的挤压，同时业余时间很多时候都是我自己自嗨在使用 App 和 kindle 阅读，想着这个东西就当做是「无心插柳」吧，而能不能「柳成荫」我告诉自己也不用太在意。（但既然来推广了感觉又显得很有心很在意）

还是我之前帖子说的，这一套都是想着给自己量身打造的东西，可能很难适用大部分人。但是在 v 站潜水那么多年我也是知道，一个软件做出来，最难的还是推广这一步，推广得好再「自我」和小众的软件也可能有很多「同频」想要尝试使用的受众。所以后续还会考虑在一些社交媒体和视频平台做一下推广，既然要体验做「老板」的感觉，除了会开发，似乎也要学点运营了。

最后关于软件后续迭代的计划，可能是：

- 支持稍后阅读，如 Instapaper 第三方服务
- windows App
- 收藏文章随机漫步，让收藏不吃灰

嗯，还是为了满足我自己的需求。

## App 送码

最后的最后，送一波 x6o4 Reader （ https://reader.x6o4.com/ ）去广告会员兑换码，大家就算不用云同步，哪怕本地订阅 V 站 RSS https://global.v2ex.co/index.xml 再使用 V 站 api key 作为 V 站第三方客户端来用体验也很不错 ：

```
NWB0NDDK72FFGU9WFGFHVAX
GZCAT904RJHYMWL3TCSU813
35NQVP5G7XUDK385WCQFVE9
YXJZJ4LM4X9X3F852VGU3HD
FPV4KNT1LL862KU81MB71CJ
02TC9CZS48KQXN74V6S9ZMG
Y657X0W19FQMAKF0ER93E9Z
X0F1T680G5MCS6JXJ9VFYQY
267HQUYDV636J146YQGC5W9
BX6AB295PEHC5F53X6MUG2A
JS62HEGDF260WVWC7N5ND9L
ZSPSQUGZT3795R58VMK1R8Z
8UTVJ4DRXSEDVE7L9KHTNAP
XFV5RC9U5SHP4RFXHKVXGMN
8US95PN7CKE1K4SF6RJ0TDN
YPVLUZKFUM5R960E9SB9LDX
7XGV4GXE6U7SBUES5FTCZMQ
VDPYHENBZJFT062BQ5BVLYQ
Z1MWTNBWZPGRSN1Z207ZSMC
0NYYPPYQTKXP5N2GB6R8XWY
```

## 关联链接

- https://reader.x6o4.com/
- https://reader.x6o4.com/tools
- https://rss-cloud.x6o4.com/
- https://www.v2ex.com/t/1223788

## 导航

- 项目页：[[10-项目/global.v2ex.co_5de0d9cd]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
