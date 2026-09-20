---
type: "corpus"
item_id: "d4387e51269a0c3d"
title: "Show HN: AgentPostage – Send physical mail with agents"
source: "hn_show"
source_name: "HN Show HN"
url: "https://news.ycombinator.com/item?id=49754184"
project_url: "https://agentpostage.com/"
author: "luca-ctx"
published_at: "2026-09-18T13:34:00Z"
captured_at: "2026-09-20T09:36:40+08:00"
lang: "en"
kind: "post"
topic: "AI 工具/Agent"
shard: "2026-09-20"
pub_day: "2026-09-18"
tags:
  - 语料
  - hn_show
  - author_luca-ctx
  - story_49754184
  - show_hn
metrics: {"points": 2, "comments": 0, "engagement_velocity": 2}
comments_count: 0
comments_total: 0
discovered_via: "hn:show_hn:90d"
---

# Show HN: AgentPostage – Send physical mail with agents

> [!info] 一句话导读
> Let your agent send physical mail. — AgentPostage

> [!meta]- 语料信息（点开展开）
> 来源：HN Show HN（post）
> 原帖：<https://news.ycombinator.com/item?id=49754184>
> 指标：点赞=2 · 评论=0 · engagement_velocity=2
> 作者：luca-ctx　|　发布：2026-09-18T13:34:00Z
> 项目链接：<https://agentpostage.com/>
> 采集：2026-09-20T09:36:40+08:00　|　id：`d4387e51269a0c3d`

## 正文

Let your agent send physical mail. — AgentPostage

# Let your agent send physical mail.

Dispute a charge. Cancel the gym. Write to the credit bureau. Your agent sends the PDF. We print it, put it in an envelope, and mail it.

First-Class from $4+ 30¢ per extra PDF page · Printing and postage included Minimum account funding: $10

US mail · MCP, CLI & API · No subscription

Works with OpenClaw Hermes Codex Claude Code Cursor ChatGPT and your agent

A task for your agent

“Mail my gym cancellation.”

 cancellation.pdf

Personal correspondence 01

Membership cancellation

Please cancel my membership at the end of the current billing period and confirm in writing.

Thank you.

AgentPostage · US mail

Membership Services

One PDF. A real letter in the mail.

## Know the price. Then post it.

First-Class

$4

Certified

$12

Certified + return receipt

$15

For the first PDF page in black ink. 30¢ per extra page. Printing, an envelope, the address coversheet and US postage are included.

Color adds 30¢ per PDF page. Single-sided or double-sided, the page rate stays the same. No weight surcharges.

Fund your account from $10. No subscription. Automatic recharge is optional.

Paper and reply envelopes

Paper

White Canary yellow Light blue Light green Orange Light red Ivory Perforated tear-off Statement paper Blue check stock Burgundy check stock Green check stock Four-up coupon paper

Include a reply envelope

None#9 right window#9 left window 6¾ reply envelope 12 reply envelopes

Other paper stocks add 10¢ per document sheet. A reply envelope adds 50¢, or $1.50 for twelve. Reply envelopes are unstamped. Specialty stocks need a correctly laid-out PDF.

Printed and posted

$4.60

3 PDF pages, First-Class.

Count your PDF pages only. The address coversheet is included. Your agent can check the price before sending.

The rates above work without JavaScript. Enable JavaScript to calculate another letter.

### Dispute a charge.

Mail your dispute letter with statements, receipts and supporting pages in the same PDF.

### Cancel the gym.

Send the written cancellation they ask for, without finding a printer or buying stamps.

### Write to a credit bureau.

Send a credit-report dispute, correction request or the documents needed to support it.

### Send in your paperwork.

Mail completed claim forms, supporting documents or a written appeal.

### Put a request in writing.

Send your landlord a repair request, a notice or a copy of the agreement you need on record.

### Ask for the documents.

Mail a signed records request or an account letter to the office that needs it.

Pick your agent. Add postage.

## Your agent. Now with mail.

Get an API key, add funds, then choose your agent.

Save the key as `AGENTPOSTAGE_API_KEY` in your agent’s environment. For ChatGPT, enter it in the GPT’s Actions settings.

Building your own? MCP · CLI · API

OpenClaw Skill

Run in a terminal on the machine where OpenClaw runs.

```
skill_dir="$HOME/.openclaw/skills/agentpostage"
mkdir -p "$skill_dir" &&
curl -fsS \
  https://agentpostage.com/skills/agentpostage/SKILL.md \
  -o "$skill_dir/SKILL.md"
```

Start a new agent session. Key setup and first send.

Hermes Skill

Run in a terminal on the machine where Hermes runs.

```
skill_dir="$HOME/.hermes/skills/agentpostage"
mkdir -p "$skill_dir" &&
curl -fsS \
  https://agentpostage.com/skills/agentpostage/SKILL.md \
  -o "$skill_dir/SKILL.md"
```

Start a new agent session. Key setup and first send.

Codex MCP

With the key in your environment, run:

