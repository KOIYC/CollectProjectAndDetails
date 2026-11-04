---
type: "corpus"
item_id: "4ac5714abbd0823b"
title: "做 SaaS 出海，终于用 Stripe 收到钱了：聊聊 MoR 被拒、代理踩坑和海外主体"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1254119"
project_url: "https://rzradar.com/"
author: "RockHammer1947"
published_at: "2026-11-03T06:12:47"
captured_at: "2026-11-04T09:58:05+08:00"
lang: "zh"
kind: "post"
topic: "SaaS/B2B"
shard: "2026-11-04"
pub_day: "2026-11-03"
tags:
  - 语料
  - v2ex
  - 1296
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 做 SaaS 出海，终于用 Stripe 收到钱了：聊聊 MoR 被拒、代理踩坑和海外主体

> [!info] 一句话导读
> 大厂出来前后折腾了 3 个月做 SaaS 出海，终于把 Stripe 收款跑通，**实际收到钱了**。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1254119>
> 指标：回复=0
> 作者：RockHammer1947　|　发布：2026-11-03T06:12:47
> 项目链接：<https://rzradar.com/>
> 采集：2026-11-04T09:58:05+08:00　|　id：`4ac5714abbd0823b`

## 正文

大厂出来前后折腾了 3 个月做 SaaS 出海，终于把 Stripe 收款跑通，**实际收到钱了**。

产品做出来了，不代表海外用户的钱就能顺利收进来。这一环，我踩的坑比预想中多。

产品做出来的速度越来越快了，有没有用户愿意正在买单才能验证是不是真需求。

## 最早想走国内主体 + MoR，结果卡在审核

一开始想先用国内主体接 MoR（Merchant of Record，代售收款平台），把收款接起来，再继续做业务。

但我当时申请的平台，注册、提交资料折腾了半天，还要求提供邓白氏和各种证明。材料准备了一轮，最后还是被拒了。

中间也找过淘宝代理，又踩了一次坑。折腾下来，产品之外的这些事情，确实消耗了不少时间和精力。

后来还是把海外主体、企业账户，再到 Stripe 收款这条路走了一遍，直到真实收到钱，这个闭环才算跑通。

这段经历让我得出的结论是：**对我这种准备长期做 SaaS 出海的业务，还是值得有自己的海外主体，把公司、账户和收款这套基础设施搭起来。** 具体选择还要结合自己的业务阶段、预算，以及各平台的审核要求。

## 把公司和账户这一段，整理成了自助教程

踩完这些坑，我把实际操作过程整理成了 [OPC 出海自助课程：美国 LLC 公司与对公账户自助开通指南]( https://rzradar.com/solo-company?utm_source=v2ex&utm_medium=community&utm_campaign=solo_launch)。这里也坦白自荐一下，**售价 ¥99**。

**⚠️⚠️⚠️注意¥99RMB 是纯自助操作教程费用，不是代办,没有代注册等服务:一次性州注册费+代理办税务合规年费,要向平台支付差不多 2000 美金，没下定决心的,没有自学能力的朋友甚拍教程⚠️⚠️⚠️**

是 **4 节视频 + 配套图文，独立购买、长期有效**，具体包括：
1. 注册前需要想清楚什么，准备哪些材料；
2. 海外平台自助申请美国 LLC ，到 EIN 的操作过程；
3. 企业账户申请前的材料准备；
4. 企业账户申请操作。

视频用来看完整顺序，图文用来填表时逐步对照。**这套课程交付的是公司与账户申请部分，不包含 Stripe 接口开发课程。**

![美国 LLC 自助课程：视频实操与图文指引]( https://rzradar.com/assets/courses/us-llc-banking-20261029.webp)

**¥99 只是数字教程费用，不是注册公司和开户的总费用。** 海外平台注册方案、州费及后续维护等费用另算，课程不提供代办，机构审核结果以各平台为准。先看课程页的费用与交付说明；如果还没有预算，或者暂时没准备实际运营海外业务，先别急着买。

购买走微信小店，订单发货消息里的「去上课」可以进入小程序。也可以用购买时的同一个微信登录电脑端，边看图文边操作；手机和 PC 的课程权益互通。

## 这些内容放在了「锐知」上

主站是 [锐知 · 一人公司基建中心]( https://rzradar.com/?utm_source=v2ex&utm_medium=community&utm_campaign=solo_launch)。除了这门付费教程，还整理了主动订阅的海外 YouTube、播客内容，以及一人公司的创业案例：中文内容、核心收获和原始出处都保留，也调研一下看是否有这种订阅监控把长视频转文字第一时间推送的需求

**信号和案例目前免登录、免费读完整内容，和付费课程分开。** 开源基建栏目后续也会加入一些自用工具，首批仓库还在整理。

![锐知主站实际界面]( https://rzradar.com/assets/promotions/v2ex-solo-home-5ce714a7d9e6bffa.webp)

微信里可以扫码打开锐知小程序，阅读内容或学习已购课程：

![锐知正式版小程序码](  )

也想听听大家的经历：你们做 SaaS 出海，收款最后选了哪条路？有没有同样卡在主体、材料审核或者企业账户这一步的？

## 关联链接

- https://rzradar.com/?utm_source=v2ex&utm_medium=community&utm_campaign=solo_launch
- https://rzradar.com/assets/courses/us-llc-banking-20261029.webp
- https://rzradar.com/assets/promotions/v2ex-solo-home-5ce714a7d9e6bffa.webp
- https://rzradar.com/solo-company?utm_source=v2ex&utm_medium=community&utm_campaign=solo_launch

## 导航

- 项目页：[[10-项目/rzradar.com_414f730f]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`SaaS/B2B`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
