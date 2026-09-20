---
type: "corpus"
item_id: "69f1f2c14295f4ab"
title: "Show HN: Filedge – parse SEC filings for $0.05 via x402, no keys"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=47942430"
project_url: "https://filedge.io/"
author: "arvindravi"
published_at: "2026-04-28T23:52:37Z"
captured_at: "2026-09-21T02:52:41+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-21"
pub_day: "2026-04-28"
tags:
  - 语料
  - hn_show
  - author_arvindravi
  - story_47942430
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:174d"
---

# Show HN: Filedge – parse SEC filings for $0.05 via x402, no keys

> [!info] 一句话导读
> Make your first call →

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=47942430>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：arvindravi　|　发布：2026-04-28T23:52:37Z
> 项目链接：<https://filedge.io/>
> 采集：2026-09-21T02:52:41+08:00　|　id：`69f1f2c14295f4ab`

## 正文

filedge
How it works
 API
 Pricing
 Foundations
 Docs
Make your first call →
How it works
 API
 Pricing
 Foundations
 Docs
 Make your first call →
Financial document intelligence
 SEC filings.
Earnings calls.
 Structured, instantly.
A single endpoint. Five cents a call. No keys, no accounts, no ceremony. Built for the agents already reading your filings.
Make your first call →
 Read the docs
API online · 184 ms p50
 x402 v2 · Base
 FinBERT NLP
POST · /v1/parse
// one call. one nickel.
POST https://filedge.io/v1/parse
{
"source" : "edgar" ,
"type" : "10-Q" ,
"ticker" : "AAPL" ,
"period" : "latest"
}
 → typed JSON · ~200ms
200 OK · application/json
 184ms
AAPL 10-Q parsed · 184ms
 NVDA earnings transcript · 212ms
 MSFT Form 4 · 98ms
 TSLA 8-K · 156ms
 META 10-K · 240ms
 GOOGL 10-Q · 176ms
 AMZN transcript · 198ms
 JPM 10-Q · 162ms
AAPL 10-Q parsed · 184ms
 NVDA earnings transcript · 212ms
 MSFT Form 4 · 98ms
 TSLA 8-K · 156ms
 META 10-K · 240ms
 GOOGL 10-Q · 176ms
 AMZN transcript · 198ms
 JPM 10-Q · 162ms
How it works
 Three steps.
 No ceremony.
Send a request. Pay a nickel. Get typed JSON. The x402 protocol handles the payment inline — your agent never sees an invoice.
01
Send a request.
POST to /v1/parse with a ticker, a document type, and a period. No API key. No auth header. Nothing to sign up for.
POST /v1/parse
{ ticker: "NVDA", type: "10-Q" }
02
Pay five cents.
The API responds with HTTP 402 and payment instructions. Your x402 client pays $0.05 in USDC on Base. No wallet code. No billing portal.
x402 v2 · Base
NETWORK Base · eip155:84532
ASSET USDC
AMOUNT $0.05
STATUS ✓ settled · 1.2s
03
Get the JSON.
Typed fields, every time. Monetary values as integers in USD cents. ISO 8601 dates. Enums with fixed vocabularies. Cached on repeat — you're never billed twice.
typed · cached · deterministic
{ "ticker" : "NVDA" ,
"revenue" : { "value" : 60923000000 },
"eps_diluted" : 2.40 ,
"signal" : "raised" }
Built for agents
 The chain is the receipt.
No monthly minimums. No seat counts. No "contact sales." Your agent pays as it goes — five cents at a time — and the ledger writes itself.
API reference
 One endpoint.
 Everything you need.
POST /v1/parse accepts SEC EDGAR filings by ticker and earnings call transcripts. Typed JSON, every time.
POST
 https://filedge.io/v1/parse
source
 string req
 edgar · transcript · url
type
 string req
 10-Q · 10-K · 8-K · form4
ticker
 string req
 e.g. AAPL
period
 string opt
 latest · YYYY-QN · YYYY
url
 string opt
 direct filing URL
response.json
 curl
 python
 node
