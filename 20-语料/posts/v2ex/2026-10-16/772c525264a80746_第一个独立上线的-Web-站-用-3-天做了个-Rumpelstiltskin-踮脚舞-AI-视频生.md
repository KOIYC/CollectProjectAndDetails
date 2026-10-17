---
type: "corpus"
item_id: "772c525264a80746"
title: "第一个独立上线的 Web 站：用 3 天做了个 Rumpelstiltskin 踮脚舞 AI 视频生成器，记录一下踩过的坑"
source: "v2ex"
source_name: "V2EX"
url: "https://www.v2ex.com/t/1249185"
project_url: "https://rumpelstiltskinaivideo.app/"
author: "komazhao"
published_at: "2026-10-15T16:42:56"
captured_at: "2026-10-16T09:38:51+08:00"
lang: "zh"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-10-16"
pub_day: "2026-10-15"
tags:
  - 语料
  - v2ex
  - 17
metrics: {"replies": 0}
comments_count: 0
comments_total: 0
discovered_via: "v2ex:独立开发"
---

# 第一个独立上线的 Web 站：用 3 天做了个 Rumpelstiltskin 踮脚舞 AI 视频生成器，记录一下踩过的坑

> [!info] 一句话导读
> 做了很多年数据和产品，一直想自己从零上线一个能收钱的站。这次赶上一个梗，终于把第一个站发出去了，记录一下。

> [!meta]- 语料信息（点开展开）
> 来源：V2EX（post）
> 原帖：<https://www.v2ex.com/t/1249185>
> 指标：回复=0
> 作者：komazhao　|　发布：2026-10-15T16:42:56
> 项目链接：<https://rumpelstiltskinaivideo.app/>
> 采集：2026-10-16T09:38:51+08:00　|　id：`772c525264a80746`

## 正文

做了很多年数据和产品，一直想自己从零上线一个能收钱的站。这次赶上一个梗，终于把第一个站发出去了，记录一下。

站点： https://rumpelstiltskinaivideo.app

## 它是干嘛的

10 月初 TikTok 和 X 上火了一个 AI 生成的片段：一个像 80 年代奇幻电影里的小矮人（ Rumpelstiltskin ），在堆满稻草的谷仓里，配着 Riff Raff 的 "Tip Toe Wing In My Jawwdinz" 踮脚跳舞。很多人想把自己放进这个片段里。

这个站做的就是这件事：上传一张照片，生成一段由你来跳舞的同款视频。

- 输入：1 张单人照片，不用写提示词
- 输出：约 11 秒、720p ，可选 16:9 （和原片同构图）或 9:16 （适合 TikTok/Reels ）
- 文件：带原片配乐的 MP4 + 无声 GIF ，无水印
- 耗时：4 ～ 7 分钟，关掉页面也会继续生成

## 技术栈

- 前端/全栈：TanStack Start
- 部署：Cloudflare Workers + D1 + R2 ，Cron Trigger 补查超时任务
- 生成流程：Nano Banana 2 把照片转成彩铅风参考图 → 火山方舟 Seedance 2.0 mini 参考视频模式逐镜头重演原片 → 服务端用 Mediabunny 合入原片配乐 → 存 R2
- 支付：Waffo Pancake （ Merchant of Record ）

## 定价和成本

不做免费试用，单条 $4.99 ，3 条 $11.99 ，10 条 $29.99 ，一次性付费，不订阅，生成失败自动退积分。

没给免费额度，是因为每条都实打实烧 GPU ，新站扛不住白嫖流量。这个决定对不对，欢迎拍砖。

## 踩过的坑

1. **照片太小直接被模型拒**：用户传了 260×626 的图，接口报 "invalid file"。后来在浏览器端先规整照片：短边小于 720 放大，长边超过 2048 缩小，极端长宽比补模糊边。
2. **用户关页面导致任务卡死**：提交模型后、写回任务 ID 前，请求被中断。改成 Workers 的 `waitUntil` 跑完后续步骤，Cron 兜底超时退款。
3. **PayPal 在日本一直登不上开发者后台**：最后换成 Waffo ，自己按文档手写 RSA 签名和 webhook 验签。
4. **Cloudflare 部署报 "compatibility date in the future"**：nitro 用本机日期写兼容日期，北京时间凌晨 Cloudflare 那边还是前一天。加 `TZ=UTC` 解决。
5. **Workers Builds 推送后一直"已加入队列"**：最后改成本地 wrangler 部署。

## 关于 GEO

这次也在实践让 ChatGPT 这类 AI 搜索能收录、推荐我的站：写 llms.txt ，每个问题做一个答案页（第一句直接给答案、数字写死），加 FAQ/Article Schema ，接 IndexNow 和 Bing Webmaster 。效果怎么样还在观察，有结果了再来更新。

## 求反馈

第一次独立上线，产品、定价、落地页、SEO 有什么问题都欢迎直说。也想听听大家做"热点梗站"的经验：热度一般能撑多久，热度过了之后怎么办？

## 关联链接

- https://rumpelstiltskinaivideo.app

## 导航

- 项目页：[[10-项目/rumpelstiltskinaivideo.app_838a01cf]]
- 渠道页：[[50-渠道/v2ex]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
