---
type: "corpus"
item_id: "89e19d09c3d499f7"
title: "Show HN: Aggregate Finance, your financial data in a spreadsheet you own"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=50371992"
project_url: "https://app.aggregatefi.com/"
author: "mitchthebaker"
published_at: "2026-11-04T21:45:08Z"
captured_at: "2026-11-05T11:21:45+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-11-05"
pub_day: "2026-11-04"
tags:
  - 语料
  - hn_show
  - author_mitchthebaker
  - story_50371992
  - show_hn
metrics: {"points": 2, "comments": 2, "engagement_velocity": 2}
comments_count: 2
comments_total: 2
discovered_via: "hn:show_hn:3d"
---

# Show HN: Aggregate Finance, your financial data in a spreadsheet you own

> [!info] 一句话导读
> I started building Aggregate Finance a couple of years ago because I was manually updating a Google Sheet to track my credit card statements, monthly recurring …

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=50371992>
> 指标：点赞=2 · 评论=2 · engagement_velocity=2
> 作者：mitchthebaker　|　发布：2026-11-04T21:45:08Z
> 项目链接：<https://app.aggregatefi.com/>
> 采集：2026-11-05T11:21:45+08:00　|　id：`89e19d09c3d499f7`

## 正文

I started building Aggregate Finance a couple of years ago because I was manually updating a Google Sheet to track my credit card statements, monthly recurring transactions, and spending habits. This seemed perfect for automation as I was having to log in to six separate banking apps to pull this information together.My original intention was to use this tool locally, but I figured it would be an excellent learning opportunity to understand how to scale the application for others to use. The core functionality of Aggregate Finance revolves around syncing banks and brokerages through Plaid to create visuals and data analytics in Google Sheets and OneDrive/Excel, but I've also added Stripe for payments, passkey and TOTP support for MFA (wanted to better learn how WebAuthn works, mostly), and Resend for emailing account updates.The first question you're likely thinking is: isn't this just reinventing the wheel? There's plenty of other personal finance/budgeting apps out there like Rocket Money, Monarch, Copilot Money, YNAB, Tiller, Credit Karma, etc. I personally tried Rocket Money but it left a bad taste in my mouth how my entire financial history was stored on their servers without having direct ownership of the data. Another pain point with these personal finance apps is you're locked into their subscription and lose access to your financial data if you cancel.That's why I opted for the Google Sheet and OneDrive/Excel approach since this persists financial data over time and provides direct data ownership. There's a fair argument that these options still share your financial data with Google or Microsoft, so I built a way to download your financial data locally via CSV/Excel/LibreOffice exports.In terms of data encryption, Aggregate Finance encrypts financial data before it reaches MongoDB: balances, transactions, merchants, statements, holdings, and any user customizations. Each user gets their own AES-256 key rather than a shared key. The reason I went with this approach is for data deletion: when someone deletes their account, their encryption key is deleted as well, so any financial data stored in prior database backups can't be decrypted.I've been using Aggregate Finance with my own live bank accounts and investment holdings, and it's already been helpful. I can see when my credit card statements are due, monitor my entire investment portfolio, keep track of recurring charges, create budgets, and see how my spending pans out over a given month or over the past year. I'm curious whether it's useful for anyone else, and I'd of course welcome any feedback on how I can improve it. You can try it with a free sample spreadsheet that contains a year of example data with no bank connection required at https://app.aggregatefi.com.

## 评论（2/2）

> **dieselgate** · 2026-11-04T22:57:57.000Z　
> Thanks for sharing, looks polished on mobile.
> Is it “agent-ready” in any capacity?

---

> **mitchthebaker** · 2026-11-05T03:09:50.000Z　
> I haven't explored any AI or agent-specific features yet but that's a good flag, thanks. Based on some initial research, it's possible to create a read-only MCP server using OAuth to sign in to Aggregate Finance securely from Claude, ChatGPT, or any other MCP client. The client would then get a short-lived token scoped to your financial data. In the meantime, you could import the Google Sheet and/or CSV/Excel downloads into an LLM and work with the data that way.

## 关联链接

- https://app.aggregatefi.com.

## 导航

- 项目页：[[10-项目/app.aggregatefi.com_c0be1bf6]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