copy
// GET /v1/parse · 10-Q · AAPL
{
 "meta" : {
 "ticker" : "AAPL" ,
 "company" : "Apple Inc." ,
 "document_type" : "10-Q" ,
 "period_end" : "2024-12-28" ,
 "filed_date" : "2025-02-07" ,
 "parsed_at" : "2025-04-22T18:04:11Z" ,
 "cache_hit" : false
 },
 "financials" : {
 "revenue" : { "value" : 124307000000 , "yoy_pct" : 4.1 },
 "net_income" : { "value" : 36206000000 , "yoy_pct" : 7.9 },
 "eps_diluted" : { "value" : 2.40 , "yoy_pct" : 10.1 },
 "gross_margin_pct" : 46.9
 },
 "segments" : [
 { "name" : "iPhone" , "revenue" : 69245000000 , "yoy_pct" : 1.1 },
 { "name" : "Services" , "revenue" : 26249000000 , "yoy_pct" : 13.9 },
 { "name" : "Mac" , "revenue" : 8970000000 , "yoy_pct" : 15.6 }
 ],
 "guidance" : {
 "provided" : true ,
 "revenue_range" : { "low" : 88500000000 , "high" : 91500000000 },
 "signal" : "raised"
 },
 "risk_flags" : [
 { "text" : "China revenue concentration risk" , "severity" : "high" },
 { "text" : "FX headwinds on international margins" , "severity" : "medium" }
 ]
}
 # Your x402 client handles the 402 + retry automatically.
curl -X POST https://filedge.io/v1/parse \
 -H "Content-Type: application/json" \
 -d '{
 "source": "edgar",
 "type": "10-Q",
 "ticker": "AAPL",
 "period": "latest"
 }'
# → HTTP 402 Payment Required
 # → x402 client pays $0.05 USDC on Base
 # → HTTP 200 OK, typed JSON returned
 from x402 import Client
client = Client() # reads wallet from env
res = client.post(
 "https://filedge.io/v1/parse" ,
 json={
 "source" : "edgar" ,
 "type" : "10-Q" ,
 "ticker" : "AAPL" ,
 },
)
print (res.json()[ "financials" ][ "revenue" ][ "value" ])
 # → 124307000000
 import { fetch } from "x402-fetch" ;
const res = await fetch( "https://filedge.io/v1/parse" , {
 method: "POST" ,
 body: JSON .stringify({
 source: "edgar" ,
 type : "10-Q" ,
 ticker: "AAPL" ,
 }),
});
const data = await res.json();
console.log(data.financials.revenue.value);
 // → 124307000000
10-Q
 Quarterly
Revenue, EPS, segments
10-K
 Annual
Full-year, MD&A, risk
8-K
 Material
Events & disclosures
Form 4
 Insider
Buys, sells, signal
Call
 Transcript
Tone, topics, Q&A
Pricing
 Five cents
a request.
 That's it.
No monthly fees. No tiered rate limits. No account. Each call costs exactly a nickel, paid in USDC on Base. Pay as you go — your agent already knows how.
Make your first call →
 View x402 docs
Per request
$
 0.05
 / call · USDC
Network Base · 84532
Asset USDC
Protocol x402 v2
Min balance $0.05
Billing per request
Rate limits none
Account not required
Cached hits free
Built on solid ground
 Primary sources.
 No magic.
Structured extraction from the source. NLP signals layered on top. No hallucinations, no re-licensed data, no vendor in the middle.
Straight from EDGAR
10-Q, 10-K, 8-K, and Form 4 data comes directly from the SEC's XBRL feed. Primary source. No third-party data vendors, no re-licensing risk.
FinBERT for sentiment
Transcript tone and risk flag scoring uses FinBERT — a financial-domain BERT model trained on financial text. Not a general model retrofitted for finance.
x402, not proprietary
Payment uses the open x402 standard. Your client works with any x402 service — not just filedge. No vendor lock-in on the payment layer.
Cached, not re-billed
Parsed documents live in Redis. TTLs vary by document type — shorter for 8-K, longer for 10-K. Request the same filing twice, pay once.
JSON agents actually use
Monetary values are integers in USD cents — no floating-point currency. Dates are ISO 8601. Enums are fixed strings. Every field typed, every time.
Discoverable by design
Serves /.well-known/x402.json for service discovery and /llms.txt for agent instructions. Find it, understand it, use it — zero setup.
Ready when you are
 From 200 pages
to 200 milliseconds.
Make your first call →
 Read the docs
No credit card · No signup · POST /v1/parse and go.
filedge
Financial document intelligence for agents. Pay-per-request, typed JSON, primary sources. Built on Base.
API ONLINE
 v2.1.0
Product
API reference
 Pricing
 Foundations
Developers
llms.txt
 x402.json
Protocol
x402 v2
 Base Network
 USDC
 EDGAR
© 2026 filedge.io · Built on Base · Powered by EDGAR
 Not investment advice. Data from SEC filings, as filed.

## 关联链接

- https://filedge.io/v1/parse

## 导航

- 项目页：[[10-项目/filedge.io_2d97b4cf]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
