---
type: "corpus"
item_id: "6b83657ab3b108c8"
title: "[自荐] SPX：基于 Next.js + Supabase + Stripe 的独立产品网站源码"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1255678"
project_url: "https://indiexyz.com/"
author: "harrybt112"
published_at: "2026-11-09T13:24:00"
captured_at: "2026-11-10T09:55:59+08:00"
lang: "zh"
kind: "post"
topic: "开发者工具"
shard: "2026-11-10"
pub_day: "2026-11-09"
tags:
  - 语料
  - v2ex
  - 300
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# [自荐] SPX：基于 Next.js + Supabase + Stripe 的独立产品网站源码

> [!info] 一句话导读
> 大家好，来分享一下我整理的网站源码产品 SPX ，也给自己的产品做个自荐。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1255678>
> 指标：回复=0
> 作者：harrybt112　|　发布：2026-11-09T13:24:00
> 项目链接：<https://indiexyz.com/>
> 采集：2026-11-10T09:55:59+08:00　|　id：`6b83657ab3b108c8`

## 正文

大家好，来分享一下我整理的网站源码产品 SPX ，也给自己的产品做个自荐。

做独立产品，核心功能之外，总有一批需要处理的事情：产品介绍页、用户登录、支付、购买后的访问权限、博客，以及部署配置。

这些事情每一项都有现成方案，但把它们接起来，仍然要花时间处理配置和流程细节。

SPX 就是把这些基础模块整理到一个项目里，让有开发基础、准备做产品的人，可以从已有代码开始修改。

目前包含：
- 网站页面：产品介绍、价格展示、FAQ 等基础页面。
- 用户登录：基于 Supabase Auth ，支持邮箱验证码，可配置 Google 登录。
- 支付与权限：Stripe 一次性付款，支付完成后通过 Webhook 更新用户访问权限。
- 会员工作区：登录后的用户页面和产品访问入口。
- 博客与 SEO 基础：文章、分类、作者页及 sitemap 配置。
- 部署文档：本地启动、数据库配置、支付配置和上线步骤。
技术栈是 Next.js 14 App Router 、TypeScript 、Supabase 、Stripe 、Tailwind CSS 和 DaisyUI 。

IndieXYZ 这套站点本身也用于展示 SPX 的页面和模块，可以先看看效果，再判断是否符合自己的需求：

产品介绍： https://indiexyz.com/#spx

使用指南： https://indiexyz.com/blog/spx-usage-guide

提前说明一下使用边界：交付的是网站源码，需要自行配置 Supabase 、Stripe 、邮件服务和部署环境；目前支付流程是一次性购买。它适合愿意改代码、希望少做一些基础搭建的开发者。

价格： [补充实际金额及币种] ，一次性购买。 第三方服务的费用需要另外承担。

也想听听大家的意见：你们做独立产品时，登录、支付、部署这些环节，哪个最耗时间？对于这类源码产品，最在意的是代码结构、文档完整度，还是后续维护？

欢迎提具体问题，我会在评论里回复。

## 关联链接

- https://indiexyz.com/#spx
- https://indiexyz.com/blog/spx-usage-guide

## 导航

- 项目页：[[10-项目/indiexyz.com_0ebf7f10]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`开发者工具`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