```
codex mcp add agentpostage \
  --url https://agentpostage.com/mcp \
  --bearer-token-env-var AGENTPOSTAGE_API_KEY
```

Start a new session and ask for your AgentPostage balance. Setup details.

Claude Code MCP

With the key in your environment, run:

```
claude mcp add --scope user --transport http agentpostage \
  https://agentpostage.com/mcp \
  --header 'Authorization: Bearer ${AGENTPOSTAGE_API_KEY}'
```

Start a new session and check the server with `/mcp`. Setup details.

Cursor MCP

Add this server to `.cursor/mcp.json` in your project. Keep any existing servers.

```
{
  "mcpServers": {
    "agentpostage": {
      "url": "https://agentpostage.com/mcp",
      "headers": {
        "Authorization": "Bearer ${env:AGENTPOSTAGE_API_KEY}"
      }
    }
  }
}
```

Restart Cursor with the key in its environment. Setup details.

ChatGPT GPT Actions

Requires a ChatGPT plan and workspace that allow creating GPTs with Actions. In a private custom GPT, add an Action and import this schema:

```
https://agentpostage.com/chatgpt-actions.json
```

Choose API Key authentication with Bearer, then enter your AgentPostage key. Upload a PDF and ask the GPT to mail it.

Keep the GPT set to Only me. Anyone who can use it can spend your mail balance. Complete setup.

Another agent? Use the mail skill with a shell, or connect through MCP or the API.

### First-Class

Letters, forms and supporting documents, mailed through USPS. Your agent can see confirmed mailing. Individual delivery tracking is not included.

From $4 · Up to 500 PDF pages · US addresses

### Certified Mail

USPS tracking and delivery status from $12. Choose Certified + return receipt from $15 to retrieve the receipt PDF when it becomes available.

Up to 150 PDF pages · US addresses

For deadline-sensitive or formal notices, check the recipient’s mailing requirements before sending.

## A few details.

Something else on your mind?

Does AgentPostage write the letter?

Your agent writes or prepares the document. AgentPostage takes the PDF and handles printing, enveloping and mailing. Scans, completed forms and multi-page documents work too. See the PDF requirements.

What do I need to connect my agent?

Create an account, verify your email with the code we send, add funds and create an API key. Install a skill or connect through MCP, CLI or API. After that, your agent can send mail and check status without you opening the site for each letter.

Can I print in color or on both sides?

Yes. Choose black-and-white or full color, single-sided or double-sided. The default is black-and-white on one side of white US letter paper. Paper colors, specialty stocks and reply envelopes are also available. Source PDFs can be up to 10 MiB. See the print options and PDF requirements.

Can my agent check the price before sending?

Yes. It can ask for an exact price using the PDF page count and print options, without sending a letter or spending funds. Sending queues the letter at that rate for automatic printing and mailing. There is no separate approval step. Manage any approvals and spending limits in your own agent.

Whose return address is on the envelope?

The sender name and US return address you provide. We add an address coversheet, so your PDF does not need an envelope window template. The coversheet is included in the price.

Can my agent check delivery?

First-Class reports confirmed mailing, without individual delivery confirmation. Certified Mail adds tracking and delivery status. The return-receipt option also provides a downloadable receipt when available. Mailing and delivery are separate events, and a delivery date is not guaranteed.

How soon will it arrive?

Printing and mailing happen after your request is submitted. Your agent can check when the letter has been mailed. First-Class typically takes about 3–7 business days after USPS accepts it, not from the moment you send the request. Certified delivery may take longer if the recipient is unavailable. We do not promise a dispatch or arrival date. Allow extra time for deadlines.

Can I cancel a letter?

Your agent can cancel while the letter is queued or waiting for funds. The window closes when we start releasing it to the printer, shown as `authorizing`. This can happen soon after sending. Only a successful cancellation response confirms it. After that, the letter cannot be recalled through AgentPostage.

What happens to my PDF and addresses?

They are shared with our printing and mailing provider to fulfil the letter. We keep our copies for 30 days after confirmed First-Class mailing, Certified delivery, cancellation or rejection. Pending letters are kept until resolved. The printing provider has its own retention policy. Read the Privacy Policy for details.

What if I stop using it or a letter fails?

You can revoke your agent’s key and turn off automatic recharge at any time. Request a refund of unused, unreserved funds when closing your account. A letter rejected before mailing authorization is not charged. Delayed, returned or undelivered mail is not automatically refundable. See the refund terms.

Your agent has a letter to send.

## Let’s get it in the mail.

Physical mail for personal agents.

# talos-kernel/Talos

## 关联链接

- https://agentpostage.com/chatgpt-actions.json
- https://agentpostage.com/mcp
- https://agentpostage.com/skills/agentpostage/SKILL.md

## 导航

- 项目页：[[10-项目/agentpostage.com_270d1370]]
- 渠道页：[[50-渠道/hn_show]]
- 赛道：`AI 工具/Agent`（见 [[浏览]] 的「按赛道」视图）
- 同渠道/同赛道批量浏览：[[浏览]]
