---
type: "corpus"
item_id: "00f2977a2e4b2d0e"
title: "Show HN: High-performance, zero-dependency charting engine for Svelte"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49867443"
project_url: "https://bonguynvan.github.io/tradecanvas"
author: "bonguynvan"
published_at: "2026-09-27T15:22:52Z"
captured_at: "2026-09-28T09:47:28+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-28"
pub_day: "2026-09-27"
tags:
  - 语料
  - hn_show
  - author_bonguynvan
  - story_49867443
  - show_hn
metrics: {"points": 5, "comments": 0, "engagement_velocity": 5}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:3d"
---

# Show HN: High-performance, zero-dependency charting engine for Svelte

> [!info] 一句话导读
> TradeCanvas Docs Examples Playground Changelog

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49867443>
> 指标：点赞=5 · 评论=0 · engagement_velocity=5
> 作者：bonguynvan　|　发布：2026-09-27T15:22:52Z
> 项目链接：<https://bonguynvan.github.io/tradecanvas>
> 采集：2026-09-28T09:47:28+08:00　|　id：`00f2977a2e4b2d0e`

## 正文

TradeCanvas Docs Examples Playground Changelog
 ☾ ★ ☰
 Docs Examples Playground Changelog
GitHub npm
 v0.14 · 66 indicators The trading chart that ships with its UI.
 A high-performance, zero-dependency canvas charting engine with a built-in
 TradingView-grade interface. Indicators, drawing tools, real-time
 streaming, replay, and a backtester — in one ChartWidget call.
 npm pnpm yarn
 npm install @tradecanvas/chart COPY
 Get started GitHub
 66 Indicators
 24 Drawing tools
 17 Chart types
 0 Dependencies
BTC ETH SOL BNB
 1m 5m 15m 1h 4h 1d
 Candles Heikin-Ashi Area Bars Baseline
Connecting to Binance…
Drag to pan Scroll to zoom Drag axes to scale Hover for crosshair
Interactive · no screenshots Every chart type, live in the page
 Each tile is a real Chart instance, not an image. Drag to pan,
 scroll to zoom, hover for the crosshair — every one responds independently.
Candlestick OHLC
 Heikin-Ashi Trend
 Area Close
 Baseline Above / below
 OHLC Bars Classic
 Step Line Discrete
Built for trading
 Everything you need for a professional trading chart, in a single package.
 /\
 66 technical indicators
 SMA, EMA, RSI, MACD, Bollinger, Ichimoku, Stochastic RSI, Supertrend,
 Anchored VWAP, plus a deep oscillator bench (PPO, RMI, Disparity, Qstick,
 PGO, and more) — all computed internally with zero external math libraries.
//
 24 drawing tools
 Trendlines, Fibonacci (incl. Time Zones), channels, Elliott waves, Gann tools.
 Click-to-place with magnet snapping, undo/redo, and full serialization.
[/]
 17 chart types
 Candlestick, OHLC bars, line, area, baseline, hollow candles, Heikin-Ashi,
 Renko, Kagi, Line Break, Point & Figure, Range Bars, Volume Candles,
 Equivolume, HLC Area, Step Line, and Line+Markers.
▦
 ChartWidget (built-in UI)
 One-line embed — new ChartWidget(host, {...}) ships a full
 TradingView-like UI: toolbar, drawing sidebar, settings dialog, status bar.
 Framework-agnostic.
$
 Trading overlay
 Render positions, orders, SL/TP markers directly on the chart. Drag to modify.
 Partial-close strips, multi-stop P&L gradient, custom label templates.
~
 Real-time streaming
 Built-in Binance WebSocket adapter with typed REST + WS validators. Or plug in
 your own data source with the simple DataAdapter interface.
 Auto-reconnect included.
⚙
 Web Worker pipeline
 Indicator math runs off the render loop via IndicatorWorkerHost —
 Promise-based calculate() , sync fallback for SSR/tests,
 per-request timeout. No frozen frames.
⊕
 Backtester + Monte Carlo
 Bar-by-bar Backtester with virtual fills, slippage / commission models,
 plus a 4-strategy reference library. runMonteCarlo() exposes
 path-dependence with P5/P95 equity bands and probability-of-profit.
⤴
 TradingView gestures
 Drag the price/time axes to scale, double-click to reset, Shift +drag for
 a measure ruler, Alt +click to pin a tooltip, hover for axis pill labels
 that follow the cursor. The set of moves a serious trader expects.
Finance Charts
 Beyond candlesticks — visualize portfolios, order books, market sectors, and KPI metrics.
 BTC $65,234
+2.4%
ETH $3,412
-1.2%
SOL $148.00
+5.1%
BNB $582.00
+0.8%
ADA $0.4500
-3.2%
DOT $7.23
+1.6%
Portfolio Performance
Order Book Depth
Crypto Market Heatmap
P&L Attribution
Fear & Greed Index
Quick start
 A full-featured trading chart with live data in one call. Drop-in ChartWidget — no framework needed.
 import { ChartWidget } from '@tradecanvas/chart/widget'
import { BinanceAdapter } from '@tradecanvas/chart'
const widget = new ChartWidget(document.getElementById('chart')!, {
 symbol: 'BTCUSDT',
 timeframe: '5m',
 theme: 'dark',
 adapter: new BinanceAdapter(),
 historyLimit: 500,
 trading: true,
 onReady: (chart) => {
 chart.on('orderPlace', (e) => console.log('order intent', e.payload))
 },
}) Read the docs See examples
 GitHub · Docs · Changelog · npm · bo-grid
 MIT · v1.0.0

## 导航

- 项目页：[[10-项目/bonguynvan.github.io_4cab560e]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
