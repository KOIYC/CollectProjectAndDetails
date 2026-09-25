---
type: "project"
title: "Show HN: CubeLV – AI that designs your automation before building it"
project_url: "https://app.cubelv.com/"
first_seen: "2026-09-25T13:54:35+08:00"
sources:
  - hn_show
tags:
  - 项目
  - hn_show
  - author_qqrun
  - story_49827478
  - show_hn
lang: "en"
---

# Show HN: CubeLV – AI that designs your automation before building it

> [!info] 一句话导读
> // 公開分享頁 origin 轉址：未登入者一律去公開頁 origin 看。

> [!meta]- 项目信息（点开展开）
> 项目链接：<https://app.cubelv.com/>
> 首次收录：2026-09-25T13:54:35+08:00
> 来源渠道：HN Show HN
> 标签：author_qqrun, story_49827478, show_hn
> 最新指标：点赞=4 · 评论=1 · engagement_velocity=4

## 观测历史

| 采集时间 | 渠道 | 指标 | 语料 |
|---|---|---|---|
| 2026-09-24T23:57:22+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-24/4ef5350f30aa6080_Show-HN-CubeLV-–-AI-that-designs-your-automation-b]] |
| 2026-09-25T13:54:35+08:00 | HN Show HN | 点赞=4 · 评论=1 · engagement_velocity=4 | [[20-语料/posts/hn_show/2026-09-24/4ef5350f30aa6080_Show-HN-CubeLV-–-AI-that-designs-your-automation-b]] |

## 摘要正文

AStockTeam   // 公開分享頁 origin 轉址：未登入者一律去公開頁 origin 看。  //  // 分享連結一律產生 app origin（已登入者點開直接開啟，不必多按登入），未登入者才轉走。  // 登入態只存在 localStorage，CloudFront / Lambda@Edge 讀不到，所以這個判斷只能在  // 瀏覽器做 —— 也因此爬蟲（不跑 JS）永遠停在 app origin，兩邊的 /share/ 都要掛 share-ogp。  //  // 擺在 head 最前面、bundle 下載之前：匿名訪客是分享連結的大宗，讓他們先拉完整份 SPA  // 再轉走等於每次點擊都白下載一次。  // 兩個 origin 相同時（dev）整段不動作；Electron / Capacitor 的 origin 也對不上，自動略過。  (function () {  var appOrigin = 'https://astockteam.ai';  var publicOrigin = 'https://astockteam.com';  if (publicOrigin === appOrigin) return;  if (location.origin !== appOrigin) return;  if (!/^\/share\/[a-f0-9]{24}/.test(location.pathname)) return;  try {  if (localStorage.getItem('isLoggedIn') === 'true') return;  } catch (e) { /* localStorage 不可用（隱私模式）→ 當作未登入 */ }  location.replace(publicOrigin + location.pathname + location.search + location.hash);  })();   @layer theme, base, components, utilities;   // Android Capacitor 8 SystemBars：原生只在 DOMContentLoaded 才呼叫 onDOMReady（native-bridge.js），  // 那刻 WebView 才從「padded 避開 system bar（innerHeight 矮）」切成「edge-to-edge passthrough（innerHeight 全高）」，  // 造成啟動 ~700ms 整個 viewport 高度跳變、畫面被往上頂一下。  // 這裡在第一幀就提早呼叫，meta viewport（viewport-fit=cover）已在 DOM，原生立即檢測到 co…
