---
type: "project"
title: "第一个独立上线的 Web 站：用 3 天做了个 Rumpelstiltskin 踮脚舞 AI 视频生成器，记录一下踩过的坑"
project_url: "https://rumpelstiltskinaivideo.app/"
first_seen: "2026-10-16T09:38:51+08:00"
sources:
  - v2ex
tags:
  - 项目
  - v2ex
  - 17
lang: "zh"
---

# 第一个独立上线的 Web 站：用 3 天做了个 Rumpelstiltskin 踮脚舞 AI 视频生成器，记录一下踩过的坑

> [!info] 一句话导读
> 做了很多年数据和产品，一直想自己从零上线一个能收钱的站。这次赶上一个梗，终于把第一个站发出去了，记录一下。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://rumpelstiltskinaivideo.app/>
> 首次收录：2026-10-16T09:38:51+08:00
> 来源渠道：V2EX
> 标签：17
> 最新指标：回复=0

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-10-16T09:38:51+08:00 | V2EX | 回复=0 | [[20-语料/posts/v2ex/2026-10-16/772c525264a80746_第一个独立上线的-Web-站-用-3-天做了个-Rumpelstiltskin-踮脚舞-AI-视频生]] |

## 摘要正文

做了很多年数据和产品，一直想自己从零上线一个能收钱的站。这次赶上一个梗，终于把第一个站发出去了，记录一下。  站点： https://rumpelstiltskinaivideo.app  ## 它是干嘛的  10 月初 TikTok 和 X 上火了一个 AI 生成的片段：一个像 80 年代奇幻电影里的小矮人（ Rumpelstiltskin ），在堆满稻草的谷仓里，配着 Riff Raff 的 "Tip Toe Wing In My Jawwdinz" 踮脚跳舞。很多人想把自己放进这个片段里。  这个站做的就是这件事：上传一张照片，生成一段由你来跳舞的同款视频。  - 输入：1 张单人照片，不用写提示词 - 输出：约 11 秒、720p ，可选 16:9 （和原片同构图）或 9:16 （适合 TikTok/Reels ） - 文件：带原片配乐的 MP4 + 无声 GIF ，无水印 - 耗时：4 ～ 7 分钟，关掉页面也会继续生成  ## 技术栈  - 前端/全栈：TanStack Start - 部署：Cloudflare Workers + D1 + R2 ，Cron Trigger 补查超时任务 - 生成流程：Nano Banana 2 把照片转成彩铅风参考图 → 火山方舟 Seedance 2.0 mini 参考视频模式逐镜头重演原片 → 服务端用 Mediabunny 合入原片配乐 → 存 R2 - 支付：Waffo Pancake （ Merchant of Record ）  ## 定价和成本  不做免费试用，单条 $4.99 ，3 条 $11.99 ，10 条 $29.99 ，一次性付费，不订阅，生成失败自动退积分。  没给免费额度，是因为每条都实打实烧 GPU ，新站扛不住白嫖流量。这个决定对不对，欢迎拍砖。  ## 踩过的坑  1. **照片太小直接被模型拒**：用户传了 260×626 的图，接口报 "invalid file"。后来在浏览器端先规整照片：短边小于 720 放大，长边超过 2048 缩小，极端长宽比补模糊边。 2. **用户关页面导致任务卡死**：提交模型后、写回任务 ID 前，请求被中断。改成 Workers 的 `waitUntil` 跑完后续步骤，Cron 兜底超时退款。 3. **PayPal 在日本一直登不上开发者后台**：最后换成 Waffo ，自己按文档手写 RSA 签名和 webhook 验签。 4. **Cloudflare 部署报 "compatibility date in the future"**：nitro 用本机日期写兼容日期，北京时间凌晨 Cloudflare 那边还是前一天。加 `TZ=UTC` 解决。 5. **Wor…
